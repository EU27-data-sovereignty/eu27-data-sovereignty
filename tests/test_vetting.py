#!/usr/bin/env python3
"""
Source tiers (#83): what "a top-quality source" means, mechanically.

    python3 -m unittest discover -s tests -v

Every host the registry cites is classified once in model/sources/authorities.csv. These tests keep that
table complete and keep its judgements from drifting upward: an unofficial mirror of a statute is never
the statute, and an archived copy is only as good as what it archived.
"""
from __future__ import annotations

import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import evidence  # noqa: E402
import provenance  # noqa: E402

KINDS = {1: {"official_law_portal", "statistics_office", "eurostat_or_commission"},
         2: {"government_or_authority", "public_body", "audit_office"},
         3: {"company", "private_foundation", "chamber_of_commerce"},
         4: {"unofficial_law_mirror", "press", "encyclopedia"},
         0: {"archive_of_another_source"}}
# Commercial or community copies of national law. Useful to a reader; never the authoritative text.
MIRRORS = {"net.jogtar.hu", "zakonyprolidi.cz", "zakony.judikaty.info", "lawspot.gr", "zakon.hr", "cylaw.org",
           "etaamb.openjustice.be"}


class Authorities(unittest.TestCase):
    def setUp(self):
        with evidence.AUTHORITIES.open(newline="", encoding="utf-8") as fh:
            self.rows = list(csv.DictReader(fh))
        self.by_host = {r["host"]: r for r in self.rows}

    def test_every_cited_host_has_a_tier(self):
        reg = provenance.registry()
        missing = sorted({evidence.host(r["url"]) for r in reg.values()
                          if r["url"] and r["doc_type"] != "unused"} - set(self.by_host))
        self.assertEqual(missing, [], "classify these hosts in model/sources/authorities.csv")

    def test_hosts_are_unique_and_sorted(self):
        hosts = [r["host"] for r in self.rows]
        self.assertEqual(hosts, sorted(set(hosts)))

    def test_each_kind_sits_in_its_tier(self):
        for r in self.rows:
            self.assertIn(r["kind"], KINDS[int(r["tier"])], r["host"])

    def test_an_unofficial_mirror_is_never_top_tier(self):
        for h in MIRRORS:
            self.assertEqual(self.by_host[h]["tier"], "4", h)

    def test_an_archive_speaks_for_the_page_it_archived(self):
        self.assertEqual(evidence.host("https://web.archive.org/web/20260313205329/https://www.riigiteataja.ee/x"),
                         "riigiteataja.ee")

    def test_eurostat_is_top_tier_only_for_its_datasets(self):
        page = {"url": "https://ec.europa.eu/digital-strategy/x", "doc_type": "webpage"}
        data = {"url": "https://ec.europa.eu/eurostat/api/x", "doc_type": "dataset"}
        self.assertEqual(evidence.tier(data), (1, "eurostat"))
        self.assertEqual(evidence.tier(page), (3, "commission_page"))

    def test_a_mirror_backed_fact_cannot_be_strong(self):
        import json  # noqa: PLC0415
        bundle = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
        for claim, cites in bundle["claims"].items():
            for c in cites:
                if c["checks"]["tier"] > 2:
                    self.assertEqual(c["grade"], evidence.STANDARD, claim)


class Recheck(unittest.TestCase):
    """A source that changes after admission (research.py recheck, #83)."""

    @classmethod
    def setUpClass(cls):
        import document  # noqa: PLC0415
        cls.document = document
        cls.src = document.Sources()
        # A printed register fact backed by exactly one source, to force outcomes on.
        cls.claim, cls.text = next(
            (c, e["register"]) for iso, e in cls._held()
            for c in [f"record:{iso}:{e['record_class']}:register"]
            if len(cls.src.backing(c, e["register"])) == 1)
        cls.sid = cls.src.backing(cls.claim, cls.text)[0]["source_id"]

    @staticmethod
    def _held():
        import national_data as nd  # noqa: PLC0415
        return [(r["iso"], r) for r in nd.read_rows() if r["status"] == "held" and r["register"]]

    def with_outcome(self, outcome):
        saved = self.src.rechecked
        self.src.rechecked = {self.sid: {"outcome": outcome, "checked": "2026-10-01", "http_status": "404",
                                         "claims_missing": self.claim if outcome == "quote_vanished" else ""}}
        try:
            return self.src.fact(self.claim, self.text)
        finally:
            self.src.rechecked = saved

    def test_a_vanished_quote_is_disputed_never_a_fact(self):
        span = self.with_outcome("quote_vanished")
        self.assertEqual(span["role"], "disputed")
        self.assertEqual(span["c"], [self.claim])
        self.assertNotIn(self.text, span["t"])

    def test_a_quote_lost_by_another_fact_on_the_same_source_leaves_this_one_alone(self):
        saved = self.src.rechecked
        self.src.rechecked = {self.sid: {"outcome": "quote_vanished", "checked": "2026-10-01",
                                         "http_status": "200", "claims_missing": "record:XX:other:register"}}
        try:
            self.assertEqual(self.src.fact(self.claim, self.text)["role"], "fact")
        finally:
            self.src.rechecked = saved

    def test_a_source_that_is_gone_is_disputed(self):
        self.assertEqual(self.with_outcome("gone")["role"], "disputed")

    def test_a_refused_fetch_disputes_nothing(self):
        self.assertEqual(self.with_outcome("unreachable")["role"], "fact")

    def test_a_changed_page_that_still_holds_the_quote_stays_a_fact(self):
        self.assertEqual(self.with_outcome("changed_quotes_present")["role"], "fact")


class Admission(unittest.TestCase):
    """The rules vetting.py admits by (#83). The researcher's own label is never what decides."""

    @classmethod
    def setUpClass(cls):
        import vetting  # noqa: PLC0415
        cls.v = vetting

    def finding(self, claim, value, established, quote="Das Zentrale Melderegister enthält 9,1 Millionen Einträge",
                found=True):
        return {"claim": claim, "value": value, "quote": quote, "title": "",
                "review": {"quote_found": found, "established": established}}

    def test_a_reviewer_who_reached_the_same_figure_agrees(self):
        f = self.finding("record:AT:civil_registry:count", "9.1 million entries", "9,1 Millionen Einträge")
        self.assertFalse(self.v.agree(f))      # figure agrees, but no shared word: not the same reading
        f = self.finding("record:AT:civil_registry:count", "9.1 Millionen Einträge", "9,1 Millionen Einträge")
        self.assertTrue(self.v.agree(f))

    def test_a_different_figure_is_disagreement(self):
        f = self.finding("record:AT:civil_registry:count", "9.1 Millionen Einträge", "8,4 Millionen Einträge")
        self.assertFalse(self.v.agree(f))

    def test_a_reviewer_who_could_not_find_the_quote_never_agrees(self):
        f = self.finding("record:AT:civil_registry:register", "Zentrales Melderegister",
                         "Zentrales Melderegister", found=False)
        self.assertFalse(self.v.agree(f))

    def test_categorical_values_must_match_exactly(self):
        f = self.finding("indicator:AT:L1", "yes", "partial")
        self.assertFalse(self.v.agree(f))
        f = self.finding("indicator:AT:L1", "yes", "Yes")
        self.assertTrue(self.v.agree(f))

    def test_a_higher_tier_wins(self):
        mirror = {"url": "https://net.jogtar.hu/x", "doc_type": "statute", "published": ""}
        portal = {"url": "https://ris.bka.gv.at/y", "doc_type": "statute"}
        self.assertEqual(self.v.resolve(mirror, portal, ""), "higher_tier")

    def test_the_same_tier_from_another_authority_stays_disputed(self):
        agency = {"url": "https://www.bmi.gv.at/z", "doc_type": "webpage", "published": "2024-01"}
        other = {"url": "https://www.brz.gv.at/w", "doc_type": "webpage"}
        self.assertEqual(self.v.resolve(agency, other, "2026-05"), "")

    def test_the_same_authority_later_supersedes_only_with_both_dates(self):
        old = {"url": "https://www.bmi.gv.at/a", "doc_type": "webpage", "published": "2024-01"}
        new = {"url": "https://www.bmi.gv.at/b", "doc_type": "webpage"}
        self.assertEqual(self.v.resolve(old, new, "2026-03"), "later_same_authority")
        self.assertEqual(self.v.resolve({**old, "published": ""}, new, "2026-03"), "")
        self.assertEqual(self.v.resolve(old, new, "2023-12"), "")


class SameValue(unittest.TestCase):
    def test_two_different_registers_are_not_the_same_value(self):
        import vetting  # noqa: PLC0415
        f = {"claim": "record:AT:tax:register", "value": "FinanzOnline", "quote": "FinanzOnline ist das Portal", "title": ""}
        self.assertFalse(vetting.same_value("Zentrales Melderegister", f))
        self.assertTrue(vetting.same_value("FinanzOnline (tax portal)", f))


class AbsenceIsAFinding(unittest.TestCase):
    def test_a_source_that_a_register_exists_contradicts_an_admitted_absence(self):
        import vetting  # noqa: PLC0415
        f = {"claim": "record:AT:fingerprint_biometric:register", "value": "Erkennungsdienstliche Evidenz",
             "quote": "Die Erkennungsdienstliche Evidenz wird geführt", "title": ""}
        self.assertFalse(vetting.same_value("No central register", f))


if __name__ == "__main__":
    unittest.main()


class CorrectionRound(unittest.TestCase):
    """A later round (#93) is staged apart from the first run, per state, with its models and a closed
    vocabulary for categorical values."""

    def test_a_round_is_staged_per_state_with_its_models_and_vocabulary(self):
        import json  # noqa: PLC0415
        import tempfile  # noqa: PLC0415
        from unittest import mock  # noqa: PLC0415
        sys.path.insert(0, str(ROOT / "model"))
        import vetting  # noqa: PLC0415
        tmp = Path(tempfile.mkdtemp())
        out = tmp / "out.json"
        finding = {"claim": "indicator:HU:C1", "question": "q", "relation": "corrects", "url": "https://nisz.hu/x",
                   "quote": "q", "quote_english": "", "value": "Yes: the Government Data Centre runs",
                   "published": "", "title": "", "publisher": "", "doc_type": "official_page", "note": ""}
        out.write_text(json.dumps([{"iso": "W01", "research": {"findings": [finding, {**finding, "claim": "record:DE:x:register",
                                                                                          "value": "Melderegister"}],
                                                                 "outcomes": [], "researcher_model": "claude-opus-5-5"},
                                    "review": {"verdicts": [], "reviewer_model": "claude-opus-5-5"}}]))
        with mock.patch.object(vetting, "ROUNDS", tmp / "rounds"), mock.patch.object(vetting, "DIR", tmp):
            vetting.stage_round(out, "r1", "2026-10-02")
            hu = json.loads((tmp / "rounds" / "r1" / "HU.json").read_text())["findings"][0]
            de = json.loads((tmp / "rounds" / "r1" / "DE.json").read_text())["findings"][0]
            merged = vetting.staged()
        self.assertEqual((hu["value"], hu["value_as_written"]), ("yes", "Yes: the Government Data Centre runs"))
        self.assertEqual(hu["researcher_model"], "claude-opus-5-5")
        self.assertEqual(de["value"], "Melderegister")                       # free text is never rewritten
        self.assertNotIn("value_as_written", de)
        self.assertEqual(sorted(merged), ["DE", "HU"])
        self.assertFalse(list(tmp.glob("[A-Z][A-Z].json")))                   # the first run's files untouched


class Wave(unittest.TestCase):
    """A research wave (docs/vetting.md 3f): only the wave's gaps, each naming its register, no printed fact."""

    def test_the_hosting_wave_is_exactly_its_open_gaps(self):
        import gaps  # noqa: PLC0415
        import national_data as nd  # noqa: PLC0415
        sys.path.insert(0, str(ROOT / "model" / "research" / "vetting"))
        import build_input  # noqa: PLC0415
        states = build_input.wave("hosting")
        self.assertTrue(all(not s["facts"] for s in states))
        asked = {g["claim"] for s in states for g in s["gaps"]}
        expected = {c["claim"] for c in gaps.cells() if c["kind"] == "holding"
                    and c["field"] in ("hosting", "foreign_dependency") and c["state"] != "filled"}
        self.assertEqual(asked, expected)
        rows = {(r["iso"], r["record_class"]): r for r in nd.read_rows()}
        for s in states:
            for g in s["gaps"]:
                _, iso, cls, _ = g["claim"].split(":")
                self.assertEqual(rows[(iso, cls)]["status"], "held")
                self.assertIn(rows[(iso, cls)]["register"], g["what"])

    def test_the_unverified_wave_is_the_cheapest_gaps_and_keeps_the_review_blind(self):
        import gaps  # noqa: PLC0415
        sys.path.insert(0, str(ROOT / "model" / "research" / "vetting"))
        import build_input  # noqa: PLC0415
        states = build_input.wave("unverified")
        asked = {g["claim"]: g for s in states for g in s["gaps"]}
        self.assertEqual(set(asked), {c["claim"] for c in gaps.cells() if c["kind"] == "holding"
                                      and c["field"] == "register" and c["state"] == "claimed_unverified"})
        for g in asked.values():
            self.assertTrue(g["earlier"], g["claim"])
            for e in g["earlier"]:
                # The earlier value is a lead for the researcher only; the question the reviewer sees omits it.
                if e["value"]:
                    self.assertNotIn(e["value"], g["what"])

