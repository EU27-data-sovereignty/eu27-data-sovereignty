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
| Classification in law | Yes[^s1][^s2] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s3] |
| State-controlled national eID | Partly[^s4] |
| Government data centres | Yes[^s5][^s6] |
| Government cloud in operation | Yes[^s7][^s6] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 31 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Sweden described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 10.61 million[^s8] |
| GDP, current prices | 600.4 EUR bn[^s9] |
| Public administration employment (NACE O) | 245.0 thousand[^s10] |
| Non-household electricity price | 97.0 EUR/MWh[^s11] |
| Renewables share of electricity | 89.2 %[^s12] |
| Land area | 407 300 km²[^s13] |

## 3. Critical data holdings, by priority

The holdings Sweden cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 24 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | Folkbokföringsverksamheten / Skatteverket's population registration data (the national population register)[^s14] | Skatteverket (Swedish Tax Agency) is responsible for population registration[^s15][^s16] | *Not stated in sources* | 10 610 500 persons folkbokförda (registered) at mid-year 2026[^s17] |
| Critical | Facial biometric (tier 0) | Passregistret (passport register), which holds holders' photographs[^s18][^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | *Disputed: sources disagree. Sveriges riksdag (Svensk författningssamling) — Passlag (1978:302), 1978 gives the value this report printed; Regeringskansliet (SFS) — Lag (2018:1693) om polisens behandling av…, 2026 gives “Biometriregister (biometric registers) of suspects, convicted persons and traces, kept by Polismyndigheten”. Neither is higher-tier or a later statement of the same authority, so both are shown and neither is printed as fact* | — | — | — |
| Critical | Breeder document scans (tier 0) | Folkbokföring (population registration of births, marriages and deaths), Skatteverket[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | Passregistret: central passport register kept by the Police Authority[^s18][^s19] | *Not yet sourced* | *Not stated in sources* | Skatteverket issues about 170,000 identity cards per year[^s21] |
| High | Digital identity credentials (tier 0) | Registret över ärenden om statlig e-legitimation (register of state e-ID cases)[^s22] | Polismyndigheten (Swedish Police Authority)[^s22] | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Land & property registry (tier 1) | Fastighetsregistret (real property register)[^s23][^s24] | The state cadastral authority (Lantmäteriet) is controller[^s23][^s24] | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Belastningsregistret (criminal records register), Police Authority[^s25][^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Misstankeregistret (register of suspects), Polismyndigheten[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electoral roll entry (tier 0) | Röstlängd (electoral roll), drawn up by the central election authority per voting district from folkbokföring data[^s28] | *Not yet sourced* | National infrastructure[^s29] | *Not yet measured* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Tax (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Business registry (tier 1) | Aktiebolagsregistret (companies register); Bolagsverket controller[^s30][^s31] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Beneficial ownership register (tier 1) | Registret över verkliga huvudmän, kept by Bolagsverket[^s32][^s33] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Vägtrafikregistret (road traffic register) kept by Transportstyrelsen[^s34][^s35] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Border and visa systems (tier 1) | Swedish national part of the Schengen Information System, kept by the Police Authority[^s36] | Police Authority and Migrationsverket are each controllers for their processing in N.SIS[^s36] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Hermes, the state information system for budgeting and follow-up, developed and managed by ESV[^s37] | ESV is responsible for state accounts[^s37] | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Primula (Statens servicecenter)[^s7] | Statens servicecenter (SSC), payroll services to 143 agencies in 2023[^s7] | *Not stated in sources* | about 1,5 million payslips (lönespecifikationer) per year[^s7] |
| High | Central bank systems (tier 1) | RIX-RTGS (Riksbank's large-value payment settlement system)[^s38] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | Rakel (national public-safety radio communication system)[^s39] | Myndigheten för civilt försvar (Swedish Civil Defence Agency)[^s39] | *Not stated in sources* | *Not yet measured* |
| High | Crisis management and civil protection (tier 1) | Systemet för varning och information till allmänheten (public warning and information system)[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | Each higher-education institution keeps a student register (studieregister)[^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | Svensk författningssamling (SFS, Swedish Code of Statutes), published electronically on a dedicated website[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Election management and results (tier 1) | Valmyndighetens it-stöd used to compile and publish results[^s29] | *Not yet sourced* | National infrastructure[^s29] | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | Vaccinationsregistret, Folkhälsomyndigheten[^s43][^s44] | Folkhälsomyndigheten coordinates communicable disease control nationally[^s45][^s46] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet verified* | *—* | *—* | *—* |

## 4. Foreign-dependency exposure

Of the 23 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 2 |
| EU provider | 0 |
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

> Not yet sized. Capacity for Sweden will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Sweden without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Authentication audit log (tier 0)
- State PKI and qualified trust services (tier 0)
- Residence and migration status (tier 1)
- Tax (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Statutory health insurance (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)

---

[^s1]: Regeringskansliet (SFS) — Säkerhetsskyddsförordning (2021:955), 2026. Säkerhetsskyddsförordning (2021:955). <https://data.riksdagen.se/dokument/sfs-2021-955.html> ([archived](https://web.archive.org/web/20260519033902/https://data.riksdagen.se/dokument/sfs-2021-955.html))
[^s2]: Sveriges riksdag / Regeringskansliet (SFS) — Säkerhetsskyddslag (2018:585), 2 kap. 5 §. Säkerhetsskyddslag (2018:585), 2 kap. 5 §. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/> ([archived](https://web.archive.org/web/20260906142442/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/sakerhetsskyddslag-2018585_sfs-2018-585/))
[^s3]: Statens offentliga utredningar (via Sveriges riksdag) — SOU 2023:61 En säker och tillgänglig statlig e-legitimation, 2023-10-16. SOU 2023:61 En säker och tillgänglig statlig e-legitimation. <https://data.riksdagen.se/dokument/HBB361.html> ([archived](https://web.archive.org/web/20250715095543/https://data.riksdagen.se/dokument/HBB361.html))
[^s4]: Regeringen (via Sveriges riksdag) — Prop. 2025/26:250 En statlig e-legitimation, 2026-05-07. Prop. 2025/26:250 En statlig e-legitimation. <https://data.riksdagen.se/dokument/HD03250.html>
[^s5]: Statens offentliga utredningar (via Sveriges riksdag) — SOU 2021:1 Säker och kostnadseffektiv it-drift, 2021-01-18. SOU 2021:1 Säker och kostnadseffektiv it-drift. <https://data.riksdagen.se/dokument/ZZB31.html>
[^s6]: Regeringskansliet (SFS, via Sveriges riksdag) — Förordning (2024:1005) om samordnad och säker statlig…, 2024-11-07. Förordning (2024:1005) om samordnad och säker statlig it-drift. <https://data.riksdagen.se/dokument/sfs-2024-1005.html>
[^s7]: Statens offentliga utredningar (via Sveriges riksdag) — SOU 2025:13 En effektivare organisering av mindre…, 2025-02-10. SOU 2025:13 En effektivare organisering av mindre myndigheter. <https://data.riksdagen.se/dokument/HDB313.html>
[^s8]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s9]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s10]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s11]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s12]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s13]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s14]: Sveriges riksdag (Svensk författningssamling) — Folkbokföringsdatalag (2026:126), 2026. Folkbokföringsdatalag (2026:126). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingsdatalag-2026126_sfs-2026-126/> ([archived](https://web.archive.org/web/20260611073903/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingsdatalag-2026126_sfs-2026-126/))
[^s15]: Regeringskansliet (SFS) — Folkbokföringsdatalag (2026:126), 2026-02-26. Folkbokföringsdatalag (2026:126). <https://data.riksdagen.se/dokument/sfs-2026-126.html>
[^s16]: Sveriges riksdag (Svensk författningssamling) — Folkbokföringslag (1991:481), 1991. Folkbokföringslag (1991:481). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingslag-1991481_sfs-1991-481/> ([archived](https://web.archive.org/web/20260913214218/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/folkbokforingslag-1991481_sfs-1991-481/))
[^s17]: Statistiska centralbyrån (SCB) — Befolkningsstatistik, 2026-08-21. Befolkningsstatistik. <https://www.scb.se/hitta-statistik/statistik-efter-amne/befolkning-och-levnadsforhallanden/befolkningens-sammansattning-och-utveckling/befolkningsstatistik/> ([archived](https://web.archive.org/web/20260914063708/https://www.scb.se/hitta-statistik/statistik-efter-amne/befolkning-och-levnadsforhallanden/befolkningens-sammansattning-och-utveckling/befolkningsstatistik/))
[^s18]: Regeringskansliet (SFS) — Passförordning (1979:664), 2026. Passförordning (1979:664). <https://data.riksdagen.se/dokument/sfs-1979-664.html>
[^s19]: Sveriges riksdag (Svensk författningssamling) — Passförordning (1979:664), 1979. Passförordning (1979:664). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/passforordning-1979664_sfs-1979-664/> ([archived](https://web.archive.org/web/20260813145910/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/passforordning-1979664_sfs-1979-664/))
[^s20]: Regeringskansliet (SFS) — Folkbokföringslag (1991:481), 2026. Folkbokföringslag (1991:481). <https://data.riksdagen.se/dokument/sfs-1991-481.html> ([archived](https://web.archive.org/web/20251208011308/https://data.riksdagen.se/dokument/sfs-1991-481.html))
[^s21]: Regeringen (via Sveriges riksdag) — Prop. 2025/26:250 En statlig e-legitimation, 2026-05-07. Prop. 2025/26:250 En statlig e-legitimation. <https://data.riksdagen.se/dokument/hd03250.html>
[^s22]: Regeringskansliet (SFS) — Lag (2026:1358) om statlig e-legitimation och…, 2026-06-18. Lag (2026:1358) om statlig e-legitimation och elektronisk identifiering. <https://data.riksdagen.se/dokument/sfs-2026-1358.html>
[^s23]: Regeringskansliet (SFS) — Förordning (2000:308) om fastighetsregister. Förordning (2000:308) om fastighetsregister. <https://data.riksdagen.se/dokument/sfs-2000-308.html>
[^s24]: Sveriges riksdag (Svensk författningssamling) — Lag (2000:224) om fastighetsregister, 2000. Lag (2000:224) om fastighetsregister. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2000224-om-fastighetsregister_sfs-2000-224/> ([archived](https://web.archive.org/web/20250210201207/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2000224-om-fastighetsregister_sfs-2000-224/))
[^s25]: Polismyndigheten — Belastningsregistret - begära utdrag. Belastningsregistret - begära utdrag. <https://polisen.se/tjanster-tillstand/belastningsregistret/> ([archived](https://web.archive.org/web/20260912120459/https://polisen.se/tjanster-tillstand/belastningsregistret/))
[^s26]: Sveriges riksdag (Svensk författningssamling) — Lag (1998:620) om belastningsregister, 1998. Lag (1998:620) om belastningsregister. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1998620-om-belastningsregister_sfs-1998-620/> ([archived](https://web.archive.org/web/20260813145908/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1998620-om-belastningsregister_sfs-1998-620/))
[^s27]: Regeringskansliet (SFS) — Lag (1998:621) om misstankeregister, 2026. Lag (1998:621) om misstankeregister. <https://data.riksdagen.se/dokument/sfs-1998-621.html>
[^s28]: Sveriges riksdag (Svensk författningssamling) — Vallag (2005:837), 2005. Vallag (2005:837). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vallag-2005837_sfs-2005-837/> ([archived](https://web.archive.org/web/20260924072102/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vallag-2005837_sfs-2005-837/))
[^s29]: Valmyndigheten — Vårt it-stöd. Vårt it-stöd. <https://www.val.se/om-valmyndigheten/vart-it-stod> ([archived](https://web.archive.org/web/20260913174143/https://www.val.se/om-valmyndigheten/vart-it-stod))
[^s30]: Regeringskansliet (SFS) — Aktiebolagslag (2005:551), 2026. Aktiebolagslag (2005:551). <https://data.riksdagen.se/dokument/sfs-2005-551.html> ([archived](https://web.archive.org/web/20230328035707/https://data.riksdagen.se/dokument/sfs-2005-551.html))
[^s31]: Sveriges riksdag (Svensk författningssamling) — Aktiebolagsförordning (2005:559), 2005. Aktiebolagsförordning (2005:559). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/aktiebolagsforordning-2005559_sfs-2005-559/> ([archived](https://web.archive.org/web/20260417064235/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/aktiebolagsforordning-2005559_sfs-2005-559/))
[^s32]: Regeringskansliet (SFS) — Lag (2017:631) om registrering av verkliga huvudmän, 2026. Lag (2017:631) om registrering av verkliga huvudmän. <https://data.riksdagen.se/dokument/sfs-2017-631.html>
[^s33]: Sveriges riksdag (Svensk författningssamling) — Lag (2017:631) om registrering av verkliga huvudmän, 2017. Lag (2017:631) om registrering av verkliga huvudmän. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2017631-om-registrering-av-verkliga_sfs-2017-631/> ([archived](https://web.archive.org/web/20260813171133/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2017631-om-registrering-av-verkliga_sfs-2017-631/))
[^s34]: Sveriges riksdag (Svensk författningssamling) — Vägtrafikdatalag (2019:369), 2019. Vägtrafikdatalag (2019:369). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vagtrafikdatalag-2019369_sfs-2019-369/> ([archived](https://web.archive.org/web/20260609063421/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/vagtrafikdatalag-2019369_sfs-2019-369/))
[^s35]: Transportstyrelsen — Fordonsdata från vägtrafikregistret. Fordonsdata från vägtrafikregistret. <https://www.transportstyrelsen.se/sv/vagtrafik/fordon/fordons-agaruppgift/uttag-av-fordonsdata-pa-fil/fordonsdata-fran-vagtrafikregistret/> ([archived](https://web.archive.org/web/20260930160034/https://www.transportstyrelsen.se/sv/vagtrafik/fordon/fordons-agaruppgift/uttag-av-fordonsdata-pa-fil/fordonsdata-fran-vagtrafikregistret/))
[^s36]: Sveriges riksdag (Svensk författningssamling) — Lag (2021:1187) med kompletterande bestämmelser till…, 2021. Lag (2021:1187) med kompletterande bestämmelser till EU:s förordningar om Schengens informationssystem. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20211187-med-kompletterande-bestammelser_sfs-2021-1187/> ([archived](https://web.archive.org/web/20260813144455/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-20211187-med-kompletterande-bestammelser_sfs-2021-1187/))
[^s37]: Sveriges riksdag (Svensk författningssamling) — Förordning (2016:1023) med instruktion för…, 2016. Förordning (2016:1023) med instruktion för Ekonomistyrningsverket. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-20161023-med-instruktion-for_sfs-2016-1023/> ([archived](https://web.archive.org/web/20250502031355/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-20161023-med-instruktion-for_sfs-2016-1023/))
[^s38]: Sveriges riksbank — Betalningssystemet RIX. Betalningssystemet RIX. <https://www.riksbank.se/sv/betalningar--kontanter/betalningssystemet-rix/>
[^s39]: Myndigheten för civilt försvar — Rakel. Rakel. <https://www.mcf.se/sv/amnesomraden/samhallsviktiga-kommunikationstjanster/rakel/> ([archived](https://web.archive.org/web/20260915155037/https://www.mcf.se/sv/amnesomraden/samhallsviktiga-kommunikationstjanster/rakel/))
[^s40]: Regeringskansliet (SFS) — Förordning (2008:1002) med instruktion för Myndigheten…, 2026. Förordning (2008:1002) med instruktion för Myndigheten för civilt försvar. <https://data.riksdagen.se/dokument/sfs-2008-1002.html> ([archived](https://web.archive.org/web/20230228040108/https://data.riksdagen.se/dokument/sfs-2008-1002.html))
[^s41]: Sveriges riksdag (Svensk författningssamling) — Förordning (1993:1153) om redovisning av studier m.m.…, 1993. Förordning (1993:1153) om redovisning av studier m.m. vid universitet och högskolor. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-19931153-om-redovisning-av-studier-m_sfs-1993-1153/> ([archived](https://web.archive.org/web/20260516085842/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/forordning-19931153-om-redovisning-av-studier-m_sfs-1993-1153/))
[^s42]: Regeringskansliet (SFS) — Lag (1976:633) om kungörande av lagar och andra…. Lag (1976:633) om kungörande av lagar och andra författningar. <https://data.riksdagen.se/dokument/sfs-1976-633.html>
[^s43]: Folkhälsomyndigheten — Nationella vaccinationsregistret. Nationella vaccinationsregistret. <https://www.folkhalsomyndigheten.se/vara-amnesomraden/vaccinationer/nationella-vaccinationsregistret/> ([archived](https://web.archive.org/web/20260907024120/https://www.folkhalsomyndigheten.se/vara-amnesomraden/vaccinationer/nationella-vaccinationsregistret/))
[^s44]: Sveriges riksdag (Svensk författningssamling) — Lag (2012:453) om register över nationella…, 2012. Lag (2012:453) om register över nationella vaccinationsprogram m.m.. <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2012453-om-register-over-nationella_sfs-2012-453/> ([archived](https://web.archive.org/web/20260606164900/https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2012453-om-register-over-nationella_sfs-2012-453/))
[^s45]: Regeringskansliet (SFS) — Förordning (2021:248) med instruktion för…, 2026. Förordning (2021:248) med instruktion för Folkhälsomyndigheten. <https://data.riksdagen.se/dokument/sfs-2021-248.html>
[^s46]: Sveriges riksdag (Svensk författningssamling) — Smittskyddslag (2004:168), 2004. Smittskyddslag (2004:168). <https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/smittskyddslag-2004168_sfs-2004-168/>

**Evidence grades:** 1 Strong, 45 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
