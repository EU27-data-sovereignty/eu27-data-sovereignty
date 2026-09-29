# Spain: critical data holdings and sovereign hosting

> Generated 2026-09-29 by `model/generate_countries.py` from the content model (`model/document.py`). The same document is typeset as the country PDF and rendered on the web. Every fact carries a footnote to a source whose text was fetched and checked; a value in *italics* is withheld because no checked source supports it yet.

## Contents

1. [Data-sovereignty placement](#1-data-sovereignty-placement)
2. [Fundamentals](#2-fundamentals)
3. [Critical data holdings, by priority](#3-critical-data-holdings-by-priority)
4. [Foreign-dependency exposure](#4-foreign-dependency-exposure)
5. [Legal and institutional posture](#5-legal-and-institutional-posture)
6. [Capacity](#6-capacity)
7. [Research still open](#7-research-still-open)

## 1. Data-sovereignty placement

> Not demonstrated. Confidence: Low. With the evidence still open, Spain could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2][^s3][^s4] |
| State-controlled national eID | Yes[^s5][^s6] |
| Government data centres | Yes[^s7][^s6] |
| Government cloud in operation | Yes[^s7] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Spain described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 49.13 million[^s8] |
| GDP, current prices | 1 687.2 EUR bn[^s9] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 132.4 EUR/MWh[^s10] |
| Renewables share of electricity | 59.7 %[^s11] |
| Land area | 502 654 km²[^s12] |

## 3. Critical data holdings, by priority

The holdings Spain cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 14 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Registro Civil (Civil Registry): a single, electronic register for all of Spain[^s13] | Registry officers work under the functional authority of the Dirección General de Seguridad Jurídica y Fe Pública (Ministry of Justice)[^s13] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Fingerprint biometric (tier 0) | The decree refers to biometric records (registros biométricos) associated with the identity of Spanish nationals[^s5] | Dirección General de la Policía has custody of the DNI personal-data processing[^s5] | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Digitised data in the Civil Registry database are being migrated into individual records by the Ministry of Justice[^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | The system comprises the Central Register of Convicted Persons, the Central Register for Protection of Victims of Domestic and Gender Violence, and others[^s14] | The registry system is non-public and depends on the Ministry of Justice[^s14] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | RD 1155/2024 art. 212: a Central Register of Foreign Nationals exists within the DGP, recording entries, travel documents, stays and authorisations[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Ley General Tributaria: tax functions include issuing tax ID numbers and maintaining the tax censuses[^s16] | AEAT's Departamento de Informática Tributaria includes sub-directorates for IT planning and for operations (Explotación)[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | The SNS protected-population database generates a unique personal health ID code[^s18] | The law assigns the Ministry of Health to generate the unique SNS personal ID code[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | RD 609/2023 creates the Central Register of Beneficial Ownership, centralising beneficial-ownership information[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Vehicle Register of the Jefatura Central de Tráfico[^s20] | The Driver and Offender Register is kept by the Jefatura Central de Tráfico[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | The Central Personnel Register is the AGE register of its staff and of acts affecting their careers[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | SIRDEE, the State digital emergency radio system, is coordinated by the Secretariat of State for Security[^s22] | The 112 emergency call service is provided by the Autonomous Communities through their own call centres[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | The BOE is published in an electronic edition[^s24] | The Agencia Estatal BOE edits, publishes and distributes the official gazette[^s24] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | Municipalities send their Padrón data to the INE for national coordination[^s25] | INE is an autonomous body with its own legal personality[^s26] | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | Reference geographic information includes cadastral parcels and registered real estate[^s27] | Ley 14/2010 assigns the IGN duties for the AGE geographic information infrastructure and its Geoportal[^s27] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 14 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 14 |

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

- Facial biometric (tier 0)
- Document issuance history (tier 0)
- Digital identity credentials (tier 0)
- Authentication audit log (tier 0)
- Electoral roll entry (tier 0)
- State PKI and qualified trust services (tier 0)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
- Firearms register (tier 1)
- Treasury and state accounts (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Crisis management and civil protection (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Agencia Estatal Boletín Oficial del Estado ff149accef. Ley 9/1968, de 5 de abril, sobre secretos oficiales (texto consolidado). <https://www.boe.es/buscar/act.php?id=BOE-A-1968-444> ([archived](https://web.archive.org/web/20260908031744/https://www.boe.es/buscar/act.php?id=BOE-A-1968-444))
[^s2]: Agencia Estatal Boletín Oficial del Estado 1c59d3287e. Ley 66/1997, art. 81. <https://www.boe.es/buscar/act.php?id=BOE-A-1997-28053> ([archived](https://web.archive.org/web/20260823103301/https://www.boe.es/buscar/act.php?id=BOE-A-1997-28053))
[^s3]: Agencia Estatal Boletín Oficial del Estado f258cd5f31. Real Decreto 1114/1999, Estatuto de la entidad pública empresarial Fábrica Nacional de Moneda y Timbre-Real Casa de la Moneda. <https://www.boe.es/eli/es/rd/1999/06/25/1114/con>
[^s4]: Ministerio para la Transformación Digital y de la Función Pública 71ad256934. Spanish Trusted Service List (TSL). <https://tsl.digital.gob.es/TSL.xml>
[^s5]: Agencia Estatal Boletín Oficial del Estado 1f4d088076, 2025-04-02. Real Decreto 255/2025, de 1 de abril, por el que se regula el Documento Nacional de Identidad. <https://www.boe.es/buscar/act.php?id=BOE-A-2025-6601> ([archived](https://web.archive.org/web/20260716095158/https://www.boe.es/buscar/act.php?id=BOE-A-2025-6601))
[^s6]: European Commission, Interoperable Europe / NIFO 92a5c57c6a, 2024. Digital Public Administration Factsheet 2024 – Spain, Supporting document. <https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO_2024_Supporting%20document_Spain_vFINAL.pdf> ([archived](https://web.archive.org/web/20251013013711/https://interoperable-europe.ec.europa.eu/sites/default/files/inline-files/NIFO_2024_Supporting%20document_Spain_vFINAL.pdf))
[^s7]: Agencia Estatal Boletín Oficial del Estado 794a6fb20f, 2024-11-06. Real Decreto 1118/2024, de 5 de noviembre, por el que se aprueba el Estatuto de la Agencia Estatal de Administración Digital. <https://www.boe.es/buscar/act.php?id=BOE-A-2024-22929> ([archived](https://web.archive.org/web/20260420153252/https://www.boe.es/buscar/act.php?id=BOE-A-2024-22929))
[^s8]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s9]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s10]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s11]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s12]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s13]: Agencia Estatal Boletín Oficial del Estado 1242dc1af6, 2011-07-22. Ley 20/2011, de 21 de julio, del Registro Civil. <https://www.boe.es/buscar/act.php?id=BOE-A-2011-12628> ([archived](https://web.archive.org/web/20260923020539/https://www.boe.es/buscar/act.php?id=BOE-A-2011-12628))
[^s14]: Agencia Estatal Boletín Oficial del Estado 9982c3b5a8, 2009. Real Decreto 95/2009, de 6 de febrero, Sistema de registros administrativos de apoyo a la Administración de Justicia. <https://www.boe.es/buscar/act.php?id=BOE-A-2009-2073>
[^s15]: Agencia Estatal Boletín Oficial del Estado 8707a4fde0, 2024. Real Decreto 1155/2024, de 19 de noviembre, Reglamento de la Ley Orgánica 4/2000. <https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099>
[^s16]: Agencia Estatal Boletín Oficial del Estado d6a2c49c95, 2003. Ley 58/2003, de 17 de diciembre, General Tributaria. <https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186> ([archived](https://web.archive.org/web/20260923155550/https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186))
[^s17]: Agencia Estatal Boletín Oficial del Estado f7248f5be0, 1994. Orden de 2 de junio de 1994 por la que se desarrolla la estructura de la Agencia Estatal de Administración Tributaria. <https://www.boe.es/buscar/act.php?id=BOE-A-1994-12973> ([archived](https://web.archive.org/web/20240625182645/https://www.boe.es/buscar/act.php?id=BOE-A-1994-12973))
[^s18]: Agencia Estatal Boletín Oficial del Estado 24f4fc4900, 2004. Real Decreto 183/2004, de 30 de enero, por el que se regula la tarjeta sanitaria individual. <https://www.boe.es/buscar/act.php?id=BOE-A-2004-2591> ([archived](https://web.archive.org/web/20260514195911/https://www.boe.es/buscar/act.php?id=BOE-A-2004-2591))
[^s19]: Agencia Estatal Boletín Oficial del Estado 66991ad2c6, 2023. Real Decreto 609/2023, de 11 de julio, por el que se crea el Registro Central de Titularidades Reales. <https://www.boe.es/buscar/act.php?id=BOE-A-2023-16159> ([archived](https://web.archive.org/web/20260925090949/https://www.boe.es/buscar/act.php?id=BOE-A-2023-16159))
[^s20]: Agencia Estatal Boletín Oficial del Estado 389d7ca27c, 2015. Real Decreto Legislativo 6/2015, texto refundido de la Ley sobre Tráfico, Circulación de Vehículos a Motor y Seguridad Vial. <https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722> ([archived](https://web.archive.org/web/20260927160300/https://www.boe.es/buscar/act.php?id=BOE-A-2015-11722))
[^s21]: Agencia Estatal Boletín Oficial del Estado d89fdafcaa, 2000. Real Decreto 2073/1999, de 30 de diciembre, Reglamento del Registro Central de Personal. <https://www.boe.es/buscar/act.php?id=BOE-A-2000-1007>
[^s22]: Agencia Estatal Boletín Oficial del Estado e34810d9a5, 2024. Real Decreto 207/2024, de 27 de febrero, estructura orgánica básica del Ministerio del Interior. <https://www.boe.es/buscar/act.php?id=BOE-A-2024-3793>
[^s23]: Agencia Estatal Boletín Oficial del Estado 2dd2eff833, 1997. Real Decreto 903/1997, de 16 de junio, acceso al servicio de atención de llamadas de urgencia 112. <https://www.boe.es/buscar/act.php?id=BOE-A-1997-14058>
[^s24]: Agencia Estatal Boletín Oficial del Estado 18a4ff3b36, 2008. Real Decreto 181/2008, de 8 de febrero, de ordenación del diario oficial «Boletín Oficial del Estado». <https://www.boe.es/buscar/act.php?id=BOE-A-2008-2389> ([archived](https://web.archive.org/web/20260912062918/https://www.boe.es/buscar/act.php?id=BOE-A-2008-2389))
[^s25]: Agencia Estatal Boletín Oficial del Estado ebc6183af4, 1985. Ley 7/1985, de 2 de abril, Reguladora de las Bases del Régimen Local. <https://www.boe.es/buscar/act.php?id=BOE-A-1985-5392> ([archived](https://web.archive.org/web/20260923004539/https://www.boe.es/buscar/act.php?id=BOE-A-1985-5392))
[^s26]: Agencia Estatal Boletín Oficial del Estado 4524b1da96, 1989. Ley 12/1989, de 9 de mayo, de la Función Estadística Pública. <https://www.boe.es/buscar/act.php?id=BOE-A-1989-10767> ([archived](https://web.archive.org/web/20260716060905/https://www.boe.es/buscar/act.php?id=BOE-A-1989-10767))
[^s27]: Agencia Estatal Boletín Oficial del Estado 4c363a0682, 2010. Ley 14/2010, de 5 de julio, sobre las infraestructuras y los servicios de información geográfica en España. <https://www.boe.es/buscar/act.php?id=BOE-A-2010-10707> ([archived](https://web.archive.org/web/20260804161511/https://www.boe.es/buscar/act.php?id=BOE-A-2010-10707))
