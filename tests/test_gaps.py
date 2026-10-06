"""docs/gaps.md: every gap is counted once, and its kind follows from the research that actually ran.

    python3 -m unittest tests.test_gaps -v
"""
import collections
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import gaps  # noqa: E402
import national_data as nd  # noqa: E402


class Cells(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cells = gaps.cells()
        cls.rows = nd.read_rows()

    def test_every_cell_is_counted_once(self):
        keys = collections.Counter((c["iso"], c["item"], c["field"]) for c in self.cells)
        self.assertEqual([k for k, n in keys.items() if n > 1], [])

    def test_the_register_cells_are_every_pair_not_established_as_absent(self):
        not_held = sum(r["status"] == "not_held" for r in self.rows)
        registers = [c for c in self.cells if c["kind"] == "holding" and c["field"] == "register"]
        self.assertEqual(len(registers), len(nd.countries()) * len(nd.RECORD_CLASSES) - not_held)
        self.assertEqual(sum(c["state"] == "filled" for c in registers),
                         sum(r["status"] == "held" for r in self.rows))

    def test_a_filled_field_is_one_the_register_has(self):
        rows = {(r["iso"], r["record_class"]): r for r in self.rows}
        for c in self.cells:
            if c["kind"] == "holding" and c["field"] != "register":
                value = rows[(c["iso"], c["item"])][c["field"]].strip()
                self.assertEqual(c["state"] == "filled", bool(value) and value != "unknown", c)

    def test_every_state_is_known_and_dry_means_two_passes(self):
        for c in self.cells:
            self.assertIn(c["state"], gaps.STATES)
            if c["state"] == "dry":
                self.assertGreaterEqual(int(c["passes"]), 2, c)
            if c["state"] == "searched_once":
                self.assertEqual(int(c["passes"]), 1, c)
            if c["state"] == "not_searched":
                self.assertEqual(int(c["passes"]), 0, c)


class Rule(unittest.TestCase):
    """The classification on hand-made inputs, each shown to flip on the one input it depends on."""

    def test_state(self):
        passes = collections.Counter({"a": 2, "b": 1, "c": 2})
        self.assertEqual(gaps.state("a", True, passes, set()), "filled")
        self.assertEqual(gaps.state("a", False, passes, set()), "dry")
        self.assertEqual(gaps.state("b", False, passes, set()), "searched_once")
        self.assertEqual(gaps.state("c", False, passes, {"c"}), "claimed_unverified")
        self.assertEqual(gaps.state("never", False, passes, set()), "not_searched")


class Page(unittest.TestCase):
    def test_the_committed_page_is_current(self):
        self.assertEqual((ROOT / "docs" / "gaps.md").read_text(encoding="utf-8"), gaps.render(gaps.cells()))


if __name__ == "__main__":
    unittest.main()
