# Estonia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Estonia could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1][^s2][^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Partly[^s4] |
| State-controlled national eID | Yes[^s5] |
| Government data centres | Yes[^s6][^s7][^s8][^s9] |
| Government cloud in operation | Yes[^s6][^s10][^s11][^s12][^s13] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Estonia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 1.36 million[^s14] |
| GDP, current prices | 41.9 EUR bn[^s15] |
| Public administration employment (NACE O) | 43.1 thousand[^s16] |
| Non-household electricity price | 141.0 EUR/MWh[^s17] |
| Renewables share of electricity | 41.1 %[^s18] |
| Land area | 43 110 km²[^s19] |

## 3. Critical data holdings, by priority

The holdings Estonia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 26 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Rahvastikuregister (Population Register)[^s20] | Siseministeerium (Ministry of the Interior)[^s20] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Biometric data under the Identity Documents Act are facial image, fingerprints, signature and iris images[^s21][^s22] | ABIS controllers are the Police and Border Guard Board and the Ministry of Foreign Affairs[^s22][^s23] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | ABIS (automaatse biomeetrilise isikutuvastuse süsteemi andmekogu; Automated Biometric Identification System database)[^s21] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s23] | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | Riigi autentimisteenus (State Authentication Service, TARA)[^s24] | RIA (Riigi Infosüsteemi Amet; Information System Authority)[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Isikut tõendavate dokumentide andmekogu (Identity Documents Database)[^s25] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s25] | *Not stated in sources* | over 3,2 miljoni isikutunnistuse ja elamisloakaardi (over 3.2 million ID cards and residence permit cards issued)[^s26] |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | Valijate nimekiri (list of voters), compiled from the Rahvastikuregister (Population Register)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | E-kinnistusraamat (e-Land Register)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Karistusregister (Criminal Records Database)[^s29] | Justiits- ja Digiministeerium (Ministry of Justice and Digital Affairs); processor Registrite ja Infosüsteemide Keskus (RIK)[^s30] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Infosüsteem POLIS (Information System POLIS)[^s31] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | elamislubade ja töölubade register (Register of Residence Permits and Work Permits)[^s32] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Maksukohustuslaste register (Register of Taxable Persons)[^s33] | Maksu- ja Tolliamet (Tax and Customs Board)[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | Impulss (import customs clearance information system)[^s34] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | sotsiaalkaitse infosüsteem (Social Security Information System, SKAIS)[^s35] | Sotsiaalkindlustusamet (Social Insurance Board)[^s35] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Tervisekassa andmekogu (Health Insurance Fund Database)[^s36] | Tervisekassa (Health Insurance Fund)[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | E-äriregister (e-Business Register)[^s37] | Tartu Maakohtu registriosakond (registrar); RIK (develops and manages the portal)[^s37] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Tegelike kasusaajate andmekogu (Beneficial Owners Database)[^s38] | Rahandusministeerium (Ministry of Finance)[^s38] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | Schengeni infosüsteemi riiklik register (national register of the Schengen Information System)[^s39] | Politsei- ja Piirivalveamet (Police and Border Guard Board)[^s39] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | teenistus- ja tsiviilrelvade register (Register of Service and Civilian Weapons)[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | riigi finants-, personali- ja palgaarvestuse süsteem SAP (state financial, personnel and payroll accounting system SAP)[^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | riigi finants-, personali- ja palgaarvestuse süsteem SAP (state financial, personnel and payroll accounting system SAP)[^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | valimiste infosüsteem (election information system) and elektroonilise hääletamise süsteem (electronic voting system)[^s27] | Riigi valimisteenistus (State Electoral Office)[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | hädaabiteadete ning abi- ja infoteadete andmekogu (database of emergency notifications and assistance and information notifications)[^s42] | Häirekeskus (Emergency Response Centre)[^s42] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | ohuteavituse süsteem (public warning system, EE-ALARM), operated by Häirekeskus[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | SCADA/EMS at Eleringi juhtimiskeskus (Elering control centre)[^s43] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Eesti Hariduse Infosüsteem (EHIS; Estonian Education Information System)[^s44] | Haridus- ja Teadusministeerium (Ministry of Education and Research)[^s45] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Riigi Teataja (State Gazette)[^s46] | Justiits- ja Digiministeerium (publisher); Registrite ja Infosüsteemide Keskus (RIK) (hosting and technical operation)[^s46] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

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

> Not yet sized. Capacity for Estonia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Estonia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Breeder document scans (tier 0)
- Digital identity credentials (tier 0)
- State PKI and qualified trust services (tier 0)
- Vehicle & licensing (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Water management control (tier 1)

---

[^s1]: Välisluureamet – Estonian National Security Authority — Korduma kippuvad küsimused (Riigi julgeoleku volitatud…. Korduma kippuvad küsimused (Riigi julgeoleku volitatud esindaja). <https://www.teabeamet.ee/nsa/kkk.html>
[^s2]: Välisluureamet – Estonian National Security Authority — Võrdlustabelid. Võrdlustabelid. <https://www.teabeamet.ee/nsa/tabelid.html>
[^s3]: Riigi Teataja — Riigisaladuse ja salastatud välisteabe seadus…, 2026-01-17. Riigisaladuse ja salastatud välisteabe seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260117004320/https://www.riigiteataja.ee/akt/RSVS>
[^s4]: Riigi Infosüsteemi Amet (Information System Authority) — Electronic identity (eID). Electronic identity (eID). <https://www.ria.ee/en/state-information-system/electronic-identity-eid-and-trust-services/electronic-identity-eid> ([archived](https://web.archive.org/web/20260915103115/https://www.ria.ee/en/state-information-system/electronic-identity-eid-and-trust-services/electronic-identity-eid))
[^s5]: Riigi Infosüsteemi Amet (Information System Authority) — Estonian electronic identity ecosystem – Overview,…, 2025-10. Estonian electronic identity ecosystem – Overview, Version 1.0. <https://www.ria.ee/sites/default/files/documents/2025-10/Estonian-eID-ecosystem.pdf> ([archived](https://web.archive.org/web/20251023190958/https://www.ria.ee/sites/default/files/documents/2025-10/Estonian-eID-ecosystem.pdf))
[^s6]: Riigikontroll (National Audit Office of Estonia) — Eesti riigi kriitiliste andmekogude turvalisuse ja…, 2018-05-14. Eesti riigi kriitiliste andmekogude turvalisuse ja säilitamise tagamine. <https://www.riigikontroll.ee/sites/default/files/arhivaalid/2462/RKTR_2462_2-1.4_2213_001-2.pdf>
[^s7]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) – Riigipilv — Riigipilve tehniline lahendus. Riigipilve tehniline lahendus. <https://www.riigipilv.ee/riigipilvest/riigipilve-tehniline-lahendus>
[^s8]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) – Riigipilv — Mis saab Riigipilvest eriolukorras?. Mis saab Riigipilvest eriolukorras?. <https://www.riigipilv.ee/riigipilvest/riigipilvest-kkk/mis-saab-riigipilvest-eriolukorras>
[^s9]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) — Serverteenused ja Riigipilv. Serverteenused ja Riigipilv. <https://www.rit.ee/serverteenused> ([archived](https://web.archive.org/web/20260612050140/https://www.rit.ee/serverteenused))
[^s10]: Eesti Riigipilv / RIT — Riigipilv — mis see on?. Riigipilv — mis see on?. <https://www.riigipilv.ee/riigipilvest/riigipilvest-kkk/riigipilv-mis-see-on> ([archived](https://web.archive.org/web/20260414213340/https://www.riigipilv.ee/riigipilvest/riigipilvest-kkk/riigipilv-mis-see-on))
[^s11]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) – Riigipilv — Eesti Riigipilv. Eesti Riigipilv. <https://www.riigipilv.ee/et>
[^s12]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) – Riigipilv — Tellijad. Tellijad. <https://www.riigipilv.ee/riigipilvest/kliendid> ([archived](https://web.archive.org/web/20260510204636/https://www.riigipilv.ee/riigipilvest/kliendid))
[^s13]: Riigi Info- ja Kommunikatsioonitehnoloogia Keskus (RIT) — Uuendatud riigipilv – Eesti avaliku sektori pilvteenus…, 2025-01-09. Uuendatud riigipilv – Eesti avaliku sektori pilvteenus on senisest võimsam ja turvalisem. <https://www.rit.ee/uudised/uuendatud-riigipilv-eesti-avaliku-sektori-pilvteenus-senisest-voimsam-ja-turvalisem>
[^s14]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s15]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s16]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s17]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s18]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s19]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s20]: Siseministeerium (Ministry of the Interior) — Rahvastikuregister. Rahvastikuregister. <https://www.siseministeerium.ee/tegevusvaldkonnad/rahvastikutoimingud/rahvastikuregister>
[^s21]: Siseministeerium (Ministry of the Interior) — Automaatse biomeetrilise isikutuvastuse süsteemi…. Automaatse biomeetrilise isikutuvastuse süsteemi andmekogu ABIS. <https://www.siseministeerium.ee/abis> ([archived](https://web.archive.org/web/20260811150453/https://www.siseministeerium.ee/abis))
[^s22]: Riigi Teataja — Isikut tõendavate dokumentide seadus (Internet Archive…, 2026-03-13. Isikut tõendavate dokumentide seadus (Internet Archive copy of Riigi Teataja). <https://web.archive.org/web/20260313205329/https://www.riigiteataja.ee/akt/itds>
[^s23]: Riigi Teataja (Vabariigi Valitsus) — Automaatse biomeetrilise isikutuvastuse süsteemi…, 2026-04-18. Automaatse biomeetrilise isikutuvastuse süsteemi andmekogu põhimäärus. <https://web.archive.org/web/20260418112026/https://www.riigiteataja.ee/akt/131122021018>
[^s24]: Riigi Infosüsteemi Amet (Information System Authority) — Riigi Infosüsteemi Ameti teenustaseme leppe vorm – Riigi…, 2025-02. Riigi Infosüsteemi Ameti teenustaseme leppe vorm – Riigi autentimisteenus (TARA). <https://www.ria.ee/sites/default/files/documents/2025-02/TARA-SLA-Riigi-autentimisteenus-1-3-2025.pdf>
[^s25]: Riigi Teataja — Isikut tõendavate dokumentide seadus (consolidated text,…, 2026-03-09. Isikut tõendavate dokumentide seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260309063502/https://www.riigiteataja.ee/akt/ITDS>
[^s26]: Siseministeerium (Ministry of the Interior) — Isikut tõendavad dokumendid ja identiteedihaldus. Isikut tõendavad dokumendid ja identiteedihaldus. <https://www.siseministeerium.ee/tegevusvaldkonnad/tohus-rahvastikuhaldus/isikut-toendavad-dokumendid-ja-identiteedihaldus> ([archived](https://web.archive.org/web/20260703201829/https://www.siseministeerium.ee/tegevusvaldkonnad/tohus-rahvastikuhaldus/isikut-toendavad-dokumendid-ja-identiteedihaldus))
[^s27]: Riigi Teataja — Riigikogu valimise seadus (consolidated text, Riigi…, 2026-02-18. Riigikogu valimise seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260218005759/https://www.riigiteataja.ee/akt/RKVS>
[^s28]: Registrite ja Infosüsteemide Keskus (RIK) — E-kinnistusraamat. E-kinnistusraamat. <https://www.rik.ee/et/e-kinnistusraamat/e-kinnistusraamat> ([archived](https://web.archive.org/web/20260829055311/https://www.rik.ee/et/e-kinnistusraamat/e-kinnistusraamat))
[^s29]: Registrite ja Infosüsteemide Keskus (RIK) — Päring karistusregistrist. Päring karistusregistrist. <https://www.rik.ee/et/karistusregister/paring-karistusregistrist> ([archived](https://web.archive.org/web/20260902232345/https://www.rik.ee/et/karistusregister/paring-karistusregistrist))
[^s30]: Riigi Teataja — Karistusregistri seadus (consolidated text, Riigi…, 2025-08-03. Karistusregistri seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20250803214052/https://www.riigiteataja.ee/akt/KarRS>
[^s31]: Riigi Teataja — Politsei andmekogu pidamise põhimäärus, 2025-12-12. Politsei andmekogu pidamise põhimäärus. <https://web.archive.org/web/20251212223739/https://www.riigiteataja.ee/akt/113012017004>
[^s32]: Riigi Teataja — Elamislubade ja töölubade registri põhimäärus, 2025-05-14. Elamislubade ja töölubade registri põhimäärus. <https://web.archive.org/web/20250514142132/https://www.riigiteataja.ee/akt/114012017018>
[^s33]: Riigi Teataja — Maksukorralduse seadus (consolidated text, Riigi Teataja…, 2026-02-07. Maksukorralduse seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260207063839/https://www.riigiteataja.ee/akt/MKS>
[^s34]: Maksu- ja Tolliamet (Tax and Customs Board) — MTA võtab kasutusele uue impordi tollivormistuse…, 2021. MTA võtab kasutusele uue impordi tollivormistuse infosüsteemi. <https://www.emta.ee/uudised/mta-votab-kasutusele-uue-impordi-tollivormistuse-infosusteemi>
[^s35]: Riigi Teataja — Sotsiaalkaitse infosüsteemi põhimäärus, 2022-10-24. Sotsiaalkaitse infosüsteemi põhimäärus. <https://web.archive.org/web/20221024144600/https://www.riigiteataja.ee/akt/108052020012>
[^s36]: Riigi Teataja — Tervisekassa andmekogu pidamise põhimäärus, 2024-11-24. Tervisekassa andmekogu pidamise põhimäärus. <https://web.archive.org/web/20241124195714/https://www.riigiteataja.ee/akt/107052024007>
[^s37]: Registrite ja Infosüsteemide Keskus (RIK) — E-äriregistri portaal. E-äriregistri portaal. <https://www.rik.ee/et/e-ariregister/e-ariregistri-portaal> ([archived](https://web.archive.org/web/20260829032113/https://www.rik.ee/et/e-ariregister/e-ariregistri-portaal))
[^s38]: Riigi Teataja — Rahapesu ja terrorismi rahastamise tõkestamise seadus…, 2026-03-06. Rahapesu ja terrorismi rahastamise tõkestamise seadus (consolidated text, Riigi Teataja snapshot). <https://web.archive.org/web/20260306092107/https://www.riigiteataja.ee/akt/RahaPTS>
[^s39]: Riigi Teataja — Schengeni infosüsteemi riikliku registri pidamise põhimäärus, 2025-10-22. Schengeni infosüsteemi riikliku registri pidamise põhimäärus. <https://web.archive.org/web/20251022021813/https://www.riigiteataja.ee/akt/118042013027>
[^s40]: Politsei- ja Piirivalveamet (Police and Border Guard Board) — Avaandmete seletuskiri – Teenistus- ja tsiviilrelvade…, 2020-06-05. Avaandmete seletuskiri – Teenistus- ja tsiviilrelvade register. <https://www.politsei.ee/files/Anal%C3%BC%C3%BCs%20ja%20statistika/ppa-avaandmete-seletuskiri-relvaregister-05.06.20.pdf>
[^s41]: Riigi Tugiteenuste Keskus (State Shared Service Centre) — Riigitöötaja iseteenindusportaal. Riigitöötaja iseteenindusportaal. <https://www.rtk.ee/riigitootaja-iseteenindusportaal> ([archived](https://web.archive.org/web/20260829052208/https://www.rtk.ee/riigitootaja-iseteenindusportaal))
[^s42]: Siseministeerium (Ministry of the Interior) — Riiklik avalikkuse hoiatamise süsteem ja ohuteavitus…, 2024-02-07. Riiklik avalikkuse hoiatamise süsteem ja ohuteavitus Eestis (EE-ALARM ülevaade). <https://www.siseministeerium.ee/sites/default/files/documents/2024-02/EE-ALARM_ylevaade_avalik_07022024.pdf>
[^s43]: Elering AS — Juhtimiskeskus, 2025-05-09. Juhtimiskeskus. <https://www.elering.ee/juhtimiskeskus>
[^s44]: Haridus- ja Teadusministeerium — EHIS - Eesti Hariduse Infosüsteem. EHIS - Eesti Hariduse Infosüsteem. <https://www.ehis.ee/> ([archived](https://web.archive.org/web/20260824092833/https://www.ehis.ee/))
[^s45]: Haridus- ja Teadusministeerium — Eesti keele tasemeeksamiks ettevalmistava…, 2024-07. Eesti keele tasemeeksamiks ettevalmistava täienduskoolituse tegevusloa taotlemise kirjeldus. <https://www.hm.ee/sites/default/files/documents/2024-07/Eesti%20keele%20tasemeeksamiks%20ettevalmistava%20t%C3%A4ienduskoolituse%20tegevusloa%20taotlemise%20kirjeldus.pdf>
[^s46]: Registrite ja Infosüsteemide Keskus (RIK) — Riigi Teataja. Riigi Teataja. <https://www.rik.ee/et/muud-teenused/riigi-teataja> ([archived](https://web.archive.org/web/20260312042839/https://www.rik.ee/et/muud-teenused/riigi-teataja))

**Evidence grades:** 3 Strong, 53 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
