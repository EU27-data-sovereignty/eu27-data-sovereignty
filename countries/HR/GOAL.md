# Croatia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Croatia could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2] |
| Classification in law | Yes[^s3][^s4] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s5][^s6] |
| State-controlled national eID | Yes[^s5][^s2][^s7] |
| Government data centres | Yes[^s1] |
| Government cloud in operation | Yes[^s1] |

What could move this placement:

- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Croatia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 3.88 million[^s8] |
| GDP, current prices | 93.0 EUR bn[^s9] |
| Public administration employment (NACE O) | 116.9 thousand[^s10] |
| Non-household electricity price | 154.8 EUR/MWh[^s11] |
| Renewables share of electricity | 58.8 %[^s12] |
| Land area | 55 896 km²[^s13] |

## 3. Critical data holdings, by priority

The holdings Croatia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 29 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | State civil registers (Državne matice): registers of births, marriages and deaths[^s14][^s15] | The state administration body for general administration sets up and runs the single information system for the civil registers[^s15] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Photograph stored in the ID-card register in the Ministry of the Interior information system (reused for driving licences)[^s16] | Competent bodies for biometric collections are the ministries of the interior, foreign affairs and justice[^s17][^s18] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Fingerprints already taken and stored electronically in a ministry document-issuance procedure are reused (central retention)[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Files underlying civil-register entries are of permanent value[^s20] | Registers whose last entry is more than 100 years old are kept by the Croatian State Archives[^s15] | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | NIAS records credential-usage history, visible to the user for the last 60 days[^s7] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | ID-card register kept in the Ministry of the Interior information system, recording invalid (lost) cards[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Nacionalni identifikacijski i autentifikacijski sustav (NIAS) (National Identification and Authentication System)[^s7] | tijelo državne uprave nadležno za digitalnu transformaciju (state administration body responsible for digital transformation)[^s7] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Registar birača (Register of voters)[^s21] | Središnje tijelo državne uprave nadležno za poslove opće uprave (central state administration body for general administration)[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | ZIS stores and maintains all land-register and cadastre data[^s22][^s23] | ZIS is jointly coordinated by the Ministry of Justice and the State Geodetic Administration[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | The Ministry information system is the Information System of the Ministry of the Interior[^s25][^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | zbirke i registri osobnih podataka sigurnosno-obavještajnih agencija (personal-data collections and registers of the security-intelligence agencies)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | AKD HRIDCA issues identification and qualified signature certificates for the eOI card[^s28] | Fina is a qualified trust service provider on the national trusted list[^s29] | National infrastructure[^s28] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Collection covers third-country nationals on short-term, temporary, long-term and permanent stay[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | matična evidencija (master record of insured persons, pension beneficiaries and contribution payers)[^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | Main books are linked into a single database for Croatia[^s32] | The register is kept by the commercial courts and preserved permanently[^s33][^s32] | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Central electronic database of beneficial owners of legal entities and trusts[^s34] | Operationally run by Fina on behalf of the Anti-Money Laundering Office, Ministry of Finance[^s34] | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Register of registered vehicles kept on the Ministry of the Interior information system[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | National information system for state border management, part of the MUP information system[^s36][^s37] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | evidencije na središnjem informacijskom sustavu ministarstva nadležnog za unutarnje poslove (records on the central information system of the Ministry of the Interior)[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | All budget-user transactions go through the State Treasury system and the single treasury account held at HNB[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | The COP payroll information system is owned by the Republic of Croatia[^s40] | Fina processes the data on behalf of the civil-service body[^s40] | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | Payments in Croatia run through TARGET-HR, EuroNCS and EuroNCSInst[^s41] | *Not yet sourced* | EU provider[^s42] | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | System 112 consists of interconnected 112 centres and the Operational Centre of Civil Protection[^s43] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | National Operational Centre of Civil Protection monitors events through the 112 centres[^s43] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Central register of higher-education certificates, diplomas and supplements (Digital Register of Diplomas)[^s44] | e-Matica is a centralised MZOM system; CARNET is the support centre[^s45] | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | CEZIH is the central store of health data for primary, secondary and tertiary care[^s46][^s47] | HZZO manages CEZIH and maintains its central part[^s46][^s47] | *Not stated in sources* | *Not yet measured* |
| Standard | Tax (tier 1) | Information system of the Tax Administration[^s48] | *Not yet sourced* | National infrastructure[^s49] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | NAJS stores health data and public-health records and registers[^s46][^s47] | NAJS is run by HZJZ[^s46][^s47] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | Building register established, kept and maintained by DGU[^s50][^s51] | Državna geodetska uprava (State Geodetic Administration)[^s50] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 29 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 1 |
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

> Not yet sized. Capacity for Croatia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Croatia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Customs declarations (tier 1)
- Statutory health insurance (tier 1)
- Judicial & criminal justice (tier 1)
- Official gazette and legislation (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

---

[^s1]: Ministarstvo pravosuđa, uprave i digitalne transformacije — Centar dijeljenih usluga (CDU) – državni oblak koji…. Centar dijeljenih usluga (CDU) – državni oblak koji pokreće digitalnu Hrvatsku. <https://mpudt.gov.hr/centar-dijeljenih-usluga-cdu-drzavni-oblak-koji-pokrece-digitalnu-hrvatsku/30983> ([archived](https://web.archive.org/web/20260907214940/https://mpudt.gov.hr/centar-dijeljenih-usluga-cdu-drzavni-oblak-koji-pokrece-digitalnu-hrvatsku/30983))
[^s2]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o državnoj informacijskoj infrastrukturi (NN…, 2014-07-28. Zakon o državnoj informacijskoj infrastrukturi (NN 92/2014), članak 12.. <https://narodne-novine.nn.hr/clanci/sluzbeni/2014_07_92_1840.html>
[^s3]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o tajnosti podataka (NN 79/2007), 2007-07-30. Zakon o tajnosti podataka (NN 79/2007). <https://narodne-novine.nn.hr/clanci/sluzbeni/2007_07_79_2483.html> ([archived](https://web.archive.org/web/20260511212235/https://narodne-novine.nn.hr/clanci/sluzbeni/2007_07_79_2483.html))
[^s4]: Zakon.hr (consolidated text of Croatian legislation) — Zakon o tajnosti podataka (NN 79/07, 86/12), članak 4.. Zakon o tajnosti podataka (NN 79/07, 86/12), članak 4.. <https://www.zakon.hr/z/217/Zakon-o-tajnosti-podataka> ([archived](https://web.archive.org/web/20260729164159/https://www.zakon.hr/z/217/zakon-o-tajnosti-podataka))
[^s5]: AKD d.o.o. — Tvrtka – osnovni podaci. Tvrtka – osnovni podaci. <https://www.akd.hr/hr/o-nama/tvrtka-osnovni-podaci> ([archived](https://web.archive.org/web/20260311051715/http://www.akd.hr/hr/o-nama/tvrtka-osnovni-podaci))
[^s6]: Financijska agencija (Fina) — O nama – Financijska agencija. O nama – Financijska agencija. <https://www.fina.hr/o-nama> ([archived](https://web.archive.org/web/20260907105158/https://www.fina.hr/o-nama))
[^s7]: NIAS / e-Građani — Opći uvjeti korištenja - NIAS, 2025. Opći uvjeti korištenja - NIAS. <https://nias.gov.hr/Home/TermsOfUse> ([archived](https://web.archive.org/web/20250914232256/https://nias.gov.hr/Home/TermsOfUse))
[^s8]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s9]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s10]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s11]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s12]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s13]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s14]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o državnim maticama (NN 96/1993), 1993-10. Zakon o državnim maticama (NN 96/1993). <https://narodne-novine.nn.hr/clanci/sluzbeni/1993_10_96_1878.html> ([archived](https://web.archive.org/web/20260420162921/https://narodne-novine.nn.hr/clanci/sluzbeni/1993_10_96_1878.html))
[^s15]: Zakon.hr (consolidated text of Narodne novine 96/93, 76/13, 98/19, 133/22) — Zakon o državnim maticama (pročišćeni tekst). Zakon o državnim maticama (pročišćeni tekst). <https://www.zakon.hr/z/603/zakon-o-drzavnim-maticama> ([archived](https://web.archive.org/web/20260723125945/https://www.zakon.hr/z/603/zakon-o-drzavnim-maticama))
[^s16]: Narodne novine d.d. — Pravilnik o vozačkim dozvolama, 2019. Pravilnik o vozačkim dozvolama. <https://narodne-novine.nn.hr/clanci/sluzbeni/2019_01_2_39.html> ([archived](https://web.archive.org/web/20260517053634/https://narodne-novine.nn.hr/clanci/sluzbeni/2019_01_2_39.html))
[^s17]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o obradi biometrijskih podataka (NN 127/2019), 2019-12. Zakon o obradi biometrijskih podataka (NN 127/2019). <https://narodne-novine.nn.hr/clanci/sluzbeni/2019_12_127_2551.html> ([archived](https://web.archive.org/web/20260612053149/https://narodne-novine.nn.hr/clanci/sluzbeni/2019_12_127_2551.html))
[^s18]: Zakon.hr (NN 127/19) — Zakon o obradi biometrijskih podataka, 2019. Zakon o obradi biometrijskih podataka. <https://www.zakon.hr/z/2431/zakon-o-obradi-biometrijskih-podataka> ([archived](https://web.archive.org/web/20260614042102/https://www.zakon.hr/z/2431/zakon-o-obradi-biometrijskih-podataka))
[^s19]: Narodne novine d.d. — Zakon o osobnoj iskaznici, 2015. Zakon o osobnoj iskaznici. <https://narodne-novine.nn.hr/clanci/sluzbeni/full/2015_06_62_1189.html> ([archived](https://web.archive.org/web/20231128121708/https://narodne-novine.nn.hr/clanci/sluzbeni/full/2015_06_62_1189.html))
[^s20]: Narodne novine d.d. — Naputak za provedbu Zakona o državnim maticama, 2021. Naputak za provedbu Zakona o državnim maticama. <https://narodne-novine.nn.hr/clanci/sluzbeni/2021_10_117_2012.html> ([archived](https://web.archive.org/web/20260612022049/https://narodne-novine.nn.hr/clanci/sluzbeni/2021_10_117_2012.html))
[^s21]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o registru birača (NN 144/2012), 2012-12. Zakon o registru birača (NN 144/2012). <https://narodne-novine.nn.hr/clanci/sluzbeni/2012_12_144_3073.html> ([archived](https://web.archive.org/web/20260518065722/https://narodne-novine.nn.hr/clanci/sluzbeni/2012_12_144_3073.html))
[^s22]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o zemljišnim knjigama (NN 63/2019), 2019-06. Zakon o zemljišnim knjigama (NN 63/2019). <https://narodne-novine.nn.hr/clanci/sluzbeni/2019_06_63_1234.html> ([archived](https://web.archive.org/web/20260612120931/https://narodne-novine.nn.hr/clanci/sluzbeni/2019_06_63_1234.html))
[^s23]: Zakon.hr — Zakon o zemljišnim knjigama. Zakon o zemljišnim knjigama. <https://www.zakon.hr/z/103/zakon-o-zemljisnim-knjigama> ([archived](https://web.archive.org/web/20260916120158/https://www.zakon.hr/z/103/zakon-o-zemljisnim-knjigama))
[^s24]: Državna geodetska uprava — Zajednički informacijski sustav zemljišnih knjiga i katastra. Zajednički informacijski sustav zemljišnih knjiga i katastra. <https://dgu.gov.hr/zajednicki-informacijski-sustav-zemljisnih-knjiga-i-katastra/161> ([archived](https://web.archive.org/web/20260715120501/https://dgu.gov.hr/zajednicki-informacijski-sustav-zemljisnih-knjiga-i-katastra/161))
[^s25]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o policijskim poslovima i ovlastima (NN 76/2009), 2009-07. Zakon o policijskim poslovima i ovlastima (NN 76/2009). <https://narodne-novine.nn.hr/clanci/sluzbeni/2009_07_76_1835.html> ([archived](https://web.archive.org/web/20260617104913/https://narodne-novine.nn.hr/clanci/sluzbeni/2009_07_76_1835.html))
[^s26]: Zakon.hr — Zakon o policijskim poslovima i ovlastima. Zakon o policijskim poslovima i ovlastima. <https://www.zakon.hr/z/173/zakon-o-policijskim-poslovima-i-ovlastima> ([archived](https://web.archive.org/web/20260902084202/https://www.zakon.hr/z/173/zakon-o-policijskim-poslovima-i-ovlastima))
[^s27]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o sigurnosno-obavještajnom sustavu Republike…, 2006-07. Zakon o sigurnosno-obavještajnom sustavu Republike Hrvatske (NN 79/2006). <https://narodne-novine.nn.hr/clanci/sluzbeni/2006_07_79_1912.html>
[^s28]: AKD d.o.o. (eid.hr) — AKD PKI – Certifikati. AKD PKI – Certifikati. <https://www.eid.hr/hr/certifikati/akd-pki> ([archived](https://web.archive.org/web/20260730092109/https://www.eid.hr/hr/certifikati/akd-pki))
[^s29]: Fina (Financijska agencija) — Vjerujte Fini. Vjerujte Fini. <https://www.fina.hr/vjerujte-fini>
[^s30]: Zakon.hr (NN 133/20, 114/22, 151/22, 40/25, 55/26) — Zakon o strancima (pročišćeni tekst). Zakon o strancima (pročišćeni tekst). <https://www.zakon.hr/z/142/zakon-o-strancima> ([archived](https://web.archive.org/web/20260720121718/https://www.zakon.hr/z/142/zakon-o-strancima))
[^s31]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o mirovinskom osiguranju (NN 157/2013), 2013-12. Zakon o mirovinskom osiguranju (NN 157/2013). <https://narodne-novine.nn.hr/clanci/sluzbeni/2013_12_157_3290.html> ([archived](https://web.archive.org/web/20260710205648/https://narodne-novine.nn.hr/clanci/sluzbeni/2013_12_157_3290.html))
[^s32]: Zakon.hr — Zakon o sudskom registru. Zakon o sudskom registru. <https://www.zakon.hr/z/271/zakon-o-sudskom-registru>
[^s33]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o sudskom registru (NN 1/1995), 1995-01. Zakon o sudskom registru (NN 1/1995). <https://narodne-novine.nn.hr/clanci/sluzbeni/1995_01_1_1.html> ([archived](https://web.archive.org/web/20260616093421/https://narodne-novine.nn.hr/clanci/sluzbeni/1995_01_1_1.html))
[^s34]: Fina (Financijska agencija) — Registar stvarnih vlasnika. Registar stvarnih vlasnika. <https://www.fina.hr/javne-usluge-za-poslovne-subjekte/registri/registar-stvarnih-vlasnika> ([archived](https://web.archive.org/web/20260820073130/https://www.fina.hr/javne-usluge-za-poslovne-subjekte/registri/registar-stvarnih-vlasnika))
[^s35]: Narodne novine d.d. — Pravilnik o registraciji i označavanju vozila, 2017. Pravilnik o registraciji i označavanju vozila. <https://narodne-novine.nn.hr/clanci/sluzbeni/full/2017_12_130_2993.html> ([archived](https://web.archive.org/web/20260921093541/https://narodne-novine.nn.hr/clanci/sluzbeni/full/2017_12_130_2993.html))
[^s36]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o nadzoru državne granice (NN 83/2013), 2013-07. Zakon o nadzoru državne granice (NN 83/2013). <https://narodne-novine.nn.hr/clanci/sluzbeni/2013_07_83_1738.html> ([archived](https://web.archive.org/web/20260511211909/https://narodne-novine.nn.hr/clanci/sluzbeni/2013_07_83_1738.html))
[^s37]: Zakon.hr — Zakon o nadzoru državne granice. Zakon o nadzoru državne granice. <https://www.zakon.hr/z/450/zakon-o-nadzoru-drzavne-granice> ([archived](https://web.archive.org/web/20260723144358/https://www.zakon.hr/z/450/zakon-o-nadzoru-drzavne-granice))
[^s38]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o nabavi i posjedovanju oružja građana (NN 94/2018), 2018-10. Zakon o nabavi i posjedovanju oružja građana (NN 94/2018). <https://narodne-novine.nn.hr/clanci/sluzbeni/2018_10_94_1816.html>
[^s39]: Ministarstvo financija — Državna riznica. Državna riznica. <https://mfin.gov.hr/istaknute-teme/drzavna-riznica/103> ([archived](https://web.archive.org/web/20260814130009/https://mfin.gov.hr/istaknute-teme/drzavna-riznica/103))
[^s40]: Narodne novine d.d. — Zakon o Registru zaposlenih i centraliziranom obračunu…, 2023. Zakon o Registru zaposlenih i centraliziranom obračunu plaća u državnoj službi i javnim službama. <https://narodne-novine.nn.hr/clanci/sluzbeni/2023_06_59_997.html> ([archived](https://web.archive.org/web/20251214072619/https://narodne-novine.nn.hr/clanci/sluzbeni/2023_06_59_997.html))
[^s41]: Hrvatska narodna banka — Payment systems, 2023-01-01. Payment systems. <https://www.hnb.hr/en/statistics/statistical-data/payment-systems> ([archived](https://web.archive.org/web/20260520195057/https://www.hnb.hr/en/statistics/statistical-data/payment-systems))
[^s42]: Hrvatska narodna banka — TARGET-HR. TARGET-HR. <https://www.hnb.hr/en/core-functions/payment-system/payment-systems/targe-hr> ([archived](https://web.archive.org/web/20260508191140/https://www.hnb.hr/en/core-functions/payment-system/payment-systems/targe-hr))
[^s43]: Ravnateljstvo civilne zaštite (MUP) — Sustav 112. Sustav 112. <https://civilna-zastita.gov.hr/sustav-112/112> ([archived](https://web.archive.org/web/20260414033755/https://civilna-zastita.gov.hr/sustav-112/112))
[^s44]: Narodne novine d.d. — Pravilnik o sadržaju i korištenju informacijskih sustava…, 2023. Pravilnik o sadržaju i korištenju informacijskih sustava u visokom obrazovanju. <https://narodne-novine.nn.hr/clanci/sluzbeni/2023_03_36_614.html> ([archived](https://web.archive.org/web/20260710102925/https://narodne-novine.nn.hr/clanci/sluzbeni/2023_03_36_614.html))
[^s45]: CARNET — e-Matica. e-Matica. <https://www.carnet.hr/projekt/e-matica-2/> ([archived](https://web.archive.org/web/20260519213940/https://www.carnet.hr/projekt/e-matica-2/))
[^s46]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o podacima i informacijama u zdravstvu (NN 14/2019), 2019-02. Zakon o podacima i informacijama u zdravstvu (NN 14/2019). <https://narodne-novine.nn.hr/clanci/sluzbeni/2019_02_14_269.html> ([archived](https://web.archive.org/web/20260514042307/https://narodne-novine.nn.hr/clanci/sluzbeni/2019_02_14_269.html))
[^s47]: Zakon.hr (NN 14/19) — Zakon o podacima i informacijama u zdravstvu, 2019. Zakon o podacima i informacijama u zdravstvu. <https://www.zakon.hr/z/1883/zakon-o-podacima-i-informacijama-u-zdravstvu> ([archived](https://web.archive.org/web/20260312003855/https://www.zakon.hr/z/1883/zakon-o-podacima-i-informacijama-u-zdravstvu))
[^s48]: Zakon.hr — Zakon o poreznoj upravi. Zakon o poreznoj upravi. <https://www.zakon.hr/z/419/zakon-o-poreznoj-upravi>
[^s49]: Hrvatska gospodarska komora (Znakovi kvalitete) — Usluga podatkovnog centra APIS IT. Usluga podatkovnog centra APIS IT. <https://znakovi.hgk.hr/proizvod/usluga-podatkovnog-centra-apis-it/> ([archived](https://web.archive.org/web/20260610123435/https://znakovi.hgk.hr/proizvod/usluga-podatkovnog-centra-apis-it/))
[^s50]: Narodne novine (Official Gazette of the Republic of Croatia) — Zakon o državnoj izmjeri i katastru nekretnina (NN 112/2018), 2018-12. Zakon o državnoj izmjeri i katastru nekretnina (NN 112/2018). <https://narodne-novine.nn.hr/clanci/sluzbeni/2018_12_112_2167.html>
[^s51]: Zakon.hr — Zakon o državnoj izmjeri i katastru nekretnina. Zakon o državnoj izmjeri i katastru nekretnina. <https://www.zakon.hr/z/156/zakon-o-drzavnoj-izmjeri-i-katastru-nekretnina> ([archived](https://web.archive.org/web/20260222053536/https://www.zakon.hr/z/156/zakon-o-drzavnoj-izmjeri-i-katastru-nekretnina))

**Evidence grades:** 4 Strong, 54 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
