# Greece: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Greece could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2][^s3][^s4] |
| State-controlled national eID | Yes[^s4][^s5] |
| Government data centres | Yes[^s6][^s7][^s8] |
| Government cloud in operation | Yes[^s4][^s9][^s10][^s11] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 29 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Greece described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 10.37 million[^s12] |
| GDP, current prices | 248.4 EUR bn[^s13] |
| Public administration employment (NACE O) | 400.6 thousand[^s14] |
| Non-household electricity price | 173.8 EUR/MWh[^s15] |
| Renewables share of electricity | 60.9 %[^s16] |
| Land area | 130 048 km²[^s17] |

## 3. Critical data holdings, by priority

The holdings Greece cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 32 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | «Μητρώο Πολιτών» (Citizens' Register): national information system combining the National Municipal Register (Δημοτολόγιο) and civil-status (registry) records[^s18][^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Facial image and two flat fingerprints collected by the Passports and Security Documents Directorate (Δ.Δ.Ε.Α./Α.Ε.Α.) of Hellenic Police HQ and stored on the passport chip[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Encrypted fingerprint images kept in the Central Database of the Passports Directorate, accessible only to authorised police staff[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Civil-status acts (births, marriages, deaths) of Greek citizens and of foreigners with events in Greece, held in the Ministry of the Interior's Registry Acts Management system within the Citizens' Register[^s18][^s19] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | GRNET keeps for 12 months a history of actions taken in the Gov.gr Wallet document-presentation process[^s21] | GRNET (Ε.Δ.Υ.Τ.Ε. Α.Ε.), company of the Greek State, is the designated processor[^s21] | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Web services supplying public bodies with data on issued Greek passports, via the Interoperability Centre[^s20] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Electoral rolls kept at the Ministry of the Interior, compiled from municipal registers (δημοτολόγια)[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | ΑΠΕΔ issues and manages certificates for trust services to all public-sector bodies[^s4][^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Criminal record consists of record slips, subject to use of the computerised system[^s24][^s25] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | Gov.gr Wallet requires the personal TaxisNet credentials (or web-banking credentials) plus a verified mobile number[^s26] | Ministry of Digital Governance is the controller for the authentication services of gov.gr[^s4][^s23] | National infrastructure[^s21] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Migration Information Systems and the Register of Aliens (Μητρώο Αλλοδαπών), centrally operated by the Ministry of Migration and Asylum[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Benefits & pensions (tier 1) | ATLAS: digital pension award system of e-EFKA, whose database holds insurance-period data digitised from former IKA archives[^s28] | *Not yet sourced* | *Not stated in sources* | *Not yet sourced* |
| High | Statutory health insurance (tier 1) | Electronic prescription system installed and operated at ΗΔΥΚΑ (IDIKA) for the social-insurance funds[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Cadastre Information System (ΣΠΕΚ), into which legacy mortgage-registry archives are being digitised[^s30] | Hellenic Cadastre (Ελληνικό Κτηματολόγιο), public-law entity supervised by the Minister of Environment and Energy[^s31][^s32] | National infrastructure[^s33] | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | Central Register of Beneficial Owners, created at the General Secretariat for Information Systems and linked to each legal entity's tax number (ΑΦΜ)[^s34][^s35][^s36] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Driving licences and police ID cards are drawn into the Gov.gr Wallet from the respective registers in which they are held[^s21] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Central information system of the Hellenic Police with its files and databases, protected by the Police IT Directorate[^s37][^s38] | *Not yet sourced* | National infrastructure[^s38] | *Not yet measured* |
| High | Border and visa systems (tier 1) | πληροφοριακό σύστημα της εθνικής αρχής στο πλαίσιο της σύμβασης SCHENGEN (information system of the national authority under the Schengen Convention)[^s37] | Hellenic Police handles requests submitted through the national SIRENE bureau[^s38] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | ηλεκτρονικό αρχείο πυροβόλων όπλων (electronic firearms file)[^s39] | Διεύθυνση Κρατικής Ασφάλειας του Αρχηγείου Ελληνικής Αστυνομίας (State Security Directorate, Hellenic Police Headquarters)[^s39] | *Not stated in sources* | *Not yet measured* |
| High | Treasury and state accounts (tier 1) | Integrated Information System for Fiscal Policy (ΟΠΣΔΠ), to evolve into a central Government ERP[^s40] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Central Human Resources Management System for the Greek public administration, from appointment to retirement[^s41] | Payroll rules to be applied centrally by the Single Payment Authority (Ενιαία Αρχή Πληρωμής, ΕΑΠ)[^s42] | *Not stated in sources* | At least 680,000 paid staff in 3,500 wider-public-sector bodies[^s42] |
| High | Election management and results (tier 1) | Courts of first instance compile detailed preference-vote results and send them in print or electronically to the Ministry of the Interior[^s22] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | EMS (Energy Management System)[^s43][^s44] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | MySchool[^s45] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Tax (tier 1) | Integrated Tax Information System of AADE: TAXIS - TAXISnet - Elenxis[^s46] | *Not yet sourced* | National infrastructure[^s47] | *Not yet measured* |
| Standard | Customs declarations (tier 1) | ICISnet — integrated customs information system of AADE[^s48] | *Not yet sourced* | National infrastructure[^s49] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Government Gazette (Εφημερίδα της Κυβερνήσεως, ΦΕΚ): printed and electronic edition and citizens' access to published texts[^s50] | National Printing Office (Εθνικό Τυπογραφείο), a public service under the Presidency of the Government, publishes the Government Gazette (ΦΕΚ) in print and electronically[^s50] | *Not stated in sources* | *Not yet measured* |
| Standard | Health records (tier 2) | National Electronic Health Record (ΕΗΦΥ): a central point for storing and managing medical data[^s51] | *Not yet sourced* | National infrastructure[^s52] | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | EODY core functions include epidemiological surveillance and provision of epidemiological data[^s53] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | Digitisation of all physical holdings of the General State Archives (ΓΑΚ) and migration of data from related information systems[^s54] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | *Not yet sourced* | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 32 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 6 |
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

> Not yet sized. Capacity for Greece will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Greece without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Business registry (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Water management control (tier 1)

---

[^s1]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 1 – Purpose and scope, 2020-09-23. Law 4727/2020, Article 1 – Purpose and scope. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-1-nomos-4727-2020-skopos-kai-pedio-efarmogis-toy/>
[^s2]: Υπουργείο Ψηφιακής Διακυβέρνησης — Αρχή Πιστοποίησης του Ελληνικού Δημοσίου – Αρχική. Αρχή Πιστοποίησης του Ελληνικού Δημοσίου – Αρχική. <https://aped.gov.gr/> ([archived](https://web.archive.org/web/20260922185215/https://aped.gov.gr/))
[^s3]: Αρχή Πιστοποίησης του Ελληνικού Δημοσίου (ΑΠΕΔ) – Υπουργείο Ψηφιακής Διακυβέρνησης — Σχετικά με την ΑΠΕΔ. Σχετικά με την ΑΠΕΔ. <https://aped.gov.gr/about-aped/> ([archived](https://web.archive.org/web/20260413053433/https://aped.gov.gr/about-aped/))
[^s4]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4727/2020 Ψηφιακή Διακυβέρνηση (ΦΕΚ Α'…, 2020-09-23. Νόμος 4727/2020 Ψηφιακή Διακυβέρνηση (ΦΕΚ Α' 184/23.09.2020), άρθρο 87. <https://api.et.gr/apiLAW/1/2020/4727/pdf>
[^s5]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 25 – Identification for the…, 2020-09-23. Law 4727/2020, Article 25 – Identification for the issuance of credentials. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-25-nomos-4727-2020-taytopoiisi-gia-tin-ekdosi/>
[^s6]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Κέντρο Δεδομένων υψηλής διαθεσιμότητας (Tier-4 Datacenter), 2023-12-01. Κέντρο Δεδομένων υψηλής διαθεσιμότητας (Tier-4 Datacenter). <https://digitalstrategy.gov.gr/project/tier-4_datacenter> ([archived](https://web.archive.org/web/20260125084953/https://digitalstrategy.gov.gr/project/tier-4_datacenter))
[^s7]: GRNET (Εθνικό Δίκτυο Υποδομών Τεχνολογίας και Έρευνας, ΕΔΥΤΕ Α.Ε.) — GRNET Datacenters. GRNET Datacenters. <https://grnet.gr/en/infrastructures/grnet-datacenters/> ([archived](https://web.archive.org/web/20260920044608/https://grnet.gr/en/infrastructures/grnet-datacenters/))
[^s8]: Κοινωνία της Πληροφορίας Μ.Α.Ε. — Παροχή Νεφο-Υπολογιστικών Υποδομών και υπηρεσιών (Cloud…, 2022-09-06. Παροχή Νεφο-Υπολογιστικών Υποδομών και υπηρεσιών (Cloud Services). <https://www.ktpae.gr/erga/parochi-nefo-ypologistikon-ypodomon-kai-ypiresion-cloud-services/>
[^s9]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ενίσχυση των κεντρικών υποδομών Κυβερνητικού Νέφους (G-…, 2023-12-01. Ενίσχυση των κεντρικών υποδομών Κυβερνητικού Νέφους (G- Cloud) της Γ.Γ.Π.Σ.Δ.Δ.. <https://digitalstrategy.gov.gr/project/g-cloud> ([archived](https://web.archive.org/web/20260413104922/https://digitalstrategy.gov.gr/project/g-cloud))
[^s10]: Κοινωνία της Πληροφορίας Μ.Α.Ε. — Government Cloud / G-Cloud, 2020-01-12. Government Cloud / G-Cloud. <https://www.ktpae.gr/erga/government-cloud-g-cloud/> ([archived](https://web.archive.org/web/20260829044912/https://www.ktpae.gr/erga/government-cloud-g-cloud/))
[^s11]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 87 – Government clouds, 2020-09-23. Law 4727/2020, Article 87 – Government clouds. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-87-nomos-4727-2020-kyvernitika-nefi/>
[^s12]: Eurostat tps00001, 2026-09-30. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s13]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s14]: Eurostat nama_10_a64_e, 2026-09-30. National accounts employment data by industry (up to NACE A*64). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table>
[^s15]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s16]: Eurostat nrg_ind_ren, 2026-09-30. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s17]: Eurostat reg_area3, 2026-09-30. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s18]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4483/2017, άρθρο 115 (Δημιουργία Μητρώου Πολιτών), 2017-07-31. Νόμος 4483/2017, άρθρο 115 (Δημιουργία Μητρώου Πολιτών). <https://api.et.gr/apiLAW/1/2017/4483/pdf>
[^s19]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4483/2017 (ΦΕΚ Α΄ 107/2017), 2017-07-31. Νόμος 4483/2017 (ΦΕΚ Α΄ 107/2017). <https://www.lawspot.gr/nomothesia/nomos-4483-2017/>
[^s20]: Ελληνική Αστυνομία - Διεύθυνση Διαβατηρίων και Εγγράφων Ασφαλείας — Προστασία Προσωπικών Δεδομένων - Διεύθυνση Διαβατηρίων &…, 2025-12-31. Προστασία Προσωπικών Δεδομένων - Διεύθυνση Διαβατηρίων & Εγγράφων Ασφαλείας. <https://www.passport.gov.gr/npc/data.html> ([archived](https://web.archive.org/web/20260902152156/https://www.passport.gov.gr/npc/data.html))
[^s21]: Υπουργείο Ψηφιακής Διακυβέρνησης — Gov.gr Wallet - Πολιτική Απορρήτου. Gov.gr Wallet - Πολιτική Απορρήτου. <https://wallet.gov.gr/privacy/> ([archived](https://web.archive.org/web/20260513043821/https://wallet.gov.gr/privacy/))
[^s22]: Lawspot (reproduction of the Government Gazette text) — Προεδρικό Διάταγμα 26/2012 (κωδικοποίηση εκλογικής…, 2012-03-14. Προεδρικό Διάταγμα 26/2012 (κωδικοποίηση εκλογικής νομοθεσίας). <https://www.lawspot.gr/nomothesia/proedriko-diatagma-26-2012/>
[^s23]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4727/2020 (ΦΕΚ Α΄ 184/2020), 2020-09-23. Νόμος 4727/2020 (ΦΕΚ Α΄ 184/2020). <https://www.lawspot.gr/nomothesia/nomos-4727-2020/> ([archived](https://web.archive.org/web/20260309090533/https://www.lawspot.gr/nomothesia/nomos-4727-2020/))
[^s24]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4620/2019 Κώδικας Ποινικής Δικονομίας, άρθρο 569, 2019-06-11. Νόμος 4620/2019 Κώδικας Ποινικής Δικονομίας, άρθρο 569. <https://api.et.gr/apiLAW/1/2019/4620/pdf>
[^s25]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4620/2019 - Κώδικας Ποινικής Δικονομίας, 2019-06-11. Νόμος 4620/2019 - Κώδικας Ποινικής Δικονομίας. <https://www.lawspot.gr/nomothesia/nomos-4620-2019/> ([archived](https://web.archive.org/web/20260308031021/https://www.lawspot.gr/nomothesia/nomos-4620-2019/))
[^s26]: Υπουργείο Ψηφιακής Διακυβέρνησης — Gov.gr Wallet. Gov.gr Wallet. <https://wallet.gov.gr/> ([archived](https://web.archive.org/web/20260905163745/https://wallet.gov.gr/))
[^s27]: Υπουργείο Μετανάστευσης και Ασύλου — Διοίκηση - Υπουργείο Μετανάστευσης και Ασύλου. Διοίκηση - Υπουργείο Μετανάστευσης και Ασύλου. <https://migration.gov.gr/migration-policy/dioikisi/> ([archived](https://web.archive.org/web/20260923144946/https://migration.gov.gr/migration-policy/dioikisi/))
[^s28]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση Ασφαλιστικής Ιστορίας e-ΕΦΚΑ, 2023-12-01. Ψηφιοποίηση Ασφαλιστικής Ιστορίας e-ΕΦΚΑ. <https://digitalstrategy.gov.gr/project/psifiopoiisi_asfalistikis_istorias_e-efka> ([archived](https://web.archive.org/web/20250918090757/https://digitalstrategy.gov.gr/project/psifiopoiisi_asfalistikis_istorias_e-efka))
[^s29]: Η.Δ.Υ.Κ.Α. Μ.Α.Ε. (IDIKA) — Ηλεκτρονική Συνταγογράφηση. Ηλεκτρονική Συνταγογράφηση. <https://www.idika.gr/erga/ilektroniki-syntagografisi/> ([archived](https://web.archive.org/web/20260903145627/https://www.idika.gr/erga/ilektroniki-syntagografisi/))
[^s30]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση Αρχείου Υποθηκοφυλακείων για το Εθνικό…, 2023-12-01. Ψηφιοποίηση Αρχείου Υποθηκοφυλακείων για το Εθνικό Κτηματολόγιο. <https://digitalstrategy.gov.gr/project/psifiopoiisi_archeioy_ypothikofylakeion_gia_to_ethniko_ktimatologio> ([archived](https://web.archive.org/web/20250613012620/https://digitalstrategy.gov.gr/project/psifiopoiisi_archeioy_ypothikofylakeion_gia_to_ethniko_ktimatologio))
[^s31]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4512/2018, άρθρο 1, 2018-01-17. Νόμος 4512/2018, άρθρο 1. <https://api.et.gr/apiLAW/1/2018/4512/pdf>
[^s32]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4512/2018, 2018-01-16. Νόμος 4512/2018. <https://www.lawspot.gr/nomothesia/nomos-4512-2018/>
[^s33]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Αναβάθμιση εξοπλισμού Κέντρου Δεδομένων (Data Center)…, 2023-12-01. Αναβάθμιση εξοπλισμού Κέντρου Δεδομένων (Data Center) και Εφεδρικού Κέντρου Δεδομένων Κτηματολογίου. <https://digitalstrategy.gov.gr/project/anavathmisi_exoplismoy_ktimatologioy_gia_leitoyrgia_se_eikoniko_perivallon_virtualization> ([archived](https://web.archive.org/web/20251119054015/https://digitalstrategy.gov.gr/project/anavathmisi_exoplismoy_ktimatologioy_gia_leitoyrgia_se_eikoniko_perivallon_virtualization))
[^s34]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4557/2018, άρθρο 20 παρ. 4, 2018-07-30. Νόμος 4557/2018, άρθρο 20 παρ. 4. <https://api.et.gr/apiLAW/1/2018/4557/pdf>
[^s35]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4557/2018, 2018-07-30. Νόμος 4557/2018. <https://www.lawspot.gr/nomothesia/nomos-4557-2018/>
[^s36]: Εθνικό Μητρώο Διοικητικών Διαδικασιών (ΜΙΤΟΣ), Υπουργείο Εσωτερικών — Κεντρικό Μητρώο Πραγματικών Δικαιούχων - Εθνικό Μητρώο…, 2026-09-29. Κεντρικό Μητρώο Πραγματικών Δικαιούχων - Εθνικό Μητρώο Διοικητικών Διαδικασιών. <https://mitos.gov.gr/index.php/%CE%94%CE%94:%CE%9A%CE%B5%CE%BD%CF%84%CF%81%CE%B9%CE%BA%CF%8C_%CE%9C%CE%B7%CF%84%CF%81%CF%8E%CE%BF_%CE%A0%CF%81%CE%B1%CE%B3%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8E%CE%BD_%CE%94%CE%B9%CE%BA%CE%B1%CE%B9%CE%BF%CF%8D%CF%87%CF%89%CE%BD> ([archived](https://web.archive.org/web/20260418223455/https://mitos.gov.gr/index.php/%CE%94%CE%94:%CE%9A%CE%B5%CE%BD%CF%84%CF%81%CE%B9%CE%BA%CF%8C_%CE%9C%CE%B7%CF%84%CF%81%CF%8E%CE%BF_%CE%A0%CF%81%CE%B1%CE%B3%CE%BC%CE%B1%CF%84%CE%B9%CE%BA%CF%8E%CE%BD_%CE%94%CE%B9%CE%BA%CE%B1%CE%B9%CE%BF%CF%8D%CF%87%CF%89%CE%BD))
[^s37]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4249/2014 (Αναδιοργάνωση της Ελληνικής…, 2014-03. Νόμος 4249/2014 (Αναδιοργάνωση της Ελληνικής Αστυνομίας), Διεύθυνση Πληροφορικής. <https://api.et.gr/apiLAW/1/2014/4249/pdf>
[^s38]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4249/2014, 2014-03-23. Νόμος 4249/2014. <https://www.lawspot.gr/nomothesia/nomos-4249-2014/>
[^s39]: Εθνικό Τυπογραφείο (Government Gazette, api.et.gr) — Νόμος 4678/2020 (τροποποίηση ν. 2168/1993, ενσωμάτωση…, 2020-03-20. Νόμος 4678/2020 (τροποποίηση ν. 2168/1993, ενσωμάτωση Οδηγίας (ΕΕ) 2017/853), άρθρο 28 παρ. 4 ν. 2168/1993. <https://api.et.gr/apiLAW/1/2020/4678/pdf>
[^s40]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Κεντρικό και Ενιαίο Σύστημα Δημοσιονομικής Πολιτικής…, 2023-12-01. Κεντρικό και Ενιαίο Σύστημα Δημοσιονομικής Πολιτικής (Government ERP). <https://digitalstrategy.gov.gr/project/government_erp> ([archived](https://web.archive.org/web/20260413112148/https://digitalstrategy.gov.gr/project/government_erp))
[^s41]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Κεντρικό Σύστημα Διαχείρισης Ανθρώπινου Δυναμικού, 2023-12-01. Κεντρικό Σύστημα Διαχείρισης Ανθρώπινου Δυναμικού. <https://digitalstrategy.gov.gr/project/kentriko_systima_diacheirisis_anthropinoy_dynamikoy> ([archived](https://web.archive.org/web/20260413104530/https://digitalstrategy.gov.gr/project/kentriko_systima_diacheirisis_anthropinoy_dynamikoy))
[^s42]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Μισθοδοσία, 2023-12-01. Μισθοδοσία. <https://digitalstrategy.gov.gr/project/misthodosia> ([archived](https://web.archive.org/web/20260413121425/https://digitalstrategy.gov.gr/project/misthodosia))
[^s43]: IPTO (ΑΔΜΗΕ) — Event at the National Control Center in Kryoneri, 2019-12. Event at the National Control Center in Kryoneri. <https://www.admie.gr/en/nea/ekdiloseis/egkainia-psifiakoy-kentroy-eleghoy-sto-kryoneri>
[^s44]: ΑΔΜΗΕ (IPTO, Independent Power Transmission Operator) — ΜΕΤΑΓΩΓΗ ΣΥΣΤΗΜΑΤΟΣ EMS, 2017-05-30. ΜΕΤΑΓΩΓΗ ΣΥΣΤΗΜΑΤΟΣ EMS. <https://www.admie.gr/anakoinoseis/enimerosi/metagogi-systimatos-ems>
[^s45]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού) — Ψηφιακές Υπηρεσίες MySchool, 2023-12-01. Ψηφιακές Υπηρεσίες MySchool. <https://digitalstrategy.gov.gr/project/myschool> ([archived](https://web.archive.org/web/20240416211029/https://digitalstrategy.gov.gr/project/myschool))
[^s46]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού…, 2023-12-01. Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού Συστήματος Φορολογίας της ΑΑΔΕ. <https://digitalstrategy.gov.gr/project/anaptyxi_neoy_enopoiimenoy_olokliromenoy_pliroforiakoy_systimatos_forologias_tis_aade>
[^s47]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4389/2016, 2016-05-27. Νόμος 4389/2016. <https://www.lawspot.gr/nomothesia/nomos-4389-2016/>
[^s48]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού…, 2023-12-01. Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού Συστήματος Τελωνείων της ΑΑΔΕ (ICISnet). <https://digitalstrategy.gov.gr/project/icisnet>
[^s49]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Αναβάθμιση διαθεσιμότητας, εφεδρείας, ασφάλειας…, 2023-12-01. Αναβάθμιση διαθεσιμότητας, εφεδρείας, ασφάλειας δεδομένων, που φιλοξενούνται στις υποδομές της ΓΓΠΣΔΔ. <https://digitalstrategy.gov.gr/project/anavathmisi_diathesimotitas_efedreias_asfaleias_dedomenon_poy_filoxenoyntai_stis_ypodomes_tis_ggpsdd> ([archived](https://web.archive.org/web/20260514161810/https://digitalstrategy.gov.gr/project/anavathmisi_diathesimotitas_efedreias_asfaleias_dedomenon_poy_filoxenoyntai_stis_ypodomes_tis_ggpsdd))
[^s50]: Εθνικό Τυπογραφείο — Αποστολή - Εθνικό Τυπογραφείο. Αποστολή - Εθνικό Τυπογραφείο. <https://et.gr/yphresia/mission/> ([archived](https://web.archive.org/web/20260514100450/https://et.gr/yphresia/mission/))
[^s51]: Υπουργείο Υγείας — Εθνικός Ηλεκτρονικός Φάκελος Υγείας. Εθνικός Ηλεκτρονικός Φάκελος Υγείας. <https://www.ehealthrecord.gov.gr/ehfy-overview-details>
[^s52]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Σύστημα Διακυβέρνησης Δεδομένων για τον Τομέα της Υγείας, 2023-12-01. Σύστημα Διακυβέρνησης Δεδομένων για τον Τομέα της Υγείας. <https://digitalstrategy.gov.gr/project/systima_diakyvernisis_dedomenon_gia_ton_tomea_tis_ygeias> ([archived](https://web.archive.org/web/20260413103817/https://digitalstrategy.gov.gr/project/systima_diakyvernisis_dedomenon_gia_ton_tomea_tis_ygeias))
[^s53]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4633/2019, 2019-10-16. Νόμος 4633/2019. <https://www.lawspot.gr/nomothesia/nomos-4633-2019/> ([archived](https://web.archive.org/web/20260121092729/https://www.lawspot.gr/nomothesia/nomos-4633-2019/))
[^s54]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση των Γενικών Αρχείων του Κράτους, 2023-12-01. Ψηφιοποίηση των Γενικών Αρχείων του Κράτους. <https://digitalstrategy.gov.gr/project/psifiopoiisi_ton_genikon_archeion_toy_kratoys> ([archived](https://web.archive.org/web/20260413121410/https://digitalstrategy.gov.gr/project/psifiopoiisi_ton_genikon_archeion_toy_kratoys))

**Evidence grades:** 3 Strong, 52 Standard. Strong: a T1 or T2 source (an authoritative original or a competent public body); an official or primary source; the quote found exactly in the hashed document; an archived copy of exactly that URL; no name in the value missing from the quote; and the value either quoted from an English source, found verbatim in the original, or resting on figures matched in the original. A categorical finding is Strong only after a blind review (a reviewer shown the quote and URL but not the proposed value). Standard: every required check passed, but one of those did not. Anything less is not printed. The checks behind each fact are listed in the country PDF and on the web page.

**Methodology:** how every fact was sourced and every figure calculated is the appendix of the country PDF, and the web page /methodology; both are generated from the code that produced this brief.
