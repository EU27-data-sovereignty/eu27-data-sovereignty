# Belgium: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Belgium could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4] |
| State-controlled national eID | Yes[^s5][^s6] |
| Government data centres | Yes[^s7] |
| Government cloud in operation | Yes[^s8] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 33 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Belgium described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 11.96 million[^s9] |
| GDP, current prices | 642.0 EUR bn[^s10] |
| Public administration employment (NACE O) | 459.5 thousand[^s11] |
| Non-household electricity price | 186.6 EUR/MWh[^s12] |
| Renewables share of electricity | 34.3 %[^s13] |
| Land area | 30 452 km²[^s14] |

## 3. Critical data holdings, by priority

The holdings Belgium cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 20 of 39 holding classes have a verified source; 2 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Rijksregister van de natuurlijke personen (National Register of Natural Persons), the central database of identification data of all registered persons[^s15][^s6] | The National Register is managed by the Directorate-General Identity and Civil Affairs of the FPS Interior[^s6][^s16] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | ID-card photos are stored and visible in the National Register[^s17][^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s17][^s5] | — | — | — |
| Critical | Breeder document scans (tier 0) | DABS: a central database holding all civil status deeds, replacing the municipal and consular registers[^s19][^s20] | DABS is governed by a DABS Management Committee responsible for its set-up and management[^s19][^s20] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | FAS audit trail of authentication logs, kept for 10 years[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Register van de Identiteitskaarten: a permanent inventory of the identity cards produced and issued in Belgium[^s22][^s6] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Federal Authentication Service (FAS)[^s21] | DG Simplification and Digitization (FPS Policy and Support, BOSA)[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | Belgium Root CA (BRCA), the top of the government CA hierarchy[^s3][^s4] | The Belgian authorities are the certification service provider responsible for the Belgium Root CAs[^s3][^s4] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | kadastrale documentatie of the AAPD (cadastral documentation of the General Administration of Patrimonial Documentation)[^s23] | Algemene Administratie van de Patrimoniumdocumentatie (AAPD) (General Administration of Patrimonial Documentation)[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Centraal Strafregister (Central Criminal Register)[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | Evibel is the internal database of the immigration service, to be replaced by eMigration[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | Pensioenkadaster (Pension Register)[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | Kruispuntbank van Ondernemingen (Crossroads Bank for Enterprises)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | UBO-register (register of ultimate beneficial owners)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Kruispuntbank van de Voertuigen (Crossroads Bank for Vehicles)[^s29] | Directie voor de Inschrijving van Voertuigen van de Federale Overheidsdienst Mobiliteit en Vervoer (DIV, Vehicle Registration Directorate of FPS Mobility and Transport)[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | Centraal Wapenregister (Central Weapons Register)[^s30] | een dienst van de Federale Politie (a service of the Federal Police)[^s30] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | NBB Securities Settlement System (NBB-SSS)[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | ASTRID-radionetwerk (ASTRID TETRA radio network)[^s32] | ASTRID (naamloze vennootschap van publiek recht, public-law company)[^s33] | *Not stated in sources* | more than 2 million radio contacts per day[^s32] |
| High | Crisis management and civil protection (tier 1) | BE-Alert (the government's alerting system)[^s34] | *Not yet sourced* | *Not stated in sources* | more than 1 million registered addresses[^s34] |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | LED, de Leer- en ErvaringsbewijzenDatabank (Learning and Experience Certificates Database)[^s35] | Agentschap voor Kwaliteitszorg in Onderwijs en Vorming (Agency for Quality Assurance in Education and Training)[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 19 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 19 |

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

> Not yet sized. Capacity for Belgium will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 2 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Belgium without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Electoral roll entry (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Statutory health insurance (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

## Appendix: fact check

### What was checked, and by whom

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. The check below is made by a second model, not by a person.

Every printed fact is put, exactly as printed, to a checker that is a different model from the one that wrote it. The checker fetches the cited source and decides whether it supports the statement as printed: the same value, name, unit, date, country and scope. A production deploy is refused unless every printed fact has a current verdict of supported from an eligible checker.

In this build, 0 of 1390 printed facts pass.

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
- Before every production deploy, factcheck.py gate requires a current supported verdict from an eligible checker for every printed fact, and this file to be current. A disagreement blocks the deploy until the fact or its source is fixed and checked again; nothing is changed automatically.

A verdict holds for one fact exactly as printed: a SHA-256 of the claim, the question it answers, the printed text and every citation behind it. If any of these changes, the verdict lapses and the fact must be checked again before the next deploy.

### Fact-check runs

No fact-check run has been recorded yet, so no printed fact has been checked.

### The verdict on each fact about Belgium

0 of 42 printed facts about Belgium pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:BE:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | none | never checked |  |
| indicator:BE:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:BE:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:BE:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | none | never checked |  |
| indicator:BE:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | none | never checked |  |
| param:BE:population_m | param:BE:population_m | program:fetch_eurostat.py | none | never checked |  |
| param:BE:gdp_eur_bn | param:BE:gdp_eur_bn | program:fetch_eurostat.py | none | never checked |  |
| param:BE:gov_employment_k | param:BE:gov_employment_k | program:fetch_eurostat.py | none | never checked |  |
| param:BE:elec_price_eur_mwh | param:BE:elec_price_eur_mwh | program:fetch_eurostat.py | none | never checked |  |
| param:BE:renewables_pct | param:BE:renewables_pct | program:fetch_eurostat.py | none | never checked |  |
| param:BE:land_km2 | param:BE:land_km2 | program:fetch_eurostat.py | none | never checked |  |
| record:BE:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | none | never checked |  |
| record:BE:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:breeder_documents:operator | Breeder document scans: the body that operates it | unrecorded | none | never checked |  |
| record:BE:authentication_audit_log:register | Authentication audit log: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:issuance_history:register | Document issuance history: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | none | never checked |  |
| record:BE:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | none | never checked |  |
| record:BE:land_property:register | Land & property registry: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:land_property:operator | Land & property registry: the body that operates it | unrecorded | none | never checked |  |
| record:BE:judicial_criminal:register | Judicial & criminal justice: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:benefits_pensions:register | Benefits & pensions: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:business_registry:register | Business registry: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | none | never checked |  |
| record:BE:firearms_register:register | Firearms register: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:firearms_register:operator | Firearms register: the body that operates it | unrecorded | none | never checked |  |
| record:BE:central_bank:register | Central bank systems: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:emergency_communications:operator | Emergency calls and public-safety radio: the body that operates it | unrecorded | none | never checked |  |
| record:BE:emergency_communications:count | Emergency calls and public-safety radio: how many records it holds | unrecorded | none | never checked |  |
| record:BE:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:crisis_management:count | Crisis management and civil protection: how many records it holds | unrecorded | none | never checked |  |
| record:BE:education:register | Education: the name of the register or system | unrecorded | none | never checked |  |
| record:BE:education:operator | Education: the body that operates it | unrecorded | none | never checked |  |

---

[^s1]: Moniteur belge (copy on etaamb.openjustice.be); numac 1999007004 — Loi du 11 décembre 1998 relative à la classification et…, 1999-05-07. Loi du 11 décembre 1998 relative à la classification et aux habilitations de sécurité. <https://etaamb.openjustice.be/fr/loi-du-11-decembre-1998_n1999007004.html>
[^s2]: Agence fédérale de contrôle nucléaire (FANC), Jurion regulatory database — Loi du 11 décembre 1998 relative à la classification,…. Loi du 11 décembre 1998 relative à la classification, aux habilitations de sécurité, aux avis de sécurité et au service public réglementé; Chapitre II. <https://www.jurion.fanc.fgov.be/jurdb-consult/plainWettekstServlet?wettekstId=1384&lang=fr>
[^s3]: eID Repository (Belgian State / certipost) — Belgian Certificate Policy & Practice Statement for eID…, 2024-09-03. Belgian Certificate Policy & Practice Statement for eID PKI infrastructure, Citizen CA, v5.0. <https://repository.eid.belgium.be/downloads/citizen/en/CPS_CitizenCA_BRCA34.pdf> ([archived](https://web.archive.org/web/20240228070218/http://repository.eid.belgium.be/downloads/citizen/en/CPS_CitizenCA_BRCA34.pdf))
[^s4]: Belgian eID PKI repository — Citizen CA Certification Practice Statement (v1.4). Citizen CA Certification Practice Statement (v1.4). <https://repository.eid.belgium.be/downloads/citizen/en/CPS_CitizenCA.pdf>
[^s5]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — eID | IBZ - FOD Binnenlandse Zaken. eID | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid> ([archived](https://web.archive.org/web/20260617223429/https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid))
[^s6]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — Wie beheert het Rijksregister van de natuurlijke personen?. Wie beheert het Rijksregister van de natuurlijke personen?. <https://www.ibz.rrn.fgov.be/nl/faq/wat-is-het-rijksregister-van-de-natuurlijke-personen/wie-beheert-het-rijksregister-van-de>
[^s7]: G-Cloud (Belgian federal government community cloud) — Housing – Datacenter-as-a-Service (G-Cloud). Housing – Datacenter-as-a-Service (G-Cloud). <https://www.gcloud.belgium.be/nl/service/detail/housing>
[^s8]: G-Cloud (Belgian federal government community cloud) — G-Cloud, de community cloud van de overheid. G-Cloud, de community cloud van de overheid. <https://www.gcloud.belgium.be/nl> ([archived](https://web.archive.org/web/20260720192938/https://www.gcloud.belgium.be/nl))
[^s9]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s10]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s11]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s12]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s13]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s14]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s15]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — Rijksregister | IBZ - FOD Binnenlandse Zaken. Rijksregister | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/rijksregister-en-bevolking/rijksregister> ([archived](https://web.archive.org/web/20260911221802/https://www.ibz.rrn.fgov.be/nl/burger/rijksregister-en-bevolking/rijksregister))
[^s16]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — Home | IBZ - FOD Binnenlandse Zaken. Home | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl>
[^s17]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — eID en GDPR, 2020-11-25. eID en GDPR. <https://www.ibz.rrn.fgov.be/sites/default/files/documents/nl/identiteitsdocumenten/eid/eID_en_GDPR.pdf>
[^s18]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — eID en GDPR | IBZ - FOD Binnenlandse Zaken. eID en GDPR | IBZ - FOD Binnenlandse Zaken. <https://www.ibz.rrn.fgov.be/nl/burger/identiteitsdocumenten/eid/eid-en-gdpr>
[^s19]: Rijksarchief in België — Het Rijksarchief is vertegenwoordigd in het…, 2023-06-14. Het Rijksarchief is vertegenwoordigd in het beheerscomité van de Databank voor Akten van de Burgerlijke Stand. <https://www.arch.be/index.php?l=nl&m=nieuws&r=alle-nieuwsberichten&a=2023-06-14-het-rijksarchief-is-vertegenwoordigd-in-het-beheerscomite-van-de-databank-voor-akten-van-de-burgerlijke-stand> ([archived](https://web.archive.org/web/20260416001407/https://www.arch.be/index.php?l=nl&m=nieuws&r=alle-nieuwsberichten&a=2023-06-14-het-rijksarchief-is-vertegenwoordigd-in-het-beheerscomite-van-de-databank-voor-akten-van-de-burgerlijke-stand))
[^s20]: FOD Binnenlandse Zaken, Algemene Directie Identiteit en Burgerzaken — FAQ DABS (NL) Versie 01/07/2020, 2020-07-01. FAQ DABS (NL) Versie 01/07/2020. <https://www.ibz.rrn.fgov.be/sites/default/files/documents/nl/dabs/FAQ_DABS_NL_20200701.pdf>
[^s21]: FPS Policy and Support (BOSA), DG Simplification and Digitization — FAS Privacy Notice – FAS – My Digital Keys – version 1.3, 2025-08-05. FAS Privacy Notice – FAS – My Digital Keys – version 1.3. <https://sma-help.bosa.belgium.be/en/fas-privacy> ([archived](https://web.archive.org/web/20260928063339/https://sma-help.bosa.belgium.be/en/fas-privacy))
[^s22]: Belgisch Staatsblad (copy published by etaamb.openjustice.be) — Koninklijk Besluit van 25/05/2005 tot bepaling van de…, 2005-05-25. Koninklijk Besluit van 25/05/2005 tot bepaling van de personen en instellingen die toegang hebben tot het register van de identiteitskaarten. <https://etaamb.openjustice.be/nl/koninklijk-besluit-van-25-mei-2005_n2005000390.html>
[^s23]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies 29/2018 van 21 maart 2018 (kadastrale documentatie), 2018-03-21. Advies 29/2018 van 21 maart 2018 (kadastrale documentatie). <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-29-2018.pdf> ([archived](https://web.archive.org/web/20240921144846/https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-29-2018.pdf))
[^s24]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies nr. 73/2026 van 15 april 2026, 2026-04-15. Advies nr. 73/2026 van 15 april 2026. <https://gegevensbeschermingsautoriteit.be/publications/advies-nr.-73-2026.pdf>
[^s25]: Gegevensbeschermingsautoriteit — Advies nr. 121/2022 van 1 juli 2022, 2022-07-01. Advies nr. 121/2022 van 1 juli 2022. <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-121-2022.pdf> ([archived](https://web.archive.org/web/20220706131107/https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-121-2022.pdf))
[^s26]: Kruispuntbank van de Sociale Zekerheid (KSZ) — Datawarehouse | DWH_ONP_SFP_CADASTRE. Datawarehouse | DWH_ONP_SFP_CADASTRE. <https://dwh.ksz-bcss.fgov.be/nl/sourcedetail/dwh-onp-sfp-cadastre.html>
[^s27]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies nr. 03/2023 van 20 januari 2023, 2023-01-20. Advies nr. 03/2023 van 20 januari 2023. <https://gegevensbeschermingsautoriteit.be/publications/advies-nr.-03-2023.pdf>
[^s28]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies nr. 81/2022 van 25 april 2022…, 2022-04-25. Advies nr. 81/2022 van 25 april 2022 (werkingsmodaliteiten UBO-register). <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-81-2022.pdf>
[^s29]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Geschillenkamer Beslissing ten gronde 56/2026 van 12…, 2026-03-12. Geschillenkamer Beslissing ten gronde 56/2026 van 12 maart 2026. <https://www.gegevensbeschermingsautoriteit.be/publications/beslissing-ten-gronde-nr.-56-2026.pdf> ([archived](https://web.archive.org/web/20260603114950/https://www.gegevensbeschermingsautoriteit.be/publications/beslissing-ten-gronde-nr.-56-2026.pdf))
[^s30]: Gegevensbeschermingsautoriteit (Belgian Data Protection Authority) — Advies nr 169/2019 van 8 november 2019, 2019-11-08. Advies nr 169/2019 van 8 november 2019. <https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-169-2019.pdf> ([archived](https://web.archive.org/web/20251008074530/https://www.gegevensbeschermingsautoriteit.be/publications/advies-nr.-169-2019.pdf))
[^s31]: Nationale Bank van België — Het Securities Settlement System (NBB-SSS). Het Securities Settlement System (NBB-SSS). <https://www.nbb.be/nl/betalingen-en-effecten/het-securities-settlement-system-nbb-sss>
[^s32]: ASTRID nv van publiek recht — Radiocommunicatie | ASTRID. Radiocommunicatie | ASTRID. <https://www.astrid.be/nl/diensten/radiocommunicatie> ([archived](https://web.archive.org/web/20250403085231/https://www.astrid.be/nl/diensten/radiocommunicatie))
[^s33]: ASTRID nv van publiek recht — Organisatie | ASTRID. Organisatie | ASTRID. <https://www.astrid.be/nl/over-astrid/organisatie> ([archived](https://web.archive.org/web/20230131192154/https://www.astrid.be/nl/over-astrid/organisatie))
[^s34]: Nationaal Crisiscentrum (NCCN) — Meer dan 1 miljoen geregistreerde adressen in BE-Alert, 2022. Meer dan 1 miljoen geregistreerde adressen in BE-Alert. <https://crisiscentrum.be/nl/newsroom/meer-dan-1-miljoen-geregistreerde-adressen-be-alert>
[^s35]: Kruispuntbank van de Sociale Zekerheid (KSZ) — Datawarehouse | DWH_AHOVOKS_LED. Datawarehouse | DWH_AHOVOKS_LED. <https://dwh.ksz-bcss.fgov.be/nl/sourcedetail/dwh-ahovoks-led> ([archived](https://web.archive.org/web/20260211053943/https://dwh.ksz-bcss.fgov.be/nl/sourcedetail/dwh-ahovoks-led))

**Evidence grades:** 6 Strong, 36 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
