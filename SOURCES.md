# Sources

Where each member state's legal and regulatory claims are checked against, how the documents
are fetched, and what to do about the ones that cannot be.

`VERIFICATION.md` is the method -- the tiered rule, the ledger, the quote requirement.
**This file is the endpoints**, and `model/source_urls.csv` is the machine-readable copy the
fetcher actually reads.

---

## The arrangement

| Piece | What it is | Tracked |
|---|---|---|
| `model/source_urls.csv` | one row per (state, column): where to look, who publishes it, the fetch policy | yes |
| `model/fetch.py` | the shared fetch layer: politeness, robots, cache paths, the manifest | yes |
| `model/fetch_sources.py` | fetches the legal corpus | yes |
| `model/fetch_manifest.csv` | sha256, size, HTTP status and retrieval date of every attempt | yes |
| `cache/legal/<ISO>/` | the documents themselves | **no** -- gitignored and `.vercelignore`d |

The cache is rebuildable, so the bytes stay out of git: national gazette PDFs are large and git
history never shrinks. The manifest carries the hash of each one, which is what makes drift
detectable without storing them. Same pattern as `countries/ARTEFACTS.csv` (#52).

**Why keep the documents at all?** Because `sources.csv` records that a claim was checked
against a URL, and a URL cannot record that the page still says what it said. A quote that no
longer appears in its source is a finding; a bare link that quietly changed underneath is
invisible, and looks exactly like a verified cell. That is the failure #54 exists to prevent.

## Fetching politely

These are government servers. Requests are serial and spaced (`DELAY`, 1.5 s), carry a
User-Agent naming the project and linking to the repository, and obey `robots.txt`. A 403 is
recorded, never retried -- it is an answer, not a transient fault.

Three fetch policies, in `source_urls.csv`:

* **auto** -- fetched normally.
* **manual** -- the host refuses automated requests. Fetch by hand into `cache/legal/<ISO>/`
  and run `./run.sh fetch legal --adopt`, which hashes it into the manifest exactly as an
  automated fetch would. The provenance is identical; only the transport differs.
* **forbidden** -- `robots.txt` publishes `Disallow: /`. Never fetched.

### Two distinctions worth keeping

**"The site forbids this" is not "the site blocked us."** Python's `RobotFileParser.read()`
collapses them: it treats a 403 on `robots.txt` as *disallow everything*, so a host that
blocked our user-agent looks identical to a host that politely asked us not to come. Only the
second is a rule. `fetch.py` fetches `robots.txt` itself and keeps the status, so the manifest
says which happened.

**Being able to fetch something is not permission to.** Poland's `isap.sejm.gov.pl` publishes
`Disallow: /` for all agents -- but serves `robots.txt` only to browser user-agents, so an
automated client is told nothing and sails straight past a rule that plainly exists. It is
marked `forbidden` by hand for that reason, and never attempted.

---

## Reachability, measured 2026-09-11

**24 of 36 attempts succeeded.** The refusals:

| State | Target | Status | Why |
|---|---|---|---|
| BE | `gazette` | `error` | connection refused or never completes |
| EE | `certification_scheme` | `403` | bot challenge (Cloudflare or WAF) |
| EE | `data_classification` | `403` | bot challenge (Cloudflare or WAF) |
| EE | `gazette` | `403` | bot challenge (Cloudflare or WAF) |
| EE | `legal_instrument` | `403` | bot challenge (Cloudflare or WAF) |
| FR | `gazette` | `403` | bot challenge (Cloudflare or WAF) |
| HU | `gazette` | `error` | connection refused or never completes |
| LT | `gazette` | `403` | bot challenge (Cloudflare or WAF) |
| NL | `certification_scheme` | `403` | bot challenge (Cloudflare or WAF) |
| PL | `gazette` | `robots-denied` | `robots.txt` publishes `Disallow: /`; not attempted |
| RO | `gazette` | `error` | connection refused or never completes |
| SK | `gazette` | `403` | bot challenge (Cloudflare or WAF) |

None of these are permanent: they are facts about how each host treats an automated client
today, recorded so the gap is visible rather than mistaken for work not yet done. Every one is
reachable by a person with a browser, which is what the **manual** policy is for.

---

## Endpoints per member state

`gazette` is the state's legal gazette -- the first place to look for any tier-1 instrument.
Rows naming a sourceable column are specific documents already identified for that cell.

| State | Column | Publisher | Policy | Endpoint |
|---|---|---|---|---|
| AT | `gazette` | Rechtsinformationssystem des Bundes | auto | [https://www.ris.bka.gv.at/](https://www.ris.bka.gv.at/) |
| BE | `gazette` | Belgisch Staatsblad / Moniteur belge | manual | [https://www.ejustice.just.fgov.be/cgi_loi/loi.pl](https://www.ejustice.just.fgov.be/cgi_loi/loi.pl) |
| BG | `gazette` | Darzhaven Vestnik | auto | [https://dv.parliament.bg/](https://dv.parliament.bg/) |
| CY | `gazette` | CyLaw | auto | [http://www.cylaw.org/](http://www.cylaw.org/) |
| CZ | `gazette` | e-Sbirka | auto | [https://www.e-sbirka.cz/](https://www.e-sbirka.cz/) |
| DE | `gazette` | Bundesministerium der Justiz | auto | [https://www.gesetze-im-internet.de/](https://www.gesetze-im-internet.de/) |
| DK | `gazette` | Retsinformation | auto | [https://www.retsinformation.dk/](https://www.retsinformation.dk/) |
| EE | `certification_scheme` | Riigi Infosusteemi Amet (RIA) | manual | [https://www.ria.ee/en/cyber-security/e-its](https://www.ria.ee/en/cyber-security/e-its) |
| EE | `data_classification` | Riigi Teataja | manual | [https://www.riigiteataja.ee/en/eli/511072014001/consoli...](https://www.riigiteataja.ee/en/eli/511072014001/consolide/current) |
| EE | `gazette` | Riigi Teataja | manual | [https://www.riigiteataja.ee/en/](https://www.riigiteataja.ee/en/) |
| EE | `legal_instrument` | Riigi Teataja | manual | [https://www.riigiteataja.ee/en/eli/518012016001/consolide](https://www.riigiteataja.ee/en/eli/518012016001/consolide) |
| EL | `gazette` | Ethniko Typographeio | auto | [https://www.et.gr/](https://www.et.gr/) |
| ES | `gazette` | Boletin Oficial del Estado | auto | [https://www.boe.es/](https://www.boe.es/) |
| FI | `gazette` | Finlex | auto | [https://www.finlex.fi/en/](https://www.finlex.fi/en/) |
| FR | `certification_scheme` | ANSSI | auto | [https://cyber.gouv.fr/sites/default/files/document/secn...](https://cyber.gouv.fr/sites/default/files/document/secnumcloud-referentiel-exigences-v3.2.pdf) |
| FR | `data_classification` | SGDSN | auto | [https://www.info.gouv.fr/upload/media/content/0001/05/1...](https://www.info.gouv.fr/upload/media/content/0001/05/1dbd413d9574bba8df1f282cab4a74f128432209.pdf) |
| FR | `gazette` | Legifrance | manual | [https://www.legifrance.gouv.fr/](https://www.legifrance.gouv.fr/) |
| FR | `legal_instrument` | DINUM | auto | [https://www.numerique.gouv.fr/offre-accompagnement/clou...](https://www.numerique.gouv.fr/offre-accompagnement/cloud-administrations/) |
| HR | `gazette` | Narodne novine | auto | [https://narodne-novine.nn.hr/](https://narodne-novine.nn.hr/) |
| HU | `gazette` | Nemzeti Jogszabalytar | manual | [https://njt.hu/](https://njt.hu/) |
| IE | `gazette` | Office of the Attorney General | auto | [https://www.irishstatutebook.ie/](https://www.irishstatutebook.ie/) |
| IT | `gazette` | Normattiva | auto | [https://www.normattiva.it/](https://www.normattiva.it/) |
| LT | `gazette` | Teisines informacijos registras | manual | [https://www.e-tar.lt/portal/index.html](https://www.e-tar.lt/portal/index.html) |
| LU | `gazette` | Journal officiel du Grand-Duche de Luxembourg | auto | [https://legilux.public.lu/](https://legilux.public.lu/) |
| LV | `gazette` | Latvijas Vestnesis | auto | [https://likumi.lv/](https://likumi.lv/) |
| MT | `gazette` | Ministry for Justice | auto | [https://legislation.mt/](https://legislation.mt/) |
| NL | `certification_scheme` | BIO-overheid (BZK) | manual | [https://www.bio-overheid.nl/media/cs5ctudu/20250924-bas...](https://www.bio-overheid.nl/media/cs5ctudu/20250924-baseline-informatiebeveiliging-overheid-2-bio2-v12-deff.pdf) |
| NL | `data_classification` | Overheid.nl Wettenbank | auto | [https://wetten.overheid.nl/BWBR0033507/2013-06-01](https://wetten.overheid.nl/BWBR0033507/2013-06-01) |
| NL | `gazette` | Overheid.nl Wettenbank | auto | [https://wetten.overheid.nl/](https://wetten.overheid.nl/) |
| NL | `legal_instrument` | Tweede Kamer der Staten-Generaal | auto | [https://www.tweedekamer.nl/downloads/document?id=2022D3...](https://www.tweedekamer.nl/downloads/document?id=2022D33299) |
| PL | `gazette` | Sejm RP | forbidden | [https://isap.sejm.gov.pl/](https://isap.sejm.gov.pl/) |
| PT | `gazette` | Diario da Republica | auto | [https://dre.pt/](https://dre.pt/) |
| RO | `gazette` | Ministerul Justitiei | manual | [https://legislatie.just.ro/](https://legislatie.just.ro/) |
| SE | `gazette` | Sveriges riksdag | auto | [https://www.riksdagen.se/](https://www.riksdagen.se/) |
| SI | `gazette` | Pravno-informacijski sistem | auto | [https://pisrs.si/](https://pisrs.si/) |
| SK | `gazette` | Slov-Lex | manual | [https://www.slov-lex.sk/](https://www.slov-lex.sk/) |

## Eurostat

A separate pipeline, `model/fetch_eurostat.py`, because it is a different kind of claim: a
figure carrying a dataset code and a period is verifiable by anyone, in a way a paraphrased
legal requirement is not. It writes `model/eurostat_pull.csv` -- value, dataset, period,
the API's own `updated` vintage and retrieval date, per country per figure -- and **reports a
diff without applying it**.

Two filters were calibrated against the existing column rather than assumed, and both would
have been wrong by guess:

* `renewables_pct` is the renewable share **of electricity** (`REN_ELC`), not of gross final
  energy consumption (`REN`). Guessing `REN` disagrees with all 27 by 36% on average.
* `elec_price_eur_mwh` excludes VAT and other recoverable taxes (`X_VAT`), not all taxes.

The period is **the most recent one all 27 report**, not simply the latest. National accounts
arrive at different times -- `nama_10_a64_e` had 10 of 27 states for 2025 and all 27 for 2024 --
so taking "latest" would silently mix vintages across countries.

## Commands

```
./run.sh fetch              both pipelines
./run.sh fetch eurostat     the six Eurostat figures, plus the diff
./run.sh fetch legal        the legal corpus
./run.sh fetch legal --report    what the manifest says; no network
./run.sh fetch legal --adopt     hash hand-fetched files into the manifest
./run.sh sources            verification-ledger coverage
```

