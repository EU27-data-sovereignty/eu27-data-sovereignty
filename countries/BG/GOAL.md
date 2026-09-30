# Bulgaria: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Bulgaria could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | *Not yet sourced* |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s1][^s2] |
| State-controlled national eID | Partly[^s1][^s3] |
| Government data centres | Yes[^s4] |
| Government cloud in operation | *Not yet sourced* |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 32 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Bulgaria described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 6.44 million[^s5] |
| GDP, current prices | 116.0 EUR bn[^s6] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 141.3 EUR/MWh[^s7] |
| Renewables share of electricity | 33.8 %[^s8] |
| Land area | 110 001 km²[^s9] |

## 3. Critical data holdings, by priority

The holdings Bulgaria cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 25 of 39 holding classes have a verified source; 1 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Facial biometric (tier 0) | *Not yet sourced* | Identity documents are issued by the Ministry of Interior, Ministry of Foreign Affairs, Ministry of Transport and Communications and Ministry of Defence[^s10] | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | National Register of Bulgarian Identity Documents (automated information fund)[^s10] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Document issuance history (tier 0) | *Not yet sourced* | From 27 April 2026 the Ministry of Interior moved to centralised personalisation and a new generation of identity documents[^s11] | *Not stated in sources* | *Not yet measured* |
| High | Digital identity credentials (tier 0) | *Not yet sourced* | Access to the register is granted to persons designated by order of the Minister of Interior (MVR runs the register)[^s12] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | The Communications Regulation Commission creates, maintains and publishes the national Trusted List[^s1] | Qualified trust service providers on the Bulgarian Trusted List: Borica AD, Evrotrust Technologies AD, InfoNotary EAD, Information Services AD and Idocs Bulgaria EOOD[^s1] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet sourced* | Criminal-record bureaus at every district court and a Central Criminal Records Bureau at the Ministry of Justice[^s13] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | *Not yet sourced* | Migration Directorate of MVR and Migration units of the regional MVR directorates (Foreigners in the Republic of Bulgaria Act)[^s14] | *Not stated in sources* | *Not yet measured* |
| High | Tax (tier 1) | Tax and Social Security Procedure Code: NRA creates and maintains the register and databases of obliged persons[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | The new Customs Import Information System (MISV) went into production on 26.11.2018[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Benefits & pensions (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Statutory health insurance (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | AGCC creates and maintains the cadastral map and cadastral registers for the whole country under the Cadastre and Property Register Act[^s17] | The Registry Agency (executive agency under the Minister of Justice) keeps the property register, commercial register, BULSTAT and other registers[^s18] | National infrastructure[^s18] | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | The software change enabling beneficial-owner entries went live on 28.01.2019[^s18] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Firearms register (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | SEBRA (System for Electronic Budget Payments) is used to initiate payments of budget organisations[^s19] | BORICA AD transforms approved SEBRA payments into ISO 20022 XML[^s19] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | BG-ALERT public warning system over mobile networks (Cell Broadcast)[^s20] | Developed jointly by MVR and the Ministry of e-Government[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | Project to modernise and extend the SCADA/EMS and information environment in ESO's Central Dispatch (CDU)[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Register of all current, interrupted and graduated students and doctoral candidates, kept as an electronic database through NACID[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | The NHIS holds an electronic health record for every citizen[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Business registry (tier 1) | The Commercial Register and Register of Non-Profit Legal Entities is a common electronic database[^s18] | *Not yet sourced* | National infrastructure[^s18] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | The State Gazette website provides the full content of all issues for the last 7 years in PDF (EU N-Lex description)[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | 2021 Population and Housing Census, the 18th in Bulgaria (census site of the National Statistical Institute)[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Geospatial base data (tier 3) | AGCC creates and maintains the topographic databases and the geo-information system[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 25 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 23 |

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

> Not yet sized. Capacity for Bulgaria will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 1 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Bulgaria without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Civil registry core (tier 0)
- Electoral roll entry (tier 0)
- Vehicle & licensing (tier 1)
- Police information systems (tier 1)
- Border and visa systems (tier 1)
- Government payroll and personnel (tier 1)
- Election management and results (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Water management control (tier 1)

---

[^s1]: Комисия за регулиране на съобщенията — Електронни удостоверителни услуги. Електронни удостоверителни услуги. <https://crc.bg/bg/rubriki/560/elektronni-udostoveritelni-uslugi>
[^s2]: Информационно обслужване АД — Информационно обслужване АД – Доклад за дейността 2024…, 2025. Информационно обслужване АД – Доклад за дейността 2024 (Annual activity report 2024). <https://www.is-bg.net/upload/4944/IS_2024_%D0%94%D0%BE%D0%BA%D0%BB%D0%B0%D0%B4%20%D0%B7%D0%B0%20%D0%B4%D0%B5%D0%B9%D0%BD%D0%BE%D1%81%D1%82%D1%82%D0%B0.pdf>
[^s3]: Вестник „Сега“ — Отпада едно от безумията за личните карти с чип, 2026-09-19. Отпада едно от безумията за личните карти с чип. <https://www.segabg.com/hot/category-consult/otpada-edno-bezumiyata-za-lichnite-karti-chip> ([archived](https://web.archive.org/web/20260925122111/https://www.segabg.com/hot/category-consult/otpada-edno-bezumiyata-za-lichnite-karti-chip))
[^s4]: Информационно обслужване АД — Инфраструктура. Инфраструктура. <https://www.is-bg.net/bg/solutions/infrastructure>
[^s5]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s6]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s7]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s8]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s9]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s10]: Държавна агенция за бежанците (копие на закона) — Закон за българските лични документи (консолидиран текст), 2024. Закон за българските лични документи (консолидиран текст). <https://aref.government.bg/sites/default/files/2024-04/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B1%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D1%82%D0%B5%20%D0%BB%D0%B8%D1%87%D0%BD%D0%B8%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B8.pdf> ([archived](https://web.archive.org/web/20260315085009/https://aref.government.bg/sites/default/files/2024-04/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B1%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D1%82%D0%B5%20%D0%BB%D0%B8%D1%87%D0%BD%D0%B8%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B8.pdf))
[^s11]: Министерство на вътрешните работи – ОДМВР София — Въвеждане на ново поколение български лични документи, 2026-04-27. Въвеждане на ново поколение български лични документи. <https://mvr.bg/sofia/%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D0%BD-%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BF%D1%80%D0%B5%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/90242> ([archived](https://web.archive.org/web/20260427064743/https://mvr.bg/sofia/%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B5%D0%BD-%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BF%D1%80%D0%B5%D1%81%D1%86%D0%B5%D0%BD%D1%82%D1%8A%D1%80/%D0%BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%B8/90242))
[^s12]: Министерство на транспорта и съобщенията (копие на правилника) — Правилник за прилагане на Закона за електронната…, 2017. Правилник за прилагане на Закона за електронната идентификация. <https://www.mtc.government.bg/sites/default/files/pravilnik_za_prilagane_na_zakona_za_elektronnata_identifikaciq.pdf> ([archived](https://web.archive.org/web/20240719053301/https://www.mtc.government.bg/sites/default/files/pravilnik_za_prilagane_na_zakona_za_elektronnata_identifikaciq.pdf))
[^s13]: Комисия за финансов надзор (копие на наредбата, актуално към 01.01.2022) — Наредба № 8 от 26.02.2008 г. за функциите и…, 2022. Наредба № 8 от 26.02.2008 г. за функциите и организацията на дейността на бюрата за съдимост. <https://www.fsc.bg/wp-content/uploads/2021/files/31563_file.pdf> ([archived](https://web.archive.org/web/20240909150602/https://www.fsc.bg/wp-content/uploads/2021/files/31563_file.pdf))
[^s14]: Министерство на външните работи (копие на закона) — Закон за чужденците в Република България. Закон за чужденците в Република България. <https://www.mfa.bg/upload/138160/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D1%87%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D1%82%D0%B5%20%D0%B2%20%D0%A0%D0%B5%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%B0%20%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D0%B8%D1%8F.pdf>
[^s15]: Министерство на вътрешните работи (копие на кодекса) — Данъчно-осигурителен процесуален кодекс. Данъчно-осигурителен процесуален кодекс. <https://www.mvr.bg/upload/296043/%D0%94%D0%9E%D0%9F%D0%9A.pdf>
[^s16]: Българска търговско-промишлена палата – Инфобизнес — Въвеждане в реална експлоатация на нова Митническа…, 2018-11-26. Въвеждане в реална експлоатация на нова Митническа информационна система за внасяне (МИСВ) на Агенция „Митници“. <https://www.infobusiness.bcci.bg/customs-26-11-18.html>
[^s17]: Агенция по геодезия, картография и кадастър — Функции на АГКК. Функции на АГКК. <https://www.cadastre.bg/funkcii-na-agkk>
[^s18]: Сметна палата на Република България — Одитен доклад № 0300101019 – Ефективност на…, 2021-08-05. Одитен доклад № 0300101019 – Ефективност на организацията и контрола на дейностите по водене и съхраняване на поддържаните от Агенцията по вписванията регистри. <https://www.bulnao.government.bg/media/documents/OD_AV_230821.pdf> ([archived](https://web.archive.org/web/20250714123738/https://www.bulnao.government.bg/media/documents/OD_AV_230821.pdf))
[^s19]: Министерство на финансите – дирекция „Държавно съкровище“ (публикувано от БНБ) — ДДС № 03/03.05.2023 г. – Изисквания за структурата,…, 2023-05-03. ДДС № 03/03.05.2023 г. – Изисквания за структурата, формата и съдържанието на платежни документи ... чрез СЕБРА. <https://www.bnb.bg/bnbweb/groups/public/documents/bnb_law/instructions_bnb_51681_bg.pdf> ([archived](https://web.archive.org/web/20250527084951/https://www.bnb.bg/bnbweb/groups/public/documents/bnb_law/instructions_bnb_51681_bg.pdf))
[^s20]: Вестник „Сега“ — МВР ще издирва бандити чрез BG-ALERT, 2026-01-07. МВР ще издирва бандити чрез BG-ALERT. <https://www.segabg.com/hot/category-bulgaria/mvr-shte-izdirva-banditi-chrez-bg-alert> ([archived](https://web.archive.org/web/20260122112807/https://www.segabg.com/hot/category-bulgaria/mvr-shte-izdirva-banditi-chrez-bg-alert))
[^s21]: Електроенергиен системен оператор ЕАД — Модернизация и Разширение на Системата SCADA/EMS и…, 2016-01-20. Модернизация и Разширение на Системата SCADA/EMS и Информационната среда в ЦДУ на ЕСО – предварително обявление. <https://www.eso.bg/fileObj.php?oid=131>
[^s22]: НАЦИД — Регистър на студенти и докторанти. Регистър на студенти и докторанти. <https://nacid.bg/bg/register_rdpzsd/>
[^s23]: Национална здравноосигурителна каса (копие на закона) — Закон за здравето. Закон за здравето. <https://www.nhif.bg/upload/30458/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD%20%D0%B7%D0%B0%20%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%B5%D1%82%D0%BE.pdf>
[^s24]: Европейска комисия / Службата за публикации на ЕС (N-Lex) — За националната база данни – България. За националната база данни – България. <https://n-lex.europa.eu/n-lex/info/info-bg/index?lang=bg> ([archived](https://web.archive.org/web/20250629165146/https://n-lex.europa.eu/n-lex/info/info-bg/index?lang=bg))
[^s25]: Национален статистически институт — Преброяване 2021. Преброяване 2021. <https://census2021.bg/> ([archived](https://web.archive.org/web/20260717163802/https://census2021.bg/))

**Evidence grades:** 4 Strong, 30 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review. Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.
