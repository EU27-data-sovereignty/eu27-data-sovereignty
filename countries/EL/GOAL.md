# Greece: critical data holdings and sovereign hosting

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

> Not demonstrated. Confidence: Low. With the evidence still open, Greece could be anywhere from 'Sovereign in law and in practice' to 'Dependent on non-EU providers'.

Groups describe what the sources show, not how sovereign a state is. A Low-confidence placement mostly reflects research that is not finished.

| Indicator | Finding |
|---|---|
| Jurisdiction requirement | *Not yet sourced* |
| Classification in law | Yes[^s1] |
| Sovereign cloud certification | *Not yet sourced* |
| State-controlled trust anchor | Yes[^s2][^s3] |
| State-controlled national eID | Yes[^s4] |
| Government data centres | Yes[^s5] |
| Government cloud in operation | Yes[^s6] |

What could move this placement:

- If jurisdiction requirement is found to be yes: Secured in law, not yet in practice.
- If any of the 29 tier 0/1 holdings whose hosting is not yet sourced turns out to run on non-EU infrastructure: Dependent on non-EU providers.

## 2. Fundamentals

Greece described on its own measured characteristics. Each figure is the published value of a pinned Eurostat series; the footnote names the series, the dimensions and the retrieval date.

| Indicator | Value |
|---|---:|
| Population | 10.37 million[^s7] |
| GDP, current prices | 248.4 EUR bn[^s8] |
| Public administration employment (NACE O) | *Under review: the pinned source does not reproduce this value* |
| Non-household electricity price | 173.8 EUR/MWh[^s9] |
| Renewables share of electricity | 51.2 %[^s10] |
| Land area | 130 048 km²[^s11] |

## 3. Critical data holdings, by priority

The holdings Greece cannot let depend on infrastructure a foreign state can compel or switch off, ranked by a declared rule. 29 of 39 holding classes have a verified source; 3 have a sourced record count or data size.

> Priority = consequence of loss (tier 0: 3, tier 1: 2, tier 2: 1, tier 3: 0) + difficulty of rebuilding (low recoverability: 2, medium: 1, high: 0) + known exposure to non-EU providers (non-EU or mixed: 2, EU provider or not yet known: 1, national: 0). Critical is 6 or more, High is 4 or 5.

| Priority | Holding | Register or system | Operator | Infrastructure dependency | Records / size |
|---|---|---|---|---|---|
| Critical | Civil registry core (tier 0) | «Μητρώο Πολιτών» (Citizens' Register): national information system combining the National Municipal Register (Δημοτολόγιο) and civil-status (registry) records[^s12] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Facial biometric (tier 0) | Facial image and two flat fingerprints collected by the Passports and Security Documents Directorate (Δ.Δ.Ε.Α./Α.Ε.Α.) of Hellenic Police HQ and stored on the passport chip[^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Fingerprint biometric (tier 0) | Encrypted fingerprint images kept in the Central Database of the Passports Directorate, accessible only to authorised police staff[^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Breeder document scans (tier 0) | Civil-status acts (births, marriages, deaths) of Greek citizens and of foreigners with events in Greece, held in the Ministry of the Interior's Registry Acts Management system within the Citizens' Register[^s12] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Critical | Authentication audit log (tier 0) | GRNET keeps for 12 months a history of actions taken in the Gov.gr Wallet document-presentation process[^s14] | GRNET (Ε.Δ.Υ.Τ.Ε. Α.Ε.), company of the Greek State, is the designated processor[^s14] | *Not stated in sources* | *Not yet measured* |
| High | Document issuance history (tier 0) | Web services supplying public bodies with data on issued Greek passports, via the Interoperability Centre[^s13] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electoral roll entry (tier 0) | Electoral rolls kept at the Ministry of the Interior, compiled from municipal registers (δημοτολόγια)[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | State PKI and qualified trust services (tier 0) | ΑΠΕΔ issues and manages certificates for trust services to all public-sector bodies[^s16] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Judicial & criminal justice (tier 1) | Criminal record consists of record slips, subject to use of the computerised system[^s17] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Defence command and logistics (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Intelligence services (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Digital identity credentials (tier 0) | Gov.gr Wallet requires the personal TaxisNet credentials (or web-banking credentials) plus a verified mobile number[^s18] | Ministry of Digital Governance is the controller for the authentication services of gov.gr[^s16] | National infrastructure[^s14] | *Not yet measured* |
| High | Residence and migration status (tier 1) | Migration Information Systems and the Register of Aliens (Μητρώο Αλλοδαπών), centrally operated by the Ministry of Migration and Asylum[^s19] | *Not yet sourced* | *Not stated in sources* | 1,007,920 residence documents in force in August 2026 (EU citizens/ethnic Greeks 274,705; temporary protection 41,788; third-country nationals 591,461; recognised refugees 99,966)[^s20] |
| High | Benefits & pensions (tier 1) | ATLAS: digital pension award system of e-EFKA, whose database holds insurance-period data digitised from former IKA archives[^s21] | *Not yet sourced* | *Not stated in sources* | HELIOS pension control and payment system (operated by ΗΔΥΚΑ/IDIKA under Law 4093/2012) consolidated data from 92 systems covering 4.5 million pensions and 2.7 million pensioners[^s22] |
| High | Statutory health insurance (tier 1) | Electronic prescription system installed and operated at ΗΔΥΚΑ (IDIKA) for the social-insurance funds[^s23] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Land & property registry (tier 1) | Cadastre Information System (ΣΠΕΚ), into which legacy mortgage-registry archives are being digitised[^s24] | Hellenic Cadastre (Ελληνικό Κτηματολόγιο), public-law entity supervised by the Minister of Environment and Energy[^s25] | National infrastructure[^s26] | *Not yet measured* |
| High | Business registry (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Beneficial ownership register (tier 1) | Central Register of Beneficial Owners, created at the General Secretariat for Information Systems and linked to each legal entity's tax number (ΑΦΜ)[^s27] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Vehicle & licensing (tier 1) | Driving licences and police ID cards are drawn into the Gov.gr Wallet from the respective registers in which they are held[^s14] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Police information systems (tier 1) | Central information system of the Hellenic Police with its files and databases, protected by the Police IT Directorate[^s28] | *Not yet sourced* | National infrastructure[^s28] | *Not yet measured* |
| High | Border and visa systems (tier 1) | National Schengen information system (N.SIS) supported by the Hellenic Police IT Directorate under the Schengen Convention ratified by Law 2514/1997[^s28] | Hellenic Police handles requests submitted through the national SIRENE bureau[^s28] | *Not stated in sources* | *Not yet measured* |
| High | Firearms register (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Treasury and state accounts (tier 1) | Integrated Information System for Fiscal Policy (ΟΠΣΔΠ), to evolve into a central Government ERP[^s29] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Government payroll and personnel (tier 1) | Central Human Resources Management System for the Greek public administration, from appointment to retirement[^s30] | Payroll rules to be applied centrally by the Single Payment Authority (Ενιαία Αρχή Πληρωμής, ΕΑΠ)[^s31] | *Not stated in sources* | At least 680,000 paid staff in 3,500 wider-public-sector bodies[^s31] |
| High | Election management and results (tier 1) | Courts of first instance compile detailed preference-vote results and send them in print or electronically to the Ministry of the Interior[^s15] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Central bank systems (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Emergency calls and public-safety radio (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Crisis management and civil protection (tier 1) | Civil Protection Operations Centre, run 24/7 by the General Secretariat for Civil Protection (Law 3013/2002 as reproduced; since superseded by Law 4662/2020, not retrieved)[^s32] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| High | Electricity grid control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Water management control (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| High | Education (tier 1) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Tax (tier 1) | Integrated Tax Information System of AADE: TAXIS - TAXISnet - Elenxis[^s33] | Independent Authority for Public Revenue (ΑΑΔΕ), established by Law 4389/2016 to assess and collect tax, customs and other public revenue[^s34] | National infrastructure[^s34] | *Not yet measured* |
| Standard | Customs declarations (tier 1) | ICISnet — integrated customs information system of AADE[^s35] | *Not yet sourced* | National infrastructure[^s36] | *Not yet measured* |
| Standard | Official gazette and legislation (tier 1) | Government Gazette (Εφημερίδα της Κυβερνήσεως, ΦΕΚ): printed and electronic edition and citizens' access to published texts[^s37] | National Printing Office (Εθνικό Τυπογραφείο), a public service under the Presidency of the Government, publishes the Government Gazette (ΦΕΚ) in print and electronically[^s37] | *Not stated in sources* | *Not yet measured* |
| Standard | Health records (tier 2) | National Electronic Health Record (ΕΗΦΥ): a central point for storing and managing medical data[^s38] | *Not yet sourced* | National infrastructure[^s39] | *Not yet measured* |
| Standard | Public health surveillance (tier 2) | EODY core functions include epidemiological surveillance and provision of epidemiological data[^s40] | National Public Health Organization (ΕΟΔΥ), private-law entity supervised by the Minister of Health (Law 4633/2019)[^s40] | *Not stated in sources* | *Not yet measured* |
| Standard | National archives (digital) (tier 3) | Digitisation of all physical holdings of the General State Archives (ΓΑΚ) and migration of data from related information systems[^s41] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |
| Standard | Statistical microdata (tier 2) | *Not yet verified* | *—* | *—* | *—* |
| Standard | Geospatial base data (tier 3) | National Spatial Data Infrastructure (ΕΥΓΕΠ) and national Geoportal, access provided by ΟΚΧΕ under Law 3882/2010 (INSPIRE)[^s42] | *Not yet sourced* | *Not stated in sources* | *Not yet measured* |

## 4. Foreign-dependency exposure

Of the 29 verified holdings, how many sources state where the infrastructure is operated. A holding counts as dependent only when a cited document says so; silence is counted as not stated, never as national.

| Infrastructure | Holdings |
|---|---:|
| National infrastructure | 6 |
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

> Not yet sized. Capacity for Greece will be derived from its own measured holdings (record counts and data sizes), not scaled from another country. 3 of 39 holding classes have a sourced measurement so far.

## 7. Research still open

Tier 0 and 1 holdings for Greece without a verified source yet. Corrections and sources are welcome through the repository's issue template.

- Business registry (tier 1)
- Firearms register (tier 1)
- Central bank systems (tier 1)
- Defence command and logistics (tier 1)
- Intelligence services (tier 1)
- Emergency calls and public-safety radio (tier 1)
- Electricity grid control (tier 1)
- Water management control (tier 1)
- Education (tier 1)

---

[^s1]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 1 – Purpose and scope, 2020-09-23. Law 4727/2020, Article 1 – Purpose and scope. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-1-nomos-4727-2020-skopos-kai-pedio-efarmogis-toy/>
[^s2]: Υπουργείο Ψηφιακής Διακυβέρνησης — Αρχή Πιστοποίησης του Ελληνικού Δημοσίου – Αρχική. Αρχή Πιστοποίησης του Ελληνικού Δημοσίου – Αρχική. <https://aped.gov.gr/> ([archived](https://web.archive.org/web/20260922185215/https://aped.gov.gr/))
[^s3]: Αρχή Πιστοποίησης του Ελληνικού Δημοσίου (ΑΠΕΔ) – Υπουργείο Ψηφιακής Διακυβέρνησης — Σχετικά με την ΑΠΕΔ. Σχετικά με την ΑΠΕΔ. <https://aped.gov.gr/about-aped/> ([archived](https://web.archive.org/web/20260413053433/https://aped.gov.gr/about-aped/))
[^s4]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 25 – Identification for the…, 2020-09-23. Law 4727/2020, Article 25 – Identification for the issuance of credentials. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-25-nomos-4727-2020-taytopoiisi-gia-tin-ekdosi/>
[^s5]: GRNET (Εθνικό Δίκτυο Υποδομών Τεχνολογίας και Έρευνας, ΕΔΥΤΕ Α.Ε.) — GRNET Datacenters. GRNET Datacenters. <https://grnet.gr/en/infrastructures/grnet-datacenters/> ([archived](https://web.archive.org/web/20260920044608/https://grnet.gr/en/infrastructures/grnet-datacenters/))
[^s6]: Lawspot (consolidated text of Law 4727/2020) — Law 4727/2020, Article 87 – Government clouds, 2020-09-23. Law 4727/2020, Article 87 – Government clouds. <https://www.lawspot.gr/nomothesia/n-4727-2020/arthro-87-nomos-4727-2020-kyvernitika-nefi/>
[^s7]: Eurostat tps00001, 2025. Population on 1 January. <https://ec.europa.eu/eurostat/databrowser/view/tps00001/default/table>
[^s8]: Eurostat nama_10_gdp, 2025. GDP and main components (output, expenditure and income). <https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table>
[^s9]: Eurostat nrg_pc_205, 2025-S2. Electricity prices for non-household consumers - bi-annual data (from 2007 onwards). <https://ec.europa.eu/eurostat/databrowser/view/nrg_pc_205/default/table>
[^s10]: Eurostat nrg_ind_ren, 2024. Share of energy from renewable sources. <https://ec.europa.eu/eurostat/databrowser/view/nrg_ind_ren/default/table>
[^s11]: Eurostat reg_area3, 2019. Area by NUTS 3 region. <https://ec.europa.eu/eurostat/databrowser/view/reg_area3/default/table>
[^s12]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4483/2017 (ΦΕΚ Α΄ 107/2017), 2017-07-31. Νόμος 4483/2017 (ΦΕΚ Α΄ 107/2017). <https://www.lawspot.gr/nomothesia/nomos-4483-2017/>
[^s13]: Ελληνική Αστυνομία - Διεύθυνση Διαβατηρίων και Εγγράφων Ασφαλείας — Προστασία Προσωπικών Δεδομένων - Διεύθυνση Διαβατηρίων &…, 2025-12-31. Προστασία Προσωπικών Δεδομένων - Διεύθυνση Διαβατηρίων & Εγγράφων Ασφαλείας. <https://www.passport.gov.gr/npc/data.html> ([archived](https://web.archive.org/web/20260902152156/https://www.passport.gov.gr/npc/data.html))
[^s14]: Υπουργείο Ψηφιακής Διακυβέρνησης — Gov.gr Wallet - Πολιτική Απορρήτου. Gov.gr Wallet - Πολιτική Απορρήτου. <https://wallet.gov.gr/privacy/> ([archived](https://web.archive.org/web/20260513043821/https://wallet.gov.gr/privacy/))
[^s15]: Lawspot (reproduction of the Government Gazette text) — Προεδρικό Διάταγμα 26/2012 (κωδικοποίηση εκλογικής…, 2012-03-14. Προεδρικό Διάταγμα 26/2012 (κωδικοποίηση εκλογικής νομοθεσίας). <https://www.lawspot.gr/nomothesia/proedriko-diatagma-26-2012/>
[^s16]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4727/2020 (ΦΕΚ Α΄ 184/2020), 2020-09-23. Νόμος 4727/2020 (ΦΕΚ Α΄ 184/2020). <https://www.lawspot.gr/nomothesia/nomos-4727-2020/> ([archived](https://web.archive.org/web/20260309090533/https://www.lawspot.gr/nomothesia/nomos-4727-2020/))
[^s17]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4620/2019 - Κώδικας Ποινικής Δικονομίας, 2019-06-11. Νόμος 4620/2019 - Κώδικας Ποινικής Δικονομίας. <https://www.lawspot.gr/nomothesia/nomos-4620-2019/> ([archived](https://web.archive.org/web/20260308031021/https://www.lawspot.gr/nomothesia/nomos-4620-2019/))
[^s18]: Υπουργείο Ψηφιακής Διακυβέρνησης — Gov.gr Wallet. Gov.gr Wallet. <https://wallet.gov.gr/> ([archived](https://web.archive.org/web/20260905163745/https://wallet.gov.gr/))
[^s19]: Υπουργείο Μετανάστευσης και Ασύλου — Διοίκηση - Υπουργείο Μετανάστευσης και Ασύλου. Διοίκηση - Υπουργείο Μετανάστευσης και Ασύλου. <https://migration.gov.gr/migration-policy/dioikisi/> ([archived](https://web.archive.org/web/20260923144946/https://migration.gov.gr/migration-policy/dioikisi/))
[^s20]: Υπουργείο Μετανάστευσης και Ασύλου — Νόμιμη Μετανάστευση Αύγουστος 2026 - Παράρτημα Β…, 2026-09. Νόμιμη Μετανάστευση Αύγουστος 2026 - Παράρτημα Β (Αναλυτικοί Πίνακες). <https://migration.gov.gr/wp-content/uploads/2026/09/%CE%A0%CE%91%CE%A1%CE%91%CE%A1%CE%A4%CE%97%CE%9C%CE%91-%CE%92_%CE%91%CF%8D%CE%B3%CE%BF%CF%85%CF%83%CF%84%CE%BF%CF%82-_2026_%CE%A5%CE%9C%CE%91-GR-%CE%95%CE%BD%CE%B7%CE%BC%CE%B5%CF%81%CF%89%CF%84%CE%B9%CE%BA%CF%8C-%CE%91%CF%8D%CE%B3%CE%BF%CF%85%CF%83%CF%84%CE%BF%CF%82-%CE%92-%CE%9D%CF%8C%CE%BC%CE%B9%CE%BC%CE%B7-%CE%9C%CE%B5%CF%84%CE%B1%CE%BD%CE%AC%CF%83%CF%84%CE%B5%CF%85%CF%83%CE%B7.pdf>
[^s21]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση Ασφαλιστικής Ιστορίας e-ΕΦΚΑ, 2023-12-01. Ψηφιοποίηση Ασφαλιστικής Ιστορίας e-ΕΦΚΑ. <https://digitalstrategy.gov.gr/project/psifiopoiisi_asfalistikis_istorias_e-efka> ([archived](https://web.archive.org/web/20250918090757/https://digitalstrategy.gov.gr/project/psifiopoiisi_asfalistikis_istorias_e-efka))
[^s22]: Η.Δ.Υ.Κ.Α. Μ.Α.Ε. (IDIKA) — Ενιαίο Σύστημα Ελέγχου & Πληρωμών Συντάξεων ΕΣΕΠΣ – ΗΛΙΟΣ. Ενιαίο Σύστημα Ελέγχου & Πληρωμών Συντάξεων ΕΣΕΠΣ – ΗΛΙΟΣ. <https://www.idika.gr/erga/eniaio-systima-syntaxeon-eseps-ilios/> ([archived](https://web.archive.org/web/20260804115242/https://www.idika.gr/erga/eniaio-systima-syntaxeon-eseps-ilios/))
[^s23]: Η.Δ.Υ.Κ.Α. Μ.Α.Ε. (IDIKA) — Ηλεκτρονική Συνταγογράφηση. Ηλεκτρονική Συνταγογράφηση. <https://www.idika.gr/erga/ilektroniki-syntagografisi/> ([archived](https://web.archive.org/web/20260903145627/https://www.idika.gr/erga/ilektroniki-syntagografisi/))
[^s24]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση Αρχείου Υποθηκοφυλακείων για το Εθνικό…, 2023-12-01. Ψηφιοποίηση Αρχείου Υποθηκοφυλακείων για το Εθνικό Κτηματολόγιο. <https://digitalstrategy.gov.gr/project/psifiopoiisi_archeioy_ypothikofylakeion_gia_to_ethniko_ktimatologio> ([archived](https://web.archive.org/web/20250613012620/https://digitalstrategy.gov.gr/project/psifiopoiisi_archeioy_ypothikofylakeion_gia_to_ethniko_ktimatologio))
[^s25]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4512/2018, 2018-01-16. Νόμος 4512/2018. <https://www.lawspot.gr/nomothesia/nomos-4512-2018/>
[^s26]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Αναβάθμιση εξοπλισμού Κέντρου Δεδομένων (Data Center)…, 2023-12-01. Αναβάθμιση εξοπλισμού Κέντρου Δεδομένων (Data Center) και Εφεδρικού Κέντρου Δεδομένων Κτηματολογίου. <https://digitalstrategy.gov.gr/project/anavathmisi_exoplismoy_ktimatologioy_gia_leitoyrgia_se_eikoniko_perivallon_virtualization> ([archived](https://web.archive.org/web/20251119054015/https://digitalstrategy.gov.gr/project/anavathmisi_exoplismoy_ktimatologioy_gia_leitoyrgia_se_eikoniko_perivallon_virtualization))
[^s27]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4557/2018, 2018-07-30. Νόμος 4557/2018. <https://www.lawspot.gr/nomothesia/nomos-4557-2018/>
[^s28]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4249/2014, 2014-03-23. Νόμος 4249/2014. <https://www.lawspot.gr/nomothesia/nomos-4249-2014/>
[^s29]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Κεντρικό και Ενιαίο Σύστημα Δημοσιονομικής Πολιτικής…, 2023-12-01. Κεντρικό και Ενιαίο Σύστημα Δημοσιονομικής Πολιτικής (Government ERP). <https://digitalstrategy.gov.gr/project/government_erp> ([archived](https://web.archive.org/web/20260413112148/https://digitalstrategy.gov.gr/project/government_erp))
[^s30]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Κεντρικό Σύστημα Διαχείρισης Ανθρώπινου Δυναμικού, 2023-12-01. Κεντρικό Σύστημα Διαχείρισης Ανθρώπινου Δυναμικού. <https://digitalstrategy.gov.gr/project/kentriko_systima_diacheirisis_anthropinoy_dynamikoy> ([archived](https://web.archive.org/web/20260413104530/https://digitalstrategy.gov.gr/project/kentriko_systima_diacheirisis_anthropinoy_dynamikoy))
[^s31]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Μισθοδοσία, 2023-12-01. Μισθοδοσία. <https://digitalstrategy.gov.gr/project/misthodosia> ([archived](https://web.archive.org/web/20260413121425/https://digitalstrategy.gov.gr/project/misthodosia))
[^s32]: Lawspot (reproduction of the Government Gazette text) — Νόμος 3013/2002, 2002-05-02. Νόμος 3013/2002. <https://www.lawspot.gr/nomothesia/nomos-3013-2002/>
[^s33]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού…, 2023-12-01. Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού Συστήματος Φορολογίας της ΑΑΔΕ. <https://digitalstrategy.gov.gr/project/anaptyxi_neoy_enopoiimenoy_olokliromenoy_pliroforiakoy_systimatos_forologias_tis_aade>
[^s34]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4389/2016, 2016-05-27. Νόμος 4389/2016. <https://www.lawspot.gr/nomothesia/nomos-4389-2016/>
[^s35]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού…, 2023-12-01. Ανάπτυξη νέου ενοποιημένου Ολοκληρωμένου Πληροφοριακού Συστήματος Τελωνείων της ΑΑΔΕ (ICISnet). <https://digitalstrategy.gov.gr/project/icisnet>
[^s36]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Αναβάθμιση διαθεσιμότητας, εφεδρείας, ασφάλειας…, 2023-12-01. Αναβάθμιση διαθεσιμότητας, εφεδρείας, ασφάλειας δεδομένων, που φιλοξενούνται στις υποδομές της ΓΓΠΣΔΔ. <https://digitalstrategy.gov.gr/project/anavathmisi_diathesimotitas_efedreias_asfaleias_dedomenon_poy_filoxenoyntai_stis_ypodomes_tis_ggpsdd> ([archived](https://web.archive.org/web/20260514161810/https://digitalstrategy.gov.gr/project/anavathmisi_diathesimotitas_efedreias_asfaleias_dedomenon_poy_filoxenoyntai_stis_ypodomes_tis_ggpsdd))
[^s37]: Εθνικό Τυπογραφείο — Αποστολή - Εθνικό Τυπογραφείο. Αποστολή - Εθνικό Τυπογραφείο. <https://et.gr/yphresia/mission/> ([archived](https://web.archive.org/web/20260514100450/https://et.gr/yphresia/mission/))
[^s38]: Υπουργείο Υγείας — Εθνικός Ηλεκτρονικός Φάκελος Υγείας. Εθνικός Ηλεκτρονικός Φάκελος Υγείας. <https://www.ehealthrecord.gov.gr/ehfy-overview-details>
[^s39]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Σύστημα Διακυβέρνησης Δεδομένων για τον Τομέα της Υγείας, 2023-12-01. Σύστημα Διακυβέρνησης Δεδομένων για τον Τομέα της Υγείας. <https://digitalstrategy.gov.gr/project/systima_diakyvernisis_dedomenon_gia_ton_tomea_tis_ygeias> ([archived](https://web.archive.org/web/20260413103817/https://digitalstrategy.gov.gr/project/systima_diakyvernisis_dedomenon_gia_ton_tomea_tis_ygeias))
[^s40]: Lawspot (reproduction of the Government Gazette text) — Νόμος 4633/2019, 2019-10-16. Νόμος 4633/2019. <https://www.lawspot.gr/nomothesia/nomos-4633-2019/> ([archived](https://web.archive.org/web/20260121092729/https://www.lawspot.gr/nomothesia/nomos-4633-2019/))
[^s41]: Υπουργείο Ψηφιακής Διακυβέρνησης (Βίβλος Ψηφιακού Μετασχηματισμού 2020-2025) — Ψηφιοποίηση των Γενικών Αρχείων του Κράτους, 2023-12-01. Ψηφιοποίηση των Γενικών Αρχείων του Κράτους. <https://digitalstrategy.gov.gr/project/psifiopoiisi_ton_genikon_archeion_toy_kratoys> ([archived](https://web.archive.org/web/20260413121410/https://digitalstrategy.gov.gr/project/psifiopoiisi_ton_genikon_archeion_toy_kratoys))
[^s42]: Lawspot (reproduction of the Government Gazette text) — Νόμος 3882/2010, 2010-09-22. Νόμος 3882/2010. <https://www.lawspot.gr/nomothesia/nomos-3882-2010/>
