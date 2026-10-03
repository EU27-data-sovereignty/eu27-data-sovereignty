#!/usr/bin/env python3
"""
The fetch layer against a real HTTP server on localhost (#92): no mocks, no internet.

    python3 -m unittest discover -s tests -v

The rules it is held to (model/fetch.py): a published robots `Disallow` is obeyed; a robots.txt that is
itself refused is not a rule, so the document is still requested and its own status recorded; a 403 is an
answer, recorded and never retried; a redirect is followed; nothing raises. And research.snapshot_matches
accepts an archived copy only of exactly the requested host.
"""
from __future__ import annotations

import http.server
import sys
import threading
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import fetch  # noqa: E402
import research  # noqa: E402

HITS: list[str] = []


class Site(http.server.BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        HITS.append(self.path)
        host = self.headers.get("Host", "")
        routes = {
            "/robots.txt": (200, "text/plain", b"User-agent: *\nDisallow: /private\n"),
            "/page": (200, "text/html; charset=utf-8", "<p>Das Register enthält 4.000 Server.</p>".encode()),
            "/forbidden": (403, "text/html", b"no"),
            "/private/doc": (200, "text/html", b"secret"),
        }
        if self.path == "/moved":
            self.send_response(301)
            self.send_header("Location", f"http://{host}/page")
            self.end_headers()
            return
        code, ctype, body = routes.get(self.path, (404, "text/plain", b""))
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):  # noqa: ANN002
        pass


class RobotsRefused(Site):
    def do_GET(self):  # noqa: N802
        if self.path == "/robots.txt":
            HITS.append(self.path)
            self.send_response(403)
            self.end_headers()
            return
        super().do_GET()


class Server(unittest.TestCase):
    handler = Site

    def setUp(self):
        HITS.clear()
        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), self.handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"
        self.patches = [mock.patch.object(fetch, "DELAY", 0), mock.patch.object(fetch, "_robots", {})]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.server.shutdown()
        self.server.server_close()


class Fetch(Server):
    def test_a_page_is_fetched_with_its_bytes_and_type(self):
        r = fetch.fetch(f"{self.base}/page")
        self.assertTrue(r.ok)
        self.assertEqual(r.content_type, "text/html")
        self.assertIn("4.000 Server".encode(), r.body)

    def test_a_redirect_is_followed(self):
        r = fetch.fetch(f"{self.base}/moved")
        self.assertTrue(r.ok)
        self.assertIn(b"4.000", r.body)

    def test_a_403_is_recorded_once_and_not_retried(self):
        r = fetch.fetch(f"{self.base}/forbidden")
        self.assertEqual(r.status, "403")
        self.assertEqual(HITS.count("/forbidden"), 1)

    def test_a_published_disallow_is_obeyed_without_requesting_the_page(self):
        r = fetch.fetch(f"{self.base}/private/doc")
        self.assertEqual(r.status, fetch.STATUS_ROBOTS)
        self.assertNotIn("/private/doc", HITS)

    def test_an_unreachable_host_is_an_error_result_not_an_exception(self):
        self.server.shutdown()
        self.server.server_close()                 # nothing listens: connection refused, at once
        r = fetch.fetch(f"{self.base}/page", timeout=2)
        self.assertIn(r.status, (fetch.STATUS_ERROR, fetch.STATUS_TIMEOUT))


class RefusedRobots(Server):
    handler = RobotsRefused

    def test_a_refused_robots_txt_is_not_a_rule(self):
        self.assertEqual(fetch.robots_check(f"{self.base}/page"), fetch.STATUS_ROBOTS_UNREADABLE)
        r = fetch.fetch(f"{self.base}/page")
        self.assertTrue(r.ok)                      # requested anyway; its own status is the answer


class Snapshot(unittest.TestCase):
    def test_only_an_archive_of_exactly_the_requested_host_is_accepted(self):
        url = "https://www.example.gov/register"
        ok = "https://web.archive.org/web/20260101000000/https://www.example.gov/register"
        self.assertTrue(research.snapshot_matches(ok, url))
        for bad in ("https://web.archive.org/web/20260101000000/https://mailbox@www.example.gov/register",
                    "https://web.archive.org/web/20260101000000/https://example.gov/register",
                    "https://web.archive.org/web/20260101000000/https://www.example.gov.evil.test/register",
                    "https://web.archive.org/web/2026"):
            with self.subTest(bad=bad):
                self.assertFalse(research.snapshot_matches(bad, url))


if __name__ == "__main__":
    unittest.main()
