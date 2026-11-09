# Estonia (EE): language draft

- Languages: et Estonian (et-EE)
- Drafted by: agent A, claude-opus-5-5, 2026-10-12
- Revised by: agent A, claude-opus-5-5, 2026-10-20 (applied the review's 0 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern)
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | et |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | EU-27 suveräänsed andmekeskused |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Ülevaade |
| nav.ranking | Ranking | Järjestus |
| nav.countries | Countries | Riigid |
| nav.holdings | Critical holdings | Kriitilised andmekogud |
| nav.hosting | Hosting | Majutus |
| nav.sources | Sources | Allikad |
| nav.ask | Ask | Küsi |
| nav.methodology | Methodology | Metoodika |
| nav.factcheck | Fact check | Faktikontroll |
| nav.about | About the data | Andmetest |
| country.kicker | Country report | Riigi aruanne |
| country.contents | Contents | Sisukord |
| country.sources | Sources | Allikad |
| section.fundamentals | Fundamentals | Põhiandmed |
| section.holdings | Critical data holdings, by priority | Kriitilised andmekogud prioriteedi järgi |
| section.exposure | Foreign-dependency exposure | Avatus välissõltuvusele |
| section.posture | Legal and institutional posture | Õiguslik ja institutsionaalne olukord |
| section.sizing | Capacity | Maht |
| section.gaps | Research still open | Veel avatud uurimistöö |
| section.placement | Data-sovereignty placement | Paigutus andmesuveräänsuse alusel |
| overview.hosting | Where key registers are hosted, and by whom | Kus peamisi registreid majutatakse ja kes neid majutab |
| overview.coverage | What is known, per state | Mis on teada, riigiti |
| col.indicator | Indicator | Näitaja |
| col.value | Value | Väärtus |
| col.priority | Priority | Prioriteet |
| col.holding | Holding | Andmekogu |
| col.register | Register or system | Register või süsteem |
| col.infrastructure | Infrastructure | Taristu |
| col.holdings | Holdings | Andmekogud |
| col.dimension | Dimension | Mõõde |
| col.position | Position | Positsioon |
| col.finding | Finding | Leid |
| col.state | State | Riik |
| col.registers_sourced | Registers sourced | Allikaga registrid |
| col.hosting_sourced | Hosting sourced | Allikaga majutus |
| fact.check_this | Check this fact | Kontrolli seda fakti |
| fact.gloss | Machine translation: | Masintõlge: |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# väärtus avaldamata, kuni allikas on olemas} other {# väärtust avaldamata, kuni allikas on olemas}} |
| fact.disputed | withheld as disputed | avaldamata kui vaidlustatud |
| status.loading | Loading the EU-27 dataset… | EU-27 andmestiku laadimine… |
| status.load_error | Could not load the data | Andmeid ei õnnestunud laadida |
| notfound.title | Page not found | Lehte ei leitud |
| notfound.back | Back to the overview | Tagasi ülevaatesse |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Masinkontrollitud, inimese poolt kinnitamata. Automatiseeritud agendid leidsid need allikad ja kontrollisid neid mehaaniliselt; ükski inimene ei ole leide üle vaadanud. Mitteingliskeelse allika ingliskeelne sõnastus on tsiteeritud teksti masintõlge või masinkokkuvõte. Käsitle iga fakti kui juhatust selle viidatud allikani, mitte kui tõendatut. Parandused on teretulnud repositooriumi probleemiteate malli (issue template) kaudu. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | Selle lehe sildid on masintõlge. Ükski inimene, kes seda keelt loeb, ei ole neid veel üle vaadanud. |

## Review

- Reviewed by: agent B, claude-fable-5-1, 2026-10-12
- Re-reviewed by: agent B, claude-fable-5-1, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer)
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | et | ok | | |
| site.kicker | et | ok | | |
| nav.overview | et | ok | | |
| nav.ranking | et | ok | | |
| nav.countries | et | ok | | |
| nav.holdings | et | ok | | |
| nav.hosting | et | ok | | |
| nav.sources | et | ok | | |
| nav.ask | et | ok | | |
| nav.methodology | et | ok | | |
| nav.factcheck | et | ok | | |
| nav.about | et | ok | elative 'Andmetest' is the idiomatic Estonian 'about the data' | |
| country.kicker | et | ok | | |
| country.contents | et | ok | | |
| country.sources | et | ok | | |
| section.fundamentals | et | ok | | |
| section.holdings | et | ok | | |
| section.exposure | et | ok | | |
| section.posture | et | ok | | |
| section.sizing | et | ok | | |
| section.gaps | et | ok | | |
| section.placement | et | ok | | |
| overview.hosting | et | ok | | |
| overview.coverage | et | ok | | |
| col.indicator | et | ok | | |
| col.value | et | ok | | |
| col.priority | et | ok | | |
| col.holding | et | ok | | |
| col.register | et | ok | | |
| col.infrastructure | et | ok | | |
| col.holdings | et | ok | | |
| col.dimension | et | ok | | |
| col.position | et | ok | | |
| col.finding | et | ok | | |
| col.state | et | ok | | |
| col.registers_sourced | et | ok | | |
| col.hosting_sourced | et | ok | | |
| fact.check_this | et | ok | | |
| fact.gloss | et | ok | | |
| fact.withheld | et | ok | ICU pattern, one/other as CLDR et; nominative väärtus after 1, partitive väärtust after other counts, correct | |
| fact.disputed | et | ok | | |
| status.loading | et | ok | | |
| status.load_error | et | ok | | |
| notfound.title | et | ok | | |
| notfound.back | et | ok | | |
| notice.disclaimer | et | ok | re-read 2026-10-20: 'kontrollitud' for the machine, 'kinnitamata' for the person; the distinction stands, nothing weakened | |
| notice.unread | et | ok | says machine translation; 'ükski inimene ... üle vaadanud': looked over, not verified; plain | |
