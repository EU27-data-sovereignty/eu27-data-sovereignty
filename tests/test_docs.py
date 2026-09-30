#!/usr/bin/env python3
"""
Documentation integrity: the decision register and the references into it.

    python3 -m unittest discover -s tests -v

`ROADMAP.md` names the pattern these tests exist to break: "a document asserts a rule,
the tree quietly stops matching it, and nothing complains", and concludes that the
countermeasure is a check that fails the build, not a more carefully written sentence.

The concrete failure being guarded here: DECISIONS.md carried two entries numbered 38,
two numbered 39, two numbered 40 and two numbered 41 for three days. `README.md` cited
"#41" meaning "no generated PDF is ever committed" while `ROADMAP.md` cited "#41" meaning
the domain choice, and both were right, which is the worst way for a reference to be
wrong. Renumbered to 47-50 on 2026-09-08; see #54.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECISIONS = ROOT / "DECISIONS.md"

HEADING = re.compile(r"^### (\d+)\. ", re.M)
# `#41` but not the `#898781` of a hex colour: one or two digits, then a non-word char.
REFERENCE = re.compile(r"(?<![\w#])#(\d{1,2})(?![0-9A-Za-z])")

# Files that cite decisions by number. Country briefs are generated and cite none.
CITING = ["README.md", "ROADMAP.md", "PROGRESS.md", "CHANGELOG.md", "ASSETS.md", "OUTREACH.md",
          "FEASIBILITY-RANKING.md", "DISTRIBUTION-AND-TRUST.md", "VERIFICATION.md", "DEPLOYMENT.md",
          "METHOD.md", "CLAUDE.md", "TODO.md", "artifacts/STYLE.md", "model/research/README.md",
          "SOURCES.md", "DECISIONS.md", ".gitignore",
          "model/README.md", "book/README.md",
          # The representation style guides are the working form of the rules this register
          # holds the reasoning for, so they cite heavily. A guide citing a decision that does
          # not exist is exactly the drift this test was written to catch.
          "artifacts/README.md", "artifacts/markdown/STYLE.md", "artifacts/html/STYLE.md",
          "artifacts/pdf/STYLE.md", "artifacts/png/STYLE.md", "artifacts/mobile/STYLE.md"]


def numbers() -> list[int]:
    return [int(n) for n in HEADING.findall(DECISIONS.read_text())]


class Register(unittest.TestCase):
    def test_numbers_are_unique(self):
        seen, dupes = set(), []
        for n in numbers():
            (dupes.append(n) if n in seen else None)
            seen.add(n)
        self.assertEqual(dupes, [], "two decisions share a number; every reference to it is ambiguous")

    def test_numbers_are_contiguous_from_one(self):
        ns = numbers()
        self.assertEqual(sorted(ns), list(range(1, len(ns) + 1)), "a decision number is missing or skipped")


class References(unittest.TestCase):
    def test_every_cited_decision_exists(self):
        known = set(numbers())
        dangling = []
        for name in CITING:
            f = ROOT / name
            if not f.is_file():
                continue
            for n in {int(m) for m in REFERENCE.findall(f.read_text())}:
                if n not in known:
                    dangling.append(f"{name} cites #{n}")
        self.assertEqual(dangling, [], "a document points at a decision that does not exist")


class EntryStructure(unittest.TestCase):
    """From #72 on, an entry must say what was chosen, why, and why not each alternative
    (README.md § How decisions are recorded). A decision without its rejected options cannot be
    reopened honestly: nobody can tell whether the alternative was weighed or never seen."""

    FIRST = 72
    PARTS = ("**Decision.**", "**Problem.**", "**Alternatives considered.**", "*Why not:*",
             "**Closes off.**", "**Verified:**", "*Would change if:*")

    def test_entries_from_72_have_every_part(self):
        text = DECISIONS.read_text()
        heads = list(HEADING.finditer(text))
        missing = []
        for i, h in enumerate(heads):
            n = int(h.group(1))
            if n < self.FIRST:
                continue
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            body = text[h.start():end]
            missing += [f"#{n} lacks {part}" for part in self.PARTS if part not in body]
        self.assertEqual(missing, [], "a decision entry is missing a required part")


if __name__ == "__main__":
    unittest.main()
