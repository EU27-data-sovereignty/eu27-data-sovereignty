# Bulgaria: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Bulgaria could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | *Not yet sourced* |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s1][^s2] |
| State-controlled national eID | Partly[^s1][^s3] |
| Government data centres | Yes[^s4] |
| Government cloud in operation | *Not yet sourced* |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 32 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Bulgaria described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 6.42 million[^s5] |
| GDP, current prices | 116.0 EUR bn[^s6] |
| Public administration employment (NACE O) | 217.8 thousand[^s7] |
| Non-household electricity price | 141.3 EUR/MWh[^s8] |
| Renewables share of electricity | 34.4 %[^s9] |
| Land area | 110 001 km²[^s10] |

## 3. Critical data holdings, by priority

The holdings Bulgaria cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 31 of 39 holding classes have a verified source; 2 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | Identity documents are issued by the Ministry of Interior, Ministry of Foreign Affairs, Ministry of Transport and Communications and Ministry of Defence[^s11] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | National Register of Bulgarian Identity Documents (automated information fund)[^s11] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Document issuance history (tier 0) | *Not yet sourced* | From 27 April 2026 the Ministry of Interior moved to centralised personalisation and a new generation of identity documents[^s12] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet sourced* | Access to the register is granted to persons designated by order of the Minister of Interior (MVR runs the register)[^s13] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | избирателните списъци, отпечатвани от ГД ГРАО (voter lists printed by DG Civil Registration and Administrative Services)[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | The Communications Regulation Commission creates, maintains and publishes the national Trusted List[^s1] | Qualified trust service providers on the Bulgarian Trusted List: Borica AD, Evrotrust Technologies AD, InfoNotary EAD, Information Services AD and Idocs Bulgaria EOOD[^s1] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet sourced* | Criminal-record bureaus at every district court and a Central Criminal Records Bureau at the Ministry of Justice[^s15] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Автоматизираната информационна система "Издирвателна дейност" - Национална Шенгенска информационна система (АИС ИД - НШИС) (Automated Information System 'Search Activity' – National Schengen Information System)[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | *Not yet sourced* | Migration Directorate of MVR and Migration units of the regional MVR directorates (Foreigners in the Republic of Bulgaria Act)[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Tax and Social Security Procedure Code: NRA creates and maintains the register and databases of obliged persons[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | The new Customs Import Information System (MISV) went into production on 26.11.2018[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | AGCC creates and maintains the cadastral map and cadastral registers for the whole country under the Cadastre and Property Register Act[^s20] | The Registry Agency (executive agency under the Minister of Justice) keeps the property register, commercial register, BULSTAT and other registers[^s21] | National infrastructure[^s21] | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | The software change enabling beneficial-owner entries went live on 28.01.2019[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | автоматизираната информационна система КАТ (АИС – КАТ) (Automated Information System KAT, the vehicle registration system)[^s16] | "Пътна полиция" при СДВР/ОДМВР (Traffic Police units of the Ministry of Interior's regional directorates)[^s16] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Национална Шенгенска информационна система (АИС ИД - НШИС) (National Schengen Information System)[^s22][^s16] | Министерството на външните работи (Ministry of Foreign Affairs), for the national visa system[^s22] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | SEBRA (System for Electronic Budget Payments) is used to initiate payments of budget organisations[^s23] | BORICA AD transforms approved SEBRA payments into ISO 20022 XML[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | TARGET-BNB (national system component of the Eurosystem's TARGET)[^s24] | Българската народна банка (Bulgarian National Bank)[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Националната система 112 (National System 112)[^s25] | *Not yet sourced* | *Not stated in sources* | шест центъра (six emergency call centres)[^s25] |
| High | Crisis management and civil protection (tier 1) | BG-ALERT public warning system over mobile networks (Cell Broadcast)[^s26][^s27] | Developed jointly by MVR and the Ministry of e-Government[^s26][^s27] | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Project to modernise and extend the SCADA/EMS and information environment in ESO's Central Dispatch (CDU)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Register of all current, interrupted and graduated students and doctoral candidates, kept as an electronic database through NACID[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | The NHIS holds an electronic health record for every citizen[^s30][^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Business registry (tier 1) | The Commercial Register and Register of Non-Profit Legal Entities is a common electronic database[^s21] | *Not yet sourced* | National infrastructure[^s21] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The State Gazette website provides the full content of all issues for the last 7 years in PDF (EU N-Lex description)[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | 2021 Population and Housing Census, the 18th in Bulgaria (census site of the National Statistical Institute)[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | AGCC creates and maintains the topographic databases and the geo-information system[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 31 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 29 |

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

> Not yet sized. Capacity for Bulgaria will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 2 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Bulgaria without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Civil registry core (tier 0)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
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

### The verdict on each fact about Bulgaria

0 of 45 printed facts about Bulgaria pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:BG:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:BG:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:BG:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | none | never checked |  |
| param:BG:population_m | param:BG:population_m | program:fetch_eurostat.py | none | never checked |  |
| param:BG:gdp_eur_bn | param:BG:gdp_eur_bn | program:fetch_eurostat.py | none | never checked |  |
| param:BG:gov_employment_k | param:BG:gov_employment_k | program:fetch_eurostat.py | none | never checked |  |
| param:BG:elec_price_eur_mwh | param:BG:elec_price_eur_mwh | program:fetch_eurostat.py | none | never checked |  |
| param:BG:renewables_pct | param:BG:renewables_pct | program:fetch_eurostat.py | none | never checked |  |
| param:BG:land_km2 | param:BG:land_km2 | program:fetch_eurostat.py | none | never checked |  |
| record:BG:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | none | never checked |  |
| record:BG:fingerprint_biometric:register | Fingerprint biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:issuance_history:operator | Document issuance history: the body that operates it | unrecorded | none | never checked |  |
| record:BG:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | none | never checked |  |
| record:BG:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | none | never checked |  |
| record:BG:judicial_criminal:operator | Judicial & criminal justice: the body that operates it | unrecorded | none | never checked |  |
| record:BG:police_records:register | Police information systems: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | none | never checked |  |
| record:BG:tax:register | Tax: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:customs:register | Customs declarations: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:land_property:register | Land & property registry: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:land_property:operator | Land & property registry: the body that operates it | unrecorded | none | never checked |  |
| record:BG:land_property:foreign_dependency | Land & property registry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | none | never checked |  |
| record:BG:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:vehicle_licensing:operator | Vehicle & licensing: the body that operates it | unrecorded | none | never checked |  |
| record:BG:border_control:register | Border and visa systems: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:border_control:operator | Border and visa systems: the body that operates it | unrecorded | none | never checked |  |
| record:BG:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | none | never checked |  |
| record:BG:central_bank:register | Central bank systems: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:central_bank:operator | Central bank systems: the body that operates it | unrecorded | none | never checked |  |
| record:BG:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:emergency_communications:count | Emergency calls and public-safety radio: how many records it holds | unrecorded | none | never checked |  |
| record:BG:crisis_management:register | Crisis management and civil protection: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:crisis_management:operator | Crisis management and civil protection: the body that operates it | unrecorded | none | never checked |  |
| record:BG:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:education:register | Education: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:health_records:register | Health records: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:business_registry:register | Business registry: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:business_registry:foreign_dependency | Business registry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | none | never checked |  |
| record:BG:official_gazette:register | Official gazette and legislation: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:statistics_microdata:register | Statistical microdata: the name of the register or system | unrecorded | none | never checked |  |
| record:BG:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | none | never checked |  |

---

[^s1]: Комисия за регулиране на съобщенията — Електронни удостоверителни услуги. Електронни удостоверителни услуги. <https://crc.bg/bg/rubriki/560/elektronni-udostoveritelni-uslugi>
[^s2]: Информационно обслужване АД — Информационно обслужване АД – Доклад за дейността 2024…, 2025. Информационно обслужване АД – Доклад за дейността 2024 (Annual activity report 2024). <https://www.is-bg.net/upload/4944/IS_2024_%D0%94%D0%BE%D0%BA%D0%BB%D0%B0%D0%B4%20%D0%B7%D0%B0%20%D0%B4%D0%B5%D0%B9%D0%BD%D0%BE%D1%81%D1%82%D1%82%D0%B0.pdf>
[^s3]: Вестник „Сега“ — Отпада едно от безумията за личните карти с чип, 2026-09-19. Отпада едно от безумията за личните карти с чип. <https://www.segabg.com/hot/category-consult/otpada-edno-bezumiyata-za-lichnite-karti-chip> ([archived](https://web.archive.org/web/20260925122111/https://www.segabg.com/hot/category-consult/otpada-edno-bezumiyata-za-lichnite-karti-chip))
[^s4]: Информационно обслужване АД — Инфраструктура. Инфраструктура. <https://www.is-bg.net/bg/solutions/infrastructure>
[^s5]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s6]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s7]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s8]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s9]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s10]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s11]: Държавна агенция за бежанците (копие на закона) — Закон за българските лични документи (консолидиран текст), 2024. Закон за българските лични документи (консолидиран текст). <https://aref.government.bg/sites/default/files/2024-04/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B1%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D1%82%D0%B5%20%D0%BB%D0%B8%D1%87%D0%BD%D0%B8%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B8.pdf> ([archived](https://web.archive.org/web/20260315085009/https://aref.government.bg/sites/default/files/2024-04/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B1%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D1%82%D0%B5%20%D0%BB%D0%B8%D1%87%D0%BD%D0%B8%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B8.pdf))
[^s12]: Министерство на вътрешните работи – ОДМВР София — Въвеждане на ново поколение български лични документи, 2026-04-27. Въвеждане на ново поколение български лични документи. <https://mvr.bg/sofia/%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D0%BD-%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BF%D1%80%D0%B5%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/90242> ([archived](https://web.archive.org/web/20260427064743/https://mvr.bg/sofia/%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D0%BD-%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BF%D1%80%D0%B5%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/90242))
[^s13]: Министерство на транспорта и съобщенията (копие на правилника) — Правилник за прилагане на Закона за електронната…, 2017. Правилник за прилагане на Закона за електронната идентификация. <https://www.mtc.government.bg/sites/default/files/pravilnik_za_prilagane_na_zakona_za_elektronnata_identifikaciq.pdf> ([archived](https://web.archive.org/web/20240719053301/https://www.mtc.government.bg/sites/default/files/pravilnik_za_prilagane_na_zakona_za_elektronnata_identifikaciq.pdf))
[^s14]: Централна избирателна комисия — Централна избирателна комисия, Протокол № 821 от 14.05.2026, 2026-05-14. Централна избирателна комисия, Протокол № 821 от 14.05.2026. <https://www.cik.bg/upload/280009/%E2%84%96+821-14052026-bld.pdf> ([archived](https://web.archive.org/web/20260519104206/https://www.cik.bg/upload/280009/%E2%84%96+821-14052026-bld.pdf))
[^s15]: Комисия за финансов надзор (копие на наредбата, актуално към 01.01.2022) — Наредба № 8 от 26.02.2008 г. за функциите и…, 2022. Наредба № 8 от 26.02.2008 г. за функциите и организацията на дейността на бюрата за съдимост. <https://www.fsc.bg/wp-content/uploads/2021/files/31563_file.pdf> ([archived](https://web.archive.org/web/20240909150602/https://www.fsc.bg/wp-content/uploads/2021/files/31563_file.pdf))
[^s16]: Изпълнителна агенция „Автомобилна администрация“ — Наредба № I-45 от 24.03.2000 г. за регистриране, отчет…, 2023-11. Наредба № I-45 от 24.03.2000 г. за регистриране, отчет ... на моторните превозни средства. <https://www.rta.government.bg/upload/11661/n-I45.pdf>
[^s17]: Министерство на външните работи (копие на закона) — Закон за чужденците в Република България. Закон за чужденците в Република България. <https://www.mfa.bg/upload/138160/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D1%87%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D1%82%D0%B5%20%D0%B2%20%D0%A0%D0%B5%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%20%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D0%B8%D1%8F.pdf>
[^s18]: Министерство на вътрешните работи (копие на кодекса) — Данъчно-осигурителен процесуален кодекс. Данъчно-осигурителен процесуален кодекс. <https://www.mvr.bg/upload/296043/%D0%94%D0%9E%D0%9F%D0%9A.pdf>
[^s19]: Българска търговско-промишлена палата – Инфобизнес — Въвеждане в реална експлоатация на нова Митническа…, 2018-11-26. Въвеждане в реална експлоатация на нова Митническа информационна система за внасяне (МИСВ) на Агенция „Митници“. <https://www.infobusiness.bcci.bg/customs-26-11-18.html>
[^s20]: Агенция по геодезия, картография и кадастър — Функции на АГКК. Функции на АГКК. <https://www.cadastre.bg/funkcii-na-agkk>
[^s21]: Сметна палата на Република България — Одитен доклад № 0300101019 – Ефективност на…, 2021-08-05. Одитен доклад № 0300101019 – Ефективност на организацията и контрола на дейностите по водене и съхраняване на поддържаните от Агенцията по вписванията регистри. <https://www.bulnao.government.bg/media/documents/OD_AV_230821.pdf> ([archived](https://web.archive.org/web/20250714123738/https://www.bulnao.government.bg/media/documents/OD_AV_230821.pdf))
[^s22]: Министерство на външните работи — Въвеждане в експлоатация на нова версия на Национална…, 2024-08-02. Въвеждане в експлоатация на нова версия на Национална визова информационна система. <https://www.mfa.bg/bg/news/41822> ([archived](https://web.archive.org/web/20260412085753/https://www.mfa.bg/bg/news/41822))
[^s23]: Министерство на финансите – дирекция „Държавно съкровище“ (публикувано от БНБ) — ДДС № 03/03.05.2023 г. – Изисквания за структурата,…, 2023-05-03. ДДС № 03/03.05.2023 г. – Изисквания за структурата, формата и съдържанието на платежни документи ... чрез СЕБРА. <https://www.bnb.bg/bnbweb/groups/public/documents/bnb_law/instructions_bnb_51681_bg.pdf> ([archived](https://web.archive.org/web/20250527084951/https://www.bnb.bg/bnbweb/groups/public/documents/bnb_law/instructions_bnb_51681_bg.pdf))
[^s24]: Българска народна банка — Платежни и сетълмент системи. Платежни и сетълмент системи. <https://www.bnb.bg/PaymentSystem/index.htm>
[^s25]: Министерство на вътрешните работи, дирекция „Национална система 112“ — 112 в България. 112 в България. <https://www.mvr.bg/112/%D0%B4%D0%B5%D0%B9%D0%BD%D0%BE%D1%81%D1%82%D0%B8/%D0%B4%D0%B5%D0%B9%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%B8-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8/112_v_bg>
[^s26]: Министерство на вътрешните работи — Мотиви към проект на наредба за реда за изграждане,…. Мотиви към проект на наредба за реда за изграждане, поддържане, развитие и използване на системата BG-ALERT. <https://www.mvr.bg/upload/8121/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B8_%D0%BD%D0%B0%D1%80%D0%B5%D0%B4%D0%B1%D0%B0_bg-alert.pdf> ([archived](https://web.archive.org/web/20251211103031/https://www.mvr.bg/upload/8121/%D0%BC%D0%BE%D1%82%D0%B8%D0%B2%D0%B8_%D0%BD%D0%B0%D1%80%D0%B5%D0%B4%D0%B1%D0%B0_bg-alert.pdf))
[^s27]: Вестник „Сега“ — МВР ще издирва бандити чрез BG-ALERT, 2026-01-07. МВР ще издирва бандити чрез BG-ALERT. <https://www.segabg.com/hot/category-bulgaria/mvr-shte-izdirva-banditi-chrez-bg-alert> ([archived](https://web.archive.org/web/20260122112807/https://www.segabg.com/hot/category-bulgaria/mvr-shte-izdirva-banditi-chrez-bg-alert))
[^s28]: Електроенергиен системен оператор ЕАД — Модернизация и Разширение на Системата SCADA/EMS и…, 2016-01-20. Модернизация и Разширение на Системата SCADA/EMS и Информационната среда в ЦДУ на ЕСО – предварително обявление. <https://www.eso.bg/fileObj.php?oid=131>
[^s29]: НАЦИД — Регистър на студенти и докторанти. Регистър на студенти и докторанти. <https://nacid.bg/bg/register_rdpzsd/>
[^s30]: Министерство на здравеопазването — Национална здравноинформационна система :: НЗИС, 2026-08-31. Национална здравноинформационна система :: НЗИС. <https://www.his.bg/>
[^s31]: Национална здравноосигурителна каса (копие на закона) — Закон за здравето. Закон за здравето. <https://www.nhif.bg/upload/30458/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%B5%D1%82%D0%BE.pdf>
[^s32]: Европейска комисия / Службата за публикации на ЕС (N-Lex) — За националната база данни – България. За националната база данни – България. <https://n-lex.europa.eu/n-lex/info/info-bg/index?lang=bg> ([archived](https://web.archive.org/web/20250629165146/https://n-lex.europa.eu/n-lex/info/info-bg/index?lang=bg))
[^s33]: Национален статистически институт — Преброяване 2021. Преброяване 2021. <https://census2021.bg/> ([archived](https://web.archive.org/web/20260717163802/https://census2021.bg/))

**Evidence grades:** 4 Strong, 41 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
