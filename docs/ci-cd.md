# CI/CD: every automated check, where it runs, and why

What runs on GitHub Actions, on which event, and what a failure means. The checks themselves are listed stage by
stage in [`testing.md`](testing.md), and the pipeline's timings in [`process.md`](process.md). The reasoning is in
[`DECISIONS.md`](../DECISIONS.md), cited by number. Last revised 2026-10-07 (#98).

## By event

| Event | Workflow | What runs | Blocks |
|---|---|---|---|
| Pull request | `ci.yml` → `gate.yml` (`pdf: false`) | The gate's model, web and e2e jobs; the fact check, reported only | The merge, by convention (`main` has no branch protection) |
| Push or pull request | `security.yml` → dotfiles `security-reusable.yml` | gitleaks over the full history with the shared ruleset, then the security gate over what the push brings | Nothing directly; a red run is a finding to fix |
| Push to `main` | `deploy.yml` → `gate.yml` (`pdf: true`, `factcheck: true`) | The full gate including 28 PDFs and the fact-check gate, then the deploy | The production deploy |
| Mondays 06:17 UTC | `monitor.yml` (`live`, `sources`) | The live site smoke test, Eurostat vintages, every cited source re-fetched | Nothing; a red run is a finding |
| Daily 07:41 UTC | `monitor.yml` (`ask`) | One fixed question to the live `/ask` | Nothing |

Every workflow declares `permissions: contents: read`. None can write to the repository, open an issue or comment.

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

The deploy job ships the gate's own `web-dist` and `pdfs` artifacts. It fails unless the packaged tree's
sha256 equals the tested build's (#97).

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

## Known limits

- `main` has no branch protection, so a red pull-request gate is advisory. The deploy's gate is what stops a bad
  push from reaching production.
- The weekly recheck runs from GitHub's addresses. If many hosts refuse them, it checks fewer sources than a
  local run would. The local `./run.sh recheck` stays the authoritative record.
- Mutation testing and the fact-check stability sample run by hand before a release ([`testing.md`](testing.md)).
