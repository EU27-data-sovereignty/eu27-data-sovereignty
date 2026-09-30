# Hungary: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Hungary could be anywhere from 'Sovereign in practice, not secured in law' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | Partly[^s1][^s2] |
| Classification in law | Yes[^s3] |
| Sovereign cloud certification | No[^s4] |
| State-controlled trust anchor | Yes[^s5] |
| State-controlled national eID | Yes[^s6][^s7] |
| Government data centres | Yes[^s8] |
| Government cloud in operation | Yes[^s2] |

What could move this placement:

- If any of the 24 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Hungary described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 9.54 million[^s9] |
| GDP, current prices | 218.8 EUR bn[^s10] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 213.2 EUR/MWh[^s11] |
| Renewables share of electricity | 24.1 %[^s12] |
| Land area | 91 248 km²[^s13] |

## 3. Critical data holdings, by priority

The holdings Hungary cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 26 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| High | Civil registry core (tier 0) | Személyiadat- és lakcímnyilvántartás (Personal Data and Address Register): the authentic official register of citizens' personal, address and notification-address data[^s14] | *Not yet sourced* | National infrastructure[^s15] | *Not yet measured* |
| High | Facial biometric (tier 0) | The SZL stores the facial image (arcképmás) and signature of citizens who applied for an ID card[^s14] | The Minister for Science and Technology is designated central organ under the 2015 facial image analysis act[^s16] | National infrastructure[^s14] | *Not yet measured* |
| High | Fingerprint biometric (tier 0) | With written consent, the SZL stores the citizen's fingerprint for replacing the permanent ID card[^s14] | Minister of Interior designated as criminal records body, including the register of criminal and law-enforcement biometric data[^s16] | National infrastructure[^s14] | *Not yet measured* |
| High | Breeder document scans (tier 0) | The electronic civil register includes the register of civil-status and name-change certificates (okiratnyilvántartás)[^s17] | Minister for Science and Technology is the civil-register keeping body[^s16] | National infrastructure[^s17] | *Not yet measured* |
| High | Authentication audit log (tier 0) | The register keeper records every data-processing operation in an automated log system (naplórendszer)[^s18] | *Not yet sourced* | National infrastructure[^s15] | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | CSCA-HUNGARY country signing CA for e-passports, operated by the passport-issuing ministry[^s19] | NISZ Zrt. is the designated provider of government e-signature, e-seal and signature validation[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | The land register contains every property located in Hungary, settlement by settlement[^s21] | Lechner Tudásközpont is designated land authority (with county government offices)[^s22] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | Police place SIS alerts via the wanted-persons register system[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | The SZL records ID card document identifiers and electronic unique identifiers[^s14] | Minister for Science and Technology keeps the register of official identity documents[^s16] | National infrastructure[^s15] | *Not yet measured* |
| High | Digital identity credentials (tier 0) | Digital citizenship register: the client-registration register created by the Digital State Act[^s18] | IdomSoft Zrt. designated as digital citizenship service provider[^s20] | National infrastructure[^s15] | *Not yet measured* |
| High | Electoral roll entry (tier 0) | The central electoral register is an electronic register kept by the National Election Office[^s24] | IdomSoft builds the National Election System used by election offices[^s25] | National infrastructure[^s15] | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | Insurance periods are established from the records of the pension and health insurance administration bodies[^s26] | Government designates the Hungarian State Treasury Pension Disbursement Directorate as a pension insurance administration body[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | NEAK keeps the register of insured persons' relationship data, entitlement and TAJ data[^s28] | NEAK is a health insurance body[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | The beneficial ownership register contains the data of reporting entities[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | N.SIS comprises the full national copy of SIS and the national backbone, among other parts[^s30] | N.SIS Office is responsible for data in the national copy[^s30] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Holders must report firearm data to police for the central firearms register[^s31] | Firearms licences are issued by the police[^s31] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | Payroll-based tax obligations are met exclusively through the centralised payroll system operated by the Treasury[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | Instant payment service launched 2 March 2020[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | EDR: the Schengen-compliant digital government radio network[^s34] | The police handle calls to emergency numbers[^s23] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Public alarm system managed by the professional disaster management body[^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Central register of issued school-leaving (matura) certificates[^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Residence and migration status (tier 1) | Third-country nationals' data are kept in the sub-registers of the central aliens-policing register[^s37] | The Minister of Interior is responsible for aliens policing and asylum[^s16] | National infrastructure[^s37] | *Not yet measured* |
| Standard | Vehicle & licensing (tier 1) | National Vehicle Register system built/run by IdomSoft[^s25] | Minister for Science and Technology is the road transport registering body[^s16] | National infrastructure[^s15] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | Vaccination data are entered into the electronic epidemiological surveillance system[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | KSH conducts censuses and micro-censuses[^s39] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | Central address register provides an authentic address source for registers[^s18] | Lechner manages national geodata databases and runs the national spatial data infrastructure[^s22] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 26 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 10 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 16 |

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

> Not yet sized. Capacity for Hungary will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Hungary without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Tax (tier 1)
- Customs declarations (tier 1)
- Business registry (tier 1)
- Judicial & criminal justice (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

---

[^s1]: Wolters Kluwer Jogtár (consolidated text of Act LXIX of 2024) — 2024. évi LXIX. törvény Magyarország kiberbiztonságáról…, 2024. 2024. évi LXIX. törvény Magyarország kiberbiztonságáról (Kiberbiztonsági tv.), 9. §. <https://net.jogtar.hu/jogszabaly?docid=a2400069.tv>
[^s2]: Wolters Kluwer Jogtár (consolidated text of Government Decree 418/2024) — 418/2024. (XII. 23.) Korm. rendelet a Magyarország…, 2024-12-23. 418/2024. (XII. 23.) Korm. rendelet a Magyarország kiberbiztonságáról szóló törvény végrehajtásáról, 1. melléklet. <https://net.jogtar.hu/jogszabaly?docid=a2400418.kor> ([archived](https://web.archive.org/web/20251123140140/https://net.jogtar.hu/jogszabaly?docid=A2400418.KOR))
[^s3]: Wolters Kluwer Jogtár (consolidated text of Act CLV of 2009) — 2009. évi CLV. törvény a minősített adat védelméről, 5.…, 2009. 2009. évi CLV. törvény a minősített adat védelméről, 5. § (4). <https://net.jogtar.hu/jogszabaly?docid=a0900155.tv> ([archived](https://web.archive.org/web/20260107073215/https://net.jogtar.hu/jogszabaly?docid=A0900155.TV))
[^s4]: Nemzeti Kibervédelmi Intézet / national cybersecurity authority — Felhő – harmadik fél által tanúsított…. Felhő – harmadik fél által tanúsított felhőszolgáltatások (Cloud – third-party certified cloud services). <https://nki.gov.hu/hatosag/tartalom/felho/> ([archived](https://web.archive.org/web/20250628235716/https://nki.gov.hu/hatosag/tartalom/felho/))
[^s5]: Kormányzati Hitelesítés Szolgáltató (GovCA), NISZ Zrt. — Kormányzati Hitelesítés Szolgáltató – Kik vagyunk. Kormányzati Hitelesítés Szolgáltató – Kik vagyunk. <https://hiteles.gov.hu/cikk/185/kormanyzati_hitelesites_szolgaltato> ([archived](https://web.archive.org/web/20260708154825/https://hiteles.gov.hu/cikk/185/kormanyzati_hitelesites_szolgaltato))
[^s6]: Digitális Magyarország Ügynökség (Digital Hungary Agency) — Portfólió – Digitális Magyarország Ügynökség. Portfólió – Digitális Magyarország Ügynökség. <https://www.dmu.gov.hu/cikkek/portfolio> ([archived](https://web.archive.org/web/20260603115511/https://www.dmu.gov.hu/cikkek/portfolio))
[^s7]: Wolters Kluwer Jogtár (consolidated text of Act CIII of 2023) — 2023. évi CIII. törvény a digitális államról és a…, 2023. 2023. évi CIII. törvény a digitális államról és a digitális szolgáltatások nyújtásának egyes szabályairól (Dáptv.), 12. §. <https://net.jogtar.hu/jogszabaly?docid=a2300103.tv> ([archived](https://web.archive.org/web/20251203022211/https://net.jogtar.hu/jogszabaly?docid=A2300103.TV))
[^s8]: Digitális Magyarország Ügynökség (Digital Hungary Agency) — Rólunk – Digitális Magyarország Ügynökség. Rólunk – Digitális Magyarország Ügynökség. <https://www.dmu.gov.hu/rolunk>
[^s9]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s10]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s11]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s12]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s13]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s14]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 1992. évi LXVI. törvény a polgárok személyi adatainak és…, 1992. 1992. évi LXVI. törvény a polgárok személyi adatainak és lakcímének nyilvántartásáról. <https://net.jogtar.hu/jogszabaly?docid=99200066.tv> ([archived](https://web.archive.org/web/20251224033602/https://net.jogtar.hu/jogszabaly?docid=99200066.TV))
[^s15]: IdomSoft Informatikai Zrt. — Történetünk | IdomSoft Zrt.. Történetünk | IdomSoft Zrt.. <https://www.idomsoft.hu/rolunk/tortenetunk> ([archived](https://web.archive.org/web/20260422201158/https://www.idomsoft.hu/rolunk/tortenetunk/))
[^s16]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 90/2026. (V. 13.) Korm. rendelet a Kormány tagjainak…, 2026. 90/2026. (V. 13.) Korm. rendelet a Kormány tagjainak feladat- és hatásköréről. <https://net.jogtar.hu/jogszabaly?docid=A2600090.KOR>
[^s17]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2010. évi I. törvény az anyakönyvi eljárásról, 2010. 2010. évi I. törvény az anyakönyvi eljárásról. <https://net.jogtar.hu/jogszabaly?docid=A1000001.TV> ([archived](https://web.archive.org/web/20260913003001/https://net.jogtar.hu/jogszabaly?docid=a1000001.tv))
[^s18]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2023. évi CIII. törvény a digitális államról és a…, 2023. 2023. évi CIII. törvény a digitális államról és a digitális szolgáltatások nyújtásának egyes szabályairól. <https://net.jogtar.hu/jogszabaly?docid=A2300103.TV> ([archived](https://web.archive.org/web/20251203022211/https://net.jogtar.hu/jogszabaly?docid=A2300103.TV))
[^s19]: Magyarország Kormánya (kormany.hu) — Tájékoztató a CSCA tanúsítványról. Tájékoztató a CSCA tanúsítványról. <https://kormany.hu/nyilvantartasok/biometrikus-utlevel/tajekoztato-a-csca-tanusitvanyrol> ([archived](https://web.archive.org/web/20260920201822/https://kormany.hu/nyilvantartasok/biometrikus-utlevel/tajekoztato-a-csca-tanusitvanyrol))
[^s20]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 320/2024. (XI. 6.) Korm. rendelet a digitális állam…, 2024. 320/2024. (XI. 6.) Korm. rendelet a digitális állam megvalósításához kapcsolódó egyes szervezetek kijelöléséről. <https://net.jogtar.hu/jogszabaly?docid=A2400320.KOR>
[^s21]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2021. évi C. törvény az ingatlan-nyilvántartásról, 2021. 2021. évi C. törvény az ingatlan-nyilvántartásról. <https://net.jogtar.hu/jogszabaly?docid=A2100100.TV>
[^s22]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 383/2016. (XII. 2.) Korm. rendelet a földművelésügyi…, 2016. 383/2016. (XII. 2.) Korm. rendelet a földművelésügyi hatósági és igazgatási feladatokat ellátó szervek kijelöléséről. <https://net.jogtar.hu/jogszabaly?docid=A1600383.KOR> ([archived](https://web.archive.org/web/20240711234223/https://net.jogtar.hu/jogszabaly?docid=a1600383.kor))
[^s23]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 1994. évi XXXIV. törvény a Rendőrségről, 1994. 1994. évi XXXIV. törvény a Rendőrségről. <https://net.jogtar.hu/jogszabaly?docid=99400034.TV> ([archived](https://web.archive.org/web/20260626121651/https://net.jogtar.hu/jogszabaly?docid=99400034.tv))
[^s24]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2013. évi XXXVI. törvény a választási eljárásról, 2013. 2013. évi XXXVI. törvény a választási eljárásról. <https://net.jogtar.hu/jogszabaly?docid=A1300036.TV> ([archived](https://web.archive.org/web/20260727221758/https://net.jogtar.hu/jogszabaly?docid=a1300036.tv))
[^s25]: IdomSoft Informatikai Zrt. — Termékek | IdomSoft Zrt.. Termékek | IdomSoft Zrt.. <https://www.idomsoft.hu/termekek> ([archived](https://web.archive.org/web/20260512054003/https://www.idomsoft.hu/termekek/))
[^s26]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 1997. évi LXXXI. törvény a társadalombiztosítási…, 1997. 1997. évi LXXXI. törvény a társadalombiztosítási nyugellátásról. <https://net.jogtar.hu/jogszabaly?docid=99700081.TV> ([archived](https://web.archive.org/web/20260509102143/https://net.jogtar.hu/jogszabaly?docid=99700081.tv))
[^s27]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 168/1997. (X. 6.) Korm. rendelet a társadalombiztosítási…, 1997. 168/1997. (X. 6.) Korm. rendelet a társadalombiztosítási nyugellátásról szóló 1997. évi LXXXI. törvény végrehajtásáról. <https://net.jogtar.hu/jogszabaly?docid=99700168.KOR> ([archived](https://web.archive.org/web/20260523233650/https://net.jogtar.hu/jogszabaly?docid=99700168.kor))
[^s28]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 386/2016. (XII. 2.) Korm. rendelet az…, 2016. 386/2016. (XII. 2.) Korm. rendelet az egészségbiztosítási szervekről. <https://net.jogtar.hu/jogszabaly?docid=A1600386.KOR>
[^s29]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2021. évi XLIII. törvény a pénzügyi és egyéb…, 2021. 2021. évi XLIII. törvény a pénzügyi és egyéb szolgáltatók azonosítási feladatához kapcsolódó adatszolgáltatási háttér megteremtéséről és működtetéséről. <https://net.jogtar.hu/jogszabaly?docid=A2100043.TV> ([archived](https://web.archive.org/web/20250823190745/https://net.jogtar.hu/jogszabaly?docid=a2100043.tv))
[^s30]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2012. évi CLXXXI. törvény a Schengeni Információs…, 2012. 2012. évi CLXXXI. törvény a Schengeni Információs Rendszer második generációja keretében történő információcseréről. <https://net.jogtar.hu/jogszabaly?docid=A1200181.TV>
[^s31]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2004. évi XXIV. törvény a lőfegyverekről és lőszerekről, 2004. 2004. évi XXIV. törvény a lőfegyverekről és lőszerekről. <https://net.jogtar.hu/jogszabaly?docid=A0400024.TV>
[^s32]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2011. évi CXCV. törvény az államháztartásról, 2011. 2011. évi CXCV. törvény az államháztartásról. <https://net.jogtar.hu/jogszabaly?docid=A1100195.TV>
[^s33]: Magyar Nemzeti Bank — Azonnali fizetés. Azonnali fizetés. <https://www.mnb.hu/penzforgalom/azonnalifizetes> ([archived](https://web.archive.org/web/20260718155137/https://www.mnb.hu/penzforgalom/azonnalifizetes))
[^s34]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 346/2010. (XII. 28.) Korm. rendelet a kormányzati célú…, 2010. 346/2010. (XII. 28.) Korm. rendelet a kormányzati célú hálózatokról. <https://net.jogtar.hu/jogszabaly?docid=A1000346.KOR>
[^s35]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2011. évi CXXVIII. törvény a katasztrófavédelemről, 2011. 2011. évi CXXVIII. törvény a katasztrófavédelemről. <https://net.jogtar.hu/jogszabaly?docid=A1100128.TV> ([archived](https://web.archive.org/web/20251202170941/https://net.jogtar.hu/jogszabaly?docid=a1100128.tv))
[^s36]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2011. évi CXC. törvény a nemzeti köznevelésről, 2011. 2011. évi CXC. törvény a nemzeti köznevelésről. <https://net.jogtar.hu/jogszabaly?docid=A1100190.TV> ([archived](https://web.archive.org/web/20260907112557/https://net.jogtar.hu/jogszabaly?docid=a1100190.tv))
[^s37]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2023. évi XC. törvény a harmadik országbeli…, 2023. 2023. évi XC. törvény a harmadik országbeli állampolgárok beutazására és tartózkodására vonatkozó általános szabályokról. <https://net.jogtar.hu/jogszabaly?docid=A2300090.TV> ([archived](https://web.archive.org/web/20260805072340/https://net.jogtar.hu/jogszabaly?docid=a2300090.tv))
[^s38]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 18/1998. (VI. 3.) NM rendelet a fertőző betegségek és a…, 1998. 18/1998. (VI. 3.) NM rendelet a fertőző betegségek és a járványok megelőzése érdekében szükséges járványügyi intézkedésekről. <https://net.jogtar.hu/jogszabaly?docid=99800018.NM>
[^s39]: Wolters Kluwer Hungary – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) — 2016. évi CLV. törvény a hivatalos statisztikáról, 2016. 2016. évi CLV. törvény a hivatalos statisztikáról. <https://net.jogtar.hu/jogszabaly?docid=A1600155.TV> ([archived](https://web.archive.org/web/20251005015911/https://net.jogtar.hu/jogszabaly?docid=a1600155.tv))

**Evidence grades:** 1 Strong, 63 Standard. Strong: an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review. Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.
