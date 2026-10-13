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

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = sorted((ROOT / ".github" / "workflows").glob("*.yml"))
DEPLOY = (ROOT / ".github" / "workflows" / "deploy.yml").read_text()
GATE = (ROOT / ".github" / "workflows" / "gate.yml").read_text()
CI = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
TEST_SH = (ROOT / "test.sh").read_text(encoding="utf-8")

USES = re.compile(r"^\s*(?:-\s*)?uses:\s*(\S+)", re.M)
SHA = re.compile(r"@[0-9a-f]{40}$")
# The owner's own reusable workflows are tracked at @main by design (security-reusable.yml).
OWN_REUSABLE = "pieteradejong/dotfiles/.github/workflows/"
# A workflow in this repository is read at the same commit as its caller, so it needs no pin.
LOCAL = "./.github/workflows/"


class Pinning(unittest.TestCase):
    def test_every_action_is_pinned_by_sha(self):
        loose = [f"{wf.name}: {ref}" for wf in WORKFLOWS for ref in USES.findall(wf.read_text())
                 if not SHA.search(ref) and not ref.startswith((OWN_REUSABLE, LOCAL))]
        self.assertEqual(loose, [], "a tag can be moved under us; pin actions by commit SHA")

    def test_vercel_cli_is_an_exact_version(self):
        self.assertRegex(DEPLOY, r"VERCEL_CLI: vercel@\d+\.\d+\.\d+\n")


def test_sh_groups() -> dict[str, list[str]]:
    """The stages of test.sh by the --only group whose block they sit in."""
    groups: dict[str, list[str]] = {}
    stack: list[str | None] = []                 # the top-level if-blocks open at this line
    for line in TEST_SH.splitlines():
        if line.startswith("if "):
            m = re.search(r"in_group (\w+)", line)
            stack.append(m.group(1) if m else None)
        elif line == "fi":
            stack.pop()
        if m := re.match(r'\s*step "([^"]+)"', line):
            group = next((g for g in reversed(stack) if g), None)
            groups.setdefault(group, []).append(m.group(1))
    return groups


class Deploy(unittest.TestCase):
    def test_typst_download_is_checksummed(self):
        self.assertRegex(GATE, r"TYPST_SHA256: [0-9a-f]{64}\n")
        self.assertIn("sha256sum -c", GATE)

    def test_upload_is_prebuilt(self):
        # A remote build has no typst and would ship the site without its PDFs (#71).
        deploys = re.findall(r"\bdeploy\b[^\n]*--prod[^\n]*", DEPLOY)
        self.assertTrue(deploys, "deploy.yml does not deploy to production")
        for line in deploys:
            self.assertIn("--prebuilt", line)

    def test_deploy_waits_for_the_gate(self):
        self.assertRegex(DEPLOY, r"\n  gate:\n(?:    .*\n)*?    uses: \./\.github/workflows/gate\.yml\n")
        self.assertRegex(DEPLOY, r"\n  deploy:\n(?:    .*\n)*?    needs: gate\n")
        self.assertRegex(DEPLOY, r"with:\n      pdf: true\n      factcheck: true\n")

    def test_the_gate_jobs_run_every_stage_of_test_sh(self):
        # The --only groups partition test.sh: every stage is in exactly one group, and gate.yml runs each
        # group, so the parallel jobs run what ./test.sh runs (docs/process.md, optimisation 3).
        groups = test_sh_groups()
        self.assertNotIn(None, groups, f"stages outside any --only group: {groups.get(None)}")
        self.assertEqual(sorted(groups), ["e2e", "live", "model", "pdf", "web"])
        for group in set(groups) - {"live"}:
            self.assertRegex(GATE, rf"\./test\.sh --only {group}\b")

    def test_the_live_ask_check_runs_after_the_deploy(self):
        # The live group calls the live /ask, so it runs on the new deploy, after it, never in the gate: a
        # broken key must not block the redeploy that fixes it.
        self.assertNotIn("--only live", GATE)
        deploy_job = DEPLOY.split("\n  deploy:\n")[1]
        self.assertLess(deploy_job.index("deploy --prebuilt --prod"), deploy_job.index("run: ./test.sh --only live"))
        live = TEST_SH.split("if ! in_group live; then", 1)[1].split("\nfi\n", 1)[0]
        self.assertIn("python3 model/ask_smoke.py --require", live)

    def test_deploy_waits_for_the_fact_check(self):
        # Every printed fact checked by the model that did not write it, before production (#87):
        # in the gate's model job, which deploy needs, and in the manual fallback.
        model_job = GATE.split("\n  model:\n")[1].split("\n  web:\n")[0]
        self.assertIn("if: inputs.factcheck\n        run: python3 model/factcheck.py gate", model_job)
        run_sh = (ROOT / "run.sh").read_text(encoding="utf-8")
        deploy = run_sh.split("    deploy)\n", 1)[1].split("\n        ;;\n", 1)[0]
        self.assertLess(deploy.index("python3 model/factcheck.py gate"), deploy.index("vercel deploy"))

    def test_deploy_ships_the_build_the_gate_tested(self):
        # Optimisation 1: no second build. The deploy downloads the gate's web app and PDFs, packages them
        # without rebuilding (./run.sh site, PREBUILT_SITE=1), and fails unless the packaged files are the
        # gate's, byte for byte.
        self.assertIn('"buildCommand": "./run.sh site"', (ROOT / "vercel.json").read_text())
        self.assertIn("name: web-dist", GATE)
        self.assertIn("name: pdfs", GATE)
        deploy_job = DEPLOY.split("\n  deploy:\n")[1]
        for needed in ("name: web-dist", "name: pdfs", "PREBUILT_SITE=1", ".vercel/output/static"):
            self.assertIn(needed, deploy_job)
        self.assertNotIn("typst", deploy_job.lower())
        run_sh = (ROOT / "run.sh").read_text(encoding="utf-8")
        site = run_sh.split("    site)\n", 1)[1].split("\n        ;;\n", 1)[0]
        self.assertIn('if [ "$pdfs" != 28 ]', site)
        self.assertIn("python3 book/report.py -o web/dist", site)      # the full build without the flag

    def test_pull_requests_and_branch_pushes_get_the_full_gate_and_an_audit(self):
        # #92: a pull request runs the gate and the dependency audit before it can reach main. #107: so does
        # every push to a branch other than main, because main's ruleset requires the checks on the commit.
        self.assertRegex(CI, r"\non:\n  pull_request:\n  push:\n    branches-ignore: \[main\]\n")
        self.assertRegex(CI, r"\n  gate:\n(?:    .*\n)*?    if: github.event_name == 'pull_request' \|\| github.event_name == 'push'\n"
                             r"    uses: \./\.github/workflows/gate\.yml\n")
        self.assertIn("npm audit --audit-level=high --prefix web", GATE)

    def test_ci_installs_the_test_packages_by_hash(self):
        self.assertIn("pip install --require-hashes -r requirements-dev.txt", GATE)
        reqs = (ROOT / "requirements-dev.txt").read_text()
        for line in reqs.splitlines():
            if line and not line.startswith(("#", " ")):
                self.assertRegex(line, r"^[a-z0-9-]+==[0-9.]+ \\$")    # exact pin, followed by hashes

    def test_the_gate_installs_every_browser_it_tests_in(self):
        # One e2e job per Playwright project, each installing the engine that project runs on.
        config = (ROOT / "web" / "playwright.config.ts").read_text()
        projects = re.findall(r"\{ name: '([^']+)', use: \{ \.\.\.devices\['([^']+)'\]", config)
        matrix = dict(re.findall(r"- \{ project: ([\w-]+), browser: \"?(\w*)\"? \}", GATE))
        self.assertEqual(sorted(matrix), sorted(p for p, _ in projects))
        engine = {"Desktop Chrome": "", "Desktop Firefox": "firefox"}
        for project, device in projects:
            self.assertEqual(matrix[project], engine.get(device, "webkit"), project)
        self.assertIn('playwright install --with-deps "${{ matrix.browser }}"', GATE)

    def test_every_cache_is_keyed_by_a_pin_or_checksum(self):
        # Optimisation 2: a stale cache can never be used, and what is installed is still verified.
        keys = re.findall(r"key: (.+)", GATE + DEPLOY + CI)
        self.assertTrue(keys)
        for key in keys:
            self.assertTrue("TYPST_SHA256" in key or "steps.playwright.outputs.version" in key, key)
        for path in re.findall(r"cache-dependency-path: ([^|\n]+)\n", GATE + DEPLOY):
            self.assertRegex(path.strip(), r"(package-lock\.json|requirements-dev\.txt)$")
        self.assertIn("npm ci", GATE)                              # the lockfile is verified on every run

    def test_the_deploy_and_the_weekly_monitor_run_the_same_smoke_test(self):
        monitor = (ROOT / ".github" / "workflows" / "monitor.yml").read_text()
        self.assertIn("python3 model/smoke.py", DEPLOY)
        self.assertIn("python3 model/smoke.py", monitor)
        self.assertRegex(monitor, r"schedule:\n\s+- cron: ")
        self.assertNotIn("issues: write", monitor)              # read-only: it opens nothing

    def test_ci_is_the_gate_on_pull_requests_and_branch_pushes_and_nothing_else(self):
        # #98: a second, weaker copy of the model checks on push, and a second gitleaks, were removed. A push to
        # main runs the gate in deploy.yml; secrets are scanned on every push and pull request by security.yml.
        # #107: a push to any other branch runs the same gate, so main's ruleset finds the checks on the commit.
        self.assertRegex(CI, r"\non:\n  pull_request:\n  push:\n    branches-ignore: \[main\]\n")
        self.assertEqual(CI.count("push:"), 1)
        self.assertNotIn("unittest discover", CI)
        self.assertNotIn("gitleaks-reusable", CI)
        security = (ROOT / ".github" / "workflows" / "security.yml").read_text()
        self.assertIn(OWN_REUSABLE + "security-reusable.yml@main", security)
        self.assertRegex(security, r"on: \[push, pull_request")

    def test_pull_requests_report_the_fact_check(self):
        # #98: on a pull request the fact-check gate runs and warns, but does not fail: the deploy enforces it.
        model_job = GATE.split("\n  model:\n")[1].split("\n  web:\n")[0]
        report = model_job.split("if: ${{ !inputs.factcheck }}\n", 1)[1]
        self.assertIn("set -o pipefail", report)
        self.assertIn("if ! python3 model/factcheck.py gate", report)
        self.assertIn("::warning title=Fact check due::", report)

    def test_the_weekly_monitor_rechecks_every_cited_source(self):
        # #98: read-only, polite, and failing only on a source that newly disputes its facts (#83).
        monitor = (ROOT / ".github" / "workflows" / "monitor.yml").read_text()
        job = monitor.split("\n  sources:\n")[1].split("\n  ask:\n")[0]
        self.assertIn("if: github.event.schedule != '41 7 * * *'", job)
        self.assertIn("poppler-utils", job)                   # without pdftotext every PDF quote looks gone
        self.assertIn("python3 model/research.py recheck --check", job)
        self.assertIn("set -o pipefail", job)
        self.assertRegex(job, r"if: always\(\)\n        uses: actions/upload-artifact@[0-9a-f]{40}")
        self.assertNotIn("contents: write", monitor)

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


class Hardening(unittest.TestCase):
    """#107: a pinned runner, a rollback after a failed post-deploy check, and a ruleset whose checks exist."""

    def test_no_workflow_runs_on_a_floating_runner_image(self):
        loose = [wf.name for wf in WORKFLOWS if "ubuntu-latest" in wf.read_text()]
        self.assertEqual(loose, [], "pin the runner image (ubuntu-24.04); -latest changes under the gate")

    def test_a_failed_smoke_test_rolls_the_deploy_back(self):
        deploy = DEPLOY.split("- name: Roll back to the previous production deployment", 1)
        self.assertEqual(len(deploy), 2, "deploy.yml needs the rollback step")
        self.assertIn("if: failure() && steps.deploy.outcome == 'success'", deploy[1])
        self.assertIn("rollback --yes", deploy[1])
        self.assertLess(DEPLOY.index("Smoke test the live domain"), DEPLOY.index("Roll back to the previous"))

    def test_the_ruleset_requires_checks_that_the_branch_gate_produces(self):
        ruleset = json.loads((ROOT / ".github" / "rulesets" / "main.json").read_text())
        self.assertEqual(ruleset["conditions"]["ref_name"]["include"], ["refs/heads/main"])
        self.assertEqual(ruleset["bypass_actors"], [])
        kinds = {r["type"] for r in ruleset["rules"]}
        self.assertTrue({"deletion", "non_fast_forward", "required_status_checks"} <= kinds)
        checks = next(r for r in ruleset["rules"] if r["type"] == "required_status_checks")
        contexts = [c["context"] for c in checks["parameters"]["required_status_checks"]]
        # The gate job in ci.yml is named Gate, so its reusable jobs report as "Gate / <job name>".
        job_names = re.findall(r"^    name: (.+)$", GATE, re.M)
        for ctx in contexts:
            if ctx.startswith("Gate / "):
                self.assertIn(ctx[len("Gate / "):], job_names, f"{ctx} is not a gate job")
            else:
                self.assertTrue(ctx.startswith("security / "), ctx)
        # Only the fast jobs: the PDFs are not built on a branch (ci.yml passes pdf: false) and the browsers
        # are not required, so a push waits for minutes, not a quarter of an hour.
        self.assertNotIn("Gate / PDFs (./test.sh --only pdf)", contexts)
        self.assertFalse(any("Browser" in c for c in contexts))

    def test_dependabot_raises_security_updates_only(self):
        text = (ROOT / ".github" / "dependabot.yml").read_text()
        self.assertEqual(len(re.findall(r"^\s+open-pull-requests-limit: 0$", text, re.M)),
                         len(re.findall(r"^\s+- package-ecosystem:", text, re.M)))

