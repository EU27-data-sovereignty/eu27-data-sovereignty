# Sweden (SE): language draft

- Languages: sv Swedish (sv-SE)
- Drafted by: agent B, claude-fable-5-1, 2026-10-12
- Revised by: agent B, claude-fable-5-1, 2026-10-20 (applied the review's 0 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern)
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | sv |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | EU-27:s suveräna datacenter |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Översikt |
| nav.ranking | Ranking | Rangordning |
| nav.countries | Countries | Länder |
| nav.holdings | Critical holdings | Kritiska informationstillgångar |
| nav.hosting | Hosting | Drift |
| nav.sources | Sources | Källor |
| nav.ask | Ask | Fråga |
| nav.methodology | Methodology | Metod |
| nav.factcheck | Fact check | Faktagranskning |
| nav.about | About the data | Om uppgifterna |
| country.kicker | Country report | Landrapport |
| country.contents | Contents | Innehåll |
| country.sources | Sources | Källor |
| section.fundamentals | Fundamentals | Grunduppgifter |
| section.holdings | Critical data holdings, by priority | Kritiska informationstillgångar, efter prioritet |
| section.exposure | Foreign-dependency exposure | Exponering för utländskt beroende |
| section.posture | Legal and institutional posture | Rättslig och institutionell ställning |
| section.sizing | Capacity | Kapacitet |
| section.gaps | Research still open | Öppna forskningsfrågor |
| section.placement | Data-sovereignty placement | Placering i fråga om datasuveränitet |
| overview.hosting | Where key registers are hosted, and by whom | Var centrala register driftas, och av vem |
| overview.coverage | What is known, per state | Vad som är känt, per stat |
| col.indicator | Indicator | Indikator |
| col.value | Value | Värde |
| col.priority | Priority | Prioritet |
| col.holding | Holding | Informationstillgång |
| col.register | Register or system | Register eller system |
| col.infrastructure | Infrastructure | Infrastruktur |
| col.holdings | Holdings | Informationstillgångar |
| col.dimension | Dimension | Dimension |
| col.position | Position | Position |
| col.finding | Finding | Iakttagelse |
| col.state | State | Stat |
| col.registers_sourced | Registers sourced | Register med källa |
| col.hosting_sourced | Hosting sourced | Drift med källa |
| fact.check_this | Check this fact | Kontrollera denna uppgift |
| fact.gloss | Machine translation: | Maskinöversättning: |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# värde undanhållet tills källa finns} other {# värden undanhållna tills källa finns}} |
| fact.disputed | withheld as disputed | undanhållen som omtvistad |
| status.loading | Loading the EU-27 dataset… | Läser in EU-27-datamängden… |
| status.load_error | Could not load the data | Det gick inte att läsa in uppgifterna |
| notfound.title | Page not found | Sidan hittades inte |
| notfound.back | Back to the overview | Tillbaka till översikten |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Maskinkontrollerad, inte verifierad av människor. Automatiserade agenter hittade dessa källor och kontrollerade dem mekaniskt; ingen person har granskat iakttagelserna. Engelsk formulering av en icke-engelsk källa är en maskinöversättning eller en maskinell sammanfattning av den citerade texten. Betrakta varje uppgift som ett spår till dess angivna källa, inte som fastställd. Rättelser välkomnas via repositoriets ärendemall. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | Etiketterna på den här sidan är en maskinöversättning. Ingen person som läser detta språk har kontrollerat dem ännu. |

- Note: sv follows Sweden usage: "drift"/"driftas" for hosting as in Swedish public-sector IT, and "informationstillgångar" (the MSB term) for holdings; Finland-Swedish texts more often keep the loanword "hosting".

## Review

- Reviewed by: agent A, claude-opus-5-5, 2026-10-12
- Re-reviewed by: agent A, claude-opus-5-5, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer)
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | sv | ok | | |
| site.kicker | sv | ok | | |
| nav.overview | sv | ok | | |
| nav.ranking | sv | ok | | |
| nav.countries | sv | ok | | |
| nav.holdings | sv | ok | | |
| nav.hosting | sv | ok | | |
| nav.sources | sv | ok | | |
| nav.ask | sv | ok | | |
| nav.methodology | sv | ok | | |
| nav.factcheck | sv | ok | | |
| nav.about | sv | ok | idiomatic menu label for 'About the data' | |
| country.kicker | sv | ok | | |
| country.contents | sv | ok | | |
| country.sources | sv | ok | | |
| section.fundamentals | sv | ok | | |
| section.holdings | sv | ok | | |
| section.exposure | sv | ok | | |
| section.posture | sv | ok | | |
| section.sizing | sv | ok | | |
| section.gaps | sv | ok | | |
| section.placement | sv | ok | | |
| overview.hosting | sv | ok | | |
| overview.coverage | sv | ok | | |
| col.indicator | sv | ok | | |
| col.value | sv | ok | | |
| col.priority | sv | ok | | |
| col.holding | sv | ok | | |
| col.register | sv | ok | | |
| col.infrastructure | sv | ok | | |
| col.holdings | sv | ok | | |
| col.dimension | sv | ok | | |
| col.position | sv | ok | | |
| col.finding | sv | ok | | |
| col.state | sv | ok | | |
| col.registers_sourced | sv | ok | | |
| col.hosting_sourced | sv | ok | | |
| fact.check_this | sv | ok | | |
| fact.gloss | sv | ok | | |
| fact.withheld | sv | ok | one/other, undanhållet/undanhållna agree | |
| fact.disputed | sv | ok | | |
| status.loading | sv | ok | | |
| status.load_error | sv | ok | | |
| notfound.title | sv | ok | | |
| notfound.back | sv | ok | | |
| notice.disclaimer | sv | ok | re-read 2026-10-20: 'machine-checked' is checked, not verified; nothing weakened | |
| notice.unread | sv | ok | says plainly it is a machine translation and that no reader of the language has checked it; no verified/approved word | |
