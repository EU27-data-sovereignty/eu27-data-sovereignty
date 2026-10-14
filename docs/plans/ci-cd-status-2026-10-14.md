# CI/CD status: 2026-10-14

A point-in-time vetting of the pipeline. It is not maintained; how the pipeline works is in
[`ci-cd.md`](../ci-cd.md), the hardening list in [`ci-cd-hardening.md`](ci-cd-hardening.md), the open items in
[`TODO.md`](../../TODO.md). Every row below names the command that was run and what it printed, so the vetting
can be repeated.

**Produced by.** Claude Fable 5.1 (`claude-fable-5-1`) in Claude Code, session
`https://claude.ai/code/session_01BAPdY8fCzhdWJnMLnZuSvN`, between 2026-10-13 15:00 UTC and 2026-10-14 07:30 UTC.
Every check was re-run on 2026-10-14 between 07:26 and 07:29 UTC and the outputs below are from that re-run.
Starting commit: `fcf0b65` (`origin/main`). All checks were read-only: `gh api` GET calls, `gh run list` and
`gh run view`, `curl` against the live domain, `vercel ls`, `git` reads. Nothing in the repository settings, on
Vercel or on `main` was changed. Asked by the owner: "please vet the status of ci/cd and document in markdown".

## The pipeline in one paragraph

A push to `main` runs `deploy.yml`: the full gate as parallel jobs (`gate.yml`: model, web, PDFs, five browser
projects), the fact-check gate, then one deploy job that downloads the gate's own build, packages it with the
pinned Vercel CLI, refuses to ship unless the packaged tree's sha256 equals the tested one, records the current
production deployment, deploys prebuilt, smoke-tests the domain, makes one real `/ask` call, promotes the
deployment if it is not already current, and rolls back to the recorded deployment if a post-deploy check fails.
Every other branch push and every pull request runs the same gate without the PDFs (`ci.yml`). Every push and
pull request also runs gitleaks and the security gate (`security.yml`, from the dotfiles repo). `monitor.yml`
smoke-tests the site, checks Eurostat vintages and re-fetches every cited source on Mondays, and asks `/ask`
one question daily. All actions are pinned by SHA, every runner is `ubuntu-24.04`, typst is checksummed, and
every workflow has `permissions: contents: read`.

## What is green

| Check | Command | Output, 2026-10-14 |
|---|---|---|
| Production serves `main` | `curl -sS https://eu27.cloud/data/eu27.json \| shasum -a 256` against `git show origin/main:web/public/data/eu27.json \| shasum -a 256` | Both `1a970a50803fdee0…b371e4a0`. The live bundle is the committed one |
| Live routes | `curl -sS -o /dev/null -w '%{http_code} %{redirect_url}'` on each path | `/` 200, `/de` 200, `/country/DE` 308 → `/DE`, `/DE` 200, `/eu27-report.pdf` 200, `/report/DE.pdf` 200, `/robots.txt` 200, `/data/eu27.json` 200; `www` 308 → apex; `http` 308 → `https`. `x-robots-tag: noindex` on every 200 |
| TLS | `openssl s_client -servername eu27.cloud` | Let's Encrypt, expires 2026-12-31; Vercel renews |
| Last deploys | `gh run list --workflow Deploy --limit 10` | 9 of the last 10 green; the one failure (run 38222218250, 2026-10-12 08:13) failed in the gate, so nothing shipped. Last green: run 38373353625 for `fcf0b65`, 2026-10-13 09:01–09:05 UTC, 9 jobs |
| Deploy job steps | `gh api repos/…/actions/runs/38373353625/jobs` | Record the current production deployment: success. Deploy prebuilt: success. Smoke test: success. Live `/ask`: success. Promote: success. Roll back: skipped (nothing failed) |
| Vercel | `vercel ls --yes` | Three most recent deployments all `Ready`, `Production`, 7–8 s each; `vercel.json` has `git.deploymentEnabled: false`, so nothing but the workflow deploys |
| Branch gate | `gh run list --workflow CI --limit 10` | 10 of 10 green on branch pushes (`ci.yml` on every branch since #107). Three cancelled runs on 2026-10-13 03:44–03:47 are the concurrency rule cancelling a run its next push superseded, as designed |
| Pull-request fact-check step (the #98 "not yet") | `gh run view 37836074455 --json jobs` | On the pull request of 2026-10-08 the model job ran "Fact-check status (reported; the deploy enforces it)": success, and "Fact-check gate": skipped. Verified in CI |
| Promote step (#107) | `gh api …/runs/38344010621/jobs` | First ran in run 38344010621 (2026-10-13 04:00): success. Runs on every deploy since |
| security | `gh run list --limit 150 --json name,conclusion` filtered to non-success | 0 failures since 2026-10-09 01:29 |
| Daily `/ask` check | `gh run list --workflow Monitor --limit 20` | Green every day from 2026-10-03 to 2026-10-13 (the run of 2026-10-12 15:22 that failed was the Monday run; its `/ask` job is skipped by design and the 17:00 daily run passed) |
| Dependabot alerts | `gh api "repos/…/dependabot/alerts?state=open"` | 0 open. The four `mobile/` alerts in `TODO.md` were closed by `ef82e87` (2026-10-08) |
| Production environment | `gh secret list --env production`; `gh variable list`; `gh api …/environments/production/deployment-branch-policies` | Secret `VERCEL_TOKEN` (set 2026-10-02) in the `production` environment only; variables `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`, `ASK_LIVE=true`; the environment's branch policy allows `main` only |
| Actions token | `gh api repos/…/actions/permissions/workflow` | `default_workflow_permissions: read`; `can_approve_pull_request_reviews: false` |
| Workflow hygiene | `git show origin/main:.github/workflows/{ci,deploy,gate,monitor,security}.yml` | Every third-party action pinned by 40-character SHA; `ubuntu-24.04` everywhere; `VERCEL_CLI: vercel@61.1.0`; typst `v0.15.1` with its sha256 checked on every run; `permissions: contents: read` in all five. `tests/test_workflows.py` holds each of these |
| Ruleset file | `git show origin/main:.github/rulesets/main.json` | Its four required contexts are the job names `ci.yml` and `security.yml` produce: `Gate / Model and data (./test.sh --only model)`, `Gate / Web app (./test.sh --only web)`, `security / gate`, `security / gitleaks` |
| Dotfiles | `git -C ~/dev/dotfiles branch -r --contains 893d744` | `origin/main` contains it: the `TODO.md` item to push it is done |

## What is red or open, in order

### 1. The three repository-settings commands of #107 are still not applied

```
gh api repos/EU27-data-sovereignty/eu27-data-sovereignty --jq .security_and_analysis
{"dependabot_security_updates":{"status":"disabled"},"secret_scanning":{"status":"disabled"},
 "secret_scanning_non_provider_patterns":{"status":"disabled"},"secret_scanning_push_protection":{"status":"disabled"},
 "secret_scanning_validity_checks":{"status":"disabled"}}
gh api repos/EU27-data-sovereignty/eu27-data-sovereignty/rulesets
[]
gh api repos/EU27-data-sovereignty/eu27-data-sovereignty/branches/main/protection
{"message":"Branch not protected", … "status":"404"}
gh api -i repos/EU27-data-sovereignty/eu27-data-sovereignty/vulnerability-alerts
HTTP/2.0 204 No Content
gh api repos/EU27-data-sovereignty/eu27-data-sovereignty/automated-security-fixes
{"enabled":false,"paused":false}
```

So: no secret scanning, no push protection, no ruleset, no branch protection, Dependabot alerts on but
security updates off. Until command B runs, a red branch gate is advisory and `main` can be force-pushed or
deleted by anyone with write access. The assistant's own rule (#106) denies `gh api` writes, so these are the
owner's: commands A, B and C in [`ci-cd-hardening.md`](ci-cd-hardening.md), each idempotent, with a read-only
check after. `gh api repos/…/actions/permissions` also shows `sha_pinning_required: false`; the test suite
enforces the pins instead, so this is a belt-and-braces option, not a gap.

### 2. The weekly recheck failed on 2026-10-12: 27 sources newly dispute their facts

The first `sources` run in CI since #98 (run 38269792964, Monday 2026-10-12, 15:22–16:35 UTC, 72 minutes of the
120 allowed; the `recheck` artifact, 301 kB, is kept until 2027-01-10):

```
changed_quotes_present=711 gone=2 quote_vanished=29 unchanged=434 unreachable=81
27 source(s) newly dispute their facts (gone or quote_vanished) since the committed recheck.
```

18 of the 27 are `finlex-fi` pages, all HTTP 200 with the quote no longer found, which points at one host
changing how it serves its pages rather than 18 statutes changing. The others: `cartaidentita-interno-gov-it`,
`ktpae-gr` (two), `mai-gov-ro`, `mfa-bg`, `oenb-at`, `pgdlisboa-pt` (two), `rte-france-com`, `sg-mai-gov-pt`.
The two `gone` are `interoperable-europe-ec-europa-eu` pages. Nothing is committed by the run, by design (#98):
the committed `recheck.csv` still decides which facts the site shows as disputed. **Owner action**, per
`ci-cd.md`: `./run.sh recheck` locally (`./run.sh retry` for the rendered route if `finlex.fi` now needs it),
then `./run.sh data`, review, commit. The Monday 2026-10-13 run (38420627826) did not run the job: it was the
daily cron's run, which skips `live` and `sources`.

### 3. 27 of 138 commits on `main` carry a personal author address

```
git log origin/main --format='%ae' | awk '{print ($0 ~ /noreply/) ? "noreply" : "personal"}' | sort | uniq -c
 111 noreply
  27 personal
```

25 are the owner's, from the first weeks (September); 2 are a collaborator's merge commits of pull requests #2
and #3 on 2026-10-08, which the security gate blocked on their branches (11 red `security` runs, 2026-10-08
19:05 to 2026-10-09 01:29, all `BLOCK author-email`) and which reached `main` through GitHub's merge button, where
the gate does not run. The last one is `f38e727`, 2026-10-08. Rewriting history on a public `main` is a decision,
not an edit, and is not recommended here; the exposure is already public. Push protection (command A) does not
cover this; the local gate and `security.yml` do, for everything that goes through `git push`.

### 4. The `/ask` key expires 2026-11-05

Already in `TODO.md` with its steps and a calendar reminder for 2026-11-02. The daily monitor would catch a
lapse only after `/ask` is down.

### 5. The rollback step has never fired

Every deploy since #107 shows "Roll back to the previous production deployment: skipped", because nothing has
failed after an upload. Its condition and its URL argument are held by `tests/test_workflows.py`; the Opus 5.5
review of 2026-10-12 caught that the first version rolled nothing back. It stays **unverified by a real failure**.
A deliberate test would mean shipping a build that fails its own smoke test, so it waits for a real one.

### 6. Scheduled runs fire six to nine hours late

The daily `41 7 * * *` cron ran at 13:28, 12:43, 14:22, 14:36, 16:22, 14:27, 14:44, 14:56, 14:40, 13:57, 14:22,
17:00 and 15:16 UTC on consecutive days; the Monday `17 6 * * 1` cron ran at 15:22. GitHub delays scheduled
workflows on repositories with little activity. Nothing is wrong, but "daily 07:41" in the docs is the request,
not the time, and a Monday recheck can finish on Monday evening.

### 7. Documents that lag the pipeline

Found while comparing the docs with the workflow files; none changes behaviour. `ci-cd.md` is corrected in the
commit that adds this report. The rest is for the owner to schedule:

| Document | Says | Is |
|---|---|---|
| `DEPLOYMENT.md`, pipeline diagram | gate = model, PDFs, e2e → deploy → smoke of a few routes | the web job, the live `/ask` step, promote and rollback are missing; the smoke test covers every route, 28 PDFs, headers, TLS and the bundle |
| `DEPLOYMENT.md`, "same gate, same prebuilt upload" for `./run.sh deploy` | the manual path equals the workflow | it runs `./test.sh` and `factcheck.py gate` and uploads, with no tree-hash check, no smoke test, no promote and no rollback; its live group tests the previous deploy |
| `DEPLOYMENT.md`, "Vercel rebuilds these" | Vercel builds | Vercel never builds here: git deploys are off and every deploy is prebuilt |
| `docs/process.md`, Diagram 1 | PR: `./test.sh --no-pdf`; push: full `./test.sh`; `vercel build` builds web and PDFs again | parallel `gate.yml` jobs since #97; nothing is built twice |
| `DECISIONS.md` #106 | the rule "allows two commands and no others" | `.claude/settings.json` allows three exact pushes (`main`, `HEAD:main`, `sovereign-appliance-merge:main`) |
| `gate.yml`, header comment | "The four groups of `./test.sh --only`" | five (model, pdf, web, e2e, live); the test asserts five |
| `README.md` § The domain | iwantmyname "stays both registrar and DNS provider" | the nameservers are Vercel's since #90; `DEPLOYMENT.md` has it right |
| `TODO.md` | "Weekly source link check" open | done by the `sources` job (#98); ticked in this commit |
| `docs/plans/ci-cd-hardening.md`, action 3 and 4 status | "NOT YET applied", 2026-10-12 | still true on 2026-10-14 (above) |
| branch `ci/preview-workflow` (`9fd6b5a`, 2026-09-30, unmerged) | a PR preview deploy | uses `ubuntu-latest`, smoke-tests `/country/DE` (now a redirect), cites #82 for previews (#82 is the quote rule). Rebase or delete before reuse |

### 8. The local tree, before this session

Named before anything was touched, as the session rule asks:

- `sovereign-appliance` (`ffab934`) was 30 commits behind `origin/main` and 1 ahead, and not an ancestor of it:
  its decisions #101–#103 were renumbered to #103–#105 on `main` (`3c41351`). Local `main` was 35 behind.
- Seven files were uncommitted on it: the stichting refresh of 2026-10-08 and the `OUTREACH.md` NL change. See
  what this session did, below.
- Three worktrees under the scratchpad directory are prunable (`git worktree list`); `TODO.md` already asks for
  `git worktree prune`.

## What this session did to the tree

1. Removed the untracked `.claude/settings.json` (byte-identical to the one `main` tracks, #106), stashed the
   seven files, made `plans/stichting-refresh` from `origin/main`, applied the stash, resolved two placement
   conflicts, and committed in two: `1e1c713` (the stichting plan, its log and fetch log) and `dff7967`
   (`OUTREACH.md`, its changelog entry, the README deploy paragraph and layout fixes). The record of the
   conflicts is in `docs/plans/stichting-log.md`, entry 2026-10-14. The stash is kept as `stash@{0}` until the
   owner has seen the branch.
2. Fast-forwarded local `main` to `origin/main` and made `ci/status-2026-10-14` from it for this report, the
   `ci-cd.md` revision, the `TODO.md` ticks and the changelog entry.
3. Pushed nothing. Both branches wait for the owner's OK; the push to `main` is a production deploy (#81).

## Owner commands, in order

1. A, B, C from [`ci-cd-hardening.md`](ci-cd-hardening.md), then its read-only check.
2. `./run.sh recheck`, `./run.sh data`, review, commit: the 27 disputed sources.
3. Push `plans/stichting-refresh` and `ci/status-2026-10-14`, wait for the branch gates, then push each to
   `main` (`git push origin <branch>:main`). After B, `main` refuses a commit whose checks have not run.
4. `git branch -D sovereign-appliance` (its content is on `main` under new numbers and on `plans/stichting-refresh`),
   `git worktree prune`, `git stash drop` once `plans/stichting-refresh` is merged.
5. Before 2026-11-05: the `/ask` key.

## Where things are documented

| What | Where |
|---|---|
| How the pipeline works, by event and job | [`docs/ci-cd.md`](../ci-cd.md), revised with this report |
| The hardening list, the three owner commands, the review that followed | [`docs/plans/ci-cd-hardening.md`](ci-cd-hardening.md), #107 |
| The push rule for the assistant | `.claude/settings.json`, `tests/test_permissions.py`, #106 |
| What the workflow files must contain | `tests/test_workflows.py` |
| Topology, headers, domain, rollback, branch rules | [`DEPLOYMENT.md`](../../DEPLOYMENT.md) |
| Why | [`DECISIONS.md`](../../DECISIONS.md) #81, #87, #92, #97, #98, #106, #107 |
