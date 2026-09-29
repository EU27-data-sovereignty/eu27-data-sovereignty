#!/usr/bin/env python3
"""
The quote check that decides whether a researched claim is admitted (model/research.py, #75).

    python3 -m unittest discover -s tests -v

Normalising too little rejects true quotes (PDF extraction breaks lines and hyphenates words,
HTML swaps quote marks); normalising too much admits paraphrase. These tests pin the line:
typography may differ, words may not.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import research  # noqa: E402

PAGE = ("<html><head><script>var x = 'Das Melderegister wird';</script></head><body>"
        "<p>Die Meldebeh&ouml;rden f&uuml;hren das „Melderegister“ auf Grundlage des "
        "Bundesmeldegesetzes&nbsp;(BMG).</p></body></html>").encode()


class Matching(unittest.TestCase):
    def text(self):
        return research.extract(PAGE, "text/html")

    def test_verbatim_quote_is_exact(self):
        self.assertEqual(research.match("Die Meldebehörden führen das \"Melderegister\" auf Grundlage",
                                        self.text()), "exact")

    def test_script_text_is_not_evidence(self):
        self.assertNotIn("wird", self.text())

    def test_paraphrase_is_not_found(self):
        self.assertEqual(research.match("Die Meldebehörden verwalten das Melderegister nach dem BMG",
                                        self.text()), "not_found")

    def test_punctuation_only_difference_is_loose_not_exact(self):
        self.assertEqual(research.match("Melderegister auf Grundlage des Bundesmeldegesetzes BMG",
                                        self.text()), "loose")

    def test_pdf_line_break_hyphenation_is_rejoined(self):
        pdf_text = "The Land Registry is kept by the Cadas-\ntral Office under the Act of 2009."
        self.assertEqual(research.match("kept by the Cadastral Office under the Act of 2009",
                                        pdf_text), "exact")

    def test_a_quote_too_short_to_be_evidence_is_refused(self):
        self.assertEqual(research.match("BMG", self.text()), "too_short")


class SourceIds(unittest.TestCase):
    def test_source_ids_satisfy_the_registry_grammar(self):
        import provenance
        for url in ("https://www.gesetze-im-internet.de/bmg/__1.html",
                    "https://example.gov.mt/Documents/Annual%20Report%202024.pdf"):
            self.assertRegex(research.source_id(url), provenance.SOURCE_ID)

    def test_the_same_url_always_gets_the_same_id(self):
        u = "https://www.rvig.nl/brp"
        self.assertEqual(research.source_id(u), research.source_id(u))


if __name__ == "__main__":
    unittest.main()
