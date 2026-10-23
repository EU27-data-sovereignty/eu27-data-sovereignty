# CLAUDE.md

Project instructions for AI assistants working in `eu27-data-sovereignty`. The workspace rules in
`~/dev/CLAUDE.md` apply as well: the security gate, noreply identity, exact pins, and confirming before
push or deploy.

## Overview

**Always optimize for maximum auditability.** When choosing between approaches, prefer the one a third
party can check. Record who or what produced each output: the model id, the run, the commit and the input
hashes. Commit the evidence rather than relying on it, and generate audit trails from the data instead of
writing them by hand.

A sourced analysis of each EU member state's critical government data holdings, and of what sovereign
hosting for them requires.
- **Scope: the 27 member states of the European Union, and only those.** Austria, Belgium, Bulgaria, Croatia,
  Cyprus, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania,
  Luxembourg, Malta, the Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain and Sweden, keyed by
  Eurostat's codes (Greece is `EL`). Not the EEA states, the United Kingdom, Switzerland, candidate countries or
  the EU institutions as holders of data in their own right: every register, indicator, ranking, page, PDF and
  language draft is per member state, and a change to this scope is a decision, not an edit.
- **Research.** Agents stage claims; `model/research.py` admits only claims whose quote is found in a
  fetched, hashed document and whose categorical label an independent reviewer agrees with (#79).
- **Rendering.** One content model (`model/document.py`) renders everything: the EU-27 report and 27
  country PDFs (typst), the React web app, the markdown briefs, the posters and the `/ask` corpus.
- **Stack.** Python is stdlib-only. The web app is React 19, Vite and Tailwind 4 in `web/`. `/ask` is a
  Vercel Function in `api/`.
- **Deployment.** Vercel at `https://eu27.cloud`. A push to `main` runs the gate, builds in GitHub Actions and
  deploys prebuilt (#81). The deploy also requires every printed fact to be checked by the model that did not
  write it (#87).

Read [`METHOD.md`](METHOD.md) for the evidence pipeline and [`DECISIONS.md`](DECISIONS.md) before
changing a rule. From #72 on, a new decision entry needs every part listed in `README.md` § How decisions
are recorded: `tests/test_docs.py` enforces it.

## Commands

```
./test.sh                              # the full gate; run before every commit
./test.sh --no-e2e                     # without Playwright
./test.sh --no-pdf                     # without compiling the PDFs (otherwise missing typst fails)
./test.sh --no-live                    # without the live /ask check (one real API call to eu27.cloud)
./test.sh --no-mobile                  # without the mobile reader's suite (no mobile/node_modules)
./test.sh --only model|pdf|web|mobile|e2e|live [--project NAME]   # one stage group; CI runs them as parallel jobs (#97, #113)
./run.sh                               # dev server, http://localhost:5173
./run.sh data                          # regenerate briefs, bundle, the split edition (mobile/assets/data, #110) and /ask corpus (pins the epoch)
./run.sh artefacts                     # re-render the 27 tracked posters (needs Chrome)
./run.sh export                        # EU-27 report + 27 country PDFs into book/build/
git push origin main                   # PRODUCTION deploy via .github/workflows/deploy.yml; allowed by .claude/settings.json (#106), still only after the owner's OK in the conversation
./run.sh deploy                        # manual fallback: gate, local vercel build, prebuilt PRODUCTION deploy

python3 model/document.py --check      # every fact shown resolves to a checked source
python3 model/sovereignty.py [ISO]     # ranking placements, range and confidence
python3 model/research.py verify [--iso XX]   # fetch, hash, quote-check staged research (slow, polite)
python3 model/research.py admit        # write verified + reviewed claims into the registers
python3 model/research.py report       # verification outcomes per state
./run.sh admit [--check]               # research then vetting admission; --check: registers reproduce (#84)
./run.sh recheck [--check]             # re-fetch every source behind a printed fact; resumable (#83)
                                       # --check: exit 1 on a source newly gone or missing a quote (weekly in CI, #98)
./run.sh retry                         # not-found quotes: served page in its charset, then rendered; admit
./run.sh eurostat check|adopt COL=PERIOD   # Eurostat vintages; pins are data (model/eurostat_pins.csv)
./run.sh vet prepare|stage|hosts|verify|admit|report|manifest   # vetting run; the agent step is /vet
./run.sh vet prepare --withheld; ./run.sh vet stage <out> --run <id> --round   # correction round (#93)
./run.sh reproduce [--evidence]        # rebuild everything from a fresh clone of HEAD and compare (#84)
./run.sh contrib forms|ingest|status|audit-sample   # citizen submissions and reviews; two-person rule (#85)
./run.sh factcheck status|gate        # cross-model fact check: what is due; the deploy gate (#87)
./run.sh factcheck prepare|stage|record|audit|replay   # a fact-check run (docs/fact-check.md); agent step /factcheck
python3 model/evidence_report.py       # docs/evidence.md, charts of grades and tiers (run by ./run.sh data)
python3 model/gaps.py [--csv out.csv]  # docs/gaps.md: every gap and how often it was searched (run by ./run.sh data)
python3 model/provenance.py            # source register coverage per namespace
./run.sh national-ai check|links       # the authored note NATIONAL-AI-STRATEGIES.md: its contract; or refetch every URL into the link register (#103)
./run.sh appliance check|links         # the authored note SOVEREIGN-APPLIANCE.md: its contract; or refetch every URL into the link register (#104)
python3 model/i18n_drafts.py check|summary   # the 27 language drafts: complete and cross-reviewed; or rewrite docs/i18n/README.md's table
python3 model/i18n.py strings|admit|check|why   # the bundle's labels into STRINGS-reader.md; admit read drafts into model/i18n/ and the reader's catalogue (#117)
python3 model/technical_universities_note.py check|links   # the authored note TECHNICAL-UNIVERSITIES.md: its contract; or refetch every URL into its link register
python3 model/draghi_note.py check|fetch|quotes|links   # the authored note DRAGHI-REPORT.md: its contract; restore the PDFs; regenerate the quote register from the PDFs; refetch URLs (#118)
python3 model/notes.py check|list      # every registered note and draft checker in one go: the test.sh stage; a new note registers here
python3 design/build_tokens.py         # regenerate design tokens (web CSS, typst, mobile)

cd mobile && ./init.sh                 # the reader: npm ci, the 28 parts, an .env.local you may leave empty (#109)
cd mobile && ./test.sh [--quick|--integration|--offline|--ci]   # its full suite; --integration needs colima start && supabase start
cd mobile && ./run.sh web|ios|android  # the app; unconfigured, it reads its bundled edition and makes no request
cd mobile && ./run.sh release          # the EAS release workflow by hand (#114); the deploy's `app` job runs it after the gate
cd mobile && ./run.sh release record <build-id>   # append an EAS build to mobile/releases.csv (model/release.py)
cd mobile && ./run.sh build ios|android | update "<msg>" | metadata lint|push|pull   # one EAS step by hand; push needs EAS_REVIEW_EMAIL/PHONE
python3 model/export_json.py --split --from web/public/data/eu27.json   # the 28 parts + manifest from the committed bundle
python3 model/edition.py check|publish|verify   # the edition channel: the tree, the deploy's publisher, the bucket read back (#112)

vercel build --yes && vercel deploy --prebuilt --yes            # protected preview
vercel curl <path> --deployment <preview-url> -- -sS            # previews need auth; plain curl gets 302
```

## Architecture (only the non-obvious)

- **Every fact is a span with claim ids.** `document.py` emits spans with a role: `fact`, `gap`,
  `method` or `label`. A value is a `fact` only if `Sources.supported(claim)`; otherwise it becomes a
  `gap`. Renderers never add content. Adding a new field means adding a claim kind, a citation and a
  span, not a string in a component.
- **Claims** are `param:<ISO>:<col>`, `record:<ISO>:<class>:<kind>` and `indicator:<ISO>:<id>`, resolved
  through `model/sources/{registry,citations}.csv`.
- **Staging is not data.** `model/research/*.json` is agent output and is never rendered. Only
  `research.py admit` moves claims into `national_data.csv`, `sovereignty_indicators.csv` and `sources/`.
- **The ranking has no score.** `sovereignty.py` returns group ids and a range. Tests fail on a numeric
  score (#10, #77).
- **The EU-27 overview copies spans** (#95). `document.infrastructure()` builds "Key infrastructure and
  hosting" from the country documents' holdings tables, never from the registers. It sits in
  `bundle["infrastructure"]`, outside `documents`, so it adds no facts to check or count. Its counts are of
  printed facts only. Renderers: `Report.overview` (PDF), `countries/EU-INFRASTRUCTURE.md`,
  `/infrastructure`, and `/ask`. Structured operators are planned (#96, `docs/hosting-operators.md`).
- **`/ask`.** `api/_ask-core.ts` holds all the logic with a structural client, so the web Vitest suite
  tests it without the SDK. `api/ask.ts` wires the real SDK, and a compile-time assignment proves the
  request type-checks. The root `package.json` and `tsconfig.json` exist only for `api/`.

## Gotchas

- **The pinned build date.** Generation stamps `SOURCE_DATE_EPOCH` from `.build-epoch`. Running a
  generator without it (e.g. plain `python3 model/generate_countries.py`) writes today's date, and the
  gate reports "generated files are stale". Use `./run.sh data`, or export the epoch first.
- **Posters go stale on any bundle change.** `countries/ARTEFACTS.csv` pins the bundle hash, so
  re-render all 27 with `./run.sh artefacts` after regenerating, or `tests/test_artifacts.py` fails.
- **Coverage floors are a ratchet.** `tests/test_provenance.py` `FLOORS` and
  `tests/test_national_data.py` `NATIONAL_DATA_FLOOR` must be **raised** when coverage grows. Lowering
  one needs a recorded reason (see the comment on `record`).
- **No fact without its evidence, as printed** (#82). A value renders only if a citation with a recorded
  quote check backs it *and* every number and date in the printed text is in the original-language quote
  (`evidence.value_in_quote`). Every output carries `evidence.DISCLAIMER`; never write prose claiming a
  check that did not run (`tests/test_evidence.py`).
- **Source tiers live in `model/sources/authorities.csv`** (#83). A new cited host must be classified there
  or the build fails. Unofficial statute mirrors are T4, never T1.
- **Citizen input is staging, never data** (#85). Issues are read with `gh api` (read-only) into
  `model/research/contrib/`. A person's review counts only under the two-person rule (`contrib.eligible`).
  The issue forms are generated (`contrib.py forms`); never edit them by hand. Posting anything to GitHub
  (a comment, a label) is outward-facing, so get the owner's OK first.
- **Changelog in the same commit.** A change a reader can see, or to how evidence is produced, adds its
  entry to `CHANGELOG.md` (newest first, citing its decision) in the same commit; a new stage adds a row to
  the README's Changelog table.
- **Never admit unreviewed labels.** Categorical values (foreign dependency, indicator values) need an
  agreeing verdict in `model/research/dependency_review/` or the indicator `review` block (#79). Seven of the
  eight "Dependent" placements in the first, unreviewed ranking did not survive review.
- **The security gate blocks email-shaped strings.** They have come in through archive URLs, and through a
  fact checker quoting a contact address (`factcheck._clean` now removes them at staging). Archived
  copies are accepted only for exactly the requested host (`research.snapshot_matches`). Fix the data;
  never bypass the gate.
- **Any change to a printed fact needs `/factcheck` before pushing to `main`** (#87). The deploy's
  fact-check gate fails on a printed fact that is new, changed or checked by its own author, and on a stale
  `docs/fact-check-audit.md`. A fact the checker did not confirm is withheld as disputed, not printed (#89):
  `document.Sources.withheld`, keyed on the fact's hash. The gate is not in `./test.sh`, so branches stay unblocked; run
  `./run.sh factcheck status` to see what is due. Never edit the ledger or a verdict to pass it.
- **The assistant may push to `main`, and only there** (#106). The tracked `.claude/settings.json` allows `git push origin
  main`, `git push origin HEAD:main` and the merge branch's push to `main`, exact forms only, and denies by prefix a
  delete of `main`, a force push, direct `vercel --prod` deploys and `gh` writes to the repository's settings. The
  allow is not consent: the owner's OK in the conversation still comes first, and the
  security gate, the Actions gate and the fact-check gate run exactly as before.
- **Push the branch first, then `main`** (#107). Once the owner applies `.github/rulesets/main.json` (NOT YET as of
  2026-10-12; `docs/plans/ci-cd-hardening.md`), `main` accepts only a commit whose fast checks have passed, and
  `ci.yml` runs them on every branch push, so: push the branch, wait for green (about five minutes), then
  `git push origin HEAD:main`. The same ruleset refuses force pushes and deletions of `main`. The deploy workflow
  rolls back to the recorded previous deployment when the smoke test or the live `/ask` check fails; that step has
  never fired, and its shape is held by `tests/test_workflows.py`.
- **A push to `main` is a production deploy** (#81), gated by `./test.sh` in Actions, run as the parallel jobs of
  `.github/workflows/gate.yml` (#97). The deploy ships the gate's own build (`web-dist` and `pdfs` artifacts,
  `PREBUILT_SITE=1`), never a second one. A new `./test.sh` stage must sit inside an `in_group` block, or
  `tests/test_workflows.py` fails. The PDFs need `typst`,
  which Vercel's image lacks, so every deploy is prebuilt (CI pins and checksums typst). The build command runs
  `npm ci` at the root (for `api/`) and in `web/`. Previews are by hand and sit behind Vercel login.
- **Pin every action by SHA** in `.github/workflows/`, and checksum any downloaded binary
  (`tests/test_workflows.py`).
- **SPA rewrite.** It must target `/index` under `cleanUrls` (`tests/test_vercel_config.py`).
- **A member state is at its code: `/de`, `/el`** (#105). Build every country link with `countryPath` in
  `web/src/utils/routes.ts`; `/country/:iso` is a redirect, and no new top-level route may be two letters
  (`tests/test_vercel_config.py`). Static segments rank ahead of `:iso`, so `/ask` is never read as a country.
- **zsh.** `echo ====` breaks, because a leading `=` is command expansion; use `echo '---'`.
- **Holdings-table columns are looked up by name.** The overview (`document.holdings_rows`) and
  `/holdings/<class>` read the columns by their label, so renaming a column label changes both. `ask_corpus`
  still reads `row[1]` and `row[2]`, so keep the holding and register in those positions.
- **Withheld labels still feed counts.** `exposure_section` and `sovereignty.py` read the raw
  `foreign_dependency`, including labels the report withholds (TODO.md). Don't build new counts that way.
- **The mobile reader renders the split edition** (#109, #110). The 28 parts under `mobile/assets/data/` are generated
  from the committed bundle and gitignored; only `manifest.json` is tracked, and it must equal
  `web/public/data/manifest.json` (`./run.sh data` writes both). `mobile/src/data/{types,format,sources}.ts` are
  byte-for-byte copies of the web's files: edit the web file, copy it, same commit. Only the deploy's `edition` job
  writes the Supabase bucket, with a key that is never on a command line (#112); the app has no write path (#111).
- **The reader is released through EAS, and the last click is the owner's** (#114–#116). The deploy's `app` job starts
  `mobile/.eas/workflows/release.yml` for the deployed commit once `EXPO_PROJECT_ID` is set: build on a native change,
  TestFlight, `require-approval` in the Expo dashboard, the upload to App Store Connect; "Submit for Review" and
  "Release" stay manual there (the launch gate, #25). **A push to `main` is therefore also an over-the-air update of
  the app's JavaScript** when the native fingerprint is unchanged, fetched only when a reader taps "Check for a newer
  edition" (`checkAutomatically: NEVER`, #115). The EAS CLI is `npx eas-cli@<exact>`, one pin in `mobile/eas.json`
  (`cli.version`) and `deploy.yml` (`EAS_CLI`), never a project dependency, which `expo-doctor` refuses
  (`mobile/test.sh` `tooling`; `./run.sh eas <args>` runs it); the workflow may have no `push` trigger and no `submit` without an
  approval; the Expo token lives only in the `production` environment, read from env, never argv
  (`tests/test_workflows.py` `App`). Credentials live on EAS; no key, keystore or `credentials.json` may be committed.
  `store.config.json` has no e-mail: the review contact comes from `EAS_REVIEW_EMAIL`/`EAS_REVIEW_PHONE` at push time.
  `mobile/releases.csv` is generated by `./run.sh release record`, never edited. `/privacy` is the policy the stores
  link to (`tests/test_privacy.py`); a processor added anywhere must be named there.
- **`NATIONAL-AI-STRATEGIES.md` is authored, not generated** (#103). It is never read by the model, the book, the web
  app or `/ask`; `tests/test_national_ai.py` fails if any of them names it. Edit it by hand, keep every snapshot cell
  sourced with an access date or marked **[unverified]**, put no cost figure in a strategy, no ranking language anywhere,
  and run `./run.sh national-ai links` after adding or changing a URL so the link register matches.
- **`SOVEREIGN-APPLIANCE.md` is authored, not generated** (#104), under the same contract shape: never read by the model,
  the book, the web app or `/ask` (`tests/test_sovereign_appliance.py`); no ranking language, no currency figure anywhere,
  a member state named only in its Precedents and Sources sections and there only with a URL and access date or
  **[unverified]**; `./run.sh appliance links` after adding or changing a URL.
- **The language drafts are staging, never rendered; the catalogue is admitted from them** (#117).
  `docs/i18n/drafts/<ISO>.md` are machine translations of `docs/i18n/STRINGS.md` (45 chrome strings) and, in a
  "Reader strings" part, `docs/i18n/STRINGS-reader.md` (the reader's strings plus the content model's labels and gaps,
  whose table `model/i18n.py strings` generates), drafted by one agent and reviewed by the agent on the other model;
  `tests/test_i18n_drafts.py` fails if a renderer, the reader included, names them. Only `model/i18n.py admit` reads
  them, and it admits a state's language column only with both parts reviewed, every `fix` applied as `fixed`, and a
  `- Read by (<lang>): <role>, <date>` line: a native speaker's reading, recorded by role, never by name. No person has
  read one yet, so the catalogue is English only. Never edit `model/i18n/` or `mobile/assets/i18n/` by hand. The web
  stage of `docs/plans/localisation-plan.md` needs its own decision entry.
- **`TECHNICAL-UNIVERSITIES.md` is authored, not generated** (#108). Per state, the institutions on a named published
  list (CESAER, EuroTech) or the state's technical university cited from a fetched page, else **[unverified]**, or one
  `none: searched <date>` row; alphabetical
  within a state, no ranking word anywhere, every URL in `docs/technical-universities-links.csv`
  (`python3 model/technical_universities_note.py links` after a change). Never rendered.
- **`DRAGHI-REPORT.md` is authored, not generated** (#118). Quote the report only as `“…” (A|B p. N)`, N being the PDF
  page (Part A's printed folio is two lower), then run `python3 model/draghi_note.py quotes`: it regenerates
  `docs/draghi-quotes.csv` from the note and re-finds each quotation in the hashed PDF. Never edit the register by
  hand. A state fact is a claim id with its printed text, `` `record:XX:…` reads “…” ``, and `check` compares it with
  the bundle: after `./run.sh data` changes a cited fact, re-read the entry. Never cite a withheld fact. The PDFs are
  gitignored under `assets/reports/MANIFEST.csv`; `fetch` restores them, and without them `check` skips re-finding
  the quotes and says so.
- **A new authored note or draft set registers in `model/notes.py`** (#108), never as a new `test.sh` stage: one stage runs the
  register, and `tests/test_notes.py` fails on a `model/*_note.py` that is not in it.
