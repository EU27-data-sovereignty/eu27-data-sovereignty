#!/usr/bin/env python3
"""
The corpus /ask answers from (model/ask_corpus.py, DECISIONS.md #78).

    python3 -m unittest discover -s tests -v

/ask must not be able to say anything the site would not. These tests pin that: every claim in
the corpus resolves to a supported citation, every fact the site shows is in the corpus, and the
file is regenerated whenever the bundle changes.
"""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))
import ask_corpus  # noqa: E402
import document  # noqa: E402

BUNDLE = json.loads((ROOT / "web" / "public" / "data" / "eu27.json").read_text(encoding="utf-8"))
CORPUS = ask_corpus.build(BUNDLE)


class Corpus(unittest.TestCase):
    def test_the_committed_corpus_is_fresh(self):
        r = subprocess.run([sys.executable, str(ROOT / "model" / "ask_corpus.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_every_claim_resolves_to_a_supported_citation(self):
        src = document.Sources()
        for d in CORPUS["documents"]:
            for b in d["blocks"]:
                for claim in b["claims"]:
                    with self.subTest(claim=claim):
                        self.assertIn(claim, BUNDLE["claims"])
                        self.assertTrue(src.supported(claim))

    def test_a_fact_block_always_carries_its_claims(self):
        for d in CORPUS["documents"]:
            for b in d["blocks"]:
                if b["kind"] == "fact":
                    self.assertTrue(b["claims"], b["text"][:80])

    def test_every_fact_the_site_shows_is_in_the_corpus(self):
        in_corpus = {c for d in CORPUS["documents"] for b in d["blocks"] for c in b["claims"]}
        shown = {c for doc in BUNDLE["documents"].values()
                 for c in document.claims_used(doc)}
        self.assertEqual(shown - in_corpus, set())

    def test_no_block_carries_a_numeric_sovereignty_score(self):
        text = json.dumps(CORPUS)
        self.assertNotIn('"score"', text)

    def test_every_country_has_its_own_document(self):
        titles = {d.get("iso") for d in CORPUS["documents"]}
        self.assertEqual(set(BUNDLE["documents"]) - titles, set())


if __name__ == "__main__":
    unittest.main()
