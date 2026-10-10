# National AI strategies for the EU-27: a foundation model good enough for each state's citizens

**Authored note, 2026-10-10. Not generated, and not part of the model, the JSON bundle, the web app, the PDFs or
`/ask`.** `run.sh data` never touches it. It is held to the standard of `countries/NL/FRONTIER-MODEL.md` (#44), not
to the standard of the model's printed facts: every factual claim below carries the URL it was read from and the
access date, and a claim that could not be confirmed from a fetched page is marked **[unverified]**. The strategy
in each entry is the author's analysis and says so. Nothing here has been machine-checked by the project's evidence
pipeline (#82, #87) or verified by a person. Decision #101 records why it is written this way.

**It ranks nothing.** States are grouped near the end by the route recommended for them; inside a group they are
alphabetical and the order carries no meaning (#10, #77). It gives no per-state cost or capacity figure (#72, #73).
The one table of cost and time bands is per route, given once, and labelled reconstructed.

**The question.** *What would give each member state a foundation AI model that is good enough for its citizens,
and what is the shortest defensible path to it?* Not frontier parity, which `FRONTIER-MODEL.md` §4 shows is out of
reach for any state alone and is the wrong goal even where it is not.

---

## Contents

- [1. The bar: what "good enough for citizens" means](#1-the-bar-what-good-enough-for-citizens-means)
- [2. The routes](#2-the-routes)
- [3. The building blocks, and how to read an entry](#3-the-building-blocks-and-how-to-read-an-entry)
- [4. The EU vehicles](#4-the-eu-vehicles)
- [5. The twenty-seven](#5-the-twenty-seven)
- [6. Across the EU-27](#6-across-the-eu-27)
- [7. Caveats](#7-caveats)
- [8. Status and next steps](#8-status-and-next-steps)
- [Sources](#sources)

---

## 1. The bar: what "good enough for citizens" means

A model is good enough for a state's citizens when a public body can put it in front of them, in their language, for
the things they come to the state for, and keep it there. That is a testable bar, and every property below can be
checked without reference to any other state or any frontier leaderboard.

| # | Property | What it means in practice | How to test it |
|---|---|---|---|
| B1 | **Works in every official language** | Reads, writes and reasons in each official language of the state, and in each regional or minority language the state recognises in law, at a quality a native speaker of that language accepts for administrative text. Not translated from English on the way in and out. | A held-out national evaluation set per language, written by the state's own language institute, scored by people who speak it. |
| B2 | **Deployable by public services under national and EU law** | Can run where the state's rules let government data run (its own data centres, a certified EU provider, or a national or EuroHPC system), under GDPR, the AI Act's obligations for public-sector use, and the state's own classification rules. | The hosting is listed in the state's own register of approved environments; a data-protection impact assessment exists; the AI Act obligations are assigned to a named body. |
| B3 | **Continuity the state controls** | The weights, the tokenizer, the training recipe and the evaluation sets are in the state's possession or escrowed under its law, with the right to keep using, modifying and serving them if every supplier walks away. | The state can demonstrate a re-deployment from its own copy without any supplier's cooperation. |
| B4 | **Provenance the state can defend** | The state knows what the model was trained on, can answer a rights-holder or a court about it, and can remove data it was not entitled to use from the next version. | A data register for the national corpus, with licence and source per item; a documented retraining path. |
| B5 | **A cost the state can carry indefinitely** | The annual operating cost (serving, refresh training, the team) is a line a ministry can defend every year, not a one-off project that leaves a model nobody can afford to update. | A five-year operating budget approved by the funding ministry, not a project grant. |
| B6 | **Evaluation owned nationally** | The state, not a supplier, defines what "good in our language, for our administration, our courts and our health system" means, and measures every candidate the same way. | A published national evaluation suite, versioned, with results for the state's own model and for the procured alternatives. |

**What the bar does not require.** It does not require the model to be trained from scratch by the state. It does not
require the model to be the best in the world, or in Europe, or even the best in its own language, as long as it
meets B1. It does not require frontier-scale compute, a national training cluster, or a national AI laboratory. It
does not require that citizens never use a foreign model; it requires that the state is never *dependent* on one for
the services it owes them. B3 is the sovereignty property that matters; B1 and B6 are what make it worth having.

**Why this bar and not "a national model".** `FRONTIER-MODEL.md` §3 separates three things that public debate
conflates: a model that is *good in the national language*, a model the state *owns*, and a model the state can
*govern* inside its jurisdiction. The bar above asks for all three at a modest scale, which every member state can
reach, instead of any of them at frontier scale, which none can reach alone.

## 2. The routes

Four routes lead to the bar. They are not exclusive: most states should take two, and every state should take R4 as
the complement to whichever of the first three it chooses. The routes generalise the three tiers of
`FRONTIER-MODEL.md` §4; the NL figures there are not reused for any other state (#72).

### R1 · Adapt: continue-pretrain and tune an open-weight base on a national corpus

**What it is.** Take a permissively licensed open-weight base model whose licence allows modification and public-sector
use, continue pretraining it on the state's curated national corpus so that the national language and
administrative register are strong, instruction-tune it on national public-service tasks, evaluate it against B1
and B6, and serve it on infrastructure that satisfies B2.

**What it needs.** A curated, rights-cleared national corpus (B4); rented or shared accelerator time measured in
weeks, not years; a standing team of a few dozen people (data, training, evaluation, serving); a licence review of
the base model; an evaluation suite (B6). It does not need a national cluster: EuroHPC AI access calls and AI
Factories exist for exactly this (section 4).

**What it buys.** Jurisdictional control and continuity over the *adapted* weights (B3, for the state's copy),
strong national-language quality (B1), a deployable model inside months rather than years, and the institutional
capability (team, corpus, evaluation) that every later route reuses.

**What it does not buy.** Independence from the upstream base model's existence and licence terms. If the base's
licence changes for future versions, the state keeps what it has and loses the upgrade path. That is a bounded
risk, and the reason to prefer bases with open licences and more than one supplier.

**European examples.** Most of the national models in section 5 that exist today took this route for at least one of
their releases; the entries name them.

### R2 · Pool: a shared model with the language community or through an EU vehicle

**What it is.** Join or lead a programme that trains a multilingual model covering the state's language(s) together
with others: a language-community programme (states sharing a language, or a regional group), or an EU vehicle
(an AI Factory's model programme, the Commission's Large AI Grand Challenge consortium, OpenEuroLLM, or a
EuroHPC-funded project). The state contributes corpus, evaluation and a share of the cost; it negotiates rights to
the weights and to continue training them.

**What it needs.** A partner that already has or is building the programme; a negotiated agreement that gives the
state possession of the weights, a continuation right and an exit (B3); the same corpus and evaluation work as R1
(B1, B4, B6); a seat in governance.

**What it buys.** A model trained on far more compute and data than the state could fund alone, at a fraction of the
cost; coverage of a small language that no commercial supplier will prioritise; a standing relationship with the
people who operate large training runs.

**What it does not buy.** Control of the roadmap. A pooled model is released when the consortium releases it, and
a small partner's language gets the weight the consortium gives it. Without the rights negotiated up front, pooling
is a nominal partnership that leaves the state exactly as dependent as before; `Netherlands_AI_strategy.md` in the
companion project calls this the principal risk of co-development.

### R3 · Build: a national mid-scale pretraining programme

**What it is.** A standing national organisation that pretrains its own models from scratch, in the 10–100 billion
parameter class, on sustained training compute the state controls or has reserved, with the national language(s)
heavily weighted in a multilingual corpus.

**What it needs.** All four binding inputs at once: a corpus large enough to justify pretraining (a language with
tens of millions of speakers, or a multilingual design that borrows from others); sustained training compute, which
means firm grid capacity and multi-year reserved time on a large cluster, national or EuroHPC; a team of one to two
hundred including people who have operated a large training run; and money as a recurring budget line, not a grant,
because the fleet depreciates in three to four years (`FRONTIER-MODEL.md` §3, §6).

**What it buys.** Full control of the recipe and the roadmap, a renewable national capability, and a seat at the
table in every European programme. Models that trail the frontier by a year or two, permanently.

**What it does not buy.** Frontier parity. `FRONTIER-MODEL.md` §4 and §6 make the case that a permanently trailing
national model can be worse than none, because it creates a constituency for mandating its own use. R3 is justified
only where the corpus, the compute, the talent and the money all exist and the state wants the capability for its
own sake, not as a way to reach the bar, which R1 and R2 reach sooner and cheaper.

### R4 · Procure with terms: frontier access as the complement

**What it is.** Buy access to frontier models for the tasks the national model cannot do, under contract terms that
keep the state within the bar: hosting in an environment that satisfies B2, continuity guarantees, weight escrow or
a fallback model the state possesses, price-change protection, and the right to evaluate every version against the
national suite (B6).

**What it needs.** A procurement vehicle, usually a framework agreement; a legal and technical team that can write
and verify the terms; the national evaluation suite, so the state knows what it is buying.

**What it buys.** The best available capability for citizens today, without any training programme. The terms,
not the model, are what deliver sovereignty here; `FRONTIER-MODEL.md` §5 argues that well-written terms buy more
security per euro than a domestic frontier run.

**What it does not buy.** A model the state owns. R4 alone fails B3. It is the complement to R1, R2 or R3, never a
substitute.

### Cost and time bands, per route

Reconstructed order-of-magnitude bands for a programme that reaches the bar, given once for all states. They are not
sourced and are not per state; a state's own number depends on its language, its existing assets and what it
already pays for compute and people. They are labelled **[reconstructed]** so that no reader takes them for a
finding.

| Route | Time to a deployable model | Order of cost | What dominates the cost | Depreciates |
|---|---|---|---|---|
| R1 Adapt | 6–18 months **[reconstructed]** | low tens of millions of euro over two years, then a few million a year **[reconstructed]** | the team and the corpus; rented compute is weeks of accelerator time | slowly: the corpus and evaluation suite keep their value |
| R2 Pool | tied to the partner's release cycle, typically 1–3 years **[reconstructed]** | a share of a consortium programme; tens of millions over several years for a contributing partner **[reconstructed]** | the contribution in kind (corpus, evaluation, people) and the cash share | with the consortium's fleet, not the state's |
| R3 Build | 3–5 years to a credible first model, then continuous **[reconstructed]** | low billions over five years for a mid-scale programme **[reconstructed]** | the cluster, its power, its refresh, and a one-to-two-hundred-person organisation | fast: a 2026 fleet is largely obsolete by 2029 (`FRONTIER-MODEL.md` §6) |
| R4 Procure | months | an operating line, from under a million to tens of millions a year by volume **[reconstructed]** | inference volume and the terms | not at all; nothing is owned |

### Choosing

The choice is forced by the building blocks a state already has, and the entries in section 5 apply it state by
state. The rule of thumb this note uses:

1. **Every state takes R1 first**, because it is the cheapest way to build the corpus, the team and the evaluation
   suite that every other route needs, and it reaches B1 to B6 by itself for most public-service uses.
2. **A state whose language is shared with another member state, or whose corpus is small, takes R2 with the
   language community or an EU vehicle**, and negotiates rights before it contributes a token.
3. **A state with a large corpus, a hosted EuroHPC system or AI Factory, a funded national programme and the fiscal
   room considers R3**, as a capability choice, with eyes open to §6 of the NL note.
4. **Every state takes R4 as the complement**, with the national evaluation suite as the yardstick.

## 3. The building blocks, and how to read an entry

Each entry in section 5 opens with a snapshot table of the state's building blocks. This section says what each
row means and why it matters for the route choice. The snapshots were collected by research agents on 2026-10-10 from
the pages cited in each row; the strategy that follows each snapshot is the author's analysis.

**Languages and speakers.** Which languages the state must serve (B1), and how many people speak each. The number of
speakers is a proxy for the size of the digital corpus: `FRONTIER-MODEL.md` §3 estimates that a language with about
25 million speakers has on the order of 1% of a frontier training corpus available in high-quality text. A language
with two million speakers has correspondingly less, which is why small-language states pool (R2) and why minority
languages inside a state are a separate problem from the majority language.

**Language shared with.** Whether another member state, a diaspora or a neighbour speaks the same language. A shared
language is the strongest reason to pool: the corpus doubles, the cost halves, and a model one state trains serves
the other's citizens at once. It is also the reason a state may not need its own model at all for B1, and can
concentrate on B2 and B3.

**EuroHPC system on national soil.** A EuroHPC Joint Undertaking supercomputer hosted in the state. It matters for
R1 (the state has a national path to accelerator time), for R2 (it is the usual host of an AI Factory), and for R3
(it is the only existing training-class infrastructure most states have). A system that is selected but not yet
operational is a building block in the future tense.

**EuroHPC AI Factory.** The Commission's and EuroHPC's programme that upgrades or builds AI-optimised supercomputers
with a service layer for start-ups, researchers and the public sector (section 4). Hosting one gives a state a
national entry point to training compute and to the programme's model work; being served by an antenna gives access
without the system.

**AI Gigafactory.** The larger EU instrument for frontier-class training facilities (section 4). A state named as a
host or lead partner has a route to R3 at a scale it could not fund alone; a bid is a signal of intent and of grid
and site capacity; absence is neither a finding nor a problem for reaching the bar.

**National or regional model efforts.** Every model programme the research found that targets the state's language,
with who runs it, who funds it, how much, which base it started from, under which licence it is released, and where
it stands. This row is the strongest predictor of the route: a funded, released, open-licensed national model means
R1 is already under way and the question is how to institutionalise it.

**National AI strategy.** Whether the government has adopted a strategy and whether it is in force. It matters less
for capability than for B5: a programme without a strategy behind it is a project, and projects end.

**Public-sector LLM use.** Government assistants, pilots and procurements already running. These are where B1 to B6
get tested in practice, and where the national evaluation suite comes from.

**Language resources.** The national corpus, the CLARIN node, the language-technology programme. These are the raw
material of R1 and R2 and the slowest building block to create from nothing.

**Key institutions.** The AI institute, the HPC centre and the language-technology lab that would carry the
programme. A route that names no institution is a wish.

**Power and grid.** Noted only where an official source says it binds (as in Ireland) or where the state's electricity
price, from this repository's fundamentals, is high enough to matter for a training programme. It does not matter
for R1, R2 or R4, whose compute is elsewhere.

**[unverified]** marks a cell the research agent could not confirm from a page it fetched on 2026-10-10. Such cells
are included because the gap is informative; nothing should be quoted from them.

## 4. The EU vehicles

What the Union offers a member state that wants a model of its own, as the official pages describe it on
2026-10-10. Each vehicle is a building block for R1 or R2, and the last one is the frame that will bind R4.

### EuroHPC AI Factories and their antennas

Nineteen AI Factories were selected in three rounds (10 December 2024, 12 March 2025 and 10 October 2025) and
thirteen antennas on 13 October 2025, the antennas with about EUR 55 million of EU funding matched by the
participating states (https://eurohpc-ju.europa.eu/ai-factories_en, accessed 2026-10-10;
https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en,
accessed 2026-10-10). A factory is an AI-optimised supercomputer with a service layer for start-ups, researchers
and the public sector; an antenna is a state's gateway to another state's factory. Six factories have signed
contracts for their new systems in 2026, each 50% EuroHPC and 50% national; no new AI-optimised system was stated
as operational on an official page by the access date, so every factory is a building block in the near future
tense. The per-state entries carry the host, system and status for each.

| Host state | Factory | Host institution | System | Round | Status on the official page |
|---|---|---|---|---|---|
| Austria | AI:AT | Advanced Computing Austria and AIT, at TU Wien | new, unnamed | Mar 2025 | selected; no contract found **[unverified]** |
| Bulgaria | BRAIN++ | Sofia Tech Park with INSAIT | Discoverer++ | Mar 2025 | tender open to 16 October 2026 |
| Czechia | CZAI | IT4Innovations, VSB-TU Ostrava | KarolAIna | Oct 2025 | selected |
| Finland | LUMI AIF | CSC, Kajaani, with CZ, DK, EE, NO, PL | LUMI-AI | Dec 2024 | contract 31 August 2026, EUR 387.8 M; availability expected 2027 |
| France | AI2F | GENCI with CEA, CINES, CNRS, Inria | Alice Recoque (exascale) | Mar 2025 | contract 18 November 2025, EUR 354.8 M; installation from 2026 |
| Germany | HammerHAI | HLRS Stuttgart | HammerHAI | Dec 2024 | contract 16 March 2026, EUR 55 M; operation expected second half of 2026 |
| Germany | JAIF | Forschungszentrum Jülich | JUPITER (exascale) | Mar 2025 | JUPITER inaugurated 5 September 2025 |
| Greece | Pharos | GRNET | DAEDALUS | Dec 2024 | DAEDALUS "fully available shortly" (June 2026) |
| Italy | IT4LIA | CINECA, Bologna, with AT and SI | new system plus Leonardo | Dec 2024 | contract 22 April 2026, EUR 290 M |
| Lithuania | LitAI | Vilnius University | new, unnamed | Oct 2025 | selected |
| Luxembourg | Meluxina-AI | LuxProvide | MeluXina-AI | Dec 2024 | contract 22 July 2026, EUR 80 M; installation from autumn 2026 |
| Netherlands | NLAIF | AIFNL Foundation with SURF, TNO | new, unnamed | Oct 2025 | selected |
| Poland | PIAST | PSNC Poznań | new, unnamed | Mar 2025 | "services available from 2026"; no contract found **[unverified]** |
| Poland | Gaia AI | Cyfronet AGH | about 1,000 GPUs | Oct 2025 | selected |
| Romania | RO AI | ICI Bucharest with Politehnica | to be acquired | Oct 2025 | selected; implementation from 1 September 2026 |
| Slovenia | SLAIF | IZUM with JSI and ARNES | new, unnamed | Mar 2025 | selected; no contract found **[unverified]** |
| Spain | BSC AIF | BSC, with PT, TR, RO | MareNostrum 5 AI upgrade | Dec 2024 | contract 26 January 2026, about EUR 129 M |
| Spain | 1HealthAI | CESGA, Galicia | not stated | Oct 2025 | selected |
| Sweden | MIMER | NAISS, Linköping | Mimer | Dec 2024 | contract 21 April 2026, EUR 29.76 M; online 2027 |

Sources for the table: the EuroHPC JU AI Factories page and the per-factory pages it links, and the contract
press releases, all accessed 2026-10-10 (https://www.eurohpc-ju.europa.eu/ai-factories/finland_en,
https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en,
https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-ai-supercomputer-hammerhai-2026-03-16_en,
https://www.eurohpc-ju.europa.eu/ai-factories/germany_en, https://www.eurohpc-ju.europa.eu/ai-factories/greece_en,
https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-boost-ai-capabilities-it4lia-ai-factory-2026-04-22_en,
https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-meluxina-ai-new-ai-optimised-supercomputer-luxembourg-ai-factory-2026-07-22_en,
https://www.eurohpc-ju.europa.eu/contract-signed-boost-marenostrum-5s-ai-capabilities-2026-01-26_en,
https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en,
https://www.eurohpc-ju.europa.eu/ai-factories/austria_en, https://www.eurohpc-ju.europa.eu/ai-factories/bulgaria_en,
https://www.eurohpc-ju.europa.eu/contract-signed-alice-recoque-europes-new-exascale-supercomputer-2025-11-18_en,
https://www.eurohpc-ju.europa.eu/ai-factories/france_en, https://www.eurohpc-ju.europa.eu/jupiter-launching-europes-exascale-era-2025-09-05_en,
https://www.eurohpc-ju.europa.eu/ai-factories/poland_en, https://www.eurohpc-ju.europa.eu/ai-factories/slovenia_en,
https://www.eurohpc-ju.europa.eu/czechia_en, https://www.eurohpc-ju.europa.eu/lithuania_en,
https://www.eurohpc-ju.europa.eu/netherlands_en, https://www.eurohpc-ju.europa.eu/spain-1health-ai_en,
https://www.eurohpc-ju.europa.eu/poland-gaia-ai-factory_en, https://www.eurohpc-ju.europa.eu/romania_en).

The EU-27 antennas: Belgium (to LUMI and JAIF), Cyprus (to Pharos), Hungary (to JAIF), Ireland (to AI2F and
Luxembourg), Latvia (to LUMI), Malta (CALYPSO, to Pharos) and Slovakia (to AI:AT). Croatia, Denmark, Estonia and
Portugal have neither a factory nor an antenna of their own on the list, though Denmark and Estonia are in the
LUMI consortium and Portugal in the BSC consortium (https://eurohpc-ju.europa.eu/ai-factories_en and
https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en,
accessed 2026-10-10).

### EuroHPC supercomputers

Twelve systems on the official list, hosted in eleven states: JUPITER (Germany, exascale, inaugurated 5
September 2025), LUMI (Finland), Leonardo (Italy), MareNostrum 5 (Spain), DAEDALUS (Greece, available "shortly"
in June 2026), Arrhenius (Sweden, inaugurated 8 September 2026), MeluXina (Luxembourg), Karolina (Czechia),
Deucalion (Portugal), Vega (Slovenia), Discoverer (Bulgaria), and Alice Recoque (France, exascale, under contract
with installation from 2026) (https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed
2026-10-10). Ireland's CASPIr has a hosting agreement and an open tender but is not yet on the list.

### AI Gigafactories

The larger instrument. InvestAI (11 February 2025) set out to mobilise EUR 200 billion, including a EUR 20 billion
fund for Gigafactories (https://digital-strategy.ec.europa.eu/en/news/eu-launches-investai-initiative-mobilise-eu200-billion-investment-artificial-intelligence,
accessed 2026-10-10). The expression-of-interest round drew 76 submissions covering 60 sites in 16 member states
(https://www.eurohpc-ju.europa.eu/ai-gigafactories/ai-gigafactories-consultations_en, accessed 2026-10-10).
Council Regulation (EU) 2026/150 of 16 January 2026 lets the Union fund up to 17% of the capital expenditure,
matched at least equally by participating states, with the JU owning the Union-funded part for at least five
years (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R0150, accessed 2026-10-10). The call for
tenders EUROHPC-2026-CEI-AIGF-01 opened 30 July 2026 for up to seven Gigafactories, each with at least three to
four times an AI Factory's count of the most advanced processors, with selection expected in early 2027; the
press release gives a 12 November 2026 deadline and the call page 3 December 2026, so the extension is
**[unverified]** (https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en
and https://eurohpc-ju.europa.eu/call-tenders-selection-artificial-intelligence-gigafactory-consortia-and-establishment-ai_en,
accessed 2026-10-10). No consortium had been selected by the access date, and no official page names the
applicants; where an entry reports a state's bid it is from that state's own ministry or from press, and says so.

**What it means for the bar.** Nothing. A Gigafactory is the R3 instrument at a scale beyond any state alone,
and the only route to frontier-class training in Europe. No state needs one to reach B1 to B6.

### OpenEuroLLM

A Digital Europe project (grant 101195233) that started 1 February 2025 for three years, coordinated by Charles
University with AMD Silo AI as co-lead and twenty partners including ALT-EDIC, to build open-source models
covering the EU official languages; its first model weights are due 31 December 2026 and the final models 31
January 2028; it has drawn 3 million GPU hours on Leonardo and 1.5 million on LUMI through the AI Factory and
EuroHPC calls (https://openeurollm.eu/, https://openeurollm.eu/deliverables, https://openeurollm.eu/news **[unverified]**,
https://alt-edic.eu/projects/openeurollm/, accessed 2026-10-10). The budget figure appears only in press
**[unverified]**. For a member state it is the most direct R2 vehicle: open weights and tokenizers for its
language at the 2026 and 2028 milestones, and a formal channel in through ALT-EDIC membership.

### The Frontier AI Grand Challenge and the EUROPA consortium

The Commission's 2026 competition (opened 13 February, closed 13 April 2026) for a model of at least 400 billion
parameters' capacity, whose winner receives up to 2.5% of EuroHPC's capacity for one year and is expected to
deliver open models (https://digital-strategy.ec.europa.eu/en/funding/turning-strategy-action-commission-launches-frontier-ai-grand-challenge,
accessed 2026-10-10). On 19 June 2026 the Commission selected the EUROPA consortium, led by the Italian company
Domyn, to build an open-source model covering all 24 official EU languages
(https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open,
accessed 2026-10-10). Other members, cash funding and the delivery date are not on the official page
**[unverified]**. For a state, it is a model to evaluate when it exists, not a programme to join.

### ALT-EDIC

The Alliance for Language Technologies, a European Digital Infrastructure Consortium set up by Implementing
Decision (EU) 2024/458 of 1 February 2024 with its seat in Villers-Cotterêts, France
(https://eur-lex.europa.eu/eli/dec_impl/2024/458/oj, accessed 2026-10-10). The latest roster fetched lists
seventeen member states (Bulgaria, Croatia, Czechia, Denmark, Finland, France, Greece, Hungary, Ireland, Italy,
Latvia, Lithuania, Luxembourg, the Netherlands, Poland, Slovenia, Spain) plus Flanders, and eight observers
(Austria, Belgium, Cyprus, Estonia, Malta, Portugal, Romania, Slovakia); Germany and Sweden appear on no fetched
list; other official pages give other counts at other dates, so the roster is **[unverified]** as current
(https://language-data-space.ec.europa.eu/related-initiatives/alt-edic_en, accessed 2026-10-10). It offers
federated language data including for languages under ten million speakers, a repository of open models, a
pooled seed fund with EuroHPC access, and evaluation and certification methods; it runs OpenEuroLLM, LLMs4EU and
LLM-BRIDGE (https://alt-edic.eu/, accessed 2026-10-10). It is the R2 vehicle for a small-language state: the
place where its corpus is pooled and its model is co-funded.

### Compute access for a public body

Two families. The general EuroHPC calls: Extreme Scale has a "Public Administration Access" track with cut-offs
4 May and 26 October 2026 on LUMI, Leonardo, MareNostrum 5 and JUPITER; AI for Science and Collaborative EU
Projects is open to "users from public sector" with six-month allocations and six cut-offs a year
(https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-extreme-scale-access-mode_en and
https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-ai-science-and-collaborative-eu-projects_en, accessed
2026-10-10). The AI Factory modes: Playground (within two working days), Fast Lane (up to 50,000 GPU hours,
within four working days) and Large Scale (over 50,000 GPU hours for up to a year, two cut-offs a month)
(https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en, accessed 2026-10-10). Whether the
industrial modes are free for public bodies is **[unverified]**. The practical reading: an R1 programme's
continued pretraining fits inside one Large Scale allocation, as OpenEuroLLM's 3 million GPU hours on Leonardo
show; no state needs to own a training cluster to adapt a model.

### The frame: the Cloud and AI Development Act

Proposed 3 June 2026 (COM(2026) 502), in the ordinary legislative procedure and not adopted. It would require each
member state to adopt a national cloud and AI strategy within a year of entry into force, define four Union
assurance levels for sovereignty (from "data processed and stored in the EU" to full control of the software
supply chain), and require public procurement to use at least Level 1
(https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0502 and
https://digital-strategy.ec.europa.eu/en/policies/cloud-and-ai-development-act, accessed 2026-10-10). If adopted,
it is the vocabulary in which B2 and the terms of R4 will be written, and the obligation that turns every entry
below into a document a state must produce anyway.

### The Apply AI Strategy and the Data Union

The AI Continent Action Plan (9 April 2025) committed EUR 10 billion to AI Factories for 2021 to 2027 and up to
five Gigafactories, and the Apply AI Strategy (8 October 2025) mobilises around EUR 1 billion with a public-sector
flagship, an "AI first" and "buy European" posture with a focus on open source, and free EuroHPC access for
frontier-competition winners (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025DC0165,
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025DC0723, accessed 2026-10-10). The Data Union
Strategy (19 November 2025) puts the first data labs under the AI Factories and targets 30 million digitised
cultural objects for AI training by the end of 2026
(https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025DC0835, accessed 2026-10-10). The European
Language Data Space is the Commission's live marketplace for language datasets, with its data available to
ALT-EDIC (https://language-data-space.ec.europa.eu/index_en, accessed 2026-10-10). For a state these are where the
national corpus (B4) gets its EU-level counterpart and its licensing frame.

## 5. The twenty-seven

One entry per member state, alphabetical by English name, in the template section 3 describes. The snapshot is
what the research found on 2026-10-10; the strategy is the author's.

### Austria (AT)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | German; population 9,197,213 (Eurostat 2025 via the EU country page); six recognised ethnic groups under the Volksgruppengesetz (Croatian, Slovene, Hungarian, Czech, Slovak, Roma); speaker counts **[unverified]**. | https://european-union.europa.eu/principles-countries-history/eu-countries/austria_en (accessed 2026-10-10); https://www.bundeskanzleramt.gv.at/themen/volksgruppen.html (accessed 2026-10-10) |
| Language shared with | Germany, and Belgium's and Luxembourg's German speakers. | https://european-union.europa.eu/principles-countries-history/eu-countries/germany_en (accessed 2026-10-10) |
| EuroHPC system on national soil | None. The national MUSICA cluster: 272 H100 GPU nodes across Vienna, Innsbruck and Linz, about 40 PFlops expected, EUR 36 million with about EUR 20 million from the EU recovery plan, coordinated by TU Wien; 2026 operating status **[unverified]**. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10); https://www.tuwien.at/tu-wien/aktuelles/news/news/musica-oesterreichs-naechster-supercomputer (accessed 2026-10-10); https://www.bundeskanzleramt.gv.at/eu-aufbauplan/aktuelles/musica-neuer-supercomputer-cluster.html (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: AI:AT, selected 12 March 2025, at TU Wien, led by Advanced Computing Austria and AIT with eleven participants; CORDIS: EUR 30.0 million, July 2025 to June 2028; press gives EUR 80 million and 650 to 700 GPUs **[unverified]**; Slovakia's antenna attaches to it; operational status **[unverified]**. | https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en (accessed 2026-10-10); https://cordis.europa.eu/project/id/101253078 (accessed 2026-10-10); (press) https://www.trendingtopics.eu/ai-factory-austria/ (accessed 2026-10-10) |
| AI Gigafactory | No Austrian bid found **[unverified]**. | https://cordis.europa.eu/project/id/101253078 (accessed 2026-10-10) |
| National or regional model efforts | No Austrian-trained foundation model found. The 2024 implementation plan floats a single federal LLM ("Bundes-LLM") for the administration; Public AI and GovGPT run on Mistral open-weight models in 3B, 8B and 14B sizes on the federal computing centre's servers (press; official pages name no model). | https://www.bmimi.gv.at/dam/jcr:0581519a-ec7f-4271-9c52-6aa19b3323ee/KI-Umsetzungsplan%202024.pdf (accessed 2026-10-10); (press) https://www.trendingtopics.eu/brz-mistral-public-ai/ (accessed 2026-10-10) |
| National AI strategy | AIM AT 2030 (2021), with AI infrastructure and modernising public administration among its fields of action, and the implementation plan of 2024 as interim report; in force. | https://www.digitalaustria.gv.at/dam/jcr:6dacb3c5-ca2b-4751-9653-45ed8765cacd/AIM_AT_2030_UAbf.pdf (accessed 2026-10-10); https://www.bmimi.gv.at/dam/jcr:0581519a-ec7f-4271-9c52-6aa19b3323ee/KI-Umsetzungsplan%202024.pdf (accessed 2026-10-10) |
| Public-sector LLM use | Public AI, launched 19 March 2026 on a shared sovereign infrastructure run by the federal computing centre BRZ: GovGPT for 180,000 federal staff, rolling out from 20 July 2026 across all thirteen ministries, with requests processed on BRZ infrastructure and not used for training; "LLM as a Service" won the eGovernment competition on 3 September 2026. | https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/03/5-konkrete-ki-anwendungen-fuer-oesterreichs-bundesverwaltung.html (accessed 2026-10-10); https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/07/proell-public-ai-launcht-govgpt-fuer-die-bundesverwaltung.html (accessed 2026-10-10); https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/09/proell-oesterreich-gewinnt-egovernment-wettbewerb-mit-public-ai.html (accessed 2026-10-10) |
| Language resources | CLARIAH-AT and the Academy's ARCHE repository **[unverified]** (pages refused); a national corpus of Austrian German **[unverified]**. | https://www.bundeskanzleramt.gv.at/themen/volksgruppen.html (accessed 2026-10-10) **[unverified]** |
| Key institutions | AIT and Advanced Computing Austria (AI:AT); TU Wien (host, MUSICA); ISTA, TU Graz, JKU Linz and the other factory participants; the BRZ (LLM as a Service). | https://cordis.europa.eu/project/id/101253078 (accessed 2026-10-10); https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/09/proell-oesterreich-gewinnt-egovernment-wettbewerb-mit-public-ai.html (accessed 2026-10-10) |
| Power and grid | MUSICA is water-cooled with heat reuse in Vienna and Innsbruck; grid figures **[unverified]**. This repository's fundamentals record a high renewables share and one of the higher electricity prices in the 27. | https://www.bundeskanzleramt.gv.at/eu-aufbauplan/aktuelles/musica-neuer-supercomputer-cluster.html (accessed 2026-10-10) |

#### What good enough means here
German, in the Austrian administrative register, for nine million citizens, with six recognised minority
languages where the law provides. Austria is the clearest example in this note of a state that reached B2
and most of B3 without a national model: a federal "LLM as a Service" on the state's own computing centre,
open-weight models from a French lab, 180,000 users, no training data leaving the building. The language is
Germany's and the compute is arriving; the gap is a model the state owns and a German register tuned for it.

#### Recommended strategy
**R2 with Germany as the base supplier; R1 on top for the Austrian register, on AI:AT; the BRZ service as
the deployment and evaluation vehicle; R4 with terms, which the BRZ already applies.**

1. **Take the German public line as the base (R2).** Teuken and its SOOFI successor are Apache-2.0 and
   trained on the same language; a serving copy under agreed terms, with Austrian evaluation data in return,
   gives Austria a model it owns outright (B3) rather than one it rents.
2. **Tune the Austrian register on AI:AT and MUSICA (R1).** Austrian administrative German, the minority
   languages' public-service text where available, and the GovGPT corpus; a small standing team at AIT or TU
   Wien, with the weights held by the BRZ. The implementation plan's "Bundes-LLM" is this, and it needs a
   budget line, not a study.
3. **Keep the BRZ service as the only deployment path (B2).** It already meets the hosting and data rules;
   the national model joins the open-weight models it serves, and is the fallback if their licences change.
4. **Make GovGPT's traffic the national evaluation set (B6).** With 180,000 users across every ministry,
   Austria has the largest public-service evaluation source in this note; versioned and published, it scores
   the German base, the Austrian tuning and anything procured.
5. **Procure frontier access with terms (R4).** The BRZ's practice (requests stay on its infrastructure, no
   training) is the template; add continuity and a national fallback.
6. **Serve Slovakia through the antenna (R2, as host).** SKAIAT attaches to AI:AT; a Slovak stage on the
   same infrastructure costs little.

#### What it does not need to do
Train an Austrian foundation model from scratch, host a Gigafactory, or buy more compute than AI:AT and
MUSICA: the language is shared, the deployment vehicle exists, and the base is available from Germany.

#### Main blocker, and what would change the recommendation
The state owns no model: GovGPT runs on a foreign lab's open weights, which satisfies B2 but leaves B3 to the
licence. The recommendation would change if Germany does not institutionalise its public line (then the
Austrian tuning starts from Mistral's open weights, as GovGPT does, with escrow terms), or if the
"Bundes-LLM" is funded with AI:AT as its home (R1 is settled).

#### Sources
- European Union, Austria, https://european-union.europa.eu/principles-countries-history/eu-countries/austria_en, accessed 2026-10-10; Germany, https://european-union.europa.eu/principles-countries-history/eu-countries/germany_en, accessed 2026-10-10.
- Bundeskanzleramt, Volksgruppen, https://www.bundeskanzleramt.gv.at/themen/volksgruppen.html, accessed 2026-10-10; MUSICA, https://www.bundeskanzleramt.gv.at/eu-aufbauplan/aktuelles/musica-neuer-supercomputer-cluster.html, accessed 2026-10-10; Public AI launch, https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/03/5-konkrete-ki-anwendungen-fuer-oesterreichs-bundesverwaltung.html, accessed 2026-10-10; GovGPT, https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/07/proell-public-ai-launcht-govgpt-fuer-die-bundesverwaltung.html, accessed 2026-10-10; eGovernment competition, https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/09/proell-oesterreich-gewinnt-egovernment-wettbewerb-mit-public-ai.html, accessed 2026-10-10.
- TU Wien, MUSICA, https://www.tuwien.at/tu-wien/aktuelles/news/news/musica-oesterreichs-naechster-supercomputer, accessed 2026-10-10; EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10; additional AI Factories, https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en, accessed 2026-10-10; CORDIS, AI-AT, https://cordis.europa.eu/project/id/101253078, accessed 2026-10-10.
- BMK, AIM AT 2030, https://www.digitalaustria.gv.at/dam/jcr:6dacb3c5-ca2b-4751-9653-45ed8765cacd/AIM_AT_2030_UAbf.pdf, accessed 2026-10-10; KI-Umsetzungsplan 2024, https://www.bmimi.gv.at/dam/jcr:0581519a-ec7f-4271-9c52-6aa19b3323ee/KI-Umsetzungsplan%202024.pdf, accessed 2026-10-10.
- (press) Trending Topics, AI Factory Austria, https://www.trendingtopics.eu/ai-factory-austria/; BRZ and Mistral, https://www.trendingtopics.eu/brz-mistral-public-ai/; both accessed 2026-10-10.

### Belgium (BE)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Dutch, French and German; population 11,900,123 (Eurostat 2025 via the EU country page); shares per language community **[unverified]** (the federal portal returned a verification page). | https://european-union.europa.eu/principles-countries-history/eu-countries/belgium_en (accessed 2026-10-10) |
| Language shared with | Dutch with the Netherlands; French with France and Luxembourg; German with Germany, Austria and Luxembourg. | https://european-union.europa.eu/principles-countries-history/eu-countries/netherlands_en (accessed 2026-10-10); https://european-union.europa.eu/principles-countries-history/eu-countries/luxembourg_en (accessed 2026-10-10) |
| EuroHPC system on national soil | None. Regional tier-1 systems: Lucia (Cenaero, Charleroi, 300 CPU and 50 GPU nodes, about 4 PFlops, funded by Wallonia); the Flemish Supercomputer Centre's tier-1 **[unverified]** (site unreachable). | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10); https://www.cenaero.be/en/hpc (accessed 2026-10-10); https://www.ugent.be/hpc/en/infrastructure (accessed 2026-10-10) |
| EuroHPC AI Factory | Not a host: a factory candidacy across Zellik and Charleroi (July 2025) became the antenna BE-AIFA, selected 13 October 2025, linked to LUMI and JUPITER, coordinated by imec with 23 partners from Flanders, Wallonia, Brussels and the federal level, EUR 10 million co-funded equally with EuroHPC, March 2026 to February 2029, with public-sector transformation among its focus areas. | https://focusonbelgium.be/en/international/towards-new-european-scale-artificial-intelligence-hub (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en (accessed 2026-10-10); https://belnet.be/en/news-events/news/ai-factory-antenna-connects-belgian-organisations-european-ai-infrastructure (accessed 2026-10-10); https://elixir-belgium.org/projects/belgian-ai-factory-antenna (accessed 2026-10-10) |
| AI Gigafactory | Not bidding, per the public broadcaster in July 2025 (press); status in the 2026 call **[unverified]**. | (press) https://www.vrt.be/vrtnws/fr/2025/07/01/la-belgique-est-candidate-pour-accueillir-une-usine-d-intelligen/ (accessed 2026-10-10) |
| National or regional model efforts | No Belgian public foundation-model programme found **[unverified]**. Fietje 2, a Dutch model on the phi-2 base (2.7B, 28 billion Dutch tokens, MIT), trained on 16 A100 GPUs of the Flemish Supercomputer Centre. Reuse of GPT-NL or of French models by Belgian bodies **[unverified]**. | https://huggingface.co/BramVanroy/fietje-2 (accessed 2026-10-10); https://gpt-nl.nl/ (accessed 2026-10-10) |
| National AI strategy | AI policy is regional: the Flemish AI plan, in a second cycle for 2024 to 2028 by decision of 22 March 2024, with EUR 13.98 million for the research programme in 2024; Wallonia's DigitalWallonia4.ai (2019) and the ARIAC research project (2021 to 2026) per the Commission's 2021 report; the federal convergence plan of 2022 **[unverified]**. | https://www.vlaanderen.be/Decision/65F9A588671BD227364EF166 (accessed 2026-10-10); https://ai-watch.ec.europa.eu/countries/belgium/belgium-ai-strategy-report_en (accessed 2026-10-10) |
| Public-sector LLM use | A federal chatbot pilot per the 2021 report; current federal pilots and the federal cloud choice **[unverified]** (the federal portal challenged the fetch). | https://ai-watch.ec.europa.eu/countries/belgium/belgium-ai-strategy-report_en (accessed 2026-10-10) |
| Language resources | CLARIN-BE since September 2021 under BELSPO with Flemish support; the Institute for the Dutch Language in Leiden is its certified B-centre. | https://clarin-be.ivdnt.org/ (accessed 2026-10-10); https://centres.clarin.eu/centre/22 (accessed 2026-10-10) |
| Key institutions | imec (antenna coordinator); Cenaero (Lucia); Belnet; TRAIL, the Walloon and Brussels AI research network; the Flemish AI research programme; the Flemish Supercomputer Centre. | https://belnet.be/en/news-events/news/ai-factory-antenna-connects-belgian-organisations-european-ai-infrastructure (accessed 2026-10-10); https://trail.ac/ (accessed 2026-10-10); https://www.flandersairesearch.be/ (accessed 2026-10-10) |
| Power and grid | No official source fetched **[unverified]**. | https://www.cenaero.be/en/hpc (accessed 2026-10-10) |

#### What good enough means here
Three languages, each the majority language of a larger neighbour, for twelve million citizens across a
federal state whose AI policy is regional. No Belgian model programme exists and none is needed for B1: the
Dutch, French and German models of the neighbours already serve the languages. What Belgium owes its
citizens is B2 to B6: those models served under Belgian rules, held in Belgian hands, evaluated on Belgian
administrative text, and funded as a standing service rather than three regional projects.

#### Recommended strategy
**R2 as the customer of three neighbours; R1 small for the Belgian registers on antenna and regional
compute; one federal serving environment; R4 with terms.**

1. **Take the neighbours' public models under agreed terms (R2).** GPT-NL for Dutch, the French public line
   for French, the German public line for German: a serving copy of each, with continuation rights and
   Belgian evaluation data in return (B3). Belgium's offer to each neighbour is its own register and its
   evaluation set; Flanders' corpus is a real contribution to GPT-NL.
2. **Tune the Belgian registers (R1, small).** Flemish and Walloon administrative text differ from their
   neighbours' standards; a small team at imec and TRAIL, on antenna compute and Lucia, produces the tuning
   stages and holds them in a federal repository.
3. **Serve all three from one federal environment that satisfies B2.** The federal cloud choice could not be
   confirmed; whatever it is, the three national-language models should run under Belgian rules on Belgian or
   EU infrastructure, and the antenna's public-sector transformation line is where that service is built.
4. **Build one evaluation set per language from federal services (B6).** The federal chatbot pilot of the
   2021 report is the start; publish the sets so procured models are scored on them.
5. **Fund it federally as a standing service (B5),** since the regions fund research and the citizens are
   served by the federal state and the municipalities alike.
6. **Procure frontier access with terms (R4),** the three neighbours' models as fallback.

#### What it does not need to do
Train a Belgian model, host a factory or bid for a Gigafactory: the languages are covered and the compute is
reachable through the antenna. It does not need a fourth regional plan; it needs one federal service.

#### Main blocker, and what would change the recommendation
No federal owner, an unconfirmed federal cloud choice, and no neighbour's model yet released under terms a
Belgian body can use (GPT-NL is limited to launching customers). The recommendation would change if GPT-NL
and the French public line publish open weights (R2 becomes a download and a tuning stage), or if the federal
state funds its own Dutch and French programme (then R1 grows, and the pooling case stays).

#### Sources
- European Union, Belgium, https://european-union.europa.eu/principles-countries-history/eu-countries/belgium_en, accessed 2026-10-10; Netherlands, https://european-union.europa.eu/principles-countries-history/eu-countries/netherlands_en, accessed 2026-10-10; Luxembourg, https://european-union.europa.eu/principles-countries-history/eu-countries/luxembourg_en, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10; antennas, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en, accessed 2026-10-10.
- Cenaero, Lucia, https://www.cenaero.be/en/hpc, accessed 2026-10-10; HPC-UGent, https://www.ugent.be/hpc/en/infrastructure, accessed 2026-10-10.
- Focus on Belgium, AI hub, https://focusonbelgium.be/en/international/towards-new-european-scale-artificial-intelligence-hub, accessed 2026-10-10; Belnet, antenna, https://belnet.be/en/news-events/news/ai-factory-antenna-connects-belgian-organisations-european-ai-infrastructure, accessed 2026-10-10; ELIXIR Belgium, https://elixir-belgium.org/projects/belgian-ai-factory-antenna, accessed 2026-10-10.
- Vlaamse Regering, AI plan decision, https://www.vlaanderen.be/Decision/65F9A588671BD227364EF166, accessed 2026-10-10; AI Watch, Belgium, https://ai-watch.ec.europa.eu/countries/belgium/belgium-ai-strategy-report_en, accessed 2026-10-10.
- CLARIN-BE, https://clarin-be.ivdnt.org/, accessed 2026-10-10; CLARIN centre registry, INT, https://centres.clarin.eu/centre/22, accessed 2026-10-10.
- Bram Vanroy, fietje-2, https://huggingface.co/BramVanroy/fietje-2, accessed 2026-10-10; GPT-NL, https://gpt-nl.nl/, accessed 2026-10-10.
- TRAIL, https://trail.ac/, accessed 2026-10-10; Flanders AI Research, https://www.flandersairesearch.be/, accessed 2026-10-10.
- (press) VRT, https://www.vrt.be/vrtnws/fr/2025/07/01/la-belgique-est-candidate-pour-accueillir-une-usine-d-intelligen/, accessed 2026-10-10.

### Bulgaria (BG)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Bulgarian; 2021 census (total 6,519,789): Bulgarian mother tongue 5,037,607, Turkish 514,386, Roma 227,974. The constitutional provision could not be fetched **[unverified]**. | https://www.nsi.bg/en/file/download/b6f1e478976849e217a6370d9d41c379f7c75b8c (accessed 2026-10-10); https://www.nsi.bg/en/statistical-data/151/1349 (accessed 2026-10-10) |
| Language shared with | No official page fetched **[unverified]**. North Macedonia's antenna is attached to Greece's factory, not Bulgaria's. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en (accessed 2026-10-10) |
| EuroHPC system on national soil | Discoverer at Sofia Tech Park, operational, 4.52 PFlops sustained, 144,384 AMD cores, liquid-cooled; co-funded by EuroHPC and the government, amounts **[unverified]**. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10); https://sofiatech.bg/en/petascale-supercomputer/ (accessed 2026-10-10); https://discoverer.bg/about-discoverer/ (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: BRAIN++, selected 12 March 2025, led by Sofia Tech Park with INSAIT and the Discoverer team; the Discoverer++ system is under tender (estimated EUR 54,228,600, deadline 16 October 2026, installation by end-2026); stated focus includes Bulgarian LLMs, hosting BgGPT, a federated data lake and a sandbox. A EUR 90 million total with 50% national co-financing is press only **[unverified]**. | https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories/bulgaria_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/acquisition-delivery-installation-and-maintenance-hardware-and-software-discoverer-ai-optimised_en (accessed 2026-10-10) |
| AI Gigafactory | No Bulgarian bid found **[unverified]**. | https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en (accessed 2026-10-10) |
| National or regional model efforts | BgGPT (INSAIT, Sofia University): the Gemma-2-27B version continued pretraining on about 100 billion tokens, 85 billion of them Bulgarian; BgGPT 3.0 (26 March 2026) on Gemma 3 in 4B, 12B and 27B sizes under the Gemma licence, with a free public chat, apps and an API; Google credited for cloud training credits. Public funding amount **[unverified]**. | https://huggingface.co/INSAIT-Institute/BgGPT-Gemma-2-27B-IT-v1.0/raw/main/README.md (accessed 2026-10-10); https://huggingface.co/INSAIT-Institute/BgGPT-Gemma-3-27B-IT (accessed 2026-10-10); https://insait.ai/insait-unveils-a-new-generation-of-ai-precision-models-for-business-and-an-upgraded-bggpt-chat-for-all-citizens/ (accessed 2026-10-10) |
| National AI strategy | The "Concept for the development of AI in Bulgaria until 2030", December 2020, with reliable AI infrastructure and a national AI research centre with scalable HPC among its priorities; the Council of Ministers decision reference **[unverified]**. The EuroHPC page says BRAIN++ aligns with it. | https://ai-watch.ec.europa.eu/countries/bulgaria/bulgaria-ai-strategy-report_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories/bulgaria_en (accessed 2026-10-10) |
| Public-sector LLM use | INSAIT reports projects with the National Revenue Agency and the National Audit Office "running on dedicated infrastructure", BgGPT 3.0 free for Bulgarian institutions, and talks with the government on a strategic AI partnership (June 2026). Procurement details **[unverified]**. | https://insait.ai/insait-unveils-a-new-generation-of-ai-precision-models-for-business-and-an-upgraded-bggpt-chat-for-all-citizens/ (accessed 2026-10-10); https://insait.ai/ (accessed 2026-10-10) |
| Language resources | CLaDA-BG, the Bulgarian CLARIN consortium led by the Academy of Sciences; its site returned 404 **[unverified]**. BRAIN++ plans a federated data lake. | https://www.clarin.eu/node/3754 (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories/bulgaria_en (accessed 2026-10-10) |
| Key institutions | INSAIT (Sofia University, with ETH Zurich and EPFL as partners); Sofia Tech Park (Discoverer, BRAIN++ lead); the Bulgarian Academy of Sciences (CLaDA-BG). INSAIT's state funding **[unverified]**. | https://insait.ai/ (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories/bulgaria_en (accessed 2026-10-10) |
| Power and grid | Discoverer has a 1 MW UPS and direct liquid cooling; the Discoverer++ tender requires energy efficiency and gives no power figure. | https://sofiatech.bg/en/petascale-supercomputer/ (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/acquisition-delivery-installation-and-maintenance-hardware-and-software-discoverer-ai-optimised_en (accessed 2026-10-10) |

#### What good enough means here
Bulgarian for about five million citizens in the registers of administration, courts, revenue and health,
with Turkish and Romani as the languages of the two largest minorities. Bulgaria has the unusual position of a
national model that is already deployed with two state institutions, a factory whose stated purpose is to host
it, and a research institute that built it with foreign cloud credits rather than state money.

#### Recommended strategy
**R1 exists; make it the state's. R2 as a supplier to the neighbourhood. R4 with terms.**

1. **Make BgGPT a state-held asset, not only an INSAIT product (B3, B5).** The model is deployed at the
   National Revenue Agency and the National Audit Office, which already satisfies B2 for those two uses, but the
   weights, recipe and evaluation sets should sit in a state repository under an agreement that survives
   INSAIT's partners and funders, and the programme should have a recurring budget line rather than cloud
   credits. The 2020 concept's "national AI research centre with scalable HPC" is the hook; the strategic
   partnership INSAIT reports discussing is the vehicle.
2. **Choose the next base for its licence.** BgGPT 3.0 is under the Gemma licence. Keep a fallback on a
   permissively licensed base, and state in the national register which licence governs each deployed version.
3. **Train the next generation on Discoverer++ when it lands, on Bulgarian power (B2).** BRAIN++'s stated
   purpose includes hosting BgGPT; the tender closes in October 2026 with installation by end-2026, after which
   the training moves from foreign cloud to national soil. Until then, EuroHPC access calls.
4. **Write the national evaluation set from the two agencies' use (B6)** and publish it, so that every procured
   model is scored against the questions the revenue agency and the audit office actually ask.
5. **Supply the neighbourhood (R2).** Bulgarian shares much with Macedonian; North Macedonia's antenna is
   attached to Greece's factory, so Bulgaria is a natural supplier of a model rather than a co-trainer. A
   serving copy under agreed terms costs Bulgaria little and extends its evaluation data.
6. **Procure frontier access with terms (R4)**, with BgGPT as the fallback the state possesses.

#### What it does not need to do
Pretrain from scratch, bid for a Gigafactory, or build a corpus from nothing: 85 billion Bulgarian tokens have
already been through continued pretraining. It does not need a new institute; it needs to own the one it has.

#### Main blocker, and what would change the recommendation
The model's public-funding status and the terms between the state and INSAIT could not be confirmed, and
the strategy document dates from 2020. The recommendation would change if the strategic partnership is signed
with the state holding the weights (R1 is settled), or if Discoverer++ slips well past 2026 (training stays on
rented compute and the EuroHPC access calls carry it).

#### Sources
- NSI, Census 2021 ethnocultural characteristics (xlsx), https://www.nsi.bg/en/file/download/b6f1e478976849e217a6370d9d41c379f7c75b8c, accessed 2026-10-10; index, https://www.nsi.bg/en/statistical-data/151/1349, accessed 2026-10-10.
- EuroHPC JU, additional AI Factories selected, https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en, accessed 2026-10-10; Bulgaria page, https://www.eurohpc-ju.europa.eu/ai-factories/bulgaria_en, accessed 2026-10-10; Discoverer++ tender, https://www.eurohpc-ju.europa.eu/acquisition-delivery-installation-and-maintenance-hardware-and-software-discoverer-ai-optimised_en, accessed 2026-10-10; our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10; antennas, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en, accessed 2026-10-10; AI Gigafactories call, https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en, accessed 2026-10-10.
- Sofia Tech Park, petascale supercomputer, https://sofiatech.bg/en/petascale-supercomputer/, accessed 2026-10-10; Discoverer, about, https://discoverer.bg/about-discoverer/, accessed 2026-10-10.
- INSAIT, home, https://insait.ai/, accessed 2026-10-10; BgGPT 3.0 announcement, https://insait.ai/insait-unveils-a-new-generation-of-ai-precision-models-for-business-and-an-upgraded-bggpt-chat-for-all-citizens/, accessed 2026-10-10.
- INSAIT, BgGPT-Gemma-2-27B-IT-v1.0 README, https://huggingface.co/INSAIT-Institute/BgGPT-Gemma-2-27B-IT-v1.0/raw/main/README.md, accessed 2026-10-10; BgGPT-Gemma-3-27B-IT, https://huggingface.co/INSAIT-Institute/BgGPT-Gemma-3-27B-IT, accessed 2026-10-10.
- AI Watch, Bulgaria AI strategy report, https://ai-watch.ec.europa.eu/countries/bulgaria/bulgaria-ai-strategy-report_en, accessed 2026-10-10.
- CLARIN ERIC members, https://www.clarin.eu/node/3754, accessed 2026-10-10.

### Croatia (HR)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Croatian and the Latin script (Constitution Art. 12), with other languages and scripts admitted locally by law. 2021 census: Croatian mother tongue 3,687,735 of 3,871,833 residents; Serbian 45,004, Bosnian 17,531, Albanian 13,503, Italian 12,890, Hungarian 7,218. | https://www.usud.hr/sites/default/files/dokumenti/The_consolidated_text_of_the_Constitution_of_the_Republic_of_Croatia_as_of_15_January_2014.pdf (accessed 2026-10-10); https://podaci.dzs.hr/media/3hue4q5v/popis_2021-stanovnistvo_rh.xlsx (accessed 2026-10-10) |
| Language shared with | Mutually intelligible with Bosnian, Serbian and Montenegrin; Slovenia's GaMS model lists Croatian, Bosnian and Serbian as secondary training languages. Diaspora figures **[unverified]**. | https://huggingface.co/cjvt/GaMS3-12B-Instruct/blob/main/README.md (accessed 2026-10-10) |
| EuroHPC system on national soil | None. National system Supek at SRCE, Zagreb: 1.25 PFlops, 81 GPUs, in operation since 28 March 2023 under HR-ZOO (EUR 26.12 million, 85% ERDF). | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10); https://www.srce.unizg.hr/en/advanced-computing (accessed 2026-10-10); https://www.srce.unizg.hr/sites/default/files/srce/vijesti/press/2023-03-28/PRIOPCENJE%20-%20PUSTANJE%20U%20RAD%20HR-ZOO-a_28.03.2023_.pdf (accessed 2026-10-10) |
| EuroHPC AI Factory | None, and no antenna. SRCE's own report of December 2025 says Croatia "missed a chance to establish a national AI factory in earlier calls"; press reports the co-financing guarantee was not secured by 30 June 2025 and that an "AI Factory Croatia" is planned in the national AI plan. | https://www.eurohpc-ju.europa.eu/ai-factories_en (accessed 2026-10-10); https://www.srce.unizg.hr/en/news/third-croatian-competence-centre-hpc-day-held/1438 (accessed 2026-10-10); (press) https://en.lider.media/2026/03/22/croatia-the-only-country-without-an-ai-factory-in-the-eu-europe-invests-billions (accessed 2026-10-10) |
| AI Gigafactory | No Croatian bid found **[unverified]**. | https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en (accessed 2026-10-10) |
| National or regional model efforts | HR-XR-XTEND (University of Zagreb, Faculty of Humanities and Social Sciences), a Horizon Europe UTTER sub-project to collect at least 6 billion tokens of Croatian and train a monolingual Croatian LLM, published through HR-CLARIN under permissive licences; base, compute and status not stated. HRVOJE-M (Ciklopea with FFZG) **[unverified]**. | https://hr-xr-xtend.ffzg.unizg.hr/ (accessed 2026-10-10) |
| National AI strategy | The National AI Development Plan to 2032 with an Action Plan 2026 to 2028, in drafting since 27 May 2025 under the Ministry of Justice, Public Administration and Digital Transformation; the Prime Minister said in February 2026 it would be adopted soon (public broadcaster). Adoption **[unverified]**. An earlier plan is listed by OECD.AI. | https://mpudt.gov.hr/news-25399/workshop-startai-a-step-towards-a-strategic-framework-held-in-zagreb/30131 (accessed 2026-10-10); (press) https://glashrvatske.hrt.hr/en/economy/croatia-keeps-pace-with-europe-on-digitalization-pm-tells-council-12559228 (accessed 2026-10-10); https://oecd.ai/en/dashboards/policy-initiatives/national-plan-for-the-development-of-ai-2008 (accessed 2026-10-10) |
| Public-sector LLM use | None found on an official page **[unverified]**. The Prime Minister cited 66 data centres, 44 state-owned (public broadcaster). | (press) https://glashrvatske.hrt.hr/en/economy/croatia-keeps-pace-with-europe-on-digitalization-pm-tells-council-12559228 (accessed 2026-10-10) |
| Language resources | HR-CLARIN, coordinated by the University of Zagreb FFZG, with the Institute for Croatian Language, FER TakeLab, SRCE and the National and University Library; repository at clarin.hr. National corpus size **[unverified]**. | https://www.clarin.hr/ (accessed 2026-10-10); https://www.clarin.eu/node/3754 (accessed 2026-10-10) |
| Key institutions | SRCE (Supek; EuroCC competence centre); University of Zagreb FFZG Institute of Linguistics (HR-XR-XTEND, HR-CLARIN); FER TakeLab; the Ministry of Justice, Public Administration and Digital Transformation. | https://www.srce.unizg.hr/en/croatian-centre-hpc (accessed 2026-10-10); https://www.clarin.hr/ (accessed 2026-10-10) |
| Power and grid | No official constraint found **[unverified]**. Supek is fully liquid-cooled. | https://www.srce.unizg.hr/en/advanced-computing (accessed 2026-10-10) |

#### What good enough means here
Croatian for 3.7 million citizens in the registers of public administration, courts and health, with the
Serbian, Italian and Hungarian minorities served where the law provides. Croatia has the corpus
institutions and a model project, but no training compute of consequence, no factory, no antenna and, on the
access date, no adopted strategy.

#### Recommended strategy
**R2 first, with Slovenia and the South Slavic neighbourhood; R1 on top for the Croatian register; R4 with
terms. The factory question is secondary.**

1. **Join a pooled South Slavic model rather than wait for a factory.** Slovenia's GaMS already treats Croatian
   as a secondary training language and will have an AI Factory in 2027; the Serbian antenna is attached to
   Greece's and Italy's factories. A continued-pretraining run on a shared Croatian, Bosnian, Serbian and
   Slovene corpus, with Croatia contributing the 6-billion-token HR-XR-XTEND corpus and HR-CLARIN's resources,
   gives Croatia a model its own compute could not. The weights, the continuation right and a Croatian serving
   copy go into the agreement before any data does (B3).
2. **Finish the corpus and the evaluation set now (B4, B6).** These are the inputs Croatia controls and the
   slowest to build. HR-XR-XTEND's corpus and HR-CLARIN's repository are the start; the public-service
   evaluation set should be written by the Institute for Croatian Language against real administrative text.
3. **Tune for the Croatian register on Supek or on EuroHPC access (R1, small).** Instruction tuning and the
   final Croatian-register stage fit on Supek's 81 GPUs or inside an AI Factory Fast Lane allocation; they do
   not need a factory.
4. **Deploy under the state's rules (B2).** The state owns 44 data centres; one of them, or the state cloud,
   serves the pooled model for a first public service, and that service's traffic becomes the evaluation set.
5. **Procure frontier access with terms (R4)** with the pooled model as the fallback.
6. **Pursue an antenna, not a factory, in the next call.** An antenna to IT4LIA or SLAIF costs a fraction of a
   factory, needs no co-financing of a supercomputer, and would give Croatian public bodies and SMEs the access
   the factories' partners already have. Write it into the 2032 plan when it is adopted.

#### What it does not need to do
Build a national AI-optimised supercomputer before the model exists, pretrain from scratch, or bid for a
Gigafactory. The corpus is too small for R3 and the neighbourhood too well served by pooling.

#### Main blocker, and what would change the recommendation
No adopted strategy and no budget line, which is why the factory call was missed; the rest follows from that.
The recommendation would change if the 2032 plan is adopted with a funded "AI Factory Croatia" (then an own
factory becomes the training home for the pooled model, and the pooling case stays), or if the Slovene or
Italian factory declines to pool (then an antenna is the minimum and the EuroHPC access calls carry the training).

#### Sources
- Constitutional Court of Croatia, consolidated Constitution, https://www.usud.hr/sites/default/files/dokumenti/The_consolidated_text_of_the_Constitution_of_the_Republic_of_Croatia_as_of_15_January_2014.pdf, accessed 2026-10-10.
- DZS, Census 2021 population tables, https://podaci.dzs.hr/media/3hue4q5v/popis_2021-stanovnistvo_rh.xlsx, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10; AI Factories, https://www.eurohpc-ju.europa.eu/ai-factories_en, accessed 2026-10-10; AI Gigafactories call, https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en, accessed 2026-10-10.
- SRCE, advanced computing, https://www.srce.unizg.hr/en/advanced-computing, accessed 2026-10-10; HR-ZOO press release (PDF), https://www.srce.unizg.hr/sites/default/files/srce/vijesti/press/2023-03-28/PRIOPCENJE%20-%20PUSTANJE%20U%20RAD%20HR-ZOO-a_28.03.2023_.pdf, accessed 2026-10-10; competence centre, https://www.srce.unizg.hr/en/croatian-centre-hpc, accessed 2026-10-10; competence-centre day, https://www.srce.unizg.hr/en/news/third-croatian-competence-centre-hpc-day-held/1438, accessed 2026-10-10.
- Ministry of Justice, Public Administration and Digital Transformation, StartAI workshop, https://mpudt.gov.hr/news-25399/workshop-startai-a-step-towards-a-strategic-framework-held-in-zagreb/30131, accessed 2026-10-10.
- OECD.AI, Croatia national plan, https://oecd.ai/en/dashboards/policy-initiatives/national-plan-for-the-development-of-ai-2008, accessed 2026-10-10.
- University of Zagreb FFZG, HR-XR-XTEND, https://hr-xr-xtend.ffzg.unizg.hr/, accessed 2026-10-10.
- HR-CLARIN, https://www.clarin.hr/, accessed 2026-10-10; CLARIN ERIC members, https://www.clarin.eu/node/3754, accessed 2026-10-10.
- CJVT, GaMS3-12B-Instruct model card, https://huggingface.co/cjvt/GaMS3-12B-Instruct/blob/main/README.md, accessed 2026-10-10.
- (press) HRT Glas Hrvatske, https://glashrvatske.hrt.hr/en/economy/croatia-keeps-pace-with-europe-on-digitalization-pm-tells-council-12559228; Lider, https://en.lider.media/2026/03/22/croatia-the-only-country-without-an-ai-factory-in-the-eu-europe-invests-billions; both accessed 2026-10-10.

### Cyprus (CY)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Greek and Turkish (Constitution Art. 3(1)). The 2021 census counted 923,381 residents in the government-controlled areas, 77.9% Cypriot citizens, as reported by press from the Statistical Service release; the primary release redirected and was not fetched **[unverified]**. No language question. | https://www.constituteproject.org/constitution/Cyprus_2013?lang=en (accessed 2026-10-10); (press) https://cbn.com.cy/article/107087/census-2021-reports-aging-population-restrained-urbanisation-university-education-increase (accessed 2026-10-10) |
| Language shared with | Greek with Greece; Turkish with Türkiye, which is not an EU language. Pharos-CY is tied to the Greek AI Factory with joint Greek LLM work. | https://european-union.europa.eu/principles-countries-history/languages_en (accessed 2026-10-10); https://www.cyi.ac.cy/index.php/in-focus/the-cyprus-institute-coordinates-the-cyprus-ai-factory-antenna-pharos-cy-advancing-artificial-intelligence-in-greek-language.html (accessed 2026-10-10) |
| EuroHPC system on national soil | None. The Cyprus Institute is a consortium member of Greece's DAEDALUS with access in proportion to investment. The national facility at the Cyprus Institute (CaSToRC) runs Cyclone and the RRF-funded Aphroditi edge-AI platform and is the EuroCC competence centre; Cyclone's specifications **[unverified]**. | https://eurohpc-ju.europa.eu/way-open-building-eurohpc-world-class-supercomputer-greece-2022-11-28_en (accessed 2026-10-10); https://hpcf.cyi.ac.cy/about.html (accessed 2026-10-10) |
| EuroHPC AI Factory | Antenna "Pharos-CY", selected 13 October 2025, linked to Pharos "including access to the DAEDALUS supercomputer"; CORDIS: 1 April 2026 to 31 March 2029, EUR 6,000,000 total, EUR 3,000,000 EU, coordinated by the Cyprus Institute with CYENS, the University of Cyprus, the Cyprus University of Technology and others; focus health, sustainability, culture and language. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en (accessed 2026-10-10); https://cordis.europa.eu/project/id/101263007 (accessed 2026-10-10); https://digital-strategy.ec.europa.eu/en/news/eu-announces-ai-factories-antennas-across-member-states-and-partner-countries (accessed 2026-10-10) |
| AI Gigafactory | No bid document found **[unverified]**. The Deputy Ministry said (press, 13 November 2025) Cyprus will join a joint initiative with Greece and Italy. | (press) https://www.cbn.com.cy/article/121443/cyprus-to-join-intergovernmental-initiative-with-greece-and-italy-to-create-ai-gigafactories (accessed 2026-10-10); (press) https://www.cbn.com.cy/article/115599/cyprus-is-ready-to-contribute-to-ai-development-in-europe-deputy-minister-says (accessed 2026-10-10) |
| National or regional model efforts | No Cypriot-built foundation model found. Pharos-CY plans "Large Language Models and digital tools for Greek" jointly with Greece, shared databases and a "unified Greek-language AI ecosystem"; budget line, base and licence not published **[unverified]**. Reuse of Meltemi or Krikri by Cypriot bodies is not documented **[unverified]**. | https://www.cyi.ac.cy/index.php/in-focus/the-cyprus-institute-coordinates-the-cyprus-ai-factory-antenna-pharos-cy-advancing-artificial-intelligence-in-greek-language.html (accessed 2026-10-10); https://cordis.europa.eu/project/id/101263007 (accessed 2026-10-10) |
| National AI strategy | The 2020 national AI strategy, approved by the Council of Ministers in January 2020 (AI Watch). A draft "National AI Strategy 2032" went to public consultation 21 July to 31 August 2026 (press), with a National AI Authority and a 75% public-sector adoption target; adoption **[unverified]**. | https://ai-watch.ec.europa.eu/countries/cyprus/cyprus-ai-strategy-report_en (accessed 2026-10-10); (press) https://cyprus-mail.com/2026/07/28/cyprus-ai-strategy-aims-to-reshape-government-and-business (accessed 2026-10-10) |
| Public-sector LLM use | The gov.cy "Digital Assistant", the first generative-AI application in the Cypriot public sector, in Greek, English and Greeklish, text and voice; over 115,000 answers in its first six months (press). Underlying platform **[unverified]**. | https://oecd.ai/en/dashboards/policy-initiatives/digital-ai-assistant (accessed 2026-10-10); (press) https://www.cbn.com.cy/article/116040/digital-assistant-gives-over-115-000-answers-to-citizens-questions-in-first-six-months (accessed 2026-10-10) |
| Language resources | CLARIN-CY: Cyprus is a CLARIN ERIC member through the Cyprus University of Technology. No national Cypriot Greek corpus found **[unverified]**. | https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Key institutions | The Cyprus Institute / CaSToRC (HPC, EuroCC, Pharos-CY coordinator); CYENS; the University of Cyprus; the Cyprus University of Technology; the Deputy Ministry of Research, Innovation and Digital Policy. CYENS's own pages were empty on fetch **[unverified]**. | https://cordis.europa.eu/project/id/101263007 (accessed 2026-10-10); https://hpcf.cyi.ac.cy/about.html (accessed 2026-10-10) |
| Power and grid | No official source fetched **[unverified]**. This repository's fundamentals record an isolated grid and one of the higher electricity prices in the 27. | https://hpcf.cyi.ac.cy/about.html (accessed 2026-10-10) |

#### What good enough means here
Greek, in the Cypriot administrative register and in the Greeklish that citizens actually type, for a state of
under a million people; Turkish as a constitutional obligation the state cannot meet through any EU partner; and
English for the large resident non-citizen population. The deployment vehicle exists (the gov.cy assistant); the
model and its hosting do not yet belong to the state.

#### Recommended strategy
**R2 with Greece as the primary route, R1 on top of it for the Cypriot register, R4 for everything the pooled
model cannot do.**

1. **Pool with Greece, and write the rights in first.** Pharos-CY already commits to joint Greek LLMs with the
   Greek factory and gives Cyprus access to DAEDALUS. The agreement that matters is the one that gives Cyprus
   possession of the weights and the right to keep serving and tuning them under Cypriot law if Athens changes
   course (B3). A small partner that contributes corpus and evaluation without that clause gets a nominal
   partnership.
2. **Adapt the Greek base for Cyprus (R1, small).** Starting from the Greek line (Meltemi today, the Pharos
   model tomorrow), tune on the Cypriot public-service corpus the Digital Assistant has been collecting since
   December 2024, including Greeklish, and evaluate on real gov.cy questions (B1, B6). This is a team of a
   handful of people at the Cyprus Institute and CYENS, on antenna compute, not a programme.
3. **Treat Turkish as a procured capability with terms (R4), and say so.** No EU partner trains Turkish for
   Cyprus; an open-weight base with strong Turkish, tuned on the Cypriot Turkish administrative corpus, served
   under the same hosting as the Greek model, is the realistic path, and the state should publish that it is a
   gap rather than let it be assumed covered.
4. **Bring the Digital Assistant's hosting inside the bar (B2).** The assistant's platform could not be confirmed;
   whatever it is, the national model should be served from an environment on the state's approved list, with
   the procured frontier model as the fallback, not the other way round.
5. **Build the national evaluation set from the assistant's traffic (B6)** and share it with Greece as Cyprus's
   contribution to the pool: it is the one asset Cyprus has that Greece does not.

#### What it does not need to do
Own training compute, host a full AI Factory or join a Gigafactory consortium as anything but a minor partner:
the antenna, DAEDALUS access and the Greek model line cover B1 to B3 for Greek. It does not need a Cypriot
foundation model trained from its own corpus, which is far too small to justify one.

#### Main blocker, and what would change the recommendation
Everything depends on the terms of the Greek pool, and no fetched page shows them. The second blocker is Turkish,
for which no pooled route exists. The recommendation would change if the Pharos-CY agreement is published with
weights and continuation rights for Cyprus (R2 is then settled), or if the Greece, Italy and Cyprus Gigafactory
initiative becomes a selected consortium with a Cypriot share of access (the compute question changes, the
language question does not).

#### Sources
- EuroHPC JU, AI Factory Antennas selected, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en, accessed 2026-10-10.
- European Commission, AI Factories Antennas, https://digital-strategy.ec.europa.eu/en/news/eu-announces-ai-factories-antennas-across-member-states-and-partner-countries, accessed 2026-10-10.
- CORDIS, Pharos-CY (101263007), https://cordis.europa.eu/project/id/101263007, accessed 2026-10-10.
- The Cyprus Institute, Pharos-CY, https://www.cyi.ac.cy/index.php/in-focus/the-cyprus-institute-coordinates-the-cyprus-ai-factory-antenna-pharos-cy-advancing-artificial-intelligence-in-greek-language.html, accessed 2026-10-10.
- Cyprus Institute HPC Facility, About, https://hpcf.cyi.ac.cy/about.html, accessed 2026-10-10.
- EuroHPC JU, DAEDALUS hosting agreement, https://eurohpc-ju.europa.eu/way-open-building-eurohpc-world-class-supercomputer-greece-2022-11-28_en, accessed 2026-10-10.
- AI Watch, Cyprus AI strategy report, https://ai-watch.ec.europa.eu/countries/cyprus/cyprus-ai-strategy-report_en, accessed 2026-10-10.
- OECD.AI, Digital AI Assistant (Cyprus), https://oecd.ai/en/dashboards/policy-initiatives/digital-ai-assistant, accessed 2026-10-10.
- Constitute, Cyprus 1960 (rev. 2013), https://www.constituteproject.org/constitution/Cyprus_2013?lang=en, accessed 2026-10-10.
- CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10; EU languages, https://european-union.europa.eu/principles-countries-history/languages_en, accessed 2026-10-10.
- (press) CBN, census 2021, https://cbn.com.cy/article/107087/census-2021-reports-aging-population-restrained-urbanisation-university-education-increase; CBN, Gigafactory willingness, https://www.cbn.com.cy/article/115599/cyprus-is-ready-to-contribute-to-ai-development-in-europe-deputy-minister-says; CBN, joint initiative, https://www.cbn.com.cy/article/121443/cyprus-to-join-intergovernmental-initiative-with-greece-and-italy-to-create-ai-gigafactories; CBN, Digital Assistant, https://www.cbn.com.cy/article/116040/digital-assistant-gives-over-115-000-answers-to-citizens-questions-in-first-six-months; Cyprus Mail, strategy 2032, https://cyprus-mail.com/2026/07/28/cyprus-ai-strategy-aims-to-reshape-government-and-business; all accessed 2026-10-10.

### Czechia (CZ)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Czech; census 2021 mother tongue: 8,996,475 of 10,524,167 (759,394 not stated); Slovak 150,738, Ukrainian 88,873, Russian 59,560, Vietnamese 43,822, Polish 30,183. Statutory status **[unverified]**. | https://scitani.gov.cz/matersky-jazyk (accessed 2026-10-10) |
| Language shared with | Slovak is mutually intelligible and the mother tongue of 150,738 residents; Czech speakers in Slovakia **[unverified]**. | https://scitani.gov.cz/matersky-jazyk (accessed 2026-10-10) |
| EuroHPC system on national soil | Karolina at IT4Innovations, Ostrava: EuroHPC petascale, 15.7 PFlops peak, 576 A100 GPUs, in operation since 2021. | https://www.it4i.cz/en/infrastructure/karolina (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/czechia_en (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: CZAI, selected 10 October 2025, linked to KarolAIna, a new AI-optimised system at IT4Innovations of about 340 AI chips and 850 PFlops in AI operations, nearly CZK 1 billion split equally with EuroHPC; consortium led by VSB-TU Ostrava with Brno University of Technology, Charles University and the Czech Technical University. Operational date **[unverified]**. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en (accessed 2026-10-10); https://www.e-infra.cz/en/news/the-czech-republic-has-its-own-ai-factory-including-a-new-ai-supercomputer (accessed 2026-10-10) |
| AI Gigafactory | A project in preparation: the Ministry of Industry and Trade held the first official meeting on an "AI Gigafactory CZ" on 15 August 2025, run by České Radiokomunikace with IT4Innovations at a Prague site; later government approval **[unverified]**; no selection. | https://www.mpo.gov.cz/cz/podnikani/digitalni-ekonomika/umela-inteligence/cesko-smeruje-k-vybudovani-ai-gigafactory--mpo-poradalo-prvni-oficialni-setkani-k-priprave-projektu--289012/ (accessed 2026-10-10) |
| National or regional model efforts | No government-funded Czech national model found. Charles University coordinates OpenEuroLLM (Digital Europe grant 101195233, launched 7 March 2025, over 32 languages, open data) with national co-financing from the education ministry, amount **[unverified]**. CSMPT7b (Brno University of Technology): continued pretraining of MPT-7B on a 67-billion-token Czech collection, Apache-2.0, trained on Karolina (2024). | https://www.vyzkumne-infrastruktury.cz/en/?p=13945 (accessed 2026-10-10); https://openeurollm.eu/ (accessed 2026-10-10); https://huggingface.co/BUT-FIT/CSMPT7b (accessed 2026-10-10) |
| National AI strategy | The National AI Strategy 2030 (NAIS), approved by government resolution 520 of 24 July 2024, with AI in public administration among seven areas; annual action plans, the 2025 plan approved by resolution 237 of 2 April 2025; a government AI commissioner. | https://www.mpo.gov.cz/cz/podnikani/digitalni-ekonomika/umela-inteligence/ (accessed 2026-10-10); https://www.mpo.gov.cz/cz/podnikani/digitalni-ekonomika/umela-inteligence/vybor-pro-umelou-inteligenci-jednal-na-mpo-o-klicovych-evropskych-iniciativach-a-harmonogramu-pripravy-akcniho-planu-2027--291280/ (accessed 2026-10-10) |
| Public-sector LLM use | NAIS and the AI Committee have a public-administration working group; no assistant pilot or model procurement found **[unverified]**. | https://www.mpo.gov.cz/cz/podnikani/digitalni-ekonomika/umela-inteligence/ (accessed 2026-10-10) |
| Language resources | The Czech National Corpus (Charles University), SYN version 14 of January 2026 at almost 5.5 billion words, funded as a large research infrastructure to 2026; LINDAT/CLARIAH-CZ is the CLARIN and ALT-EDIC node; Czechia joined ALT-EDIC in May 2024. | https://www.korpus.cz/ (accessed 2026-10-10); https://www.vyzkumne-infrastruktury.cz/en/?p=13945 (accessed 2026-10-10) |
| Key institutions | IT4Innovations (Karolina, CZAI); ÚFAL at Charles University (OpenEuroLLM coordination, LINDAT); the Institute of the Czech National Corpus; Brno University of Technology FIT; the Ministry of Industry and Trade; e-INFRA CZ. | https://www.eurohpc-ju.europa.eu/czechia_en (accessed 2026-10-10); https://www.korpus.cz/ (accessed 2026-10-10) |
| Power and grid | No official constraint found **[unverified]**. | https://www.it4i.cz/en/infrastructure/karolina (accessed 2026-10-10) |

#### What good enough means here
Czech for nine million citizens in the registers of administration, courts and health, with Slovak
understood by most and spoken natively by 150,000 residents. Czechia has a large national corpus, a EuroHPC
system, a factory on the way, an adopted strategy with annual action plans, and the coordination of Europe's
main open multilingual model project; what it does not have is a Czech model the state funds and deploys.

#### Recommended strategy
**R2 through OpenEuroLLM as the base, R1 on top for the Czech register, pooled with Slovakia; R4 with terms.
R3 only through the Gigafactory, if selected, as a separate choice.**

1. **Take the OpenEuroLLM weights as the national base (R2).** Czechia coordinates the project and co-funds
   it; its first model weights are due at the end of 2026 and the final models in January 2028. The state
   should secure, in writing, what coordination does not automatically give it: possession of the weights,
   the right to continue training them, and a Czech evaluation seat (B3).
2. **Adapt the base for the Czech administrative register on KarolAIna (R1).** The Czech National Corpus at
   5.5 billion words and the LINDAT node are the data; CSMPT7b showed the technique on Karolina. A standing
   programme at ÚFAL and IT4Innovations, funded under NAIS's annual action plan, owns the Czech corpus register
   (B4), the evaluation set (B6) and the release schedule, with KarolAIna as the home once operational and
   the EuroHPC access calls until then.
3. **Pool with Slovakia (R2, as supplier).** Slovakia has no factory and only an antenna to Austria; a joint
   Czech and Slovak continued-pretraining run on CZAI, with Slovak institutions contributing their corpus and
   evaluation, serves both and costs Czechia little. Rights in the agreement first.
4. **Deploy one service under the state's rules (B2) and build the evaluation set from it (B6).** No pilot was
   found; the public-administration working group should name one, run it on KarolAIna or the state's own
   environment, and publish the evaluation set.
5. **Keep the Gigafactory separate.** The Prague project is an industrial-policy bid; if selected it gives
   Czechia an R3 option and the citizen model does not wait for it.
6. **Procure frontier access with terms (R4)**, the national adaptation as fallback.

#### What it does not need to do
Pretrain from scratch or fund a Czech-only model from nothing: the OpenEuroLLM base it coordinates, adapted on
its own corpus, meets the bar sooner. It does not need more compute than KarolAIna.

#### Main blocker, and what would change the recommendation
No Czech model is funded or deployed by the state, and the OpenEuroLLM weights are a 2026 to 2028 deliverable.
The recommendation would change if OpenEuroLLM's milestones slip badly (then R1 starts on an existing open
base at once, as CSMPT7b did), or if the Gigafactory is selected (R3 becomes a choice to cost on its own).

#### Sources
- ČSÚ, mother tongue, https://scitani.gov.cz/matersky-jazyk, accessed 2026-10-10.
- IT4Innovations, Karolina, https://www.it4i.cz/en/infrastructure/karolina, accessed 2026-10-10; EuroHPC JU, Czechia, https://www.eurohpc-ju.europa.eu/czechia_en, accessed 2026-10-10.
- EuroHPC JU, six additional AI Factories, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en, accessed 2026-10-10; e-INFRA CZ, Czech AI Factory, https://www.e-infra.cz/en/news/the-czech-republic-has-its-own-ai-factory-including-a-new-ai-supercomputer, accessed 2026-10-10.
- MPO, AI page, https://www.mpo.gov.cz/cz/podnikani/digitalni-ekonomika/umela-inteligence/, accessed 2026-10-10; Gigafactory meeting, https://www.mpo.gov.cz/cz/podnikani/digitalni-ekonomika/umela-inteligence/cesko-smeruje-k-vybudovani-ai-gigafactory--mpo-poradalo-prvni-oficialni-setkani-k-priprave-projektu--289012/, accessed 2026-10-10; AI Committee, https://www.mpo.gov.cz/cz/podnikani/digitalni-ekonomika/umela-inteligence/vybor-pro-umelou-inteligenci-jednal-na-mpo-o-klicovych-evropskych-iniciativach-a-harmonogramu-pripravy-akcniho-planu-2027--291280/, accessed 2026-10-10.
- MŠMT research infrastructures, OpenEuroLLM co-funding, https://www.vyzkumne-infrastruktury.cz/en/?p=13945, accessed 2026-10-10; OpenEuroLLM, https://openeurollm.eu/, accessed 2026-10-10.
- BUT FIT, CSMPT7b, https://huggingface.co/BUT-FIT/CSMPT7b, accessed 2026-10-10.
- Czech National Corpus, https://www.korpus.cz/, accessed 2026-10-10.

### Denmark (DK)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Danish; population 5,992,734 (Eurostat 2025 via the EU country page); speaker counts and the German-border minority **[unverified]**. | https://european-union.europa.eu/principles-countries-history/eu-countries/denmark_en (accessed 2026-10-10) |
| Language shared with | Mutually intelligible with Norwegian and Swedish; Danish is a training language of Finland's Viking and Sweden's GPT-SW3 families. Faroese and Greenlandic **[unverified]**. | https://huggingface.co/LumiOpen/Viking-33B (accessed 2026-10-10); https://huggingface.co/AI-Sweden-Models/gpt-sw3-40b (accessed 2026-10-10) |
| EuroHPC system on national soil | None found; the EuroHPC Denmark page returned 404 **[unverified]** as absence. Denmark is a member of the LUMI consortium. | https://www.lumi-supercomputer.eu/about-lumi/ (accessed 2026-10-10) |
| EuroHPC AI Factory | Not a host; a partner state in the LUMI AI Factory consortium (with Czechia, Estonia, Norway and Poland), whose LUMI-AI system was contracted on 31 August 2026 for EUR 387.8 million, available in 2027. EuroCC Denmark is the national competence centre. | https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en (accessed 2026-10-10); https://digst.dk/kunstig-intelligens/ai-fabrikker/ (accessed 2026-10-10) |
| AI Gigafactory | A purchaser, not a host: the ministry committed on 31 July 2026 up to DKK 750 million over five years to buy capacity from a European Gigafactory, possibly in Finland. | https://via.ritzau.dk/pressemeddelelse/15067561/danmark-melder-sig-pa-banen-i-projekt-med-ai-gigafabrikker-skal-styrke-europaeisk-suverænitet-og-konkurrenceevne?lang=da (accessed 2026-10-10) |
| National or regional model efforts | Danish Foundation Models (Aarhus, SDU, Copenhagen, the Alexandra Institute), DKK 30.7 million from the Ministry of Digital Affairs for 2024 to 2027, open-access models usable commercially. Munin 1.0 (June 2026 per the release URL **[unverified]** as to date): 8B models post-trained from the Swiss Apertus-8B and other open bases, Apache-2.0. DFM-Mimir: a small model trained from scratch on about 70 billion tokens on SDU's cloud, Apache-2.0. Gefion: a privately funded 1,528-H100 system owned by DCAI, inaugurated 23 October 2024. | https://chc.au.dk/research/danish-foundation-models-dfm (accessed 2026-10-10); https://di.ku.dk/english/news/2024/ministry-of-digital-affairs-grants-30-7-million-to-ambitious-danish-language-model-project/ (accessed 2026-10-10); https://huggingface.co/danish-foundation-models/munin-apertus-8b (accessed 2026-10-10); https://huggingface.co/danish-foundation-models/DFM-Mimir (accessed 2026-10-10); https://escience.sdu.dk/index.php/news/gefion-inauguration/ (accessed 2026-10-10) |
| National AI strategy | A strategic AI initiative within the national digitalisation strategy, which allocates DKK 740 million for 2024 to 2027; a joint public-sector digitalisation strategy for 2026 to 2029 with responsible AI as a focus. The December 2024 AI strategy's text and figures **[unverified]** (PDFs refused fetches). | https://digst.dk/kunstig-intelligens/strategier-for-kunstig-intelligens/ (accessed 2026-10-10); https://digst.dk/digital-transformation/den-faellesoffentlige-digitaliseringsstrategi/ (accessed 2026-10-10) |
| Public-sector LLM use | Børge, the Agency for Digital Government's assistant for borger.dk editors since February 2025, runs on Anthropic's Claude (the model is described as replaceable). AI-as-a-service through the factories is expected "probably from 2027". | https://digst.dk/kunstig-intelligens/kommunikation-paa-borgerdk-med-generativ-ai-assistent/ (accessed 2026-10-10); https://digst.dk/kunstig-intelligens/ai-fabrikker/ (accessed 2026-10-10) |
| Language resources | sprogteknologi.dk, the agency's catalogue of 216 resources from 43 organisations including parliamentary documents and the Danish Dynaword training corpus; CLARIN-DK at the University of Copenhagen. | https://sprogteknologi.dk/ (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Key institutions | DCAI (Gefion); DeiC (national HPC coordination); EuroCC Denmark; the DFM consortium; the Centre for Language Technology at Copenhagen. | https://www.deic.dk/en (accessed 2026-10-10); https://cst.ku.dk/english/projects/danish-foundation-models-en/ (accessed 2026-10-10) |
| Power and grid | No official source fetched **[unverified]**. This repository's fundamentals record a high renewables share. | https://www.deic.dk/en (accessed 2026-10-10) |

#### What good enough means here
Danish for six million citizens in the registers of administration, courts and health, understood across
the Scandinavian languages. Denmark has made its choices in public: a funded open-model programme that
post-trains open bases rather than pretraining, a privately funded H100 cluster, membership of Finland's
factory, and a decision to buy Gigafactory capacity rather than host it. Its production assistant runs on an
American model. The bar is reachable with what exists; B3 is the property the state has not yet claimed.

#### Recommended strategy
**R1 is funded; make it the deployed model. R2 through LUMI and the Nordic pool. R4 with terms, which the
state is already writing. No hosting.**

1. **Make the DFM models the state's own (B3, B5).** The programme runs to 2027 on a ministry grant and
   releases under Apache-2.0 from open bases. Give it a recurring line beyond 2027, hold the weights and the
   Dynaword corpus register in the agency's own repository (B4), and make the agency the deploying customer.
2. **Move Børge, or its successor, onto the national model as the fallback (B2, B3).** The agency describes
   the vendor model as replaceable; the national model should be the one it is replaceable by, hosted on the
   state's approved environment, with the procured model as the better-performing primary where it is.
3. **Pool with the Nordic programmes (R2).** Viking and GPT-SW3 already train on Danish; LUMI-AI is Denmark's
   factory by consortium. A joint Scandinavian continued-pretraining run on LUMI-AI in 2027, with Denmark's
   curated corpus, serves all three states; rights in the agreement first.
4. **Keep the Gigafactory purchase as what it is (R4 compute).** Buying capacity rather than hosting is the
   right call for a state of this size; the contract should carry the same terms as any procurement: EU
   hosting, continuity, a national fallback.
5. **Build the evaluation set from borger.dk (B6)** and publish it: the yardstick for DFM releases, for Claude,
   and for anything procured later.

#### What it does not need to do
Host a EuroHPC system or a factory, pretrain from scratch at scale, or bid for a Gigafactory: the
programme's post-training approach, LUMI-AI and the purchase commitment cover the bar.

#### Main blocker, and what would change the recommendation
The national model is not yet deployed anywhere and the programme ends in 2027; the state's own assistant
runs on a foreign model with no stated fallback. The recommendation would change if DFM is funded past 2027
with the agency as customer (R1 is settled), or if Gefion's owners offer the state training access on terms
(a national training home appears without hosting one).

#### Sources
- European Union, Denmark, https://european-union.europa.eu/principles-countries-history/eu-countries/denmark_en, accessed 2026-10-10.
- LUMI, about, https://www.lumi-supercomputer.eu/about-lumi/, accessed 2026-10-10.
- EuroHPC JU, first seven AI Factories, https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en, accessed 2026-10-10; LUMI-AI contract, https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en, accessed 2026-10-10.
- Digitaliseringsstyrelsen, AI factories, https://digst.dk/kunstig-intelligens/ai-fabrikker/, accessed 2026-10-10; AI strategies, https://digst.dk/kunstig-intelligens/strategier-for-kunstig-intelligens/, accessed 2026-10-10; joint digitalisation strategy, https://digst.dk/digital-transformation/den-faellesoffentlige-digitaliseringsstrategi/, accessed 2026-10-10; Børge, https://digst.dk/kunstig-intelligens/kommunikation-paa-borgerdk-med-generativ-ai-assistent/, accessed 2026-10-10; sprogteknologi.dk, https://sprogteknologi.dk/, accessed 2026-10-10.
- Ministry press release via Ritzau, https://via.ritzau.dk/pressemeddelelse/15067561/danmark-melder-sig-pa-banen-i-projekt-med-ai-gigafabrikker-skal-styrke-europaeisk-suverænitet-og-konkurrenceevne?lang=da, accessed 2026-10-10.
- Aarhus University, DFM, https://chc.au.dk/research/danish-foundation-models-dfm, accessed 2026-10-10; University of Copenhagen, grant, https://di.ku.dk/english/news/2024/ministry-of-digital-affairs-grants-30-7-million-to-ambitious-danish-language-model-project/, accessed 2026-10-10; CST, https://cst.ku.dk/english/projects/danish-foundation-models-en/, accessed 2026-10-10.
- danish-foundation-models, munin-apertus-8b, https://huggingface.co/danish-foundation-models/munin-apertus-8b, accessed 2026-10-10; DFM-Mimir, https://huggingface.co/danish-foundation-models/DFM-Mimir, accessed 2026-10-10.
- SDU eScience, Gefion inauguration, https://escience.sdu.dk/index.php/news/gefion-inauguration/, accessed 2026-10-10.
- DeiC, https://www.deic.dk/en, accessed 2026-10-10; CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10.
- LumiOpen, Viking-33B, https://huggingface.co/LumiOpen/Viking-33B, accessed 2026-10-10; AI Sweden, gpt-sw3-40b, https://huggingface.co/AI-Sweden-Models/gpt-sw3-40b, accessed 2026-10-10.

### Estonia (EE)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Estonian; population 1,369,995 (Eurostat 2025 via the EU country page); the 2021 census records Estonian as the mother tongue of 67% and 243 mother tongues in all; the Russian-speaking share **[unverified]** on the fetched page. | https://european-union.europa.eu/principles-countries-history/eu-countries/estonia_en (accessed 2026-10-10); https://www.stat.ee/en/news/243-mother-tongues-spoken-estonia (accessed 2026-10-10) |
| Language shared with | Finnish is a close relative; the diaspora **[unverified]**. Estonian is among TildeOpen's 34 languages. | https://huggingface.co/TildeAI/TildeOpen-30b (accessed 2026-10-10) |
| EuroHPC system on national soil | None found (the EuroHPC Estonia page returned 404) **[unverified]** as absence. Estonia is in the LUMI consortium through ETAIS. | https://www.lumi-supercomputer.eu/about-lumi/ (accessed 2026-10-10); https://hpc.ut.ee/news/2026-09-01 (accessed 2026-10-10) |
| EuroHPC AI Factory | Not a host; a partner state of the LUMI AI Factory consortium, with continued access to LUMI-AI from 2027 for researchers and public and private users; the Estonian contribution **[unverified]**. No antenna. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en (accessed 2026-10-10); https://hpc.ut.ee/news/2026-09-01 (accessed 2026-10-10) |
| AI Gigafactory | A purchaser: press reports a plan to spend up to EUR 20 million in 2028 to 2032 on services from a Nordic consortium with its main site in Finland; the pages refused fetches **[unverified]**. | https://www.lumi-supercomputer.eu/about-lumi/ (accessed 2026-10-10) **[unverified]** |
| National or regional model efforts | EstLLM (TartuNLP and TalTechNLP), funded by the Ministry of Education and Research under the Estonian Language Technology Programme 2018 to 2027: 8B (continued pretraining of Llama 3.1 on about 35 billion tokens including the 8.6-billion-token Estonian National Corpus) and 70B-Instruct (about 60 billion tokens, then SFT and DPO), both under the Llama 3.1 licence (2025 to 2026); compute **[unverified]**. The Bürokratt roadmap aims at an Estonian-adapted LLM from 2026. | https://huggingface.co/tartuNLP/Llama-3.1-EstLLM-8B-0525 (accessed 2026-10-10); https://huggingface.co/tartuNLP/Llama-3.1-EstLLM-70B-Instruct-0826 (accessed 2026-10-10); https://www.kratid.ee/en/burokratt (accessed 2026-10-10) |
| National AI strategy | The state AI portal names no current strategy document; an AI and data action plan for 2024 to 2026 and an "Eesti.ai" programme of January 2026 appear in search results only **[unverified]**. | https://www.kratid.ee/en (accessed 2026-10-10); https://www.kratid.ee/en/tehisintellekt (accessed 2026-10-10) |
| Public-sector LLM use | Bürokratt, RIA's network of chatbots on public-sector sites, offers institutions LLMs; several institutions already use it; the software is free and hosting about EUR 150 a month in the State Cloud plus LLM usage; roadmap: LLM and retrieval deployment by end-2025, an Estonian-adapted LLM from 2026. | https://www.kratid.ee/en/burokratt (accessed 2026-10-10) |
| Language resources | The Estonian Language Technology Programme 2018 to 2027 (budget **[unverified]**, the ministry page refused); the Estonian National Corpus at 8.6 billion tokens; CLARIN Estonia at the Centre of Estonian Language Resources. | https://huggingface.co/tartuNLP/Llama-3.1-EstLLM-8B-0525 (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Key institutions | The University of Tartu HPC Centre and ETAIS; TartuNLP; TalTechNLP; the Centre of Estonian Language Resources; RIA; the Ministry of Justice and Digital Affairs. | https://hpc.ut.ee/news/2026-09-01 (accessed 2026-10-10); https://www.kratid.ee/en (accessed 2026-10-10) |
| Power and grid | Estonian grid **[unverified]**; LUMI-AI, the compute Estonia relies on, will run on renewables. This repository's fundamentals record a frontline state. | https://hpc.ut.ee/news/2026-09-01 (accessed 2026-10-10) |

#### What good enough means here
Estonian for a nation of 1.4 million where a third of residents have another mother tongue, mostly Russian,
in the registers of a famously digital administration. Estonia has already chosen the citizen-grade route in
practice: a ministry-funded continued-pretraining line (EstLLM), a state deployment vehicle (Bürokratt) that
exposes LLMs to institutions for a few hundred euro a month, and a seat in Finland's factory. What it lacks
is a licence it can defend and a strategy document on the record.

#### Recommended strategy
**R1 is funded; move it onto a defensible base and into Bürokratt. R2 through LUMI and the Finnish pool.
R4 with terms, which the state is already writing as a Gigafactory purchaser.**

1. **Make EstLLM the Bürokratt model (B2, B3).** The roadmap says an Estonian-adapted LLM from 2026; the
   ministry-funded line is it. Hold the weights and the National Corpus register (B4) at the Centre of
   Estonian Language Resources, serve from the State Cloud, and make RIA the customer.
2. **Change the base for the deployed version.** EstLLM's generations carry the Llama 3.1 licence; the
   public-service version should be continued-pretrained on an Apache-2.0 base, as TildeOpen (CC-BY-4.0,
   covering Estonian) or Finland's Viking show is possible at this scale, with the Llama line kept for
   research.
3. **Train on LUMI and LUMI-AI (R2 compute).** ETAIS membership gives the access; 35 to 60 billion tokens of
   continued pretraining is one allocation. No national compute is needed.
4. **Pool with Finland and the Baltic antenna (R2).** A Finno-Baltic continued-pretraining run on LUMI-AI,
   with Estonia's corpus and evaluation set, serves Estonian alongside Finnish and the TildeOpen languages;
   rights to the weights in the agreement first.
5. **Serve Russian-speaking residents deliberately.** A third of residents are not served by an Estonian-only
   model; the pooled or procured model must be evaluated on Russian-language public-service questions, and the
   state should say which route covers them.
6. **Put the model programme on the record (B5).** No current strategy document was found; the Language
   Technology Programme ends in 2027, and its successor is where the recurring line belongs.
7. **Procure frontier access with terms (R4)**, EstLLM as the fallback; the Gigafactory purchase is one such
   contract and should carry the same terms.

#### What it does not need to do
Host compute, pretrain from scratch, or bid to host a Gigafactory: the corpus is small, the neighbour hosts
the factory, and the state's own deployment vehicle already exists.

#### Main blocker, and what would change the recommendation
The deployed licence and the end of the Language Technology Programme in 2027, with no successor on the
record. The recommendation would change if the 2026 Bürokratt LLM ships on an open-licensed base with a
funded successor programme (R1 is settled), or if the Nordic Gigafactory is selected with Estonian training
rights (the compute question changes, the language question does not).

#### Sources
- European Union, Estonia, https://european-union.europa.eu/principles-countries-history/eu-countries/estonia_en, accessed 2026-10-10; Statistics Estonia, 243 mother tongues, https://www.stat.ee/en/news/243-mother-tongues-spoken-estonia, accessed 2026-10-10.
- LUMI, about, https://www.lumi-supercomputer.eu/about-lumi/, accessed 2026-10-10; University of Tartu HPC Center, https://hpc.ut.ee/news/2026-09-01, accessed 2026-10-10; EuroHPC JU, LUMI-AI contract, https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en, accessed 2026-10-10.
- tartuNLP, Llama-3.1-EstLLM-8B-0525, https://huggingface.co/tartuNLP/Llama-3.1-EstLLM-8B-0525, accessed 2026-10-10; Llama-3.1-EstLLM-70B-Instruct-0826, https://huggingface.co/tartuNLP/Llama-3.1-EstLLM-70B-Instruct-0826, accessed 2026-10-10.
- kratid.ee, Bürokratt, https://www.kratid.ee/en/burokratt, accessed 2026-10-10; home, https://www.kratid.ee/en, accessed 2026-10-10; AI, https://www.kratid.ee/en/tehisintellekt, accessed 2026-10-10.
- CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10; TildeAI, TildeOpen-30b, https://huggingface.co/TildeAI/TildeOpen-30b, accessed 2026-10-10.

### Finland (FI)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Finnish and Swedish; population 5,635,971 (Eurostat 2025 via the EU country page); the status of Sámi and speaker counts **[unverified]**. | https://european-union.europa.eu/principles-countries-history/eu-countries/finland_en (accessed 2026-10-10) |
| Language shared with | Swedish with Sweden; Finnish is a national minority language in Sweden (Language Act 2009:600 §7); Estonian affinity **[unverified]**. | https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/spraklag-2009600_sfs-2009-600/ (accessed 2026-10-10) |
| EuroHPC system on national soil | LUMI at CSC's Kajaani data centre, pre-exascale, 380 PFlops sustained, 11,912 AMD GPUs, hosted by an eleven-country consortium, lifespan to 2027; LUMI-AI to replace it from the second half of 2027. | https://www.lumi-ai-factory.eu/computing-infrastructure/ (accessed 2026-10-10); https://www.lumi-supercomputer.eu/about-lumi/ (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: the LUMI AI Factory, selected 10 December 2024, hosted by CSC with Czechia, Denmark, Estonia, Norway and Poland; LUMI-AI contracted with Bull on 31 August 2026, EUR 387.8 million, 50% EuroHPC, AMD MI430X, a tenfold AI capacity increase, users in 2027; language among the key sectors; antennas in Iceland, Latvia and Switzerland. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/finland_en (accessed 2026-10-10); https://csc.fi/en/media-release/new-pan-european-supercomputer-and-eu-ai-factory-in-finland/ (accessed 2026-10-10) |
| AI Gigafactory | The government backed a Nokia-led consortium's expression of interest (press, July 2025); Latvia's ministry says Finland submitted two projects; the government's own release refused fetches **[unverified]**; no selection yet. | (press) https://yle.fi/a/74-20171278 (accessed 2026-10-10); https://www.em.gov.lv/en/article/latvia-and-finland-could-jointly-propose-ai-gigaproject-european-support-competition (accessed 2026-10-10) |
| National or regional model efforts | Poro 34B (Silo AI's SiloGen with TurkuNLP and HPLT): 1 trillion tokens of Finnish, English and code, pretrained on LUMI on compute provided by CSC, Apache-2.0 (2024). Viking 7B to 33B: the Nordic languages plus English and code, 2 trillion tokens on LUMI, Apache-2.0. Poro 2 and the AMD acquisition of Silo AI **[unverified]** (pages refused). FinGPT, used with Poro in ministry pilots; developer **[unverified]**. | https://huggingface.co/LumiOpen/Poro-34B (accessed 2026-10-10); https://huggingface.co/LumiOpen/Viking-33B (accessed 2026-10-10); https://www.sitra.fi/en/projects/generative-ai-pilot-projects/ (accessed 2026-10-10) |
| National AI strategy | The AI 4.0 programme, adopted by the Ministry of Economic Affairs and Employment in 2022, actions to 2030; a successor **[unverified]**. | https://digital-skills-jobs.europa.eu/en/initiatives/national-strategies/finland-artificial-intelligence-40-programme (accessed 2026-10-10) |
| Public-sector LLM use | Sitra-funded pilots (December 2023 to June 2024) at the Ministry of Transport, the Prime Minister's Office and the Ministry of Justice, further training FinGPT and Poro on legislative text; a government-wide platform **[unverified]**. | https://www.sitra.fi/en/projects/generative-ai-pilot-projects/ (accessed 2026-10-10) |
| Language resources | The Language Bank of Finland (Kielipankki), coordinated by FIN-CLARIN (University of Helsinki) with CSC as technical operator. | https://www.kielipankki.fi/language-bank/ (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Key institutions | CSC, a state- and university-owned non-profit company (LUMI, Kajaani); TurkuNLP; Silo AI; HPLT; Aalto University and the ELLIS Institute as the factory's training hub. | https://csc.fi/en/about-us/ (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/finland_en (accessed 2026-10-10) |
| Power and grid | LUMI runs on 100% renewable electricity with waste heat warming Kajaani households; the site has up to 230 MW of ready-built electrical infrastructure; LUMI-AI will run entirely on renewables. This repository's fundamentals record the lowest electricity price in the 27. | https://www.lumi-supercomputer.eu/sustainable-future/ (accessed 2026-10-10); https://hpc.ut.ee/news/2026-09-01 (accessed 2026-10-10) |

#### What good enough means here
Finnish and Swedish for 5.6 million citizens, with Sámi where recognised, in the registers of
administration, courts and health. Finland hosts Europe's largest AI-capable public system and its
successor, has two open model families pretrained on it under Apache-2.0, cheap renewable power with grid
headroom, a language bank with a state operator, and ministries that have already fine-tuned the national
models on their own text. Every building block for every route is present.

#### Recommended strategy
**R3 at mid scale is already Finland's practice; make the state its customer. R2 as the host of the Nordic
and Baltic pool. R4 with terms. The Gigafactory is a national choice the bar does not need.**

1. **Make the state the owner and customer of the Poro and Viking line (B3, B5).** The models were built by a
   company with a university and a research project on CSC-provided compute; the company's ownership could not
   be confirmed. The state should hold the weights, tokenizers and recipes of the national models in CSC's
   repository under Apache-2.0, fund a standing programme at CSC with TurkuNLP, and make a ministry the
   deploying customer, so the line does not depend on one firm's strategy.
2. **Deploy what the pilots proved (B2, B6).** Three ministries fine-tuned Poro on legislative text in 2024;
   one of them should run the result as a live service on CSC-hosted infrastructure, and its traffic becomes
   the national evaluation set, published.
3. **Host the Nordic and Baltic pool on LUMI-AI (R2, as host).** Viking already trains on all the Scandinavian
   languages; Denmark, Estonia, Latvia (by antenna) and Sweden (by consortium) are attached. A standing
   multilingual continued-pretraining run on LUMI-AI, with each partner's corpus and evaluation set and with
   weights rights for all, makes Finland the supplier of the region's models at marginal cost.
4. **Keep the Swedish-language obligation inside the pool.** Swedish for Finland's citizens is Sweden's
   language; the pooled model, not a separate Finnish programme, is where it is served.
5. **Procure frontier access with terms (R4)**, Poro as the fallback the state possesses.
6. **Treat the Gigafactory as industrial policy.** A Nokia-led bid next to LUMI on 230 MW of renewable
   headroom is the strongest siting case in this note, but it is R3 at frontier scale; the citizen model
   neither waits for it nor is argued through it.

#### What it does not need to do
Build anything new for the bar: the system, the successor, the models, the corpus and the pilots exist. It
does not need to pretrain from scratch again before LUMI-AI, nor to wait for the Gigafactory.

#### Main blocker, and what would change the recommendation
The national models are a company's products trained on public compute, with no state ownership or recurring
programme on any fetched page, and the 2024 pilots have no confirmed successor. The recommendation would
change if the state funds the line at CSC with a deploying ministry (R1 and R3 are settled), or if the
Gigafactory is selected at Kajaani (the pool's training home grows, and frontier-scale R3 becomes a choice
to cost separately).

#### Sources
- European Union, Finland, https://european-union.europa.eu/principles-countries-history/eu-countries/finland_en, accessed 2026-10-10; Riksdagen, Språklag 2009:600, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/spraklag-2009600_sfs-2009-600/, accessed 2026-10-10.
- LUMI AI Factory, computing infrastructure, https://www.lumi-ai-factory.eu/computing-infrastructure/, accessed 2026-10-10; LUMI, about, https://www.lumi-supercomputer.eu/about-lumi/, accessed 2026-10-10; sustainable future, https://www.lumi-supercomputer.eu/sustainable-future/, accessed 2026-10-10.
- EuroHPC JU, LUMI-AI contract, https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en, accessed 2026-10-10; Finland, https://www.eurohpc-ju.europa.eu/finland_en, accessed 2026-10-10; CSC media release, https://csc.fi/en/media-release/new-pan-european-supercomputer-and-eu-ai-factory-in-finland/, accessed 2026-10-10; CSC about, https://csc.fi/en/about-us/, accessed 2026-10-10.
- LumiOpen, Poro-34B, https://huggingface.co/LumiOpen/Poro-34B, accessed 2026-10-10; Viking-33B, https://huggingface.co/LumiOpen/Viking-33B, accessed 2026-10-10.
- Sitra, generative AI pilots, https://www.sitra.fi/en/projects/generative-ai-pilot-projects/, accessed 2026-10-10.
- Digital Skills and Jobs Platform, AI 4.0 programme, https://digital-skills-jobs.europa.eu/en/initiatives/national-strategies/finland-artificial-intelligence-40-programme, accessed 2026-10-10.
- Kielipankki, https://www.kielipankki.fi/language-bank/, accessed 2026-10-10; CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10.
- Latvian Ministry of Economics, https://www.em.gov.lv/en/article/latvia-and-finland-could-jointly-propose-ai-gigaproject-european-support-competition, accessed 2026-10-10; University of Tartu HPC Center, https://hpc.ut.ee/news/2026-09-01, accessed 2026-10-10.
- (press) Yle, https://yle.fi/a/74-20171278, accessed 2026-10-10.

### France (FR)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | French (Constitution art. 2); regional languages are part of the national heritage (art. 75-1). Population 68,882,600 (Eurostat, 1 January 2025, provisional); speaker counts per language **[unverified]**. | https://www.conseil-constitutionnel.fr/le-bloc-de-constitutionnalite/texte-integral-de-la-constitution-du-4-octobre-1958-en-vigueur (accessed 2026-10-10); https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?geo=FR&geo=ES&geo=PT&geo=IT&geo=MT&sex=T&age=TOTAL&time=2025&format=JSON&lang=EN (accessed 2026-10-10) |
| Language shared with | Belgium and Luxembourg (official), French protected as a minority language in Italy (Law 482/1999); the wider francophone world **[unverified]** from an official page. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-15;482~art2 (accessed 2026-10-10) |
| EuroHPC system on national soil | Alice Recoque, exascale, to be installed at CEA's TGCC by the Jules Verne consortium (GENCI and CEA with SURF and GRNET), Eviden XH3500, about 1 EFlops expected, "details to be announced mid 2026"; a future system. National systems Jean Zay (IDRIS), Adastra (CINES) and Joliot-Curie (TGCC) carry interim AI Factory access; Jean Zay's capacity **[unverified]**. | https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: AI2F, selected 12 March 2025, led by GENCI with CEA, CINES, CNRS, Inria, Station F and others; services from the second half of 2025 on existing systems; relies on Alice Recoque from 2026; the page cites a public AI investment of EUR 2.8 billion and a planned 50,000-GPU federation with Germany's exascale system. Ireland's antenna is attached to it. | https://www.eurohpc-ju.europa.eu/ai-factories/france_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en (accessed 2026-10-10) |
| AI Gigafactory | The government confirmed its interest in hosting one and committed to buy EUR 100 million of compute from the project selected on French soil, for administrations, research and hospitals, at the 2027 horizon; no site or consortium named; candidate consortia are press only **[unverified]**. | https://www.entreprises.gouv.fr/espace-presse/lancement-dun-appel-projet-europeen-sur-les-capacites-de-calculs-ia-la-france-se (accessed 2026-10-10); https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en (accessed 2026-10-10) |
| National or regional model efforts | Lucie-7B (OpenLLM-France, led by LINAGORA): about 3 trillion tokens, a third French, trained on Jean Zay with about 550,000 H100 GPU hours under a GENCI grand-challenge grant, Apache-2.0, instruct release January 2025; public funding amount not stated. Mistral AI (private): Mistral Small 3.1 under Apache-2.0 (March 2025), Mistral Compute announced June 2025; state funding **[unverified]**. | https://huggingface.co/OpenLLM-France/Lucie-7B (accessed 2026-10-10); https://genci.fr/resultats-projets/resultats/lucie-7b-open-multilingual-model-centered-french (accessed 2026-10-10); https://mistral.ai/news/mistral-small-3-1 (accessed 2026-10-10); https://mistral.ai/news/mistral-compute (accessed 2026-10-10) |
| National AI strategy | The national AI strategy, launched 2018 within France 2030: phase 1 (2018 to 2022) EUR 1.5 billion including Jean Zay, phase 2 (2021 to 2025) EUR 1 billion; a third phase and the 2025 summit figures **[unverified]** (ministry pages refused fetches). | https://www.entreprises.gouv.fr/fr/numerique/enjeux/la-strategie-nationale-pour-l-ia (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories/france_en (accessed 2026-10-10) |
| Public-sector LLM use | Albert API, DINUM's "public infrastructure of generative-AI services" for administrations within the ALLiaNCE incubator; its code organisation publishes a sovereign agentic coding bundle (September 2026). Base models and user counts are press only **[unverified]**. | https://www.numerique.gouv.fr/offre-accompagnement/expertise-alliance-ia-etat/ (accessed 2026-10-10); https://github.com/etalab-ia (accessed 2026-10-10); (press) https://www.presse-citron.net/albert-3-choses-a-savoir-sur-cette-ia-de-letat-qui-ne-plait-pas-a-tout-le-monde/ (accessed 2026-10-10) |
| Language resources | ORTOLANG, the CNRS-led platform of French language tools and resources; France is not listed among CLARIN ERIC members, observer status **[unverified]**; Lucie's training datasets are published under Creative Commons. | https://www.ortolang.fr/ (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Key institutions | GENCI (AI2F lead); IDRIS and CINES; CEA TGCC; Inria; DINUM (Albert); LINAGORA and OpenLLM-France; Mistral AI. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en (accessed 2026-10-10); https://www.numerique.gouv.fr/offre-accompagnement/expertise-alliance-ia-etat/ (accessed 2026-10-10) |
| Power and grid | The ministry cites decarbonised electricity as the case for hosting; grid-connection figures **[unverified]**. | https://www.entreprises.gouv.fr/espace-presse/lancement-dun-appel-projet-europeen-sur-les-capacites-de-calculs-ia-la-france-se (accessed 2026-10-10) |

#### What good enough means here
French for sixty-nine million citizens and for Belgium's and Luxembourg's francophones, in the registers of
administration, courts and health, with the regional languages where the law recognises them. France is the
state in this note with every building block at once: an exascale system on the way, a factory, a private
frontier lab releasing open weights, a public open model, a state-run generative-AI platform for
administrations, and a government commitment to buy Gigafactory compute. The bar is reachable with what exists;
the question is ownership and terms.

#### Recommended strategy
**R1 on the public line, institutionalised; R4 with real terms toward the national frontier lab; R2 as the
supplier to the francophone states; R3 is a live national choice, kept separate from the citizen model.**

1. **Make the state's own model line a standing programme (R1, B5).** Lucie was trained on Jean Zay under a
   one-off grand-challenge grant by a community led by a company. Albert serves administrations on models
   whose identity could not be confirmed. The state should fund one programme, at GENCI with DINUM as the
   deploying customer, that owns a French-register model under a permissive licence, holds its weights and
   recipe (B3), and publishes what it was trained on (B4). Lucie's open corpus is the start.
2. **Write the terms into the Mistral relationship (R4).** A domestic frontier lab under French law is the
   best R4 position any state in this note has, but proximity is not possession: the state's contracts should
   secure weight escrow or an open-weight fallback version, continuity guarantees and evaluation on a
   national set, so that a change of ownership or strategy at the lab never strands a public service.
3. **Build the national evaluation suite on Albert's traffic (B6)** and publish it, as the yardstick for the
   public model, for Mistral's models and for anything bought from abroad.
4. **Keep the Gigafactory purchase as compute procurement, not a model programme.** The compute-purchase
   commitment buys capacity for administrations, research and hospitals; it is R3 infrastructure with a public
   offtake, and the citizen model does not depend on it. `FRONTIER-MODEL.md`'s reason to keep the two asks
   apart applies here too.
5. **Supply Belgium and Luxembourg (R2).** Both lean on French models for their francophone services; a
   serving copy of the public French model under agreed terms, with their evaluation data in return, costs
   France little.
6. **Deploy under the state's rules (B2).** Albert already runs as public infrastructure; the national model's
   hosting should be on the state's approved environments and say so in the register.

#### What it does not need to do
Build a second frontier lab, or subsidise frontier pretraining to meet the bar: the public mid-scale line and
terms with the domestic lab reach B1 to B6. It does not need to wait for Alice Recoque.

#### Main blocker, and what would change the recommendation
The public line is a community grant and a platform with unconfirmed models, not a funded programme with a
named owner; and the state's leverage over its domestic frontier lab is informal. The recommendation would
change if the third strategy phase funds a state model programme with Albert as customer (R1 is settled), or
if the Gigafactory selected on French soil carries public-sector training rights (R3 becomes an option to cost
for the state's own frontier ambitions, separately).

#### Sources
- Conseil constitutionnel, Constitution, https://www.conseil-constitutionnel.fr/le-bloc-de-constitutionnalite/texte-integral-de-la-constitution-du-4-octobre-1958-en-vigueur, accessed 2026-10-10; Eurostat demo_pjan, https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?geo=FR&geo=ES&geo=PT&geo=IT&geo=MT&sex=T&age=TOTAL&time=2025&format=JSON&lang=EN, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en, accessed 2026-10-10; additional AI Factories, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en, accessed 2026-10-10; France AI Factory, https://www.eurohpc-ju.europa.eu/ai-factories/france_en, accessed 2026-10-10; antennas, https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en, accessed 2026-10-10; Gigafactories call, https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en, accessed 2026-10-10.
- DGE, Gigafactory call press release, https://www.entreprises.gouv.fr/espace-presse/lancement-dun-appel-projet-europeen-sur-les-capacites-de-calculs-ia-la-france-se, accessed 2026-10-10; national AI strategy, https://www.entreprises.gouv.fr/fr/numerique/enjeux/la-strategie-nationale-pour-l-ia, accessed 2026-10-10.
- OpenLLM-France, Lucie-7B, https://huggingface.co/OpenLLM-France/Lucie-7B, accessed 2026-10-10; GENCI, Lucie-7B, https://genci.fr/resultats-projets/resultats/lucie-7b-open-multilingual-model-centered-french, accessed 2026-10-10.
- Mistral AI, Mistral Small 3.1, https://mistral.ai/news/mistral-small-3-1, accessed 2026-10-10; Mistral Compute, https://mistral.ai/news/mistral-compute, accessed 2026-10-10.
- DINUM, ALLiaNCE, https://www.numerique.gouv.fr/offre-accompagnement/expertise-alliance-ia-etat/, accessed 2026-10-10; etalab-ia, https://github.com/etalab-ia, accessed 2026-10-10.
- ORTOLANG, https://www.ortolang.fr/, accessed 2026-10-10; CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10; Law 482/1999 art. 2, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-15;482~art2, accessed 2026-10-10.
- (press) Presse-Citron, Albert, https://www.presse-citron.net/albert-3-choses-a-savoir-sur-cette-ia-de-letat-qui-ne-plait-pas-a-tout-le-monde/, accessed 2026-10-10.

### Germany (DE)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | German; population 83,577,140 (Eurostat 2025 via the EU country page). The Charter-recognised minority languages (Danish, Frisian, Sorbian, Romani, Low German) and their speaker counts **[unverified]** (the interior-ministry and Bundestag pages could not be fetched). | https://european-union.europa.eu/principles-countries-history/eu-countries/germany_en (accessed 2026-10-10) |
| Language shared with | Austria (official), Belgium and Luxembourg (among their official languages); the diaspora **[unverified]**. | https://european-union.europa.eu/principles-countries-history/eu-countries/austria_en (accessed 2026-10-10); https://european-union.europa.eu/principles-countries-history/eu-countries/luxembourg_en (accessed 2026-10-10) |
| EuroHPC system on national soil | JUPITER at Jülich, exascale, operational, 1 EFlops sustained; EUR 500 million, half EuroHPC and half the federal research ministry and North Rhine-Westphalia; 5,884 nodes with four GH200 superchips each; installation to conclude in 2026. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10); https://www.fz-juelich.de/en/ias/jsc/jupiter (accessed 2026-10-10); https://www.fz-juelich.de/en/ias/jsc/jupiter/tech (accessed 2026-10-10) |
| EuroHPC AI Factory | Two: JAIF at Jülich (JUPITER plus the JARVIS inference system; CORDIS: EUR 25.0 million, November 2025 to October 2028, with RWTH Aachen, Fraunhofer and TU Darmstadt) and HammerHAI at HLRS Stuttgart with LRZ, KIT and GWDG (a new AI-optimised system contracted March 2026 for EUR 55 million, operation expected in the second half of 2026). Antennas: Belgium and Hungary to JAIF, the United Kingdom to HammerHAI. | https://cordis.europa.eu/project/id/101250682 (accessed 2026-10-10); https://www.hlrs.de/news/detail/hammerhai (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-ai-supercomputer-hammerhai-2026-03-16_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories_en (accessed 2026-10-10) |
| AI Gigafactory | The Hightech-Agenda (cabinet, 31 July 2025) states at least one European Gigafactory should be in Germany (press); Deutsche Telekom, IONOS and the Schwarz Group's IT subsidiary planned separate expressions of interest (press); status of German consortia in the tender **[unverified]**. | (press) https://www.forschung-und-lehre.de/politik/hightech-agenda-passiert-bundeskabinett-7224 (accessed 2026-10-10); (press) https://in.marketscreener.com/quote/stock/SAP-SE-436555/news/No-joint-German-bid-for-AI-gigafactory-50284021/ (accessed 2026-10-10) |
| National or regional model efforts | Teuken-7B (OpenGPT-X, funded by the economics ministry 2022 to 2024; Fraunhofer, Jülich, TU Dresden, DFKI): 24 EU languages, 4 trillion tokens on JUWELS Booster, Apache-2.0; funding amount **[unverified]**. SOOFI (about EUR 20 million from the economics ministry, announced 18 November 2025, coordinated by the German AI Association): an open model of around 100 billion parameters plus a reasoning model; licence and status **[unverified]**. Aleph Alpha (private) agreed to merge with Cohere on 16 September 2026, pending approval (press). | https://opengpt-x.de/en/ (accessed 2026-10-10); https://huggingface.co/openGPT-X/Teuken-7B-instruct-commercial-v0.4 (accessed 2026-10-10); https://www.l3s.de/soofi-launches-europes-path-towards-its-own-ai-language-models/ (accessed 2026-10-10); (press) https://www.heise.de/en/news/Soofi-Germany-to-develop-sovereign-AI-language-model-11083336.html (accessed 2026-10-10); (press) https://siliconangle.com/2026/09/16/cohere-and-aleph-alpha-agree-to-merge-in-reported-20b-deal/ (accessed 2026-10-10) |
| National AI strategy | The federal AI strategy of November 2018, updated December 2020, with funding raised to EUR 5 billion to 2025, a "learning strategy" with no end date; the Hightech-Agenda of 31 July 2025 as the successor frame, with a target of 10% of economic output on AI by 2030 (press). | https://www.ki-strategie-deutschland.de/ (accessed 2026-10-10); (press) https://www.forschung-und-lehre.de/politik/hightech-agenda-passiert-bundeskabinett-7224 (accessed 2026-10-10) |
| Public-sector LLM use | Baden-Württemberg's F13 assistant for state employees (July 2024), on Aleph Alpha technology, hosted by STACKIT in the state's own data centre, later released as open source; federal platforms **[unverified]**. | https://www.baden-wuerttemberg.de/de/service/presse/pressemitteilung/pid/mit-dem-neuen-f13-in-die-verwaltung-der-zukunft (accessed 2026-10-10) |
| Language resources | Eight CLARIN-D centres, merged into CLARIAH-DE and the DFG-funded Text+ consortium; the German Reference Corpus's size **[unverified]** (the IDS page refused). | https://www.research-in-germany.org/en/research-landscape/why-germany/research-infrastructure/CLARIN.html (accessed 2026-10-10) |
| Key institutions | Jülich Supercomputing Centre; HLRS with LRZ, KIT and GWDG; Fraunhofer IAIS and FIT; DFKI; hessian.AI; L3S; the German AI Association; IDS Mannheim. | https://www.hlrs.de/news/detail/hammerhai (accessed 2026-10-10); https://ki-verband.de/ (accessed 2026-10-10) |
| Power and grid | No official grid source fetched **[unverified]**; JUPITER is described as the most energy-efficient of the largest systems. This repository's fundamentals record one of the higher electricity prices in the 27. | https://www.fz-juelich.de/en/ias/jsc/jupiter (accessed 2026-10-10) |

#### What good enough means here
German for 84 million citizens in Germany and for Austria, Luxembourg and Belgium's German-speaking
community, with the minority languages where the law provides, across a federal administration where the
Länder deploy their own assistants. Germany hosts Europe's exascale system and two factories, funded a
24-language open base model, is funding a 100-billion-parameter successor, and had a domestic frontier lab
that is now merging across the Atlantic. The bar is reachable with public assets alone; the question is
which of them the federal state actually deploys.

#### Recommended strategy
**R1 on the publicly funded line (Teuken, then SOOFI), institutionalised as a federal programme; R2 as the
supplier to the German-speaking states; R4 with terms, now that the domestic lab's ownership is changing;
R3 is a national choice through the Gigafactory, kept separate.**

1. **Give the public model line a permanent federal owner (B5).** OpenGPT-X ended in December 2024 and SOOFI
   runs on a grant to July 2026 per press. A federal programme at Jülich and Fraunhofer, under the
   Hightech-Agenda, with a release cadence and a deploying customer (the federal IT centre), is what turns two
   projects into an institution. Teuken's Apache-2.0 release is the licence to keep.
2. **Train on JUPITER and HammerHAI, serve from federal and Land data centres (B2).** The compute exists
   and is national; the federal question is only which body operates the model for the administration.
3. **Write terms into the Aleph Alpha relationship before the merger closes (R4, B3).** F13 and other Land
   deployments run on its technology; a merger that moves control abroad is exactly the case B3 exists for.
   The Länder and the federal state should secure weight escrow or an open-weight fallback, continuity and
   evaluation rights now.
4. **Supply Austria, Luxembourg and Belgium's German speakers (R2).** A German-register public model under
   Apache-2.0 serves them at once; Austria already runs a federal assistant on open weights and would take a
   German one. Their evaluation data in return.
5. **Make F13's open-source release the federal evaluation bench (B6).** A Land has already published an
   assistant; its traffic, anonymised and checked, is the start of a national evaluation set, extended by the
   federal deployment.
6. **Keep the Gigafactory separate.** The Hightech-Agenda wants one in Germany; it is R3 at frontier scale and
   industrial policy, and the citizen model neither waits for it nor is argued through it.

#### What it does not need to do
Build or subsidise a frontier lab to meet the bar, or train a German-only model: the multilingual public line
plus the German register reaches B1 to B6. It does not need the Gigafactory.

#### Main blocker, and what would change the recommendation
The public model line is a sequence of grants with no named federal owner or customer, and the domestic lab
the Länder rely on is changing hands. The recommendation would change if the Hightech-Agenda funds SOOFI's
successor as a federal programme with the federal IT centre as customer (R1 is settled), or if the Aleph
Alpha merger closes without escrow terms (R4 falls back to the public line alone, and its deployment becomes
urgent).

#### Sources
- European Union, Germany, https://european-union.europa.eu/principles-countries-history/eu-countries/germany_en, accessed 2026-10-10; Austria, https://european-union.europa.eu/principles-countries-history/eu-countries/austria_en, accessed 2026-10-10; Luxembourg, https://european-union.europa.eu/principles-countries-history/eu-countries/luxembourg_en, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10; AI Factories, https://www.eurohpc-ju.europa.eu/ai-factories_en, accessed 2026-10-10; HammerHAI contract, https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-ai-supercomputer-hammerhai-2026-03-16_en, accessed 2026-10-10.
- Forschungszentrum Jülich, JUPITER, https://www.fz-juelich.de/en/ias/jsc/jupiter, accessed 2026-10-10; technical overview, https://www.fz-juelich.de/en/ias/jsc/jupiter/tech, accessed 2026-10-10; CORDIS, JAIF, https://cordis.europa.eu/project/id/101250682, accessed 2026-10-10; HLRS, HammerHAI, https://www.hlrs.de/news/detail/hammerhai, accessed 2026-10-10.
- OpenGPT-X, https://opengpt-x.de/en/, accessed 2026-10-10; Teuken-7B, https://huggingface.co/openGPT-X/Teuken-7B-instruct-commercial-v0.4, accessed 2026-10-10; L3S, SOOFI, https://www.l3s.de/soofi-launches-europes-path-towards-its-own-ai-language-models/, accessed 2026-10-10.
- Bundesregierung, KI-Strategie, https://www.ki-strategie-deutschland.de/, accessed 2026-10-10; Baden-Württemberg, F13, https://www.baden-wuerttemberg.de/de/service/presse/pressemitteilung/pid/mit-dem-neuen-f13-in-die-verwaltung-der-zukunft, accessed 2026-10-10.
- Research in Germany, CLARIN, https://www.research-in-germany.org/en/research-landscape/why-germany/research-infrastructure/CLARIN.html, accessed 2026-10-10; KI Bundesverband, https://ki-verband.de/, accessed 2026-10-10.
- (press) Forschung & Lehre, https://www.forschung-und-lehre.de/politik/hightech-agenda-passiert-bundeskabinett-7224; MarketScreener, https://in.marketscreener.com/quote/stock/SAP-SE-436555/news/No-joint-German-bid-for-AI-gigafactory-50284021/; heise, https://www.heise.de/en/news/Soofi-Germany-to-develop-sovereign-AI-language-model-11083336.html; SiliconANGLE, https://siliconangle.com/2026/09/16/cohere-and-aleph-alpha-agree-to-merge-in-reported-20b-deal/; all accessed 2026-10-10.

### Greece (EL)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Greek, an official EU language since 1981. The 2021 census (reference date 22 October 2021) collects no language data, and the ELSTAT pages fetched do not show the national total; the speaker count is **[unverified]**. | https://european-union.europa.eu/principles-countries-history/languages_en (accessed 2026-10-10); https://www.statistics.gr/en/2021-census-pop-hous (accessed 2026-10-10) |
| Language shared with | Cyprus, where Greek is a constitutional official language (Art. 3(1)). Cyprus's AI Factory antenna Pharos-CY plans joint "Large Language Models and digital tools for Greek" with the Greek factory. Diaspora figures **[unverified]**. | https://www.constituteproject.org/constitution/Cyprus_2013?lang=en (accessed 2026-10-10); https://www.cyi.ac.cy/index.php/in-focus/the-cyprus-institute-coordinates-the-cyprus-ai-factory-antenna-pharos-cy-advancing-artificial-intelligence-in-greek-language.html (accessed 2026-10-10) |
| EuroHPC system on national soil | DAEDALUS, owned and operated by GRNET at Lavrion; HPE procurement contract of 28 March 2025, over 89 PFlops, EUR 36 M (EuroHPC 35%, Greece 2.0 RRF 65%); listed 31st on the June 2026 TOP500 at 85.69 PFlops on NVIDIA GH200; "expected to become fully available to European users shortly" (EuroHPC, 23 June 2026); GRNET says operational during 2026. | https://eurohpc-ju.europa.eu/eurohpc-ju-signs-procurement-contract-daedalus-supercomputer-2025-03-28_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/two-new-eurohpc-systems-join-top500-jupiter-remains-among-worlds-fastest-supercomputers-2026-06-23_en (accessed 2026-10-10); https://grnet.gr/daedalus/ (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: Pharos, one of the first seven selected 10 December 2024, built on DAEDALUS, run by GRNET under the Ministry of Digital Governance; EUR 30 M, 50% EuroHPC JU and 50% national, 36 months from March 2025 (ILSP: 1 April 2025 to 31 March 2028); "Culture and Language" is one of three focus sectors; antennas in Cyprus, Malta, North Macedonia and Serbia. Law 5263/2025 created the company "PHAROS AI FACTORY" (State 30%, HCAP 70%) with Greek language and culture in its purpose. | https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en (accessed 2026-10-10); https://grnet.gr/en/2024/12/12/pr-ai-factories/ (accessed 2026-10-10); https://www.ilsp.gr/en/projects/pharos/ (accessed 2026-10-10); https://eurohpc-ju.europa.eu/ai-factories_en (accessed 2026-10-10); https://www.taxheaven.gr/law/5263/2025/arthro/8 (commercial host of the statute text, accessed 2026-10-10) |
| AI Gigafactory | No official Greek bid or consortium page found **[unverified]**. The Commission's expression-of-interest round drew 76 responses from 16 member states across 60 sites, none named. A Cypriot ministry statement (press) describes a joint Greece, Italy and Cyprus initiative after the November 2025 intergovernmental summit. | https://digital-strategy.ec.europa.eu/en/news/overwhelming-response-76-respondents-express-interest-european-ai-gigafactories-initiative (accessed 2026-10-10); (press) https://www.cbn.com.cy/article/121443/cyprus-to-join-intergovernmental-initiative-with-greece-and-italy-to-create-ai-gigafactories (accessed 2026-10-10) |
| National or regional model efforts | Meltemi-7B (ILSP / Athena RC; base Mistral-7B; about 40 B tokens of continued pretraining; Apache-2.0; trained on Amazon cloud through GRNET's OCRE framework; released 26 March 2024). Llama-Krikri-8B (ILSP / Athena RC; base Llama-3.1-8B; about 110 B tokens upsampled, 56.7 B Greek; Llama 3.1 licence; same compute route; paper 19 May 2025). Funder and amounts not stated on either page **[unverified]**. The Pharos "Culture and Language" line commits to open AI models for Greek, with no named model, base or budget published **[unverified]**. | https://huggingface.co/ilsp/Meltemi-7B-v1 (accessed 2026-10-10); https://huggingface.co/ilsp/Llama-Krikri-8B-Instruct (accessed 2026-10-10); https://www.ekt.gr/en/news/30578 (accessed 2026-10-10) |
| National AI strategy | "A Blueprint for Greece's AI Transformation", 25 November 2024, by the High-Level Advisory Committee on AI; its own page calls it a "policy proposal". GRNET calls Pharos a flagship project under it. A formal adoption decision was not found **[unverified]**. A draft law implementing the AI Act went to consultation in June 2026 (press). | https://foresight.gov.gr/en/studies/A-Blueprint-for-Greece-s-AI-Transformation (accessed 2026-10-10); https://grnet.gr/en/2024/12/12/pr-ai-factories/ (accessed 2026-10-10); (press) https://en.protothema.gr/2026/06/23/greece-opens-public-consultation-on-national-framework-for-regulating-ai-under-new-eu-law/ (accessed 2026-10-10) |
| Public-sector LLM use | mAIgov, the gov.gr assistant of the Ministry of Digital Governance, live since December 2023 in 25 languages, trained on over 1,600 gov.gr services and 3,270 procedures, over 1.6 million interactions (OECD.AI). Vendor and underlying model **[unverified]**; the gov.gr page returned 403. Agreements with OpenAI and Mistral are reported in press only **[unverified]**. | https://oecd.ai/en/dashboards/policy-initiatives/maigov-7493 (accessed 2026-10-10); (press) https://greekcitytimes.com/2026/06/08/greece-prepares-to-shape-a-national-artificial-intelligence-policy/ (accessed 2026-10-10) |
| Language resources | CLARIN:EL, the national language-resource infrastructure, a certified CLARIN B-centre hosted by ILSP / Athena RC; ILSP runs a project on Greek dialects and varieties. Size of the Hellenic National Corpus **[unverified]**. | https://centres.clarin.eu/centre/75 (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10); https://www.ilsp.gr/en/ (accessed 2026-10-10) |
| Key institutions | GRNET (DAEDALUS, Pharos coordinator); ILSP / Athena RC (Meltemi, Krikri, CLARIN:EL); NCSR Demokritos, NTUA and the Growthfund (Pharos core consortium); EKT (Greek-language AI services); the Pharos AI Factory company. | https://grnet.gr/en/2024/12/12/pr-ai-factories/ (accessed 2026-10-10); https://www.ilsp.gr/en/ (accessed 2026-10-10); https://www.taxheaven.gr/law/5263/2025/arthro/8 (accessed 2026-10-10) |
| Power and grid | DAEDALUS runs on renewable energy with liquid cooling (Green500 23rd). No official statement of a grid constraint on Greek AI compute was found **[unverified]**. This repository's fundamentals give a mid-range electricity price. | https://eurohpc-ju.europa.eu/eurohpc-ju-signs-procurement-contract-daedalus-supercomputer-2025-03-28_en (accessed 2026-10-10) |

#### What good enough means here
Greek for about ten million citizens plus Cyprus, in the administrative register of gov.gr's 1,600 services, the
courts and the health system; accessible to the Greek diaspora through the same front door. The state already has
the deployment vehicle (mAIgov) and the models (Meltemi and Krikri): the gap is between a model a research
institute publishes and a model a ministry owns, hosts under its own rules and funds every year.

#### Recommended strategy
**R1, already under way; institutionalise it. R2 with Cyprus. R4 with terms.**

1. **Move the Greek model line from project to institution.** Meltemi and Krikri were trained on rented
   Amazon capacity through GRNET's OCRE framework, by ILSP, with no stated funder. The Pharos AI Factory company
   created by Law 5263/2025 names Greek language and culture in its purpose; make it the owner of a standing
   Greek-model programme with ILSP as the technical lead, a recurring budget line rather than project funding
   (B5), and DAEDALUS as the training home once it is fully available (B2, B3).
2. **Keep the open-weight adapt route, and choose the base for its licence.** Meltemi's Apache-2.0 release is the
   stronger precedent for B3 than Krikri's Llama 3.1 licence; the next generation should start from a base whose
   licence a court would read as permitting indefinite state use and modification, and the state should hold the
   weights, the tokenizer and the recipe in its own repository.
3. **Pool with Cyprus through Pharos-CY.** The antenna agreement already names joint Greek LLMs and shared
   databases. Write the weights and continuation rights into it now, so that a Cypriot ministry can serve the
   model under Cypriot law without a Greek decision in between (B3 for both states).
4. **Make mAIgov the evaluation bench (B6).** Its 1.6 million interactions are the national evaluation set in
   waiting: a versioned, anonymised set of real citizen questions with answers checked by the competent
   ministries, run against every candidate, national or procured.
5. **Put terms on the frontier deals (R4).** The reported agreements with OpenAI and Mistral are the complement,
   not the model; the contract should require hosting that satisfies the state's classification rules, a
   fallback to the national model, and evaluation on the mAIgov set before every rollout.
6. **Adopt the strategy formally.** The Blueprint is a policy proposal on its own page; a government decision that
   names the Pharos company as owner of the model programme is what turns B5 from intent into a budget line.

#### What it does not need to do
Pretrain from scratch (R3) or lead a Gigafactory: the Greek corpus is served well by continued pretraining of
an open base, and the compute for that fits inside DAEDALUS and Pharos. It does not need a second model
institute; it needs the one it has to be funded.

#### Main blocker, and what would change the recommendation
No fetched page states who funds the Greek models or for how long; until a recurring line exists, each model is a
one-off. DAEDALUS was not yet fully available in June 2026, so the training home is in the future tense. The
recommendation would change if the Pharos company's budget line for language models is published with a
multi-year figure (R1 is then settled and the question becomes R2 scale), or if a Greece, Italy and Cyprus
Gigafactory consortium is selected (R3 becomes an option worth costing).

#### Sources
- EuroHPC JU, DAEDALUS procurement contract, https://eurohpc-ju.europa.eu/eurohpc-ju-signs-procurement-contract-daedalus-supercomputer-2025-03-28_en, accessed 2026-10-10.
- EuroHPC JU, two new systems join the TOP500, https://www.eurohpc-ju.europa.eu/two-new-eurohpc-systems-join-top500-jupiter-remains-among-worlds-fastest-supercomputers-2026-06-23_en, accessed 2026-10-10.
- GRNET, DAEDALUS, https://grnet.gr/daedalus/, accessed 2026-10-10.
- EuroHPC JU, selection of the first seven AI Factories, https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en, accessed 2026-10-10.
- EuroHPC JU, AI Factories, https://eurohpc-ju.europa.eu/ai-factories_en, accessed 2026-10-10.
- GRNET, Pharos press release, https://grnet.gr/en/2024/12/12/pr-ai-factories/, accessed 2026-10-10.
- ILSP, Pharos project page, https://www.ilsp.gr/en/projects/pharos/, accessed 2026-10-10.
- EKT, Pharos news, https://www.ekt.gr/en/news/30578, accessed 2026-10-10.
- Law 5263/2025 Art. 8 (Taxheaven), https://www.taxheaven.gr/law/5263/2025/arthro/8, accessed 2026-10-10.
- ILSP, Meltemi-7B-v1 model card, https://huggingface.co/ilsp/Meltemi-7B-v1, accessed 2026-10-10.
- ILSP, Llama-Krikri-8B-Instruct model card, https://huggingface.co/ilsp/Llama-Krikri-8B-Instruct, accessed 2026-10-10.
- Special Secretariat of Foresight, Blueprint, https://foresight.gov.gr/en/studies/A-Blueprint-for-Greece-s-AI-Transformation, accessed 2026-10-10.
- OECD.AI, mAIgov, https://oecd.ai/en/dashboards/policy-initiatives/maigov-7493, accessed 2026-10-10.
- CLARIN:EL centre record, https://centres.clarin.eu/centre/75, accessed 2026-10-10; CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10; ILSP, https://www.ilsp.gr/en/, accessed 2026-10-10.
- European Commission, Gigafactory expressions of interest, https://digital-strategy.ec.europa.eu/en/news/overwhelming-response-76-respondents-express-interest-european-ai-gigafactories-initiative, accessed 2026-10-10.
- EU official languages, https://european-union.europa.eu/principles-countries-history/languages_en, accessed 2026-10-10; ELSTAT 2021 census, https://www.statistics.gr/en/2021-census-pop-hous, accessed 2026-10-10.
- Cyprus constitution (Constitute), https://www.constituteproject.org/constitution/Cyprus_2013?lang=en, accessed 2026-10-10; Cyprus Institute on Pharos-CY, https://www.cyi.ac.cy/index.php/in-focus/the-cyprus-institute-coordinates-the-cyprus-ai-factory-antenna-pharos-cy-advancing-artificial-intelligence-in-greek-language.html, accessed 2026-10-10.
- (press) Protothema, AI Act consultation, https://en.protothema.gr/2026/06/23/greece-opens-public-consultation-on-national-framework-for-regulating-ai-under-new-eu-law/; Greek City Times, https://greekcitytimes.com/2026/06/08/greece-prepares-to-shape-a-national-artificial-intelligence-policy/; CBN, https://www.cbn.com.cy/article/121443/cyprus-to-join-intergovernmental-initiative-with-greece-and-italy-to-create-ai-gigafactories; all accessed 2026-10-10.

### Hungary (HU)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Hungarian; census 2022 mother tongue: 8,302,828 of 9,603,634 (1,175,656 not answering); German 28,473, Roma 23,192, Ukrainian 15,315, Romanian 11,186, Slovak 10,123, Croatian 8,232. The Fundamental Law provision **[unverified]**. | https://nepszamlalas2022.ksh.hu/en/results/final-data/tables/nsz2022-1.1.6-eng.xlsx (accessed 2026-10-10); https://nepszamlalas2022.ksh.hu/en/results/tables (accessed 2026-10-10) |
| Language shared with | Hungarian minorities in Slovakia, Romania, Serbia and Ukraine, figures **[unverified]**; 8,533 Hungarian mother-tongue speakers in Czechia (2021). | https://scitani.gov.cz/matersky-jazyk (accessed 2026-10-10) |
| EuroHPC system on national soil | Levente: hosting agreement with DKF in Budapest (9 July 2025), at least 23 PFlops, EUR 42 million with EuroHPC up to 35%; not yet procured; HUN-REN cites 2027. The national system in service is Komondor (5 PFlops, Debrecen, since the end of 2022), operated by DKF since 1 January 2025. | https://eurohpc-ju.europa.eu/way-open-building-eurohpc-world-class-supercomputer-hungary-2025-07-09_en (accessed 2026-10-10); https://hun-ren.hu/research_news/hungarian-style-ai-from-competence-to-impact-from-impact-to-the-future-109042 (accessed 2026-10-10); https://hirek.unideb.hu/en/node/14153 (accessed 2026-10-10); https://ncc.dkf.hu/ (accessed 2026-10-10) |
| EuroHPC AI Factory | No factory; the antenna HunAIFA, selected 13 October 2025, linked to Germany's JUPITER AI Factory with access to the HUN-REN Cloud, coordinated by HUN-REN SZTAKI with Wigner, ELTE and others; about EUR 10 million over three years, shared equally with EuroHPC. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en (accessed 2026-10-10); https://hun-ren.hu/hunren_news/ai-factory-antenna-programme-109669 (accessed 2026-10-10) |
| AI Gigafactory | No Hungarian bid found **[unverified]**. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en (accessed 2026-10-10) |
| National or regional model efforts | PULI (HUN-REN Hungarian Research Centre for Linguistics): PULI GPT-3SX (2022, 32 billion words, free for non-profit research); PULI-LlumiX-32K (continued pretraining of LLaMA-2 on 7.9 billion Hungarian words, Llama 2 licence); PULI-LlumiX-Llama-3.1 (8.7 billion Hungarian words, Llama 3.1 licence); funders **[unverified]**. Racka-4B (ELTE, Qwen3-4B base, trained on Komondor, non-commercial because of unchecked web data) is press only **[unverified]**. | https://hun-ren.hu/en/news/a-new-level-in-artificial-intelligence-based-research-for-the-hungarian-language (accessed 2026-10-10); https://huggingface.co/NYTK/PULI-LlumiX-32K (accessed 2026-10-10); https://huggingface.co/NYTK/PULI-LlumiX-Llama-3.1 (accessed 2026-10-10); (press) https://telex.hu/techtud/2026/07/05/mesterseges-intelligenica-magyar-fejlesztes-racka-elte-mynds-ai-llm (accessed 2026-10-10) |
| National AI strategy | Hungary's AI Strategy 2020 to 2030 (September 2020), with Hungarian language-processing technologies for administrative procedures among its targets and training datasets to be collected by two ministries. A 2025 update is press only **[unverified]**. | https://ai-watch.ec.europa.eu/countries/hungary/hungary-ai-strategy-report_en (accessed 2026-10-10) |
| Public-sector LLM use | The 2020 strategy foresaw an AI telephone customer service at NISZ; no LLM-based assistant or model procurement found **[unverified]**. | https://ai-watch.ec.europa.eu/countries/hungary/hungary-ai-strategy-report_en (accessed 2026-10-10) |
| Language resources | HunCLARIN at the Research Centre for Linguistics with seven members; the Hungarian National Corpus size and CLARIN ERIC status **[unverified]**. | https://clarin.hu/ (accessed 2026-10-10); https://clarin.hu/en (accessed 2026-10-10) |
| Key institutions | HUN-REN Research Centre for Linguistics (PULI, HunCLARIN); HUN-REN SZTAKI (antenna); HUN-REN Wigner; ELTE; DKF (Komondor, Levente host). | https://hun-ren.hu/hunren_news/ai-factory-antenna-programme-109669 (accessed 2026-10-10); https://ncc.dkf.hu/ (accessed 2026-10-10) |
| Power and grid | Komondor is liquid-cooled with waste heat reused at a Debrecen pool; grid figures **[unverified]**. This repository's fundamentals record one of the higher electricity prices in the 27. | https://ncc.dkf.hu/hu/a-komondor-a-vilag-egyik-legzoldebb-szuperszamitogepe.html (accessed 2026-10-10) |

#### What good enough means here
Hungarian for 8.3 million citizens in Hungary and for the Hungarian-speaking minorities in four neighbouring
states, in the registers of administration, courts and health. Hungarian is shared with no other member state
as a majority language, so the national model is Hungary's to build; the research centre has already done the
continued pretraining three times, and the state has a strategy that names the goal.

#### Recommended strategy
**R1, institutionalised at the linguistics centre; R2 through the antenna and JUPITER for compute; R4 with
terms. No factory needed.**

1. **Fund PULI as the national programme (R1, B5).** Three generations exist with no stated funder. The 2020
   strategy's language-technology objective is the hook; a recurring line at the HUN-REN Research Centre for
   Linguistics, with a release cadence, turns a research series into the state's model.
2. **Move off the Llama licences for the deployed version (B3).** The current PULI generations carry Llama 2
   and Llama 3.1 licences; the public-service version should be continued-pretrained on a base whose licence
   permits indefinite state use and modification, with the weights held in a state repository.
3. **Use the antenna and JUPITER for training until Levente runs (R2 compute).** HunAIFA's link to the
   JUPITER AI Factory and the EuroHPC access calls cover a continued-pretraining run of the size PULI has
   done; Komondor carries the tuning. Levente, when procured, becomes the national home.
4. **Collect the administrative corpus the strategy promised (B4).** The 2020 strategy assigned training
   datasets to two ministries; the national register of what the model was trained on, with licences, is the
   deliverable that makes the model deployable.
5. **Deploy one service under the state's rules (B2) and build the evaluation set from it (B6).** No pilot was
   found; a NISZ citizen service on the national model is the natural first.
6. **Offer the model to the minorities' administrations (R2, as supplier)** in Slovakia, Romania and Serbia,
   where Hungarian-language public services exist in law and no other model will serve them.
7. **Procure frontier access with terms (R4)**, PULI as the fallback.

#### What it does not need to do
Host a factory, bid for a Gigafactory, or pretrain from scratch: 8.7 billion words of continued pretraining
is the right scale, and the antenna plus Komondor plus Levente is enough compute.

#### Main blocker, and what would change the recommendation
No funder is named for the models, the deployed licences are restrictive, and Levente is not yet procured.
The recommendation would change if a 2025 strategy update funds PULI (R1 is settled), or if Levente's
procurement slips well past 2027 (the antenna and the access calls stay the training home and nothing else
changes).

#### Sources
- KSH, Census 2022 table 1.1.6, https://nepszamlalas2022.ksh.hu/en/results/final-data/tables/nsz2022-1.1.6-eng.xlsx, index https://nepszamlalas2022.ksh.hu/en/results/tables, accessed 2026-10-10; ČSÚ, https://scitani.gov.cz/matersky-jazyk, accessed 2026-10-10.
- EuroHPC JU, Levente hosting agreement, https://eurohpc-ju.europa.eu/way-open-building-eurohpc-world-class-supercomputer-hungary-2025-07-09_en, accessed 2026-10-10; antennas, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en, accessed 2026-10-10.
- HUN-REN, antenna programme, https://hun-ren.hu/hunren_news/ai-factory-antenna-programme-109669, accessed 2026-10-10; Hungarian-style AI, https://hun-ren.hu/research_news/hungarian-style-ai-from-competence-to-impact-from-impact-to-the-future-109042, accessed 2026-10-10; PULI GPT-3SX, https://hun-ren.hu/en/news/a-new-level-in-artificial-intelligence-based-research-for-the-hungarian-language, accessed 2026-10-10.
- NYTK, PULI-LlumiX-32K, https://huggingface.co/NYTK/PULI-LlumiX-32K, accessed 2026-10-10; PULI-LlumiX-Llama-3.1, https://huggingface.co/NYTK/PULI-LlumiX-Llama-3.1, accessed 2026-10-10.
- AI Watch, Hungary AI strategy report, https://ai-watch.ec.europa.eu/countries/hungary/hungary-ai-strategy-report_en, accessed 2026-10-10.
- DKF, HPC competence centre, https://ncc.dkf.hu/, accessed 2026-10-10; Komondor, https://ncc.dkf.hu/hu/a-komondor-a-vilag-egyik-legzoldebb-szuperszamitogepe.html, accessed 2026-10-10; University of Debrecen, https://hirek.unideb.hu/en/node/14153, accessed 2026-10-10.
- CLARIN Hungary, https://clarin.hu/ and https://clarin.hu/en, accessed 2026-10-10.
- (press) Telex, Racka, https://telex.hu/techtud/2026/07/05/mesterseges-intelligenica-magyar-fejlesztes-racka-elte-mynds-ai-llm, accessed 2026-10-10.

### Ireland (IE)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Irish is the first official language and English the second (Constitution Art. 8); Irish an official EU language since 2007. Census 2022: 1,873,997 people aged 3 and over could speak Irish, 553,965 of them only within education; 65,156 speakers in the Gaeltacht. | https://www.irishstatutebook.ie/eli/cons/en/html (accessed 2026-10-10); https://www.cso.ie/en/releasesandpublications/ep/p-cpp8/censusofpopulation2022profile8-theirishlanguageandeducation/keyfindings/ (accessed 2026-10-10); https://european-union.europa.eu/principles-countries-history/languages_en (accessed 2026-10-10) |
| Language shared with | English with Malta and the wider world; Irish with Northern Ireland. Diaspora figures **[unverified]**. | https://european-union.europa.eu/principles-countries-history/languages_en (accessed 2026-10-10); https://www.adaptcentre.ie/news-and-events/innovative-irish-language-and-ai-initiatives-launched-in-dcu (accessed 2026-10-10) |
| EuroHPC system on national soil | CASPIr: hosting agreement with the University of Galway signed 13 October 2025, to be operated by ICHEC, mid-range, over 15 PFlops, for AI and machine-learning workloads; invitation to tender of 27 March 2026, up to EUR 25 M, EuroHPC 35% and Ireland 65%. No award found **[unverified]**. | https://www.eurohpc-ju.europa.eu/way-open-building-eurohpc-world-class-supercomputer-ireland-2025-10-13_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/invitation-tender-procure-caspir-supercomputer-2026-03-27_en (accessed 2026-10-10); https://www.ichec.ie/node/1115 (accessed 2026-10-10) |
| EuroHPC AI Factory | Antenna "AIF IRL-Antenna", selected 13 October 2025, led by ICHEC with CeADAR, EUR 10 M co-funded evenly by the EU and DFHERIS, linked to AI2F (France, with access to the Alice Recoque exascale system) and the Luxembourg AI Factory; an AI sandbox and a secure data environment for start-ups, SMEs and the public sector. Ireland is not a full AI Factory host. | https://www.ichec.ie/node/1114 (accessed 2026-10-10); https://www.gov.ie/en/department-of-further-and-higher-education-research-innovation-and-science/press-releases/minister-lawless-welcomes-the-successful-outcome-of-the-irish-ai-factory-antenna-bid-and-passing-major-milestone-towards-securing-a-supercomputer **[unverified]** (accessed 2026-10-10); https://eurohpc-ju.europa.eu/ai-factories_en (accessed 2026-10-10) |
| AI Gigafactory | No Irish bid, expression of interest or position found on any official page **[unverified]**; press lists Ireland among the states in the joint procurement. | (press) https://www.parapolitika.gr/diethni/article/1770236/ (accessed 2026-10-10) |
| National or regional model efforts | UCCIX, an open Irish-language LLM on Llama 2-13B from University College Cork (May 2024); funder and weights availability **[unverified]**. eSTÓR at ADAPT (DCU): EUR 900,000 over three years from the Gaeltacht department, announced 21 November 2025, to "develop new neural language models suited to Irish" and evaluation sets; no named model yet **[unverified]**. Gaois (DCU): up to EUR 4,013,886 for 2026 to 2029 for the national corpus and other resources, including "a structured supply of information … to AI models". | https://arxiv.org/abs/2405.13010 (accessed 2026-10-10); https://www.gov.ie/en/department-of-rural-and-community-development-and-the-gaeltacht/press-releases/minister-calleary-announces-49m-in-funding-for-irish-language-digital-projects-in-dublin-city-university/ (accessed 2026-10-10); https://www.adaptcentre.ie/news-and-events/innovative-irish-language-and-ai-initiatives-launched-in-dcu (accessed 2026-10-10) |
| National AI strategy | "AI – Here for Good" (2021), refreshed 6 November 2024: AI Act implementation, a regulatory sandbox, a "safe space" for civil servants to experiment, access to advanced AI computing; no national-model action. A further update during 2025 was announced; its outcome **[unverified]**. | https://www.gov.ie/en/department-of-enterprise-tourism-and-employment/publications/national-ai-strategy-refresh-2024/ (accessed 2026-10-10); https://enterprise.gov.ie/en/publications/national-ai-strategy-refresh-2024.html (accessed 2026-10-10) |
| Public-sector LLM use | Guidelines for the responsible use of AI in the public service, 8 May 2025, citing the Revenue Commissioners "using Large Language Models to route taxpayer queries". Procurement of specific models **[unverified]**. | https://www.gov.ie/en/department-of-public-expenditure-infrastructure-public-service-reform-and-digitalisation/press-releases/minister-chambers-launches-guidelines-on-the-use-of-ai-for-better-public-services/ (accessed 2026-10-10); https://www.ichec.ie/node/1114 (accessed 2026-10-10) |
| Language resources | Corpas, the National Corpus of the Irish Language (Gaois, DCU); eSTÓR, a bilingual repository of public-body text feeding the Commission's eTranslation. Ireland is not listed as a CLARIN ERIC member. | https://www.gov.ie/en/department-of-rural-and-community-development-and-the-gaeltacht/press-releases/minister-calleary-announces-49m-in-funding-for-irish-language-digital-projects-in-dublin-city-university/ **[unverified]** (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Key institutions | ICHEC (University of Galway; CASPIr operator; antenna lead); CeADAR (applied AI centre, antenna partner); ADAPT (TCD and DCU; eSTÓR); Gaois (DCU); UCC. | https://www.ichec.ie/node/1114 (accessed 2026-10-10); https://www.ceadar.ie/ (accessed 2026-10-10); https://www.adaptcentre.ie/about/ (accessed 2026-10-10) |
| Power and grid | Binding. The CRU records data centres rising from about 5% of electricity demand in 2015 to 21% in 2023 and 85% of demand growth; decision CRU2025236 of 12 December 2025 requires new data centres to provide new renewable and dispatchable generation. This repository's fundamentals record the highest electricity price in the 27 and an isolated grid. | https://consult.cru.ie/en/consultation/review-large-energy-users-connection-policy (accessed 2026-10-10); https://cru.ie/publications/28573 (accessed 2026-10-10) |

#### What good enough means here
Two different problems. For English, every open-weight model already meets B1, and the state's question is only
B2 to B6: hosting under its rules, continuity, provenance, cost and evaluation. For Irish, the first official
language, no open model is good enough today: the corpus is small, most speakers use the language only in
education, and the state's obligation to serve in Irish is constitutional. "Good enough" for Ireland means an
English-capable model the state controls, and an Irish capability built deliberately on top of it.

#### Recommended strategy
**R1 for Irish on an English-strong open base; R2 for compute through the antenna until CASPIr runs; R4 with
terms for English-language services. Not R3, and no national training cluster.**

1. **Build the Irish capability as a continued-pretraining and tuning programme (R1), institutionally at
   ADAPT and ICHEC.** The state has just funded the inputs: Corpas and the Gaois resources with an explicit data
   supply to AI models, and eSTÓR's remit to develop Irish neural language models. UCCIX showed the technique on
   Llama 2. The next step is one named programme that owns the Irish evaluation set (B6), the rights-cleared Irish
   corpus (B4), and a release schedule on an open-licensed base, with the weights held by the state (B3).
2. **Use the antenna's compute and partners for training, not a national cluster (R2).** The antenna gives
   access to the French and Luxembourg factories, and CASPIr arrives later; Irish-language continued pretraining
   is weeks of accelerator time, which these cover. The CRU's connection policy makes any new large load a
   generation-building obligation, and a training cluster is the wrong thing to spend that on.
3. **Serve English-language public services from a procured model under terms (R4), hosted in-state or in the
   EU under the state's approved environments (B2).** Ireland hosts more hyperscale capacity than most states;
   the terms, not the location, are what the state lacks: continuity, escrow or a national fallback, evaluation
   on a national set before each version.
4. **Keep one national model as the fallback for both languages.** An English-strong open base, tuned on
   Irish public-service text and the Irish corpus, held and served by the state, is the continuity guarantee
   behind every procured model (B3), and the vehicle for Irish (B1).
5. **Write the national model into the strategy update.** The 2024 refresh names compute access and a safe
   space for civil servants but no model; the 2025 update is the place for the Irish programme and the
   procurement terms.

#### What it does not need to do
Pretrain from scratch, host a full AI Factory, bid for a Gigafactory, or build training capacity on the Irish
grid. It does not need to improve English-language capability; it needs to own what it uses.

#### Main blocker, and what would change the recommendation
The grid: the CRU decision ties any new data-centre load to new generation, which rules out a national training
cluster for the foreseeable future and makes the antenna and CASPIr the only compute path. The second blocker
is that no Irish-language programme has yet named a model, a base or a licence. The recommendation would change
if eSTÓR publishes a model and evaluation set (R1 becomes a question of institutionalising it), or if CASPIr is
procured and operational (training moves onto national soil).

#### Sources
- Irish Statute Book, Constitution of Ireland, https://www.irishstatutebook.ie/eli/cons/en/html, accessed 2026-10-10.
- CSO, Census 2022 Profile 8, https://www.cso.ie/en/releasesandpublications/ep/p-cpp8/censusofpopulation2022profile8-theirishlanguageandeducation/keyfindings/, accessed 2026-10-10.
- EuroHPC JU, CASPIr hosting agreement, https://www.eurohpc-ju.europa.eu/way-open-building-eurohpc-world-class-supercomputer-ireland-2025-10-13_en, accessed 2026-10-10; invitation to tender, https://www.eurohpc-ju.europa.eu/invitation-tender-procure-caspir-supercomputer-2026-03-27_en, accessed 2026-10-10.
- ICHEC, AI Factory Antenna, https://www.ichec.ie/node/1114, accessed 2026-10-10; CASPIr, https://www.ichec.ie/node/1115, accessed 2026-10-10.
- gov.ie (DFHERIS), antenna outcome, https://www.gov.ie/en/department-of-further-and-higher-education-research-innovation-and-science/press-releases/minister-lawless-welcomes-the-successful-outcome-of-the-irish-ai-factory-antenna-bid-and-passing-major-milestone-towards-securing-a-supercomputer **[unverified]**, accessed 2026-10-10.
- gov.ie (DETE), National AI Strategy Refresh 2024, https://www.gov.ie/en/department-of-enterprise-tourism-and-employment/publications/national-ai-strategy-refresh-2024/ **[unverified]**, accessed 2026-10-10; mirror https://enterprise.gov.ie/en/publications/national-ai-strategy-refresh-2024.html, accessed 2026-10-10.
- gov.ie (DPENDR), public-service AI guidelines, https://www.gov.ie/en/department-of-public-expenditure-infrastructure-public-service-reform-and-digitalisation/press-releases/minister-chambers-launches-guidelines-on-the-use-of-ai-for-better-public-services/ **[unverified]**, accessed 2026-10-10.
- gov.ie (DRCDG), Irish-language digital projects funding, https://www.gov.ie/en/department-of-rural-and-community-development-and-the-gaeltacht/press-releases/minister-calleary-announces-49m-in-funding-for-irish-language-digital-projects-in-dublin-city-university/ **[unverified]**, accessed 2026-10-10.
- ADAPT Centre, eSTÓR launch, https://www.adaptcentre.ie/news-and-events/innovative-irish-language-and-ai-initiatives-launched-in-dcu, accessed 2026-10-10; About, https://www.adaptcentre.ie/about/, accessed 2026-10-10.
- CeADAR, https://www.ceadar.ie/, accessed 2026-10-10.
- arXiv, UCCIX, https://arxiv.org/abs/2405.13010, accessed 2026-10-10.
- CRU, Large Energy Users connection policy consultation, https://consult.cru.ie/en/consultation/review-large-energy-users-connection-policy, accessed 2026-10-10; decision CRU2025236, https://cru.ie/publications/28573, accessed 2026-10-10.
- EuroHPC JU, AI Factories, https://eurohpc-ju.europa.eu/ai-factories_en, accessed 2026-10-10; CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10; EU languages, https://european-union.europa.eu/principles-countries-history/languages_en, accessed 2026-10-10.
- (press) Parapolitika, https://www.parapolitika.gr/diethni/article/1770236/ **[unverified]**, accessed 2026-10-10.

### Italy (IT)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Italian (Law 482/1999 art. 1); twelve protected minority languages including French, Franco-Provençal, Friulian, Ladin, Occitan, Sardinian, German, Slovene, Croatian, Albanian, Greek and Catalan (art. 2). Population 58,943,464 (Eurostat, 1 January 2025, provisional); speaker counts **[unverified]**. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-15;482 (accessed 2026-10-10); https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-15;482~art2 (accessed 2026-10-10) |
| Language shared with | Italian-speaking communities abroad **[unverified]** from an official page. | https://huggingface.co/Almawave/Velvet-14B (accessed 2026-10-10) |
| EuroHPC system on national soil | Leonardo at CINECA, Bologna, operational, 249.04 PFlops sustained, 13,824 Ampere GPUs; the LISA upgrade inaugurated June 2026. | https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories/italy_en (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: IT4LIA, selected 10 December 2024, hosted by CINECA at the Bologna Tecnopolo with Austria and Slovenia; the successor system contracted 22 April 2026 with E4 and Dell, EUR 290 million, 50% EuroHPC, NVIDIA GB200, over 160 EFlops of peak AI inference, an inference partition on European accelerators; services "to be confirmed". Serbia's and Switzerland's antennas attach to it. | https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-boost-ai-capabilities-it4lia-ai-factory-2026-04-22_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en (accessed 2026-10-10) |
| AI Gigafactory | Press only: a national proposal with Eni and Leonardo sites, a first phase of 95 MW and a larger tier in preparation **[unverified]**; no selection yet. | (press) https://www.fortuneita.com/?p=372395 (accessed 2026-10-10); (press) https://www.corrierecomunicazioni.it/?p=349245 (accessed 2026-10-10) |
| National or regional model efforts | Minerva-7B (Sapienza NLP with CINECA and Babelscape): almost 2.5 trillion tokens, 1.14 trillion Italian, pretrained from scratch, funded by the PNRR FAIR project, Apache-2.0 (December 2024). Velvet-14B (Almawave, private): trained on Leonardo on over 4 trillion tokens in six languages, Apache-2.0 (January 2025). Italia (iGenius): gated, **[unverified]**. The EUROPA consortium led by the Italian company Domyn won the Frontier AI Grand Challenge on 19 June 2026 (section 4). | https://huggingface.co/sapienzanlp/Minerva-7B-instruct-v1.0 (accessed 2026-10-10); https://huggingface.co/Almawave/Velvet-14B (accessed 2026-10-10); https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open (accessed 2026-10-10) |
| National AI strategy | The Italian AI Strategy 2024 to 2026 (22 July 2024), four areas including public administration. Law 132 of 23 September 2025, in force 10 October 2025: the Presidency of the Council prepares a strategy approved at least every two years (art. 19); AgID and ACN are the national AI authorities (art. 20); up to EUR 1 billion of equity investment authorised (art. 23); public administrations use AI in a supporting role with a human responsible (art. 14). | https://innovazione.gov.it/notizie/articoli/strategia-italiana-per-l-intelligenza-artificiale-2024-2026/ (accessed 2026-10-10); https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-09-23;132 (accessed 2026-10-10); https://www.gazzettaufficiale.it/eli/gu/2025/09/25/223/sg/pdf (accessed 2026-10-10) |
| Public-sector LLM use | Law 132/2025 art. 14 frames public-administration use; specific pilots or procurements **[unverified]** (AgID pages refused fetches). | https://www.gazzettaufficiale.it/eli/gu/2025/09/25/223/sg/pdf (accessed 2026-10-10) |
| Language resources | CLARIN-IT (CNR's Zampolli institute); Minerva's Italian pretraining data described as open; the FAIR foundation under the PNRR. | https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10); https://huggingface.co/sapienzanlp/Minerva-7B-instruct-v1.0 (accessed 2026-10-10) |
| Key institutions | CINECA (Leonardo, IT4LIA); Sapienza NLP and Babelscape (Minerva); the FAIR foundation; AI4I; AgID and ACN; the Department for Digital Transformation; CNR ILC; Almawave; Domyn. | https://www.eurohpc-ju.europa.eu/ai-factories/italy_en (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Power and grid | Press only for the Gigafactory's megawatts **[unverified]**. This repository's fundamentals record one of the higher electricity prices in the 27 and a high seismic classification. | https://www.eurohpc-ju.europa.eu/ai-factories/italy_en (accessed 2026-10-10) |

#### What good enough means here
Italian for fifty-nine million citizens, with twelve protected minority languages the state must serve where
they are spoken, in the registers of administration, courts and health. Italy has a pre-exascale system, a
factory with the largest AI contract in this note, an open Italian model pretrained from scratch with public
money, a law that names the strategy owner and the regulators, and the company leading the EU's
24-language frontier project; it has no state-deployed model and no stated public-sector pilot.

#### Recommended strategy
**R1 on Minerva's line, institutionalised; the factory and the EUROPA model as the R2 base; R4 with terms;
R3 as a national choice tied to the Gigafactory, kept separate.**

1. **Turn Minerva into the state's model (R1, B3, B5).** It was funded by a recovery-plan research project
   and released under Apache-2.0; the FAIR foundation's horizon is the PNRR's. Law 132's biennial strategy
   is the vehicle to name an owner, a recurring line and a deploying customer, with the weights and corpus
   register held by the state.
2. **Train the next generations on IT4LIA's new system (B2).** The contracted successor to Leonardo is
   the training home; until it runs, Leonardo, as Velvet and Minerva showed.
3. **Treat the EUROPA model as a base to adapt, not a programme to wait for (R2).** When the 24-language model
   exists, the Italian-register stage on it belongs to the national programme; the state should secure rights
   to the weights through the Commission's open-model terms and its own evaluation seat.
4. **Deploy one service under art. 14 and build the evaluation set (B2, B6).** No pilot was confirmed; AgID,
   as national AI authority, should name one and publish the evaluation set, so every procured model is
   scored against real administrative questions.
5. **Serve the minority languages through the neighbours' models (R2, as customer).** Slovene (GaMS), German,
   French (Lucie) and Croatian are covered by other states' programmes; a serving copy under agreed terms is
   cheaper than twelve Italian minority-language stages.
6. **Procure frontier access with terms (R4)**, Minerva as the fallback.
7. **Keep the Gigafactory separate.** Press-only today; if selected it gives Italy frontier-class training,
   and the citizen model neither waits for it nor is argued through it.

#### What it does not need to do
Start a new model programme, or treat the frontier project it leads as the citizen model: the mid-scale line
exists and the factory is funded. It does not need the Gigafactory to meet the bar.

#### Main blocker, and what would change the recommendation
No state-deployed model and no funded owner for Minerva beyond the research project; public-sector pilots
could not be confirmed. The recommendation would change if the biennial strategy under Law 132 names a
model programme and customer (R1 is settled), or if the Gigafactory is selected (R3 becomes a choice to cost
separately).

#### Sources
- Normattiva, Law 482/1999, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-15;482 and art. 2, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-15;482~art2, accessed 2026-10-10; Law 132/2025, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-09-23;132, accessed 2026-10-10; Gazzetta Ufficiale, https://www.gazzettaufficiale.it/eli/gu/2025/09/25/223/sg/pdf, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en, accessed 2026-10-10; Italy AI Factory, https://www.eurohpc-ju.europa.eu/ai-factories/italy_en, accessed 2026-10-10; first seven AI Factories, https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en, accessed 2026-10-10; IT4LIA contract, https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-boost-ai-capabilities-it4lia-ai-factory-2026-04-22_en, accessed 2026-10-10; antennas, https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en, accessed 2026-10-10.
- Sapienza NLP, Minerva-7B, https://huggingface.co/sapienzanlp/Minerva-7B-instruct-v1.0, accessed 2026-10-10; Almawave, Velvet-14B, https://huggingface.co/Almawave/Velvet-14B, accessed 2026-10-10.
- European Commission, EUROPA consortium, https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open, accessed 2026-10-10.
- Department for Digital Transformation, strategy 2024 to 2026, https://innovazione.gov.it/notizie/articoli/strategia-italiana-per-l-intelligenza-artificiale-2024-2026/, accessed 2026-10-10.
- CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10.
- (press) Fortune Italia, https://www.fortuneita.com/?p=372395; Corriere Comunicazioni, https://www.corrierecomunicazioni.it/?p=349245; both accessed 2026-10-10.

### Latvia (LV)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Latvian; population 1,856,932 (Eurostat 2025 via the EU country page); census speaker shares **[unverified]** (the statistics page returned 404). TildeOpen used 29 billion words of Latvian text. | https://european-union.europa.eu/principles-countries-history/eu-countries/latvia_en (accessed 2026-10-10); https://www.researchlatvia.gov.lv/en/world-class-ai-model-european-languages-developed-latvia (accessed 2026-10-10) |
| Language shared with | No official page fetched **[unverified]**; Latvian is among TildeOpen's 34 languages. | https://huggingface.co/TildeAI/TildeOpen-30b (accessed 2026-10-10) |
| EuroHPC system on national soil | None found (the EuroHPC Latvia page returned 404) **[unverified]** as absence; Latvia is not in the LUMI consortium. | https://www.lumi-supercomputer.eu/about-lumi/ (accessed 2026-10-10) |
| EuroHPC AI Factory | No factory; the antenna AIFA-LAT, led by Riga Technical University with the University of Latvia, the State Digital Development Agency and others, EUR 8.4 million for 2026 to 2028 with EUR 3.98 million national co-funding, linked to the LUMI AI Factory; aims at a national AI competence centre with language technologies among its niches and "several million AI training hours for the public sector". | https://www.izm.gov.lv/en/article/latvia-joins-european-artificial-intelligence-factories-network-strengthening-science-innovation-and-digital-literacy (accessed 2026-10-10); https://digital-strategy.ec.europa.eu/en/news/eu-announces-ai-factories-antennas-across-member-states-and-partner-countries (accessed 2026-10-10) |
| AI Gigafactory | A proposal: the Ministry of Economics reported (8 October 2025) a conceptual proposal by the Finnish provider DataCrunch with Latvian ICT companies for an AI data park on renewable energy, a second Latvian project, and the possibility of a joint Latvian and Finnish bid; status under the formal call **[unverified]**. | https://www.em.gov.lv/en/article/latvia-and-finland-could-jointly-propose-ai-gigaproject-european-support-competition (accessed 2026-10-10) |
| National or regional model efforts | TildeOpen (Tilde, Riga, private): a 30B dense model over 34 languages including the Baltic and Nordic ones, 2 trillion tokens, trained on LUMI with 768 MI250X GPUs under the EuroHPC Large AI Grand Challenge, CC-BY-4.0, released September 2025, long-context update April 2026, "not a ready-made chatbot"; no Latvian government role described. | https://huggingface.co/TildeAI/TildeOpen-30b (accessed 2026-10-10); https://tilde.ai/?p=20213 (accessed 2026-10-10); https://tilde.ai/?p=26124 (accessed 2026-10-10) |
| National AI strategy | The Artificial Intelligence Centre Law, adopted by the Saeima on 6 March 2025, creating a statutory AI Centre with the environment, economics and defence ministries as founders and oversight by the State Digital Development Agency; the 2020 report and the digital guidelines **[unverified]**. | https://perseus-prx1.saeima.lv/en/news/saeima-news/34443-saeima-approves-the-creation-of-an-artificial-intelligence-technology-ecosystem-in-latvia (accessed 2026-10-10) |
| Public-sector LLM use | A memorandum with Microsoft (3 December 2024) supporting the national AI centre and a first pilot in the investment agency's processes; the antenna promises public-sector training hours; the state language platform hugo.gov.lv loaded no content **[unverified]**. | https://www.varam.gov.lv/en/article/latvia-and-microsoft-collaborate-advance-artificial-intelligence-innovation (accessed 2026-10-10); https://www.izm.gov.lv/en/article/latvia-joins-european-artificial-intelligence-factories-network-strengthening-science-innovation-and-digital-literacy (accessed 2026-10-10) |
| Language resources | CLARIN-LV at IMCS, University of Latvia, a B-centre since 2023, funded partly by the recovery plan's language-technology initiative; the Latvian National Corpora Collection at korpuss.lv, including a 403.6-million-word web corpus. | https://www.clarin.lv/ (accessed 2026-10-10); https://korpuss.lv/en (accessed 2026-10-10) |
| Key institutions | Tilde; IMCS at the University of Latvia; Riga Technical University (antenna lead); the AI Centre; the State Digital Development Agency; VARAM. An HPC centre **[unverified]**. | https://www.clarin.lv/ (accessed 2026-10-10); https://www.izm.gov.lv/en/article/latvia-joins-european-artificial-intelligence-factories-network-strengthening-science-innovation-and-digital-literacy (accessed 2026-10-10) |
| Power and grid | No official data fetched **[unverified]**; the Gigafactory proposal speaks of renewable energy. This repository's fundamentals record a frontline state. | https://www.em.gov.lv/en/article/latvia-and-finland-could-jointly-propose-ai-gigaproject-european-support-competition (accessed 2026-10-10) |

#### What good enough means here
Latvian for 1.9 million citizens, with a large Russian-speaking population, in the registers of
administration, courts and health. Latvia's position is unusual: the largest open model built on a EuroHPC
system for the Baltic languages was made by a Riga company with Commission compute, under a licence the
state can build on, and the state has no visible role in it; a statutory AI Centre exists by law, an antenna
to Finland's factory is funded, and the public sector's first partnership is with an American vendor.

#### Recommended strategy
**R1 on TildeOpen as the base, held by the AI Centre; R2 through the antenna and the Finnish pool; R4 with
terms.**

1. **Adopt TildeOpen as the national base and hold a state copy (B3).** CC-BY-4.0 permits it; a model that
   already knows Latvian from 29 billion words is the cheapest start any small-language state in this note
   has. The AI Centre should hold the weights and recipe, commission Tilde or IMCS for the Latvian
   public-service tuning stage, and own the result.
2. **Use the antenna's public-sector training hours for exactly this (R2 compute).** AIFA-LAT promises
   several million training hours for the public sector on LUMI; the Latvian-register stage and the
   evaluation runs fit inside them.
3. **Build the national corpus register and evaluation set at IMCS (B4, B6).** CLARIN-LV and korpuss.lv are
   the register; the evaluation set comes from the first state service on the national model.
4. **Deploy under the state's rules (B2).** The Microsoft memorandum is the current path for pilots; the
   national model should be served from the state's own environment as the fallback, with the procured
   model primary where it is better, both scored on the same set.
5. **Pool with Finland and Estonia (R2).** TildeOpen already covers the region's languages; a Finno-Baltic
   continued-pretraining run on LUMI-AI with Latvia's corpus keeps the base current. Rights in the agreement
   first.
6. **Serve Russian-speaking residents deliberately,** as for Estonia: say which route covers them, and
   evaluate it.
7. **Procure frontier access with terms (R4)**, the national tuning as fallback; the Gigafactory, whether as
   host of a data park or as purchaser, is a separate industrial choice.

#### What it does not need to do
Host EuroHPC compute, pretrain its own base, or wait for the Gigafactory: a Latvian-capable open base exists
and the antenna's hours cover the rest.

#### Main blocker, and what would change the recommendation
No state programme owns a Latvian model, and the strategy on the record is an institutional law rather than
a plan with a budget line. The recommendation would change if the AI Centre is funded with a model line
(R1 proceeds at once), or if Tilde changes TildeOpen's licence or stops releases (the pool with Finland
becomes the base instead).

#### Sources
- European Union, Latvia, https://european-union.europa.eu/principles-countries-history/eu-countries/latvia_en, accessed 2026-10-10; Research Latvia, TildeOpen, https://www.researchlatvia.gov.lv/en/world-class-ai-model-european-languages-developed-latvia, accessed 2026-10-10.
- Ministry of Education and Science, AIFA-LAT, https://www.izm.gov.lv/en/article/latvia-joins-european-artificial-intelligence-factories-network-strengthening-science-innovation-and-digital-literacy, accessed 2026-10-10; European Commission, antennas, https://digital-strategy.ec.europa.eu/en/news/eu-announces-ai-factories-antennas-across-member-states-and-partner-countries, accessed 2026-10-10.
- Ministry of Economics, Gigafactory, https://www.em.gov.lv/en/article/latvia-and-finland-could-jointly-propose-ai-gigaproject-european-support-competition, accessed 2026-10-10.
- TildeAI, TildeOpen-30b, https://huggingface.co/TildeAI/TildeOpen-30b, accessed 2026-10-10; Tilde, release, https://tilde.ai/?p=20213, accessed 2026-10-10; update, https://tilde.ai/?p=26124, accessed 2026-10-10.
- Saeima, AI Centre Law, https://perseus-prx1.saeima.lv/en/news/saeima-news/34443-saeima-approves-the-creation-of-an-artificial-intelligence-technology-ecosystem-in-latvia, accessed 2026-10-10; VARAM, Microsoft memorandum, https://www.varam.gov.lv/en/article/latvia-and-microsoft-collaborate-advance-artificial-intelligence-innovation, accessed 2026-10-10.
- CLARIN-LV, https://www.clarin.lv/, accessed 2026-10-10; korpuss.lv, https://korpuss.lv/en, accessed 2026-10-10; LUMI, about, https://www.lumi-supercomputer.eu/about-lumi/, accessed 2026-10-10.

### Lithuania (LT)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Lithuanian; population 2,890,664 (Eurostat 2025 via the EU country page); census speaker shares **[unverified]** (statistics pages refused). | https://european-union.europa.eu/principles-countries-history/eu-countries/lithuania_en (accessed 2026-10-10) |
| Language shared with | No official page fetched **[unverified]**; Lithuanian is among TildeOpen's 34 languages. | https://huggingface.co/TildeAI/TildeOpen-30b (accessed 2026-10-10) |
| EuroHPC system on national soil | None yet; Lithuania is not in the LUMI consortium. The LitAI Factory's system will be the first EuroHPC-co-funded machine on Lithuanian soil. | https://www.eurohpc-ju.europa.eu/lithuania_en (accessed 2026-10-10); https://www.lumi-supercomputer.eu/about-lumi/ (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: LitAI, selected 10 October 2025, led by Vilnius University at the LRTC VDC3 data centre in Vilnius with three other universities, the State Data Agency, LRTC and the Innovation Agency, "a sovereign AI optimised infrastructure"; the university puts the value at around EUR 130 million; the EU share is reported inconsistently (EUR 65 million by press, EUR 90 million by the Commission platform) **[unverified]**; timeline not stated. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/lithuania_en (accessed 2026-10-10); https://www.ff.vu.lt/en/news/3236-lithuania-to-build-an-artificial-intelligence-factory-project-to-be-coordinated-by-vilnius-university (accessed 2026-10-10); (press) https://www.lrt.lt/en/news-in-english/19/2709522/lithuania-wins-eu-bid-to-set-up-eur130m-ai-factory (accessed 2026-10-10) |
| AI Gigafactory | A joint proposal with Poland is reported in press only **[unverified]**; Lithuania was a partner in Poland's Baltic AI GigaFactory expression of interest. | https://www.gov.pl/web/cyfryzacja/wniosek-dotyczacy-baltic-ai-gigafactory-zlozony (accessed 2026-10-10) |
| National or regional model efforts | Neurotechnology (Vilnius, private): the first open Lithuanian LLMs, Llama 2 at 7B and 13B, pretrained on over 14 billion Lithuanian tokens (August 2024); licence and funder not stated. No public national model programme found **[unverified]**; the 2026 to 2035 guidelines cite the preservation of the Lithuanian language but name no model. | https://neurotechnology.com/press_release_nlp_large_language_model_for_lithuanian.html (accessed 2026-10-10); https://digital-skills-jobs.europa.eu/en/initiatives/national-strategies/lithuania-national-artificial-intelligence-strategic-guidelines (accessed 2026-10-10) |
| National AI strategy | The National AI Strategic Guidelines for 2026 to 2035 (Ministry of the Economy and Innovation with the Innovation Agency, the digital-solutions agency and a GovAI competence centre), adopted in 2026 with four strands including infrastructure, data, compute and the state cloud; the action plan is to follow; the adoption act **[unverified]** (the ministry page refused). | https://digital-skills-jobs.europa.eu/en/initiatives/national-strategies/lithuania-national-artificial-intelligence-strategic-guidelines (accessed 2026-10-10) |
| Public-sector LLM use | A GovAI competence centre co-launched the guidelines; pilots and procurements **[unverified]**. | https://digital-skills-jobs.europa.eu/en/initiatives/national-strategies/lithuania-national-artificial-intelligence-strategic-guidelines (accessed 2026-10-10) |
| Language resources | CLARIN-LT at Vytautas Magnus University; raštija.lt, Vilnius University's integrated Lithuanian language and writing resources, including a 10,000-hour annotated speech corpus. | https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10); https://xn--ratija-ckb.lt/ (accessed 2026-10-10) |
| Key institutions | Vilnius University (LitAI lead, raštija.lt); Kaunas University of Technology; VILNIUS TECH; Vytautas Magnus University (CLARIN-LT); LRTC; the State Data Agency; the Innovation Agency; the GovAI competence centre; Neurotechnology. | https://www.eurohpc-ju.europa.eu/lithuania_en (accessed 2026-10-10); https://xn--ratija-ckb.lt/ (accessed 2026-10-10) |
| Power and grid | No official data fetched **[unverified]**. This repository's fundamentals record a frontline state. | https://www.eurohpc-ju.europa.eu/lithuania_en (accessed 2026-10-10) |

#### What good enough means here
Lithuanian for 2.9 million citizens in the registers of administration, courts and health. Lithuania is
about to have a factory of its own, described by EuroHPC as sovereign AI infrastructure, with a national
strategy adopted the same year; it has a private open model line, a speech corpus of unusual size, and no
public model programme. The order of operations matters: the factory arrives before the model it should
train.

#### Recommended strategy
**R1 funded now so the factory has a model to train; R2 with the Baltic and Polish neighbourhood; R4 with
terms.**

1. **Fund a Lithuanian model programme before the factory lands (R1, B5).** The guidelines' action plan is
   due from the Innovation Agency; it should name a programme at Vilnius University with CLARIN-LT, owning
   the corpus register (B4) and the evaluation set (B6), with the GovAI centre as customer. Neurotechnology's
   14-billion-token pretraining and TildeOpen's Lithuanian coverage show the technique and the base.
2. **Start on an existing Lithuanian-capable base, not from scratch.** TildeOpen (CC-BY-4.0) or an
   Apache-2.0 multilingual base, continued-pretrained on raštija.lt's resources and the speech corpus, held
   by the state (B3); the first run on EuroHPC access calls or Poland's PIAST, the second on LitAI.
3. **Make LitAI the training home and the public-sector serving environment (B2).** The factory's stated
   purpose is sovereign infrastructure; the national model should be its first public-sector workload.
4. **Pool with the Baltic states and Poland (R2).** Lithuania sat in Poland's Gigafactory expression of
   interest and shares TildeOpen's language set with Latvia and Estonia; a joint continued-pretraining run on
   LitAI or LUMI-AI, with rights to the weights for all, serves three small languages at the cost of one.
5. **Deploy one GovAI service and build the evaluation set from it (B6).** None was found; the first one is
   the bench.
6. **Procure frontier access with terms (R4)**, the national model as fallback; the Gigafactory is a separate
   industrial choice.

#### What it does not need to do
Pretrain from scratch, wait for the factory before starting the model, or bid to host a Gigafactory alone:
the base exists and the factory covers the training.

#### Main blocker, and what would change the recommendation
No public model programme and no action plan yet, while a large infrastructure arrives. The recommendation
would change if the action plan funds a model line at Vilnius University (R1 is settled), or if the LitAI
system slips far beyond the guidelines' horizon (then the Baltic pool on LUMI-AI is the training home).

#### Sources
- European Union, Lithuania, https://european-union.europa.eu/principles-countries-history/eu-countries/lithuania_en, accessed 2026-10-10.
- EuroHPC JU, six additional AI Factories, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en, accessed 2026-10-10; Lithuania, https://www.eurohpc-ju.europa.eu/lithuania_en, accessed 2026-10-10; LUMI, about, https://www.lumi-supercomputer.eu/about-lumi/, accessed 2026-10-10.
- Vilnius University, LitAI, https://www.ff.vu.lt/en/news/3236-lithuania-to-build-an-artificial-intelligence-factory-project-to-be-coordinated-by-vilnius-university, accessed 2026-10-10.
- Digital Skills and Jobs Platform, Lithuania guidelines, https://digital-skills-jobs.europa.eu/en/initiatives/national-strategies/lithuania-national-artificial-intelligence-strategic-guidelines, accessed 2026-10-10.
- Neurotechnology, Lithuanian LLM, https://neurotechnology.com/press_release_nlp_large_language_model_for_lithuanian.html, accessed 2026-10-10; TildeAI, TildeOpen-30b, https://huggingface.co/TildeAI/TildeOpen-30b, accessed 2026-10-10.
- raštija.lt, https://xn--ratija-ckb.lt/, accessed 2026-10-10; CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10.
- Ministry of Digital Affairs of Poland, Baltic AI GigaFactory, https://www.gov.pl/web/cyfryzacja/wniosek-dotyczacy-baltic-ai-gigafactory-zlozony, accessed 2026-10-10.
- (press) LRT, https://www.lrt.lt/en/news-in-english/19/2709522/lithuania-wins-eu-bid-to-set-up-eur130m-ai-factory, accessed 2026-10-10.

### Luxembourg (LU)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Luxembourgish is the national language and French, German and Luxembourgish the administrative languages (law of 24 February 1984), with French alone authentic in legislation; a 2018 ministry study found French spoken by 98% of residents, English 80%, German 78%, Luxembourgish 77%, with a large Portuguese-speaking community. Population 681,973 (Eurostat 2025 via the EU country page). | https://luxembourg.public.lu/en/society-and-culture/languages/languages-spoken-luxembourg.html (accessed 2026-10-10); https://european-union.europa.eu/principles-countries-history/eu-countries/luxembourg_en (accessed 2026-10-10) |
| Language shared with | French with France and Belgium; German with Germany, Austria and Belgium; Luxembourgish with no other state. | https://european-union.europa.eu/principles-countries-history/eu-countries/luxembourg_en (accessed 2026-10-10) |
| EuroHPC system on national soil | MeluXina at LuxProvide, Bissen, operational, 12.81 PFlops sustained. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: the Luxembourg AI Factory, in the first round of 10 December 2024, coordinated by LuxProvide with Luxinnovation, LNDS, the University and LIST; MeluXina-AI, over 2,100 GPU accelerators, contracted 22 July 2026 for EUR 80 million with installation from autumn 2026 on the Bissen and Bettembourg sites; the parliamentary committee report puts total investment at EUR 126 million (EUR 63 million EuroHPC, EUR 60 million national); Ireland's antenna attaches to it. | https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en (accessed 2026-10-10); https://cordis.europa.eu/project/id/101234366 (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-meluxina-ai-new-ai-optimised-supercomputer-luxembourg-ai-factory-2026-07-22_en (accessed 2026-10-10); https://wdocs-pub.chd.lu/docs/Dossiers_parlementaires/8518/20250827_RapportCommission.pdf (accessed 2026-10-10) |
| AI Gigafactory | No bid found **[unverified]**. | https://www.eurohpc-ju.europa.eu/ai-factories_en (accessed 2026-10-10) |
| National or regional model efforts | No Luxembourgish generative model found **[unverified]**. A strategic partnership with Mistral AI (June 2025) deploys models on-site with data on Luxembourg territory: a legal chatbot on Legilux and a chatbot on the main government sites. LuxEmbedder, a Luxembourgish sentence-embedding model (COLING 2025), is academic and not generative. | https://gouvernement.lu/en/actualites/toutes_actualites/communiques/2026/03-mars/04-frieden-ai4lux.html (accessed 2026-10-10); https://arxiv.org/abs/2412.03331 (accessed 2026-10-10) |
| National AI strategy | Luxembourg's AI Strategy, published May 2025 under "Accelerating Digital Sovereignty 2030" with data and quantum strategies, with new budgetary resources for 2025 to 2030 (amounts not stated); in force; the AI4LUX campaign followed in March 2026. | https://gouvernement.lu/en/publications/rapport-etude-analyse/minist-digitalisation/2025-luxembourg-ai-strategy.html (accessed 2026-10-10); https://luxinnovation.lu/news/government-unveils-strategic-initiative-accelerating-digital-sovereignty-2030 (accessed 2026-10-10) |
| Public-sector LLM use | All civil servants to receive access to a sovereign chatbot able to handle sensitive information and build agents, hosted on-site under the Mistral partnership (March 2026); the Legilux chatbot; rollout completion **[unverified]**. | https://gouvernement.lu/en/actualites/toutes_actualites/communiques/2026/03-mars/04-frieden-ai4lux.html (accessed 2026-10-10) |
| Language resources | The Zenter fir d'Lëtzebuerger Sprooch (law of 20 July 2018), which sets spelling and grammar and runs the online dictionary; a national corpus and CLARIN membership **[unverified]**. | https://gouvernement.lu/fr/actualites/toutes_actualites.gouv2024_mcult+fr+actualites+mes-actualites+2024+fevrier+sproochegesetz-40-joer.html (accessed 2026-10-10) |
| Key institutions | LuxProvide (MeluXina, the factory); LIST; the University of Luxembourg; LNDS; Luxinnovation; LuxConnect; the ZLS. | https://cordis.europa.eu/project/id/101234366 (accessed 2026-10-10) |
| Power and grid | More than half of MeluXina-AI's five-year operating cost is electricity and cooling (committee report); grid constraints **[unverified]**. | https://wdocs-pub.chd.lu/docs/Dossiers_parlementaires/8518/20250827_RapportCommission.pdf (accessed 2026-10-10) |

#### What good enough means here
Four languages for 680,000 residents: French and German, which the neighbours' models serve; English, which
every model serves; and Luxembourgish, the national language spoken by three quarters of residents, which no
one else will ever build. Luxembourg has a EuroHPC system, a first-round factory with a large accelerator
count for its size, a strategy under a sovereignty banner, and a government-wide sovereign assistant from a
French lab hosted on its own territory. It has met B2 by procurement; B3 depends on the terms, and B1 for
Luxembourgish depends on a programme nobody has started.

#### Recommended strategy
**R4 is Luxembourg's chosen route; write the terms. R2 as the customer of France and Germany. R1 small for
Luxembourgish on MeluXina-AI: the one thing only Luxembourg will do.**

1. **Put escrow and continuity terms into the Mistral partnership (R4, B3).** On-site hosting delivers B2;
   it does not deliver possession. The contract should secure weight escrow or an open-weight fallback
   version the state holds, continuation rights and evaluation on a national set, so that a change of the
   lab's ownership or terms never strands the civil service's assistant.
2. **Build the Luxembourgish model (R1).** The ZLS corpus, the online dictionary, legislation's French with
   Luxembourgish parliamentary text, and the LuxEmbedder work are the inputs; a continued-pretraining stage of
   an open multilingual base on MeluXina-AI, held by the state, served beside the procured models. It is a
   small team's work and a national obligation nobody else carries.
3. **Take the French and German public lines as fallbacks (R2).** Lucie and the German line are Apache-2.0;
   serving copies under agreed terms give Luxembourg state-held models for two of its administrative languages
   at no training cost.
4. **Make the civil-service assistant the evaluation bench (B6)** across all four languages, published, so
   that the procured and the national models are scored alike.
5. **Serve Ireland through the antenna (R2, as host),** which attaches to Luxembourg's factory.
6. **Fund the Luxembourgish line under the sovereignty strategy (B5),** whose budget lines are not public.

#### What it does not need to do
Train a French or German model, pretrain from scratch, or bid for a Gigafactory: the factory is already large
for the state's needs and the neighbours cover two languages.

#### Main blocker, and what would change the recommendation
No Luxembourgish generative model exists or is planned on any fetched page, and the state's sovereignty rests
on a partnership whose terms are not public. The recommendation would change if the partnership publishes
escrow terms (R4 is settled), or if the strategy funds a Luxembourgish line (R1 proceeds on MeluXina-AI at
once).

#### Sources
- luxembourg.public.lu, languages, https://luxembourg.public.lu/en/society-and-culture/languages/languages-spoken-luxembourg.html, accessed 2026-10-10; European Union, Luxembourg, https://european-union.europa.eu/principles-countries-history/eu-countries/luxembourg_en, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10; first seven AI Factories, https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en, accessed 2026-10-10; MeluXina-AI contract, https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-meluxina-ai-new-ai-optimised-supercomputer-luxembourg-ai-factory-2026-07-22_en, accessed 2026-10-10; AI Factories, https://www.eurohpc-ju.europa.eu/ai-factories_en, accessed 2026-10-10.
- CORDIS, L-AIF, https://cordis.europa.eu/project/id/101234366, accessed 2026-10-10; Chambre des Députés, committee report on bill 8518, https://wdocs-pub.chd.lu/docs/Dossiers_parlementaires/8518/20250827_RapportCommission.pdf, accessed 2026-10-10.
- gouvernement.lu, AI strategy, https://gouvernement.lu/en/publications/rapport-etude-analyse/minist-digitalisation/2025-luxembourg-ai-strategy.html, accessed 2026-10-10; AI4LUX, https://gouvernement.lu/en/actualites/toutes_actualites/communiques/2026/03-mars/04-frieden-ai4lux.html, accessed 2026-10-10; Sproochegesetz, https://gouvernement.lu/fr/actualites/toutes_actualites.gouv2024_mcult+fr+actualites+mes-actualites+2024+fevrier+sproochegesetz-40-joer.html, accessed 2026-10-10.
- Luxinnovation, Accelerating Digital Sovereignty 2030, https://luxinnovation.lu/news/government-unveils-strategic-initiative-accelerating-digital-sovereignty-2030, accessed 2026-10-10.
- arXiv, LuxEmbedder, https://arxiv.org/abs/2412.03331, accessed 2026-10-10.

### Malta (MT)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Maltese is the national language; Maltese and English are the official languages (Constitution art. 5). Population 574,250 (Eurostat, 1 January 2025, provisional); speaker counts **[unverified]**. | https://legislation.mt/eli/const/eng/pdf (accessed 2026-10-10); https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?geo=FR&geo=ES&geo=PT&geo=IT&geo=MT&sex=T&age=TOTAL&time=2025&format=JSON&lang=EN (accessed 2026-10-10) |
| Language shared with | English with Ireland; the Maltese diaspora **[unverified]**. | https://legislation.mt/eli/const/eng/pdf (accessed 2026-10-10) |
| EuroHPC system on national soil | None. | https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en (accessed 2026-10-10) |
| EuroHPC AI Factory | No factory; the antenna CALYPSO, led by the MDIA and linked to Greece's Pharos factory, "both an extension of Pharos and a national innovation hub"; selection date and funding not on the page. | https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories_en (accessed 2026-10-10) |
| AI Gigafactory | No Maltese bid found **[unverified]**. | https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en (accessed 2026-10-10) |
| National or regional model efforts | No Maltese generative model found. BERTu, an encoder pretrained from scratch on Korpus Malti by the University of Malta's MLRS (2022), CC BY-NC-SA 4.0. MDIA-funded Maltese language projects are press only **[unverified]**. | https://huggingface.co/MLRS/BERTu (accessed 2026-10-10) |
| National AI strategy | "The Ultimate AI Launchpad", the strategy and vision to 2030 (2019), overseen by the MDIA, 72 actions with no mention of the Maltese language; listed by OECD.AI as active and under realignment. A realigned strategy 2025 to 2030 with 83 measures went to consultation in November 2025 per a law-firm guide **[unverified]** officially. | https://digital-skills-jobs.europa.eu/en/initiatives/national-strategies/malta-strategy-and-vision-artificial-intelligence-malta-2030 (accessed 2026-10-10); https://oecd.ai/en/dashboards/policy-initiatives/the-ultimate-ai-launchpad-a-strategy-and-vision-for-artificial-intelligence-in-malta-2030-2591 (accessed 2026-10-10); (secondary) https://www.legal500.com/guides/chapter/malta-artificial-intelligence/ (accessed 2026-10-10) |
| Public-sector LLM use | No government LLM assistant found; the public-sector pilots listed in the secondary guide are not language models **[unverified]**. | (secondary) https://www.legal500.com/guides/chapter/malta-artificial-intelligence/ (accessed 2026-10-10) |
| Language resources | Korpus Malti (MLRS, University of Malta), 5.75 GB, CC BY-NC-SA 4.0, token count not stated; Malta is not listed among CLARIN ERIC members. | https://huggingface.co/datasets/MLRS/korpus_malti (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Key institutions | MDIA (strategy, antenna); the University of Malta's Institute of Linguistics and Language Technology and MLRS; the Ministry for the Economy. | https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en (accessed 2026-10-10); https://www.um.edu.mt/linguistics/ (accessed 2026-10-10) |
| Power and grid | No official statement fetched **[unverified]**. This repository's fundamentals record an isolated grid. | https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en (accessed 2026-10-10) |

#### What good enough means here
Two languages for half a million citizens: English, which every open model already serves, and Maltese, a
Semitic language with a small corpus that no commercial supplier will prioritise and whose national status is
constitutional. The bar for Malta is an English-capable model the state controls (B2, B3, B5) and a Maltese
capability built deliberately on top of it (B1), which no fetched page shows anyone building.

#### Recommended strategy
**R1 for Maltese, small, at the University of Malta on antenna compute; R2 through Greece's factory for the
compute and through ALT-EDIC for the small-language programme; R4 with terms for everything in English.**

1. **Fund a Maltese continued-pretraining stage (R1).** Korpus Malti and BERTu show the corpus and the team
   exist at MLRS; what is missing is a generative model. A small programme, a handful of people, continued
   pretraining of an open multilingual base on the rights-cleared Maltese corpus, instruction-tuned on
   public-service text, with the weights held by the MDIA (B3). The licence on the corpus itself is
   non-commercial today and must be settled for public-sector use (B4).
2. **Use CALYPSO and Pharos for the compute (R2).** The antenna gives access to DAEDALUS through Greece's
   factory; the run is weeks of accelerator time. No Maltese compute is needed for the bar.
3. **Put Maltese into the EU small-language programmes (R2).** ALT-EDIC, where Malta is an observer, exists
   for languages under ten million speakers; OpenEuroLLM and the EUROPA model cover all 24 official languages.
   Malta's contribution is its corpus and an evaluation set; its return is a base that already knows Maltese.
4. **Serve English-language public services from a procured model under terms (R4), hosted in the EU under
   the state's approved environments (B2),** with the national model as the fallback the state possesses.
5. **Write the Maltese language into the realigned strategy (B5).** The 2019 strategy does not mention it; the
   2025 to 2030 realignment is where a recurring line for the Maltese model belongs.
6. **Build the evaluation set from the first public service (B6).** No assistant exists; the first one, in
   both languages, is the bench.

#### What it does not need to do
Own compute, host a factory, bid for a Gigafactory, or pretrain from scratch. It does not need to improve
English; it needs to own what it uses and to build Maltese.

#### Main blocker, and what would change the recommendation
Nobody is building a Maltese generative model, the national corpus is under a non-commercial licence, and
the strategy omits the language. The recommendation would change if the realigned strategy funds a Maltese
model line (R1 proceeds at once on antenna compute), or if OpenEuroLLM's 2026 release proves strong enough in
Maltese that the state's stage becomes tuning only.

#### Sources
- legislation.mt, Constitution of Malta, https://legislation.mt/eli/const/eng/pdf, accessed 2026-10-10; Eurostat demo_pjan, https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?geo=FR&geo=ES&geo=PT&geo=IT&geo=MT&sex=T&age=TOTAL&time=2025&format=JSON&lang=EN, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en, accessed 2026-10-10; antennas, https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en, accessed 2026-10-10; AI Factories, https://www.eurohpc-ju.europa.eu/ai-factories_en, accessed 2026-10-10; Gigafactories call, https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en, accessed 2026-10-10.
- MLRS, BERTu, https://huggingface.co/MLRS/BERTu, accessed 2026-10-10; Korpus Malti, https://huggingface.co/datasets/MLRS/korpus_malti, accessed 2026-10-10; University of Malta, Institute of Linguistics, https://www.um.edu.mt/linguistics/, accessed 2026-10-10.
- Digital Skills and Jobs Platform, Malta AI strategy, https://digital-skills-jobs.europa.eu/en/initiatives/national-strategies/malta-strategy-and-vision-artificial-intelligence-malta-2030, accessed 2026-10-10; OECD.AI, https://oecd.ai/en/dashboards/policy-initiatives/the-ultimate-ai-launchpad-a-strategy-and-vision-for-artificial-intelligence-in-malta-2030-2591, accessed 2026-10-10.
- CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10.
- (secondary) Legal 500, Malta AI guide, https://www.legal500.com/guides/chapter/malta-artificial-intelligence/, accessed 2026-10-10.

### Netherlands (NL)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Dutch; Frisian official in Fryslân; Dutch Sign Language recognised; Limburgish, Low Saxon, Yiddish, Romani and Papiamentu recognised under the European Charter; Papiamentu and English official in the Caribbean municipalities. Population 18,044,027 (Eurostat 2025 via the EU country page); speaker counts **[unverified]**. | https://www.rijksoverheid.nl/onderwerpen/erkende-talen/erkende-talen-in-nl (accessed 2026-10-10); https://european-union.europa.eu/principles-countries-history/eu-countries/netherlands_en (accessed 2026-10-10) |
| Language shared with | Belgium, where Dutch is one of three official languages (Flanders); the diaspora **[unverified]**. | https://european-union.europa.eu/principles-countries-history/eu-countries/belgium_en (accessed 2026-10-10) |
| EuroHPC system on national soil | None; SURF is in France's Alice Recoque consortium. The national system Snellius at SURF (its GPU count and performance not on the fetched page **[unverified]**); the September 2026 cabinet letter names investment in its successor. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10); https://www.surf.nl/en/services/compute/snellius-the-national-supercomputer (accessed 2026-10-10); https://www.eerstekamer.nl/behandeling/20260921/brief_van_de_staatssecretaris_van/document3/f=/vn18lk58uobh.pdf (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: NLAIF, selected 10 October 2025, led by the AI Factory foundation with SURF, TNO, Samenwerking Noord and AIC4NL, in Groningen; the cabinet decided on 27 June 2025 on EUR 70 million national, EUR 60 million regional and EUR 70 million requested from EuroHPC, EUR 200 million in all; CORDIS: EUR 14.1 million project, July 2026 to June 2029; press reports the supercomputer fully operational by early 2028. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en (accessed 2026-10-10); https://cordis.europa.eu/project/id/101314093 (accessed 2026-10-10); https://www.rijksoverheid.nl/actueel/nieuws/2025/06/27/nederland-zet-in-op-200-miljoen-euro-voor-aifabriek-in-groningen (accessed 2026-10-10); (press) https://ioplus.nl/en/posts/eurofiber-to-host-ai-facility-in-groningen (accessed 2026-10-10) |
| AI Gigafactory | Eneco and Volt state they submitted expressions of interest and asked ministers (23 February 2026) for a financial commitment or compute pre-purchase without which participation "is not possible"; the government's position and bid status **[unverified]**. | https://news.eneco.com/eneco-and-volt-political-action-needed-for-ai-gigafactory/ (accessed 2026-10-10); https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en (accessed 2026-10-10) |
| National or regional model efforts | GPT-NL (TNO, NFI and SURF; EUR 13.5 million from the economics ministry, announced November 2023): training since June 2025 on lawfully obtained data including over 20 billion tokens of news text with publishers remunerated; access limited to launching customers; code repositories open-sourced March 2026; "v.1" listed for autumn 2026; size, base and licence **[unverified]**. The ASML and Mistral partnership **[unverified]** (the release redirected). The cabinet makes EUR 120 million available for an IPCEI on AI (September 2026). | https://www.tno.nl/en/newsroom/2023/11/netherlands-starts-realisation-gpt-nl/ (accessed 2026-10-10); https://www.tno.nl/en/newsroom/2025/07/large-dataset-news-organizations-dutch/ (accessed 2026-10-10); https://gpt-nl.nl/ (accessed 2026-10-10); https://www.eerstekamer.nl/behandeling/20260921/brief_van_de_staatssecretaris_van/document3/f=/vn18lk58uobh.pdf (accessed 2026-10-10) |
| National AI strategy | The Netherlands Digitalisation Strategy, priority 3 "Artificial Intelligence", naming "open language models from the Netherlands or the EU" among its infrastructure aims; the cabinet letter of 21 September 2026 on the digital economy and sovereignty sets the current lines (the Groningen factory, the IPCEI, a shared government AI infrastructure under exploration). Formal adoption date **[unverified]**. | https://www.nldigitalgovernment.nl/dossiers/priority-3-artificial-intelligence/ (accessed 2026-10-10); https://www.eerstekamer.nl/behandeling/20260921/brief_van_de_staatssecretaris_van/document3/f=/vn18lk58uobh.pdf (accessed 2026-10-10) |
| Public-sector LLM use | ICTU, 27 municipalities and TNO trialling GPT-NL with the assistant "Gem" (February 2026); a government-wide generative-AI monitor (December 2025); an AI marketplace under the Apply AI programme. | https://www.nldigitalgovernment.nl/dossiers/priority-3-artificial-intelligence/ (accessed 2026-10-10) |
| Language resources | The Institute for the Dutch Language (INT), a certified CLARIN B-centre with large Dutch corpora, listed under the CLARIN-BE consortium; the SoNaR corpus and CLARIAH-NL **[unverified]**. | https://centres.clarin.eu/centre/22 (accessed 2026-10-10) |
| Key institutions | SURF; TNO and NFI; the AI Factory foundation with AIC4NL and Samenwerking Noord; ICTU; INT. | https://cordis.europa.eu/project/id/101314093 (accessed 2026-10-10); https://gpt-nl.nl/ (accessed 2026-10-10) |
| Power and grid | Binding: the government's grid-congestion letter records over 15,000 large-consumer applications queued at the end of 2025, and the coalition agreement gives congestion the highest priority; a central-government approach to data-centre capacity is due in autumn 2026. The companion note `countries/NL/FRONTIER-MODEL.md` treats grid capacity as the binding constraint for any training cluster. | https://www.eerstekamer.nl/nonav/behandeling/20260402/brief_regering_voortgang_aanpak/document3/f=/vmwpn4ekmqzi.pdf (accessed 2026-10-10); https://www.eerstekamer.nl/behandeling/20260921/brief_van_de_staatssecretaris_van/document3/f=/vn18lk58uobh.pdf (accessed 2026-10-10) |

#### What good enough means here
Dutch for eighteen million citizens and, with Flanders, for Belgium's majority, in the registers of
administration, courts and health, with Frisian and the Caribbean municipalities' languages where the law
provides. The Netherlands is the repository's reference case: its frontier question is answered in
`countries/NL/FRONTIER-MODEL.md`, and this entry asks only the citizen-grade one. GPT-NL is the one national
model in this note built on the premise that every token was lawfully obtained and its publishers paid,
which is B4 by construction; what it lacks is public weights, a stated licence, and a home.

#### Recommended strategy
**R1 is under way with the strongest provenance in Europe; finish it in the open and institutionalise it.
R2 with Flanders. R4 with terms. The Gigafactory is a grid question, kept separate.**

1. **Release GPT-NL's weights under a licence the state can defend, and hold them (B3).** Access is limited to
   launching customers and the licence is unstated. A model the state paid for and whose data it can defend
   should be the state's to deploy; the economics ministry should own the weights and the data register, with
   TNO, NFI and SURF as the operating consortium.
2. **Fund it as a programme, not a project (B5).** The companion note's judgement that the committed sum is
   not a serious number for the attached ambition stands; the IPCEI envelope and the factory are the vehicles,
   and a recurring line with a release cadence is the deliverable.
3. **Make Gem the deployment and evaluation vehicle (B2, B6).** Twenty-seven municipalities and ICTU are
   already piloting; the state's shared AI infrastructure under exploration is where it should be served, and
   Gem's traffic, anonymised and checked, is the national evaluation set.
4. **Train on EuroHPC access until Groningen runs, then on NLAIF.** Snellius carries the tuning; the
   Groningen system is the home from 2028 per press, on the northern grid the companion note identifies as
   the right place for any Dutch load.
5. **Pool with Flanders (R2, as supplier).** Belgium has no factory and no Dutch programme; a Flemish stage
   on GPT-NL, with Flanders' corpus and evaluation data and a serving copy for Belgian bodies under agreed
   terms, serves 25 million Dutch speakers for the cost of one programme.
6. **Procure frontier access with terms (R4),** GPT-NL as fallback. The companion note's recommendation
   stands: continuity guarantees, weight escrow and price protection buy more security per euro than a
   domestic frontier run.
7. **Decide the Gigafactory on the grid, not on the model.** Eneco and Volt ask for a pre-purchase; the
   autumn 2026 data-centre approach is where that belongs. The citizen model does not depend on it.

#### What it does not need to do
Pretrain at frontier scale or build a training cluster in the Randstad: the companion note shows why. It does
not need to wait for Groningen, or for a licence decision on someone else's model, to deploy its own.

#### Main blocker, and what would change the recommendation
The weights, size and licence of the state-funded model are unpublished, and the grid queue constrains any
national compute beyond the factory. The recommendation would change if GPT-NL v.1 ships in autumn 2026 with
open weights under a defensible licence (R1 is settled and the remaining work is Gem and terms), or if the
government pre-purchases Gigafactory compute (R3 becomes an option to cost, separately, as the companion note
asks).

#### Sources
- Rijksoverheid, recognised languages, https://www.rijksoverheid.nl/onderwerpen/erkende-talen/erkende-talen-in-nl, accessed 2026-10-10; European Union, Netherlands, https://european-union.europa.eu/principles-countries-history/eu-countries/netherlands_en, accessed 2026-10-10; Belgium, https://european-union.europa.eu/principles-countries-history/eu-countries/belgium_en, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10; six additional AI Factories, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en, accessed 2026-10-10; Gigafactories call, https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en, accessed 2026-10-10.
- SURF, Snellius, https://www.surf.nl/en/services/compute/snellius-the-national-supercomputer, accessed 2026-10-10; CORDIS, NLAIF, https://cordis.europa.eu/project/id/101314093, accessed 2026-10-10; Rijksoverheid, AI factory Groningen, https://www.rijksoverheid.nl/actueel/nieuws/2025/06/27/nederland-zet-in-op-200-miljoen-euro-voor-aifabriek-in-groningen, accessed 2026-10-10.
- TNO, GPT-NL start, https://www.tno.nl/en/newsroom/2023/11/netherlands-starts-realisation-gpt-nl/, accessed 2026-10-10; news dataset, https://www.tno.nl/en/newsroom/2025/07/large-dataset-news-organizations-dutch/, accessed 2026-10-10; GPT-NL, https://gpt-nl.nl/, accessed 2026-10-10.
- NL Digital Government, priority 3, https://www.nldigitalgovernment.nl/dossiers/priority-3-artificial-intelligence/, accessed 2026-10-10.
- Eerste Kamer, cabinet letter on the digital economy and sovereignty (21 September 2026), https://www.eerstekamer.nl/behandeling/20260921/brief_van_de_staatssecretaris_van/document3/f=/vn18lk58uobh.pdf, accessed 2026-10-10; grid-congestion letter (2 April 2026), https://www.eerstekamer.nl/nonav/behandeling/20260402/brief_regering_voortgang_aanpak/document3/f=/vmwpn4ekmqzi.pdf, accessed 2026-10-10.
- Eneco, Gigafactory, https://news.eneco.com/eneco-and-volt-political-action-needed-for-ai-gigafactory/, accessed 2026-10-10.
- CLARIN centre registry, INT, https://centres.clarin.eu/centre/22, accessed 2026-10-10.
- (press) IO+, Eurofiber, https://ioplus.nl/en/posts/eurofiber-to-host-ai-facility-in-groningen, accessed 2026-10-10.

### Poland (PL)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Polish; census 2021 (language used at home): 37,868,618 of 38,036,118; Silesian 467,145, German 216,342, Kashubian 89,198, Ukrainian 55,104. The statutory status of Polish and of Kashubian as a regional language **[unverified]** (the Sejm page returned a bot screen). | https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/6536/10/1/1/jezyk_uzywany_w_domu_-_dane_nsp_2021_dla_kraju_i_jednostek_podzialu_terytorialnego.xlsx (accessed 2026-10-10); https://stat.gov.pl/spisy-powszechne/nsp-2021/nsp-2021-wyniki-ostateczne/tablice-z-ostatecznymi-danymi-w-zakresie-przynaleznosci-narodowo-etnicznej-jezyka-uzywanego-w-domu-oraz-przynaleznosci-do-wyznania-religijnego,10,1.html (accessed 2026-10-10) |
| Language shared with | Polish mother tongue declared by 30,183 people in Czechia (2021) and 3,398 in Hungary (2022); the wider diaspora **[unverified]**. | https://scitani.gov.cz/matersky-jazyk (accessed 2026-10-10); https://nepszamlalas2022.ksh.hu/en/results/final-data/tables/nsz2022-1.1.6-eng.xlsx (accessed 2026-10-10) |
| EuroHPC system on national soil | No EuroHPC classical system; the EuroHPC quantum computer PIAST-Q at PSNC. National systems at Cyfronet: Helios (37 PFlops theoretical, 440 GH200 superchips) and Athena (384 A100). | https://www.eurohpc-ju.europa.eu/ai-factories/poland_en (accessed 2026-10-10); https://www.psnc.pl/polish-ai-and-quantum-infrastructure-in-the-spotlight-at-eurohpc-user-days-2026-in-dublin/ (accessed 2026-10-10); https://www.cyfronet.pl/en/supercomputers/our-supercomputers (accessed 2026-10-10) |
| EuroHPC AI Factory | Two: PIAST (PSNC Poznań, selected 12 March 2025, "services available from 2026", planned capacity over 1,500 GPUs) and Gaia (Cyfronet AGH within PLGrid, selected 10 October 2025, with LLMs among its target sectors). Funding amounts **[unverified]** on official pages. | https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories/poland_en (accessed 2026-10-10) |
| AI Gigafactory | The "Baltic AI GigaFactory" expression of interest, submitted 20 June 2025 by Poland as leader with Estonia, Lithuania and Latvia: EUR 3 billion, 65% private, up to two Polish sites on 100% green energy, with developing PLLuM and Bielik among its goals. Press reports Estonia and Latvia withdrew and that Poland entered lot 1 of the EuroHPC call **[unverified]**; no selection yet. | https://www.gov.pl/web/cyfryzacja/wniosek-dotyczacy-baltic-ai-gigafactory-zlozony (accessed 2026-10-10); (press) https://itwiz.pl/komisja-europejska-wywraca-do-gory-nogami-projekt-gigafabryk-ai/ (accessed 2026-10-10); (press) https://spidersweb.pl/2026/07/gigafabryka-ai-polska-1-mld-euro.html (accessed 2026-10-10) |
| National or regional model efforts | PLLuM, "the first government LLM": 18 versions from 8B to 70B, a 100-billion-word corpus with no synthetic data, released 24 February 2025 by the NASK-led consortium (now HIVE: NASK, Wrocław University of Science and Technology, IPI PAN, OPI-PIB, University of Łódź, COI, Cyfronet); funded by the Minister of Digital Affairs under subsidy 1/WII/DBI/2025, about PLN 18.5 million; the December 2025 generation is Apache-2.0 on Mistral-Nemo (12B) and under the Llama 3.1 licence on the Llama variants. Bielik (SpeakLeash foundation with Cyfronet): Bielik-11B-v3.0, Apache-2.0, trained on Athena and Helios under a PLGrid grant; funder **[unverified]**. | https://www.gov.pl/web/cyfryzacja/czesc-jestem-pllum-jak-powstaje-polski-ekosystem-modeli-jezykowych (accessed 2026-10-10); https://science.nask.pl/en/news/12757 (accessed 2026-10-10); https://huggingface.co/CYFRAGOVPL/PLLuM-12B-chat-2512 (accessed 2026-10-10); https://huggingface.co/CYFRAGOVPL/Llama-PLLuM-8B-chat-2512 (accessed 2026-10-10); https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct (accessed 2026-10-10) |
| National AI strategy | The 2020 policy, adopted by Council of Ministers resolution 196 of 28 December 2020, in force. A 2030 policy is a draft dated 15 April 2026 that names PLLuM and Bielik as the basis of an open-source strategy, a pilot of PLLuM in at least 1,000 public entities, and a PLGrid compute target; adoption **[unverified]**. | https://www.gov.pl/web/ai/polityka-dla-rozwoju-sztucznej-inteligencji-w-polsce-od-roku-2020 (accessed 2026-10-10); https://www.gov.pl/attachment/2af79671-76df-435e-b75d-769f8886cc7c (accessed 2026-10-10) |
| Public-sector LLM use | The Ministry stated in February 2025 that PLLuM's first deployment would be the mObywatel app; NASK describes a citizen assistant and a civil-servant assistant; press reports the PLLuM-based assistant reached all users around 31 December 2025 **[unverified]** as to date. | https://www.gov.pl/web/cyfryzacja/czesc-jestem-pllum-jak-powstaje-polski-ekosystem-modeli-jezykowych (accessed 2026-10-10); https://science.nask.pl/en/news/12757 (accessed 2026-10-10); (press) https://imagazine.pl/2026/01/02/mobywatel-wchodzi-w-2026-rok-z-polskim-ai/ (accessed 2026-10-10) |
| Language resources | NKJP, the National Corpus of Polish, over 1.5 billion words (IPI PAN with partners); CLARIN-PL at Wrocław University of Science and Technology, funded through 2027, hosting the PLLuM demo. | https://nkjp.pl/ (accessed 2026-10-10); https://clarin-pl.eu/ (accessed 2026-10-10) |
| Key institutions | NASK (PLLuM, HIVE); PSNC (PIAST); Cyfronet AGH (Gaia, PLGrid, Helios); OPI PIB; IPI PAN; Wrocław University of Science and Technology (CLARIN-PL); the SpeakLeash foundation (Bielik). | https://www.cyfronet.pl/en/supercomputers/our-supercomputers (accessed 2026-10-10); https://science.nask.pl/en/news/12757 (accessed 2026-10-10) |
| Power and grid | The Ministry's Gigafactory site requirement is 100% green energy with adequate power and cooling; grid figures **[unverified]**. | https://www.gov.pl/web/cyfryzacja/wniosek-dotyczacy-baltic-ai-gigafactory-zlozony (accessed 2026-10-10) |

#### What good enough means here
Polish for thirty-eight million citizens in the registers of administration, courts, revenue and health, with
Silesian, Kashubian and the minority languages where the law provides. Poland is the state in this note where
the government itself has already shipped a national model to citizens: PLLuM, funded by the digital ministry,
trained on a curated corpus, deployed in the national app. The question is no longer whether but how to keep it.

#### Recommended strategy
**R1 is delivered; institutionalise and keep it open. R2 as a supplier and through the two factories. R3 is a
live option tied to the Gigafactory, kept separate. R4 with terms.**

1. **Give PLLuM a permanent home and a recurring line (B5).** A subsidy under a single decision number funded
   the model that now serves every mObywatel user. Write the HIVE consortium's programme into the 2030 policy
   as a standing commitment, with a release cadence, so the model in citizens' hands is never one budget year
   from abandonment.
2. **Settle the licence split (B3).** The December 2025 generation is Apache-2.0 on the Mistral-Nemo base and
   under the Llama 3.1 licence on the Llama variants. The deployed public-service model should be the one whose
   licence the state can defend indefinitely; keep the Llama line as a research variant and say so in the
   register. Bielik's Apache-2.0 release is the community counterpart and belongs in the same register.
3. **Move training onto the two factories as they come online (B2).** Helios and Athena already carry the
   runs; PIAST from 2026 and Gaia with its LLM focus give the programme national, EU co-funded training homes.
   No further compute is needed for the bar.
4. **Make mObywatel's traffic the national evaluation set (B6).** The assistant's anonymous questions, with
   answers checked by the competent ministries, versioned and published, become the yardstick for PLLuM
   generations and for every procured model.
5. **Supply the neighbourhood (R2).** Polish is not shared with another member state, so pooling is as a
   supplier: Moldova's antenna is attached to PIAST, and the Baltic partners of the Gigafactory bid are
   small-language states that would take a multilingual continued-pretraining run on PLLuM's recipe.
6. **Keep the Gigafactory separate from the citizen model.** The Baltic bid, now in the EuroHPC call, is an R3
   instrument and an industrial-policy project; if selected it gives Poland a frontier-class training home. The
   citizen model does not wait for it, and bundling the two risks the smaller, delivered thing for the larger,
   uncertain one.
7. **Procure frontier access with terms (R4)** for what a 70B model cannot do, PLLuM as the fallback the state
   already possesses.

#### What it does not need to do
Train a new national model from scratch, buy a national training cluster outside the factories, or wait for
the Gigafactory selection before the next PLLuM generation. It does not need to choose between PLLuM and
Bielik; it needs both in one register with their licences.

#### Main blocker, and what would change the recommendation
The 2030 policy is still a draft, and the programme behind the deployed model rests on a one-off subsidy. The
recommendation would change if the 2030 policy is adopted with the 1,000-entity pilot and a budget line (R1 is
settled and the remaining work is evaluation and terms), or if the Gigafactory is selected with Poland as lead
(R3 becomes a choice to cost on its own).

#### Sources
- GUS, Census 2021 language tables (xlsx), https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/6536/10/1/1/jezyk_uzywany_w_domu_-_dane_nsp_2021_dla_kraju_i_jednostek_podzialu_terytorialnego.xlsx, index https://stat.gov.pl/spisy-powszechne/nsp-2021/nsp-2021-wyniki-ostateczne/tablice-z-ostatecznymi-danymi-w-zakresie-przynaleznosci-narodowo-etnicznej-jezyka-uzywanego-w-domu-oraz-przynaleznosci-do-wyznania-religijnego,10,1.html, accessed 2026-10-10.
- ČSÚ, mother tongue, https://scitani.gov.cz/matersky-jazyk, accessed 2026-10-10; KSH, table 1.1.6, https://nepszamlalas2022.ksh.hu/en/results/final-data/tables/nsz2022-1.1.6-eng.xlsx, accessed 2026-10-10.
- EuroHPC JU, Poland AI Factories, https://www.eurohpc-ju.europa.eu/ai-factories/poland_en, accessed 2026-10-10; additional AI Factories, https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en, accessed 2026-10-10; six additional AI Factories, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en, accessed 2026-10-10.
- PSNC, EuroHPC User Days 2026, https://www.psnc.pl/polish-ai-and-quantum-infrastructure-in-the-spotlight-at-eurohpc-user-days-2026-in-dublin/, accessed 2026-10-10.
- Cyfronet AGH, our supercomputers, https://www.cyfronet.pl/en/supercomputers/our-supercomputers, accessed 2026-10-10.
- Ministry of Digital Affairs, Baltic AI GigaFactory, https://www.gov.pl/web/cyfryzacja/wniosek-dotyczacy-baltic-ai-gigafactory-zlozony, accessed 2026-10-10; PLLuM, https://www.gov.pl/web/cyfryzacja/czesc-jestem-pllum-jak-powstaje-polski-ekosystem-modeli-jezykowych, accessed 2026-10-10; 2020 policy, https://www.gov.pl/web/ai/polityka-dla-rozwoju-sztucznej-inteligencji-w-polsce-od-roku-2020, accessed 2026-10-10; 2030 draft, https://www.gov.pl/attachment/2af79671-76df-435e-b75d-769f8886cc7c, accessed 2026-10-10.
- NASK, PLLuM available, https://science.nask.pl/en/news/12757, accessed 2026-10-10.
- CYFRAGOVPL model cards, https://huggingface.co/CYFRAGOVPL/PLLuM-12B-chat-2512 and https://huggingface.co/CYFRAGOVPL/Llama-PLLuM-8B-chat-2512, accessed 2026-10-10; SpeakLeash, https://huggingface.co/speakleash/Bielik-11B-v3.0-Instruct, accessed 2026-10-10.
- NKJP, https://nkjp.pl/, accessed 2026-10-10; CLARIN-PL, https://clarin-pl.eu/, accessed 2026-10-10.
- (press) iMagazine, https://imagazine.pl/2026/01/02/mobywatel-wchodzi-w-2026-rok-z-polskim-ai/; ITwiz, https://itwiz.pl/komisja-europejska-wywraca-do-gory-nogami-projekt-gigafabryk-ai/; Spider's Web, https://spidersweb.pl/2026/07/gigafabryka-ai-polska-1-mld-euro.html; all accessed 2026-10-10.

### Portugal (PT)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Portuguese (Constitution art. 11(3)); Mirandese's recognition **[unverified]**. Population 10,749,635 (Eurostat, 1 January 2025, provisional); speaker counts **[unverified]**. | https://www.parlamento.pt/Legislacao/Paginas/ConstituicaoRepublicaPortuguesa.aspx (accessed 2026-10-10); https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?geo=FR&geo=ES&geo=PT&geo=IT&geo=MT&sex=T&age=TOTAL&time=2025&format=JSON&lang=EN (accessed 2026-10-10) |
| Language shared with | Brazil and the Portuguese-speaking African states **[unverified]** from an official page; EuroLLM-9B (IST and Unbabel) covers Portuguese among 35 languages. | https://huggingface.co/utter-project/EuroLLM-9B (accessed 2026-10-10) |
| EuroHPC system on national soil | Deucalion, hosted by FCT at Guimarães, inaugurated 6 September 2023, 7.48 PFlops sustained, 33 A100 nodes; operational. | https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en (accessed 2026-10-10); https://deucalion.acnca.pt/ (accessed 2026-10-10) |
| EuroHPC AI Factory | None on Portuguese soil; FCT is a partner of the BSC AI Factory and co-funds the MareNostrum 5 AI upgrade. The overview lists Portugal under Spain's factory; the antennas page lists no Portuguese antenna **[unverified]**. | https://www.eurohpc-ju.europa.eu/ai-factories/spain_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/contract-signed-boost-marenostrum-5s-ai-capabilities-2026-01-26_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en (accessed 2026-10-10) |
| AI Gigafactory | Press reports a Council of Ministers resolution authorising up to EUR 200 million over seven years for compute time on Portuguese territory, Sines as the site and a joint Iberian bid with Spain **[unverified]** against an official page; no selection yet. | (press) https://eco.sapo.pt/2026/07/07/governo-condiciona-200-milhoes-para-gigafabrica-ao-acesso-a-tempo-de-computacao/ (accessed 2026-10-10); https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en (accessed 2026-10-10) |
| National or regional model efforts | AMALIA, "the first open language model developed in European Portuguese", presented 1 July 2026 by the Prime Minister: a consortium of public universities and research centres, financed by the recovery plan with EUR 5.5 million plus EUR 1.5 million to 2027, Apache-2.0, 9B text and 10B vision-language checkpoints published; the compute used **[unverified]**. EuroLLM-9B (IST, Unbabel and partners, EU-funded): 4 trillion tokens on 400 H100s of MareNostrum 5, Apache-2.0. | https://portugal.gov.pt/pt/gc25/comunicacao/noticias/llm-amalia-demonstra-o-potencial-de-portugal (accessed 2026-10-10); https://amaliallm.pt/ (accessed 2026-10-10); https://huggingface.co/amalia-llm (accessed 2026-10-10); https://www.engium.uminho.pt/en/launch-of-amalia-the-first-large-scale-llm-in-european-portuguese/ (accessed 2026-10-10); https://huggingface.co/utter-project/EuroLLM-9B (accessed 2026-10-10) |
| National AI strategy | A National AI Agenda with an action plan to 2030, over EUR 400 million to 2030 and EUR 25 million for public-administration AI, in force from January 2026 per press; the resolution and its text **[unverified]**. | (press) https://dplnews.com/?p=301517 (accessed 2026-10-10) |
| Public-sector LLM use | The government says AMALIA will serve citizen contact, administrative automation and decision support in public bodies; ARTE lists an "IA.gov" line for responsible AI in public administration. | https://portugal.gov.pt/pt/gc25/comunicacao/noticias/llm-amalia-demonstra-o-potencial-de-portugal (accessed 2026-10-10); https://www.arte.gov.pt/ (accessed 2026-10-10) |
| Language resources | PORTULAN CLARIN (University of Lisbon); AMALIA's data partners include Arquivo.pt, the National Library, Torre do Tombo and RCAAP, with 86 datasets published. | https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10); https://amaliallm.pt/parceiros/ (accessed 2026-10-10); https://huggingface.co/amalia-llm (accessed 2026-10-10) |
| Key institutions | FCT (Deucalion host, factory partner, funding channel); CNCA, INESC TEC and the University of Minho (Deucalion and MACC); NOVA, IST, Coimbra, Porto and Minho (AMALIA); ARTE; Unbabel and IST (EuroLLM). | https://deucalion.acnca.pt/ (accessed 2026-10-10); https://macc.fccn.pt/ (accessed 2026-10-10); https://www.arte.gov.pt/ (accessed 2026-10-10) |
| Power and grid | No official statement fetched **[unverified]**. This repository's fundamentals record an isolated grid and a high seismic classification. | https://deucalion.acnca.pt/ (accessed 2026-10-10) |

#### What good enough means here
European Portuguese for eleven million citizens, distinct from the Brazilian variety that dominates web
text, in the registers of administration, courts and health, with Mirandese where recognised. Portugal has
just done the hard part: a publicly funded, open-licensed national model built from the national archive,
library and research repositories, and a plan to put it on the government portal. The task is to keep it.

#### Recommended strategy
**R1 is delivered; institutionalise it. R2 with Spain through the factory and with EuroLLM. R4 with terms.
The Gigafactory purchase is separate.**

1. **Fund AMALIA past 2027 as a standing programme (B5).** The recovery-plan money runs to 2027. The
   National AI Agenda's public-administration line is the natural home; a recurring budget with a release
   cadence, the weights and recipe held by the state (B3), and the data register already built with the
   archive and library partners (B4).
2. **Train the next generation on the upgraded MareNostrum 5 as a factory partner (R2 compute).** Portugal
   co-funds the AI upgrade; Deucalion carries tuning and serving. AMALIA's compute could not be confirmed;
   the next run should be on infrastructure Portugal has rights to, and say so.
3. **Pool with Spain's ALIA and with EuroLLM (R2).** ALIA covers Portuguese among 35 languages and EuroLLM
   was built at IST on MareNostrum 5; a European-Portuguese stage on either recipe, with AMALIA's corpus, is
   cheaper than a from-scratch generation and keeps the national model abreast of larger bases. Rights to the
   weights in the agreement first.
4. **Deploy on gov.pt under the state's rules (B2) and build the evaluation set from it (B6).** The planned
   portal deployment is the evaluation bench; publish the set so procured models are scored on it.
5. **Procure frontier access with terms (R4)**, AMALIA as the fallback.
6. **Keep the Gigafactory purchase as compute procurement.** The reported budget is for compute
   time on Portuguese soil; it is R3 infrastructure with a public offtake, and the citizen model does not
   depend on it.

#### What it does not need to do
Host a factory, pretrain from scratch at larger scale, or wait for the Gigafactory: the model exists, the
corpus is national, and the factory partnership covers training.

#### Main blocker, and what would change the recommendation
Funding stops in 2027 on the fetched pages, the strategy's text could not be confirmed, and the model's
training compute is unstated. The recommendation would change if the agenda's budget names AMALIA beyond
2027 (R1 is settled), or if the Iberian Gigafactory is selected with Portuguese training rights (R3 becomes a
choice to cost separately).

#### Sources
- Assembleia da República, Constitution, https://www.parlamento.pt/Legislacao/Paginas/ConstituicaoRepublicaPortuguesa.aspx, accessed 2026-10-10; Eurostat demo_pjan, https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjan?geo=FR&geo=ES&geo=PT&geo=IT&geo=MT&sex=T&age=TOTAL&time=2025&format=JSON&lang=EN, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en, accessed 2026-10-10; Spain AI Factory, https://www.eurohpc-ju.europa.eu/ai-factories/spain_en, accessed 2026-10-10; MareNostrum 5 AI contract, https://www.eurohpc-ju.europa.eu/contract-signed-boost-marenostrum-5s-ai-capabilities-2026-01-26_en, accessed 2026-10-10; antennas, https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en, accessed 2026-10-10; Gigafactories call, https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en, accessed 2026-10-10.
- Deucalion, https://deucalion.acnca.pt/, accessed 2026-10-10; MACC, https://macc.fccn.pt/, accessed 2026-10-10.
- Portal do Governo, AMALIA, https://portugal.gov.pt/pt/gc25/comunicacao/noticias/llm-amalia-demonstra-o-potencial-de-portugal, accessed 2026-10-10; AMALIA, https://amaliallm.pt/, accessed 2026-10-10; partners, https://amaliallm.pt/parceiros/, accessed 2026-10-10; amalia-llm, https://huggingface.co/amalia-llm, accessed 2026-10-10; University of Minho, https://www.engium.uminho.pt/en/launch-of-amalia-the-first-large-scale-llm-in-european-portuguese/, accessed 2026-10-10.
- utter-project, EuroLLM-9B, https://huggingface.co/utter-project/EuroLLM-9B, accessed 2026-10-10.
- ARTE, https://www.arte.gov.pt/, accessed 2026-10-10; CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10.
- (press) ECO, Gigafactory, https://eco.sapo.pt/2026/07/07/governo-condiciona-200-milhoes-para-gigafabrica-ao-acesso-a-tempo-de-computacao/; DPL News, AI Agenda, https://dplnews.com/?p=301517; both accessed 2026-10-10.

### Romania (RO)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Romanian is the official language (Constitution Art. 13). Census mother-tongue figures **[unverified]**: the Presidency, legislation portal and census hosts refused every connection on the access date. This repository's fundamentals give a population of about 19 million. | https://www.eurohpc-ju.europa.eu/romania_en (accessed 2026-10-10) **[unverified]** |
| Language shared with | The Republic of Moldova **[unverified]** from an official page; Moldova's AI Factory antenna FAIMA is attached to Poland's PIAST factory, not to Romania. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en (accessed 2026-10-10) |
| EuroHPC system on national soil | None on the official list. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: RO AI Factory, selected 10 October 2025, hosted by ICI Bucharest with Politehnica Bucharest and partners including the Romanian Academy's AI institute; an AI-optimised supercomputer to be acquired; implementation from 1 September 2026 under grant 101314645, operational by end-2027 (press); ICI still refers users to the Spanish factory meanwhile. Romania also appears as a partner of the BSC factory. Budget **[unverified]**. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/romania_en (accessed 2026-10-10); https://ici.ro/?s=AI+Factory (accessed 2026-10-10); (press) https://agerpres.ro/english/2026/09/01/implementation-of-ro-ai-factory-project-hosted-by-ici-bucharest-starts--1589833 (accessed 2026-10-10) |
| AI Gigafactory | A bid in preparation: the "Black Sea AI Gigafactory" expression of interest of 15 April 2026 by the Ministries of Energy and Finance with ADR, to pre-select a consortium leader, about 20,000 GPUs in a first phase, deadline 14 June 2026. Sites, power and investment figures are press only **[unverified]**; no EuroHPC selection yet. | https://adr.gov.ro/articole/lansarea-expresiei-de-interes-pentru-selectia-unui-lider-de-consortiu-pentru-black-sea-ai-gigafactory (accessed 2026-10-10); (press) https://www.businessforum.ro/industry/20250624/romania-submits-bid-for-black-sea-ai-gigafactory-1942 (accessed 2026-10-10); (press) https://cursdeguvernare.ro/black-sea-ai-gigafactory-investitorii-au-cerut-clarificari-privind-ajutoarele-de-stat-racordarea-la-retea-si-garantiile-de-comercializare-raspunsurile-ministerului-energiei.html (accessed 2026-10-10) |
| National or regional model efforts | OpenLLM-Ro (ILDS Bucharest, Politehnica, University of Bucharest), privately funded by BRD Groupe Société Générale with university compute: RoLlama2 and RoMistral (continued pretraining on about 40 billion Romanian tokens), then RoLlama3.1-8B-Instruct under a CC-BY-NC-4.0 licence (2025). No public funding stated. | https://arxiv.org/html/2405.07703v4 (accessed 2026-10-10); https://huggingface.co/OpenLLM-Ro/RoLlama3.1-8b-Instruct (accessed 2026-10-10) |
| National AI strategy | The National AI Strategy 2024 to 2027, approved by the Government in July 2024 (engineering-association press); the decision number and gazette reference **[unverified]**. | (press) https://www.agir.ro/univers-ingineresc/numar-14-2024/a-fost-aprobata-strategia-nationala-in-domeniul-inteligentei-artificiale-2024---2027_8443.html (accessed 2026-10-10) |
| Public-sector LLM use | None found **[unverified]**. The recovery plan funds a secure government cloud and e-identity, not HPC or AI compute. | https://reforms-investments.ec.europa.eu/romanias-recovery-and-resilience-plan (accessed 2026-10-10) |
| Language resources | CoRoLa, the Romanian Academy's reference corpus, over one billion words, built by its AI institute (RACAI) and the Iași institute, open for public use; RACAI hosts a CLARIN knowledge centre, but Romania is absent from the CLARIN ERIC member list. | https://corola.racai.ro/ (accessed 2026-10-10); https://www.racai.ro/en/ (accessed 2026-10-10); https://www.clarin.eu/node/3754 (accessed 2026-10-10) |
| Key institutions | ICI Bucharest (factory host); Politehnica Bucharest (co-coordinator, OpenLLM-Ro compute); RACAI, the Romanian Academy's AI institute (CoRoLa); ILDS (OpenLLM-Ro); ADR (Gigafactory technical support). | https://www.eurohpc-ju.europa.eu/romania_en (accessed 2026-10-10); https://www.racai.ro/en/ (accessed 2026-10-10) |
| Power and grid | The ADR notice states no site or power figure; the nuclear-adjacent site and megawatt figures are press only **[unverified]**. | https://adr.gov.ro/articole/lansarea-expresiei-de-interes-pentru-selectia-unui-lider-de-consortiu-pentru-black-sea-ai-gigafactory (accessed 2026-10-10) |

#### What good enough means here
Romanian for nineteen million citizens, and for Moldova's if the two states choose to pool, in the registers of
administration, courts and health, plus the Hungarian minority's language where the law provides. Romania has
a large corpus, a model line that works, a factory on the way and a Gigafactory bid, and not one of them is
publicly funded as a national model programme.

#### Recommended strategy
**R1 now, publicly funded; R2 with Moldova and through the factory; R3 only if the Gigafactory is selected,
and then as a capability choice; R4 with terms.**

1. **Fund the Romanian model line as a public programme (R1, B5).** OpenLLM-Ro has shown continued
   pretraining on 40 billion Romanian tokens with bank money and university compute. The state should take it
   over as a standing programme at ICI and Politehnica, with RACAI's corpus as the national data register
   (B4), and release under a licence that permits public-sector use; the current non-commercial licence on the
   latest release does not.
2. **Use the factory as the training home from 2027 and EuroHPC access until then.** RO AI Factory's own
   system is not yet procured; the Spanish factory, to which ICI refers users, and the AI access calls carry
   the next run.
3. **Pool with Moldova (R2) and offer it the model.** The language is shared; Moldova's antenna is attached
   to Poland's factory, so Romania is the natural supplier of the Romanian model rather than a co-trainer. A
   bilateral agreement that gives Moldova a serving copy and Romania the evaluation data from a second
   administration serves both.
4. **Separate the Gigafactory from the model question.** The Black Sea bid is an energy and industrial-policy
   project run by the energy and finance ministries; if selected, it gives Romania an R3 option and a share of
   access, but the citizen-grade model does not wait for it and should not be bundled with it, for the reason
   `FRONTIER-MODEL.md` gives: the two compete for the same political capital and the larger ask sinks the smaller.
5. **Deploy one service under the state's rules (B2) and build the evaluation set from it (B6).** The
   recovery-plan government cloud is the environment; no public-sector pilot was found, so the first one is
   the evaluation bench.
6. **Procure frontier access with terms (R4)**, the national model as fallback.

#### What it does not need to do
Wait for the Gigafactory, pretrain from scratch before the factory exists, or join CLARIN before training: the
corpus and the technique are in hand.

#### Main blocker, and what would change the recommendation
No public funding for the model line, and a licence on the current release that a public body cannot use. The
census and legal pages could not be fetched, so the language figures are the least certain in this entry. The
recommendation would change if the Black Sea Gigafactory is selected in early 2027 (R3 becomes a real option
to cost, separately), or if the factory's system is procured early (training moves home sooner).

#### Sources
- EuroHPC JU, six additional AI Factories, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en, accessed 2026-10-10; Romania page, https://www.eurohpc-ju.europa.eu/romania_en, accessed 2026-10-10; antennas, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en, accessed 2026-10-10; our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10.
- ICI Bucharest, site search, https://ici.ro/?s=AI+Factory, accessed 2026-10-10.
- ADR, Black Sea AI Gigafactory expression of interest, https://adr.gov.ro/articole/lansarea-expresiei-de-interes-pentru-selectia-unui-lider-de-consortiu-pentru-black-sea-ai-gigafactory, accessed 2026-10-10.
- European Commission, Romania's recovery and resilience plan, https://reforms-investments.ec.europa.eu/romanias-recovery-and-resilience-plan, accessed 2026-10-10.
- arXiv, OpenLLM-Ro technical report, https://arxiv.org/html/2405.07703v4, accessed 2026-10-10; OpenLLM-Ro, RoLlama3.1-8b-Instruct, https://huggingface.co/OpenLLM-Ro/RoLlama3.1-8b-Instruct, accessed 2026-10-10.
- Romanian Academy, CoRoLa, https://corola.racai.ro/, accessed 2026-10-10; RACAI, https://www.racai.ro/en/, accessed 2026-10-10; CLARIN ERIC members, https://www.clarin.eu/node/3754, accessed 2026-10-10.
- (press) Agerpres, https://agerpres.ro/english/2026/09/01/implementation-of-ro-ai-factory-project-hosted-by-ici-bucharest-starts--1589833; Business Forum, https://www.businessforum.ro/industry/20250624/romania-submits-bid-for-black-sea-ai-gigafactory-1942; CursDeGuvernare, https://cursdeguvernare.ro/black-sea-ai-gigafactory-investitorii-au-cerut-clarificari-privind-ajutoarele-de-stat-racordarea-la-retea-si-garantiile-de-comercializare-raspunsurile-ministerului-energiei.html; AGIR, https://www.agir.ro/univers-ingineresc/numar-14-2024/a-fost-aprobata-strategia-nationala-in-domeniul-inteligentei-artificiale-2024---2027_8443.html; all accessed 2026-10-10.

### Slovakia (SK)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Slovak, the state language under Act 270/1995; census 2021: 5,449,270 residents, 12% with a mother tongue other than Slovak; the breakdown by Hungarian, Romani and Rusyn **[unverified]**. | https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/1995/270/ (accessed 2026-10-10); https://www.scitanie.sk/ (accessed 2026-10-10) |
| Language shared with | Czech is mutually intelligible; Slovak is the mother tongue of 150,738 people in Czechia (2021) and 10,123 in Hungary (2022). | https://scitani.gov.cz/matersky-jazyk (accessed 2026-10-10); https://nepszamlalas2022.ksh.hu/en/results/final-data/tables/nsz2022-1.1.6-eng.xlsx (accessed 2026-10-10) |
| EuroHPC system on national soil | None. National systems: Devana at the Slovak Academy of Sciences (32 A100 GPUs, about 800 TFlops, 130 kW) and Perun, funded by the recovery plan (project 17I03-04-P02-00001), reported in full operation on 31 March 2026 at over 24 PFlops across two systems (state press agency). | https://vs.sav.sk/en/services/supercomputer-devana/ (accessed 2026-10-10); https://hpc.sav.sk/en/hpc-at-sas/our-projects/ (accessed 2026-10-10); (press) https://www.tasr.sk/tasr-clanok/TASR:2026033100000448 (accessed 2026-10-10) |
| EuroHPC AI Factory | No factory; the antenna SKAIAT, selected 13 October 2025 and linked to Austria's AI:AT; host institution **[unverified]**. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en (accessed 2026-10-10); https://digital-strategy.ec.europa.eu/en/policies/ai-factories (accessed 2026-10-10) |
| AI Gigafactory | No Slovak bid found **[unverified]**. | https://digital-strategy.ec.europa.eu/en/policies/ai-factories (accessed 2026-10-10) |
| National or regional model efforts | Academic, Apache-2.0: mistral-sk-7b (Mistral-7B fine-tuned on the Araneum Slovacum web corpus; TU Košice, SAS institutes; Leonardo compute) and Qwen3-14B-sk (same institutions; Leonardo and Perun). The Slovak NLP community coordinated by KInIT records a September 2025 memorandum on Slovak language models. No government-funded national model found; funders **[unverified]**. | https://huggingface.co/slovak-nlp/mistral-sk-7b (accessed 2026-10-10); https://huggingface.co/slovak-nlp/Qwen3-14B-sk (accessed 2026-10-10); https://journals.savba.sk/index.php/jc/article/view/4266 (accessed 2026-10-10); https://kinit.sk/?p=42195 (accessed 2026-10-10) |
| National AI strategy | The adopted document is the Digital Transformation Strategy 2030 with action plans to 2026. A ministry presentation of 27 February 2026 sets out a six-pillar AI vision, including infrastructure and AI Factories, and a national AI strategy to be submitted to government by the end of the second quarter of 2026; adoption **[unverified]**. | https://mirri.gov.sk/sekcie/informatizacia/umela-inteligencia/ (accessed 2026-10-10); https://mirri.gov.sk/sekcie/informatizacia/dokumenty/vladny-cloud/eska-cloud-workshop-2026/attachment/12_neprezentovane_strategicky-pristup-k-ai-v-podmienkach-slovenskej-republiky-ivan-liska/ (accessed 2026-10-10) |
| Public-sector LLM use | Planned in the same presentation: twelve AI assistants for the most common life situations, co-pilots for officials, a central AI-system register, a central MLOps platform, proof of concept by the end of 2026. Nothing deployed was found **[unverified]**. | https://mirri.gov.sk/sekcie/informatizacia/dokumenty/vladny-cloud/eska-cloud-workshop-2026/attachment/12_neprezentovane_strategicky-pristup-k-ai-v-podmienkach-slovenskej-republiky-ivan-liska/ (accessed 2026-10-10) |
| Language resources | The Slovak National Corpus at the Ľ. Štúr Institute of Linguistics, texts from 1955 (size not stated); CLARIN-SK founded February 2026. | https://korpus.juls.savba.sk/ (accessed 2026-10-10); https://kinit.sk/?p=42195 (accessed 2026-10-10) |
| Key institutions | The Computing Centre of the Slovak Academy of Sciences and the National Supercomputing Centre (Devana, Perun); the EuroCC competence centre with TU Košice; KInIT (the Slovak NLP community); the Ľ. Štúr Institute; the digital ministry MIRRI. | https://nscc.sk/ (accessed 2026-10-10); https://eurocc-slovakia.sk/ (accessed 2026-10-10); https://kinit.sk/about/ (accessed 2026-10-10) |
| Power and grid | No official constraint found **[unverified]**; Devana draws 130 kW. This repository's fundamentals record one of the higher electricity prices in the 27. | https://vs.sav.sk/en/services/supercomputer-devana/ (accessed 2026-10-10) |

#### What good enough means here
Slovak for five million citizens, with Hungarian for the largest minority and Romani and Rusyn where the law
provides, in the registers of administration, courts and health. Slovakia has a new recovery-plan
supercomputer, academic Slovak models under open licences, a corpus institute, an antenna to Austria, and a
ministry plan for twelve citizen assistants; it does not yet have an adopted AI strategy or a state model
programme.

#### Recommended strategy
**R2 with Czechia as the primary route; R1 on Perun for the Slovak register; the twelve assistants as the
deployment and evaluation vehicle; R4 with terms.**

1. **Pool with Czechia (R2).** The languages are mutually intelligible, Czechia has Karolina, a factory on the
   way and the OpenEuroLLM coordination, and a joint run on a Czech and Slovak corpus costs Slovakia a share
   it can afford. Negotiate possession of the weights and a continuation right (B3) before contributing the
   corpus; use the antenna to Austria as the second compute door.
2. **Adapt for the Slovak register on Perun (R1).** The academic groups have shown the technique twice on
   open bases under Apache-2.0; Perun's 24 PFlops are enough for the Slovak-register stage. Turn the
   September 2025 memorandum into a funded programme at the Academy and TU Košice with KInIT, owning the
   corpus register (B4) and the evaluation set (B6).
3. **Make the twelve assistants run on the national model, hosted under the state's rules (B2).** The
   ministry's plan is the deployment vehicle; the proof of concept due by the end of 2026 should be built on
   the Slovak model, not on a procured one alone, and its traffic becomes the national evaluation set.
4. **Adopt the strategy with the model programme in it (B5).** The presentation's "infrastructure and AI
   Factories" pillar is the place; without the adopted document there is no recurring line.
5. **Procure frontier access with terms (R4)** for what the pooled model cannot do, with the Slovak
   adaptation as fallback.

#### What it does not need to do
Host a factory, bid for a Gigafactory, or pretrain from scratch: the corpus is small, the neighbour is
capable, and Perun covers the adaptation.

#### Main blocker, and what would change the recommendation
No adopted AI strategy and no state model programme; the assistants are planned on no named model. The
recommendation would change if the strategy is adopted with a funded model line (R1 proceeds on Perun at
once), or if the Czech pool is not available (then OpenEuroLLM's weights, via ALT-EDIC where Slovakia is an
observer, become the base).

#### Sources
- Slov-Lex, Act 270/1995, https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/1995/270/, accessed 2026-10-10; Census 2021 portal, https://www.scitanie.sk/, accessed 2026-10-10.
- ČSÚ, mother tongue, https://scitani.gov.cz/matersky-jazyk, accessed 2026-10-10; KSH, table 1.1.6, https://nepszamlalas2022.ksh.hu/en/results/final-data/tables/nsz2022-1.1.6-eng.xlsx, accessed 2026-10-10.
- Computing Centre SAS, Devana, https://vs.sav.sk/en/services/supercomputer-devana/, accessed 2026-10-10; HPC at SAS, projects, https://hpc.sav.sk/en/hpc-at-sas/our-projects/, accessed 2026-10-10; NSCC, https://nscc.sk/, accessed 2026-10-10; EuroCC Slovakia, https://eurocc-slovakia.sk/, accessed 2026-10-10.
- EuroHPC JU, antennas, https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en, accessed 2026-10-10; European Commission, AI Factories, https://digital-strategy.ec.europa.eu/en/policies/ai-factories, accessed 2026-10-10.
- slovak-nlp, mistral-sk-7b, https://huggingface.co/slovak-nlp/mistral-sk-7b, accessed 2026-10-10; Qwen3-14B-sk, https://huggingface.co/slovak-nlp/Qwen3-14B-sk, accessed 2026-10-10; Jazykovedný časopis, https://journals.savba.sk/index.php/jc/article/view/4266, accessed 2026-10-10.
- KInIT, Slovak NLP community, https://kinit.sk/?p=42195, accessed 2026-10-10; about, https://kinit.sk/about/, accessed 2026-10-10.
- MIRRI, AI page, https://mirri.gov.sk/sekcie/informatizacia/umela-inteligencia/, accessed 2026-10-10; strategic approach to AI (PDF), https://mirri.gov.sk/sekcie/informatizacia/dokumenty/vladny-cloud/eska-cloud-workshop-2026/attachment/12_neprezentovane_strategicky-pristup-k-ai-v-podmienkach-slovenskej-republiky-ivan-liska/, accessed 2026-10-10.
- Slovak National Corpus, https://korpus.juls.savba.sk/, accessed 2026-10-10.
- (press) TASR, Perun, https://www.tasr.sk/tasr-clanok/TASR:2026033100000448, accessed 2026-10-10.

### Slovenia (SI)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Slovene; Italian and Hungarian have official status alongside it in the areas where those minorities live. About 2.4 million people have Slovene as their mother tongue, about 1.85 million of them in Slovenia. Minority speaker counts **[unverified]**. | https://www.gov.si/en/topics/official-language/ (accessed 2026-10-10) |
| Language shared with | About 0.55 million Slovene speakers live outside Slovenia (the difference between the two official figures; countries not named). The GaMS model card lists Croatian, Bosnian and Serbian as secondary training languages. | https://www.gov.si/en/topics/official-language/ (accessed 2026-10-10); https://huggingface.co/cjvt/GaMS3-12B-Instruct/blob/main/README.md (accessed 2026-10-10) |
| EuroHPC system on national soil | Vega at IZUM, Maribor, operational, 6.92 PFlops sustained. The 2021 national programme records the HPC RIVR budget as EUR 20 million and total HPC investment as EUR 26.5 million. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en (accessed 2026-10-10); https://www.gov.si/assets/ministrstva/MDP/National_Programme_for_AI_2025.pdf (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: SLAIF, selected 12 March 2025; IZUM will build and run a new AI-optimised system with the Jožef Stefan Institute and ARNES in a new ARNES data centre at the Mariborski otok hydro plant; partners include the Universities of Ljubljana, Maribor, Nova Gorica and Primorska; expected operational early 2027 and to replace Vega. Budget EUR 135 million is press only **[unverified]**. | https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/ai-factories/slovenia_en (accessed 2026-10-10); https://www.uni-lj.si/en/news/2025-03-14-the-university-of-ljubljana-will-play-a-key-role-in-establishing-the-slovenian-artificial-intelligence-factory (accessed 2026-10-10); https://slovenia.si/business-and-innovation/one-of-europes-most-powerful-supercomputers-to-be-built-in-slovenia (accessed 2026-10-10) |
| AI Gigafactory | No Slovenian bid found on any official page **[unverified]**. | https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en (accessed 2026-10-10) |
| National or regional model efforts | GaMS (University of Ljubljana FRI / CJVT), from the PoVeJMo programme (2023 to 2026) funded by ARIS through the Recovery and Resilience Plan with Horizon Europe support and NVIDIA sovereign-AI support. GaMS3-12B: base Gemma-3-12B, Gemma licence, about 100.9 billion tokens of continued pretraining plus parallel and long-context stages, about 150k GPU hours on Leonardo; released, with a public chatbot and local-installation support from SLAIF; a 27B Nemotron-based variant also released. Training text from a public donation campaign, the National and University Library, Dnevnik and the Slovenian Press Agency. PoVeJMo's funding amount **[unverified]**. | https://huggingface.co/cjvt/GaMS3-12B-Instruct/blob/main/README.md (accessed 2026-10-10); https://www.uni-lj.si/en/news/2026-07-20-slovene-language-obtains-its-own-generative-large-language-model-gams (accessed 2026-10-10); https://gams.povejmo.si/odprtidostop/ (accessed 2026-10-10) |
| National AI strategy | The national AI programme to 2025 (NpUI), approved 27 May 2021, about EUR 110 million over five years, with language technologies and public administration as priorities. The National AI Strategy to 2030 (NsUI 2030) was adopted 5 March 2026; its first strategic goal covers Slovene language technologies, data and models, its second public-sector use. | https://www.gov.si/assets/ministrstva/MDP/National_Programme_for_AI_2025.pdf (accessed 2026-10-10); https://oecd.ai/en/dashboards/policy-initiatives/national-ai-programme-of-slovenia-3004 (accessed 2026-10-10); https://www.gov.si/zbirke/projekti-in-programi/nacionalna-strategija-za-umetno-inteligenco-do-leta-2030/ (accessed 2026-10-10) |
| Public-sector LLM use | NsUI 2030 goal 2 targets public-sector AI use with human oversight; specific government assistant pilots or model procurements **[unverified]**. | https://www.gov.si/zbirke/projekti-in-programi/nacionalna-strategija-za-umetno-inteligenco-do-leta-2030/ (accessed 2026-10-10) |
| Language resources | CLARIN.SI (lead: Jožef Stefan Institute) with an LLM-benchmark dashboard; CJVT develops Slovene resources; the GaMS corpus target reported as 40 billion words. National corpus size **[unverified]**. | https://www.clarin.si/info/about/ (accessed 2026-10-10); https://www.cjvt.si/en/ (accessed 2026-10-10); https://slovenia.si/business-and-innovation/slovenian-in-the-age-of-artificial-intelligence (accessed 2026-10-10) |
| Key institutions | IZUM (Vega, SLAIF lead); Jožef Stefan Institute (SLAIF technical coordinator, CLARIN.SI); ARNES (data centre); SLING (EuroCC competence centre); University of Ljubljana FRI / CJVT (GaMS). | https://www.eurohpc-ju.europa.eu/ai-factories/slovenia_en (accessed 2026-10-10); https://www.sling.si/en/ (accessed 2026-10-10) |
| Power and grid | The ARNES data centre is cabled directly to the Mariborski otok hydroelectric plant, with a waste-heat agreement for Maribor; foundation stone 6 May 2025. | https://www.gov.si/en/news/2025-05-06-foundation-stone-unveiled-for-arnes-data-centre/ (accessed 2026-10-10) |

#### What good enough means here
Slovene for two million citizens in the registers of public administration, courts, health and education, with
the Italian and Hungarian minorities served in their own languages where the law requires it. Slovenia is the
rare small-language state where the national model already exists, is open, is trained on a curated and
partly donated national corpus, and has a strategy behind it that names Slovene models as its first goal.

#### Recommended strategy
**R1 is done; make it permanent. R2 to extend it. R4 under terms.**

1. **Turn PoVeJMo into a standing programme (B5).** The programme that produced GaMS ran 2023 to 2026 on
   recovery-plan money. The strategy to 2030 names Slovene models as goal 1; the budget decision that follows
   should fund the GaMS team as a permanent line at the University of Ljubljana with CJVT, with a release
   cadence tied to each new open base, and with SLAIF's local-installation support as the public-service
   deployment path.
2. **Resolve the licence question before the next generation (B3).** GaMS3 is released under the Gemma licence
   and the 27B variant under Nemotron terms. The state should hold the weights and recipe in its own
   repository and, for the next base, prefer a licence that a court reads as permitting indefinite state use;
   if the next generation stays on Gemma, say so and keep a fallback on a permissively licensed base.
3. **Train the next generation on SLAIF once it runs, not on Leonardo.** GaMS was trained mostly on Italy's
   Leonardo through EuroHPC access; from 2027 the new Maribor system brings training onto national soil and
   onto hydro power. Until then, the EuroHPC AI access calls remain the route.
4. **Pool the South Slavic neighbourhood (R2).** The GaMS corpus already carries Croatian, Bosnian and
   Serbian as secondary languages. A shared continued-pretraining run with Croatia, which has no factory, and
   with the Serbian antenna's partners, is cheap for Slovenia and large for them; the weights and continuation
   rights go in the agreement first.
5. **Build the public-sector evaluation set (B6) and the deployment under the state's rules (B2).** The
   strategy's goal 2 is public-sector use; no pilot was found. One ministry should run GaMS on SLAIF or on the
   state's own environment for a real service, and the questions it collects become the national evaluation
   set every candidate is scored on.
6. **Procure frontier access with terms (R4)** for what a 12B to 27B model cannot do, evaluated on the
   national set, with GaMS as the fallback the state possesses.

#### What it does not need to do
Pretrain from scratch, bid for a Gigafactory, or buy more compute than SLAIF: the Slovene corpus is small
enough that continued pretraining of an open base is the right technique, and the factory is the right size.

#### Main blocker, and what would change the recommendation
The team and the corpus live in a research programme that has ended on paper, and the strategy's goal has no
published multi-year budget line yet. The recommendation would change if the GaMS licence situation closes
off public-sector use (then the next generation moves base at once), or if SLAIF's new system slips well past
2027 (then Leonardo access remains the home and the pooling case grows).

#### Sources
- EuroHPC JU, additional AI Factories selected, https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en, accessed 2026-10-10.
- EuroHPC JU, Slovenia AI Factory page, https://www.eurohpc-ju.europa.eu/ai-factories/slovenia_en, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en, accessed 2026-10-10.
- EuroHPC JU, AI Gigafactories call, https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en, accessed 2026-10-10.
- Government of Slovenia, National Programme for AI 2025 (PDF), https://www.gov.si/assets/ministrstva/MDP/National_Programme_for_AI_2025.pdf, accessed 2026-10-10.
- OECD.AI, National AI Programme of Slovenia, https://oecd.ai/en/dashboards/policy-initiatives/national-ai-programme-of-slovenia-3004, accessed 2026-10-10.
- Government of Slovenia, NsUI 2030 project page, https://www.gov.si/zbirke/projekti-in-programi/nacionalna-strategija-za-umetno-inteligenco-do-leta-2030/, accessed 2026-10-10.
- Government of Slovenia, ARNES data centre foundation stone, https://www.gov.si/en/news/2025-05-06-foundation-stone-unveiled-for-arnes-data-centre/, accessed 2026-10-10.
- Government of Slovenia, official language, https://www.gov.si/en/topics/official-language/, accessed 2026-10-10.
- Slovenia.si, supercomputer, https://slovenia.si/business-and-innovation/one-of-europes-most-powerful-supercomputers-to-be-built-in-slovenia, accessed 2026-10-10; Slovenian in the age of AI, https://slovenia.si/business-and-innovation/slovenian-in-the-age-of-artificial-intelligence, accessed 2026-10-10.
- University of Ljubljana, SLAIF, https://www.uni-lj.si/en/news/2025-03-14-the-university-of-ljubljana-will-play-a-key-role-in-establishing-the-slovenian-artificial-intelligence-factory, accessed 2026-10-10; GaMS press release, https://www.uni-lj.si/en/news/2026-07-20-slovene-language-obtains-its-own-generative-large-language-model-gams, accessed 2026-10-10.
- CJVT, GaMS3-12B-Instruct model card, https://huggingface.co/cjvt/GaMS3-12B-Instruct/blob/main/README.md, accessed 2026-10-10; PoVeJMo open access, https://gams.povejmo.si/odprtidostop/, accessed 2026-10-10.
- CLARIN.SI, https://www.clarin.si/info/about/, accessed 2026-10-10; CJVT, https://www.cjvt.si/en/, accessed 2026-10-10; SLING, https://www.sling.si/en/, accessed 2026-10-10.

### Spain (ES)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Castilian is the official language of the state; Catalan and Valencian, Basque and Galician are co-official in their communities (Constitution art. 3). Population 49,128,297 (Eurostat, 1 January 2025, provisional); speakers per language **[unverified]**. | https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229 (accessed 2026-10-10); https://alia.gob.es/ (accessed 2026-10-10) |
| Language shared with | Catalan is protected in Italy (Law 482/1999); Spanish-speaking states outside the EU and the diaspora **[unverified]** from an official page. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-15;482~art2 (accessed 2026-10-10) |
| EuroHPC system on national soil | MareNostrum 5 at BSC, operational, 215.40 PFlops sustained, with a Hopper accelerated partition. | https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en (accessed 2026-10-10) |
| EuroHPC AI Factory | Two: the BSC AI Factory (selected 10 December 2024; the MareNostrum 5 AI upgrade, contract 26 January 2026, about EUR 129 million, 50% EuroHPC, installation from early 2026; consortium with Portugal, Türkiye and Romania) and 1HealthAI (selected 10 October 2025, led by CESGA in Galicia with CSIC and the Galician universities). | https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/contract-signed-boost-marenostrum-5s-ai-capabilities-2026-01-26_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/spain-1health-ai_en (accessed 2026-10-10) |
| AI Gigafactory | A bid: Móra la Nova (Tarragona) with San Fernando de Henares (Madrid) added on 14 January 2026, a public-private investment that "could exceed EUR 4,000 million", with the public vehicle SETT in the consortium, operational between 2027 and 2028. The June 2026 Council of Ministers decision on the public stake and a joint Iberian bid are press only **[unverified]**; no selection yet. | https://digital.gob.es/comunicacion/notas-prensa/mtdfp/2026/01/el-gobierno-incluira-a-madrid-en-una-candidatura-conjunta-con-ca (accessed 2026-10-10); (press) https://www.bolsamania.com/noticias/empresas/economia--amp-lopez-asegura-que-la-candidatura-espanola-para-albergar-una-gigafactoria-europea-de-ia-esta-lista--22806950.html (accessed 2026-10-10); (press) https://eco.sapo.pt/2026/07/07/governo-condiciona-200-milhoes-para-gigafabrica-ao-acesso-a-tempo-de-computacao/ (accessed 2026-10-10) |
| National or regional model efforts | ALIA, 100% publicly funded, coordinated by BSC under the State Secretariat for Digitalisation and AI, covering Castilian and the co-official languages, verified by AESIA; development phase about EUR 10 million, current phase to end June 2026, next phase being defined; weights and code Apache-2.0. ALIA-40B pretrained from scratch on 9.37 trillion tokens on MareNostrum 5; the Salamandra family likewise. Latxa (Basque, HiTZ) on Llama 3.1 and Qwen bases, trained on Leonardo, funded by the Basque and Spanish governments; Projecte Aina (Catalan, Generalitat) and Proxecto Nós (Galician). | https://alia.gob.es/ (accessed 2026-10-10); https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/case-study-alia (accessed 2026-10-10); https://huggingface.co/BSC-LT/ALIA-40b (accessed 2026-10-10); https://huggingface.co/BSC-LT/salamandra-7b-instruct (accessed 2026-10-10); https://huggingface.co/HiTZ/Latxa-Qwen3.5-4B (accessed 2026-10-10); https://projecteaina.cat/ (accessed 2026-10-10); https://nos.gal/ (accessed 2026-10-10) |
| National AI strategy | The AI Strategy 2024, approved by the Council of Ministers on 14 May 2024: EUR 1,500 million from the recovery plan for 2024 and 2025, EUR 90 million for MareNostrum, ALIA named as the language-model programme; in force. | https://www.lamoncloa.gob.es/consejodeministros/resumenes/Paginas/2024/140524-rueda-de-prensa-ministros.aspx (accessed 2026-10-10) |
| Public-sector LLM use | GobTechLab testing about 19 AI use cases; municipal citizen assistants; tax-agency tools on ALIA being explored; a primary-care assistant. | https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/case-study-alia (accessed 2026-10-10) |
| Language resources | CLARIAH-ES (CLARIN ERIC member, led by HiTZ); the Language Technologies Plan of 2019 as ALIA's origin; CATalog, about 23 billion Catalan tokens; the Aina and Nós programmes. | https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10); https://alia.gob.es/ (accessed 2026-10-10) |
| Key institutions | BSC (MareNostrum 5, ALIA, the factory); the State Secretariat for Digitalisation and AI; AESIA; CESGA; HiTZ; CiTIUS and ILG; SETT. | https://alia.gob.es/ (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/spain-1health-ai_en (accessed 2026-10-10) |
| Power and grid | The ministry's bid note stresses energy capacity and efficiency; grid figures **[unverified]**. This repository's fundamentals record an isolated grid and one of the lower electricity prices in the 27. | https://digital.gob.es/comunicacion/notas-prensa/mtdfp/2026/01/el-gobierno-incluira-a-madrid-en-una-candidatura-conjunta-con-ca (accessed 2026-10-10) |

#### What good enough means here
Castilian for forty-nine million citizens, and Catalan, Valencian, Basque and Galician as co-official
languages their administrations must serve, in the registers of administration, courts and health. Spain is
the clearest case in this note of a state that has already built the bar: a publicly funded, open-licensed,
regulator-verified model family in every official language, pretrained from scratch on a EuroHPC system on
national soil, with the regional governments funding their own languages' models beside it.

#### Recommended strategy
**R3 is done at mid scale; keep it as a standing programme. R2 as the supplier to Portugal and to the
Spanish-speaking world. R4 with terms. The Gigafactory is a separate national choice.**

1. **Fund ALIA's next phase before the gap opens (B5).** The current phase ended in June 2026 and the next
   is "being defined". The model family already meets B1, B3 and B4; a recurring line under the strategy,
   with a release cadence tied to MareNostrum 5's AI upgrade, is what turns a programme into an institution.
2. **Keep the regional lines pooled with the national one (R2, internally).** Latxa, Aina and Nós are
   funded by their governments and trained on EuroHPC systems; the national programme should guarantee them
   compute on the upgraded MareNostrum 5 and share the evaluation suite, so that Basque, Catalan and Galician
   quality rises with the Castilian model rather than beside it.
3. **Make AESIA's verification and GobTechLab's use cases the national evaluation suite (B6).** Spain already
   has a regulator checking the model; publishing the evaluation sets, with the tax and health use cases'
   real questions, gives every procured model the same yardstick.
4. **Supply Portugal and the wider Spanish-speaking world (R2).** Portugal co-funds the factory and sits in
   its consortium; a Portuguese stage on the ALIA recipe, with AMALIA's corpus, is cheaper for both than two
   programmes. Latin American administrations are a market for the same model, on terms Spain sets.
5. **Procure frontier access with terms (R4)** for what a 40B model cannot do, with ALIA as the fallback the
   state possesses.
6. **Keep the Gigafactory separate.** The Tarragona and Madrid bid, with its public vehicle, is an industrial
   choice; if selected it gives Spain frontier-class training, and the citizen model neither waits for it nor
   is argued through it.

#### What it does not need to do
Start another model programme, buy a national training cluster outside the factory, or wait for the
Gigafactory: the bar is met by what exists, and the work is continuity.

#### Main blocker, and what would change the recommendation
The next ALIA phase has no published budget and the regional programmes' funding is not visible on fetched
pages; continuity is the whole risk. The recommendation would change if the next phase is funded with a
multi-year figure (nothing else needs to change), or if the Gigafactory is selected with public-sector
training rights (R3 at frontier scale becomes a choice to cost separately).

#### Sources
- BOE, Constitución Española, https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229, accessed 2026-10-10.
- EuroHPC JU, our supercomputers, https://www.eurohpc-ju.europa.eu/about/our-supercomputers_en, accessed 2026-10-10; first seven AI Factories, https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en, accessed 2026-10-10; MareNostrum 5 AI contract, https://www.eurohpc-ju.europa.eu/contract-signed-boost-marenostrum-5s-ai-capabilities-2026-01-26_en, accessed 2026-10-10; 1HealthAI, https://www.eurohpc-ju.europa.eu/spain-1health-ai_en, accessed 2026-10-10.
- ALIA, https://alia.gob.es/, accessed 2026-10-10; OSOR case study, https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/document/case-study-alia, accessed 2026-10-10.
- BSC, ALIA-40b, https://huggingface.co/BSC-LT/ALIA-40b, accessed 2026-10-10; salamandra-7b-instruct, https://huggingface.co/BSC-LT/salamandra-7b-instruct, accessed 2026-10-10.
- HiTZ, Latxa-Qwen3.5-4B, https://huggingface.co/HiTZ/Latxa-Qwen3.5-4B, accessed 2026-10-10; Projecte Aina, https://projecteaina.cat/, accessed 2026-10-10; Proxecto Nós, https://nos.gal/, accessed 2026-10-10.
- La Moncloa, Council of Ministers 14 May 2024, https://www.lamoncloa.gob.es/consejodeministros/resumenes/Paginas/2024/140524-rueda-de-prensa-ministros.aspx, accessed 2026-10-10.
- Ministry for Digital Transformation, Gigafactory bid, https://digital.gob.es/comunicacion/notas-prensa/mtdfp/2026/01/el-gobierno-incluira-a-madrid-en-una-candidatura-conjunta-con-ca, accessed 2026-10-10.
- CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10; Law 482/1999 art. 2, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-15;482~art2, accessed 2026-10-10.
- (press) Bolsamania, https://www.bolsamania.com/noticias/empresas/economia--amp-lopez-asegura-que-la-candidatura-espanola-para-albergar-una-gigafactoria-europea-de-ia-esta-lista--22806950.html; ECO, https://eco.sapo.pt/2026/07/07/governo-condiciona-200-milhoes-para-gigafabrica-ao-acesso-a-tempo-de-computacao/; both accessed 2026-10-10.

### Sweden (SE)

#### Snapshot
| Field | Finding | Source |
|---|---|---|
| Official and recognised languages, approximate speakers | Swedish is the principal language (Language Act 2009:600 §4); the national minority languages are Finnish, Yiddish, Meänkieli, Romani Chib and Sámi (§7), with Swedish Sign Language protected (§9). Population 10,587,710 (Eurostat 2025 via the EU country page); speaker counts **[unverified]**. | https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/spraklag-2009600_sfs-2009-600/ (accessed 2026-10-10); https://european-union.europa.eu/principles-countries-history/eu-countries/sweden_en (accessed 2026-10-10) |
| Language shared with | Finland, where Swedish is an official language; mutually intelligible with Danish and Norwegian; a training language of Finland's Viking. | https://european-union.europa.eu/principles-countries-history/eu-countries/finland_en (accessed 2026-10-10); https://huggingface.co/LumiOpen/Viking-33B (accessed 2026-10-10) |
| EuroHPC system on national soil | Arrhenius at Linköping University (NAISS), mid-range, over 60 PFlops, EUR 68.5 million with EuroHPC co-funding up to 35%, inaugurated 8 September 2026. Sweden is also in the LUMI consortium. | https://eurohpc-ju.europa.eu/eurohpc-ju-inaugurates-arrhenius-new-mid-range-supercomputer-together-naiss-sweden-2026-09-08_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-procurement-contract-arrhenius-supercomputer-2025-07-10_en (accessed 2026-10-10) |
| EuroHPC AI Factory | Yes: the Sweden AI Factory (formerly MIMER), selected 10 December 2024, hosted by NAISS at Linköping with RISE; the Bull system contracted 21 April 2026 for EUR 29.76 million, 50% EuroHPC and 50% the Swedish Research Council, online in 2027; services since April 2025 with over 230 clients by October 2026; Switzerland's antenna attaches to it. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en (accessed 2026-10-10); https://www.eurohpc-ju.europa.eu/sweden_en (accessed 2026-10-10); https://www.naiss.se/?p=6302 (accessed 2026-10-10) |
| AI Gigafactory | No official Swedish page fetched **[unverified]**. | https://www.eurohpc-ju.europa.eu/sweden_en (accessed 2026-10-10) |
| National or regional model efforts | GPT-SW3 (AI Sweden with RISE and WASP), up to 40B parameters on 320 billion tokens of Swedish, Norwegian, Danish, Icelandic, English and code, released openly in November 2023 with Vinnova funding; its licence is a modified RAIL that limits access to Nordic-affiliated users and lets the licensor change terms, the 40B card for research only. Svea, the AI Sweden-led public-sector collaboration, includes fine-tuning open models and training some from scratch in its second stage. | https://huggingface.co/AI-Sweden-Models/gpt-sw3-40b (accessed 2026-10-10); https://huggingface.co/AI-Sweden-Models/gpt-sw3-20b-instruct/blob/fbd72fa5f006b18348cfb012d34a105380387e2e/LICENSE (accessed 2026-10-10); https://www.ai.se/en/news/open-release-first-large-nordic-language-model-gpt-sw3 (accessed 2026-10-10); https://www.ai.se/en/news/organizations-participating-svea-demonstrate-bold-leadership-sweden-needs (accessed 2026-10-10) |
| National AI strategy | Sweden's AI strategy, published by the government on 20 February 2026: a top-ten ambition, language models named as a research strength, fossil-free electricity as an asset for compute; the action plan **[unverified]**. | https://www.regeringen.se/informationsmaterial/2026/02/sveriges-ai-strategi/ (accessed 2026-10-10) |
| Public-sector LLM use | Svea: over 60 municipalities, regions and agencies, a chatbot used weekly by 1,500 public employees, a permanent national generative-AI service targeted in 2026; funder not named. | https://www.ai.se/en/news/organizations-participating-svea-demonstrate-bold-leadership-sweden-needs (accessed 2026-10-10) |
| Language resources | Språkbanken Text at the University of Gothenburg, the national language-data infrastructure and SWE-CLARIN lead. | https://spraakbanken.gu.se/en (accessed 2026-10-10); https://www.clarin.eu/content/participating-consortia (accessed 2026-10-10) |
| Key institutions | AI Sweden (the national applied-AI centre); NAISS and NSC at Linköping (Arrhenius; Berzelius, an A100 and H200 cluster donated by the Wallenberg foundation); RISE; WASP. | https://www.ai.se/en/about-ai-sweden (accessed 2026-10-10); https://www.nsc.liu.se/systems/berzelius/ (accessed 2026-10-10) |
| Power and grid | The strategy cites good access to fossil-free electricity; Arrhenius is 24th on the Green500; grid-connection constraints **[unverified]**. This repository's fundamentals record a low electricity price and a high renewables share. | https://www.regeringen.se/informationsmaterial/2026/02/sveriges-ai-strategi/ (accessed 2026-10-10); https://eurohpc-ju.europa.eu/eurohpc-ju-inaugurates-arrhenius-new-mid-range-supercomputer-together-naiss-sweden-2026-09-08_en (accessed 2026-10-10) |

#### What good enough means here
Swedish for 10.6 million citizens, and for Finland's Swedish speakers, with Finnish, Sámi, Meänkieli, Romani
and Yiddish where the law provides, in the registers of administration, courts and health. Sweden has a new
EuroHPC system, a factory already serving clients, a national model family whose licence is the problem, a
public-sector collaboration that already puts an assistant in front of 1,500 officials, and a strategy a few
months old. The bar is close; the gap is ownership and licence.

#### Recommended strategy
**R1 through Svea, institutionalised, on a permissively licensed base; R2 in the Nordic pool and through
LUMI; R4 with terms.**

1. **Make Svea's permanent national service the owner of a state-held model (B3, B5).** Svea's second stage
   already fine-tunes open models; the third stage is a permanent service in 2026. That service should hold
   its model's weights, recipe and corpus register in a public body's repository, with a recurring line from
   the strategy, rather than depending on a centre's project funding.
2. **Retire GPT-SW3's licence for public-service use.** A model whose licence limits access by affiliation and
   can be changed by the licensor fails B3 for a state; the next national model should be continued-pretrained
   from an Apache-2.0 base, as Finland's Viking is, and GPT-SW3 kept as research heritage.
3. **Train on Arrhenius and the factory, serve on the state's environments (B2).** Berzelius and Arrhenius
   carry the runs today; the factory's system from 2027. No further compute is needed.
4. **Pool with Finland and Denmark (R2).** Viking already covers Swedish; a Scandinavian continued-pretraining
   run on LUMI-AI with Sweden's Språkbanken corpus serves Finland's Swedish speakers at once. Rights to the
   weights in the agreement first.
5. **Build the national evaluation set from Svea's traffic (B6)** and publish it, as the yardstick for the
   national model and every procured one.
6. **Procure frontier access with terms (R4)**, the Svea model as the fallback.

#### What it does not need to do
Pretrain from scratch again, host a Gigafactory, or buy compute beyond the factory: the state's work is a
licence decision, an owner and a budget line.

#### Main blocker, and what would change the recommendation
The only large Swedish model carries a licence a public service cannot build on, and Svea's funding and the
strategy's action plan could not be confirmed. The recommendation would change if AI Sweden re-releases the
family under an open licence (the base question is moot), or if the action plan funds Svea's permanent
service with a state-held model (R1 is settled).

#### Sources
- Riksdagen, Språklag 2009:600, https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/spraklag-2009600_sfs-2009-600/, accessed 2026-10-10; European Union, Sweden, https://european-union.europa.eu/principles-countries-history/eu-countries/sweden_en, accessed 2026-10-10; Finland, https://european-union.europa.eu/principles-countries-history/eu-countries/finland_en, accessed 2026-10-10.
- EuroHPC JU, Arrhenius inauguration, https://eurohpc-ju.europa.eu/eurohpc-ju-inaugurates-arrhenius-new-mid-range-supercomputer-together-naiss-sweden-2026-09-08_en, accessed 2026-10-10; Arrhenius contract, https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-procurement-contract-arrhenius-supercomputer-2025-07-10_en, accessed 2026-10-10; Sweden AI Factory contract, https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en, accessed 2026-10-10; Sweden, https://www.eurohpc-ju.europa.eu/sweden_en, accessed 2026-10-10.
- NAISS, https://www.naiss.se/?p=6302, accessed 2026-10-10; NSC, Berzelius, https://www.nsc.liu.se/systems/berzelius/, accessed 2026-10-10.
- AI Sweden, gpt-sw3-40b, https://huggingface.co/AI-Sweden-Models/gpt-sw3-40b, accessed 2026-10-10; licence, https://huggingface.co/AI-Sweden-Models/gpt-sw3-20b-instruct/blob/fbd72fa5f006b18348cfb012d34a105380387e2e/LICENSE, accessed 2026-10-10; open release, https://www.ai.se/en/news/open-release-first-large-nordic-language-model-gpt-sw3, accessed 2026-10-10; Svea, https://www.ai.se/en/news/organizations-participating-svea-demonstrate-bold-leadership-sweden-needs, accessed 2026-10-10; about, https://www.ai.se/en/about-ai-sweden, accessed 2026-10-10.
- Regeringen, Sveriges AI-strategi, https://www.regeringen.se/informationsmaterial/2026/02/sveriges-ai-strategi/, accessed 2026-10-10.
- Språkbanken Text, https://spraakbanken.gu.se/en, accessed 2026-10-10; CLARIN consortia, https://www.clarin.eu/content/participating-consortia, accessed 2026-10-10.
- LumiOpen, Viking-33B, https://huggingface.co/LumiOpen/Viking-33B, accessed 2026-10-10.

## 6. Across the EU-27

### What the twenty-seven entries have in common

Five things recur often enough to be findings about Europe rather than about any state. Each is the author's
reading of the snapshots above; none is a printed fact of the model.

1. **The model usually exists; the owner usually does not.** In most states a model in the national language
   has been trained, often with public money, by a university, an institute or a company. In few of them does a
   ministry hold the weights, the recipe and the data register, fund the programme as a recurring line, and
   deploy it. The gap between B1 and B3 to B5 is institutional, not technical.
2. **Licences are the quiet failure.** A large share of the national models are continued pretraining of
   Llama or Gemma bases under their vendors' licences, or carry research-only or affiliation-limited terms. A
   state cannot build a public service on a licence another party can change. The states whose lines are
   Apache-2.0 or CC-BY (Spain, Portugal, Finland, Italy, Greece's Meltemi, Poland's 12B line, Latvia's
   TildeOpen, Slovakia's academic models) have an asset the others still have to make.
3. **Funding ends on a date.** Recovery-plan money, project grants and single subsidies built most of these
   models, with end dates between 2026 and 2028. The programmes that outlive the grant are the ones that have
   been written into a strategy with a budget line, and that is a decision each government has still to take.
4. **The evaluation set is nowhere published.** Several states run assistants with large traffic (Greece,
   Austria, Poland, Sweden, Estonia, Cyprus); none publishes a versioned national evaluation set. B6 is the
   cheapest property in the bar and the least done.
5. **The Gigafactory is a separate question everywhere.** Bids, purchases and abstentions are industrial and
   grid decisions. No entry's route to the bar depends on one, and `FRONTIER-MODEL.md`'s warning not to bundle
   the frontier ask with the citizen-grade one applies in every state that has both.

### Language clusters: who can share a model

A shared language is the strongest reason to pool. The table lists the clusters the entries use; the vehicle
column names the programme or factory the pool would run through.

| Cluster | States | Natural supplier or host | Vehicle |
|---|---|---|---|
| Dutch | Netherlands, Belgium (Flanders) | Netherlands (GPT-NL) | NLAIF from 2028; EuroHPC access until then |
| French | France, Belgium, Luxembourg | France (public line, Lucie) | AI2F and Alice Recoque |
| German | Germany, Austria, Luxembourg, Belgium (German community) | Germany (Teuken, SOOFI) | JAIF, HammerHAI, AI:AT |
| Greek | Greece, Cyprus | Greece (Meltemi, Krikri, Pharos) | Pharos and DAEDALUS, Pharos-CY |
| Scandinavian | Denmark, Sweden, Finland (Swedish) | Finland (Viking), Sweden | LUMI-AI, Sweden AI Factory |
| Finno-Baltic | Finland, Estonia, Latvia, Lithuania | Finland (LUMI-AI), Latvia (TildeOpen) | LUMI-AI, AIFA-LAT, LitAI |
| Czech and Slovak | Czechia, Slovakia | Czechia (OpenEuroLLM coordination, CZAI) | CZAI and KarolAIna, SKAIAT |
| South Slavic | Slovenia, Croatia, with Serbia's and North Macedonia's antennas | Slovenia (GaMS, SLAIF) | SLAIF, IT4LIA |
| Iberian | Spain, Portugal | Spain (ALIA), Portugal (AMALIA, EuroLLM) | BSC AI Factory, MareNostrum 5 |
| Italian and its minority languages | Italy, with Slovene, German, French and Croatian from the neighbours | Italy (Minerva), neighbours as suppliers | IT4LIA |
| Hungarian | Hungary, with minorities in Slovakia, Romania and Serbia | Hungary (PULI) | HunAIFA and JUPITER, Levente |
| Romanian | Romania, Moldova | Romania (OpenLLM-Ro, RO AI) | RO AI Factory, PIAST for Moldova's antenna |
| Bulgarian | Bulgaria, with North Macedonia's antenna | Bulgaria (BgGPT) | BRAIN++ |
| Polish | Poland, as supplier to its Baltic partners | Poland (PLLuM, Bielik) | PIAST, Gaia |
| Single languages with English | Ireland (Irish), Malta (Maltese) | the state itself, on an English-strong base | AIF IRL-Antenna, CALYPSO, ALT-EDIC |

### The states by recommended route

The groups below are a recommendation and not a ranking. Inside a group the states are alphabetical by
English name and the order carries no meaning (#10, #77). A state's group says which route the entry
recommends as primary; every entry also recommends R4 with terms, and most recommend a second route.

| Route | States (alphabetical; no order) |
|---|---|
| R1 · a funded national line exists: institutionalise it, settle its licence, deploy it | Bulgaria (BG), Denmark (DK), Estonia (EE), France (FR), Germany (DE), Greece (EL), Hungary (HU), Italy (IT), Netherlands (NL), Poland (PL), Portugal (PT), Romania (RO), Slovenia (SI), Sweden (SE) |
| R1 · start the national line on an existing open base with the state's own corpus | Czechia (CZ), Ireland (IE), Latvia (LV), Lithuania (LT), Malta (MT) |
| R2 · pool with a language neighbour as the primary route, with a small R1 stage on top | Austria (AT), Belgium (BE), Croatia (HR), Cyprus (CY), Luxembourg (LU), Slovakia (SK) |
| R3 · mid-scale pretraining is already the state's practice: keep it as a standing programme | Finland (FI), Spain (ES) |

### What every state should do first

Whatever the route, the same four moves open it, and none costs much:

1. **Name an owner.** One public body that holds the weights, the recipe and the data register, with a
   recurring budget line and a release cadence (B3, B5).
2. **Settle the licence.** Decide which base licence the public-service model will carry, and keep a
   fallback on a permissively licensed base if the chosen one can change (B3).
3. **Publish the evaluation set.** From the first public service's traffic, versioned, scored for every
   candidate, national or procured (B6).
4. **Write the terms into every procurement.** Hosting under the state's rules, continuity, escrow or a
   national fallback, and evaluation on the national set before each version (B2, R4).

## 7. Caveats

1. **Authored judgement.** The strategy in every entry is one author's reading of the building blocks on
   2026-10-10. Two people with the same snapshots could recommend differently; the groups in section 6 are
   defensible, the choice between adjacent routes for a given state often is not.
2. **The snapshots are current to their access dates and no later.** AI Factory selections, Gigafactory awards,
   model releases and strategies move within months. A cell is evidence of what a page said on the day it was
   read, not of what is true when this is read.
3. **Cited, not checked.** The repository's evidence pipeline (fetch, hash, quote check, independent review,
   cross-model fact check: #82, #87) did not run on this note. The link register records that each URL answered
   on the day of the check; it does not record that the page says what the cell says. **[unverified]** marks the
   cells the researcher could not confirm from a fetched page, and nothing should be quoted from them.
4. **Speaker counts are approximate and from secondary sources** where the entry says so. They are a proxy for
   corpus size, not a measurement of it.
5. **No cost per state.** The band table in section 2 is reconstructed order-of-magnitude, given once; a state's
   own figure depends on what it already pays for people and compute. Nothing here is a budget.
6. **The repository's own model half is still unsourced.** `FEASIBILITY-RANKING.md` was superseded for ranking
   on unsourced research; this note does not quote it as a finding, and until the follow-on in section 8 lands,
   none of the building blocks here is a printed fact of the model.
7. **"Good enough" is a bar set here.** A state may set a higher one, or a different one, and the routes do not
   change; only the point at which a state stops does.
8. **The EU vehicles are described from their official pages as of October 2026**, which say what is planned and
   selected, not what is operating; where an entry depends on a facility that is not yet operational it says so.

## 8. Status and next steps

| Step | State |
|---|---|
| Bar, routes and building blocks written | ✅ 2026-10-10 |
| Snapshots for all 27 states collected with URLs and access dates | ✅ 2026-10-10, seven research agents |
| Strategy written per state, states grouped by route | ✅ 2026-10-10 |
| Every cited URL fetched once; non-200 lines marked unverified | ✅ 2026-10-10, `docs/national-ai-strategies-links.csv` |
| Gate checks the note's contract (`tests/test_national_ai.py`) | ✅ 2026-10-10 |
| Second-model review of the entries against their cited pages | ⬜ Owner's call; would be written to `docs/plans/national-ai-strategies-factcheck-<date>.md` |
| The sourced follow-on: reviewed yes/partial/no indicators per state in their own section and overview | ⬜ Planned, `ROADMAP.md` § Planned |

When the follow-on lands, the snapshot tables here become a pointer to the generated overview and only the
strategies stay authored (#101).

The working log of the session that produced this note, with the decisions, the research run, the counts and the
problems met, is [`docs/plans/national-ai-log.md`](docs/plans/national-ai-log.md).
