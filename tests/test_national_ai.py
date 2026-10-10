#!/usr/bin/env python3
"""
`NATIONAL-AI-STRATEGIES.md` keeps its contract (#101): one entry per state in a fixed template, every snapshot
cell sourced or marked unverified, every URL in the committed link register, no ranking language, no cost in a
strategy, never rendered. The note is prose; these are the parts of it a build can refuse.

    python3 -m unittest tests.test_national_ai -v
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import national_ai_note as note  # noqa: E402


class TheNote(unittest.TestCase):
    """The committed note, as it is."""

    @classmethod
    def setUpClass(cls):
        cls.body = note.text()

    def test_the_note_holds_its_contract(self):
        self.assertEqual(note.problems(self.body), [])

    def test_every_state_has_an_entry_in_english_name_order(self):
        names = note.states()
        isos = [e["iso"] for e in note.entries(self.body)]
        self.assertEqual(isos, [i for i, _ in sorted(names.items(), key=lambda kv: kv[1])])

    def test_the_link_register_is_current(self):
        links = note.load_links()
        cited = set(note.urls(self.body))
        self.assertEqual(cited - set(links), set(), "cited URLs missing from docs/national-ai-strategies-links.csv")
        self.assertEqual(set(links) - cited, set(), "registered URLs no longer cited")

    def test_every_access_date_is_a_real_date_on_or_before_the_link_check(self):
        links = note.load_links()
        checked = max((r["checked"] for r in links.values()), default="9999-12-31")
        for d in set(note.ACCESSED.findall(self.body)):
            self.assertRegex(d, r"^20\d\d-\d\d-\d\d$")
            self.assertLessEqual(d, checked, f"a claim was accessed after the link register was written: {d}")

    def test_the_cited_decisions_exist(self):
        heads = {int(n) for n in re.findall(r"^### (\d+)\. ", (ROOT / "DECISIONS.md").read_text(), re.M)}
        for n in {int(m) for m in re.findall(r"(?<![\w#])#(\d{1,3})(?![0-9A-Za-z])", self.body)}:
            self.assertIn(n, heads, f"the note cites #{n}, which does not exist")

    def test_the_docs_test_lists_the_note_as_a_citing_file(self):
        self.assertIn('"NATIONAL-AI-STRATEGIES.md"', (ROOT / "tests" / "test_docs.py").read_text())


class TheChecker(unittest.TestCase):
    """The checker refuses what the contract forbids, shown on a synthetic note."""

    @classmethod
    def setUpClass(cls):
        cls.names = note.states()
        cls.good = cls.build()

    @classmethod
    def entry(cls, iso: str, name: str, *, strategy="Take R1 with the national corpus.", src="(https://example.org/x, accessed 2026-10-10)",
              extra="") -> str:
        rows = "\n".join(f"| {f} | finding | {src} |" for f in note.SNAPSHOT_FIELDS)
        return (f"### {name} ({iso})\n\n#### Snapshot\n| Field | Finding | Source |\n|---|---|---|\n{rows}\n\n"
                f"#### What good enough means here\nText.\n\n#### Recommended strategy\n{strategy}\n\n"
                f"#### What it does not need to do\nText.\n\n#### Main blocker, and what would change the recommendation\nText.{extra}\n\n"
                f"#### Sources\n- a (https://example.org/x, accessed 2026-10-10)\n- b (https://example.org/y, accessed 2026-10-10)\n"
                f"- c (https://example.org/z, accessed 2026-10-10)\n\n")

    @classmethod
    def build(cls) -> str:
        ordered = sorted(cls.names.items(), key=lambda kv: kv[1])
        body = ("# T\n\nAuthored note. Not generated. See #101. It ranks nothing.\n\n---\n\n## 2. The routes\n\nR1 **[reconstructed]**\n\n"
                "## 3. The building blocks\n\n## 5. The twenty-seven\n\n")
        for iso, name in ordered:
            body += cls.entry(iso, name)
        groups = "| R1 | " + ", ".join(f"{n} ({i})" for i, n in ordered) + " |"
        body += f"## 6. Across the EU-27\n\nThe groups below are a recommendation and not a ranking.\n\n| Route | States |\n|---|---|\n{groups}\n\n## 7. Caveats\n"
        return body

    def problems(self, body: str) -> list[str]:
        saved = note.load_links
        try:
            note.load_links = lambda: {u: {"url": u, "status": "200", "checked": "2026-10-10"} for u in note.urls(body)}
            return [p for p in note.problems(body) if "reads the note" not in p]
        finally:
            note.load_links = saved

    def test_a_well_formed_note_passes(self):
        self.assertEqual(self.problems(self.good), [])

    def test_a_missing_state_fails(self):
        body = self.good.replace(self.entry("MT", "Malta"), "")
        self.assertTrue(any("27 states" in p for p in self.problems(body)))

    def test_a_missing_snapshot_row_fails(self):
        body = self.good.replace("| Power and grid | finding | (https://example.org/x, accessed 2026-10-10) |\n", "", 1)
        self.assertTrue(any("snapshot lacks the row 'Power and grid'" in p for p in self.problems(body)))

    def test_an_unsourced_cell_fails_unless_marked(self):
        body = self.good.replace("| Key institutions | finding | (https://example.org/x, accessed 2026-10-10) |",
                                 "| Key institutions | finding | |", 1)
        self.assertTrue(any("neither a URL" in p for p in self.problems(body)))
        marked = body.replace("| Key institutions | finding | |", "| Key institutions | finding **[unverified]** | |", 1)
        self.assertEqual(self.problems(marked), [])

    def test_a_cost_in_a_strategy_fails(self):
        body = self.good.replace("Take R1 with the national corpus.", "Spend €50 million on R1.", 1)
        self.assertTrue(any("currency figure" in p for p in self.problems(body)))

    def test_ranking_language_fails(self):
        body = self.good.replace("#### What it does not need to do\nText.", "#### What it does not need to do\nIt is ranked first.", 1)
        self.assertTrue(any("ranking language" in p for p in self.problems(body)))

    def test_a_reconstructed_mark_in_an_entry_fails(self):
        body = self.good.replace("#### What it does not need to do\nText.", "#### What it does not need to do\nAbout **[reconstructed]** a year.", 1)
        self.assertTrue(any("[reconstructed]" in p for p in self.problems(body)))

    def test_a_dead_link_must_be_marked_unverified(self):
        saved = note.load_links
        try:
            note.load_links = lambda: {u: {"url": u, "status": "404" if u.endswith("/z") else "200", "checked": "2026-10-10"}
                                       for u in note.urls(self.good)}
            self.assertTrue(any("answered 404" in p for p in note.problems(self.good)))
            marked = self.good.replace("- c (https://example.org/z, accessed 2026-10-10)", "- c **[unverified]** (https://example.org/z, accessed 2026-10-10)")
            self.assertFalse(any("answered 404" in p for p in note.problems(marked)))
        finally:
            note.load_links = saved

    def test_a_group_out_of_alphabetical_order_fails(self):
        ordered = sorted(self.names.items(), key=lambda kv: kv[1])
        good_row = "| R1 | " + ", ".join(f"{n} ({i})" for i, n in ordered) + " |"
        bad_row = "| R1 | " + ", ".join(f"{n} ({i})" for i, n in reversed(ordered)) + " |"
        self.assertTrue(any("not alphabetical" in p for p in self.problems(self.good.replace(good_row, bad_row))))


if __name__ == "__main__":
    unittest.main()
