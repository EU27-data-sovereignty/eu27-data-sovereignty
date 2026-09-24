#!/usr/bin/env python3
"""
The source register, model/sources/ (DECISIONS.md #67).

    python3 -m unittest discover -s tests -v

What a test needs from the register is not "does it parse" but "can every published figure be
traced to a document": each citation names a registered source and says where in it; each source
is cited; a dataset value actually reproduces the cell it supports; and the coverage per namespace
only ever goes up.

FLOORS is a ratchet, one per namespace, asserted from both sides like test_sources.COVERAGE_FLOOR:
removing a citation fails the build, and so does adding one without raising the floor. The launch
gate (memory: nothing launches below full coverage) is every floor at its namespace's total.
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import provenance  # noqa: E402

# Supported claims per namespace. Raise in the commit that adds the citations.
FLOORS = {"param": 138, "assumption": 0}


class Register(unittest.TestCase):
    def setUp(self):
        self.reg = provenance.registry()
        self.cites = provenance.citations()

    def test_register_is_sound(self):
        self.assertEqual(provenance.validate(self.reg, self.cites), [])

    def test_coverage_never_regresses(self):
        cov = provenance.coverage(self.reg, self.cites)
        for ns, floor in FLOORS.items():
            self.assertGreaterEqual(cov[ns][0], floor,
                                    f"{ns}: supported claims fell below the floor of {floor}")

    def test_floors_are_kept_current(self):
        cov = provenance.coverage(self.reg, self.cites)
        for ns, floor in FLOORS.items():
            self.assertLessEqual(cov[ns][0] - floor, 0,
                                 f"{ns}: {cov[ns][0]} claims are supported but the floor is {floor}. "
                                 "Raise it here so the progress cannot be undone silently.")

    def test_a_dataset_value_that_does_not_reproduce_is_not_coverage(self):
        """gov_employment_k is cited to its pinned series but 26 of 27 cells do not reproduce it."""
        params = provenance.parameters()
        rows = [c for c in self.cites if c["claim"].endswith(":gov_employment_k")]
        self.assertEqual(len(rows), 27)
        supported = [c for c in rows if provenance.supported(c, self.reg, params)]
        self.assertLessEqual(len(supported), 1)


class Rules(unittest.TestCase):
    REG = {"x:doc@2026": {"source_id": "x:doc@2026", "title": "T", "publisher": "P",
                          "url": "https://example.org", "doc_type": "report", "published": "2026",
                          "language": "en", "license": "", "archived_url": "", "notes": ""}}

    def cite(self, **kw):
        base = {"claim": "doc:README.md#x", "source_id": "x:doc@2026", "locator": "p. 1",
                "quote": "a quote long enough to be evidence", "value_as_found": "", "unit": "",
                "confidence": "primary", "retrieved": "2026-09-24", "checked_by": "test"}
        return {**base, **kw}

    def test_unknown_source_is_rejected(self):
        errors = provenance.validate(self.REG, [self.cite(source_id="y:missing")])
        self.assertTrue(any("not in the registry" in e for e in errors))

    def test_missing_locator_is_rejected(self):
        errors = provenance.validate(self.REG, [self.cite(locator="")])
        self.assertTrue(any("locator is empty" in e for e in errors))

    def test_short_quote_is_rejected(self):
        errors = provenance.validate(self.REG, [self.cite(quote="too short")])
        self.assertTrue(any("quote" in e for e in errors))

    def test_uncited_source_is_rejected(self):
        errors = provenance.validate(self.REG, [])
        self.assertTrue(any("cited by nothing" in e for e in errors))

    def test_an_assumption_is_declared_not_supported(self):
        c = self.cite(confidence="assumption")
        self.assertFalse(provenance.supported(c, self.REG, {}))


class NoHandTypedCitations(unittest.TestCase):
    """A source named in prose drifts from the source cited in the register: "LFS 2025" sat in every
    generated brief while the pinned series was nama_10_a64_e for 2023. Renderings look sources up."""

    def test_generator_prints_no_literal_eurostat_citation(self):
        src = (ROOT / "model" / "generate_countries.py").read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"\(Eurostat[^){]*\)", src), [])


if __name__ == "__main__":
    unittest.main()
