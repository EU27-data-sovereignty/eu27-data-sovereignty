#!/usr/bin/env python3
"""
The parts of `vercel.json` that the rest of the gate cannot see.

    python3 -m unittest discover -s tests -v

Playwright runs against `vite preview`, which has its own SPA fallback, so a routing rule
that only breaks on Vercel passes every other stage. That happened: from the first deploy
until 2026-09-27 the SPA rewrite pointed at `/index.html` while `cleanUrls` was on. Vercel
308-redirects every `.html` path under `cleanUrls`, so the rewrite failed its filesystem
check and every deep link -- `/matrix`, `/country/DE`, a refresh on any page but `/` --
returned 404. The first fix, `/`, then 404'd the home page itself once deploys went prebuilt
(#71), because the build output serves `index.html` at `/index`. DEPLOYMENT.md records both.
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
            self.assertEqual(dest, "/index",
                             f"under cleanUrls index.html is served at /index; a rewrite to {dest} 404s")


class Headers(unittest.TestCase):
    def test_csp_applies_to_every_path(self):
        everywhere = [h for block in CONFIG["headers"] if block["source"] == "/(.*)"
                      for h in block["headers"]]
        keys = {h["key"] for h in everywhere}
        for key in ("Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options"):
            self.assertIn(key, keys, f"{key} must be set on every path (#50)")

    def test_noindex_until_stage_two(self):
        # robots.txt alone does not keep a linked URL out of an index, and since #80 the site
        # sits on a public domain. Remove this header together with robots.txt's Disallow at
        # stage 2 (DEPLOYMENT.md "Staging and domain"), and this test with it.
        everywhere = {h["key"]: h["value"] for block in CONFIG["headers"] if block["source"] == "/(.*)"
                      for h in block["headers"]}
        self.assertEqual(everywhere.get("X-Robots-Tag"), "noindex", "the site is not to be indexed yet (#80)")


if __name__ == "__main__":
    unittest.main()


class Deploys(unittest.TestCase):
    def test_vercel_never_builds_from_git_itself(self):
        # The project is connected to the repo (2026-10-05), but production ships only from GitHub Actions,
        # prebuilt, after ./test.sh and the fact-check gate (#81, #87). A Vercel-side build from a push would
        # skip both, and cannot build the PDFs anyway (no typst).
        self.assertEqual(CONFIG.get("git"), {"deploymentEnabled": False})
