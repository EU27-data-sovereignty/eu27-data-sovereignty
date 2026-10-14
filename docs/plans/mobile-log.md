# The mobile reader: what was done and decided

A log of the work behind [`mobile/`](../../mobile/README.md), newest first, in the shape of
[`technical-universities-log.md`](technical-universities-log.md). Each entry records who or what produced it,
what the owner asked, what was decided and why, what changed, how it was checked, and what is still open. The
decisions of record are `DECISIONS.md` #109 to #113; this log is the working narrative behind them, not a second
copy. Planning, not data: nothing here is read by the model, the book, the web app, `/ask` or the app.

## 2026-10-14 — the reader rebuilt on the content model, the edition channel built and proven locally

**Produced by.** Claude Fable 5.1 (`claude-fable-5-1`) in Claude Code, session
`https://claude.ai/code/session_01DjpW3YvBtYNeseYvKMKe7n`, on branch `mobile/rebuild` from `faa10cb`
(`ci/status-2026-10-14`). Three `Explore` subagents mapped the old reader, the schema-2 bundle contract and the
workspace template; two `Plan` subagents designed the app and edition channel, and the gate, CI and paperwork; the
plan was approved by the owner in plan mode before any file changed.

**Asked by the owner.** "make a mobile app with react native and supabase", then "as always include a
comprehensive test.sh", then "and document everything in markdown". Asked in planning, the owner chose: an EU-27
reader rather than a new app; Supabase in v1 as the edition channel, a hosted project in an EU region, over the
2026-10-03 plan's recommendation of no Supabase; offline-first with the bundle shipped in the app; the deploy
workflow as the only writer; English only, no store release, no EAS; replacing `mobile/` in this repo.

### Decisions

1. **Rebuild, not port** (#109). The old reader's 1,140 lines rendered schema-1 fields that no longer exist. The
   new app takes from `templates/rn-supabase` exactly: `.gitignore`, `.prettierrc`, `.prettierignore` (extended),
   `eslint.config.js`, `tsconfig.json` (extended), `jest.config.js` (rewritten), `expo-env.d.ts`,
   `package-lock.json` (reconciled with `npm install --save-exact` after the dependency list was cut to sixteen),
   `scripts/check-audit.mjs`, `audit-allowlist.json` (the same four advisories), `src/components/ErrorBoundary.tsx`
   (re-themed on the generated tokens), and the icon placeholders (replaced by generated EU-blue tiles). Everything
   else was written for this app. Kept from the old reader: `src/constants/Colors.ts` (generated), the pinned
   copies (regenerated from `web/`), `src/services/supabase.ts` (null when unconfigured, no auth), `.env.template`
   (the same two names), and the ideas of the parity and security suites.
2. **The parts are generated, the manifest tracked** (#110). A judgment call made in planning and stated as such:
   the 28 parts are a pure function of the committed 7.5 MB bundle, proven by `tests/test_export_split.py`;
   tracking them would add a second 7.5 MB per edition to history. One `.gitignore` line reverses it.
3. **One stdlib module, `model/edition.py`, for check, publish and verify** (#112), rather than curl lines or the
   Supabase CLI, so the publisher is unit-tested against a fake Storage server and run against the real one by the
   integration test, and `smoke.py` imports `verify` for the deploy and the weekly monitor.
4. **A separate `edition` job after the deploy job** (#112), not a step inside it: the service-role key is scoped
   to one job, the deploy job's rollback condition is untouched, and a publish can only follow a site that was not
   rolled back.
5. **The check for a newer edition is a tap, with an opt-in automatic check** (#111). A check on every launch would
   make "Data not collected" untrue of an app that contacts a host on every start.
6. **The integration round-trip runs in the deploy's gate only** (#113): `supabase start` pulls about a dozen
   images and would be the critical path of every branch push.

### What changed

- `model/export_json.py`: `split_bundle`, `merge_parts`, `write_split`, `index_entry`; `--split [DIR]`, `--from
  FILE`. `run.sh data`, `test.sh` (generated-files stage), `model/reproduce.py`, `init.sh` run the split.
- `model/edition.py` (new): `check`, `publish`, `verify`. `model/smoke.py`: `--edition-url`, `--manifest`, and
  `--site ''` to check the channel alone.
- `mobile/`: the app (`app/`, `src/`), `supabase/config.toml` and the bucket migration, `scripts/`,
  `__tests__/` (five suites plus the integration suite), `test.sh`, `run.sh`, `init.sh`, `README.md`.
- `.github/workflows/gate.yml`: jobs `mobile` and `mobile-integration`, input `mobile_integration`;
  `deploy.yml`: job `edition`, and `mobile_integration: true`; `monitor.yml`: the edition check;
  `dependabot.yml`: `/mobile`.
- `tests/`: `test_export_split.py`, `test_edition.py` (new); `test_workflows.py` (six groups, the `Edition`
  class), `test_evidence.py` (mobile surfaces and `test_the_mobile_app_shows_it`), `test_ignore_rules.py`.
- `.gitignore`; `model/national_ai_note.py` and `model/sovereign_appliance_note.py` skip `.expo`, `coverage`
  and `supabase` when scanning `mobile/`.
- Documentation: `DECISIONS.md` #109–#113, `CHANGELOG.md`, `README.md`, `CLAUDE.md`, `docs/testing.md`,
  `docs/ci-cd.md`, `DEPLOYMENT.md`, `ROADMAP.md`, `TODO.md`, `PROGRESS.md`, `artifacts/mobile/STYLE.md`,
  `docs/plans/mobile-app.md` (status), `docs/plans/stichting.md` (one line), this log.

### How it was checked

| Command | Result |
|---|---|
| `python3 -m unittest tests.test_export_split -q` | 13 tests, OK: round trip byte for byte, self-contained parts, every claim in exactly one state part, the two manifests the committed bundle's |
| `python3 -m unittest tests.test_edition -q` | 12 tests, OK: immutable, idempotent, the pointer last, altered bytes refused by name, the key never on stdout, in a URL or in the summary |
| `python3 -m unittest tests.test_workflows tests.test_evidence tests.test_ignore_rules tests.test_export_split tests.test_edition tests.test_repeatability -q` | 96 tests, OK |
| `python3 -m unittest tests.test_docs -q` | OK: #109–#113 carry every part |
| `cd mobile && ./test.sh --ci` | 20 steps PASS (gate and integration skipped by flag) |
| `cd mobile && npx jest --coverage` | 5 suites, 75 tests; 77.5% statements, 70.9% branches, 78.2% functions, 80.8% lines |
| `cd mobile && npx expo export --platform web` | one bundle, 7.8 MB, the 28 parts inside |
| `cd mobile && npm run doctor` | 21 of 21 |
| `cd mobile && node scripts/check-audit.mjs` | 5 root advisories, 4 allowlisted, 1 moderate noted, ok |
| `colima start && cd mobile && supabase start && ./test.sh --quick --ci --integration` | 9 of 9 integration steps passed against 127.0.0.1:54321 |
| `./test.sh --only mobile` | PASS |
| `python3 model/notes.py check` | four checkers, all pass with the rebuilt tree |
| `shasum -a 256 web/public/data/manifest.json mobile/assets/data/manifest.json` | identical, `3b5cd5208d5f8687…`; edition `1a970a50803fdee0…` |

### Mistakes made and corrected during the session

- A heredoc meant for `mobile/package.json` landed in the repository root and `npm install` ran there,
  overwriting the root `package.json`, its lockfile and `node_modules`. Restored with `git checkout --
  package.json package-lock.json` and a fresh `npm ci` at the root (12 entries, as before); the mobile install
  was redone with `npm --prefix mobile`.
- `prettier --write .` reformatted the parity-pinned copies and the generated parts, which failed the parity
  suite; `.prettierignore` now lists `assets/data/`, the three copies, the generated tokens and the lockfile.
- `android.usesCleartextTraffic` is not in SDK 57's app config schema (expo-doctor); dropped, and the security
  test now asserts that nothing re-enables cleartext instead.
- The `tooling` step's grep for EAS matched its own pattern in `test.sh`; it now scans the five files that could
  name EAS.

### Still open

- **The hosted Supabase project** (owner): an EU-27 region, the migration applied, the repository variable
  `SUPABASE_URL` and the `production` secret `SUPABASE_SERVICE_ROLE_KEY`. Until then the deploy's `edition` job
  is skipped and the weekly check reports "not configured".
- **A reading on a device by a person.** The app has run under Jest and as a web export; `./run.sh ios` has not
  been opened in a simulator in this session.
- **The first Actions timings** of the `mobile` and `mobile-integration` jobs; the ruleset context after two
  weeks (#113).
- **The four Dependabot alerts**, to be dismissed by the owner with the allowlist's reasons.
- **A signed manifest**, so the channel proves authorship and not only integrity (#111).
- **The push to `main`.** The branch is pushed first; `main` only after the owner's OK and `/factcheck` status
  (`./run.sh factcheck status`: no printed fact changed in this work, so nothing is due).
