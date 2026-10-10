# Design decisions

An ADR-style log of the decisions behind this project and the reasoning for each, so the "why" survives
independently of any chat transcript or anyone's memory.

**Conventions.** Newest section last. Each entry records what was decided, when, why, what was rejected,
and what would change it. Decisions that get overturned are marked **Superseded** and left in place — a
decision that changed is more informative than one quietly erased. From #72 on, every entry follows the
required structure in `README.md` § How decisions are recorded, and `tests/test_docs.py` enforces it.

---

## Scope and structure

### 1. Scope is EU-27 only
**2026-09-03.** The 27 member states, no EFTA, UK, Western Balkans or candidate countries.

Every EU-27 state shares one legal baseline — GDPR, NIS2, the Data Act, and the (still unresolved) EU Cloud
Services Scheme — which is what makes them comparable on a single axis. Norway, Switzerland and the UK each
need their own adequacy and jurisdiction framing, so folding them in would mean four framings rather than
one. Rejected: geographic Europe (~44 states), where most have no meaningful national cloud programme and
the pages would be speculative.

*Would change if:* the EFTA states' sovereign-cloud programmes become substantial enough to warrant their
own comparable treatment.

### 2. One directory per country
**2026-09-03.** `countries/<ISO2>/` holds every artefact for that country: inputs, model outputs, the
brief, and eventually its PDF and poster.

Everything about a country is in one place, and there are no cross-country files that must be kept in sync
with the per-country ones. `countries/SUMMARY.md` and `model/eu27_results.csv` are the only aggregate
files, and both are generated.

### 3. Extend `GOAL.md` to 12 sections rather than add a second document
**2026-09-03.** The generated brief grew from 9 to 12 sections (adding legal posture, provider landscape,
migration path) instead of introducing a separate `STRATEGY.md`.

One brief per country is simpler to navigate and to publish. The known cost: `generate_countries.py`
rewrites `GOAL.md` unconditionally, so hand-edits are lost. `TODO.md` wants DE/FR/IT/ES/PL hand-deepened
eventually, which will collide with this. The documented escape is to rename a country's file out of the
generator's path.

*Would change if:* hand-authored country analysis becomes the main deliverable rather than the exception.

**Amended 2026-09-21 (#60):** a thirteenth section, the Tier 0/Tier 1 national data register, was
appended on the same reasoning — the alternative was a second generated document per country. The
count in this entry's title is left as it was written; the live list is `SECTIONS` in
`model/generate_countries.py`, which drives both the headings and each brief's contents list.

### 4. Research all 27 legal cells now, rather than scaffold and fill later
**2026-09-03.** The six legal/regulatory columns were populated for every state in one pass.

A structurally complete section full of `TODO` markers is worse than no section: it looks finished in a
table of contents and disappoints on arrival. The tradeoff is that these are one researcher's unverified
claims — addressed by decision 25 rather than by hedging the prose.

### 5. NL is excluded from generation
**Superseded by #72** (2026-09-29): the Netherlands is no longer the baseline the others derive from.
**2026-09-03.** `generate_countries.py` skips the Netherlands.

`countries/NL/GOAL.md` is the hand-written 20-section narrative that the entire model derives from — the
generator reads it as the baseline. Regenerating it would overwrite the source with a scaled copy of
itself. NL still receives CSVs, a bundle entry, an app page, a PDF and a poster.

---

## Architecture

### 6. Python is the source of truth; everything else renders one dict
**2026-09-03.** `model/country_data.py` assembles every fact about a country. The markdown brief, the JSON
bundle, the web app, the PDFs and the book are all renderings of that dict.

Four presentations of the same numbers will disagree eventually unless they share one origin. The app
therefore never recomputes canonical figures for display. The single deliberate exception is the scenario
sandbox, which recomputes under user-chosen assumptions and is visually marked as hypothetical.

### 7. Fact assembly split from rendering
**2026-09-03.** `write_goal()` was refactored from a 176-line function that interleaved fact-gathering with
markdown formatting into a pure dict → markdown renderer.

Without this, `export_json.py` would have had to re-derive the same flags and ratios, and the two would
have drifted. Verified behaviour-preserving: regenerating all 27 countries after the refactor produced a
byte-for-byte zero diff.

### 8. The migration phase map is keyed on `Class`, not `Workload`
**Superseded in part by #72** (2026-09-29): workloads are no longer Dutch rows renamed per country.
**2026-09-03.** `model/migration_phases.csv` maps the seven workload *classes* to phases.

The generator rewrites workload *names* per country — the Dutch "Digital identity / DigiD" becomes
"Digital identity / Online-Ausweis eID + BundID" in Germany — so a name-keyed map would break for 26 of 27
countries. The seven class names are stable across all of them; a test now asserts this.

### 9. `capacity_model.py` stays ignorant of `eu27_parameters.csv`
**2026-09-03.** The capacity model reads only a country directory plus shared assumptions. The
country-level hybrid-eligibility gate (does an in-jurisdiction commercial region exist?) is applied
downstream in `country_data.py`.

Keeps the model runnable against any country directory without a parameter file, which is what makes it
portable and easy to test.

---

## Method and honesty

### 10. No composite sovereignty score
**2026-09-03.** The sovereignty matrix shows eight ordinal dimensions side by side and never sums them.

The dimensions are not commensurable — certification strength and seismic risk do not add. A single number
would imply a precision this dataset does not have and would be the first thing quoted out of context. Each
column's normalization is stated on the page, and every cell links to its source text.

### 11. The matrix test guards column variance, not leader saturation
**2026-09-03.** France scores 1.00 on all eight dimensions and Germany on seven.

The first version of the test failed on any fully-saturated country. On inspection the distribution is
healthy — every column has at least two distinct values, column means range 0.19–0.81, and total scores
spread 2.2–8.0 with stdev 1.50 — and France genuinely does lead EU sovereign-cloud doctrine. Saturation by
a real leader is a finding; a dimension that scores everyone identically is the actual defect, so that is
what the test now checks.

*Would change if:* discriminating data becomes available for the leading states — eIDAS wallet notification
status, share of government workloads under national certification, or operator ownership structure (who
operates the sovereign cloud, and on whose technology).

### 12. Storage is not the sizing driver — confirmed, not assumed
**2026-09-03.** `TIER0-TIER1-SIZING.md` asked whether site count was being derived from storage volume,
which would invert the model. It is not.

`capacity_model.py` computes `sites = max(sites_by_mw, min_sites)`, and the hand-set `min_sites` floor
strictly binds for **24 of 27 countries**. Germany alone genuinely needs more sites than its floor (6
against a floor of 4); France and Italy sit exactly at the tie, where `sites_by_mw == min_sites == 4`, so
their floor coincides with the engineering answer rather than overriding it. NL's storage would have to
grow roughly 10× to change its site count.

The finding that matters more: site count is mostly a *political* parameter, not an engineering result,
and the app should show that rather than hide it.

**Corrected 2026-09-04.** This entry first read "26 of 27, Germany alone" — inherited from an early survey
that counted the France and Italy ties as floor-bound and repeated without checking. The TS/Python parity
test caught it by asserting the count. Recomputed from the model: 24 strictly floor-bound, 3 at or above
their floor (DE, FR, IT), of which only DE exceeds it.

### 13. Stdlib-only Python, no pytest
**2026-09-03.** The model and its tests use only the standard library.

The project already had this property and it is worth keeping: the Python half needs no install step at
all, which makes CI trivial and the model portable.

---

## Verification

### 14. Vet, don't assert
**2026-09-03.** Every claim gets a measurement before it is reported.

This is not a slogan; it has caught four real defects that would otherwise have shipped:

1. **`IT` and `ES` had unquoted commas** in `eu27_parameters.csv`, shifting every later field. Italy's
   published brief printed " Sicily" as its entire threat-notes section.
2. **Two writers disagreed on row order** in `eu27_results.csv` — the generator put NL first, `--all`
   sorted alphabetically — which would have made any golden-file test pure noise.
3. **An incorrect claim of my own**: that all three hyperscalers anchor their principal EU regions in
   Dublin. AWS and Azure do; Google's `europe-west1` is in Belgium. The existing
   `hyperscaler_regions_live=2` was right and the prose was wrong.
4. **73.5% mean prose similarity** across the 26 generated briefs (47 of 325 pairs above 80%, LT–LV at
   90.2%), which is why the book is structured as argument-plus-gazetteer rather than a read-through.
5. **Two miscounted headline figures**, both caught by asserting them in tests rather than repeating them.
   The `min_sites` floor binds for 24 countries, not 26 (see #12). And eight states fall below 1 MW per
   site, not nine — the "nine" came from `README.md`, which was itself wrong about a different metric
   (states under 3 MW total design load, also eight). The same eight countries happen to satisfy both:
   SI, EE, LV, CY, MT, LU, LT, HR.

The pattern in every one of these: a number quoted from an earlier summary rather than recomputed. The
app now derives these counts from the data at render time, so the page cannot drift from the model.

### 15. The generator is byte-reproducible
**2026-09-03.** Generated files stamp their date from `SOURCE_DATE_EPOCH` when set, following the
reproducible-builds convention.

Previously every run rewrote 27 files with a new date, so real changes were buried in date churn and
"regenerating changes nothing" could not be tested. Now it can be, and it is — the refactor in decision 7
was proven safe this way.

### 16. Both writers sort `eu27_results.csv` by ISO
**2026-09-03.** See defect 2 above. Committed generated files must be identical regardless of which code
path produced them, or golden-file comparison is worthless.

### 17. `test.sh` fails fast
**2026-09-04.** The full gate runs everything in cheap-to-expensive order and stops at the first failure.

Chosen deliberately. The alternative — `templates/general/general-template/scripts/test.sh` omits `set -e`
and accumulates an exit code so every check runs and a summary prints — is better when you want one full
report per run, and is the fallback if fail-fast becomes annoying.

---

## Tooling and stack

### 18. React 19 / Vite 6 / TypeScript 5.7 / Vitest 3 / ESLint 9 flat config
**2026-09-04.** Rather than the pins in `templates/ts-web/production-ready`.

`templates/DEPENDENCY_MATRIX.md` carries a 2026-09-01 audit note stating its Dec-2024 pins are ~20 months
stale and that recent workspace projects have moved to React 19 / Vite 6–8 / TS 6. This is a greenfield app
with no legacy constraint, so it follows current practice rather than a self-declared-stale baseline. Exact
version pinning, no `^` or `~`, per the workspace rule.

Consequence: the template's `.eslintrc.cjs` is a rule-list reference rather than a copyable file, since
ESLint 9 uses flat config.

### 19. Template bugs deliberately not copied
**2026-09-04.** Four defects confirmed in `templates/ts-web/production-ready`:

- `"test": "vitest"` is **watch mode**, so `./run.sh test`, `run.sh health` and the `pre-push` hook all
  hang in non-interactive use. Here: `"test": "vitest run"` with `test:watch` separate.
- `test:` config is duplicated in `vite.config.ts` and `vitest.config.ts`; the standalone file wins at
  runtime, so the vite block is dead config. Here: only `vitest.config.ts`.
- `@vitest/coverage-v8` is not installed, so the 80% thresholds in `vitest.config.ts` silently cannot run.
- `dist/` is committed by accident.

Worth reporting back to the template so they get fixed at source.

### 20. Tailwind, matching the template
**2026-09-04.** Despite the app being SVG-chart-heavy, where Tailwind does comparatively little.

Consistency with the workspace's other web projects won over dropping three build dependencies.

### 21. Warm Neutral + Terracotta design system
**Superseded for this project by #76** (2026-09-29): EU blue and gold from `design/tokens.json`.
**2026-09-04.** From `~/dev/design/DESIGN_SYSTEMS.md`, with Editorial Data-Report as the layout reference.

Of the five systems in that library, two are dark single-theme (Nocturnal Cartography, Quant Terminal) and
unusable in print. Warm Neutral + Terracotta is authored paper-first, is mostly neutral so it survives
grayscale conversion for the book, and its single accent collapses to one distinguishable gray. Its
institutional restraint also suits a ministerial audience better than a dashboard palette.

### 22. Playwright drives the installed Chrome
**2026-09-04.** `channel: 'chrome'` with `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1`.

Full Playwright API for E2E, axe and visual regression without the ~400 MB Chromium download, which
`~/dev/CLAUDE.md` asks be confirmed before pulling. Note the local binary is at
`/Applications/Chrome.app/Contents/MacOS/Google Chrome` — not the conventional `Google Chrome.app` path —
with Brave and Edge as fallbacks.

### 23. Typst over Pandoc + LaTeX
**2026-09-04.** Typst 0.15.1, installed via Homebrew: a single 44.9 MB bottle with zero dependencies,
Apache-2.0.

`pandoc` was already installed but no TeX engine was. MacTeX is multi-GB; BasicTeX ~100 MB plus package
installs; Tectonic was the closest alternative. Typst needs no LaTeX distribution at all and its templates
are readable, which fits the workspace's dependency-light rule.

---

## Publication

### 24. Deliverables are committed; build output is not
**2026-09-04.** Per-country PDFs, posters and the JSON bundle are tracked. `web/dist/` and
`web/node_modules/` are gitignored. Tracking a binary CI cannot rebuild has a cost, paid in #51-#53:
it can go stale silently, and it did.

**Supersedes** an earlier decision to "commit everything", which was taken when the site was hand-written
static HTML with no build step. With Vite, `dist/` is regenerated by Vercel on every push, so committing it
adds permanent binary churn and buys nothing.

### 25. Publication is gated on verification
**2026-09-04.** The site stays on `*.vercel.app` and nothing goes to print until: Tier-1 legal cells are
verified against primary sources, a sampling audit has produced a measured error rate per column,
provenance is visible on every page and in every PDF, the corrections channel is live, and three briefs
have been read end to end.

The six legal columns are **factual claims about real jurisdictions** — a different epistemic category from
the scaled capacity placeholders. The repo's "working assumption" banner honestly covers a scaled MW
figure; it does not cover asserting what Spain's certification regime requires. Publishing unverified legal
claims under an authoritative-sounding domain is this project's one real reputational risk, and a printed
book cannot be corrected after the fact.

**Amended 2026-09-05.** As first written, this gate named only the website and the printed book. The
public GitHub repository is a **third publication channel**, and it went live on 2026-09-04 with the legal
cells still unverified. That was deliberate rather than an oversight: a public repository carrying
prominent caveats and a corrections channel is a reasonable way to *obtain* verification, and it is the
lowest-stakes of the three because a reader arrives at source files that say what they are. The gate on
the custom domain and on print is unchanged. What the repository owes in exchange is that the caveat
travels with the claim — hence the section 10 warning, the `data_status` column, `model/README.md` and the
caveat printed on every poster.

### 26. Named individuals never go in the public repo
**2026-09-04.** The outreach contact list holds institutional roles and published official contact points —
committee, directorate, agency. Named individuals live in the separate **private** repo
`sovereign-data-centers-contacts`.

A list of named officials in a public GitHub repo is a scrape target, ages badly, and a public official's
work contact is still personal data under GDPR requiring a documented lawful basis. The institutional map
carries essentially all the useful information at none of the risk.

### 27. The book is an authored argument plus a country gazetteer
**2026-09-04.** Parts I, II and V are newly written (~20–30k words); the 27 country briefings are an
explicitly labelled reference section.

Driven by measurement, not taste: at 73.5% mean pairwise prose similarity, the generated briefs would make
an unreadable read-through book. Reference works are allowed to be formulaic — an almanac entry is supposed
to resemble every other entry — but only if the book is honest about which part is reference and puts the
argument somewhere else.

### 28. Grayscale-safe book interior
**2026-09-04.** Mono interior, colour cover, every heatmap re-encoded by value and texture rather than hue.

Briefing documents get photocopied, so a chart that dies in black and white dies in exactly the setting
this book is for. Mono print-on-demand is also roughly a third the unit cost at ~300 pages. The web and PDF
editions keep full colour.

---

## The web app

### 29. Heatmaps are HTML tables, not SVG
**2026-09-04.** The sovereignty matrix and workload heatmap render as `<table>` elements with a `<button>`
per cell, rather than as SVG `<rect>` grids.

Every cell has to be individually focusable and screen-reader addressable. With real DOM elements that is
free — a button gets keyboard focus and an `aria-label` naming its row, column and value. With SVG it
means hand-plumbing roles, tabindex and labels onto shapes that have none of it by default. The axe
accessibility tests passed on the first run as a direct result.

The cost is that SVG's expressiveness is unavailable for these two charts. That is a fair trade for the
two views the whole site is built around.

*Would change if:* a chart needs geometry a table cannot express — which is exactly why the choropleth,
when built, will be SVG.

### 30. D3 is used as a maths library, not a charting library
**2026-09-04.** Only `scaleLinear` and `scaleQuantize` are imported. No `d3.select`, no data joins.

D3's DOM-manipulation half fights React, which owns the DOM. Its scales, projections and statistics are
genuinely worth having. Using only the second half is deliberate.

Known inefficiency: importing the `d3` meta-package pulls a 47 KB chunk to use two functions. Importing
`d3-scale` directly would cut that to roughly 15 KB. Left as-is for now under decision 32.

### 31. No Three.js, and no 3D
**2026-09-04.** Considered and rejected.

There is no third dimension in this data. A 3D rendering of a 27 × 8 ordinal matrix would occlude cells
behind other cells and read worse than the flat grid, at roughly 600 KB. The one arguable case — a globe
showing subsea cable landings — is decoration: the sovereignty argument in this project is jurisdictional,
not geographic.

### 32. Known improvements deliberately deferred
**2026-09-04.** Three changes were identified as genuine improvements and consciously not made, to keep
the codebase simple while the data is still unverified:

- **`scaleQuantile` instead of `scaleQuantize`** in the workload heatmap. `scaleQuantize` splits the
  domain evenly, and with Germany at 24,531 servers against Malta's 502 most countries fall into the
  lightest bucket. `scaleQuantile` splits by rank, which is what a 27-row comparison wants. This is a real
  legibility bug, not a preference.
- **Sub-package imports** (`d3-scale` rather than `d3`), for the chunk-size reason in decision 30.
- **The choropleth** (`/map`), which needs `d3-geo` with a conic projection. Cyprus and Malta are ~3,000 km
  from Ireland, so an unprojected EU map wastes most of its area on ocean.

Recorded here rather than lost, because "we knew and chose not to" is different from "we missed it".

### 33. Scripts at the repo root, following the workspace template convention
**2026-09-04.** `init.sh`, `run.sh` and `test.sh` sit flat at the root, matching
`templates/rn-supabase` rather than the `scripts/` subdirectory used by the older general template.

Conventions copied from `templates/ts-web/production-ready`: `set -e`, the `RED/GREEN/YELLOW/BLUE/NC`
colour block, `print_info`/`print_success`/`print_error`, `case "${1:-...}"` dispatch, unknown command →
error then help then exit 1.

Four bugs in that template were deliberately **not** copied, and are worth fixing at source:

| Template bug | Consequence |
|---|---|
| `"test": "vitest"` | Watch mode. `./run.sh test`, `run.sh health` and the pre-push hook all hang non-interactively |
| `test:` config in both `vite.config.ts` and `vitest.config.ts` | The vite block is dead config; the standalone file wins |
| `@vitest/coverage-v8` not installed | The 80% thresholds in `vitest.config.ts` silently cannot run |
| `dist/` committed | Build output in git |

### 34. The build date lives in `.build-epoch`
**2026-09-04.** One file, read by all three scripts.

It was first written as a literal in `run.sh` and `test.sh` and omitted from `init.sh` — so initialising a
fresh clone regenerated the bundle with today's date and immediately made the committed file look stale.
`test.sh` caught this on its first full run. A constant duplicated across three files is a constant that
will disagree with itself.

### 35. Accessibility defects found by testing, not by review
**2026-09-04.** The axe suite found three real problems on first run:

- `aria-sort` was on the sort `<button>` rather than the `<th>` that owns it — invalid ARIA.
- `--color-fg-muted` (`#898781`) measures **3.21:1** against the page. That value comes from the design
  system, where it is correct for axis ticks at the 3:1 graphical threshold, but it fails AA as body text.
  Darkened to `#6f6d66` (4.63:1) so one token is safe everywhere it is used. Worth feeding back to
  `~/dev/design/DESIGN_SYSTEMS.md`.
- White on the terracotta accent measures **3.12:1**. Replaced with slate (4.85:1).

None of these were visible to the palette validator, which checks chart colours against a surface, not
arbitrary text-on-background pairs in a finished layout.

### 36. Screenshots are part of testing, not a nicety
**2026-09-04.** The rotated column headers in the matrix were clipped to `w-6`, rendering every dimension
name as "Sov...", "Cert...", "Hyp...". Types passed, lint passed, axe passed, 15 E2E assertions passed —
and the chart was unreadable.

Nothing except looking at the rendered page catches that class of defect. The plan's "render it and look
at it" step is load-bearing.

### 37. The E2E suite binds a dedicated port
**2026-09-04.** Playwright's preview server uses 4823 with `strictPort`, not Vite's default 4173.

Another project in this workspace was already serving 4173. The preview server failed to bind, Playwright
happily reused the existing one, and the tests ran green against a completely different application before
this was noticed. `strictPort` turns that silent pass into a hard failure.

---

## Print and distribution

### 38. The book directory is `book/`, not `paper_book/`
**2026-09-04.** Renamed; `run.sh`, `.gitignore` and #26 above updated to match.

`run.sh` called `paper_book/build.py` and `.gitignore` excluded `paper_book/contacts/`, but neither the
directory nor the script had ever been written — so `./run.sh book` and `./run.sh export` both failed with
a Python "no such file" error while `CHANGELOG.md` listed them as delivered commands. Given the folder had
to be created anyway, it takes the shorter name, and there is exactly one name for it rather than two.

### 39. One typst renderer for the book and the per-country briefs
**2026-09-04.** `book/build.py --briefs` emits 27 standalone A4 PDFs from the same `country_entry()` that
renders the book's gazetteer chapter. `run.sh export` points at it. The Chrome-headless export path implied
by `init.sh`'s browser check is abandoned.

The alternative was printing the React app's `/country/:iso` route to PDF with headless Chrome. That gives
web CSS in a print context: no facing-page margins, no widow and orphan control, and page breaks that fall
where the viewport says rather than where the document should break. Acceptable for a screenshot, weak for
a document handed to a ministry.

The deeper objection is #6. Two renderers means two places the same country's figures can diverge, which is
the failure mode the single-dict rule exists to prevent. A brief is the gazetteer entry plus a title block —
about forty lines of shared code, not a second pipeline. `country_entry(c, standalone=True)` promotes the
section headings by one level and drops the chapter title; everything else is identical by construction.

Chrome is still required for the Playwright E2E suite (#22), so `init.sh` keeps the check — but its stated
justification was corrected, since it claimed Chrome was needed for an export that no longer uses it.

*Would change if:* a brief needs a chart the model cannot emit as typst or SVG.

### 40. A5 book, A4 briefs
**2026-09-04.** Two page geometries in `templates/style.typ`, sharing colours, type scale and table helpers.

A book that is read through and a brief that is handed across a desk are different objects. The A5 interior
takes recto part openers and a page break per country; the A4 brief takes a title block and no forced breaks
at all, because it is meant to be read straight through in two pages. The two wrappers are deliberately not
factored into one parameterised function — the page geometry and the heading behaviour genuinely differ, and
the shared part is small enough that duplicating fifteen lines is clearer than the abstraction that would
avoid it.

### 41. The book and web build output is never committed
**2026-09-04, scope corrected 2026-09-08.** `book/build/` and `web/dist/` are gitignored. The typeset
briefs and the book are built on demand.

**This entry was written as "no generated PDF is ever committed", which contradicted #24 on the same
day** and left `README.md` asserting something the tree did not do. It governs the *typst build
directories*, not every generated binary: the tracked per-country poster and briefing PDF under
`countries/<ISO>/` are deliverables under #24, kept honest by #51-#53. See #51 for why the two
pipelines exist and which rule applies to which.

Twenty-eight PDFs at roughly 40 KB each for the briefs and 700 KB for the book is about 1.8 MB per build —
and CI already regenerates model outputs on every push, so any change to `model/` would rewrite all
twenty-eight binaries. Git history never shrinks, and `~/dev/CLAUDE.md` is explicit that regenerable build
artifacts stay out of it. The build is deterministic given `.build-epoch` (#34), which is what makes not
committing them safe: the PDF is always reproducible from source at any commit.

This is also why the briefs are written to `web/dist/briefs/` and never to `web/public/`. `public/` is
tracked — `eu27.json` lives there and CI asserts it is fresh — so a PDF placed there would be committed by
the same rule that keeps the bundle honest.

### 42. The PDFs ship from the existing web app, not a separate one
**2026-09-04.** `./run.sh build` writes the briefs into `web/dist/briefs/<ISO>.pdf`, served from the same
origin as the app at `/briefs/<ISO>.pdf`.

A separate PDF site would need its own deployment, its own domain, and its own copy of the provenance
banner that #25 requires everywhere — three new things to keep in sync, for content derived from the data
the main app already serves. It would also put the PDF a navigation hop away from `/country/:iso`, which is
the page where a reader actually wants it.

The reason to split would be a different audience or different access control. There is one audience here,
and it is the same one for both.

*Open:* Vercel's build image has no typst, so a deploy built there produces the app without the briefs.
Either the build installs typst, or CI builds the briefs and attaches them to a GitHub Release with the app
linking out. Unresolved; the local build is correct either way.

### 43. The outreach map is institutional; individuals live elsewhere
**2026-09-04.** `OUTREACH.md` carries offices, agencies, committees and press desks for all 27 states plus
the EU layer. Named individuals go in the private `sovereign-data-centers-contacts` repo, under #26.

Two-thirds of the map was already in `model/eu27_parameters.csv` — `sovereign_cloud_initiative`,
`certification_scheme` and `procurement_vehicle` name the operator, the certifying authority and the buying
channel for every member state, researched against primary sources when those columns were built. Rebuilding
that from memory would have produced a second, less reliable copy of a dataset the repo already has.

The file therefore carries an explicit provenance table separating what it inherits from the CSV from what
was added from general knowledge. Ministry names, parliamentary committees and press desks are in the second
category and are marked check-before-send: digital portfolios are merged, split and renamed at nearly every
reshuffle, and three of the twenty-seven moved within the last two years.

Send order is operator, then scrutiny, then trade press, then ministry — not the reverse. The operator holds
the workload inventory the model is guessing at and is the only party who can falsify it, and a ministerial
send that arrives before the operator has seen it tends to be routed back to that operator as a threat.

---

## Artefacts, outreach and deployment

### 47. Per-country infographics are generated from the model, never illustrated
**2026-09-05.** Each country gets a one-page PNG infographic and a PDF briefing, rendered
by headless Chrome from a `/poster/:iso` route in the app.

Every figure comes from `country_data.build()` via the JSON bundle, so a poster cannot
disagree with its brief. This is the deliberate opposite of the existing Dutch artwork
(decision 48), whose grid routing, cable landings and growth curves were drawn by an image
model and derive from nothing in this repository — and which still shows PUE 1.70 against
the model's 1.25.

Two rules the layout follows, both from the security audit:

- **No state emblems, flags, crowns or official-looking wordmarks.** These are concept
  posters for a programme that exists in no member state, and they say so. This rule is about
  *artefacts*, which travel without the page that explains them; #61 records where a country
  flag emoji is nonetheless allowed, and it is navigation only.
- **The caveat is printed on the poster.** An image gets shared without the page that
  explains it, so the disclaimer has to travel with the pixels.

Poster height is measured per country from the rendered DOM rather than fixed: region
counts vary from two to five, so a fixed height would clip Romania or leave Malta
two-thirds blank.

### 48. AI-generated assets must be labelled at every reference
**2026-09-05.** Arising from the security audit.

`countries/NL/Rijkscloud-...png` carries C2PA Content Credentials naming OpenAI `gpt-image`
v2.0 and the IPTC code `trainedAlgorithmicMedia`, plus an invisible watermark. None of this
was documented anywhere, which is the worst case: the provenance is embedded, so a
C2PA-aware viewer reveals it before the repository does.

Any AI-generated asset must be labelled wherever it is referenced, with its tool, date and
what in it is model-derived versus illustrative. Future artwork avoids state iconography
entirely.

Remediation is tracked in `ROADMAP.md` and not yet complete.

### 49. Outreach lists: institutions in public, individuals never
**2026-09-05.** Extends decision 26 after a request to put named politicians and
journalists in the README.

The public README carries the institutional map — ITRE, LIBE, IMCO, DG CONNECT, DG DIGIT,
the Telecom Working Party, ENISA, and each state's procurement body and cloud operator,
which are already columns in the dataset. Named individuals live in
`paper_book/contacts/`, gitignored, in official capacity only and with no personal contact
details.

Roles outlast people: "Chair, ITRE" survives an election and a name does not, so the
institutional map is also the more durable artefact.

**A near miss worth recording.** `.gitignore` contained `book/contacts/` rather than
`paper_book/contacts/` — the prefix was lost when the line was written, so the directory
intended to hold named individuals was never actually ignored. The security audit reported
it clean only because the directory did not yet exist. Found and fixed 2026-09-05 before
any file was created; the rule is now widened to `**/contacts/` and `*-contacts.md` so a
differently-named file cannot slip through. Verified with `git check-ignore`.

### 50. Deployment is staged, and the domain is deliberately unofficial-sounding
**Amended by #99** (2026-10-08): the web app now carries the EU27.CLOUD brand, whose lockup reads "European Union
Data Sovereignty Initiative"; the footer's statement of non-affiliation stays.
**Stage 3 amended by #80** (2026-09-30): the domain is attached before the audit gate, still `noindex`; announcing it stays gated.
**2026-09-05.** Vercel, static build from `web/dist`, Git-integrated: `main` ships
production, every PR gets a preview URL.

Three stages, gated on verification rather than on readiness of the code:

| Stage | Where | Gate |
|---|---|---|
| Now | `*.vercel.app`, `noindex` via `robots.txt` | none — it is a working draft |
| Next | `*.vercel.app`, indexable | Tier-1 legal cells verified against primary sources |
| Then | `eu27.cloud` | sampling audit error rate measured |

**The domain choice follows from decision 25.** Unverified claims about what 27
jurisdictions require must not sit under a name that reads as a register.
`eusovereigncloud.eu`, `sovereigncloud.eu` and anything on `.eu` imply an EU institution;
`.org` implies an established NGO. `eu27.cloud` is short and topical, and `.cloud`
unmistakably signals a project. It pairs with a masthead line stating the work is
independent and unaffiliated.

`vercel.json` sets a strict CSP (`default-src 'self'`, no inline scripts, `frame-ancestors
'none'`), `nosniff`, `DENY` framing and a restrictive `Permissions-Policy`. The app makes
one network call — fetching its own data bundle — so nothing looser is needed. No
analytics.

### 44. The frontier-model question is answered in-repo, and kept separate from the capacity case
**2026-09-06.** "Why not build our own model too?" comes up every time the sovereign cloud
plan is discussed, so the answer now lives in `countries/NL/FRONTIER-MODEL.md` rather than
being re-argued each time. It was drafted as a standalone repo and merged here instead,
because it is a Netherlands-specific note that only makes sense next to the NL reference case.

**It is deliberately framed as a separate ask, not an extension of RijksCloud.** A frontier
training cluster is ~150 MW against RijksCloud's 14.2 MW design load, and $4-6B against
€339M CAPEX — more than ten times the power and an order of magnitude more capital, for one
purpose. The two proposals compete for the same scarce input, Dutch grid connections, and
bundling them would make the government-cloud case politically unaffordable. The note says so
explicitly, and also records where the arguments against a national frontier model are
*weaker* against a sovereign cloud (jurisdiction is not fungible; buildings depreciate over
decades, accelerators over three years).

**Placement follows the generation rule.** `GOAL.md`, `params.csv`, `workloads_inputs.csv` and
the region files under `countries/<ISO>/` are rewritten by `generate_countries.py` on every
`run.sh data`. `FRONTIER-MODEL.md` uses a name the generator never writes, so it survives —
the same property `CAPACITY_PLAN.md` and `TODO.md` already rely on. Anything authored that
lands in a country directory must respect this.

The cost figures in it are reconstructed order-of-magnitude estimates, not sourced values,
and are labelled as such. This is a lower evidentiary standard than the model's parameters
and the note must not be cited as if it met the same bar (#25).

### 45. Named individuals move to a separate private repo
**2026-09-06.** Contact material naming individuals no longer lives in this repo under
`.gitignore` protection. It lives in the private repo `sovereign-data-centers-contacts`, one
directory per ISO code, mirroring `countries/`. #26 stands — the reasoning is unchanged — but
the mechanism is now repo visibility rather than pattern matching. The ignore rules
(`**/contacts/`, `*-contacts.md`) stay as a backstop; the redundant `paper_book/contacts/`
line is dropped.

Filename-based protection kept nearly failing, in the same direction each time. #49 records
the first near miss: `.gitignore` said `book/contacts/` when the directory was
`paper_book/contacts/`, so it went unprotected until caught. The second surfaced while adding
the NL list: `NL-contacts-NOTES.md` reads as contacts-related but does not match
`*-contacts.md`, and would have been committed to a public repo. Both were caught, but the
failure mode is a silent one — the file simply becomes publishable, and nothing complains.

The second reason is backup, and it is the one that actually forced the move. Gitignored
files are not pushed anywhere, so the contact material existed on exactly one laptop, with a
clean `git status` giving the false impression it was safe. A private repo protects and backs
up in the same act.

The `llm-compiler` layered guard (hooks plus a forbidden-path CI check plus Gitleaks) was the
alternative and was rejected: it exists to keep private files *inside* an otherwise-public
repo, which is a harder problem than simply not putting them there. It stays the right answer
for `llm-compiler`, where the private notes and the public code genuinely share a tree.

Also resolves the `paper_book/` leftover from #38. Its `contacts/README.md` — never moved
during the rename — held the actual rules for contact records, and is now `CONVENTIONS.md` in
the private repo.

### 46. The contacts repo is nested inside this one, not merged into it
**2026-09-07.** `sovereign-data-centers-contacts` is now checked out at `contacts/` rather
than living as a sibling directory under `~/dev/projects/`. It is still a separate private
repo with its own `.git` and its own remote — nothing was merged, and no file moved between
repos. #26, #49 and #45 all stand unchanged; this is a change of *where the private working
tree sits on disk*, not of the boundary.

The reason is friction. The private tree mirrors `countries/<ISO>/` one directory at a time,
and working on the NL entry meant two checkouts, two `cd`s and two mental models of the same
country.

**Both of #45's protections survive intact, which is the whole test of this arrangement.**

*Backup*, #45's deciding reason: the nested repo keeps its own private remote, so the
material is still pushed somewhere and still exists on more than one laptop. Merging the
files in under `.gitignore` — the obvious reading of "consolidate them" — would have thrown
this away, and it is the thing #45 says actually forced the split.

*Leak resistance* is now stronger than either arrangement. Git does not descend into a
directory containing `.git`, so `contacts/` cannot be committed here as content at all: `git
add -f contacts/` stages a mode-160000 gitlink, a 180-byte line naming a commit, and no file
contents. Verified on a scratch clone of this repo with the real private files copied in —
473 distinctive tokens in `NL/list.md`, zero of them in the staged diff. That is a structural
property of git rather than a pattern that has to be written correctly, which is exactly what
#49 and #45 record failing twice in the same direction. The `**/contacts/` and `*-contacts.md`
rules stay as a second layer.

**What genuinely gets worse, recorded rather than glossed.** Contact names now sit inside this
repo's checkout, where a `grep -r`, an editor's project-wide search, or an AI assistant working
in the public tree can read them and paste them into a public file. Neither `.gitignore` nor
the nested `.git` protects against that — both stop git, not the reader. The sibling-directory
layout did protect against it, by accident of distance. This is the price of the change and it
is a real one; `ripgrep` and `git grep` both honour `.gitignore` and so skip `contacts/`, but
plain `grep -r` does not.

**A second hazard worth knowing before it bites: `git clean -ffd`.** One `-f` refuses to remove
an untracked nested repository — verified, `git clean -nxfd` does not list `contacts/`. Two
does: `git clean -nxffd` lists it, and would take the private repo's `.git` with it. Keep the
private repo pushed and this costs nothing; leave work uncommitted there and a routine cleanup
of build output destroys it.

**Why not a git submodule**, the other way to get one tree. `~/dev/DATA_PRIVACY.md` §1 rejects
private submodules inside public repos and is right to: `.gitmodules` is tracked, so the public
repo would publish the private repo's URL, and `git clone --recurse-submodules` would fail for
every visitor without access, which is all of them. A nested repo that the outer one simply
ignores has the same ergonomics and none of that.

The `llm-compiler` five-layer guard remains rejected for the reason #45 gives, and now for one
more: it exists to protect files that share a git history with public code, and these do not
share one at all.

Also removes `book/contacts/` — an empty directory left behind by the `paper_book/` → `book/`
rename in #38 and the near miss in #49. An empty directory called `contacts` in this repo is a
trap for exactly the mistake the rules above exist to prevent.


## Maintenance and integrity

### 51. The per-country artefacts ship in the repository, deliberately
**Superseded in part by #76** (2026-09-29): the Chrome briefing PDF is retired; one per-country PDF remains.
**2026-09-08.** Resolves the contradiction the second security audit found: #24 said the
posters and per-country PDFs are tracked, #41 said no generated PDF is ever committed, both
were dated 2026-09-04, and `README.md` quoted the second one absolutely while the tree did
the first. 54 binaries sat in that gap for three days.

**They stay tracked, and #41 is scoped to the build directories it actually meant.** There
are two PDF pipelines and only one of them produces a deliverable:

| Pipeline | Output | Tracked |
|---|---|---|
| `book/build.py --briefs` (typst), `./run.sh export` | `book/build/briefs/`, `web/dist/briefs/` | no — #41 |
| `model/export_artifacts.py` (headless Chrome), `./run.sh artefacts` | `countries/<ISO>/<ISO>-infographic.png`, `<ISO>-briefing.pdf` | yes — #24 |

The audience argument decides it. These are for policymakers and civil servants, and the
repository is a distribution channel (#25): a reader who opens `countries/EE/` should find
Estonia's poster and brief there, not a build instruction requiring Node, Chrome and a
local web server. 12.7 MB of a 17 MB `.git` is a real cost, and a bounded one — 54 files
that only change when the model does.

What made it defensible rather than merely convenient is that both objections got fixed
rather than accepted: the churn (#53) and the staleness (#52).

**One tension is recorded rather than resolved.** #39 abandoned the Chrome-headless PDF path
the day before #47 reinstated it, on the grounds that web CSS in a print context gives no
facing-page margins, no widow control and page breaks where the viewport falls — "acceptable
for a screenshot, weak for a document handed to a ministry". That judgement stands, and it is
why the *site* serves the typst brief at `/briefs/<ISO>.pdf`. What #39's other objection —
two renderers, two places the figures can diverge (#6) — does not reach is these two, because
both render from the same `country_data.build()` dict and cannot disagree about a number.

So the tracked PDF is the web brief as printed: an offline copy of what the page shows,
next to the data it was made from. The typeset A4 brief remains the document for a ministry.
If only one per-country PDF should exist, the typst one is the one to keep, and that is a
product decision rather than a housekeeping one — `ROADMAP.md` carries it as an open
question.

### 52. A tracked binary CI cannot rebuild carries a manifest
**2026-09-08.** `countries/ARTEFACTS.csv` records each artefact's sha256 **and the sha256 of
the JSON bundle it was rendered from**. `tests/test_artifacts.py` fails when the recorded
bundle hash is not the current one.

The bundle hash is the load-bearing half. CI has no Chrome and no built app, so it cannot
re-render an artefact and diff it the way it already does for the markdown briefs — which is
exactly how these drifted. `fe4a2f3` rendered all 54. `f03fde7` changed the bundle and
re-rendered the 27 posters **but not the 27 PDFs**, which kept a provenance line reading
"Generated 2026-09-03" for the next three days: wrong, on the artefact specifically designed
to travel without the page that explains it, and invisible precisely because half the
artefacts *had* been refreshed. A hash comparison needs no browser, so the gap closes where
the tooling is thin.

**What this does not gate is presentation.** The manifest ties an artefact to the data it
shows, not to the version of the app that drew it; a CSS change does not invalidate 54
binaries. Wrong numbers are the harm worth failing a build over, and a restyled poster is not.

A partial run (`export_artifacts.py DE MT`) carries the other 25 rows' recorded hashes over
unchanged rather than stamping today's bundle onto them. A manifest that certifies files it
did not render is worse than none, because it looks like a check.

The cost is deliberate: change the model without Chrome installed and CI goes red until the
artefacts are re-rendered. That is what "the countermeasure is a check that fails the build"
means when the thing being guarded is a binary.

### 53. Chrome's wall-clock PDF dates are rewritten to the build epoch
**2026-09-08.** `/CreationDate` and `/ModDate` are rewritten to `SOURCE_DATE_EPOCH` (#34)
after each PDF is printed, so re-running the exporter on unchanged data produces
byte-identical files.

Without it the 27 tracked PDFs were the only part of the repository that was not
byte-reproducible: #15 makes the generator deterministic and #34 pins the date precisely so
a diff shows real changes, and then Skia stamped the current time into 27 binaries. Verified
by running the full export twice and comparing hashes, not by reasoning about it (#14).

**The rewrite is length-preserving on purpose.** A PDF's cross-reference table is a list of
byte offsets, so a replacement one character longer corrupts every object after the Info
dict. Chrome always writes the full `D:YYYYMMDDHHMMSS+00'00'` form, which is exactly as long
as the pinned stamp; a substitution that would change the length is skipped rather than
risked.

`/Creator` and `/Producer` still name the local Chrome and Skia build, so byte-identity holds
within one Chrome major version, not across them. The posters need nothing: Chrome writes no
`tIME` or `tEXt` chunk into a screenshot PNG.

### 54. Verification is a ledger with quotes, ratcheted by a test
**2026-09-08.** `model/sources.csv` holds one row per sourced claim —
`country,column,url,publisher,retrieved,confidence,quote` — validated by `model/sources.py`
and guarded by `tests/test_sources.py`. `VERIFICATION.md` is the working document.

**The quote is the requirement, not the URL.** A link proves a page exists; it does not show
that the page says what the cell claims, and a source that has since been rewritten is worse
than no source because the cell looks checked. Any row whose quote is under 20 characters
fails validation.

**Tiering follows the risk, not the effort.** The three columns that assert a legal
obligation — `legal_instrument`, `data_classification`, `certification_scheme` — require the
instrument itself (`confidence: primary`). The four describing what a state runs, buys or
depends on take an official government page. The three ordinal columns are author
judgements derived from the others (#10) and are disclosed rather than cited; a source row
for one is a validation error, because pretending a judgement is sourced is the specific
dishonesty #25 exists to prevent. 7 sourceable columns x 27 states = 189 cells.

**`COVERAGE_FLOOR` is a ratchet, not a target.** It may only be raised. The end state
`ROADMAP.md` step 3 asks for — CI failing on any unsourced legal cell — already exists as
`sources.py --strict`, but a gate that fails on the day it lands is a gate someone disables
on the day after. The floor makes progress irreversible without pretending it is complete.

### 55. Decision numbers are unique, and a test enforces it
**2026-09-08.** `tests/test_docs.py` asserts that `DECISIONS.md` numbers are unique and
contiguous, and that every `#N` reference in the documents resolves to an entry.

This register had two entries numbered 38, two numbered 39, two numbered 40 and two numbered
41 for three days. `README.md` cited #41 meaning "no generated PDF is committed" and
`ROADMAP.md` cited #41 meaning the domain choice; both citations were correct, which is the
worst way for a reference to be wrong, because nothing looks broken. The second block was
renumbered to #47-#50 and every reference to it updated.

The same conclusion as #52 and as `ROADMAP.md`'s "pattern worth naming": three of the four
findings in the second audit were drift between what a document asserted and what the tree
did, and prose cannot detect prose going stale.

### 56. Source documents are cached locally; the manifest is tracked, the bytes are not
**2026-09-11.** `model/fetch.py` retrieves every document consulted into `cache/`, which is
gitignored and `.vercelignore`d, and records its sha256, size, HTTP status and retrieval date
in `model/fetch_manifest.csv`, which is tracked. `SOURCES.md` is the arrangement in full.

**Keeping the bytes is the point.** #54 made the quote the unit of evidence precisely because a
URL cannot show that a page still says what it said. But a quote alone cannot be re-checked once
the page is reorganised or the statute consolidated. With the document kept and hashed, a source
that changed under us becomes a detectable finding instead of a cell that merely looks verified.

**Not in git**, because national gazette PDFs run to megabytes, git history never shrinks, and
the workspace rule on large binaries says so. The manifest is the same trade already made for
the per-country artefacts in #52: the hash travels with the repository, the bytes do not.

**A refusal is a row, not a gap.** Twelve of the 36 endpoints tried refuse an automated client —
bot challenges, connections that never complete, one published `Disallow: /`. Each is recorded
with its status. Dropping them would make a blocked source indistinguishable from work not yet
done, which is the distinction this whole workstream exists to preserve.

**Two honesty rules in the fetcher, both learned by getting them wrong first.** Python's
`RobotFileParser.read()` treats a 403 on `robots.txt` as *disallow everything*, so a host that
blocked our user-agent looks identical to one that asked us not to come; only the second is a
rule, so `robots.txt` is fetched directly and its status kept. And Poland's `isap.sejm.gov.pl`
publishes `Disallow: /` but serves `robots.txt` only to browser user-agents — an automated client
is told nothing and sails past a rule that plainly exists. It is marked `forbidden` by hand.
Being *able* to fetch something is not permission to.

### 57. Eurostat columns are pinned to a vintage, not re-pulled to the latest
**2026-09-11.** Each of the six Eurostat columns in `eu27_parameters.csv` names a dataset, a
filter set **and a period**, recorded in `SERIES` in `model/fetch_eurostat.py` and reproduced
per value in `model/eurostat_pull.csv`. The fetcher compares against the pin. It never adopts a
newer period on its own; it says one exists and stops.

**Because "latest" silently mixes vintages.** National accounts arrive at different times, so
the newest period is routinely partial — `nama_10_a64_e` had 10 of 27 states for 2025 and all 27
for 2024. A column assembled from whatever each country had last published is not a comparison,
it is 27 different questions. Pinning also makes drift mean something: a value that no longer
matches its pin is a defect, because the pin cannot move by itself.

**The pins were recovered by measurement, not memory.** Scanning every available period against
the existing column showed five of the six reproduce their pinned vintage to within 0.06%. The
figures were already right; what they lacked was a recorded provenance, which is what
`ROADMAP.md` step 4 actually asked for.

**This decision exists because getting it wrong was cheap and convincing.** The first version of
the fetcher used `nrg_cons=MWH2000-19999` for a column documented as band IC. Band IC is
500–1,999 MWh/yr; that code is band ID. The mis-specified tool reported, with a full table and a
sample of 27, that the column was 10% adrift and the published OPEX was overstated by 12%. All of
it false. A measurement tool that is itself wrong does not fail quietly — it manufactures
findings and attaches evidence to them, which is worse than having no tool. Filters and periods
now carry their reasoning inline, and `tests/test_fetch.py` enforces that every column except the
one known defect reproduces from the source it claims.

### 58. Absence is evidenced by an enumeration, and `confidence: absence` records it
**2026-09-11.** `sources.py` accepts a fourth confidence value, `absence`, admissible for tier 1
alongside `primary`. It cites an **authoritative enumeration** — the competent authority's own
register of schemes — showing the category is empty, rather than an instrument.

**Because the rule as written was unsatisfiable.** 22 of the 81 tier-1 cells assert that
something does not exist, 21 of them in `certification_scheme` ("No national scheme; ISO 27001").
Nothing enacts the absence of a scheme. Under a tier-1 rule admitting only `primary`, those cells
could never be sourced: tier 1 was capped at 59/81 = 72.8%, the ledger at 167/189, and
`--strict` — the end state #54 and `ROADMAP.md` step 3 both point at — could never pass. A gate
that cannot pass is not a strict gate, it is a dead one, and `COVERAGE_FLOOR` would have ratcheted
to a ceiling nobody had written down.

**A claim about a complete list is evidenced by the complete list.** Demanding an instrument for
a negative is a category error, which is why 78% of that column was stuck.

**The guard matters more than the value.** `absence` is the one confidence level that could make
the ledger *less* honest, by excusing a source nobody could find. So a row may only be `absence`
if the cell it cites actually asserts an absence; anything else is a validation error, and
`tests/test_sources.py` asserts the refusal on a real positive cell (France's SecNumCloud).

The alternative considered and not taken: splitting `certification_scheme` into a boolean
`has_national_cloud_scheme` plus a name populated only when true. Cleaner modelling, but a data
migration across 27 briefs, the bundle and the matrix, to fix a schema problem a confidence value
fixes in one line. Revisit if the column needs restructuring for other reasons.

### 59. A feasibility ranking exists, as an authored note and a bounded exception to #10
**Superseded by #77** (2026-09-29): the rule-based, sourced placement replaces this authored grouping.
**2026-09-13.** `FEASIBILITY-RANKING.md` ranks all 27 states by how feasible a combined plan for
sovereign data centers *and* sovereign AI models would be. It was asked for directly, and "which
countries could actually do this?" is the question a reader of the matrix arrives at anyway.

**#10 still governs the model and the app.** Nothing in `eu27_parameters.csv`, the JSON bundle, the
matrix or the briefs gains a score. The exception is confined to one authored note, under four
conditions that carry #10's reasoning into it:

- **Groups, not a score.** States are placed in four groups by judgement, then ordered within them;
  no number is computed, so there is no false precision to quote. The note says the groups are the
  finding and the within-group order is not.
- **The caveats live in the body.** Same rule as the briefs under #25: the unverified status of both
  halves is stated where the ranking is read, not only in a header.
- **The evidentiary standard is stated, and it is low.** The data center half uses the author's
  ordinal columns (2 of 189 legal cells sourced). The model half uses no repository data at all — it
  is general knowledge to roughly May 2026, with no ledger rows. That is below even
  `FRONTIER-MODEL.md`'s bar (#44), and the note must not be cited as if it met the model's.
- **It sits at the repository root, outside the generator.** `generate_countries.py` never writes
  there, so it survives `run.sh data`, as #44 requires of anything authored.

**"Sovereign data models" was read as sovereign AI models**, following #44's framing. If a schema or
data-standards meaning was intended, the model half is replaced rather than amended.

*Would change if:* the model half is sourced (at which point it could become ledger rows and the note a
re-ranking), or the ranking starts being quoted without its caveats, in which case it is withdrawn.

---

## The critical national data register

### 60. Critical national data is a sourced register, not prose
**2026-09-21.** `model/national_data.csv` records, per member state, which Tier 0 and Tier 1
record classes the state holds, the register that holds them, and the official page describing
it — validated by `model/national_data.py`, ratcheted by `tests/test_national_data.py`, and
rendered as a section in all four country renderings.

`TIER0-TIER1-SIZING.md` already had the vocabulary: the identity spine and the legal/fiscal
state, tiered by consequence of loss. What it did not have was a single URL, or any country but
the Netherlands. Its own open items asked for "the 'tiered sovereignty' argument as a reusable
section for country write-ups". This is that, made machine-checkable.

It clones the bargain `sources.csv` strikes (#54) rather than inventing a second one: every row
carries the publisher, the retrieval date and **a quote from the page**, because a URL shows that
a page exists, not that it says what the row claims.

**Three states, not two.** `held`, `not_held`, and no row at all. All fifteen record classes
render for every country, always — a sparse table hides the gap, whereas a full table with twelve
blanks *is* the coverage report, readable by someone who will never run the test suite. A blank
says "not yet recorded" in words, never a dash and never colour alone.

`status: not_held` requires `confidence: absence` and an authoritative enumeration, extending #58.
**This guard is weaker than the one in `sources.py`**, and the docstring says so: there, an
absence claim is checked against the parameter cell in a different file; here the cell *is* the
row, so nothing independent corroborates it. The claim is also more consequential — several
member states genuinely keep fingerprints only on the document chip, so "no central register" is
a real finding a careless row could fake.

Where a register is *hosted* is deliberately not a column. That is a separate factual claim
needing its own source, and recording it unsourced beside sourced cells is what #25 exists to
prevent.

*Would change if:* coverage reaches a point where tier 1 stops being reachable by one researcher,
at which point the published percentage narrows to tier 0 — which is where the sovereignty
argument lives — rather than staying honestly stuck near zero.

### 61. Flags in navigation, never on an artefact
**2026-09-21.** Country flag emoji appear in `countries/SUMMARY.md`, the web country index and
the mobile country list. They appear nowhere else.

This **extends #47, it does not contradict it.** #47's layout rule — no state emblems, flags,
crowns or official-looking wordmarks — exists because a poster travels without the page that
explains it, and must not read as something a government published. An index entry is not a
document: it is a way of finding one, seen beside the country's name and its ISO code, in a table
that says on its face what it is.

So the exclusions are the artefacts, and they are absolute: no flag on a poster, a briefing PDF,
a title block or a wordmark. The book is excluded too, for unrelated reasons — see #62.

The glyph is derived from the ISO code by regional-indicator offset. `EL → GR` is the only
override: Eurostat writes Greece as EL, which is not an ISO 3166-1 alpha-2 code and has no flag
codepoint. Everywhere the flag is shown it is decorative and carries `aria-hidden`, sitting beside
the country name and never replacing it — the name stays the accessible label and the thing the
mobile filter matches on.

### 62. The flag glyph is derived, not stored in the bundle
**2026-09-21.** `model/emoji.py` and `flagEmoji()` in `web/src/utils/format.ts`. Nothing about
flags reaches `web/public/data/eu27.json`.

This **narrows #6**, which is why it gets its own entry rather than an edit to #6. #6 says Python
is the source of truth and everything else renders one dict — but it governs canonical *figures*.
A glyph derived from `iso2`, which is already in the bundle, is presentation, in the same category
as `mw()`, `eur()` and `num()`, none of which live in the bundle either.

The deciding argument is cost, and it is asymmetric. Any new bundle key changes its sha256, which
marks all 54 tracked artefacts stale (#52) and forces a Chrome re-render — in exchange for a
character that by #61 must appear on none of them. Deriving it instead made the whole
table-of-contents change cost zero artefact churn.

Two implementations is the accepted price, and it is smaller than it looks:
`mobile/__tests__/parity.test.ts` already pins `mobile/src/data/format.ts` byte-for-byte to the
web file, so the two TypeScript renderers share one copy; and both implementations are asserted
against the same literal 27-pair table rather than recomputing the same arithmetic twice.

**The book is excluded on separate grounds.** Its interior is mono (#28), and `typst` can only
reach flag glyphs by falling back to Apple Color Emoji — colour, and macOS-only, so `./run.sh book`
would render correctly here and emit empty boxes on any Linux machine, silently. The outline
identifies countries by ISO code instead: `DE · Germany`. Since typst has no short-title, that
means the visible chapter head carries the code, which also makes a 27-entry Contents scannable.
`tests/test_book.py` asserts no regional-indicator codepoint reaches the typst source, so this is
enforced rather than remembered.

### 63. `artifacts/` holds style guides; `artefacts` are the tracked binaries
**2026-09-21.** The new top-level `artifacts/` directory holds one style guide per output
representation. The existing sense of the word — `countries/ARTEFACTS.csv`, `./run.sh artefacts`,
#51 — keeps its narrower meaning: the tracked per-country PNG and PDF.

The collision is real and was accepted deliberately, because the alternative names (`style/`,
`representations/`) were worse at saying what the directory is for. It is mitigated by
`artifacts/README.md` opening with the disambiguation, and by the two senses never appearing in
the same sentence without it.

The guides are the working form of rules that were otherwise spread across this register and a
handful of source comments; nobody could answer "what are the rules for the PDF?" without reading
all of it. They cite decisions by number rather than restating the reasoning, and they are listed
in `tests/test_docs.py`'s `CITING`, so a guide citing a decision that does not exist fails the
suite — which is what stops them becoming decorative.

*Would change if:* a third sense of the word appears, at which point this one is renamed rather
than disambiguated again.

### 64. Distribution, encryption and accountability are one authored note
**2026-09-22.** `DISTRIBUTION-AND-TRUST.md` argues that how widely a sovereign estate can be spread
and how thoroughly it must be encrypted and audited are the same question, and proposes answers to
the governance questions the Dutch reference case has left open since it was written. It is the
second authored note, written under #59's conditions.

**One note, not two.** The obvious split — deployment topology in one document, the governance
triad in another — was rejected because the argument only works joined. Distribution multiplies the
places state data physically sits, which is a straightforward loss until encryption makes a seized
replica inert and a verifiable audit trail makes an unauthorised read detectable by someone outside
the operator. Separating them would have produced one document recommending wide distribution
without its preconditions, and another listing security properties with no account of what they buy.

**#59's four conditions carry over intact.** It proposes rather than measures, so #10 is untouched:
no member state is scored or ordered, and the note contains no figures at all, deliberately — the
model has no term for distributed topology, so any number would be invented. Its caveats sit in the
body. It states its evidentiary standard and that standard is low: it makes no per-country factual
claim, so `VERIFICATION.md`'s tiered bar is not engaged rather than met, and the note says so in
those words. It lives at the repository root, where `generate_countries.py` never writes, so
`./run.sh data` cannot clobber it (#44).

**It answers an open item the repository raised against itself.** `TIER0-TIER1-SIZING.md` item 4
proposed absolute national control for Tier 0/1 and a looser posture for the Tier 2/3 bulk, called
it "worth developing as a section in the country write-ups", and left the mechanism unnamed. The
mechanism is attestation-gated key release, and naming it is most of what makes that proposal
actionable. The same document's item 3 had already concluded that design effort belongs on "key
custody and audit"; nothing in the repository had taken that up.

The Netflix and Cloudflare material is an analogy and is flagged as one. It is cited to public
vendor documentation inline and deliberately kept out of `model/source_urls.csv`, which is the
ledger for parameter cells — adding vendor engineering pages to it would misrepresent how much of
the model is sourced.

*Would change if:* distribution becomes a modelled dimension, at which point the topology half stops
being an argument and becomes a result, and this note keeps only the parts the model cannot express.

### 65. Hand-made or externally generated images live in `countries/<ISO>/assets/`
**2026-09-24.** Amends #2. A country's folder keeps everything about that country in one place, but
not all of it in one flat list: images that are neither model output nor generated by
`export_artifacts.py` go in `countries/<ISO>/assets/`. The first and only one so far is the NL concept
poster, moved from `countries/NL/` with its provenance entry in `ASSETS.md` updated to match.

The line being drawn is between files a script writes and files a person put there. The tracked
briefing PDF and infographic stay where #51 put them, because `ARTEFACTS.csv`, `export_artifacts.py`
and `tests/test_artifacts.py` all name those paths and regenerate them; an asset has no generator,
so it needs its own entry in `ASSETS.md` instead, and a subdirectory makes the difference visible
without opening that file. A top-level `assets/` was the alternative and was rejected on #2's own
reasoning: an image of one country belongs with that country.

Verified: `git grep Rijkscloud-Dutch` names only the new path, and `./test.sh` passes with this
entry in place (it failed on the dangling `#65` citation before it existed).

*Would change if:* an asset is shared across countries, at which point it goes in a top-level
`assets/` rather than being copied into each.

### 66. The private outreach inventory may hold institution-published work contacts, proved on the page
**2026-09-24.** Amends #26/#49 for the private contacts repo only; nothing changes in this one. The
private inventory (`contacts/people.csv`) may now record a work address that the person's **own
institution publishes on its own site** — an MEP's address in the Parliament's open data, a deputy's
address on the parliament's member page — beside the institutional routes it already allowed. Never a
phone number, a private or webmail address, a social handle, or an address found anywhere but that
institution's page. `contacts/CONVENTIONS.md` rule 2 carries the amendment and the GDPR basis
(legitimate interest; an Art. 14 notice at first contact; a `review_by` date on every row).

**Why a mechanical proof rather than a rule.** The research pass that built the inventory was sampled
by an adversarial verifier, which found two of 49 sampled rows carrying a journalist's address that
was on no page at all — built from the outlet's naming pattern. A sample cannot find the rest. So each
row is fetched and checked: the address must appear on its cited page (after undoing Cloudflare,
entity, `[at]` and span-splitting obfuscation), and the seat quote — every cell of it, plus the
person's surname — must appear on the page cited for the seat. An address that is not on its page is
removed, not kept on trust; a page that cannot be fetched leaves the row unchecked, never passed.
Rows go out only when both checks carry a date.

The same bargain as `sources.csv` (#54): a URL shows that a page exists, not that it says what the row
claims. What is new is that a script, not a reader, holds the row to it.

Verified: `python3 contacts/tools/people.py` — 956 rows, 910 people, 0 validation errors, leak check
0 public-repo lines; 850/956 send-ready. `contacts/tools/check_contacts.py` — 929 contacts found on
their page, 27 unreached; 870 seat quotes found, 77 not found, 9 unreached. 78 addresses were removed
because their cited page did not carry them. (Figures from the run after the matching fixes of the
same day; an earlier run, with a bug that rewrote " at " to "@" in quote text, read 845/919/866.)

*Would change if:* a named individual ever needs to appear in this repository, which #26 still forbids.

### 67. One source register; every claim cites a registered document
**2026-09-24.** `model/sources/registry.csv` holds each original document or dataset once, under a
stable `source_id` (`<publisher>:<doc>[@vintage]`); `model/sources/citations.csv` links a claim to it
with a locator and the evidence. Claims are namespaced — `param:`, `assumption:`, `workload:`,
`inventory:`, `record:`, `doc:` — so the same register serves the legal cells, the Eurostat cells, the
planning assumptions, and the IT inventories and Tier 0/1 record counts still to come.
`model/provenance.py` validates it and reports coverage per namespace; `tests/test_provenance.py`
ratchets that coverage the way `test_sources.py` does. Supersedes `model/sources.csv` (#54), whose two
rows migrated; `sources.py` keeps the tiered rule (#54, #58) and reads the register.

**Why one register rather than a sixth ledger.** Provenance lived in five files with five schemas and no
shared key, so a document cited twice was two strings, and only the legal cells could answer "where
does this come from?". The Eurostat cells were the proof: `write_goal()` typed its own citations,
and one of them — "Eurostat LFS 2025" — named a series and year the pinned source (#57) does not use.
Renderings now look citations up; a test fails if a literal "(Eurostat …)" returns to the generator.

**Two rules that make it honest rather than merely tidy.** A dataset citation has no quote, so its
evidence is the locator plus the value found there, and a value that does not reproduce the cell
within 0.5% is cited but not counted as sourced — which is why every brief now says, beside the
public-administration employment figure, that it does not reproduce its source. And
`confidence: assumption` declares a working assumption as one, with its rationale; it is counted as
*declared*, never as sourced. The launch gate is every published namespace at full sourced coverage,
with assumptions either sourced or visibly declared (widening #25, at the author's instruction of the
same date).

Verified: `python3 model/provenance.py` — 8 sources, 164 citations, 0 errors; `param` 138/621
supported (2 legal cells + 136 reproducing Eurostat cells; 26 `gov_employment_k` cells cited, not
supported), `assumption` 0/22. `capacity_model.py --all --json --no-write` byte-identical to the
pre-change baseline; `eu27.json` unchanged (sha256 `e472325f…`, the hash `ARTEFACTS.csv` records),
so no tracked artefact is stale; the regenerated diff is citation text only (26 `GOAL.md`, 27
`params.csv`). `./test.sh` passes: 94 Python, 66 Vitest, 15 Playwright.

*Would change if:* the register outgrows CSV review — thousands of citations — at which point it moves
to SQLite with a CSV export for diffs, keeping the same schema.

### 68. The public institutional register routes by web page, never by email address
**2026-09-24.** `model/institutions.csv` admits an https page (contact page, press office, secretariat,
web form) or a postal address as a body's route, and no email address at all — not even a generic
inbox such as `press@`. `model/institutions.py` rejects `mailto:`; the private screen
(`contacts/tools/check_institutions.py`) also tests every candidate with the commit gate's own
patterns, so a row the gate would block never reaches a commit.

Found by the gate, not by review: the first fill of the register (91 rows, 53 routed by `mailto:`) was
blocked at commit for "real email address" and "phone-number-shaped value". `institutions.py` had
allowed a generic inbox and rejected only a `first.last@` shape — a finer line than the gate draws,
and a line a regex can get wrong in either direction. The gate's rule is simpler and holds: this
repository is public, so it carries no addresses. The page that publishes an inbox is as good a route
for a reader, and survives the inbox being renamed.

Cost, accepted: coverage fell from the 67 pairs the email-routed rows would have filled to 25. Those
bodies are not lost — their inboxes are in the private repo — but each needs its contact page found
before it enters this register.

Verified: `python3 model/institutions.py` — 37 rows, 25/324 pairs, 0 errors; the gate passes the
commit that adds them; `contacts/tools/people.py` leak check 0 lines.

*Would change if:* the gate gains a per-file allowance for published institutional inboxes, which is a
policy change in `dotfiles`, not here.

### 69. A register's existence is the claim `record:<ISO>:<class>:register`
**2026-09-26.** `national_data.csv` keeps only the facts about a register (tier, class, status, name,
holder). The page that describes it is in `sources/registry.csv` and the quote in
`sources/citations.csv`, under the claim `record:<ISO>:<record_class>:register`. #67 had reserved
`record:<ISO|*>:<record_class>:<count|size>` for the Tier 0/1 counts and sizes still to come; this widens
the kind to `<register|count|size>` rather than taking the bare 3-part `record:<ISO>:<class>` the TODO
first proposed, so that a register's existence, its record count and its record size for the same class
sit side by side without colliding. `provenance.py` now checks the shape and counts the 405 (country,
class) register claims as the namespace's denominator, which without it would have reported 3 of 3.

`national_data.load()` joins the citation and registry entry back into the old row shape, the adapter
`sources.load()` used in #67, so the validator and all four renderers are unchanged and every output
is byte-identical. Putting `source_id` into `eu27.json` is still ROADMAP step A2, a separate change
to the bundle. The three source ids (`rvig:brp`, `kadaster:brk`, `kvk:handelsregister`) carry no
vintage: they are live pages, dated by each citation's `retrieved`. All three pages were re-read on
2026-09-26 and still carry their quotes verbatim.

Verified: `python3 model/provenance.py` — 11 sources, 167 citations, 0 errors; `record` 3/405
supported. `python3 model/national_data.py` — 0 errors, 3/405 pairs. `for_country()` for all 27
countries and `capacity_model.py --all --json --no-write` are both byte-identical to the pre-change
baseline. After `./run.sh data`, `countries/`, `web/public/data/` and `mobile/assets/` show no diff,
and `eu27.json` is still sha256 `e472325f…`, the hash `ARTEFACTS.csv` records. `./test.sh` passes:
106 Python, 66 Vitest, 15 Playwright. `mobile` `npm test` passes: 19 Jest.

*Would change if:* a record class turns out to need more than one register per country (a federal
state with one register per Land), at which point the kind gains a qualifier rather than the row
gaining a second citation.

### 70. `eu27.cloud` is registered through Vercel, not an EU registrar
**Superseded by #80** (2026-09-30): the domain was registered at iwantmyname, and its DNS stays there.
**2026-09-27.** #50 chose `eu27.cloud` for stage 3; this settles where it is bought. It is registered
through Vercel on the team `pieteradejongs-projects`, the same account the site already deploys from, so
the domain, its DNS and the project sit in one place. It is bought now to hold the name. It is **not**
attached to the project until the stage-3 gate in #50 is met, so the site stays on `*.vercel.app` with
`noindex`.

Rejected:
- **An EU registrar with EU-hosted DNS and DNSSEC**, the approach `EU27-CLOUD-BRIEF.md` recommends. It
  fits the project's subject better, but it would mean a second account and wiring DNS across providers,
  for a domain that does not serve anything yet. Whether Vercel DNS supports DNSSEC has not been checked.
- **`eu.cloud`**, which is unavailable. It would have failed #50's test anyway, because a bare `eu`
  looks more official than any `.eu` name.
- **Defensive registrations** (`eu-27.cloud`, `eu27dc.cloud`, `eu27.eu`, all suggested by the brief).
  `eu27.eu` is ruled out by #50. The others are not worth their renewal cost for an unindexed draft.
- **`eu27.dev`**, which renews at $13/yr against `eu27.cloud`'s $24. Rejected because `.cloud` is the name
  #50 argued for, and $11 a year does not justify reopening that choice.

Price: $7.99 for the first year, **$24/yr on renewal**. The README's "$9.99/yr" (checked 2026-09-11) was
the first-year price and has been corrected.

Verified: availability and price only. On 2026-09-26, Vercel `get_bulk_availability` returned
`eu27.cloud` `available: true` and `eu.cloud` `available: false`. `get_bulk_price` returned purchase
7.99, renewal 24. `get_purchase_quote` for the team returned cost 7.99 USD with auto-renew on.
**Registration: NOT YET.** It is waiting on the registrant's postal address. Recheck with
`vercel domains ls` after the purchase and record the result here.

*Would change if:* the project starts to present itself as practising the sovereignty it describes, at
which point moving the domain to an EU registrar and EU-hosted DNS becomes worth the extra account.

### 71. Deploys are built locally and uploaded prebuilt, so the site can serve the PDFs
**Superseded by #81** (2026-09-30): the same prebuilt upload, now built in GitHub Actions on every push to `main`.
**2026-09-29.** `./run.sh deploy` runs `vercel build --prod` on this machine and uploads `.vercel/output` with
`vercel deploy --prebuilt --prod`. `vercel.json`'s `buildCommand` builds the web app, the 27 briefs and the
EU-27 country report (`book/build.py --report`) into `web/dist/`.

The report and the briefs need `typst` and `pandoc`, which Vercel's build image does not have (#42's open
item). There were three ways to get them onto the site:

- **Install both on Vercel in the build command.** That means downloading pinned binaries with checksums on
  every build: a supply-chain surface (`supply-chain.md`) to maintain, for a site that already deploys by hand
  from one machine.
- **Commit the PDFs.** About 2.8 MB for the report plus 1.5 MB of briefs, rewritten whenever the model changes.
  #41 already rejected that for typst output.
- **Build locally, upload prebuilt.** This one: no new tooling anywhere, nothing binary in git. Deploys were
  already manual and local (#50 as corrected in DEPLOYMENT.md), so it closes off nothing that was working.

The cost is that a deploy needs this machine's toolchain, and a remote build now fails at the report step.
That is deliberate: it cannot quietly ship a site without its PDFs. `run.sh deploy` checks for both tools
before building.

It also moved the SPA rewrite to `/index`. Prebuilt output under `cleanUrls` serves `index.html` at `/index`,
and the earlier `/` destination 404'd the home page on the first prebuilt preview.

Verified: 2026-09-29, prebuilt preview `sovereign-data-centers-936ynu1tv`, via `vercel curl`: `/`, `/matrix`,
`/country/DE` and `/countries` 200 text/html; `/eu27-report.pdf` and `/briefs/DE.pdf` 200 application/pdf,
report sha256 identical to the local build; CSP present. Production: NOT YET.

*Would change if:* the site needs deploys from CI or from another machine. The next step would be pinned
typst and pandoc binaries in the build command.

---

## Own fundamentals, one pipeline, sourced output

### 72. Each country is analysed on its own fundamentals; the Netherlands is one of 27
**Decision.** 2026-09-29. No country's figures or text are derived from, scaled from or framed against
another country. `scale_workloads`, `model/scaling_rules.csv`, `BASELINE`, the `nl`/`nl_s` arguments of
`country_data.build` and the `scale.*_ratio` fields are removed. The Netherlands is analysed like the other 26;
its hand-written `countries/NL/GOAL.md` and `FRONTIER-MODEL.md` stay as notes, not inputs.

**Problem.** Every figure for 26 states was the Dutch workload table multiplied by that state's population,
public-administration employment and GDP relative to the Netherlands (`generate_countries.py`
`scale_workloads`). The text followed: "What is structurally different from the Dutch case", "Relative to
the Dutch baseline". A reader in Tallinn or Madrid got a Dutch plan resized, not an analysis of their
state. The Netherlands was chosen only because its spreadsheet came first; no entry ever justified it.

**Alternatives considered.**
- **Own fundamentals, sized from each state's critical holdings (chosen).** See #73.
- **Keep the scaling, reframe the text.** *Why not:* the numbers would still be Dutch numbers resized, so the
  framing would be cosmetic and the claim of a per-country analysis untrue.
- **Scale from an EU-average template instead of NL.** *Why not:* removes the Dutch bias but keeps the
  defect: a state is still a resized template, not measured.
- **ROADMAP Plan B as written: anchor on IT inventories, fall back to IT spend relative to NL.** *Why not:*
  its fallback keeps the Netherlands as the denominator; it is superseded here, and its inventory idea is
  folded into #73.

**Closes off.** Every figure that depended on the Dutch table: the 27-country golden file
(`model/eu27_results.csv`), the spreadsheet reproduction as a test of the other 26, and any sentence that
explains a state by contrast with another. Supersedes #5 and the premise of #8 (workloads as Dutch rows
renamed per country).

**Verified:** 2026-09-29. `tests/test_model.py` `NoCountryIsDerivedFromAnother`: changing the Netherlands'
parameter row leaves the other 26 documents identical; no other brief contains "Dutch" or "Netherlands";
the bundle has no `capacity`, `scale` or `totals`. `python3 -m unittest discover -s tests` → OK. The
spreadsheet reproduction is **kept**, renamed `EngineReproducesTheSpreadsheet`, as an arithmetic check of
the capacity engine only; its Dutch inputs size nothing.

*Would change if:* a sourced, published per-country figure turns out to be unobtainable for most states and
the project decides an explicitly labelled common template is better than showing nothing.

### 73. Sizing comes from each state's inventory of critical holdings; until then, "not yet sized"
**Decision.** 2026-09-29. Capacity is sized bottom-up from an inventory of each state's critical data
holdings (`model/holding_classes.csv`, 39 classes; per-country rows extending `national_data.csv`).
Record counts and data sizes come from cited sources. A state without enough measured holdings shows
"not yet sized" and its coverage ("7 of 39 holdings measured"), never a scaled estimate. The Dutch-scaled
servers, MW, sites and CAPEX are withdrawn from every output.

**Problem.** After #72 there is no demand input: the only one was the Dutch table. Something measurable per
state has to replace it, and the author asked for the holdings a state cannot let depend on foreign
control to be inventoried, prioritised and documented first.

**Alternatives considered.**
- **Critical-holdings inventory, researched across all 27 at once (chosen).** Directly measures what must
  stay sovereign; the Tier 0/1 register (#69) and the reserved `record:…:count/size` claims already point
  here.
- **Driver × intensity (citizens × cores per eID user, etc.).** *Why not:* the intensities would be declared
  assumptions with no per-state source, so it trades a Dutch template for an invented one.
- **Wait for government IT inventories (server counts, IT spend).** *Why not:* almost none are public;
  most states would show nothing for months, and spend is not capacity.
- **Keep the scaled figures in a labelled appendix until replaced.** *Why not:* the author chose to withdraw
  them; a labelled number still gets quoted without its label.

**Closes off.** Headline EU-27 totals, the scenario sandbox and the site-count finding (#12) until enough
states are sized. The web shows "sized: n of 27" instead.

**Verified:** NOT YET. Taxonomy written (`model/holding_classes.csv`, 39 rows); research run for all 27 in
progress; nothing admitted yet.

*Would change if:* after the research run, fewer than a handful of states have any measurable holding, in
which case the sizing method itself needs revisiting.

### 74. One content model and one design-token source feed every output
**Decision.** 2026-09-29. `model/document.py` turns the #6 fact dict into one ordered document per country
(sections → blocks → claim ids). The typst report, the 27 per-country PDFs, the web country page and
`GOAL.md` all render that structure. `design/tokens.json` is the single source for colour, type and
spacing, generated into web CSS, typst and the mobile constants.

**Problem.** One country was drawn by seven renderers with seven section lists (GOAL.md 13, book 5, web 9,
poster 7, mobile 10, the report via pandoc, the Chrome PDF), and styled by four unrelated palettes. #6
unified the facts; nothing unified what is said about them or how it looks.

**Alternatives considered.**
- **One content model, thin renderers (chosen).**
- **Keep markdown as the source and convert it (the v1 report, pandoc over GOAL.md).** *Why not:* the web
  cannot make an interactive table or a claim marker out of prose, and regex-patching pandoc output is
  brittle.
- **Render PDFs from the web page with headless Chrome (the #51 briefing path).** *Why not:* print output
  inherits screen layout, needs Chrome in the build, and cannot do footnotes on the page.
- **Leave the renderers separate and add a parity test.** *Why not:* tests detect drift after the fact; one
  structure removes it.

**Closes off.** Hand-written prose inside React components or typst code; per-output section lists; the
pandoc dependency. Supersedes #39's scope and the "deliberately not shared" section lists.

**Verified:** 2026-09-29. `model/document.py` builds all 27 documents; `book/report.py` (report and 27
country PDFs), `model/generate_countries.py` (27 GOAL.md) and the web `DocumentView` render them.
`design/build_tokens.py --check` passes (`tests/test_tokens.py`). pandoc and `goal_body()` are removed.

*Would change if:* an output needs content that genuinely has no place in the others (the poster is the
likely case), in which case it gets its own block type, not its own renderer.

### 75. Every claim is sourced on the page and in an appendix; the build fails otherwise
**Decision.** 2026-09-29. Every factual sentence or table cell in the content model carries claim ids that
resolve through `model/provenance.py` to the source register. PDFs print numbered footnotes at the foot of
the page and an appendix listing each source once (title, publisher, URL, retrieval date, document sha256,
archived copy, and every claim that cites it with its quote). The web shows a marker that opens the same
record. A declared assumption is shown as an assumption, never as sourced. `test.sh` fails on any factual
claim without a citation.

**Problem.** The register held 138 sourced cells of 621, and no output showed a single source to the reader.
The author requires source documentation for everything, "unimpeachable".

**Alternatives considered.**
- **Footnotes plus appendix, generated from the register, with a hard gate (chosen).** Every source is
  mechanically checkable: the document is fetched, hashed, and the quote must appear in it.
- **Appendix only.** *Why not:* a reader of page 40 cannot tell which statement rests on which source.
- **Links only (URL per claim).** *Why not:* links rot and pages change; without the hash, the quote and an
  archived copy, a link proves only that a page existed.
- **Warn instead of fail on unsourced claims.** *Why not:* a warning is how 483 unsourced cells accumulated.

**Closes off.** Publishing any statement the register cannot back. Most of the current posture text is
unsourced and will show as such until researched.

**Verified:** 2026-09-29. `python3 model/document.py --check` → "27 documents checked, 0 unsourced facts",
now a `test.sh` stage. `tests/test_book.py` asserts one footnote per fact span and that every footnote
link lands on an appendix entry; the web e2e test follows a footnote to its source.

*Would change if:* never for the gate itself; the display format may change.

### 76. EU colours without the emblem; one per-country PDF
**Superseded in part by #99** (2026-10-08): on the web app only, the EU27.CLOUD badge (a ring of stars), the flag
"27" favicon and the "European Union Data Sovereignty Initiative" lockup now appear. The PDFs and posters keep this rule.
**Decision.** 2026-09-29. All outputs use EU blue `#003399` and gold `#FFCC00` from `design/tokens.json`. No
circle of stars, flag or other official mark appears anywhere (#50 and `artifacts/README.md` invariant 3
stand). The Chrome-printed `countries/<ISO>/<ISO>-briefing.pdf` and the mono typst briefs are retired;
the one per-country PDF is `/report/<ISO>.pdf` from #74. The PNG posters stay for now.

**Problem.** The v1 report drew the circle of stars on a flag-blue cover, which broke invariant 3. The web
used Warm Neutral + Terracotta (#21), the book mono (#28), the report EU blue. There were three different
per-country PDFs.

**Alternatives considered.**
- **EU colours, no emblem, everywhere (chosen).** Recognisably European without looking official.
- **Keep the stars with a disclaimer.** *Why not:* #50's reason is that the work must not be mistaken for an
  EU institution's; a disclaimer does not undo what the emblem signals first.
- **EU theme on PDFs only.** *Why not:* two brands to maintain for one body of work.
- **Keep all three per-country PDFs.** *Why not:* three documents that disagree about the same country.

**Closes off.** The terracotta web theme (#21, superseded for this project) and the #51 Chrome PDF path.
#28's mono rule remains for a printed book edition only.

**Verified:** 2026-09-29. `tests/test_tokens.py` fails on any star shape in a template and on any hex
colour in a web component. `tests/test_artifacts.py` `Retired` fails if a briefing PDF reappears;
`git ls-files 'countries/*/*-briefing.pdf'` → empty. `vercel.json` redirects `/briefs/:iso.pdf`.

*Would change if:* the project is formally endorsed by an EU body and permitted to use its marks.

### 77. States are placed in data-sovereignty groups by a published rule, with computed confidence
**Decision.** 2026-09-29. Each member state is placed in one of five ordered groups by the decision rule in
`model/sovereignty.py`: *Sovereign in law and in practice*, *Sovereign in practice, not secured in law*,
*Secured in law, not yet in practice*, *Not demonstrated*, *Dependent on non-EU providers*. The inputs are
seven sourced indicators (`model/indicators.csv`: jurisdiction requirement, classification in law, sovereign
cloud certification, state-controlled trust anchor and eID, government data centres, government cloud in
operation) plus two computed from the critical-holdings register (share of verified tier 0/1 holdings on
national or EU infrastructure; any sourced non-EU dependency). An input without a checked source is
*unknown* and counts as not demonstrated. Confidence is the width of the range of groups the state could
reach if every unknown resolved for or against it: one group High, two Medium, three or more Low. States
within a group are listed alphabetically. Amends #10 for this ranking only.

**Problem.** The author asked for a ranking of data sovereignty by country covering all 27 now, with the
confidence in each placement and the reason made clear. #10 forbids a composite score, and nearly every
input is still unresearched, so any ranking today mostly measures the research.

**Alternatives considered.**
- **Rule-based groups with a computed range (chosen).** Answers "where does each state stand" without a
  number to quote; the range makes unfinished research visible instead of hiding it in a score.
- **Weighted index (0-100).** *Why not:* the weights would be invented, the dimensions do not add (#10), and
  a precise-looking number is exactly what gets quoted without its caveats.
- **Per-dimension ranks only.** *Why not:* within #10, but it does not answer the question asked; a reader
  must build the ranking in their head, inconsistently.
- **Dominance layers (A above B only if at least as strong on every dimension).** *Why not:* weight-free and
  honest, but with this many unknowns most pairs are incomparable, and the layers are hard to read.
- **Rank only states above an evidence threshold.** *Why not:* the author asked for all 27; the range
  carries the same warning without hiding anyone.
- **Coverage percentage as the confidence.** *Why not:* an arbitrary threshold; the range says what the
  missing evidence could actually change.

**Closes off.** A single sovereignty score anywhere in the bundle or the outputs; an order within a group;
treating silence in the sources as evidence of national hosting.

**Verified:** 2026-09-29. `tests/test_sovereignty.py`: every rule branch, plus exhaustive checks that the
placement always lies inside its range and that resolving an unknown favourably never worsens a group;
`python3 -m unittest tests.test_sovereignty` → 14 tests OK. The indicator research has not run: all 27
states are currently *Not demonstrated*, Low confidence, full range.

*Would change if:* a dimension proves unmeasurable across most states (it is then dropped from the rule,
not guessed), or the groups start being quoted without their confidence, in which case the ranking is
withdrawn as #59 provides.

### 78. /ask answers questions from the sourced corpus only, through the Anthropic API, storing nothing
**Decision.** 2026-09-29. `/ask` lets anyone ask about data sovereignty in the EU. A Vercel Function
(`api/ask.ts`, logic in `api/_ask-core.ts`) sends the question to the Anthropic API with the model
`claude-opus-5`, adaptive thinking at effort `medium`, `max_tokens` 2000, server-side refusal fallbacks
(`fallbacks: "default"`), and one set of documents: `api/_corpus.json`, built by `model/ask_corpus.py`
from the content model, one block per sourced fact or explicit gap, with citations enabled. Every
citation maps back to claim ids, which the page resolves to quote, URL, hash and archived copy. The
system prompt and corpus are cached (1-hour TTL); the question comes last. Questions are single-turn,
at most 500 characters, and never logged or stored by this project. Spending is capped by a dedicated
Anthropic workspace with a monthly spend limit, plus a per-IP rate limit in the Vercel Firewall.

**Problem.** The author wants anyone to be able to ask about EU data sovereignty. A chatbot that answers
from general knowledge would say things this project cannot source, contradicting #75, and a public
endpoint that calls a paid API needs a hard cost ceiling. Visitors' questions are other people's data, so
the privacy policy (§2 of `ai-and-external-services.md`) requires a decision naming the processor and
what it receives.

**Alternatives considered.**
- **The whole corpus in context, with citations and caching (chosen).** About 80k tokens today, well
  inside the 1M context, so every answer can draw on everything and cite it; caching makes repeat
  questions cheap.
- **Retrieval with a vector database.** *Why not:* more parts, a new processor, and a retrieval step that
  can miss the relevant fact; no gain while the corpus fits in context.
- **Answer from general knowledge as well, labelled.** *Why not:* the author chose sourced-only; mixing
  checked and unchecked statements on one page is what #75 forbids.
- **A daily spend counter in a data store (e.g. Upstash).** *Why not:* a new store that would hold
  visitor identifiers; a provider-side workspace limit is a harder ceiling with no data kept by us.
- **Log questions to learn what people ask.** *Why not:* the author chose to store nothing; question
  text can contain personal data.
- **Claude Sonnet 5 or Opus 5.5.** *Why not:* the author chose Opus 5 for answer quality.

**Closes off.** Answers that go beyond the verified findings; conversation history (each question
stands alone); any server-side record of what was asked.

**Verified:** 2026-09-29. `web/src/__tests__/ask-core.test.ts` (7 tests: validation, request shape,
citation-to-claim mapping, error mapping, the question is never logged); `tests/test_ask_corpus.py`
(every corpus claim resolves to a supported citation; every fact the site shows is in the corpus);
Playwright `/ask` tests with a recorded stream, and axe on `/ask`. `vercel build` emits
`.vercel/output/functions/api/ask.func`; the built handler returns 400 for empty and over-long questions
and a readable error without a key. **Live answers: NOT YET** — waiting for the API key and the eval.

*Would change if:* the corpus outgrows the context window (then retrieval), costs exceed the workspace
limit in normal use (then a cheaper model, by the author's decision), or a legal or privacy review
requires a different processor.

### 79. A categorical judgement is admitted only after an independent review agrees with it
**Decision.** 2026-09-29. Any value that classifies evidence rather than quoting it (a holding's foreign
dependency, an indicator's yes/partial/no) enters the register only when a separate reviewer agent,
applying written definitions to the verified quotes, reaches the same value. Disagreement or no review
makes the value unknown, which under #77 never helps a state. Dependency reviews are staged in
`model/research/dependency_review/<ISO>.json` and read by `research.py admit`. Indicator reviews are
the second stage of research run 2.

**Problem.** Research run 1 classified each holding's dependency (national, EU provider, non-EU
provider, mixed) with no review. The quote check proves the words are in the document, not that the
category follows from them. A spot-check of the eight states the rule first placed "Dependent" found at
least three built on misclassified evidence: an EU company (Germany's Mühlbauer, Estonia's SK ID
Solutions) labelled "mixed", and Eurosystem infrastructure (TARGET) treated as non-EU. A High-confidence
"Dependent" placement is the most quotable claim this project makes; it cannot rest on an unchecked label.

**Alternatives considered.**
- **Independent review, agreement required (chosen).** Cheap (one agent per state), mechanical to
  enforce, and it fails safe: a disputed value becomes unknown rather than being corrected by a second
  unchecked judgement.
- **Accept the reviewer's value when it differs.** *Why not:* that swaps one unchecked judgement for
  another, and a reviewer "correcting" towards national would upgrade a state on no stronger evidence.
- **Keep the labels and fix only the spotted errors.** *Why not:* the spot-check sampled eight of 61;
  the error rate in the rest is unknown.
- **Drop categorical judgements entirely and show only quotes.** *Why not:* the ranking (#77) needs the
  categories; the review makes them defensible.
- **Human expert review of every label.** *Why not:* the right end state for the published launch
  (#67), but not available now; agreement between two independent passes is the interim standard,
  stated as such.

**Closes off.** Publishing a dependency category, and therefore any "Dependent" placement, that only one
agent asserted.

**Verified:** 2026-09-29. With no reviews staged, `research.py admit` admitted 0 dependency values
(previously 61). The review run then returned 93 verdicts: 77 agreed, 16 disputed (5 mixed → EU
provider, 3 mixed → unknown, 1 mixed → non-EU, 4 non-EU → unknown, 3 national → unknown). After
re-admission: 43 national, 4 EU provider, 2 non-EU provider. The eight High-confidence "Dependent"
placements fell to one, Ireland, whose two triggers were spot-checked by hand against their sources
(the electoral register's migration to a Microsoft Azure tenancy; Motorola Solutions' ownership of the
TETRA network operator).

*Would change if:* a human reviewer with subject expertise takes over admission, or the two-pass
agreement rate proves so high that sampling would do.

---

## Domain and continuous deployment

### 80. `eu27.cloud` is registered at iwantmyname and attached now, still `noindex`
**Decision.** 2026-09-30. `eu27.cloud` was registered at iwantmyname (whois registrar Key-Systems, created
2026-09-30T06:35Z). It stays there, and so does its DNS: an apex record and a `www` record at iwantmyname
point it at the Vercel project `sovereign-data-centers`, with the values `vercel domains add` prints.
`www.eu27.cloud` redirects to the apex. The domain is attached **now**, ahead of #50's stage-3 gate, and it
serves `noindex` twice over: through `robots.txt` and through an `X-Robots-Tag: noindex` header on every path
(`tests/test_vercel_config.py`). The site is not announced. The stage-2 indexing gate and the launch gate
(every published claim cites a source) are unchanged.

**Problem.** #70 planned the purchase through Vercel, and the docs said so. The name was bought elsewhere, so
`vercel domains ls` knew nothing about it. Holding a paid domain unattached also meant the push-to-deploy
pipeline (#81) had no stable address to smoke-test.

**Alternatives considered.**
- **Keep it at iwantmyname, point records at Vercel, attach now with `noindex` (chosen).** One DNS change,
  and no transfer. The registrar is independent of the host, which is closer to the separation
  `EU27-CLOUD-BRIEF.md` recommends than #70 was.
- **Transfer the domain to Vercel.** *Why not:* ICANN locks a new registration against transfer for 60
  days, and it would undo the separation above for no gain.
- **Delegate the nameservers to Vercel.** *Why not:* it moves all of the zone's DNS to the host. Two records
  at the registrar do the same job.
- **Hold it unattached until stage 3, as #50 and #70 said.** *Why not:* `noindex` plus not announcing
  already keeps unverified claims from reading as a register, which was #50's concern. The owner chose to
  attach now.

**Closes off.** The `*.vercel.app` address as the one the project names. It stays as a fallback. Removing
`noindex` now needs both the `robots.txt` lines and the header gone, and a test changed.

**Verified:** NOT YET. Registration, 2026-09-30: `whois eu27.cloud` shows `Registrar: Key-Systems, LLC` and
`Creation Date: 2026-09-30T06:35:17.873Z`. `vercel domains ls` shows 0 domains, as expected for an external
registration. Attachment is verified when `vercel domains inspect eu27.cloud` shows it configured, and when
`curl -sSI https://eu27.cloud/` returns 200 with `x-robots-tag: noindex`.

*Would change if:* the project starts to present itself as practising the sovereignty it describes. That is
#70's condition, and it would then favour an EU registrar with EU-hosted DNS and DNSSEC.

### 81. Production deploys from GitHub Actions on every push to `main`
**Decision.** 2026-09-30. `.github/workflows/deploy.yml` runs on every push to `main`, and on demand. The
**gate** job runs the full `./test.sh`, including Playwright, with Google Chrome from the runner image. The
**deploy** job needs the gate, runs in the GitHub environment `production`, and does three things:
- installs typst v0.15.1 from its release tarball, checked against a sha256 in the workflow;
- runs `vercel pull`, then `vercel build --prod`, with the CLI pinned to `vercel@61.1.0`;
- uploads with `vercel deploy --prebuilt --prod`, then smoke-tests `https://eu27.cloud`: `/`, `/country/DE`,
  `/eu27-report.pdf`, `robots.txt`, the `noindex` header, and the live `/data/eu27.json` hash against the
  committed one.

`VERCEL_TOKEN` is a secret. `VERCEL_ORG_ID` and `VERCEL_PROJECT_ID` are repository variables.
`ANTHROPIC_API_KEY` stays in Vercel only. Deploys never overlap (`concurrency: production`). Each run's summary
records the deployment, the commit and the bundle hash, and replaces the hand-written deploy log.
`./run.sh deploy` stays as the manual fallback.

**Problem.** A push shipped nothing. A stale site was the recorded failure mode: the 2026-09-11 deploy stayed
live for 16 days while it fell 12 commits behind (DEPLOYMENT.md). Deploys could run only from this Mac,
because the PDFs need typst (#71).

**Alternatives considered.**
- **GitHub Actions, prebuilt upload, pinned and checksummed typst (chosen).** It keeps #71's guarantee that a
  build without typst cannot ship. It runs on any push from any machine, and the full gate stands in front
  of every deploy.
- **A local `./run.sh ship` that pushes and then deploys.** *Why not:* it still works from one machine only,
  and a push from anywhere else ships nothing, so the site can go stale again.
- **The Vercel GitHub App (Git integration), with typst downloaded in `buildCommand`.** *Why not:* the
  install would have to run on every remote build inside Vercel's image, where the gate does not run. It
  would also turn on PR previews before preview protection has been thought through (DEPLOYMENT.md, Known gaps).

**Closes off.** A green push to `main` that stays unpublished: a merge now is a release. It also closes off
the deploy log as hand-written rows in DEPLOYMENT.md. A CI-built PDF sets code in DejaVu Sans Mono, not
Menlo, so it is not byte-identical to one built on this Mac.

**Verified:** NOT YET. `tests/test_workflows.py` passes. It checks that every action is pinned by SHA, the
Vercel CLI version is exact, the typst download is checksummed, the upload is prebuilt, the deploy needs the
gate, and only `main` deploys. The typst v0.15.1 tarball's sha256 matched GitHub's published digest when it
was downloaded on 2026-09-30. What verifies the decision is the first green `Deploy` run on `main`, with its
smoke test passing against `https://eu27.cloud`.

*Would change if:* the build starts needing secrets at build time, or Vercel's build image gains typst. In
the second case the Git integration would do the same job with less of our own CI.

---

## Evidence that holds up

### 82. A fact is printed only if its figures are in its quote; nothing is claimed as human-verified
**Decision.** 2026-09-30. Four rules, in `model/evidence.py`, `model/provenance.py` and `model/document.py`:
- **Recorded evidence.** `provenance.supported()` accepts a non-dataset citation only with a quote of 20
  or more characters and a passing quote check in `research/verification.csv` for the source URL, at the
  sha256 the registry records. A dataset citation still needs its value to reproduce the cell.
- **Value in quote.** `Sources.fact()` checks the printed text against each supporting citation. Every
  number and date must appear in the original-language quote, in any EU number format, or the value is
  a gap. A missing acronym is disclosed, not fatal. Categorical values (indicators, infrastructure
  dependency, "No central register") come from a closed vocabulary and are admitted by review (#79).
  `document.py --check` re-runs the rule on every fact span.
- **Disclosure.** Every output carries one disclaimer, in the same words: machine-checked, not
  human-verified; English wording is machine translation or summary.
- **Honest method text.** The list of checks is generated from `evidence.CHECKS`, and the ranking rule
  from `sovereignty.RULE`. `tests/test_evidence.py` fails on wording that claims a check that did not run.
- **An evidence grade, not a score.** `evidence.assess` lists the checks each citation passed, and a
  fixed rule (`evidence.GRADE_RULE`) turns them into Strong or Standard. Anything less is not printed.
  Each fact span carries its best grade (`g`). The report, web and briefs show the grade, the checklist,
  and the original quote before its machine translation.
- **Review agreement, enforced.** `research.admit_indicators` admits an indicator value only when the
  agent's value, the reviewer's value and the staged value are the same (#79). Any other value is
  withdrawn with its citations, and a source left uncited is marked `unused`. Dependencies were already
  enforced this way.

**Problem.** The gate proved that each quote is in its document. It never proved the report printed what the
quote says. A 2026-09-30 audit found 9 of 31 printed record counts carried numbers missing from their
quote. `record:BG:authentication_audit_log:count` printed a 10-year retention period as a record count.
`record:FR:police_records:count` added "48 million victim records" to a quote that says 17 million.
`supported()` returned `True` for any non-dataset citation, so 5 hand-migrated citations (#67) with no
recorded quote check were printed as facts. The report also said every fact was "fetched, hashed and
checked", which was false for the 5 migrated citations. (This entry first said it was also false for 136
Eurostat figures. That was wrong: their raw API responses are stored with a sha256 in
`fetch_manifest.csv`. The registry that footnotes cite simply did not show it. Corrected 2026-09-30.)

**Alternatives considered.**
- **Figures hard, summaries labelled (chosen).** Numbers and dates are where a misreading does harm and
  where a check is mechanical. The words of an English summary of a foreign quote cannot be checked
  mechanically, so they are labelled as a summary and shown beside the original.
- **Verbatim only.** *Why not:* only 15 of 676 record facts are verbatim extracts. About 580 would become
  gaps until every claim is re-researched, and the report would be empty for reasons of format, not
  evidence.
- **Hard on acronyms too.** *Why not:* 138 facts failed only on an acronym, mostly a correct
  transliteration of one in the quote (*MVR* for *МВР*). Treating a transliteration like an invented
  figure removes true facts, and disclosing it per fact loses nothing.
- **A numeric confidence score per fact.** *Why not:* nothing has calibrated one. Without a human audit,
  a number such as 0.87 claims a precision nobody measured (#10, #77).

**Closes off.** Printing a figure its quote does not contain, whatever the researcher meant by it. A
value that bundles a second figure or an article number with its finding is withheld until re-staged
with a clean value. That is why `record:FR:police_records:count` is a gap and not "17 million". It also
closes off describing the checks as a human review.

**Verified:** 2026-09-30. `python3 model/document.py --check`: 27 documents checked, 0 unsourced facts.
Printed facts fell from 997 to 922, with `tests/test_evidence.py` `FACT_FLOOR = 922`. The coverage floors
fell from param 138 to 136 and record 1017 to 1014 (`tests/test_provenance.py`, reason recorded).
`tests/test_evidence.py` asserts that BG `authentication_audit_log:count` and FR `police_records:count`
are not printed, and that a citation without a recorded quote check supports nothing. Enforcing review
agreement withdrew EE K2, LU C2, PL C1 and RO C1: indicator coverage fell from 134 to 130, and printed facts
to 918. No state changed group. Grades on 2026-09-30: 76 Strong and 842 Standard. `tests/test_evidence.py`
recomputes every bundle grade from its checks and asserts no Strong fact misses a required check. EE's and RO's ranges widened to reach "Sovereign in law and in practice".

*Would change if:* a human sampling audit measures the error rate of machine summaries. The words of a
summary could then be graded by that rate rather than only labelled. It would also change if a claim
kind gains a structured value (a number with a unit), which could be matched exactly instead of by
tokens.

### 83. "Top quality" is a source tier per host; facts are vetted against it, and contradictions are shown
**Decision.** 2026-09-30. Every cited host is classified once in `model/sources/authorities.csv`:
- **T1:** official law portal or gazette, statistics office, Eurostat;
- **T2:** competent public body or audit office;
- **T3:** other institution or company;
- **T4:** unofficial law mirror, press, encyclopedia.

`evidence.tier()` reads the table. An archived copy counts as the page it archived, and `ec.europa.eu` is
T1 only for a dataset. A fact is Strong only if its source is T1 or T2. A vetting run re-examines every
printed fact and then the gaps: it looks for a T1/T2 source (an upgrade or a corroboration), newer
information (supersedes), a contradiction, or a filled gap. Each finding goes through the existing
quote check, the value-in-quote rule (#82) and a blind review. A contradiction makes the fact
**disputed**, never silently replaced. A later statement by the same authority supersedes, and a higher
tier wins. Otherwise the fact stays disputed.

**Problem.** Each of the 918 printed facts rests on the one source a single agent found in one pass on
2026-09-29. Nothing recorded how good that source was beyond "official" or "secondary". With tiers
applied, 166 facts rest on a T4 source, 158 of them on an unofficial copy of a statute such as
`net.jogtar.hu` or `zakonyprolidi.cz`, where the official portal exists. 302 of 574 cited sources have no
publication date, and nothing re-checked a source after admission.

**Alternatives considered.**
- **A tier per host, in a table, with two rules in code (chosen).** It is complete, since a test fails on
  an unclassified host, and every judgement is one reviewable line.
- **A tier from the `doc_type` and `confidence` the research agent chose.** *Why not:* those are the
  agent's own labels. `confidence: official` sits on 158 citations of commercial statute mirrors.
- **"The operator's own domain is T1 for its register."** *Why not, for now:* `national_data.csv`'s
  `holder_url` is the URL the agent cited (`research.admit`), so the rule is true by construction. The
  first version of this change applied it and marked 531 facts T1. It needs operator domains recorded
  on their own evidence first.
- **Replace a contradicted fact with the newest top-tier source automatically.** *Why not:* a newer page
  can be wrong, or about a different register. Showing both sources costs one visible gap. Silently
  replacing risks printing the error with more confidence.

**Closes off.** A Strong grade on anything but a T1/T2 source. Treating an unofficial copy of a law as
the law. Resolving a contradiction by judgement rather than by the two published rules.

**Verified:** 2026-09-30, for the tiers: `tests/test_vetting.py` passes. Every cited host is classified,
mirrors are T4, and no fact below T2 is Strong. Best tier per printed fact is T1 343, T2 400, T3 9 and
T4 166 (`docs/evidence.md`), and Strong fell from 76 to 59.

The vetting run, verified 2026-09-30, run `wf_1c6b8bb6-450` (manifest in `model/research/vetting/runs/`):
- 27 staging files, each with the workflow's sha256 and the reviewer model;
- 1,017 findings, 862 of them with the reviewer's agreement;
- `vetting.py report`: 363 gaps filled, 244 corroborated, 26 superseded (23 higher tier, 3 later same
  authority), 12 disputed; rejected: 153 by review, 176 unverifiable, 38 unestablished holdings, 5 below
  T2; of the input items, 447 had no better source and 201 were not reached;
- best tier per printed fact afterwards: T1 635, T2 633, T3 9, T4 113, with 107 Strong of 1,390 facts.
- Corrected 2026-10-01: 8 "corroborations" and 2 "disputes" cited a document the fact already cited.
  A finding like that is now `same_source`, not a second source. The corrected counts are 238
  corroborated, 10 disputed and 106 Strong.

*Would change if:* a person reviews `authorities.csv` and reclassifies hosts, since the table is an
agent's work. It would also change if operator domains are recorded independently, which would allow
the operator-domain rule.

### 84. The project reproduces from scratch; the method is generated, not written
**Decision.** 2026-09-30. Four parts.
- **One command per step.** `./run.sh` gains `admit` (research, then vetting, always both), `recheck`,
  `retry`, `eurostat check|adopt`, `vet prepare|stage|hosts|verify|admit|report`, and `reproduce`. The
  agent step is the checked-in `/vet` skill (`.claude/skills/vet/SKILL.md`), which runs the checked-in
  `workflow.js` and records a manifest per run (`model/research/vetting/runs/`). The manifest holds the
  input, output and prompt hashes, the commit, the model, the tool versions and the outcome totals.
- **Proof, not assertion.**
  - `./run.sh admit --check` (a `./test.sh` stage) re-runs admission on the committed evidence and fails
    if any register would change. Admission reads no clock.
  - `./run.sh reproduce` clones HEAD into a temp directory, regenerates everything, requires `git status`
    to stay clean, re-runs the admission check, compiles all 28 PDFs, builds the web app and runs the
    tests.
  - `--evidence` also re-fetches every source.
  - Tool versions are pinned in `.tool-versions` and `.nvmrc`. `init.sh` warns on a mismatch, and
    `tests/test_workflows.py` holds CI to the pins.
- **Eurostat vintages as data.**
  - Pins live in `model/eurostat_pins.csv`, with the date and decision behind each.
  - Adopted today: population 2026, public-administration employment 2024, renewables 2025, land area
    2026, and Portugal's revised 2025 GDP (306.7 → 308.5).
  - The employment column had reproduced no Eurostat period (Sweden 420.4 against the official 245.0).
    It is now the official series and is printed on all 27 pages, where it was withheld.
- **A generated methodology appendix.**
  - `model/methodology.py` builds one content-model document. Every rule in it is the constant the code
    runs, and every number is counted from the build's files.
  - The EU-27 report and each country PDF carry it as an appendix, and the web `/methodology` page renders
    it. The PDFs stamp the commit and the bundle's sha256 when they are built.

**Problem.** The process was documented but not repeatable. A vetting run needed inline one-off code: to
split the input, extract the result, tier 171 hosts and apply Eurostat values. Nothing recorded a run's
inputs or tool versions. Nothing proved the registers follow from the evidence. Admission stamped the
date it ran on. CI ran Python 3.12 in one workflow and 3.14 in another, and this machine runs Node 26
where CI pins 24. The methodology page was hand-written, which is how "fetched, hashed and checked" came
to be printed over citations that were never checked (#82).

**Alternatives considered.**
- **Commands, a checked-in skill, a clean-room rebuild, and admission as a checked fixed point
  (chosen).** A stranger with a clone can run every mechanical step without Claude. The one agent step is
  written down, versioned and hashed.
- **A headless script (`claude -p`) for the agent step.** *Why not:* the owner chose a skill that keeps a
  person in the loop for the judgement calls, such as tiering new hosts.
- **Commit the fetched documents, so the evidence reproduces offline.** *Why not:* copyright, and 599 MB.
  Re-fetching (`reproduce --evidence`) plus archived copies is the reproducible path. Drift is reported
  as a finding, not hidden.
- **Keep the methodology hand-written, reviewed carefully.** *Why not:* that is exactly how the
  overstatement of #82 happened. Generated text cannot claim a rule the code does not run, and a test
  holds each rule to its constant.

**Closes off.** An edited register that admission would not produce. A pin changed without a recorded
decision. A methodology sentence that describes a rule other than the one that runs. A vetting run
whose prompts, input or model cannot be identified.

**Verified:** 2026-09-30, in part.
- `./run.sh eurostat check` reports 0 of 162 values differing, and writes nothing.
- `tests/test_fetch.py` holds every Eurostat column to its pinned source, with no column excused as a
  known defect.
- `tests/test_methodology.py` (7 tests) passes. The DE PDF's appendix and build stamp were checked in
  the compiled text.
- `tests/test_repeatability.py` passes.
- `./run.sh admit --check`: "6 of 6 registers reproduce from the committed evidence". Its first run found
  admission was not a fixed point (46 register rows moved on a second run). Admission now rebuilds from
  its base every time.
- A register cell edited by hand makes `admit --check` exit 1, naming the line ("5 of 6 registers
  reproduce").
- `./run.sh reproduce` on commit `f62eaac`: "reproduced from scratch" in 30 s. A fresh clone regenerated
  every output with `git status` clean, admission reproduced all 6 registers, all 28 PDFs compiled, the
  web app built, and the Python suite passed.
- `--evidence`, the full re-fetch in a clean room: NOT YET.

*Would change if:* the agent runs become deterministic (a pinned model snapshot with fixed sampling),
which would let a rerun reproduce the findings themselves. It would also change if fetched documents
could be archived with rights to redistribute, which would make the evidence reproducible offline.

---

## Bottom-up and human-verified

### 85. Citizens source and review facts; a person verifies a fact only under a two-person rule
**Decision.** 2026-10-01. Anyone may contribute through two public GitHub issue forms. Both are generated
from the model by `model/contrib.py forms`, so their choices cannot drift from it.
- **`submit-source`** is for a public document that establishes a fact.
- **`review-fact`** is for confirming or rejecting a printed fact, or a submission by its issue number.

`contrib.py ingest` reads them into `model/research/contrib/` (read-only `gh api`). A submission becomes a
staged finding and passes the same mechanical checks as agent research: fetch, hash, quote, value in
quote, tier. The automated model review is replaced by a person's.

**The two-person rule.** A review counts only if the reviewer:
- is on `model/contrib/reviewers.csv`, added by a pull request the maintainer reviews;
- did not submit the fact;
- declares that they read the source's language (from the source's language, or else the state's
  official languages);
- declares no conflict of interest.

Each reviewer counts once per fact. **Effects:**
- one eligible confirmation makes a fact **human-verified**: the new top grade, **Verified**, if it was
  already Strong;
- one eligible rejection makes it **disputed**, shown with the reason;
- two rejections withdraw it, unless two reviewers confirmed it.

**Disclosure.** Every output's disclaimer is computed (`evidence.disclaimer`). It reads exactly as
before until a person has verified a fact, and from then on states "N of M facts also verified by a
person".

**Links and audit.**
- Every fact has a prefilled **Check this fact** link, and every country page a **Submit a source**
  link.
- `contrib.py audit-sample` draws a seeded, stratified random sample of unreviewed facts. It is the human
  sampling audit #25 and #67 require.
- `docs/evidence.md` lists where help is needed, per state.

**Contributor terms.** Contributions are pseudonymous, licensed CC BY 4.0 under a DCO sign-off, with no
copyright assignment (`CONTRIBUTING.md`, `LICENSE-DATA`). The rules for publishing and correcting are in
`docs/editorial-policy.md`.

**Problem.** Agents found every source, and no person had verified any finding. The automated reviewer
was the same model as the researcher, the human sampling audit had no auditor, and there was no way for
a citizen to contribute except one English-only corrections form with no process behind it. The gaps
concentrate where machines fail: pages built with JavaScript or refusing automated requests, and states
whose languages the agents read least well. People who live there are best placed to fill them.

**Alternatives considered.**
- **GitHub issue forms, a vetted pseudonymous roster, and mechanical eligibility (chosen).** Every step
  is public and reproducible. No personal data beyond a public handle is held, and the evidence, not the
  contributor, earns the trust.
- **A web form on `eu27.cloud` from the start.** *Why not:* it needs a database, a privacy notice, a
  GDPR controller and anti-spam before launch, and a legal entity to be the controller (#86). It is
  phase 2.
- **Verified real names for reviewers.** *Why not:* a barrier to entry and a GDPR load, and a risk to
  contributors in states where reporting on government systems is sensitive. A maintained roster
  prevents one person posing as several without knowing who anyone is.
- **Majority voting by any GitHub user.** *Why not:* accounts cost nothing, so a vote can be bought or
  faked. Eligibility (roster, language, no conflict, not the submitter) is what makes one confirmation
  mean something.
- **Keep review automated only.** *Why not:* a model checking a model shares its blind spots (METHOD.md
  section 7). A person reading the source's language is the check the method lacked.

**Closes off.** Calling a fact human-verified without an eligible person's confirmation. Anyone, the
maintainer included, verifying their own submission. A rejection acted on silently, in either
direction.

**Verified:** 2026-10-01, in part.
- `tests/test_contrib.py` (15 tests) passes. It checks that:
  - the forms equal the model's vocabulary;
  - a submission parses into the right claim, and missing attestations are refused;
  - the submitter, an unlisted handle, a reviewer without the language and a declared conflict are
    each ignored;
  - one confirmation verifies, one rejection disputes, two withdraw, two confirmations outvote one
    rejection, and a reviewer counts once;
  - the disclaimer is unchanged at zero.
- `./run.sh admit --check`: 6 of 6.
- NOT YET: the first real submission and review, and the first audit sample with a measured error rate.
  The roster is empty until the maintainer approves the first reviewers.

*Would change if:* the project gains a legal entity and a privacy notice, which would allow the web form;
or abuse appears that the roster cannot stop, which would mean requiring two confirmations instead of
one.

### 86. The legal entity is deferred; everything is built so a Dutch stichting can take it over unchanged
**Decision.** 2026-10-01. The project stays, for now, with its owner in a personal capacity. The intended
home is a Dutch foundation (*stichting*), probably with ANBI status, not founded yet. Meanwhile nothing is
built that would block the move:
- contributions are licensed CC BY 4.0 with no copyright assignment, so only the owner's own rights need
  transferring;
- personal data is limited to public GitHub handles, so there is no controller obligation yet beyond
  GitHub's;
- `docs/editorial-policy.md` states the ownership and funding plainly, and the deferral.

**Problem.** Requirement 2 is that the project is housed in a European non-profit. Founding a stichting
takes:
- statutes, a notary, a board of at least one and preferably three, and registration with the KvK;
- for ANBI: a published policy plan, board, pay and annual accounts.

The owner chose to defer it. Building anything that assumes an entity, such as a web form that collects
personal data, would either need the entity first or need undoing later.

**Alternatives considered.**
- **Defer, and build entity-ready (chosen).** No rework at transfer.
- **Found the stichting now.** *Why not:* the owner's call, for later.
- **A vereniging (association) whose contributors are members.** *Why not, for now:* a membership drive
  by an interested party could capture it, a credibility risk for a project whose subject is
  independence from outside control. To revisit with the entity.

**Closes off.** Collecting personal data beyond public handles, which waits for the entity to be its
controller. Accepting money without first publishing the funder.

**Verified:** 2026-10-01. `LICENSE-DATA` carries the contributions clause, and `CONTRIBUTING.md` and
`docs/editorial-policy.md` exist. `tests/test_contrib.py` refuses a submission without the CC BY/DCO
attestation. The entity itself: NOT YET (deferred).

*Would change if:* the owner founds the stichting. Then the transfer of the owner's rights, the board and
the ANBI publication follow, and phase 2 (the web form) becomes possible.

### 87. Every printed fact is checked by the model that did not write it, before every production deploy
**Decision.** 2026-10-01. A production deploy now requires every printed fact to have a current verdict of
*supported* from a checker model that did not write it. The owner asked for this.
- **The rule.** Fable 5.1 checks what Opus 5.5 wrote, and Opus 5.5 checks what Fable 5.1 wrote. Fable 5.1
  checks anything whose author was never recorded, which today is every fact. Rule and process are in
  `model/factcheck.py`.
- **What a verdict covers.** It holds for the fact *exactly as printed*: a SHA-256 of the claim, the
  question it answers, the printed text and every citation (URL, fetched-document hash, locator, quote).
  If any of these changes, the verdict lapses, so a push re-checks only what changed.
- **Where it runs.** The check runs locally through the `/factcheck` skill and the checked-in workflow,
  which names each checker's model. `factcheck.py stage` refuses a batch whose checker reports a
  different model than the one asked for, or that wrote a fact in it.
- **What the gate requires.** `factcheck.py gate` runs in the deploy workflow's gate job and in
  `./run.sh deploy`. It also requires `docs/fact-check-audit.md`, the generated audit file, to be current.
- **On a disagreement.** It blocks the deploy, and nothing changes automatically. Every disagreement
  stays on the record in the audit file. *Superseded in part by #89: a disagreement now withholds the
  fact instead of blocking the deploy.*
- **The appendix.** Every asset carries a generated fact-check appendix (`model/factcheck_appendix.py`):
  the EU-27 report, each country PDF, each brief, the web pages `/fact-check` and `/fact-check/<ISO>`,
  and the `/ask` corpus. Each poster carries a one-line summary.
- **Authorship from now on.** The vetting workflow now names its models and records `researcher_model`,
  so authors are recorded going forward.

**Problem.** Each fact was found by one agent and reviewed blind by the same model (#83). The two readings
could share that model's blind spots, and `evidence.assess` says so: "blind, same model". Nothing recorded
which model wrote a fact, and nothing stopped a model from reviewing its own work. Nothing checked a fact
again before a deploy: a push to `main` shipped whatever the registers held.

**Alternatives considered.**
- **Check locally, enforce in CI (chosen).** The model is set by the orchestrator, not inherited, and
  checked against what the checker reports. No model key goes into GitHub, and CI stays a deterministic
  check over committed files.
- **Run the check inside the deploy workflow.** *Why not:* it puts an Anthropic key in GitHub. It
  re-fetches every source with model calls on every push. And the agent run is not reproducible, so the
  deploy itself would not be.
- **Re-check every fact on every push.** *Why not:* about 58 agents per push, for facts that did not
  change. The fact hash gives the same guarantee — every printed fact has a verdict on exactly what is
  printed — without that cost. `prepare --all` remains for a full re-check.
- **Turn a disagreement into a gap automatically.** *Why not:* that would let a single model's verdict
  silently withdraw a fact. The owner decides, and the audit file keeps the record.
- **Check facts with no recorded author with both models.** *Why not:* it doubles the first run. Every
  recorded review so far was Opus 5.5, so Fable 5.1 adds the second model. The owner chose Fable 5.1.
  This is a judgement, not a proof that Fable 5.1 wrote none of them; the appendix lists those authors
  as "unrecorded".
- **Gate every commit (in `test.sh`).** *Why not:* any data change on a branch would need a paid agent run
  before its tests passed. The deploy is what the rule protects.

**Closes off.**
- Deploying a printed fact that no second model has checked as printed.
- A checker model reviewing a fact it wrote.
- Hand-written fact-check claims. The audit file and every appendix are generated, and the gate fails
  when the audit file is stale.

**Verified:** 2026-10-01, the machinery only.
- `python3 -m unittest tests.test_factcheck` passes 27 tests. They cover the rule; the fact hash; stage
  refusing a model mismatch, an author-checker and a foreign claim; the gate failing on a missing,
  stale, disagreeing or ineligible verdict and on a stale audit file; and the appendix in the PDFs,
  briefs, web, posters and `/ask`.
- `python3 model/factcheck.py gate` on the current data prints `0 of 1390 printed facts checked,
  supported, checker ≠ author` and exits 1. So `main` cannot deploy until the first run is recorded.
- `factcheck.py prepare` plans 58 batches, all for claude-fable-5-1.
- The first run: 2026-10-02.
  - The pilot `wf_074137f6-b8e` covered 30 facts. The full run `wf_da123db1-a4e` covered the other
    1,360, in 57 batches; 16 of them were re-run after a session limit.
  - Every response in the agent transcripts is from `claude-fable-5-1`.
  - Result: 1,309 supported. 81 not confirmed (48 not supported, 33 unclear), which are withheld under
    #89.
  - `python3 model/factcheck.py gate` prints `1309 of 1309 printed facts checked, supported, checker ≠
    author` and exits 0.
  - Measured cost: about $250–370 from the transcripts' token usage, more than the $185–280 estimated
    from the pilot.
  - On 2026-10-02 the first automatic deploy (`Deploy` run 37072208296) passed the fact-check gate step in
    CI.

*Would change if:* authors are recorded for the earlier facts (re-research), or a third independent model
family is added, which could become the checker for unrecorded facts. Also if `evidence.assess` should
credit a cross-model check in the grades; that is a separate decision.

### 88. The methodology is in every asset, set apart in a method teal
**Decision.** 2026-10-01. The owner asked for both changes.
- **Everywhere.** The generated methodology (#84) and the fact-check appendix (#87) are now in every
  asset:
  - the EU-27 report and every country PDF;
  - every markdown brief, in full rather than as a pointer;
  - the web pages `/methodology` and `/fact-check`;
  - the `/ask` corpus, generated rather than only the hand-written summary;
  - every poster, as a footer line pointing to `/methodology` and `/fact-check/<ISO>`, since a poster
    cannot hold the text.
- **The methodology covers the fact check.** It gains a section on it, built from `factcheck.RULE`.
- **One colour for how-we-know material.** A new design token, `method` (teal), marks it everywhere:
  - light #0F6E6E on wash #E8F4F3; dark #5FC4BF on wash #10282E;
  - the PDF appendices open with a teal band, and the web pages use a teal `MethodFrame`;
  - method callouts and the poster's method line are teal;
  - every one of these sections carries the kicker "Method · how this was made". The briefs carry the
    kicker as text, since markdown has no colour.

**Problem.** The methodology was in the PDFs and on the web but not in the briefs. `/ask` answered from a
hand-written summary, which is the drift that #82 and #84 removed elsewhere. Nothing visually set method
apart from findings: method notes used the same EU blue as content.

**Alternatives considered.**
- **A teal method accent (chosen).** A hue used for nothing else, so it can't be confused with content
  (blue), gaps (gold) or the ranking colours. Every text pair passes WCAG AA (5.4:1 or better), and the
  generator checks this.
- **A deep-navy appendix band.** *Why not:* no new colour, but the blue is shared with content, so it
  marks method less distinctly.
- **A quiet grey back-matter style.** *Why not:* easy to skip, and the method is what a skeptical reader
  most needs to find.

**Closes off.** Using the method teal for anything but how-we-know material. A brief, PDF, page or poster
without the methodology or a pointer to it.

**Verified:** 2026-10-01.
- `python3 -m unittest tests.test_methodology` passes 14 tests. `Everywhere` checks the briefs in full,
  the `/ask` corpus, the poster line, both PDF appendices in `method-appendix`, the web `MethodFrame` and
  the token in both themes.
- `design/build_tokens.py` passes its contrast check.
- The DE PDF renders both appendices with the teal band.
- Playwright: 33 passed, including accessibility on `/methodology`, `/fact-check` and `/fact-check/DE`.
  Wide tables became keyboard-scrollable as part of this.

*Would change if:* the design system adopts a different semantic colour scheme, or print tests show the
teal does not hold up in black and white. The kicker carries the meaning without colour.

### 89. A fact the fact check does not confirm is withheld, not a reason to block the deploy
**Decision.** 2026-10-02. The owner chose this, to get the site online without lowering the standard for
what is printed.
- **What is withheld.** A fact with a *not supported* or *unclear* verdict, on the fact exactly as it
  would print, is no longer printed. The content model shows it as disputed instead, with the checker's
  model, the run and its reason. This is `document.Sources.withheld`, through the same
  `document.disputed()` that every renderer already shows.
- **How it is matched.** The verdict is matched on the fact's hash. `factcheck.fact_record` and
  `citation_record` are shared by the bundle and the content model, so both compute the same hash. If the
  fact or its source changes, the old verdict withholds nothing, and the fact is checked again before the
  next deploy.
- **The gate is unchanged.** Every *printed* fact needs a current supported verdict from an eligible
  checker. A withheld fact is not printed, so the gate no longer counts it.
- **Where withheld facts are listed.** The audit file has a section "Withheld after the fact check".
  Each country's fact-check appendix lists its own; the EU-27 appendix counts them per state.

**Problem.** Under #87, any disagreement blocked the deploy until the owner resolved it. The pilot
disagreed with 2 of 30 facts, which suggests about 90 across the report. Resolving each before the first
deploy would keep the site offline for days. Meanwhile the site stayed online at its fallback address,
with an older build that no second model had checked at all.

**Alternatives considered.**
- **Withhold on disagreement (chosen).** Nothing the check did not confirm is printed, the site can
  deploy the same day, and each disagreement stays visible and open on the record.
- **Block the deploy until every disagreement is resolved (#87 as first decided).** *Why not:* days
  offline, and in the meantime the fallback site served older, unchecked facts.
- **Deploy once without the gate.** *Why not:* it breaks the rule that every production deploy is fact
  checked.
- **Withhold only *not supported*, and print *unclear*.** *Why not:* "unclear" includes facts whose
  source the checker could not fetch. Printing those would print facts no second model has confirmed.

**Closes off.** Printing a fact that the check disagreed with, or could not check, as printed.
Resolving a disagreement by editing a verdict: only a changed fact, checked again, comes back.

**Verified:** 2026-10-02.
- `python3 -m unittest tests.test_factcheck` passes 34 tests. The withholding tests check that, for all
  1,390 facts, the content model and the bundle compute the same hash. A matching *not supported* or
  *unclear* verdict withholds the fact. A verdict on an older version withholds nothing. A supported
  verdict prints the fact. Every current disagreement is absent from the printed facts, and a withheld
  fact does not block the gate.
- After `./run.sh data`, both pilot disagreements on Germany are disputed in the bundle.
- The full run (`wf_da123db1-a4e`): 81 facts are withheld, all listed in `docs/fact-check-audit.md`. The
  gate exits 0 at 1,309 of 1,309. `FACT_FLOOR` went from 1390 to 1309, with the reason recorded beside it.

*Would change if:* withheld facts turn out to be mostly true facts that the checker could not fetch. Then
an *unclear* verdict could trigger a retry route instead of being withheld outright.

### 90. eu27.cloud uses Vercel's nameservers; DNS is not kept at the registrar
**Decision.** 2026-10-02. The owner chose this.
- At iwantmyname, the nameservers for `eu27.cloud` are set to `ns1.vercel-dns.com` and
  `ns2.vercel-dns.com`.
- Vercel serves the apex and `www`, and issues the TLS certificate.
- The domain stays registered at iwantmyname.

This supersedes #80's "DNS kept there".

**Problem.** #80 recorded that DNS was kept at iwantmyname with two records pointing at Vercel, and
`DEPLOYMENT.md` said so. On 2026-10-02 the registry listed the domain as *inactive*, with no nameservers at
all. `vercel domains inspect` showed it expected `ns1/ns2.vercel-dns.com` and saw none, and `eu27.cloud`
resolved nowhere. The site was reachable only at its `vercel.app` fallback, and every `Deploy` run's smoke
test would fail.

**Alternatives considered.**
- **Vercel's nameservers (chosen).** One change at the registrar. Vercel then creates the records and the
  certificate. The fewest steps, and the fewest ways for the records and the project to drift apart.
- **iwantmyname's nameservers, plus records there, as #80 intended.** *Why not:* two steps and two
  records, which is the setup that was never completed. It also gives no benefit while the only thing
  on the domain is this site.

**Closes off.** Keeping DNS records at iwantmyname. A future mail or verification record would be added
in Vercel's DNS, not at the registrar.

**Verified:** 2026-10-02.
- The registry lists `ns1.vercel-dns.com` and `ns2.vercel-dns.com`.
- Google and Cloudflare DNS-over-HTTPS resolve `eu27.cloud` to Vercel's addresses.
- `vercel domains verify eu27.cloud` reports `configured_correctly`.
- `https://eu27.cloud/` returns 200 with `x-robots-tag: noindex`, and `www` redirects (308) to the apex.
- The first automatic deploy, `Deploy` run 37072208296, passed the smoke test on re-run, serving bundle
  `71ad7382…`.

*Would change if:* the domain needs services Vercel's DNS cannot host, or the project moves off Vercel.

### 91. The site takes the report's look: EU-blue bands, gold kickers and the print serif
**Decision.** 2026-10-02, at the owner's request.
- **Page headers.** Every page opens with a band like the PDF report's cover and chapter bands: EU blue
  (#003399), a gold (#FFCC00) letter-spaced kicker, the title in Libertinus Serif, and a gold rule. The
  method pages, `/methodology` and `/fact-check`, use a teal band (`method_deep` #0F6E6E) with a pale-teal
  kicker. `web/src/components/PageBand.tsx`.
- **The serif** is also used for section headings, the site name and the headline figures. Body text, tables
  and navigation stay in Inter. The active navigation link takes a gold underline.
- **The font** is self-hosted from `@fontsource/libertinus-serif` (5.3.0, exact pin, OFL), regular weight,
  Latin and Latin Extended. The CSS name comes from the design tokens' `print_family`, so the web and the
  PDF name the same face.
- **The front page** shows four pages of the EU-27 report: the cover, the ranking, Germany and the
  methodology. They are rendered from the PDF at build time by `book/report.py` (`PREVIEWS`), using typst
  alone, and never committed.

**Problem.** The site and the PDF looked like two different publications: a sans-serif web app beside a
serif, EU-blue report. The owner asked for the front page, then the whole site, to follow the report's
cover.

**Alternatives considered.**
- **The report's look across the site, serif for display only (chosen).** One identity across the PDF, the
  web and the posters. Inter keeps long tables and body text legible on screen.
- **Serif everywhere, body text included.** *Why not:* Libertinus at small sizes in dense tables reads worse
  on screen than Inter.
- **Google Fonts.** *Why not:* the CSP allows fonts from this origin only (`default-src 'self'`), and loading
  from Google would send each visitor's address to a third party.
- **Gold kicker on the teal band.** *Why not:* 4.0:1 contrast, under the 4.5:1 that text needs. The pale
  teal wash gives 5.4:1.
- **Committed screenshots of the PDF.** *Why not:* they would go stale with every data change, and no media
  goes in git. Rendering at build time keeps them the deployed PDF's own pages.

**Closes off.** A page title outside `PageBand`. Fonts loaded from a third party. Committed images of the
report.

**Verified:** 2026-10-02.
- The type-check and lint are clean.
- Playwright and axe pass on every route.
- Contrast: white on EU blue 10.9:1, gold on EU blue 7.2:1, white on deep teal 6.0:1, pale teal on deep
  teal 5.4:1.
- Screenshots of `/`, `/country/DE` and `/methodology`, in light and dark mode, were checked by eye.
- `book/report.py -o` renders the four previews: the cover, the ranking, Germany's chapter and the
  methodology opener.

*Would change if:* print or accessibility testing shows the serif hurting readability, or the project
adopts an institutional identity, for example on transfer to the foundation (#86).

### 92. Every pull request runs the full gate; the live site is smoke-tested after each deploy and weekly
**Decision.** 2026-10-02, from the testing plan the owner approved.
- **Pull requests (`ci.yml`).** `./test.sh --no-pdf` runs on every pull request, with the same pinned setup as
  the deploy gate, plus `npm audit --audit-level=high` for the root and `web/`. The deploy gate also runs
  the audit, and installs poppler so the compiled PDFs are inspected.
- **The live site (`model/smoke.py`).** One stdlib-only smoke test runs after every deploy and every Monday
  (`monitor.yml`, read-only, opens nothing). It checks:
  - every route, the 28 PDFs and the 4 previews;
  - every security header `vercel.json` sets, and noindex;
  - the `www` redirect, and a TLS certificate valid for at least 14 more days;
  - that the served bundle is the committed one.
- **New checks in the gate.**
  - `book/check_pdfs.py`: disclaimer, both appendices, country named, fonts embedded and a size budget, for
    each compiled PDF.
  - A gzipped size budget: data 900 KB, JavaScript 400 KB.
  - Seeded generated-input tests for the evidence rules (`tests/test_properties.py`).
  - Fetch-layer tests against a local HTTP server (`tests/test_fetch_network.py`).
  - Component tests (Vitest).
  - Browser tests: accessibility in dark mode, every route at 375 px, and print.
- **The clean room** (`./run.sh reproduce`) now runs `./test.sh --no-e2e` in the fresh clone.
- **`docs/testing.md`** lists every suite and where it runs. A test fails if a test file or workflow is
  missing from it.

**Problem.** A pull request got only the Python tests. Vitest, Playwright, type-check, lint, the build and
the PDFs first ran on push to `main`, which is the production deploy. Nothing checked the live site's
headers, routes or certificate after a deploy or between deploys. The evidence rules were tested on
hand-picked examples only. The fetch layer had no network-level test. Of the PDFs, only the page count and
the disclaimer were checked.

**Alternatives considered.**
- **The full gate on pull requests, smoke checks after deploy and weekly (chosen).** Every check runs before
  a change can reach `main`, and the site is watched without a commit.
- **Keep the deploy as the first full test.** *Why not:* a failing browser test is found only by a production
  deploy that then does not happen. That is safe, but late.
- **`hypothesis` for the generated inputs.** *Why not, for now:* it adds a dependency to a stdlib-only model.
  Seeded `random` gives reproducible cases with no dependency; `hypothesis` stays open, with the owner's OK.
- **Have the weekly monitor open GitHub issues.** *Why not:* that is outward-facing and needs the owner's OK.
  A failed run with its summary is visible enough for now.

**Closes off.** Merging a pull request that has not passed `./test.sh`. A deploy that does not check the live
headers and certificate. A test file or workflow missing from `docs/testing.md`.

**Verified:** 2026-10-02.
- `model/smoke.py` on eu27.cloud: 54 of 54 checks passed. `tests/test_smoke.py` shows it fails against a
  local server serving the wrong things.
- `book/check_pdfs.py` finds 0 problems in 28 PDFs and 4 previews, and reports a removed `DE.pdf`.
- Each generated-input property failed against a deliberately broken rule (an always-true value check,
  English-only number reading, an always-Opus checker, and a hash that ignored the printed text), then
  passed against the real one.
- Playwright: 56 passed. Vitest: 49 passed. `npm audit --audit-level=high`: 0 vulnerabilities, root and
  `web/`, after `undici` 8.11.2 and `brace-expansion` 5.0.12.
- `./run.sh reproduce`: "reproduced from scratch".
- The pull-request job runs on GitHub only on the next pull request: NOT YET.

*Would change if:* the gate grows too slow for pull requests (then split the browser tests into their own
job), or the owner approves the items that wait for an OK, listed in `docs/testing.md`.

### 93. A withheld fact can be corrected by a later round, through every check again
**Decision.** 2026-10-02, after the owner approved re-researching the withheld facts.
- **What the round is.** A *correction round* re-researches only the facts the cross-model check withheld
  (#89). Its input is each fact, how it printed, its source and the checker's reason
  (`vetting.py prepare --withheld`).
- **The `corrects` relation.** In the vetting workflow, a finding with relation `corrects` is a T1/T2 quote
  that supports a correct statement answering the same question.
- **Where it is staged.** `vetting.py stage --round` writes `model/research/vetting/rounds/<run>/<ISO>.json`,
  never over the first run. Every finding carries its researcher and reviewer models.
- **What admission lets it do.** A `corrects` finding may replace the printed value only for a claim the fact
  check ever withheld. That is read from the staged verdicts, which never change, so admission still
  reproduces. The finding must also pass every check the first run's did: a T1/T2 source, the quote found in
  the fetched page, and blind-review agreement. The old citations are marked superseded.
- **The new value is checked again.** It is a changed fact, so `/factcheck` checks it with the model that did
  not write it before it can ship.
- **Categorical values.** In a round, these are reduced to their vocabulary term, so "Yes: the agency runs …"
  becomes "yes". The wording as written is kept beside it. A value that does not start with a vocabulary
  term is left as it was and fails the reviewer's agreement.

**Problem.** The first run's resolution rules (#83) replace a printed value only with a higher-tier source,
or a later statement of the same authority; anything else is "disputed". A fact the fact check withheld
because its *wording* went beyond its quote could therefore never be corrected from a source of the same
tier. It would stay withheld for good, however clear the better quote.

**Alternatives considered.**
- **A separate round, with a narrow `corrects` rule for withheld claims (chosen).** It only touches values
  that already failed a check, it runs every check again, and the first run stays reproducible.
- **Edit the withheld values by hand.** *Why not:* never: admission decides, and a hand edit is unauditable.
- **Re-run the whole vetting workflow.** *Why not:* it would overwrite the first run's staging files, and
  cost several times as much for 69 facts.
- **Let any later same-tier source replace a printed value.** *Why not:* that reopens every confirmed fact to
  whichever source an agent finds last. The rule stays limited to values that already failed.

**Closes off.** Correcting a withheld fact any way other than a verified, blindly agreed T1/T2 finding,
followed by a second-model check. Overwriting the first vetting run's staging files.

**Verified:** 2026-10-02/03, round `wf_ee4d0054-063`.
- 69 withheld facts went in, 6 research and 6 review agents ran, and 57 findings came back for 55 claims.
- 39 were fetched and checked: 30 exact matches, 7 fetch failures, 2 quotes not found.
- Admitted: 6 corrected, 22 corroborated, and 1 superseded by a higher-tier source. Not admitted: 20 where
  the reviewer disagreed, 9 not verified, and 1 below T2.
- `admit --check`: 6 of 6 registers reproduce.
- `tests/test_vetting.py` `CorrectionRound` passes.
- The fact check of the changed facts (`wf_72f99a66-4e9`, claude-fable-5-1, authors recorded as
  claude-opus-5-5): 25 of 31 supported, 6 not supported and withheld again.
- Result: 1,346 printed facts pass the gate, and 46 are withheld, down from 69.

*Would change if:* rounds start replacing many confirmed facts, which would mean the narrow rule is being
stretched, or a person's review (#85) becomes the way to settle a withheld fact.

### 94. A second checker's disagreement withholds a confirmed fact too
**Decision.** 2026-10-03; the owner agreed, after a second sample.
- **What withholds a fact.** A fact that one checker confirmed, but the other checker model did not confirm
  in a stability sample, is withheld as disputed. The check is on the same fact hash.
- **The reason shown** says it was confirmed once and that a second checker did not confirm it, and gives
  that checker's reason.
- **Where it comes from.** `factcheck.second_opinions()` reads the staged samples, which never change, and
  `document.Sources.withheld` applies it.
- **The ledger is untouched.** Replay still reproduces it. A changed fact is checked again, as with any
  withheld fact.
- **Samples are independent.** A later sample draws only facts no earlier sample checked.

**Problem.** Two stability samples, each of 50 facts Fable 5.1 had confirmed, were put to Opus 5.5. It did
not confirm 5 of the first 50 and 1 of the second 50: 6 of 100 in all. The rejections are specific, for
example a name not in the quote, a parenthetical the source does not state, or a quote that is only menu
text. Leaving them printed would print facts a model has rejected for a stated reason.

**Alternatives considered.**
- **Withhold on a second checker's disagreement (chosen).** The same standard as a first-checker
  disagreement: nothing a checker rejected is printed.
- **Leave samples as measurement only.** *Why not:* it would knowingly print six facts with a recorded
  objection.
- **Re-check everything with both models.** *Why not:* it doubles the cost for a measured 6% gain. Sampling
  finds the rate and withholds what it finds; more samples, or a full second pass, stay possible.

**Closes off.** Printing a fact that either checker model rejected on its current form.

**Verified:** 2026-10-03.
- Samples `wf_8232a23d-013` (45 of 50 agreed) and `wf_90fb82e7-35e` (49 of 50).
- After `./run.sh data`: 1,340 printed facts pass, and 52 are withheld, 6 of them on a second opinion.
- `python3 model/factcheck.py gate` prints `1340 of 1340`.
- `tests/test_factcheck.py` shows a second opinion withholds on the same hash and not on a stale one.

*Would change if:* further samples show a disagreement rate that justifies checking every fact with both
models; or a person's review (#85) becomes the arbiter between the two checkers.

### 95. Hosting is printed per holding; an EU-27 overview reuses the country facts
**Decision.** 2026-10-05; the owner asked how to document each state's key digital infrastructure and chose
a generated overview, with structured operators to follow (#96).
- **Hosting is printed.** Each country's holdings table gains a "Hosting (as sourced)" column from the
  admitted `hosting` field, claim `record:<ISO>:<class>:hosting`. The same rules as every fact apply:
  value in quote (#82), fact check (#87), withheld when not confirmed (#89).
- **The overview is generated, not written.** `document.infrastructure()` lists every holding whose hosting
  is printed or withheld, by state, and counts per state what the printed facts say. Each cell is a copy
  of the span the country document prints, with the same text, claim and kind, so it carries the same
  source and the same fact-check verdict.
- **Where it appears.** The bundle (`infrastructure`), the EU-27 report after the ranking,
  `countries/EU-INFRASTRUCTURE.md`, the web page `/infrastructure`, and `/ask`.
- **It stays outside `documents`**, so it adds no fact to check and no fact to count twice.
- **Its counts are of printed facts only.** "What is known, per state" counts a dependency only where the
  report prints it as a fact, never a withheld or unprinted label.
- **Layout: one table by state, not one per class.** `/holdings/<class>` already compares one class
  across the 27, and the `/holdings/<class>` pages now take their column names from the document.

**Problem.** `national_data.csv` held 71 cited hosting values, and none was printed anywhere. The question
the project exists to answer, where a state's critical registers run and who runs them, had admitted
evidence that no reader could see. A hand-written summary would answer it but would bypass sourcing,
fact check and withholding, and drift from the registers.

**Alternatives considered.**
- **Print hosting, and generate the overview from the country spans (chosen).** It adds no new kind of
  fact and no new renderer rules.
- **A hand-written overview.** *Why not:* renderers add no content (#74), and every fact must carry its
  source as printed (#82).
- **Build the overview from the registers.** *Why not:* it could print a value the country report
  withholds, or word it differently, which changes the fact-check hash.
- **One table per tier 0/1 class.** *Why not:* that is 34 tables of mostly gaps, and `/holdings/<class>`
  already compares one class across the 27.

**Closes off.** Describing where a state's data is hosted in any output other than through a printed,
fact-checked hosting span.

**Verified:** 2026-10-05, partly.
- `python3 model/document.py --check`: 27 documents and the overview, 0 unsourced facts.
- 1,400 printed facts (1,340 + 60 hosting). 11 hosting values print as gaps, because their quote lacks a
  year or number they state.
- `tests/test_evidence.py`: every overview fact is a printed country span, and every printed hosting is in
  the overview.
- **NOT YET:** the cross-model fact check of the 60 new facts. `./run.sh factcheck status` lists them as
  never checked, and the deploy gate blocks a push to `main` until `/factcheck` runs.
- **Found while verifying, not yet fixed.** In 7 states (AT, CY, EL, FR, HU, IE, SE), the country report's
  "Foreign-dependency exposure" section counts admitted dependency labels that the same report withholds.
  AT, for example, shows "National: 2" while both labels print as disputed. The ranking reads the same raw
  labels (`sovereignty.py:129`). IE stays "Dependent on non-EU providers" on a printed fact (emergency
  radio), but its electoral-register label (Azure) is withheld. The overview counts printed facts only, so
  it disagrees with those sections until they are fixed (TODO.md).

*Would change if:* hosting becomes structured (#96), at which point the overview's tables are computed
from operators rather than copied free text; or a reader needs the overview per class rather than per state.

### 96. Hosting becomes structured: operators as entities with sourced ownership links
**Decision.** 2026-10-05; the owner chose it over printing hosting as free text alone. Planned, not built.
The full design is [`docs/hosting-operators.md`](docs/hosting-operators.md).
- **Organisations are entities.** `model/organisations.csv` holds each organisation's seat and sector. A
  holding links to the organisations that operate, process, host or provide cloud for it, in
  `model/hosting.csv`, with the delivery model and location.
- **Ownership is a sourced link.** `model/org_links.csv` says who owns or controls whom, and each link has
  its own quote and source.
- **Every categorical value is reviewed** by an independent model before admission (#79), like the
  dependency labels.
- **Dependency can be derived, but is never overwritten.** A dependency derived from the links is
  reconciled against the reviewed label. Agreement corroborates the label, a gap may be filled through the
  fact check, and a disagreement goes to review. No printed fact changes silently.
- **Placements are diffed.** Any placement change that follows needs the owner's OK.

**Problem.** Hosting is free text. Cross-country questions, such as which private or non-EU firms run
state registers, cannot be computed, and the dependency label is a judgement that review overturned in
seven of eight unreviewed "Dependent" cases (#79). The idea is borrowed from Palantir's Ontology: objects,
properties and links that every view reads.

**Alternatives considered.**
- **Separate entity and link tables, reviewed per value (chosen).** One organisation is shared across
  states and holdings, and every value is cited.
- **Keep hosting as free text.** *Why not:* nothing about operators can be computed, and dependency stays
  a judgement only.
- **New columns on `national_data.csv`.** *Why not:* a holding can have several organisations,
  organisations repeat across states, and the register's header is fixed.
- **A graph database or an ontology platform.** *Why not:* the project is stdlib-only, and three CSV files
  are enough at this scale and auditable in a diff.

**Closes off.** Recording who runs a holding only in prose, and a dependency label that cannot be traced
to a sourced organisation.

**Verified:** NOT YET. Nothing is built. The plan is checked against the code that it would extend:
`provenance.RECORD_KINDS` and `NAMESPACES`, `national_data.read_rows`, `research.dependency_verdict`,
`reproduce.REGISTERS` and `factcheck.facts()`.

*Would change if:* the backfill finds too few sourced ownership links to derive anything; or one
organisation per holding proves enough, making a column simpler than a table.

### 97. The gate runs as parallel jobs, and the deploy ships the build the gate tested
**Decision.** 2026-10-06, on the owner's go-ahead for optimisations 1–3 of `docs/process.md`.
- **Parallel jobs.** `.github/workflows/gate.yml` runs `./test.sh --only model`, `--only web`, `--only pdf` and
  `--only e2e --project <name>` (one job per Playwright project) at the same time. `ci.yml` (pull requests,
  without PDFs) and `deploy.yml` (with PDFs and the fact-check gate) both call it.
- **One build.** The deploy downloads the `web-dist` and `pdfs` artifacts, packages them with
  `PREBUILT_SITE=1 vercel build` (`./run.sh site`), and fails unless the tree sha256 of
  `.vercel/output/static` equals the gate's files.
- **Caches** are keyed only by a pin or a checksum: lockfiles, `requirements-dev.txt`, `TYPST_SHA256` and the
  Playwright version.

**Problem.** A deploy took about 11.5 minutes (run 37383861627): 414 s of `./test.sh` in one job, then a
second, untested build of the web app and all 28 PDFs (152 s) in the deploy job. The deploy shipped a build
the browser tests had never seen. Today's advisory fix (GHSA-68fv-2mgg-jv7q) waited behind the whole sequence.

**Alternatives considered.**
- **Parallel jobs in a reusable workflow, shipping the gate's artifacts (chosen).** One definition for pull
  requests and deploys, and what ships is what was tested.
- **Keep one sequential job and add only caches.** *Why not:* it saves about a minute, and leaves the second,
  untested build.
- **Move the Vercel build into the gate job.** *Why not:* the gate would need `VERCEL_TOKEN`, which only the
  `production` environment may read, and every test would run with a production credential in reach.
- **Let Vercel build remotely.** *Why not:* its image has no typst, so it cannot build the PDFs (#71).
- **Skip the gate on a push whose tree passed a pull request's gate (optimisation 4).** *Why not now:* it needs
  this split first. It stays proposed in `docs/process.md`.

**Closes off.** A stage of `./test.sh` that sits outside every `--only` group, which `tests/test_workflows.py`
now fails. It also closes off a deploy that builds anything itself: the deploy job installs no typst, and
`./run.sh site` refuses `PREBUILT_SITE=1` without `index.html` and 28 PDFs.

**Verified:** in part, locally on 2026-10-06:
- `./test.sh --only web`, `--only pdf` (28 PDFs) and `--only e2e --project firefox` each exit 0;
- `PREBUILT_SITE=1 npx vercel@61.1.0 build` on a prebuilt `web/dist` gives a tree sha256 equal to
  `web/dist`'s (`ba417761…`), with `functions/api/ask.func` emitted;
- `python3 -m unittest tests.test_workflows` passes 17 tests;
- `actionlint` reports nothing on the new workflow.

**In CI**, on the first run (`d8bd0d1`, 2026-10-06, every cache cold): every job passed. The deploy took
5 min 08 s from push to live, against about 11.5 min before. The tree-hash check passed, and so did 55 of 55
smoke checks. The PDF job (3:59) is now the critical path.

*Would change if:* the parallel jobs' setup time outweighs the saving (each job installs its own
dependencies); or GitHub artifacts prove unreliable enough that a deploy fails for want of one.

### 98. CI checks once, reports the fact check on pull requests, and rechecks every cited source weekly
**Decision.** 2026-10-07, on the owner's go-ahead after a review of the CI/CD checks.
- **`ci.yml` runs on pull requests only**, and only the gate (`gate.yml`, without PDFs). Its `model` job and its
  `gitleaks` job are removed. A push to `main` runs the full gate in `deploy.yml`; secrets are scanned on every
  push and pull request by `security.yml` (`security-reusable.yml`: gitleaks over the full history, then the
  security gate).
- **The fact check is reported on pull requests.** When `gate.yml` runs without `factcheck`, its model job runs
  `factcheck.py gate`, writes the result to the run summary and raises a `::warning` if it would fail. The step
  does not fail the job. The deploy still enforces the gate (#87).
- **A weekly source recheck.** `monitor.yml`'s new `sources` job runs `research.py recheck --check` on Mondays.
  It re-fetches every source behind a printed fact (#83) and fails if a source is newly `gone` or
  `quote_vanished` against the committed `recheck.csv`. A refusal (`unreachable`) never fails it. It commits
  nothing, and it keeps the run's `recheck.csv` and fetch manifest as an artifact for 90 days.

**Problem.** Four gaps found on 2026-10-07:
- On a push to `main`, `ci.yml`'s `model` job re-ran the Python tests next to the deploy's gate. Its staleness
  check ran 2 of the 5 generators and failed on any diff in the tree, so it was a weaker copy of a check that
  already ran.
- A pull request with an unchecked printed fact went green. It failed only when pushed to `main`, which is the
  production deploy.
- Nothing re-fetched cited sources unless the owner ran `./run.sh recheck`. The last committed recheck was
  2026-09-30, and it covered 691 of today's 1,257 sources.
- gitleaks ran twice per push, once through `gitleaks-reusable.yml`, which the dotfiles policy (§9) calls
  superseded.

**Alternatives considered.**
- **One gate per event, a reported fact check, and a read-only weekly recheck (chosen).**
- **Keep `ci.yml`'s `model` job and make its staleness check match `test.sh`.** *Why not:* on a push to `main` it
  would duplicate the deploy's gate job for job, and two copies of one check drift apart, as this one already had.
- **Enforce the fact check on pull requests.** *Why not:* a branch must stay unblocked while facts are being
  researched (#87). A pull request is where unchecked facts are expected; only shipping them is not.
- **Let the weekly job commit the recheck result.** *Why not:* `recheck.csv` decides which facts are shown as
  disputed. A CI job writing evidence to `main` with no one reviewing it would be a deploy nobody approved. It would
  also give the job `contents: write`, which no workflow here has.
- **Fail the weekly job on `unreachable` too.** *Why not:* GitHub's runner addresses are refused more often than
  a laptop's, and #83 already rules that a refusal is not evidence of change. It would fail every week.

**Closes off.** A second copy of the model checks in `ci.yml`, a second gitleaks run, and a scheduled job that
writes to the repository. `tests/test_workflows.py` fails on any of them, and on a monitor without the recheck.

**Verified:** in part, locally on 2026-10-07:
- `python3 -m unittest tests.test_workflows tests.test_research` passes 40 tests. Run against the previous
  `ci.yml`, `gate.yml`, `monitor.yml` and `research.py`, the 8 new tests fail (2 failures, 6 errors).
- `actionlint .github/workflows/*.yml` reports nothing.
- `research.py recheck --check --source interoperable-europe-ec-europa-eu:92a5c57c6a` (404, committed as `gone`)
  exits 0. With its committed row changed to `unchanged`, the same command exits 1 and prints it in the table.
  Both runs' file changes were reverted.
- `factcheck.py gate` today: 1490 of 1490 printed facts pass, so the pull-request step would print no warning.

NOT YET in CI: the first pull request showing the fact-check step, and the first `sources` run (by
`workflow_dispatch` or on a Monday), its duration and its artifact.

*Would change if:* the weekly recheck regularly exceeds its 120-minute timeout (1,257 sources at 1.5 s apart);
or GitHub runners are refused by so many hosts that the recheck covers too few sources to mean anything. Then it
would run from a machine the owner controls.

### 99. The web app takes the EU27.CLOUD brand: badge, wordmark, map bands and a night-navy palette
**Decision.** 2026-10-08, at the request of Marco Buhlmann (repository admin), who chose to ship the design as is
and record it here rather than drop its official-looking parts. The web app (`web/`) now shows:
- **Brand marks.** The EU27.CLOUD badge (a "27" inside a ring of stars) and wordmark in the header, the full lockup
  with "EUROPEAN UNION DATA SOVEREIGNTY INITIATIVE" in the footer, and a favicon built from the 27 national flags
  arranged as "27". Files: `web/public/brand/`, `web/public/favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`.
- **Page bands.** `PageBand` draws the EU silhouette artwork (`web/public/brand/hero-bg.webp`) on night navy
  `#0A0F1D` instead of flat EU blue. Method pages tint it method teal, so #88 still sets them apart.
- **Tokens** (`design/tokens.json`, generated by `design/build_tokens.py`): brand `night`; dark theme rebased on the
  artwork's navy (`bg_page #0A0F1D`, `bg_card #111A2E`), dark `accent_text` gold `#FFCC00`; light `fg_primary`
  `#00205B`; a display family (Montserrat, self-hosted via `@fontsource/montserrat` 5.3.0) for headings, page-band
  titles and stats; `shape.radius_px` 10 for every `rounded` surface. EU blue `#003399` and gold `#FFCC00` stay the
  highlight and accent.
- **Header controls.** A sun/moon icon toggle replaces the "Light mode"/"Dark mode" text button.
- **Front-page subtitle**, on the web and the report cover (`book/report.py`, #91): "A research-backed framework for
  every EU member state: which critical government data should remain within national borders—and which sovereign
  data centres should host it."

- **Page layouts** follow the mockup, rendered from the bundle as before: a tile map of the 27 beside the front
  page's title (`web/src/charts/TileMap.tsx`), progress meters, entry cards and a question box that hands its text
  to `/ask` as router state; Countries as cards with bars and tier 0 dots; Critical holdings by tier with domain
  filters; the ranking's groups as a ladder and its findings as pills; Hosting as cards grouped by state with a
  dependency filter (`HostingCards`, the table's own spans through `DocumentView`'s new `tables` hook); Sources
  with tier and grade distributions and filters that hide entries without renumbering them; Ask beside its
  examples; method pages with a contents list. No page states a fact the bundle does not.

The design was reviewed as a static mockup first (`mockups/eu27-redesign/`).

**Problem.** The site had no visual identity of its own: a serif text title, flat EU-blue bands and no logo or
favicon. A brand (badge, wordmark, map artwork) was designed for it, and three of its parts break #76 and
`artifacts/README.md` invariant 4: the ring of stars, national flags, and an official-sounding wordmark.

**Alternatives considered.**
- **Ship the brand as designed and record the exception here (chosen).** The owner of the request judged the
  recognisable brand worth the risk #50 names, and kept the footer's line "not affiliated with any government or
  EU body".
- **Ship the palette, type, bands and wordmark, but leave out the star badge, flag favicon and tagline.** *Why
  not:* rejected by the requester, who asked for the design as is.
- **Keep the old look until the project owner reviews the brand.** *Why not:* the requester, an admin, asked for it
  to go live now; this pull request is where the owner can still refuse it before merge.

**Closes off.** The web app can no longer claim #76's "no circle of stars, flag or other official mark appears
anywhere". A reader may take the site for an EU institution's at first sight, which #50 was written to prevent; the
footer disclaimer is now the only counter to that. The web and the PDFs no longer share one look (#74, #91): the
PDFs keep the flat EU-blue cover and no emblem. The new subtitle says what data "should" stay national, a more
prescriptive tone than #72/#73/#77 chose; it is the requester's wording.

**Verified:** locally on 2026-10-08:
- `./test.sh --no-pdf --no-e2e --no-live` exits 0 ("All checks passed").
- `python3 design/build_tokens.py --check` exits 0, and `python3 -m unittest tests.test_tokens` passes 4 tests,
  including every WCAG contrast pair for the new dark palette.
- In `web/`: `npm run format:check`, `npm run lint` and `npm run type-check` report nothing; `npm test` passes
  51 tests; `npm run build` succeeds.
- The dev server, viewed in a browser: Overview and Methodology in dark mode, Overview in light mode; the method
  band is teal-tinted; the logo switches with the theme.

- Layouts, the same day: `npx playwright test e2e/app.spec.ts --project=chrome` passes 59 tests, including the
  axe checks in both themes and no sideways scroll at 375 px; one test now finds the 27 country cards instead of
  table rows. The macOS visual baselines (`e2e/visual.spec.ts-snapshots/`) were regenerated and pass.

NOT YET: the PDFs (`typst` is not installed on the machine that made this change), Firefox, WebKit and the phone
projects, and the live `/ask` check. CI runs them before the deploy.

*Would change if:* the European Commission or a reader objects that the badge or lockup implies EU endorsement; or
the project owner decides #50's reasoning outweighs the brand. Then the badge is replaced by a mark without stars,
the favicon by one without flags, and the lockup's tagline by a neutral line.

### 100. The repository, the Vercel project and the working directory are all named `eu27-data-sovereignty`
**Decision.** 2026-10-08, at the owner's request. The GitHub repo `EU27-data-sovereignty/sovereign-data-centers`
becomes `EU27-data-sovereignty/eu27-data-sovereignty`. The Vercel project `sovereign-data-centers` becomes
`eu27-data-sovereignty`; the project ID does not change, so `deploy.yml` is unaffected. The local directory
becomes `~/dev/projects/eu27-data-sovereignty`. Every live link (`model/contrib.py` `REPO`, and through it the
bundle's review and submit links; the user agents in `model/fetch.py` and `model/smoke.py`; `Layout.tsx`;
`CONTRIBUTING.md`; `LICENSE-DATA`) points at the new repo. Before this they pointed at
`pieteradejong/sovereign-data-centers`, the location before the move to the org, and worked only through
GitHub's redirects.

**Problem.** The project covers government data holdings and the sovereignty of their hosting, not data centres
alone. Its name matched neither the org (`EU27-data-sovereignty`) nor the site (`eu27.cloud`), and its public
links depended on two chained redirects.

**Alternatives considered.**
- **Rename the repo, the Vercel project and the directory together, and fix the links (chosen).**
- **Keep `sovereign-data-centers`.** *Why not:* the name describes a narrower project than this one, and differs
  from the org and the site.
- **Rename the repo only, and keep relying on redirects.** *Why not:* a redirect breaks the moment anyone creates
  a repo at the old name, and the issue links in the bundle are how citizens submit sources (#85).
- **Also rename the private `sovereign-data-centers-contacts` repo.** *Why not:* nothing depends on its name, and
  it is checked out at `contacts/` regardless.

**Closes off.** The old fallback URL `sovereign-data-centers.vercel.app` as the documented one, and new links to
the old repo name. History (the deploy table in `DEPLOYMENT.md`, earlier entries here and in `CHANGELOG.md`) keeps
the old names, because it records what was true then.

**Verified:** NOT YET. The tree side is checked by `./test.sh` and `git grep -n 'pieteradejong/sovereign-data-centers'`
returning only this entry and the changelog's. The repo rename, the Vercel rename and its domains, and the first deploy under the new names
are verified after they are carried out, by `gh repo view`, the Vercel project's domain list, `curl -sSI` on
`eu27.cloud` and on the new `.vercel.app` URL, and a green `Deploy` run.

*Would change if:* the project's scope narrows back to hosting infrastructure alone, or the org is renamed.

### 101. National AI strategies per state are an authored note, held to the frontier-model standard, never rendered and never ranked
**Decision.** 2026-10-10, at the owner's request. `NATIONAL-AI-STRATEGIES.md`, at the repository root, works out
for each of the 27 member states a strategy for a foundation AI model that is *good enough for its citizens*, not
frontier. It is an authored note in the sense of #44: not generated, not in the bundle, the web app, the PDFs or
`/ask`; `run.sh data` never touches it. Every factual claim in it carries the URL it came from and the access date,
and a claim not confirmed from a fetched page is marked **[unverified]**, the convention of `docs/plans/stichting.md`.
Cost and time bands are given once, per route, labelled reconstructed order-of-magnitude, never per state (#72).
States are grouped by the route recommended for them, alphabetical within a group, and the note says in the same
place that the groups are a recommendation and not a ranking (#10, #77). Its per-state snapshots are the seed for a
later sourced run that would turn the building blocks into reviewed indicators (`ROADMAP.md` § Planned).

**Problem.** The project's only treatment of national AI models was the model half of `FEASIBILITY-RANKING.md`, which
was written from memory, ranked the 27, and was superseded by #77 with its model half still "Not started". #59's
*Would change if* anticipated the facts being sourced. The owner wants the question explored for every state first,
in one document, before any of it is admitted as printed fact.

**Alternatives considered.**
- **An authored note at the root, one file for all 27, cited or marked unverified, route groups but no order (chosen).**
- **Render it through the content model as a per-state section and an EU-27 overview.** *Why not:* every printed value
  needs a fetched, hashed, quote-checked citation and an agreeing independent review before it prints (#79, #82, #87);
  that is the right end state, but it admits yes/partial/no facts, not a strategy, and the owner asked for the
  exploration first. Kept as the planned follow-on.
- **Extend `FEASIBILITY-RANKING.md`.** *Why not:* it is superseded, it ranks, and its model half has no sources; a
  reader would take the new material for part of the old ranking.
- **One note per state under `countries/<ISO>/`, like `NL/FRONTIER-MODEL.md`.** *Why not:* the owner asked for one
  document, and the routes, the language clusters and the EU vehicles are shared material that would be copied 27
  times or live nowhere.
- **Per-state cost figures.** *Why not:* #72 forbids scaling one state from another, and the only costed case is NL's;
  a per-state figure would be NL's figure with a different population.

**Closes off.** An order or score over the 27 in this note or anything derived from it; a per-state cost or capacity
figure (#73); quoting the note as a finding of the model (it carries the same caveat wording as #44's note); and
adding the note to any generated output without the sourced follow-on.

**Verified:** 2026-10-10. `./run.sh national-ai links` wrote `docs/national-ai-strategies-links.csv`: 393 URLs,
387 answered, 6 did not (four `gov.ie` pages refusing automated requests, two pages gone), each on a
line marked **[unverified]**. `./run.sh national-ai check` printed `27 states, 393 URLs (387 answered at the
last link check), 223 unverified marks, 36,795 words, 0 problems`. `tests/test_national_ai.py` and
`tests/test_docs.py` pass; `./test.sh --only model` recorded in `CHANGELOG.md`. The second-model review in
`docs/plans/national-ai-strategies-factcheck-<date>.md` is the owner's call and has not run.

*Would change if:* the sourced follow-on lands and the snapshots become reviewed indicators, at which point the
snapshot tables here become a pointer to the generated overview and only the strategies stay authored; or a reader
shows that a route grouping is being read as a ranking, in which case the groups are dissolved into the per-state
entries.
