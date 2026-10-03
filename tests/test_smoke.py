#!/usr/bin/env python3
"""
The live-site smoke test (model/smoke.py, #92) checks what a reader is served, after every deploy and weekly.

    python3 -m unittest discover -s tests -v

Its route list must cover the end-to-end routes and every member state, and it must fail, not pass, against
a server that serves the wrong thing. That is checked here against a local server, with no network.
"""
from __future__ import annotations

import http.server
import json
import re
import sys
import threading
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import smoke  # noqa: E402


class Coverage(unittest.TestCase):
    def test_routes_cover_every_e2e_route(self):
        spec = (ROOT / "web" / "e2e" / "app.spec.ts").read_text(encoding="utf-8")
        block = re.search(r"const ROUTES = \[(.*?)\]", spec, re.S).group(1)
        self.assertEqual(sorted(set(re.findall(r"'([^']+)'", block)) - set(smoke.ROUTES)), [])

    def test_every_member_state_pdf_is_checked(self):
        bundle = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
        self.assertEqual(sorted(smoke.ISOS), sorted(bundle["documents"]))

    def test_expected_headers_are_vercel_json_s(self):
        h = smoke.expected_headers()
        for name in ("content-security-policy", "x-frame-options", "x-content-type-options", "x-robots-tag"):
            self.assertIn(name, h)


class Wrong(http.server.BaseHTTPRequestHandler):
    """Serves 200 with the wrong type and no security headers, and 404 for PDFs."""

    def do_GET(self):  # noqa: N802
        if self.path.endswith(".pdf") or self.path.endswith(".png"):
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Allow: /\n")

    do_HEAD = do_GET

    def log_message(self, *args):  # noqa: ANN002
        pass


class FailsOnTheWrongSite(unittest.TestCase):
    def test_a_wrong_site_fails_every_content_check(self):
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Wrong)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            site = f"http://www.127.0.0.1:{server.server_port}".replace("www.", "")
            results = {name: ok for name, ok, _ in smoke.run(site, None, min_days=14)}
        finally:
            server.shutdown()
        self.assertFalse(results["GET /"])                       # text/plain, not HTML
        self.assertFalse(results["HEAD /report/DE.pdf"])         # 404
        self.assertFalse(results["header content-security-policy"])
        self.assertFalse(results["robots.txt disallows indexing"])
        self.assertFalse(any(ok for name, ok in results.items() if name.startswith("TLS")))


if __name__ == "__main__":
    unittest.main()
