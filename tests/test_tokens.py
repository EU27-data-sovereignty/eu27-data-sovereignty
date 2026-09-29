#!/usr/bin/env python3
"""
The design tokens: one source, generated everywhere, contrast-checked (DECISIONS.md #74, #76).

    python3 -m unittest discover -s tests -v

`design/tokens.json` is the only place a colour is defined. The web CSS, the typst tokens and
the mobile theme are generated from it; editing one of them by hand is exactly the drift that
left four unrelated palettes in this repo. These tests fail when a generated file no longer
matches the source, or when a palette change drops a text pair below WCAG AA.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "design"))
import build_tokens  # noqa: E402


class Tokens(unittest.TestCase):
    def test_generated_files_are_fresh(self):
        r = subprocess.run([sys.executable, str(ROOT / "design" / "build_tokens.py"), "--check"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_contrast_pairs_pass(self):
        tokens = json.loads((ROOT / "design" / "tokens.json").read_text())
        self.assertEqual(build_tokens.check_contrast(tokens), [])

    def test_no_emblem_in_any_template(self):
        """#76: EU colours, never the circle of stars."""
        for path in (ROOT / "book" / "templates").glob("*.typ"):
            self.assertNotRegex(path.read_text(), re.compile(r"_star|eu-stars|polygon\("),
                                f"{path.name} draws a star shape")

    def test_no_hex_colours_in_web_components(self):
        """Components use role tokens; a hex outside tokens.css is a palette fork."""
        offenders = []
        for path in (ROOT / "web" / "src").rglob("*.tsx"):
            for n, line in enumerate(path.read_text().splitlines(), 1):
                if re.search(r"\[#[0-9a-fA-F]{3,8}\]", line):
                    offenders.append(f"{path.relative_to(ROOT)}:{n}")
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
