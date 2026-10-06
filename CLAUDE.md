# CLAUDE.md

Project instructions for AI assistants working in `sovereign-data-centers`. The workspace rules in
`~/dev/CLAUDE.md` apply as well: the security gate, noreply identity, exact pins, and confirming before
push or deploy.

## Overview

**Always optimize for maximum auditability.** When choosing between approaches, prefer the one a third
party can check. Record who or what produced each output: the model id, the run, the commit and the input
hashes. Commit the evidence rather than relying on it, and generate audit trails from the data instead of
writing them by hand.

A sourced analysis of each EU member state's critical government data holdings, and of what sovereign
hosting for them requires.
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
./test.sh --only model|pdf|web|e2e|live [--project NAME]   # one stage group; CI runs them as parallel jobs (#97)
./run.sh                               # dev server, http://localhost:5173
./run.sh data                          # regenerate briefs, bundle and /ask corpus (pins the epoch)
./run.sh artefacts                     # re-render the 27 tracked posters (needs Chrome)
./run.sh export                        # EU-27 report + 27 country PDFs into book/build/
git push                               # to main = PRODUCTION deploy via .github/workflows/deploy.yml; owner's OK first
./run.sh deploy                        # manual fallback: gate, local vercel build, prebuilt PRODUCTION deploy

python3 model/document.py --check      # every fact shown resolves to a checked source
python3 model/sovereignty.py [ISO]     # ranking placements, range and confidence
python3 model/research.py verify [--iso XX]   # fetch, hash, quote-check staged research (slow, polite)
python3 model/research.py admit        # write verified + reviewed claims into the registers
python3 model/research.py report       # verification outcomes per state
./run.sh admit [--check]               # research then vetting admission; --check: registers reproduce (#84)
./run.sh recheck                       # re-fetch every source behind a printed fact; resumable (#83)
./run.sh retry                         # not-found quotes: served page in its charset, then rendered; admit
./run.sh eurostat check|adopt COL=PERIOD   # Eurostat vintages; pins are data (model/eurostat_pins.csv)
./run.sh vet prepare|stage|hosts|verify|admit|report|manifest   # vetting run; the agent step is /vet
./run.sh vet prepare --withheld; ./run.sh vet stage <out> --run <id> --round   # correction round (#93)
./run.sh reproduce [--evidence]        # rebuild everything from a fresh clone of HEAD and compare (#84)
./run.sh contrib forms|ingest|status|audit-sample   # citizen submissions and reviews; two-person rule (#85)
./run.sh factcheck status|gate        # cross-model fact check: what is due; the deploy gate (#87)
./run.sh factcheck prepare|stage|record|audit|replay   # a fact-check run (docs/fact-check.md); agent step /factcheck
python3 model/evidence_report.py       # docs/evidence.md, charts of grades and tiers (run by ./run.sh data)
python3 model/provenance.py            # source register coverage per namespace
python3 design/build_tokens.py         # regenerate design tokens (web CSS, typst, mobile)

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
- **A push to `main` is a production deploy** (#81), gated by `./test.sh` in Actions, run as the parallel jobs of
  `.github/workflows/gate.yml` (#97). The deploy ships the gate's own build (`web-dist` and `pdfs` artifacts,
  `PREBUILT_SITE=1`), never a second one. A new `./test.sh` stage must sit inside an `in_group` block, or
  `tests/test_workflows.py` fails. The PDFs need `typst`,
  which Vercel's image lacks, so every deploy is prebuilt (CI pins and checksums typst). The build command runs
  `npm ci` at the root (for `api/`) and in `web/`. Previews are by hand and sit behind Vercel login.
- **Pin every action by SHA** in `.github/workflows/`, and checksum any downloaded binary
  (`tests/test_workflows.py`).
- **SPA rewrite.** It must target `/index` under `cleanUrls` (`tests/test_vercel_config.py`).
- **zsh.** `echo ====` breaks, because a leading `=` is command expansion; use `echo '---'`.
- **Holdings-table columns are looked up by name.** The overview (`document.holdings_rows`) and
  `/holdings/<class>` read the columns by their label, so renaming a column label changes both. `ask_corpus`
  still reads `row[1]` and `row[2]`, so keep the holding and register in those positions.
- **Withheld labels still feed counts.** `exposure_section` and `sovereignty.py` read the raw
  `foreign_dependency`, including labels the report withholds (TODO.md). Don't build new counts that way.
- **The mobile reader is stale** (schema-1 bundle). Don't copy the new bundle into it without the
  schema-2 port.
