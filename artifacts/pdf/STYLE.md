# PDF style

**There are two PDF pipelines in this repository, and they share nothing.** Conflating them is the
most common mistake here, so they are stated separately throughout.

| | Typst pipeline | Chrome pipeline |
|---|---|---|
| Produces | the A5 book, and 27 standalone A4 country briefs | the 27 `<ISO>-briefing.pdf` |
| Built by | `book/build.py` → `typst compile` | `model/export_artifacts.py` → headless Chrome |
| Source | `web/public/data/eu27.json` + `book/manuscript/*.typ` | the built web app, printing `/country/:iso` |
| Styling lives in | `book/templates/style.typ` | `web/src/` — see [`../html/STYLE.md`](../html/STYLE.md) |
| Colour | **mono** (#28) | full colour |
| Tracked in git | **no** (#41) — output goes to gitignored `book/build/` | **yes** (#51) |
| Needs | `typst` (`brew install typst`) | Chrome + `npm` |

Typst rather than Pandoc + LaTeX is a decision (#23). Do not reintroduce a LaTeX toolchain.

---

## The Typst pipeline

### Structure

The book is an authored argument wrapped around a country gazetteer (#27): Parts I, II and V are
hand-written Typst in `book/manuscript/`; Part III is the 27 countries, Part IV the reference
tables. `book/build.py` assembles them in order and emits one `.typ` file, by string concatenation
— there is no template engine.

**One renderer serves both the book chapter and the standalone brief** (#39). `country_entry()`
takes `standalone`, which promotes every section heading by one level, because the brief's title
block already carries the country name that the book puts in a chapter head. A brief and its
chapter therefore cannot disagree. Do not fork this function.

Geometry is fixed (#40): the book is A5 with inside/outside margins and part openers forced to
recto; the brief is A4 with no forced breaks, because a brief is read straight through.

### Mono, and why it is not negotiable

The interior uses `luma()` only — `ink` 15, `mid` 95, `quiet` 140, `rule` 200, `wash` 244. **No
hue anywhere** (#28). Briefing documents get photocopied, so a chart that dies in black and white
dies in exactly the setting this book is for; mono print-on-demand is also roughly a third the
unit cost at ~300 pages.

Consequences for anything you add:

- Heatmaps and charts re-encode by **value and texture**, never by hue.
- A distinction that survives only in colour has to be re-encoded or dropped.
- The web and Chrome-printed PDF editions keep full colour. Mono is a property of this pipeline,
  not of the project.

### Type and tables

- Serif text — Libertinus Serif, falling back to Georgia and Times New Roman. 9.5pt in the book,
  10pt in the brief; justified, `leading: 0.62em`.
- Headings are unnumbered (`set heading(numbering: none)`). Level 1 breaks to recto, level 2
  breaks the page, level 3 is small bold.
- Use the shared `#datatable()` helper, which is `breakable: false` — a table that splits across
  an A5 spread is unreadable. Caption is 6.5pt `quiet`.
- Use `#standfirst()` for the one-line stake at the top of a country chapter.
- **Escape everything from the data.** `esc()` and `esc_md()` handle Typst's `#@$\<>*_~[]` and
  convert markdown `**bold**` to Typst `*bold*`. Country names and register names arrive from
  CSVs and will contain characters Typst treats as syntax.

### Table of contents

The book carries `#outline(title: [Contents], depth: 2, indent: 1em)`, placed after the half-title.
`depth: 2` captures part openers and country chapters but not per-country subsections, which is
correct: a 27-country outline at depth 3 would run for pages.

**Countries are identified in the outline by ISO code, not by flag emoji** — `DE · Germany`.
Two reasons, both hard: `typst` can only reach flag glyphs by falling back to Apple Color Emoji,
which is colour (against the mono rule above) and macOS-only, so the book would silently render
tofu on any other machine and stop being reproducible. Flag emoji belong in the markdown, HTML and
mobile contents lists, where neither problem exists.

The standalone A4 briefs carry **no** outline. A contents list for a single country is noise.

### Front matter

There is no cover, no index and no bibliography — only the half-title. This is a known gap
recorded in `book/README.md`, not an oversight to fix incidentally.

### Output is never committed

`book/build/` is gitignored (#41, #24). The book and the A4 briefs are build output; only the
27 `countries/<ISO>/` artefacts are tracked deliverables. CI has no `typst`, so **the book is
ungated** — there is no test on its Typst output. Check it by eye.

---

## The Chrome pipeline

The 27 `<ISO>-briefing.pdf` are headless Chrome printing the app's `/country/:iso` route (#42).
There is no separate stylesheet: **their style is the HTML style guide**, filtered through
`@media print`. To change how a briefing PDF looks, change the app.

Two properties matter beyond "the file exists", and both are load-bearing:

- **Byte-reproducible.** Chrome stamps wall-clock `/CreationDate` and `/ModDate` into every PDF,
  which produced 27 spurious diffs per run. Both fields are rewritten to `SOURCE_DATE_EPOCH`
  after export (#53).
- **Detectably stale.** Every run rewrites `countries/ARTEFACTS.csv` with each artefact's sha256
  *and* the sha256 of the JSON bundle it was rendered from (#52). `tests/test_artifacts.py` fails
  when the bundle has moved on — the only way to catch a tracked binary that CI cannot rebuild.

**Consequence: any change to `eu27.json` invalidates all 54 tracked artefacts at once.** Re-render
them in the same commit as the change, or the suite fails.

The app renders client-side, so Chrome must be given `--virtual-time-budget`; without it, the
capture is a loading message, which is indistinguishable from success until someone opens the file.

No state emblems or flag emoji in these PDFs (#47).

## Verify

```
./run.sh book                     # A5 book -> book/build/book.pdf
./run.sh export                   # 27 A4 briefs -> book/build/briefs/
./run.sh artefacts                # the 27 tracked briefing PDFs + 27 posters
python3 -m unittest tests.test_artifacts -v
```

Then open `book/build/book.pdf` and check: Contents page present, no tofu, still monochrome.
