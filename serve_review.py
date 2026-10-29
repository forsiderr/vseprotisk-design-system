#!/usr/bin/env python3
"""
Upgates review proxy — first test.

Fetches the real Upgates shop and injects an override stylesheet into the served
HTML, so the user can review pixel-perfect changes BEFORE applying them to Upgates.

Usage:
    python3 serve_review.py [--port PORT] [--bind HOST] [--upstream SHOP_URL]

- --override is the local CSS file served at /__override.css and injected.
- Internal absolute links to the upstream origin are rewritten to the proxy so
  navigation stays inside the review version.
- GET only (review tool). POST/checkout is outside scope for this test.

Requires: Python stdlib only.
"""
from __future__ import annotations

import argparse
import http.server
import re
import socketserver
import urllib.parse
import urllib.request
from pathlib import Path
from http import HTTPStatus

HERE = Path(__file__).resolve().parent
DEFAULT_OVERRIDE = HERE / "override-carbon.css"
INJECT_TAG = '<link rel="stylesheet" href="/__override.css">'


def build_handler(upstream: str, override_path: Path, origin: str):
    upstream = upstream.rstrip("/")
    up_parsed = urllib.parse.urlparse(upstream)
    upstream_netloc = up_parsed.netloc
    scheme = up_parsed.scheme or "https"

    class _Handler(http.server.BaseHTTPRequestHandler):
        server_version = "VSPReviewProxy/0.1"

        # ---- helpers ----
        def _log(self, code, note=""):
            self.log_message('"%s" %s %s', self.path, code, note)

        def _serve_override(self):
            data = override_path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/css; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)
            self._log(200, "(override css)")

        def _fetch(self, path: str) -> tuple[int, dict, bytes]:
            """GET upstream path; return (status, headers, body)."""
            target = f"{scheme}://{upstream_netloc}{path}"
            req = urllib.request.Request(
                target,
                headers={"User-Agent": "Mozilla/5.0 VSPReviewProxy"},
            )
            with urllib.request.urlopen(req, timeout=25) as resp:
                body = resp.read()
                hdrs = {k: v for k, v in resp.getheaders()}
                return resp.status, hdrs, body

        def _inject_and_rewrite(self, html: bytes) -> bytes:
            text = html.decode("utf-8", errors="replace")
            # rewrite internal absolute URLs to proxy origin so nav stays in review
            text = re.sub(
                r'((?:href|src|action)=")(https?://)' + re.escape(upstream_netloc) + r'/',
                r'\1' + origin + r'/',
                text,
            )
            # inject override link before </head>, else prepend to <body>
            if "</head>" in text:
                text = text.replace("</head>", INJECT_TAG + "</head>", 1)
            else:
                text = INJECT_TAG + text
            return text.encode("utf-8")

        # ---- routing ----
        def do_GET(self):  # noqa: N802 (http.server API)
            parsed = urllib.parse.urlparse(self.path)

            if parsed.path == "/__override.css":
                self._serve_override()
                return

            # absolute URL passed straight through? rebuild relative to upstream
            path = self.path
            if parsed.scheme or parsed.netloc:
                path = parsed.path + ("?" + parsed.query if parsed.query else "")

            status, headers, body = self._fetch(path)
            ctype = headers.get("Content-Type", "")
            if "text/html" in ctype:
                body = self._inject_and_rewrite(body)

            self.send_response(status)
            for k in ("Content-Type",):
                if k in headers:
                    self.send_header(k, headers[k])
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
            self._log(status, ctype.split(";")[0])

        def log_message(self, fmt, *args):
            # route to stderr, quiet by default
            pass

    return _Handler


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8124)
    ap.add_argument("--bind", default="0.0.0.0")
    ap.add_argument("--upstream", default="https://vseprotisk.t2.upgates.shop")
    ap.add_argument("--override", default=str(DEFAULT_OVERRIDE))
    ap.add_argument("--origin", default="", help="public origin for link rewriting, e.g. http://130.162.216.100:8124")
    args = ap.parse_args()

    override_path = Path(args.override)
    if not override_path.exists():
        print(f"override css not found: {override_path}", file=__import__("sys").stderr)
        return 1
    origin = f"http://{args.origin or args.bind}:{args.port}"

    Handler = build_handler(args.upstream, override_path, origin)

    class ThreadingTCPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
        allow_reuse_address = True

    with ThreadingTCPServer((args.bind, args.port), Handler) as httpd:
        print(f"review proxy on http://{args.bind}:{args.port}", flush=True)
        print(f"upstream: {args.upstream}", flush=True)
        print(f"override: {override_path}", flush=True)
        print(f"open http://127.0.0.1:{args.port}/  (from this machine) ; "
              f"or http://<public-ip>:{args.port}/  (from elsewhere)", flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
