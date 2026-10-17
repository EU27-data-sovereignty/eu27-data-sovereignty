#!/usr/bin/env python3
"""
The mobile release ledger (#114): generated from EAS, held in shape by `check`, and every row retraceable.

    python3 -m unittest tests.test_release -v
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import release  # noqa: E402

HEAD = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()


def build(**over) -> dict:
    base = {"id": "11111111-2222-3333-4444-555555555555", "platform": "IOS", "appVersion": "1.0.0",
            "appBuildVersion": "3", "runtimeVersion": "1.0.0", "channel": "production", "gitCommitHash": HEAD,
            "status": "FINISHED", "fingerprint": {"hash": "f" * 40}}
    base.update(over)
    return base


class Ledger(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "app.json").write_text(json.dumps({"expo": {"version": "1.0.0", "extra": {"eas": {"projectId": "a" * 8 + "-" + "b" * 4}}}}))
        self.ledger = self.tmp / "releases.csv"

    def test_the_committed_ledger_passes(self):
        results = release.check(ROOT / "mobile", ROOT / "mobile" / "releases.csv")
        self.assertTrue(all(ok for _, ok, _ in results), results)

    def test_a_row_is_what_a_reader_needs_to_retrace_a_build(self):
        row = release.row_from(build(), "e" * 64, "2026-10-16T00:00:00+00:00")
        self.assertEqual(list(row), release.COLUMNS)
        self.assertEqual(row["platform"], "ios")
        self.assertEqual(row["build_number"], "3")
        self.assertEqual(row["fingerprint"], "f" * 40)
        self.assertEqual(row["git_commit"], HEAD)
        self.assertEqual(row["status"], "finished")

    def test_check_refuses_a_commit_not_in_this_repository_and_a_version_behind_the_ledger(self):
        release.eas_build = lambda app_dir, build_id: build()  # type: ignore[assignment]
        self.assertEqual(release.record(ROOT / "mobile", self.ledger, build()["id"]), 0)
        rows = release.read_ledger(self.ledger)
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(rows[0]["edition_manifest_sha256"]), 64)
        # A second record of the same build changes nothing.
        self.assertEqual(release.record(ROOT / "mobile", self.ledger, build()["id"]), 0)
        self.assertEqual(len(release.read_ledger(self.ledger)), 1)
        ok = {name: ok for name, ok, _ in release.check(self.tmp, self.ledger)}
        self.assertTrue(all(ok.values()), ok)
        # The ledger edited by hand: a commit this repository does not have, and app.json behind it.
        text = self.ledger.read_text().replace(HEAD, "0" * 40).replace(",1.0.0,3,", ",9.0.0,3,")
        self.ledger.write_text(text)
        ok = {name: ok for name, ok, _ in release.check(self.tmp, self.ledger)}
        self.assertFalse(ok["commit 0000000 exists"])
        self.assertFalse(ok["app.json version is not behind the ledger"])

    def test_record_refuses_a_build_whose_commit_is_unknown(self):
        release.eas_build = lambda app_dir, build_id: build(gitCommitHash="0" * 40)  # type: ignore[assignment]
        self.assertEqual(release.record(ROOT / "mobile", self.ledger, "x"), 1)
        self.assertFalse(self.ledger.exists())


if __name__ == "__main__":
    unittest.main()
