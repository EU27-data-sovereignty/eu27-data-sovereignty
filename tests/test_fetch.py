#!/usr/bin/env python3
"""
The fetch manifest, model/fetch_manifest.csv, and the Eurostat pull.

    python3 -m unittest discover -s tests -v

The cache itself is gitignored and rebuildable, so these tests must pass on a fresh clone
that has none of it -- which is exactly what CI is. They therefore assert things that are
true with or without the bytes on disk: the manifest is well-formed and sorted, a row that
claims a successful fetch carries a hash, and any cached file that *is* present still
matches the hash recorded for it.

That last one is the point of the manifest (#52, the same pattern as countries/ARTEFACTS.csv).
A source document that changed under us is the failure the whole verification workstream
exists to catch; silently re-reading the new bytes would hide it.
"""
from __future__ import annotations

import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import fetch  # noqa: E402
import fetch_eurostat  # noqa: E402
import sources  # noqa: E402


class Manifest(unittest.TestCase):
    def test_manifest_agrees_with_whatever_is_cached(self):
        self.assertEqual(fetch.verify(), [])

    def test_rows_are_sorted(self):
        rows = fetch.load_manifest()
        order = [fetch.sort_key(r) for r in rows]
        self.assertEqual(order, sorted(order), "sort the manifest so diffs stay readable")

    def test_a_successful_fetch_records_a_hash(self):
        for r in fetch.load_manifest():
            if r["http_status"] == "200":
                self.assertTrue(r["sha256"], f"{r['iso']}/{r['key']} fetched 200 but has no sha256")
                self.assertNotEqual(r["bytes"], "0", f"{r['iso']}/{r['key']} fetched 200 but is empty")

    def test_failures_are_recorded_rather_than_omitted(self):
        """A blocked gazette must appear as a row with its status, not vanish.

        Seven of the 27 national sources refuse automated requests (SOURCES.md). If a
        failure were simply dropped, it would be indistinguishable from work not yet done,
        which is the distinction the manifest exists to preserve.
        """
        for r in fetch.load_manifest():
            self.assertTrue(r["http_status"], f"{r['iso']}/{r['key']} has no recorded status")


class EurostatPull(unittest.TestCase):
    """The pull is a tracked output, so it is checked even though the cache is not."""

    def setUp(self):
        path = ROOT / "model" / "eurostat_pull.csv"
        if not path.exists():
            self.skipTest("no eurostat_pull.csv yet; run ./run.sh fetch eurostat")
        with path.open(newline="", encoding="utf-8") as fh:
            self.rows = list(csv.DictReader(fh))

    def test_every_country_and_column_is_present(self):
        isos, columns = set(sources.countries()), set(fetch_eurostat.SERIES)
        got = {(r["iso"], r["column"]) for r in self.rows}
        missing = {(i, c) for i in isos for c in columns} - got
        self.assertEqual(missing, set(), "the pull is incomplete")

    def test_every_value_carries_its_provenance(self):
        """A figure without a dataset code and a period is not more verifiable than before."""
        for r in self.rows:
            where = f"{r['iso']}/{r['column']}"
            self.assertTrue(r["dataset"], f"{where}: no dataset code")
            self.assertTrue(r["period"], f"{where}: no period")
            self.assertTrue(r["updated"], f"{where}: no dataset vintage")
            self.assertRegex(r["retrieved"], r"^\d{4}-\d{2}-\d{2}$", f"{where}: bad retrieval date")
            float(r["value"])  # raises if it is not a number

    def test_one_period_per_column(self):
        """All 27 come from the same period, or the column is quietly mixing vintages."""
        by_column: dict[str, set[str]] = {}
        for r in self.rows:
            by_column.setdefault(r["column"], set()).add(r["period"])
        for column, periods in by_column.items():
            self.assertEqual(len(periods), 1, f"{column} mixes periods {sorted(periods)}")


class EurostatProvenance(unittest.TestCase):
    """Does each Eurostat column actually reproduce from the source it claims?

    This is the check that caught the one real defect. `eu27_parameters.csv` describes six
    columns as Eurostat figures; five reproduce from their pinned dataset and period almost
    exactly, and `gov_employment_k` reproduces from no period at all.
    """

    # Ordinary Eurostat revision between the pull and the commit. Anything larger means the
    # cell did not come from where it says it did.
    TOLERANCE_PCT = 0.5

    # gov_employment_k was excluded here as a known defect until 2026-09-30: 9 of 27 values matched no
    # year of nama_10_a64_e NACE O (Sweden 40% out). It was rebuilt from the official 2024 series
    # (DECISIONS #84), so every column is held to its pinned source now.
    KNOWN_BAD: set[str] = set()

    def setUp(self):
        path = ROOT / "model" / "eurostat_pull.csv"
        if not path.exists():
            self.skipTest("no eurostat_pull.csv yet; run ./run.sh fetch eurostat")
        with path.open(newline="", encoding="utf-8") as fh:
            self.rows = list(csv.DictReader(fh))

    def test_sound_columns_reproduce_from_their_pinned_source(self):
        off = []
        for r in self.rows:
            if r["column"] in self.KNOWN_BAD:
                continue
            cur, new = float(r["current"]), float(r["value"])
            if cur and abs(new - cur) / abs(cur) * 100 > self.TOLERANCE_PCT:
                off.append(f"{r['iso']}/{r['column']}: csv {cur} vs {r['dataset']}@{r['period']} {new}")
        self.assertEqual(off, [], "these cells do not reproduce from the source they claim")

    def test_no_column_is_tolerated_as_a_known_defect(self):
        """A drifting column fails the test above; it is never silently tolerated."""
        self.assertEqual(self.KNOWN_BAD, set())      # none since #84; a new one needs a recorded reason

    def test_every_column_is_pinned_to_a_period(self):
        for column, spec in fetch_eurostat.SERIES.items():
            self.assertEqual(len(spec), 5, f"{column}: expected a pinned period in its spec")
            self.assertTrue(spec[4], f"{column}: period pin is empty")


if __name__ == "__main__":
    unittest.main()
