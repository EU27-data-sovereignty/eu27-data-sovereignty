# CI/CD: every automated check, where it runs, and why

What runs on GitHub Actions, on which event, and what a failure means. The checks themselves are listed stage by
stage in [`testing.md`](testing.md), and the pipeline's timings in [`process.md`](process.md). The reasoning is in
[`DECISIONS.md`](../DECISIONS.md), cited by number. Last revised 2026-10-16 (#114–#116); the vetting of that day, with
every check and its output, is [`plans/ci-cd-status-2026-10-14.md`](plans/ci-cd-status-2026-10-14.md).

## By event

| Event | Workflow | What runs | Blocks |
|---|---|---|---|
| Push to any branch but `main` | `ci.yml` → `gate.yml` (`pdf: false`) | The gate's model, web, mobile and e2e jobs; the fact check, reported only. One run per branch: a newer push cancels the run the older one started (#107) | The later push to `main`, once the ruleset is applied (NOT YET on 2026-10-14): `main` accepts only a commit whose model, web and security checks have passed |
| Pull request | `ci.yml` → `gate.yml` (`pdf: false`) | The same | The same; no reviewer is required (#107) |
| Push or pull request | `security.yml` → dotfiles `security-reusable.yml` | gitleaks over the full history with the shared ruleset, then the security gate over what the push brings | Nothing directly; a red run is a finding to fix |
| Push to `main` | `deploy.yml` → `gate.yml` (`pdf: true`, `factcheck: true`, `mobile_integration: true`) | The full gate including 28 PDFs, the fact-check gate and the mobile edition round-trip against a local Supabase; then the deploy job: the gate's own build packaged and checked byte for byte, the current production deployment recorded, the prebuilt upload, the smoke test, one live `/ask` call, promotion if needed, and a rollback to the recorded deployment if the smoke test or the `/ask` call fails (#107); then the `edition` job, once `SUPABASE_URL` is set: the split edition published to the bucket and read back (#112); then the `app` job, once `EXPO_PROJECT_ID` is set: the reader's release workflow started on EAS for the same commit, which builds on a native change, sends the build to TestFlight, waits for the owner's approval and uploads it to App Store Connect, or publishes the JavaScript as an over-the-air update (#114, #115) | The production deploy; the app's build and upload |
| Mondays 06:17 UTC | `monitor.yml` (`live`, `sources`) | The live site smoke test and the edition channel (#111), Eurostat vintages, every cited source re-fetched | Nothing; a red run is a finding |
| Daily 07:41 UTC | `monitor.yml` (`ask`) | One fixed question to the live `/ask` | Nothing |

The cron times are requests: GitHub has started these runs six to nine hours late on every day observed
(2026-10-03 to 2026-10-13), so a Monday recheck can finish on Monday evening.

Every workflow declares `permissions: contents: read`. None can write to the repository, open an issue or comment.
Every job runs on `ubuntu-24.04`, never `-latest`, so the browser and system libraries under the gate change only
with a commit (#107).

## The gate (`gate.yml`)

`./test.sh` split into parallel jobs (#97). The `--only` groups partition its stages, and
`tests/test_workflows.py` fails if a stage sits outside every group, so CI runs exactly what `./test.sh` runs
locally.

| Job | Command | What it proves |
|---|---|---|
| `model` | `./test.sh --only model` | Data integrity (next section) |
| `model` | `factcheck.py gate`, if `factcheck` | Every printed fact is checked by the model that did not write it, and the audit file is current (#87). Deploy only |
| `model` | `factcheck.py gate`, if not `factcheck` | The same check, written to the run summary as a warning that never fails the job (#98). Pull requests only |
| `web` | `npm audit --audit-level=high` (root and `web/`) | No high-severity advisory in the shipped dependencies |
| `web` | `./test.sh --only web` | `api/` type-checks against the real SDK; type-check, lint, format, Vitest and build; the gzipped size budget |
| `pdf` | `./test.sh --only pdf` | The EU-27 report and 27 country PDFs compile and pass inspection (disclaimer, appendices, fonts, size). Deploy only |
| `e2e` | `./test.sh --only e2e --project <name>` | Playwright, one job per browser project |
| `mobile` | `./test.sh --only mobile` | The mobile reader's suite (`mobile/test.sh --ci`): parity with `web/` byte for byte, the 28 parts against the manifest and the committed bundle, the generated tokens, format, lint, types, Jest with coverage floors, expo-doctor, the web export, `npm audit` against `mobile/audit-allowlist.json` (#113) |
| `mobile-integration` | `MOBILE_TEST_FLAGS=--integration ./test.sh --only mobile`, if `mobile_integration` | A local Supabase stack; the deploy's own publisher fills the bucket; anonymous reads, refused writes, `verify`, the app installing a good edition and rejecting an altered one. Deploy only: `supabase start` would be the critical path on every push (#113) |

The deploy job ships the gate's own `web-dist` and `pdfs` artifacts. It fails unless the packaged tree's
sha256 equals the tested build's (#97). After the upload it runs `model/smoke.py` against the domain and
`./test.sh --only live` (one real `/ask` call), promotes the deployment if Vercel has not (after a rollback Vercel
pauses automatic promotion), and on a failed smoke test or `/ask` call rolls back to the production deployment it
recorded before the upload (#107). The run stays red either way.

## Data integrity checks

All of these are in the `model` job, on every pull request and before every deploy.

| Check | Fails when |
|---|---|
| `python3 -m unittest discover -s tests` | CSV or referential integrity breaks, an output stops being deterministic, a coverage floor drops (a ratchet, #73), a cited host has no source tier (#83), a numeric score appears (#10, #77), a printed figure is not in its quote (#82), a workflow action is unpinned, or a decision entry lacks a part (#72) |
| `model/sources.py`, `model/national_data.py` | The verification ledger or the national register is invalid |
| `model/document.py --check` | A printed fact does not resolve to a checked citation (#75) |
| Generated files are current | Regenerating the briefs, bundle, `/ask` corpus, `evidence.md` or `gaps.md` with the pinned epoch changes them |
| `model/reproduce.py admit-check` | Re-running admission on the committed evidence does not give the committed registers (#84) |
| `factcheck.py replay`, `audit --check` | The fact-check ledger does not rebuild from the staged verdicts, or the audit file is stale (#87) |

## Checks of what changes without a commit (`monitor.yml`)

| Job | Command | Fails when |
|---|---|---|
| `live` | `model/smoke.py --site https://eu27.cloud` | A route, PDF, preview, security header, noindex, the www redirect, the TLS certificate or the served bundle is wrong. The deploy runs the same smoke test |
| `live` | `model/fetch_eurostat.py --check` | Reports new Eurostat vintages; never applies them |
| `sources` | `model/research.py recheck --check` | A source behind a printed fact is newly `gone` (404/410) or `quote_vanished`, compared with the committed `model/research/recheck.csv` (#98) |
| `ask` | `model/ask_smoke.py` | The live `/ask` does not stream an answer that cites a claim (required once `ASK_LIVE` is `true`) |

The `sources` job fetches politely: one request at a time, 1.5 s apart, obeying `robots.txt` (`model/fetch.py`).
A refusal (`unreachable`) never fails it, because a refusal is not evidence of change (#83). It installs
`pdftotext`, without which every PDF quote would look vanished. It commits nothing. The run's `recheck.csv` and
`fetch_manifest.csv` are kept as the `recheck` artifact for 90 days. **When it fails:** run `./run.sh recheck`
locally, then `./run.sh data`, review, and commit. The facts on the failing sources are then shown as disputed.

## Supply chain

Enforced by `tests/test_workflows.py` unless noted.

- Every action is pinned by commit SHA. The exceptions are this repository's own workflows and the owner's
  dotfiles reusable workflows, tracked at `@main` by design.
- typst is pinned and checked against its sha256. The Vercel CLI is an exact version.
- Test-only Python packages install with `pip --require-hashes`; npm installs with `npm ci` from the lockfile.
- Every cache is keyed by a pin or a checksum.
- Python, Node and typst versions match `.tool-versions`.

## Changes on 2026-10-07 (#98)

| Gap found | Change | Covered now by |
|---|---|---|
| `ci.yml`'s `model` job re-ran the Python tests on each push to `main`, with a weaker staleness check (2 of 5 generators, failing on any tree diff) | Removed. `ci.yml` runs on pull requests only, and only the gate | `deploy.yml`'s gate on push; `ci.yml`'s gate on pull requests |
| A pull request with an unchecked printed fact went green and failed only at the production deploy | The pull-request gate runs `factcheck.py gate` as a warning | `gate.yml`, model job |
| Cited sources were re-fetched only when the owner ran `./run.sh recheck`; the last committed run (2026-09-30) covered 691 of today's 1,257 sources | Weekly `recheck --check`, read-only, with an artifact | `monitor.yml`, `sources` job |
| gitleaks ran twice per push, once through the superseded `gitleaks-reusable.yml` | Removed from `ci.yml` | `security.yml` |

**Decisions taken** (full entry: `DECISIONS.md` #98):
- **The fact check is reported on pull requests, not enforced.** A branch must stay unblocked while facts are
  being researched; only shipping an unchecked fact is refused.
- **The weekly recheck never commits.** `recheck.csv` decides which facts are shown as disputed. Writing it from
  CI would be a change to the published report that nobody reviewed, and it would need `contents: write`.
- **`unreachable` does not fail the recheck.** GitHub's runner addresses are refused more often than a laptop's.

**Verified** locally on 2026-10-07:
- `./test.sh --no-e2e --no-live` exits 0: 331 tests, 28 PDFs with 0 problems, generated files current.
- The 8 new tests fail against the previous workflows and `research.py` (2 failures, 6 errors), and pass now.
- `actionlint` reports nothing.
- `recheck --check` on a committed `gone` source exits 0. With its row set to `unchanged`, it exits 1 and lists
  the source.

**Not yet verified in CI:** the first pull request showing the fact-check step, and the first `sources` run, with
its duration against the 120-minute timeout and its artifact.

## Changes on 2026-10-12 (#107)

| Gap found | Change | Covered now by |
|---|---|---|
| A deploy that failed its smoke test stayed in front of readers | The deploy job records the project's production deployment before the upload and, if the smoke test or the live `/ask` call fails afterwards, runs `vercel rollback <that url>`. The first version called `vercel rollback` with no argument, which only prints a status; the Opus 5.5 review of the same day caught it | `deploy.yml`, last two steps; `tests/test_workflows.py` holds the step's condition and argument |
| After a rollback Vercel stops promoting, so the next green deploy would not take the domain | A promote step after the live check makes the deployment that passed the current one when it is not | `deploy.yml`, promote step |
| `main` could be force-pushed or deleted, and a commit could reach it untested | A ruleset for `main` (`.github/rulesets/main.json`): no deletion, no non-fast-forward, four required checks (model, web, security gate, gitleaks). `ci.yml` now runs the gate on every branch push, so the checks exist before the push to `main` | the file and `ci.yml` are in the tree; the ruleset is applied by the owner with one `gh api` call, NOT YET on 2026-10-14 |
| `ubuntu-latest` could change the browser under the gate between two pushes | Every job pinned to `ubuntu-24.04` | `tests/test_workflows.py` |
| Nothing watched the exact pins for published vulnerabilities | `.github/dependabot.yml`: security updates only, version updates off for every ecosystem | the file is in the tree; Dependabot security updates are switched on by the owner, NOT YET on 2026-10-14 |

**Verified in CI since**, from the run history (`plans/ci-cd-status-2026-10-14.md`):
- The promote step first ran in Deploy run 38344010621 (2026-10-13 04:00 UTC) and on every deploy since.
- The first `sources` run (#98) was Monday 2026-10-12, run 38269792964: 72 minutes of the 120 allowed, the `recheck`
  artifact kept; it failed on 27 sources newly disputing their facts, 18 of them one host, which is the job doing
  what it is for. The committed `recheck.csv` is unchanged until the owner re-runs `./run.sh recheck`.
- The fact-check status step ran on the pull request of 2026-10-08 (CI run 37836074455), reported, not enforced.
- Branch pushes run the gate (CI runs on 2026-10-13, all green; three cancelled by the concurrency rule).

**Not yet:** the rollback step has never fired, because no deploy has failed after its upload; the ruleset, secret
scanning with push protection, and Dependabot security updates are repository settings the owner applies
(`plans/ci-cd-hardening.md`, commands A to C); the `security / gate` and `security / gitleaks` contexts in the
ruleset depend on the job ids of the dotfiles reusable workflow at `@main`.

## Changes on 2026-10-14 (#109–#113)

| Change | Where | What the run history has verified |
|---|---|---|
| The `mobile` job on every branch push and pull request | `gate.yml` | NOT YET: no run on a branch with it yet |
| The `mobile-integration` job in the deploy's gate | `gate.yml`, `deploy.yml` | NOT YET; locally, `cd mobile && ./test.sh --quick --ci --integration`: 9 of 9 steps against local Supabase 2.120.0 |
| The `edition` job after the deploy | `deploy.yml` | NOT YET: skipped until the owner sets `SUPABASE_URL`; the publisher is tested in `tests/test_edition.py` and by the integration run |
| The edition check in the weekly smoke test | `monitor.yml` | NOT YET: reports "not configured" until the variable exists |
| Dependabot watches `mobile/package-lock.json` | `dependabot.yml` | NOT YET: security updates are still off in the settings (#107 A to C) |

## Changes on 2026-10-16 (#114–#116)

| Change | Where | What the run history has verified |
|---|---|---|
| The `app` job after `edition`: `npm ci` in `mobile/`, `app.json`'s project id checked against the variable, `npx eas-cli@25.0.0 workflow:run` (the `EAS_CLI` pin, equal to `eas.json`'s `cli.version`) with `EXPO_TOKEN` in that step's env | `deploy.yml` | NOT YET: skipped until the owner sets `EXPO_PROJECT_ID`; the shape is held by `tests/test_workflows.py` `App` |
| The EAS workflow: `workflow_dispatch` only, `require-approval` before `submit`, Android never submitted | `mobile/.eas/workflows/release.yml` | NOT YET: `eas workflow:validate` needs the owner's login; `mobile/test.sh` `workflows` holds the triggers and the approval |
| `mobile/test.sh` gains `workflows`, `listing` (`eas metadata:lint`) and `release` (the ledger); `tooling` holds the EAS CLI pin | `mobile/test.sh` | Locally on 2026-10-16: PASS |

Secrets after this change: `VERCEL_TOKEN`, `SUPABASE_SERVICE_ROLE_KEY` and `EXPO_TOKEN`, all in the `production`
environment (restricted to `main`), each read by exactly one step through its environment; `tests/test_workflows.py`
fails on a second reference or a `--token` on a command line.

## Known limits

- Until the owner applies the ruleset (command B), a red branch or pull-request gate is advisory. The deploy's
  gate is what stops a bad push from reaching production; a force push or a deletion of `main` is not refused.
- Scheduled runs start hours after their cron time (above).
- The rollback is held by tests, not by a real failure.
- The weekly recheck runs from GitHub's addresses. If many hosts refuse them, it checks fewer sources than a
  local run would. The local `./run.sh recheck` stays the authoritative record.
- Mutation testing and the fact-check stability sample run by hand before a release ([`testing.md`](testing.md)).
