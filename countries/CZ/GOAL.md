# Czechia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Czechia could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2] |
| Classification in law | Yes[^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s4][^s5] |
| State-controlled national eID | Yes[^s6][^s7] |
| Government data centres | Yes[^s8] |
| Government cloud in operation | Yes[^s8][^s2] |

What could move this placement:

- If any of the 33 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Czechia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 10.91 million[^s9] |
| GDP, current prices | 347.3 EUR bn[^s10] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 182.5 EUR/MWh[^s11] |
| Renewables share of electricity | 17.9 %[^s12] |
| Land area | 77 212 km²[^s13] |

## 3. Critical data holdings, by priority

The holdings Czechia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 27 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Facial biometric (tier 0) | ID card register (Evidence občanských průkazů), a public administration information system[^s14] | Ministry of the Interior is the controller of the ID card register[^s14] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s14] | — | — | — |
| Critical | Breeder document scans (tier 0) | Collection of documents (sbírka listin) underlying each civil status register book[^s15] | Registry offices transfer electronic civil status data to the Ministry of the Interior to set up a central civil-status information system by 31 Dec 2026[^s15] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | NIA keeps operational data including a record of each use of NIA data[^s7] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | The ID card register records invalid cards, the date and the reason they became invalid[^s14] | Ministry of the Interior is the controller of the ID card register[^s14] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | National point for identification and authentication (Národní bod, NIA), administered by DIA[^s7] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Electoral roll entry (tier 0) | Election administration information system (ISSV) whose components include the voter list[^s16] | Ministry of the Interior administers the ISSV, which keeps voter records[^s16] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | *Not yet sourced* | DIA acts as founder of the State Trust Services Administration[^s5] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Cadastre is kept in the Cadastre of Real Estate Information System (ISKN)[^s17] | ČÚZK is the central state authority for surveying and the cadastre[^s18] | *Not stated in sources* | More than 33 million documents in the digital part of the cadastral deed collection[^s17] |
| High | Judicial & criminal justice (tier 1) | Criminal Records Register: public administration IS of persons finally convicted[^s19] | Ministry of Justice is the controller[^s19] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | Police operate and control the foreigners' information system, incl. photos and fingerprints[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Automated Tax Information System (ADIS) of the Financial Administration[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | Automated import system e-Dovoz completing electronic customs systems for transit, export and import[^s22] | Customs Administration: General Directorate of Customs and customs offices[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | ČSSZ keeps the register of pension insurance contributors[^s24] | MPSV is controller of the integrated MPSV information system, which includes the ČSSZ system[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | VZP keeps the register of all persons insured under public health insurance[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | The Public Register is a public administration IS kept electronically by the registry courts[^s26] | DIA administers the Basic Register of Persons (ROS) and assigns company identification numbers[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Register of beneficial owners is a public administration IS controlled by the Ministry of Justice[^s28] | Kept by the court competent for registration; entries made by courts or notaries[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Road Vehicle Register, controlled by the Ministry of Transport, records vehicles, owners and operators[^s29] | Ministry of Transport keeps the central driver register and digital tachograph system[^s30] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Ministry of Foreign Affairs visa information system incl. photographs and fingerprints[^s20] | Police Presidium operates the national component of SIS and the SIRENE function[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Central Firearms Register: non-public public administration IS[^s32] | Police Presidium is the controller[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | Civil service information system for service relationships[^s33] | Office of the Government is the controller[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | ISSV components include the register of candidate lists and of polling-station commissions[^s16] | Czech Statistical Office runs results collection and builds the results system including software[^s16] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | 14 interconnected 112 call centres[^s34] | 112 runs through 14 regional operational and information centres of the Fire Rescue Service[^s35] | *Not stated in sources* | 1,995,395 calls and 33,035 SMS to 112 in 2025[^s35] |
| High | Crisis management and civil protection (tier 1) | Crisis management information system supporting crisis authorities[^s36] | Administered by the Ministry of the Interior through the Fire Rescue Service directorate[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | SÚKL ('Ústav') establishes eRecept as a public administration information system[^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Includes the register of infectious disease cases and vaccination[^s38] | Infectious disease IS: Ministry of Health controller, ÚZIS operator[^s38] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | ČÚZK publishes parcels from ISKN and buildings/addresses from RÚIAN[^s17] | ČÚZK is the controller of the territorial identification register (RÚIAN)[^s27] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 26 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 26 |

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

> Not yet sized. Capacity for Czechia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Czechia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Civil registry core (tier 0)
- Police information systems (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Národní úřad pro kybernetickou a informační bezpečnost (NÚKIB), Sbírka zákonů ČR — Vyhláška č. 505/2025 Sb., o některých požadavcích pro…, 2025-12-05. Vyhláška č. 505/2025 Sb., o některých požadavcích pro zápis do katalogu cloud computingu, příloha č. 4. <https://www.zakonyprolidi.cz/cs/2025-505> ([archived](https://web.archive.org/web/20260421002355/https://www.zakonyprolidi.cz/cs/2025-505))
[^s2]: Sbírka zákonů ČR (consolidated text via zakonyprolidi.cz) — Zákon č. 365/2000 Sb., o informačních systémech veřejné…, 2026-01-01. Zákon č. 365/2000 Sb., o informačních systémech veřejné správy, § 6m odst. 2 (consolidated text, version effective 1.1.2026). <https://www.zakonyprolidi.cz/cs/2000-365> ([archived](https://web.archive.org/web/20260130002605/https://www.zakonyprolidi.cz/cs/2000-365))
[^s3]: Sbírka zákonů ČR (consolidated text via zakonyprolidi.cz) — Zákon č. 412/2005 Sb., o ochraně utajovaných informací a…, 2005-10-18. Zákon č. 412/2005 Sb., o ochraně utajovaných informací a o bezpečnostní způsobilosti, § 4 Stupně utajení. <https://www.zakonyprolidi.cz/cs/2005-412> ([archived](https://web.archive.org/web/20260416083654/https://www.zakonyprolidi.cz/cs/2005-412))
[^s4]: Správa státních služeb vytvářejících důvěru, s. p. o. — Úvodní strana – Správa státních služeb vytvářejících důvěru. Úvodní strana – Správa státních služeb vytvářejících důvěru. <https://sssvd.gov.cz/>
[^s5]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 297/2016 Sb., o službách vytvářejících důvěru…, 2016. Zákon č. 297/2016 Sb., o službách vytvářejících důvěru pro elektronické transakce. <https://www.zakonyprolidi.cz/cs/2016-297> ([archived](https://web.archive.org/web/20260503120919/https://www.zakonyprolidi.cz/cs/2016-297))
[^s6]: Digitální a informační agentura — Elektronická identita – Informační web elektronické…. Elektronická identita – Informační web elektronické identity (Národní identitní autorita). <https://info.identitaobcana.cz/> ([archived](https://web.archive.org/web/20241116155854/https://info.identitaobcana.cz/))
[^s7]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 250/2017 Sb., o elektronické identifikaci, 2017. Zákon č. 250/2017 Sb., o elektronické identifikaci. <https://www.zakonyprolidi.cz/cs/2017-250>
[^s8]: Státní pokladna Centrum sdílených služeb, s. p. — SPCSS – Státní pokladna Centrum sdílených služeb, s. p.…, 2026-05-14. SPCSS – Státní pokladna Centrum sdílených služeb, s. p. (homepage, archived 14 May 2026). <https://web.archive.org/web/20260514094405/https://www.spcss.cz/>
[^s9]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s10]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s11]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s12]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s13]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s14]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 269/2021 Sb., o občanských průkazech, 2021. Zákon č. 269/2021 Sb., o občanských průkazech. <https://www.zakonyprolidi.cz/cs/2021-269>
[^s15]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 301/2000 Sb., o matrikách, jménu a příjmení, 2000. Zákon č. 301/2000 Sb., o matrikách, jménu a příjmení. <https://www.zakonyprolidi.cz/cs/2000-301> ([archived](https://web.archive.org/web/20260224043912/https://www.zakonyprolidi.cz/cs/2000-301))
[^s16]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 88/2024 Sb., o správě voleb, 2024. Zákon č. 88/2024 Sb., o správě voleb. <https://www.zakonyprolidi.cz/cs/2024-88> ([archived](https://web.archive.org/web/20260113232740/https://www.zakonyprolidi.cz/cs/2024-88))
[^s17]: Český úřad zeměměřický a katastrální — Výroční zpráva ČÚZK za rok 2025, 2026-03-10. Výroční zpráva ČÚZK za rok 2025. <https://cuzk.gov.cz/getattachment/f9eb09fe-b4e4-4fae-9a5a-57af8e46edeb/Vyrocni-zprava-2025_final.pdf.aspx> ([archived](https://web.archive.org/web/20260310200755/https://cuzk.gov.cz/getattachment/f9eb09fe-b4e4-4fae-9a5a-57af8e46edeb/Vyrocni-zprava-2025_final.pdf.aspx))
[^s18]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 359/1992 Sb., o zeměměřických a katastrálních…, 1992. Zákon č. 359/1992 Sb., o zeměměřických a katastrálních orgánech. <https://www.zakonyprolidi.cz/cs/1992-359> ([archived](https://web.archive.org/web/20260210112357/https://www.zakonyprolidi.cz/cs/1992-359))
[^s19]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 269/1994 Sb., o rejstříku trestů, 1994. Zákon č. 269/1994 Sb., o rejstříku trestů. <https://www.zakonyprolidi.cz/cs/1994-269> ([archived](https://web.archive.org/web/20260312160053/https://www.zakonyprolidi.cz/cs/1994-269))
[^s20]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 326/1999 Sb., o pobytu cizinců na území České…, 1999. Zákon č. 326/1999 Sb., o pobytu cizinců na území České republiky. <https://www.zakonyprolidi.cz/cs/1999-326>
[^s21]: Generální finanční ředitelství — Organizační řád Generálního finančního ředitelství. Organizační řád Generálního finančního ředitelství. <https://financnisprava.gov.cz/assets/cs/prilohy/fs-financni-sprava-cr/OR_FS_UZ_D4.pdf>
[^s22]: Celní správa ČR — e-Dovoz (tisková zpráva), 2010-10-29. e-Dovoz (tisková zpráva). <https://celnisprava.gov.cz/cz/crhradeckralove/tiskove-zpravy/2010/Stranky/e-dovoz.aspx>
[^s23]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 17/2012 Sb., o Celní správě České republiky, 2012. Zákon č. 17/2012 Sb., o Celní správě České republiky. <https://www.zakonyprolidi.cz/cs/2012-17> ([archived](https://web.archive.org/web/20260214074216/https://www.zakonyprolidi.cz/cs/2012-17))
[^s24]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 582/1991 Sb., o organizaci a provádění…, 1991. Zákon č. 582/1991 Sb., o organizaci a provádění sociálního zabezpečení. <https://www.zakonyprolidi.cz/cs/1991-582>
[^s25]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 592/1992 Sb., o pojistném na veřejné zdravotní…, 1992. Zákon č. 592/1992 Sb., o pojistném na veřejné zdravotní pojištění. <https://www.zakonyprolidi.cz/cs/1992-592> ([archived](https://web.archive.org/web/20260501174125/https://www.zakonyprolidi.cz/cs/1992-592))
[^s26]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 304/2013 Sb., o veřejných rejstřících…, 2013. Zákon č. 304/2013 Sb., o veřejných rejstřících právnických a fyzických osob. <https://www.zakonyprolidi.cz/cs/2013-304> ([archived](https://web.archive.org/web/20260201065444/https://www.zakonyprolidi.cz/cs/2013-304))
[^s27]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 111/2009 Sb., o základních registrech, 2009. Zákon č. 111/2009 Sb., o základních registrech. <https://www.zakonyprolidi.cz/cs/2009-111> ([archived](https://web.archive.org/web/20251114195208/https://www.zakonyprolidi.cz/cs/2009-111))
[^s28]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 37/2021 Sb., o evidenci skutečných majitelů, 2021. Zákon č. 37/2021 Sb., o evidenci skutečných majitelů. <https://www.zakonyprolidi.cz/cs/2021-37> ([archived](https://web.archive.org/web/20251007111453/https://www.zakonyprolidi.cz/cs/2021-37))
[^s29]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 56/2001 Sb., o podmínkách provozu vozidel na…, 2001. Zákon č. 56/2001 Sb., o podmínkách provozu vozidel na pozemních komunikacích. <https://www.zakonyprolidi.cz/cs/2001-56> ([archived](https://web.archive.org/web/20260323232108/https://www.zakonyprolidi.cz/cs/2001-56))
[^s30]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 361/2000 Sb., o provozu na pozemních komunikacích, 2000. Zákon č. 361/2000 Sb., o provozu na pozemních komunikacích. <https://www.zakonyprolidi.cz/cs/2000-361> ([archived](https://web.archive.org/web/20260711182736/https://www.zakonyprolidi.cz/cs/2000-361))
[^s31]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 273/2008 Sb., o Policii České republiky, 2008. Zákon č. 273/2008 Sb., o Policii České republiky. <https://www.zakonyprolidi.cz/cs/2008-273> ([archived](https://web.archive.org/web/20260404065219/https://www.zakonyprolidi.cz/cs/2008-273))
[^s32]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 90/2024 Sb., o zbraních a střelivu, 2024. Zákon č. 90/2024 Sb., o zbraních a střelivu. <https://www.zakonyprolidi.cz/cs/2024-90> ([archived](https://web.archive.org/web/20260623173655/https://www.zakonyprolidi.cz/cs/2024-90))
[^s33]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 234/2014 Sb., o státní službě, 2014. Zákon č. 234/2014 Sb., o státní službě. <https://www.zakonyprolidi.cz/cs/2014-234> ([archived](https://web.archive.org/web/20260427134705/https://www.zakonyprolidi.cz/cs/2014-234))
[^s34]: Hasičský záchranný sbor České republiky — Tísňová linka 112 má svůj den. Tísňová linka 112 má svůj den. <https://hzscr.gov.cz/clanek/tisnova-linka-112-ma-svuj-den> ([archived](https://web.archive.org/web/20250429081533/https://hzscr.gov.cz/clanek/tisnova-linka-112-ma-svuj-den))
[^s35]: Hasičský záchranný sbor České republiky — Tísňová linka 112 funguje už 22 let, 2026-02-10. Tísňová linka 112 funguje už 22 let. <https://hzscr.gov.cz/clanek/hzs-jihoceskeho-kraje-menu-informacni-servis-zpravodajstvi-2026-unor-tisnova-linka-112-funguje-uz-22-let.aspx>
[^s36]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 240/2000 Sb., o krizovém řízení (krizový zákon), 2000. Zákon č. 240/2000 Sb., o krizovém řízení (krizový zákon). <https://www.zakonyprolidi.cz/cs/2000-240>
[^s37]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 378/2007 Sb., o léčivech, 2007. Zákon č. 378/2007 Sb., o léčivech. <https://www.zakonyprolidi.cz/cs/2007-378>
[^s38]: Zákony pro lidi (consolidated text of Sbírka zákonů) — Zákon č. 258/2000 Sb., o ochraně veřejného zdraví, 2000. Zákon č. 258/2000 Sb., o ochraně veřejného zdraví. <https://www.zakonyprolidi.cz/cs/2000-258> ([archived](https://web.archive.org/web/20260319172250/https://www.zakonyprolidi.cz/cs/2000-258))

**Evidence grades:** 3 Strong, 56 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review. Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.
