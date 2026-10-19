#!/usr/bin/env python3
"""
The register of authored notes and agent drafts, and the one gate stage that checks them all.

    python3 model/notes.py check     # every registered checker, one line each; exit 1 if any fails
    python3 model/notes.py list      # what is registered

An authored note (the national-AI strategies, the sovereign appliance, the technical universities) or an
agent draft set (the language drafts, and the catalogue admitted from them) is prose or staging the model never renders, held to a contract its own checker
enforces. Each checker is a module under model/ with a `check` subcommand. Registering it here is what
puts it in the gate: test.sh runs this file once, so a new note adds a line here, not a stage there,
and tests/test_notes.py fails if a checker module exists that is not registered.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# module -> what it holds to its contract. Order is the order the lines print in the gate.
CHECKERS: dict[str, str] = {
    "national_ai_note.py": "the national-AI note (#103)",
    "sovereign_appliance_note.py": "the sovereign-appliance note (#104)",
    "i18n_drafts.py": "the language drafts (docs/plans/localisation-plan.md)",
    "i18n.py": "the admitted interface catalogue (#117)",
    "technical_universities_note.py": "the technical-universities note",
}


def check() -> int:
    failed = []
    for module, what in CHECKERS.items():
        r = subprocess.run([sys.executable, str(ROOT / "model" / module), "check"],
                           capture_output=True, text=True)
        lines = r.stdout.strip().splitlines() or [""]
        # Each checker prints its counts on one line and then its problems, one per line; find the counts line.
        headline = next((l for l in lines if "problems" in l), lines[-1])
        mark = "ok  " if r.returncode == 0 else "FAIL"
        print(f"  {mark} {what}: {headline.strip()}")
        if r.returncode != 0:
            failed.append(module)
            rest = [l for l in lines if l is not headline]
            if rest:
                print("\n".join("       " + line for line in rest[:20]))
            if r.stderr.strip():
                print("\n".join("       " + line for line in r.stderr.strip().splitlines()[-5:]))
    return 1 if failed else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        sys.exit(check())
    elif cmd == "list":
        for module, what in CHECKERS.items():
            print(f"{module}\t{what}")
    else:
        print(__doc__)
        sys.exit(2)
