# NATIONAL-AI-STRATEGIES.md: second-model review, 2026-10-10

The fact check of [`NATIONAL-AI-STRATEGIES.md`](../../NATIONAL-AI-STRATEGIES.md) by a model that did not write it,
in the pattern of [`stichting-factcheck-2026-10-08.md`](stichting-factcheck-2026-10-08.md). Committed as evidence, not
summarised. The decisions behind the note are `DECISIONS.md` #103; the working log is
[`national-ai-log.md`](national-ai-log.md).

**Produced by.** Six Claude Opus 5.5 (`claude-opus-5-5`) subagents, launched from the Claude Fable 5.1 session
`https://claude.ai/code/session_01FcnUV5xYY1w5oSz7Vnzqf2` that wrote the note, one per cluster of entries plus
one for sections 2, 4 and 6. Each fetched the cited pages itself (WebFetch, with `pdftotext` or a local parse
where a PDF or spreadsheet would not read), judged every factual claim in the snapshot tables against them, and
tried to source every cell marked **[unverified]** from an official page. None edited the repository. The note's
revision checked is the one in commit `5537135`.

**Verdicts.** CONFIRMED: the fetched page supports the claim, with a quote of at most 25 words. NOT CONFIRMED: the
page is reachable and does not say it, or says otherwise. UNCLEAR: page unreachable or ambiguous. For unverified
cells, FOUND gives the page, the quote and the fact as sourced; NOT FOUND says what was tried. Quotes came through
a summarising extractor unless marked otherwise, so they are evidence of what the reviewer saw, not exact text.

## Totals

| Part | Claims checked | Confirmed | Not confirmed | Unclear | Unverified cells | Found | Not found |
|---|---|---|---|---|---|---|---|
| Austria, Belgium, Germany, Luxembourg, Netherlands | 151 | 140 | 3 | 8 | 39 | 17 | 22 |
| Bulgaria, Cyprus, Greece, Ireland, Romania | 256 | 227 | 11 | 18 | 47 | 14 | 33 |
| Croatia, Czechia, Hungary, Poland, Slovakia, Slovenia | 274 | 258 | 2 | 14 | 46 | 21 | 25 |
| Denmark, Estonia, Finland, Latvia, Lithuania, Sweden | 174 | 158 | 11 | 5 | 46 | 17 | 29 |
| France, Italy, Malta, Portugal, Spain | 175 | 161 | 11 | 3 | 35 | 17 | 18 |
| Sections 2, 4 and 6 (routes, EU vehicles, cross-cutting) | 56 | 43 | 12 | 1 | 9 | 6 | 3 |
| **All** | **1,086** | **987** | **50** | **49** | **222** | **92** | **130** |

Sections 2 and 6 carry no URL and no unverified mark, so they had nothing to check. Of the 50 claims not
confirmed, 19 were true on an official page the note had not cited (only the citation changed) and 31 were wrong,
overstated or unsourced in the note (the text changed).

## What was applied to the note

Every NOT CONFIRMED verdict and every FOUND cell was applied by the writing session in the commit that adds this
file, with each edit asserted to match exactly one place in the note. In short:

- **Corrected.** MeluXina-AI's accelerator count (1,008 GPUs, not over 2,100); the Dutch Caribbean languages;
  Gefion's funders (a foundation and the state's investment fund, not private); the Lithuanian factory's EU share
  (EUR 65 million, not 90); Latvia's AI Centre founders; Meltemi's announcement date; the Romanian models' training
  data (a slice of a 40-billion-token corpus, not 40 billion tokens); Cyprus's DAEDALUS access, consultation dates
  and adoption target; the EU supercomputer count by state (twelve, not eleven); OpenEuroLLM's GPU-hour awards and
  what they were for; the AI Factory access-mode timings; the AI Continent Action Plan's EUR 10 billion (a total for
  supercomputing and factories, not a commitment to factories); the "buy European" quotation; Sweden's MIMER timing;
  AMALIA's consortium; Lucie's instruct date; ORTOLANG's lead; the "provisional" flag on four Eurostat populations.
- **Removed as unsourced.** Mutual intelligibility claims (Danish, Swedish), "Finnish is a close relative" (now
  marked), "English with Ireland" (now sourced to the Irish Constitution), the Swiss antenna's attachment, Svea's
  stage-two scope, the Italian LISA inauguration date, the PLLuM demo at CLARIN-PL, the SRCE quotation's wording.
- **Filled from official pages.** Austria's 2001 minority-language census, MUSICA's opening, AI:AT's expected
  operation, Vienna's Gigafactory expression of interest; Germany's Teuken funding, SOOFI's first release, KIPITZ;
  Luxembourg's rollout count and CLARIN status; the Dutch cabinet's Gigafactory position, SoNaR and CLARIAH-NL;
  Bulgaria's Discoverer and BRAIN++ funding; Cyprus's census; Greece's Green500 and cooling; Ireland's UCCIX weights
  and eSTÓR; Romania's census and factory grant; Estonia's Russian-speaking share, Gigafactory purchase, EstLLM
  compute and Eesti.ai; Finland's Sámi Language Act, Poro 2, the Silo AI acquisition and FinGPT; Latvia's language
  survey and 2020 report; Lithuania's Neurotechnology licence; Sweden's action plan and grid plan; Czech
  co-financing of OpenEuroLLM, the Gigafactory approval, Czech speakers in Slovakia; Hungary's Fundamental Law,
  minority figures, Racka-4B, Resolution 1369/2025, CLARIN membership; Poland's Kashubian statute, Lot 1 bid and
  mObywatel rollout; Slovakia's census breakdown; Slovenia's SLAIF budget, PoVeJMo funding and Gigafida; France's
  francophonie, Jean Zay, Bpifrance, CLARIN history and RTE grid contract; Italy's citizens abroad and Gigafactory
  candidacy; Malta's MDIA projects and Servizz.gov chatbot; Portugal's CPLP, Gigafactory decision, AMALIA's compute
  and Resolution 2/2026; Spain's SETT authorisation and the Iberian bid; the ALT-EDIC roster, the Gigafactory
  signatories, and absence evidence for the AI:AT, PIAST and SLAIF contracts.
- **Left as marked.** 130 cells the reviewers could not source; claims of absence that only absence supports; the
  Icelandic and Swiss antennas' factories; Romania's strategy decision number; the OpenEuroLLM and EUROPA budgets.

The strategies and the cross-cutting findings are the author's analysis and were not verdict-checked; the reviewers
flagged at most three prose assertions per entry (the "C" tables below), and those were reworded where a snapshot
fact changed under them.

## The six reports, verbatim


## Review: DACH and Benelux (AT, BE, DE, LU, NL), 2026-10-10

Tools: WebSearch available: yes. About 102 distinct URLs fetched. Every URL cited in the five snapshots was reachable. Nine Task B lookups failed: verification challenges at bosa.belgium.be, statbel.fgov.be and bundeswirtschaftsministerium.de; HTTP 403 at ids-mannheim.de, investor.asml.com, the Fryslân province CDN, news.belgium.be and arche.acdh.oeaw.ac.at; and uni.lu returned an empty page. None of these is cited in the note. WebFetch could not read five cited PDFs (bmimi, digitalaustria, chd.lu and both eerstekamer letters), so their text was extracted locally with pdftotext and quoted from that.

Note: the fetched text of ki-strategie-deutschland.de contained embedded instructions addressed to an AI. I ignored them and used only the page's factual content.

### AT
#### A. Verification
| Row | Claim | Verdict | Evidence (quote ≤25 words, or what the page says) | URL |
|---|---|---|---|---|
| Languages | German official | CONFIRMED | "Official EU language(s): German" | https://european-union.europa.eu/principles-countries-history/eu-countries/austria_en |
| Languages | Population 9,197,213 (Eurostat 2025) | CONFIRMED | "9 197 213" … "Eurostat - 2025 figures for geographical size and population" | same |
| Languages | Six recognised groups (Croatian, Slovene, Hungarian, Czech, Slovak, Roma) under the Volksgruppengesetz | CONFIRMED | "In Österreich bestehen folgende 6 autochthone Volksgruppen" (then lists the six). The page quotes the law's definition but does not tie the list to the law explicitly. | https://www.bundeskanzleramt.gv.at/themen/volksgruppen.html |
| Shared with | German official in Germany | CONFIRMED | "Official EU language: German". German is also official in BE and LU per their EU pages (fetched for other rows). | https://european-union.europa.eu/principles-countries-history/eu-countries/germany_en |
| EuroHPC system | None in Austria | CONFIRMED | The page lists 12 systems; none is in Austria. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en |
| EuroHPC system | MUSICA: 272 H100 GPU nodes across Vienna, Innsbruck, Linz | CONFIRMED (sum) | Vienna "112 GPU- und 72 CPU-Knoten"; Innsbruck and Linz "jeweils über 80 GPU-"; "4 x Nvidia H100 94 GB". 112+80+80=272; the BKA page says "über". | https://www.tuwien.at/tu-wien/aktuelles/news/news/musica-oesterreichs-naechster-supercomputer |
| EuroHPC system | About 40 PFlops expected | CONFIRMED | "etwa 40 Petaflops" | same and BKA MUSICA page |
| EuroHPC system | EUR 36 million, about EUR 20 million from the EU recovery plan | CONFIRMED | "Investitionen in Höhe von insgesamt 36 Millionen Euro"; "mit 20 Millionen Euro gefördert" | https://www.bundeskanzleramt.gv.at/eu-aufbauplan/aktuelles/musica-neuer-supercomputer-cluster.html |
| EuroHPC system | Coordinated by TU Wien | CONFIRMED | "Projektkoordinator: Technische Universität Wien" | TU Wien page |
| AI Factory | AI:AT selected 12 March 2025 | CONFIRMED | The release is dated 12 March 2025 and follows "the second cut-off on 1 February 2025". | https://eurohpc-ju.europa.eu/eurohpc-ju-selects-additional-ai-factories-strengthen-europes-ai-leadership-2025-03-12_en |
| AI Factory | At TU Wien, led by ACA and AIT | CONFIRMED | "The AI Factory will be installed at TU Wien, Vienna." The page names ACA and AIT as "main entities driving" it. | same |
| AI Factory | Eleven participants | CONFIRMED | CORDIS lists "Participants (11)" beside coordinator ACA. | https://cordis.europa.eu/project/id/101253078 |
| AI Factory | CORDIS EUR 30.0 million, July 2025 to June 2028 | CONFIRMED | "€ 29 999 998,79"; start "1 July 2025", end "30 June 2028" | same |
| AI Factory | Slovakia's antenna attaches to it | CONFIRMED | "This Antenna will be linked to AI:AT, the AI Factory located in Austria." (antennas release; also the ai-factories page) | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en |
| Model efforts | 2024 implementation plan floats a "Bundes-LLM" | CONFIRMED | "So könnte beispielsweise ein großes Sprachmodell („Bundes-LLM") für Österreichs Bundesverwaltung geschaffen werden" | https://www.bmimi.gv.at/dam/jcr:0581519a-ec7f-4271-9c52-6aa19b3323ee/KI-Umsetzungsplan%202024.pdf |
| Model efforts | Public AI and GovGPT use Mistral open weights 3B, 8B, 14B on BRZ servers (press) | CONFIRMED (press) | "Mistral 3B, 8B und 14B"; "ausschließlich auf Servern des BRZ betrieben" | https://www.trendingtopics.eu/brz-mistral-public-ai/ |
| Strategy | AIM AT 2030 (2021) | CONFIRMED | "Artificial Intelligence Mission Austria 2030 (AIM AT 2030) … Wien, 2021" | https://www.digitalaustria.gv.at/dam/jcr:6dacb3c5-ca2b-4751-9653-45ed8765cacd/AIM_AT_2030_UAbf.pdf |
| Strategy | Fields of action include AI infrastructure and modernising administration | CONFIRMED | "4.3 Infrastruktur für Künstliche Intelligenz"; "4.7 Öffentliche Verwaltung mit KI modernisieren" | same |
| Strategy | 2024 implementation plan as interim report | CONFIRMED | "nicht nur als ein erster Zwischenbericht, sondern auch als inhaltliche Ergänzung zu AIM AT 2030 zu verstehen" | bmimi Umsetzungsplan 2024 |
| Strategy | In force | UNCLEAR | Neither document states a status. The plan calls it an "agile Strategie" with no end date. | both |
| Public LLM | Public AI launched 19 March 2026 on shared sovereign BRZ infrastructure | CONFIRMED | "19. März 2026"; "gemeinsame souveräne KI-Infrastruktur des Bundesrechenzentrums" | https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/03/5-konkrete-ki-anwendungen-fuer-oesterreichs-bundesverwaltung.html |
| Public LLM | GovGPT for 180,000 federal staff | CONFIRMED (floor) | "mehr als 180.000 Bundesbedienstete". The figure is a target floor, not a user count. | https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/07/proell-public-ai-launcht-govgpt-fuer-die-bundesverwaltung.html |
| Public LLM | Rollout from 20 July 2026 | CONFIRMED | "Von 20. bis 23. Juli" in the Bundeskanzleramt first; other ministries follow from 21 and 28 July. | same |
| Public LLM | Across all thirteen ministries | UNCLEAR | The July page says pilot users are in all ministries and "weitere Ressorts folgen", but gives no count. The September page refers to all 13 federal ministries collectively. | July and Sept BKA pages |
| Public LLM | Requests processed on BRZ infrastructure, not used for training | CONFIRMED | "KI-Basisinfrastruktur des Bundesrechenzentrums"; "nicht zum Training verwendet" | July BKA page |
| Public LLM | "LLM as a Service" won the eGovernment competition on 3 September 2026 | CONFIRMED (wording) | The page is dated 3 Sept 2026 and names "Public AI Initiative mit LLMaaS" (Large Language Model as a Service). The award date itself is not stated. | https://www.bundeskanzleramt.gv.at/bundeskanzleramt/nachrichten-der-bundesregierung/2026/09/proell-oesterreich-gewinnt-egovernment-wettbewerb-mit-public-ai.html |
| Institutions | AIT, ACA; TU Wien; ISTA, TU Graz, JKU Linz among participants; BRZ for LLMaaS | CONFIRMED | CORDIS lists ISTA, TU Wien, TU Graz, "Universitat Linz", AIT, coordinator ACA. The Sept page has "einer vom BRZ zentral bereitgestellten, sicheren KI-Infrastruktur". | CORDIS; Sept BKA page |
| Power | MUSICA water-cooled, heat reuse in Vienna and Innsbruck | CONFIRMED (Innsbruck planned) | Largely water-cooled at about 40 °C. Vienna heats neighbouring buildings; Innsbruck plans to feed district heating (2024 text). | BKA MUSICA page |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speaker counts of the six Volksgruppen languages | FOUND | 2001 census (everyday language, multiple answers allowed): Burgenland Croatian 19,374; Romani 4,348; Slovak 3,343; Slovene 18,520; Czech 11,035; Hungarian 25,884. This is the latest count, per the 6th Charter state report. | https://www.bundeskanzleramt.gv.at/dam/jcr:c214b235-766a-4836-8342-ca273945e99f/6._at_staatenbericht_sprachencharta_de.pdf | "letztmals mit der Feststellung der „Umgangssprache" … im Jahr 2001 erhoben" |
| EuroHPC system | MUSICA 2026 operating status | FOUND | Formally opened on 3 July 2026; 45.11 PFlops in total; more than 1,000 H100 GPUs; in the TOP500 top 100. | https://www.tuwien.at/tu-wien/aktuelles/news/news/supercomputer-musica-nimmt-betrieb-auf | "wurde am 3. Juli 2026 feierlich eröffnet"; "Gesamtleistung von 45.11 Petaflops" |
| AI Factory | Press EUR 80 million and 650 to 700 GPUs | NOT FOUND (official) | Only the press page has these figures (EUR 40m EU plus EUR 40m Austria; 650 to 700 GPUs). The official EuroHPC and AIT pages give neither. | tried EuroHPC 2025-03-12 page, AIT blog | – |
| AI Factory | Operational status | FOUND | AIT (consortium lead), 9 April 2026: the AI:AT supercomputer is expected to be operational in 2027. | https://www.ait.ac.at/en/blog/ai-factory-austria-aiat | "It is expected to become operational in 2027." |
| Gigafactory | "No Austrian bid found" | FOUND (contradicts cell) | Vienna submitted an AI Gigafactory expression of interest, signed 18 June 2025 by the Chancellor, the Mayor of Vienna and others. The page says these are not yet formal applications. | https://www.bundeskanzleramt.gv.at/themen/europa-aktuell/2025/07/wien-im-rennen-um-standort-einer-europaeischen-ki-gigafabrik-.html | "Bei den Interessenbekundungen handelt es sich noch nicht um förmliche Bewerbungen." (signed "am 18. Juni 2025") |
| Language resources | CLARIAH-AT and ARCHE | FOUND | ARCHE is a certified CLARIN B-centre at the Austrian Academy of Sciences, in the CLARIAH-AT consortium. CLARIAH-AT is Austria's CLARIN national consortium. | https://centres.clarin.eu/centre/45 ; https://www.clarin.eu/content/participating-consortia | "Austrian Centre for Digital Humanities - A Resource Centre for the HumanitiEs"; type "B", "Certified"; consortium "CLARIAH-AT" |
| Language resources | National corpus of Austrian German | NOT FOUND | Search results point to the Austria Media Corpus (amc) on ARCHE, but the ARCHE metadata page returned 403. Not confirmed from a fetched page. | tried arche.acdh.oeaw.ac.at/browser/metadata/35808 | – |
| Power | Grid figures | NOT FOUND | Not searched. Time went to the higher-value cells. | – | – |

#### C. Prose flags
1. Recommended strategy, step 1: "Teuken and its SOOFI successor are Apache-2.0". The SOOFI model card says "License: closed-beta" and "This model is a beta preview and a research artifact. It is not an open release." (https://huggingface.co/Soofi-Project/Soofi-S-Base). Only Teuken is Apache-2.0.
2. "What good enough means" and step 4 say "180,000 users". The source gives a target of "mehr als 180.000 Bundesbedienstete", not users reached.
3. "What it does not need to do" (no Gigafactory) reads as though Austria never sought one. Vienna filed an expression of interest in June 2025 (see B).

### BE
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Dutch, French, German | CONFIRMED | "Dutch, French, German" | https://european-union.europa.eu/principles-countries-history/eu-countries/belgium_en |
| Languages | Population 11,900,123 (Eurostat 2025) | CONFIRMED | "Population: 11 900 123" (2025 figures) | same |
| Shared with | Dutch with NL | CONFIRMED | "Official EU language(s): Dutch" | https://european-union.europa.eu/principles-countries-history/eu-countries/netherlands_en |
| Shared with | French and German with LU | CONFIRMED | "French, German" | https://european-union.europa.eu/principles-countries-history/eu-countries/luxembourg_en |
| EuroHPC system | None in Belgium | CONFIRMED | None of the 12 listed systems is in Belgium. | EuroHPC supercomputers page |
| EuroHPC system | Lucia at Cenaero, Charleroi | CONFIRMED | "hosted within the A6K ecosystem in Charleroi" | https://www.cenaero.be/en/hpc |
| EuroHPC system | 300 CPU and 50 GPU nodes, about 4 PFlops | CONFIRMED | "a CPU partition with 300 compute nodes"; "a GPU partition with 50 compute nodes"; "approximately 4 PetaFLOPS" | same |
| EuroHPC system | Funded by Wallonia | CONFIRMED | "The supercomputer is funded by the Walloon Region." | same |
| AI Factory | Factory candidacy across Zellik and Charleroi (July 2025) | CONFIRMED | Dated "03/07/2025"; Green Energy Park Zellik and Cenaero Charleroi. | https://focusonbelgium.be/en/international/towards-new-european-scale-artificial-intelligence-hub |
| AI Factory | BE-AIFA selected 13 October 2025 | CONFIRMED | Release dated 13 October 2025, heading BE-AIFA. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en |
| AI Factory | Linked to LUMI and JUPITER | CONFIRMED | "It will be linked with the LUMI AI Factory in Finland and the JUPITER AI-Factory in Germany." | same |
| AI Factory | Coordinated by imec, 23 partners from Flanders, Wallonia, Brussels, federal level | CONFIRMED | "The project is coordinated by imec."; "23 leading research centers, universities, and public institutions" | https://elixir-belgium.org/projects/belgian-ai-factory-antenna |
| AI Factory | EUR 10 million co-funded equally with EuroHPC | CONFIRMED | "total budget of €10 million"; "co-funded equally by the EuroHPC Joint Undertaking and the Belgian federal and regional governments" | same |
| AI Factory | March 2026 to February 2029 | CONFIRMED | "1 March 2026 - 28 February 2029" | same |
| AI Factory | Public-sector transformation among focus areas | CONFIRMED | "as well as the public services digital transformation" | EuroHPC antennas release |
| Gigafactory | Not bidding, per VRT July 2025 (press) | CONFIRMED | "La Belgique n'est pas, à ce stade, candidate pour une gigafactoy de type industriel" | https://www.vrt.be/vrtnws/fr/2025/07/01/la-belgique-est-candidate-pour-accueillir-une-usine-d-intelligen/ |
| Model efforts | Fietje 2 on phi-2, 2.7B | CONFIRMED | "an adapated version of microsoft/phi-2"; "a size of 2.7 billion parameters" | https://huggingface.co/BramVanroy/fietje-2 |
| Model efforts | 28 billion Dutch tokens, MIT | CONFIRMED | "continue-pretrained on 28B Dutch tokens"; licence MIT | same |
| Model efforts | 16 A100 GPUs of the Flemish Supercomputer Centre | CONFIRMED | "four nodes of 4x A100 80GB each (16 total)"; credits the VSC | same |
| Strategy | Flemish AI plan, second cycle 2024 to 2028, decision of 22 March 2024 | CONFIRMED | "2de cyclus van het Vlaamse Beleidsplan Artificiële Intelligentie"; title "…2024-2028…" | https://www.vlaanderen.be/Decision/65F9A588671BD227364EF166 |
| Strategy | EUR 13.98 million for the research programme in 2024 | CONFIRMED | "13,98 miljoen euro" | same |
| Strategy | DigitalWallonia4.ai (2019) | CONFIRMED | Launched 27 Nov 2019; "the effective start took place on July 1, 2019" | https://ai-watch.ec.europa.eu/countries/belgium/belgium-ai-strategy-report_en |
| Strategy | ARIAC 2021 to 2026 | CONFIRMED | "runs from 2021 to 2026" | same |
| Public LLM | Federal chatbot pilot per the 2021 report | CONFIRMED | "the use of AI for a chatbot pilot" (FPS BOSA) | same |
| Language resources | CLARIN-BE since September 2021 under BELSPO with Flemish support | CONFIRMED | "Since September 2021, CLARIN-BE is the Belgian infrastructure…"; "established by BELSPO through the support from Flanders" | https://clarin-be.ivdnt.org/ |
| Language resources | INT in Leiden is its certified B-centre | CONFIRMED | "Instituut voor de Nederlandse Taal"; type "B", "Certified"; consortium "CLARIN-BE". The address gives Leiden but also "Belgium". | https://centres.clarin.eu/centre/22 |
| Institutions | imec, Belnet | CONFIRMED | "imec is coordinating the initiative" | https://belnet.be/en/news-events/news/ai-factory-antenna-connects-belgian-organisations-european-ai-infrastructure |
| Institutions | TRAIL as Walloon and Brussels AI research network | CONFIRMED (wording) | "TRAIL a pour but de créer une structure permettant de mobiliser les capacités de recherche et d'innovation des régions" (it calls itself a structure, not a network) | https://trail.ac/ |
| Institutions | Flemish AI research programme | CONFIRMED (title only) | The page shows only "Vlaams AI-Onderzoeksprogramma". | https://www.flandersairesearch.be/ |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Shares per language community | NOT FOUND | statbel.fgov.be returned a verification challenge. Belgium runs no language census, so only regional populations exist, and those came only from press. | tried statbel structure-population page; WebSearch | – |
| EuroHPC system | Flemish Supercomputer Centre tier-1 | FOUND (name and host only) | The current VSC Tier-1 systems are Hortense at HPC-UGent and sofia at VUB-HPC. No specs in the fetched text. | https://docs.vscentrum.be/compute/tier1.html | "sofia @ VUB-HPC"; "Hortense @ HPC-UGent" |
| Gigafactory | Status in the 2026 call | NOT FOUND | The EuroHPC call page (30 July 2026) names no countries or bidders. Search found no Belgian 2026 bid. | https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en | – |
| Model efforts | Belgian public foundation-model programme | NOT FOUND | Search found nothing. | WebSearch | – |
| Model efforts | Reuse of GPT-NL or French models by Belgian bodies | NOT FOUND | gpt-nl.nl does not mention Belgian reuse; access is "vooralsnog enkel beschikbaar voor Launching Customers". | https://gpt-nl.nl/ | – |
| Strategy | Federal convergence plan of 2022 | NOT FOUND (official) | Search results (law firms, press) put Council of Ministers approval at 28 October 2022. The BOSA page gave a verification challenge and news.belgium.be returned 403, so there is no official page fetched. | tried bosa.belgium.be national-convergence-plan page; news.belgium.be/fr/node/31568/pdf | – |
| Public LLM | Current federal pilots and federal cloud choice | NOT FOUND | BOSA pages challenged the fetch. Search returned only Dutch and other countries' items. | WebSearch; bosa.belgium.be | – |
| Power | No official source | NOT FOUND | Not searched. | – | – |

#### C. Prose flags
1. Main blocker: "GPT-NL is limited to launching customers". CONFIRMED by gpt-nl.nl. No issue.
2. "Recommended strategy", step 1 and the blocker refer to "the French public line" publishing open weights. Not checked here; it belongs to the FR entry.

### DE
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | German; population 83,577,140 (Eurostat 2025) | CONFIRMED | "83 577 140"; "German" | https://european-union.europa.eu/principles-countries-history/eu-countries/germany_en |
| Shared with | Austria (official), Luxembourg | CONFIRMED | Both EU pages list German as an official EU language. | austria_en; luxembourg_en |
| EuroHPC system | JUPITER at Jülich, operational, 1 EFlops sustained | CONFIRMED | JUPITER, Forschungszentrum Jülich campus, Operational, "1 exaflop" | EuroHPC supercomputers page |
| EuroHPC system | EUR 500 million, half EuroHPC, half federal research ministry and NRW | CONFIRMED (sum) | EuroHPC €250m; "BMFTR" €125m; "MKW NRW" €125m. No total is stated. | https://www.fz-juelich.de/en/ias/jsc/jupiter |
| EuroHPC system | 5,884 nodes, four GH200 each | CONFIRMED | "features 5884 compute nodes"; "four GH200 superchips" | https://www.fz-juelich.de/en/ias/jsc/jupiter/tech |
| EuroHPC system | Installation to conclude in 2026 | CONFIRMED | "is expected to conclude in 2026" | same |
| AI Factory | JAIF with JARVIS inference system | CONFIRMED | "As part of JAIF, JUPITER will be extended with the inference system JARVIS." | https://cordis.europa.eu/project/id/101250682 |
| AI Factory | CORDIS EUR 25.0 million, Nov 2025 to Oct 2028 | CONFIRMED | "€ 24 996 884,00"; "1 November 2025" to "31 October 2028" | same |
| AI Factory | With RWTH Aachen, Fraunhofer, TU Darmstadt | CONFIRMED | Participants: RWTH Aachen, Fraunhofer, TU Darmstadt (coordinator FZJ) | same |
| AI Factory | HammerHAI at HLRS with LRZ, KIT, GWDG | CONFIRMED | "High-Performance Computing Center Stuttgart (coordinator)", Leibniz Supercomputing Centre, KIT, GWDG (also SICOS BW) | https://www.hlrs.de/news/detail/hammerhai |
| AI Factory | New system contracted March 2026, EUR 55 million | CONFIRMED | Published 16 March 2026, "Today's signature"; "A total of €55 million has been budgeted" | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-ai-supercomputer-hammerhai-2026-03-16_en |
| AI Factory | Operation expected H2 2026 | CONFIRMED | "is expected to go into operation in the second half of 2026" | same |
| AI Factory | Antennas: BE and HU to JAIF, UK to HammerHAI | CONFIRMED | "JAIF Antennas: Belgium, Hungary"; "HammerHAI Antenna: United Kingdom" | https://www.eurohpc-ju.europa.eu/ai-factories_en |
| Gigafactory | Hightech-Agenda (cabinet 31 July 2025): at least one Gigafactory in Germany (press) | CONFIRMED | "Mindestens eine der europäischen Gigafactories für künstliche Intelligenz solle in Deutschland stehen." The date is inferred from "gestern" in an article published 1 Aug 2025. | https://www.forschung-und-lehre.de/politik/hightech-agenda-passiert-bundeskabinett-7224 |
| Gigafactory | Telekom, IONOS, Schwarz Group IT subsidiary planned separate EoIs (press) | CONFIRMED | "We will submit an expression of interest accordingly" (Telekom); IONOS competing application; "the IT subsidiary of the Schwarz Group" | https://in.marketscreener.com/quote/stock/SAP-SE-436555/news/No-joint-German-bid-for-AI-gigafactory-50284021/ |
| Model efforts | Teuken-7B: economics ministry funding, 2022 to 2024 | CONFIRMED | "funded by the German Federal Ministry for Economic Affairs and Climate Action (BMWK)"; "from January 2022 to December 2024" | https://opengpt-x.de/en/ |
| Model efforts | Fraunhofer, Jülich, TU Dresden, DFKI | CONFIRMED | Developers: "Fraunhofer, Forschungszentrum Jülich, TU Dresden, DFKI" | https://huggingface.co/openGPT-X/Teuken-7B-instruct-commercial-v0.4 |
| Model efforts | 24 EU languages, 4T tokens, JUWELS Booster, Apache-2.0 | CONFIRMED | "all official 24 European languages"; "pre-trained with 4T tokens"; "trained our models on JUWELS Booster"; "released under Apache 2.0" | same |
| Model efforts | SOOFI: about EUR 20 million from the economics ministry | CONFIRMED | "SOOFI is funded with approximately €20 million by the Federal Ministry for Economic Affairs and Energy." | https://www.l3s.de/soofi-launches-europes-path-towards-its-own-ai-language-models/ |
| Model efforts | Announced 18 November 2025 | CONFIRMED (page date) | The L3S article is dated 18 Nov 2025. The KI-Bundesverband news item is dated 17 Nov 2025. | same; https://ki-verband.de/ |
| Model efforts | Coordinated by the German AI Association | CONFIRMED | "The consortium is coordinated by the German AI Association." | L3S page |
| Model efforts | Open model of around 100B parameters plus a reasoning model | CONFIRMED (plan) | "an open AI language model with around 100 billion parameters"; "a specialised reasoning model will be developed" | L3S page; heise |
| Model efforts | Aleph Alpha agreed to merge with Cohere on 16 Sept 2026, pending approval (press) | CONFIRMED | "Cohere Inc. and Aleph Alpha GmbH today signed a merger agreement"; brand change "once the deal clears regulators" | https://siliconangle.com/2026/09/16/cohere-and-aleph-alpha-agree-to-merge-in-reported-20b-deal/ |
| Strategy | AI strategy November 2018, updated December 2020 | CONFIRMED | "am 15. November 2018, hat die Bundesregierung ihre Strategie Künstliche Intelligenz beschlossen"; "Kabinett beschließt Fortschreibung" (file dated 2020-12-01) | https://www.ki-strategie-deutschland.de/ |
| Strategy | Funding raised to EUR 5 billion to 2025 | CONFIRMED | "Bis 2025 werden die Investitionen des Bundes in KI … von drei auf fünf Milliarden Euro erhöht." | same |
| Strategy | Learning strategy, no end date | CONFIRMED | "Die KI-Strategie ist als lernende Strategie angelegt" | same |
| Strategy | Hightech-Agenda 31 July 2025, 10% of economic output on AI by 2030 (press) | CONFIRMED | "bis 2030 zehn Prozent der deutschen Wirtschaftsleistung KI-basiert zu erwirtschaften" | forschung-und-lehre |
| Public LLM | BW F13 for state employees, July 2024 | CONFIRMED | Presented 25 July 2024; "ein KI-Assistenzsystem" for "Mitarbeitenden der Landesverwaltung" | https://www.baden-wuerttemberg.de/de/service/presse/pressemitteilung/pid/mit-dem-neuen-f13-in-die-verwaltung-der-zukunft |
| Public LLM | On Aleph Alpha technology | CONFIRMED | "auf Basis der neuesten Technologie von Aleph Alpha" | same |
| Public LLM | Hosted by STACKIT in the state's own data centre | UNCLEAR | The page says "im eigenen Rechenzentrum" and calls STACKIT "souveräner Cloud-Partner", but does not say STACKIT hosts F13 in the state's data centre. | same |
| Public LLM | Later released as open source | CONFIRMED (linked headline) | Linked release of 23 July 2025: "KI-Assistenz F13 wird zur Open-Source-Software" | same |
| Language resources | Eight CLARIN-D centres, merged into CLARIAH-DE, DFG-funded Text+ | CONFIRMED | "8 German CLARIN centres"; merger with DARIAH-DE; "Text+ is funded by the Deutsche Forschungsgemeinschaft" | https://www.research-in-germany.org/en/research-landscape/why-germany/research-infrastructure/CLARIN.html |
| Institutions | HLRS with LRZ, KIT, GWDG; German AI Association | CONFIRMED | See the HammerHAI row; "Deutschlands größtes KI-Netzwerk" | hlrs.de; ki-verband.de |
| Institutions | JSC, Fraunhofer IAIS and FIT, DFKI, hessian.AI, L3S, IDS | UNCLEAR (not on cited pages) | The two cited pages do not name these. The JAIF CORDIS objective names hessian.AI, Fraunhofer FIT and IAIS. | – |
| Power | JUPITER described as the most energy-efficient of the largest systems | CONFIRMED | "the most energy-efficient system of the top 5 of the listing" | https://www.fz-juelich.de/en/ias/jsc/jupiter |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Charter languages and speaker counts | FOUND (partial) | The Bundestag lists the minority languages Danish, North and Saterland Frisian, Lower and Upper Sorbian and Romani, plus the regional language Low German. The only count is an MP's statement in debate: Low German speakers fell from six million to 2.5 million. No other counts. | https://www.bundestag.de/dokumente/textarchiv/2017/kw22-de-minderheitensprachen/507588 | "Dänisch, Nord- und Saterfriesisch, Nieder- und Obersorbisch sowie Romanes"; "von sechs auf 2,5 Millionen Menschen" |
| Shared with | Diaspora | NOT FOUND | Not searched. | – | – |
| Gigafactory | Status of German consortia in the tender | FOUND (partial) | A Bundestag minor interpellation (19 March 2026) records six expressions of interest for German sites, including Telekom, the Schwarz Group, Ionos, the Bavarian government and Silicon Saxony. It also records that the government told the budget committee it would contribute EUR 805 million from the Sondervermögen. Bid status in the 2026 tender (deadline 12 Nov 2026): NOT FOUND. | https://dserver.bundestag.de/btd/21/048/2104817.pdf | "gibt die Bundesregierung an, sich mit 805 Mio. Euro aus dem Sondervermögen Infrastruktur und Klimaneutralität am Aufbau einer Gigafabrik beteiligen zu wollen" |
| Model efforts | Teuken / OpenGPT-X funding amount | FOUND | About EUR 14 million from the BMWK. TU Dresden gives the project end as 31 March 2025. | https://tu-dresden.de/tu-dresden/newsportal/news/mehrsprachig-und-open-source-forschungsprojekt-opengpt-x-veroeffentlicht-grosses-ki-sprachmodell | "rund 14 Millionen Euro" |
| Model efforts | SOOFI licence and status | FOUND | Soofi-S-Base: 31.6B total parameters (about 3.2B active), closed-beta preview, not an open release. The licence is to be permissive but is not yet set. Training ran 24 March to 13 May 2026. | https://huggingface.co/Soofi-Project/Soofi-S-Base | "This model is a beta preview and a research artifact. It is not an open release."; "Will be released under a permissive license." |
| Public LLM | Federal platforms | FOUND | KIPITZ, the federal AI assistant for public staff. Deutsche Telekom announced (21 May 2026) that it is building a sovereign AI platform for the BMDS on which KIPITZ runs. The source is the operator's own release, not a ministry page. | https://www.telekom.com/de/newsroom/aktuelles/medieninformationen/2026/05/telekom-baut-souveraene-ki-plattform-fuer-die-bundesregierung | "auf der souveränen Infrastruktur der Telekom betrieben" |
| Language resources | German Reference Corpus size | NOT FOUND | The IDS corpus page returned 403. Search showed only dated figures from secondary PDFs. | tried https://www.ids-mannheim.de/digspra/kl/projekte/korpora/ | – |
| Power | Official grid source | NOT FOUND | Search pointed to Bundestag Drucksache 21/4910 (national data-centre strategy, 18/19 March 2026), not fetched. Only law-firm commentary was seen. | WebSearch | – |

#### C. Prose flags
1. Recommended strategy, step 1: "OpenGPT-X ended in December 2024". opengpt-x.de gives Jan 2022 to Dec 2024, but TU Dresden gives the end as 31 March 2025 ("will end on March 31, 2025"). The sources conflict.
2. "is funding a 100-billion-parameter successor". That was the plan. The first SOOFI release is a 31.6B closed-beta preview with no final licence (HF model card). Steps 1 and 4 call the German public line Apache-2.0, which holds for Teuken only.
3. Step 1: "SOOFI runs on a grant to July 2026 per press". CONFIRMED by heise: "is funding the project with 20 million euros until July 2026".

### LU
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Law of 24 Feb 1984: administrative languages French, German, Luxembourgish; French alone authentic in legislation | CONFIRMED | "'French, German or Luxembourgish may be used' in administrative and judicial matters"; "only the French language text is deemed authentic" | https://luxembourg.public.lu/en/society-and-culture/languages/languages-spoken-luxembourg.html |
| Languages | Luxembourgish the national language | CONFIRMED (other cited page) | The cited page does not say so. The gouvernement.lu Sproochegesetz page (cited in the language-resources row) says Luxembourgish was "légalement été reconnu comme langue nationale". | https://gouvernement.lu/fr/actualites/toutes_actualites.gouv2024_mcult+fr+actualites+mes-actualites+2024+fevrier+sproochegesetz-40-joer.html |
| Languages | 2018 study: French 98%, English 80%, German 78%, Luxembourgish 77% | CONFIRMED | "98% of the Luxembourg population speaks French"; 80% English, 78% German, 77% Luxembourgish | luxembourg.public.lu |
| Languages | Large Portuguese-speaking community | CONFIRMED | "followed by Luxembourgish, German, English and Portuguese"; Portuguese immigrants use their mother tongue at work | same |
| Languages | Population 681,973 (Eurostat 2025) | CONFIRMED | "Population: 681 973" | luxembourg_en |
| Shared with | French, German shared | CONFIRMED | "French, German" | luxembourg_en |
| EuroHPC system | MeluXina, LuxProvide, Bissen, operational, 12.81 PFlops | CONFIRMED | Luxembourg, Bissen, Operational, "12.81 petaflops" | EuroHPC supercomputers page |
| AI Factory | First round, 10 December 2024 | CONFIRMED | Release "10 December 2024" | https://eurohpc-ju.europa.eu/selection-first-seven-ai-factories-drive-europes-leadership-ai-2024-12-10_en |
| AI Factory | Coordinated by LuxProvide with Luxinnovation, LNDS, the University, LIST | CONFIRMED | LuxProvide coordinates; "Bringing together expertise from Luxinnovation", LNDS, University of Luxembourg, LIST | same; CORDIS lists LuxProvide as coordinator, LNDS in the objective text only |
| AI Factory | MeluXina-AI over 2,100 GPU accelerators | NOT CONFIRMED | The EuroHPC contract page says "across 252 nodes for a total of 1,008 GPUs" (NVIDIA GB200 NVL4). No figure near 2,100 appears. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-meluxina-ai-new-ai-optimised-supercomputer-luxembourg-ai-factory-2026-07-22_en |
| AI Factory | Contracted 22 July 2026 for EUR 80 million | CONFIRMED | Published 22 July 2026, "signed a procurement contract"; "EUR 80 000 000" | same |
| AI Factory | Installation from autumn 2026, Bissen and Bettembourg | CONFIRMED | "Installation activities are expected to start in fall of 2026."; Bissen and Bettembourg | same |
| AI Factory | Committee report: total EUR 126m (EUR 63m EuroHPC, EUR 60m national) | CONFIRMED | "l'investissement total s'élève à 126 millions d'euros, dont 63 millions d'euros seront financés par l'EuroHPC JU" … "60 millions d'euros resteront à charge du budget national" | https://wdocs-pub.chd.lu/docs/Dossiers_parlementaires/8518/20250827_RapportCommission.pdf |
| AI Factory | Ireland's antenna attaches to it | CONFIRMED (secondary link) | "Antenna: Ireland" under Luxembourg. The antennas release says it is "primarily linked with AI2F, the AI Factory in France as well as with the Luxembourg AI Factory". | ai-factories page; antennas release |
| Model efforts | Mistral partnership June 2025; on-site deployment, data on Luxembourg territory | CONFIRMED | "The strategic partnership signed in June 2025 between Luxembourg and Mistral AI"; "data stored on Luxembourg territory" | https://gouvernement.lu/en/actualites/toutes_actualites/communiques/2026/03-mars/04-frieden-ai4lux.html |
| Model efforts | Legal chatbot on Legilux; chatbot on main government sites | CONFIRMED (planned) | "dedicated legal chatbot on the Legilux platform"; chatbot for "the most visited government websites" | same |
| Model efforts | LuxEmbedder, Luxembourgish sentence embedding, COLING 2025 | CONFIRMED | "an enhanced sentence embedding model for Luxembourgish"; "Accepted at COLING 2025" | https://arxiv.org/abs/2412.03331 |
| Strategy | AI Strategy published May 2025 | CONFIRMED | Last update 22.05.2025; Luxinnovation: "officially presented on 19 May 2025" | gouvernement.lu strategy page; luxinnovation |
| Strategy | Under "Accelerating Digital Sovereignty 2030", with data and quantum strategies | CONFIRMED | Data, AI and quantum are "the three key pillars of national strategies" (Luxinnovation article titled after the initiative) | https://luxinnovation.lu/news/government-unveils-strategic-initiative-accelerating-digital-sovereignty-2030 |
| Strategy | New budgetary resources 2025 to 2030, amounts not stated | CONFIRMED | "new dedicated budgetary resources allocated for the 2025–2030 period" | same |
| Strategy | In force; AI4LUX campaign March 2026 | CONFIRMED (AI4LUX) / UNCLEAR (in force) | AI4LUX launched per the 04.03.2026 release. "In force" is not stated. | gouvernement.lu AI4LUX |
| Public LLM | All civil servants to get a sovereign chatbot that can build agents (March 2026) | CONFIRMED | "all civil servants will, in the coming weeks, gain access to a sovereign chatbot" | gouvernement.lu AI4LUX |
| Public LLM | Able to handle sensitive information | UNCLEAR | Not confirmed by the WebFetch summary. The page stresses local deployment and data confidentiality. | same |
| Language resources | ZLS, law of 20 July 2018, spelling, grammar, online dictionary | CONFIRMED | Created by the law of 20 July 2018; "publie les règles de l'orthographe et la grammaire"; runs the LOD | gouvernement.lu Sproochegesetz page |
| Institutions | LuxProvide, LIST, University, Luxinnovation | CONFIRMED | CORDIS: coordinator LUXPROVIDE SA; participants Luxinnovation GIE, PNED GIE, Université du Luxembourg, LIST | https://cordis.europa.eu/project/id/101234366 |
| Institutions | LNDS, LuxConnect, ZLS | UNCLEAR (not on cited page) | CORDIS names LNDS only in the objective text. LuxConnect is absent there but the committee report says MeluXina-AI is hosted on "deux sites de LuxConnect S.A.". | CORDIS; chd.lu report |
| Power | More than half of the five-year operating cost is electricity and cooling | CONFIRMED | "32 millions d'euros de coûts opérationnels (dont plus de la moitié est destinée à couvrir les besoins en électricité et refroidissement) sur cinq ans" | chd.lu report |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Gigafactory | No bid found | NOT FOUND | Search found no Luxembourg Gigafactory expression of interest. The 2026 call page names no countries. | WebSearch; EuroHPC call page | – |
| Model efforts | No Luxembourgish generative model | NOT FOUND | Search surfaced a Feb 2026 uni.lu item on "LuxVLD" (Microsoft-funded), but the page fetched empty, so its nature is unconfirmed. | tried https://www.uni.lu/en/?p=8541 | – |
| Public LLM | Rollout completion | FOUND | Since mid-June 2026, more than 14,000 public agents have access to a sovereign AI agent (government briefing, July 2026). | https://gouvernement.lu/dam-assets/images-documents/actualites/2026/07-juillet/06-obertin-ia/document/manner-sichen-einfach-froen.pdf | "Depuis la mi-juin 2026, plus de 14 000 agents publics ont accès à un agent IA souverain." |
| Language resources | CLARIN membership | FOUND | Luxembourg is not among CLARIN ERIC members on the participating-consortia page. | https://www.clarin.eu/content/participating-consortia | Members list (Austria … United Kingdom) does not include Luxembourg |
| Language resources | National corpus | NOT FOUND | Search found only the LOD dataset and academic datasets. No national corpus page. | WebSearch | – |
| Power | Grid constraints | NOT FOUND | The committee report records the Chamber of Commerce's call for "un approvisionnement en électricité décarbonée, fiable et compétitive", but no grid constraint. | chd.lu report | – |

#### C. Prose flags
1. "a first-round factory with a large accelerator count for its size" rests on the ">2,100 GPU accelerators" figure. The contract page gives 1,008 GPUs.
2. "Luxembourgish, the national language spoken by three quarters of residents": 77% per the 2018 study. CONFIRMED.

### NL
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Dutch official; Frisian official in Fryslân | CONFIRMED | "Nederlands is de officiële taal van Nederland."; "Het Fries is een officiële taal in de provincie Fryslân." | https://www.rijksoverheid.nl/onderwerpen/erkende-talen/erkende-talen-in-nl |
| Languages | Dutch Sign Language recognised | CONFIRMED | "De Nederlandse Gebarentaal is erkend" | same |
| Languages | Limburgish, Low Saxon, Yiddish, Romani, Papiamentu recognised under the Charter | CONFIRMED | "erkent het Fries, Papiaments, Limburgs en Nedersaksisch als regionale talen"; "Jiddisch … en Romanes" | same |
| Languages | Papiamentu and English official in the Caribbean municipalities | NOT CONFIRMED | The page mentions Papiamentu on Bonaire under Part III of the Charter but does not call it official there, and does not mention English. | same |
| Languages | Population 18,044,027 (Eurostat 2025) | CONFIRMED | "Population: 18 044 027" | netherlands_en |
| Shared with | Dutch official in Belgium | CONFIRMED | "Dutch, French, German" | belgium_en |
| EuroHPC system | None; SURF in the Alice Recoque consortium | CONFIRMED | None in the NL; the Netherlands participates through SURF in Alice Recoque. | EuroHPC supercomputers page |
| EuroHPC system | Snellius at SURF | CONFIRMED | The page describes Snellius with "GPGPUs"; no counts. | https://www.surf.nl/en/services/compute/snellius-the-national-supercomputer |
| EuroHPC system | Sept 2026 cabinet letter names investment in its successor | CONFIRMED | "investering in de opvolger van de nationale supercomputer" | https://www.eerstekamer.nl/behandeling/20260921/brief_van_de_staatssecretaris_van/document3/f=/vn18lk58uobh.pdf |
| AI Factory | NLAIF selected 10 October 2025 | CONFIRMED | Release dated 10 October 2025 | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-six-additional-ai-factories-expand-europes-ai-capabilities-2025-10-10_en |
| AI Factory | Led by the AI Factory foundation with SURF, TNO, Samenwerking Noord, AIC4NL | CONFIRMED | "The AIFNL Foundation will be the lead partner … with a consortium comprising SURF, Samenwerking Noord, TNO and AIC4NL." | same |
| AI Factory | In Groningen | CONFIRMED | The Rijksoverheid page names Groningen. The EuroHPC page does not. | https://www.rijksoverheid.nl/actueel/nieuws/2025/06/27/nederland-zet-in-op-200-miljoen-euro-voor-aifabriek-in-groningen |
| AI Factory | Cabinet decision 27 June 2025: EUR 70m national, 60m regional, 70m requested from EuroHPC, 200m total | CONFIRMED | "€ 70 miljoen"; "€ 60 miljoen"; "Europese cofinancieringsaanvraag van € 70 miljoen"; "€ 200 miljoen" (EuroHPC not named) | same |
| AI Factory | CORDIS EUR 14.1 million, July 2026 to June 2029 | CONFIRMED | "€ 14 101 608,86"; "1 July 2026" to "30 June 2029" | https://cordis.europa.eu/project/id/101314093 |
| AI Factory | Press: fully operational by early 2028 | CONFIRMED (press) | "expected to be fully operational by early 2028" | https://ioplus.nl/en/posts/eurofiber-to-host-ai-facility-in-groningen |
| Gigafactory | Eneco and Volt submitted EoIs; on 23 Feb 2026 asked ministers for a financial commitment or compute pre-purchase; participation "not possible" without it | CONFIRMED | "several Dutch parties, including Eneco and Volt, have already submitted an expression of interest"; "without a financial commitment from the Netherlands participation in the European tender will not be possible" | https://news.eneco.com/eneco-and-volt-political-action-needed-for-ai-gigafactory/ |
| Model efforts | GPT-NL by TNO, NFI, SURF; EUR 13.5m from the economics ministry; announced Nov 2023 | CONFIRMED | "Non-profit parties TNO, NFI and SURF will jointly develop the model"; "has pledged 13.5 million"; dated 2 Nov 2023 | https://www.tno.nl/en/newsroom/2023/11/netherlands-starts-realisation-gpt-nl/ |
| Model efforts | Training since June 2025; over 20B news tokens; publishers remunerated | CONFIRMED | "Training started in June 2025."; "over 20 billion tokens"; "publishers will receive appropriate remuneration" | https://www.tno.nl/en/newsroom/2025/07/large-dataset-news-organizations-dutch/ |
| Model efforts | Lawfully obtained data; access limited to launching customers; code repos open-sourced March 2026; v.1 autumn 2026 | CONFIRMED | "rechtmatig verkregen data"; "enkel beschikbaar voor Launching Customers"; 19 March 2026 "Open source publicatie van eerste drie code repositories"; "Najaar 2026: GPT-NL v.1" | https://gpt-nl.nl/ |
| Model efforts | Cabinet makes EUR 120m available for an IPCEI on AI (Sept 2026) | CONFIRMED | "Het kabinet stelt € 120 miljoen beschikbaar voor Nederlandse deelname aan een IPCEI voor Artificial Intelligence (AI)" | eerstekamer 21 Sept 2026 letter |
| Strategy | NDS priority 3 AI, "open language models from the Netherlands or the EU" | CONFIRMED | "open language models from the Netherlands or the EU" | https://www.nldigitalgovernment.nl/dossiers/priority-3-artificial-intelligence/ |
| Strategy | Letter of 21 Sept 2026 on digital economy and sovereignty | CONFIRMED | "Digitale Economie en Soevereiniteit"; "Den Haag, 21 september 2026" | eerstekamer letter |
| Strategy | Letter lines: Groningen factory, IPCEI, shared government AI infrastructure under exploration | CONFIRMED | "Ik ondersteun de realisatie van de AI-fabriek in Groningen"; "We verkennen het realiseren van een hoogwaardige gedeelde AI-infrastructuur van de overheid." | same |
| Public LLM | ICTU, 27 municipalities and TNO trialling GPT-NL with "Gem" (Feb 2026) | CONFIRMED | "ICTU, 27 local councils, and TNO are the first to trial GPT-NL for the virtual assistant Gem" (26 Feb 2026) | nldigitalgovernment priority 3 |
| Public LLM | Government-wide generative-AI monitor (Dec 2025) | CONFIRMED | "TNO published the 1st Government-wide Monitor on Generative AI" (4 Dec 2025) | same |
| Public LLM | AI marketplace under Apply AI | NOT CONFIRMED on cited page | Not on nldigitalgovernment. It is confirmed in the 21 Sept 2026 letter: "een AI-marktplaats waarvoor recent Europees budget … 'Apply AI: GenAI for public administrations'". Add that URL to the cell. | eerstekamer letter |
| Language resources | INT, certified CLARIN B-centre, large Dutch corpora, listed under CLARIN-BE | CONFIRMED | Type "B", "Certified"; "large Dutch corpora"; consortium "CLARIN-BE" | https://centres.clarin.eu/centre/22 |
| Institutions | SURF; TNO and NFI; AI Factory foundation, AIC4NL, Samenwerking Noord | CONFIRMED | CORDIS coordinator "Stichting Nederlandse AI-fabriek"; participants SURF, AICoalitie4NL, Samenwerking Noord, TNO; gpt-nl.nl names TNO, NFI, SURF | CORDIS; gpt-nl.nl |
| Institutions | ICTU, INT | UNCLEAR (not on cited pages) | Both are confirmed on other cited pages (nldigitalgovernment; CLARIN centre 22). | – |
| Power | Over 15,000 large-consumer applications queued end-2025 | CONFIRMED | "de wachtrij voor grootverbruikers op 31 december jl. ruim 15.000 aanvragen van afnemers omvat" | https://www.eerstekamer.nl/nonav/behandeling/20260402/brief_regering_voortgang_aanpak/document3/f=/vmwpn4ekmqzi.pdf |
| Power | Coalition agreement gives congestion highest priority | CONFIRMED | "Het Coalitieakkoord «Aan de slag» kent de aanpak van netcongestie dan ook de hoogste prioriteit toe." | same |
| Power | Central-government approach to data-centre capacity due autumn 2026 | CONFIRMED | "een sterkere regierol voor de Rijksoverheid voor het ontwikkelen van datacentercapaciteit … Dit najaar zal ik die aanpak met uw Kamer delen." | 21 Sept 2026 letter |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speaker counts | NOT FOUND | The Fryske Taalatlas 2020 PDF on the province's CDN returned 403. Rijksoverheid gives no counts. | tried cuatro.sim-cdn.nl Fryske Taalatlas 2020 | – |
| Shared with | Diaspora | NOT FOUND | Not searched. | – | – |
| EuroHPC system | Snellius GPU count and performance | FOUND (partial) | TOP500 (06/2026): "Snellius Phase 3 GPU", Nvidia H100 SXM5 94GB, 52,096 cores, Rmax 13.64 PFlop/s, Rpeak 21.66 PFlop/s, rank 148. That is one partition, not the whole system, and the source is TOP500, not SURF. | https://top500.org/system/180316 | "Snellius Phase 3 GPU - ThinkSystem SD665-N V3 … Nvidia H100 SXM5 94Gb"; Rmax "13.64 PFlop/s" |
| Gigafactory | Government position and bid status | FOUND | Cabinet letter of 31 March 2026 (Kamerstuk 26643 nr. 1499): no budget room for the financial commitments the joint Gigafactory procurement requires. The cabinet prefers Gigafactories fully financed by the market. | https://zoek.officielebekendmakingen.nl/kst-26643-1499.pdf | "binnen de huidige begroting geen ruimte bestaat voor het aangaan van de vereiste financiële verplichtingen" |
| Model efforts | GPT-NL size, base, licence | NOT FOUND | The GPT-NL Hugging Face organisation lists no models ("None public yet"); datasets only. TNO and gpt-nl.nl pages are silent. | https://huggingface.co/GPT-NL | "None public yet" |
| Model efforts | ASML and Mistral partnership | NOT FOUND (official) | asml.com redirects to investor.asml.com, which returned 403. Search results give 9 Sept 2025 and EUR 1.3bn, but no page was fetched. | tried asml.com and investor.asml.com | – |
| Strategy | NDS formal adoption date | NOT FOUND (official) | nldigitalgovernment says only that the government "announced" the NDS. Press found by search says the ministerraad approved it on 4 July 2025, but no official page was fetched. | https://www.nldigitalgovernment.nl/overview/dutch-digitalisation-strategy/ | – |
| Language resources | SoNaR corpus | FOUND | SoNaR-500, more than 500 million words, distributed by the Dutch Language Institute; owner Taalunie, financed by NTU/STEVIN. | https://taalmaterialen.ivdnt.org/download/tstc-sonar-corpus/ | "meer dan 500 miljoen woorden tekst" |
| Language resources | CLARIAH-NL | FOUND | CLARIAH-NL is the Dutch CLARIN national consortium, led by the KNAW Humanities Cluster. | https://www.clarin.eu/content/participating-consortia | "National Consortium: CLARIAH-NL"; "Leading NC Partner: KNAW Humanities Cluster" |

#### C. Prose flags
1. Recommended strategy, step 7: "Decide the Gigafactory on the grid … Eneco and Volt ask for a pre-purchase". The cabinet already decided on 31 March 2026 that the budget has no room for the commitment, and prefers market-financed Gigafactories (Kamerstuk 26643 nr. 1499). The blocker's "if the government pre-purchases Gigafactory compute" should reflect this decision.
2. "What good enough means": "with Frisian and the Caribbean municipalities' languages where the law provides". This relies on the NOT CONFIRMED claim that Papiamentu and English are official in the Caribbean municipalities.
3. Step 5: "serves 25 million Dutch speakers". The figure is not in any cited source.

### Summary
| State | Claims checked | Confirmed | Not confirmed | Unclear | Unverified cells | Found | Not found |
|---|---|---|---|---|---|---|---|
| AT | 28 | 26 | 0 | 2 | 8 | 5 | 3 |
| BE | 29 | 29 | 0 | 0 | 8 | 1 | 7 |
| DE | 35 | 33 | 0 | 2 | 8 | 5 | 3 |
| LU | 27 | 23 | 1 | 3 | 6 | 2 | 4 |
| NL | 32 | 29 | 2 | 1 | 9 | 4 | 5 |

Counting notes: the LU strategy row that is part confirmed and part unclear ("in force") is counted as unclear. "CONFIRMED (press)", "(plan)", "(sum)", "(partial)" and similar qualified verdicts are counted as confirmed. In Task B, partial finds count as FOUND and "NOT FOUND (official)" counts as not found. The AT Gigafactory cell is FOUND and contradicts the snapshot.

## Review: Bulgaria, Romania, Greece, Cyprus and Ireland (BG, CY, EL, IE, RO), 2026-10-10
Tools: WebSearch available yes (about 30 queries); about 104 distinct URLs fetched; 16 failed (403: irishstatutebook.ie, 4 gov.ie pages, gov.cy census page, fra.europa.eu, digital-skills-jobs.europa.eu; 404: parapolitika.gr article, hpcf.cyi.ac.cy/cyclone.html; hang-up: legislatie.just.ro; redirect to home page: pio.gov.cy, dfa.ie; empty or unreadable: parliament.bg (en and bg), constcourt.bg PDF). Each failure was retried once at most. Two xlsx files (NSI and the Romanian census) and one PDF (CYSTAT) were parsed locally, because WebFetch could not read them.

Method notes: a verdict applies to the URL(s) cited in that row. When a fact sits on a different page from the one cited, the verdict is NOT CONFIRMED for the cited page, and the page that does carry the fact is named.

### BG
#### A. Verification
| Row | Claim | Verdict | Evidence (quote ≤25 words, or what the page says) | URL |
|---|---|---|---|---|
| Languages | Census 2021 total 6,519,789 | CONFIRMED | xlsx sheet "POPULATION BY MOTHER TONGUE … AS OF 07.09.2021": "Total for the country 6519789" | nsi.bg/en/file/download/b6f1e478… |
| Languages | Bulgarian mother tongue 5,037,607 | CONFIRMED | same row: Bulgarian "5037607" (note: 616,681 are "Unknown") | same |
| Languages | Turkish 514,386 | CONFIRMED | same row: Turkish "514386" | same |
| Languages | Roma 227,974 | CONFIRMED | same row: Roma "227974" | same |
| Shared with | North Macedonia's antenna is attached to Greece's factory | CONFIRMED | "As an Antenna to the Pharos AI Factory, this effort will be implemented by UKIM" (VEZILKA) | eurohpc antennas 2025-10-13 |
| EuroHPC system | Discoverer at Sofia Tech Park | CONFIRMED | Discoverer listed in Sofia, Bulgaria, hosted by Sofia Tech Park | eurohpc our-supercomputers |
| EuroHPC system | Operational | CONFIRMED (weak) | EuroHPC lists access and a June 2026 TOP500 rank (#317); Sofia Tech Park: "DC accomplished and ready for operations" | our-supercomputers; sofiatech petascale |
| EuroHPC system | 4.52 PFlops sustained | CONFIRMED | 4.52 petaflops sustained, 5.94 peak | our-supercomputers |
| EuroHPC system | 144,384 AMD cores | CONFIRMED | "The number of processor cores is 144,384"; CPU "AMD EPYC 7H12 64core" (EuroHPC) | sofiatech petascale; our-supercomputers |
| EuroHPC system | Liquid-cooled | CONFIRMED | "Direct Liquid Cooling (DLC) technology" | sofiatech petascale |
| EuroHPC system | Co-funded by EuroHPC and the government | CONFIRMED | "Co-funded by the European High-Performance Computing Joint Undertaking (EuroHPC JU) and the Bulgarian government" | discoverer.bg/about-discoverer |
| AI Factory | BRAIN++ | CONFIRMED | "The Bulgarian Robotics & AI Nexus (BRAIN++)" | eurohpc ai-factories/bulgaria |
| AI Factory | Selected 12 March 2025 | CONFIRMED | Press release dated 12 March 2025, which names the Bulgarian factory | eurohpc 2025-03-12 |
| AI Factory | Led by Sofia Tech Park | CONFIRMED | "BRAIN++ is an independent initiative lead by Sofia Tech Park (STP)" | eurohpc bulgaria |
| AI Factory | With INSAIT and the Discoverer team | CONFIRMED | INSAIT and "the Bulgarian supercomputer Discoverer's team" contribute "specialized knowledge in AI research and high-performance computing infrastructure" | eurohpc bulgaria |
| AI Factory | Discoverer++ tender estimated EUR 54,228,600 | CONFIRMED | "The estimated total value for the call is EUR 54 228 600." | eurohpc Discoverer++ tender |
| AI Factory | Deadline 16 October 2026 | CONFIRMED | "16 October 2026, 16:00 (CEST)" (the description says CET) | same |
| AI Factory | Installation by end-2026 | CONFIRMED | "Discoverer++ is planned to be installed at Sofia Tech Park supercomputing datacentre by the end of 2026." | same |
| AI Factory | Focus: Bulgarian LLMs, hosting BgGPT, federated data lake, sandbox | CONFIRMED | "Hosting and development of models like BgGPT for Bulgarian language processing"; "federated AI data lake"; "BulgAI Sandbox" | eurohpc bulgaria |
| Models | Gemma-2-27B continued pretraining on about 100 B tokens | CONFIRMED | "continuously pre-trained on around 100 billion tokens (85 billion in Bulgarian)" | HF BgGPT-Gemma-2-27B README |
| Models | 85 B of them Bulgarian | CONFIRMED | same quote | same |
| Models | BgGPT 3.0 on 26 March 2026 | CONFIRMED | Announcement dated March 26, 2026 | insait.ai BgGPT 3.0 article |
| Models | Gemma 3 in 4B, 12B and 27B | CONFIRMED | "Available in 4B, 12B and 27B sizes." | HF BgGPT-Gemma-3-27B-IT |
| Models | Gemma licence | CONFIRMED | "distributed under the Gemma Terms of Use" | HF (both cards) |
| Models | Free public chat, apps, API | CONFIRMED | "any user can use its features freely and at no cost"; models "can also be accessed directly via API key" | insait.ai article |
| Models | Google credited for cloud training credits | CONFIRMED | thanks Google for "GCP credits needed to train the BgGPT models" | insait.ai article |
| Strategy | "Concept for the development of AI in Bulgaria until 2030" | CONFIRMED | "Concept for the development of artificial intelligence in Bulgaria until 2030" | AI Watch BG |
| Strategy | December 2020 | CONFIRMED | "published its National AI strategy (Bulgaria, 2020) in December 2020" | AI Watch BG |
| Strategy | Reliable AI infrastructure priority | CONFIRMED | "Building a reliable infrastructure for AI development" | AI Watch BG |
| Strategy | National AI research centre with scalable HPC | CONFIRMED | "scalable high performance computing infrastructure in the national AI Research Centre of Excellence" | AI Watch BG |
| Strategy | EuroHPC page says BRAIN++ aligns with it | CONFIRMED | "By aligning with Bulgaria's National AI Strategy, BRAIN++ seeks to foster collaboration" | eurohpc bulgaria |
| Public sector | Projects with the National Revenue Agency and the National Audit Office | CONFIRMED | "the National Revenue Agency and the Bulgarian National Audit Office" | insait.ai article |
| Public sector | "running on dedicated infrastructure" | CONFIRMED (wording) | The page says "These projects run on dedicated infrastructure, ensuring data security." The note's quoted form "running on" is not verbatim. | insait.ai article |
| Public sector | BgGPT 3.0 free for Bulgarian institutions | CONFIRMED | "freely available to Bulgarian users and institutions" | insait.ai article |
| Public sector | Talks with the government on a strategic AI partnership (June 2026) | CONFIRMED | Headline of 16 June 2026: "INSAIT and Bulgarian government discuss strategic partnership in AI and innovation" | insait.ai home |
| Language resources | CLaDA-BG, the Bulgarian CLARIN consortium led by the Academy of Sciences | CONFIRMED | Member table: Bulgaria, CLaDA-BG, leading partner the Bulgarian Academy of Sciences | clarin.eu/node/3754 |
| Language resources | BRAIN++ plans a federated data lake | CONFIRMED | "Access to high-quality datasets through a federated AI data lake" | eurohpc bulgaria |
| Institutions | INSAIT is part of Sofia University | UNCLEAR | insait.ai shows an "SU-ENG" logo under "In partnership with:", with no text naming the university | insait.ai |
| Institutions | ETH Zurich and EPFL as partners | CONFIRMED | Both logos appear under "In partnership with:" | insait.ai |
| Institutions | Sofia Tech Park (Discoverer, BRAIN++ lead) | CONFIRMED | see the AI Factory rows | eurohpc bulgaria |
| Institutions | BAS (CLaDA-BG) | CONFIRMED | see the language resources row | clarin.eu |
| Power | Discoverer has a 1 MW UPS | CONFIRMED | "uninterruptible power supply (UPS) with a capacity of 1 MW" | sofiatech petascale |
| Power | Direct liquid cooling | CONFIRMED | "Direct Liquid Cooling (DLC) technology" | sofiatech petascale |
| Power | Tender requires energy efficiency, gives no power figure | CONFIRMED | Lists "Energy efficiency." and gives no wattage figure | eurohpc Discoverer++ tender |

The Gigafactory row cites the call page; that page names no bidders or states, which is consistent with the note.

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Constitutional provision | NOT FOUND | parliament.bg (en and bg) returned an empty shell; the constcourt.bg PDF is an encrypted scan. Search snippets show Art. 3, but only from non-official hosts. | — | — |
| Shared with | Language shared with | NOT FOUND | Only the cited antenna page was checked; no official page on Bulgarian-Macedonian sharing was searched. | — | — |
| EuroHPC system | Co-funding amounts | FOUND | EUR 4 M European, EUR 7.5 M Bulgarian (Sofia Tech Park, 13 March 2021); EuroHPC gives a total of about EUR 11.5 M | https://sofiatech.bg/en/?p=27756 ; https://eurohpc-ju.europa.eu/discoverer-powers-bulgarian-eurohpc-supercomputer-inaugurated-2021-10-21_en | "The European investment in Discoverer is 4 million euro, while the co-funding by Bulgaria is another 7,5 million euro." / "joint investment of about EUR 11,5 million from the EuroHPC JU and the Republic of Bulgaria" |
| AI Factory | EUR 90 M total, 50% national | FOUND | BRAIN++ budget EUR 90 M, with a commitment to 50% national funding from 2026 (Sofia Tech Park, 12 March 2025; INSAIT gives the same EUR 90 M) | https://sofiatech.bg/en/?p=43068 ; https://insait.ai/bulgaria-will-have-its-own-ai-factory-a-project-for-90m-eur/ | "will have a budget of 90 million euros"; "commitment to provide 50% national funding from 2026" |
| Gigafactory | No Bulgarian bid | NOT FOUND (bid) | No bid document. Related official fact: on 3 Oct 2025 the government said it was exploring a gigafactory with IBM and the Commission. | https://www.mig.government.bg/breaking-news/bulgaria-explores-possibility-of-building-an-ai-gigafactory-in-partnership-with-ibm-and-the-european-commission/?lang=en | "We are exploring the possibility of building an AI gigafactory in partnership with IBM and the European Commission." |
| Models | BgGPT public funding | NOT FOUND | INSAIT pages credit only Google GCP credits; no public funding line was found | — | — |
| Strategy | Council of Ministers decision reference | NOT FOUND | OECD.AI gives the approval date (16 December 2020) but no decision number | https://oecd.ai/en/dashboards/policy-initiatives/concept-for-the-development-of-ai-in-bulgaria-until-2030-4622 | "The Bulgarian government approved on 16 December 2020 its national AI strategic document." |
| Public sector | Procurement details | NOT FOUND | No procurement notice found | — | — |
| Language resources | CLaDA-BG site 404 | FOUND (site) | clada-bg.eu/organization is reachable. It describes the national research infrastructure but does not name BAS as lead. | https://clada-bg.eu/organization/ | "Bulgarian national research infrastructure for resources and technologies for language, cultural and historical heritage" |
| Institutions | INSAIT state funding | NOT FOUND | Search found press figures only (not fetched); no official budget line was found | — | — |

#### C. Prose flags
1. "The model is deployed at the National Revenue Agency and the National Audit Office": INSAIT says it is "implementing projects" with them. "Deployed" is stronger than the source.

### CY
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Greek and Turkish, Art. 3(1) | CONFIRMED | "The official languages of the Republic are Greek and Turkish." | constituteproject Cyprus_2013 |
| Languages | 923,381 residents (government-controlled areas) | CONFIRMED (press) | "which on 1 October 2021 reached 923,381 persons" | cbn.com.cy 107087 |
| Languages | 77.9% Cypriot citizens | CONFIRMED (press) | "719,252 persons or 77.9% were Cypriots" | same |
| Languages | No language question | UNCLEAR | The press page does not mention language either way | same |
| Shared with | Greek with Greece | CONFIRMED | Greek listed as official EU language; "1981: Greek" | europa.eu languages |
| Shared with | Turkish is not an EU language | CONFIRMED | Turkish absent from the 24 listed | same |
| Shared with | Pharos-CY tied to the Greek factory with joint Greek LLM work | CONFIRMED | "Large Language Models (LLMs) and digital tools for the Greek language" | cyi.ac.cy Pharos-CY |
| EuroHPC system | None in Cyprus | CONFIRMED | EuroHPC's list of 12 systems has none in Cyprus | eurohpc our-supercomputers (cross-checked) |
| EuroHPC system | CyI is a DAEDALUS consortium member | CONFIRMED | Cyprus "also involved in the project as members of the DAEDALUS consortium" | eurohpc 2022-11-28 |
| EuroHPC system | Access in proportion to investment (for Cyprus) | NOT CONFIRMED | The proportional clause names only Greece and the JU: "jointly managed by Greece and the EuroHPC JU in proportion to their investments" | eurohpc 2022-11-28 |
| EuroHPC system | National facility at CyI | CONFIRMED | "The Cyprus Institute has built a national facility that combines large-scale simulation capacity with modern AI acceleration" | hpcf.cyi.ac.cy/about |
| EuroHPC system | CaSToRC runs it | NOT CONFIRMED | CaSToRC is not mentioned on the cited page | hpcf.cyi.ac.cy/about |
| EuroHPC system | Cyclone | CONFIRMED | "Cyclone anchors our open-access services for large-scale simulations" | same |
| EuroHPC system | RRF-funded Aphroditi edge-AI platform | CONFIRMED | "Aphroditi is part of the Cyprus Edge-AI Hub initiative"; EDGE-AI "funded by the European Union Recovery and Resilience Facility" | same |
| EuroHPC system | EuroCC competence centre | CONFIRMED | "Recognized as the National HPC Competence Centre (EuroCC)" | same |
| AI Factory | Antenna "Pharos-CY" | CONFIRMED | Pharos-CY listed for Cyprus | eurohpc antennas |
| AI Factory | Selected 13 October 2025 | CONFIRMED | Press release dated 13 October 2025 | same |
| AI Factory | Linked to Pharos "including access to the DAEDALUS supercomputer" | CONFIRMED | "linked with the Pharos AI Factory in Greece including access to the DAEDALUS supercomputer" | same |
| AI Factory | 1 April 2026 to 31 March 2029 | CONFIRMED | CORDIS dates | cordis 101263007 |
| AI Factory | EUR 6,000,000 total | CONFIRMED | "€6,000,000.00" | same |
| AI Factory | EUR 3,000,000 EU | CONFIRMED | "€3,000,000.00" | same |
| AI Factory | Coordinated by the Cyprus Institute | CONFIRMED | Coordinator: The Cyprus Institute | same |
| AI Factory | With CYENS, UCY, CUT and others | CONFIRMED | Participants include CYENS, University of Cyprus, Technologiko Panepistimio Kyprou | same |
| AI Factory | Focus health, sustainability, culture and language | CONFIRMED | Health; sustainability; culture and language | same |
| Gigafactory | Deputy Ministry (13 Nov 2025): joint initiative with Greece and Italy | CONFIRMED (press) | "Cyprus will participate in a joint intergovernmental initiative with Greece and Italy for the creation of AI Gigafactories." | cbn 121443 |
| Models | Pharos-CY plans LLMs and digital tools for Greek | CONFIRMED | same quote as the shared-with row | cyi.ac.cy |
| Models | Shared databases | CONFIRMED | "Shared databases and interoperable AI applications" | same |
| Models | "unified Greek-language AI ecosystem" | CONFIRMED | "unified Greek-language AI ecosystem" | same |
| Strategy | 2020 strategy approved by Council of Ministers, January 2020 | CONFIRMED | "In January 2020, the Council of Ministers has approved the National AI strategy of Cyprus." | AI Watch CY |
| Strategy | Draft "National AI Strategy 2032" | CONFIRMED (press) | Article refers to the "National AI Strategy 2032" | cyprus-mail 2026-07-28 |
| Strategy | Consultation 21 July to 31 August 2026 | NOT CONFIRMED | The cited article gives no dates; it only links to e-consultation. Other press found by search gives these dates. | same |
| Strategy | National AI Authority | CONFIRMED (press) | "A proposed National AI Authority would oversee implementation and compliance" | same |
| Strategy | 75% **public-sector** adoption target | NOT CONFIRMED | Article: "Among the headline targets is reaching 75 per cent AI adoption by 2032"; it does not say public sector | same |
| Public sector | gov.cy "Digital Assistant" | CONFIRMED | OECD.AI policy initiative page | oecd.ai digital-ai-assistant |
| Public sector | First generative-AI application in the public sector | CONFIRMED | "the Cypriot public sector's first Generative Artificial Intelligence (AI) application" | same |
| Public sector | Greek, English and Greeklish | CONFIRMED | "Citizens can submit their queries in both Greek and English"; also "Greeklish" | same |
| Public sector | Text and voice | NOT CONFIRMED | Neither cited page mentions voice. The launch article (cbn, 18 Dec 2024, not cited) says "either in writing or verbally". | oecd.ai; cbn 116040 |
| Public sector | Over 115,000 answers in six months | CONFIRMED (press) | "more than 115,000 citizen questions" | cbn 116040 |
| Language resources | CLARIN-CY through CUT | CONFIRMED | CLARIN-CY led by "Digital Heritage Research Lab (Cyprus University of Technology)" | clarin participating-consortia |
| Institutions | CyI (HPC, EuroCC, Pharos-CY coordinator) | CONFIRMED | hpcf about; CORDIS coordinator | cordis; hpcf |
| Institutions | CYENS, UCY, CUT | CONFIRMED | CORDIS participants | cordis |
| Institutions | Deputy Ministry of Research, Innovation and Digital Policy | UNCLEAR | Not named on either cited page (it is named in the cbn Gigafactory article) | cordis; hpcf |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Primary census release | FOUND | CYSTAT final results (09/08/2024): population 923,381; Cypriots 719,252 (77.9%). Parsed from the CYSTAT infographic PDF. | https://library.cystat.gov.cy/Infographics/Census%202021_Infographics_EL_090824.pdf | "Πληθυσμός … 923.381"; "719.252 … Κύπριοι … 77,9%" |
| EuroHPC system | Cyclone specifications | NOT FOUND | hpcf.cyi.ac.cy/cyclone.html returned 404; search found only an undated NI4OS training slide (not fetched) | — | — |
| Models | Pharos-CY LLM budget, base, licence | NOT FOUND | The CyI page says only "funded by the EuroHPC JU and by the Cyprus Government"; CORDIS gives the antenna total only | — | — |
| Models | Reuse of Meltemi or Krikri by Cypriot bodies | NOT FOUND | One search; no result | — | — |
| Gigafactory | Bid document | NOT FOUND | No official bid page found | — | — |
| Strategy | Adoption of 2032 strategy | NOT FOUND | Search results describe it as a draft; the Taskforce was created by Council of Ministers decision 97.538 of 22/1/2025 (press). No adoption found. | — | — |
| Public sector | Underlying platform | NOT FOUND (official); press lead | Press (cbn, 18 Dec 2024, photo credited PIO): Microsoft Azure OpenAI. No official page reached. | https://cbn.com.cy/article/2024/12/18/811902/digital-assistant-now-available-on-govcy (press) | "The Digital Assistant is based on Microsoft Azure OpenAI technologies" |
| Language resources | National Cypriot Greek corpus | NOT FOUND | Search found a UCY lexical database paper and a Bamberg spoken corpus; no national corpus | — | — |
| Institutions | CYENS pages | NOT FOUND | Not retried | — | — |
| Power | Official source | NOT FOUND | Search found a university feasibility study and press on EuroAsia; no regulator or ministry page | — | — |

#### C. Prose flags
1. Strategy point 4 says "The assistant's platform could not be confirmed". Press reports Azure OpenAI (see B). The prose could cite that as press.
2. Point 2, "the Cypriot public-service corpus the Digital Assistant has been collecting since December 2024": the launch date is supported by press. That the assistant collects a reusable corpus is not stated on any fetched page.

### EL
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Greek official EU language since 1981 | CONFIRMED | "1981: Greek" | europa.eu languages |
| Languages | Census reference date 22 October 2021 | CONFIRMED | "reference date of the data the 22nd of October 2021" | statistics.gr 2021-census |
| Languages | Census collects no language data | CONFIRMED | Variables listed; language not among them | same |
| Languages | ELSTAT pages do not show national total | CONFIRMED | No figures on the page | same |
| Shared with | Greek official in Cyprus (Art. 3(1)) | CONFIRMED | "The official languages of the Republic are Greek and Turkish." | constituteproject |
| Shared with | Pharos-CY joint LLMs for Greek | CONFIRMED | "Large Language Models (LLMs) and digital tools for the Greek language" | cyi.ac.cy |
| EuroHPC system | Owned and operated by GRNET | CONFIRMED | GRNET "manages and runs the system" (contract page); "implemented by … GRNET S.A." | eurohpc 2025-03-28; grnet.gr/daedalus |
| EuroHPC system | Lavrion | CONFIRMED | "former Power Station building at the Lavrion Technological Cultural Park" | eurohpc 2025-03-28 |
| EuroHPC system | HPE contract 28 March 2025 | CONFIRMED | Dated 28 March 2025; HPE "the selected vendor" | same |
| EuroHPC system | Over 89 PFlops | CONFIRMED | "over 89 petaflops" | same |
| EuroHPC system | EUR 36 M | CONFIRMED | "total acquisition cost of EUR 36 million" | same |
| EuroHPC system | EuroHPC 35%, Greece 2.0 RRF 65% | CONFIRMED | 35% JU; 65% National Recovery and Resilience Plan "Greece 2.0" | same |
| EuroHPC system | 31st on June 2026 TOP500 | CONFIRMED | "enters the TOP500 at 31st position" | eurohpc 2026-06-23 |
| EuroHPC system | 85.69 PFlops | CONFIRMED | "With a performance of 85,69 petaflops" | same |
| EuroHPC system | NVIDIA GH200 | CONFIRMED | "HPE's NVIDIA GH200 direct liquid cooled architecture" | same |
| EuroHPC system | "expected to become fully available to European users shortly" | CONFIRMED | verbatim | same |
| EuroHPC system | GRNET says operational during 2026 | CONFIRMED | "DAEDALUS is expected to become operational during 2026" | grnet.gr/daedalus |
| AI Factory | Pharos one of first seven, 10 Dec 2024 | CONFIRMED | Press release dated 10 December 2024 | eurohpc 2024-12-10 |
| AI Factory | Built on DAEDALUS | CONFIRMED | "aims to exploit DAEDALUS, the EuroHPC supercomputer currently under deployment in Greece" | same |
| AI Factory | Run by GRNET under the Ministry of Digital Governance | CONFIRMED | "will be managed and operated by … (GRNET)"; contract page: under the Ministry of Digital Governance | grnet pr; eurohpc 2025-03-28 |
| AI Factory | EUR 30 M | CONFIRMED | "The project has a total budget of €30 million" | grnet pr |
| AI Factory | 50% EuroHPC, 50% national | CONFIRMED | "funded 50% by the EuroHPC Joint Undertaking and 50% by National Resources" | grnet pr |
| AI Factory | 36 months from March 2025 | CONFIRMED | "scheduled to commence in March 2025, with a total duration of 36 months" | grnet pr |
| AI Factory | ILSP: 1 April 2025 to 31 March 2028 | CONFIRMED | "Start Date: 01/04/2025"; "End Date: 31/03/2028" | ilsp.gr pharos |
| AI Factory | Culture and Language one of three focus sectors | CONFIRMED | "Health, Culture and Language and Sustainability" | grnet pr |
| AI Factory | Antennas in Cyprus, Malta, North Macedonia, Serbia | CONFIRMED | "Antennas: Cyprus, Malta, North Macedonia and Serbia" | eurohpc ai-factories |
| AI Factory | Law 5263/2025 created "PHAROS AI FACTORY" | CONFIRMED | distinctive title "ΦΑΡΟΣ AI FACTORY"; international "PHAROS AI FACTORY" | taxheaven 5263/2025 art. 8 |
| AI Factory | State 30% | CONFIRMED | "σε ποσοστό τριάντα τοις εκατό (30%)" | same |
| AI Factory | HCAP 70% | CONFIRMED | Ε.Ε.Σ.Υ.Π. Α.Ε. (the Greek name of HCAP) "σε ποσοστό εβδομήντα τοις εκατό (70%)" | same |
| AI Factory | Greek language and culture in its purpose | CONFIRMED | "με σκοπό τη δημιουργία γλωσσικών μοντέλων για την ελληνική γλώσσα και τον ελληνικό πολιτισμό" | same |
| Gigafactory | 76 responses | CONFIRMED | "76 expressions of interest proposing to set up AI Gigafactories in 16 Member States across 60 different sites" | digital-strategy 76 respondents |
| Gigafactory | 16 member states | CONFIRMED | same | same |
| Gigafactory | 60 sites | CONFIRMED | same | same |
| Gigafactory | None named | CONFIRMED | "will not disclose further information about the identity of the Respondents" | same |
| Gigafactory | Cypriot statement on joint Greece, Italy, Cyprus initiative after Nov 2025 summit | CONFIRMED (press) | follows the 3rd Greece–Cyprus Intergovernmental Summit, 13 Nov 2025 | cbn 121443 |
| Models | Meltemi-7B, ILSP | CONFIRMED | HF ilsp org card | HF Meltemi-7B-v1 |
| Models | Base Mistral-7B | CONFIRMED | "built on top of Mistral-7B" | same |
| Models | About 40 B tokens | CONFIRMED | "approximately 40 billion tokens" | same |
| Models | Apache-2.0 | CONFIRMED | "apache-2.0" | same |
| Models | Amazon cloud via GRNET OCRE | CONFIRMED | "The ILSP team utilized Amazon's cloud computing services" via GRNET under OCRE | same |
| Models | Released 26 March 2024 | NOT CONFIRMED | The HF card gives no date. ILSP's own announcement, "Meltemi, the first open-source Large Language Model for Greek", is dated 28/03/2024 (https://www.ilsp.gr/en/catalogos-news-en/page/2). | HF Meltemi |
| Models | Krikri base Llama-3.1-8B | CONFIRMED | "is built on top of Llama-3.1-8B" | HF Llama-Krikri-8B-Instruct |
| Models | About 110 B tokens upsampled | CONFIRMED | "resulting in a size of 110 billion tokens" | same |
| Models | 56.7 B Greek | CONFIRMED | "56.7 billion monolingual Greek tokens" | same |
| Models | Llama 3.1 licence | CONFIRMED | "llama3.1" | same |
| Models | Same compute route | CONFIRMED | Amazon via GRNET "OCRE Cloud framework" | same |
| Models | Paper 19 May 2025 | CONFIRMED | "Published May 19, 2025" (arXiv 2505.13772) | same |
| Models | Pharos Culture and Language commits to open AI models for Greek | CONFIRMED | EKT: project aims to "develop open AI models" for Greek language and culture | ekt.gr/en/news/30578 |
| Strategy | "A Blueprint for Greece's AI Transformation", 25 Nov 2024 | CONFIRMED | "25 November, 2024" | foresight.gov.gr |
| Strategy | By the High-Level Advisory Committee on AI | CONFIRMED | High-Level Advisory Committee on Artificial Intelligence | same |
| Strategy | Page calls it a "policy proposal" | CONFIRMED | "This policy proposal aims not only to foster the development of Greece's economy and society" | same |
| Strategy | GRNET calls Pharos a flagship under it | CONFIRMED | "This initiative is a flagship project under the Blueprint for Greece's AI Transformation" | grnet pr |
| Strategy | AI Act draft law consultation, June 2026 | CONFIRMED (press) | Ministry "placed the bill online for consultation on Sunday, June 21, 2026" | protothema |
| Public sector | mAIgov, Ministry of Digital Governance | CONFIRMED | "Launched in December 2023 by the Ministry of Digital Governance" | oecd.ai maigov |
| Public sector | Live since December 2023 | CONFIRMED | same | same |
| Public sector | 25 languages | CONFIRMED | "mAigov supports interactions in 25 languages" | same |
| Public sector | Over 1,600 gov.gr services | CONFIRMED | "over 1,600 services available on gov.gr" | same |
| Public sector | 3,270 procedures | CONFIRMED | "more than 3,270 administrative procedures" | same |
| Public sector | Over 1.6 M interactions | CONFIRMED | over 1.6 million interactions since launch | same |
| Language resources | CLARIN:EL, certified B-centre at ILSP / Athena RC | CONFIRMED | "CLARIN:EL National Infrastructure for Language Resources & Technologies in Greece"; B-centre; certified | centres.clarin.eu/centre/75 |
| Language resources | ILSP project on Greek dialects and varieties | CONFIRMED | "AI for Greek dialects and language varieties spoken in Greece" | ilsp.gr/en |
| Institutions | GRNET (DAEDALUS, Pharos coordinator) | CONFIRMED | see above | grnet pr |
| Institutions | ILSP / Athena RC (Meltemi, Krikri, CLARIN:EL) | CONFIRMED | ilsp.gr lists CLARIN:EL; Meltemi and Krikri are confirmed on the HF cards, not on ilsp.gr/en | ilsp.gr; HF |
| Institutions | NCSR Demokritos, NTUA, Growthfund core consortium | CONFIRMED | core members NCSR Demokritos, NTUA, Athena RC, GrowthFund | grnet pr |
| Institutions | EKT (Greek-language AI services) | NOT CONFIRMED | The cited GRNET page lists EKT as an affiliated body only. The role is on ekt.gr/en/news/30578 (not cited in this row): EKT "will play a central role in the development and implementation of a comprehensive suite" | grnet pr |
| Institutions | Pharos AI Factory company | CONFIRMED | see Law 5263/2025 rows | taxheaven |
| Power | Renewable energy | CONFIRMED | "renewable energy sources" | eurohpc 2025-03-28 |
| Power | Liquid cooling | NOT CONFIRMED | The cited page says only "advanced cooling systems". The TOP500 page (2026-06-23) says "direct liquid cooled". | eurohpc 2025-03-28 |
| Power | Green500 23rd | NOT CONFIRMED | Not on the cited page. On the TOP500 page: "DAEDALUS and Arrhenius ranked 23rd and 24th in the Green500 list" | eurohpc 2025-03-28 |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speaker count | NOT FOUND | The census has no language question. Search gave only press population totals, which disagree (10,432,481 preliminary vs a Wikipedia figure); no ELSTAT page was reached. | — | — |
| Shared with | Diaspora figures | NOT FOUND (official) | Press attributes "over 5 million people of Greek origin … in 140 countries" to the General Secretariat for Greeks Abroad; no official page was fetched | — | — |
| Models | Meltemi/Krikri funder and amounts | NOT FOUND | No source names a funder. ILSP's announcement is dated 28/03/2024. | — | — |
| Models | Pharos named model, base, budget | NOT FOUND | EKT and ILSP pages name no model or budget line | — | — |
| Gigafactory | Official Greek bid | NOT FOUND | Search found a press report of a PPC proposal (Western Macedonia), not an official bid page | — | — |
| Strategy | Formal adoption decision | NOT FOUND | Foresight page presents it as a proposal | — | — |
| Public sector | mAIgov vendor and model | NOT FOUND (official); press lead | The EC digital-skills page returned 403. Press reports Microsoft Azure OpenAI, with OTE as contractor. | — | — |
| Public sector | OpenAI and Mistral agreements | NOT FOUND (official) | Press only: OpenAI MoU September 2025 (education); Mistral agreement November (public administration) | greekcitytimes (press) | "In September 2025, Greece signs a memorandum of understanding with OpenAI for applications in education." |
| Language resources | Hellenic National Corpus size | NOT FOUND (total) | ILSP gives only the EGC general corpus, which is part of the HNC: more than 34 M words. Search shows 47 M words in non-official sources. | https://www.ilsp.gr/?p=3555 | "contains more than 34,000,000 words of written texts" |
| Power | Grid constraint statement | NOT FOUND | No search hit | — | — |

#### C. Prose flags
1. None beyond the snapshot. The prose's "DAEDALUS was not yet fully available in June 2026" matches the 23 June 2026 EuroHPC page.

### IE
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Irish first, English second official (Art. 8) | UNCLEAR | irishstatutebook.ie returned 403 twice | irishstatutebook.ie |
| Languages | Irish official EU language since 2007 | CONFIRMED | "2007: Bulgarian, Irish, Romanian" | europa.eu languages |
| Languages | 1,873,997 aged 3+ could speak Irish | CONFIRMED | "stood at 1,873,997" | cso.ie profile 8 |
| Languages | 553,965 only within education | CONFIRMED | "a further 553,965 indicated they only spoke Irish within the education system" | same |
| Languages | 65,156 in the Gaeltacht | CONFIRMED | "65,156 indicated they could speak Irish" | same |
| Shared with | English with Malta | UNCLEAR | The EU page lists English as an official language but does not say which states use it | europa.eu languages |
| Shared with | Irish with Northern Ireland | UNCLEAR | ADAPT page mentions only "data from the Northern Ireland Placenames Project" | adaptcentre DCU article |
| EuroHPC system | CASPIr hosting agreement with University of Galway | CONFIRMED | agreement between the EuroHPC JU and "the University of Galway" | eurohpc 2025-10-13 Ireland |
| EuroHPC system | Signed 13 October 2025 | CONFIRMED | ICHEC: signed on 13 October 2025 | ichec.ie/node/1115 |
| EuroHPC system | Operated by ICHEC | CONFIRMED | "This new supercomputer will be operated by the Irish Centre for High-End Computing" | eurohpc 2025-10-13 |
| EuroHPC system | Mid-range | CONFIRMED | "mid-range supercomputer" | same |
| EuroHPC system | Over 15 PFlops | CONFIRMED | "capable of performing over 15 petaflops" | same |
| EuroHPC system | AI and ML workloads | CONFIRMED | "It will support cutting-edge AI and machine learning workloads." | same |
| EuroHPC system | Tender 27 March 2026 | CONFIRMED | published 27 March 2026 | eurohpc CASPIr ITT |
| EuroHPC system | Up to EUR 25 M | CONFIRMED | "The total acquisition budget of the system is up to EUR 25 million." | same |
| EuroHPC system | EuroHPC 35%, Ireland 65% | CONFIRMED | 35% JU, 65% Ireland | same |
| AI Factory | "AIF IRL-Antenna" | CONFIRMED | "AI Factory Antenna in Ireland (AIF IRL-Antenna)" | ichec.ie/node/1114 |
| AI Factory | Selected 13 October 2025 | CONFIRMED | successful bid announced 13 October 2025 | same |
| AI Factory | Led by ICHEC with CeADAR | CONFIRMED | consortium led by ICHEC, CeADAR core partner | same |
| AI Factory | EUR 10 M co-funded evenly by EU and DFHERIS | CONFIRMED | €10m, "evenly co-funded by the EU and DFHERIS" | same |
| AI Factory | Linked to AI2F with Alice Recoque access | CONFIRMED | access to the "exascale-class supercomputer (Alice Recoque)" | same |
| AI Factory | Linked to the Luxembourg AI Factory | CONFIRMED | second link with the Luxembourg AI Factory (Meluxina-AI) | same |
| AI Factory | AI sandbox and secure data environment for start-ups, SMEs, public sector | CONFIRMED | "AI Sandbox and Secure Data Environment" | same |
| AI Factory | Not a full AI Factory host | CONFIRMED | Ireland appears only as "Antenna: Ireland" under Luxembourg and France | eurohpc ai-factories |
| Gigafactory | Press lists Ireland among states in the joint procurement | UNCLEAR | parapolitika.gr article returned 404 twice | parapolitika |
| Models | UCCIX, an open Irish-language LLM | CONFIRMED | "an open-source Irish-based LLM" | arXiv 2405.13010 |
| Models | On Llama 2-13B | CONFIRMED | "based on Llama 2-13B" | same |
| Models | From University College Cork | UNCLEAR | Affiliations not shown on the abstract page | same |
| Models | May 2024 | CONFIRMED | v1 submitted 13 May 2024 | same |
| Models | eSTÓR EUR 900,000 over three years | CONFIRMED | "€900K over the next three years" | adaptcentre DCU article |
| Models | From the Gaeltacht department | CONFIRMED | announced by the "Minister for Rural and Community Development and the Gaeltacht" | same |
| Models | Announced 21 November 2025 | CONFIRMED | article dated 21 November 2025 | same |
| Models | Quoted "develop new neural language models suited to Irish" | NOT CONFIRMED (wording) | The page reads "develop new neural Language Models tailored for Irish". The quote as printed is not verbatim; the gov.ie source it may come from returned 403. | adaptcentre DCU article |
| Models | And evaluation sets | CONFIRMED | "develop stronger evaluation methods and datasets" | same |
| Models | Gaois up to EUR 4,013,886, 2026 to 2029 | UNCLEAR | gov.ie returned 403 twice. ADAPT says "€4 million over the next four years". | gov.ie Calleary; adaptcentre |
| Models | "a structured supply of information … to AI models" | UNCLEAR | gov.ie returned 403 twice; not on the ADAPT page | gov.ie Calleary |
| Strategy | "AI – Here for Good" (2021) | CONFIRMED | first strategy "launched in July 2021" | enterprise.gov.ie refresh |
| Strategy | Refreshed 6 November 2024 | CONFIRMED | page dated 6th November 2024 | same |
| Strategy | AI Act implementation | CONFIRMED | refresh covers AI Act implementation | same |
| Strategy | Regulatory sandbox | CONFIRMED | commits to an AI regulatory sandbox | same |
| Strategy | "safe space" for civil servants | CONFIRMED | "creating a safe space where civil and public servants are encouraged to experiment with AI tools" | same |
| Strategy | Access to advanced AI computing | CONFIRMED | "promoting increased use of and access to advanced AI computing services" | same |
| Strategy | No national-model action | UNCLEAR | The summary page names none; the full PDF was not read | same |
| Strategy | Further update during 2025 announced | UNCLEAR | Not on enterprise.gov.ie; gov.ie returned 403. Search shows an "Updated National Digital Strategy 2025" was announced. | gov.ie DETE; enterprise.gov.ie |
| Public sector | Guidelines of 8 May 2025 | UNCLEAR | gov.ie returned 403 twice | gov.ie Chambers |
| Public sector | Revenue "using Large Language Models to route taxpayer queries" | UNCLEAR | gov.ie returned 403 twice; ICHEC page does not mention it | gov.ie; ichec 1114 |
| Language resources | Ireland not a CLARIN ERIC member | CONFIRMED | Ireland not listed | clarin participating-consortia |
| Institutions | ICHEC (Galway; CASPIr operator; antenna lead) | CONFIRMED | see rows above | ichec 1114 |
| Institutions | CeADAR applied AI centre, antenna partner | CONFIRMED | "CeADAR is Ireland's national centre for Applied AI"; core partner (ICHEC) | ceadar.ie; ichec 1114 |
| Institutions | ADAPT (TCD and DCU) | CONFIRMED | "Coordinated by Trinity College Dublin and co-hosted by Dublin City University" | adaptcentre about |
| Institutions | Gaois (DCU) | UNCLEAR | Not on the cited pages for this row | — |
| Institutions | UCC | UNCLEAR | No affiliation shown on any cited page | — |
| Power | Data centres 5% (2015) to 21% (2023) | CONFIRMED | "rose from 5% of Ireland's total demand in 2015 to 21% in 2023" | consult.cru.ie |
| Power | 85% of demand growth | CONFIRMED | "accounting for 85% of the overall electricity demand growth" | same |
| Power | Decision CRU2025236 of 12 Dec 2025 | CONFIRMED | "has today, 12 December 2025, published a decision paper on the Large Energy Users connection policy" | cru.ie/publications/28573 |
| Power | New data centres must provide new renewable and dispatchable generation | CONFIRMED | "New data centres connecting under this policy will be required to provide new renewable and dispatchable" generation | same |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Shared with | Diaspora figures | NOT FOUND (official) | dfa.ie strategy page redirects to ireland.ie home. Search attributes "around 70 million" to the government's Diaspora Strategy 2020-2025. | — | — |
| EuroHPC system | CASPIr award | NOT FOUND (no award) | The tender page still describes competitive dialogue then contract; search found no award | https://www.eurohpc-ju.europa.eu/invitation-tender-procure-caspir-supercomputer-2026-03-27_en | — |
| AI Factory | gov.ie Lawless press release [unverified] | FOUND (alternative source) | gov.ie returned 403. The same facts (EUR 10 M, even EU/DFHERIS split, ICHEC with CeADAR) are on ICHEC's page, already cited. | https://www.ichec.ie/node/1114 | "evenly co-funded by the EU and DFHERIS" |
| Gigafactory | Irish bid or position | NOT FOUND | Search found only the antenna and CASPIr | — | — |
| Models | UCCIX funder and weights | FOUND (weights); NOT FOUND (funder) | Hugging Face org ReliableAI hosts UCCIX model repositories (13B, 70B-class, Llama-3.1-8B, Mistral-24B variants); compute credited to CloudCIX; no funder named | https://huggingface.co/ReliableAI | "releasing our Irish-based Large Language Model, UCCIX, and its accompanied curated dataset" |
| Models | eSTÓR named model | NOT FOUND | No model named on the ADAPT pages | — | — |
| Strategy | 2025 update outcome | NOT FOUND | Search: announced, outcome not found | — | — |
| Public sector | Model procurement | NOT FOUND | Search found a press report of a Revenue staff LLM ("Revenue helper"), no tender or vendor | — | — |
| Language resources | gov.ie Calleary link [unverified] | FOUND (alternative source) | eSTÓR data feeds the Commission's eTranslation (ADAPT, rebrand article); Corpas is one of the five Gaois projects (ADAPT, 21 Nov 2025) | https://www.adaptcentre.ie/news-and-events/irish-language-technology-resource-marks-growth-with-rebrand/ ; https://www.adaptcentre.ie/news-and-events/innovative-irish-language-and-ai-initiatives-launched-in-dcu | "can be shared nationally and relayed to the European Commission to improve their eTranslation system for Irish" |

#### C. Prose flags
1. "Ireland hosts more hyperscale capacity than most states" has no source in the snapshot. It is also comparative language close to a ranking.
2. "Irish-language continued pretraining is weeks of accelerator time": no source.

### RO
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Shared with | Moldova's antenna FAIMA attached to Poland's PIAST | CONFIRMED | "It will be linking the country's innovation ecosystem to PIAST AI Factory in Poland." | eurohpc antennas |
| EuroHPC system | None on the official list | CONFIRMED | No Romanian system among the 12 listed | eurohpc our-supercomputers |
| AI Factory | RO AI Factory | CONFIRMED | "RO AI Factory" | eurohpc 2025-10-10 |
| AI Factory | Selected 10 October 2025 | CONFIRMED | Press release dated 10 October 2025 | same |
| AI Factory | Hosted by ICI Bucharest | CONFIRMED | "hosted and co-coordinated in Bucharest by the National Institute for Research & Development in Informatics" | eurohpc romania |
| AI Factory | With Politehnica Bucharest | CONFIRMED | UPB co-coordinator | eurohpc 2025-10-10 |
| AI Factory | Partners include the Romanian Academy's AI institute | CONFIRMED | lists "the Research Institute for Artificial Intelligence (ICIA)", linking to racai.ro | eurohpc romania |
| AI Factory | AI-optimised supercomputer to be acquired | CONFIRMED | "The Factory aims to acquire and deploy an AI-optimised supercomputer" | same |
| AI Factory | Implementation from 1 September 2026 | CONFIRMED (press) | "RO AI Factory project begins on September 1" | agerpres 2026-09-01 |
| AI Factory | Grant 101314645 | CONFIRMED (press) | "Grant Agreement No. 101314645" (also on CORDIS) | same |
| AI Factory | Operational by end-2027 | CONFIRMED (press) | "expected to become operational by the end of 2027" | same |
| AI Factory | ICI refers users to the Spanish factory meanwhile | CONFIRMED | "Prin BSC AI Factory, aceștia pot avea acces la infrastructura europeană"; "fără să aștepta operaționalizarea RO AI Factory" | ici.ro search |
| AI Factory | Romania a partner of the BSC factory | CONFIRMED (weak) | ai-factories page lists "Portugal, Romania and Türkiye" under Spain without stating the relationship | eurohpc ai-factories |
| Gigafactory | "Black Sea AI Gigafactory" EoI | CONFIRMED | "identificarea și preselectarea unui Lider de Consorțiu" | adr.gov.ro |
| Gigafactory | 15 April 2026 | CONFIRMED | dated 15 April 2026 | same |
| Gigafactory | Ministries of Energy and Finance | CONFIRMED | issued by the Ministry of Energy and the Ministry of Finance | same |
| Gigafactory | With ADR | CONFIRMED | "cu sprijinul tehnic al Autorității pentru Digitalizarea României (ADR)" | same |
| Gigafactory | To pre-select a consortium leader | CONFIRMED | same as EoI quote | same |
| Gigafactory | About 20,000 GPUs first phase | CONFIRMED | "o fază inițială de implementare de aproximativ 20.000 de GPU-uri" | same |
| Gigafactory | Deadline 14 June 2026 | CONFIRMED | "Termen-limită de depunere: 14.06.2026, ora 17:00" | same |
| Gigafactory | No EuroHPC selection yet | CONFIRMED | Call deadline is 12 November 2026, with selection in early 2027 | eurohpc gigafactories call |
| Models | OpenLLM-Ro (ILDS, Politehnica, University of Bucharest) | CONFIRMED | author affiliations include ILDS, POLITEHNICA Bucharest, University of Bucharest | arXiv 2405.07703v4 |
| Models | Privately funded by BRD Groupe Société Générale | CONFIRMED | "with funding from BRD Groupe Societe Generale" | same |
| Models | University compute | CONFIRMED | "computing power for training the models (POLITEHNICA Bucharest)" | same |
| Models | RoLlama2 | CONFIRMED | "the first foundational Romanian LLM (i.e., RoLlama) based on the open-source Llama 2 model" | same |
| Models | RoLlama2 and RoMistral continued pretraining on about 40 billion Romanian tokens | NOT CONFIRMED | 40B is the size of the Romanian part of CulturaX ("around 40M documents and 40B tokens"). The foundational models were trained on 5%, 10% and 20% of it. In v4, RoMistral-Instruct has "no pretraining on Romanian". | same |
| Models | RoLlama3.1-8B-Instruct under CC-BY-NC-4.0 | CONFIRMED | "License: cc-by-nc-4.0" | HF RoLlama3.1-8b-Instruct |
| Models | (2025) | CONFIRMED | points to RoLlama3.1-8b-Instruct-2025-04-23 | same |
| Models | No public funding stated | CONFIRMED | No funding stated on HF; arXiv credits BRD only | HF; arXiv |
| Strategy | National AI Strategy 2024-2027 approved by the Government in July 2024 | CONFIRMED (press) | "Guvernul a aprobat Strategia Națională în domeniul Inteligenței Artificiale (SN-IA) 2024 - 2027" (issue of 16-31 July 2024) | agir.ro |
| Public sector | RRF funds a secure government cloud | CONFIRMED | "while building a secure government cloud infrastructure" | reforms-investments RO |
| Public sector | And e-identity | CONFIRMED | "supporting the e-Identity deployment" | same |
| Public sector | Not HPC or AI compute | CONFIRMED | No HPC or AI compute investment mentioned | same |
| Language resources | CoRoLa reference corpus | CONFIRMED | "o imagine obiectivă a limbii române actuale scrise și vorbite" | corola.racai.ro |
| Language resources | Over one billion words | CONFIRMED | "1+ Mld. de cuvinte" | same |
| Language resources | Built by RACAI and the Iași institute | CONFIRMED | ICIA "Mihai Drăgănescu" and the Institutul de Informatică Teoretică, Iași | same |
| Language resources | Open for public use | CONFIRMED | "deschis utilizării publice" | same |
| Language resources | RACAI hosts a CLARIN knowledge centre | CONFIRMED | "RACAI4RO CLARIN K-Centre" | racai.ro/en |
| Language resources | Romania absent from the CLARIN ERIC member list | CONFIRMED | Romania not listed | clarin.eu/node/3754 |
| Institutions | ICI Bucharest (factory host) | CONFIRMED | see AI Factory | eurohpc romania |
| Institutions | Politehnica (co-coordinator, OpenLLM-Ro compute) | CONFIRMED | co-host on eurohpc page; compute per arXiv | eurohpc romania |
| Institutions | RACAI, the Romanian Academy's AI institute (CoRoLa) | CONFIRMED | "Research Institute for Artificial Intelligence 'Mihai Drăgănescu', Romanian Academy" | racai.ro/en |
| Institutions | ILDS (OpenLLM-Ro) | UNCLEAR | Not on the cited pages for this row (it is on arXiv) | eurohpc romania; racai |
| Institutions | ADR (Gigafactory technical support) | UNCLEAR | Not on the cited pages for this row (it is on adr.gov.ro) | same |
| Power | ADR notice states no site or power figure | CONFIRMED | The page gives no site location or power capacity | adr.gov.ro |

The language row is wholly marked [unverified], so it is treated under B. The cited eurohpc romania page is reachable, but it says nothing about the official language or the population.

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Census mother-tongue figures | FOUND | Census 2021 (RPL 2021), resident population 19,053,815; Romanian mother tongue 15,153,198; Hungarian 1,038,806; Romani 199,050; information unavailable 2,502,378. Table 2.3.1, parsed from the xlsx. The INS census host answered on the access date. | https://www.recensamantromania.ro/wp-content/uploads/2023/06/Tabel-2.03.1-si-Tabel-2.03.2.xlsx (index: https://www.recensamantromania.ro/rezultate-rpl-2021/rezultate-definitive-caracteristici-etno-culturale-demografice/) | "2.3.1 POPULATIA REZIDENTA DUPA LIMBA MATERNA … ROMÂNIA 19053815 15153198 1038806 199050" |
| Languages | Constitution Art. 13 | NOT FOUND (official) | fra.europa.eu returned 403; search found only municipal PDF copies | — | — |
| Shared with | Moldova from an official page | NOT FOUND (official) | ConstitutionNet (International IDEA) reports Moldovan Law nr. 52 of 16 March 2023, which replaces "Moldovan language" with "Romanian language". No Moldovan government page was fetched. | — | — |
| AI Factory | Budget | FOUND | CORDIS: "Romanian EuroHPC AI Factory at ICI Bucharest", 1 Sep 2026 to 31 Aug 2029, total cost EUR 8,000,000, EU contribution EUR 4,000,000. Press figures of about EUR 50 M likely include the supercomputer, which is not in this grant. | https://cordis.europa.eu/project/id/101314645 | Total cost "€8,000,000.00"; EU contribution "€4,000,000.00" |
| Gigafactory | Sites, power, investment | NOT FOUND (official) | Press: Cernavodă (phase I) and Doicești (phase II), up to 1,500 MW, EUR 4-5 bn, and a government memorandum (27 Nov). No gov.ro text was reached. | — | — |
| Strategy | Decision number and gazette | NOT FOUND (fetch failed) | A search snippet from legislatie.just.ro (record 286251) names HG nr. 832/2024 of 11 July 2024, M.Of. nr. 730 of 25 July 2024. The page hung up twice and the snippet could not be confirmed. | https://legislatie.just.ro/Public/DetaliiDocumentAfis/286251 (unreachable) | — |
| Public sector | LLM use | NOT FOUND | Search found consultancy studies only | — | — |
| Power | Nuclear-adjacent site, MW | NOT FOUND (official) | as Gigafactory row | — | — |

#### C. Prose flags
1. Recommended strategy point 1: "OpenLLM-Ro has shown continued pretraining on 40 billion Romanian tokens" repeats the NOT CONFIRMED snapshot claim. The report trains on fractions of a 40B-token corpus.
2. "a Gigafactory bid": the official page shows an expression of interest to pre-select a consortium leader, not a submitted EuroHPC bid. A 2025 press item calls the June 2025 letter of intent a bid. The snapshot words this carefully; the prose is looser.

### Summary
| State | Claims checked | Confirmed | Not confirmed | Unclear | Unverified cells | Found | Not found |
|---|---|---|---|---|---|---|---|
| BG | 44 | 43 | 0 | 1 | 10 | 3 | 7 |
| CY | 42 | 35 | 5 | 2 | 10 | 1 | 9 |
| EL | 69 | 65 | 4 | 0 | 10 | 0 | 10 |
| IE | 56 | 42 | 1 | 13 | 9 | 3 | 6 |
| RO | 45 | 42 | 1 | 2 | 8 | 2 | 6 |

Most IE UNCLEAR verdicts come from gov.ie and irishstatutebook.ie returning 403.

"Found" counts only official or institutional pages. Press-only leads are listed in the tables as NOT FOUND (official): CY Digital Assistant on Azure OpenAI; EL mAIgov on Azure OpenAI; RO Gigafactory sites and MW.

## Review: Visegrád, Slovenia and Croatia (HR, CZ, HU, PL, SK, SI), 2026-10-10

Tools: WebSearch available: yes. About 115 URLs fetched (WebFetch, plus curl for the census spreadsheets and three PDFs that WebFetch could not decode; those were parsed locally with pdftotext and a stdlib unzip script). 2 failed: nytud.hu research-group page (HTTP 403, retried once, still 403) and businessinfo.cz gigafactory article (HTTP 403, Task B only). Every URL cited in the six snapshots was reachable.

Verdict key: C = CONFIRMED, NC = NOT CONFIRMED, U = UNCLEAR. Quotes are from the fetched page, in its language.

### HR

#### A. Verification
| Row | Claim | Verdict | Evidence (quote ≤25 words, or what the page says) | URL |
|---|---|---|---|---|
| Languages | Croatian and Latin script official (Art. 12) | C | "The Croatian language and the Latin script shall be in official use in the Republic of Croatia." | usud.hr consolidated Constitution PDF |
| Languages | Other languages and scripts admitted locally by law | C | "In individual local units, another language and Cyrillic or some other script may be introduced in official use ... under conditions specified by law." | same |
| Languages | Croatian mother tongue 3,687,735 of 3,871,833 | C | Tab. 3 (materinski jezik): "Republika Hrvatska ... hrvatski \| Croatian \| 3687735"; total 3871833 | podaci.dzs.hr popis_2021-stanovnistvo_rh.xlsx |
| Languages | Serbian 45,004 | C | "srpski \| Serbian \| 45004" | same |
| Languages | Bosnian 17,531 | C | "bosanski \| Bosnian \| 17531" | same |
| Languages | Albanian 13,503 | C | "albanski \| Albanian \| 13503" | same |
| Languages | Italian 12,890 | C | "talijanski \| Italian \| 12890" | same |
| Languages | Hungarian 7,218 | C | "mađarski \| Hungarian \| 7218" | same |
| Shared | Mutually intelligible with Bosnian, Serbian, Montenegrin | U | Not stated on the cited GaMS model card (it lists languages only). | huggingface.co/cjvt/GaMS3-12B-Instruct |
| Shared | GaMS lists Croatian, Bosnian, Serbian as secondary | C | "Slovene, English (primary), Croatian, Bosnian and Serbian (secondary)" | same |
| EuroHPC system | None in Croatia | C | The list of twelve EuroHPC systems contains none in Croatia. | eurohpc-ju.europa.eu our-supercomputers |
| EuroHPC system | Supek at SRCE, 1.25 PFlops | C | "providing a power of 1.25 PFLOPS" | srce.unizg.hr/en/advanced-computing |
| EuroHPC system | 81 GPUs | C | "8384 processor cores, 81 GPUs, and 32 TB of working memory" (the page's GPU table sums to 80) | same; also HR-ZOO press PDF "81 grafičkim procesorom" |
| EuroHPC system | In operation since 28 March 2023 under HR-ZOO | C | "(Zagreb, 28 ožujka 2023.) ... u rad puštena nova generacija nacionalne e-infrastrukture HR-ZOO i predstavljeno je najjače superračunalo ... „Supek“" | SRCE HR-ZOO press release PDF |
| EuroHPC system | EUR 26.12 million | C | "Ukupna vrijednost projekta HR-ZOO iznosi 26.120.172,29 eura" | same |
| EuroHPC system | 85% ERDF | C | "sufinancirala Europska unija iz Europskog fonda za regionalni razvoj u iznosu od 85 %" | same |
| AI Factory | No factory, no antenna | C | Croatia appears neither among factories nor antennas. | eurohpc-ju.europa.eu/ai-factories_en |
| AI Factory | SRCE December 2025 report: Croatia "missed a chance to establish a national AI factory in earlier calls" | NC (wording) | Substance and date (16 Dec 2025) confirmed, but the page reads: "Although Croatia missed the opportunity to establish a national AI factory in earlier calls". The note's quoted words differ. | srce.unizg.hr news 1438 |
| AI Factory | (press) Co-financing guarantee not secured by 30 June 2025 | C | Srce: "we were unable to obtain the necessary guarantees for the national part of the funding" before the 30 June 2025 deadline | en.lider.media 2026/03/22 |
| AI Factory | (press) "AI Factory Croatia" planned in national AI plan | C | Plan to prioritise "The establishment of an AI factory in the Republic of Croatia (AI Factory Croatia)" | same |
| Model efforts | HR-XR-XTEND at Zagreb FFZG | C | Contact: "University of Zagreb, Faculty of Humanities and Social Sciences, Institute of Linguistics" | hr-xr-xtend.ffzg.unizg.hr |
| Model efforts | Horizon Europe UTTER sub-project | C | Part of "Unified transcription and translation for extended reality (UTTER)", Horizon Europe (also credits UKRI) | same |
| Model efforts | At least 6 billion tokens | C | "collect at least 6 billion tokens of Croatian text" | same |
| Model efforts | Monolingual Croatian LLM | C | "create a LLM for the Croatian language using monolingual data only" | same |
| Model efforts | Via HR-CLARIN under permissive licences | C | Results "accessible under permissive licenses" via the HR-CLARIN repository | same |
| Model efforts | Base, compute, status not stated | C | Not stated. Note: a news item on the page says "HR-GPT Beta" was presented in September 2024. | same |
| Strategy | Plan to 2032 with Action Plan 2026–2028 | C | "National AI Development Plan for the Period until 2032" and "Action Plan 2026-2028" | mpudt.gov.hr news 30131 |
| Strategy | Drafting since 27 May 2025 | C | Workshop of 27.05.2025 "marked the kick-off of the work of an Expert Working Group" | same |
| Strategy | Under Ministry of Justice, Public Administration and Digital Transformation | C | Footer: "Ministry of Justice, Public Administration and Digital Tranformation" | same |
| Strategy | (press) PM said in Feb 2026 adoption would come soon | C | 06 Feb 2026: "the government would soon adopt a National Plan for the Development of Artificial Intelligence (AI) through 2032" | glashrvatske.hrt.hr |
| Strategy | An earlier plan is listed by OECD.AI | U | The OECD.AI entry is a placeholder: "The Croatian government is currently working on a National Plan for the Development of AI"; start year 2020 and "adopted in late 2022" conflict on the page. It doesn't clearly list an earlier adopted plan. | oecd.ai policy-initiatives 2008 |
| Public-sector LLM | (press) 66 data centres, 44 state-owned | C | Croatia has 66 data centres, 44 of them state-owned | glashrvatske.hrt.hr |
| Language resources | HR-CLARIN coordinated by FFZG | C | "Koordinirajuća institucija ... Sveučilište u Zagrebu, Filozofski fakultet" | clarin.hr |
| Language resources | Partners: Institute for Croatian Language, FER TakeLab, SRCE, National and University Library | C | Partners listed: "Institut za hrvatski jezik", "Fakultet elektrotehnike i računarstva, TakeLab", "Sveučilišni računski centar", "Nacionalna i sveučilišna knjižnica" (plus three more) | same |
| Language resources | Repository at clarin.hr | C | "Pohranite svoje istraživačke podatke u HR-CLARIN repozitorij" (repository.clarin.hr) | same |
| Language resources | HR-CLARIN in CLARIN ERIC | C | Members: "HR-CLARIN" / "University of Zagreb" | clarin.eu/node/3754 |
| Key institutions | SRCE as EuroCC competence centre | C | "in 2019 SRCE obtained the mandate ... to establish a national consortium of the National Competence Centers in the Framework of EuroHPC (EuroCC) project" | srce.unizg.hr/en/croatian-centre-hpc |
| Power | Supek fully liquid-cooled | C | "100% of the heat is removed by Direct Liquid Cooling (DLC)" | srce.unizg.hr/en/advanced-computing |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Shared | Diaspora figures | NOT FOUND | I didn't reach an official page with a figure. A search found only press relaying a State Office estimate of about 3.2 million, plus academic ranges; hrvatiizvanrh.gov.hr gave no figure in the results. | n/a | n/a |
| Gigafactory | No Croatian bid found | FOUND (partial) | Croatia is one of 18 Member States that signed the EuroHPC joint procurement agreement for AI Gigafactories; no Croatian-led bid found. | https://digital-skills-jobs.europa.eu/en/latest/news/eu-ai-gigafactories-call-open-until-12-november-targeting-over-eu30-billion-investment | "Croatia, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Poland" |
| Model efforts | HRVOJE-M (Ciklopea with FFZG) | NOT FOUND | Two searches. The only hit is a LinkedIn post (not official), which gives EUR 1.46 million and 20–25 billion units. Nothing on a Ciklopea or FFZG page. | n/a | n/a |
| Strategy | Adoption of 2032 plan | NOT FOUND | Searches of vlada.gov.hr and mpudt.gov.hr found no adoption record; the latest is the Feb 2026 "soon". | n/a | n/a |
| Public-sector LLM | None on an official page | NOT FOUND (official); lead found | Press (tportal, 9 June 2026; informator.hr) reports that the ministry launched an AI virtual assistant on the gov.hr portal, answering from the portal's knowledge base and funded by NPOO. I found no ministry page. This may contradict "none found"; worth an official check. | (press) https://www.tportal.hr/tehno/clanak/dostupan-24-sata-dnevno-sredisnji-drzavni-portal-dobio-ai-asistent-20260609 | n/a (not fetched) |
| Language resources | National corpus size | NOT FOUND | Searched for the Croatian National Corpus (HNK) v3 size. Only secondary sources (about 216.8 million tokens, 2016). No official page fetched. | n/a | n/a |
| Power | No official constraint | NOT FOUND | No search beyond the cited page. | n/a | n/a |

#### C. Prose flags
1. Recommended strategy step 1: "the Serbian antenna is attached to Greece's and Italy's factories". CONFIRMED: SAIFA is linked to Pharos (Greece) and IT4LIA (Italy) (https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en).
2. Step 4 assumes that no public AI service exists yet. The press report of a gov.hr AI assistant (June 2026, see B) needs reconciling.

### CZ

#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Czech mother tongue 8,996,475 | C | Czech "8 996 475" (2021) | scitani.gov.cz/matersky-jazyk |
| Languages | Of 10,524,167 | C | Total "10 524 167" | same |
| Languages | 759,394 not stated | C | "nezjištěno ... 759 394" | same |
| Languages | Slovak 150,738 | C | "150 738" | same |
| Languages | Ukrainian 88,873 | C | "88 873" | same |
| Languages | Russian 59,560 | C | "59 560" | same |
| Languages | Vietnamese 43,822 | C | "43 822" | same |
| Languages | Polish 30,183 | C | "30 183" | same |
| Shared | Slovak mutually intelligible | U | Not on the cited census page. | same |
| EuroHPC system | Karolina at IT4I Ostrava, EuroHPC petascale | C | "EuroHPC petascale system Karolina, hosted and operated by IT4Innovations National Supercomputing Center" | eurohpc-ju.europa.eu/czechia_en |
| EuroHPC system | 15.7 PFlops peak | C | "theoretical peak performance of 15.7 PFlop/s". Note: the EuroHPC list page gives "12.91 petaflops Peak performance", so the sources differ. | it4i.cz karolina |
| EuroHPC system | 576 A100 GPUs | C | "576x NVIDIA A100" | same |
| EuroHPC system | In operation since 2021 | C | Start of operation "summer 2021" | same |
| AI Factory | CZAI selected 10 October 2025 | C | Dated "10 October 2025": "The Czech AI Factory (CZAI) will support the development and adoption of AI in Czechia." | eurohpc six additional factories |
| AI Factory | Linked to KarolAIna, AI-optimised, at IT4I | C | KarolAIna, "a new supercomputer optimised for AI workloads" | same |
| AI Factory | About 340 AI chips | C | "approximately 340 state-of-the-art AI chips" | e-infra.cz news |
| AI Factory | 850 PFlops in AI operations | C | "850 PFlop/s in AI operations" | same |
| AI Factory | Nearly CZK 1 billion split equally with EuroHPC | C | "nearly CZK 1 billion"; EuroHPC JU provides half, Czechia co-finances half | same |
| AI Factory | Led by VSB-TU Ostrava with BUT, Charles University, CTU | C | Confirmed; the page also lists two more partners (a neurodegenerative-disorders research centre and the Academy's Institute of Organic Chemistry and Biochemistry). | same |
| Gigafactory | MPO held the first official meeting on AI Gigafactory CZ | C | "první oficiální národní setkání k přípravě českého záměru" | mpo.gov.cz 289012 |
| Gigafactory | Meeting on 15 August 2025 | U | 15 August 2025 is the publication date; the page gives no meeting date. | same |
| Gigafactory | Run by České Radiokomunikace with IT4Innovations | C | CRA and IT4Innovations are the two partners; CRA to coordinate if successful | same |
| Gigafactory | At a Prague site | U | The page says only that the Prague Gateway data centre "by se ... mohlo stát součástí projektu AI Gigafactory"; it doesn't confirm the site. | same |
| Model efforts | Charles University coordinates OpenEuroLLM | C | Coordinated by Charles University | vyzkumne-infrastruktury.cz ?p=13945 |
| Model efforts | Digital Europe grant 101195233 | C | "grant agreement No 101195233"; "Digital Europe Programme" | openeurollm.eu |
| Model efforts | Launched 7 March 2025 | C | Launch press conference "7 March 2025" | vyzkumne-infrastruktury.cz |
| Model efforts | Over 32 languages | C | "more than 32 languages" | same |
| Model efforts | Open data | C | "fully accessible data" | same |
| Model efforts | National co-financing from education ministry | C | Ministry "ready to provide a national share of project co-financing" | same |
| Model efforts | CSMPT7b: continued pretraining of MPT-7B | C | Continued pretraining from the "English MPT7b model" | huggingface.co/BUT-FIT/CSMPT7b |
| Model efforts | 67-billion-token Czech collection | C | "Model was pretrained on ~67b token Large Czech Collection" | same |
| Model efforts | Apache-2.0 | C | "License: apache-2.0" | same |
| Model efforts | Trained on Karolina | C | "Training was done on Karolina cluster." | same |
| Model efforts | 2024 | C | Release plan dated 13.03.2024 | same |
| Strategy | NAIS 2030 approved by resolution 520 of 24 July 2024 | C | "byla schválena usnesením vlády č. 520 dne 24. července 2024" | mpo.gov.cz umela-inteligence |
| Strategy | AI in public administration among seven areas | C | "AI ve veřejné správě a veřejných službách" | same |
| Strategy | Annual action plans | C | "Akční plán bude každoročně vyhodnocován a aktualizován" | same |
| Strategy | 2025 plan approved by resolution 237 of 2 April 2025 | C | Resolution no. 237 of 2 April 2025. The body text names it as the Digitální Česko implementation plan for 2025, the headline as the NAIS action plan. | same |
| Strategy | Government AI commissioner | C | "nový vládní zmocněnec pro umělou inteligenci" (21.1.2026) | mpo.gov.cz 291280 |
| Public-sector LLM | AI Committee has a public-administration working group | C (other cited page) | Not on the row's cited page. The MPO page of 21.1.2026 (cited in the strategy row) lists working groups of the "klíčových oblastí NAIS", including AI in public administration. | mpo.gov.cz 291280 |
| Language resources | Czech National Corpus at Charles University | C | "na Filozofické fakultě Univerzity Karlovy" | korpus.cz |
| Language resources | SYN v14, January 2026 | C | Announcement dated "23. ledna 2026" | same |
| Language resources | Almost 5.5 billion words | C | "téměř 5,5 mld. slov" | same |
| Language resources | Funded as large RI to 2026 | C | Roadmap of large RIs, project LM2023044 (2023–2026) | same |
| Language resources | LINDAT/CLARIAH-CZ is the CLARIN and ALT-EDIC node | C | "the Czech node of the pan-European infrastructure CLARIN ERIC"; "the node for ... ALT-EDIC" | vyzkumne-infrastruktury.cz |
| Language resources | Joined ALT-EDIC May 2024 | C | Joined "in May 2024" | same |
| Key institutions | ÚFAL at Charles University (OpenEuroLLM coordination, LINDAT) | U | The cited pages name Charles University, not ÚFAL. | eurohpc czechia_en; korpus.cz |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Statutory status | FOUND (partial) | Czech is the language of administrative proceedings under § 16(1) of the Administrative Procedure Code (Act 500/2004); Slovak may also be used. The page is an archived Foreign Ministry notice, valid to 30 Nov 2017. | https://mzv.gov.cz/bern/cz/viza_a_konzularni_informace/matricni_zalezitosti/uredni_jazyk_ceske_republiky_ustanoveni.html | "V řízení se jedná a písemnosti se vyhotovují v českém jazyce." |
| Shared | Czech speakers in Slovakia | FOUND | Czech is the mother tongue of 33,864 residents of Slovakia (census 2021). | https://www.scitanie.sk/storage/app/media/dokumenty/narodnost_materinsky_jazyk_SK.xlsx | Row "český", total column: "33864" |
| Gigafactory | Later government approval | FOUND | The Czech government approved participation in the AI Gigafactory initiative and authorised MPO to join the EuroHPC procurement (CzechTrade, 06.07.2026). Press puts the decision on 22 June 2026. | https://www.czechtradeoffices.com/za/news/czech-republic-enters-the-race-to-host-one-of-europe-s-ai-gigafactories | "The Czech Government has officially approved the country's participation in the European AI Gigafactory Initiative." |
| AI Factory | KarolAIna operational date | NOT FOUND | No date found. The VUT project page gives the CZAI project duration as 1.5.2026–30.4.2029. Press (lupa.cz, May 2026) said the tender was not yet issued. | https://www.vut.cz/en/rad/projects/detail/38052 | "1.5.2026 — 30.4.2029" (duration only) |
| Model efforts | OpenEuroLLM national co-financing amount | FOUND | MŠMT project 8Y25001: state-budget support CZK 47.156 million; total recognised costs CZK 94.314 million; 1 Feb 2025 to 31 Dec 2028. | https://starfos.tacr.cz/projekty/8Y25001 | "Výše podpory ze státního rozpočtu" 47 156 tis. Kč |
| Public-sector LLM | No pilot or procurement | NOT FOUND | One search found nothing official. Press mentions a municipal AI assistant article in the Interior Ministry's magazine (2/2026), not checked. | n/a | n/a |
| Power | No official constraint | NOT FOUND | One search found only press (Forbes CZ: distributors report dozens of data-centre connection requests). Nothing from ČEPS or ERÚ. | n/a | n/a |

#### C. Prose flags
1. Recommended strategy step 1: "first model weights are due at the end of 2026 and the final models in January 2028". There is no source for this in the snapshot, and it is unchecked.
2. Step 5, "The Prague project": the cited MPO page doesn't fix a Prague site (see A).
3. "What good enough means": "spoken natively by 150,000 residents" matches 150,738.

### HU

#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Hungarian mother tongue 8,302,828 | C | Total, Hungarian, 2022: "8302828" | nepszamlalas2022.ksh.hu nsz2022-1.1.6-eng.xlsx |
| Languages | Of 9,603,634 | C | "Population ... 9603634" | same |
| Languages | 1,175,656 not answering | C | "Did not wish to answer, no answer ... 1175656" | same |
| Languages | German 28,473 | C | "German ... 28473" | same |
| Languages | Roma 23,192 | C | "Roma (Romany, Bea) ... 23192" | same |
| Languages | Ukrainian 15,315 | C | "Ukrainian ... 15315" | same |
| Languages | Romanian 11,186 | C | "Romanian ... 11186" | same |
| Languages | Slovak 10,123 | C | "Slovakian ... 10123" | same |
| Languages | Croatian 8,232 | C | "Croatian ... 8232" | same; table 1.1.6 is listed on nepszamlalas2022.ksh.hu/en/results/tables |
| Shared | 8,533 Hungarian MT in Czechia | C | Hungarian "8 533" | scitani.gov.cz/matersky-jazyk |
| EuroHPC system | Levente: hosting agreement with DKF, Budapest | C | LEVENTE "a new world-class mid-range EuroHPC supercomputer", hosted and operated by DKF in Budapest | eurohpc-ju.europa.eu Levente 2025-07-09 |
| EuroHPC system | Agreement dated 9 July 2025 | U | 9 July 2025 is the publication date; the page says only that the agreement "has now been signed". | same |
| EuroHPC system | At least 23 PFlops | C | "capable to executing at least 23 petaflops" | same |
| EuroHPC system | EUR 42 million | C | "The total cost of the LEVENTE project is EUR 42 million." | same |
| EuroHPC system | EuroHPC up to 35% | C | EuroHPC JU 35%, capped at "EUR 14,8 million" | same |
| EuroHPC system | Not yet procured | C | Procurement "will begin in the immediate future" (July 2025) | same |
| EuroHPC system | HUN-REN cites 2027 | C | "Levente, Hungary's own 20-petaflops HPC supercomputer, which is scheduled to go online in 2027". Note: 20 PF here, at least 23 PF at EuroHPC. | hun-ren.hu research_news 109042 |
| EuroHPC system | Komondor 5 PFlops | C | "has a performance of 5 petaflops" | hirek.unideb.hu node 14153 |
| EuroHPC system | Debrecen | C | "the Supercomputer Center on the Kassai út Campus of the University of Debrecen" | same |
| EuroHPC system | Since end of 2022 | C | Expected "to start operation in December" (article of Nov/Dec 2022) | same |
| EuroHPC system | Operated by DKF since 1 January 2025 | U | "2025. január 1-től a Digitális Kormányzati Fejlesztés és Projektmenedzsment Kft.-hez (DKF) került" refers to the national HPC remit; the same site calls Komondor "a KIFÜ szuperszámítógépe". | ncc.dkf.hu |
| AI Factory | Antenna HunAIFA, no factory | C | "The Hungarian AI Factory Antenna (HunAIFA)" | eurohpc antennas 2025-10-13 |
| AI Factory | Selected 13 October 2025 | C | Dated "13 October 2025" | same |
| AI Factory | Linked to JUPITER AI Factory | C | Links to the "JUPITER AI Factory (JAIF)" | same |
| AI Factory | Access to HUN-REN Cloud | C | Access to the "local HUN-REN Cloud" | same |
| AI Factory | Coordinated by HUN-REN SZTAKI | C | HUN-REN SZTAKI coordinates the consortium | hun-ren.hu hunren_news 109669 |
| AI Factory | With Wigner, ELTE and others | C | Partners: HUN-REN Wigner, ELTE, the Hungarian Chamber of Commerce and Industry, Neumann Technology Platform | same |
| AI Factory | About EUR 10 million over three years | C | Three-year project, budget approximately €10 million | same |
| AI Factory | Shared equally with EuroHPC | U | Neither page gives a per-antenna split. EuroHPC says EU funding of "around €55 million" for all antennas is matched by participating states. | both |
| Model efforts | PULI at HUN-REN Research Centre for Linguistics | C | Credits "the ELKH Hungarian Research Centre for Linguistics (NYTK)" | hun-ren.hu/en/news a-new-level |
| Model efforts | PULI GPT-3SX, 2022 | C | Article dated 22.11.2022 | same |
| Model efforts | 32 billion words | C | "material consisting of 32 billion words" | same |
| Model efforts | Free for non-profit research | C | "For non-profit research and development purposes, both language models are available free of charge." | same |
| Model efforts | LlumiX-32K: continued pretraining of LLaMA-2 | C | "The LLaMA-2-7B-32K model were continuously pretrained on Hungarian dataset" | huggingface.co/NYTK/PULI-LlumiX-32K |
| Model efforts | 7.9 billion Hungarian words | C | "Hungarian: 7.9 billion words" | same |
| Model efforts | Llama 2 licence | C | "License: llama2" | same |
| Model efforts | LlumiX-Llama-3.1: 8.7 billion words | C | "Hungarian (8.7 billion words)" | huggingface.co/NYTK/PULI-LlumiX-Llama-3.1 |
| Model efforts | Llama 3.1 licence | C | "License: llama3.1" | same |
| Strategy | AI Strategy 2020–2030 | C | "Hungary's Artificial Intelligence Strategy 2020-2030" | ai-watch.ec.europa.eu Hungary |
| Strategy | September 2020 | C | "In September 2020, the Hungarian Government published its National AI strategy" | same |
| Strategy | Hungarian language processing for administrative procedures | C | Programme to "support the automation of administrative procedures using AI-based services" | same |
| Strategy | Datasets collected by two ministries | C | Innovation and Interior ministries "collecting both oral and written training data sets" | same |
| Public-sector LLM | AI telephone service at NISZ | C | NISZ "is developing a telephone-based customer service for the public administration using AI solutions" | same |
| Language resources | HunCLARIN at the Research Centre for Linguistics | C | First listed member: "Nyelvtudományi Kutatóközpont" | clarin.hu |
| Language resources | Seven members | C | Seven active members listed (plus three inactive) | clarin.hu (Hungarian page; the /en page doesn't list them) |
| Key institutions | SZTAKI, Wigner, ELTE (antenna); DKF | C | As above | hun-ren 109669; ncc.dkf.hu |
| Power | Komondor liquid-cooled | C | "teljes mértékben közvetlen folyadékhűtéses HPC ... infrastruktúra" | ncc.dkf.hu Komondor green |
| Power | Waste heat reused at a Debrecen pool | C | "A megtermelt hulladékhő ... a Debreceni Sportuszodában hasznosul" | same |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Fundamental Law provision | FOUND | Article H)(1) of the Fundamental Law: Hungarian is the official language. | https://njt.jog.gov.hu/jogszabaly/2011-4301-02-00 | "Magyarországon a hivatalos nyelv a magyar." |
| Shared | Minority figures SK, RO, RS, UA | FOUND (SK only) | Slovakia, census 2021: 462,175 residents with Hungarian mother tongue. Romania, Serbia and Ukraine: only secondary or old sources found. | https://www.scitanie.sk/storage/app/media/dokumenty/narodnost_materinsky_jazyk_SK.xlsx | Row "maďarský", total column: "462175" |
| Gigafactory | No Hungarian bid | FOUND (partial) | Hungary signed the EuroHPC joint procurement agreement for AI Gigafactories; no Hungarian bid found. | https://digital-skills-jobs.europa.eu/en/latest/news/eu-ai-gigafactories-call-open-until-12-november-targeting-over-eu30-billion-investment | "Croatia, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Poland" |
| Model efforts | PULI funders | NOT FOUND | Neither HF card has a funding section. The 2022 article says only that the compute came from an ELKH infrastructure tender. One search found nothing more. | n/a | n/a |
| Model efforts | Racka-4B (press only) | FOUND | Official model card: ELTE (Humanities and Informatics faculties), base Qwen3-4B, trained on Komondor (64 × A100), 160B tokens, CC BY-NC-SA 4.0, research only; licence attributed to "Hungarian and EU regulations, as well as the licensing terms of our source data"; no dedicated funding. | https://huggingface.co/elte-nlp/Racka-4B | "This model is only to be used for research purposes, commercial or for-profit usage is not permitted." |
| Strategy | 2025 update | FOUND (partial) | Government Resolution 1369/2025 (X. 14.) on measures promoting domestic AI use: Hungarian linguistic-cultural multimodal database, state and market data centres. I found the renewed strategy text itself only via press and a law-firm note (published 3 Sept 2025). | https://njt.jog.gov.hu/jogszabaly/2025-1369-30-22 | "1369/2025. (X. 14.) Korm. határozat a mesterséges intelligencia hazai alkalmazását előmozdító intézkedésekről" |
| Public-sector LLM | No LLM assistant | NOT FOUND | One search found nothing. | n/a | n/a |
| Language resources | CLARIN ERIC status | FOUND | Hungary is a CLARIN ERIC member (HunCLARIN, Hungarian Research Centre for Linguistics). | https://www.clarin.eu/node/3754 | Members: "HunCLARIN" / "Hungarian Research Centre for Linguistics" |
| Language resources | Hungarian National Corpus size | NOT FOUND | The official nytud.hu page returned 403 twice. Secondary sources give about 1 billion, 1.04 billion (v2.0.5) and 1.5 billion words, and they conflict. | n/a | n/a |
| Power | Grid figures | NOT FOUND | One search; no MAVIR data-centre figure. | n/a | n/a |

#### C. Prose flags
1. Recommended strategy step 6: "Hungarian-language public services exist in law" in Slovakia, Romania and Serbia. This is unchecked.
2. "Main blocker" treats a 2025 strategy update as hypothetical ("if a 2025 strategy update funds PULI"). Resolution 1369/2025 exists, and press reports a renewed strategy published in September 2025 (see B).

### PL

#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Polish at home 37,868,618 | C | "Polski \| 37868618" | stat.gov.pl jezyk_uzywany_w_domu xlsx |
| Languages | Of 38,036,118 | C | "Ogółem \| 38036118" | same |
| Languages | Silesian 467,145 | C | "śląski \| 467145" | same |
| Languages | German 216,342 | C | "niemiecki \| 216342" | same |
| Languages | Kashubian 89,198 | C | "kaszubski \| 89198" | same |
| Languages | Ukrainian 55,104 | C | "ukraiński \| 55104" | same |
| Shared | 30,183 Polish MT in Czechia | C | Polish "30 183" | scitani.gov.cz |
| Shared | 3,398 in Hungary | C | Total, Polish, 2022 mother tongue: "3398" | ksh nsz2022-1.1.6 xlsx |
| EuroHPC system | No EuroHPC classical system | C | None in Poland among the twelve systems | eurohpc our-supercomputers |
| EuroHPC system | PIAST-Q at PSNC | C | "a European ion-trapped quantum computer hosted at PCSS as part of the EuroHPC Joint Undertaking" | psnc.pl User Days 2026 |
| EuroHPC system | Helios 37 PFlops theoretical | C | "Helios has 37 PFLOPS of theoretical computing power" | cyfronet.pl our-supercomputers |
| EuroHPC system | 440 GH200 | C | "440 NVIDIA Grace Hopper GH200 superchips" | same |
| EuroHPC system | Athena 384 A100 | C | "384 NVIDIA A100 GPGPU cards" | same |
| AI Factory | PIAST at PSNC, selected 12 March 2025 | C | Dated "12 March 2025"; PIAST led by PSNC | eurohpc 2025-03-12 |
| AI Factory | "Services available from 2026" | C | "Services Available from ... 2026" | eurohpc ai-factories/poland_en |
| AI Factory | Planned capacity over 1,500 GPUs | C | "planned capacity exceeding 1,500 GPUs" (PSNC page; not on the EuroHPC Poland page) | psnc.pl |
| AI Factory | Gaia at Cyfronet in PLGrid, selected 10 Oct 2025 | C | "deployed and operated by Cyfronet AGH" "within the framework of the PLGrid infrastructure" | eurohpc 2025-10-10 |
| AI Factory | LLMs among target sectors | C | "The target sectors include healthcare, the space and LLMs." | same |
| Gigafactory | Baltic AI GigaFactory EoI, 20 June 2025 | C | Page dated 20.06.2025, titled as submitted ("złożony"); no separate submission date | gov.pl wniosek baltic |
| Gigafactory | Poland lead with EE, LT, LV | C | "Polska wspólnie z Estonią, Litwą i Łotwą" | same |
| Gigafactory | EUR 3 billion | C | "3 mld euro" | same |
| Gigafactory | 65% private | C | "65 proc. całkowitej inwestycji zostanie pokryte z kapitału prywatnego" | same |
| Gigafactory | Up to two Polish sites | C | "maksymalnie w dwóch lokalizacjach" | same |
| Gigafactory | 100% green energy | C | "dostęp do w 100% zielonej energii" | same |
| Gigafactory | PLLuM and Bielik among goals | C | "takich jak PLLuM i Bielik" | same |
| Model efforts | "the first government LLM" | C | "pierwszy rządowy LLM (Large Language Model) zaprojektowany specjalnie z myślą o języku polskim" | gov.pl czesc-jestem-pllum |
| Model efforts | 18 versions | C | Family of 18 versions | same |
| Model efforts | 8B to 70B | U | Not on the gov.pl page or the two fetched cards. | same; HF cards |
| Model efforts | 100-billion-word corpus, no synthetic data | C | About 100 billion words, "bez generowania syntetycznych treści" | same |
| Model efforts | Released 24 February 2025 | C | NASK article dated 24.02.2025: the assistant "is now available to Internet users" | science.nask.pl 12757 |
| Model efforts | NASK-led, now HIVE: NASK, PWr, IPI PAN, OPI-PIB, Łódź, COI, Cyfronet | C | All named. The page also lists the PAN Institute of Slavic Studies, which the note omits. | same |
| Model efforts | Funded by the Minister of Digital Affairs, subsidy 1/WII/DBI/2025 | C | "Project financed by the Minister of Digital Affairs under the targeted subsidy No. 1/WII/DBI/2025." | HF Llama-PLLuM-8B-chat-2512 |
| Model efforts | About PLN 18.5 million | C | About 18.5 million PLN; contract 25 March 2025 | HF PLLuM-12B-chat-2512 |
| Model efforts | Dec 2025 generation Apache-2.0 on Mistral-Nemo 12B | C | Base Mistral-Nemo-Base-2407; "License: apache-2.0" | same |
| Model efforts | Llama 3.1 licence on Llama variants | C | Base "Llama-3.1-8B"; licence "llama3.1" | HF Llama-PLLuM-8B |
| Model efforts | Bielik-11B-v3.0, SpeakLeash with Cyfronet | C | "SpeakLeash & ACK Cyfronet AGH" | HF speakleash Bielik-11B-v3.0-Instruct |
| Model efforts | Apache-2.0 | C | "License: Apache 2.0" | same |
| Model efforts | Trained on Athena and Helios under a PLGrid grant | C | "Athena and Helios supercomputer"; "computational grant number PLG/2024/016951" | same |
| Strategy | Resolution 196 of 28 December 2020 | C | "Uchwała nr 196 Rady Ministrów z dnia 28 grudnia 2020 r." | gov.pl/web/ai polityka 2020 |
| Strategy | In force | U | Not stated on the page. The 2030 draft would repeal it ("Traci moc uchwała nr 196"), which implies it is in force. | same |
| Strategy | 2030 draft dated 15 April 2026 | C | "Data sporządzenia 2026-04-15" | gov.pl attachment 2af79671 |
| Strategy | PLLuM and Bielik as basis | C | "wspólnie projekty PLLuM i BIELIK stanowią podstawę długofalowej strategii budowy suwerennego ekosystemu AI" | same |
| Strategy | Pilot in at least 1,000 public entities | C | "Min. 1000 podmiotów publicznych przeprowadzone pilotażowe wdrożenie polskiego modelu językowego PLLuM" | same |
| Strategy | PLGrid compute target | C | "80% wykorzystania zasobów infrastruktury technologicznej PLGrid" | same |
| Public-sector LLM | Ministry, Feb 2025: first deployment mObywatel | C | First deployment to be integration with the mObywatel app | gov.pl czesc-jestem-pllum |
| Public-sector LLM | NASK: citizen and civil-servant assistants | C | "mObywatel Assistant"; "an assistant for civil servants that will automate document processing" | science.nask.pl 12757 |
| Language resources | NKJP over 1.5 billion words | C | "korpus referencyjny polszczyzny wielkości ponad półtora miliarda słów" | nkjp.pl |
| Language resources | IPI PAN with partners | C | Coordinated by IPI PAN with partners | same |
| Language resources | CLARIN-PL at PWr | C | Politechnika Wrocławska as "Lider projektu" | clarin-pl.eu |
| Language resources | Funded through 2027 | C | Funding period 2025–2027 under FENG | same |
| Language resources | Hosts the PLLuM demo | NC | The page doesn't mention PLLuM or a demo. | same |
| Key institutions | NASK, PSNC, Cyfronet, OPI, IPI PAN, PWr, SpeakLeash | C | As above | cyfronet.pl; science.nask.pl |
| Power | Gigafactory site: 100% green, adequate power and cooling | C | "odpowiednie systemy zasilania i chłodzenia" | gov.pl wniosek baltic |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Statutory status of Polish and Kashubian | FOUND (Kashubian); NOT FOUND (Polish) | Consolidated minorities act (Dz.U. 2026 poz. 75), art. 19(2): Kashubian is the regional language. I didn't fetch the constitutional or statutory text on Polish. | https://eli.gov.pl/api/acts/DU/2026/75/text/T/D20260075L.pdf | "Językiem regionalnym w rozumieniu ustawy jest język kaszubski." |
| Shared | Wider diaspora | NOT FOUND | No search beyond the census tables. | n/a | n/a |
| AI Factory | Funding amounts | NOT FOUND (official) | Press only: Gaia about PLN 300 million or EUR 70 million, half EU; PIAST EUR 50 million EU plus PLN 340 million national. No gov.pl or EuroHPC page found. | n/a | n/a |
| Gigafactory | Poland entered lot 1 | FOUND | The Council of Ministers adopted a resolution enabling participation; Poland bids in Lot 1, committing to buy AI services worth EUR 100 million in 2028–2033 (14.07.2026). | https://www.gov.pl/web/cyfryzacja/uchwala-rzadu-droga-do-gigafabryki-ai-otwarta | "Polska ubiega się o realizację projektu w ramach Lot 1." |
| Gigafactory | Estonia and Latvia withdrew | NOT FOUND (official) | Press only (itwiz: a deputy minister is quoted saying both withdrew). The gov.pl page doesn't mention it. | n/a | n/a |
| Model efforts | Bielik funder | NOT FOUND | The model card names only the computational grant PLG/2024/016951; the search returned nothing relevant. | n/a | n/a |
| Strategy | 2030 policy adoption | NOT FOUND | The gov.pl draft page (published 16.04.2026, version 1.0) shows a draft only. | https://www.gov.pl/web/cyfryzacja/projekt-uchwaly-rady-ministrow-w-sprawie-ustanowienia-polityki-rozwoju-sztucznej-inteligencji-w-polsce-do-2030-roku-id260 | n/a |
| Public-sector LLM | Assistant reached all users about 31 Dec 2025 | FOUND | Ministry, 30.12.2025: the PLLuM-based chatbot is available to all mObywatel users (app 4.71.1+, not mObywatel Junior) from 31 December. | https://www.gov.pl/web/cyfryzacja/nowa-usluga-w-mobywatelu-wirtualny-asystent-ulatwi-korzystanie-z-uslug-publicznych | "Od 31 grudnia br." / "Czatbot korzysta z polskiego modelu językowego PLLuM." |
| Power | Grid figures | NOT FOUND | One search found PSE connection-refusal data for generation, nothing for data centres. | n/a | n/a |

#### C. Prose flags
1. Recommended strategy step 5: "Moldova's antenna is attached to PIAST". CONFIRMED: FAIMA (Moldova) is linked to the PIAST AI Factory (https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en). The EuroHPC ai-factories overview lists no antenna under PIAST, so the two EuroHPC pages differ.
2. Step 6: "The Baltic bid, now in the EuroHPC call". The government page describes a Polish Lot 1 bid, and press reports Estonia and Latvia withdrew, so calling it "the Baltic bid" may be out of date.

### SK

#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Slovak, state language under Act 270/1995 | C | "Zákon Národnej rady Slovenskej republiky o štátnom jazyku Slovenskej republiky" | slov-lex.sk 1995/270 |
| Languages | 5,449,270 residents | C | "OBYVATELIA 5449270 obyvateľov" | scitanie.sk |
| Languages | 12% other mother tongue | C | "12 %uviedlo iný materinský jazyk ako slovenský" | same |
| Shared | Czech mutually intelligible | U | Not on the cited census pages. | scitani.gov.cz |
| Shared | Slovak MT 150,738 in Czechia | C | "150 738" | scitani.gov.cz |
| Shared | 10,123 in Hungary | C | "Slovakian ... 10123" | ksh xlsx |
| EuroHPC system | None | C | No Slovak system among the twelve | eurohpc our-supercomputers |
| EuroHPC system | Devana at SAS, 32 A100 | C | 8 GPU nodes with "four Nvidia A100 40 GB GPGPU accelerators" each (32, derived) | vs.sav.sk Devana |
| EuroHPC system | About 800 TFlops | C | "~800 TFlops" | same |
| EuroHPC system | 130 kW | C | "Power input" "130 kW" | same |
| EuroHPC system | Perun funded by recovery plan | C | "Recovery and Resilience Plan of the Slovak Republic – Component 17, Investment 3" | hpc.sav.sk our-projects |
| EuroHPC system | Project 17I03-04-P02-00001 | C | "17I03-04-P02-00001" | same |
| EuroHPC system | (press) Full operation 31 March 2026 | C | Perun "put in full operation" (31 March 2026). The article is in English. | tasr.sk |
| EuroHPC system | (press) Over 24 PFlops across two systems | C | "a computing performance exceeding 24 petaFLOPS" | same |
| AI Factory | Antenna SKAIAT, selected 13 October 2025 | C | SKAIAT among antennas announced 13 October 2025 | eurohpc antennas 2025-10-13 |
| AI Factory | Linked to Austria's AI:AT | C | Linked to "AI:AT, the AI Factory in Austria" (the digital-strategy page lists SKAIAT without the link) | same; digital-strategy.ec.europa.eu |
| Model efforts | mistral-sk-7b: Mistral-7B on Araneum Slovacum | C | "a Slovak language version of the Mistral-7B-v0.1"; "Araneum Slovacum VII Maximum web corpus" | HF slovak-nlp/mistral-sk-7b |
| Model efforts | TU Košice and SAS institutes | C | "Technical University of Košice"; "Ľ. Štúr Institute of Linguistics, Slovak Academy of Sciences" | same |
| Model efforts | Leonardo compute | C | "high performance computing resources operated by CINECA", National Leonardo access call 2023 | same |
| Model efforts | Apache-2.0 | C | "Apache license 2.0" | same |
| Model efforts | Qwen3-14B-sk, same institutions | C | TU Košice, the SAS Centre of Social and Psychological Sciences, the Ľ. Štúr Institute | HF slovak-nlp/Qwen3-14B-sk |
| Model efforts | Leonardo and Perun | C | CINECA Leonardo; "PERUN supercomputer ... provided by the Technical University of Košice" | same |
| Model efforts | Apache-2.0 | C | "Apache license 2.0" | same |
| Model efforts | Slovak NLP community coordinated by KInIT | C | "The community is coordinated by the Kempelen Institute of Intelligent Technologies." | kinit.sk ?p=42195 |
| Model efforts | September 2025 memorandum | C | "Memorandum of Understanding on cooperation in the development of natural language processing" (September 2025) | same. The journals.savba.sk article it also cites supports only the Mistral fine-tune, not the model name or compute. |
| Strategy | Digital Transformation Strategy 2030 adopted | C | "Slovenská vláda prijala Stratégiu digitálnej transformácie Slovenska 2030." | mirri.gov.sk umela-inteligencia |
| Strategy | Action plans to 2026 | C | Links to the "Akčný plán digitálnej transformácie Slovenska na roky 2023-2026" | same |
| Strategy | Presentation of 27 February 2026 | C | "27.02.2026" | mirri.gov.sk presentation PDF |
| Strategy | Six-pillar AI vision | C | "6 pilierov Vízie AI pre Slovensko" | same |
| Strategy | Incl. infrastructure and AI Factories | C | "Zapojenie do európskej iniciatívy AI Factories" | same |
| Strategy | Strategy to government by end of Q2 2026 | C | "do konca 2. kvartálu 2026 ... Predloženie Národnej AI stratégie na rokovanie vlády SR" | same |
| Public-sector LLM | Twelve assistants for life situations | C | "Nasadenie 12 kľúčových AI asistentov pre najčastejšie životné situácie." | same |
| Public-sector LLM | Co-pilots for officials | C | "Inteligentná podpora úradníkov (AI co-piloti)" | same |
| Public-sector LLM | Central AI-system register | C | "Zriadenie Centrálneho registra AI systémov verejnej správy" | same |
| Public-sector LLM | Central MLOps platform | C | "Centrálna platforma pre trénovanie a prevádzku modelov (MLOps framework)" | same |
| Public-sector LLM | Proof of concept by end of 2026 | C | "Infraštruktúra, dáta a „Proof of Concept“: do konca 4. kvartálu 2026" | same |
| Language resources | SNK at the Štúr Institute, texts from 1955 | C | "elektronická databáza primárne obsahujúca slovenské texty od r. 1955" | korpus.juls.savba.sk |
| Language resources | Size not stated | C | No size given | same |
| Language resources | CLARIN-SK founded February 2026 | C | "Establishment of the CLARIN-SK association (February 2026)" | kinit.sk ?p=42195 |
| Key institutions | Computing Centre SAS and NSCC (Devana, Perun) | C | Perun implemented by NSCC member "CSČ SAV" | nscc.sk |
| Key institutions | EuroCC competence centre with TU Košice | U | The page shows TU Košice and VS SAV logos but doesn't describe their roles. | eurocc-slovakia.sk |
| Power | Devana draws 130 kW | C | "130 kW" | vs.sav.sk |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Hungarian, Romani, Rusyn breakdown | FOUND | Census 2021 mother tongue: Hungarian 462,175; Romani 100,526; Rusyn 38,679 (Slovak 4,456,102; not stated 312,364; total 5,449,270). | https://www.scitanie.sk/storage/app/media/dokumenty/narodnost_materinsky_jazyk_SK.xlsx | Rows "maďarský ... 462175", "rómsky ... 100526", "rusínsky ... 38679" |
| AI Factory | SKAIAT host institution | NOT FOUND | Neither EuroHPC antenna page names a host. Search only surfaced KInIT as coordinator of a different body (SKAI-eDIH). | https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en | n/a |
| Gigafactory | No Slovak bid | FOUND (partial) | Slovakia signed the EuroHPC joint procurement agreement; no Slovak bid found. | https://digital-skills-jobs.europa.eu/en/latest/news/eu-ai-gigafactories-call-open-until-12-november-targeting-over-eu30-billion-investment | "Portugal, Slovakia, Spain" and "Sweden" |
| Model efforts | Funders | FOUND (partial) | The model cards credit compute via the National Leonardo access call, awarded by the Computing Centre of the Slovak Academy of Sciences, and Perun via TU Košice; one author's work was supported by DiusAI a. s. No government model grant is named. | https://huggingface.co/slovak-nlp/Qwen3-14B-sk | "awarded through the National Leonardo access call by the Computing Centre of the Slovak Academy of Sciences" |
| Strategy | Adoption | NOT FOUND | No government resolution found. A LinkedIn post (not official) says an AI-administration bill was approved 26 Aug 2026. | n/a | n/a |
| Public-sector LLM | Nothing deployed | NOT FOUND | Nothing found. | n/a | n/a |
| Power | No official constraint | NOT FOUND | No search beyond the cited page. | n/a | n/a |

#### C. Prose flags
1. Main blocker: "ALT-EDIC where Slovakia is an observer". This is unchecked; one search found nothing.
2. Main blocker: "No adopted AI strategy". Possibly overtaken: press reports an AI law approved by government on 26 Aug 2026 and the strategy tied to it (see B). Unconfirmed.

### SI

#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Slovene official | C | "Slovenian is the official language of the Republic of Slovenia." | gov.si/en/topics/official-language |
| Languages | Italian and Hungarian official alongside, in minority areas | C | "Hungarian or Italian is an official language alongside Slovenian." | same |
| Languages | About 2.4 million MT | C | "Slovenian is the mother tongue of around 2.4 million people, of whom around 1.85 million live in Slovenia." | same |
| Languages | About 1.85 million in Slovenia | C | same | same |
| Shared | About 0.55 million outside Slovenia (derived) | C | Arithmetic from the two figures above. | same |
| Shared | GaMS secondary languages | C | "Croatian, Bosnian and Serbian (secondary)" | HF GaMS3 card |
| EuroHPC system | Vega at IZUM, Maribor | C | "hosted by IZUM"; "located in Maribor, Slovenia" | eurohpc our-supercomputers |
| EuroHPC system | Operational | C | Listed with an access link; no explicit status field | same |
| EuroHPC system | 6.92 PFlops sustained | C | "6.92 petaflops Sustained performance" | same |
| EuroHPC system | HPC RIVR EUR 20 million | C | "HPC RIVR project, with a budget of EUR 20 million" | gov.si National_Programme_for_AI_2025.pdf |
| EuroHPC system | Total HPC investment EUR 26.5 million | C | "bringing the total investment in HPC capacity (Slovenian and EU part) to EUR 26.5 million" | same |
| AI Factory | SLAIF selected 12 March 2025 | C | Dated "12 March 2025"; IZUM host and coordinator | eurohpc 2025-03-12 |
| AI Factory | IZUM builds and runs the new system with JSI and ARNES | C | "IZUM will develop and manage the new supercomputer system" with JSI and ARNES | eurohpc ai-factories/slovenia_en |
| AI Factory | New ARNES data centre at Mariborski otok | C | "a new advanced data centre built by ARNES near the Mariborski otok hydroelectric power plant" | same |
| AI Factory | Partners incl. Universities of Ljubljana, Maribor, Nova Gorica, Primorska | C | Listed | same; uni-lj 2025-03-14 |
| AI Factory | Operational early 2027 | C | "is expected to be operational in early 2027" | uni-lj 2025-03-14 |
| AI Factory | Replaces Vega | C | Replacing Vega (uni-lj). Note: slovenia.si says it will "significantly upgrade the capabilities of the existing Vega", and the EuroHPC press release says SLAIF integrates with VEGA. | uni-lj; slovenia.si |
| Model efforts | GaMS from UL FRI / CJVT, PoVeJMo 2023–2026 | C | "(PoVeJMo), which ran from 2023 to 2026" | uni-lj 2026-07-20 |
| Model efforts | Funded by ARIS through the RRP | C | "funded through the 'Recovery and Resilience Plan' by the Slovenian Research and Innovation Agency (ARIS) and NextGenerationEU" | HF GaMS3 card |
| Model efforts | Horizon Europe support | C | "Horizon Europe (project 101186647, AI4DH)" | same |
| Model efforts | NVIDIA sovereign-AI support | C | NVIDIA "through its Sovereign AI initiative" | same |
| Model efforts | Base Gemma-3-12B | C | Base "gemma-3-12b-pt" | same |
| Model efforts | Gemma licence | C | Licence: Gemma | same |
| Model efforts | About 100.9 billion tokens of continued pretraining | C | "Base CPT: 100,876,943,360 tokens" | same |
| Model efforts | Plus parallel and long-context stages | C | Parallel alignment 12.8B tokens; Long CPT 20.1B tokens | same |
| Model efforts | About 150k GPU hours on Leonardo | C | "LEONARDO (EuroHPC): about 150k GPU hours" | same |
| Model efforts | Released, with a public chatbot | C | "released as an open-source model on Hugging Face"; "available to users as a chatbot on the povejmo.si platform" | uni-lj 2026-07-20 |
| Model efforts | Local-installation support from SLAIF | C | "Če potrebujete pomoč pri lokalni namestitvi ... se lahko obrnete na" SLAIF | gams.povejmo.si/odprtidostop |
| Model efforts | 27B Nemotron-based variant released | C | GaMS-27B-Instruct-Nemotron listed among released models | same |
| Model efforts | Text from donation campaign, NUK, Dnevnik, STA | C | "Additional training data were provided by organisations including" NUK, Dnevnik, the Slovenian Press Agency; public donation campaign | uni-lj 2026-07-20 |
| Strategy | NpUI approved 27 May 2021 | C | "Ljubljana, 27 May 2021, approved by the Government" | gov.si NpUI PDF |
| Strategy | About EUR 110 million over five years | C | "expected to invest around EUR 110 million over five years". Note: OECD.AI shows €110,000,000 as an annual expenditure range. | same; oecd.ai 3004 |
| Strategy | Language technologies and public administration priorities | C | Priority sectors include "language technologies and cultural identity, the public sector" | oecd.ai 3004 |
| Strategy | NsUI 2030 adopted 5 March 2026 | C | "Vlada Republike Slovenije je 5. marca 2026 sprejela Nacionalno strategijo za umetno inteligenco do leta 2030." | gov.si nsui 2030 |
| Strategy | Goal 1 covers Slovene language technologies, data, models | C | "Poseben poudarek je namenjen slovenskemu jeziku, slovenski kulturi in kulturni dediščini." | same |
| Strategy | Goal 2 public-sector use | C | "Povečanje uporabe umetne inteligence v gospodarstvu, znanosti, javnem sektorju in civilni družbi" | same |
| Public-sector LLM | Goal 2 with human oversight | C | "... etičnih standardov in človeškega nadzora" | same |
| Language resources | CLARIN.SI lead: Jožef Stefan Institute | U | The cited page names no lead. CLARIN ERIC's member list gives "CLARIN.SI" / "Jožef Stefan Institute" (clarin.eu/node/3754). | clarin.si/info/about |
| Language resources | LLM-benchmark dashboard | C | Services menu: "LLM Benchmarks" | same |
| Language resources | CJVT develops Slovene resources | C | "the development and maintenance of key digital language resources" | cjvt.si/en |
| Language resources | GaMS corpus target 40 billion words | C | "an extensive volume of training data amounting to 40 billion words" | slovenia.si language-AI page |
| Key institutions | JSI as SLAIF technical coordinator | C | JSI "technical coordinator for the AI Factory part" (EuroHPC 12 March 2025). The slovenia_en page calls it a collaborator. | eurohpc 2025-03-12 |
| Key institutions | SLING EuroCC competence centre | C | "National Competence Centre SLING is co-funded by the Ministry of Education, Science and Youth" | sling.si/en |
| Power | ARNES DC cabled directly to Mariborski otok | C | "will be directly connected to the Mariborski otok hydroelectric power plant via an electrical cable" | gov.si 2025-05-06 |
| Power | Waste-heat agreement for Maribor | C | Letter of intent: "Use of excess heat from the Arnes data centre and supercomputer in Maribor" | same |
| Power | Foundation stone 6 May 2025 | C | Dated "6. 5. 2025" | same |

#### B. Unverified cells
| Row | Cell | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Minority speaker counts | NOT FOUND | Only a journal article citing 2002 census figures (Italian MT 3,762). No SURS table fetched. | n/a | n/a |
| Gigafactory | No Slovenian bid | FOUND (indirect) | Slovenia is not among the 18 Member States that signed the EuroHPC joint procurement agreement. | https://digital-skills-jobs.europa.eu/en/latest/news/eu-ai-gigafactories-call-open-until-12-november-targeting-over-eu30-billion-investment | "Croatia, Czechia, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Poland" ... "Portugal, Slovakia, Spain" and "Sweden" |
| AI Factory | Budget EUR 135 million (press only) | FOUND | Government (11.2.2026): SLAIF is a EUR 135 million strategic project co-financed by Slovenia and EuroHPC JU; the new system replaces Vega in Maribor by 2027. | https://www.gov.si/novice/2026-02-11-slovenija-vstopa-v-novi-razvojni-cikel-umetne-inteligence-od-uspesnih-edih-ov-do-tovarne-ui/ | "SLAIF je strateški projekt vreden 135 milijonov evrov" |
| Model efforts | PoVeJMo funding amount | FOUND | Total investment EUR 4 million, EU (RRF) contribution EUR 3.4 million, September 2023 to June 2026. | https://reforms-investments.ec.europa.eu/projects/povejmo-adaptive-natural-language-processing-large-language-models-co-financing-research-innovation_en | "the total value of the investment is EUR 4 million" |
| Public-sector LLM | Assistant pilots or procurements | NOT FOUND | One search found none; the NsUI page lists no public-sector pilots. | n/a | n/a |
| Language resources | National corpus size | FOUND | Gigafida 2.0, the reference corpus of written standard Slovene: 1,134,693,933 words, 59,861,870 sentences, 38,310 texts. | https://www.clarin.si/repository/xmlui/handle/11356/1320 | "59861870 sentences, 1134693933 words, 38310 texts" |

#### C. Prose flags
1. Recommended strategy step 2: "the 27B variant under Nemotron terms". Unchecked: the gams.povejmo.si page lists GaMS-27B-Instruct-Nemotron but no licence, and I didn't fetch its card.
2. Step 3: "GaMS was trained mostly on Italy's Leonardo". CONFIRMED: about 150k Leonardo GPU hours, against about 1k on the faculty node and about 40k on NVIDIA DGX Cloud Lepton (GaMS3 card).
3. Main blocker: "a research programme that has ended on paper". CONFIRMED: the EC page says PoVeJMo runs September 2023 to June 2026.

### Summary
| State | Claims checked | Confirmed | Not confirmed | Unclear | Unverified cells | Found | Not found |
|---|---|---|---|---|---|---|---|
| HR | 38 | 35 | 1 | 2 | 7 | 1 (partial) | 6 |
| CZ | 47 | 43 | 0 | 4 | 7 | 4 (1 partial) | 3 |
| HU | 48 | 45 | 0 | 3 | 10 | 6 (3 partial) | 4 |
| PL | 53 | 50 | 1 | 2 | 9 | 3 (1 partial) | 6 |
| SK | 42 | 40 | 0 | 2 | 7 | 3 (2 partial) | 4 |
| SI | 46 | 45 | 0 | 1 | 6 | 4 (1 indirect) | 2 |

PL "Found" counts the statutory-status cell as partial: Kashubian found, Polish not found. That cell is counted in Found, not in Not found.

NOT CONFIRMED claims:
1. HR, AI Factory row: the note's quotation of SRCE, "missed a chance to establish a national AI factory in earlier calls", is not verbatim. The page reads "Although Croatia missed the opportunity to establish a national AI factory in earlier calls". The substance and the December 2025 date are confirmed. https://www.srce.unizg.hr/en/news/third-croatian-competence-centre-hpc-day-held/1438
2. PL, Language resources row: "CLARIN-PL ... hosting the PLLuM demo". clarin-pl.eu doesn't mention PLLuM or a demo. https://clarin-pl.eu/

## Review: Nordic and Baltic (DK, EE, FI, LV, LT, SE), 2026-10-10
Tools: WebSearch available: yes; about 109 URLs fetched; 13 failed (2x 404, 9x 403/bot wall, 2x timeout). Every URL cited in the six Snapshot tables was reachable on the first try.

Verdicts: CONFIRMED / NOT CONFIRMED / UNCLEAR. Quotes are as returned by WebFetch, which extracts text with a model. Treat them as close paraphrase-quotes and re-check them mechanically before admitting anything.

### DK
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Population 5,992,734 (Eurostat 2025) | CONFIRMED | "5 992 734"; "Eurostat - 2025 figures" | european-union.europa.eu/.../denmark_en |
| Languages | Danish is the official language | CONFIRMED | "Official EU language(s): Danish" | same |
| Shared with | Danish is a training language of Viking | CONFIRMED | "pretrained on Finnish, English, Swedish, Danish, Norwegian, Icelandic and code" | huggingface.co/LumiOpen/Viking-33B |
| Shared with | Danish is a training language of GPT-SW3 | CONFIRMED | "320B tokens in Swedish, Norwegian, Danish, Icelandic, English, and programming code" | huggingface.co/AI-Sweden-Models/gpt-sw3-40b |
| Shared with | Mutually intelligible with Norwegian and Swedish | NOT CONFIRMED | Neither cited page says this. The Viking card says only that the model is fluent in the Scandinavian languages. | both HF cards |
| EuroHPC system | Denmark is a member of the LUMI consortium | CONFIRMED | "Finland, Belgium, the Czech Republic, Denmark, Estonia, Iceland, the Netherlands, Norway, Poland, Sweden, and Switzerland" | lumi-supercomputer.eu/about-lumi/ |
| AI Factory | Partner in the LUMI AI Factory with CZ, EE, NO, PL | CONFIRMED | "led by Finland, together with 5 other countries" (Czech Republic, Denmark, Estonia, Norway, Poland) | eurohpc-ju.europa.eu/selection-first-seven-... |
| AI Factory | LUMI-AI contracted 31 Aug 2026, EUR 387.8 million | CONFIRMED | "a total budget of EUR 387 800 000" | eurohpc-ju.europa.eu/...lumi-ai-supercomputer-2026-08-31_en |
| AI Factory | Available in 2027 | CONFIRMED | "expected to be installed and made available to users in 2027" | same |
| AI Factory | EuroCC Denmark is the national competence centre | CONFIRMED | "det danske kompetencecenter for supercomputing" | digst.dk/kunstig-intelligens/ai-fabrikker/ |
| Gigafactory | Ministry statement of 31 July 2026 | CONFIRMED | Press release dated 31.7.2026 | via.ritzau.dk/.../15067561/... |
| Gigafactory | Up to DKK 750 million over five years, buying capacity | CONFIRMED | "Danmark har tilkendegivet at ville aftage kapacitet for op til 750 mio. kr. over fem år." | same |
| Gigafactory | Possibly in Finland | CONFIRMED | "der kan aftages kapacitet fra AI-gigafabrikker i Finland" | same |
| Models | DFM partners: Aarhus, SDU, Copenhagen, Alexandra Institute | CONFIRMED | "in collaboration with the University of Southern Denmark, the University of Copenhagen, and the Alexandra Institute" | chc.au.dk/... |
| Models | DKK 30.7 million from the Ministry of Digital Affairs, 2024 to 2027 | CONFIRMED | "Ministry of Digital Affairs with DKK 30,700,000"; "2024 - 2027". KU adds that 20.7m is for 2024-27 and 10m comes from the 2025 research reserve. | chc.au.dk/...; di.ku.dk/... |
| Models | Open access, usable commercially | CONFIRMED | "can also be used for commercial purposes" | di.ku.dk/... |
| Models | Munin 1.0: 8B, post-trained from Apertus-8B and other open bases | CONFIRMED | "a Danish-focused text-only language model from the Munin 1.0 family"; base "swiss-ai/Apertus-8B-2509"; the collection lists "existing base models post-trained" | huggingface.co/danish-foundation-models/munin-apertus-8b |
| Models | Munin licence Apache-2.0 | CONFIRMED | Licence: Apache 2.0 | same |
| Models | DFM-Mimir trained from scratch, about 70B tokens, on SDU's cloud, Apache-2.0 | CONFIRMED | "trained from scratch"; "~70.5B"; "Trained on SDU UCloud"; "released under the Apache License 2.0" | huggingface.co/danish-foundation-models/DFM-Mimir |
| Models | Gefion: 1,528 H100, owned by DCAI, inaugurated 23 Oct 2024 | CONFIRMED | "1,528 NVIDIA H100 Tensor Core GPUs"; "owned and operated by the Danish Centre for AI Innovation A/S (DCAI)"; "Wednesday, 23rd of October" (page dated 24 Oct 2024) | escience.sdu.dk/.../gefion-inauguration/ |
| Models | Gefion is "privately funded" | NOT CONFIRMED | "funded by the Novo Nordisk Foundation and Export and Investment Fund of Denmark (EIFO)". EIFO is the state's investment fund, so "privately" does not match the page. | same |
| Strategy | DKK 740 million, 2024 to 2027 | CONFIRMED | "udmønte 740 mio. kr. i perioden 2024-2027" | digst.dk/.../strategier-for-kunstig-intelligens/ |
| Strategy | Strategic AI initiative within the digitalisation strategy | CONFIRMED | "Den strategiske indsats for kunstig intelligens skal udstikke en ambitiøs og ansvarlig retning"; 29 initiatives, two on AI | same |
| Strategy | Joint public-sector strategy 2026 to 2029, with responsible AI as a focus | CONFIRMED | "Den fællesoffentlige digitaliseringsstrategi for 2026-2029"; "kunstig intelligens på en ansvarlig måde" | digst.dk/.../den-faellesoffentlige-digitaliseringsstrategi/ |
| Public LLM | Børge, for borger.dk editors, since February 2025 | CONFIRMED | "Digitaliseringsstyrelsen lancerede i februar 2025 AI-assistenten Børge" | digst.dk/.../kommunikation-paa-borgerdk-... |
| Public LLM | Runs on Anthropic's Claude | CONFIRMED | "baseret på sprogmodellen Claude 3.5 Sonnet"; current model "claude-sonnet-4-5-20250929" | same |
| Public LLM | The model is replaceable | CONFIRMED | "nemt at udskifte" | same |
| Public LLM | AI services through the factories "probably from 2027" | CONFIRMED | "Inferens og drift af AI bliver en mulighed formentligt fra 2027." The note's "AI-as-a-service" is a paraphrase. | digst.dk/.../ai-fabrikker/ |
| Lang. resources | sprogteknologi.dk: 216 resources from 43 organisations, run by the agency | CONFIRMED | "216 sprogressourcer"; "43 forskellige organisationer"; "drives af" Digitaliseringsstyrelsen | sprogteknologi.dk |
| Lang. resources | Includes parliamentary documents and Danish Dynaword | CONFIRMED | "Folketingets dokumenter - træningsdata"; Danish Dynaword listed (21 Aug 2025) | same |
| Lang. resources | CLARIN-DK at the University of Copenhagen | CONFIRMED | "CLARIN-DK", "University of Copenhagen" | clarin.eu/content/participating-consortia |
| Key institutions | DeiC coordinates national HPC | CONFIRMED | "DeiC coordinates the use of the national supercomputers available to Danish researchers" | deic.dk/en |
| Key institutions | Centre for Language Technology at Copenhagen, in DFM | CONFIRMED | "Centre for Language Technology"; post-training and benchmark data for DFM | cst.ku.dk/... |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speaker counts and the German-border minority | NOT FOUND | A search found Council of Europe Framework Convention documents saying Denmark applies the Convention only to the German minority in South Jutland. The CoE PDF returned 403, so nothing was fetched. No speaker count found. | (rm.coe.int/6th-op-denmark-en/1680b05cee, 403) | – |
| Shared with | Faroese and Greenlandic | NOT FOUND | No official page fetched. | – | – |
| EuroHPC system | Absence of a system (EuroHPC DK page 404) | FOUND | EuroHPC lists 12 supercomputers, none in Denmark (Arrhenius is the only Nordic one besides LUMI). | https://eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en | List: JUPITER, LUMI, LEONARDO, MARENOSTRUM 5, MELUXINA, KAROLINA, VEGA, DISCOVERER, DEUCALION, DAEDALUS, ARRHENIUS, ALICE RECOQUE |
| Models | Munin 1.0 release date | FOUND | Munin 1.0 release note dated 11 June 2026. The page says the family is "post-trained on top of several best-in-class open models". | https://www.foundationmodels.dk/news/index.html | "Munin 1.0 release note" (June 11, 2026) |
| Strategy | December 2024 AI strategy text and figures | NOT FOUND | A search shows the "Strategisk indsats for kunstig intelligens" was presented on 2 Dec 2024. Press and parliamentary snippets give 61 to 62.5 mio. kr. for 2024-2027. The ft.dk PDFs return 403 to WebFetch and to curl, so no official figure was fetched. | (ft.dk/samling/20241/almdel/DIU/bilag/31/2949937.pdf, 403) | – |
| Power and grid | Grid and renewables | NOT FOUND | Not searched. The cited DeiC page says nothing on power. | – | – |

#### C. Prose flags
1. "a privately funded H100 cluster": the SDU page names EIFO, the state's investment fund, as a co-funder (see A).
2. "Its production assistant runs on an American model": confirmed (Claude Sonnet 4.5 at present).

### EE
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Population 1,369,995 (Eurostat 2025) | CONFIRMED | "1 369 995" | european-union.europa.eu/.../estonia_en |
| Languages | Estonian is the mother tongue of 67% (2021 census) | CONFIRMED | "Estonian is spoken as a mother tongue by 67%" | stat.ee/en/news/243-mother-tongues-spoken-estonia |
| Languages | 243 mother tongues | CONFIRMED | "243 different mother tongues are spoken in Estonia" | same |
| Shared with | Finnish is a close relative | NOT CONFIRMED | The cited TildeOpen card does not say this (it may sit under the cell's [unverified] marker; the marker's scope is ambiguous). | huggingface.co/TildeAI/TildeOpen-30b |
| Shared with | Estonian is among TildeOpen's 34 languages | CONFIRMED | The list includes "Estonian". The card's metadata says "32 languages", the text 34. | same |
| EuroHPC system | In the LUMI consortium through ETAIS | CONFIRMED | "Estonia already participates in the consortium operating the current LUMI supercomputer" (through ETAIS) | hpc.ut.ee/news/2026-09-01 |
| AI Factory | Partner state of the LUMI AI Factory | CONFIRMED | Partners: Czechia, Denmark, Estonia, Norway, Poland | eurohpc-ju.europa.eu/...lumi-ai-...-2026-08-31_en |
| AI Factory | Continued access to LUMI-AI from 2027 for researchers and public and private users | CONFIRMED | "Scheduled to become available to users in 2027"; researchers and the public and private sectors can "continue to compute" | hpc.ut.ee/news/2026-09-01 |
| AI Factory | No antenna | CONFIRMED (uncited page) | Estonia is absent from the Commission's antenna list of 13 Oct 2025 | digital-strategy.ec.europa.eu/en/news/eu-announces-ai-factories-antennas-... |
| Models | EstLLM by TartuNLP and TalTechNLP | CONFIRMED | "TartuNLP and TalTechNLP research groups" | huggingface.co/tartuNLP/Llama-3.1-EstLLM-8B-0525 |
| Models | Funded by the Ministry of Education and Research under the Language Technology Programme 2018 to 2027 | CONFIRMED | "Estonian Language Technology Program 2018-2027" | same |
| Models | 8B: continued pretraining of Llama 3.1, about 35B tokens, incl. 8.6B-token National Corpus | CONFIRMED | "approximately 35B tokens"; "Estonian National Corpus (8.6B tokens)" | same |
| Models | 70B-Instruct: about 60B tokens, then SFT and DPO | CONFIRMED | "on approximately 60B tokens"; "supervised fine-tuning and direct preference optimization were applied" | .../Llama-3.1-EstLLM-70B-Instruct-0826 |
| Models | Llama 3.1 licence | CONFIRMED | "Llama 3.1 Community License Agreement" | both cards |
| Models | Released 2025 to 2026 | UNCLEAR | Neither card states a release date. The 8B card's heading reads "0825" while its ID is "0525". | both cards |
| Models | Bürokratt roadmap: an Estonian-adapted LLM from 2026 | CONFIRMED | From 2026: "building an LLM adapted to Estonian" | kratid.ee/en/burokratt |
| Strategy | The portal names no current strategy document | CONFIRMED | No national AI strategy or action plan is named on either page | kratid.ee/en; kratid.ee/en/tehisintellekt |
| Public LLM | A network of chatbots that offers institutions LLMs; several institutions use it | CONFIRMED | "network of chatbots on public sector institutions' websites"; "offers institutions the ability to use large language models"; "Several public sector institutions already use Bürokratt" | kratid.ee/en/burokratt |
| Public LLM | "RIA's" network | UNCLEAR | The page names RIA as contact and as offering "support from the first demo to production". It does not say RIA operates the network. | same |
| Public LLM | Software free; hosting about EUR 150/month in the State Cloud, plus LLM usage | CONFIRMED | Hosting in the State Cloud at about €150 per month, plus LLM usage costs; software free | same |
| Public LLM | LLM and retrieval by end-2025 | CONFIRMED | By end of 2025: "deploying an LLM with retrieval (RAG)" | same |
| Lang. resources | CLARIN Estonia at the Centre of Estonian Language Resources | CONFIRMED | "CLARIN Estonia", "Center of Estonian Language Resources" | clarin.eu/content/participating-consortia |
| Key institutions | UT HPC Centre and ETAIS; RIA; Ministry of Justice and Digital Affairs | CONFIRMED | Both appear as contacts on kratid.ee; ETAIS appears on hpc.ut.ee | hpc.ut.ee; kratid.ee/en |
| Power | LUMI-AI will run on renewables | CONFIRMED | "The supercomputer will run entirely on renewable energy." | hpc.ut.ee/news/2026-09-01 |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Russian-speaking share | FOUND | 2021 census: 29% have Russian as their mother tongue | https://stat.ee/en/news/population-census-76-estonias-population-speak-foreign-language | "Russian is the next most widely spoken language, with 29% speaking it as their mother tongue" |
| Shared with | Diaspora | NOT FOUND | Not searched | – | – |
| EuroHPC system | Absence of a system | FOUND | No Estonian system in EuroHPC's list of 12 | https://eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en | (list as under DK) |
| AI Factory | Estonian contribution | NOT FOUND | A search surfaced a LUMI AIF launch presentation said to list "EE 5 M€". The PDF returned 404 twice, so it was not fetched. | (lumi-supercomputer.eu/content/uploads/2025/04/LUMI-AI-Factory-Launch-Manninen.pdf, 404) | – |
| Gigafactory | Up to EUR 20 million, 2028 to 2032, Nordic consortium, main site in Finland | FOUND (press; no ministry page fetched) | ERR (public broadcaster): up to €20m of AI computing services in 2028-2032, announced by the Ministry of Justice and Digital Affairs. Invest in Estonia (state agency): Estonia signed a cooperation agreement with Nokia to join a Nordic consortium (EE, FI, LV; SE and DK in negotiation), Dec 2025. **The cell's own source (LUMI about page) does not mention any of this; replace it.** | https://news.err.ee/1610102149/estonia-eyes-20-million-share-of-eu-s-10-billion-ai-computing-drive ; https://investinestonia.com/estonia-joins-nordic-ai-gigafactory-project/ | "The Estonian state plans to purchase services worth up to €20 million between 2028 and 2032"; "a cooperation agreement with Nokia to participate in a Nordic consortium" |
| Models | EstLLM compute | FOUND | Trained on LUMI on 16 to 32 nodes of AMD MI250X; about 100,000 GPU-hours across all experiments (developers' paper) | https://arxiv.org/pdf/2603.02041 | "Training was conducted on the LUMI Supercomputer with 16–32 nodes" |
| Strategy | AI and data action plan 2024 to 2026 | NOT FOUND (official) | Only secondary sources (regulations.ai, ERR) were seen. regulations.ai points to an mkm.ee release, which was not fetched. | – | – |
| Strategy | Eesti.ai programme, January 2026 | FOUND | Launched 27 January 2026 as "a nationally managed programme" led by an international council of entrepreneurs and experts. The page calls it a programme, not a strategy. | https://www.valitsus.ee/en/news/government-launched-eestiai-initiative-together-leading-entrepreneurs | "a nationally managed programme" |
| Lang. resources | Language Technology Programme budget | NOT FOUND | The search found only a 2025 single-year line (about EUR 1.53m) in a document-register mirror, not an official page | – | – |
| Power and grid | Estonian grid | NOT FOUND | Not searched | – | – |

#### C. Prose flags
1. "a third of residents have another mother tongue, mostly Russian": consistent with stat.ee (Estonian 67%, Russian 29%). It can now be sourced.
2. "a strategy document on the record": ERR reports a new state AI strategy due by year-end. This came from a search snippet only and was not fetched.

### FI
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Population 5,635,971; Finnish and Swedish | CONFIRMED | "5 635 971"; "Finnish, Swedish" | european-union.europa.eu/.../finland_en |
| Shared with | Swedish with Sweden | CONFIRMED | "Svenska är huvudspråk i Sverige." | riksdagen.se/.../spraklag-2009600 |
| Shared with | Finnish is a national minority language in Sweden (§7) | CONFIRMED | "De nationella minoritetsspråken är finska, jiddisch, meänkieli, romani chib och samiska." | same |
| EuroHPC system | LUMI at CSC's Kajaani data centre | CONFIRMED | "located in CSC's data center in Kajaani, Finland" | lumi-ai-factory.eu/computing-infrastructure/ |
| EuroHPC system | "Pre-exascale" | UNCLEAR | Neither cited page uses the term ("Europe's top-tier supercomputer") | both cited pages |
| EuroHPC system | 380 PFlops sustained | CONFIRMED | "The sustained computing power is 380 petaflops (HPL...)" | lumi-ai-factory.eu/computing-infrastructure/ |
| EuroHPC system | 11,912 AMD GPUs | CONFIRMED | "a total of 11 912 AMD GPU processors" | same |
| EuroHPC system | Eleven-country consortium | CONFIRMED | "hosted by the 11-country LUMI consortium" | same |
| EuroHPC system | Lifespan to 2027 | CONFIRMED | "for the lifespan of 2021–2027" | lumi-supercomputer.eu/about-lumi/ |
| EuroHPC system | LUMI-AI to replace it from H2 2027 | CONFIRMED | "LUMI-AI will gradually replace the current LUMI supercomputer"; "second half of 2027" | lumi-ai-factory.eu/computing-infrastructure/ |
| AI Factory | Selected 10 December 2024 | CONFIRMED (page cited under DK) | Published "10 December 2024", Finland "LUMI AI Factory" | eurohpc-ju.europa.eu/selection-first-seven-... |
| AI Factory | Hosted by CSC with CZ, DK, EE, NO, PL | CONFIRMED | "Hosted in Finland, at the CSC"; "Czechia, Denmark, Estonia, Norway, and Poland" | eurohpc-ju.europa.eu/finland_en |
| AI Factory | Bull, 31 Aug 2026, EUR 387.8m, 50% EuroHPC, MI430X, tenfold, users 2027 | CONFIRMED | "Bull, the selected vendor"; "EUR 387 800 000"; "fund 50%"; "AMD Instinct MI430X"; "a tenfold increase"; "made available to users in 2027" | eurohpc-ju.europa.eu/...2026-08-31_en |
| AI Factory | Language among the key sectors | CONFIRMED | finland_en lists "Language" among the key sectors. The 2026 contract release lists language only among other user communities. | eurohpc-ju.europa.eu/finland_en |
| AI Factory | Antennas in Iceland, Latvia and Switzerland | NOT CONFIRMED | None of the three cited pages mentions antennas. The Commission antenna page lists LV, IS and CH but does not say which factory each joins. Latvia's link to LUMI AIF is confirmed by izm.gov.lv (cited under LV). **This conflicts with the SE row, which attaches Switzerland's antenna to the Sweden AI Factory.** | contract, finland_en, csc.fi (cited); digital-strategy.ec.europa.eu antenna page |
| Gigafactory | The government backed a Nokia-led consortium's expression of interest (July 2025) | CONFIRMED | "formally announced its backing for a plan by a business consortium led by Nokia" (Yle, 6 July 2025) | yle.fi/a/74-20171278 |
| Gigafactory | Finland submitted two projects | CONFIRMED | "Finland has submitted two projects." | em.gov.lv/... |
| Gigafactory | No selection yet | UNCLEAR | Neither cited page (both 2025) speaks to the current status. ERR (Aug 2026) and Ritzau (31 Jul 2026) say bids are due in November or the decision comes later in the year, which is consistent. | – |
| Models | Poro 34B: SiloGen with TurkuNLP and HPLT; 1T tokens of Finnish, English and code; LUMI on CSC compute; Apache-2.0; 2024 | CONFIRMED | "1 trillion tokens"; "Finnish, English and code"; credits CSC; Apache 2.0; paper 2 Apr 2024 | huggingface.co/LumiOpen/Poro-34B |
| Models | Viking: Nordic languages plus English and code, 2T tokens on LUMI, Apache-2.0 | CONFIRMED | "being trained on 2 trillion tokens"; LUMI; "Apache 2.0 License". The 7B size was not checked (only the 33B card was fetched). | huggingface.co/LumiOpen/Viking-33B |
| Models | FinGPT used with Poro in ministry pilots | CONFIRMED | "further training in Finnish language models (including FinGPT, Poro) with legislative texts" | sitra.fi/... |
| Strategy | AI 4.0, Ministry of Economic Affairs and Employment, 2022, actions to 2030 | CONFIRMED | "Actions for period 2022-2030" | digital-skills-jobs.europa.eu/.../finland-... |
| Public LLM | Sitra pilots December 2023 to June 2024 | CONFIRMED | Schedule "01.12.2023 — 30.06.2024". The same page also says "Projects ended in August 2024". | sitra.fi/... |
| Public LLM | Ministry of Transport, PM's Office, Ministry of Justice | CONFIRMED | Transport and Communications ran the drafting pilot; the PMO and Justice ran the consultation pilot | same |
| Lang. resources | Kielipankki coordinated by FIN-CLARIN (University of Helsinki) | CONFIRMED | "The Language Bank is coordinated by the national FIN-CLARIN consortium"; CLARIN lists FIN-CLARIN as led by the "University of Helsinki" | kielipankki.fi; clarin.eu |
| Lang. resources | CSC as technical operator | UNCLEAR | The page names CSC only for "technical support" and in the copyright line | kielipankki.fi/language-bank/ |
| Key institutions | CSC is a state- and university-owned non-profit | CONFIRMED | "owned by the Finnish Government and Finnish higher education institutions"; "non-profit limited liability company" | csc.fi/en/about-us/ |
| Key institutions | Aalto and the ELLIS Institute as the training hub | CONFIRMED | "on grounds of Aalto University, together with ELLIS Institute" | eurohpc-ju.europa.eu/finland_en |
| Power | 100% renewable electricity | CONFIRMED | "LUMI's energy consumption is covered by 100% renewable electricity." | lumi-supercomputer.eu/sustainable-future/ |
| Power | Waste heat warms Kajaani households | CONFIRMED | "used to heat up hundreds of households annually in the city of Kajaani" | same |
| Power | Up to 230 MW | CONFIRMED | "a ready-built electrical infrastructure of up to 230 MW" | same |
| Power | LUMI-AI entirely on renewables | CONFIRMED | "The supercomputer will run entirely on renewable energy." | hpc.ut.ee/news/2026-09-01 |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Status of Sámi | FOUND | The Sámi Language Act (1086/2003) gives Sámi people the right to use Sámi with public authorities, centred on the Sámi homeland (Inari, Enontekiö, Utsjoki, northern Sodankylä) | https://samediggi.fi/en/areas-of-expertise/sami-languages/the-sami-language-act/ | "Sámi people have the right to use either Finnish or Sámi when dealing with public authorities." |
| Languages | Speaker counts | NOT FOUND | Not searched beyond the Sámi page, which gives no count | – | – |
| Shared with | Estonian affinity | NOT FOUND | Not searched | – | – |
| Gigafactory | The government's own release | NOT FOUND | The search found valtioneuvosto.fi/en/-/1410877 (dated 4.7.2025 in snippets), but both language versions return 403 (a Cloudflare wall, also to curl) | (valtioneuvosto.fi/en/-/1410877/..., 403) | – |
| Models | Poro 2 | FOUND | Llama-Poro-2-70B: continued pretraining of Llama 3.1 70B on 165B tokens (Finnish, English, code, math), by AMD Silo AI, TurkuNLP and HPLT, on LUMI, under the **Llama 3.3 Community License** (not Apache) | https://huggingface.co/LumiOpen/Llama-Poro-2-70B-Instruct | "165B tokens of Finnish, English, code, and math data" |
| Models | AMD's acquisition of Silo AI | FOUND | AMD completed the acquisition on 12 Aug 2024, all cash, about USD 665 million | https://ir.amd.com/news-events/press-releases/detail/1210/amd-to-acquire-world-labs-to-advance-the-future-of-ai-compute (the page carries the Silo AI release despite its slug) | "today announced the completion of its acquisition of Silo AI, the largest private AI lab in Europe" |
| Models | FinGPT's developer | FOUND | FinGPT is seven monolingual Finnish models (186M to 13B) by the TurkuNLP Group, University of Turku, with Hugging Face, the National Library of Finland and AMD co-authors (EMNLP 2023) | https://huggingface.co/papers/2311.05640 | "we train seven monolingual models from scratch (186M to 13B parameters) dubbed FinGPT" |
| Strategy | Successor to AI 4.0 | NOT FOUND | Not searched | – | – |
| Public LLM | Government-wide platform | NOT FOUND | Not searched. The Sitra page names demo services by Futurice and SiloGen only. | – | – |

#### C. Prose flags
1. "the company's ownership could not be confirmed": now confirmed. AMD completed the acquisition of Silo AI on 12 Aug 2024 (B above). Poro 2 also moved to a Llama 3.3 licence, which bears on recommendation 1 (Apache-2.0).
2. "Finland hosts Europe's largest AI-capable public system": not supported by any fetched page. EuroHPC's list includes JUPITER (Germany), so this needs a source or softer wording.
3. "Three ministries fine-tuned Poro on legislative text in 2024": the Sitra page describes two pilots run by three bodies (one is the Prime Minister's Office, not a ministry). They trained "FinGPT, Poro", with demo services built by contractors.

### LV
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Population 1,856,932; Latvian | CONFIRMED | "1 856 932"; "Latvian" | european-union.europa.eu/.../latvia_en |
| Languages | TildeOpen used 29 billion words of Latvian | CONFIRMED | "For Latvian alone, 29 billion words were used" | researchlatvia.gov.lv/... |
| Shared with | Latvian among TildeOpen's 34 languages | CONFIRMED | List includes Latvian | huggingface.co/TildeAI/TildeOpen-30b |
| EuroHPC system | Latvia not in the LUMI consortium | CONFIRMED | Latvia is absent from the 11-country list | lumi-supercomputer.eu/about-lumi/ |
| AI Factory | AIFA-LAT, led by RTU with UL, the SDDA and others | CONFIRMED | "AI Factory Antenna – Latvia" (AIFA-LAT); Riga Technical University lead | izm.gov.lv/... |
| AI Factory | EUR 8.4m, 2026 to 2028, EUR 3.98m national co-funding | CONFIRMED | "8.4M EUR million"; "3.98M EUR million in national co-funding" | same |
| AI Factory | Linked to the LUMI AI Factory | CONFIRMED | Latvia would join the LUMI AI Factory consortium | same |
| AI Factory | National AI competence centre; language technologies niche; "several million AI training hours for the public sector" | CONFIRMED | "national AI competence centre"; "Language technologies"; "several million AI training hours for the public sector" | same |
| Gigafactory | 8 Oct 2025: DataCrunch with Latvian ICT companies, renewable-powered | CONFIRMED | "Published: 08.10.2025."; "in collaboration with major Latvian information and communication technology companies"; "powered by renewable (green) energy" | em.gov.lv/... |
| Gigafactory | Second Latvian project; possible joint LV-FI bid | CONFIRMED | "Latvia has also submitted another project"; "Latvia and Finland could jointly submit" | same |
| Models | TildeOpen 30B dense, 34 languages incl. Baltic and Nordic, 2T tokens | CONFIRMED | "A 30B parameter dense decoder-only transformer"; "across 2 trillion tokens" | huggingface.co/TildeAI/TildeOpen-30b |
| Models | On LUMI with 768 MI250X, under the Large AI Grand Challenge | CONFIRMED | "768 AMD MI250X GPUs"; "EuroHPC JU Large AI Grand Challenge" | same |
| Models | CC-BY-4.0 | CONFIRMED | Licence CC-BY-4.0 | same |
| Models | Released September 2025 | CONFIRMED | Release article dated "September 3, 2025" | tilde.ai/?p=20213 |
| Models | Long-context update April 2026 | CONFIRMED | "TildeOpen will henceforth process 8 times larger text volumes" (28 Apr 2026) | tilde.ai/?p=26124 |
| Models | "Not a ready-made chatbot" | CONFIRMED | "this is not a ready-made chatbot or an end-user solution" | same |
| Models | No Latvian government role described | CONFIRMED | "commissioned by the European Commission and developed by the Latvian company Tilde" | researchlatvia.gov.lv/... |
| Strategy | AI Centre Law adopted 6 March 2025 | CONFIRMED | "Artificial Intelligence Centre Law"; adopted "on Thursday, 6 March" (release 07.03.2025) | saeima.lv/... |
| Strategy | Founders: the environment, economics and defence ministries | NOT CONFIRMED | The founders are "the Ministry of Smart Administration and Regional Development (VARAM)", the Ministry of Economics and the Ministry of Defence. VARAM is no longer the environment ministry. | same |
| Strategy | Oversight by the SDDA | CONFIRMED | "oversight provided by the State Digital Development Agency" | same |
| Public LLM | Microsoft memorandum (3 Dec 2024), national AI centre, first pilot in LIAA | CONFIRMED | "Memorandum of Understanding with Microsoft"; "develop a National Center for Artificial Intelligence"; "pilot project to integrate AI solutions into LIAA's processes" | varam.gov.lv/... |
| Lang. resources | CLARIN-LV at IMCS UL, B-centre since 2023, recovery-plan language-technology initiative | CONFIRMED | "pirmo reizi iegūst B-centra statusu" (Jan 2023); "Valodu tehnoloģiju iniciatīva" | clarin.lv |
| Lang. resources | korpuss.lv incl. a 403.6M-word web corpus | CONFIRMED | "Latvian National Corpora Collection"; Tīmeklis2020 "403.6M words" | korpuss.lv/en |
| Key institutions | Tilde; IMCS; RTU; AI Centre; SDDA; VARAM | CONFIRMED | Named across clarin.lv and izm.gov.lv | as cited |
| Power | The Gigafactory proposal speaks of renewable energy | CONFIRMED | "powered by renewable (green) energy" | em.gov.lv/... |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Census speaker shares | FOUND (survey, not census) | Adult Education Survey 2022 (ages 18-69): Latvian is the mother tongue of 64.3% and Russian of 37.7%; 62.0% use Latvian at home | https://stat.gov.lv/en/statistics-themes/education/level-education/press-releases/21052-mother-tongue-and-language-used | "Latvian for 64.3 % of the inhabitants" |
| Shared with | Official page | NOT FOUND | Not searched | – | – |
| EuroHPC system | Absence of a system | FOUND | No Latvian system in EuroHPC's list of 12 | https://eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en | (list as under DK) |
| Gigafactory | Status under the formal call | NOT FOUND | Invest in Estonia (Dec 2025) lists Latvia in the Nokia-led Nordic consortium with EE and FI, but nothing official on the formal-call status | https://investinestonia.com/estonia-joins-nordic-ai-gigafactory-project/ | "Estonia, Finland, and Latvia are currently included" (paraphrased by the fetcher) |
| Strategy | The 2020 report | FOUND | "Developing artificial intelligence solutions" ("Par mākslīgā intelekta risinājumu attīstību"), released by the Latvian Government in February 2020 | https://ai-watch.ec.europa.eu/countries/latvia-0/latvia-ai-strategy-report_en | "Par mākslīgā intelekta risinājumu attīstību" |
| Strategy | Digital guidelines | NOT FOUND | Not fetched | – | – |
| Public LLM | hugo.gov.lv | NOT FOUND | Page title "Tulkot tekstu \| Hugo.gov.lv"; content loads only by JavaScript | https://hugo.gov.lv/ | – |
| Key institutions | HPC centre | NOT FOUND | One search, no official page | – | – |
| Power | Grid data | NOT FOUND | Not searched | – | – |

#### C. Prose flags
1. "the largest open model built on a EuroHPC system for the Baltic languages": a superlative no fetched page supports. Needs a source or softer wording.
2. "a large Russian-speaking population": consistent with CSB (37.7% Russian mother tongue, ages 18-69). It can now be sourced.

### LT
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Population 2,890,664; Lithuanian | CONFIRMED | "2 890 664"; "Lithuanian" | european-union.europa.eu/.../lithuania_en |
| Shared with | Lithuanian among TildeOpen's languages | CONFIRMED | List includes Lithuanian | huggingface.co/TildeAI/TildeOpen-30b |
| EuroHPC system | None yet; not in the LUMI consortium | CONFIRMED | Lithuania is absent from the LUMI list; lithuania_en names no system | lumi about; eurohpc lithuania_en |
| EuroHPC system | The LitAI system will be the first EuroHPC-co-funded machine on Lithuanian soil | NOT CONFIRMED | lithuania_en "doesn't say whether this would be the first". (The Commission DSJ news title says "first artificial intelligence centre", which is a different claim.) | eurohpc-ju.europa.eu/lithuania_en |
| AI Factory | LitAI selected 10 October 2025 | CONFIRMED | Published "10 October 2025"; "LitAI Factory" | eurohpc-ju.europa.eu/...six-additional-ai-factories-...-2025-10-10_en |
| AI Factory | Led by VU at LRTC VDC3 with three other universities, the State Data Agency, LRTC, the Innovation Agency | CONFIRMED | "upgrade-ready LRTC VDC3 data center facility in Vilnius"; KTU, VILNIUS TECH, VMU, State Data Agency, LRTC, Innovation Agency | eurohpc-ju.europa.eu/lithuania_en |
| AI Factory | "A sovereign AI optimised infrastructure" | CONFIRMED | "transform Lithuania's HPC capabilities into a sovereign AI optimised infrastructure" | same |
| AI Factory | The university puts the value at around EUR 130m | CONFIRMED | "The project's estimated value is around EUR 130 million" | ff.vu.lt/... |
| AI Factory | Timeline not stated | NOT CONFIRMED | The EuroHPC selection release says the six factories are "set to be deployed next year" (2026) | eurohpc-ju.europa.eu/...2025-10-10_en |
| Gigafactory | Lithuania was a partner in Poland's Baltic AI GigaFactory EoI | CONFIRMED | "Polska wspólnie z Estonią, Litwą i Łotwą" (20.06.2025) | gov.pl/web/cyfryzacja/... |
| Models | Neurotechnology, Aug 2024, Llama 2 7B and 13B, over 14B Lithuanian tokens | CONFIRMED | "August 27, 2024"; "LlamaV2 7 and 13 billion parameter"; "more than 14 billion tokens in Lithuanian" | neurotechnology.com/... |
| Models | "The first open Lithuanian LLMs" | NOT CONFIRMED (wording) | The page says "its first open-source large language model (LLM) customized for the Lithuanian language", that is, the company's first, not the first in Lithuania | same |
| Models | Licence and funder not stated (on that page) | CONFIRMED | Neither is stated on the press release (the HF card states the licence; see B) | same |
| Models | Guidelines cite preservation of Lithuanian and name no model | CONFIRMED | "preservation of the Lithuanian language and cultural identity"; no model mentioned | digital-skills-jobs.europa.eu/.../lithuania-... |
| Strategy | Guidelines 2026 to 2035; Ministry of the Economy and Innovation with the Innovation Agency, the State Digital Solutions Agency and the GovAI centre | CONFIRMED | "National Artificial Intelligence Strategic Guidelines for 2026–2035" | same |
| Strategy | Adopted in 2026 | CONFIRMED | Adoption year 2026 | same |
| Strategy | Four strands including infrastructure, data, compute, state cloud | CONFIRMED (wording loose) | Four strands; the second, "technological infrastructure and data", covers "state cloud solutions, high-speed computing capabilities" | same |
| Strategy | Action plan to follow | CONFIRMED | The Innovation Agency will "develop a concrete action plan" | same |
| Public LLM | GovAI centre co-launched the guidelines | CONFIRMED | GovAI Competence Center listed as a partner | same |
| Lang. resources | CLARIN-LT at VMU | CONFIRMED | "CLARIN-LT", "Vytautas Magnus University" | clarin.eu |
| Lang. resources | raštija.lt, VU, 10,000-hour annotated speech corpus | CONFIRMED | "© Vilniaus universitetas"; "Bendra anotuota garsyno trukmė yra 10 000 val." | xn--ratija-ckb.lt |
| Key institutions | VU, KTU, VILNIUS TECH, VMU, LRTC, State Data Agency, Innovation Agency | CONFIRMED | As listed on lithuania_en | eurohpc-ju.europa.eu/lithuania_en |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Census speaker shares | NOT FOUND | osp.stat.gov.lt 2021 census page returned 403. Secondary sources give about 85.3% Lithuanian, 6.8% Russian and 5.1% Polish native speakers; not used. | (osp.stat.gov.lt/en/2021-gyventoju-ir-bustu-surasymo-rezultatai/tautybe-gimtoji-kalba-ir-tikyba, 403) | – |
| Shared with | Official page | NOT FOUND | Not searched | – | – |
| AI Factory | EU share: EUR 65m (press) vs EUR 90m (Commission platform) | FOUND | The Commission's Digital Skills and Jobs platform (Ministry news, updated 22 Jan 2026) gives **EUR 65 million**, 50% of EUR 130m. EUR 90m does not appear on it. **The "EUR 90 million by the Commission platform" in the cell is contradicted.** | https://digital-skills-jobs.europa.eu/en/latest/news/eimin-lithuania-wins-eu65-million-eu-competition-first-artificial-intelligence-centre | "a total project value of 130 million euros"; "50% co-financing for the project will be provided by the EuroHPC Joint Undertaking" |
| Gigafactory | Joint proposal with Poland | NOT FOUND (official) | A search shows bne IntelliNews (8 Jul 2026): joint procurement agreement signed 7 Jul 2026 after a Jan 2026 MoU. The page returned 403, and eimin.lrv.lt returns 403. | (intellinews.com/...-453441/, 403) | – |
| Models | No public national model programme | NOT FOUND | No programme found. Absence was not confirmed on an official page. | – | – |
| Strategy | Adoption act | NOT FOUND | The ministry PDF and news pages on eimin.lrv.lt return 403 | – | – |
| Public LLM | Pilots and procurements | NOT FOUND | Not searched further | – | – |
| Power | Grid | NOT FOUND | Not searched | – | – |
| (extra) Models | Neurotechnology licence (cell says "not stated") | FOUND | Llama 2 Community License | https://huggingface.co/neurotechnology/Lt-Llama-2-13b-hf | "Llama2 Community License Agreement" |

#### C. Prose flags
1. "a factory of its own ... with a national strategy adopted the same year": LitAI was selected in October 2025 and the guidelines were adopted in 2026, so these are not the same year.
2. "the factory arrives before the model it should train": EuroHPC said the six factories are "set to be deployed next year" (2026). No later date was fetched.

### SE
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Swedish is the principal language (§4) | CONFIRMED | "Svenska är huvudspråk i Sverige." | riksdagen.se/.../spraklag-2009600 |
| Languages | Minority languages Finnish, Yiddish, Meänkieli, Romani Chib, Sámi (§7) | CONFIRMED | "De nationella minoritetsspråken är finska, jiddisch, meänkieli, romani chib och samiska." | same |
| Languages | Swedish Sign Language protected (§9) | CONFIRMED | "särskilt ansvar för att skydda och främja det svenska teckenspråket" | same |
| Languages | Population 10,587,710 | CONFIRMED | "10 587 710" | european-union.europa.eu/.../sweden_en |
| Shared with | Swedish is official in Finland | CONFIRMED | "Finnish, Swedish" | .../finland_en |
| Shared with | Mutually intelligible with Danish and Norwegian | NOT CONFIRMED | Neither cited page says so | finland_en; Viking-33B |
| Shared with | A training language of Viking | CONFIRMED | "...Swedish, Danish, Norwegian, Icelandic and code" | Viking-33B |
| EuroHPC system | Arrhenius at Linköping University, mid-range, over 60 PFlops | CONFIRMED | "hosted by Linköping University"; "a mid-range supercomputer"; "more than 60 petaflops" | eurohpc-ju.europa.eu/...arrhenius...2026-09-08_en |
| EuroHPC system | EUR 68.5m, EuroHPC up to 35% | CONFIRMED | "estimated total value for Arrhenius is EUR 68.5 million"; "co-fund up to 35%" | .../arrhenius-supercomputer-2025-07-10_en |
| EuroHPC system | Inaugurated 8 September 2026 | CONFIRMED | Release of 8 Sep 2026, "ribbon-cutting ceremony" | .../2026-09-08_en |
| EuroHPC system | Sweden is in the LUMI consortium | CONFIRMED (uncited page) | Sweden is in the about-lumi list | lumi-supercomputer.eu/about-lumi/ |
| AI Factory | Sweden AI Factory, formerly MIMER | CONFIRMED | "Mimer AI Factory becomes Sweden AI Factory" (24 Aug 2026) | naiss.se/?p=6302 |
| AI Factory | Selected 10 December 2024 | CONFIRMED (page cited under DK) | "MIMER" in the 10 Dec 2024 list | eurohpc-ju.europa.eu/selection-first-seven-... |
| AI Factory | Hosted by NAISS at Linköping with RISE | CONFIRMED | "hosted by NAISS in partnership with RISE Research Institutes" | eurohpc-ju.europa.eu/sweden_en |
| AI Factory | Bull, 21 April 2026, EUR 29.76m, 50% EuroHPC, 50% Swedish Research Council | CONFIRMED | "Bull, the selected vendor"; "EUR 29 760 000"; "fund 50% of the total cost" | .../ai-optimised-supercomputer-sweden-2026-04-21_en |
| AI Factory | Online in 2027 | CONFIRMED | "is expected to come online in 2027" (the contract page itself says only "installation ... will start in 2026") | eurohpc-ju.europa.eu/sweden_en |
| AI Factory | Services since April 2025 | CONFIRMED | Services available from "April 2025" | same |
| AI Factory | Over 230 clients by October 2026 | CONFIRMED | "has helped more than 230 clients" (NAISS, 24 Aug 2026: "more than 200 organisations"). Two fetches of sweden_en returned different detail; re-check mechanically. | same |
| AI Factory | Switzerland's antenna attaches to it | NOT CONFIRMED | None of the cited pages mentions antennas or Switzerland. This conflicts with the FI row. | sweden_en; contract; naiss |
| Models | GPT-SW3 by AI Sweden with RISE and WASP | CONFIRMED | "developed by AI Sweden in collaboration with RISE and the WASP WARA for Media and Language" | gpt-sw3-40b |
| Models | Up to 40B, 320B tokens of SV, NO, DA, IS, EN and code | CONFIRMED | "320B tokens in Swedish, Norwegian, Danish, Icelandic, English, and programming code" | same |
| Models | Open release Nov 2023, Vinnova funding | CONFIRMED | Dated 16 Nov 2023; "with funding from Vinnova" | ai.se/en/news/open-release-... |
| Models | Modified RAIL; Nordic-affiliated users; licensor may change terms | CONFIRMED | "modified Responsible AI License (RAIL)"; "be affiliated with a Nordic company, university, or public sector organization"; "can be changed by the Licensor from time to time" | gpt-sw3-20b-instruct LICENSE |
| Models | The 40B card is for research only | CONFIRMED | "You agree to use the model for research purposes only." | gpt-sw3-40b |
| Models | Svea's second stage includes fine-tuning open models and training some from scratch | NOT CONFIRMED | Stage 2 brings "new language models, transcription, and specialized chats". Fine-tuning and from-scratch training are discussed as what Sweden needs, not as Stage 2 work. | ai.se/en/news/organizations-participating-svea-... |
| Strategy | Published 20 February 2026 | CONFIRMED | Published 20 Feb 2026 (updated 26 Feb) | regeringen.se/.../sveriges-ai-strategi/ |
| Strategy | Top-ten ambition | CONFIRMED | "Sverige ska vara bland de tio främsta nationerna inom artificiell intelligens (AI) i världen." | same |
| Strategy | Language models named as a research strength | CONFIRMED | "världsledande forskning inom maskininlärning, språkmodeller, datorseende och AI-säkerhet" | same |
| Strategy / Power | Fossil-free electricity as an asset for compute | CONFIRMED | "god tillgång till fossilfri el och gynnsamt klimat för infrastruktur för beräkningskraft" | same |
| Public LLM | Svea: over 60 municipalities, regions and agencies | CONFIRMED | "over 60 municipalities, regions, and government agencies" (the Stage 2 text says 55) | ai.se/.../svea |
| Public LLM | 1,500 public employees use it weekly | CONFIRMED | "1,500 public sector employees use the chatbot prototype Svea every week" | same |
| Public LLM | Permanent national generative-AI service targeted in 2026 | CONFIRMED | "establishing a permanent, national service for generative AI" (in 2026) | same |
| Public LLM | Funder not named | CONFIRMED | No funder named (technology partners Airon, Intel) | same |
| Lang. resources | Språkbanken Text at GU, national language-data infrastructure | CONFIRMED | "a part of Språkbanken, a national e-infrastructure". Note: the page says the unit will be called "Språkbanken at the University of Gothenburg", not Språkbanken Text. | spraakbanken.gu.se/en |
| Lang. resources | SWE-CLARIN lead | CONFIRMED | "SWE-CLARIN", led by "Språkbanken" | clarin.eu |
| Key institutions | AI Sweden is the national applied-AI centre | CONFIRMED | "Sweden's national center for applied artificial intelligence" | ai.se/en/about-ai-sweden |
| Key institutions | Berzelius: A100 and H200, donated by the Wallenberg foundation; NSC | CONFIRMED | "donated to NSC by the Knut and Alice Wallenberg foundation in 2020"; A100 and "H200 141GB" | nsc.liu.se/systems/berzelius/ |
| Power | Arrhenius 24th on the Green500 | CONFIRMED | "placing it 24th in the latest Green500 list" | .../2026-09-08_en |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speaker counts | NOT FOUND | Not searched | – | – |
| Gigafactory | No official Swedish page | NOT FOUND | One search: no Swedish government EoI or bid found | – | – |
| Strategy | The action plan | FOUND | A "Handlingsplan för Sveriges AI-strategi" accompanies the strategy, listing decided and planned measures, most decided in 2025 | https://www.regeringen.se/informationsmaterial/2026/02/sveriges-ai-strategi/ | "Handlingsplan för Sveriges AI-strategi" |
| Power | Grid-connection constraints | FOUND | Svenska kraftnät's grid development plan 2026-2035 says capacity reinforcement in all three regions is driven by connection requests, and lists new server halls among drivers of demand to 2050 | https://www.svk.se/4977e3/siteassets/om-oss/rapporter/natutvecklingsplanen-2026-2035/svk_natutveckling_nup_2026-2035.pdf | "I alla tre regionerna drivs behovet av kapacitetsförstärkningar av anslutningsförfrågningar" |

#### C. Prose flags
1. "Svea's second stage already fine-tunes open models": not what the page says (see A).
2. "the strategy's action plan could not be confirmed" (main blocker): the action plan exists on the strategy page (B above). Its funding of Svea was not checked.
3. "the factory's system from 2027": confirmed by sweden_en.

### Summary
| State | Claims checked | Confirmed | Not confirmed | Unclear | Unverified cells | Found | Not found |
|---|---|---|---|---|---|---|---|
| DK | 33 | 31 | 2 | 0 | 6 | 2 | 4 |
| EE | 24 | 21 | 1 | 2 | 10 | 5 | 5 |
| FI | 32 | 28 | 1 | 3 | 9 | 4 | 5 |
| LV | 25 | 24 | 1 | 0 | 9 | 3 | 6 |
| LT | 22 | 19 | 3 | 0 | 8 (+1 extra) | 1 (+1 extra) | 7 |
| SE | 38 | 35 | 3 | 0 | 4 | 2 | 2 |
| Total | 174 | 158 | 11 | 5 | 46 | 17 | 29 |

#### NOT CONFIRMED
1. DK, Language shared with: "mutually intelligible with Norwegian and Swedish". The cited HF cards do not say this.
2. DK, Models: Gefion "privately funded". SDU says it is funded by the Novo Nordisk Foundation and EIFO, the state's fund.
3. EE, Language shared with: "Finnish is a close relative". The cited TildeOpen card is silent.
4. FI, AI Factory: "antennas in Iceland, Latvia and Switzerland". No cited page mentions antennas. This also conflicts with SE's "Switzerland's antenna attaches to it".
5. LV, Strategy: AI Centre founders given as "the environment, economics and defence ministries". The Saeima release names VARAM as the Ministry of Smart Administration and Regional Development.
6. LT, EuroHPC system: LitAI's machine "will be the first EuroHPC-co-funded machine on Lithuanian soil". The cited page does not say so.
7. LT, AI Factory: "timeline not stated". EuroHPC says the factories are "set to be deployed next year" (2026).
8. LT, Models: Neurotechnology's are "the first open Lithuanian LLMs". The page says "its first", meaning the company's first.
9. SE, Language shared with: "mutually intelligible with Danish and Norwegian". The cited pages are silent.
10. SE, AI Factory: "Switzerland's antenna attaches to it". No cited page says so.
11. SE, Models: Svea's second stage "includes fine-tuning open models and training some from scratch". The page presents this as what Sweden needs, not as Stage 2 work.

Also contradicted in Task B:
- LT: "EUR 90 million by the Commission platform". The Commission DSJ page says EUR 65 million (50% of EUR 130m).
- EE: the Gigafactory cell cites the LUMI about page, which does not mention it. The fact is in ERR (press).

## Review: France, Iberia, Italy and Malta (FR, IT, MT, PT, ES), 2026-10-10

Tools: WebSearch available yes; about 95 URLs fetched (WebFetch, plus curl/pdftotext for four PDFs and one bot-blocked page); 17 failed (403: enseignementsup-recherche.gouv.fr, info.gouv.fr, economie.gouv.fr, mdia.gov.mt, two gov.mt pages, nso.gov.mt; connection refused: idris.fr; 401/404: two Hugging Face iGenius URLs, an OSOR-style francophonie.org guess, eurydice, cplp.org id page, an ACL preview; empty: diariodarepublica.pt; JS-only: fedlex.admin.ch). Every non-press URL cited in the five snapshots was reachable. The press-only URLs (Presse-Citron, Fortune Italia, Corriere Comunicazioni, ECO, DPL News, Bolsamania) support only **[unverified]** items and were not fetched for Task A.

Method note: a claim is judged against the URLs cited **in its own row**. Where a row's own pages are silent but another URL cited elsewhere in the same entry supports the claim, it is marked CONFIRMED with "(other row's URL)".

### FR
#### A. Verification
| Row | Claim | Verdict | Evidence (quote ≤25 words, or what the page says) | URL |
|---|---|---|---|---|
| Languages | French is the language of the Republic (art. 2) | CONFIRMED | "La langue de la République est le français." | conseil-constitutionnel.fr (Constitution) |
| Languages | Regional languages are national heritage (art. 75-1) | CONFIRMED | "Les langues régionales appartiennent au patrimoine de la France." | conseil-constitutionnel.fr |
| Languages | Population 68,882,600, 1 Jan 2025 | CONFIRMED | Eurostat JSON value index FR = 68882600 | ec.europa.eu/eurostat demo_pjan |
| Languages | "provisional" | CONFIRMED | status {"1":"p"}: FR (index 1) flagged p = provisional | Eurostat demo_pjan |
| Shared with | French official in Belgium and Luxembourg | NOT CONFIRMED | Only cited URL is Italy's Law 482/1999; it says nothing about Belgium or Luxembourg (no source for this half of the claim) | normattiva.it 482~art2 |
| Shared with | French protected as minority language in Italy (Law 482/1999) | CONFIRMED | "…e di quelle parlanti il francese, il franco-provenzale, il friulano, il ladino, l'occitano e il sardo" | normattiva.it 482~art2 |
| EuroHPC system | Alice Recoque, exascale, at CEA's TGCC | CONFIRMED | "Alice Recoque will be located at CEA's supercomputing centre TGCC" | eurohpc-ju our-supercomputers |
| EuroHPC system | Jules Verne consortium, GENCI and CEA with SURF and GRNET | CONFIRMED | "operated by the Jules Verne consortium, led by France through" GENCI and CEA "with the participation of the Netherlands through SURF and Greece through GRNet" | our-supercomputers |
| EuroHPC system | Eviden XH3500 | CONFIRMED | "Its architecture will be based on the new Eviden Sequana XH3500 platform." | our-supercomputers |
| EuroHPC system | About 1 EFlops expected | CONFIRMED | "1 exaflops* Sustained performance" (*Expected performance) | our-supercomputers |
| EuroHPC system | "details to be announced mid 2026" | CONFIRMED | "Final composition and details to be announced mid 2026." | our-supercomputers |
| EuroHPC system | Jean Zay (IDRIS), Adastra (CINES), Joliot-Curie (TGCC) carry interim access | CONFIRMED | "Jean Zay at IDRIS (CNRS), Adastra at CINES (France Universités), and Joliot-Curie at TGCC (CEA)" | eurohpc-ju additional AI Factories 2025-03-12 |
| AI Factory | AI2F selected 12 March 2025 | CONFIRMED (other row's URL) | Date "12 March 2025" on the additional-factories release; the France factory page itself gives no date | eurohpc-ju 2025-03-12 release |
| AI Factory | Led by GENCI with CEA, CINES, CNRS, Inria, Station F and others | CONFIRMED | "led by the French Hosting Entity GENCI … AMIAD, CEA, Cines, CNRS … Inria, The French Tech, Station F, and HubFranceIA" | 2025-03-12 release; ai-factories/france_en |
| AI Factory | Services from second half of 2025 on existing systems | CONFIRMED | "From the second half of 2025" | ai-factories/france_en |
| AI Factory | Relies on Alice Recoque from 2026 | CONFIRMED | "before the availability in 2026 of Alice Recoque, the 2nd European EuroHPC Exascale system" | france_en |
| AI Factory | Public AI investment EUR 2.8 billion | CONFIRMED | "with a public investment of 2.8 B€" | france_en |
| AI Factory | Planned 50,000-GPU federation with Germany's exascale system | CONFIRMED | "federate our EuroHPC' two exascale systems toward a virtual supercomputer of 50 000 GPUs" | france_en |
| AI Factory | Ireland's antenna attached to AI2F | CONFIRMED | Ireland antenna "primarily linked to AI2F, the AI Factory in France" | ai-factory-antennas |
| Gigafactory | Government confirmed interest in hosting | CONFIRMED | "La France confirme son intérêt pour accueillir une gigafactory d'IA sur son sol." | entreprises.gouv.fr press release |
| Gigafactory | EUR 100 million compute purchase for administrations, research, hospitals, 2027 horizon | CONFIRMED | "commander un volume de capacité de calcul de 100 millions d'euros" … "à l'horizon 2027" | entreprises.gouv.fr |
| Gigafactory | No site or consortium named | CONFIRMED | Page names none; EuroHPC call page names no candidates either | entreprises.gouv.fr; eurohpc-ju Gigafactories call 2026-07-30 |
| Models | Lucie-7B about 3 trillion tokens | CONFIRMED | "was trained on 3 trillion tokens of multilingual data" | huggingface.co/OpenLLM-France/Lucie-7B |
| Models | A third French | CONFIRMED | "French (32.4%)" | HF Lucie-7B |
| Models | Trained on Jean Zay, about 550,000 H100 GPU hours | CONFIRMED | "pre-trained on 512 H100 80GB GPUs for about 550,000 GPU hours on the Jean Zay supercomputer" | HF Lucie-7B |
| Models | Under a GENCI grand-challenge grant | CONFIRMED | HF: "(Grant 2024-GC011015444)"; GENCI: "the aim of the Grand Challenge was to develop Lucie-7B" | HF Lucie-7B; genci.fr |
| Models | Led by LINAGORA (OpenLLM-France) | CONFIRMED | "Developed by the OpenLLM-France community led by LINAGORA" | genci.fr |
| Models | Apache-2.0 | CONFIRMED | "License: apache-2.0" | HF Lucie-7B |
| Models | Instruct release January 2025 | NOT CONFIRMED | Neither page dates an instruct release. HF base card shows only a paper "Published Mar 15, 2025"; GENCI names Lucie-7B-Instruct-humandata without a date | HF Lucie-7B; genci.fr |
| Models | Public funding amount not stated | CONFIRMED | Neither page gives an amount | HF; genci.fr |
| Models | Mistral Small 3.1 under Apache-2.0, March 2025 | CONFIRMED | "Mistral Small 3.1 is released under an Apache 2.0 license." Dated March 17, 2025 | mistral.ai/news/mistral-small-3-1 |
| Models | Mistral Compute announced June 2025 | CONFIRMED | Dated June 11, 2025: "Mistral Compute is a new AI infrastructure offering…" | mistral.ai/news/mistral-compute |
| Strategy | Launched 2018, within France 2030 | CONFIRMED | "a lancé en 2018 une stratégie nationale pour l'intelligence artificielle"; attached to France 2030 | entreprises.gouv.fr strategy page |
| Strategy | Phase 1 2018–2022 EUR 1.5 bn incl. Jean Zay | CONFIRMED | Phase 1 €1.5 billion; funded … the "supercalculateur Jean Zay" | entreprises.gouv.fr |
| Strategy | Phase 2 2021–2025 EUR 1 bn | CONFIRMED | Phase 2 (2021–2025): €1 billion under France 2030 | entreprises.gouv.fr |
| Public sector | Albert API, "public infrastructure of generative-AI services" | CONFIRMED | "infrastructure publique de services d'IA générative" | numerique.gouv.fr ALLiaNCE |
| Public sector | Within the ALLiaNCE incubator (DINUM) | CONFIRMED | "un incubateur au sein de Direction interministérielle du numérique (DINUM)" | numerique.gouv.fr |
| Public sector | Code organisation publishes a sovereign agentic coding bundle (September 2026) | CONFIRMED | albert-code: "Bundle agentic coding souverain : OpenCode + agent-vm + Albert API + skills État + MCP", updated 25 Sep 2026 (last-update date, not a publication date) | github.com/etalab-ia |
| Language resources | ORTOLANG, platform of French language tools and resources | CONFIRMED | "Plate-forme d'outils et de ressources linguistiques pour un traitement optimisé de la langue française." | ortolang.fr |
| Language resources | ORTOLANG is CNRS-led | NOT CONFIRMED | Page lists CNRS as one of eight partner institutions; it does not say CNRS leads | ortolang.fr |
| Language resources | France not listed among CLARIN ERIC members | CONFIRMED | France absent from the members table | clarin.eu participating-consortia |
| Language resources | Lucie's training datasets under Creative Commons | CONFIRMED (other row's URL) | "datasets under a Creative-Common license downloadable from the Hugging Face platform" | genci.fr |
| Institutions | GENCI, IDRIS, CINES, CEA TGCC, Inria, DINUM | CONFIRMED | On the 2025-03-12 release and numerique.gouv.fr; LINAGORA/OpenLLM-France and Mistral are supported only by other rows' URLs | 2025-03-12 release; numerique.gouv.fr |
| Power | Ministry cites decarbonised electricity as the case for hosting | CONFIRMED | The minister cites France's "électricité décarbonée" | entreprises.gouv.fr press release |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speaker counts per language | NOT FOUND | Searched DGLFLF/culture.gouv.fr and INSEE; only press, secondary and 1999-census references surfaced; no official page fetched | — | — |
| Shared with | Wider francophone world | FOUND | The OIF serves 90 states and governments; 396 million French speakers worldwide | https://www.francophonie.org/ | "…au service de ses 90 Etats et gouvernements." / "396 Millions de locuteurs dans le monde" |
| EuroHPC system | Jean Zay's capacity | FOUND | 125.9 petaflops (64-bit) after the extension inaugurated 13 May 2025; storage of the order of 100 PB | https://www.cnrs.fr/fr/presse/supercalculateur-jean-zay-la-france-multiplie-par-4-les-ressources-scientifiques-en-ia | "125,9 pétaflops de puissance de calcul 64 bits" |
| Gigafactory | Candidate consortia | NOT FOUND | DGE and EuroHPC pages name none; nothing official found | — | — |
| Models | Mistral state funding | FOUND (partial) | Bpifrance (state investment bank) was an existing investor joining Mistral's EUR 1.7 bn Series C (Sept 2025); no amount stated | https://www.caissedesdepots.fr/eclairage/en/news/mistral-ai-raises-eu17b-accelerate-technological-progress-ai | "existing investors: Andreessen Horowitz, Bpifrance, General Catalyst" |
| Strategy | Third phase and 2025 summit figures | NOT FOUND | Search shows info.gouv.fr reporting a third phase launched after the 6 Feb 2025 interministerial committee, but info.gouv.fr and economie.gouv.fr returned 403 to WebFetch and curl | — | — |
| Public sector | Albert base models and user counts | NOT FOUND (usage only) | Official page names no models ("open-weight ou propriétaires") and no user count; it gives >70 public projects and >100,000 weekly requests | https://ia.numerique.gouv.fr/outils-ia/albert-api | "Déjà utilisé dans plus de 70 projets publics." / "Plus de 100 000 requêtes hebdomadaires traitées." |
| Language resources | France's CLARIN observer status | FOUND | France was a CLARIN observer 2017–2022; it is not listed now (not a member) | https://www.clarin.eu/blog/tour-de-clarin-france | "France was an observer of CLARIN from 2017-2022." |
| Power | Grid-connection figures | FOUND | RTE fast-track contract for the Campus IA site at Fouju: 240 MW by end 2027, 700 MW before end 2029, up to 1,400 MW (26 Jan 2026) | https://assets.rte-france.com/prod/public/2026-01/20260122_CP_RACCORDEMENT_FASTTRACK_CAMPUSIA_VDEF_0.pdf | "un premier palier de puissance de 240 MW d'ici fin 2027, suivi d'un second palier de 700 MW avant fin 2029" |

#### C. Prose flags
None. The prose's factual assertions repeat the snapshot.

### IT
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Italian is the official language (Law 482/1999 art. 1) | CONFIRMED | "La lingua ufficiale della Repubblica è l'italiano." | normattiva.it 482 |
| Languages | Twelve protected minority languages incl. French, Franco-Provençal, Friulian, Ladin, Occitan, Sardinian, German, Slovene, Croatian, Albanian, Greek, Catalan (art. 2) | CONFIRMED | "…popolazioni albanesi, catalane, germaniche, greche, slovene e croate e di quelle parlanti il francese, il franco-provenzale, il friulano, il ladino, l'occitano e il sardo" (law says "germaniche", Germanic) | normattiva.it 482~art2 |
| Languages | Population 58,943,464 | CONFIRMED (value) | Eurostat value for IT = 58943464. The IT row cites only Normattiva; add the Eurostat URL to the row | Eurostat demo_pjan |
| Languages | "provisional" | NOT CONFIRMED | Eurostat flags only FR (status {"1":"p"}); IT carries no status flag | Eurostat demo_pjan |
| EuroHPC system | Leonardo at CINECA, Bologna, operational | CONFIRMED | "located in the Bologna Technopole, Italy"; IT4LIA "coordinated by CINECA" | our-supercomputers; ai-factories/italy_en |
| EuroHPC system | 249.04 PFlops sustained | CONFIRMED | "249.04 petaflops Sustained performance" | our-supercomputers |
| EuroHPC system | 13,824 Ampere GPUs | CONFIRMED | "13824 "Da Vinci" GPUs (based on NVIDIA Ampere architecture)" | our-supercomputers |
| EuroHPC system | LISA upgrade inaugurated June 2026 | NOT CONFIRMED | italy_en mentions "its AI-enhanced LISA system" with no inauguration date; our-supercomputers does not mention LISA | italy_en; our-supercomputers |
| AI Factory | IT4LIA selected 10 December 2024 | CONFIRMED | Release dated "10 December 2024" | eurohpc-ju first seven AI Factories |
| AI Factory | Hosted by CINECA at the Bologna Tecnopolo | CONFIRMED | "hosted by CINECA Consorzio Interuniversitario and will be located in Bologna, Italy" | first seven release |
| AI Factory | With Austria and Slovenia | CONFIRMED | "in collaboration with Austria and Slovenia" | first seven release |
| AI Factory | Successor contracted 22 April 2026 with E4 and Dell | CONFIRMED | "signed a procurement contract with E4 Computer Engineering and Dell Technologies" (22 April 2026) | IT4LIA contract 2026-04-22 |
| AI Factory | EUR 290 million | CONFIRMED | "a total budget of EUR 290.000.000" | IT4LIA contract |
| AI Factory | 50% EuroHPC | CONFIRMED | "The EuroHPC JU will fund 50% of the total cost" | IT4LIA contract |
| AI Factory | NVIDIA GB200 | CONFIRMED | "the liquid-cooled NVIDIA GB200 NVL4 architecture" | IT4LIA contract |
| AI Factory | Over 160 EFlops peak AI inference | CONFIRMED | "is expected to deliver more than 160 Exaflops of peak AI inference performance" | IT4LIA contract |
| AI Factory | Inference partition on European accelerators | CONFIRMED | "AI‑optimised inference accelerators from European‑based" Axelera AI | IT4LIA contract |
| AI Factory | Services "to be confirmed" | CONFIRMED | "To be confirmed soon" (italy_en). Note: the contract page says IT4LIA has provided resources on Leonardo "Since April 2025" | italy_en; IT4LIA contract |
| AI Factory | Serbia's and Switzerland's antennas attach to it | CONFIRMED | Serbia "also connects to the IT4LIA AI Factory"; Switzerland collaborates with IT4LIA among others | ai-factory-antennas |
| Models | Minerva-7B by Sapienza NLP with CINECA and Babelscape | CONFIRMED | "developed by Sapienza NLP," with CINECA, contributions from Babelscape | HF sapienzanlp/Minerva-7B-instruct-v1.0 |
| Models | Almost 2.5T tokens, 1.14T Italian | CONFIRMED | "almost 2.5 trillion tokens"; 1.14 trillion Italian | HF Minerva |
| Models | Pretrained from scratch | CONFIRMED | "pretrained from scratch on Italian" | HF Minerva |
| Models | Funded by PNRR FAIR | CONFIRMED | "funded by the PNRR MUR project PE0000013-FAIR" | HF Minerva |
| Models | Apache-2.0 | CONFIRMED | "License: apache-2.0" | HF Minerva |
| Models | December 2024 | UNCLEAR | Only "Updated Dec 7, 2024" on the Minerva collection; no release date for the model | HF Minerva |
| Models | Velvet-14B trained on Leonardo | CONFIRMED | "trained on the HPC Leonardo infrastructure hosted by CINECA" | HF Almawave/Velvet-14B |
| Models | Over 4T tokens | CONFIRMED | training "culminated in more than 4 trillion tokens" | HF Velvet |
| Models | Six languages | CONFIRMED | "six languages (Italian, English, Spanish, Portuguese-Brazilian, German, French)" | HF Velvet |
| Models | Apache-2.0, January 2025 | CONFIRMED | "made available under the Apache 2.0 license"; "January 31st, 2025" | HF Velvet |
| Models | EUROPA consortium led by Italian Domyn won on 19 June 2026 | CONFIRMED | "EUROPA, a European consortium led by the Italian company Domyn"; "Publication 19 June 2026" | digital-strategy.ec.europa.eu |
| Strategy | Italian AI Strategy 2024–2026, 22 July 2024 | CONFIRMED | "Data 22 luglio 2024" | innovazione.gov.it |
| Strategy | Four areas incl. public administration | CONFIRMED | "quattro macroaree: Ricerca, Pubblica Amministrazione, Imprese e Formazione" | innovazione.gov.it |
| Strategy | Law 132 of 23 Sept 2025, in force 10 Oct 2025 | CONFIRMED | "LEGGE 23 settembre 2025, n. 132"; "Entrata in vigore del provvedimento: 10/10/2025" | normattiva.it 132 |
| Strategy | Art. 19: Presidency prepares the strategy, approved at least every two years | CONFIRMED | "predisposta e aggiornata dalla struttura della Presidenza del Consiglio dei ministri" … "approvata con cadenza almeno biennale dal Comitato interministeriale per la transizione digitale" (approval is by the CITD) | gazzettaufficiale.it PDF |
| Strategy | Art. 20: AgID and ACN national AI authorities | CONFIRMED | "l'Agenzia per l'Italia digitale (AgID) e l'Agenzia per la cybersicurezza nazionale (ACN) sono designate quali Autorità nazionali" | GU PDF |
| Strategy | Art. 23: up to EUR 1 billion equity | CONFIRMED | "fino all'ammontare complessivo di un miliardo di euro, l'investimento, sotto forma di equity e quasi equity" | GU PDF |
| Strategy / Public sector | Art. 14: PA use in a supporting role, human responsible | CONFIRMED | "in funzione strumentale e di supporto all'attività provvedimentale … della persona che resta l'unica responsabile" (heading "Uso dell'intelligenza artificiale nella pubblica amministrazione"; the PDF's two-column layout scrambles article numbers, so the number 14 is inferred from heading order) | GU PDF |
| Language resources | CLARIN-IT (CNR Zampolli institute) | CONFIRMED | "CLARIN-IT" / "Institute for Computational Linguistics A. Zampolli, Italian National Research Council" | clarin.eu |
| Language resources | Minerva's Italian pretraining data described as open | CONFIRMED | "truly-open (data and model) Italian-English LLMs" | HF Minerva |
| Language resources | "the FAIR foundation under the PNRR" | UNCLEAR | Minerva card names "the PNRR MUR project PE0000013-FAIR", not a foundation; italy_en mentions only FAIR datasets | HF Minerva; italy_en |
| Institutions | CINECA, AI4I, ACN, CNR ILC | CONFIRMED | italy_en names CINECA, ACN, AI4I as co-funders; CLARIN page names CNR ILC. FAIR, AgID, the Department, Almawave and Domyn are supported only by other rows' URLs | italy_en; clarin.eu |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speaker counts | NOT FOUND (partial context) | ISTAT 2024 gives shares, not minority-language counts: 48.4% use only or mainly Italian; 10.1% use another language somewhere | https://www.istat.it/comunicato-stampa/luso-della-lingua-italiana-dei-dialetti-e-delle-lingue-straniere-anno-2024/ | "Nel 2024 quasi una persona su due (48,4%) parla solo o prevalentemente italiano in tutti i contesti relazionali" |
| Shared with | Italian-speaking communities abroad | FOUND (partial) | 6.382 million Italian citizens habitually resident abroad at 31 Dec 2024 (provisional); citizens, not speakers. Swiss constitutional status of Italian not fetched (fedlex is JS-only) | https://www.istat.it/wp-content/uploads/2025/07/Stat-today_Italiani-residenti-allestero_2023-24.pdf | "Al 31 dicembre 2024 i cittadini italiani abitualmente dimoranti all'estero sono 6 milioni e 382mila" |
| Gigafactory | National proposal with Eni and Leonardo sites, 95 MW first phase | FOUND (partial) | MIMIT confirms an Italian Gigafactory candidacy (30 May 2026); Eni, Leonardo, sites and 95 MW not on any official page found | https://www.mimit.gov.it/it/notizie-stampa/spazio-urso-incontra-a-parigi-il-ministro-francese-baptiste-europa-sia-protagonista-della-nuova-corsa-allo-spazio | "Urso ha illustrato gli obiettivi della candidatura italiana alla realizzazione di una AI Gigafactory europea" |
| Models | Italia (iGenius), gated | NOT FOUND | huggingface.co/iGeniusAI/Italia-9B-Instruct-v0.1 returned 401, the org page 404 | — | — |
| Public sector | Specific pilots or procurements | NOT FOUND | AgID page (18 Feb 2025) covers draft PA AI-adoption guidelines in consultation; it names no LLM pilot or procurement | https://www.agid.gov.it/it/notizie/intelligenza-artificiale-in-consultazione-le-linee-guida-pa | (no pilot named) |
| Power | Gigafactory megawatts | NOT FOUND | No official MW figure found (MIMIT page has none) | — | — |

#### C. Prose flags
None beyond the snapshot. ("No stated public-sector pilot" remains consistent with what was found.)

### MT
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Maltese national language; Maltese and English official (art. 5) | CONFIRMED | "The National language of Malta is the Maltese" … "The Maltese and the English languages … shall be the official languages of Malta" | legislation.mt Constitution PDF |
| Languages | Population 574,250 | CONFIRMED | Eurostat value MT = 574250 | Eurostat demo_pjan |
| Languages | "provisional" | NOT CONFIRMED | No status flag on MT; only FR is flagged p | Eurostat demo_pjan |
| Shared with | English shared with Ireland | NOT CONFIRMED | Only cited URL is Malta's Constitution, which says nothing about Ireland | legislation.mt |
| EuroHPC system | None | CONFIRMED | Systems listed in 12 countries; Malta not among them | our-supercomputers |
| AI Factory | No factory; antenna CALYPSO led by MDIA, linked to Greece's Pharos | CONFIRMED | "Led by the MDIA"; ai-factories_en: "Antennas: Cyprus, Malta, North Macedonia and Serbia" under Greece | ai-factory-antennas; ai-factories_en |
| AI Factory | "both an extension of Pharos and a national innovation hub" | CONFIRMED | "both an extension of PHAROS and a national innovation hub" | ai-factory-antennas |
| AI Factory | Selection date and funding not on the page | CONFIRMED | Neither is stated | ai-factory-antennas |
| Models | BERTu, pretrained from scratch on Korpus Malti | CONFIRMED | "A Maltese monolingual model pre-trained from scratch on the Korpus Malti v4.0 using the BERT (base) architecture" | HF MLRS/BERTu |
| Models | University of Malta's MLRS, 2022 | CONFIRMED | MLRS account; citation July 2022 workshop paper (UM appears only through the um.edu.mt link) | HF BERTu |
| Models | CC BY-NC-SA 4.0 | CONFIRMED | "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" | HF BERTu |
| Strategy | "The Ultimate AI Launchpad", strategy to 2030, 2019 | CONFIRMED | OECD.AI entry title; DSJ: "Adoption in 2019" (DSJ heading is "The Strategy and Vision for Artificial Intelligence in Malta 2030") | oecd.ai; digital-skills-jobs |
| Strategy | Overseen by MDIA | CONFIRMED | "The Malta Digital Innovation Authority (MDIA) is responsible for the oversight and governance of the Strategy." | digital-skills-jobs |
| Strategy | 72 actions | CONFIRMED | "A total of 72 AI actions are undertaken." | digital-skills-jobs |
| Strategy | No mention of the Maltese language | CONFIRMED | Strategy content does not mention it | digital-skills-jobs |
| Strategy | OECD.AI lists it as active and under realignment | CONFIRMED | "Active"; "Malta is currently in the process of realigning its National AI Strategy" | oecd.ai |
| Language resources | Korpus Malti, MLRS, 5.75 GB, CC BY-NC-SA 4.0, token count not stated | CONFIRMED | "Total file size: 5.75 GB"; "cc-by-nc-sa-4.0"; no token count | HF datasets/MLRS/korpus_malti |
| Language resources | Malta not a CLARIN ERIC member | CONFIRMED | Malta absent from the members table | clarin.eu |
| Institutions | MDIA; University of Malta's Institute of Linguistics and Language Technology | CONFIRMED | "Institute of Linguistics & Language Technology"; the UM page does not mention MLRS; Ministry for the Economy not on the row's pages | um.edu.mt/linguistics; antennas |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speaker counts | NOT FOUND | NSO census report page 403; eurydice 404; only press figures surfaced | — | — |
| Shared with | Maltese diaspora | NOT FOUND | Not searched beyond the language search; nothing official found | — | — |
| Gigafactory | No Maltese bid | NOT FOUND (no official statement either way) | Searches return only the CALYPSO antenna; the EuroHPC call names no candidates | — | — |
| Models | MDIA-funded Maltese language projects | FOUND | MDIA funded three University of Malta AI projects with EUR 161,800 (22 Apr 2021), all on the Maltese language (speech, text, Edu.AI) | https://www.um.edu.mt/newspoint/news/2021/04/ai-projects-receive-funding | "Three projects led by University of Malta researchers … are being collectively funded €161,800 by the Malta Digital Innovation Authority" |
| Strategy | Realigned strategy 2025–2030, 83 measures, consultation Nov 2025 (official) | NOT FOUND | mdia.gov.mt and gov.mt consultation NL-0040-2025 return 403. Search snippets from both show the consultation (closed 16 Feb 2026) and the 83 measures, but no page could be fetched | — | — |
| Public sector | No government LLM assistant; pilots not language models | FOUND (relevant, partial) | OECD.AI lists the Servizz.gov Chatbot: AI-powered, Maltese or English, since 2023, about 40,000 interactions in its first eight months; whether it is an LLM is not stated | https://oecd.ai/en/dashboards/policy-initiatives/ai-chatbot | "Users can ask questions in Maltese or English." |
| Power | Official statement | NOT FOUND | Not found | — | — |

#### C. Prose flags
| Prose claim | Verdict | Evidence | URL |
|---|---|---|---|
| "No assistant exists" (Recommended strategy 6) and "No government LLM assistant found" | UNCLEAR, worth rewording | OECD.AI lists an AI-powered Servizz.gov chatbot in Maltese and English (start 2023, active); model type unstated | https://oecd.ai/en/dashboards/policy-initiatives/ai-chatbot |
| "ALT-EDIC, where Malta is an observer" | CONFIRMED | "Six Observing Member States: Austria, Denmark, Estonia, Malta, Romania and Slovakia." (13 Feb 2024) | https://ec.europa.eu/newsroom/lds/items/818324/en |

### PT
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Portuguese official (art. 11(3)) | CONFIRMED | "A língua oficial é o Português." | parlamento.pt Constitution |
| Languages | Population 10,749,635 | CONFIRMED | Eurostat value PT = 10749635 | Eurostat demo_pjan |
| Languages | "provisional" | NOT CONFIRMED | No status flag on PT | Eurostat demo_pjan |
| Shared with | EuroLLM-9B (IST, Unbabel) covers Portuguese among 35 languages | CONFIRMED | Developers include "Unbabel, Instituto Superior Técnico"; 35 languages incl. Portuguese | HF utter-project/EuroLLM-9B |
| EuroHPC system | Deucalion hosted by FCT at Guimarães | CONFIRMED | "Deucalion is hosted by FCT and managed by CNCA"; "located in Guimarães, Portugal" | our-supercomputers |
| EuroHPC system | Inaugurated 6 September 2023 | CONFIRMED | "Inaugurated on September 6, 2023, in Guimarães." | deucalion.acnca.pt |
| EuroHPC system | 7.48 PFlops, 33 A100 nodes | CONFIRMED | "7.48 petaflops Sustained performance"; "33 nodes, each with 4x Nvidia Ampere A100" | our-supercomputers |
| EuroHPC system | Operational | CONFIRMED | "currently supports thousands of users across hundreds of research and innovation projects" | deucalion.acnca.pt |
| AI Factory | None on Portuguese soil; FCT a partner of the BSC AI Factory | CONFIRMED | "a joint initiative of the Kingdom of Spain, the Republic of Portugal…"; FCT represents Portugal | ai-factories/spain_en |
| AI Factory | FCT co-funds the MareNostrum 5 AI upgrade | CONFIRMED | Other 50% from "Spain, Portugal and Türkiye" | MN5 contract 2026-01-26 |
| AI Factory | Overview lists Portugal under Spain's factory | CONFIRMED (other row's URL) | "Portugal, Romania and Türkiye" under Spain | ai-factories_en (not cited in the PT row) |
| Models | AMALIA "the first open language model developed in European Portuguese" | CONFIRMED | "o primeiro modelo de linguagem aberto desenvolvido em português europeu" | portugal.gov.pt AMALIA news |
| Models | Presented 1 July 2026 by the Prime Minister | CONFIRMED | Dated 1 July 2026; presented by the Prime Minister | portugal.gov.pt |
| Models | Consortium of public universities and research centres | CONFIRMED | "a consortium of public universities and national research centres" | engium.uminho.pt |
| Models | Recovery plan, EUR 5.5 m plus EUR 1.5 m to 2027 | CONFIRMED | "an initial investment of 5.5 million euros" (PRR); further 1.5 million by 2027 | engium.uminho.pt; portugal.gov.pt |
| Models | Apache-2.0 | CONFIRMED | "Todos os materiais estão disponíveis de acordo com a licença Apache 2.0" | amaliallm.pt |
| Models | 9B text and 10B vision-language checkpoints published | CONFIRMED | AMALIA-9B-0626-SFT/DPO (text, 9B); AMALIA-VL-SFT/DPO (image-text-to-text, 10B) | huggingface.co/amalia-llm |
| Models | EuroLLM-9B EU-funded, 4T tokens on 400 H100s of MareNostrum 5, Apache-2.0 | CONFIRMED | "trained on 4 trillion tokens"; "400 Nvidia H100 GPUs of the Marenostrum 5 supercomputer"; "Apache License 2.0" | HF EuroLLM-9B |
| Public sector | AMALIA for citizen contact, administrative automation, decision support | CONFIRMED | Supporting citizen services, automating administrative tasks, informing decisions, gradual integration into public services | portugal.gov.pt |
| Public sector | ARTE lists an "IA.gov" line | CONFIRMED | "Soluções de inteligência artificial responsável na Administração Pública" | arte.gov.pt |
| Language resources | PORTULAN CLARIN (University of Lisbon) | CONFIRMED | "PORTULAN CLARIN" / "University of Lisbon" | clarin.eu |
| Language resources | Data partners Arquivo.pt, National Library, Torre do Tombo, RCAAP | CONFIRMED | "arquivo.pt / FCT", "RCCAP / FCT", "Arquivo Nacional Torre do Tombo", "Biblioteca Nacional de Portugal" | amaliallm.pt/parceiros |
| Language resources | 86 datasets published | CONFIRMED | "View 86 datasets" | huggingface.co/amalia-llm |
| Institutions | FCT, CNCA, INESC TEC, University of Minho (Deucalion and MACC); ARTE | CONFIRMED | "operated by the National Center for Advanced Computing (CNCA), INESC TEC, and the University of Minho"; MACC lists UMinho, INESC TEC, FCT | deucalion.acnca.pt; macc.fccn.pt; arte.gov.pt |
| Institutions | NOVA, IST, Coimbra, Porto and Minho (AMALIA) | NOT CONFIRMED | None of the row's pages lists AMALIA's consortium. The UMinho page names only UMinho units and describes IST as the unveiling venue | deucalion; macc; arte; engium.uminho.pt |
| Institutions | Unbabel and IST (EuroLLM) | CONFIRMED (other row's URL) | EuroLLM card lists both | HF EuroLLM-9B |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Mirandese's recognition | NOT FOUND | Lei 7/99 identified via search; diariodarepublica.pt returned an empty page; the parlamento.pt Constitution (first 100k chars) does not mention it | — | — |
| Languages | Speaker counts | NOT FOUND | Not separately searched; no official page fetched | — | — |
| Shared with | Brazil and the Portuguese-speaking African states | FOUND | CPLP founding members: Angola, Brazil, Cabo Verde, Guinea-Bissau, Mozambique, Portugal, São Tomé and Príncipe, Timor-Leste; membership open to states with Portuguese as an official language | https://secretariadoexecutivo.cplp.org/media/e23bn0a0/r2_res_rev_estatutos_2023_aprovado_.pdf | "qualquer Estado, desde que use o Português como língua oficial, poderá tornar-se Membro da CPLP" |
| AI Factory | Antennas page lists no Portuguese antenna | FOUND | 13 antennas listed (BE, CY, HU, IS, IE, LV, MT, MD, MK, RS, SK, CH, UK); none Portuguese | https://www.eurohpc-ju.europa.eu/ai-factory-antennas_en | (absence; no quotable sentence) |
| Gigafactory | EUR 200 m over seven years, Sines, joint Iberian bid | FOUND (partial) | Government (Council of Ministers, 25 June 2026): Portugal joins an Iberian bid; up to EUR 200 m of compute purchase in the first phase, matched by EuroHPC. Seven years, Sines and "on Portuguese territory" are not on the official page | https://portugal.gov.pt/pt/gc25/comunicacao/noticias/gigafabricas-de-inteligencia-artificial-reforcam-soberania-tecnologica-com-investimento-de-200-milhoes | "Portugal vai integrar uma candidatura ibérica ao programa europeu EuroHPC" |
| Models | AMALIA's compute | FOUND | Trained on MareNostrum 5, Deucalion and EuroHPC infrastructure; developed from EuroLLM-9B (AICEP page) | https://portugalglobal.pt/en/trade/international-promotion/portugal-is-the-official-partner-country-of-the-smart-country-convention-2026/amalia-artificial-intelligence-multimodal-language-agent/ | "national supercomputers (Mare Nostrum 5, Deucalion) and European infrastructure (EuroHPC)" |
| Strategy | Resolution and text of the National AI Agenda | FOUND (budget not found) | Resolução do Conselho de Ministros n.º 2/2026 (DR 1.ª série n.º 5, 8 Jan 2026) approves the Agenda and the Action Plan 2026–2030; in force the day after publication; approved 4 Dec 2025. The EUR 400 m and EUR 25 m figures are not in the text | https://bo.digital.gov.pt/api/assets/etic/6c8282d1-dd2d-438a-a60c-b8582c4858bb | "Aprovar o Plano de Ação da Agenda Nacional de Inteligência Artificial (PAANIA) para o quinquénio 2026-2030" |
| Power | Official statement | NOT FOUND | Not searched; no official page | — | — |

#### C. Prose flags
| Prose claim | Verdict | Evidence | URL |
|---|---|---|---|
| "AMALIA's compute could not be confirmed" / "training compute is unstated" | Now answerable | AICEP: trained on MareNostrum 5, Deucalion and EuroHPC; built from EuroLLM-9B (relevant to recommendation 3, "Pool with … EuroLLM") | portugalglobal.pt AMALIA page |
| "a plan to put it on the government portal" / "planned portal deployment on gov.pt" | UNCLEAR | The government's AMALIA news describes gradual integration into public services; it does not name gov.pt | portugal.gov.pt AMALIA news |
| "Funding stops in 2027 on the fetched pages" | CONFIRMED with addition | RCM 2/2026 Action Plan item II.7: "Continuação do projeto AMALIA", ARTE and FCT, extending its use to new cases (no amount) | bo.digital.gov.pt RCM 2/2026 |

### ES
#### A. Verification
| Row | Claim | Verdict | Evidence | URL |
|---|---|---|---|---|
| Languages | Castilian official; Catalan/Valencian, Basque, Galician co-official in their communities (art. 3) | CONFIRMED | "El castellano es la lengua española oficial del Estado." "Las demás lenguas españolas serán también oficiales en las respectivas Comunidades Autónomas…" | boe.es Constitución |
| Languages | Population 49,128,297 | CONFIRMED (value) | Eurostat ES = 49128297. The ES row cites BOE and alia.gob.es, neither of which gives it; add the Eurostat URL | Eurostat demo_pjan |
| Languages | "provisional" | NOT CONFIRMED | No status flag on ES | Eurostat demo_pjan |
| Shared with | Catalan protected in Italy (Law 482/1999) | CONFIRMED | "…popolazioni albanesi, catalane…" | normattiva.it 482~art2 |
| EuroHPC system | MareNostrum 5 at BSC, operational, 215.40 PFlops | CONFIRMED | "215.40 petaflops Sustained performance" | our-supercomputers |
| EuroHPC system | Hopper accelerated partition | CONFIRMED | "The ACC partition is based on NVIDIA Hopper" | our-supercomputers |
| AI Factory | BSC AI Factory selected 10 Dec 2024 | CONFIRMED | Release dated "10 December 2024" | first seven release |
| AI Factory | MN5 AI upgrade contract 26 Jan 2026, about EUR 129 m, 50% EuroHPC | CONFIRMED | "co-funded with a total budget of around EUR 129 000 000"; EuroHPC funds half | MN5 contract 2026-01-26 |
| AI Factory | Installation from early 2026 | CONFIRMED | installation "will start in early 2026" | MN5 contract |
| AI Factory | Consortium with Portugal, Türkiye and Romania | CONFIRMED | "a joint initiative of Spain, Portugal, Turkey and Romania" | first seven release |
| AI Factory | 1HealthAI selected 10 October 2025 | NOT CONFIRMED | The 1HealthAI page gives no selection date | eurohpc-ju spain-1health-ai |
| AI Factory | 1HealthAI led by CESGA with CSIC and the Galician universities | CONFIRMED | "Led by the Galicia Supercomputing Center (CESGA)"; CSIC co-lead; "the three Galician public universities" | spain-1health-ai |
| Gigafactory | Móra la Nova with San Fernando de Henares added on 14 Jan 2026 | CONFIRMED | Headline "El Gobierno incluirá a Madrid en una candidatura conjunta con Cataluña…"; published 14/01/2026 | digital.gob.es press note |
| Gigafactory | Investment "could exceed EUR 4,000 million" | CONFIRMED | "La inversión público-privada conjunta podría superar los 4.000 millones de euros." | digital.gob.es |
| Gigafactory | SETT in the consortium | CONFIRMED | "la Sociedad Española para la Transformación Tecnológica (SETT)" part of the consortium | digital.gob.es |
| Gigafactory | Operational between 2027 and 2028 | CONFIRMED (nuance) | "Las gigafactorías seleccionadas deberán estar operativas entre 2027 y 2028." This is a requirement on selected gigafactories, not the bid's own schedule | digital.gob.es |
| Models | ALIA 100% publicly funded | CONFIRMED | "FINANCIACIÓN 100% PÚBLICA" | alia.gob.es |
| Models | Coordinated by BSC under the State Secretariat for Digitalisation and AI | CONFIRMED | coordinated by BSC with backing of the "Secretaría de Estado de Digitalización e Inteligencia Artificial" | alia.gob.es |
| Models | Covers Castilian and co-official languages | CONFIRMED | castellano, catalán y valenciano, euskera, gallego | alia.gob.es |
| Models | Verified by AESIA | CONFIRMED | verified by "la Agencia Española de Supervisión de la Inteligencia Artificial (AESIA)" | alia.gob.es |
| Models | Development phase about EUR 10 m | CONFIRMED | "approximately €10 million in funding" | OSOR case study |
| Models | Current phase to end June 2026; next phase being defined | CONFIRMED | "The present phase of the ALIA project runs until the end of June 2026"; "the next phase is currently being defined" | OSOR |
| Models | Weights and code Apache-2.0 | CONFIRMED | released "under the Apache 2.0 licence" | OSOR |
| Models | ALIA-40B pretrained from scratch on 9.37T tokens on MareNostrum 5 | CONFIRMED (card inconsistent) | "pre-trained from scratch on 9.37 trillion tokens of highly curated data"; the data section also says "2.68 trillion tokens used across 2 epochs" | HF BSC-LT/ALIA-40b |
| Models | Salamandra likewise | CONFIRMED | "pre-trained from scratch on 12.875 trillion tokens"; "All models were trained on MareNostrum 5" | HF salamandra-7b-instruct |
| Models | Latxa (Basque, HiTZ) on Llama 3.1 and Qwen bases | CONFIRMED | "built on top of Qwen3.5-4B"; citation: "Scaling up to Llama 3.1 Instruct 70B as backbone" | HF HiTZ/Latxa-Qwen3.5-4B |
| Models | Latxa trained on Leonardo | CONFIRMED | "The models were trained on the Leonardo supercomputer at CINECA under the EuroHPC Joint Undertaking." | HF Latxa |
| Models | Funded by the Basque and Spanish governments | CONFIRMED | "Ikergaitu and ALIA projects (Basque and Spanish Government)" | HF Latxa |
| Models | Projecte Aina (Catalan, Generalitat) | CONFIRMED | "Una iniciativa del Govern"; Generalitat de Catalunya funds | projecteaina.cat |
| Models | Proxecto Nós (Galician) | CONFIRMED | aims to "promover a presenza dixital do galego" | nos.gal |
| Strategy | AI Strategy 2024 approved 14 May 2024 | CONFIRMED | Approved by the Council of Ministers 14 May 2024 | lamoncloa.gob.es |
| Strategy | EUR 1,500 m from the recovery plan for 2024 and 2025 | CONFIRMED | "está dotada con 1.500 millones de euros procedentes del Plan de Recuperación" … "se desplegará durante los años 2024 y 2025" | lamoncloa.gob.es |
| Strategy | EUR 90 m for MareNostrum | CONFIRMED | "recibirá una inversión de 90 millones de euros para mejorar sus prestaciones" | lamoncloa.gob.es |
| Strategy | ALIA named as the language-model programme | CONFIRMED | "la creación de modelos de lenguaje en castellano y lenguas cooficiales que se denominará ALIA" | lamoncloa.gob.es |
| Strategy | "in force" | UNCLEAR | The page (May 2024) gives a 2024–2025 deployment; it cannot say whether the strategy is in force in October 2026 | lamoncloa.gob.es |
| Public sector | GobTechLab testing about 19 AI use cases | CONFIRMED | "currently identifying and testing approximately 19 high-impact AI use cases" | OSOR |
| Public sector | Municipal citizen assistants | CONFIRMED | "generative AI assistants for municipalities" | OSOR |
| Public sector | Tax-agency tools on ALIA being explored | CONFIRMED | "advanced tools built on ALIA are being explored" | OSOR |
| Public sector | Primary-care assistant | CONFIRMED | Cardiomentor adapts ALIA to "assist primary care professionals in the medical field" | OSOR |
| Language resources | CLARIAH-ES, CLARIN ERIC member, led by HiTZ | CONFIRMED | "CLARIAH-ES" / "Basque Center for Language Technology (HiTZ)" | clarin.eu |
| Language resources | Language Technologies Plan 2019 as ALIA's origin | CONFIRMED | "EL PROYECTO ALIA SE INICIÓ CON EL PLAN DE TECNOLOGÍAS DEL LENGUAJE EN 2019." | alia.gob.es |
| Language resources | CATalog about 23 bn Catalan tokens | CONFIRMED (other row's URL) | OSOR: "contains approximately 23 billion tokens"; not on alia.gob.es | OSOR |
| Language resources | Aina and Nós programmes | CONFIRMED (partly other row's URL) | alia.gob.es names AINA (and ILENIA), not Nós; Nós is on nos.gal | alia.gob.es; nos.gal |
| Institutions | BSC, State Secretariat, AESIA, CESGA | CONFIRMED | alia.gob.es; spain-1health-ai. HiTZ, CiTIUS and ILG, SETT are supported only by other rows' URLs | alia.gob.es; spain-1health-ai |
| Power | Ministry's bid note stresses energy capacity and efficiency | CONFIRMED | "con especial hincapié en la capacidad energética, las cadenas de suministro fiables"; no figures | digital.gob.es |

#### B. Unverified cells
| Row | Cell (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Languages | Speakers per language | NOT FOUND | INE ECEPOV-2021 has a "Conocimiento y uso de lenguas" table set (found by search), but no figures were extracted from an INE page | — | — |
| Shared with | Spanish-speaking states outside the EU and the diaspora | FOUND (partial) | ALIA's official site: Castilian spoken by 600 million people worldwide (speakers, not a list of states) | https://alia.gob.es/ | "hablado por 600 millones de personas en el mundo" |
| Gigafactory | June 2026 Council of Ministers decision on the public stake | FOUND | 16 June 2026: Council authorised EUR 719 m via SETT into the public-private consortium for the multi-site bid (Móra la Nova and San Fernando de Henares) | https://digital.gob.es/content/dam/portal-mtdfp/comunicacion/comunicacion_ministro/2026/06/16-06-2026/20260602%20NP%20GigafactoriasVF.pdf | "El Consejo de Ministros ha autorizado hoy una inversión de 719 millones de euros … a través de la SETT" |
| Gigafactory | Joint Iberian bid | FOUND | Portuguese government: Portugal joins an Iberian bid (25 June 2026). The Spanish 16 June note does not mention Portugal | https://portugal.gov.pt/pt/gc25/comunicacao/noticias/gigafabricas-de-inteligencia-artificial-reforcam-soberania-tecnologica-com-investimento-de-200-milhoes | "Portugal vai integrar uma candidatura ibérica ao programa europeu EuroHPC" |
| Power | Grid figures | NOT FOUND | Neither ministry note gives MW or grid figures | — | — |

#### C. Prose flags
None. Prose claims (current phase ended June 2026, next phase being defined, Portugal co-funds and sits in the factory consortium) match the pages.

### Summary
| State | Claims checked | Confirmed | Not confirmed | Unclear | Unverified cells | Found | Not found |
|---|---|---|---|---|---|---|---|
| FR | 44 | 41 | 3 | 0 | 9 | 5 | 4 |
| IT | 41 | 37 | 2 | 2 | 6 | 2 | 4 |
| MT | 19 | 17 | 2 | 0 | 7 | 2 | 5 |
| PT | 26 | 24 | 2 | 0 | 8 | 5 | 3 |
| ES | 45 | 42 | 2 | 1 | 5 | 3 | 2 |
| Total | 175 | 161 | 11 | 3 | 35 | 17 | 18 |

"Found" includes partial finds (marked FOUND (partial) in the tables): FR 1, IT 2, MT 1, PT 2, ES 1.

#### NOT CONFIRMED claims
1. FR, Language shared with: "French official in Belgium and Luxembourg". The only cited URL (Italy's Law 482/1999) does not support it; the row needs a source.
2. FR, Models: "Lucie instruct release January 2025". Neither the HF card nor GENCI dates an instruct release.
3. FR, Language resources: ORTOLANG "CNRS-led". The site lists CNRS as one of eight partners and does not say it leads.
4. IT, Languages: population "provisional". Eurostat flags only FR as provisional.
5. IT, EuroHPC system: "LISA upgrade inaugurated June 2026". The cited pages name LISA with no date.
6. MT, Languages: population "provisional". Not flagged.
7. MT, Language shared with: "English with Ireland". The cited Maltese Constitution is silent on Ireland.
8. PT, Languages: population "provisional". Not flagged.
9. PT, Key institutions: "NOVA, IST, Coimbra, Porto and Minho (AMALIA)". None of the row's pages lists the consortium; the UMinho page names only UMinho and has IST as the venue.
10. ES, Languages: population "provisional". Not flagged. The ES and IT rows also do not cite Eurostat at all.
11. ES, AI Factory: "1HealthAI selected 10 October 2025". The cited 1HealthAI page gives no date.

## Review: sections 2, 4 and 6 (routes, EU vehicles, cross-cutting), 2026-10-10

Tools: WebSearch available yes; 86 URLs fetched (48 cited plus 38 for Task B and fallbacks); 9 failed (all 6 cited EUR-Lex URLs return an empty WAF challenge to both curl and WebFetch, retried once each; openeurollm.eu/news is 404; two Funding & Tenders JSON probes 404).

Method note: pages were fetched with curl and converted to text in the scratchpad, and quotes were matched by regex, so every quote below is verbatim from the page as served on 2026-10-10. The EUR-Lex texts were read from the same CELEX documents on the Publications Office (publications.europa.eu/resource/celex/<CELEX> and the cellar DOC_1 it resolves to), because eur-lex.europa.eu itself was unreachable. Those verdicts are marked "(via PO copy)". The cited URL should either be kept with that caveat or switched to the Publications Office URL.

### Section 4

#### A. Verification

| Where (subsection or table row) | Claim | Verdict | Evidence (quote ≤25 words, or what the page says) | URL |
|---|---|---|---|---|
| AI Factories intro | 19 AI Factories and 13 antennas | CONFIRMED | "The European Union has established 19 AI Factories and 13 AI Factory Antennas that offer free, customised support" | https://eurohpc-ju.europa.eu/ai-factories_en |
| AI Factories intro | Three rounds on 10 Dec 2024, 12 Mar 2025, 10 Oct 2025 | NOT CONFIRMED (on cited pages) | Neither cited page gives the round dates. The antenna release says only "Last week, following the last cut-off ... six new AI Factories have been selected". The dates are correct on uncited releases (fetched): 2024-12-10 "Publication date 10 December 2024"; 2025-03-12 "Press release 12 March 2025"; 2025-10-10 "Press release 10 October 2025". Add those three URLs. | https://eurohpc-ju.europa.eu/ai-factories_en ; https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en |
| AI Factories intro | 13 antennas on 13 Oct 2025, about EUR 55 M EU funding matched by states | CONFIRMED | "The European Union will fund the AI Factory Antennas with an investment of around €55 million, matched by contributions from the EuroHPC JU participating states." (dated 13 October 2025) | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en |
| AI Factories intro | Six factories signed contracts in 2026, each 50% EuroHPC / 50% national | CONFIRMED | "With LUMI-AI, EuroHPC JU has now signed its sixth AI Factory procurement contract for a next-generation AI-optimised supercomputer." Each 2026 release: "The EuroHPC JU will fund 50% of the total cost". | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en |
| AI Factories intro | No new AI-optimised system stated as operational by the access date | UNCLEAR | This is a claim of absence. HammerHAI is "expected to go into operation in the second half of 2026", and the EuroHPC press listing up to 9 Oct 2026 has no operational notice for it. Caveat: on 11 June 2026 the listing shows the inauguration of "LISA, the Leonardo Improved Supercomputing Architecture partition". That is not an AI Factory procurement, but a reader could count it. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-ai-supercomputer-hammerhai-2026-03-16_en |
| Table: Austria | AI:AT, ACA and AIT at TU Wien, new system, Mar 2025 | CONFIRMED | "consortium is led by Advanced Computing Austria GmbH (ACA) and the AIT Austrian Institute of Technology and includes TU Wien". Services available from: "NA". | https://www.eurohpc-ju.europa.eu/ai-factories/austria_en |
| Table: Bulgaria | BRAIN++, Sofia Tech Park with INSAIT, Discoverer++, tender open to 16 Oct 2026 | NOT CONFIRMED (status on cited page) | The cited page confirms the host and system ("lead by Sofia Tech Park (STP) with the support of INSAIT"; "access to the Discoverer++ supercomputer") but has no tender date. The date is correct on an uncited tender page: "Status Open ... Deadline date 16 October 2026, 16:00 (CEST)". Cite https://www.eurohpc-ju.europa.eu/acquisition-delivery-installation-and-maintenance-hardware-and-software-discoverer-ai-optimised_en | https://www.eurohpc-ju.europa.eu/ai-factories/bulgaria_en |
| Table: Czechia | CZAI, IT4Innovations, VSB-TU Ostrava, KarolAIna, selected | CONFIRMED | "linked to KarolAIna, a new supercomputer ... hosted and operated by IT4Innovations"; "The consortium is led by VSB—Technical University of Ostrava" | https://www.eurohpc-ju.europa.eu/czechia_en |
| Table: Finland | LUMI AIF, CSC Kajaani with CZ, DK, EE, NO, PL; contract 31 Aug 2026, EUR 387.8 M; available 2027 | CONFIRMED | "total budget of EUR 387 800 000"; "expected to be installed and made available to users in 2027"; "led by Finland and involving Czechia, Denmark, Estonia, Norway, and Poland" | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-lumi-ai-supercomputer-2026-08-31_en |
| Table: France | AI2F, GENCI with CEA, CINES, CNRS, Inria; Alice Recoque; contract 18 Nov 2025, EUR 354.8 M; installation from 2026 | CONFIRMED | "total budget of EUR 354 800 000"; "The installation of the system will start in 2026." (published 18 November 2025). France page: "led by GENCI with ... AMIAD, CEA, CINES, CNRS ... Inria" | https://www.eurohpc-ju.europa.eu/contract-signed-alice-recoque-europes-new-exascale-supercomputer-2025-11-18_en |
| Table: Germany HammerHAI | HLRS; contract 16 Mar 2026, EUR 55 M; operation H2 2026 | CONFIRMED | "A total of €55 million has been budgeted"; "expected to go into operation in the second half of 2026" (published 16 March 2026) | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-ai-supercomputer-hammerhai-2026-03-16_en |
| Table: Germany JAIF | FZJ, JUPITER, Mar 2025, inaugurated 5 Sep 2025 | CONFIRMED | "JUPITER, Europe's first exascale supercomputer, was inaugurated today in Jülich" (5 September 2025); "JUPITER AI Factory (JAIF), selected in March 2025" | https://www.eurohpc-ju.europa.eu/jupiter-launching-europes-exascale-era-2025-09-05_en |
| Table: Greece | Pharos, GRNET, DAEDALUS "fully available shortly" (June 2026) | NOT CONFIRMED (on cited page) | The Greece page says only "leveraging the DAEDALUS supercomputer, which is currently being deployed in Greece". The claim is correct on an uncited release of 23 June 2026: "is expected to become fully available to European users shortly." Cite https://www.eurohpc-ju.europa.eu/two-new-eurohpc-systems-join-top500-jupiter-remains-among-worlds-fastest-supercomputers-2026-06-23_en | https://www.eurohpc-ju.europa.eu/ai-factories/greece_en |
| Table: Italy | IT4LIA, CINECA with AT and SI; contract 22 Apr 2026, EUR 290 M | CONFIRMED | "total budget of EUR 290.000.000"; "coordinated by CINECA and implemented in collaboration with ... (ARNES), Advanced Computing Austria ACA GmbH, and AIT" | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-boost-ai-capabilities-it4lia-ai-factory-2026-04-22_en |
| Table: Lithuania | LitAI, Vilnius University, selected | CONFIRMED | "The LitAI Factory project will be led by the Vilnius University" | https://www.eurohpc-ju.europa.eu/lithuania_en |
| Table: Luxembourg | MeluXina-AI, LuxProvide; contract 22 Jul 2026, EUR 80 M; installation from autumn 2026 | CONFIRMED | "total budget of EUR 80 000 000"; "Installation activities are expected to start in fall of 2026." | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-meluxina-ai-new-ai-optimised-supercomputer-luxembourg-ai-factory-2026-07-22_en |
| Table: Netherlands | NLAIF, AIFNL Foundation with SURF, TNO | CONFIRMED | "The AIFNL Foundation will be the lead partner and hosting entity together with a consortium comprising SURF, Samenwerking Noord, TNO and AIC4NL." | https://www.eurohpc-ju.europa.eu/netherlands_en |
| Table: Poland PIAST | PSNC Poznań, "services available from 2026" | CONFIRMED | "Services Available from 2026"; "supported by the Poznańskie Centrum Superkomputerowo-Sieciowe (PCSS)" | https://www.eurohpc-ju.europa.eu/ai-factories/poland_en |
| Table: Poland Gaia | Cyfronet AGH, about 1,000 GPUs | CONFIRMED | "High-performance supercomputing infrastructure: ~1,000 GPUs"; "Academic Computer Centre Cyfronet AGH (coordinator)" | https://www.eurohpc-ju.europa.eu/poland-gaia-ai-factory_en |
| Table: Romania | ICI Bucharest with Politehnica; to be acquired; implementation from 1 Sep 2026 | NOT CONFIRMED (date) | Host and acquisition are supported: "hosted and co-coordinated in Bucharest by ... ICI Bucharest with University Politehnica of Bucharest"; "aims to acquire and deploy an AI-optimised supercomputer". No 1 September 2026 date appears on the page. | https://www.eurohpc-ju.europa.eu/romania_en |
| Table: Slovenia | SLAIF, IZUM with JSI and ARNES | CONFIRMED | "IZUM will develop and manage the new supercomputer system in collaboration with the Jožef Stefan Institute and ARNES." | https://www.eurohpc-ju.europa.eu/ai-factories/slovenia_en |
| Table: Spain BSC | BSC with PT, TR, RO; MN5 AI upgrade; contract 26 Jan 2026, about EUR 129 M | CONFIRMED | "total budget of around EUR 129 000 000"; "a joint initiative of Spain, Portugal, Türkiye and Romania" | https://www.eurohpc-ju.europa.eu/contract-signed-boost-marenostrum-5s-ai-capabilities-2026-01-26_en |
| Table: Spain 1HealthAI | CESGA, Galicia; system not stated | CONFIRMED | "Led by the Galicia Supercomputing Center (CESGA)" | https://www.eurohpc-ju.europa.eu/spain-1health-ai_en |
| Table: Sweden | MIMER, NAISS Linköping; contract 21 Apr 2026, EUR 29.76 M; online 2027 | NOT CONFIRMED ("online 2027") | Budget and host are supported: "total budget of EUR 29 760 000"; "in Linköping, Sweden". On timing the page says only "The installation of the system will start in 2026." The year 2027 does not appear. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-signs-contract-deploy-new-ai-optimised-supercomputer-sweden-2026-04-21_en |
| Antennas | BE (LUMI and JAIF), CY (Pharos), HU (JAIF), IE (AI2F and Luxembourg), LV (LUMI), MT CALYPSO (Pharos), SK (AI:AT) | CONFIRMED | "It will be linked with the LUMI AI Factory in Finland and the JUPITER AI-Factory in Germany" (BE); "primarily linked with AI2F ... as well as with the Luxembourg AI Factory" (IE). The other links are stated the same way. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en |
| Antennas | HR, DK, EE, PT have no factory or antenna; DK and EE in LUMI, PT in BSC | CONFIRMED | Factory list: "Finland / Czechia, Denmark, Estonia, Norway, and Poland"; "Spain / Portugal, Romania and Türkiye". None of the four appears as a host or an antenna. | https://eurohpc-ju.europa.eu/ai-factories_en |
| Supercomputers | Twelve systems on the official list | CONFIRMED | "Up to now, the EuroHPC JU has procured twelve state-of-the-art supercomputers, located across Europe." | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en |
| Supercomputers | "hosted in eleven states" | NOT CONFIRMED | The page places the 12 systems in 12 different states: DE, FI, IT, ES, LU, CZ, SI, BG, PT, EL, SE, FR. That is twelve states, not eleven. The note's own list of systems also names 12 states. | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en |
| Supercomputers | DAEDALUS available "shortly" in June 2026; Arrhenius inaugurated 8 Sep 2026 | NOT CONFIRMED (on cited page) | The list page says "DAEDALUS will be a mid-range petascale EuroHPC supercomputer" and gives no Arrhenius date. Both facts are on uncited releases: 23 June 2026 ("expected to become fully available ... shortly") and https://www.eurohpc-ju.europa.eu/eurohpc-ju-inaugurates-arrhenius-new-mid-range-supercomputer-together-naiss-sweden-2026-09-08_en ("inaugurated Arrhenius", 8 September 2026). | https://www.eurohpc-ju.europa.eu/supercomputers/our-supercomputers_en |
| Supercomputers | JUPITER exascale, inaugurated 5 Sep 2025; Alice Recoque exascale, under contract, installation from 2026 | CONFIRMED | "JUPITER is Europe's first Exascale supercomputer"; Alice Recoque release: "The installation of the system will start in 2026." | (as above and the 2025-11-18 release) |
| Supercomputers | Ireland's CASPIr has a hosting agreement and open tender; not on list | NOT CONFIRMED (no source) | The list page does not include CASPIr, which supports "not yet on the list". The sentence has no URL. The EuroHPC press listing (uncited) shows "27 March 2026 Invitation to Tender to Procure CASPIr Supercomputer". A hosting agreement was not seen on any fetched page. | (none given) |
| AI Gigafactories | InvestAI 11 Feb 2025: EUR 200 bn including EUR 20 bn Gigafactory fund | CONFIRMED | "InvestAI, an initiative to mobilise €200 billion for investment in AI, including a new European fund of €20 billion for AI gigafactories" (Publication 11 February 2025) | https://digital-strategy.ec.europa.eu/en/news/eu-launches-investai-initiative-mobilise-eu200-billion-investment-artificial-intelligence |
| AI Gigafactories | 76 submissions, 60 sites, 16 member states | CONFIRMED | "A total of 76 expressions of interest proposing to set up AI Gigafactories in 16 Member States across 60 different sites" | https://www.eurohpc-ju.europa.eu/ai-gigafactories/ai-gigafactories-consultations_en |
| AI Gigafactories | Reg. (EU) 2026/150 of 16 Jan 2026: up to 17% of capex, at least matched, JU owns the Union part at least 5 years | CONFIRMED (via PO copy; cited URL unreachable) | "shall cover up to 17 % of the capital expenditure (CAPEX)"; "One or more Participating States shall at least match the Union contribution."; "for a duration of at least five years" | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R0150 (read at publications.europa.eu/resource/celex/32026R0150) |
| AI Gigafactories | Call EUROHPC-2026-CEI-AIGF-01 opened 30 Jul 2026; up to seven; at least 3–4× an AI Factory's processors; selection early 2027 | CONFIRMED | "up to seven AI Gigafactories"; "at least three to four times the number of the most advanced AI processors currently available in the most powerful European AI factories"; "Following their selection in early 2027" | https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en ; https://eurohpc-ju.europa.eu/call-tenders-selection-artificial-intelligence-gigafactory-consortia-and-establishment-ai_en |
| AI Gigafactories | Press release gives 12 Nov 2026; call page gives 3 Dec 2026 | CONFIRMED (both as stated) | Press release: "Following the submission deadline on 12 November 2026". Call page: "Deadline date 3 December 2026, 17:00 (CET)". | (both URLs above) |
| OpenEuroLLM | Digital Europe grant 101195233; started 1 Feb 2025 for 3 years; Charles University coordinator, AMD Silo AI co-lead, 20 partners incl. ALT-EDIC; EU official languages | CONFIRMED | "grant agreement No 101195233"; "20 leading European research institutions and EuroHPC centres coordinated by Charles University (Czechia) and co-led by AMD Silo AI"; "started on February 1st, 2025, for a duration of 3 years"; "foundation models for EU official languages and beyond" | https://openeurollm.eu/deliverables ; https://alt-edic.eu/projects/openeurollm/ ; https://openeurollm.eu/ |
| OpenEuroLLM | First model weights due 31 Dec 2026; final models 31 Jan 2028 | CONFIRMED | "31 DEC 2026 First models ... Initial release of LLM models (tokenizers and model weights)"; "31 JAN 2028 Final models" | https://openeurollm.eu/deliverables |
| Frontier AI Grand Challenge | Opened 13 Feb, closed 13 Apr 2026; ≥400 bn parameters' capacity; up to 2.5% of EuroHPC capacity for one year; open models | CONFIRMED | "Opening: 13 February 2026 \| Closing: 13 April 2026"; "computational capacity equivalent to at least 400 billion parameters"; "up to 2.5% of the overall EuroHPC computing capacity for one year" | https://digital-strategy.ec.europa.eu/en/funding/turning-strategy-action-commission-launches-frontier-ai-grand-challenge |
| EUROPA | Selected 19 Jun 2026; led by Italian company Domyn; open-source model in all 24 official EU languages | CONFIRMED | "selected EUROPA, a European consortium led by the Italian company Domyn"; "an open-source artificial intelligence (AI) model covering all 24 official EU languages" (Publication 19 June 2026) | https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open |
| ALT-EDIC | Implementing Decision (EU) 2024/458 of 1 Feb 2024; seat Villers-Cotterêts | CONFIRMED (via PO copy; cited URL unreachable) | "COMMISSION IMPLEMENTING DECISION (EU) 2024/458 of 1 February 2024"; "ALT-EDIC shall have its statutory seat in Villers-Cotterêts, France." The LDS page gives 7 February 2024 as the set-up date, which is the OJ publication date. | https://eur-lex.europa.eu/eli/dec_impl/2024/458/oj |
| ALT-EDIC | Roster: 17 member states (as listed) plus Flanders, 8 observers (as listed) | CONFIRMED (for this page) | "seventeen Members States: Bulgaria, Croatia, Czechia, ..."; "eight observing Member States: Austria, Belgium, Cyprus, Estonia, Malta, Portugal, Romania, and Slovakia". Currency: see B. | https://language-data-space.ec.europa.eu/related-initiatives/alt-edic_en |
| ALT-EDIC | Offers federated data incl. languages under 10 M speakers, an open-model repository, a pooled seed fund with EuroHPC access, evaluation and certification; runs OpenEuroLLM, LLMs4EU, LLM-BRIDGE | CONFIRMED on the other cited URL (wrong URL attached) | alt-edic.eu home lists only the projects (menu: "ALT-EDIC4EU \| LLM-BRIDGE \| LLMs4EU \| OpenEuroLLM"). The offer text is on the LDS ALT-EDIC page: "languages with few speakers (less than 10 million speakers)"; "ALT-EDIC will act as a pool seed fund ... providing access to the necessary European High-Performance Computing". Move the citation. | https://alt-edic.eu/ (offer actually at https://language-data-space.ec.europa.eu/related-initiatives/alt-edic_en) |
| Compute access | Extreme Scale "Public Administration Access" track; cut-offs 4 May and 26 Oct 2026; LUMI, Leonardo, MareNostrum 5, JUPITER | CONFIRMED | "Public Administration Access – Intended for applications with PIs coming from the public sector."; "4 May 2026, 10:00 / 26 Oct 2026"; "pre-exascale systems LUMI, Leonardo, MareNostrum5, and on the exascale sy[stem]" | https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-extreme-scale-access-mode_en |
| Compute access | AI for Science: open to "users from public sector", 6-month allocations, six cut-offs a year | CONFIRMED | "users from public sector"; "The allocations are granted for six (6) months."; six 2026 cut-offs listed (27 Feb, 30 Apr, 30 Jun, 1 Sep, 30 Oct, 11 Dec) | https://www.eurohpc-ju.europa.eu/eurohpc-ju-call-proposals-ai-science-and-collaborative-eu-projects_en |
| Compute access | AI Factory modes: Playground; Fast Lane up to 50,000 GPU h; Large Scale over 50,000 GPU h | CONFIRMED | "Fast Lane access, for users already familiar with HPC requiring up to 50,000 GPU hours"; "Large Scale access ... requiring more than 50,000 GPU hours" | https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en |
| Compute access | Timings: Playground within 2 working days, Fast Lane within 4, Large Scale up to a year, two cut-offs a month | NOT CONFIRMED (on cited page) | The cited page has none of these timings. The uncited Large Scale call page (https://www.eurohpc-ju.europa.eu/large-scale-access-ai-factories_en) says "granted for a period of three, six, or twelve months" and "Access is granted within 10 working days from cut-off", and its cut-off list runs about twice a month. The 2- and 4-day figures were not seen on any fetched page. | https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en |
| Compute access | "continued pretraining fits inside one Large Scale allocation, as OpenEuroLLM's 3 million GPU hours on Leonardo show" | NOT CONFIRMED | The 3 M Leonardo hours were awarded for a synthetic-data project, not for continued pretraining: "The EuroHPC AI Factory Large Scale call has allocated 3 million GPU hours on the Leonardo Booster ... to develop 'MultiSynt: an open multilingual synthetic dataset'" (OpenEuroLLM blog, 27 May 2025) | https://openeurollm.eu/blog/multisynt-synthetic-training-data |
| Cloud and AI Development Act | Proposed 3 Jun 2026, COM(2026) 502, ordinary legislative procedure | CONFIRMED (via PO copy) | "Brussels, 3.6.2026 COM(2026) 502 final 2026/0138(COD) Proposal for a REGULATION" | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0502 |
| Cloud and AI Development Act | National cloud and AI strategy within a year; four assurance levels (L1 data in EU … L4 full supply-chain control); procurement at least Level 1 | CONFIRMED (nuance) | "Article 7 requires Member States to adopt a national cloud and AI strategy ... within one year of its entry into force."; "Level 1: where data is processed and stored in infrastructure located in the Union"; Art. 30: "contracting authorities that procure cloud computing services to procure, as a minimum requirement, Union assurance level 1". Nuance: the minimum covers procurement of cloud computing services, not all public procurement. | PO copy of 52026PC0502; https://digital-strategy.ec.europa.eu/en/policies/cloud-and-ai-development-act |
| Apply AI / AI Continent | AI Continent Action Plan (9 Apr 2025) committed EUR 10 bn to AI Factories for 2021–2027 | NOT CONFIRMED (as phrased) | The text gives a total, not a commitment to AI Factories alone: "overall investments in supercomputing infrastructures and AI Factories in the EU will reach EUR 10 billion over the 2021-2027 period". Date confirmed: "Brussels, 9.4.2025". | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025DC0165 (via PO copy) |
| Apply AI / AI Continent | Up to five Gigafactories | CONFIRMED (via PO copy) | "mobilise EUR 20 billion investment for AI infrastructure, notably targeting up to 5 AI Gigafactories across the Union" | same |
| Apply AI | 8 Oct 2025; around EUR 1 bn; public-sector flagship; "AI first"; open source; free EuroHPC access for frontier-competition winners | CONFIRMED (via PO copy) | "Brussels, 8.10.2025"; "mobilising around EUR 1 billion"; "2.11. Public sector"; "By adopting an AI first policy"; "These projects will receive free access to EuroHPC supercomputers" | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025DC0723 |
| Apply AI | "buy European" posture (in quotation marks in the note) | NOT CONFIRMED (as a quotation) | The phrase "buy European" does not appear. The nearest wording is "integrate AI building on European solutions" and "demand for European-made open source AI solutions". Drop the quotation marks or quote the text. | same |
| Data Union | 19 Nov 2025; first data labs under the AI Factories; 30 M digitised cultural objects for AI training by end 2026 | CONFIRMED (via PO copy) | "Brussels, 19.11.2025"; "the first data labs will be established under the AI Factories initiative through EuroHPC"; "making 30 million digitised cultural objects available for AI training (Q4 2026)" | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025DC0835 |
| Language Data Space | Live marketplace for language datasets; data available to ALT-EDIC | CONFIRMED | Index: "The European Marketplace for Language Data." LDS ALT-EDIC page: "This data will also be available to the ALT-EDIC." | https://language-data-space.ec.europa.eu/index_en |

#### B. Unverified claims

| Where | Claim (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| Table: Austria | AI:AT "no contract found" | FOUND | The AI:AT tender (EUROHPC/2026/CD/0002, opened 25 Feb 2026) closed on 14 April 2026. No contract award appears in the EuroHPC press releases up to 9 Oct 2026. Suggested cell: "tender closed 14 April 2026; no contract announced". | https://www.eurohpc-ju.europa.eu/acquisition-delivery-installation-and-maintenance-hardware-and-software-aiat-ai-optimised_en ; https://www.eurohpc-ju.europa.eu/media-events/press-releases_en | "Status ClosedReference EUROHPC/2026/CD/0002 ... Deadline date 14 April 2026" ; "AI:AT will be installed in Wien (Austria), at TU Wien" |
| Table: Poland PIAST | "no contract found" | FOUND (absence only) | No PIAST tender page was found. The procurements page lists only the Discoverer++ call as open, and the press listing (Mar–Oct 2026) has no PIAST contract. This is absence evidence: the note can say "no tender or contract announced by EuroHPC JU by 2026-10-10". | https://www.eurohpc-ju.europa.eu/about/procurements-supercomputers_en ; press-releases_en pages 0–2 | "Showing results 1 to 1 ... Discoverer++ AI-optimised supercomputer" |
| Table: Slovenia | SLAIF "no contract found" | FOUND (absence only) | Same as PIAST: no SLAIF tender or contract on the EuroHPC procurements page or in the press listing up to 9 Oct 2026. WebSearch on the EuroHPC domain also turned up no SLAIF tender. | same | (as above) |
| AI Gigafactories | Deadline moved from 12 Nov to 3 Dec 2026 ("extension") | NOT FOUND | Searched for an extension or corrigendum. The call page has no "extend", "amend" or "corrigendum" text; the Funding & Tenders topic JSON returned 404; WebSearch found only third-party pages that give 12 Nov. A search-engine snippet of the same call page shows 12 November, which suggests the page was changed. No official notice of the change was found. | https://eurohpc-ju.europa.eu/call-tenders-selection-artificial-intelligence-gigafactory-consortia-and-establishment-ai_en | "Deadline date 3 December 2026, 17:00 (CET)" |
| OpenEuroLLM | 3 M GPU h on Leonardo and 1.5 M on LUMI "through the AI Factory and EuroHPC calls" (cited openeurollm.eu/news is 404) | FOUND (with correction) | (a) 1.5 M GPU hours on LUMI came through the Finnish LUMI Extreme Scale Access 2025 call (26 May 2025). (b) 3 M GPU hours on Leonardo Booster came through the AI Factory Large Scale call, but for the MultiSynt synthetic dataset. (c) Since Dec 2025 the project has had strategic access of over 10 M GPU hours on LUMI, Leonardo, JUPITER and MareNostrum 5. Replace the 404 URL. | https://openeurollm.eu/blog/LUMI-Extreme-Scale-Access-2025 ; https://openeurollm.eu/blog/multisynt-synthetic-training-data ; https://www.openeurollm.eu/blog/strategic-access-EuroHPC-OpenEuroLLM | "awarded 1.5 million GPU hours ... through the Finnish LUMI Extreme Scale Access 2025 call" ; "granted strategic access across multiple EuroHPC centres, in the amount of over 10 million GPU hours" |
| OpenEuroLLM | Budget figure "only in press" | NOT FOUND (official) | No budget figure appears on openeurollm.eu (home, deliverables, launch post, first-year post) or on alt-edic.eu/projects/openeurollm. WebSearch found only press figures, which disagree with each other. Keep it [unverified]. | https://openeurollm.eu/blog/launch-press-release ; https://openeurollm.eu/blog/first-year-progress-and-next-steps | (no figure on page) |
| EUROPA | Other members, cash funding and delivery date | NOT FOUND (official) | The Commission page names only Domyn. The Domyn blog fetched (europe-role-ai-race) confirms the selection but names no partners and gives no date. A WebSearch summary named Fraunhofer and "second half of 2027", but those did not appear in the fetched page text, so they are not supplied. | https://www.domyn.com/blog/europe-role-ai-race | "On June 19, the European Commission selected the Domyn-led Europa consortium to build Europe's frontier AI model" |
| ALT-EDIC | Roster current; "Germany and Sweden appear on no fetched list" | FOUND (contradicts the note) | ALT-EDIC's own member page lists 17 member states plus Flanders as Members, and as Observers AT, BE, CY, EE, IS (Iceland), MT, PT, RO, **SE (Sweden, via Linköping University)** and SK. That is nine EU observers plus Iceland. Germany is absent. The sentence about Sweden is wrong; the observer count should be 9 EU states plus Iceland on this page. | https://alt-edic.eu/member-states/ | "Observers ... SE – Sweden \| Linköping University \| SK – Slovakia \| Ministry of Education" |
| Compute access | Whether the industrial AI Factory modes are free for public bodies | FOUND | The industrial modes are not for public bodies: they are open to industry only, free for SMEs and start-ups, and pay-per-use for others. Public authorities apply through the AI for Science and Collaborative EU Projects call, which is free. | https://www.eurohpc-ju.europa.eu/ai-factories/faqs-ai-factories_en ; https://www.eurohpc-ju.europa.eu/ai-factories/ai-factories-access-modes_en | "The AI Factories for Industrial Innovation call is open for applicants coming from industrial sector only." ; "Access time offered via the EUROHPC JU access calls is free of charge." |

### Section 2 (examples only)

#### A. Verification

| Where (subsection or table row) | Claim | Verdict | Evidence (quote ≤25 words, or what the page says) | URL |
|---|---|---|---|---|
| R1–R4 "European examples" | No route names a European example with a URL. R1 points to section 5. R2 names vehicles (an AI Factory's model programme, "the Commission's Large AI Grand Challenge consortium", OpenEuroLLM, EuroHPC-funded projects) without URLs. | n/a (nothing to check) | Observation, not a verdict: R2 says "Large AI Grand Challenge" but section 4 describes the Frontier AI Grand Challenge and EUROPA. Check that this name is intended. | (none) |

#### B. Unverified claims

| Where | Claim (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| — | No **[unverified]** marks in section 2 (the cost bands are **[reconstructed]** and out of scope) | n/a | — | — | — |

### Section 6

#### A. Verification

| Where (subsection or table row) | Claim | Verdict | Evidence (quote ≤25 words, or what the page says) | URL |
|---|---|---|---|---|
| All of section 6 | No claim in section 6 carries a URL (it is the author's reading, as the section says) | n/a (nothing to check) | Consistency observations against the section 4 sources: (1) the language-cluster table's "PIAST for Moldova's antenna" matches the antenna page ("linking ... to PIAST AI Factory in Poland"); (2) its "Serbia's ... antennas" under South Slavic with SLAIF: Serbia's antenna is linked to Pharos and IT4LIA, not SLAIF ("integrate ... with the EuroHPC Pharos AI Factory in Greece and IT4LIA AI Factory in Italy"), which the vehicle column partly reflects; (3) "NLAIF from 2028" has no source in section 4. | https://www.eurohpc-ju.europa.eu/eurohpc-ju-selects-ai-factory-antennas-broaden-ai-factories-initiative-2025-10-13_en |

#### B. Unverified claims

| Where | Claim (short) | Outcome | Fact as sourced | URL (accessed 2026-10-10) | Quote |
|---|---|---|---|---|---|
| — | No **[unverified]** marks in section 6 | n/a | — | — | — |

### Summary

| Section | Claims checked | Confirmed | Not confirmed | Unclear | Unverified | Found | Not found |
|---|---|---|---|---|---|---|---|
| 4 | 56 | 43 | 12 | 1 | 9 | 6 | 3 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

How to read the counts: the 43 confirmed include one fact confirmed on a different cited URL (the ALT-EDIC offer). The 12 NOT CONFIRMED in section 4 fall into two groups. Six are facts found on uncited official pages, so only the citation needs changing: the round dates, Bulgaria's tender, Greece's DAEDALUS, DAEDALUS and Arrhenius on the supercomputers page, CASPIr, and the AI Factory mode timings (the 2- and 4-working-day figures were not found anywhere). Six are wrong or overstated: "eleven states" (the page gives twelve), Romania's 1 Sept 2026 date, Sweden "online 2027", "EUR 10 bn to AI Factories", "buy European" as a quotation, and the 3 M Leonardo hours offered as evidence for continued pretraining. Seven section 4 verdicts rely on Publications Office copies, because the cited EUR-Lex URLs could not be fetched.
