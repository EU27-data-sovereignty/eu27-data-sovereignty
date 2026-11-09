# Austria (AT): language draft

- Languages: de German (de-AT)
- Drafted by: agent A, claude-opus-5-5, 2026-10-12
- Revised by: agent A, claude-opus-5-5, 2026-10-20 (applied the review's 3 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern)
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | de |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | Souveräne Rechenzentren der EU-27 |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Überblick |
| nav.ranking | Ranking | Rangfolge |
| nav.countries | Countries | Staaten |
| nav.holdings | Critical holdings | Kritische Datenbestände |
| nav.hosting | Hosting | Hosting |
| nav.sources | Sources | Quellen |
| nav.ask | Ask | Fragen |
| nav.methodology | Methodology | Methodik |
| nav.factcheck | Fact check | Faktenprüfung |
| nav.about | About the data | Über die Daten |
| country.kicker | Country report | Länderbericht |
| country.contents | Contents | Inhalt |
| country.sources | Sources | Quellen |
| section.fundamentals | Fundamentals | Grundlagen |
| section.holdings | Critical data holdings, by priority | Kritische Datenbestände, nach Priorität |
| section.exposure | Foreign-dependency exposure | Exposition gegenüber Auslandsabhängigkeit |
| section.posture | Legal and institutional posture | Rechtliche und institutionelle Ausgangslage |
| section.sizing | Capacity | Kapazität |
| section.gaps | Research still open | Noch offene Recherchen |
| section.placement | Data-sovereignty placement | Einordnung zur Datensouveränität |
| overview.hosting | Where key registers are hosted, and by whom | Wo zentrale Register gehostet werden und von wem |
| overview.coverage | What is known, per state | Was je Staat bekannt ist |
| col.indicator | Indicator | Indikator |
| col.value | Value | Wert |
| col.priority | Priority | Priorität |
| col.holding | Holding | Datenbestand |
| col.register | Register or system | Register oder System |
| col.infrastructure | Infrastructure | Infrastruktur |
| col.holdings | Holdings | Datenbestände |
| col.dimension | Dimension | Dimension |
| col.position | Position | Position |
| col.finding | Finding | Befund |
| col.state | State | Staat |
| col.registers_sourced | Registers sourced | Register mit Quelle |
| col.hosting_sourced | Hosting sourced | Hosting mit Quelle |
| fact.check_this | Check this fact | Diese Angabe prüfen |
| fact.gloss | Machine translation: | Maschinelle Übersetzung: |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# Wert zurückgehalten, bis eine Quelle vorliegt} other {# Werte zurückgehalten, bis eine Quelle vorliegt}} |
| fact.disputed | withheld as disputed | als strittig zurückgehalten |
| status.loading | Loading the EU-27 dataset… | EU-27-Datensatz wird geladen… |
| status.load_error | Could not load the data | Die Daten konnten nicht geladen werden |
| notfound.title | Page not found | Seite nicht gefunden |
| notfound.back | Back to the overview | Zurück zum Überblick |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Maschinell geprüft, nicht von Menschen verifiziert. Automatisierte Agenten haben diese Quellen gefunden und mechanisch geprüft; kein Mensch hat die Befunde überprüft. Der englische Wortlaut einer nicht englischsprachigen Quelle ist eine maschinelle Übersetzung oder eine maschinelle Zusammenfassung des zitierten Textes. Behandeln Sie jede Angabe als Hinweis auf ihre zitierte Quelle, nicht als gesichert. Korrekturen sind über die Issue-Vorlage des Repositorys willkommen. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | Die Beschriftungen auf dieser Seite sind eine maschinelle Übersetzung. Kein Mensch, der diese Sprache liest, hat sie bisher geprüft. |

- Note: identical to the DE draft. No string in this table carries an Austrian-specific administrative term (differences such as Meldewesen arise in the facts, which are not translated here); the reviewer should say whether Austrian usage prefers Übersicht to Überblick.

## Review

- Reviewed by: agent B, claude-fable-5-1, 2026-10-12
- Re-reviewed by: agent B, claude-fable-5-1, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer)
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | de | ok | | |
| site.kicker | de | ok | | |
| nav.overview | de | ok | | |
| nav.ranking | de | ok | | |
| nav.countries | de | ok | | |
| nav.holdings | de | ok | | |
| nav.hosting | de | ok | | |
| nav.sources | de | ok | | |
| nav.ask | de | ok | | |
| nav.methodology | de | ok | | |
| nav.factcheck | de | ok | | |
| nav.about | de | ok | natural label for the menu over Quellen, Methodik, Faktenprüfung | |
| country.kicker | de | ok | | |
| country.contents | de | ok | | |
| country.sources | de | ok | | |
| section.fundamentals | de | ok | | |
| section.holdings | de | ok | | |
| section.exposure | de | ok | fix applied 2026-10-20, re-reviewed | |
| section.posture | de | ok | | |
| section.sizing | de | ok | | |
| section.gaps | de | ok | | |
| section.placement | de | ok | | |
| overview.hosting | de | ok | | |
| overview.coverage | de | ok | | |
| col.indicator | de | ok | | |
| col.value | de | ok | | |
| col.priority | de | ok | | |
| col.holding | de | ok | | |
| col.register | de | ok | | |
| col.infrastructure | de | ok | | |
| col.holdings | de | ok | | |
| col.dimension | de | ok | | |
| col.position | de | ok | | |
| col.finding | de | ok | | |
| col.state | de | ok | | |
| col.registers_sourced | de | ok | fix applied 2026-10-20, re-reviewed | |
| col.hosting_sourced | de | ok | fix applied 2026-10-20, re-reviewed | |
| fact.check_this | de | ok | | |
| fact.gloss | de | ok | | |
| fact.withheld | de | ok | ICU pattern, one/other as CLDR de; Wert / Werte agree with the count in each branch | |
| fact.disputed | de | ok | | |
| status.loading | de | ok | | |
| status.load_error | de | ok | | |
| notfound.title | de | ok | | |
| notfound.back | de | ok | | |
| notice.disclaimer | de | ok | re-read 2026-10-20: 'geprüft' for the machine, 'verifiziert' for the person; the distinction stands, nothing weakened | |
| notice.unread | de | ok | says machine translation; 'kein Mensch ... hat sie geprüft': checked, not verified; plain | |
