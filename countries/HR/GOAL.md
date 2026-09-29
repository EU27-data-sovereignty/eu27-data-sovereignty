# Croatia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Croatia could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2] |
| Classification in law | Yes[^s3] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s4][^s5] |
| State-controlled national eID | Yes[^s4][^s2] |
| Government data centres | Yes[^s1] |
| Government cloud in operation | Yes[^s1] |

What could move this placement:

- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Croatia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 3.87 million[^s6] |
| GDP, current prices | 93.0 EUR bn[^s7] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 154.8 EUR/MWh[^s8] |
| Renewables share of electricity | 58.0 %[^s9] |
| Land area | 55 896 km²[^s10] |

## 3. Critical data holdings, by priority

The holdings Croatia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 24 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | State civil registers (Državne matice): registers of births, marriages and deaths[^s11] | The state administration body for general administration sets up and runs the single information system for the civil registers[^s11] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Photograph stored in the ID-card register in the Ministry of the Interior information system (reused for driving licences)[^s12] | Competent bodies for biometric collections are the ministries of the interior, foreign affairs and justice[^s13] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Fingerprints already taken and stored electronically in a ministry document-issuance procedure are reused (central retention)[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Files underlying civil-register entries are of permanent value[^s15] | Registers whose last entry is more than 100 years old are kept by the Croatian State Archives[^s11] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | NIAS records credential-usage history, visible to the user for the last 60 days[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | ID-card register kept in the Ministry of the Interior information system, recording invalid (lost) cards[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | ZIS stores and maintains all land-register and cadastre data[^s17] | ZIS is jointly coordinated by the Ministry of Justice and the State Geodetic Administration[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | The Ministry information system is the Information System of the Ministry of the Interior[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | AKD HRIDCA issues identification and qualified signature certificates for the eOI card[^s20] | Fina is a qualified trust service provider on the national trusted list[^s21] | National infrastructure[^s20] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Collection covers third-country nationals on short-term, temporary, long-term and permanent stay[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | Main books are linked into a single database for Croatia[^s23] | The register is kept by the commercial courts and preserved permanently[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Central electronic database of beneficial owners of legal entities and trusts[^s24] | Operationally run by Fina on behalf of the Anti-Money Laundering Office, Ministry of Finance[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Register of registered vehicles kept on the Ministry of the Interior information system[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | National information system for state border management, part of the MUP information system[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | All budget-user transactions go through the State Treasury system and the single treasury account held at HNB[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | The COP payroll information system is owned by the Republic of Croatia[^s28] | Fina processes the data on behalf of the civil-service body[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | Payments in Croatia run through TARGET-HR, EuroNCS and EuroNCSInst[^s29] | *Not yet sourced* | EU provider[^s30] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | System 112 consists of interconnected 112 centres and the Operational Centre of Civil Protection[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | National Operational Centre of Civil Protection monitors events through the 112 centres[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Central register of higher-education certificates, diplomas and supplements (Digital Register of Diplomas)[^s32] | e-Matica is a centralised MZOM system; CARNET is the support centre[^s33] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | CEZIH is the central store of health data for primary, secondary and tertiary care[^s34] | HZZO manages CEZIH and maintains its central part[^s34] | *Not stated in sources* | *Not yet measured* |
| Standard | Tax (tier 1) | Information system of the Tax Administration[^s35] | *Not yet sourced* | National infrastructure[^s36] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | NAJS stores health data and public-health records and registers[^s34] | NAJS is run by HZJZ[^s34] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | Building register established, kept and maintained by DGU[^s37] | DGU establishes and keeps the spatial units register[^s37] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 24 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 1 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 21 |

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

> Not yet sized. Capacity for Croatia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Croatia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Digital identity credentials (tier 0)
- Electoral roll entry (tier 0)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Judicial & criminal justice (tier 1)
- Firearms register (tier 1)
- Official gazette and legislation (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

---

[^s1]: Ministarstvo pravosuđa, uprave i digitalne transformacije 5df8638476. Centar dijeljenih usluga (CDU) – državni oblak koji pokreće digitalnu Hrvatsku. <https://mpudt.gov.hr/centar-dijeljenih-usluga-cdu-drzavni-oblak-koji-pokrece-digitalnu-hrvatsku/30983> ([archived](https://web.archive.org/web/20260907214940/https://mpudt.gov.hr/centar-dijeljenih-usluga-cdu-drzavni-oblak-koji-pokrece-digitalnu-hrvatsku/30983))
[^s2]: Narodne novine (Official Gazette of the Republic of Croatia) 7f0c2da59e, 2014-07-28. Zakon o državnoj informacijskoj infrastrukturi (NN 92/2014), članak 12.. <https://narodne-novine.nn.hr/clanci/sluzbeni/2014_07_92_1840.html>
[^s3]: Zakon.hr (consolidated text of Croatian legislation) d00cece7f0. Zakon o tajnosti podataka (NN 79/07, 86/12), članak 4.. <https://www.zakon.hr/z/217/Zakon-o-tajnosti-podataka> ([archived](https://web.archive.org/web/20260729164159/https://www.zakon.hr/z/217/zakon-o-tajnosti-podataka))
[^s4]: AKD d.o.o. def3eaefa0. Tvrtka – osnovni podaci. <https://www.akd.hr/hr/o-nama/tvrtka-osnovni-podaci> ([archived](https://web.archive.org/web/20260311051715/http://www.akd.hr/hr/o-nama/tvrtka-osnovni-podaci))
[^s5]: Financijska agencija (Fina) edfd258b86. O nama – Financijska agencija. <https://www.fina.hr/o-nama> ([archived](https://web.archive.org/web/20260907105158/https://www.fina.hr/o-nama))
[^s6]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s7]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s8]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s9]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s10]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s11]: Zakon.hr (consolidated text of Narodne novine 96/93, 76/13, 98/19, 133/22) 0f6fea538a. Zakon o državnim maticama (pročišćeni tekst). <https://www.zakon.hr/z/603/zakon-o-drzavnim-maticama> ([archived](https://web.archive.org/web/20260723125945/https://www.zakon.hr/z/603/zakon-o-drzavnim-maticama))
[^s12]: Narodne novine d.d. e0eb436c60, 2019. Pravilnik o vozačkim dozvolama. <https://narodne-novine.nn.hr/clanci/sluzbeni/2019_01_2_39.html> ([archived](https://web.archive.org/web/20260517053634/https://narodne-novine.nn.hr/clanci/sluzbeni/2019_01_2_39.html))
[^s13]: Zakon.hr (NN 127/19) 8bbb4f4295, 2019. Zakon o obradi biometrijskih podataka. <https://www.zakon.hr/z/2431/zakon-o-obradi-biometrijskih-podataka> ([archived](https://web.archive.org/web/20260614042102/https://www.zakon.hr/z/2431/zakon-o-obradi-biometrijskih-podataka))
[^s14]: Narodne novine d.d. 097b518ec9, 2015. Zakon o osobnoj iskaznici. <https://narodne-novine.nn.hr/clanci/sluzbeni/full/2015_06_62_1189.html> ([archived](https://web.archive.org/web/20231128121708/https://narodne-novine.nn.hr/clanci/sluzbeni/full/2015_06_62_1189.html))
[^s15]: Narodne novine d.d. 73362f4348, 2021. Naputak za provedbu Zakona o državnim maticama. <https://narodne-novine.nn.hr/clanci/sluzbeni/2021_10_117_2012.html> ([archived](https://web.archive.org/web/20260612022049/https://narodne-novine.nn.hr/clanci/sluzbeni/2021_10_117_2012.html))
[^s16]: NIAS / e-Građani 4ed5216d7b, 2025. Opći uvjeti korištenja - NIAS. <https://nias.gov.hr/Home/TermsOfUse> ([archived](https://web.archive.org/web/20250914232256/https://nias.gov.hr/Home/TermsOfUse))
[^s17]: Zakon.hr 8f97e69c61. Zakon o zemljišnim knjigama. <https://www.zakon.hr/z/103/zakon-o-zemljisnim-knjigama> ([archived](https://web.archive.org/web/20260916120158/https://www.zakon.hr/z/103/zakon-o-zemljisnim-knjigama))
[^s18]: Državna geodetska uprava 17c9b87387. Zajednički informacijski sustav zemljišnih knjiga i katastra. <https://dgu.gov.hr/zajednicki-informacijski-sustav-zemljisnih-knjiga-i-katastra/161> ([archived](https://web.archive.org/web/20260715120501/https://dgu.gov.hr/zajednicki-informacijski-sustav-zemljisnih-knjiga-i-katastra/161))
[^s19]: Zakon.hr 04e71ec94f. Zakon o policijskim poslovima i ovlastima. <https://www.zakon.hr/z/173/zakon-o-policijskim-poslovima-i-ovlastima> ([archived](https://web.archive.org/web/20260902084202/https://www.zakon.hr/z/173/zakon-o-policijskim-poslovima-i-ovlastima))
[^s20]: AKD d.o.o. (eid.hr) b6872cee28. AKD PKI – Certifikati. <https://www.eid.hr/hr/certifikati/akd-pki> ([archived](https://web.archive.org/web/20260730092109/https://www.eid.hr/hr/certifikati/akd-pki))
[^s21]: Fina (Financijska agencija) 75a3b680b0. Vjerujte Fini. <https://www.fina.hr/vjerujte-fini>
[^s22]: Zakon.hr (NN 133/20, 114/22, 151/22, 40/25, 55/26) 690977a22c. Zakon o strancima (pročišćeni tekst). <https://www.zakon.hr/z/142/zakon-o-strancima> ([archived](https://web.archive.org/web/20260720121718/https://www.zakon.hr/z/142/zakon-o-strancima))
[^s23]: Zakon.hr 85fba9c324. Zakon o sudskom registru. <https://www.zakon.hr/z/271/zakon-o-sudskom-registru>
[^s24]: Fina (Financijska agencija) a3c12cf10f. Registar stvarnih vlasnika. <https://www.fina.hr/javne-usluge-za-poslovne-subjekte/registri/registar-stvarnih-vlasnika> ([archived](https://web.archive.org/web/20260820073130/https://www.fina.hr/javne-usluge-za-poslovne-subjekte/registri/registar-stvarnih-vlasnika))
[^s25]: Narodne novine d.d. 5927b0452f, 2017. Pravilnik o registraciji i označavanju vozila. <https://narodne-novine.nn.hr/clanci/sluzbeni/full/2017_12_130_2993.html> ([archived](https://web.archive.org/web/20260921093541/https://narodne-novine.nn.hr/clanci/sluzbeni/full/2017_12_130_2993.html))
[^s26]: Zakon.hr f4bed7f372. Zakon o nadzoru državne granice. <https://www.zakon.hr/z/450/zakon-o-nadzoru-drzavne-granice> ([archived](https://web.archive.org/web/20260723144358/https://www.zakon.hr/z/450/zakon-o-nadzoru-drzavne-granice))
[^s27]: Ministarstvo financija bae053acc3. Državna riznica. <https://mfin.gov.hr/istaknute-teme/drzavna-riznica/103> ([archived](https://web.archive.org/web/20260814130009/https://mfin.gov.hr/istaknute-teme/drzavna-riznica/103))
[^s28]: Narodne novine d.d. 2d26cf1c14, 2023. Zakon o Registru zaposlenih i centraliziranom obračunu plaća u državnoj službi i javnim službama. <https://narodne-novine.nn.hr/clanci/sluzbeni/2023_06_59_997.html> ([archived](https://web.archive.org/web/20251214072619/https://narodne-novine.nn.hr/clanci/sluzbeni/2023_06_59_997.html))
[^s29]: Hrvatska narodna banka fae2aa7296, 2023-01-01. Payment systems. <https://www.hnb.hr/en/statistics/statistical-data/payment-systems> ([archived](https://web.archive.org/web/20260520195057/https://www.hnb.hr/en/statistics/statistical-data/payment-systems))
[^s30]: Hrvatska narodna banka 96c8b3481f. TARGET-HR. <https://www.hnb.hr/en/core-functions/payment-system/payment-systems/targe-hr> ([archived](https://web.archive.org/web/20260508191140/https://www.hnb.hr/en/core-functions/payment-system/payment-systems/targe-hr))
[^s31]: Ravnateljstvo civilne zaštite (MUP) 4bf6bee9fd. Sustav 112. <https://civilna-zastita.gov.hr/sustav-112/112> ([archived](https://web.archive.org/web/20260414033755/https://civilna-zastita.gov.hr/sustav-112/112))
[^s32]: Narodne novine d.d. fc8e579fe7, 2023. Pravilnik o sadržaju i korištenju informacijskih sustava u visokom obrazovanju. <https://narodne-novine.nn.hr/clanci/sluzbeni/2023_03_36_614.html> ([archived](https://web.archive.org/web/20260710102925/https://narodne-novine.nn.hr/clanci/sluzbeni/2023_03_36_614.html))
[^s33]: CARNET 2a13b5890a. e-Matica. <https://www.carnet.hr/projekt/e-matica-2/> ([archived](https://web.archive.org/web/20260519213940/https://www.carnet.hr/projekt/e-matica-2/))
[^s34]: Zakon.hr (NN 14/19) bf6df2b587, 2019. Zakon o podacima i informacijama u zdravstvu. <https://www.zakon.hr/z/1883/zakon-o-podacima-i-informacijama-u-zdravstvu> ([archived](https://web.archive.org/web/20260312003855/https://www.zakon.hr/z/1883/zakon-o-podacima-i-informacijama-u-zdravstvu))
[^s35]: Zakon.hr f04124ae0e. Zakon o poreznoj upravi. <https://www.zakon.hr/z/419/zakon-o-poreznoj-upravi>
[^s36]: Hrvatska gospodarska komora (Znakovi kvalitete) 6be8f98659. Usluga podatkovnog centra APIS IT. <https://znakovi.hgk.hr/proizvod/usluga-podatkovnog-centra-apis-it/> ([archived](https://web.archive.org/web/20260610123435/https://znakovi.hgk.hr/proizvod/usluga-podatkovnog-centra-apis-it/))
[^s37]: Zakon.hr 6d33676629. Zakon o državnoj izmjeri i katastru nekretnina. <https://www.zakon.hr/z/156/zakon-o-drzavnoj-izmjeri-i-katastru-nekretnina> ([archived](https://web.archive.org/web/20260222053536/https://www.zakon.hr/z/156/zakon-o-drzavnoj-izmjeri-i-katastru-nekretnina))
