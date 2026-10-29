#!/usr/bin/env python3
"""
Upgates live-review proxy (auto-update).

Run this on YOUR PC, point your browser at http://127.0.0.1:8124/. It:
  - fetches the real Upgates shop,
  - inlines the current override CSS as a <style> (correct on first paint),
  - auto-updates: a small script re-fetches the override every N seconds and
    swaps the same style node in place — push a change and it appears live,
    no page refresh, no reload loop.

Works on Windows and macOS/Linux. Python 3.8+ stdlib only.

Usage (on your machine):
    python3 serve_review.py            # then open http://127.0.0.1:8124/

Options:
    --port PORT          default 8124
    --bind HOST          default 127.0.0.1
    --upstream URL       default https://vseprotisk.t2.upgates.shop
    --override-url URL   default https://raw.githubusercontent.com/forsiderr/
                              vseprotisk-design-system/main/override-carbon.css
    --poll SECONDS       re-fetch interval (default 3)
"""
from __future__ import annotations

import argparse
import json
import re
import socketserver
import urllib.error
import urllib.parse
import urllib.request
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

DEFAULT_OVERRIDE_URL = (
    "https://raw.githubusercontent.com/forsiderr/"
    "vseprotisk-design-system/main/override-carbon.css"
)

# Auto-update script: re-polls the override and rewrites the same <style> node.
# Never reloads the page; matches by data attribute (no link-href matching).
AUTO_REFRESH_JS = (
    "<script data-vsp-js>\n"
    "(function(){\n"
    "  var ENDPOINT = '/__override.css';\n"
    "  var last = null;\n"
    "  function apply(text){\n"
    "    var el = document.querySelector('style[data-vsp-live]');\n"
    "    if (!el){ el = document.createElement('style'); el.setAttribute('data-vsp-live','1'); document.head.appendChild(el); }\n"
    "    if (el.textContent !== text) el.textContent = text;\n"
    "  }\n"
    "  function poll(){\n"
    "    var x = new XMLHttpRequest();\n"
    "    x.open('GET', ENDPOINT + '?c=' + Date.now(), true);\n"
    "    x.onreadystatechange = function(){\n"
    "      if (x.readyState === 4 && x.status === 200){\n"
    "        var t = x.responseText;\n"
    "        if (t !== last){ last = t; apply(t); }\n"
    "      }\n"
    "    };\n"
    "    x.send();\n"
    "  }\n"
    "  poll();\n"
    "  setInterval(poll, __POLL__ * 1000);\n"
    "})();\n"
    "</script>"
)


def build_handler(upstream: str, override_url: str, origin: str, poll: int):
    upstream = upstream.rstrip("/")
    up = urllib.parse.urlparse(upstream)
    scheme = up.scheme or "https"
    upstream_netloc = up.netloc
    fresh_js = AUTO_REFRESH_JS.replace("__POLL__", str(poll))

    class _Handler(BaseHTTPRequestHandler):
        server_version = "VSPlive/0.3"

        def log_message(self, format, *args):  # quiet by default
            pass

        def _fetch_bytes(self, url: str, timeout: int = 25) -> tuple[int, str, bytes]:
            req = urllib.request.Request(url, headers={"User-Agent": "VSPlive-review"})
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return resp.status, resp.headers.get("Content-Type") or "", resp.read()
            except urllib.error.HTTPError as e:
                return e.code, "text/plain", str(e).encode()
            except Exception as e:  # network hiccup
                return HTTPStatus.BAD_GATEWAY, "text/plain", str(e).encode()

        def _write_raw(self, status, ctype, body):
            self.send_response(status)
            if ctype:
                self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            try:
                self.wfile.write(body)
            except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError):
                pass  # client (browser) closed the connection mid-write — expected on reload

        def do_GET(self):  # noqa: N802
            parsed = urllib.parse.urlparse(self.path)

            if parsed.path == "/__override.css":
                status, ctype, data = self._fetch_bytes(override_url, timeout=20)
                if status == 200:
                    self._write_raw(200, "text/css; charset=utf-8", data)
                else:
                    self._write_raw(HTTPStatus.BAD_GATEWAY, "text/plain",
                                    b"override fetch failed")
                return

            path = self.path
            if parsed.scheme or parsed.netloc:
                path = parsed.path + ("?" + parsed.query if parsed.query else "")

            status, ctype, body = self._fetch_bytes(scheme + "://" + upstream_netloc + path)

            if "text/html" in ctype:
                try:
                    text = body.decode("utf-8", "replace")
                except Exception:
                    text = ""

                # fetch the CURRENT override and inline it as <style data-vsp-live>
                _, _ct, override = self._fetch_bytes(override_url, timeout=20)
                style_inline = (
                    "<style data-vsp-live>" + override.decode("utf-8", "replace") + "</style>"
                )
                inject = style_inline + fresh_js

                # rewrite internal absolute links to the proxy origin
                text = re.sub(
                    r'((?:href|src|action)=")(https?://)' + re.escape(upstream_netloc) + r'/',
                    r"\1" + origin + r"/",
                    text,
                )
                if "</head>" in text:
                    text = text.replace("</head>", inject + "</head>", 1)
                else:
                    text = inject + text
                body = text.encode("utf-8")

            self._write_raw(status, ctype, body)

    return _Handler


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8124)
    ap.add_argument("--bind", default="127.0.0.1")
    ap.add_argument("--upstream", default="https://vseprotisk.t2.upgates.shop")
    ap.add_argument("--override-url", default=DEFAULT_OVERRIDE_URL)
    ap.add_argument("--poll", type=int, default=3)
    args = ap.parse_args()

    origin = f"http://{args.bind}:{args.port}"
    Handler = build_handler(args.upstream, args.override_url, origin, args.poll)

    class Threaded(socketserver.ThreadingMixIn, HTTPServer):
        allow_reuse_address = True

    with Threaded((args.bind, args.port), Handler) as httpd:
        print("=" * 62)
        print("Running locally — open this in your browser:")
        print(f"   http://{args.bind}:{args.port}/")
        print(f"  upstream : {args.upstream}")
        print(f"  override : {args.override_url}")
        print(f"  auto-update every {args.poll}s — when I push, it appears live")
        print("  Ctrl+C to stop")
        print("=" * 62, flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
