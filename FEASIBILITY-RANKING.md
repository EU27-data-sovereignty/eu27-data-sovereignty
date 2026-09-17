# Feasibility ranking: sovereign data centers and sovereign AI models

**Authored note, 2026-09-13. Not generated, and not part of the model, the JSON bundle or the web app.**
It answers one question that the rest of the repository deliberately does not: *across the EU-27, how
feasible is it for each state to put together a credible national plan for both sovereign government
data centers and sovereign AI models?*

Read the [caveats](#caveats) before quoting anything here. This note ranks, which `DECISIONS.md` #10
rules out for the model and the app; the bounded exception and its conditions are recorded in #59.

---

## Contents

- [What the question means](#what-the-question-means)
- [Method](#method)
- [The ranking](#the-ranking)
- [Where the two halves diverge](#where-the-two-halves-diverge)
- [Caveats](#caveats)
- [What would change the ranking](#what-would-change-the-ranking)
- [Status and next steps](#status-and-next-steps)

---

## What the question means

**"Sovereign data centers"** is the question the model already answers: a state-controlled
government-cloud core, sized per country in `countries/<ISO>/` and summarised in
`countries/SUMMARY.md`.

**"Sovereign data models"** is read here as **sovereign AI / language models** — the adjacent question
`countries/NL/FRONTIER-MODEL.md` asks for the Netherlands. If the intended meaning was data models in the
schema sense (common government data standards, interoperability), the model half of this note does not
apply and would have to be redone.

**"Feasible" means a credible national plan, not frontier parity.** `FRONTIER-MODEL.md` §4 defines three
tiers, and they set the bar:

| Tier | What it is | Who can do it |
|---|---|---|
| 1 — Sovereign deployment | Fine-tune and serve open-weight models on national soil, under national law | Every member state. Does not discriminate, so it barely affects the ranking |
| 2 — Mid-scale pretraining | A national 5k–20k accelerator cluster and a standing training organisation | A minority. **This is what the model half of the ranking mostly measures** |
| 3 — Frontier parity | 100k+ accelerators, ~150 MW firm power | No state alone; only as lead partner in an EU AI Gigafactory consortium |

The two halves are weighted equally. Neither is allowed to rescue a state that is weak on the other.

## Method

### Data center half — from this repository

Taken from `model/eu27_parameters.csv`, the same columns the sovereignty matrix shows:

| Input | Column | Better for feasibility |
|---|---|---|
| Government cloud maturity | `gov_cloud_maturity` | federated > operational > pilot |
| Certification regime | `certification_strength` | stringent > national > baseline |
| Dependence on US hyperscalers | `hyperscaler_dependency` | low > medium > high > critical |
| Power cost | `elec_price_eur_mwh` | lower |
| Clean power | `renewables_pct` | higher |
| Physical constraints | `grid_isolated`, `seismic`, `frontline` | absent (frontline also raises political urgency, so it cuts both ways) |
| Scale | `gdp_eur_bn`, and the site floor from `min_sites` | enough fiscal room; not a micro state where sites shrink below 1 MW |
| Momentum | `sovereign_cloud_initiative` | a recent, funded, government-level decision |

The three ordinal columns are **author judgements, not measurements** (`model/README.md`), and only 2 of
the 189 legal and regulatory cells are sourced as of 2026-09-11.

### Model half — from outside this repository

**None of this is in `eu27_parameters.csv`.** It was assembled from general knowledge current to roughly
May 2026 and has not been checked against sources. It weighs:

- **An existing national model effort**, especially one that is state-funded (ALIA, PLLuM, GPT-NL) rather
  than purely commercial or academic
- **Compute on national soil**: a EuroHPC supercomputer, or hosting a EuroHPC AI Factory (AIF below)
- **Language corpus size**, and whether a neighbour's model already covers the language (Dutch in
  Flanders, German in Austria, Greek in Cyprus)
- **Training talent and an AI lab ecosystem**
- **Fiscal capacity** and any AI Gigafactory bid

### Combining them

Each state was placed into one of four groups by judgement, not by arithmetic, and ordered within the
group. **The groups are the finding; order within a group is not.** Adjacent states in the same group
could swap on a different reasonable weighting.

## The ranking

Abbreviations: maturity federated / operational / pilot; certification stringent / national / baseline;
dependency is hyperscaler dependency. **AIF** = hosts a EuroHPC AI Factory; **AIF?** = believed to, not
confirmed — the least certain column in this note.

### Group A — building blocks exist for both halves

| Rank | Country | Data centers (repo) | Models (unverified) | Main blocker |
|---:|---|---|---|---|
| 1 | France | federated · stringent · low dependency · €153/MWh | Mistral, Lucie, Jean Zay, AIF | Few; choosing among qualified SecNumCloud providers |
| 2 | Germany | federated · stringent · medium dependency | Teuken (OpenGPT-X), Aleph Alpha, JUPITER, two AIFs | €226/MWh power; federal coordination |
| 3 | Spain | operational · national · medium dependency · €132/MWh · 60% renewables | ALIA (state-funded), MareNostrum 5, AIF | No single state cloud; grid-isolated |
| 4 | Italy | federated (PSN) · national · medium dependency | Minerva, Velvet, Italia; Leonardo, AIF | Seismic; €220/MWh power |

Spain and Italy are close. Spain is placed above on the strength of a state-funded national model and
cheaper power; Italy's Polo Strategico Nazionale is the more mature sovereign data center.

### Group B — one half strong, the other workable

| Rank | Country | Data centers (repo) | Models (unverified) | Main blocker |
|---:|---|---|---|---|
| 5 | Finland | operational · national · medium dependency · €75/MWh (lowest in the EU-27) | LUMI, Poro/Viking, AIF | Small language; frontline |
| 6 | Netherlands | pilot, with a July 2026 cabinet decision · national · high dependency | GPT-NL (€13.5M), Snellius, AIF? | Grid congestion. Already worked through in this repository |
| 7 | Poland | operational · baseline · high dependency · frontline | PLLuM (state-funded), Bielik, AIF | Hyperscaler dependency |
| 8 | Sweden | pilot · baseline · high dependency · €97/MWh · 88% renewables | GPT-SW3, AIF | No single state cloud |
| 9 | Czechia | operational (eGC, security level 4) · national · medium dependency | IT4I, AIF?; little national model work | Model half is thin |
| 10 | Estonia | operational · national · **low dependency**; data embassy in Luxembourg | TartuNLP; very small corpus | Easy data center, hard model |
| 11 | Denmark | pilot · baseline · **critical dependency** · €122/MWh | Gefion, Danish Foundation Models | The mirror image of Estonia |
| 12 | Portugal | sovereign-cloud plan approved May 2026 · €133/MWh | Amália, Deucalion, AI Gigafactory bid | Seismic; grid-isolated |

### Group C — data center plan workable; model plan leans on the EU or a neighbour

| Rank | Country | Summary |
|---:|---|---|
| 13 | Greece | G-Cloud operational; Pharos AIF, Meltemi and Krikri models. Seismic |
| 14 | Austria | BRZ operational, 90% renewables; German-language models reusable. High dependency |
| 15 | Romania | ~€560m RRF-funded plan for four government DCs; AIF?, OpenLLM-Ro, Gigafactory bid. Frontline and seismic |
| 16 | Bulgaria | State hybrid cloud operational; BgGPT strong for the country's size, AIF. Frontline and seismic |
| 17 | Slovenia | DRO state cloud; Vega, AIF, GaMS. Very small |
| 18 | Luxembourg | State-owned Tier IV LuxConnect DCs, MeluXina, AIF. Micro state: two sites |
| 19 | Belgium | Federal G-Cloud, but Google chosen as the public-cloud pillar (June 2026); Dutch and French models come from neighbours |
| 20 | Lithuania | State cloud run under the Ministry of National Defence; AIF?. Frontline |
| 21 | Hungary | Government cloud operational; PULI, Komondor. €213/MWh power |
| 22 | Latvia | Federated state cloud completed May 2026; TildeOpen. Small |

### Group D — hard as a stand-alone national plan; federate instead

| Rank | Country | Main blocker |
|---:|---|---|
| 23 | Slovakia | €209/MWh power; almost no model work |
| 24 | Croatia | Seismic; almost no model work |
| 25 | Ireland | Highest power price (€255/MWh), critical dependency, grid-isolated, data center grid pressure |
| 26 | Cyprus | Pilot-stage cloud, grid-isolated, €243/MWh; can reuse Greek-language models |
| 27 | Malta | Government hybrid cloud partly on Azure, grid-isolated, micro state |

## Where the two halves diverge

A single rank hides the most useful thing the exercise shows: **for many states the two halves point in
different directions.**

- **Easy data center, hard model — Estonia, Luxembourg, Latvia.** Mature, low-dependency state clouds, but
  corpora too small for national pretraining. Their realistic model plan is Tier 1 only.
- **Hard data center, workable model — Denmark, Sweden.** Real model and compute assets (Gefion, GPT-SW3,
  cheap clean power) sitting beside pilot-stage government clouds and high or critical dependency.
- **The language is already covered — Belgium, Austria, Cyprus, Ireland, Malta.** A neighbour's or a
  global model already serves the language. The "sovereign model" need there is about jurisdiction and
  control (Tier 1), not language, and a national pretraining programme would be hard to justify.
- **The frontier question is an EU question for everyone.** `FRONTIER-MODEL.md` §3 and §4 apply to every
  state on this list: Tier 3 exists only through AI Gigafactory consortia, which cluster around Germany,
  France, Portugal, Finland and Romania.

The README already records that states under ~3 MW cannot sustain three in-country sites. **Groups C and
D are largely those states**, and the same logic extends to models: the credible plan is a national core
plus an EU federation layer, which this repository keeps out of scope.

## Caveats

1. **It is a ranking, and #10 exists for a reason.** Certification strength, seismic risk and corpus size
   do not add. The groups are defensible; a precise rank is not, and "Ireland is 25th" is exactly the kind
   of line that gets quoted without this paragraph.
2. **The data center half inherits the repository's verification gap.** Three of its inputs are the
   author's ordinal judgements, and the legal cells behind them are 2 of 189 sourced (`VERIFICATION.md`).
3. **The model half is below even that standard.** It is from memory, current to roughly May 2026, with no
   ledger rows and no quotes. The AIF column in particular must be checked before anything is cited.
4. **It is a snapshot.** Several inputs changed within weeks of this note: the Dutch cabinet decision
   (July 2026), Portugal's sovereign-cloud plan (May 2026), Belgium's Google selection (June 2026), the
   EuroHPC Gigafactory call (July 2026).
5. **"Sovereign data models" was interpreted, not specified.** See [What the question means](#what-the-question-means).

Under `DECISIONS.md` #25, the public repository is a publication channel. This note carries its caveats in
the body, not only in a header, for the same reason the country briefs do.

## What would change the ranking

- **Sourcing the model half** — especially AI Factory hosting and the status of each national model —
  could move several Group B/C boundaries (Czechia, Netherlands, Romania, Lithuania).
- **AI Gigafactory awards.** A state named lead partner of a Gigafactory moves up regardless of its
  national model effort.
- **Verification of the ordinal columns.** A change to `hyperscaler_dependency` for Denmark, Ireland or
  Belgium would move them directly.
- **A different weighting.** Weighting the data center half more heavily lifts Estonia, Luxembourg and
  Latvia and drops Denmark and Sweden; weighting models more heavily does the reverse.
- **A different reading of "data models"**, which replaces the model half entirely.

## Status and next steps

| Step | State |
|---|---|
| Ranking drafted, both halves, all 27 states | ✅ 2026-09-13 |
| Recorded as a bounded exception to #10 | ✅ `DECISIONS.md` #59 |
| Model-half facts sourced (AI Factories, national models, Gigafactory bids) | ⬜ Not started |
| Confirm the intended meaning of "sovereign data models" | ⬜ Open |
| Re-rank after sourcing, and record what moved | ⬜ Waits on the step above |

Progress on these is tracked in `ROADMAP.md`, and changes to this note are logged in `CHANGELOG.md`.
