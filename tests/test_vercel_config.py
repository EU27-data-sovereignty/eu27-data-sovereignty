#!/usr/bin/env python3
"""
The parts of `vercel.json` that the rest of the gate cannot see.

    python3 -m unittest discover -s tests -v

Playwright runs against `vite preview`, which has its own SPA fallback, so a routing rule
that only breaks on Vercel passes every other stage. That happened: from the first deploy
until 2026-09-27 the SPA rewrite pointed at `/index.html` while `cleanUrls` was on. Vercel
308-redirects every `.html` path under `cleanUrls`, so the rewrite failed its filesystem
check and every deep link -- `/matrix`, `/country/DE`, a refresh on any page but `/` --
returned 404. DEPLOYMENT.md records it.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "vercel.json").read_text())


class Routing(unittest.TestCase):
    def test_spa_rewrite_survives_clean_urls(self):
        rewrites = CONFIG.get("rewrites", [])
        catch_all = [r for r in rewrites if r["source"] == "/(.*)"]
        self.assertEqual(len(catch_all), 1, "the SPA needs exactly one catch-all rewrite")
        dest = catch_all[0]["destination"]
        if CONFIG.get("cleanUrls"):
            self.assertFalse(dest.endswith(".html"),
                             f"cleanUrls redirects .html paths, so a rewrite to {dest} 404s every deep link")


class Headers(unittest.TestCase):
    def test_csp_applies_to_every_path(self):
        everywhere = [h for block in CONFIG["headers"] if block["source"] == "/(.*)"
                      for h in block["headers"]]
        keys = {h["key"] for h in everywhere}
        for key in ("Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options"):
            self.assertIn(key, keys, f"{key} must be set on every path (#50)")


if __name__ == "__main__":
    unittest.main()
