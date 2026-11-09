# Croatia (HR): language draft

- Languages: hr Croatian (hr-HR)
- Drafted by: agent A, claude-opus-5-5, 2026-10-12
- Revised by: agent A, claude-opus-5-5, 2026-10-20 (applied the review's 0 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern); 2026-10-20 round 3: applied 1 fix
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | hr |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | Suvereni podatkovni centri EU-27 |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Pregled |
| nav.ranking | Ranking | Poredak |
| nav.countries | Countries | Države |
| nav.holdings | Critical holdings | Kritične zbirke podataka |
| nav.hosting | Hosting | Udomljavanje |
| nav.sources | Sources | Izvori |
| nav.ask | Ask | Pitajte |
| nav.methodology | Methodology | Metodologija |
| nav.factcheck | Fact check | Provjera činjenica |
| nav.about | About the data | O podacima |
| country.kicker | Country report | Izvješće o državi |
| country.contents | Contents | Sadržaj |
| country.sources | Sources | Izvori |
| section.fundamentals | Fundamentals | Osnovni podaci |
| section.holdings | Critical data holdings, by priority | Kritične zbirke podataka, prema prioritetu |
| section.exposure | Foreign-dependency exposure | Izloženost ovisnosti o inozemstvu |
| section.posture | Legal and institutional posture | Pravni i institucionalni položaj |
| section.sizing | Capacity | Kapacitet |
| section.gaps | Research still open | Još otvorena istraživanja |
| section.placement | Data-sovereignty placement | Položaj u pogledu suverenosti podataka |
| overview.hosting | Where key registers are hosted, and by whom | Gdje su ključni registri udomljeni i tko ih udomljuje |
| overview.coverage | What is known, per state | Što je poznato, po državi |
| col.indicator | Indicator | Pokazatelj |
| col.value | Value | Vrijednost |
| col.priority | Priority | Prioritet |
| col.holding | Holding | Zbirka podataka |
| col.register | Register or system | Registar ili sustav |
| col.infrastructure | Infrastructure | Infrastruktura |
| col.holdings | Holdings | Zbirke podataka |
| col.dimension | Dimension | Dimenzija |
| col.position | Position | Položaj |
| col.finding | Finding | Nalaz |
| col.state | State | Država |
| col.registers_sourced | Registers sourced | Registri s izvorom |
| col.hosting_sourced | Hosting sourced | Udomljavanje s izvorom |
| fact.check_this | Check this fact | Provjerite ovu činjenicu |
| fact.gloss | Machine translation: | Strojni prijevod: |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# vrijednost zadržana dok se ne pronađe izvor} few {# vrijednosti zadržane dok se ne pronađe izvor} other {# vrijednosti zadržano dok se ne pronađe izvor}} |
| fact.disputed | withheld as disputed | zadržano kao sporno |
| status.loading | Loading the EU-27 dataset… | Učitavanje skupa podataka EU-27… |
| status.load_error | Could not load the data | Podaci se nisu mogli učitati |
| notfound.title | Page not found | Stranica nije pronađena |
| notfound.back | Back to the overview | Natrag na pregled |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Strojno provjereno, bez ljudske potvrde. Automatizirani agenti pronašli su ove izvore i mehanički ih provjerili; nijedna osoba nije pregledala nalaze. Engleski tekst izvora koji nije na engleskom jeziku strojni je prijevod ili strojni sažetak citiranog teksta. Svaku činjenicu smatrajte uputom na njezin citirani izvor, a ne utvrđenom. Ispravci su dobrodošli putem predloška za prijavu problema (issue template) u repozitoriju. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | Oznake na ovoj stranici strojni su prijevod. Još ih nije pregledala nijedna osoba koja čita ovaj jezik. |

## Review

- Reviewed by: agent B, claude-fable-5-1, 2026-10-12
- Re-reviewed by: agent B, claude-fable-5-1, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer); round 4: 3 fixes re-reviewed
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | hr | ok | | |
| site.kicker | hr | ok | | |
| nav.overview | hr | ok | | |
| nav.ranking | hr | ok | | |
| nav.countries | hr | ok | | |
| nav.holdings | hr | ok | | |
| nav.hosting | hr | ok | | |
| nav.sources | hr | ok | | |
| nav.ask | hr | ok | | |
| nav.methodology | hr | ok | | |
| nav.factcheck | hr | ok | | |
| nav.about | hr | ok | natural label for the menu | |
| country.kicker | hr | ok | | |
| country.contents | hr | ok | | |
| country.sources | hr | ok | | |
| section.fundamentals | hr | ok | | |
| section.holdings | hr | ok | | |
| section.exposure | hr | ok | | |
| section.posture | hr | ok | | |
| section.sizing | hr | ok | | |
| section.gaps | hr | ok | | |
| section.placement | hr | ok | | |
| overview.hosting | hr | ok | | |
| overview.coverage | hr | ok | | |
| col.indicator | hr | ok | | |
| col.value | hr | ok | | |
| col.priority | hr | ok | | |
| col.holding | hr | ok | | |
| col.register | hr | ok | | |
| col.infrastructure | hr | ok | | |
| col.holdings | hr | ok | | |
| col.dimension | hr | ok | | |
| col.position | hr | ok | | |
| col.finding | hr | ok | | |
| col.state | hr | ok | | |
| col.registers_sourced | hr | ok | | |
| col.hosting_sourced | hr | ok | | |
| fact.check_this | hr | ok | | |
| fact.gloss | hr | ok | | |
| fact.withheld | hr | ok | ICU pattern, one/few/other as CLDR hr; 1 (21, 31) vrijednost zadržana, 2–4 vrijednosti zadržane, 5+ vrijednosti zadržano (gen. pl. with neuter predicate): every branch agrees | |
| fact.disputed | hr | ok | | |
| status.loading | hr | ok | | |
| status.load_error | hr | ok | | |
| notfound.title | hr | ok | | |
| notfound.back | hr | ok | | |
| notice.disclaimer | hr | ok | fix applied 2026-10-20 round 3, re-reviewed | |
| notice.unread | hr | ok | says machine translation; 'nijedna osoba ... pregledala': reviewed, not verified; plain | |
