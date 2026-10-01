# Slovenia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Slovenia could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3][^s4] |
| State-controlled national eID | Yes[^s3][^s5][^s6][^s4] |
| Government data centres | Yes[^s7] |
| Government cloud in operation | Yes[^s8][^s9][^s10] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 27 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Slovenia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 2.13 million[^s11] |
| GDP, current prices | 71.2 EUR bn[^s12] |
| Public administration employment (NACE O) | 51.1 thousand[^s13] |
| Non-household electricity price | 150.3 EUR/MWh[^s14] |
| Renewables share of electricity | 45.6 %[^s15] |
| Land area | 20 145 km²[^s16] |

## 3. Critical data holdings, by priority

The holdings Slovenia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 30 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | The Central Population Register (CRP) is the central database of basic population data for Slovenia[^s17][^s18] | CRP is managed by the Ministry of the Interior[^s17][^s18] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | The ID card issuance register stores the digital photograph, but in a form that biometric readers cannot read[^s19] | The interior ministry manages the ID card issuance register centrally[^s19] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s19] | — | — | — |
| Critical | Breeder document scans (tier 0) | The collection of documents underlying civil status entries is part of the civil status register[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | The register records production and delivery dates and the validity status of each ID card[^s19] | The interior ministry manages the ID card issuance register centrally[^s19] | *Not stated in sources* | *Not yet measured* |
| High | Authentication audit log (tier 0) | SI-PASS keeps registered-user records including account usage data[^s21] | Controller: Ministry of the Interior and Public Administration, SI-TRUST[^s21] | National infrastructure[^s21] | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Voting rights are recorded in the register of voting rights, kept within the permanent-residence register and CRP[^s22][^s18] | *Not yet sourced* | *Not stated in sources* | 1.695.249 voters entered in the electoral rolls[^s23] |
| High | Land & property registry (tier 1) | The Land Register is a public book of rights in real property, kept by the district courts[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | Police records include criminal offences, misdemeanours and wanted persons[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | SI-PASS is the single identity-verification and e-signature service for citizens, businesses and civil servants[^s3][^s5] | SI-TRUST operates within the Ministry of the Interior and Public Administration[^s4] | National infrastructure[^s21] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | SI-TRUST manages the SI-TRUST Root and the qualified issuers SIGEN-CA and SIGOV-CA[^s3][^s4] | SI-TRUST operates within the Ministry of the Interior and Public Administration[^s3][^s4] | National infrastructure[^s5] | *Not yet measured* |
| High | Residence and migration status (tier 1) | The interior ministry manages the central register of residence permits and their revocations (Register tujcev)[^s18][^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | The tax register is a single computerised, linked database of taxpayers[^s27] | Under the Financial Administration Act (ZFU), FURS keeps and manages the tax register[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | FURS runs the SIAIS2 import declaration system; a centralised-clearance upgrade was ordered in 2024[^s28] | *Not yet sourced* | *Not stated in sources* | 1.146.962 customs declarations accepted in 2025[^s29] |
| High | Benefits & pensions (tier 1) | matična evidenca o zavarovancih in uživalcih pravic (master record of insured persons and beneficiaries)[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | ZZZS keeps the register of persons covered by compulsory health insurance[^s31] | *Not yet sourced* | *Not stated in sources* | About 2.1 million insured persons (2025)[^s32] |
| High | Business registry (tier 1) | Poslovni register Slovenije (PRS) (Slovenian Business Register)[^s33] | AJPES[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | The RDL is a database of beneficial owners, kept for ownership transparency and AML purposes[^s34][^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | SIS consists of a central system and national SIS systems in the member states, linked by a network[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | UJP provides payment services to budget users and keeps the register of budget users and their sub-accounts[^s37][^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | TARGET services settle large-value payments, securities transactions and instant payments[^s39][^s40] | *Not yet sourced* | EU provider[^s39][^s40] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Regional notification centres receive and process 112 emergency calls[^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | NCKU provides premises, IT and telecom conditions for the government in crises threatening national security[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | ELES ensures safe, reliable and efficient operation of the transmission and distribution system[^s43] | Under ZOEE, ELES performs the mandatory public service of combined transmission and distribution system operator[^s44][^s43] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | The register is kept in the application 'Centralna evidenca udeležencev vzgoje in izobraževanja'[^s45] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Firearms register (tier 1) | The central register of issued firearms documents combines the registers kept by the competent bodies[^s46] | *Not yet sourced* | National infrastructure[^s46] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Pravni informacijski sistem Republike Slovenije (PISRS) (Legal Information System of the Republic of Slovenia), sole publication platform of the Uradni list RS[^s47] | Služba Vlade Republike Slovenije za zakonodajo (Government Legislation Office)[^s47] | *Not stated in sources* | *Not yet measured* |
| Standard | Government payroll and personnel (tier 1) | MFERAC supports budget users in finance, accounting and payroll/HR[^s48][^s49] | *Not yet sourced* | National infrastructure[^s49] | *Not yet measured* |
| Standard | Health records (tier 2) | CRPP is the single system for collecting and exchanging health data on patients in Slovenia[^s50] | NIJZ is responsible for the CeZZ information system, its maintenance and security[^s51] | National infrastructure[^s51] | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | e-ARH.si is the Slovenian electronic archive for long-term preservation of electronic archival records[^s52] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 29 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 6 |
| EU provider | 1 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 22 |

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

> Not yet sized. Capacity for Slovenia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Slovenia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Vehicle & licensing (tier 1)
- Judicial & criminal justice (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Water management control (tier 1)

---

[^s1]: Urad Vlade Republike Slovenije za varovanje tajnih podatkov — Tajni podatki, 2026-03-26. Tajni podatki. <https://www.gov.si/teme/tajni-podatki/> ([archived](https://web.archive.org/web/20260518182748/https://www.gov.si/teme/tajni-podatki/))
[^s2]: Uradni list Republike Slovenije — Zakon o tajnih podatkih (uradno prečiščeno besedilo)…, 2006-05-16. Zakon o tajnih podatkih (uradno prečiščeno besedilo) (ZTP-UPB2), 13. člen. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2006-01-2128/zakon-o-tajnih-podatkih-uradno-precisceno-besedilo-ztp-upb2>
[^s3]: Ministrstvo za notranje zadeve und javno upravo — Sektor za storitve zaupanja, 2026-08-10. Sektor za storitve zaupanja. <https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-notranje-zadeve-in-javno-upravo/o-ministrstvu/direktorat-za-informatiko/urad-za-razvoj-digitalnih-resitev/sektor-za-storitve-zaupanja/>
[^s4]: SI-TRUST / Državni center za storitve zaupanja — O nas - SI-TRUST. O nas - SI-TRUST. <https://www.si-trust.gov.si/sl/o-nas> ([archived](https://web.archive.org/web/20260727081457/https://www.si-trust.gov.si/sl/o-nas))
[^s5]: SI-TRUST / Državni center za storitve zaupanja — Spletna prijava in e-podpis (SI-PASS). Spletna prijava in e-podpis (SI-PASS). <https://www.si-trust.gov.si/sl/si-pass> ([archived](https://web.archive.org/web/20260727081439/https://www.si-trust.gov.si/sl/si-pass))
[^s6]: SI-TRUST / Državni center za storitve zaupanja — Elektronska osebna izkaznica. Elektronska osebna izkaznica. <https://www.si-trust.gov.si/sl/eoi> ([archived](https://web.archive.org/web/20260615134158/https://www.si-trust.gov.si/sl/eoi))
[^s7]: Ministrstvo za notranje zadeve in javno upravo (GOV.SI) — Sektor za podatkovno in strežniško infrastrukturo. Sektor za podatkovno in strežniško infrastrukturo. <https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-notranje-zadeve-in-javno-upravo/o-ministrstvu/direktorat-za-informatiko/urad-za-digitalno-infrastrukturo/sektor-za-podatkovno-in-streznisko-infrastrukturo/>
[^s8]: Ministrstvo za javno upravo — Vzdrževanje državnega računalniškega oblaka (DRO - VMware), 2026-03-25. Vzdrževanje državnega računalniškega oblaka (DRO - VMware). <https://www.gov.si/zbirke/javne-objave/vzdrzevanje-drzavnega-racunalniskega-oblaka-dro-vmware-260317002023/>
[^s9]: Ministrstvo za notranje zadeve in javno upravo (GOV.SI) — Sektor za virtualizacijo in orkestracijo. Sektor za virtualizacijo in orkestracijo. <https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-notranje-zadeve-in-javno-upravo/o-ministrstvu/direktorat-za-informatiko/urad-za-digitalno-infrastrukturo/sektor-za-virt/>
[^s10]: Ministrstvo za notranje zadeve in javno upravo (GOV.SI) — Informatika v državni upravi, 2026-08-20. Informatika v državni upravi. <https://www.gov.si/teme/informatika-v-drzavni-upravi/>
[^s11]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s12]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s13]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s14]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s15]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s16]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s17]: Ministrstvo za notranje zadeve (CRP portal) — Predstavitev CRP - CRP portal. Predstavitev CRP - CRP portal. <https://ecrp.gov.si/predstavitevCRP.html> ([archived](https://web.archive.org/web/20250527084027/https://ecrp.gov.si/predstavitevCRP.html))
[^s18]: Ministrstvo za notranje zadeve in javno upravo — Registri in evidence prebivalstva, 2026-08-17. Registri in evidence prebivalstva. <https://www.gov.si/teme/registri-in-evidence-prebivalstva/> ([archived](https://web.archive.org/web/20260314092109/https://www.gov.si/teme/registri-in-evidence-prebivalstva/))
[^s19]: Uradni list Republike Slovenije — Zakon o spremembah in dopolnitvah Zakona o osebni…, 2025-03-18. Zakon o spremembah in dopolnitvah Zakona o osebni izkaznici (ZOIzk-1C), Uradni list RS, št. 17/2025. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2025-01-0584> ([archived](https://web.archive.org/web/20260510231526/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2025-01-0584))
[^s20]: Uradni list Republike Slovenije — Zakon o matičnem registru (uradno prečiščeno besedilo)…, 2011-02-21. Zakon o matičnem registru (uradno prečiščeno besedilo) (ZMatR-UPB2), Uradni list RS, št. 11/2011. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2011-01-0451> ([archived](https://web.archive.org/web/20231115081008/http://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2011-01-0451))
[^s21]: SI-TRUST / Ministrstvo za notranje zadeve in javno upravo — Obvestilo posameznikom glede obdelave osebnih podatkov…. Obvestilo posameznikom glede obdelave osebnih podatkov storitve SI-PASS. <https://www.si-trust.gov.si/sl/si-pass-obvestilo-posameznikom>
[^s22]: GOV.SI (Ministrstvo za notranje zadeve) — Volivci in evidenca volilne pravice. Volivci in evidenca volilne pravice. <https://www.gov.si/teme/volivci-in-evidenca-volilne-pravice/> ([archived](https://web.archive.org/web/20260518161634/https://www.gov.si/teme/volivci-in-evidenca-volilne-pravice/))
[^s23]: Državna volilna komisija — Volitve v Državni zbor 2026, 2026. Volitve v Državni zbor 2026. <https://www.dvk-rs.si/volitve-in-referendumi/drzavni-zbor-rs/volitve-drzavnega-zbora-rs/volitve-v-drzavni-zbor/> ([archived](https://web.archive.org/web/20260728104354/https://www.dvk-rs.si/volitve-in-referendumi/drzavni-zbor-rs/volitve-drzavnega-zbora-rs/volitve-v-drzavni-zbor/))
[^s24]: Sodstvo Republike Slovenije — Zemljiška knjiga - javne knjige. Zemljiška knjiga - javne knjige. <https://www.sodisce.si/javne_knjige/zemljiska_knjiga/> ([archived](https://web.archive.org/web/20260720094305/https://www.sodisce.si/javne_knjige/zemljiska_knjiga/))
[^s25]: Uradni list Republike Slovenije — Zakon o nalogah in pooblastilih policije (ZNPPol),…, 2013-02-18. Zakon o nalogah in pooblastilih policije (ZNPPol), Uradni list RS, št. 15/2013. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2013-01-0435/> ([archived](https://web.archive.org/web/20260119082921/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2013-01-0435/))
[^s26]: Uradni list Republike Slovenije — Zakon o tujcih (uradno prečiščeno besedilo)…, 2021-06-07. Zakon o tujcih (uradno prečiščeno besedilo) (ZTuj-2-UPB9), Uradni list RS, št. 91/2021. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2021-01-1957> ([archived](https://web.archive.org/web/20260216110731/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2021-01-1957/))
[^s27]: Finančna uprava Republike Slovenije — Vpis v davčni register in davčna številka. Vpis v davčni register in davčna številka. <https://www.fu.gov.si/davki_in_druge_dajatve/poslovanje_z_nami/vpis_v_davcni_register_in_davcna_stevilka/> ([archived](https://web.archive.org/web/20260520064339/https://www.fu.gov.si/davki_in_druge_dajatve/poslovanje_z_nami/vpis_v_davcni_register_in_davcna_stevilka/))
[^s28]: Finančna uprava Republike Slovenije — Letno poročilo Finančne uprave za leto 2024, 2025. Letno poročilo Finančne uprave za leto 2024. <https://www.gov.si/assets/organi-v-sestavi/FURS/Strateski-dokumenti/2025/Letno-porocilo-Financne-uprave-za-leto-2024.pdf> ([archived](https://web.archive.org/web/20260916213111/https://www.gov.si/assets/organi-v-sestavi/FURS/Strateski-dokumenti/2025/Letno-porocilo-Financne-uprave-za-leto-2024.pdf))
[^s29]: Finančna uprava Republike Slovenije — Letno poročilo Finančne uprave za leto 2025, 2026-02. Letno poročilo Finančne uprave za leto 2025. <https://www.gov.si/assets/organi-v-sestavi/FURS/Strateski-dokumenti/2026/Letno-porocilo-Financne-uprave-za-leto-2025.pdf>
[^s30]: Zavod za pokojninsko in invalidsko zavarovanje Slovenije (ZPIZ) — O zavodu. O zavodu. <https://www.zpiz.si/cms/?ids=content2019&inf=1191> ([archived](https://web.archive.org/web/20260710194720/https://www.zpiz.si/cms/?ids=content2019&inf=1191))
[^s31]: Zavod za zdravstveno zavarovanje Slovenije — Evidenca o zavarovanih osebah (katalog zbirke). Evidenca o zavarovanih osebah (katalog zbirke). <https://www.zzzs.si/fileadmin/user_upload/dokumenti/informacije_in_publikacije/evidenca_o_zavarovanih_osebah.pdf> ([archived](https://web.archive.org/web/20240802165003/https://www.zzzs.si/fileadmin/user_upload/dokumenti/informacije_in_publikacije/evidenca_o_zavarovanih_osebah.pdf))
[^s32]: Zavod za zdravstveno zavarovanje Slovenije — Poslovanje ZZZS v letu 2025, 2026. Poslovanje ZZZS v letu 2025. <https://zavezanec.zzzs.si/fileadmin/user_upload/dokumenti/novice/2026/zzzsporocilo2025-infografika-web.pdf>
[^s33]: AJPES — Poslovni register Slovenije – Splošno. Poslovni register Slovenije – Splošno. <https://www.ajpes.si/registri/poslovni_register/splosno> ([archived](https://web.archive.org/web/20260912024435/https://www.ajpes.si/registri/poslovni_register/splosno))
[^s34]: AJPES — Register dejanskih lastnikov - Splošno. Register dejanskih lastnikov - Splošno. <https://www.ajpes.si/registri/drugi_registri/register_dejanskih_lastnikov/splosno>
[^s35]: Finančna uprava Republike Slovenije — Preverite vpis v register dejanskih lastnikov, 2026-09-24. Preverite vpis v register dejanskih lastnikov. <https://www.gov.si/novice/2026-09-24-preverite-vpis-v-register-dejanskih-lastnikov/>
[^s36]: GOV.SI (Ministrstvo za notranje zadeve) — Prenovljeni Schengenski informacijski sistem, 2023-03-08. Prenovljeni Schengenski informacijski sistem. <https://www.gov.si/novice/2023-03-08-prenovljeni-schengenski-informacijski-sistem/> ([archived](https://web.archive.org/web/20230604005507/https://www.gov.si/novice/2023-03-08-prenovljeni-schengenski-informacijski-sistem/))
[^s37]: Uprava Republike Slovenije za javna plačila — Register proračunskih uporabnikov, 2026-04-13. Register proračunskih uporabnikov. <https://www.gov.si/teme/register-proracunskih-uporabnikov/> ([archived](https://web.archive.org/web/20251208071415/https://www.gov.si/teme/register-proracunskih-uporabnikov/))
[^s38]: GOV.SI (Uprava RS za javna plačila) — O Upravi Republike Slovenije za javna plačila. O Upravi Republike Slovenije za javna plačila. <https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-javna-placila/o-upravi/> ([archived](https://web.archive.org/web/20260517120748/https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-javna-placila/o-upravi/))
[^s39]: European Central Bank — TARGET Services. TARGET Services. <https://www.ecb.europa.eu/paym/target/html/index.en.html> ([archived](https://web.archive.org/web/20260917182025/https://www.ecb.europa.eu/paym/target/html/index.en.html))
[^s40]: Banka Slovenije — Plačilna infrastruktura. Plačilna infrastruktura. <https://www.bsi.si/sl/placilni-sistemi/placilna-infrastruktura>
[^s41]: GOV.SI (Uprava RS za zaščito in reševanje) — Urad za obveščanje in alarmiranje. Urad za obveščanje in alarmiranje. <https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/o-upravi/urad-za-obvescanje-in-alarmiranje/> ([archived](https://web.archive.org/web/20260323061511/https://www.gov.si/drzavni-organi/organi-v-sestavi/uprava-za-zascito-in-resevanje/o-upravi/urad-za-obvescanje-in-alarmiranje/))
[^s42]: GOV.SI (Ministrstvo za obrambo) — Nacionalni center za krizno upravljanje. Nacionalni center za krizno upravljanje. <https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-obrambo/o-ministrstvu/direktorat-za-obrambne-zadeve/nacionalni-center-za-krizno-upravljanje/> ([archived](https://web.archive.org/web/20250727032849/https://www.gov.si/drzavni-organi/ministrstva/ministrstvo-za-obrambo/o-ministrstvu/direktorat-za-obrambne-zadeve/nacionalni-center-za-krizno-upravljanje/))
[^s43]: Portal Energetika (ministry responsible for energy) — ELES, d.o.o. sistemski operater prenosnega…. ELES, d.o.o. sistemski operater prenosnega elektroenergetskega omrežja. <https://www.energetika-portal.si/podrocja/energetika/upravljanje-kapitalskih-nalozb/eles/> ([archived](https://web.archive.org/web/20250516111733/https://www.energetika-portal.si/podrocja/energetika/upravljanje-kapitalskih-nalozb/eles/))
[^s44]: ELES, d. o. o. — ELES, d. o. o.. ELES, d. o. o.. <https://www.eles.si/>
[^s45]: Uradni list Republike Slovenije — Pravilnik o načinu in pogojih dostopa do podatkov iz…, 2011-06-03. Pravilnik o načinu in pogojih dostopa do podatkov iz centralne evidence udeležencev vzgoje in izobraževanja, Uradni list RS, št. 43/2011. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2011-01-2099> ([archived](https://web.archive.org/web/20240504214009/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2011-01-2099))
[^s46]: Uradni list Republike Slovenije — Zakon o orožju (ZOro-1), Uradni list RS, št. 61/2000, 2000-07-06. Zakon o orožju (ZOro-1), Uradni list RS, št. 61/2000. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2000-01-2747/zakon-o-orozju-zoro-1> ([archived](https://web.archive.org/web/20210924055842/https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2000-01-2747/zakon-o-orozju-zoro-1))
[^s47]: Uradni list Republike Slovenije — O glasilu, 2026. O glasilu. <https://www.uradni-list.si/glasilo-uradni-list-rs/glasilo-uradni-list-rs/o-glasilu> ([archived](https://web.archive.org/web/20260608175302/https://www.uradni-list.si/glasilo-uradni-list-rs/glasilo-uradni-list-rs/o-glasilu))
[^s48]: GOV.SI (Ministrstvo za finance) — Sistem MFERAC. Sistem MFERAC. <https://www.gov.si/zbirke/storitve/mferac/>
[^s49]: Ministrstvo za finance — Prenova MFERAC, 2024-01-24. Prenova MFERAC. <https://www.gov.si/zbirke/projekti-in-programi/prenova-mferac/> ([archived](https://web.archive.org/web/20260216201728/https://www.gov.si/zbirke/projekti-in-programi/prenova-mferac/))
[^s50]: eZdravje (NIJZ) — CRPP - eZdravje. CRPP - eZdravje. <https://ezdrav.si/resitve/crpp/> ([archived](https://web.archive.org/web/20251015032134/https://ezdrav.si/resitve/crpp/))
[^s51]: Uradni list Republike Slovenije — Zakon o digitalizaciji zdravstva (ZDigZ), Uradni list…, 2025-12-04. Zakon o digitalizaciji zdravstva (ZDigZ), Uradni list RS, št. 100/2025. <https://www.uradni-list.si/glasilo-uradni-list-rs/vsebina/2025-01-3387>
[^s52]: GOV.SI — Slovenski elektronski arhiv. Slovenski elektronski arhiv. <https://www.gov.si/teme/slovenski-elektronski-arhiv/> ([archived](https://web.archive.org/web/20260612043003/https://www.gov.si/teme/slovenski-elektronski-arhiv/))

**Evidence grades:** 5 Strong, 57 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
