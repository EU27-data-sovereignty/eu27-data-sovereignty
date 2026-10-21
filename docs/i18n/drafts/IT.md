# Italy (IT): language draft

- Languages: it Italian (it-IT)
- Drafted by: agent B, claude-fable-5-1, 2026-10-12
- Revised by: agent B, claude-fable-5-1, 2026-10-20 (applied the review's 2 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern); 2026-10-20 round 3: applied 1 fix
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | it |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | Centri dati sovrani EU-27 |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Panoramica |
| nav.ranking | Ranking | Classifica |
| nav.countries | Countries | Paesi |
| nav.holdings | Critical holdings | Patrimoni critici |
| nav.hosting | Hosting | Hosting |
| nav.sources | Sources | Fonti |
| nav.ask | Ask | Chiedi |
| nav.methodology | Methodology | Metodologia |
| nav.factcheck | Fact check | Verifica dei fatti |
| nav.about | About the data | Informazioni sui dati |
| country.kicker | Country report | Rapporto per paese |
| country.contents | Contents | Indice |
| country.sources | Sources | Fonti |
| section.fundamentals | Fundamentals | Dati fondamentali |
| section.holdings | Critical data holdings, by priority | Patrimoni di dati critici, per priorità |
| section.exposure | Foreign-dependency exposure | Esposizione alla dipendenza estera |
| section.posture | Legal and institutional posture | Assetto giuridico e istituzionale |
| section.sizing | Capacity | Capacità |
| section.gaps | Research still open | Ricerca ancora aperta |
| section.placement | Data-sovereignty placement | Collocazione in materia di sovranità dei dati |
| overview.hosting | Where key registers are hosted, and by whom | Dove sono ospitati i registri chiave, e da chi |
| overview.coverage | What is known, per state | Cosa si sa, per Stato |
| col.indicator | Indicator | Indicatore |
| col.value | Value | Valore |
| col.priority | Priority | Priorità |
| col.holding | Holding | Patrimonio |
| col.register | Register or system | Registro o sistema |
| col.infrastructure | Infrastructure | Infrastruttura |
| col.holdings | Holdings | Patrimoni |
| col.dimension | Dimension | Dimensione |
| col.position | Position | Posizione |
| col.finding | Finding | Risultato |
| col.state | State | Stato |
| col.registers_sourced | Registers sourced | Registri con fonte |
| col.hosting_sourced | Hosting sourced | Hosting con fonte |
| fact.check_this | Check this fact | Verifica questo fatto |
| fact.gloss | Machine translation: | Traduzione automatica: |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# valore omesso in attesa di fonte} many {# valori omessi in attesa di fonte} other {# valori omessi in attesa di fonte}} |
| fact.disputed | withheld as disputed | omesso perché contestato |
| status.loading | Loading the EU-27 dataset… | Caricamento del set di dati EU-27… |
| status.load_error | Could not load the data | Impossibile caricare i dati |
| notfound.title | Page not found | Pagina non trovata |
| notfound.back | Back to the overview | Torna alla panoramica |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Controllato automaticamente, non verificato da persone. Agenti automatizzati hanno individuato queste fonti e le hanno controllate meccanicamente; nessuna persona ha esaminato i risultati. La formulazione in inglese di una fonte non in inglese è una traduzione automatica o un riassunto automatico del testo citato. Si consideri ogni fatto come un indizio verso la fonte citata, non come accertato. Le correzioni sono benvenute tramite il modulo per le segnalazioni del repository. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | Le etichette di questa pagina sono una traduzione automatica. Nessuna persona che legge questa lingua le ha ancora controllate. |

## Review

- Reviewed by: agent A, claude-opus-5-5, 2026-10-12
- Re-reviewed by: agent A, claude-opus-5-5, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer); round 4: 3 fixes re-reviewed
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | it | ok | | |
| site.kicker | it | ok | | |
| nav.overview | it | ok | | |
| nav.ranking | it | ok | | |
| nav.countries | it | ok | | |
| nav.holdings | it | ok | | |
| nav.hosting | it | ok | | |
| nav.sources | it | ok | | |
| nav.ask | it | ok | | |
| nav.methodology | it | ok | | |
| nav.factcheck | it | ok | | |
| nav.about | it | ok | fix applied 2026-10-20 round 3, re-reviewed | |
| country.kicker | it | ok | | |
| country.contents | it | ok | | |
| country.sources | it | ok | | |
| section.fundamentals | it | ok | | |
| section.holdings | it | ok | | |
| section.exposure | it | ok | | |
| section.posture | it | ok | | |
| section.sizing | it | ok | | |
| section.gaps | it | ok | | |
| section.placement | it | ok | fix applied 2026-10-20, re-reviewed | |
| overview.hosting | it | ok | | |
| overview.coverage | it | ok | | |
| col.indicator | it | ok | | |
| col.value | it | ok | | |
| col.priority | it | ok | | |
| col.holding | it | ok | | |
| col.register | it | ok | | |
| col.infrastructure | it | ok | | |
| col.holdings | it | ok | | |
| col.dimension | it | ok | | |
| col.position | it | ok | | |
| col.finding | it | ok | | |
| col.state | it | ok | | |
| col.registers_sourced | it | ok | | |
| col.hosting_sourced | it | ok | | |
| fact.check_this | it | ok | | |
| fact.gloss | it | ok | | |
| fact.withheld | it | ok | one/many/other; singular and plural agree with omesso/omessi (many is reached only at millions) | |
| fact.disputed | it | ok | | |
| status.loading | it | ok | | |
| status.load_error | it | ok | | |
| notfound.title | it | ok | | |
| notfound.back | it | ok | | |
| notice.disclaimer | it | ok | fix applied 2026-10-20, re-reviewed | |
| notice.unread | it | ok | says plainly it is a machine translation and that no reader of the language has checked it; no verified/approved word | |
