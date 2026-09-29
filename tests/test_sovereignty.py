#!/usr/bin/env python3
"""
The data-sovereignty placement rule (model/sovereignty.py, DECISIONS.md #77).

    python3 -m unittest discover -s tests -v

A ranking is the most quotable thing this project publishes, so its rule is pinned branch by
branch, and the two properties that make its confidence honest are checked exhaustively: an
unknown never helps a state, and the placement always lies inside its computed range.
"""
from __future__ import annotations

import itertools
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import sovereignty as sv  # noqa: E402

ALL_YES = {i: "yes" for i in sv.INDICATOR_IDS}


def holding(tier=0, status="held", dep="national"):
    return {"tier": tier, "status": status, "foreign_dependency": dep}


SOVEREIGN_HOLDINGS = [holding(0), holding(0), holding(1), holding(1, dep="eu_provider")]


class RuleBranches(unittest.TestCase):
    def test_law_and_practice(self):
        self.assertEqual(sv.place(ALL_YES, SOVEREIGN_HOLDINGS)["group"], "law_and_practice")

    def test_practice_without_the_law(self):
        self.assertEqual(sv.place({**ALL_YES, "L1": "partial"}, SOVEREIGN_HOLDINGS)["group"],
                         "practice_only")

    def test_law_without_practice(self):
        self.assertEqual(sv.place({**ALL_YES, "C1": "no", "C2": "no"}, SOVEREIGN_HOLDINGS)["group"],
                         "law_only")

    def test_neither(self):
        self.assertEqual(sv.place({**ALL_YES, "L1": "no", "K2": "partial"}, SOVEREIGN_HOLDINGS)["group"],
                         "not_demonstrated")

    def test_a_sourced_non_eu_dependency_outranks_everything(self):
        h = SOVEREIGN_HOLDINGS + [holding(1, dep="non_eu_provider")]
        self.assertEqual(sv.place(ALL_YES, h)["group"], "dependent")

    def test_a_non_eu_national_eid_is_dependent(self):
        self.assertEqual(sv.place({**ALL_YES, "K2": "no"}, SOVEREIGN_HOLDINGS)["group"], "dependent")

    def test_tier_two_holdings_do_not_decide_the_group(self):
        h = SOVEREIGN_HOLDINGS + [holding(2, dep="non_eu_provider")]
        self.assertEqual(sv.place(ALL_YES, h)["group"], "law_and_practice")


class Confidence(unittest.TestCase):
    def test_fully_settled_evidence_is_high_confidence(self):
        p = sv.place(ALL_YES, SOVEREIGN_HOLDINGS)
        self.assertEqual((p["confidence"], p["range"]), ("High", ["law_and_practice"]))

    def test_no_evidence_at_all_is_placed_not_demonstrated_with_low_confidence(self):
        h = [holding(0, status="unrecorded") for _ in range(9)]
        p = sv.place({}, h)
        self.assertEqual(p["group"], "not_demonstrated")
        self.assertEqual(p["confidence"], "Low")
        self.assertEqual(p["range"], sv.GROUPS)

    def test_an_unknown_dependency_can_only_lower_the_worst_case(self):
        p = sv.place(ALL_YES, SOVEREIGN_HOLDINGS + [holding(1, dep="unknown")])
        self.assertEqual(p["range"][-1], "dependent")

    def test_could_move_names_the_deciding_unknown(self):
        p = sv.place({**ALL_YES, "L1": "unknown"}, SOVEREIGN_HOLDINGS)
        self.assertEqual(p["group"], "practice_only")
        self.assertIn({"input": "L1", "if": "yes", "group": "law_and_practice"}, p["could_move"])


class Properties(unittest.TestCase):
    """Exhaustive over indicator values and a small set of holding patterns."""

    PATTERNS = [
        SOVEREIGN_HOLDINGS,
        SOVEREIGN_HOLDINGS + [holding(0, dep="unknown")],
        SOVEREIGN_HOLDINGS + [holding(1, status="unrecorded")],
        [holding(0, dep="non_eu_provider")],
        [holding(0, status="unrecorded")],
    ]
    VALUES = ("yes", "partial", "no", "unknown")
    KEYS = ("L1", "K1", "K2", "C1")      # the inputs the rule reads (C2 mirrors C1)

    def cases(self):
        for combo in itertools.product(self.VALUES, repeat=len(self.KEYS)):
            ind = {**ALL_YES, **dict(zip(self.KEYS, combo)), "C2": "no"}
            for h in self.PATTERNS:
                yield ind, h

    def test_the_placement_is_always_inside_its_range(self):
        for ind, h in self.cases():
            p = sv.place(ind, h)
            self.assertIn(p["group"], p["range"], (ind, h))

    def test_resolving_an_unknown_favourably_never_worsens_the_group(self):
        for ind, h in self.cases():
            placed = sv.GROUPS.index(sv.place(ind, h)["group"])
            for k, v in ind.items():
                if v == "unknown":
                    better = sv.GROUPS.index(sv.place({**ind, k: "yes"}, h)["group"])
                    self.assertLessEqual(better, placed, (ind, k))

    def test_no_numeric_score_is_produced(self):
        p = sv.place(ALL_YES, SOVEREIGN_HOLDINGS)
        self.assertFalse(any(isinstance(v, (int, float)) for v in p.values()))


if __name__ == "__main__":
    unittest.main()
