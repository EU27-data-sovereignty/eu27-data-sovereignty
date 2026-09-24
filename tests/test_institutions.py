#!/usr/bin/env python3
"""
The institutional contact map, model/institutions.csv.

    python3 -m unittest discover -s tests -v

Institutions only: a row names a body and its published inbound channel, never a person (#26, #49).
Rows arrive from the private research pass through contacts/tools/check_institutions.py, which
admits a row only if it passes this validator, names no one in the private inventory, and has its
quote found on the body's own page (#66).

PAIRS_FLOOR is a ratchet on (country, function) pairs filled, asserted from both sides.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import institutions  # noqa: E402

PAIRS_FLOOR = 25   # of 324 = 12 functions x 27 member states


class Map(unittest.TestCase):
    def setUp(self):
        self.rows = institutions.load()

    def test_every_row_is_a_usable_route(self):
        self.assertEqual(institutions.validate(self.rows), [])

    def test_coverage_never_regresses(self):
        filled = sum(len(v) for v in institutions.coverage(self.rows).values())
        self.assertGreaterEqual(filled, PAIRS_FLOOR)

    def test_the_floor_is_kept_current(self):
        filled = sum(len(v) for v in institutions.coverage(self.rows).values())
        self.assertLessEqual(filled - PAIRS_FLOOR, 0,
                             f"{filled} pairs are filled but PAIRS_FLOOR is {PAIRS_FLOOR}; raise it")


if __name__ == "__main__":
    unittest.main()
