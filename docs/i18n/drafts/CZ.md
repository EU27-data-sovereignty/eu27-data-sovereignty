# Czechia (CZ): language draft

- Languages: cs Czech (cs-CZ)
- Drafted by: agent A, claude-opus-5-5, 2026-10-12
- Revised by: agent A, claude-opus-5-5, 2026-10-20 (applied the review's 0 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern)
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | cs |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | Suverénní datová centra EU-27 |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Přehled |
| nav.ranking | Ranking | Pořadí |
| nav.countries | Countries | Země |
| nav.holdings | Critical holdings | Kritické datové fondy |
| nav.hosting | Hosting | Hosting |
| nav.sources | Sources | Zdroje |
| nav.ask | Ask | Zeptat se |
| nav.methodology | Methodology | Metodika |
| nav.factcheck | Fact check | Ověření faktů |
| nav.about | About the data | O datech |
| country.kicker | Country report | Zpráva o zemi |
| country.contents | Contents | Obsah |
| country.sources | Sources | Zdroje |
| section.fundamentals | Fundamentals | Základní údaje |
| section.holdings | Critical data holdings, by priority | Kritické datové fondy podle priority |
| section.exposure | Foreign-dependency exposure | Expozice vůči závislosti na zahraničí |
| section.posture | Legal and institutional posture | Právní a institucionální postavení |
| section.sizing | Capacity | Kapacita |
| section.gaps | Research still open | Dosud neuzavřený výzkum |
| section.placement | Data-sovereignty placement | Zařazení z hlediska datové suverenity |
| overview.hosting | Where key registers are hosted, and by whom | Kde jsou klíčové registry hostovány a kým |
| overview.coverage | What is known, per state | Co je známo o jednotlivých státech |
| col.indicator | Indicator | Ukazatel |
| col.value | Value | Hodnota |
| col.priority | Priority | Priorita |
| col.holding | Holding | Datový fond |
| col.register | Register or system | Registr nebo systém |
| col.infrastructure | Infrastructure | Infrastruktura |
| col.holdings | Holdings | Datové fondy |
| col.dimension | Dimension | Rozměr |
| col.position | Position | Pozice |
| col.finding | Finding | Zjištění |
| col.state | State | Stát |
| col.registers_sourced | Registers sourced | Registry se zdrojem |
| col.hosting_sourced | Hosting sourced | Hosting se zdrojem |
| fact.check_this | Check this fact | Ověřit tento fakt |
| fact.gloss | Machine translation: | Strojový překlad: |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# hodnota zadržena do doložení zdroje} few {# hodnoty zadrženy do doložení zdroje} many {# hodnoty zadrženo do doložení zdroje} other {# hodnot zadrženo do doložení zdroje}} |
| fact.disputed | withheld as disputed | zadrženo jako sporné |
| status.loading | Loading the EU-27 dataset… | Načítání datové sady EU-27… |
| status.load_error | Could not load the data | Data se nepodařilo načíst |
| notfound.title | Page not found | Stránka nenalezena |
| notfound.back | Back to the overview | Zpět na přehled |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Strojově zkontrolováno, neověřeno člověkem. Automatizovaní agenti tyto zdroje našli a mechanicky je zkontrolovali; zjištění nepřezkoumal žádný člověk. Anglické znění neanglického zdroje je strojový překlad nebo strojové shrnutí citovaného textu. Každý fakt berte jako vodítko k jeho citovanému zdroji, nikoli jako prokázaný. Opravy jsou vítány prostřednictvím šablony pro hlášení (issue template) v repozitáři. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | Popisky na této stránce jsou strojový překlad. Zatím je nezkontroloval žádný člověk, který tento jazyk čte. |

## Review

- Reviewed by: agent B, claude-fable-5-1, 2026-10-12
- Re-reviewed by: agent B, claude-fable-5-1, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer)
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | cs | ok | | |
| site.kicker | cs | ok | | |
| nav.overview | cs | ok | | |
| nav.ranking | cs | ok | | |
| nav.countries | cs | ok | | |
| nav.holdings | cs | ok | | |
| nav.hosting | cs | ok | | |
| nav.sources | cs | ok | | |
| nav.ask | cs | ok | | |
| nav.methodology | cs | ok | | |
| nav.factcheck | cs | ok | | |
| nav.about | cs | ok | natural label for the menu | |
| country.kicker | cs | ok | | |
| country.contents | cs | ok | | |
| country.sources | cs | ok | | |
| section.fundamentals | cs | ok | | |
| section.holdings | cs | ok | | |
| section.exposure | cs | ok | | |
| section.posture | cs | ok | | |
| section.sizing | cs | ok | | |
| section.gaps | cs | ok | | |
| section.placement | cs | ok | | |
| overview.hosting | cs | ok | | |
| overview.coverage | cs | ok | | |
| col.indicator | cs | ok | | |
| col.value | cs | ok | | |
| col.priority | cs | ok | | |
| col.holding | cs | ok | | |
| col.register | cs | ok | | |
| col.infrastructure | cs | ok | | |
| col.holdings | cs | ok | | |
| col.dimension | cs | ok | | |
| col.position | cs | ok | | |
| col.finding | cs | ok | | |
| col.state | cs | ok | | |
| col.registers_sourced | cs | ok | | |
| col.hosting_sourced | cs | ok | | |
| fact.check_this | cs | ok | | |
| fact.gloss | cs | ok | | |
| fact.withheld | cs | ok | ICU pattern, one/few/many/other as CLDR cs; 1 hodnota zadržena, 2–4 hodnoty zadrženy, 1,5 hodnoty zadrženo (genitive sg. after a decimal), 5 hodnot zadrženo: every branch agrees | |
| fact.disputed | cs | ok | | |
| status.loading | cs | ok | | |
| status.load_error | cs | ok | | |
| notfound.title | cs | ok | | |
| notfound.back | cs | ok | | |
| notice.disclaimer | cs | ok | re-read 2026-10-20: 'zkontrolováno' for the machine, 'ověřeno' for the person; the distinction stands, nothing weakened | |
| notice.unread | cs | ok | says machine translation; 'nezkontroloval žádný člověk': checked, not verified; plain | |
