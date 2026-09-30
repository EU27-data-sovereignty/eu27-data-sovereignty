# Latvia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Latvia could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2] |
| Classification in law | Yes[^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s4] |
| State-controlled national eID | Yes[^s5][^s6] |
| Government data centres | Yes[^s7][^s4] |
| Government cloud in operation | Yes[^s8][^s9] |

What could move this placement:

- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Latvia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 1.86 million[^s10] |
| GDP, current prices | 43.0 EUR bn[^s11] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 136.1 EUR/MWh[^s12] |
| Renewables share of electricity | 55.5 %[^s13] |
| Land area | 63 290 km²[^s14] |

## 3. Critical data holdings, by priority

The holdings Latvia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 14 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Fizisko personu reģistrs (Register of Natural Persons), the single system for registering and identifying natural persons[^s15] | The controller and holder of the Register is PMLP (Office of Citizenship and Migration Affairs)[^s15] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | Civil status register entries are held on paper in one copy and electronically in the Register of Natural Persons[^s16] | Registry offices keep paper civil status entries for 100 years, then transfer them to the National Archives of Latvia[^s16] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Invalid (revoked, lost) identity documents are entered in the state information system 'Register of Invalid Documents'[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | LVRTC provides four eID means: eID card, eParaksts card, eParaksts card+ and eParaksts mobile[^s18] | The Digital Security Supervisory Committee has qualified and supervises two eID providers: Smart-ID and the state company LVRTC[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Voter Register Law establishes the Voter Register and the Electronic Online Voter Register[^s19] | PMLP processes the data in, and is the controller of, the Voter Register[^s19] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Judicial & criminal justice (tier 1) | TIS is the state information system for case management and proceedings of all courts, including the Supreme Court and the Constitutional Court[^s20] | The Punishment Register is a state information system controlled and held by the Interior Ministry Information Centre[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Cabinet regulations define the data held in the Integrated Interior Information System for locating persons, property and documents[^s22] | The system's controller and holder is the Interior Ministry Information Centre[^s22] | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | The Register of Natural Persons records residence permits, EU registration certificates and permanent residence certificates[^s15] | Asylum Law: PMLP maintains the Register of Asylum Seekers[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Law on Taxes and Fees: VID communicates with taxpayers through its Electronic Declaration System (EDS)[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | Customs documents go through EU central customs systems, the Electronic Customs Data Processing System, or the VID EDS[^s25] | Under Union Customs Code Article 5, the customs administration of Latvia is the State Revenue Service[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | SAIS is the state information system holding social insurance data used to record insured persons and to grant and pay benefits and pensions[^s26] | The controller of SAIS is the Agency (State Social Insurance Agency)[^s26] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | VIIS includes the student and graduate registers and the register of recognition statements for foreign qualifications[^s27] | The controller of VIIS is the Ministry of Education and Science[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Surveillance data are received and processed in the EPID system, including data from the Latvian Digital Health Centre's systems[^s28] | SPKC keeps the records of infectious diseases and laboratory-confirmed pathogens[^s28] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | The base geospatial data include administrative boundaries and the geospatial information of the State Address Register[^s29] | Geospatial Information Law: LĢIA, under the Ministry of Defence, implements state policy in geodesy, cartography and geospatial information[^s29] | *Not stated in sources* | *Not yet measured* |

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

> Not yet sized. Capacity for Latvia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Latvia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Facial biometric (tier 0)
- Fingerprint biometric (tier 0)
- Authentication audit log (tier 0)
- State PKI and qualified trust services (tier 0)
- Statutory health insurance (tier 1)
- Land & property registry (tier 1)
- Business registry (tier 1)
- Beneficial ownership register (tier 1)
- Vehicle & licensing (tier 1)
- Border and visa systems (tier 1)
- Firearms register (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Crisis management and civil protection (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

---

[^s1]: Saeima / Latvijas Vēstnesis (likumi.lv) — Nacionālās kiberdrošības likums (National Cybersecurity…, 2024-07-04. Nacionālās kiberdrošības likums (National Cybersecurity Law), Art. 32. <https://likumi.lv/ta/id/353390> ([archived](https://web.archive.org/web/20260421100217/https://likumi.lv/ta/id/353390))
[^s2]: Ministru kabinets (likumi.lv) — MK noteikumi Nr. 822 (19.12.2023) Valsts noslēpuma,…, 2023-12-19. MK noteikumi Nr. 822 (19.12.2023) Valsts noslēpuma, NATO, ES un ārvalstu institūciju klasificētās informācijas aizsardzības noteikumi, para. 2.1. <https://likumi.lv/ta/id/348742> ([archived](https://web.archive.org/web/20260408194732/https://likumi.lv/ta/id/348742))
[^s3]: Saeima (likumi.lv) — Likums "Par valsts noslēpumu" (Law on State Secrets),…, 1996-10-17. Likums "Par valsts noslēpumu" (Law on State Secrets), Art. 3(1). <https://likumi.lv/ta/id/41058> ([archived](https://web.archive.org/web/20260925033723/https://likumi.lv/ta/id/41058))
[^s4]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — Par mums (About us). Par mums (About us). <https://www.lvrtc.lv/par-lvrtc/par-mums/> ([archived](https://web.archive.org/web/20260807133227/https://www.lvrtc.lv/par-lvrtc/par-mums/))
[^s5]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — eParaksta un e-Identitātes integrācijas risinājumi. eParaksta un e-Identitātes integrācijas risinājumi. <https://www.lvrtc.lv/projekti/eparaksts_identitate/> ([archived](https://web.archive.org/web/20260207134940/https://www.lvrtc.lv/projekti/eparaksts_identitate/))
[^s6]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — eParaksta vēsture (eParaksts history). eParaksta vēsture (eParaksts history). <https://www.lvrtc.lv/par-lvrtc/vesture-2/eparaksta-vesture/> ([archived](https://web.archive.org/web/20260410091905/https://www.lvrtc.lv/par-lvrtc/vesture-2/eparaksta-vesture/))
[^s7]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — Datu centri (Data centres), public sector services. Datu centri (Data centres), public sector services. <https://www.lvrtc.lv/pakalpojumi/valsts_sektoram/datu_centri/> ([archived](https://web.archive.org/web/20260514171247/https://www.lvrtc.lv/pakalpojumi/valsts_sektoram/datu_centri/))
[^s8]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — Latvijas Nacionālais federētais mākonis (Latvian…. Latvijas Nacionālais federētais mākonis (Latvian National Federated Cloud). <https://www.lvrtc.lv/projekti/latvijas-nacionalais-federetais-makonis/> ([archived](https://web.archive.org/web/20260512124930/https://www.lvrtc.lv/projekti/latvijas-nacionalais-federetais-makonis/))
[^s9]: VAS Latvijas Valsts radio un televīzijas centrs (LVRTC) — LVDC – loģiski vienotais datu centrs 2. kārta (Logically…. LVDC – loģiski vienotais datu centrs 2. kārta (Logically unified data centre, phase 2). <https://www.lvrtc.lv/projekti/lvdc-2/> ([archived](https://web.archive.org/web/20260312033831/https://www.lvrtc.lv/projekti/lvdc-2/))
[^s10]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s11]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s12]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s13]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s14]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s15]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Fizisko personu reģistra likums. Fizisko personu reģistra likums. <https://likumi.lv/ta/id/296185> ([archived](https://web.archive.org/web/20260920214621/https://likumi.lv/ta/id/296185))
[^s16]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Civilstāvokļa aktu reģistrācijas likums. Civilstāvokļa aktu reģistrācijas likums. <https://likumi.lv/ta/id/253442> ([archived](https://web.archive.org/web/20260907140710/https://likumi.lv/ta/id/253442))
[^s17]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Personu apliecinošu dokumentu likums. Personu apliecinošu dokumentu likums. <https://likumi.lv/ta/id/243484> ([archived](https://web.archive.org/web/20260921064509/https://likumi.lv/ta/id/243484))
[^s18]: Aizsardzības ministrija — Elektroniskā identifikācija. Elektroniskā identifikācija. <https://www.mod.gov.lv/lv/kiberdrosiba/digitalas-drosibas-uzraudzibas-komiteja/elektroniska-identifikacija>
[^s19]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Vēlētāju reģistra likums. Vēlētāju reģistra likums. <https://likumi.lv/ta/id/83681> ([archived](https://web.archive.org/web/20250623071345/https://likumi.lv/ta/id/83681))
[^s20]: Ministru kabinets / Likumi.lv — Tiesu informatīvās sistēmas noteikumi. Tiesu informatīvās sistēmas noteikumi. <https://likumi.lv/ta/id/284905>
[^s21]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Sodu reģistra likums. Sodu reģistra likums. <https://likumi.lv/ta/id/261384> ([archived](https://web.archive.org/web/20260823151729/https://likumi.lv/ta/id/261384))
[^s22]: Ministru kabinets / Likumi.lv — Noteikumi par integrētajā iekšlietu informācijas sistēmā…. Noteikumi par integrētajā iekšlietu informācijas sistēmā iekļaujamām ziņām personas, mantas vai dokumenta atrašanās vietas vai cilvēka personības noskaidrošanai vai neatpazīta cilvēka līķa identificēšanai. <https://likumi.lv/ta/id/312122> ([archived](https://web.archive.org/web/20241104215536/https://likumi.lv/ta/id/312122))
[^s23]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Patvēruma likums. Patvēruma likums. <https://likumi.lv/ta/id/278986> ([archived](https://web.archive.org/web/20250624200825/https://likumi.lv/ta/id/278986))
[^s24]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Par nodokļiem un nodevām. Par nodokļiem un nodevām. <https://likumi.lv/ta/id/33946> ([archived](https://web.archive.org/web/20260312042603/https://likumi.lv/ta/id/33946))
[^s25]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Muitas likums. Muitas likums. <https://likumi.lv/ta/id/283024> ([archived](https://web.archive.org/web/20260210002446/https://likumi.lv/ta/id/283024))
[^s26]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Par valsts sociālo apdrošināšanu. Par valsts sociālo apdrošināšanu. <https://likumi.lv/ta/id/45466> ([archived](https://web.archive.org/web/20260308035439/https://likumi.lv/ta/id/45466))
[^s27]: Ministru kabinets / Likumi.lv — Valsts izglītības informācijas sistēmas noteikumi. Valsts izglītības informācijas sistēmas noteikumi. <https://likumi.lv/ta/id/307796> ([archived](https://web.archive.org/web/20250614053013/https://likumi.lv/ta/id/307796))
[^s28]: Ministru kabinets / Likumi.lv — Infekcijas slimību reģistrācijas kārtība. Infekcijas slimību reģistrācijas kārtība. <https://likumi.lv/ta/id/20667> ([archived](https://web.archive.org/web/20260315234430/https://likumi.lv/ta/id/20667))
[^s29]: Saeima / Likumi.lv (VSIA Latvijas Vēstnesis) — Ģeotelpiskās informācijas likums. Ģeotelpiskās informācijas likums. <https://likumi.lv/ta/id/202999>

**Evidence grades:** 2 Strong, 35 Standard. Strong: an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review. Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.
