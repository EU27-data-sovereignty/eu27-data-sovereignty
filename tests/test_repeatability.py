#!/usr/bin/env python3
"""
The process can be repeated by someone else, the same way (DECISIONS #84).

    python3 -m unittest discover -s tests -v

The /vet skill and docs/vetting.md name commands; every one must exist. Each agent run leaves a manifest
that says what went in and what came out. The register check itself (admission reproduces the committed
registers) is a stage of ./test.sh, `./run.sh admit --check`.
"""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUN_SH = (ROOT / "run.sh").read_text(encoding="utf-8")
SKILL = (ROOT / ".claude" / "skills" / "vet" / "SKILL.md").read_text(encoding="utf-8")
RUNBOOK = (ROOT / "docs" / "vetting.md").read_text(encoding="utf-8")
VETTING = (ROOT / "model" / "vetting.py").read_text(encoding="utf-8")


class Commands(unittest.TestCase):
    def test_every_run_sh_command_the_skill_and_runbook_name_exists(self):
        named = set(re.findall(r"\./run\.sh ([a-z]+)", SKILL + RUNBOOK))
        cases = set(re.findall(r"^    ([a-z|:]+)\)", RUN_SH, re.M))
        known = {c for group in cases for c in group.split("|")}
        self.assertEqual(sorted(named - known), [])

    def test_every_vet_subcommand_named_exists_in_vetting_py(self):
        named = set(re.findall(r"\./run\.sh vet ([a-z]+)", SKILL + RUNBOOK))
        choices = set(re.findall(r'"([a-z]+)"', re.search(r"choices=\[([^\]]+)\]", VETTING).group(1)))
        self.assertEqual(sorted(named - choices), [])

    def test_the_skill_runs_the_checked_in_workflow(self):
        self.assertIn("scriptPath: model/research/vetting/workflow.js", SKILL)
        self.assertTrue((ROOT / "model" / "research" / "vetting" / "workflow.js").exists())

    def test_the_skill_never_pushes_on_its_own(self):
        self.assertIn("Never push without the", SKILL)


class Manifests(unittest.TestCase):
    FIELDS = {"run", "input_sha256", "output_sha256", "workflow_sha256", "built_from_commit",
              "reviewer_model", "tools", "findings", "outcomes"}

    def test_every_manifest_says_what_went_in_and_came_out(self):
        for path in sorted((ROOT / "model" / "research" / "vetting" / "runs").glob("*.json")):
            doc = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(sorted(self.FIELDS - set(doc)), [], path.name)
            self.assertRegex(doc["workflow_sha256"], r"^[0-9a-f]{64}$", path.name)
            self.assertRegex(doc["output_sha256"], r"^[0-9a-f]{64}$", path.name)


class TestingDoc(unittest.TestCase):
    """docs/testing.md lists every suite (#92); a new test file not listed there fails here."""

    def test_every_python_test_module_is_listed(self):
        doc = (ROOT / "docs" / "testing.md").read_text(encoding="utf-8")
        missing = [p.stem for p in sorted((ROOT / "tests").glob("test_*.py")) if p.stem not in doc]
        self.assertEqual(missing, [])

    def test_every_workflow_is_listed(self):
        doc = (ROOT / "docs" / "testing.md").read_text(encoding="utf-8")
        for wf in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
            if wf.name in ("security.yml",):     # the shared security workflow, documented in DEPLOYMENT.md
                continue
            self.assertIn(wf.name, doc, wf.name)


class Pins(unittest.TestCase):
    def test_eurostat_pins_are_data_with_a_decision(self):
        import csv  # noqa: PLC0415
        rows = list(csv.DictReader((ROOT / "model" / "eurostat_pins.csv").open(encoding="utf-8")))
        self.assertEqual(len(rows), 6)
        for r in rows:
            self.assertRegex(r["decision"], r"^#\d+$", r["column"])
            self.assertRegex(r["adopted"], r"^\d{4}-\d{2}-\d{2}$", r["column"])


if __name__ == "__main__":
    unittest.main()
