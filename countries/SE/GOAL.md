# Sweden: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Sweden could be anywhere from 'Secured in law, not yet in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2] |
| State-controlled national eID | Partly[^s3] |
| Government data centres | Yes[^s4][^s5] |
| Government cloud in operation | Yes[^s6][^s5] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Sweden described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 10.59 million[^s7] |
| GDP, current prices | 600.4 EUR bn[^s8] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 97.0 EUR/MWh[^s9] |
| Renewables share of electricity | 88.1 %[^s10] |
| Land area | 407 300 km²[^s11] |

## 3. Critical data holdings, by priority

The holdings Sweden cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 16 of 39 holding classes have a verified source; 2 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Folkbokföringsverksamheten / Skatteverket's population registration data (the national population register)[^s12] | Skatteverket (Swedish Tax Agency) is responsible for population registration[^s13] | *Not stated in sources* | 10,605,529 persons registered in Sweden (2025), per folkbokföring data supplied by Skatteverket[^s14] |
| Critical | Facial biometric (tier 0) | Passregistret (passport register), which holds holders' photographs[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | No central register[^s16] | — | — | — |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Passregistret: central passport register kept by the Police Authority[^s15] | *Not yet sourced* | *Not stated in sources* | Skatteverket issues about 170,000 identity cards per year[^s17] |
| High | Digital identity credentials (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | Fastighetsregistret (real property register)[^s18] | The state cadastral authority (Lantmäteriet) is controller[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Belastningsregistret (criminal records register), Police Authority[^s19] | Courts are each controllers for court case data under Domstolsdatalag (2015:728)[^s20] | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | Röstlängd (electoral roll), drawn up by the central election authority per voting district from folkbokföring data[^s21] | *Not yet sourced* | National infrastructure[^s22] | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | Aktiebolagsregistret (companies register); Bolagsverket controller[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Registret över verkliga huvudmän, kept by Bolagsverket[^s24] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Vägtrafikregistret (road traffic register) kept by Transportstyrelsen[^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Swedish national part of the Schengen Information System, kept by the Police Authority[^s26] | Police Authority and Migrationsverket are each controllers for their processing in N.SIS[^s26] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | Vapenregistren (firearms registers) kept by the Police Authority under the new Vapenlag (2026:408)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Hermes, the state information system for budgeting and follow-up, developed and managed by ESV[^s28] | ESV is responsible for state accounts[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Each higher-education institution keeps a student register (studieregister)[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Election management and results (tier 1) | Valmyndighetens it-stöd used to compile and publish results[^s22] | *Not yet sourced* | National infrastructure[^s22] | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | Vaccinationsregistret, Folkhälsomyndigheten[^s30] | Folkhälsomyndigheten coordinates communicable disease control nationally[^s31] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 15 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 13 |

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

> Not yet sized. Capacity for Sweden will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 2 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Sweden without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Breeder document scans (tier 0)
- Digital identity credentials (tier 0)
- Authentication audit log (tier 0)
- State PKI and qualified trust services (tier 0)
- Residence and migration status (tier 1)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Police information systems (tier 1)
- Official gazette and legislation (tier 1)
- Government payroll and personnel (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Crisis management and civil protection (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

---

[^s1]: Sveriges riksdag / Regeringskansliet (SFS) — Säkerhetsskyddslag (2018:585), 2 kap. 5 §. Säkerhetsskyddslag (2018:585), 2 kap. 5 §. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/> ([archived](https://web.archive.org/web/20260906142442/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/))
[^s2]: Statens offentliga utredningar (via Sveriges riksdag) — SOU 2023:61 En säker och tillgänglig statlig e-legitimation, 2023-10-16. SOU 2023:61 En säker och tillgänglig statlig e-legitimation. <https://data.riksdagen.se/dokument/HBB361.html> ([archived](https://web.archive.org/web/20250715095543/https://data.riksdagen.se/dokument/HBB361.html))
[^s3]: Regeringen (via Sveriges riksdag) — Prop. 2025/26:250 En statlig e-legitimation, 2026-05-07. Prop. 2025/26:250 En statlig e-legitimation. <https://data.riksdagen.se/dokument/HD03250.html>
[^s4]: Statens offentliga utredningar (via Sveriges riksdag) — SOU 2021:1 Säker och kostnadseffektiv it-drift, 2021-01-18. SOU 2021:1 Säker och kostnadseffektiv it-drift. <https://data.riksdagen.se/dokument/ZZB31.html>
[^s5]: Regeringskansliet (SFS, via Sveriges riksdag) — Förordning (2024:1005) om samordnad och säker statlig…, 2024-11-07. Förordning (2024:1005) om samordnad och säker statlig it-drift. <https://data.riksdagen.se/dokument/sfs-2024-1005.html>
[^s6]: Statens offentliga utredningar (via Sveriges riksdag) — SOU 2025:13 En effektivare organisering av mindre…, 2025-02-10. SOU 2025:13 En effektivare organisering av mindre myndigheter. <https://data.riksdagen.se/dokument/HDB313.html>
[^s7]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s8]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s9]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s10]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s11]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s12]: Sveriges riksdag (Svensk författningssamling) — Folkbokföringsdatalag (2026:126), 2026. Folkbokföringsdatalag (2026:126). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingsdatalag-2026126_sfs-2026-126/> ([archived](https://web.archive.org/web/20260611073903/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingsdatalag-2026126_sfs-2026-126/))
[^s13]: Sveriges riksdag (Svensk författningssamling) — Folkbokföringslag (1991:481), 1991. Folkbokföringslag (1991:481). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingslag-1991481_sfs-1991-481/> ([archived](https://web.archive.org/web/20260913214218/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingslag-1991481_sfs-1991-481/))
[^s14]: Statistiska centralbyrån (SCB) — Sveriges befolkning, 2026-02-24. Sveriges befolkning. <https://www.scb.se/hitta-statistik/sverige-i-siffror/manniskorna-i-sverige/sveriges-befolkning/> ([archived](https://web.archive.org/web/20260921030628/https://www.scb.se/hitta-statistik/sverige-i-siffror/manniskorna-i-sverige/sveriges-befolkning/))
[^s15]: Sveriges riksdag (Svensk författningssamling) — Passförordning (1979:664), 1979. Passförordning (1979:664). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/passforordning-1979664_sfs-1979-664/> ([archived](https://web.archive.org/web/20260813145910/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/passforordning-1979664_sfs-1979-664/))
[^s16]: Sveriges riksdag (Svensk författningssamling) — Passlag (1978:302), 1978. Passlag (1978:302). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/passlag-1978302_sfs-1978-302/> ([archived](https://web.archive.org/web/20260813152209/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/passlag-1978302_sfs-1978-302/))
[^s17]: Regeringen (via Sveriges riksdag) — Prop. 2025/26:250 En statlig e-legitimation, 2026-05-07. Prop. 2025/26:250 En statlig e-legitimation. <https://data.riksdagen.se/dokument/hd03250.html>
[^s18]: Sveriges riksdag (Svensk författningssamling) — Lag (2000:224) om fastighetsregister, 2000. Lag (2000:224) om fastighetsregister. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2000224-om-fastighetsregister_sfs-2000-224/> ([archived](https://web.archive.org/web/20250210201207/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2000224-om-fastighetsregister_sfs-2000-224/))
[^s19]: Sveriges riksdag (Svensk författningssamling) — Lag (1998:620) om belastningsregister, 1998. Lag (1998:620) om belastningsregister. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1998620-om-belastningsregister_sfs-1998-620/> ([archived](https://web.archive.org/web/20260813145908/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1998620-om-belastningsregister_sfs-1998-620/))
[^s20]: Sveriges riksdag (Svensk författningssamling) — Domstolsdatalag (2015:728), 2015. Domstolsdatalag (2015:728). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/domstolsdatalag-2015728_sfs-2015-728/>
[^s21]: Sveriges riksdag (Svensk författningssamling) — Vallag (2005:837), 2005. Vallag (2005:837). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vallag-2005837_sfs-2005-837/> ([archived](https://web.archive.org/web/20260924072102/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vallag-2005837_sfs-2005-837/))
[^s22]: Valmyndigheten — Vårt it-stöd. Vårt it-stöd. <https://www.val.se/om-valmyndigheten/vart-it-stod> ([archived](https://web.archive.org/web/20260913174143/https://www.val.se/om-valmyndigheten/vart-it-stod))
[^s23]: Sveriges riksdag (Svensk författningssamling) — Aktiebolagsförordning (2005:559), 2005. Aktiebolagsförordning (2005:559). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/aktiebolagsforordning-2005559_sfs-2005-559/> ([archived](https://web.archive.org/web/20260417064235/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/aktiebolagsforordning-2005559_sfs-2005-559/))
[^s24]: Sveriges riksdag (Svensk författningssamling) — Lag (2017:631) om registrering av verkliga huvudmän, 2017. Lag (2017:631) om registrering av verkliga huvudmän. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2017631-om-registrering-av-verkliga_sfs-2017-631/> ([archived](https://web.archive.org/web/20260813171133/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2017631-om-registrering-av-verkliga_sfs-2017-631/))
[^s25]: Sveriges riksdag (Svensk författningssamling) — Vägtrafikdatalag (2019:369), 2019. Vägtrafikdatalag (2019:369). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vagtrafikdatalag-2019369_sfs-2019-369/> ([archived](https://web.archive.org/web/20260609063421/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vagtrafikdatalag-2019369_sfs-2019-369/))
[^s26]: Sveriges riksdag (Svensk författningssamling) — Lag (2021:1187) med kompletterande bestämmelser till…, 2021. Lag (2021:1187) med kompletterande bestämmelser till EU:s förordningar om Schengens informationssystem. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20211187-med-kompletterande-bestammelser_sfs-2021-1187/> ([archived](https://web.archive.org/web/20260813144455/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20211187-med-kompletterande-bestammelser_sfs-2021-1187/))
[^s27]: Sveriges riksdag (Svensk författningssamling) — Vapenlag (2026:408), 2026. Vapenlag (2026:408). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vapenlag-2026408_sfs-2026-408/> ([archived](https://web.archive.org/web/20260919075515/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vapenlag-2026408_sfs-2026-408/))
[^s28]: Sveriges riksdag (Svensk författningssamling) — Förordning (2016:1023) med instruktion för…, 2016. Förordning (2016:1023) med instruktion för Ekonomistyrningsverket. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-20161023-med-instruktion-for_sfs-2016-1023/> ([archived](https://web.archive.org/web/20250502031355/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-20161023-med-instruktion-for_sfs-2016-1023/))
[^s29]: Sveriges riksdag (Svensk författningssamling) — Förordning (1993:1153) om redovisning av studier m.m.…, 1993. Förordning (1993:1153) om redovisning av studier m.m. vid universitet och högskolor. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-19931153-om-redovisning-av-studier-m_sfs-1993-1153/> ([archived](https://web.archive.org/web/20260516085842/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-19931153-om-redovisning-av-studier-m_sfs-1993-1153/))
[^s30]: Sveriges riksdag (Svensk författningssamling) — Lag (2012:453) om register över nationella…, 2012. Lag (2012:453) om register över nationella vaccinationsprogram m.m.. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2012453-om-register-over-nationella_sfs-2012-453/> ([archived](https://web.archive.org/web/20260606164900/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2012453-om-register-over-nationella_sfs-2012-453/))
[^s31]: Sveriges riksdag (Svensk författningssamling) — Smittskyddslag (2004:168), 2004. Smittskyddslag (2004:168). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/smittskyddslag-2004168_sfs-2004-168/>
