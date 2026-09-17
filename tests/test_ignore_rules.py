#!/usr/bin/env python3
"""
The ignore rules that keep things out of git and off Vercel.

    python3 -m unittest discover -s tests -v

`.vercelignore` is read by the Vercel CLI *instead of* `.gitignore`, never in addition to
it, so every rule that matters has to exist in both files. That asymmetry has already cost
this repo once (#46: `cache/` would have uploaded the entire fetched corpus with the
source), and it is invisible in review -- a deploy that ships too much looks exactly like
one that does not.

These tests are the countermeasure `ROADMAP.md` prescribes for a documented rule the tree
can quietly stop matching: a check that fails the build, not a more carefully worded
sentence.
"""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITIGNORE = ROOT / ".gitignore"
VERCELIGNORE = ROOT / ".vercelignore"

# Named individuals, in the private repo checked out at contacts/ (#45, #46, #26). The
# nested .git is the real protection; these rules are the second layer, and the second
# layer is exactly the kind of thing that gets deleted in a tidy-up.
PERSONAL = ["**/contacts/", "*-contacts.md"]

# The Expo reader is local-only: no build, no store listing, no deploy.
MOBILE_GIT = ["mobile/node_modules/", "mobile/.expo/", "mobile/dist/", "mobile/.env.local"]


def rules(path: Path) -> list[str]:
    """Every non-comment, non-blank line, which is what the ignore files actually mean."""
    return [ln.strip() for ln in path.read_text().splitlines()
            if ln.strip() and not ln.lstrip().startswith("#")]


class Personal(unittest.TestCase):
    def test_contacts_rules_in_both_files(self):
        for path in (GITIGNORE, VERCELIGNORE):
            have = rules(path)
            for rule in PERSONAL:
                self.assertIn(rule, have, f"{path.name} lost `{rule}`; personal data could ship")


class Mobile(unittest.TestCase):
    def test_mobile_is_never_deployed(self):
        self.assertIn("mobile/", rules(VERCELIGNORE),
                      ".vercelignore must exclude mobile/: vercel.json builds web/ only")

    def test_mobile_build_output_is_not_committed(self):
        have = rules(GITIGNORE)
        for rule in MOBILE_GIT:
            self.assertIn(rule, have, f".gitignore lost `{rule}`")


class Cache(unittest.TestCase):
    def test_fetched_corpus_in_both_files(self):
        for path in (GITIGNORE, VERCELIGNORE):
            self.assertIn("cache/", rules(path), f"{path.name} lost `cache/` (#46)")


if __name__ == "__main__":
    unittest.main()
