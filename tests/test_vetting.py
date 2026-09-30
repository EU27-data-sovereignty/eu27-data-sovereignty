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
MIRRORS = {"net.jogtar.hu", "zakonyprolidi.cz", "zakony.judikaty.info", "lawspot.gr", "zakon.hr"}


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


if __name__ == "__main__":
    unittest.main()
