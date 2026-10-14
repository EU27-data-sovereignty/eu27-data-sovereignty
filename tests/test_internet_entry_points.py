#!/usr/bin/env python3
"""
`INTERNET-ENTRY-POINTS.md` keeps its contract: the authored-note header, the Definitions, the 27 states in order,
the five columns, every row's Basis one of the allowed shapes citing the map's JSON or a PeeringDB page, a 'none'
row only alone, a Counts line under every table that is exactly what the rows give, every URL in the committed
link register, no ranking or size word, never rendered. The note is prose; these are the parts a build can refuse.

    python3 -m unittest tests.test_internet_entry_points -v
"""
from __future__ import annotations

import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import internet_entry_points_note as note  # noqa: E402
import national_ai_note as nai  # noqa: E402

D = "2026-10-14"
E1 = "https://www.submarinecablemap.com/api/v3/landing-point/sines-portugal.json"
E2 = "https://www.peeringdb.com/ix/26"
E3 = "https://likumi.lv/ta/id/353390"


def synthetic() -> str:
    """A well-formed note: every state with 'none' rows, except PT (one landing point, one planned), NL (one
    exchange) and LV (one statute row), each with the Counts line its table gives."""
    rows = {
        "PT": [["E1", "Sines, Portugal", "—", f"EllaLink, Medusa (planned, RFS 2026)", f"E1: {E1}, accessed {D}"],
               ["E2", "(none in PeeringDB)", "—", "—", f"none: searched {D}"]],
        "NL": [["E1", "(none on the map)", "—", "—", f"none: searched {D}"],
               ["E2", "AMS-IX", "Amsterdam", "https://www.ams-ix.net", f"E2: {E2}, accessed {D}"]],
        "LV": [["E1", "(none on the map)", "—", "—", f"none: searched {D}"],
               ["E2", "(none in PeeringDB)", "—", "—", f"none: searched {D}"],
               ["E3", "the single state internet exchange point", "—", "—", f"E3: {E3}, accessed {D}"]],
    }
    parts = [
        "# T\n\nAn authored note, 2026-10-14. Not generated. It ranks nothing: the order within a state is by Kind then Name.\n",
        "## Definitions\n",
        f"- E1: a landing point, per https://example.org/geo.json, accessed {D}.",
        f"- E2: an exchange, per https://example.org/ix, accessed {D}.",
        "- E3: a statute that names one, cited on the row.",
        "- Satellite gateways are out: no list exists that a row could cite.",
        "- Derived terms: no-landing, single-landing and single-exchange are counts, defined here. The owner asked for choke points; this note counts.\n",
    ]
    for iso in sorted(note.STATES, key=lambda i: note.STATES[i]):
        table = rows.get(iso, [["E1", "(none on the map)", "—", "—", f"none: searched {D}"],
                               ["E2", "(none in PeeringDB)", "—", "—", f"none: searched {D}"]])
        parts.append(f"## {note.STATES[iso]} ({iso})\n")
        parts.append("| " + " | ".join(note.COLUMNS) + " |")
        parts.append("|---|---|---|---|---|")
        parts.extend("| " + " | ".join(r) + " |" for r in table)
        parts.append("")
        parts.append(note.counts_line(table))
        parts.append("")
    parts.append("## Method\n\n- One bullet.\n")
    return "\n".join(parts)


GOOD = synthetic()


class TheNote(unittest.TestCase):
    """The committed note, as it is."""

    @classmethod
    def setUpClass(cls):
        cls.body = note.NOTE.read_text(encoding="utf-8")

    def test_the_note_holds_its_contract(self):
        probs, _ = note.problems(self.body)
        self.assertEqual(probs, [])

    def test_the_link_register_is_current(self):
        links = note.load_links()
        cited = set(nai.urls(self.body))
        self.assertEqual(cited - set(links), set(), "cited URLs missing from docs/internet-entry-points-links.csv")
        self.assertEqual(set(links) - cited, set(), "registered URLs no longer cited")

    def test_every_access_date_is_a_real_date_on_or_before_the_link_check(self):
        links = note.load_links()
        checked = max((r["checked"] for r in links.values()), default="9999-12-31")
        for d in set(nai.ACCESSED.findall(self.body)):
            self.assertRegex(d, r"^20\d\d-\d\d-\d\d$")
            self.assertLessEqual(d, checked, f"a row was accessed after the link register was written: {d}")

    def test_every_counts_line_is_what_its_table_gives(self):
        self.assertEqual(note.with_counts(self.body), self.body, "run `python3 model/internet_entry_points_note.py counts`")

    def test_no_row_cites_the_cable_map_html_pages(self):
        self.assertNotRegex(self.body, r"submarinecablemap\.com/(landing-point|submarine-cable)/[a-z0-9-]+(?!\.json)\b")

    def test_the_cited_decisions_exist(self):
        heads = {int(n) for n in re.findall(r"^### (\d+)\. ", (ROOT / "DECISIONS.md").read_text(), re.M)}
        for n in {int(m) for m in re.findall(r"(?<![\w#])#(\d{1,3})(?![0-9A-Za-z])", self.body)}:
            self.assertIn(n, heads, f"the note cites #{n}, which does not exist")

    def test_the_docs_test_lists_the_note_as_a_citing_file(self):
        self.assertIn('"INTERNET-ENTRY-POINTS.md"', (ROOT / "tests" / "test_docs.py").read_text())

    def test_the_gate_and_run_script_know_the_note(self):
        self.assertIn("python3 model/notes.py check", (ROOT / "test.sh").read_text())
        self.assertIn('"internet_entry_points_note.py"', (ROOT / "model" / "notes.py").read_text())
        self.assertIn("entry-points)", (ROOT / "run.sh").read_text())


class TheChecker(unittest.TestCase):
    """The checker refuses what the contract forbids, shown on a synthetic note in an empty root."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def problems(self, body: str, links: dict | None = None, registry: set | None = None) -> list[str]:
        saved, saved_reg = note.load_links, note.registry_urls
        try:
            note.load_links = lambda: links if links is not None else {
                u: {"url": u, "status": "200", "checked": D} for u in nai.urls(body)}
            note.registry_urls = lambda root: registry if registry is not None else {E3}
            return note.problems(body, root=self.root)[0]
        finally:
            note.load_links, note.registry_urls = saved, saved_reg

    def test_an_e1_row_filed_under_the_wrong_state_fails(self):
        body = GOOD.replace("| E1 | Sines, Portugal |", "| E1 | Sines, Spain |")
        self.assertTrue(any("label does not end with the state's name" in p for p in self.problems(body)))

    def test_an_e3_row_cites_only_a_registered_page(self):
        self.assertTrue(any("not in model/sources/registry.csv" in p for p in self.problems(GOOD, registry=set())))

    def test_an_unverified_e1_row_is_not_in_service(self):
        row = [["E1", "A, Portugal", "—", "X", "[unverified]"]]
        self.assertIn("E1 1 (in service 0, planned-only 0, unverified 1)", note.counts_line(row))
        self.assertIn("no-landing yes", note.counts_line(row))

    def test_a_plural_size_word_fails_and_a_quoted_phrase_is_not_scanned(self):
        self.assertTrue(any("'gateways'" in p for p in self.problems(GOOD.replace("- One bullet.", "- The gateways of Europe."))))
        self.assertEqual(self.problems(GOOD.replace("- One bullet.", '- The owner wrote "the key hubs".')), [])

    def test_a_well_formed_note_passes(self):
        self.assertEqual(self.problems(GOOD), [])

    def test_counts_is_idempotent_on_a_well_formed_note(self):
        self.assertEqual(note.with_counts(GOOD), GOOD)

    def test_counts_rewrites_a_hand_edited_line(self):
        body = GOOD.replace("Counts: E1 1 (in service 1", "Counts: E1 9 (in service 1")
        self.assertTrue(any("counts line is" in p for p in self.problems(body)))
        self.assertEqual(note.with_counts(body), GOOD)

    def test_counts_inserts_a_missing_line(self):
        body = re.sub(r"^Counts: E1 1 .*\n", "", GOOD, count=1, flags=re.M)
        self.assertTrue(any("0 Counts lines" in p for p in self.problems(body)))
        self.assertEqual(note.with_counts(body), GOOD)

    def test_the_derived_terms_follow_the_rows(self):
        self.assertIn("no-landing no; single-landing yes; single-exchange yes.", note.counts_line(
            [["E1", "A, Portugal", "—", "X", f"E1: {E1}, accessed {D}"]]))
        self.assertIn("E1 1 (in service 0, planned-only 1, unverified 0)", note.counts_line(
            [["E1", "A, Portugal", "—", "X (planned, RFS 2027)", f"E1: {E1}, accessed {D}"]]))
        self.assertIn("no-landing yes; single-landing no; single-exchange no.", note.counts_line(
            [["E2", "A", "B", "—", f"E2: {E2}, accessed {D}"], ["E2", "C", "B", "—", f"E2: {E2}, accessed {D}"]]))

    def test_a_missing_definition_fails(self):
        self.assertTrue(any("satellite" in p for p in self.problems(GOOD.replace("- Satellite", "- Orbital"))))

    def test_a_missing_header_token_fails(self):
        self.assertTrue(any("header" in p for p in self.problems(GOOD.replace("It ranks nothing", "It lists"))))

    def test_wrong_columns_fail(self):
        body = GOOD.replace("| Kind | Name | Place | Cables or website | Basis |", "| Kind | Name | City | Cables | Basis |")
        self.assertTrue(any("table columns" in p for p in self.problems(body)))

    def test_a_state_out_of_order_fails(self):
        body = GOOD.replace("## Austria (AT)", "## Austria (AT)\n\n| Kind | Name | Place | Cables or website | Basis |\n|---|---|---|---|---|\n"
                            f"| E1 | (none on the map) | — | — | none: searched {D} |\n"
                            f"| E2 | (none in PeeringDB) | — | — | none: searched {D} |\n\n"
                            + note.counts_line([]) + "\n\n## Sweden (SE)", 1)
        self.assertTrue(any("state headings" in p for p in self.problems(body)))

    def test_a_kind_and_basis_that_disagree_fail(self):
        body = GOOD.replace(f"| E2 | AMS-IX | Amsterdam | https://www.ams-ix.net | E2: {E2}", f"| E2 | AMS-IX | Amsterdam | https://www.ams-ix.net | E1: {E1}")
        self.assertTrue(any("E2 row with an E1 basis" in p for p in self.problems(body)))

    def test_the_cable_maps_html_page_is_refused(self):
        body = GOOD.replace(E1, "https://www.submarinecablemap.com/landing-point/sines-portugal")
        self.assertTrue(any("basis" in p and "sines-portugal" in p for p in self.problems(body)))

    def test_rows_out_of_order_fail(self):
        body = GOOD.replace(f"| E1 | Sines, Portugal | — | EllaLink, Medusa (planned, RFS 2026) | E1: {E1}, accessed {D} |\n"
                            f"| E2 | (none in PeeringDB) | — | — | none: searched {D} |",
                            f"| E2 | (none in PeeringDB) | — | — | none: searched {D} |\n"
                            f"| E1 | Sines, Portugal | — | EllaLink, Medusa (planned, RFS 2026) | E1: {E1}, accessed {D} |")
        self.assertTrue(any("not in order" in p for p in self.problems(body)))

    def test_a_none_row_beside_a_real_row_fails(self):
        body = GOOD.replace(f"| E2 | AMS-IX | Amsterdam | https://www.ams-ix.net | E2: {E2}, accessed {D} |",
                            f"| E2 | (none in PeeringDB) | — | — | none: searched {D} |\n"
                            f"| E2 | AMS-IX | Amsterdam | https://www.ams-ix.net | E2: {E2}, accessed {D} |")
        self.assertTrue(any("'none' row beside a real row" in p for p in self.problems(body)))

    def test_a_kind_with_neither_rows_nor_a_none_row_fails(self):
        body = GOOD.replace(f"| E1 | (none on the map) | — | — | none: searched {D} |\n| E2 | AMS-IX", "| E2 | AMS-IX")
        self.assertTrue(any("NL: E1: no row and no 'none' row" in p for p in self.problems(body)))

    def test_a_ranking_or_size_word_fails(self):
        self.assertTrue(any("ranking or size word 'largest'" in p for p in self.problems(GOOD.replace("- One bullet.", "- The largest one."))))
        self.assertTrue(any("in the place" in p for p in self.problems(GOOD.replace("| AMS-IX | Amsterdam |", "| AMS-IX | Amsterdam hub |"))))

    def test_a_derived_term_outside_definitions_fails(self):
        self.assertTrue(any("outside Definitions" in p for p in self.problems(GOOD.replace("- One bullet.", "- Malta is no-landing."))))

    def test_a_number_in_a_place_fails_and_a_verbatim_name_may_carry_one(self):
        self.assertTrue(any("a number in the place" in p for p in self.problems(GOOD.replace("| Amsterdam |", "| Amsterdam, 10 Gbit |"))))
        self.assertEqual(self.problems(GOOD.replace("| AMS-IX |", "| TOP-IX 2 MTU 9000 |")), [])

    def test_an_e1_row_without_cables_must_be_unverified(self):
        body = GOOD.replace("| EllaLink, Medusa (planned, RFS 2026) |", "| — |")
        self.assertTrue(any("names its cables" in p for p in self.problems(body)))
        marked = body.replace(f"E1: {E1}, accessed {D}", "[unverified]")
        self.assertFalse(any("names its cables" in p for p in self.problems(marked)))

    def test_an_unregistered_url_fails(self):
        self.assertTrue(any("not in internet-entry-points-links.csv" in p for p in self.problems(GOOD, links={})))

    def test_a_renderer_naming_the_note_fails(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "model").mkdir()
            (root / "model" / "document.py").write_text('open("INTERNET-ENTRY-POINTS.md")\n')
            self.assertEqual(note.renderers(root), ["model/document.py"])
            saved = note.load_links
            try:
                note.load_links = lambda: {u: {"url": u, "status": "200", "checked": D} for u in nai.urls(GOOD)}
                self.assertTrue(any("names the note" in p for p in note.problems(GOOD, root=root)[0]))
            finally:
                note.load_links = saved


if __name__ == "__main__":
    unittest.main()
