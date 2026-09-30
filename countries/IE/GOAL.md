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
| State-controlled trust anchor | *Not yet sourced* |
| State-controlled national eID | *Not yet sourced* |
| Government data centres | Yes[^s1][^s2] |
| Government cloud in operation | Yes[^s2][^s3] |

What could move this placement:

Nothing: every input the rule reads is settled by a source.

## 2. Fundamentals

Ireland described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 5.44 million[^s4] |
| GDP, current prices | 602.4 EUR bn[^s5] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 255.2 EUR/MWh[^s6] |
| Renewables share of electricity | 41.3 %[^s7] |
| Land area | 68 655 km²[^s8] |

## 3. Critical data holdings, by priority

The holdings Ireland cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 22 of 39 holding classes have a verified source; 7 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Facial biometric (tier 0) | SAFE 2 registration biometric facial templates (Public Services Card)[^s9] | Department of Social Protection (DSP)[^s9] | *Not stated in sources* | Facial templates for 70% of the State's population (2021)[^s9] |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Electoral roll entry (tier 0) | *Not yet sourced* | *Not yet sourced* | Non-EU provider[^s10] | 3.87 million registered electors (December 2024)[^s10] |
| High | Document issuance history (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | ROS digital certificate PKI (Revenue CA), also used by CRO, Department of Transport and Department of Social Protection[^s11] | Revenue Commissioners act as Certification Authority for ROS digital certificates[^s11] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | National Land Register (folios of the Land Registry) and Registry of Deeds[^s12] | Tailte Éireann (civil service body under the Tailte Éireann Act 2022)[^s12] | *Not stated in sources* | 2.4 million folios with associated spatial data accessible via landdirect.ie[^s12] |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | PULSE (An Garda Síochána's national incident and intelligence database)[^s13] | An Garda Síochána[^s13] | *Not stated in sources* | *Not yet measured* |
| High | Intelligence services (tier 1) | Defence Forces Military Intelligence holdings[^s14] | National Security Analysis Centre (established by Government in 2019)[^s14] | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | National Digital Radio Service (NDRS), TETRA network for first responders[^s15] | *Not yet sourced* | Non-EU provider[^s15] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Irish Residence Permission (IRP) register: the register of non-nationals with permission to be in the State[^s16] | Immigration Service Delivery (ISD), Department of Justice (took over first-time registration from the Garda National Immigration Bureau, 13 January 2025)[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | Automated Import System (AIS), Automated Export System (AES) and New Computerised Transit System (NCTS)[^s18] | Revenue Commissioners[^s18] | *Not stated in sources* | *Not yet sourced* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | PCRS eligibility records (medical card / GMS scheme eligibility, keyed on PPSN)[^s19] | HSE Primary Care Reimbursement Service (PCRS)[^s19] | *Not stated in sources* | 1,552,553 GMS (medical card) eligible persons and 785,152 GP visit card holders in 2025[^s20] |
| High | Business registry (tier 1) | Register of companies, business names and limited partnerships held by the Companies Registration Office[^s21] | Companies Registration Office (CRO), an office of the Department of Enterprise, Tourism and Employment[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Vehicle & licensing (tier 1) | National Vehicle and Driver File (NVDF)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | National connection to the Schengen Information System (SIS), live in Ireland since 15 March 2021[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Firearm certificates (three-year certificates, renewal phases administered by An Garda Síochána)[^s24] | An Garda Síochána (applications decided by the local Superintendent)[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Financial Management Shared Services (FMSS) system, the shared government financial management system (incl. the Exchequer)[^s25] | National Shared Services Office (FMSS); Department of Finance manages the Exchequer[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | Election Count Database System (Ecount), used alongside the manual paper-ballot count[^s26] | Returning Officers per constituency[^s26] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | TARGET2-Ireland (Irish component of the Eurosystem T2 RTGS system)[^s27] | Central Bank of Ireland[^s28] | EU provider[^s27] | *Not yet measured* |
| High | Defence command and logistics (tier 1) | Defence Forces Enterprise network (NGWE project) and national Communications Information Services Network (CISN)[^s14] | Defence Forces CIS Corps[^s14] | National infrastructure[^s14] | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | National Control Centres (NCCs) of the transmission system operator[^s29] | EirGrid (transmission system operator)[^s29] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | National Operations Management Centre (24/7 alarm and treatment monitoring)[^s30] | Uisce Éireann (national water utility, designated activity company)[^s30] | *Not stated in sources* | Alarms monitored at 517 water treatment plants[^s30] |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | National Shared Care Record (NSCR), HSE MyHealth@IE programme (read-only aggregated record)[^s31] | Health Service Executive (Health Identifiers Service)[^s32] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Computerised Infectious Disease Reporting (CIDR)[^s33] | Health Protection Surveillance Centre (HPSC); CIDR established 2004[^s34] | *Not stated in sources* | On average 33,394 notified cases per year, 2013-2019 (range 25,814-46,065)[^s34] |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 22 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 1 |
| EU provider | 1 |
| Mixed | 0 |
| Non-EU provider | 2 |
| Not stated in sources | 18 |

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

> Not yet sized. Capacity for Ireland will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 7 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Ireland without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Civil registry core (tier 0)
- Fingerprint biometric (tier 0)
- Breeder document scans (tier 0)
- Document issuance history (tier 0)
- Digital identity credentials (tier 0)
- Authentication audit log (tier 0)
- Tax (tier 1)
- Benefits & pensions (tier 1)
- Beneficial ownership register (tier 1)
- Judicial & criminal justice (tier 1)
- Official gazette and legislation (tier 1)
- Government payroll and personnel (tier 1)
- Crisis management and civil protection (tier 1)
- Education (tier 1)

---

[^s1]: Office of the Government Chief Information Officer (OGCIO) — Cloud Computing Advice Note (October 2019), 2019-10. Cloud Computing Advice Note (October 2019). <https://assets.per.gov.ie/documents/4468be59812f40dda7003116cf05f196_1.pdf>
[^s2]: Office of the Government Chief Information Officer (OGCIO) — Build To Share, 2025-07-30. Build To Share. <https://www.ogcio.gov.ie/en/corporate-pages/policy/build-to-share/> ([archived](https://web.archive.org/web/20260128012721/https://www.ogcio.gov.ie/en/corporate-pages/policy/build-to-share/))
[^s3]: Office of the Government Chief Information Officer (OGCIO) — Infrastructure, 2025-07-30. Infrastructure. <https://www.ogcio.gov.ie/en/corporate-pages/services/infrastructure/> ([archived](https://web.archive.org/web/20260618083911/https://www.ogcio.gov.ie/en/corporate-pages/services/infrastructure/))
[^s4]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s5]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s6]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s7]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s8]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s9]: Data Protection Commission — DPC announces conclusion of investigation into use of…, 2025-06-12. DPC announces conclusion of investigation into use of facial matching technology in connection with Public Services Card. <https://www.dataprotection.ie/en/news-media/press-releases/dpc-announces-conclusion-investigation-use-facial-matching-technology-connection-public-services> ([archived](https://web.archive.org/web/20260926120514/https://www.dataprotection.ie/en/news-media/press-releases/dpc-announces-conclusion-investigation-use-facial-matching-technology-connection-public-services))
[^s10]: An Coimisiún Toghcháin (Electoral Commission) — Oversight Report on the Electoral Registers, 2025. Oversight Report on the Electoral Registers. <https://cdn.electoralcommission.ie/app/uploads/2025/04/30104313/Oversight-Report-on-the-Electoral-Registers_online_english_tagged.pdf> ([archived](https://web.archive.org/web/20251026075202/https://cdn.electoralcommission.ie/app/uploads/2025/04/30104313/Oversight-Report-on-the-Electoral-Registers_online_english_tagged.pdf))
[^s11]: Revenue Commissioners — Tax and Duty Manual Part 38-06-01 Revenue Online Service…, 2025-10. Tax and Duty Manual Part 38-06-01 Revenue Online Service (ROS). <https://www.revenue.ie/en/tax-professionals/tdm-wm/income-tax-capital-gains-tax-corporation-tax/part-38/38-06-01.pdf> ([archived](https://web.archive.org/web/20260520131022/https://www.revenue.ie/en/tax-professionals/tdm-wm/income-tax-capital-gains-tax-corporation-tax/part-38/38-06-01.pdf))
[^s12]: Tailte Éireann — Tailte Éireann Annual Report 2024, 2025. Tailte Éireann Annual Report 2024. <https://tailte.ie/wp-content/uploads/2025/11/TE_AnnualReport2024_GA_EN.pdf> ([archived](https://web.archive.org/web/20260513220930/https://tailte.ie/wp-content/uploads/2025/11/TE_AnnualReport2024_GA_EN.pdf))
[^s13]: An Garda Síochána — Garda Information Services Centre (GISC). Garda Information Services Centre (GISC). <https://www.garda.ie/en/about-us/our-departments/garda-information-services-centre-gisc-/> ([archived](https://web.archive.org/web/20260610071140/https://www.garda.ie/en/about-us/our-departments/garda-information-services-centre-gisc-/))
[^s14]: Department of Defence — Department of Defence and Defence Forces Annual Report 2024, 2025. Department of Defence and Defence Forces Annual Report 2024. <https://assets.gov.ie/static/documents/54a1dec6/Department_of_Defence_and_Defence_Forces_Annual_Report_2024_English_DNet.pdf> ([archived](https://web.archive.org/web/20260311093310/https://assets.gov.ie/static/documents/54a1dec6/Department_of_Defence_and_Defence_Forces_Annual_Report_2024_English_DNet.pdf))
[^s15]: Motorola Solutions, Inc. — Motorola Solutions Acquires TETRA Ireland…, 2022-03-23. Motorola Solutions Acquires TETRA Ireland Communications, The Provider of Ireland's National Digital Radio Service. <https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-acquires-tetra-ireland-communications.html> ([archived](https://web.archive.org/web/20260711055831/https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-acquires-tetra-ireland-communications.html))
[^s16]: Immigration Service Delivery, Department of Justice — Information on revocation of registered Irish Residence…. Information on revocation of registered Irish Residence Permissions. <https://www.irishimmigration.ie/information-on-revocation-of-registered-irish-residence-permissions/> ([archived](https://web.archive.org/web/20260518125209/https://www.irishimmigration.ie/information-on-revocation-of-registered-irish-residence-permissions/))
[^s17]: An Garda Síochána — Immigration (GNIB) - Registration & Renewal of…. Immigration (GNIB) - Registration & Renewal of Immigration Permission. <https://www.garda.ie/en/about-us/organised-serious-crime/immigration-gnib-/> ([archived](https://web.archive.org/web/20260917111236/https://www.garda.ie/en/about-us/organised-serious-crime/immigration-gnib-/))
[^s18]: Revenue Commissioners — Annual Report 2025, 2026. Annual Report 2025. <https://www.revenue.ie/en/corporate/press-office/annual-report/2025/ar-2025.pdf> ([archived](https://web.archive.org/web/20260507225147/https://www.revenue.ie/en/corporate/press-office/annual-report/2025/ar-2025.pdf))
[^s19]: Health Information and Quality Authority — Primary Care Reimbursement Service (PCRS). Primary Care Reimbursement Service (PCRS). <https://www.hiqa.ie/areas-we-work/health-information/data-collections/primary-care-reimbursement-service-pcrs>
[^s20]: Health Service Executive (copy hosted by HRB National Drugs Library) — Primary Care Reimbursement Service Statistical Analysis…, 2026. Primary Care Reimbursement Service Statistical Analysis of Claims and Payments 2025. <https://www.drugsandalcohol.ie/46590/1/PCRS_Statistical_Analysis_of_Claims_and_Payments_2025.pdf>
[^s21]: Department of Enterprise, Tourism and Employment — Companies Registration Office (CRO). Companies Registration Office (CRO). <https://enterprise.gov.ie/en/who-we-are/offices-agencies/companies-registration-office-cro-.html> ([archived](https://web.archive.org/web/20260526152748/https://enterprise.gov.ie/en/who-we-are/offices-agencies/companies-registration-office-cro-.html))
[^s22]: Government of Ireland PSB Data Catalogue — National Vehicle and Driver Database. National Vehicle and Driver Database. <https://datacatalogue.gov.ie/dataset/national-vehicle-and-driver-database> ([archived](https://web.archive.org/web/20260217001228/https://datacatalogue.gov.ie/dataset/national-vehicle-and-driver-database))
[^s23]: An Garda Síochána — Schengen Information System (SIS): When was it introduced?. Schengen Information System (SIS): When was it introduced?. <https://www.garda.ie/en/about-us/our-departments/garda-national-crime-security-intelligence-service1/schengen-information-system-sis-/when-was-it-introduced-.html>
[^s24]: An Garda Síochána — Firearms Licensing. Firearms Licensing. <https://www.garda.ie/en/about-us/online-services/firearms-licensing/> ([archived](https://web.archive.org/web/20260917111136/https://www.garda.ie/en/about-us/online-services/firearms-licensing/))
[^s25]: Office of the Comptroller and Auditor General — Report on the Accounts of the Public Services 2022,…, 2023. Report on the Accounts of the Public Services 2022, Chapter 6: Financial management shared services: implementation progress. <https://www.audit.gov.ie/media/jqinw3i5/6-financial-management-shared-services-implementation-progress.pdf>
[^s26]: Department of Housing, Local Government and Heritage — Memorandum for the Guidance of Returning Officers,…, 2024. Memorandum for the Guidance of Returning Officers, General Election 2024. <https://assets.gov.ie/312963/3e85cb42-027b-4ede-8249-20112f9f652c.pdf>
[^s27]: Central Bank of Ireland — T2. T2. <https://www.centralbank.ie/financial-system/payments-and-securities-settlements/target-services/t2> ([archived](https://web.archive.org/web/20260315043823/https://www.centralbank.ie/financial-system/payments-and-securities-settlements/target-services/t2))
[^s28]: Central Bank of Ireland — Annual Report 2025 and Annual Performance Statement…, 2026. Annual Report 2025 and Annual Performance Statement 2025-2026. <https://www.centralbank.ie/docs/default-source/publications/corporate-reports/annual-reports/annual-report-2025-and-annual-performance-statement-2025-2026.pdf> ([archived](https://web.archive.org/web/20260801021138/https://www.centralbank.ie/docs/default-source/publications/corporate-reports/annual-reports/annual-report-2025-and-annual-performance-statement-2025-2026.pdf))
[^s29]: EirGrid — National Control Centres. National Control Centres. <https://www.eirgrid.ie/grid/how-grid-works/national-control-centres>
[^s30]: Uisce Éireann — Delivering Water Services for Ireland: Annual Report and…, 2025. Delivering Water Services for Ireland: Annual Report and Financial Statements 2024. <https://www.water.ie/sites/default/files/2025-07/Uisce-Eireann-2024-Annual-Report-EN.pdf>
[^s31]: HSE MyHealth@IE programme (hosted by Irish Institute of Pharmacy) — National Shared Care Record: Enabling Data, Enhancing…, 2026-06-10. National Shared Care Record: Enabling Data, Enhancing Care (MyHealth@IE programme webinar). <https://iiop.ie/sites/default/files/2026-06/NSCR%20Presentation_10%20June%202026_IIOPWebinar.pdf>
[^s32]: Health Information and Quality Authority — National Register of Individual Health Identifiers. National Register of Individual Health Identifiers. <https://www.hiqa.ie/areas-we-work/health-information/data-collections/national-register-individual-health-identifiers>
[^s33]: Health Protection Surveillance Centre (HSE) — Computerised Infectious Disease Reporting (CIDR). Computerised Infectious Disease Reporting (CIDR). <https://www.hpsc.ie/cidr/> ([archived](https://web.archive.org/web/20260911101522/https://www.hpsc.ie/cidr/))
[^s34]: Health Information and Quality Authority — Computerised Infectious Disease Reporting (CIDR) system. Computerised Infectious Disease Reporting (CIDR) system. <https://www.hiqa.ie/areas-we-work/health-information/data-collections/computerised-infectious-disease-reporting-cidr> ([archived](https://web.archive.org/web/20240704233334/https://www.hiqa.ie/areas-we-work/health-information/data-collections/computerised-infectious-disease-reporting-cidr))
