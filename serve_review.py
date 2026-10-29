#!/usr/bin/env python3
"""
Upgates live-review proxy (auto-update).

Run this on YOUR PC, point your browser at http://127.0.0.1:8124/. It:
  - fetches the real Upgates shop,
  - injects the current override CSS (pulled live from GitHub, so when the
    developer pushes a change it flows in automatically),
  - AUTO-APPLIES the override without you refreshing: it re-polls the override
    URL every few seconds and swaps the stylesheet in-place when changed.

Usage (on your machine):
    python3 serve_review.py
    # then open http://127.0.0.1:8124/

Options:
    --port PORT          default 8124
    --upstream URL       default https://vseprotisk.t2.upgates.shop
    --override-url URL   default https://raw.githubusercontent.com/forsiderr/
                              vseprotisk-design-system/main/override-carbon.css
    --poll SECONDS       how often to re-fetch the override (default 3)
    --bind HOST          default 127.0.0.1 (only reachable from this machine)

Requires Python 3.8+ standard library only.
"""
from __future__ import annotations

import argparse
import re
import socketserver
import time
import urllib.parse
import urllib.request
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

DEFAULT_OVERRIDE_URL = (
    "https://raw.githubusercontent.com/forsiderr/"
    "vseprotisk-design-system/main/override-carbon.css"
)
INJECT_TAG = '<link rel="stylesheet" href="/__override.css">'

AUTO_REFRESH_JS = """
<script>
/* VSP auto-update: re-poll the injected override and swap in place. */
(function () {
  var url = location.protocol + '//' + location.host + '/__override.css';
  var link = document.querySelector('link[href="' + url + '"]');
  if (!link) { location.reload(); return; }
  var i = 0;
  setInterval(function () {
    i++;
    var probe = url + '?v=' + Date.now();
    var nl = document.createElement('link');
    nl.rel = 'stylesheet';
    nl.href = probe;
    nl.onload = function () {
      if (this.getAttribute('data-swap')) { return; }
      var old = document.querySelector('link[data-vsp-live]');
      // remove the previous live copy, keep the base injected tag as fallback
      var others = document.querySelectorAll('link[href^="' + url + '"]');
      for (var k = 0; k < others.length; k++) {
        if (!others[k].getAttribute('data-vsp-live')) continue;
        others[k].parentNode.removeChild(others[k]);
      }
      nl.setAttribute('data-vsp-live', '1');
      document.body.appendChild(nl);   // re-apply on top (layer wins anyway)
    };
    document.body.appendChild(nl);
  }, parseInt('__POLL__', 10) * 1000);
})();
</script>
"""


def build_handler(upstream: str, override_url: str, origin: str, poll: int):
    upstream = upstream.rstrip("/")
    up = urllib.parse.urlparse(upstream)
    scheme = up.scheme or "https"
    upstream_netloc = up.netloc
    fresh_js = AUTO_REFRESH_JS.replace("__POLL__", str(poll))

    class _Handler(BaseHTTPRequestHandler):
        server_version = "VSPlive/0.2"

        def log_message(self, format, *args):  # quiet
            pass

        def _fetch_bytes(self, url: str, timeout: int = 25) -> tuple[int, str, bytes]:
            req = urllib.request.Request(url, headers={"User-Agent": "VSPlive-review"})
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    body = resp.read()
                    ctype = resp.headers.get("Content-Type") or ""
                    return resp.status, ctype, body
            except Exception as exc:  # network/upstream hiccup
                return HTTPStatus.BAD_GATEWAY, "text/plain", str(exc).encode()

        def _serve_override(self):
            # always fetch the freshest override from the remote URL (no local copy)
            status, ctype, data = self._fetch_bytes(override_url, timeout=20)
            if status != 200:
                self.send_response(HTTPStatus.BAD_GATEWAY)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(f"override fetch failed: {data!r}".encode())
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/css; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):  # noqa: N802
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path == "/__override.css":
                self._serve_override()
                return
            path = self.path
            if parsed.scheme or parsed.netloc:
                path = parsed.path + ("?" + parsed.query if parsed.query else "")

            status, ctype, body = self._fetch_bytes(scheme + "://" + upstream_netloc + path)
            if "text/html" in ctype:
                try:
                    text = body.decode("utf-8", "replace")
                except Exception:
                    return self._write_raw(status, ctype, body)
                text = re.sub(
                    r'((?:href|src|action)=")(https?://)' + re.escape(upstream_netloc) + r'/',
                    r"\1" + origin + r"/",
                    text,
                )
                if "</head>" in text:
                    text = text.replace("</head>", INJECT_TAG + fresh_js + "</head>", 1)
                else:
                    text = INJECT_TAG + text
                body = text.encode("utf-8")
            self._write_raw(status, ctype, body)

        def _write_raw(self, status, ctype, body):
            self.send_response(status)
            if ctype:
                self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            try:
                self.wfile.write(body)
            except BrokenPipeError:
                pass

    return _Handler, fresh_js


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8124)
    ap.add_argument("--bind", default="127.0.0.1")
    ap.add_argument("--upstream", default="https://vseprotisk.t2.upgates.shop")
    ap.add_argument("--override-url", default=DEFAULT_OVERRIDE_URL)
    ap.add_argument("--poll", type=int, default=3)
    args = ap.parse_args()

    origin = f"http://{args.bind}:{args.port}"
    Handler, _ = build_handler(args.upstream, args.override_url, origin, args.poll)

    class Threaded(socketserver.ThreadingMixIn, HTTPServer):
        allow_reuse_address = True

    with Threaded((args.bind, args.port), Handler) as httpd:
        print("=" * 60)
        print("Running locally — no login needed.")
        print(f"  open  http://{args.bind}:{args.port}/   (in your browser)")
        print(f"  upstream : {args.upstream}")
        print(f"  override : {args.override_url}")
        print(f"  auto-apply every {args.poll}s — push a change and watch it update")
        print("  Ctrl+C to stop")
        print("=" * 60, flush=True)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
