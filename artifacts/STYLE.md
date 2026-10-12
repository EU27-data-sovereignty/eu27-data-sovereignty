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

Brand blue, navy and a deeper gold, from the EU27.CLOUD landing design (#101). On the web, gold is kept for the
hero underline, the selector band, link underlines and focus rings on navy.

| Token | Light | Dark | Use |
|---|---|---|---|
| `eu_blue` (brand) | `#1E3A8A` | — | Eyebrows, links, filled buttons and selected states |
| `eu_gold` (brand) | `#F2C230` | — | The hero underline, the active toggle, link underlines; **never text on white** |
| `eu_deep` (brand) | `#0B1B3F` | — | Primary ink in light mode, the page in dark mode |
| `navy_surface` / `navy_border` / `navy_hover` (brand) | `#13265A` / `#2A3F7A` / `#18306B` | — | The audience selector's buttons, the same in both themes |
| `accent` | `#1E3A8A` | `#F2C230` | Focus rings and selected outlines |
| `accent_text` | `#1E3A8A` | `#C9D5F2` | Links, accented text, bars |
| `fg_on_accent` | `#FFFFFF` | `#0B1B3F` | Text on an accent fill |
| `fg_primary` / `fg_secondary` / `fg_muted` | `#0B1B3F` / `#374151` / `#4B5563` | `#E6EAF3` / `#C9D5F2` / `#AFBBDA` | Headings, body, captions and gaps |
| `bg_page` / `bg_card` / `bg_emphasis` | `#F4F6FA` / `#FFFFFF` / `#EEF1F8` | `#0B1B3F` / `#13265A` / `#18306B` | Surfaces; `bg_emphasis` is the table header |
| `hero_from` → `hero_to` / `band` / `map_fill` | `#EEF2F9` → `#E3E9F4` / `#DDE1E9` / `#DCE0E7` | `#13265A` → `#0B1B3F` / `#0F2150` / `#1E2E5C` | The hero gradient, the selector band, the EU silhouette |
| `gap_mark` | `#9AA8C4` | `#9AA8C4` | The dashed rule under a disputed value; the hero's dot texture |
| `rank_1` … `rank_5` | blue ramp, then amber `#A16A00` | lighter ramp, amber `#E5AC1F` | The five ranking groups, best to worst (#77) |

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
