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


class RecheckCheck(unittest.TestCase):
    """`recheck --check` fails only on a source that newly disputes its facts (#98)."""

    @staticmethod
    def rows(**outcomes):
        return {sid: {"source_id": sid, "outcome": o} for sid, o in outcomes.items()}

    def test_a_source_that_is_newly_gone_or_lost_a_quote_is_reported(self):
        before = self.rows(a="unchanged", b="changed_quotes_present")
        after = self.rows(a="gone", b="quote_vanished")
        self.assertEqual([r["source_id"] for r in research.new_disputes(before, after)], ["a", "b"])

    def test_a_source_already_disputed_in_the_committed_rows_is_not_new(self):
        before = self.rows(a="gone", b="quote_vanished")
        after = self.rows(a="quote_vanished", b="gone")
        self.assertEqual(research.new_disputes(before, after), [])

    def test_a_refusal_is_not_evidence_of_change(self):
        before = self.rows(a="unchanged")
        self.assertEqual(research.new_disputes(before, self.rows(a="unreachable")), [])

    def test_a_source_never_rechecked_before_counts_when_it_is_gone(self):
        self.assertEqual(len(research.new_disputes({}, self.rows(new="gone"))), 1)

    def test_the_cli_takes_check(self):
        import inspect
        self.assertIn("check", inspect.signature(research.recheck).parameters)
        self.assertIn("recheck(args.source, args.check)", inspect.getsource(research.main))


class ArchivedCopies(unittest.TestCase):
    def test_a_snapshot_of_the_same_url_is_accepted(self):
        self.assertTrue(research.snapshot_matches(
            "https://web.archive.org/web/20250626022512/https://www.mfa.bg/upload/x.pdf",
            "https://www.mfa.bg/upload/x.pdf"))

    def test_a_snapshot_with_userinfo_in_the_host_is_rejected(self):
        """It happened: the archive answered with .../https://crisis@mfa.bg/..., a different URL."""
        self.assertFalse(research.snapshot_matches(
            "https://web.archive.org/web/20250626022512/https://crisis@mfa.bg/upload/x.pdf",
            "https://www.mfa.bg/upload/x.pdf"))

    def test_a_snapshot_of_another_host_is_rejected(self):
        self.assertFalse(research.snapshot_matches(
            "https://web.archive.org/web/2025/https://example.org/x", "https://www.mfa.bg/x"))


class SourceIds(unittest.TestCase):
    def test_source_ids_satisfy_the_registry_grammar(self):
        import provenance
        for url in ("https://www.gesetze-im-internet.de/bmg/__1.html",
                    "https://example.gov.mt/Documents/Annual%20Report%202024.pdf"):
            self.assertRegex(research.source_id(url), provenance.SOURCE_ID)

    def test_the_same_url_always_gets_the_same_id(self):
        u = "https://www.rvig.nl/brp"
        self.assertEqual(research.source_id(u), research.source_id(u))


class Decoding(unittest.TestCase):
    """A page is read in the charset it declares (found 2026-09-30: 141 genuine quotes on ISO-8859-1
    pages could never match while every page was decoded as UTF-8)."""

    def test_a_latin1_page_keeps_its_accents(self):
        body = '<html><head><meta charset="iso-8859-1"></head><body>Lei da proteção de dados</body></html>'
        text = research.extract(body.encode("iso-8859-1"), "text/html")
        self.assertIn("proteção", text)
        self.assertEqual(research.match("Lei da proteção de dados pessoais", text + " pessoais"), "exact")

    def test_utf8_is_read_as_utf8(self):
        self.assertEqual(research.decode("Ελληνικά".encode("utf-8")), "Ελληνικά")

    def test_an_undeclared_legacy_page_falls_back_to_windows_1252(self):
        self.assertEqual(research.decode("Straße".encode("cp1252")), "Straße")


if __name__ == "__main__":
    unittest.main()
