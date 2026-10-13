# 2026-10-12 to 13: every decision and change of the session

The one place that lists what this session decided, changed, checked and left open, with a pointer to where each
item is recorded in full. The decisions of record are `DECISIONS.md` #105 to #108; the reader-facing entries are in
`CHANGELOG.md` under 2026-10-12; the three working logs are [`country-paths-log.md`](country-paths-log.md),
[`ci-cd-hardening.md`](ci-cd-hardening.md) and [`technical-universities-log.md`](technical-universities-log.md),
and the plan is [`localisation-plan.md`](localisation-plan.md). Planning, not data: nothing here is read by the
model, the book, the web app or `/ask`.

**Produced by.** Claude Fable 5.1 (`claude-fable-5-1`) in Claude Code, session
`https://claude.ai/code/session_01JzrUgU5ZozYWCPBXUD2b5w`, with subagents named per item. Every commit passed the
security gate; every push to `main` had the owner's OK in the conversation and ran as a production deploy.

## 1. What the owner asked, in order

1. One address per member state, `eu27.cloud/de` as the example.
2. Whether a mobile app exists (answered: a stale, local-only Expo reader in `mobile/`, schema-1 bundle; `mobile-app.md`).
3. Push everything; then a next todo.
4. Why the assistant could not deploy; then a permission rule for this project that keeps every safety, privacy and
   data-integrity rule, documented in markdown.
5. A plan for country URLs; `CLAUDE.md` to name the 27 states as the scope; language drafts for all 27 states,
   checked by two different agents; all in markdown.
6. Whether the CI/CD is strong enough; the actions that least slow development; do them all, following the i18n
   standards, with a thorough `test.sh`; a quality check by a different model, then push.
7. The top technical schools of every state in a suitably named markdown file; everything in `test.sh` without bloat.
8. All decisions and changes documented in markdown (this file and the universities log).

## 2. Decisions

Numbered entries carry Decision, Problem, Alternatives with *Why not*, Closes off, Verified and *Would change if*.

| # | Decision, in one line | Record |
|---|---|---|
| 105 | A member state's page is its lower-case code as a top-level path (`/de`, `/el`), not a subdomain; `/country/<ISO>` redirects; no other two-letter route. | `DECISIONS.md` #105; `country-paths-log.md` |
| 106 | A tracked `.claude/settings.json` allows the assistant exact push forms to `main` and denies every other outward action by name; the owner's OK still precedes each push. | `DECISIONS.md` #106; `country-paths-log.md` §3 |
| 107 | The deploy records the production target, promotes the deployment that passed and rolls back by URL on a failed smoke test; `main` has a ruleset (in tree, NOT YET applied); runner pinned to `ubuntu-24.04`; Dependabot security-only. Required reviews, a staging environment and visual regression in CI rejected. | `DECISIONS.md` #107; `ci-cd-hardening.md` |
| 108 | The technical universities are an authored note on named published lists, never a ranking; every note's checker runs through `model/notes.py`, one `test.sh` stage. | `DECISIONS.md` #108; `technical-universities-log.md` |

Decisions without a number, each recorded where it was made:

- The branch's #101 to #103 were renumbered to #103 to #105 because `main` had taken #101 and #102 (commit
  `3c41351`; `country-paths-log.md` §2).
- The appliance note and the country paths were cut as two commits, the appliance first, so decision numbers stay
  contiguous (`f73c24a`, `0a64633`).
- Other sessions' uncommitted work in the same checkout was left untouched; the day's work ran in a worktree on
  `sovereign-appliance-merge`.
- The language drafts are staging, never rendered, and the plan that would admit them reserves #109, not yet
  written; the URL scheme will be `/<iso>/<lang>`; BCP 47 tags, Unicode NFC, ICU MessageFormat and `Intl` are the
  standards (`localisation-plan.md` §3, §3a, §6).
- A second agent on the same model is not the cross-model check of #87; the note and #108 were corrected to say so
  and the cross-model check was run (`6747558`).
- In `dotfiles`, policy §5 names a per-project allow rule for one outward command as a sanctioned pattern, with
  this project as the example (`893d744` there, NOT YET pushed).

## 3. Commits on `main`, in order

| Commit | What | Decision |
|---|---|---|
| `0a64633` | Each member state at its code; `/country/<ISO>` redirects | #105 |
| `3c41351` | Renumber #101–#103 to #103–#105 | — |
| `b7f5931` | Merge `origin/main` (landing design, guide pages); six conflicts by hand | — |
| `2ead774` | Track `.claude/settings.json` | #106 |
| `7f265ac` | `country-paths-log.md` | #105, #106 |
| `9e264bf` | The first push under #106 recorded: run 38334656899, the live redirect | #106 |
| `56d1fea` | 27 language drafts, cross-reviewed by two agents on two models; the localisation plan; `CLAUDE.md` scope | plan |
| `0635ca4` | Drafts follow the i18n standards; the checker enforces BCP 47 and NFC | plan |
| `79fe268` | Rollback, ruleset, pinned runner, Dependabot security-only, `ci.yml` on every branch | #107 |
| `4182d8c` | The Opus 5.5 quality review applied: a rollback that rolls back, an allow that cannot delete `main`, honest tense, corrected verdicts | #106, #107 |
| `88ecf9b` | Changelog: no citation of #109 before it exists | — |
| `d7a8f79` | `deploy.yml` records the project's production target; a failed promote fails the step | #107 |
| `3fe96b5` | A failed promote does not trigger the rollback | #107 |
| `79fdf01` | `TECHNICAL-UNIVERSITIES.md`, its checker and register; one `test.sh` stage for every note | #108 |
| `96991e6` | The second Opus 5.5 review applied: LU and SI "none found", #108 written, the register's headline, the ranking list | #108 |
| `6747558` | The same-model review named as such; the Fable 5.1 cross-model check recorded | #108 |

Pushes to `main` and their deploy runs, every one green: `7f265ac` 38334656899, `56d1fea` 38340306619, `79fe268`
38341578281, `3fe96b5` 38344010621, `6747558` 38345425553. The last two ran the new record and promote steps; the
rollback step was skipped in both because nothing failed.

## 4. What changed, by area

- **Web app.** `web/src/utils/routes.ts` (`countryPath`), `App.tsx` (`:iso` route after the static ones, redirects
  for `/country/:iso` and upper-case codes), `vercel.json` (permanent redirect), six link sites; Playwright and
  smoke route lists; three visual baselines renamed.
- **Permissions.** `.claude/settings.json` tracked: three exact allows, twelve denies (deletes, `+` refs, force
  pushes, `vercel --prod`, `gh repo edit`, `gh api` writes). `tests/test_permissions.py` holds the shape.
- **Pipeline.** `deploy.yml` record, promote and rollback steps; `ci.yml` on every branch push with per-ref
  concurrency; `.github/rulesets/main.json`; `.github/dependabot.yml`; every workflow on `ubuntu-24.04`;
  `tests/test_workflows.py` checks each.
- **Localisation.** `docs/i18n/STRINGS.md` (45 keys, languages and BCP 47 tags per state, the standards),
  `docs/i18n/drafts/<ISO>.md` ×27 (agent A `claude-opus-5-5` drafted 14 states, agent B `claude-fable-5-1` 13, each
  reviewed the other's every cell: 1,440 cells, 1,398 `ok`, 42 `fix`), `docs/i18n/README.md`,
  `model/i18n_drafts.py` (`check`, `summary`), `tests/test_i18n_drafts.py`, `docs/plans/localisation-plan.md`.
- **Universities.** `TECHNICAL-UNIVERSITIES.md`, `docs/technical-universities-links.csv`,
  `model/technical_universities_note.py`.
- **The gate.** `model/notes.py` and `tests/test_notes.py`; `test.sh` at 18 stages; `docs/testing.md` renumbered.
- **Docs.** `CLAUDE.md` (scope line, commands, gotchas for #105 to #108, the drafts, the register), `DECISIONS.md`
  #105 to #108, `CHANGELOG.md` 2026-10-12, the four plan documents and this index.

## 5. The reviews, and what each caught

| Round | Reviewer | Scope | Found |
|---|---|---|---|
| 1 | `claude-opus-5-5`, independent agent | the day's eleven commits | `vercel rollback` without an argument rolls nothing back (CLI 61 prints a status, exit 0); the allow `git push origin *:main` matched a delete and a force push; present tense for the unapplied ruleset; three French honesty notices passed as `ok` with "machine-checked" rendered as *verified*; LU exposure suggestions repeating rejected causation wording; drafts citing #105; `docs/testing.md` stale; four tests passing on broken input |
| 2 | same reviewer, follow-up | `deploy.yml` | the record step must read `targets.production.url`, not the newest deployment; the promote step needs `set -e`; then a nit, the rollback must not run on a failed promote |
| 3 | `claude-opus-5-5`, separate session | the universities note | LU and SI general universities as stand-ins; no #108; ranking-word list; a date that read as the capture date; the C3 choice wording; the register headline; the `-f` regex; a blank line |
| 4 | the owner's standard applied | labels | round 3 was called "second-model"; it is the same model; corrected |
| 5 | `claude-fable-5-1` agent | every C1, C2 and C3 row against its page | zero discrepancies; the live cesaer.org page reached, same 44 members, one renamed |

Everything found was applied before the next push to `main`.

## 6. Verification record

| Check | Where | Result |
|---|---|---|
| `./test.sh --no-live` | merged tree, and again on `6747558` | 18 stages, exit 0 |
| `./run.sh factcheck status` | merged tree | 1490 of 1490 printed facts checked, checker ≠ author |
| `python3 model/i18n_drafts.py check` | `0635ca4` on | 27 files, 1,440 cells, 0 problems |
| `python3 model/notes.py check` | `96991e6` on | four checkers `ok` |
| `python3 model/technical_universities_note.py check` | `6747558` | 27 states, 61 rows, 0 problems |
| Actions on `sovereign-appliance-merge` before each push | branch | all checks green (22 on the last push) |
| Deploy runs listed in §3 | `main` | five green; record and promote ran on the last two |
| `curl -sI https://eu27.cloud/country/DE` | production | 308 to `/DE`, then `/de` serves 200 |

## 7. NOT YET, said out loud

- The ruleset on `main`, secret scanning with push protection, and Dependabot security updates are repository
  settings the assistant's own rule denies; the three commands are in `ci-cd-hardening.md`. Until B runs, a push to
  `main` is not held to the fast checks.
- The rollback step has never fired. Its argument, order and guard are tested; its effect is not.
- No person has read the 27 language drafts or the universities note. The 42 `fix` cells are not applied.
- Decision #109 (localisation) is reserved, not written; nothing renders a draft.
- `dotfiles` commit `893d744` is not pushed.
- The `sovereign-appliance` branch in the owner's checkout sits at `0a64633` with other sessions' uncommitted files
  (the stichting plan, `OUTREACH.md`, a README paragraph); not touched.

## 8. Open, and whose

- Owner: commands A, B, C; push `dotfiles`; read the note and a draft or two; reset `sovereign-appliance` to `main`
  once the stichting files are committed or stashed; `git worktree prune` after.
- Next content todo: print `eu27.cloud/<iso>` on the country PDFs and posters (a `label` span, a changelog entry,
  `/factcheck`).
- Localisation stage 1: apply the 42 fixes, a native reading, then #109.
- The mobile reader to schema 2 (`TODO.md`).
