#!/usr/bin/env python3
"""
`SOVEREIGN-APPLIANCE.md` keeps its contract (#104): the authored-note header, the named sections, no ranking
language, no currency figure, member states named only in Precedents and Sources and there only with a source,
every URL in the committed link register, never rendered. The note is prose; these are the parts a build can refuse.

    python3 -m unittest tests.test_sovereign_appliance -v
"""
from __future__ import annotations

import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import sovereign_appliance_note as note  # noqa: E402

GOOD = """# T

Authored note. Not generated. The exception is #59; #104 records it. It ranks nothing.

---

## Contents

- [Precedents](#precedents)

## The idea

A box in a cage, filled before demand. The host supplies power and a port.

## Precedents

One state's agreement (https://example.org/a, accessed 2026-10-12) says the premises are inviolable.

- Estonia provides nothing; the text is quoted (https://example.org/a, accessed 2026-10-12).

## Caveats

1. Nothing here is sourced to the project's standard.

## Status and next steps

| Step | State |
|---|---|
| Drafted | done |

## Sources

- Gazette: https://example.org/a (accessed 2026-10-12)
"""


class TheNote(unittest.TestCase):
    """The committed note, as it is."""

    @classmethod
    def setUpClass(cls):
        cls.body = note.text()

    def test_the_note_holds_its_contract(self):
        self.assertEqual(note.problems(self.body), [])

    def test_the_link_register_is_current(self):
        links = note.load_links()
        cited = set(note.nai.urls(self.body))
        self.assertEqual(cited - set(links), set(), "cited URLs missing from docs/sovereign-appliance-links.csv")
        self.assertEqual(set(links) - cited, set(), "registered URLs no longer cited")

    def test_every_access_date_is_a_real_date_on_or_before_the_link_check(self):
        links = note.load_links()
        checked = max((r["checked"] for r in links.values()), default="9999-12-31")
        for d in set(note.nai.ACCESSED.findall(self.body)):
            self.assertRegex(d, r"^20\d\d-\d\d-\d\d$")
            self.assertLessEqual(d, checked, f"a claim was accessed after the link register was written: {d}")

    def test_the_cited_decisions_exist(self):
        heads = {int(n) for n in re.findall(r"^### (\d+)\. ", (ROOT / "DECISIONS.md").read_text(), re.M)}
        for n in {int(m) for m in re.findall(r"(?<![\w#])#(\d{1,3})(?![0-9A-Za-z])", self.body)}:
            self.assertIn(n, heads, f"the note cites #{n}, which does not exist")

    def test_the_docs_test_lists_the_note_as_a_citing_file(self):
        self.assertIn('"SOVEREIGN-APPLIANCE.md"', (ROOT / "tests" / "test_docs.py").read_text())

    def test_the_gate_and_run_script_know_the_note(self):
        # The gate runs every registered note checker through model/notes.py, one stage for all of them.
        self.assertIn("python3 model/notes.py check", (ROOT / "test.sh").read_text())
        self.assertIn('"sovereign_appliance_note.py"', (ROOT / "model" / "notes.py").read_text())
        self.assertIn("appliance)", (ROOT / "run.sh").read_text())


class TheChecker(unittest.TestCase):
    """The checker refuses what the contract forbids, shown on a synthetic note in an empty root."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def problems(self, body: str, status: str = "200") -> list[str]:
        saved = note.load_links
        try:
            note.load_links = lambda: {u: {"url": u, "status": status, "checked": "2026-10-12"}
                                       for u in note.nai.urls(body)}
            return note.problems(body, root=self.root)
        finally:
            note.load_links = saved

    def test_a_well_formed_note_passes(self):
        self.assertEqual(self.problems(GOOD), [])

    def test_a_header_without_the_decision_fails(self):
        self.assertTrue(any("header" in p for p in self.problems(GOOD.replace("#104 records it", "nothing records it"))))

    def test_a_missing_section_fails(self):
        self.assertTrue(any("missing section: ## Caveats" in p for p in self.problems(GOOD.replace("## Caveats", "## Notes"))))

    def test_ranking_language_fails(self):
        body = GOOD.replace("filled before demand", "filled ahead of demand")
        self.assertTrue(any("ranking language" in p for p in self.problems(body)))

    def test_a_currency_figure_fails(self):
        body = GOOD.replace("The host supplies power and a port.", "The host charges €5 million.")
        self.assertTrue(any("currency figure" in p for p in self.problems(body)))

    def test_a_state_named_outside_the_allowed_sections_fails(self):
        body = GOOD.replace("A box in a cage", "A box in a cage in Estonian hands")
        self.assertTrue(any("names a member state ('Estonian')" in p for p in self.problems(body)))

    def test_a_state_named_in_precedents_needs_a_source_in_the_same_unit(self):
        body = GOOD.replace("- Estonia provides nothing; the text is quoted (https://example.org/a, accessed 2026-10-12).",
                            "- Estonia provides nothing; the text is quoted.")
        self.assertTrue(any("names a state without a URL" in p for p in self.problems(body)))
        marked = body.replace("- Estonia provides nothing; the text is quoted.",
                              "- Estonia provides nothing; the text is quoted **[unverified]**.")
        self.assertEqual(self.problems(marked), [])

    def test_a_dead_link_must_be_marked_unverified(self):
        self.assertTrue(any("answered 404" in p for p in self.problems(GOOD, status="404")))
        marked = GOOD.replace("accessed 2026-10-12)", "accessed 2026-10-12) **[unverified]**")
        self.assertFalse(any("answered 404" in p for p in self.problems(marked, status="404")))

    def test_an_unregistered_url_fails(self):
        saved = note.load_links
        try:
            note.load_links = lambda: {}
            self.assertTrue(any("not in sovereign-appliance-links.csv" in p for p in note.problems(GOOD, root=self.root)))
        finally:
            note.load_links = saved

    def test_a_renderer_naming_the_note_fails(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "model").mkdir()
            (root / "model" / "render.py").write_text('open("SOVEREIGN-APPLIANCE.md")\n')
            self.assertEqual(note.renderers(root), ["model/render.py"])
            saved = note.load_links
            try:
                note.load_links = lambda: {u: {"url": u, "status": "200", "checked": "2026-10-12"} for u in note.nai.urls(GOOD)}
                self.assertTrue(any("reads the note" in p for p in note.problems(GOOD, root=root)))
            finally:
                note.load_links = saved


if __name__ == "__main__":
    unittest.main()
