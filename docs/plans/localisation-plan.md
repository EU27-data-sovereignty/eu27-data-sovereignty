# Plan: a country URL that speaks the country's language

Drafted 2026-10-12 at the owner's request. A plan, not a decision: nothing in it renders until the decision
entry it proposes (#107) is written and the tests named here exist. The language drafts it relies on are
agent output under `docs/i18n/drafts/`, and `docs/i18n/README.md` says what state they are in.

## 1. Where we are

Since #105 every member state has its own address: `eu27.cloud/de`, `eu27.cloud/fr`, `eu27.cloud/el`, and
the old `/country/<ISO>` redirects. The page behind each address is in English. The facts on it are
printed from the original-language quote with a machine gloss into English (#82), so the evidence is
already in the state's language; the chrome around it is not.

## 2. The goal

`eu27.cloud/de` reads as a German page: navigation, section titles, table headings, the notices and the
not-found page in German, the facts as they are today. `eu27.cloud/be` offers Dutch, French and German.
`eu27.cloud/ie` offers English and Irish. The EU-27 overview, the ranking, the methodology and `/ask`
stay English in the first stage.

## 3. The URL scheme

| Address | Serves |
|---|---|
| `/de` | Germany, in the state's first official language (German) |
| `/be` | Belgium, in Dutch (the first listed language); a switch offers `fr` and `de` |
| `/be/fr` | Belgium, in French |
| `/de/en` | Germany, in English |
| `/en` | nothing: #105 reserves two-letter top-level segments for states, and `en` is not one |

The language is the second path segment, never a query parameter and never a top-level segment. A reader
who types the address gets the state's own language; a reader who wants English adds `/en`. The server
side needs nothing new: the SPA rewrite already catches `/de/en`. The router adds one optional segment to
the `:iso` route and reads it through the same helper that builds every country link (`countryPath`),
which gains a language argument.

Why not `Accept-Language`: it hides the choice in the browser, it makes two readers of the same link see
different pages, and the smoke test and the fact-check audit could not name what a URL shows.

## 4. What is translated, and what is not

Translated: the 45 strings in `docs/i18n/STRINGS.md`. They are chrome, they carry no fact, and they are
the same on every page.

Not translated, in this stage or any other without its own decision:
- **Facts.** A printed value is the original quote plus its gloss (#82, #87). The gloss is English. A
  gloss into the state's language would be a second machine translation that the fact checker has not
  seen; it is possible later, as a labelled second gloss, after #87's checker has a rule for it.
- **The guides, the methodology, the hero text.** Long prose, changed often; a later stage.
- **The posters and the PDFs.** typst needs a font per script (Greek, Cyrillic) and a hyphenation
  pattern per language; the web page first, the PDFs when the fonts are pinned and checksummed like
  typst itself (#81).
- **`/ask`.** Its corpus is English; a question in German is answered in German by the model already.

## 5. The pipeline, so a third party can check it

1. **Source.** `docs/i18n/STRINGS.md`: the keys, the English text, where each prints, and the official
   languages per state. A test will fail if the app prints a string that is not in the table, so the
   table cannot drift from the app.
2. **Drafts.** One file per state under `docs/i18n/drafts/`, written by an agent, with the agent and the
   model id on the file. The format is fixed so a script reads it.
3. **Cross-review.** A second agent, on a different model, reviews every cell of every file it did not
   draft and records `ok` or `fix` with a note and a suggested wording. The drafting pair of 2026-10-12
   was claude-opus-5-5 (agent A, 14 states) and claude-fable-5-1 (agent B, 13 states), each reviewing
   the other. `python3 model/i18n_drafts.py check` fails if a file is unreviewed, reviewed by its own
   drafter, missing a key, missing a language, or has a disclaimer that is not a full translation.
4. **Native reading.** A `fix` is applied by the drafter and re-reviewed. Before anything renders, each
   language gets one reading by a person who speaks it, recorded in the file as a third line
   (`Read by: <role>, <date>`), because the project's honesty notice says what no person has reviewed,
   and a translated honesty notice no person has read is the one thing the notice must not be.
5. **Admission.** A script moves reviewed and read drafts into `model/i18n/<lang>.json`, one file per
   language, with the state variants (`de-AT`, `nl-BE`) as overlays. Drafts stay where they are, as the
   trail. The bundle carries the tables; renderers look strings up by key and never hold a literal.
6. **Rendering.** The web app reads the language from the URL, falls back to English per key, and marks
   a page that has any fallback with the English notice. `tests/test_i18n.py` checks every admitted
   language has every key; the Playwright suite opens `/de`, `/be/fr` and `/ie/ga` and reads the
   navigation.
7. **The honesty notice.** `notice.disclaimer` renders only from an admitted, read translation; a
   language without one shows the English notice. The evidence test that forbids prose claiming a check
   that did not run applies to every language.

## 6. The decision to write (#107, not yet written)

- **Decision.** Language is the second path segment under a state; the first official language is the
  default; strings come from admitted tables keyed by `STRINGS.md`; facts are not translated.
- **Alternatives.** `Accept-Language` (rejected: §3); a query parameter (rejected: not an address);
  top-level language routes (closed off by #105); translating the glosses in the same stage (rejected:
  §4); machine drafts rendered without a native reading (rejected: §5.4).
- **Closes off.** Any literal string in a renderer; any rendered translation without a review by a
  different agent and a reading by a person.
- **Verified / Would change if.** To be filled when the stage ships.

## 7. Stages and their checks

| Stage | Work | Check |
|---|---|---|
| 0 (done) | `STRINGS.md`, 27 drafts, cross-review, `i18n_drafts.py check` | `check` exits 0; `docs/i18n/README.md` summary |
| 1 | `fix` verdicts applied and re-reviewed; one native reading per language | every file carries `Read by:` |
| 2 | #107; `model/i18n/`; admission script; the router segment; `countryPath(iso, lang)`; the switch | `tests/test_i18n.py`; Playwright on `/de`, `/be/fr`, `/ie/ga`; `./test.sh` green |
| 3 | PDFs per language once fonts are pinned | `tests/test_workflows.py` checksums; PDF stage green |
| 4 | glosses into the state's language, under #87's checker | a fact-check run with the new rule |

## 8. Cost and risk, in one line each

- Twenty-four languages across 27 states, 45 strings each: a small table, a large review surface; the
  disclaimer is the one string whose wording carries weight, and it is reviewed twice and read once.
- A reader of `/de` must never see a page that mixes a translated notice with an English fact label
  and conclude a person checked it; the per-key fallback notice in §5.6 is what prevents it.
