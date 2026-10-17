#!/usr/bin/env python3
"""
The privacy page (#116): one page the app stores link to, naming every processor the plans name, and the
same claims the mobile reader's own tests hold it to.

    python3 -m unittest tests.test_privacy -v
"""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = (ROOT / "web" / "src" / "pages" / "Privacy.tsx").read_text(encoding="utf-8")
APP = json.loads((ROOT / "mobile" / "app.json").read_text(encoding="utf-8"))["expo"]
LISTING = json.loads((ROOT / "mobile" / "store.config.json").read_text(encoding="utf-8"))["apple"]

# Every service that sees a reader's request, per docs/plans/stichting.md § Privacy and mobile/README.md.
PROCESSORS = ["Vercel", "Anthropic", "Supabase", "Expo", "Apple", "Google"]


class Page(unittest.TestCase):
    def test_the_route_exists_and_the_stores_and_the_app_point_at_it(self):
        app_tsx = (ROOT / "web" / "src" / "App.tsx").read_text(encoding="utf-8")
        self.assertIn('path="privacy"', app_tsx)
        self.assertEqual(APP["extra"]["privacyPath"], "/privacy")
        self.assertEqual(LISTING["info"]["en-US"]["privacyPolicyUrl"], f"{APP['extra']['siteUrl']}/privacy")
        layout = (ROOT / "web" / "src" / "components" / "Layout.tsx").read_text(encoding="utf-8")
        self.assertIn('to="/privacy"', layout)

    def test_every_processor_is_named_with_what_it_sees(self):
        for who in PROCESSORS:
            self.assertIn(who, PAGE, f"the privacy page does not name {who}")
        self.assertRegex(PAGE, r"network address")
        self.assertIn("no cookies", PAGE)

    def test_the_app_s_claims_are_the_ones_its_tests_hold(self):
        # The reader's security suite asserts: no permissions, no analytics, no request unless asked, the
        # update check only on the same tap (#115). The page may not promise more or less.
        self.assertIn("collects nothing", PAGE)
        self.assertIn("makes no\n        request", PAGE.replace("makes no request", "makes no\n        request"))
        self.assertIn("Expo’s update service", PAGE)
        self.assertEqual(APP["updates"]["checkAutomatically"], "NEVER")
        self.assertEqual(APP["android"]["permissions"], [])

    def test_no_email_address_on_the_page(self):
        self.assertNotRegex(PAGE, r"[\w.+-]+@[\w-]+\.[\w.]+")


if __name__ == "__main__":
    unittest.main()
