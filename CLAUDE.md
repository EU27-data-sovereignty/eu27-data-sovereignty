# CLAUDE.md

Project instructions for AI assistants working in `sovereign-data-centers`. The workspace rules in
`~/dev/CLAUDE.md` apply as well: the security gate, noreply identity, exact pins, and confirming before
push or deploy.

## Overview

A sourced analysis of each EU member state's critical government data holdings, and of what sovereign
hosting for them requires.
- **Research.** Agents stage claims; `model/research.py` admits only claims whose quote is found in a
  fetched, hashed document and whose categorical label an independent reviewer agrees with (#79).
- **Rendering.** One content model (`model/document.py`) renders everything: the EU-27 report and 27
  country PDFs (typst), the React web app, the markdown briefs, the posters and the `/ask` corpus.
- **Stack.** Python is stdlib-only. The web app is React 19, Vite and Tailwind 4 in `web/`. `/ask` is a
  Vercel Function in `api/`.
- **Deployment.** Vercel, built locally and deployed prebuilt.

Read [`METHOD.md`](METHOD.md) for the evidence pipeline and [`DECISIONS.md`](DECISIONS.md) before
changing a rule. From #72 on, a new decision entry needs every part listed in `README.md` § How decisions
are recorded: `tests/test_docs.py` enforces it.

## Commands

```
./test.sh                              # the full gate; run before every commit
./test.sh --no-e2e                     # without Playwright
./run.sh                               # dev server, http://localhost:5173
./run.sh data                          # regenerate briefs, bundle and /ask corpus (pins the epoch)
./run.sh artefacts                     # re-render the 27 tracked posters (needs Chrome)
./run.sh export                        # EU-27 report + 27 country PDFs into book/build/
./run.sh deploy                        # gate, local vercel build, prebuilt PRODUCTION deploy; owner's OK first

python3 model/document.py --check      # every fact shown resolves to a checked source
python3 model/sovereignty.py [ISO]     # ranking placements, range and confidence
python3 model/research.py verify [--iso XX]   # fetch, hash, quote-check staged research (slow, polite)
python3 model/research.py admit        # write verified + reviewed claims into the registers
python3 model/research.py report       # verification outcomes per state
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
- **Never admit unreviewed labels.** Categorical values (foreign dependency, indicator values) need an
  agreeing verdict in `model/research/dependency_review/` or the indicator `review` block (#79). Seven of the
  eight "Dependent" placements in the first, unreviewed ranking did not survive review.
- **The security gate blocks email-shaped strings.** They have come in through archive URLs. Archived
  copies are accepted only for exactly the requested host (`research.snapshot_matches`). Fix the data;
  never bypass the gate.
- **Deploys are prebuilt and manual.** A push ships nothing. The PDFs need `typst` locally. The build
  command runs `npm ci` at the root (for `api/`) and in `web/`. Previews sit behind Vercel login.
- **SPA rewrite.** It must target `/index` under `cleanUrls` (`tests/test_vercel_config.py`).
- **zsh.** `echo ====` breaks, because a leading `=` is command expansion; use `echo '---'`.
- **The mobile reader is stale** (schema-1 bundle). Don't copy the new bundle into it without the
  schema-2 port.
