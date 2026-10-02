#!/usr/bin/env python3
"""
The methodology appendix (model/methodology.py, #84) states nothing of its own.

    python3 -m unittest discover -s tests -v

Every rule in it must be the constant the code runs, it must be in every output, and it may not
describe a check that is not in evidence.CHECKS.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
sys.path.insert(0, str(ROOT / "book"))

import document  # noqa: E402
import evidence  # noqa: E402
import sovereignty as sv  # noqa: E402

BUNDLE = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
DOC = BUNDLE["methodology"]
TEXT = " ".join(s["t"] for s in document.walk_spans(DOC))


class Content(unittest.TestCase):
    def test_every_rule_is_the_constant_the_code_runs(self):
        for rule in (BUNDLE["notice"]["disclaimer"], evidence.GRADE_RULE, evidence.WITHHELD, document.PRIORITY_RULE,
                     sv.UNKNOWN_RULE, sv.CONFIDENCE_RULE):
            self.assertIn(rule, TEXT, rule[:50])
        for name, what in evidence.CHECKS:
            self.assertIn(f"{name}: {what}", TEXT)
        for group, condition in sv.RULE:
            self.assertIn(f"{sv.LABELS[group]}: {condition}.", TEXT)

    def test_every_eurostat_series_is_documented_with_its_pinned_period(self):
        from fetch_eurostat import SERIES  # noqa: PLC0415
        for col, (ds, _f, _m, _d, period) in SERIES.items():
            row = next(r for s in DOC["sections"] for b in s["blocks"] if b["type"] == "table"
                       for r in b["rows"] if r[0]["t"] == col)
            self.assertEqual((row[1]["t"], row[3]["t"]), (ds, period), col)

    def test_its_counts_are_the_documents_counts(self):
        facts = sum(1 for d in BUNDLE["documents"].values() for s in document.walk_spans(d) if s["role"] == "fact")
        self.assertIn(f"{facts} facts are printed", TEXT)

    def test_it_asserts_no_fact(self):
        self.assertEqual({s["role"] for s in document.walk_spans(DOC)} - {"method", "label"}, set())


class Rendered(unittest.TestCase):
    def test_it_is_an_appendix_of_the_report_and_every_country_pdf(self):
        import report  # noqa: PLC0415
        self.assertIn("Appendix: methodology", report.report_typ(BUNDLE))
        for iso in ("DE", "MT"):
            self.assertIn("Appendix: methodology", report.country_typ(BUNDLE, iso))

    def test_the_pdfs_carry_their_commit_and_bundle_hash(self):
        import report  # noqa: PLC0415
        self.assertRegex(report.build_stamp(), r"^Built from commit \S+.*; data bundle sha256 [0-9a-f]{16}\.$")

    def test_the_web_page_renders_the_generated_document(self):
        page = (ROOT / "web" / "src" / "pages" / "Methodology.tsx").read_text(encoding="utf-8")
        self.assertIn("bundle.methodology", page)


class Everywhere(unittest.TestCase):
    """The methodology is in every asset, set apart in the method teal (#88)."""

    def test_it_states_the_fact_check_from_its_constants(self):
        import factcheck  # noqa: PLC0415
        titles = [s["title"] for s in DOC["sections"]]
        self.assertIn("The cross-model fact check before every deploy", titles)
        for author, checker in factcheck.RULE:
            self.assertIn(author, TEXT)
            self.assertIn(checker, TEXT)

    def test_every_brief_carries_it_in_full(self):
        first = DOC["sections"][1]["title"]
        for iso in BUNDLE["documents"]:
            brief = (ROOT / "countries" / iso / "GOAL.md").read_text(encoding="utf-8")
            self.assertIn("## Appendix: methodology", brief, iso)
            self.assertIn(f"### {first}", brief, iso)

    def test_ask_answers_from_it(self):
        corpus = json.loads((ROOT / "api" / "_corpus.json").read_text(encoding="utf-8"))
        titles = [d["title"] for d in corpus["documents"]]
        self.assertIn("Methodology: how every fact was sourced, checked and calculated", titles)

    def test_every_poster_points_to_it(self):
        poster = (ROOT / "web" / "src" / "pages" / "Poster.tsx").read_text(encoding="utf-8")
        self.assertIn("Method: /methodology", poster)
        self.assertIn("var(--color-method)", poster)

    def test_the_pdfs_set_both_appendices_in_the_method_style(self):
        import report  # noqa: PLC0415
        for typ in (report.report_typ(BUNDLE), report.country_typ(BUNDLE, "DE")):
            self.assertEqual(typ.count("#method-appendix["), 2)
        template = (ROOT / "book" / "templates" / "report.typ").read_text(encoding="utf-8")
        self.assertIn("Method · how this was made", template)

    def test_the_web_pages_use_the_method_frame(self):
        pages = ROOT / "web" / "src" / "pages"
        for name in ("Methodology.tsx", "FactCheck.tsx"):
            self.assertIn("<MethodFrame", (pages / name).read_text(encoding="utf-8"), name)

    def test_the_method_colour_is_a_token_in_both_themes(self):
        tokens = json.loads((ROOT / "design" / "tokens.json").read_text(encoding="utf-8"))
        for theme in ("light", "dark"):
            self.assertIn("method", tokens["themes"][theme])
            self.assertIn("method_wash", tokens["themes"][theme])
        self.assertIn(["method", "bg_page"], tokens["contrast"]["text"])


if __name__ == "__main__":
    unittest.main()
