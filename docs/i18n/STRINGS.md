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

| ISO | State | Languages |
|---|---|---|
| AT | Austria | de |
| BE | Belgium | nl, fr, de |
| BG | Bulgaria | bg |
| CY | Cyprus | el |
| CZ | Czechia | cs |
| DE | Germany | de |
| DK | Denmark | da |
| EE | Estonia | et |
| EL | Greece | el |
| ES | Spain | es |
| FI | Finland | fi, sv |
| FR | France | fr |
| HR | Croatia | hr |
| HU | Hungary | hu |
| IE | Ireland | ga (en is the source) |
| IT | Italy | it |
| LT | Lithuania | lt |
| LU | Luxembourg | fr, de, lb (national, not an EU language) |
| LV | Latvia | lv |
| MT | Malta | mt (en is the source) |
| NL | Netherlands | nl |
| PL | Poland | pl |
| PT | Portugal | pt |
| RO | Romania | ro |
| SE | Sweden | sv |
| SI | Slovenia | sl |
| SK | Slovakia | sk |

States that share a language (AT and DE; BE and NL; BE, FR and LU; CY and EL; FI and SE; BE and LU for
German) get their own file each: the draft for Austria may differ from the one for Germany in register
and in administrative terms (Austrian German says *Meldewesen* where German German says
*Einwohnermeldewesen*), and the reviewer is asked to say so.
