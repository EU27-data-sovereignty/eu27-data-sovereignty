# Ireland: critical data holdings and sovereign hosting

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

> Dependent on non-EU providers. Confidence: High. With the evidence still open, Ireland could be anywhere from 'Dependent on non-EU providers' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Partly[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2] |
| State-controlled national eID | Yes[^s3] |
| Government data centres | Yes[^s4][^s1][^s5] |
| Government cloud in operation | Yes[^s5][^s6] |

What could move this placement:

Nothing: every input the rule reads is settled by a source.

## 2. Fundamentals

Ireland described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 5.51 million[^s7] |
| GDP, current prices | 602.4 EUR bn[^s8] |
| Public administration employment (NACE O) | 150.8 thousand[^s9] |
| Non-household electricity price | 255.2 EUR/MWh[^s10] |
| Renewables share of electricity | 41.7 %[^s11] |
| Land area | 68 655 km²[^s12] |

## 3. Critical data holdings, by priority

The holdings Ireland cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 9 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | register of births (with registers of stillbirths, deaths, marriages etc.)[^s13] | an tArd-Chláraitheoir (Registrar General)[^s13] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | SAFE 2 registration biometric facial templates (Public Services Card)[^s14] | Department of Social Protection (DSP)[^s14] | *Not stated in sources* | Facial templates for 70% of the State's population (2021)[^s14] |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | foreign births register[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Electoral roll entry (tier 0) | *Not yet sourced* | *Not yet sourced* | Non-EU provider[^s16] | 3.87 million registered electors (December 2024)[^s16] |
| High | Document issuance history (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | MyGovID[^s3] | *Not yet sourced* | *Not stated in sources* | over 3.2 million people actively using their MyGovID account[^s3] |
| High | State PKI and qualified trust services (tier 0) | ROS digital certificate PKI (Revenue CA), also used by CRO, Department of Transport and Department of Social Protection[^s2] | Revenue Commissioners act as Certification Authority for ROS digital certificates[^s2] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | National Land Register (folios of the Land Registry) and Registry of Deeds[^s17][^s18] | Tailte Éireann (civil service body under the Tailte Éireann Act 2022)[^s17] | *Not stated in sources* | 2.4 million folios with associated spatial data accessible via landdirect.ie[^s17][^s18] |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | PULSE (An Garda Síochána's national incident and intelligence database)[^s19] | An Garda Síochána[^s19] | *Not stated in sources* | *Not yet measured* |
| High | Intelligence services (tier 1) | Defence Forces Military Intelligence holdings[^s20] | National Security Analysis Centre (established by Government in 2019)[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | National Digital Radio Service (NDRS), TETRA network for first responders[^s21] | *Not yet sourced* | Non-EU provider[^s21] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Irish Residence Permission (IRP) register: the register of non-nationals with permission to be in the State[^s22] | Immigration Service Delivery (ISD), Department of Justice (took over first-time registration from the Garda National Immigration Bureau, 13 January 2025)[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | ROS database[^s4] | Revenue[^s4] | *Not stated in sources* | over 900,000 self-assessed taxpayers, 287,000 companies and 293,000 VAT traders registered[^s4] |
| High | Customs declarations (tier 1) | Automated Import System (AIS), Automated Export System (AES) and New Computerised Transit System (NCTS)[^s4] | Revenue Commissioners[^s4] | *Not stated in sources* | *Not yet sourced* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | PCRS eligibility records (medical card / GMS scheme eligibility, keyed on PPSN)[^s24] | HSE Primary Care Reimbursement Service (PCRS)[^s24] | *Not stated in sources* | 1,552,553 GMS (medical card) eligible persons and 785,152 GP visit card holders in 2025[^s25] |
| High | Business registry (tier 1) | Register of companies, business names and limited partnerships held by the Companies Registration Office[^s26] | Companies Registration Office (CRO), an office of the Department of Enterprise, Tourism and Employment[^s26] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Central Register of Beneficial Ownership of Companies and Industrial and Provident Societies[^s27] | Registrar of Beneficial Ownership of Companies and Industrial and Provident Societies[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | National Vehicle and Driver File (NVDF)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | National connection to the Schengen Information System (SIS), live in Ireland since 15 March 2021[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Firearm certificates (three-year certificates, renewal phases administered by An Garda Síochána)[^s30] | An Garda Síochána (applications decided by the local Superintendent)[^s30] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Financial Management Shared Services (FMSS) system, the shared government financial management system (incl. the Exchequer)[^s31] | National Shared Services Office (FMSS); Department of Finance manages the Exchequer[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | Election Count Database System (Ecount), used alongside the manual paper-ballot count[^s32] | Returning Officers per constituency[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | TARGET2-Ireland (Irish component of the Eurosystem T2 RTGS system)[^s33] | Central Bank of Ireland[^s33][^s34] | EU provider[^s33] | *Not yet measured* |
| High | Defence command and logistics (tier 1) | Defence Forces Enterprise network (NGWE project) and national Communications Information Services Network (CISN)[^s20] | Defence Forces CIS Corps[^s20] | National infrastructure[^s20] | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | National Control Centres (NCCs) of the transmission system operator[^s35] | EirGrid (transmission system operator)[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Disputed: the cited source no longer contains the quoted text (rechecked 2026-09-30)* | *Disputed: the cited source no longer contains the quoted text (rechecked 2026-09-30)* | *Not stated in sources* | *Disputed: the cited source no longer contains the quoted text (rechecked 2026-09-30)* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | National Shared Care Record (NSCR), HSE MyHealth@IE programme (read-only aggregated record)[^s36] | Health Service Executive (Health Identifiers Service)[^s37] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Computerised Infectious Disease Reporting (CIDR)[^s38] | Health Protection Surveillance Centre (HPSC); CIDR established 2004[^s39] | *Not stated in sources* | On average 33,394 notified cases per year, 2013-2019 (range 25,814-46,065)[^s39] |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 27 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 1 |
| EU provider | 1 |
| Mixed | 0 |
| Non-EU provider | 2 |
| Not stated in sources | 23 |

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

> Not yet sized. Capacity for Ireland will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 9 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Ireland without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Fingerprint biometric (tier 0)
- Document issuance history (tier 0)
- Authentication audit log (tier 0)
- Benefits & pensions (tier 1)
- Judicial & criminal justice (tier 1)
- Official gazette and legislation (tier 1)
- Government payroll and personnel (tier 1)
- Crisis management and civil protection (tier 1)
- Education (tier 1)

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

### The verdict on each fact about Ireland

0 of 67 printed facts about Ireland pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:IE:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | none | never checked |  |
| indicator:IE:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:IE:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:IE:C1 | indicator C1: Does the state operate its own government data centres that are in operation today? | unrecorded | none | never checked |  |
| indicator:IE:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | none | never checked |  |
| param:IE:population_m | param:IE:population_m | program:fetch_eurostat.py | none | never checked |  |
| param:IE:gdp_eur_bn | param:IE:gdp_eur_bn | program:fetch_eurostat.py | none | never checked |  |
| param:IE:gov_employment_k | param:IE:gov_employment_k | program:fetch_eurostat.py | none | never checked |  |
| param:IE:elec_price_eur_mwh | param:IE:elec_price_eur_mwh | program:fetch_eurostat.py | none | never checked |  |
| param:IE:renewables_pct | param:IE:renewables_pct | program:fetch_eurostat.py | none | never checked |  |
| param:IE:land_km2 | param:IE:land_km2 | program:fetch_eurostat.py | none | never checked |  |
| record:IE:civil_registry:register | Civil registry core: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:civil_registry:operator | Civil registry core: the body that operates it | unrecorded | none | never checked |  |
| record:IE:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:facial_biometric:operator | Facial biometric: the body that operates it | unrecorded | none | never checked |  |
| record:IE:facial_biometric:count | Facial biometric: how many records it holds | unrecorded | none | never checked |  |
| record:IE:breeder_documents:register | Breeder document scans: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:electoral_roll:foreign_dependency | Electoral roll entry: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | none | never checked |  |
| record:IE:electoral_roll:count | Electoral roll entry: how many records it holds | unrecorded | none | never checked |  |
| record:IE:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:digital_identity_credentials:count | Digital identity credentials: how many records it holds | unrecorded | none | never checked |  |
| record:IE:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | none | never checked |  |
| record:IE:land_property:register | Land & property registry: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:land_property:operator | Land & property registry: the body that operates it | unrecorded | none | never checked |  |
| record:IE:land_property:count | Land & property registry: how many records it holds | unrecorded | none | never checked |  |
| record:IE:police_records:register | Police information systems: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:police_records:operator | Police information systems: the body that operates it | unrecorded | none | never checked |  |
| record:IE:intelligence:register | Intelligence services: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:intelligence:operator | Intelligence services: the body that operates it | unrecorded | none | never checked |  |
| record:IE:emergency_communications:register | Emergency calls and public-safety radio: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:emergency_communications:foreign_dependency | Emergency calls and public-safety radio: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | none | never checked |  |
| record:IE:residence_permits:register | Residence and migration status: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:residence_permits:operator | Residence and migration status: the body that operates it | unrecorded | none | never checked |  |
| record:IE:tax:register | Tax: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:tax:operator | Tax: the body that operates it | unrecorded | none | never checked |  |
| record:IE:tax:count | Tax: how many records it holds | unrecorded | none | never checked |  |
| record:IE:customs:register | Customs declarations: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:customs:operator | Customs declarations: the body that operates it | unrecorded | none | never checked |  |
| record:IE:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:health_insurance:operator | Statutory health insurance: the body that operates it | unrecorded | none | never checked |  |
| record:IE:health_insurance:count | Statutory health insurance: how many records it holds | unrecorded | none | never checked |  |
| record:IE:business_registry:register | Business registry: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:business_registry:operator | Business registry: the body that operates it | unrecorded | none | never checked |  |
| record:IE:beneficial_ownership:register | Beneficial ownership register: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:beneficial_ownership:operator | Beneficial ownership register: the body that operates it | unrecorded | none | never checked |  |
| record:IE:vehicle_licensing:register | Vehicle & licensing: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:border_control:register | Border and visa systems: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:firearms_register:register | Firearms register: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:firearms_register:operator | Firearms register: the body that operates it | unrecorded | none | never checked |  |
| record:IE:public_finance:register | Treasury and state accounts: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:public_finance:operator | Treasury and state accounts: the body that operates it | unrecorded | none | never checked |  |
| record:IE:electoral_management:register | Election management and results: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:electoral_management:operator | Election management and results: the body that operates it | unrecorded | none | never checked |  |
| record:IE:central_bank:register | Central bank systems: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:central_bank:operator | Central bank systems: the body that operates it | unrecorded | none | never checked |  |
| record:IE:central_bank:foreign_dependency | Central bank systems: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | none | never checked |  |
| record:IE:defence_command:register | Defence command and logistics: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:defence_command:operator | Defence command and logistics: the body that operates it | unrecorded | none | never checked |  |
| record:IE:defence_command:foreign_dependency | Defence command and logistics: where its infrastructure runs: national / eu_provider / non_eu_provider / mixed | unrecorded | none | never checked |  |
| record:IE:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:grid_control:operator | Electricity grid control: the body that operates it | unrecorded | none | never checked |  |
| record:IE:health_records:register | Health records: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:health_records:operator | Health records: the body that operates it | unrecorded | none | never checked |  |
| record:IE:public_health_surveillance:register | Public health surveillance: the name of the register or system | unrecorded | none | never checked |  |
| record:IE:public_health_surveillance:operator | Public health surveillance: the body that operates it | unrecorded | none | never checked |  |
| record:IE:public_health_surveillance:count | Public health surveillance: how many records it holds | unrecorded | none | never checked |  |

---

[^s1]: Office of the Government Chief Information Officer (OGCIO) — Cloud Computing Advice Note (October 2019), 2019-10. Cloud Computing Advice Note (October 2019). <https://assets.per.gov.ie/documents/4468be59812f40dda7003116cf05f196_1.pdf>
[^s2]: Revenue Commissioners — Tax and Duty Manual Part 38-06-01 Revenue Online Service…, 2025-10. Tax and Duty Manual Part 38-06-01 Revenue Online Service (ROS). <https://www.revenue.ie/en/tax-professionals/tdm-wm/income-tax-capital-gains-tax-corporation-tax/part-38/38-06-01.pdf> ([archived](https://web.archive.org/web/20260520131022/https://www.revenue.ie/en/tax-professionals/tdm-wm/income-tax-capital-gains-tax-corporation-tax/part-38/38-06-01.pdf))
[^s3]: Department of Social Protection — Department of Social Protection Annual Report 2025, 2026-09-15. Department of Social Protection Annual Report 2025. <https://assets.gov.ie/static/documents/d05bae0e/20260915_-_DepartmentSocialProtection_AnnualReport_2025_EN_web.pdf>
[^s4]: Revenue Commissioners — Annual Report 2025, 2026. Annual Report 2025. <https://www.revenue.ie/en/corporate/press-office/annual-report/2025/ar-2025.pdf> ([archived](https://web.archive.org/web/20260507225147/https://www.revenue.ie/en/corporate/press-office/annual-report/2025/ar-2025.pdf))
[^s5]: Office of the Government Chief Information Officer (OGCIO) — Build To Share, 2025-07-30. Build To Share. <https://www.ogcio.gov.ie/en/corporate-pages/policy/build-to-share/> ([archived](https://web.archive.org/web/20260128012721/https://www.ogcio.gov.ie/en/corporate-pages/policy/build-to-share/))
[^s6]: Office of the Government Chief Information Officer (OGCIO) — Infrastructure, 2025-07-30. Infrastructure. <https://www.ogcio.gov.ie/en/corporate-pages/services/infrastructure/> ([archived](https://web.archive.org/web/20260618083911/https://www.ogcio.gov.ie/en/corporate-pages/services/infrastructure/))
[^s7]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s8]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s9]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s10]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s11]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s12]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s13]: Office of the Attorney General (Irish Statute Book) — Civil Registration Act 2004, Section 13, 2004. Civil Registration Act 2004, Section 13. <https://www.irishstatutebook.ie/eli/2004/act/3/section/13/enacted/en/html> ([archived](https://web.archive.org/web/20260615114456/https://www.irishstatutebook.ie/eli/2004/act/3/section/13/enacted/en/html))
[^s14]: Data Protection Commission — DPC announces conclusion of investigation into use of…, 2025-06-12. DPC announces conclusion of investigation into use of facial matching technology in connection with Public Services Card. <https://www.dataprotection.ie/en/news-media/press-releases/dpc-announces-conclusion-investigation-use-facial-matching-technology-connection-public-services> ([archived](https://web.archive.org/web/20260926120514/https://www.dataprotection.ie/en/news-media/press-releases/dpc-announces-conclusion-investigation-use-facial-matching-technology-connection-public-services))
[^s15]: Office of the Attorney General (Irish Statute Book) — Passports Act 2008, 2008. Passports Act 2008. <https://www.irishstatutebook.ie/eli/2008/act/4/enacted/en/print> ([archived](https://web.archive.org/web/20260607170551/https://www.irishstatutebook.ie/eli/2008/act/4/enacted/en/print))
[^s16]: An Coimisiún Toghcháin (Electoral Commission) — Oversight Report on the Electoral Registers, 2025. Oversight Report on the Electoral Registers. <https://cdn.electoralcommission.ie/app/uploads/2025/04/30104313/Oversight-Report-on-the-Electoral-Registers_online_english_tagged.pdf> ([archived](https://web.archive.org/web/20251026075202/https://cdn.electoralcommission.ie/app/uploads/2025/04/30104313/Oversight-Report-on-the-Electoral-Registers_online_english_tagged.pdf))
[^s17]: Tailte Éireann — Tailte Éireann Annual Report 2024, 2025. Tailte Éireann Annual Report 2024. <https://tailte.ie/wp-content/uploads/2025/11/TE_AnnualReport2024_GA_EN.pdf> ([archived](https://web.archive.org/web/20260513220930/https://tailte.ie/wp-content/uploads/2025/11/TE_AnnualReport2024_GA_EN.pdf))
[^s18]: Tailte Éireann — Tailte Éireann Annual Report 2025, 2026-09. Tailte Éireann Annual Report 2025. <https://tailte.ie/wp-content/uploads/2026/09/Annual-Report-2025-Final-EN-GA-1.pdf>
[^s19]: An Garda Síochána — Garda Information Services Centre (GISC). Garda Information Services Centre (GISC). <https://www.garda.ie/en/about-us/our-departments/garda-information-services-centre-gisc-/> ([archived](https://web.archive.org/web/20260610071140/https://www.garda.ie/en/about-us/our-departments/garda-information-services-centre-gisc-/))
[^s20]: Department of Defence — Department of Defence and Defence Forces Annual Report 2024, 2025. Department of Defence and Defence Forces Annual Report 2024. <https://assets.gov.ie/static/documents/54a1dec6/Department_of_Defence_and_Defence_Forces_Annual_Report_2024_English_DNet.pdf> ([archived](https://web.archive.org/web/20260311093310/https://assets.gov.ie/static/documents/54a1dec6/Department_of_Defence_and_Defence_Forces_Annual_Report_2024_English_DNet.pdf))
[^s21]: Motorola Solutions, Inc. — Motorola Solutions Acquires TETRA Ireland…, 2022-03-23. Motorola Solutions Acquires TETRA Ireland Communications, The Provider of Ireland's National Digital Radio Service. <https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-acquires-tetra-ireland-communications.html> ([archived](https://web.archive.org/web/20260711055831/https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-acquires-tetra-ireland-communications.html))
[^s22]: Immigration Service Delivery, Department of Justice — Information on revocation of registered Irish Residence…. Information on revocation of registered Irish Residence Permissions. <https://www.irishimmigration.ie/information-on-revocation-of-registered-irish-residence-permissions/> ([archived](https://web.archive.org/web/20260518125209/https://www.irishimmigration.ie/information-on-revocation-of-registered-irish-residence-permissions/))
[^s23]: An Garda Síochána — Immigration (GNIB) - Registration & Renewal of…. Immigration (GNIB) - Registration & Renewal of Immigration Permission. <https://www.garda.ie/en/about-us/organised-serious-crime/immigration-gnib-/> ([archived](https://web.archive.org/web/20260917111236/https://www.garda.ie/en/about-us/organised-serious-crime/immigration-gnib-/))
[^s24]: Health Information and Quality Authority — Primary Care Reimbursement Service (PCRS). Primary Care Reimbursement Service (PCRS). <https://www.hiqa.ie/areas-we-work/health-information/data-collections/primary-care-reimbursement-service-pcrs>
[^s25]: Health Service Executive (copy hosted by HRB National Drugs Library) — Primary Care Reimbursement Service Statistical Analysis…, 2026. Primary Care Reimbursement Service Statistical Analysis of Claims and Payments 2025. <https://www.drugsandalcohol.ie/46590/1/PCRS_Statistical_Analysis_of_Claims_and_Payments_2025.pdf>
[^s26]: Department of Enterprise, Tourism and Employment — Companies Registration Office (CRO). Companies Registration Office (CRO). <https://enterprise.gov.ie/en/who-we-are/offices-agencies/companies-registration-office-cro-.html> ([archived](https://web.archive.org/web/20260526152748/https://enterprise.gov.ie/en/who-we-are/offices-agencies/companies-registration-office-cro-.html))
[^s27]: Office of the Attorney General (Irish Statute Book) — S.I. No. 110 of 2019 European Union (Anti-Money…, 2019. S.I. No. 110 of 2019 European Union (Anti-Money Laundering: Beneficial Ownership of Corporate Entities) Regulations 2019. <https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print> ([archived](https://web.archive.org/web/20260613064358/https://www.irishstatutebook.ie/eli/2019/si/110/made/en/print))
[^s28]: Government of Ireland PSB Data Catalogue — National Vehicle and Driver Database. National Vehicle and Driver Database. <https://datacatalogue.gov.ie/dataset/national-vehicle-and-driver-database> ([archived](https://web.archive.org/web/20260217001228/https://datacatalogue.gov.ie/dataset/national-vehicle-and-driver-database))
[^s29]: An Garda Síochána — Schengen Information System (SIS): When was it introduced?. Schengen Information System (SIS): When was it introduced?. <https://www.garda.ie/en/about-us/our-departments/garda-national-crime-security-intelligence-service1/schengen-information-system-sis-/when-was-it-introduced-.html>
[^s30]: An Garda Síochána — Firearms Licensing. Firearms Licensing. <https://www.garda.ie/en/about-us/online-services/firearms-licensing/> ([archived](https://web.archive.org/web/20260917111136/https://www.garda.ie/en/about-us/online-services/firearms-licensing/))
[^s31]: Office of the Comptroller and Auditor General — Report on the Accounts of the Public Services 2022,…, 2023. Report on the Accounts of the Public Services 2022, Chapter 6: Financial management shared services: implementation progress. <https://www.audit.gov.ie/media/jqinw3i5/6-financial-management-shared-services-implementation-progress.pdf>
[^s32]: Department of Housing, Local Government and Heritage — Memorandum for the Guidance of Returning Officers,…, 2024. Memorandum for the Guidance of Returning Officers, General Election 2024. <https://assets.gov.ie/312963/3e85cb42-027b-4ede-8249-20112f9f652c.pdf>
[^s33]: Central Bank of Ireland — T2. T2. <https://www.centralbank.ie/financial-system/payments-and-securities-settlements/target-services/t2> ([archived](https://web.archive.org/web/20260315043823/https://www.centralbank.ie/financial-system/payments-and-securities-settlements/target-services/t2))
[^s34]: Central Bank of Ireland — Annual Report 2025 and Annual Performance Statement…, 2026. Annual Report 2025 and Annual Performance Statement 2025-2026. <https://www.centralbank.ie/docs/default-source/publications/corporate-reports/annual-reports/annual-report-2025-and-annual-performance-statement-2025-2026.pdf> ([archived](https://web.archive.org/web/20260801021138/https://www.centralbank.ie/docs/default-source/publications/corporate-reports/annual-reports/annual-report-2025-and-annual-performance-statement-2025-2026.pdf))
[^s35]: EirGrid — National Control Centres. National Control Centres. <https://www.eirgrid.ie/grid/how-grid-works/national-control-centres>
[^s36]: HSE MyHealth@IE programme (hosted by Irish Institute of Pharmacy) — National Shared Care Record: Enabling Data, Enhancing…, 2026-06-10. National Shared Care Record: Enabling Data, Enhancing Care (MyHealth@IE programme webinar). <https://iiop.ie/sites/default/files/2026-06/NSCR%20Presentation_10%20June%202026_IIOPWebinar.pdf>
[^s37]: Health Information and Quality Authority — National Register of Individual Health Identifiers. National Register of Individual Health Identifiers. <https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-register-individual-health-identifiers>
[^s38]: Health Protection Surveillance Centre (HSE) — Computerised Infectious Disease Reporting (CIDR). Computerised Infectious Disease Reporting (CIDR). <https://www.hpsc.ie/cidr/> ([archived](https://web.archive.org/web/20260911101522/https://www.hpsc.ie/cidr/))
[^s39]: Health Information and Quality Authority — Computerised Infectious Disease Reporting (CIDR) system. Computerised Infectious Disease Reporting (CIDR) system. <https://www.hiqa.ie/areas-we-work/health-information/data-collections/computerised-infectious-disease-reporting-cidr> ([archived](https://web.archive.org/web/20240704233334/https://www.hiqa.ie/areas-we-work/health-information/data-collections/computerised-infectious-disease-reporting-cidr))

**Evidence grades:** 29 Strong, 38 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
