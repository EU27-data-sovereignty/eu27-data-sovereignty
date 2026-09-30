# Style guide

The one look for every representation: the web app, the EU-27 report and the country PDFs, the posters,
the markdown briefs and the mobile reader. The per-format guides in this directory add only what is
specific to their format and cite this file for the rest.

**The source of truth is [`design/tokens.json`](../design/tokens.json).** `design/build_tokens.py`
generates `web/src/styles/tokens.css`, `book/templates/tokens.typ` and `mobile/src/constants/Colors.ts`
from it. It checks WCAG contrast before writing and refuses a palette that fails. `tests/test_tokens.py`
fails if a generated file is stale, if a web component hard-codes a hex colour, or if a template draws a
star (#74, #76).

## Colour

EU blue and gold, and nothing that reads as official.

| Token | Light | Dark | Use |
|---|---|---|---|
| `eu_blue` (brand) | `#003399` | — | Accent and cover |
| `eu_gold` (brand) | `#FFCC00` | — | Rules, highlights, the selected state; **never text on white** |
| `accent` | `#003399` | `#FFCC00` | Buttons, focus rings, header rules |
| `accent_text` | `#003399` | `#A9C0FF` | Links and accented text |
| `fg_on_accent` | `#FFFFFF` | `#0A0F1E` | Text on an accent fill |
| `fg_primary` / `fg_secondary` / `fg_muted` | `#14171F` / `#454C5E` / `#5A6173` | `#FFFFFF` / `#C6CCDB` / `#9AA3B8` | Body, secondary, captions and gaps |
| `bg_page` / `bg_card` / `bg_emphasis` | `#F6F7FA` / `#FFFFFF` / `#EAF0FB` | `#0A0F1E` / `#111A31` / `#18264A` | Surfaces |
| `rank_1` … `rank_5` | blue ramp, then amber `#B07800` | lighter ramp, amber `#E0A100` | The five ranking groups, best to worst (#77) |

- **No emblem.** No circle of stars, no flag, no crown, no official wordmark on any artefact (#47, #50,
  #76). Country flag emoji appear only in the markdown index (`countries/SUMMARY.md`).
- **Colour is never the only cue.** A group, a gap or a status is always also written in words. Low
  confidence on the map is hatched as well as coloured.
- **Contrast** is checked by the generator for every text pair (4.5:1) and UI pair (3:1), in both themes.
- **Dark mode** is selected, not inverted: every token has a dark value, and an explicit toggle wins over
  the OS setting in both directions.

## Type

| | Web and mobile | Print (typst) |
|---|---|---|
| Family | Inter, system fallback | Libertinus Serif, Georgia fallback |
| Body | 14 px | 10 pt |
| Tables | 14 px, `tabular-nums` for figures | 8.5 pt |
| Footnotes | superscript `[n]` link | 7 pt at the foot of the page |

Numeric columns are right-aligned. Headings never skip a level.

## How facts, gaps and method look

The content model gives every piece of text a role (#75), and every renderer shows the roles the same way:

| Role | Looks like | Carries |
|---|---|---|
| `fact` | plain text, then a source marker: web `[n]` link, PDF footnote, markdown `[^sn]` | claim ids resolving to a checked source |
| `gap` | *muted italic*: "Not yet sourced", "Not yet verified" | nothing; a value is withheld, never shown unsourced |
| `method` | plain text | this project's own rules and reasoning |
| `label` | plain or bold | row and column names |

- **Source lists** show each source once, numbered in first-citation order: the title, publisher, URL,
  the archived copy (when one matches the URL exactly) and the document hash, then every claim on that
  page that rests on it, with its quote.
- **Web and PDF agree on numbering.** Footnote `[3]` on a country page and `[S3]` in that country's PDF
  name the same document.

## Provenance travels with the artefact

Anything that can be shared on its own carries its own caveat: the site banner, the PDF running footer,
the poster footer and the markdown header (#25). The wording comes from the bundle (`provenance`), so
every representation hedges the same way.

## The ranking

Groups, never scores (#10, #77). Wherever a placement appears it shows its **confidence** and the
guardrail: "Groups describe what the sources show, not how sovereign a state is." States within a group
are alphabetical. No representation may add an order or a number.

## Layout

- **Web.** The page never scrolls sideways at 375 px: wide tables scroll in their own container, and long
  unbreakable strings (hashes, claim ids) wrap.
- **PDF.** A4, with each country chapter on a new page under a blue band and gold rule, and a running
  header naming the chapter.
- **Poster.** 1,024 px wide; fundamentals and tier 0 holdings only; its own source list.
