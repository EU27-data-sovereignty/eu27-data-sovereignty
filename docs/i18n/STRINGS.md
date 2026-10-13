# The strings a language draft covers

The English wording the web app, the PDFs and the briefs print around the facts: navigation, section
titles, table headings, the notices. Facts are never translated here; a printed fact stays in its
original-language quote with its machine gloss (#82). A draft translates this table and nothing else.

Keys are stable identifiers. The `en` column is the source text as the app prints it on 2026-10-12.
A draft file (`drafts/<ISO>.md`) carries every key below, in this order, with one column per official
language of that state.

| key | en | where it prints |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | browser tab, PDF title |
| site.kicker | EU-27 | page band kicker |
| nav.overview | Overview | navigation |
| nav.ranking | Ranking | navigation |
| nav.countries | Countries | navigation |
| nav.holdings | Critical holdings | navigation |
| nav.hosting | Hosting | navigation |
| nav.sources | Sources | navigation |
| nav.ask | Ask | navigation |
| nav.methodology | Methodology | navigation |
| nav.factcheck | Fact check | navigation |
| country.kicker | Country report | country page band |
| country.contents | Contents | country page, sidebar |
| country.sources | Sources | country page, sidebar and heading |
| section.fundamentals | Fundamentals | country report section 1 |
| section.holdings | Critical data holdings, by priority | country report section 2 |
| section.exposure | Foreign-dependency exposure | country report section 3 |
| section.posture | Legal and institutional posture | country report section 4 |
| section.sizing | Capacity | country report section 5 |
| section.gaps | Research still open | country report section 6 |
| section.placement | Data-sovereignty placement | country report section 7 |
| overview.hosting | Where key registers are hosted, and by whom | EU-27 overview |
| overview.coverage | What is known, per state | EU-27 overview |
| col.indicator | Indicator | table heading |
| col.value | Value | table heading |
| col.priority | Priority | table heading |
| col.holding | Holding | table heading |
| col.register | Register or system | table heading |
| col.infrastructure | Infrastructure | table heading |
| col.holdings | Holdings | table heading |
| col.dimension | Dimension | table heading |
| col.position | Position | table heading |
| col.finding | Finding | table heading |
| col.state | State | table heading |
| col.registers_sourced | Registers sourced | table heading |
| col.hosting_sourced | Hosting sourced | table heading |
| fact.check_this | Check this fact | link on every fact |
| fact.gloss | Machine translation: | label before a glossed quote |
| fact.withheld | withheld until sourced | a value with no checked source |
| fact.disputed | withheld as disputed | a value the fact checker did not confirm |
| status.loading | Loading the EU-27 dataset… | before the bundle arrives |
| status.load_error | Could not load the data | bundle failed |
| notfound.title | Page not found | unknown route |
| notfound.back | Back to the overview | unknown route |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | footer of every page, every PDF and brief |

## Official languages per state

The columns a draft carries. The code is the ISO 639-1 code; where English is official (IE, MT) the
`en` column is the source and only the other language is drafted. Luxembourgish is not an official EU
language but is a national language of Luxembourg; its column is marked as such.

| ISO | State | Languages | BCP 47 tags |
|---|---|---|---|
| AT | Austria | de | de-AT |
| BE | Belgium | nl, fr, de | nl-BE, fr-BE, de-BE |
| BG | Bulgaria | bg | bg-BG |
| CY | Cyprus | el | el-CY |
| CZ | Czechia | cs | cs-CZ |
| DE | Germany | de | de-DE |
| DK | Denmark | da | da-DK |
| EE | Estonia | et | et-EE |
| EL | Greece | el | el-GR |
| ES | Spain | es | es-ES |
| FI | Finland | fi, sv | fi-FI, sv-FI |
| FR | France | fr | fr-FR |
| HR | Croatia | hr | hr-HR |
| HU | Hungary | hu | hu-HU |
| IE | Ireland | ga (en is the source) | ga-IE |
| IT | Italy | it | it-IT |
| LT | Lithuania | lt | lt-LT |
| LU | Luxembourg | fr, de, lb (national, not an EU language) | fr-LU, de-LU, lb-LU |
| LV | Latvia | lv | lv-LV |
| MT | Malta | mt (en is the source) | mt-MT |
| NL | Netherlands | nl | nl-NL |
| PL | Poland | pl | pl-PL |
| PT | Portugal | pt | pt-PT |
| RO | Romania | ro | ro-RO |
| SE | Sweden | sv | sv-SE |
| SI | Slovenia | sl | sl-SI |
| SK | Slovakia | sk | sk-SK |

## The standards the drafts follow

- **Language tags are BCP 47 (RFC 5646):** an ISO 639-1 language subtag and an ISO 3166-1 region subtag,
  `de-AT`, `nl-BE`, `sv-FI`. The region is the ISO 3166-1 code, so Greece's tag is `el-GR` although the
  project keys the state as `EL` (Eurostat's code). A draft file's `Languages:` line carries the tag of every
  column, and a renderer puts it in `<html lang>`, in `hreflang` alternates with an `x-default`, and in
  `Content-Language`.
- **Column headers are the language subtag alone** (`de`, `nl`); the state's file gives the region. The
  URL carries the subtag too (`/be/fr`), never the full tag.
- **Text is UTF-8, Unicode NFC.** The checker fails a cell that is not NFC, so composed and decomposed
  diacritics cannot mix, and a cell with leading or trailing whitespace.
- **The source is the English the app prints** (`en-GB` spelling). "EU-27" and the ellipsis (U+2026) are
  kept as they are.
- **No string is built by concatenation and none carries a placeholder today.** A future string with a count
  or a date is written as an ICU MessageFormat pattern with the plural forms of the target language, and
  numbers and dates are formatted with `Intl` for the page's tag, never by hand.
- **Direction is left to right** for every official EU language; no bidi handling is needed.

States that share a language (AT and DE; BE and NL; BE, FR and LU; CY and EL; FI and SE; BE and LU for
German) get their own file each: the draft for Austria may differ from the one for Germany in register
and in administrative terms (Austrian German says *Meldewesen* where German German says
*Einwohnermeldewesen*), and the reviewer is asked to say so.
