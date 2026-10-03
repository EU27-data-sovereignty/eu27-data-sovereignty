#!/usr/bin/env python3
"""
The evidence rules under Hypothesis (#92): generated inputs that shrink to the smallest failing case.

    python3 -m pip install --require-hashes -r requirements-dev.txt
    python3 -m unittest tests.test_hypothesis -v

`tests/test_properties.py` checks the same rules with seeded stdlib generators and always runs; this adds
Hypothesis's search and shrinking where it is installed (CI). Without it, the tests skip and say so.
"""
from __future__ import annotations

import sys
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import evidence  # noqa: E402
import factcheck  # noqa: E402

try:
    from hypothesis import given, settings, strategies as st
except ImportError:                                    # pragma: no cover
    given = None

SEPARATORS = [(",", "."), (".", ","), (" ", ","), (" ", ","), ("", "."), ("", ",")]


def written(value: int, places: int, thousands: str, decimal: str) -> str:
    whole, frac = divmod(value, 10 ** places) if places else (value, 0)
    groups = f"{whole:,}".split(",")
    return thousands.join(groups) + (f"{decimal}{frac:0{places}d}" if places else "")


@unittest.skipIf(given is None, "hypothesis is not installed (pip install --require-hashes -r requirements-dev.txt)")
class Rules(unittest.TestCase):
    if given is not None:
        @settings(max_examples=400, deadline=None)
        @given(st.integers(1, 10**9), st.sampled_from([0, 1, 2, 3]), st.sampled_from(SEPARATORS))
        def test_a_figure_is_found_in_any_eu_format(self, value, places, sep):
            printed = written(value, places, " ", ".")
            quote = f"Il registro contiene {written(value, places, *sep)} voci."
            self.assertTrue(evidence.value_in_quote(f"{printed} entries", quote)["ok"], (printed, quote))

        @settings(max_examples=400, deadline=None)
        @given(st.integers(1000, 10**9), st.integers(1, 10**6))
        def test_a_different_figure_is_never_found(self, value, delta):
            quote = f"Das Register enthält {written(value, 0, '.', ',')} Einträge."
            other = written(value + delta, 0, " ", ".")
            self.assertFalse(evidence.value_in_quote(f"{other} entries", quote)["ok"], (other, quote))

        @settings(max_examples=300, deadline=None)
        @given(st.sets(st.sampled_from([*factcheck.CHECKERS.values(), "unrecorded", "person:a",
                                        "program:fetch_eurostat.py", "claude-sonnet-5-5"]), min_size=1))
        def test_no_author_set_gets_a_checker_that_wrote_it(self, authors):
            checker = factcheck.checker_for(authors)
            if checker:
                self.assertNotIn(checker, authors)
            else:
                self.assertTrue(set(factcheck.CHECKERS.values()) <= authors)

        @settings(max_examples=300, deadline=None)
        @given(st.text(min_size=1, max_size=40), st.text(min_size=1, max_size=40))
        def test_the_fact_hash_separates_any_two_printed_texts(self, a, b):
            base = {"claim": "record:XX:tax:register", "what": "q", "categorical": False, "citations": []}
            same = factcheck.fact_sha256({**base, "printed": a}) == factcheck.fact_sha256({**base, "printed": b})
            self.assertEqual(same, a == b)


if __name__ == "__main__":
    unittest.main()
