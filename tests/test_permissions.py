#!/usr/bin/env python3
"""
.claude/settings.json (#106): the assistant may push to main in exact forms and nothing else outward.

    python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETTINGS = json.loads((ROOT / ".claude" / "settings.json").read_text(encoding="utf-8"))
ALLOW = SETTINGS["permissions"]["allow"]
DENY = SETTINGS["permissions"]["deny"]


class Allow(unittest.TestCase):
    def test_every_allow_is_an_exact_push_to_origin_main(self):
        for rule in ALLOW:
            self.assertRegex(rule, r"^Bash\(git push origin (?:main|[A-Za-z0-9._/-]+:main)\)$",
                             f"{rule}: only an exact push of a named ref to origin main may be allowed (#106)")
            self.assertNotIn("*", rule, f"{rule}: a wildcard can match a delete (:main) or a force push (+ref:main)")

    def test_nothing_allowed_is_a_delete_or_a_force_push(self):
        for rule in ALLOW:
            inner = rule[len("Bash("):-1]
            self.assertNotRegex(inner, r" :main$|\+|--force|(?:^| )-f(?: |$)")


class Deny(unittest.TestCase):
    def test_the_outward_actions_are_denied_by_prefix(self):
        wanted = ["Bash(git push origin :main)", "Bash(git push origin +*)", "Bash(git push origin --force*)",
                  "Bash(git push --force*)", "Bash(git push origin --delete:*)", "Bash(vercel deploy --prod:*)",
                  "Bash(gh repo edit:*)", "Bash(gh api -X:*)", "Bash(gh api --method:*)"]
        for rule in wanted:
            self.assertIn(rule, DENY, f"{rule} must stay denied (#106)")

    def test_no_deny_is_also_allowed(self):
        self.assertEqual(sorted(set(ALLOW) & set(DENY)), [])


if __name__ == "__main__":
    unittest.main()
