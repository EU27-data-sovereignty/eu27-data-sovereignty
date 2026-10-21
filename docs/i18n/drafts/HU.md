# Hungary (HU): language draft

- Languages: hu Hungarian (hu-HU)
- Drafted by: agent A, claude-opus-5-5, 2026-10-12
- Revised by: agent A, claude-opus-5-5, 2026-10-20 (applied the review's 0 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern); 2026-10-20 round 3: applied 1 fix
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | hu |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | Az EU-27 szuverén adatközpontjai |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Áttekintés |
| nav.ranking | Ranking | Rangsor |
| nav.countries | Countries | Országok |
| nav.holdings | Critical holdings | Kritikus adatvagyon |
| nav.hosting | Hosting | Tárhelyszolgáltatás |
| nav.sources | Sources | Források |
| nav.ask | Ask | Kérdezzen |
| nav.methodology | Methodology | Módszertan |
| nav.factcheck | Fact check | Tényellenőrzés |
| nav.about | About the data | Az adatokról |
| country.kicker | Country report | Országjelentés |
| country.contents | Contents | Tartalom |
| country.sources | Sources | Források |
| section.fundamentals | Fundamentals | Alapadatok |
| section.holdings | Critical data holdings, by priority | Kritikus adatvagyon, prioritás szerint |
| section.exposure | Foreign-dependency exposure | Külföldi függőségnek való kitettség |
| section.posture | Legal and institutional posture | Jogi és intézményi helyzet |
| section.sizing | Capacity | Kapacitás |
| section.gaps | Research still open | Még lezáratlan kutatás |
| section.placement | Data-sovereignty placement | Besorolás az adatszuverenitás szempontjából |
| overview.hosting | Where key registers are hosted, and by whom | Hol és kinél vannak elhelyezve a kulcsfontosságú nyilvántartások |
| overview.coverage | What is known, per state | Mi ismert államonként |
| col.indicator | Indicator | Mutató |
| col.value | Value | Érték |
| col.priority | Priority | Prioritás |
| col.holding | Holding | Adatállomány |
| col.register | Register or system | Nyilvántartás vagy rendszer |
| col.infrastructure | Infrastructure | Infrastruktúra |
| col.holdings | Holdings | Adatállományok |
| col.dimension | Dimension | Dimenzió |
| col.position | Position | Helyzet |
| col.finding | Finding | Megállapítás |
| col.state | State | Állam |
| col.registers_sourced | Registers sourced | Forrással igazolt nyilvántartások |
| col.hosting_sourced | Hosting sourced | Forrással igazolt tárhely |
| fact.check_this | Check this fact | Ellenőrizze ezt a tényt |
| fact.gloss | Machine translation: | Gépi fordítás: |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# érték visszatartva, amíg nincs forrás} other {# érték visszatartva, amíg nincs forrás}} |
| fact.disputed | withheld as disputed | vitatottként visszatartva |
| status.loading | Loading the EU-27 dataset… | Az EU-27 adatkészlet betöltése… |
| status.load_error | Could not load the data | Az adatokat nem sikerült betölteni |
| notfound.title | Page not found | Az oldal nem található |
| notfound.back | Back to the overview | Vissza az áttekintéshez |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Gépileg ellenőrizve, ember által nem igazolva. Automatizált ágensek találták meg ezeket a forrásokat, és mechanikusan ellenőrizték őket; egyetlen ember sem vizsgálta át a megállapításokat. Egy nem angol nyelvű forrás angol nyelvű szövege az idézett szöveg gépi fordítása vagy gépi összefoglalása. Minden tényt a hivatkozott forrására mutató nyomként kezeljen, ne megalapozott tényként. A javításokat szívesen fogadjuk az adattár (repository) hibajegysablonján (issue template) keresztül. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | Az oldalon látható feliratok gépi fordítás eredményei. Még egyetlen olyan ember sem nézte át őket, aki ezt a nyelvet olvassa. |

## Review

- Reviewed by: agent B, claude-fable-5-1, 2026-10-12
- Re-reviewed by: agent B, claude-fable-5-1, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer); round 4: 3 fixes re-reviewed
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | hu | ok | | |
| site.kicker | hu | ok | | |
| nav.overview | hu | ok | | |
| nav.ranking | hu | ok | | |
| nav.countries | hu | ok | | |
| nav.holdings | hu | ok | | |
| nav.hosting | hu | ok | | |
| nav.sources | hu | ok | | |
| nav.ask | hu | ok | | |
| nav.methodology | hu | ok | | |
| nav.factcheck | hu | ok | | |
| nav.about | hu | ok | natural label for the menu | |
| country.kicker | hu | ok | | |
| country.contents | hu | ok | | |
| country.sources | hu | ok | | |
| section.fundamentals | hu | ok | | |
| section.holdings | hu | ok | | |
| section.exposure | hu | ok | | |
| section.posture | hu | ok | | |
| section.sizing | hu | ok | | |
| section.gaps | hu | ok | | |
| section.placement | hu | ok | | |
| overview.hosting | hu | ok | | |
| overview.coverage | hu | ok | | |
| col.indicator | hu | ok | | |
| col.value | hu | ok | | |
| col.priority | hu | ok | | |
| col.holding | hu | ok | | |
| col.register | hu | ok | | |
| col.infrastructure | hu | ok | | |
| col.holdings | hu | ok | | |
| col.dimension | hu | ok | | |
| col.position | hu | ok | | |
| col.finding | hu | ok | | |
| col.state | hu | ok | | |
| col.registers_sourced | hu | ok | | |
| col.hosting_sourced | hu | ok | | |
| fact.check_this | hu | ok | | |
| fact.gloss | hu | ok | | |
| fact.withheld | hu | ok | ICU pattern, one/other as CLDR hu; both branches identical, which is right since Hungarian keeps the noun singular after a numeral | |
| fact.disputed | hu | ok | | |
| status.loading | hu | ok | | |
| status.load_error | hu | ok | | |
| notfound.title | hu | ok | | |
| notfound.back | hu | ok | | |
| notice.disclaimer | hu | ok | re-read 2026-10-20: 'ellenőrizve' for the machine, 'igazolva' for the person; the distinction stands, nothing weakened | |
| notice.unread | hu | ok | fix applied 2026-10-20 round 3, re-reviewed | |
