# TODO (EU-27)

Country-level workstreams live in `countries/NL/TODO.md` (the reference case) and apply to every country.
This file tracks the cross-country work.

## Model
- [x] Parameterized capacity model reproducing the Dutch xlsx (`model/capacity_model.py`)
- [x] EU-27 parameter dataset from Eurostat (`model/eu27_parameters.csv`)
- [x] Scaling rules from the NL baseline with small-state floors and frontline multiplier
- [ ] Replace population/GDP scaling with real per-country government IT inventories where published
      (FR DINUM, DE ITZBund, IT PSN migration data, PL RChO, EE RIT are the likeliest sources) —
      planned as Part B of `ROADMAP.md` § Sourcing plan
- [ ] Per-country PUE and facility CAPEX (climate and seismic design change both)
- [ ] Sensitivity: site size (12 MW unit), replication factor, headroom, utilization
- [ ] 5- and 10-year growth per country

## Geography
- [ ] Replace the first-pass regions in `generate_countries.py` with scored site selection per country
- [ ] Seismic and flood zoning as hard exclusions in the scoring
- [ ] Grid connection lead time as a scored criterion (IE, NL, DE, BE, ES are all constrained)

## Testing
- [ ] Put the web and mobile suites in CI. `ci.yml` runs the Python suite and gitleaks only — no
      `npm run build`, no Vitest, no Playwright, no Jest — which is how a red gate survived a week
      (2026-09-13 to 2026-09-21). Nothing copies `mobile/assets/data/eu27.json` either, and the
      parity test that would catch the drift runs in neither `./test.sh` nor CI.

## Federation (deferred by decision, Sept 2026)
- [ ] Out-of-country reserve for frontline and micro states (EE data-embassy pattern)
- [ ] Pooled sovereign capacity for states under ~3 MW
- [ ] Mutual DR pairs and treaty basis

## Critical national data register (`model/national_data.csv`)
- [x] Schema, validator, coverage ratchet and the section in all four renderings (#60)
- [x] NL: BRP, BRK, Handelsregister — 3 of 405 pairs
- [ ] Tier 0 for the five large states (DE, FR, IT, ES, PL) — 40 pairs, the highest-value batch
- [ ] Tier 0 for the remaining 21 states — 168 pairs; this is where the sovereignty argument lives
- [ ] Tier 1 across all 27 — 189 pairs; decide first whether the published percentage narrows to
      tier 0 rather than sitting stuck near zero (#60)
- [ ] Re-try the four NL pages that failed the first pass: Belastingdienst (no describing sentence),
      DigiD (publisher not attributable with confidence), RDW (no register named), DUO (404)
- [ ] Validate the `TIER0-TIER1-SIZING.md` per-citizen figures against the Kadaster, RvIG and
      Belastingdienst annual reports — a different task from recording the registers; planned as
      Part C of `ROADMAP.md` § Sourcing plan (counts from annual reports, sizes from standards)

## Write-ups
- [ ] Hand-edit the five large states (DE, FR, IT, ES, PL) into full analyses like `countries/NL/GOAL.md`
- [ ] Verify the sovereign-cloud and digital-ID entries in `eu27_parameters.csv` against primary sources

## Sources (the launch gate, #67)
- [x] One source register for every claim (`model/sources/`, `model/provenance.py`) — A1, 2026-09-24
- [ ] A2: `source_id` in `fetch_manifest.csv`, `national_data.csv`, `institutions.csv`; sources in the
      bundle, a web Sources page, mobile links, a book bibliography
- [ ] A3: declare the 22 assumptions and 7 scaling rules (`confidence: assumption`, with rationale)
- [ ] Full coverage in every published namespace before any launch step (`ROADMAP.md` § Sourcing plan)

## Outreach
- [x] People inventory, private (`contacts/people.csv`): 956 rows, 850 send-ready — 2026-09-24
- [ ] Second research pass: MT (none), CY, HU, HR, EL, SI (five rows or fewer)
- [ ] Re-research the 77 rows whose seat quote was not found on its page, and the ~30 unreachable
- [ ] Institutional map beyond 25/324: contact *pages* for the email-routed bodies (#68)

