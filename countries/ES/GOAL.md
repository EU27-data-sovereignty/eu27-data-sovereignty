# Spain: critical data holdings and sovereign hosting

> Generated 2026-09-29 by `model/generate_countries.py` from the content model (`model/document.py`). The same document is typeset as the country PDF and rendered on the web.
>
> **Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.** A value that no checked source supports is withheld and shown as a gap. A gap means not yet sourced, never that the thing does not exist. A value in *italics* is withheld.

## Contents

1. [Data-sovereignty placement](#1-data-sovereignty-placement)
2. [Fundamentals](#2-fundamentals)
3. [Critical data holdings, by priority](#3-critical-data-holdings-by-priority)
4. [Foreign-dependency exposure](#4-foreign-dependency-exposure)
5. [Legal and institutional posture](#5-legal-and-institutional-posture)
6. [Capacity](#6-capacity)
7. [Research still open](#7-research-still-open)

## 1. Data-sovereignty placement

> Not demonstrated. Confidence: Low. With the evidence still open, Spain could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1] |
| Classification in law | Yes[^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4][^s5] |
| State-controlled national eID | Yes[^s6][^s7] |
| Government data centres | Yes[^s8][^s9][^s7] |
| Government cloud in operation | Yes[^s8][^s9] |

What could move this placement:

- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Spain described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 49.59 million[^s10] |
| GDP, current prices | 1 690.0 EUR bn[^s11] |
| Public administration employment (NACE O) | 1 727.4 thousand[^s12] |
| Non-household electricity price | 132.4 EUR/MWh[^s13] |
| Renewables share of electricity | 60.7 %[^s14] |
| Land area | 502 654 km²[^s15] |

## 3. Critical data holdings, by priority

The holdings Spain cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 30 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Registro Civil (Civil Registry): a single, electronic register for all of Spain[^s16] | Registry officers work under the functional authority of the Dirección General de Seguridad Jurídica y Fe Pública (Ministry of Justice)[^s16] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | ADDNIFIL (automated DNI file holding photographs and fingerprints)[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | *Disputed: sources disagree. Agencia Estatal Boletín Oficial del Estado — Real Decreto 255/2025, de 1 de abril, por el que se…, 2025-04-02 gives the value this report printed; Agencia Estatal Boletín Oficial del Estado — Orden INT/1202/2011, de 4 de mayo, por la que se regulan…, 2011-05-13 gives “ADDNIFIL (automated DNI file holding fingerprints and photographs)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | Dirección General de la Policía has custody of the DNI personal-data processing[^s6] | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Digitised data in the Civil Registry database are being migrated into individual records by the Ministry of Justice[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | ADDNIFIL (national identity document management file)[^s17] | Dirección General de la Policía (Directorate-General of Police), Ministerio del Interior[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | censo electoral (electoral roll)[^s19] | Oficina del Censo Electoral (Electoral Census Office), within the instituto nacional de estadística[^s19] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | AC Raíz FNMT-RCM (FNMT-RCM root certification authority)[^s20] | Fábrica Nacional de Moneda y Timbre-Real Casa de la Moneda (state public business entity)[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Disputed: sources disagree. Agencia Estatal Boletín Oficial del Estado — Real Decreto Legislativo 1/2004, texto refundido de la…, 2004-03-08 gives the value this report printed; Agencia Estatal Boletín Oficial del Estado — Decreto de 8 de febrero de 1946, Ley Hipotecaria… gives “Registro de la Propiedad (Property Registry)”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | Ministerio de Hacienda (Ministry of Finance)[^s22] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | The system comprises the Central Register of Convicted Persons, the Central Register for Protection of Victims of Domestic and Gender Violence, and others[^s23][^s24] | The registry system is non-public and depends on the Ministry of Justice[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | PERPOL (records of persons of police interest)[^s17] | Gabinete de Coordinación de la Secretaría de Estado de Interior (Coordination Cabinet of the Secretariat of State for the Interior), for the Base de Datos de Señalamientos Nacionales[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Ley General Tributaria: tax functions include issuing tax ID numbers and maintaining the tax censuses[^s26] | AEAT's Departamento de Informática Tributaria includes sub-directorates for IT planning and for operations (Explotación)[^s27][^s28] | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | Registro de Prestaciones Sociales Públicas (Register of Public Social Benefits)[^s29] | Instituto Nacional de la Seguridad Social (National Social Security Institute)[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | The SNS protected-population database generates a unique personal health ID code[^s30][^s31] | The law assigns the Ministry of Health to generate the unique SNS personal ID code[^s30][^s31] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Registro Mercantil (Commercial Registry), with the Registro Mercantil Central[^s32] | Ministerio de Justicia (Ministry of Justice)[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Vehicle Register of the Jefatura Central de Tráfico[^s33] | The Driver and Offender Register is kept by the Jefatura Central de Tráfico[^s33][^s34] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | N.SIS II/SIRENE II (national part of the Schengen Information System)[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Registro Nacional de Armas (National Firearms Register)[^s35] | Intervención Central de Armas y Explosivos de la Dirección General de la Guardia Civil (Central Arms and Explosives Office, Guardia Civil)[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | The Central Personnel Register is the AGE register of its staff and of acts affecting their careers[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | base de datos de los resultados electorales del Ministerio del Interior (Ministry of the Interior election results database)[^s37] | Indra Soluciones Tecnologías de la Información, S.L.U. (contractor for the provisional-count service)[^s37] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | Central de Información de Riesgos (Central Credit Register), Banco de España[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | SIRDEE, the State digital emergency radio system, is coordinated by the Secretariat of State for Security[^s39] | The 112 emergency call service is provided by the Autonomous Communities through their own call centres[^s40] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Red de Alerta Nacional de Protección Civil (National Civil Protection Alert Network)[^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Cecoel (Centro de Control Eléctrico, Electricity Control Centre)[^s42] | Red Eléctrica de España, S.A. (sole transmission operator)[^s43] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | Sistemas Automáticos de Información Hidrológica (SAIH) (Automatic Hydrological Information Systems), used by the Confederaciones Hidrográficas[^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Education (tier 1) | Registro Nacional de Titulados Universitarios Oficiales (RNTUO) (National Register of Official University Graduates)[^s45] | Ministerio de Educación (Ministry of Education; the register now sits with the universities ministry)[^s46] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | The BOE is published in an electronic edition[^s47] | The Agencia Estatal BOE edits, publishes and distributes the official gazette[^s47] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Municipalities send their Padrón data to the INE for national coordination[^s48] | INE is an autonomous body with its own legal personality[^s49] | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | Reference geographic information includes cadastral parcels and registered real estate[^s50] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 30 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 30 |

## 5. Legal and institutional posture

0 of 8 posture entries have a verified source. The others were researched from public policy documents but are withheld here until each is checked against the governing instrument.

| Dimension | Position |
|---|---|
| Governing instrument | *Not yet sourced* |
| Sovereign or government cloud | *Not yet sourced* |
| Cloud certification | *Not yet sourced* |
| Data classification | *Not yet sourced* |
| Procurement route | *Not yet sourced* |
| National digital identity | *Not yet sourced* |
| Internet exchange | *Not yet sourced* |
| Hyperscaler regions in country | *Not yet sourced* |

## 6. Capacity

> Not yet sized. Capacity for Spain will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Spain without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Authentication audit log (tier 0)
- Customs declarations (tier 1)
- Treasury and state accounts (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)

## Appendix: methodology

*Method · how this was made*

### What this is, and what it is not

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template.

This appendix is generated from the code and data that produced this document. Every rule below is the rule the build runs, and every number is counted from the files it reads. In this build: 1388 facts are printed, 3342 values are withheld as gaps, and 22 are withheld as disputed.

### How sources were found

Research agents, one per member state, looked for each critical holding and each indicator. Each claim needed a verbatim quote of 8 to 60 words from an exact URL. Nothing an agent returned was used until it passed the mechanical checks below. Agent output is staged separately and is never rendered.

| Quote check of the first research runs | Claims |
|---|---:|
| exact | 2138 |
| loose | 20 |
| not_found | 107 |
| fetch_failed | 251 |

A vetting run then re-examined every printed fact, and after it the gaps. It looked for a better source, for newer information and for any source that disagrees. Each of its findings was judged by a blind reviewer, shown the quote and URL but never the proposed value. Runs: wf_1c6b8bb6-450. Reviewer model: claude-opus-5-5, the same model as the researcher.

| Vetting outcome | Findings or items |
|---|---:|
| below_T2 | 5 |
| corroborated | 238 |
| disputed | 10 |
| filled_gap | 363 |
| holding_not_established | 38 |
| no_better_found | 447 |
| not_reached | 201 |
| not_verified | 176 |
| review_disagreed | 153 |
| same_source | 8 |
| superseded_higher_tier | 23 |
| superseded_later_same_authority | 3 |

Every cited source is re-fetched periodically and each quote looked for again. A fact whose quote has vanished, or whose source is gone, is withheld as disputed. A refusal to serve the page changes nothing.

| Latest recheck | Sources |
|---|---:|
| changed_quotes_present | 373 |
| gone | 3 |
| quote_vanished | 3 |
| unchanged | 306 |
| unreachable | 6 |

### What must hold for a fact to be printed

- Researched claims (holdings, operators, legal bases, indicators): the cited page or PDF was downloaded and its SHA-256 recorded, and the quoted text was found in the extracted document by literal matching. Every number and date in the printed value was found in the original-language quote; the English wording is a machine summary of the quote unless it appears in it verbatim. An archived copy was looked up on the Internet Archive; where none exists the footnote says so.
- Eurostat figures: the value was read from a pinned Eurostat dataset through its API and compared with the table cell, within 0.5%. The raw API response is stored and its SHA-256 recorded in model/fetch_manifest.csv. The footnote names the dataset, its dimensions and the retrieval date.
- Categorical findings (infrastructure dependency, sovereignty indicators): admitted only when a second, independent automated reviewer reached the same value from the same quote.

The printed value is checked against its quote at build time. Every number and date in it must appear in the original-language quote, read in any EU number format. A number found only in the English translation does not count. An abbreviation not found in the quote is shown in the fact's checklist. A value that is not a verbatim extract is a machine summary of the quote, and is labelled as one.

A value that no checked source supports is withheld and shown as a gap. A gap means not yet sourced, never that the thing does not exist.

### Source tiers

How good is the best source behind each fact? Each cited host is classified once. An archived copy counts as the page it archived. The classification was drawn up by an agent and has not been reviewed by a person.

| Tier | Printed facts |
|---|---:|
| T1 authoritative original (official law portal, statistics office, Eurostat) | 633 |
| T2 competent public body or audit office | 633 |
| T3 other institution or company | 9 |
| T4 secondary (unofficial law mirror, press, encyclopedia) | 113 |

### Evidence grades

Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict.

| Grade | Printed facts |
|---|---:|
| Verified | 0 |
| Strong | 106 |
| Standard | 1282 |

There is no numeric confidence score: nothing has calibrated one.

### Calculations

Priority of a holding. Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

Infrastructure exposure counts, for each state, the verified holdings whose cited source says where the infrastructure runs. Silence counts as not stated, never as national.

Data-sovereignty placement. An input without a checked source is unknown and counts as not demonstrated: never as sovereign, never as dependent. Each state is placed by the first rule it meets, in this order:

- Dependent on non-EU providers: a source shows a tier 0 or 1 holding on non-EU infrastructure, or a national eID or trust anchor outside state or EU control.
- Sovereign in law and in practice: a statute keeps government data under national or EU jurisdiction, and at least 75% of verified tier 0/1 holdings run on national or EU infrastructure, the trust anchor and eID are state-controlled, and the state runs its own data centres or government cloud.
- Sovereign in practice, not secured in law: the practice test, without the statute.
- Secured in law, not yet in practice: the statute, without the practice test.
- Not demonstrated: neither.

Confidence is how many groups a state could still reach if every unknown resolved for or against it: one group is High, two Medium, three or more Low. Within a group, states are alphabetical; the order carries no meaning.

Fundamentals are Eurostat values at a pinned period, read through the dissemination API. Each is multiplied into the unit shown and rounded, and must reproduce the published value within 0.5%:

| Figure | Dataset | Filters | Period | Scale | Decimals |
|---|---|---|---|---|---|
| population_m | tps00001 | indic_de=JAN | 2026 | × 1e-06 | 3 |
| gdp_eur_bn | nama_10_gdp | na_item=B1GQ; unit=CP_MEUR | 2025 | × 0.001 | 1 |
| gov_employment_k | nama_10_a64_e | na_item=EMP_DC; nace_r2=O; unit=THS_PER | 2024 | × 1 | 1 |
| elec_price_eur_mwh | nrg_pc_205 | currency=EUR; nrg_cons=MWH500-1999; tax=X_VAT; unit=KWH | 2025-S2 | × 1000 | 1 |
| renewables_pct | nrg_ind_ren | nrg_bal=REN_ELC; unit=PC | 2025 | × 1 | 1 |
| land_km2 | reg_area3 | landuse=L0008; unit=KM2 | 2026 | × 1 | 0 |

### The cross-model fact check before every deploy

Before anything is published, every printed fact is checked once more, exactly as printed, by a second model: the one that did not write it. The checker fetches the cited source and decides whether it supports the statement as printed. A production deploy is refused unless every printed fact has a current verdict of supported. The rule, the steps and each fact's verdict are in the fact-check appendix.

| Fact written by | Checked by |
|---|---|
| claude-opus-5-5 | claude-fable-5-1 |
| claude-fable-5-1 | claude-opus-5-5 |
| anything else: unrecorded, a person, or a program | claude-fable-5-1 |

In this build, 28 of 1388 printed facts pass the fact check.

### Citizens and human review

Anyone in any member state may submit a source or check a printed fact, through public issue forms. A submitted source passes the same mechanical checks as agent research. A fact counts as verified by a person only under the two-person rule: confirmed by someone on the reviewer roster, who did not submit it, who reads the source's language, and who declared no conflict of interest. One such rejection makes a fact disputed; two withdraw it, unless two reviewers confirmed it.

| Human review | Count |
|---|---:|
| Facts verified by a person | 0 |
| Facts disputed by a reviewer | 0 |
| Facts withdrawn after review | 0 |
| Reviewers on the roster | 0 |
| Citizen submissions staged | 0 |

### Questions answered on the web

The web page's Ask feature answers questions using only these sourced findings, with a citation for every fact. Each question is sent to Anthropic's API to generate the answer and is not stored by this site. The model is told the findings are machine-checked and to say so in every answer.

### Reproducing this document

Everything is built from the project's repository. `./run.sh reproduce` rebuilds every output in a fresh clone and compares it with the published one. `./run.sh reproduce --evidence` also re-fetches every cited source and checks every quote again. The git commit and the data bundle's SHA-256 this document was built from are printed on its title page.

Not reproducible byte for byte: agent research gives different findings if run again, so what is reproducible is their admission, from the recorded outputs. Also not: the posters (browser screenshots), and the hash of a page rendered in a browser.

### What this does not establish

- No person has verified any finding. Agents found and checked everything.
- The blind reviewer during research was the same model as the researcher, so the two readings can share its blind spots. The fact check before each deploy uses a different model, which narrows that risk but does not remove blind spots that models share.
- English wording of a non-English source is a machine translation or machine summary. Its figures are checked against the original; its words are not.
- A gap means not yet sourced. It never means the thing does not exist.
- Most states do not publish where their critical registers are hosted, so placements are mostly of low confidence. That is a finding about transparency, not about sovereignty.

## Appendix: fact check

*Method · how this was made*

### What was checked, and by whom

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. The check below is made by a second model, not by a person.

Every printed fact is put, exactly as printed, to a checker that is a different model from the one that wrote it. The checker fetches the cited source and decides whether it supports the statement as printed: the same value, name, unit, date, country and scope. A fact it does not confirm is withheld, shown as disputed with the checker's reason, until it is corrected and checked again. A production deploy is refused unless every printed fact has a current verdict of supported from an eligible checker.

In this build, 28 of 1388 printed facts pass, and 2 facts are withheld after the check.

| Fact written by | Checked by |
|---|---|
| claude-opus-5-5 | claude-fable-5-1 |
| claude-fable-5-1 | claude-opus-5-5 |
| anything else: unrecorded, a person, or a program | claude-fable-5-1 |

### How a check runs

- factcheck.py prepare lists every printed fact whose verdict is missing, stale or not passing, hashes each as printed, names its author from the recorded files, and assigns the checker by the rule.
- The checked-in workflow (model/research/factcheck/workflow.js) asks for that checker model by name, one agent per batch of one state's facts. The checker fetches each cited page (or the Eurostat API response), looks for the quote, and decides whether it supports the statement exactly as printed: value, unit, date, country and scope. It answers supported, not supported or unclear, with a reason.
- factcheck.py stage refuses any batch whose checker reports a different model than the one asked for, or is an author of a fact in it.
- factcheck.py record writes the verdicts to the ledger, the run's manifest (input, workflow and bundle hashes, commit, counts) and this audit file.
- A fact the checker does not confirm is withheld: it is shown as disputed, with the checker's reason, instead of printed, until the fact or its source is corrected and checked again. The verdict stays on the record.
- Before every production deploy, factcheck.py gate requires a current supported verdict from an eligible checker for every printed fact, and this file to be current.

A verdict holds for one fact exactly as printed: a SHA-256 of the claim, the question it answers, the printed text and every citation behind it. If any of these changes, the verdict lapses and the fact must be checked again before the next deploy.

### Fact-check runs

| Run | Date | Facts checked | Checker models | Verdicts |
|---|---|---:|---|---|
| wf_074137f6-b8e | 2026-10-01 | 30 | claude-fable-5-1: 30 | supported: 28; not supported: 2 |

### The verdict on each fact about Spain

0 of 58 printed facts about Spain pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:ES:L1 | indicator L1: Does a statute or binding regulation require government data (or classified government data) to be stored and processed under national or EU jurisdiction? | unrecorded | none | never checked |  |
| indicator:ES:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | none | never checked |  |
| indicator:ES:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:ES:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:ES:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | none | never checked |  |
| indicator:ES:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | none | never checked |  |
| param:ES:population_m | param:ES:population_m | program:fetch_eurostat.py | none | never checked |  |
| param:ES:gdp_eur_bn | param:ES:gdp_eur_bn | program:fetch_eurostat.py | none | never checked |  |
| param:ES:gov_employment_k | param:ES:gov_employment_k | program:fetch_eurostat.py | none | never checked |  |
| param:ES:elec_price_eur_mwh | param:ES:elec_price_eur_mwh | program:fetch_eurostat.py | none | never checked |  |
| param:ES:renewables_pct | param:ES:renewables_pct | program:fetch_eurostat.py | none | never checked |  |
| param:ES:land_km2 | param:ES:land_km2 | program:fetch_eurostat.py | none | never checked |  |
| record:ES:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | none | never checked |  |
| record:ES:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:fingerprint_biometric:operator | Fingerprint biometric: the body that operates it | unrecorded | none | never checked |  |
| record:ES:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | none | never checked |  |
| record:ES:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:electoral_roll:operator | Electoral roll entry: the body that operates it | unrecorded | none | never checked |  |
| record:ES:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | none | never checked |  |
| record:ES:land_property:operator | Land & property registry: the body that operates it | unrecorded | none | never checked |  |
| record:ES:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | none | never checked |  |
| record:ES:police_records:register | Police information systems: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:police_records:operator | Police information systems: the body that operates it | unrecorded | none | never checked |  |
| record:ES:tax:register | Tax: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:tax:operator | Tax: the body that operates it | unrecorded | none | never checked |  |
| record:ES:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:benefits_pensions:operator | Benefits & pensions: the body that operates it | unrecorded | none | never checked |  |
| record:ES:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | none | never checked |  |
| record:ES:business_registry:register | Business registry: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:business_registry:operator | Business registry: the body that operates it | unrecorded | none | never checked |  |
| record:ES:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | none | never checked |  |
| record:ES:border_control:register | Border and visa systems: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:firearms_register:register | Firearms register: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:firearms_register:operator | Firearms register: the body that operates it | unrecorded | none | never checked |  |
| record:ES:government_payroll:register | Government payroll and personnel: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:electoral_management:register | Election management and results: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:electoral_management:operator | Election management and results: the body that operates it | unrecorded | none | never checked |  |
| record:ES:central_bank:register | Central bank systems: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | none | never checked |  |
| record:ES:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:grid_control:operator | Electricity grid control: the body that operates it | unrecorded | none | never checked |  |
| record:ES:water_control:register | Water management control: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:education:register | Education: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:education:operator | Education: the body that operates it | unrecorded | none | never checked |  |
| record:ES:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:official_gazette:operator | Official gazette and legislation: the body that operates it | unrecorded | none | never checked |  |
| record:ES:statistics_microdata:register | Statistical microdata: the name of the register or system | unrecorded | none | never checked |  |
| record:ES:statistics_microdata:operator | Statistical microdata: the body that operates it | unrecorded | none | never checked |  |
| record:ES:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | none | never checked |  |

### Withheld after the fact check: Spain

None.

---

[^s1]: Agencia Estatal Boletín Oficial del Estado — Ley 40/2015, de 1 de octubre, de Régimen Jurídico del…, 2019. Ley 40/2015, de 1 de octubre, de Régimen Jurídico del Sector Público (consolidated), artículo 46 bis. <https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566> ([archived](https://web.archive.org/web/20260924022258/https://www.boe.es/buscar/act.php?id=BOE-A-2015-10566))
[^s2]: Agencia Estatal Boletín Oficial del Estado — Ley 9/1968, de 5 de abril, sobre secretos oficiales…. Ley 9/1968, de 5 de abril, sobre secretos oficiales (texto consolidado). <https://www.boe.es/buscar/act.php?id=BOE-A-1968-444> ([archived](https://web.archive.org/web/20260908031744/https://www.boe.es/buscar/act.php?id=BOE-A-1968-444))
[^s3]: Agencia Estatal Boletín Oficial del Estado — Ley 66/1997, art. 81. Ley 66/1997, art. 81. <https://www.boe.es/buscar/act.php?id=BOE-A-1997-28053> ([archived](https://web.archive.org/web/20260823103301/https://www.boe.es/buscar/act.php?id=BOE-A-1997-28053))
[^s4]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 1114/1999, Estatuto de la entidad pública…. Real Decreto 1114/1999, Estatuto de la entidad pública empresarial Fábrica Nacional de Moneda y Timbre-Real Casa de la Moneda. <https://www.boe.es/eli/es/rd/1999/06/25/1114/con>
[^s5]: Ministerio para la Transformación Digital y de la Función Pública — Spanish Trusted Service List (TSL). Spanish Trusted Service List (TSL). <https://tsl.digital.gob.es/TSL.xml>
[^s6]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 255/2025, de 1 de abril, por el que se…, 2025-04-02. Real Decreto 255/2025, de 1 de abril, por el que se regula el Documento Nacional de Identidad. <https://www.boe.es/buscar/act.php?id=BOE-A-2025-6601> ([archived](https://web.archive.org/web/20260716095158/https://www.boe.es/buscar/act.php?id=BOE-A-2025-6601))
[^s7]: European Commission, Interoperable Europe / NIFO — Digital Public Administration Factsheet 2024 – Spain,…, 2024. Digital Public Administration Factsheet 2024 – Spain, Supporting document. <https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO_2024_Supporting%20document_Spain_vFINAL.pdf> ([archived](https://web.archive.org/web/20251013013711/https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO_2024_Supporting%20document_Spain_vFINAL.pdf))
[^s8]: Agencia Estatal Boletín Oficial del Estado (Ministerio de la Presidencia, Justicia y Relaciones con las Cortes) — Resolución de 26 de diciembre de 2024 - Convenio para la…, 2025-01-03. Resolución de 26 de diciembre de 2024 - Convenio para la prestación de la solución de Nube Híbrida NubeSARA. <https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-131> ([archived](https://web.archive.org/web/20260422231005/https://www.boe.es/diario_boe/txt.php?id=BOE-A-2025-131))
[^s9]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 1118/2024, de 5 de noviembre, por el que se…, 2024-11-06. Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital. <https://www.boe.es/buscar/act.php?id=BOE-A-2024-22929> ([archived](https://web.archive.org/web/20260420153252/https://www.boe.es/buscar/act.php?id=BOE-A-2024-22929))
[^s10]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s11]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s12]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s13]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s14]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s15]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s16]: Agencia Estatal Boletín Oficial del Estado — Ley 20/2011, de 21 de julio, del Registro Civil, 2011-07-22. Ley 20/2011, de 21 de julio, del Registro Civil. <https://www.boe.es/buscar/act.php?id=BOE-A-2011-12628> ([archived](https://web.archive.org/web/20260923020539/https://www.boe.es/buscar/act.php?id=BOE-A-2011-12628))
[^s17]: Agencia Estatal Boletín Oficial del Estado — Orden INT/1202/2011, de 4 de mayo, por la que se regulan…, 2011-05-13. Orden INT/1202/2011, de 4 de mayo, por la que se regulan los ficheros de datos de carácter personal del Ministerio del Interior. <https://www.boe.es/buscar/act.php?id=BOE-A-2011-8382> ([archived](https://web.archive.org/web/20260413120016/https://www.boe.es/buscar/act.php?id=BOE-A-2011-8382))
[^s18]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 896/2003, de 11 de julio, por el que se…, 2003-07-12. Real Decreto 896/2003, de 11 de julio, por el que se regula la expedición del pasaporte ordinario. <https://www.boe.es/buscar/act.php?id=BOE-A-2003-13978>
[^s19]: Agencia Estatal Boletín Oficial del Estado — Ley Orgánica 5/1985, de 19 de junio, del Régimen…. Ley Orgánica 5/1985, de 19 de junio, del Régimen Electoral General (consolidated), artículo veintinueve. <https://www.boe.es/buscar/act.php?id=BOE-A-1985-11672> ([archived](https://web.archive.org/web/20260921205319/https://www.boe.es/buscar/act.php?id=BOE-A-1985-11672))
[^s20]: Fábrica Nacional de Moneda y Timbre - Real Casa de la Moneda — Certificados raíz de la FNMT. Certificados raíz de la FNMT. <https://www.sede.fnmt.gob.es/descargas/certificados-raiz-de-la-fnmt> ([archived](https://web.archive.org/web/20260811165335/https://www.sede.fnmt.gob.es/descargas/certificados-raiz-de-la-fnmt))
[^s21]: Fábrica Nacional de Moneda y Timbre - Real Casa de la Moneda — Información institucional, 2025-11-11. Información institucional. <https://www.fnmt.es/institucion/informacion-institucional> ([archived](https://web.archive.org/web/20260410193006/https://www.fnmt.es/institucion/informacion-institucional))
[^s22]: Agencia Estatal Boletín Oficial del Estado — Real Decreto Legislativo 1/2004, texto refundido de la…, 2004-03-08. Real Decreto Legislativo 1/2004, texto refundido de la Ley del Catastro Inmobiliario (consolidated). <https://www.boe.es/buscar/act.php?id=BOE-A-2004-4163> ([archived](https://web.archive.org/web/20260902100910/https://www.boe.es/buscar/act.php?id=BOE-A-2004-4163))
[^s23]: Servicio Público de Justicia (Ministerio de la Presidencia, Justicia y Relaciones con las Cortes) — SIRAJ 2 - Catálogo de Servicios y Soluciones. SIRAJ 2 - Catálogo de Servicios y Soluciones. <https://www.administraciondejusticia.gob.es/-/soluciones-siraj-2> ([archived](https://web.archive.org/web/20260218102306/https://www.administraciondejusticia.gob.es/-/soluciones-siraj-2))
[^s24]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 95/2009, de 6 de febrero, Sistema de…, 2009. Real Decreto 95/2009, de 6 de febrero, Sistema de registros administrativos de apoyo a la Administración de Justicia. <https://www.boe.es/buscar/act.php?id=BOE-A-2009-2073>
[^s25]: Agencia Estatal Boletín Oficial del Estado — Orden de 28 de junio de 1995 por la que se crea el…, 1995-07-05. Orden de 28 de junio de 1995 por la que se crea el fichero automatizado Base de Datos de Señalamientos Nacionales (BDSN). <https://www.boe.es/buscar/act.php?id=BOE-A-1995-16259>
[^s26]: Agencia Estatal Boletín Oficial del Estado — Ley 58/2003, de 17 de diciembre, General Tributaria, 2003. Ley 58/2003, de 17 de diciembre, General Tributaria. <https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186> ([archived](https://web.archive.org/web/20260923155550/https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186))
[^s27]: Agencia Estatal Boletín Oficial del Estado — Orden de 2 de junio de 1994 por la que se desarrolla la…, 1994. Orden de 2 de junio de 1994 por la que se desarrolla la estructura de la Agencia Estatal de Administración Tributaria. <https://www.boe.es/buscar/act.php?id=BOE-A-1994-12973> ([archived](https://web.archive.org/web/20240625182645/https://www.boe.es/buscar/act.php?id=BOE-A-1994-12973))
[^s28]: Agencia Estatal de Administración Tributaria — Organigrama - Departamento de Informática Tributaria. Organigrama - Departamento de Informática Tributaria. <https://sede.agenciatributaria.gob.es/Sede/gobierno-abierto/transparencia/organigrama/departamento-informatica-tributaria.html> ([archived](https://web.archive.org/web/20250215200406/https://sede.agenciatributaria.gob.es/Sede/gobierno-abierto/transparencia/organigrama/departamento-informatica-tributaria.html))
[^s29]: Agencia Estatal Boletín Oficial del Estado — Real Decreto Legislativo 8/2015, texto refundido de la…. Real Decreto Legislativo 8/2015, texto refundido de la Ley General de la Seguridad Social (consolidated). <https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724> ([archived](https://web.archive.org/web/20260926075037/https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724))
[^s30]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 183/2004, de 30 de enero, por el que se…, 2004. Real Decreto 183/2004, de 30 de enero, por el que se regula la tarjeta sanitaria individual. <https://www.boe.es/buscar/act.php?id=BOE-A-2004-2591> ([archived](https://web.archive.org/web/20260514195911/https://www.boe.es/buscar/act.php?id=BOE-A-2004-2591))
[^s31]: Ministerio de Sanidad — Tarjeta Sanitaria Individual. Tarjeta Sanitaria Individual. <https://www.sanidad.gob.es/areas/saludDigital/tarjetaSanitariaSNS/home.htm> ([archived](https://web.archive.org/web/20260903035910/https://www.sanidad.gob.es/areas/saludDigital/tarjetaSanitariaSNS/home.htm))
[^s32]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 1784/1996, Reglamento del Registro…. Real Decreto 1784/1996, Reglamento del Registro Mercantil (consolidated), artículo 1. <https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533> ([archived](https://web.archive.org/web/20260924114427/https://www.boe.es/buscar/act.php?id=BOE-A-1996-17533))
[^s33]: Agencia Estatal Boletín Oficial del Estado — Real Decreto Legislativo 6/2015, texto refundido de la…, 2015. Real Decreto Legislativo 6/2015, texto refundido de la Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial. <https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722> ([archived](https://web.archive.org/web/20260927160300/https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722))
[^s34]: Dirección General de Tráfico — Sede Electrónica DGT - Informe y certificado de conductor. Sede Electrónica DGT - Informe y certificado de conductor. <https://sede.dgt.gob.es/es/permisos-de-conducir/informe-de-conductor/> ([archived](https://web.archive.org/web/20260620073449/https://sede.dgt.gob.es/es/permisos-de-conducir/informe-de-conductor/))
[^s35]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 137/1993, de 29 de enero, Reglamento de…, 2020-08-05. Real Decreto 137/1993, de 29 de enero, Reglamento de Armas (consolidated), artículo 9. <https://www.boe.es/buscar/act.php?id=BOE-A-1993-6202> ([archived](https://web.archive.org/web/20260928025859/https://www.boe.es/buscar/act.php?id=BOE-A-1993-6202))
[^s36]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 2073/1999, de 30 de diciembre, Reglamento…, 2000. Real Decreto 2073/1999, de 30 de diciembre, Reglamento del Registro Central de Personal. <https://www.boe.es/buscar/act.php?id=BOE-A-2000-1007>
[^s37]: Agencia Estatal Boletín Oficial del Estado — Anuncio de formalización de contratos: Dirección General…, 2024-03-27. Anuncio de formalización de contratos: Dirección General de Política Interior, Expediente EPE/11/2024. <https://www.boe.es/diario_boe/txt.php?id=BOE-B-2024-11865> ([archived](https://web.archive.org/web/20251201110905/https://www.boe.es/diario_boe/txt.php?id=BOE-B-2024-11865))
[^s38]: Banco de España (Portal del Cliente Bancario) — La Central de Información de Riesgos, 2018-01-03. La Central de Información de Riesgos. <https://clientebancario.bde.es/pcb/es/blog/La_Central_de_I_122c89639bbb061.html> ([archived](https://web.archive.org/web/20260508164747/https://clientebancario.bde.es/pcb/es/blog/La_Central_de_I_122c89639bbb061.html))
[^s39]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 207/2024, de 27 de febrero, estructura…, 2024. Real Decreto 207/2024, de 27 de febrero, estructura orgánica básica del Ministerio del Interior. <https://www.boe.es/buscar/act.php?id=BOE-A-2024-3793>
[^s40]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 903/1997, de 16 de junio, acceso al…, 1997. Real Decreto 903/1997, de 16 de junio, acceso al servicio de atención de llamadas de urgencia 112. <https://www.boe.es/buscar/act.php?id=BOE-A-1997-14058>
[^s41]: Agencia Estatal Boletín Oficial del Estado — Ley 17/2015, de 9 de julio, del Sistema Nacional de…. Ley 17/2015, de 9 de julio, del Sistema Nacional de Protección Civil (consolidated). <https://www.boe.es/buscar/act.php?id=BOE-A-2015-7730> ([archived](https://web.archive.org/web/20260923215549/https://www.boe.es/buscar/act.php?id=BOE-A-2015-7730))
[^s42]: Red Eléctrica de España — Centro de control eléctrico (Cecoel), 2008-10-21. Centro de control eléctrico (Cecoel). <https://www.ree.es/es/publicaciones/educacion/centro-de-control-electrico-cecoel> ([archived](https://web.archive.org/web/20251109040325/https://www.ree.es/es/publicaciones/educacion/centro-de-control-electrico-cecoel))
[^s43]: Agencia Estatal Boletín Oficial del Estado — Ley 24/2013, de 26 de diciembre, del Sector Eléctrico…. Ley 24/2013, de 26 de diciembre, del Sector Eléctrico (consolidated). <https://www.boe.es/buscar/act.php?id=BOE-A-2013-13645> ([archived](https://web.archive.org/web/20260928104552/https://www.boe.es/buscar/act.php?id=BOE-A-2013-13645))
[^s44]: Ministerio para la Transición Ecológica y el Reto Demográfico — Sistemas SAIH. Sistemas SAIH. <https://www.miteco.gob.es/es/agua/temas/evaluacion-de-los-recursos-hidricos/saih.html> ([archived](https://web.archive.org/web/20260726180059/https://www.miteco.gob.es/es/agua/temas/evaluacion-de-los-recursos-hidricos/saih.html))
[^s45]: Ministerio de Ciencia, Innovación y Universidades — Consulta al Registro Nacional de Titulados…. Consulta al Registro Nacional de Titulados Universitarios Oficiales. <https://www.ciencia.gob.es/Universidades/ConsultaTitulos.html> ([archived](https://web.archive.org/web/20260722151315/https://www.ciencia.gob.es/Universidades/ConsultaTitulos.html))
[^s46]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 1002/2010, de 5 de agosto, sobre expedición…. Real Decreto 1002/2010, de 5 de agosto, sobre expedición de títulos universitarios oficiales (consolidated). <https://www.boe.es/buscar/act.php?id=BOE-A-2010-12621>
[^s47]: Agencia Estatal Boletín Oficial del Estado — Real Decreto 181/2008, de 8 de febrero, de ordenación…, 2008. Real Decreto 181/2008, de 8 de febrero, de ordenación del diario oficial «Boletín Oficial del Estado». <https://www.boe.es/buscar/act.php?id=BOE-A-2008-2389> ([archived](https://web.archive.org/web/20260912062918/https://www.boe.es/buscar/act.php?id=BOE-A-2008-2389))
[^s48]: Agencia Estatal Boletín Oficial del Estado — Ley 7/1985, de 2 de abril, Reguladora de las Bases del…, 1985. Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local. <https://www.boe.es/buscar/act.php?id=BOE-A-1985-5392> ([archived](https://web.archive.org/web/20260923004539/https://www.boe.es/buscar/act.php?id=BOE-A-1985-5392))
[^s49]: Agencia Estatal Boletín Oficial del Estado — Ley 12/1989, de 9 de mayo, de la Función Estadística Pública, 1989. Ley 12/1989, de 9 de mayo, de la Función Estadística Pública. <https://www.boe.es/buscar/act.php?id=BOE-A-1989-10767> ([archived](https://web.archive.org/web/20260716060905/https://www.boe.es/buscar/act.php?id=BOE-A-1989-10767))
[^s50]: Agencia Estatal Boletín Oficial del Estado — Ley 14/2010, de 5 de julio, sobre las infraestructuras y…, 2010. Ley 14/2010, de 5 de julio, sobre las infraestructuras y los servicios de información geográfica en España. <https://www.boe.es/buscar/act.php?id=BOE-A-2010-10707> ([archived](https://web.archive.org/web/20260804161511/https://www.boe.es/buscar/act.php?id=BOE-A-2010-10707))

**Evidence grades:** 0 Strong, 58 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced, checked and calculated is in the two appendices above, generated from the code that produced this brief; the same text is in the country PDF and on the web pages /methodology and /fact-check.
