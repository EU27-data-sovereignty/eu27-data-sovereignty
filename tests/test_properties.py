#!/usr/bin/env python3
"""
The evidence rules, tried on many generated inputs rather than a few chosen ones (#92).

    python3 -m unittest discover -s tests -v

Stdlib only: inputs come from `random.Random` with fixed seeds, so every run tries the same cases and a
failure reproduces. Each property is a rule the project's honesty rests on:
- a figure printed in one EU number format is found in a quote that writes it in another, and a changed
  digit never is (#82, value in quote);
- the fact hash changes when anything it covers changes, and only then (#87);
- no rule ever gives a fact to a checker that wrote it (#87);
- every state is placed in exactly one group, inside its own reported range (#77).
"""
from __future__ import annotations

import copy
import json
import random
import sys
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import evidence  # noqa: E402
import factcheck  # noqa: E402

CASES = 500


def eu_formats(value: Decimal, places: int) -> list[str]:
    """`value` as written across the EU: 1,234.5 · 1.234,5 · 1 234,5 · 1234.5 · 1234,5 (thin and normal
    spaces). Every one denotes the same number."""
    whole, _, frac = f"{value:.{places}f}".partition(".")
    groups = []
    while len(whole) > 3:
        groups.insert(0, whole[-3:])
        whole = whole[:-3]
    groups.insert(0, whole)
    out = []
    for thousands, decimal in ((",", "."), (".", ","), (" ", ","), (" ", ","), ("", "."), ("", ",")):
        out.append(thousands.join(groups) + (decimal + frac if frac else ""))
    return out


class ValueInQuote(unittest.TestCase):
    def test_a_figure_is_found_in_any_eu_format(self):
        rng = random.Random(82)
        for _ in range(CASES):
            places = rng.choice([0, 1, 2, 3])
            value = Decimal(rng.randint(1, 99_999_999)) / (10 ** places)
            printed = f"{value:,.{places}f}".replace(",", " ")       # how document.num prints
            for written in eu_formats(value, places):
                quote = f"Das Register enthielt {written} Einträge im Jahr 2024."
                with self.subTest(printed=printed, written=written):
                    self.assertTrue(evidence.value_in_quote(f"{printed} records", quote)["ok"])

    def test_a_changed_digit_is_never_found(self):
        rng = random.Random(83)
        for _ in range(CASES):
            value = rng.randint(1000, 99_999_999)
            other = value + rng.choice([1, 9, 10, 100, 1000])
            quote = f"Le registre contenait {value:,} dossiers.".replace(",", ".")
            with self.subTest(value=value, other=other):
                self.assertFalse(evidence.value_in_quote(f"{other:,} records".replace(",", " "), quote)["ok"])

    def test_a_number_only_in_the_translation_does_not_count(self):
        rng = random.Random(84)
        for _ in range(CASES // 5):
            n = rng.randint(10, 9999)
            quote = f"Rekisteri sisältää tietoja. [English: The register holds {n} entries.]"
            self.assertFalse(evidence.value_in_quote(f"{n} entries", quote)["ok"])


class FactHash(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bundle = json.loads(factcheck.BUNDLE.read_text(encoding="utf-8"))
        cls.facts = [f for f in factcheck.facts(bundle) if f["citations"]]

    def test_changing_any_covered_field_changes_the_hash(self):
        rng = random.Random(87)
        for _ in range(CASES):
            fact = rng.choice(self.facts)
            before = factcheck.fact_sha256(fact)
            changed = copy.deepcopy(fact)
            where = rng.choice(["claim", "what", "printed", "categorical", "citation"])
            if where == "citation":
                cite = rng.choice(changed["citations"])
                key = rng.choice(sorted(cite))
                cite[key] = f"{cite[key]}x"
            elif where == "categorical":
                changed["categorical"] = not changed["categorical"]
            else:
                changed[where] = f"{changed[where]}x"
            with self.subTest(claim=fact["claim"], where=where):
                self.assertNotEqual(factcheck.fact_sha256(changed), before)

    def test_fields_outside_the_fact_do_not_change_it(self):
        rng = random.Random(88)
        for _ in range(CASES // 5):
            fact = rng.choice(self.facts)
            extra = {**fact, "iso": "XX", "fact_sha256": "0" * 64, "author_model": "anyone"}
            self.assertEqual(factcheck.fact_sha256(extra), factcheck.fact_sha256(fact))


class Checker(unittest.TestCase):
    def test_no_author_set_gets_a_checker_that_wrote_it(self):
        rng = random.Random(89)
        pool = [*factcheck.CHECKERS.values(), "unrecorded", "person:a", "person:b",
                "program:fetch_eurostat.py", "claude-sonnet-5-5"]
        for _ in range(CASES):
            authors = set(rng.sample(pool, rng.randint(1, 4)))
            checker = factcheck.checker_for(authors)
            with self.subTest(authors=sorted(authors)):
                if checker:
                    self.assertNotIn(checker, authors)
                    self.assertEqual(factcheck.ineligible(checker, authors), "")
                else:
                    self.assertTrue(set(factcheck.CHECKERS.values()) <= authors)


class Placement(unittest.TestCase):
    def test_every_state_is_in_one_group_inside_its_own_range(self):
        bundle = json.loads(factcheck.BUNDLE.read_text(encoding="utf-8"))
        sov = bundle["sovereignty"]
        order = [g["id"] for g in sov["groups"]]
        for iso, p in sov["placements"].items():
            with self.subTest(iso=iso):
                self.assertIn(p["group"], order)
                lo, hi = order.index(p["range"][0]), order.index(p["range"][-1])
                self.assertLessEqual(min(lo, hi), order.index(p["group"]))
                self.assertLessEqual(order.index(p["group"]), max(lo, hi))


if __name__ == "__main__":
    unittest.main()
