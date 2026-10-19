#!/usr/bin/env python3
"""
The language drafts (docs/i18n/drafts/, docs/plans/localisation-plan.md) are agent output: complete,
cross-reviewed by a different agent, and rendered nowhere.

    python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import i18n_drafts  # noqa: E402


class Contract(unittest.TestCase):
    def test_every_state_has_a_complete_cross_reviewed_draft(self):
        out = io.StringIO()
        with redirect_stdout(out):
            rc = i18n_drafts.check()
        self.assertEqual(rc, 0, out.getvalue())

    def test_a_draft_is_reviewed_by_the_other_agent_on_the_other_model(self):
        keys, states = i18n_drafts.spec()
        for iso in states:
            text = (i18n_drafts.DRAFTS / f"{iso}.md").read_text(encoding="utf-8")
            drafted = i18n_drafts._field(text, "Drafted by")
            reviewed = i18n_drafts._field(text, "Reviewed by")
            d_model = drafted.split(",")[1].strip() if "," in drafted else ""
            r_model = reviewed.split(",")[1].strip() if "," in reviewed else ""
            self.assertTrue(d_model and r_model, f"{iso}: model ids missing")
            self.assertNotEqual(d_model, r_model, f"{iso}: drafted and reviewed on the same model")


class NeverRendered(unittest.TestCase):
    """No renderer, exporter or corpus may read the drafts until the plan's decision is written."""

    READERS = ["model/document.py", "model/export_json.py", "model/generate_countries.py", "model/ask_corpus.py",
               "book", "web/src", "api", "mobile/src", "mobile/app"]

    def test_nothing_reads_the_drafts(self):
        hits = []
        for rel in self.READERS:
            p = ROOT / rel
            files = [p] if p.is_file() else [f for f in p.rglob("*") if f.suffix in {".py", ".ts", ".tsx", ".typ"}]
            for f in files:
                try:
                    t = f.read_text(encoding="utf-8")
                except (UnicodeDecodeError, OSError):
                    continue
                if "i18n/drafts" in t or "docs/i18n" in t:
                    hits.append(str(f.relative_to(ROOT)))
        self.assertEqual(hits, [], "the language drafts are staging, never rendered")


if __name__ == "__main__":
    unittest.main()
