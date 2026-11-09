# Portugal (PT): language draft

- Languages: pt Portuguese (pt-PT)
- Drafted by: agent B, claude-fable-5-1, 2026-10-12
- Revised by: agent B, claude-fable-5-1, 2026-10-20 (applied the review's 3 fixes; added nav.about and notice.unread; fact.withheld as an ICU plural pattern)
- Status: draft, machine-translated, not rendered anywhere, reviewed by a different agent

## Strings

| key | en | pt |
|---|---|---|
| site.title | EU-27 Sovereign Data Centres | Centros de dados soberanos da EU-27 |
| site.kicker | EU-27 | EU-27 |
| nav.overview | Overview | Visão geral |
| nav.ranking | Ranking | Classificação |
| nav.countries | Countries | Países |
| nav.holdings | Critical holdings | Acervos críticos |
| nav.hosting | Hosting | Alojamento |
| nav.sources | Sources | Fontes |
| nav.ask | Ask | Perguntar |
| nav.methodology | Methodology | Metodologia |
| nav.factcheck | Fact check | Verificação de factos |
| nav.about | About the data | Sobre os dados |
| country.kicker | Country report | Relatório por país |
| country.contents | Contents | Índice |
| country.sources | Sources | Fontes |
| section.fundamentals | Fundamentals | Dados fundamentais |
| section.holdings | Critical data holdings, by priority | Acervos de dados críticos, por prioridade |
| section.exposure | Foreign-dependency exposure | Exposição à dependência estrangeira |
| section.posture | Legal and institutional posture | Enquadramento jurídico e institucional |
| section.sizing | Capacity | Capacidade |
| section.gaps | Research still open | Investigação ainda em aberto |
| section.placement | Data-sovereignty placement | Posicionamento em matéria de soberania dos dados |
| overview.hosting | Where key registers are hosted, and by whom | Onde estão alojados os registos essenciais, e por quem |
| overview.coverage | What is known, per state | O que se sabe, por Estado |
| col.indicator | Indicator | Indicador |
| col.value | Value | Valor |
| col.priority | Priority | Prioridade |
| col.holding | Holding | Acervo |
| col.register | Register or system | Registo ou sistema |
| col.infrastructure | Infrastructure | Infraestrutura |
| col.holdings | Holdings | Acervos |
| col.dimension | Dimension | Dimensão |
| col.position | Position | Posição |
| col.finding | Finding | Constatação |
| col.state | State | Estado |
| col.registers_sourced | Registers sourced | Registos com fonte |
| col.hosting_sourced | Hosting sourced | Alojamento com fonte |
| fact.check_this | Check this fact | Verificar este facto |
| fact.gloss | Machine translation: | Tradução automática: |
| fact.withheld | {count, plural, one {# value withheld until sourced} other {# values withheld until sourced}} | {count, plural, one {# valor retido até ter fonte} many {# valores retidos até terem fonte} other {# valores retidos até terem fonte}} |
| fact.disputed | withheld as disputed | retido por ser contestado |
| status.loading | Loading the EU-27 dataset… | A carregar o conjunto de dados EU-27… |
| status.load_error | Could not load the data | Não foi possível carregar os dados |
| notfound.title | Page not found | Página não encontrada |
| notfound.back | Back to the overview | Voltar à visão geral |
| notice.disclaimer | Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. | Controlado por máquina, não verificado por pessoas. Agentes automatizados encontraram estas fontes e controlaram-nas mecanicamente; nenhuma pessoa reviu as constatações. A redação em inglês de uma fonte noutra língua é uma tradução automática ou um resumo automático do texto citado. Trate cada facto como uma pista para a fonte citada, não como estabelecido. As correções são bem-vindas através do modelo de issues do repositório. |
| notice.unread | The labels on this page are a machine translation. No person who reads this language has checked them yet. | As etiquetas desta página são uma tradução automática. Nenhuma pessoa que leia esta língua as conferiu ainda. |

- Note: pt is European Portuguese: "alojamento" (not Brazilian "hospedagem"), "registo"/"facto" (not "registro"/"fato").

## Review

- Reviewed by: agent A, claude-opus-5-5, 2026-10-12
- Re-reviewed by: agent A, claude-opus-5-5, 2026-10-20 (applied fixes, fact.withheld, nav.about, notice.unread, every disclaimer)
- Verdict: 47 ok, 0 fix

| key | lang | verdict | note | suggested |
|---|---|---|---|---|
| site.title | pt | ok | | |
| site.kicker | pt | ok | | |
| nav.overview | pt | ok | | |
| nav.ranking | pt | ok | | |
| nav.countries | pt | ok | | |
| nav.holdings | pt | ok | | |
| nav.hosting | pt | ok | | |
| nav.sources | pt | ok | | |
| nav.ask | pt | ok | | |
| nav.methodology | pt | ok | | |
| nav.factcheck | pt | ok | | |
| nav.about | pt | ok | idiomatic menu label for 'About the data' | |
| country.kicker | pt | ok | | |
| country.contents | pt | ok | | |
| country.sources | pt | ok | | |
| section.fundamentals | pt | ok | | |
| section.holdings | pt | ok | | |
| section.exposure | pt | ok | | |
| section.posture | pt | ok | | |
| section.sizing | pt | ok | | |
| section.gaps | pt | ok | | |
| section.placement | pt | ok | fix applied 2026-10-20, re-reviewed | |
| overview.hosting | pt | ok | | |
| overview.coverage | pt | ok | | |
| col.indicator | pt | ok | | |
| col.value | pt | ok | | |
| col.priority | pt | ok | | |
| col.holding | pt | ok | | |
| col.register | pt | ok | | |
| col.infrastructure | pt | ok | | |
| col.holdings | pt | ok | | |
| col.dimension | pt | ok | | |
| col.position | pt | ok | | |
| col.finding | pt | ok | | |
| col.state | pt | ok | | |
| col.registers_sourced | pt | ok | | |
| col.hosting_sourced | pt | ok | | |
| fact.check_this | pt | ok | | |
| fact.gloss | pt | ok | | |
| fact.withheld | pt | ok | one/many/other; under pt-PT 0 selects other, so '0 valores retidos' | |
| fact.disputed | pt | ok | fix applied 2026-10-20, re-reviewed | |
| status.loading | pt | ok | | |
| status.load_error | pt | ok | | |
| notfound.title | pt | ok | | |
| notfound.back | pt | ok | | |
| notice.disclaimer | pt | ok | fix applied 2026-10-20, re-reviewed | |
| notice.unread | pt | ok | says plainly it is a machine translation and that no reader of the language has checked it; no verified/approved word | |
