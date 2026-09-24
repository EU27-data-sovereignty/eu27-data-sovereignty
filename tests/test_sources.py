#!/usr/bin/env python3
"""
The verification ledger: the legal-cell citations in model/sources/citations.csv (#67).

    python3 -m unittest discover -s tests -v

The ledger is the gate on everything public-facing (ROADMAP.md, DECISIONS.md #25), so
what it needs from a test is not "does it parse" but "is a row in it actually evidence":
a real country, a sourceable column, an absolute URL, a retrieval date, and a quote long
enough to show the cited page says what the cell claims.

COVERAGE_FLOOR is a ratchet. It may only be raised, and raising it is the commit that
records verification progress. The end state ROADMAP step 3 asks for -- CI failing on any
unsourced legal cell -- is `python3 model/sources.py --strict`; the floor is the honest
interim, because a check that fails on day one gets disabled on day two.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import sources  # noqa: E402

# Raise as cells are verified. 189 = 7 sourceable columns x 27 member states.
COVERAGE_FLOOR = 2


class Ledger(unittest.TestCase):
    def setUp(self):
        self.rows = sources.load()  # raises if the header is not exactly FIELDS

    def test_every_row_is_usable_evidence(self):
        self.assertEqual(sources.validate(self.rows), [])

    def test_coverage_never_regresses(self):
        covered = sources.covered_cells(self.rows)
        self.assertGreaterEqual(
            covered,
            COVERAGE_FLOOR,
            f"coverage fell to {covered} from a floor of {COVERAGE_FLOOR}: a source row was "
            "removed. Sources are only ever added, or replaced by a better one.",
        )

    def test_the_floor_is_kept_current(self):
        covered = sources.covered_cells(self.rows)
        self.assertLessEqual(
            covered - COVERAGE_FLOOR,
            0,
            f"{covered} cells are sourced but COVERAGE_FLOOR is still {COVERAGE_FLOOR}. "
            "Raise it in this file so the progress cannot be undone silently.",
        )


class AbsenceIsEvidencedNotAssumed(unittest.TestCase):
    """`confidence: absence` exists so a cell claiming nothing exists can still be sourced.

    22 of the 81 tier-1 cells assert an absence, so a rule admitting only `primary` capped
    tier 1 at 72.8% and made `--strict` unsatisfiable. The value that fixes that is also the
    easiest one to abuse -- it would let any hard-to-find instrument be waved through -- so
    the guard is that the cited cell must actually assert an absence.
    """

    def test_absence_is_a_confidence_value(self):
        self.assertIn("absence", sources.CONFIDENCE)

    def test_tier1_accepts_only_primary_or_absence(self):
        self.assertEqual(set(sources.TIER1_CONFIDENCE), {"primary", "absence"})
        self.assertNotIn("secondary", sources.TIER1_CONFIDENCE)
        self.assertNotIn("official", sources.TIER1_CONFIDENCE)

    def test_absence_on_a_positive_cell_is_rejected(self):
        """The whole guard. FR certification_scheme names SecNumCloud; it is not an absence."""
        row = {
            "country": "FR", "column": "certification_scheme",
            "url": "https://example.org/register", "publisher": "Some authority",
            "retrieved": "2026-09-11", "confidence": "absence",
            "quote": "This register lists every national scheme currently in force.",
        }
        errors = sources.validate([row])
        self.assertTrue(
            any("does not assert one" in e for e in errors),
            f"`absence` must be refused on a cell naming a real scheme; got {errors}",
        )

    def test_absence_on_a_negative_cell_is_accepted(self):
        """NL certification_scheme is 'No national cloud scheme; BIO is the binding baseline'."""
        row = {
            "country": "NL", "column": "certification_scheme",
            "url": "https://example.org/register", "publisher": "Some authority",
            "retrieved": "2026-09-11", "confidence": "absence",
            "quote": "This register lists every national scheme currently in force.",
        }
        self.assertEqual(sources.validate([row]), [])

    def test_the_ceiling_is_now_reachable(self):
        """Before `absence`, 22 tier-1 cells could never be sourced and --strict never passed."""
        neg = sources.negative_cells()
        self.assertGreater(sum(neg.values()), 0, "expected negative cells in the dataset")
        tier1_neg = sum(neg[c] for c in sources.TIER1)
        self.assertGreater(tier1_neg, 20, "the problem this value solves should still be visible")


class TieringIsWiredToTheData(unittest.TestCase):
    """The column lists are hand-maintained and sit next to a CSV that changes."""

    def test_every_named_column_exists_in_the_parameters(self):
        import csv

        with sources.PARAMETERS.open(newline="", encoding="utf-8") as fh:
            header = set(csv.DictReader(fh).fieldnames or [])
        named = set(sources.TIER1 + sources.TIER2 + sources.JUDGEMENT)
        self.assertEqual(named - header, set(), "sources.py names a column the dataset does not have")

    def test_tiers_do_not_overlap(self):
        self.assertEqual(set(sources.TIER1) & set(sources.TIER2), set())
        self.assertEqual(set(sources.REQUIRED) & set(sources.JUDGEMENT), set())

    def test_all_27_states_are_addressable(self):
        self.assertEqual(len(sources.countries()), 27)


if __name__ == "__main__":
    unittest.main()
