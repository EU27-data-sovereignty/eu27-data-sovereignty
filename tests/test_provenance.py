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
# record fell from 1029 to 1017 on 2026-09-29, deliberately: #79 withdrew the 12 dependency claims an
# independent reviewer did not confirm. A floor may only be lowered by a recorded decision.
# param fell from 138 to 136 and record from 1017 to 1014 on 2026-09-30, deliberately: #82 requires a
# recorded quote check at the registered hash, which the 5 hand-migrated citations of #67 never had
# (param:FR/NL:data_classification, record:NL:{civil_registry,business_registry,land_property}:register).
# indicator fell from 134 to 130 the same day: #79 admits a value only when the reviewer reached it on
# its own, and EE K2, LU C2, PL C1 and RO C1 had been admitted at the reviewer's changed value.
# Raised 2026-09-30 by the charset fix, the Eurostat vintages (#84: the employment column now
# reproduces) and the first vetting run (#83).
FLOORS = {"param": 162, "assumption": 0, "record": 1511, "indicator": 142}


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
        """Until 2026-09-30, 26 of 27 gov_employment_k cells did not reproduce their series and were
        withheld; the column was rebuilt from the official series (#84). The rule still holds: a cell
        that differs from its dataset by more than the tolerance is not sourced."""
        params = provenance.parameters()
        rows = [c for c in self.cites if c["claim"].endswith(":gov_employment_k")]
        self.assertEqual(len(rows), 27)
        self.assertTrue(all(provenance.supported(c, self.reg, params) for c in rows))
        off = {**rows[0], "value_as_found": str(float(rows[0]["value_as_found"]) * 1.10)}
        self.assertFalse(provenance.supported(off, self.reg, params))


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

    def test_a_well_formed_record_claim_is_accepted(self):
        for claim in ("record:NL:civil_registry:register", "record:*:tax:count"):
            with self.subTest(claim=claim):
                self.assertEqual(provenance.validate(self.REG, [self.cite(claim=claim)]), [])

    def test_a_malformed_record_claim_is_rejected(self):
        """#67 reserved the shape; the register rows (national_data.csv) are its first users."""
        for claim in ("record:NL:civil_registry",          # the kind is missing
                      "record:NL:civil_registry:rows",     # unknown kind
                      "record:NL:fingerprints:register",   # not a record class
                      "record:UK:civil_registry:register"):  # not a member state
            with self.subTest(claim=claim):
                errors = provenance.validate(self.REG, [self.cite(claim=claim)])
                self.assertTrue(any("record claim must be" in e for e in errors))


class RecordDenominator(unittest.TestCase):
    def test_every_country_and_record_class_is_a_register_claim(self):
        """Without a denominator, 3 cited registers would read as 3 of 3 -- 100% sourced."""
        claims = provenance.claims_by_namespace()["record"]
        self.assertEqual(len(claims), 27 * 39)
        self.assertIn("record:NL:civil_registry:register", claims)


class NoHandTypedCitations(unittest.TestCase):
    """A source named in prose drifts from the source cited in the register: "LFS 2025" sat in every
    generated brief while the pinned series was nama_10_a64_e for 2023. Renderings look sources up."""

    def test_generator_prints_no_literal_eurostat_citation(self):
        src = (ROOT / "model" / "generate_countries.py").read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"\(Eurostat[^){]*\)", src), [])


if __name__ == "__main__":
    unittest.main()
