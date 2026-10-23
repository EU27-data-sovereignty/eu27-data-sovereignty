#!/usr/bin/env python3
"""
`DRAGHI-REPORT.md` keeps its contract (#118): every quotation of the report is a row of the generated quote register,
found on its page of the hashed PDF; every fact about a state is a claim id the committed bundle prints, with the text
it prints; one entry per state in a fixed template; no ranking language or currency figure outside a quotation; never
rendered. The PDFs are gitignored, so these tests run offline against the manifest and the register; `check` re-finds
every quotation in the PDFs too wherever they are on disk.

    python3 -m unittest tests.test_draghi_note -v
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import draghi_note as note  # noqa: E402


class TheNote(unittest.TestCase):
    """The committed note, register and manifest, as they are."""

    @classmethod
    def setUpClass(cls):
        cls.body = note.text()

    def test_the_note_holds_its_contract(self):
        self.assertEqual(note.problems(self.body), [])

    def test_every_state_has_an_entry_in_english_name_order(self):
        self.assertEqual([e["iso"] for e in note.entries(self.body)],
                         sorted(note.STATES, key=lambda i: note.STATES[i]))

    def test_the_quote_register_is_generated_from_the_note(self):
        cited = {(m.group(2), m.group(3), note.norm(m.group(1))) for m in note.CITED.finditer(self.body)}
        rows = {(r["part"], r["page"], note.norm(r["quote"])) for r in note.load_quotes()}
        self.assertEqual(cited, rows, "run `python3 model/draghi_note.py quotes`")

    def test_every_quotation_was_found_in_the_manifest_s_file(self):
        manifest = note.load_manifest()
        for r in note.load_quotes():
            self.assertEqual(r["found"], "yes", r["quote"][:60])
            self.assertEqual(r["pdf_sha256"], manifest[note.PARTS[r["part"]]["file"]]["sha256"])

    def test_the_manifest_pins_both_parts_to_the_commission_s_urls(self):
        manifest = note.load_manifest()
        self.assertEqual(sorted(manifest), sorted(p["file"] for p in note.PARTS.values()))
        for row in manifest.values():
            self.assertRegex(row["sha256"], r"^[0-9a-f]{64}$")
            self.assertTrue(row["url"].startswith("https://commission.europa.eu/document/download/"), row["url"])
            self.assertEqual(row["content_type"], "application/pdf")

    def test_the_link_register_is_current(self):
        links = note.load_links(note.LINKS)
        self.assertEqual(set(note.urls(self.body)), set(links))

    def test_the_cited_decisions_exist(self):
        heads = {int(n) for n in re.findall(r"^### (\d+)\. ", (ROOT / "DECISIONS.md").read_text(), re.M)}
        for n in {int(m) for m in re.findall(r"(?<![\w#])#(\d{1,3})(?![0-9A-Za-z])", self.body)}:
            self.assertIn(n, heads, f"the note cites #{n}, which does not exist")

    def test_the_docs_test_lists_the_note_as_a_citing_file(self):
        self.assertIn('"DRAGHI-REPORT.md"', (ROOT / "tests" / "test_docs.py").read_text())


class TheChecker(unittest.TestCase):
    """The checker refuses what the contract forbids, shown on a synthetic note."""

    QUOTE = "A single EU-wide policy for public administrations’ procurement of cloud service"
    CLAIMS = {f"indicator:{i}:C1": ["Yes"] for i in note.STATES}

    @classmethod
    def entry(cls, iso: str, name: str) -> str:
        return (f"### {name} ({iso})\n\n#### Where Draghi names it\nnone: searched both parts 2026-10-23.\n\n"
                f"#### Proposals that land on its holdings\nAnalysis.\n\n"
                f"#### What the project prints today\n- `indicator:{iso}:C1` reads “Yes”.\n\n#### Open questions\n- None.\n\n")

    @classmethod
    def build(cls) -> str:
        body = ("# T\n\nAuthored note. Not generated. See #118. It ranks nothing.\n\n---\n\n## 1. The report\n\n"
                f"## 2. What it says about hosting state data\n\n“{cls.QUOTE}” (B p. 84).\n\n"
                "## 3. What it means for this project\n\n## 4. The twenty-seven\n\n")
        for iso in sorted(note.STATES, key=lambda i: note.STATES[i]):
            body += cls.entry(iso, note.STATES[iso])
        return body + "## 5. Caveats\n"

    def problems(self, body: str) -> list[str]:
        quotes = [{"part": "B", "page": "84", "quote": self.QUOTE, "found": "yes", "pdf_sha256": ""}]
        return [p for p in note.problems(body, quotes=quotes, claims=self.CLAIMS, links={})
                if "MANIFEST" not in p and "manifest" not in p and "names the note" not in p]

    def test_a_well_formed_note_passes(self):
        self.assertEqual(self.problems(self.build()), [])

    def test_a_missing_state_fails(self):
        body = self.build().replace(self.entry("MT", "Malta"), "")
        self.assertTrue(any("27 states" in p for p in self.problems(body)))

    def test_a_quotation_outside_the_register_fails(self):
        body = self.build().replace("(B p. 84).", "(B p. 85).", 1)
        self.assertTrue(any("not in draghi-quotes.csv" in p for p in self.problems(body)))

    def test_a_long_quotation_with_no_page_fails(self):
        body = self.build().replace("## 3. What", "“an unsourced sentence that reads like a quotation of the report” here.\n\n## 3. What")
        self.assertTrue(any("neither a page nor a claim id" in p for p in self.problems(body)))

    def test_a_claim_text_that_drifted_from_the_bundle_fails(self):
        body = self.build().replace("`indicator:NL:C1` reads “Yes”", "`indicator:NL:C1` reads “No”")
        self.assertTrue(any("but the bundle prints" in p for p in self.problems(body)))

    def test_a_withheld_or_unknown_claim_fails(self):
        body = self.build().replace("`indicator:NL:C1` reads “Yes”", "`indicator:NL:C2` reads “Yes”")
        self.assertTrue(any("does not print as a fact" in p for p in self.problems(body)))

    def test_another_state_s_claim_fails(self):
        body = self.build().replace("`indicator:NL:C1` reads “Yes”", "`indicator:DE:C1` reads “Yes”")
        self.assertTrue(any("another state's claim" in p for p in self.problems(body)))

    def test_an_entry_without_a_claim_fails(self):
        body = self.build().replace("- `indicator:NL:C1` reads “Yes”.", "- Nothing.")
        self.assertTrue(any("cites no claim id" in p for p in self.problems(body)))

    def test_a_currency_figure_in_an_entry_fails(self):
        body = self.build().replace("### Netherlands (NL)\n\n#### Where Draghi names it\nnone: searched both parts 2026-10-23.\n\n"
                                    "#### Proposals that land on its holdings\nAnalysis.",
                                    "### Netherlands (NL)\n\n#### Where Draghi names it\nnone: searched both parts 2026-10-23.\n\n"
                                    "#### Proposals that land on its holdings\nIt would cost EUR 40 million.")
        self.assertTrue(any("currency figure" in p for p in self.problems(body)))

    def test_ranking_language_fails_outside_a_quotation_only(self):
        body = self.build().replace("## 5. Caveats", "It is ranked first.\n\n## 5. Caveats")
        self.assertTrue(any("ranking language" in p for p in self.problems(body)))
        quoted = self.build().replace("## 5. Caveats", "As written, “are in the top ten worldwide”.\n\n## 5. Caveats")
        self.assertFalse(any("ranking language" in p for p in self.problems(quoted)))

    def test_an_empty_names_it_subsection_fails(self):
        body = self.build().replace("### Malta (MT)\n\n#### Where Draghi names it\nnone: searched both parts 2026-10-23.",
                                    "### Malta (MT)\n\n#### Where Draghi names it\nSomewhere.")
        self.assertTrue(any("MT: 'Where Draghi names it'" in p for p in self.problems(body)))


if __name__ == "__main__":
    unittest.main()
