# Slovakia: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Slovakia could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | *Not yet sourced* |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s1][^s2] |
| State-controlled national eID | Yes[^s3] |
| Government data centres | Yes[^s4] |
| Government cloud in operation | Yes[^s4] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Slovakia described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 5.42 million[^s5] |
| GDP, current prices | 136.8 EUR bn[^s6] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 209.0 EUR/MWh[^s7] |
| Renewables share of electricity | 24.9 %[^s8] |
| Land area | 48 702 km²[^s9] |

## 3. Critical data holdings, by priority

The holdings Slovakia cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 29 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Register obyvateľov Slovenskej republiky (Register of Inhabitants of the Slovak Republic), a public-administration information system identifying persons, their residence and relationships[^s10] | The Ministry of Interior (ministerstvo) administers the Register of Natural Persons, a base register; retention is permanent[^s10] | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Evidencia občianskych preukazov (ID card records) kept by the Ministry of Interior and district police directorates[^s11] | The Ministry of Interior keeps the central register of travel documents, which includes the facial image[^s12] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | Zbierka listín (collection of source documents) kept by registry offices as the basis for civil-status entries[^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Evidencia občianskych preukazov (ID card issuance records), incl. numbers of issued, lost and stolen cards and destruction dates[^s11] | Kept by the Ministry of Interior and district police directorates[^s11] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | eID: electronic identity card with contact chip, issued since 2 December 2013[^s3] | The Ministry of Interior administers the authentication part of the authentication module; MIRRI administers its communication part[^s14] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Stály zoznam voličov (permanent electoral roll) compiled and kept by each municipality[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | Slovenská národná certifikačná autorita (SNCA), providing qualified trust services free of charge to public authorities[^s16] | NASES has operated the Slovak National Certification Authority (SNCA) and provided qualified trust services since 1 August 2019[^s2] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Kataster nehnuteľností (real-estate cadastre) including ownership, liens and other rights[^s17] | The Office of Geodesy, Cartography and Cadastre (ÚGKK SR, 'úrad') administers the cadastral records and the cadastre information system[^s17] | *Not stated in sources* | *Not yet sourced* |
| High | Judicial & criminal justice (tier 1) | Register trestov (Criminal Records Register) kept by the General Prosecutor's Office[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Police Force information systems processing personal data, fingerprint (dactyloscopic) data and face images[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | Police Force information systems holding records on foreigners' entry, stay and departure, visa and residence applicants[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | Register poistencov a sporiteľov starobného dôchodkového sporenia (register of insured persons and pension savers) and employer register kept by Sociálna poisťovňa[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | Centrálny register poistencov (central register of insured persons) kept by the Health Care Surveillance Authority (ÚDZS)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | Obchodný register (Commercial Register) and collection of deeds, kept electronically by registry courts[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Register partnerov verejného sektora (Register of Public Sector Partners), run by the Ministry of Justice with Žilina District Court as registering body[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Evidencia vozidiel (vehicle register), an information system of the Police Force[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Police Force records on undesirable persons, border-control data on foreigners and illegal stay[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Police Force information system on firearms licences, holders and registered weapons[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | Centrálny informačný systém štátnej služby (central civil-service information system) administered by the Government Office[^s27] | Government Office of the Slovak Republic (Úrad vlády SR)[^s27] | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | Register kandidátov a kandidátnych listín (Register of candidates and candidate lists), created and operated by the Ministry of Interior[^s15] | Election results are processed through the information system of the Statistical Office of the Slovak Republic[^s15] | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | Národná banka Slovenska operates two payment systems: TARGET-SK (RTGS) and SIPS (retail)[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Coordination centres receive 112 calls, eCall and SMS emergency communications[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Informačný systém krízového riadenia štátu (state crisis management information system)[^s30] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Dispatch control of the transmission system, incl. defence and restoration plan in a blackout[^s31] | SEPS a.s. is the transmission system operator including the Slovak Electricity Dispatch Centre[^s32] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Centrálny register (central register of children, pupils and students) under the School Act[^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | Národný zdravotnícky informačný systém (National Health Information System), administered by the National Health Information Centre[^s34] | National Health Information Centre (NCZI, 'národné centrum')[^s34] | *Not stated in sources* | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Slov-Lex, the public administration information system administered and operated by the Ministry of Justice[^s35] | The Ministry of Justice publishes the Collection of Laws; it is issued in electronic and paper form[^s35] | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | Elektronický archív Slovenska (Electronic Archive of Slovakia), the long-term repository of electronic archival records of public authorities[^s36] | The Electronic Archive also archives structured data and data from Ministry of Interior production systems[^s36] | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | Register adries (Address Register), administered by the Ministry of Interior[^s37] | ÚGKK SR creates, administers and operates the geodesy, cartography and cadastre information system (ISGKK)[^s38] | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 29 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 29 |

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

> Not yet sized. Capacity for Slovakia will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Slovakia without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Fingerprint biometric (tier 0)
- Authentication audit log (tier 0)
- Tax (tier 1)
- Customs declarations (tier 1)
- Treasury and state accounts (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Water management control (tier 1)

---

[^s1]: Národná agentúra pre sieťové a elektronické služby (NASES) — Činnosť agentúry. Činnosť agentúry. <https://www.nases.gov.sk/o-nas/cinnost-agentury> ([archived](https://web.archive.org/web/20260928114903/https://www.nases.gov.sk/o-nas/cinnost-agentury))
[^s2]: Národná agentúra pre sieťové a elektronické služby (SNCA) — Certifikačná autorita. Certifikačná autorita. <https://snca.gov.sk/o-nas/certifikacna-autorita> ([archived](https://web.archive.org/web/20260612111428/https://snca.gov.sk/o-nas/certifikacna-autorita))
[^s3]: Národná agentúra pre sieťové a elektronické služby (slovensko.sk) — Nové elektronické občianske preukazy s čipom, 2013-12-01. Nové elektronické občianske preukazy s čipom. <https://www.slovensko.sk/sk/eid> ([archived](https://web.archive.org/web/20260218060914/https://www.slovensko.sk/sk/eid))
[^s4]: Ministerstvo investícií, regionálneho rozvoja a informatizácie SR (MIRRI) — Vládny cloud. Vládny cloud. <https://mirri.gov.sk/sekcie/informatizacia/dokumenty/vladny-cloud/>
[^s5]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s6]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s7]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s8]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s9]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s10]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o hlásení pobytu občanov Slovenskej republiky a…. Zákon o hlásení pobytu občanov Slovenskej republiky a registri obyvateľov Slovenskej republiky 253/1998. <https://zakony.judikaty.info/predpis/zakon-253/1998> ([archived](https://web.archive.org/web/20240913011250/https://zakony.judikaty.info/predpis/zakon-253/1998))
[^s11]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o občianskych preukazoch 224/2006. Zákon o občianskych preukazoch 224/2006. <https://zakony.judikaty.info/predpis/zakon-224/2006> ([archived](https://web.archive.org/web/20220307183542/https://zakony.judikaty.info/predpis/zakon-224/2006))
[^s12]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o cestovných dokladoch 647/2007. Zákon o cestovných dokladoch 647/2007. <https://zakony.judikaty.info/predpis/zakon-647/2007> ([archived](https://web.archive.org/web/20240913021636/https://zakony.judikaty.info/predpis/zakon-647/2007))
[^s13]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon Národnej rady Slovenskej republiky o matrikách…. Zákon Národnej rady Slovenskej republiky o matrikách 154/1994. <https://zakony.judikaty.info/predpis/zakon-154/1994> ([archived](https://web.archive.org/web/20240913021122/https://zakony.judikaty.info/predpis/zakon-154/1994))
[^s14]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o e-Governmente 305/2013. Zákon o e-Governmente 305/2013. <https://zakony.judikaty.info/predpis/zakon-305/2013>
[^s15]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o podmienkach výkonu volebného práva 180/2014. Zákon o podmienkach výkonu volebného práva 180/2014. <https://zakony.judikaty.info/predpis/zakon-180/2014> ([archived](https://web.archive.org/web/20240913004101/https://zakony.judikaty.info/predpis/zakon-180/2014))
[^s16]: Národná agentúra pre sieťové a elektronické služby — Kvalifikované dôveryhodné služby. Kvalifikované dôveryhodné služby. <https://www.nases.gov.sk/sluzby/sluzby-pre-po-a-ovm/doveryhodne-sluzby-snca> ([archived](https://web.archive.org/web/20260928114903/https://www.nases.gov.sk/sluzby/sluzby-pre-po-a-ovm/doveryhodne-sluzby-snca))
[^s17]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Katastrálny zákon 162/1995. Katastrálny zákon 162/1995. <https://zakony.judikaty.info/predpis/zakon-162/1995> ([archived](https://web.archive.org/web/20251008162932/https://zakony.judikaty.info/predpis/zakon-162/1995))
[^s18]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o registri trestov 330/2007. Zákon o registri trestov 330/2007. <https://zakony.judikaty.info/predpis/zakon-330/2007> ([archived](https://web.archive.org/web/20240913022235/https://zakony.judikaty.info/predpis/zakon-330/2007))
[^s19]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon Národnej rady Slovenskej republiky o Policajnom…. Zákon Národnej rady Slovenskej republiky o Policajnom zbore 171/1993. <https://zakony.judikaty.info/predpis/zakon-171/1993> ([archived](https://web.archive.org/web/20240915235127/https://zakony.judikaty.info/predpis/zakon-171/1993))
[^s20]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o pobyte cudzincov 404/2011. Zákon o pobyte cudzincov 404/2011. <https://zakony.judikaty.info/predpis/zakon-404/2011> ([archived](https://web.archive.org/web/20250624013534/https://zakony.judikaty.info/predpis/zakon-404/2011))
[^s21]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o sociálnom poistení 461/2003. Zákon o sociálnom poistení 461/2003. <https://zakony.judikaty.info/predpis/zakon-461/2003> ([archived](https://web.archive.org/web/20250624100422/https://zakony.judikaty.info/predpis/zakon-461/2003))
[^s22]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o zdravotných poisťovniach, dohľade nad zdravotnou…. Zákon o zdravotných poisťovniach, dohľade nad zdravotnou starostlivosťou 581/2004. <https://zakony.judikaty.info/predpis/zakon-581/2004>
[^s23]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o obchodnom registri 530/2003. Zákon o obchodnom registri 530/2003. <https://zakony.judikaty.info/predpis/zakon-530/2003> ([archived](https://web.archive.org/web/20250624003611/https://zakony.judikaty.info/predpis/zakon-530/2003))
[^s24]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o registri partnerov verejného sektora 315/2016. Zákon o registri partnerov verejného sektora 315/2016. <https://zakony.judikaty.info/predpis/zakon-315/2016> ([archived](https://web.archive.org/web/20240522091210/https://zakony.judikaty.info/predpis/zakon-315/2016))
[^s25]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o cestnej premávke 8/2009. Zákon o cestnej premávke 8/2009. <https://zakony.judikaty.info/predpis/zakon-8/2009> ([archived](https://web.archive.org/web/20240225121954/https://zakony.judikaty.info/predpis/zakon-8/2009))
[^s26]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o strelných zbraniach a strelive 190/2003. Zákon o strelných zbraniach a strelive 190/2003. <https://zakony.judikaty.info/predpis/zakon-190/2003> ([archived](https://web.archive.org/web/20240521050240/https://zakony.judikaty.info/predpis/zakon-190/2003))
[^s27]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o štátnej službe 55/2017. Zákon o štátnej službe 55/2017. <https://zakony.judikaty.info/predpis/zakon-55/2017>
[^s28]: Národná banka Slovenska — Platobné systémy. Platobné systémy. <https://nbs.sk/platby/platobne-systemy/> ([archived](https://web.archive.org/web/20260617103250/https://nbs.sk/platby/platobne-systemy/))
[^s29]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o integrovanom záchrannom systéme 129/2002. Zákon o integrovanom záchrannom systéme 129/2002. <https://zakony.judikaty.info/predpis/zakon-129/2002> ([archived](https://web.archive.org/web/20250624004629/https://zakony.judikaty.info/predpis/zakon-129/2002))
[^s30]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o riadení štátu v krízových situáciách mimo času…. Zákon o riadení štátu v krízových situáciách mimo času vojny a vojnového stavu 387/2002. <https://zakony.judikaty.info/predpis/zakon-387/2002>
[^s31]: Slovenská elektrizačná prenosová sústava, a. s. — Dispečing. Dispečing. <https://www.sepsas.sk/pre-partnerov/dispecing/> ([archived](https://web.archive.org/web/20260614225618/https://www.sepsas.sk/pre-partnerov/dispecing/))
[^s32]: Slovenská elektrizačná prenosová sústava, a. s. — O spoločnosti. O spoločnosti. <https://www.sepsas.sk/o-nas/o-spolocnosti/> ([archived](https://web.archive.org/web/20260516114637/https://www.sepsas.sk/o-nas/o-spolocnosti/))
[^s33]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o výchove a vzdelávaní (školský zákon) 245/2008. Zákon o výchove a vzdelávaní (školský zákon) 245/2008. <https://zakony.judikaty.info/predpis/zakon-245/2008> ([archived](https://web.archive.org/web/20240715115213/https://zakony.judikaty.info/predpis/zakon-245/2008))
[^s34]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o národnom zdravotníckom informačnom systéme 153/2013. Zákon o národnom zdravotníckom informačnom systéme 153/2013. <https://zakony.judikaty.info/predpis/zakon-153/2013> ([archived](https://web.archive.org/web/20250624093444/https://zakony.judikaty.info/predpis/zakon-153/2013))
[^s35]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o tvorbe právnych predpisov a o Zbierke zákonov…. Zákon o tvorbe právnych predpisov a o Zbierke zákonov Slovenskej republiky 400/2015. <https://zakony.judikaty.info/predpis/zakon-400/2015> ([archived](https://web.archive.org/web/20250624015208/https://zakony.judikaty.info/predpis/zakon-400/2015))
[^s36]: Ministerstvo vnútra Slovenskej republiky — Elektronický archív Slovenska MV SR. Elektronický archív Slovenska MV SR. <https://www.minv.sk/?elektronicky-archiv-slovenska-mv-sr>
[^s37]: Zákony.Judikáty.info (consolidated text of the Slovak Collection of Laws) — Zákon o registri adries 125/2015. Zákon o registri adries 125/2015. <https://zakony.judikaty.info/predpis/zakon-125/2015> ([archived](https://web.archive.org/web/20210228034237/https://zakony.judikaty.info/predpis/zakon-125/2015))
[^s38]: Úrad geodézie, kartografie a katastra Slovenskej republiky — Výročná správa ÚGKK SR za rok 2025, 2026. Výročná správa ÚGKK SR za rok 2025. <https://www.skgeodesy.sk/files/sk/slovensky/ugkk/kontrakty-vyrocne-spravy/ugkk-sr_vyrocna-sprava_2025.pdf> ([archived](https://web.archive.org/web/20260609112750/https://www.skgeodesy.sk/files/sk/slovensky/ugkk/kontrakty-vyrocne-spravy/ugkk-sr_vyrocna-sprava_2025.pdf))

**Evidence grades:** 3 Strong, 48 Standard. Strong: an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review. Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.
