"""The PDFs are typeset by typst and CI has no typst, so their source is gated here instead.

These tests do not compile anything. They import the renderers and assert on the *typst source*
they emit, which needs only the JSON bundle -- so they run everywhere `unittest discover` does,
including CI.

A country flag emoji must never reach a PDF: typst can only reach those glyphs through Apple Color
Emoji, so the same source would render flags here and empty boxes on Linux, silently. And every
fact in a typeset document must arrive with its footnote (#75).
"""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "book"))

import build as book  # noqa: E402
import report  # noqa: E402

BUNDLE = ROOT / "web" / "public" / "data" / "eu27.json"

# U+1F1E6..U+1F1FF REGIONAL INDICATOR SYMBOL LETTER A..Z -- flag emoji are pairs of these.
REGIONAL_INDICATORS = range(0x1F1E6, 0x1F200)


def flag_chars(text: str) -> list[str]:
    return [c for c in text if ord(c) in REGIONAL_INDICATORS]


class Typeset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not BUNDLE.exists():
            raise unittest.SkipTest("run ./run.sh data first")
        cls.bundle = json.loads(BUNDLE.read_text(encoding="utf-8"))
        cls.report = report.report_typ(cls.bundle)

    def test_no_flag_emoji_in_the_report_or_any_country_pdf(self):
        self.assertEqual(flag_chars(self.report), [])
        for iso in sorted(self.bundle["documents"]):
            with self.subTest(iso=iso):
                self.assertEqual(flag_chars(report.country_typ(self.bundle, iso)), [])

    def test_no_flag_emoji_in_the_book(self):
        self.assertEqual(flag_chars(book.assemble(sorted(book.AUTHORED), "2026-01-01")), [])

    def test_every_country_chapter_head_carries_its_name_and_iso(self):
        for iso, d in sorted(self.bundle["documents"].items()):
            with self.subTest(iso=iso):
                self.assertIn(f"\n= {d['name']} ({iso})\n", self.report)

    def test_every_footnote_points_at_an_appendix_entry(self):
        """#75: a footnote's [Sn] link must land on a source listed in the appendix."""
        for text in (self.report, report.country_typ(self.bundle, "NL")):
            linked = set(re.findall(r"#link\(<src-(\d+)>\)", text))
            listed = set(re.findall(r"\] <src-(\d+)>", text))
            self.assertTrue(linked)
            self.assertEqual(linked - listed, set())

    def test_every_fact_span_gets_a_footnote(self):
        """One footnote per distinct citation (source, locator, date) of every fact span: a fact
        that rests on three documents shows all three."""
        expected = 0
        # The EU-27 overview (#95) follows the ranking and footnotes its facts like the country chapters.
        for d in [self.bundle["infrastructure"], *self.bundle["documents"].values()]:
            for s in report.document_spans(d):
                if s.get("role") == "fact":
                    cites = {(c["source_id"], c["locator"], c["retrieved"])
                             for claim in s["c"] for c in self.bundle["claims"].get(claim, [])}
                    self.assertTrue(cites, s["t"][:60])
                    expected += len(cites)
        body = self.report.split("= Data-sovereignty ranking", 1)[1]
        ranking, chapters = body.split("\n= ", 1)
        self.assertEqual(chapters.count("#footnote["), expected)


if __name__ == "__main__":
    unittest.main()
