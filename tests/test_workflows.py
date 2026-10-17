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
        self.assertRegex(DEPLOY, r"with:\n      pdf: true\n      factcheck: true\n      mobile_integration: true\n")

    def test_the_gate_jobs_run_every_stage_of_test_sh(self):
        # The --only groups partition test.sh: every stage is in exactly one group, and gate.yml runs each
        # group, so the parallel jobs run what ./test.sh runs (docs/process.md, optimisation 3).
        groups = test_sh_groups()
        self.assertNotIn(None, groups, f"stages outside any --only group: {groups.get(None)}")
        self.assertEqual(sorted(groups), ["e2e", "live", "mobile", "model", "pdf", "web"])
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
        self.assertRegex(CI, r"\n  gate:\n    name: .+\n    uses: \./\.github/workflows/gate\.yml\n")
        self.assertNotIn("    if: github.event_name", CI)        # the triggers already say which events run it
        self.assertRegex(CI, r"\nconcurrency:\n  group: gate-\$\{\{ github\.ref \}\}\n  cancel-in-progress: true\n")
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


class Edition(unittest.TestCase):
    """The edition channel (#111, #112): published by one job after the site is final, written by one stdlib
    module, read back anonymously after every deploy and every week."""

    EDITION_PY = (ROOT / "model" / "edition.py").read_text(encoding="utf-8")
    MONITOR = (ROOT / ".github" / "workflows" / "monitor.yml").read_text(encoding="utf-8")

    def job(self) -> str:
        parts = DEPLOY.split("\n  edition:\n")
        self.assertEqual(len(parts), 2, "deploy.yml needs the edition job")
        # Up to the next job (#114 added `app` after it): the key rules below are about this job alone.
        return parts[1].split("\n  app:\n", 1)[0]

    def test_the_edition_is_published_by_its_own_job_after_the_deploy(self):
        job = self.job()
        self.assertRegex(job, r"\n    needs: deploy\n")
        self.assertIn("if: vars.SUPABASE_URL != ''", job)            # phased in like ASK_LIVE: skipped until set
        self.assertRegex(job, r"environment:\n      name: production\n")
        self.assertLess(DEPLOY.index("Roll back to the previous production deployment"), DEPLOY.index("\n  edition:\n"))
        deploy_job = DEPLOY.split("\n  deploy:\n")[1].split("\n  # The edition channel", 1)[0]
        for forbidden in ("model/edition.py", "SUPABASE", "--edition-url"):
            self.assertNotIn(forbidden, deploy_job, "the deploy job itself never touches the bucket")

    def test_the_service_key_reaches_only_the_publisher_through_its_environment(self):
        self.assertEqual(DEPLOY.count("secrets.SUPABASE_SERVICE_ROLE_KEY"), 1)
        job = self.job()
        step = job.split("- name: Publish the edition", 1)[1].split("- name:", 1)[0]
        self.assertIn("env:\n          SUPABASE_SERVICE_ROLE_KEY: ${{ secrets.SUPABASE_SERVICE_ROLE_KEY }}", step)
        for line in job.splitlines():
            if line.strip().startswith("run:"):
                self.assertNotIn("SERVICE_ROLE", line, "the key is never on a command line")
                self.assertNotIn("echo", line)
        for wf in WORKFLOWS:
            if wf.name != "deploy.yml":
                self.assertNotIn("SERVICE_ROLE", wf.read_text(), wf.name)

    def test_the_publisher_is_one_stdlib_module_and_nothing_unpinned(self):
        job = self.job()
        step = job.split("- name: Publish the edition", 1)[1].split("- name:", 1)[0]
        runs = [ln.strip() for ln in step.splitlines() if ln.strip().startswith("run:")]
        self.assertEqual(len(runs), 1)
        self.assertTrue(runs[0].startswith("run: python3 model/edition.py publish "), runs[0])
        for tool in ("npx", "curl", "supabase ", "pip "):
            self.assertNotIn(tool, step, f"{tool.strip()} in the publish step: an unpinned tool")
        self.assertIn("import urllib.request", self.EDITION_PY)
        self.assertNotIn("import requests", self.EDITION_PY)

    def test_an_edition_is_immutable_and_only_the_pointer_moves(self):
        self.assertIn('"x-upsert": "true" if upsert else "false"', self.EDITION_PY)
        self.assertIn("put_immutable(store, f\"{edition}/{name}\"", self.EDITION_PY)
        self.assertIn("upsert=False", self.EDITION_PY)
        pointer = self.EDITION_PY.split("def put_pointer", 1)[1].split("\ndef ", 1)[0]
        self.assertIn("upsert=True", pointer)
        self.assertEqual(self.EDITION_PY.count("upsert=True"), 1, "only latest.json is ever overwritten")
        self.assertIn("os.environ.get(\"SUPABASE_SERVICE_ROLE_KEY\")", self.EDITION_PY)
        self.assertNotIn("add_argument(\"--key", self.EDITION_PY)

    def test_the_deploy_and_the_weekly_monitor_read_the_edition_back(self):
        job = self.job()
        self.assertIn("python3 model/smoke.py --site '' --edition-url", job)
        self.assertIn("--manifest mobile/assets/data/manifest.json", job)
        self.assertIn("--edition-url", self.MONITOR)
        self.assertIn("--manifest mobile/assets/data/manifest.json", self.MONITOR)
        for text in (job, self.MONITOR):
            self.assertLess(text.index("export_json.py --split --from"), text.index("--edition-url"),
                            "the parts are generated before they are checked")

    def test_the_mobile_group_runs_in_the_gate_and_its_round_trip_only_in_the_deploy_s_gate(self):
        self.assertRegex(GATE, r"\n  mobile:\n(?:    .*\n)*?      - name: Run the mobile group\n        run: \./test\.sh --only mobile\n")
        self.assertRegex(GATE, r"\n  mobile-integration:\n(?:    .*\n)*?    if: inputs\.mobile_integration\n")
        self.assertIn("MOBILE_TEST_FLAGS=--integration ./test.sh --only mobile", GATE)
        self.assertNotIn("mobile_integration: true", CI)
        self.assertRegex(GATE, r"supabase/setup-cli@[0-9a-f]{40} # v[\d.]+\n        with:\n          version: \d+\.\d+\.\d+\n")


class App(unittest.TestCase):
    """The reader's release (#114, #115): one job after the deploy starts the EAS workflow for the same commit,
    with the pinned CLI from the lockfile and the token in the production environment; the EAS workflow itself
    never runs on a push and never submits without an approval."""

    RELEASE = (ROOT / "mobile" / ".eas" / "workflows" / "release.yml").read_text(encoding="utf-8")
    MOBILE_PKG = json.loads((ROOT / "mobile" / "package.json").read_text(encoding="utf-8"))
    EAS_JSON = json.loads((ROOT / "mobile" / "eas.json").read_text(encoding="utf-8"))

    def job(self) -> str:
        parts = DEPLOY.split("\n  app:\n")
        self.assertEqual(len(parts), 2, "deploy.yml needs the app job")
        return parts[1]

    def test_the_release_starts_from_its_own_job_after_the_deploy_in_the_production_environment(self):
        job = self.job()
        self.assertRegex(job, r"\n    needs: deploy\n")
        self.assertIn("if: vars.EXPO_PROJECT_ID != ''", job)               # phased in like SUPABASE_URL
        self.assertRegex(job, r"environment:\n      name: production\n")
        self.assertLess(DEPLOY.index("\n  edition:\n"), DEPLOY.index("\n  app:\n"))
        self.assertIn("working-directory: mobile", job)
        self.assertIn("cache-dependency-path: mobile/package-lock.json", job)
        self.assertIn("run: npm ci\n", job)

    def test_the_token_reaches_only_the_workflow_run_step_through_its_environment(self):
        self.assertEqual(DEPLOY.count("secrets.EXPO_TOKEN"), 1)
        job = self.job()
        step = job.split("- name: Start the release workflow", 1)[1].split("- name:", 1)[0]
        self.assertIn("env:\n          EXPO_TOKEN: ${{ secrets.EXPO_TOKEN }}", step)
        runs = [ln.strip() for ln in step.splitlines() if ln.strip().startswith("run:")]
        self.assertEqual(runs, ['run: npx --yes "$EAS_CLI" workflow:run .eas/workflows/release.yml --non-interactive'])
        for line in job.splitlines():
            if line.strip().startswith("run:"):
                self.assertNotIn("EXPO_TOKEN", line, "the token is never on a command line")
                self.assertNotIn("--token", line)
                self.assertNotIn("echo", line)
        for wf in WORKFLOWS:
            if wf.name != "deploy.yml":
                self.assertNotIn("EXPO_TOKEN", wf.read_text(), wf.name)

    def test_the_cli_is_one_pinned_version_everywhere(self):
        pin = re.search(r"EAS_CLI: eas-cli@(\d+\.\d+\.\d+)\n", DEPLOY)
        self.assertIsNotNone(pin, "deploy.yml pins EAS_CLI: eas-cli@x.y.z")
        version = pin.group(1)
        self.assertEqual(self.EAS_JSON["cli"]["version"], version, "eas.json enforces the same pin on the CLI")
        for field in ("dependencies", "devDependencies"):
            self.assertNotIn("eas-cli", self.MOBILE_PKG.get(field, {}), "expo-doctor refuses eas-cli as a dependency")
        self.assertNotIn("npx eas ", self.job(), "never a floating eas: the pinned EAS_CLI, like VERCEL_CLI")
        self.assertNotIn("eas-cli@latest", DEPLOY)
        self.assertNotIn("expo/expo-github-action", DEPLOY)

    def test_the_eas_workflow_runs_only_when_asked_and_submits_only_after_an_approval(self):
        on = self.RELEASE.split("\non:\n", 1)[1].split("\njobs:\n", 1)[0]
        self.assertEqual([ln.strip().rstrip(":").split(":")[0] for ln in on.splitlines() if ln.strip()],
                         ["workflow_dispatch"])
        jobs = re.findall(r"^  (\w+):\n", self.RELEASE, re.M)
        self.assertIn("require_approval", jobs)
        self.assertIn("type: require-approval", self.RELEASE)
        for submit in ("submit_ios",):
            block = self.RELEASE.split(f"\n  {submit}:\n", 1)[1].split("\n  ", 1)[0]
            self.assertIn("require_approval", block, f"{submit} runs only after the approval")
        self.assertNotIn("submit_android", self.RELEASE, "no Play account yet (#114)")
        self.assertIn("submit_beta_review: false", self.RELEASE)
        self.assertLessEqual(len(self.RELEASE.encode()), 16 * 1024)

    def test_installed_apps_never_check_for_code_on_their_own(self):
        app = json.loads((ROOT / "mobile" / "app.json").read_text(encoding="utf-8"))["expo"]
        self.assertEqual(app["updates"]["checkAutomatically"], "NEVER")
        self.assertEqual(app["runtimeVersion"], {"policy": "appVersion"})
        self.assertEqual(self.EAS_JSON["build"]["production"]["channel"], "production")
        self.assertIn("channel: production", self.RELEASE)


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



class Hardening(unittest.TestCase):
    """#107: a pinned runner, a rollback after a failed post-deploy check, and a ruleset whose checks exist."""

    def test_no_workflow_runs_on_a_floating_runner_image(self):
        loose = [wf.name for wf in WORKFLOWS if "ubuntu-latest" in wf.read_text()]
        self.assertEqual(loose, [], "pin the runner image (ubuntu-24.04); -latest changes under the gate")

    def test_a_failed_smoke_test_rolls_the_deploy_back(self):
        deploy = DEPLOY.split("- name: Roll back to the previous production deployment", 1)
        self.assertEqual(len(deploy), 2, "deploy.yml needs the rollback step")
        self.assertIn("if: failure() && steps.deploy.outcome == 'success'", deploy[1])
        self.assertIn('rollback "https://${{ steps.previous.outputs.url }}" --yes', deploy[1],
                      "vercel rollback without a deployment argument only prints a status (CLI 61)")
        self.assertLess(DEPLOY.index("id: previous"), DEPLOY.index("id: deploy"),
                        "the previous production deployment is recorded before the upload")
        self.assertIn("steps.previous.outputs.url != ''", deploy[1])
        self.assertIn("steps.promote.outcome != 'failure'", deploy[1],
                      "a failed promote is not a failed deployment; it must not trigger the rollback")
        record = DEPLOY.split("id: previous", 1)[1].split("- name:", 1)[0]
        self.assertIn(".targets.production.url", record,
                      "record the project's production target; the newest deployment may be the one rolled back")
        promote = DEPLOY.split("is the current production deployment", 1)[1].split("- name:", 1)[0]
        self.assertIn("set -euo pipefail", promote, "a failed promote must fail the step")
        self.assertLess(DEPLOY.index("Smoke test the live domain"), DEPLOY.index("Roll back to the previous"))

    def test_the_ruleset_requires_checks_that_the_branch_gate_produces(self):
        ruleset = json.loads((ROOT / ".github" / "rulesets" / "main.json").read_text())
        self.assertEqual(ruleset["conditions"]["ref_name"]["include"], ["refs/heads/main"])
        self.assertEqual(ruleset["bypass_actors"], [])
        kinds = {r["type"] for r in ruleset["rules"]}
        self.assertTrue({"deletion", "non_fast_forward", "required_status_checks"} <= kinds)
        checks = next(r for r in ruleset["rules"] if r["type"] == "required_status_checks")
        contexts = [c["context"] for c in checks["parameters"]["required_status_checks"]]
        # The caller job's display name in ci.yml prefixes every reusable job: "<caller> / <job name>".
        caller = re.search(r"\n  gate:\n    name: (.+)\n", CI).group(1)
        job_names = re.findall(r"^    name: (.+)$", GATE, re.M)
        security = (ROOT / ".github" / "workflows" / "security.yml").read_text()
        sec_caller = re.search(r"^name: (.+)$", security, re.M).group(1)
        for ctx in contexts:
            if ctx.startswith(f"{caller} / "):
                self.assertIn(ctx[len(caller) + 3:], job_names, f"{ctx} is not a gate job")
            else:
                self.assertIn(ctx, (f"{sec_caller} / gate", f"{sec_caller} / gitleaks"),
                              f"{ctx}: not a job of the reusable security workflow as named today")
        # Only the fast jobs: the PDFs are not built on a branch (ci.yml passes pdf: false) and the browsers
        # are not required, so a push waits for minutes, not a quarter of an hour.
        self.assertNotIn("Gate / PDFs (./test.sh --only pdf)", contexts)
        self.assertFalse(any("Browser" in c for c in contexts))

    def test_dependabot_raises_security_updates_only(self):
        text = (ROOT / ".github" / "dependabot.yml").read_text()
        self.assertEqual(len(re.findall(r"^\s+open-pull-requests-limit: 0$", text, re.M)),
                         len(re.findall(r"^\s+- package-ecosystem:", text, re.M)))

if __name__ == "__main__":
    unittest.main()
