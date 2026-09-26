# Migrate `national_data.csv` onto the source register (#67)

**Status: done 2026-09-26, recorded as DECISIONS.md #69.** The plan below is kept as written;
[Results](#results) at the end shows what ran and what it printed.

## Context
`model/national_data.csv` keeps its own provenance in five columns: `url`, `publisher`, `retrieved`, `confidence` and `quote`. That is the duplicated provenance #67 was written to end, and the `record:` namespace #67 reserved for these rows is still unused. There are 3 rows today (all NL: BRP, BRK, Handelsregister), so the move is cheap. It gets more expensive with every row researched, which is why TODO.md puts it before Tier 0 research.

Decided in this session:
- **Claim id:** `record:<ISO>:<record_class>:register`. The reserved shape widens to `<register|count|size>`, so a register's existence, its record count and its record size live side by side for the same class.
- **Byte-identical outputs:** copy #67's adapter pattern. Exposing `source_id` in `eu27.json` (roadmap step A2) is a separate, later change.

## Step 0: put this document in the repo ✅
Copy this whole file, the plan plus the Findings appendix, to `NATIONAL-DATA-MIGRATION.md` at the repo root. That matches the existing top-level docs (`SOURCES.md`, `VERIFICATION.md`). Tick its checklist as the steps land, and fill in the actual verification output at the end.

## Pre-flight ✅
- The 4 uncommitted files (PROGRESS, ROADMAP, TODO, STYLE) and the 5 unpushed commits are the user's. Don't mix them into this commit. Ask whether to land them first, since this work also edits TODO, PROGRESS and ROADMAP.
- **Baseline, captured before any edit** (see memory `sovereign-dc-verification-baseline`), saved to the scratchpad:
  - `shasum -a 256 web/public/data/eu27.json mobile/assets/data/eu27.json`
  - `python3 model/capacity_model.py --all --json --no-write > base_model.json`
  - a JSON dump of `nd.for_country(nd.load(), iso)` for all 27 ISOs, saved as `base_nd.json`

## Changes

### 1. `model/sources/registry.csv`: add 3 sources, kept in sorted order
| source_id | publisher | url | doc_type |
|---|---|---|---|
| `kadaster:brk` | Kadaster | https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brk | webpage |
| `kvk:handelsregister` | Kamer van Koophandel (KVK) | https://www.kvk.nl/over-het-handelsregister/ | webpage |
| `rvig:brp` | Rijksdienst voor Identiteitsgegevens (RvIG) | https://www.rvig.nl/basisregistratie-personen | webpage |

- **No `@vintage`.** These are live web pages; each citation's `retrieved` carries the date. This also keeps `@` out of anything the mobile email regex might see later.
- **`title`:** read from the page's own `<title>`. If the page can't be read, use the register name and say so in `notes`. Don't invent a title.
- **`language`:** `nl`.
- **`published`, `license`, `archived_url`:** left empty unless the page states them.

### 2. `model/sources/citations.csv`: add 3 `record:` citations, kept in sorted order
- **claim:** `record:NL:civil_registry:register`, `record:NL:land_property:register` and `record:NL:business_registry:register`.
- **quote, confidence (`official`), retrieved (`2026-09-21`):** moved verbatim from the CSV.
- **locator:** a short description of where the quoted sentence sits on the page, since `validate()` requires a non-empty locator.
- **`value_as_found`, `unit`:** empty.
- **`checked_by`:** `national_data.csv migration (#67)`, matching the legal rows.

### 3. `model/national_data.csv`
Drop the five provenance columns. The new header is `iso,tier,record_class,status,register,holder,holder_url`.

`holder` and `holder_url` stay. They are facts about the register, not provenance of the claim.

### 4. `model/national_data.py`: adapter, the same pattern as `sources.load()` from 69f2775
- `FIELDS` becomes the 7 columns above. The exact-header check in `load()` then rejects the old file.
- `load()` reads the CSV, then joins each row to its citation `record:<iso>:<class>:register` (via `provenance.citations()`) and to that citation's registry entry (via `provenance.registry()`). It returns rows in **today's shape**: `url` and `publisher` come from the registry; `retrieved`, `confidence` and `quote` come from the citation. The import stays local, as it is in `sources.py`.
- Two new errors, raised by `validate()`, or by a helper it calls, over the joined data:
  - a `held` or `not_held` row with no `:register` citation, or with more than one
  - a `record:*:*:register` citation that has no matching row (an orphan)
- `status_errors()`, `validate()` (https, publisher, date, quote ≥ 20, **email check**, sort order), `for_country()` and `NOTE` all stay as they are. They see the same row shape as before. `for_country()` output is therefore unchanged, and so is every renderer: generate_countries, export_json, web `Country.tsx`, mobile, and `book/build.py`.

### 5. `model/provenance.py`
- Docstring line 28 becomes `record:<ISO|*>:<record_class>:<register|count|size>`, described as a Tier 0/1 register's existence, record count or size.
- `validate()` gets a `record:` shape check next to the `param:` one (lines 143-146). A record claim needs 4 parts; the ISO must be in `parameters()` or `*`; the class must be in `national_data.RECORD_CLASSES`, imported locally to avoid a cycle; the kind must be one of `register`, `count`, `size`.
- `claims_by_namespace()` gains a `record` denominator of the 27 ISOs × 15 classes, each as a `:register` claim, which is 405. Without it, coverage would report 3/3 = 100%. The count and size denominators come with Part C.

### 6. Tests
- **`tests/test_provenance.py`:**
  - `FLOORS` gains `"record": 3`
  - a malformed record claim is rejected (wrong arity, unknown class, unknown kind)
  - the record denominator is 405
- **`tests/test_national_data.py`:**
  - `ValidationRules.BASE` stays a joined row, so the existing rule tests keep testing `validate()`
  - a header containing the old provenance columns is rejected
  - a held row with no citation is an error
  - an orphan `:register` citation is an error
  - `TheDutchBriefStaysInSync` should keep passing unchanged, since it reads `nd.load()`

### 7. Docs, in the same commit
- **`DECISIONS.md`:** a new entry after the last number that records the `:register` suffix, with a `Verified:` line holding the actual command output. The suffix closes off the bare 3-part shape from TODO.md.
- **`TODO.md`:** tick the migration item and correct its wording from `record:<ISO>:<record_class>` to `:register`.
- **`ROADMAP.md`:** A2 notes that national_data is on the register, and that `source_id` is not yet in the bundle.
- **`PROGRESS.md`:** a line in the status section.
- **Not touched:** `countries/NL/GOAL.md`. It is hand-written and nothing it shows changes.

## Verification (report every number, don't assert)
1. `python3 model/provenance.py`: 11 sources, 167 citations, 0 errors; coverage shows record 3/405.
2. `python3 model/national_data.py`: 0 errors, still 3 of 405 pairs.
3. Recompute the `for_country()` dump for all 27 and `diff` it against `base_nd.json`: it must be empty.
4. `python3 model/capacity_model.py --all --json --no-write`: byte-identical to `base_model.json`.
5. `./run.sh data`, then `git diff --stat -- countries web/public/data mobile/assets`: it must be empty. Also check that the `eu27.json` sha256 equals the baseline and the `ARTEFACTS.csv` `bundle_sha256`.
6. `./test.sh` passes (Python + Vitest + Playwright), with counts up only by the new tests.
7. `cd mobile && npm test`: parity passes. It is not in `./test.sh` or CI, so run it by hand.
8. Commit through the security gate. **Don't push without the user's confirmation.**

---

## Results

**Pre-flight.** The user's 4 pending doc edits were committed on their own first, as `7630bde`. That
commit printed the gate's `origin is PUBLIC — personal data blocks this commit` line, which is only a
banner (`dotfiles/security/gate.sh:287`): it turns strict mode on, and the checks then passed.

**Steps 1-7.** All done as planned. Details the plan left open:

- **Titles** were read from the live pages on 2026-09-26. All three returned HTTP 200, and all three
  quotes are still on the page verbatim.

  | source_id | title |
  |---|---|
  | `rvig:brp` | Basisregistratie Personen \| RvIG |
  | `kadaster:brk` | Waar bestaat de BRK uit? - Kadaster.nl zakelijk |
  | `kvk:handelsregister` | Over het Handelsregister \| KVK |

- **Locators:**

  | Source | Locator |
  |---|---|
  | RvIG | "Intro section, first paragraph" |
  | Kadaster | first item of the "bestaat uit" list under the heading "Basisregistratie Kadaster (BRK)" |
  | KVK | intro paragraph under the heading "Over het Handelsregister" |

- **Line endings are preserved:** `citations.csv` and `national_data.csv` are CRLF, `registry.csv` is
  LF. The data diff is therefore 10 lines: 3 rows rewritten, 3 citations added, 3 sources added.
- **New functions in `national_data.py`:**
  - `claim(r)`
  - `citation_errors(rows, cites)`, run by `main()`: each row needs exactly one `:register`
    citation, and each such citation needs its row. `:count` and `:size` claims need no row.
  - `PROVENANCE`
- **New in `provenance.py`:**
  - `RECORD_KINDS`
  - `record_classes()`, a local import that avoids the import cycle
  - the `record:` shape check
  - the 405-claim denominator

**Verification**, run on 2026-09-26:

| # | Check | Result |
|---|---|---|
| 1 | `python3 model/provenance.py` | 11 sources, 167 citations, exit 0; `record` 3/405 (0.7%) |
| 2 | `python3 model/national_data.py` | exit 0; 3/405 pairs |
| 3 | `for_country()` dump, all 27 countries, vs baseline | `cmp` identical (111,124 bytes) |
| 4 | `capacity_model.py --all --json --no-write` vs baseline | `cmp` identical |
| 5 | `./run.sh data`, then `git status` | no change under `countries/`, `web/public/data/` or `mobile/assets/`; `eu27.json` sha256 `e472325f068f…c09e609`, equal to the baseline and to `ARTEFACTS.csv` |
| 6 | `./test.sh` | exit 0: 106 Python (97 + 9 new), 66 Vitest, 15 Playwright; tsc, eslint, prettier and build clean |
| 7 | `cd mobile && npm test` | 3 suites, 19 tests passed |
| 8 | Commit | goes through the gate. Not pushed. |

## Appendix: findings from the exploration (2026-09-26)

### A. Current `model/national_data.csv` (all of it)
```
iso,tier,record_class,status,register,holder,holder_url,url,publisher,retrieved,confidence,quote
NL,0,civil_registry,held,Basisregistratie Personen (BRP),Rijksdienst voor Identiteitsgegevens (RvIG),https://www.rvig.nl/,https://www.rvig.nl/basisregistratie-personen,Rijksdienst voor Identiteitsgegevens (RvIG),2026-09-21,official,De Nederlandse overheid registreert persoonsgegevens in de Basisregistratie Personen (BRP).
NL,1,land_property,held,Basisregistratie Kadaster (BRK),Kadaster,https://www.kadaster.nl/,https://www.kadaster.nl/zakelijk/registraties/basisregistraties/brk,Kadaster,2026-09-21,official,de kadastrale registratie van onroerende zaken en zakelijke rechten
NL,1,business_registry,held,Handelsregister,Kamer van Koophandel (KVK),https://www.kvk.nl/,https://www.kvk.nl/over-het-handelsregister/,Kamer van Koophandel (KVK),2026-09-21,official,Bedrijven en organisaties zijn ingeschreven in het Handelsregister van KVK. Dat register is openbaar.
```

### B. The validator: `model/national_data.py` (#60, DECISIONS.md:934-967)
- `FIELDS` (65-68) is checked as an exact header in `load()` (139-144). `CONFIDENCE` (100) is `primary`, `official`, `secondary`, `absence`.
- `status_errors()` (147-168):
  - `not_held` requires `absence`
  - `held` can't claim `absence`
  - `held` must name a register
- `validate()` (171-222):
  - `url` and `holder_url` are https
  - publisher is not empty
  - `retrieved` is YYYY-MM-DD
  - quote is at least 20 characters
  - no email address in `register` or `quote`
  - no duplicates
  - rows sorted by (iso, tier)
- `for_country()` (274-299) is the single view every renderer uses. It returns all 15 classes; unrecorded classes have `""` in the provenance keys.
- The ratchet is in `tests/test_national_data.py`: `NATIONAL_DATA_FLOOR = 3` (line 18), `ValidationRules.BASE` (72-78), and `TheDutchBriefStaysInSync` (125-158), which asserts that `r["url"]` appears in `countries/NL/GOAL.md`.

### C. The source register (#67, DECISIONS.md:1118-1151)
- `model/sources/registry.csv`:
  - header: `source_id,title,publisher,url,doc_type,published,language,license,archived_url,notes`
  - 8 sources
  - no `retrieved` or `confidence` column; those two live on the citation
- `model/sources/citations.csv`:
  - header: `claim,source_id,locator,quote,value_as_found,unit,confidence,retrieved,checked_by`
  - 164 rows, all `param:`: 162 Eurostat and 2 legal (FR and NL `data_classification`)
- `model/provenance.py`:
  - `SOURCE_ID = ^[a-z0-9-]+:[a-z0-9_.-]+(@...)?$`. The publisher part allows no dots, so `rvig.nl` is invalid and `rvig:brp` is valid.
  - `DOC_TYPES` includes `webpage` and `register`.
  - `CONFIDENCE` adds `assumption` to the four that `national_data` allows.
  - The only shape check is for `param:` (143-146).
  - `claims_by_namespace()` (172-181) fills only `param` and `assumption`.
  - `coverage()` (184) reports (supported, declared, total).
  - There is no "resolve" helper. Callers join citation and registry themselves (`generate_countries.cite()`, `sources.load()`).
  - `tests/test_provenance.py:29` has `FLOORS = {"param": 138, "assumption": 0}`.

### D. The precedent: commit 69f2775
`sources.py:load()` keeps the old ledger row shape by joining `provenance.citations()` to `provenance.registry()`, so the validator and the renderers were left alone. The legal citations use a descriptive `locator` and `checked_by=sources.csv migration (#67)`. This plan copies that adapter.

### E. Every reader of national_data provenance
The data flows: `nd.load()` → `nd.for_country()` → `country_data.build(national_data=…)` (country_data.py:167,194). That is called from `generate_countries.py:751,769` and `export_json.py:46,53` (and `:74` adds `nd.NOTE`).

| Renderer | Location | Fields read |
|---|---|---|
| Markdown briefs | `model/generate_countries.py:276-298` | `publisher`, `url`, `holder`, `holder_url` |
| Web | `web/src/pages/Country.tsx:310-341`, types `web/src/data/types.ts:118-131` | `url`, `publisher` |
| Mobile | `mobile/app/country/[iso].tsx:254-277`, types must equal web | no provenance fields |
| Book | `book/build.py:205-233` | `url` |

`retrieved`, `confidence` and `quote` only ship in `eu27.json`.

### F. Generated outputs and gates
- `web/public/data/eu27.json` and its byte-copy `mobile/assets/data/eu27.json`. The copy is enforced by `mobile/__tests__/parity.test.ts`, which also bans email-shaped text.
- `countries/ARTEFACTS.csv` pins the bundle sha256 (`e472325f…`). `tests/test_artifacts.py:75-80` fails when the bundle changes.
- `countries/NL/GOAL.md:492,502,505` is hand-written (#5); the generator never touches it.
- Regenerate with `./run.sh data`. There is no script that copies the bundle to mobile.
- `./test.sh` runs Python unittest, `sources.py`, `national_data.py`, the regenerate-and-diff check, then the web type-check, lint, prettier, Vitest, build and Playwright. It does **not** run `provenance.py` or mobile Jest; nor does CI.

### G. Decisions taken in this session
| Question | Choice | Alternative rejected |
|---|---|---|
| Claim id for a register's existence | `record:<ISO>:<class>:register`, with the docstring widened to `<register\|count\|size>` | bare `record:<ISO>:<class>`, which clashes with the reserved 4-part shape |
| Bundle | Byte-identical, via the adapter; `source_id` in the bundle is deferred to A2 | add `source_id` to `eu27.json` now |
| Source ids | `rvig:brp`, `kadaster:brk`, `kvk:handelsregister`, no vintage | `rvig.nl` (fails the regex) |
