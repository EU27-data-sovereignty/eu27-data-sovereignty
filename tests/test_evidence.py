#!/usr/bin/env python3
"""
What the outputs say about their own evidence (model/evidence.py).

    python3 -m unittest discover -s tests -v

An output may not describe a check that did not run, and every output says, in the same words, that
no person has verified the findings. These tests read the committed outputs (the bundle, the briefs)
and the renderers' source, because a sentence in a template is exactly where overstatement crept in.
"""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
sys.path.insert(0, str(ROOT / "book"))

import evidence  # noqa: E402
import sovereignty as sv  # noqa: E402

BUNDLE = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
BRIEFS = sorted((ROOT / "countries").glob("*/GOAL.md"))

# Wording that claimed more than ran: 136 Eurostat facts were never hashed (2026-09-30 audit).
OVERSTATED = re.compile(r"fetched,? hashed,? and checked|every fact [^.;]{0,40}checked source"
                        r"|verified findings|checked against a fetched source", re.I)
SURFACES = [
    ROOT / "book" / "report.py", ROOT / "model" / "generate_countries.py",
    ROOT / "model" / "export_json.py", ROOT / "model" / "national_data.py",
    ROOT / "api" / "_ask-core.ts", *sorted((ROOT / "web" / "src").rglob("*.tsx")),
]


class Disclaimer(unittest.TestCase):
    def test_the_bundle_carries_it(self):
        self.assertEqual(BUNDLE["notice"]["disclaimer"], evidence.DISCLAIMER)
        self.assertIn("not human-verified", BUNDLE["provenance"])

    def test_every_brief_carries_it(self):
        self.assertEqual(len(BRIEFS), 27)
        for brief in BRIEFS:
            self.assertIn(evidence.DISCLAIMER, brief.read_text(encoding="utf-8"), brief.parent.name)

    def test_the_report_and_country_pdfs_carry_it(self):
        import report  # noqa: PLC0415
        self.assertIn("not human-verified", report.report_typ(BUNDLE))
        self.assertIn("not human-verified", report.country_typ(BUNDLE, "DE"))

    def test_ask_is_told_to_say_it(self):
        core = (ROOT / "api" / "_ask-core.ts").read_text(encoding="utf-8")
        self.assertIn("no person has verified them", core)
        self.assertIn("not verified by a person", core)

    def test_the_web_app_shows_it(self):
        pages = {p.name: p.read_text(encoding="utf-8") for p in (ROOT / "web" / "src").rglob("*.tsx")}
        self.assertIn("notice.disclaimer", pages["Overview.tsx"])
        self.assertIn("notice.disclaimer", pages["Methodology.tsx"])
        self.assertIn("not human-verified", pages["Poster.tsx"])


class NoOverstatement(unittest.TestCase):
    def test_no_surface_claims_a_check_that_did_not_run(self):
        hits = [f"{p.relative_to(ROOT)}: {m.group(0)!r}" for p in SURFACES
                for m in OVERSTATED.finditer(p.read_text(encoding="utf-8"))]
        hits += [f"{b.relative_to(ROOT)}: {m.group(0)!r}" for b in BRIEFS
                 for m in OVERSTATED.finditer(b.read_text(encoding="utf-8"))]
        self.assertEqual(hits, [])


class RankingRule(unittest.TestCase):
    def test_the_published_rule_names_every_group_once_in_evaluation_order(self):
        self.assertEqual(sorted(g for g, _ in sv.RULE), sorted(sv.GROUPS))
        self.assertEqual(sv.RULE[0][0], "dependent")      # group() checks dependency first

    def test_the_published_share_is_the_one_the_rule_uses(self):
        self.assertIn(f"{sv.H1_SHARE:.0%}", dict(sv.RULE)["law_and_practice"])

    def test_the_report_prints_the_rule_from_the_bundle(self):
        src = (ROOT / "book" / "report.py").read_text(encoding="utf-8")
        self.assertNotIn("at least 75%", src)
        self.assertIn('sov["rule"]', src)


if __name__ == "__main__":
    unittest.main()
