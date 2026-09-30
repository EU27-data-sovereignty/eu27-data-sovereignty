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
        self.assertIn(report.esc(evidence.DISCLAIMER), report.report_typ(BUNDLE))
        self.assertIn(report.esc(evidence.DISCLAIMER), report.country_typ(BUNDLE, "DE"))

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


class ValueInQuote(unittest.TestCase):
    """The printed value against its quote (#82)."""

    def check(self, value, quote, title=""):
        return evidence.value_in_quote(value, quote, title)

    def test_a_number_written_in_another_locale_matches(self):
        self.assertTrue(self.check("1,007,920 residence documents", "ΣΥΝΟΛΟ 274.705 1.007.920")["ok"])
        self.assertTrue(self.check("4.1 million users", "über 4,1 Millionen Bürger nutzen die App")["ok"])
        self.assertTrue(self.check("1 007 920", "total 1,007,920 in force")["ok"])

    def test_a_number_the_quote_does_not_contain_fails(self):
        r = self.check("17 million records (2022), plus 48 million victim records",
                       "En 2022, le TAJ contenait : 17 millions de fiches "
                       "[English: In 2022, the TAJ contained: 17 million records]")
        self.assertFalse(r["ok"])
        self.assertEqual(r["missing_numbers"], ["48"])

    def test_a_number_only_in_the_gloss_does_not_count(self):
        r = self.check("kept for 10 years", "съхранява се за срок от десет години [English: kept for 10 years]")
        self.assertFalse(r["ok"])

    def test_a_missing_acronym_is_disclosed_not_fatal(self):
        r = self.check("Weapons register kept by the MVR", "Министерството на вътрешните работи (МВР) води регистър")
        self.assertTrue(r["ok"])
        self.assertEqual(r["missing_names"], ["MVR"])
        self.assertEqual(r["how"], "summary")

    def test_capitalised_compounds_and_generic_abbreviations_are_not_names(self):
        self.assertEqual(evidence.acronyms("Directorate-General for ID and EU IT"), set())
        self.assertEqual(evidence.acronyms("ZMR and RTR-GmbH"), {"ZMR", "RTR-GmbH"})

    def test_how_a_value_relates_to_its_quote_is_recorded(self):
        self.assertEqual(self.check("Zentrales Melderegister", "des Zentrales Melderegister wird geführt")["how"],
                         "verbatim")
        self.assertEqual(self.check("Central Register", "Zentralregister [English: the Central Register]")["how"],
                         "verbatim_gloss")


class Review(unittest.TestCase):
    def test_every_admitted_indicator_was_reached_by_the_reviewer_on_its_own(self):
        import csv  # noqa: PLC0415
        import research  # noqa: PLC0415
        with (ROOT / "model" / "sovereignty_indicators.csv").open(newline="", encoding="utf-8") as fh:
            admitted = {(r["iso"], r["indicator"]) for r in csv.DictReader(fh)}
        staged = {(iso, ind["id"]): ind for iso, doc in research.staged(None, research.INDICATOR_STAGING).items()
                  for ind in doc.get("indicators", [])}
        disputed = sorted(k for k in admitted if not research.agreed(staged[k]))
        self.assertEqual(disputed, [])


class Grades(unittest.TestCase):
    """The evidence grade is computed by one rule and never read from data (#82)."""

    def test_the_bundle_grade_is_the_rule_recomputed(self):
        import provenance  # noqa: PLC0415
        reg = provenance.registry()
        docs = BUNDLE["documents"]
        text = {c: sp["t"] for d in docs.values() for sp in self._spans(d) if sp.get("role") == "fact"
                for c in sp["c"]}
        kind = {c: sp.get("k") for d in docs.values() for sp in self._spans(d) if sp.get("role") == "fact"
                for c in sp["c"]}
        for claim, cites in BUNDLE["claims"].items():
            for c in cites:
                again = evidence.assess(text[claim], {**c, "claim": claim}, reg[c["source_id"]],
                                        categorical=kind[claim] == "categorical")
                self.assertEqual((c["grade"], c["checks"]), (again["grade"], again["checks"]), claim)

    def test_no_strong_fact_misses_a_required_check(self):
        for claim, cites in BUNDLE["claims"].items():
            for c in cites:
                if c["grade"] != evidence.STRONG:
                    continue
                ck = c["checks"]
                self.assertIn(ck["source"], ("primary", "official"), claim)
                self.assertTrue(ck["archived"] and ck["document_hashed"], claim)
                self.assertEqual(ck.get("quote_match"), "exact", claim)
                self.assertFalse(ck.get("names_not_in_quote"), claim)
                self.assertNotIn("review", ck, claim)

    def test_a_span_carries_its_best_grade(self):
        for d in BUNDLE["documents"].values():
            for sp in self._spans(d):
                if sp.get("role") == "fact":
                    grades = {c["grade"] for c in BUNDLE["claims"][sp["c"][0]]}
                    want = evidence.STRONG if evidence.STRONG in grades else evidence.STANDARD
                    self.assertEqual(sp["g"], want, sp["c"])

    @staticmethod
    def _spans(doc):
        import document  # noqa: PLC0415
        return document.walk_spans(doc)


class RenderedFacts(unittest.TestCase):
    """What the documents print, after #82."""

    # Fact spans across the 27 documents. A ratchet like test_provenance.FLOORS: adding facts without
    # raising it fails, and so does losing any. It fell from 997 to 922 on 2026-09-30 by #82: 5
    # citations had no recorded quote check, and 70 printed values carried a number or date their
    # quote does not contain. Then to 918: 4 indicator values admitted at a reviewer's changed value
    # were withdrawn (#79).
    FACT_FLOOR = 918

    @classmethod
    def setUpClass(cls):
        import document  # noqa: PLC0415
        import export_json  # noqa: PLC0415
        cls.document = document
        cls.src = document.Sources()
        bundle = export_json.build_bundle()
        cls.docs = {iso: document.country(c, cls.src) for iso, c in bundle["countries"].items()}
        cls.facts = [(iso, s) for iso, d in cls.docs.items() for s in document.walk_spans(d)
                     if s["role"] == "fact"]

    def test_the_fact_count_is_the_recorded_one(self):
        self.assertEqual(len(self.facts), self.FACT_FLOOR)

    def test_every_printed_value_is_backed_as_printed(self):
        errors = [e for iso, d in self.docs.items() for e in self.document.check(d, self.src)]
        self.assertEqual(errors, [])

    def test_a_retention_period_is_not_printed_as_a_record_count(self):
        self.assertFalse(any(s["c"] == ["record:BG:authentication_audit_log:count"] for _, s in self.facts))

    def test_a_figure_its_quote_does_not_contain_is_not_printed(self):
        self.assertFalse(any(s["c"] == ["record:FR:police_records:count"] for _, s in self.facts))

    def test_a_citation_without_a_recorded_quote_check_supports_nothing(self):
        import provenance  # noqa: PLC0415
        c = next(c for c in self.src.cites if c["checked_by"].startswith("research.py"))
        forged = {**c, "source_id": "hand-typed:x"}
        reg = {**self.src.reg, "hand-typed:x": {**self.src.reg[c["source_id"]], "notes": "typed in by hand"}}
        self.assertTrue(provenance.supported(c, self.src.reg, self.src.params))
        self.assertFalse(provenance.supported(forged, reg, self.src.params))


if __name__ == "__main__":
    unittest.main()
