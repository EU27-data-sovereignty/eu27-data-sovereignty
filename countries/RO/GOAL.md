# Romania: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Romania could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2][^s3] |
| State-controlled national eID | Yes[^s4][^s5][^s6] |
| Government data centres | *Not yet sourced* |
| Government cloud in operation | Partly[^s7][^s8] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 34 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Romania described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 19.04 million[^s9] |
| GDP, current prices | 380.1 EUR bn[^s10] |
| Public administration employment (NACE O) | 409.7 thousand[^s11] |
| Non-household electricity price | 188.7 EUR/MWh[^s12] |
| Renewables share of electricity | 49.9 %[^s13] |
| Land area | 234 270 km²[^s14] |

## 3. Critical data holdings, by priority

The holdings Romania cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 15 of 39 holding classes have a verified source; 0 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Facial biometric (tier 0) | Facial image and fingerprints are collected when the electronic identity card (CEI) is issued[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Breeder document scans (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| Critical | Authentication audit log (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Document issuance history (tier 0) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | ROeID is Romania's Single Sign-On solution. It generates and manages digital identities for all Romanian citizens.[^s6] | ROeID was implemented by the Authority for the Digitalization of Romania (ADR)[^s6] | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | The Electoral Register is a national IT system. It records identification data of Romanian citizens with voting rights and their polling station assignment.[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | Documents signed with the MAI-issued advanced signature certificate on the CEI have the same value as handwritten signatures[^s15] | The MAI IT directorate (DGCTI) manages the Central PKI Certification Authority and the certification authority of the MAI central apparatus[^s17] | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Police information systems (tier 1) | Romania set up the National Alerts IT System (SINS). It holds alerts of national and Schengen interest issued by national authorities.[^s18] | The Ministry of Internal Affairs, through its specialised structure, is the central public authority that manages SINS. It is responsible for the system's functioning and the integrity of its alerts.[^s18] | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Residence and migration status (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Tax (tier 1) | ANAF is consolidating its central database through a Big-Data project[^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Customs declarations (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Benefits & pensions (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Statutory health insurance (tier 1) | SIUI is the health insurance IT platform, run by CNAS[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Vehicle & licensing (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Border and visa systems (tier 1) | Council Decision 2017/1908 gave Romania access to the Visa Information System (VIS)[^s21] | Centrul Național SIS is a structure within, or subordinated to, the Ministry of Internal Affairs[^s22] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Government payroll and personnel (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Election management and results (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Central bank systems (tier 1) | BNR operates the financial market infrastructures ReGIS, SaFIR and TARGET-România[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Electricity grid control (tier 1) | Operational control of the national power system is ensured by the National Energy Dispatch and five territorial dispatch centres[^s24] | Transelectrica is responsible for keeping the national power system running safely at all times[^s24] | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | WATMAN is the IT system for integrated water management, aimed at flood prevention[^s25] | The WATMAN project beneficiary is the National Administration Romanian Waters (total investment EUR 63 million)[^s25] | *Not stated in sources* | *Not yet measured* |
| High | Education (tier 1) | The new integrated system will bring together data from existing platforms such as SIIIR, PMIPN and Edusal[^s26] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Health records (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Official gazette and legislation (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Public health surveillance (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | National archives (digital) (tier 3) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | The ANCPI Geoportal is one of the online platforms ANCPI manages[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 15 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 0 |
| EU provider | 0 |
| Mixed | 0 |
| Non-EU provider | 0 |
| Not stated in sources | 15 |

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

> Not yet sized. Capacity for Romania will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 0 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Romania without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Civil registry core (tier 0)
- Fingerprint biometric (tier 0)
- Breeder document scans (tier 0)
- Document issuance history (tier 0)
- Authentication audit log (tier 0)
- Residence and migration status (tier 1)
- Customs declarations (tier 1)
- Benefits & pensions (tier 1)
- Business registry (tier 1)
- Beneficial ownership register (tier 1)
- Vehicle & licensing (tier 1)
- Judicial & criminal justice (tier 1)
- Firearms register (tier 1)
- Official gazette and legislation (tier 1)
- Treasury and state accounts (tier 1)
- Election management and results (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Crisis management and civil protection (tier 1)

## Appendix: fact check

### What was checked, and by whom

> Machine-checked, not human-verified. Automated agents found these sources and checked them mechanically; no person has reviewed the findings. English wording of a non-English source is a machine translation or a machine summary of the quoted text. Treat each fact as a lead to its cited source, not as established. Corrections are welcome through the repository's issue template. The check below is made by a second model, not by a person.

Every printed fact is put, exactly as printed, to a checker that is a different model from the one that wrote it. The checker fetches the cited source and decides whether it supports the statement as printed: the same value, name, unit, date, country and scope. A production deploy is refused unless every printed fact has a current verdict of supported from an eligible checker.

In this build, 0 of 1390 printed facts pass.

| Fact written by | Checked by |
|---|---|
| claude-opus-5-5 | claude-fable-5-1 |
| claude-fable-5-1 | claude-opus-5-5 |
| anything else: unrecorded, a person, or a program | claude-fable-5-1 |

### How a check runs

- factcheck.py prepare lists every printed fact whose verdict is missing, stale or not passing, hashes each as printed, names its author from the recorded files, and assigns the checker by the rule.
- The checked-in workflow (model/research/factcheck/workflow.js) asks for that checker model by name, one agent per batch of one state's facts. The checker fetches each cited page (or the Eurostat API response), looks for the quote, and decides whether it supports the statement exactly as printed: value, unit, date, country and scope. It answers supported, not supported or unclear, with a reason.
- factcheck.py stage refuses any batch whose checker reports a different model than the one asked for, or is an author of a fact in it.
- factcheck.py record writes the verdicts to the ledger, the run's manifest (input, workflow and bundle hashes, commit, counts) and this audit file.
- Before every production deploy, factcheck.py gate requires a current supported verdict from an eligible checker for every printed fact, and this file to be current. A disagreement blocks the deploy until the fact or its source is fixed and checked again; nothing is changed automatically.

A verdict holds for one fact exactly as printed: a SHA-256 of the claim, the question it answers, the printed text and every citation behind it. If any of these changes, the verdict lapses and the fact must be checked again before the next deploy.

### Fact-check runs

No fact-check run has been recorded yet, so no printed fact has been checked.

### The verdict on each fact about Romania

0 of 29 printed facts about Romania pass.

| Claim | What it answers | Written by | Checked by | Verdict | Run |
|---|---|---|---|---|---|
| indicator:RO:L2 | indicator L2: Is the government's data classification scheme established in a statute or binding regulation? | unrecorded | none | never checked |  |
| indicator:RO:K1 | indicator K1: Is the root of the government's public key infrastructure or its qualified trust service operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:RO:K2 | indicator K2: Is the national electronic identity scheme operated by the state or a state-controlled body? | unrecorded | none | never checked |  |
| indicator:RO:C2 | indicator C2: Is a national sovereign or government cloud platform in operation (not announced)? | unrecorded | none | never checked |  |
| param:RO:population_m | param:RO:population_m | program:fetch_eurostat.py | none | never checked |  |
| param:RO:gdp_eur_bn | param:RO:gdp_eur_bn | program:fetch_eurostat.py | none | never checked |  |
| param:RO:gov_employment_k | param:RO:gov_employment_k | program:fetch_eurostat.py | none | never checked |  |
| param:RO:elec_price_eur_mwh | param:RO:elec_price_eur_mwh | program:fetch_eurostat.py | none | never checked |  |
| param:RO:renewables_pct | param:RO:renewables_pct | program:fetch_eurostat.py | none | never checked |  |
| param:RO:land_km2 | param:RO:land_km2 | program:fetch_eurostat.py | none | never checked |  |
| record:RO:facial_biometric:register | Facial biometric: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:digital_identity_credentials:register | Digital identity credentials: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:digital_identity_credentials:operator | Digital identity credentials: the body that operates it | unrecorded | none | never checked |  |
| record:RO:electoral_roll:register | Electoral roll entry: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:trust_services_pki:register | State PKI and qualified trust services: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:trust_services_pki:operator | State PKI and qualified trust services: the body that operates it | unrecorded | none | never checked |  |
| record:RO:police_records:register | Police information systems: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:police_records:operator | Police information systems: the body that operates it | unrecorded | none | never checked |  |
| record:RO:tax:register | Tax: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:health_insurance:register | Statutory health insurance: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:border_control:register | Border and visa systems: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:border_control:operator | Border and visa systems: the body that operates it | unrecorded | none | never checked |  |
| record:RO:central_bank:register | Central bank systems: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:grid_control:register | Electricity grid control: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:grid_control:operator | Electricity grid control: the body that operates it | unrecorded | none | never checked |  |
| record:RO:water_control:register | Water management control: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:water_control:operator | Water management control: the body that operates it | unrecorded | none | never checked |  |
| record:RO:education:register | Education: the name of the register or system | unrecorded | none | never checked |  |
| record:RO:geospatial:register | Geospatial base data: the name of the register or system | unrecorded | none | never checked |  |

---

[^s1]: Serviciul Român de Informații (republishing the statute) — Legea nr. 182/2002 privind protecția informațiilor…, 2002-04-12. Legea nr. 182/2002 privind protecția informațiilor clasificate (Art. 18). <https://www.sri.ro/assets/files/legislatie/2024/Lege_182.2002.pdf> ([archived](https://web.archive.org/web/20251021133206/https://www.sri.ro/assets/files/legislatie/2024/Lege_182.2002.pdf))
[^s2]: Autoritatea pentru Digitalizarea României — Semnătura electronică, Trusted list. Semnătura electronică, Trusted list. <https://www.adr.gov.ro/semnatura-electronica-trusted-list> ([archived](https://web.archive.org/web/20260615083106/https://www.adr.gov.ro/semnatura-electronica-trusted-list))
[^s3]: Autoritatea pentru Digitalizarea României — Romanian Trusted List (TSL) – Serviciul de…. Romanian Trusted List (TSL) – Serviciul de Telecomunicatii Speciale entry. <https://trustedlist.adr.gov.ro/trustedlist.xml> ([archived](https://web.archive.org/web/20260908033515/https://trustedlist.adr.gov.ro/trustedlist.xml))
[^s4]: Autoritatea pentru Digitalizarea României — Comisia Europeană recunoaște ROeID ca fiind sistemul de…, 2024-09-13. Comisia Europeană recunoaște ROeID ca fiind sistemul de identificare electronică al Statului Român. <https://www.adr.gov.ro/articole/comisia-europeana-recunoaste-roeid-ca-fiind-sistemul-de-identificare-electronica-al-statului-roman> ([archived](https://web.archive.org/web/20260122073937/https://www.adr.gov.ro/articole/comisia-europeana-recunoaste-roeid-ca-fiind-sistemul-de-identificare-electronica-al-statului-roman))
[^s5]: Autoritatea pentru Digitalizarea României (ROeID) — ROeID – Glosar termeni. ROeID – Glosar termeni. <https://roeid.ro/glosar-termeni>
[^s6]: Autoritatea pentru Digitalizarea României — Acasă - ROeID. Acasă - ROeID. <https://roeid.ro/> ([archived](https://web.archive.org/web/20260903070414/https://roeid.ro/))
[^s7]: Autoritatea pentru Digitalizarea României — Proiecte în implementare. Proiecte în implementare. <https://www.adr.gov.ro/proiecte-in-implementare> ([archived](https://web.archive.org/web/20260429160355/https://www.adr.gov.ro/proiecte-in-implementare))
[^s8]: Autoritatea pentru Digitalizarea României — ADR a organizat conferința de status a proiectului…, 2025-02-20. ADR a organizat conferința de status a proiectului „Implementarea infrastructurii de Cloud Guvernamental”. <https://www.adr.gov.ro/articole/adr-a-organizat-conferinta-de-status-a-proiectului-implementarea-infrastructurii-de-cloud-guvernamental> ([archived](https://web.archive.org/web/20260608060129/https://www.adr.gov.ro/articole/adr-a-organizat-conferinta-de-status-a-proiectului-implementarea-infrastructurii-de-cloud-guvernamental))
[^s9]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s10]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s11]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s12]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s13]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s14]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s15]: Ministerul Afacerilor Interne - Direcția Generală pentru Evidența Persoanelor — Despre | Cartea electronică de identitate. Despre | Cartea electronică de identitate. <https://carteadeidentitate.gov.ro/despre/> ([archived](https://web.archive.org/web/20260820162144/https://carteadeidentitate.gov.ro/despre/))
[^s16]: Autoritatea Electorală Permanentă — Notă de informare - Registrul electoral. Notă de informare - Registrul electoral. <https://www.registrulelectoral.ro/upload/public/FormulareCereri/Nota%20de%20informare%20finala%20RE.pdf>
[^s17]: Ministerul Afacerilor Interne — Direcția Generală pentru Comunicații și Tehnologia…. Direcția Generală pentru Comunicații și Tehnologia Informației. <https://www.mai.gov.ro/despre-noi/organizare/aparat-central/directia-generala-pentru-comunicatii-si-tehnologia-informatiei/> ([archived](https://web.archive.org/web/20260310104221/https://www.mai.gov.ro/despre-noi/organizare/aparat-central/directia-generala-pentru-comunicatii-si-tehnologia-informatiei/))
[^s18]: Inspectoratul General al Poliției de Frontieră — Sistemul de Informații Schengen - Poliția de Frontieră…. Sistemul de Informații Schengen - Poliția de Frontieră Română. <https://www.politiadefrontiera.ro/ro/main/pg-sistemul-de-informatii-schengen-87.html> ([archived](https://web.archive.org/web/20260826035149/https://www.politiadefrontiera.ro/ro/main/pg-sistemul-de-informatii-schengen-87.html))
[^s19]: Agenția Națională de Administrare Fiscală — Plan Strategic ANAF 2025-2028, 2024. Plan Strategic ANAF 2025-2028. <https://static.anaf.ro/static/10/Anaf/Informatii_R/240917_%20Plan_%20StrategicANAF2025-2028.pdf>
[^s20]: Casa Națională de Asigurări de Sănătate — SIUI Platforma Informatică a Asigurărilor de Sănătate. SIUI Platforma Informatică a Asigurărilor de Sănătate. <https://siui.casan.ro/> ([archived](https://web.archive.org/web/20260727073727/https://siui.casan.ro/))
[^s21]: Ministerul Afacerilor Interne — Comunicate de presa - Schengen Romania, 2018-07-05. Comunicate de presa - Schengen Romania. <https://schengen.mai.gov.ro/index09.htm> ([archived](https://web.archive.org/web/20250523114019/https://schengen.mai.gov.ro/index09.htm))
[^s22]: Ministerul Afacerilor Interne — Structuri în subordinea / în cadrul MAI. Structuri în subordinea / în cadrul MAI. <https://www.mai.gov.ro/despre-noi/organizare/structuri-in-subordinea-in-cadrul-mai/> ([archived](https://web.archive.org/web/20260709212319/https://www.mai.gov.ro/despre-noi/organizare/structuri-in-subordinea-in-cadrul-mai/))
[^s23]: Banca Națională a României — BNR Infrastructuri ale pieței financiare operate de BNR. BNR Infrastructuri ale pieței financiare operate de BNR. <https://www.bnr.ro/2152-sisteme-operate-de-bnr> ([archived](https://web.archive.org/web/20260514142924/https://www.bnr.ro/2152-sisteme-operate-de-bnr))
[^s24]: C.N.T.E.E. Transelectrica S.A. — Operator de sistem - Transelectrica. Operator de sistem - Transelectrica. <https://www.transelectrica.ro/ro/web/tel/operator-de-sistem> ([archived](https://web.archive.org/web/20250803190750/https://www.transelectrica.ro/ro/web/tel/operator-de-sistem))
[^s25]: Administrația Națională Apele Române — WATMAN - Administrația Națională Apele Române. WATMAN - Administrația Națională Apele Române. <https://rowater.ro/activitatea-institutiei/proiecte/proiecte-implementate/watman/> ([archived](https://web.archive.org/web/20260519042221/https://rowater.ro/activitatea-institutiei/proiecte/proiecte-implementate/watman/))
[^s26]: Ministerul Educației și Cercetării — Sistem integrat de management al informațiilor în educație, 2026-07-30. Sistem integrat de management al informațiilor în educație. <https://www.edu.ro/proiect_sistem_integrat_management_informatii_educationale> ([archived](https://web.archive.org/web/20260928194106/https://www.edu.ro/proiect_sistem_integrat_management_informatii_educationale))
[^s27]: Agenția Națională de Cadastru și Publicitate Imobiliară — ANCPI - Agentia Nationala de Cadastru si Publicitate…, 2026-08-20. ANCPI - Agentia Nationala de Cadastru si Publicitate Imobiliara. <https://www.ancpi.ro/>

**Evidence grades:** 1 Strong, 28 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. Verified: Strong, and confirmed by a person under the two-person rule: someone on the reviewer roster, other than whoever submitted it, who reads the source's language and declared no conflict. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
