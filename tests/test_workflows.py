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

    def test_deploy_waits_for_the_fact_check(self):
        # Every printed fact checked by the model that did not write it, before production (#87):
        # in the gate job, which deploy needs, and in the manual fallback.
        gate = DEPLOY.split("\n  deploy:\n")[0]
        self.assertIn("run: python3 model/factcheck.py gate", gate)
        run_sh = (ROOT / "run.sh").read_text(encoding="utf-8")
        deploy = run_sh.split("    deploy)\n", 1)[1].split("\n        ;;\n", 1)[0]
        self.assertLess(deploy.index("python3 model/factcheck.py gate"), deploy.index("vercel deploy"))

    def test_pull_requests_get_the_full_gate_and_an_audit(self):
        # #92: a pull request runs ./test.sh and the dependency audit before it can reach main.
        ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
        self.assertIn("run: ./test.sh --no-pdf", ci)
        self.assertIn("if: github.event_name == 'pull_request'", ci)
        for wf in (ci, DEPLOY):
            self.assertIn("npm audit --audit-level=high --prefix web", wf)

    def test_ci_installs_the_test_packages_by_hash(self):
        for wf in ((ROOT / ".github" / "workflows" / "ci.yml").read_text(), DEPLOY):
            self.assertIn("pip install --require-hashes -r requirements-dev.txt", wf)
        reqs = (ROOT / "requirements-dev.txt").read_text()
        for line in reqs.splitlines():
            if line and not line.startswith(("#", " ")):
                self.assertRegex(line, r"^[a-z0-9-]+==[0-9.]+ \\$")    # exact pin, followed by hashes

    def test_the_gate_installs_every_browser_it_tests_in(self):
        config = (ROOT / "web" / "playwright.config.ts").read_text()
        for wf in ((ROOT / ".github" / "workflows" / "ci.yml").read_text(), DEPLOY):
            self.assertIn("playwright install --with-deps firefox webkit", wf)
        for project in ("firefox", "webkit", "iphone-se", "iphone-17-pro"):
            self.assertIn(f"name: '{project}'", config)

    def test_the_deploy_and_the_weekly_monitor_run_the_same_smoke_test(self):
        monitor = (ROOT / ".github" / "workflows" / "monitor.yml").read_text()
        self.assertIn("python3 model/smoke.py", DEPLOY)
        self.assertIn("python3 model/smoke.py", monitor)
        self.assertRegex(monitor, r"schedule:\n\s+- cron: ")
        self.assertNotIn("issues: write", monitor)              # read-only: it opens nothing

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
