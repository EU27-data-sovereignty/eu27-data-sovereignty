# France (FR): language draft

- Languages: fr French (fr-FR)
- Drafted by: agent A, claude-opus-5-5, 2026-10-12
- Revised by: agent A, claude-opus-5-5, 2026-10-20 (applied the review's 1 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern)
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | fr |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | Centres de données souverains de l'EU-27 |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Vue d'ensemble |
| nav.ranking | Ranking | Classement |
| nav.countries | Countries | Pays |
| nav.holdings | Critical holdings | Patrimoine de données critiques |
| nav.hosting | Hosting | Hébergement |
| nav.sources | Sources | Sources |
| nav.ask | Ask | Interroger |
| nav.methodology | Methodology | Méthodologie |
| nav.factcheck | Fact check | Vérification des faits |
| nav.about | About the data | À propos des données |
| country.kicker | Country report | Rapport par pays |
| country.contents | Contents | Sommaire |
| country.sources | Sources | Sources |
| section.fundamentals | Fundamentals | Éléments fondamentaux |
| section.holdings | Critical data holdings, by priority | Données critiques détenues, par priorité |
| section.exposure | Foreign-dependency exposure | Exposition à la dépendance étrangère |
| section.posture | Legal and institutional posture | Situation juridique et institutionnelle |
| section.sizing | Capacity | Capacité |
| section.gaps | Research still open | Recherches encore ouvertes |
| section.placement | Data-sovereignty placement | Positionnement en matière de souveraineté des données |
| overview.hosting | Where key registers are hosted, and by whom | Où les registres clés sont hébergés, et par qui |
| overview.coverage | What is known, per state | Ce qui est connu, par État |
| col.indicator | Indicator | Indicateur |
| col.value | Value | Valeur |
| col.priority | Priority | Priorité |
| col.holding | Holding | Ensemble de données |
| col.register | Register or system | Registre ou système |
| col.infrastructure | Infrastructure | Infrastructure |
| col.holdings | Holdings | Ensembles de données |
| col.dimension | Dimension | Dimension |
| col.position | Position | Position |
| col.finding | Finding | Constat |
| col.state | State | État |
| col.registers_sourced | Registers sourced | Registres avec source |
| col.hosting_sourced | Hosting sourced | Hébergement avec source |
| fact.check_this | Check this fact | Vérifier ce fait |
| fact.gloss | Machine translation: | Traduction automatique : |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# valeur retenue en attendant une source} many {# de valeurs retenues en attendant une source} other {# valeurs retenues en attendant une source}} |
| fact.disputed | withheld as disputed | retenu car contesté |
| status.loading | Loading the EU-27 dataset… | Chargement du jeu de données EU-27… |
| status.load_error | Could not load the data | Impossible de charger les données |
| notfound.title | Page not found | Page introuvable |
| notfound.back | Back to the overview | Retour à la vue d'ensemble |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Contrôlé par machine, non vérifié par une personne. Des agents automatisés ont trouvé ces sources et les ont contrôlées mécaniquement ; aucune personne n'a examiné les constats. La formulation anglaise d'une source non anglophone est une traduction automatique ou un résumé automatique du texte cité. Considérez chaque fait comme une piste vers sa source citée, et non comme établi. Les corrections sont les bienvenues via le modèle de ticket (issue template) du dépôt. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | Les libellés de cette page sont une traduction automatique. Aucune personne qui lit cette langue ne les a encore contrôlés. |

## Review

- Reviewed by: agent B, claude-fable-5-1, 2026-10-12
- Re-reviewed by: agent B, claude-fable-5-1, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer)
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | fr | ok | | |
| site.kicker | fr | ok | | |
| nav.overview | fr | ok | | |
| nav.ranking | fr | ok | | |
| nav.countries | fr | ok | | |
| nav.holdings | fr | ok | | |
| nav.hosting | fr | ok | | |
| nav.sources | fr | ok | | |
| nav.ask | fr | ok | | |
| nav.methodology | fr | ok | | |
| nav.factcheck | fr | ok | | |
| nav.about | fr | ok | natural label for the menu | |
| country.kicker | fr | ok | | |
| country.contents | fr | ok | | |
| country.sources | fr | ok | | |
| section.fundamentals | fr | ok | | |
| section.holdings | fr | ok | | |
| section.exposure | fr | ok | | |
| section.posture | fr | ok | | |
| section.sizing | fr | ok | | |
| section.gaps | fr | ok | | |
| section.placement | fr | ok | | |
| overview.hosting | fr | ok | | |
| overview.coverage | fr | ok | | |
| col.indicator | fr | ok | | |
| col.value | fr | ok | | |
| col.priority | fr | ok | | |
| col.holding | fr | ok | | |
| col.register | fr | ok | | |
| col.infrastructure | fr | ok | | |
| col.holdings | fr | ok | | |
| col.dimension | fr | ok | | |
| col.position | fr | ok | | |
| col.finding | fr | ok | | |
| col.state | fr | ok | | |
| col.registers_sourced | fr | ok | | |
| col.hosting_sourced | fr | ok | | |
| fact.check_this | fr | ok | | |
| fact.gloss | fr | ok | | |
| fact.withheld | fr | ok | ICU pattern, one/many/other as CLDR fr; one covers 0 and 1 as French wants, many (millions) takes 'de valeurs', correct | |
| fact.disputed | fr | ok | | |
| status.loading | fr | ok | | |
| status.load_error | fr | ok | | |
| notfound.title | fr | ok | | |
| notfound.back | fr | ok | | |
| notice.disclaimer | fr | ok | fix applied 2026-10-20, re-reviewed; 'contrôlé' for the machine, 'vérifié' for the person; the distinction stands, nothing weakened | |
| notice.unread | fr | ok | says machine translation; 'aucune personne ... contrôlés': checked, not verified; plain | |
