#!/usr/bin/env python3
"""
The GitHub Actions workflows, and the deploy workflow in particular (#81).

    python3 -m unittest discover -s tests -v

Since #81 a push to main ships production from CI, so the workflows are part of the supply
chain of the live site. Two rules from the workspace policy are checked here, because a
sentence in a policy doc does not fail a build: actions are pinned by commit SHA, and a
downloaded binary is checked against a checksum. Stdlib only, so the YAML is read as text.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = sorted((ROOT / ".github" / "workflows").glob("*.yml"))
DEPLOY = (ROOT / ".github" / "workflows" / "deploy.yml").read_text()

USES = re.compile(r"^\s*(?:-\s*)?uses:\s*(\S+)", re.M)
SHA = re.compile(r"@[0-9a-f]{40}$")
# The owner's own reusable workflows are tracked at @main by design (security-reusable.yml).
OWN_REUSABLE = "pieteradejong/dotfiles/.github/workflows/"


class Pinning(unittest.TestCase):
    def test_every_action_is_pinned_by_sha(self):
        loose = [f"{wf.name}: {ref}" for wf in WORKFLOWS for ref in USES.findall(wf.read_text())
                 if not SHA.search(ref) and not ref.startswith(OWN_REUSABLE)]
        self.assertEqual(loose, [], "a tag can be moved under us; pin actions by commit SHA")

    def test_vercel_cli_is_an_exact_version(self):
        self.assertRegex(DEPLOY, r"VERCEL_CLI: vercel@\d+\.\d+\.\d+\n")


class Deploy(unittest.TestCase):
    def test_typst_download_is_checksummed(self):
        self.assertRegex(DEPLOY, r"TYPST_SHA256: [0-9a-f]{64}\n")
        self.assertIn("sha256sum -c", DEPLOY)

    def test_upload_is_prebuilt(self):
        # A remote build has no typst and would ship the site without its PDFs (#71).
        deploys = re.findall(r"\bdeploy\b[^\n]*--prod[^\n]*", DEPLOY)
        self.assertTrue(deploys, "deploy.yml does not deploy to production")
        for line in deploys:
            self.assertIn("--prebuilt", line)

    def test_deploy_waits_for_the_gate(self):
        self.assertIn("run: ./test.sh", DEPLOY)
        self.assertRegex(DEPLOY, r"\n  deploy:\n(?:    .*\n)*?    needs: gate\n")

    def test_only_main_deploys(self):
        self.assertRegex(DEPLOY, r"push:\n\s+branches: \[main\]\n")
        self.assertNotIn("pull_request", DEPLOY)


class ToolVersions(unittest.TestCase):
    """CI builds with the versions pinned in .tool-versions, so a clean-room rebuild reproduces (#84)."""

    PINNED = dict(line.split() for line in (ROOT / ".tool-versions").read_text().splitlines() if line.strip())

    def test_every_workflow_uses_the_pinned_python_and_node(self):
        for wf in WORKFLOWS:
            text = wf.read_text()
            for v in re.findall(r'python-version: "([^"]+)"', text):
                self.assertEqual(v, self.PINNED["python"], wf.name)
            for v in re.findall(r'node-version: "([^"]+)"', text):
                self.assertEqual(v, self.PINNED["nodejs"], wf.name)

    def test_ci_installs_the_pinned_typst(self):
        found = re.findall(r"TYPST_VERSION: v(\S+)", "".join(wf.read_text() for wf in WORKFLOWS))
        self.assertTrue(found)
        self.assertEqual(set(found), {self.PINNED["typst"]})

    def test_nvmrc_agrees(self):
        self.assertEqual((ROOT / ".nvmrc").read_text().strip(), self.PINNED["nodejs"])


if __name__ == "__main__":
    unittest.main()
