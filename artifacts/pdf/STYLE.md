# PDF style

Shared look: [`../STYLE.md`](../STYLE.md). This file covers what is specific to PDFs.

**There is one PDF pipeline** (#74, #76). The Chrome-printed briefing PDFs and the mono A4 briefs are
retired.

| | EU-27 report and country reports | Print book |
|---|---|---|
| Built by | `book/report.py` → `typst compile` | `book/build.py` → `typst compile` |
| Source | the content model in `web/public/data/eu27.json` | `book/manuscript/*.typ` (authored parts only) |
| Template | `book/templates/report.typ` + generated `tokens.typ` | `book/templates/style.typ` |
| Colour | EU blue and gold (#76) | **mono** (#28), for photocopying |
| Output | `web/dist/eu27-report.pdf`, `web/dist/report/<ISO>.pdf` at deploy; `book/build/` locally | `book/build/book.pdf` |
| Tracked in git | **no** (#41); built at every deploy (#71) | no |

Typst rather than LaTeX is a decision (#23). Do not reintroduce a LaTeX toolchain, and do not
reintroduce pandoc: the report renders the content model directly.

## Structure

- **The report.** Cover, then:
  - contents (one entry per country, clickable, with PDF bookmarks);
  - *About this report* and the EU-27 table;
  - the *Data-sovereignty ranking* chapter (the rule, one row per state with confidence and range,
    the indicator grid);
  - 27 country chapters in alphabetical order;
  - the *Sources* appendix.
- **A country report.** The same chapter code, with its own cover, contents and source appendix.
- **Chapter order is the content model's section order:** placement, fundamentals, holdings by
  priority, dependency exposure, legal posture, capacity status, open research.

## Sources on the page

- **Footnotes.** Every `fact` span gets one footnote per distinct citation. Each note carries the source's
  short label, the locator where it adds anything, the retrieval date, and a link to its appendix entry
  `[Sn]`.
- **The appendix** lists each source once, in order of first citation. Each entry gives the title,
  publisher, URL, archived copy and document hash, then every claim citing it, with its quote.
- **Tests.** `tests/test_book.py` asserts one footnote per distinct citation and that every footnote link
  lands on an appendix entry.

## Cover

A full-bleed EU-blue cover with a gold rule. **No circle of stars** (#76); `tests/test_tokens.py` fails
if a template draws one. The cover says the work is independent and not affiliated with any government
or EU body.

## Verify

```
python3 book/report.py                 # book/build/eu27-report.pdf
python3 book/report.py --countries     # book/build/report/<ISO>.pdf
python3 -m unittest tests.test_book -v
```
Then open the report: check the cover, the contents, one country's first page with footnotes, and the
appendix. `typst compile --pages N --format png` renders single pages for a quick look.
