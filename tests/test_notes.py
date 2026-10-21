#!/usr/bin/env python3
"""
model/notes.py is the register of authored notes and agent drafts: every `model/*_note.py` checker and the
drafts checker is registered, every registered module exists, and the one test.sh stage runs the register.

    python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "model"))

import notes  # noqa: E402


class Registry(unittest.TestCase):
    def test_every_note_checker_is_registered(self):
        on_disk = sorted(p.name for p in (ROOT / "model").glob("*_note.py")) + ["i18n_drafts.py", "i18n_site.py"]
        self.assertEqual(sorted(set(on_disk)), sorted(notes.CHECKERS),
                         "a checker exists that the gate never runs, or the register names a module that is gone")

    def test_every_registered_module_exists(self):
        for module in notes.CHECKERS:
            self.assertTrue((ROOT / "model" / module).exists(), module)

    def test_the_gate_runs_the_register_once(self):
        test_sh = (ROOT / "test.sh").read_text(encoding="utf-8")
        self.assertEqual(test_sh.count("python3 model/notes.py check"), 1)
        for module in notes.CHECKERS:
            self.assertNotIn(f"model/{module} check", test_sh, f"{module} runs through the register, not its own stage")


if __name__ == "__main__":
    unittest.main()
