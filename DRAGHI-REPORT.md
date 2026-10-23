# The Draghi report and the EU-27's critical government data

**Authored note, 2026-10-23. Not generated, and not part of the model, the JSON bundle, the web app, the PDFs, the
reader or `/ask`.** `run.sh data` never touches it. It reads Mario Draghi's *The future of European competitiveness*
(European Commission, September 2024) against this project's per-state registers. Decision #118 records why it is
written this way. It ranks nothing. Section 4 lists the states alphabetically, and the order carries no meaning (#10, #77).
It gives no per-state cost or capacity figure (#72, #73).

**Two kinds of statement, kept apart.**
- What Draghi says appears as a verbatim quotation followed by its page, “…” (A p. 36) or (B p. 84). A and B are the
  report's two parts. The page is the page of the PDF file: Part B's printed page numbers match it, and Part A's run two
  lower. Every quotation is a row of [`docs/draghi-quotes.csv`](docs/draghi-quotes.csv), found mechanically on that page
  of the hashed PDF (`python3 model/draghi_note.py quotes`). The hashes are in
  [`assets/reports/MANIFEST.csv`](assets/reports/MANIFEST.csv).
- What the project knows about a state is cited by the claim id its own document prints, for example
  `indicator:NL:C2` reads “No”. `model/draghi_note.py check` compares each such text with the committed bundle, so a
  value here can never drift from the value a reader of the state's report sees. A fact the project withholds as
  disputed (#89) or still lists as a gap is not cited and is never filled here.

**What is analysis.** Everything else in the note is the author's analysis and is marked as such. The author is a
claude-opus-5-5 session, working from the text extracted from the two PDFs. Two agents on the same model extracted
quotations, and every one was checked mechanically against its page. No other model has reviewed the analysis, and no
person has read it (TODO.md).

---

## Contents

- [1. The report](#1-the-report)
- [2. What it says about hosting state data](#2-what-it-says-about-hosting-state-data)
- [3. What it means for this project](#3-what-it-means-for-this-project)
- [4. The twenty-seven](#4-the-twenty-seven)
- [5. Caveats](#5-caveats)
- [Sources](#sources)

---

## 1. The report

Ursula von der Leyen asked Mario Draghi, a former president of the ECB, for the report, and the Commission published it
on 9 September 2024 in two parts:
- **Part A**, *A competitiveness strategy for Europe*: 73 pages of diagnosis and headline proposals.
- **Part B**, *In-depth analysis and recommendations*: 328 pages, sector by sector.

The report carries its own status line: “This document should not be considered as representative of the European
Commission’s official position.” (A p. 2). It is therefore one author's recommendation to the Commission, neither law nor
Commission policy, and this note treats it as such.

Its scope matches the project's in one respect and departs from it in another:
- **The same unit.** Like the project, it counts the 27 member states as the unit that acts.
- **A different direction.** Most of its proposals move a decision from the member states to the EU level, or
  coordinate the states from there.

That tension runs through everything below. The project describes what each state holds and where it is hosted today.
Draghi argues about who should decide where it is hosted tomorrow.

The two PDFs are archived in `assets/reports/draghi-2024/`. They are gitignored, and the tracked manifest records their
URLs and hashes. `python3 model/draghi_note.py fetch` restores and verifies them.

## 2. What it says about hosting state data

**The dependency, as Draghi measures it.** He finds that “The three US-based cloud ‘Hyperscalers’ (Amazon Web Services, Microsoft Azure and Google Cloud) account
for 65% of this market.” (B p. 77), and that “Europe’s dependence on cloud services developed and run by US companies is massive”
(A p. 59). Part B adds that “EU cloud providers’ share decreased to under 16% in 2021, with the largest operator (DT)
capturing only 2% of the EU market” (B p. 77). On data leaving the EU, Part B says the ‘data value loss’ “is today
estimated at 90%” (B p. 67). More broadly, “The EU relies on foreign countries for over 80% of digital products,
services, infrastructure and intellectual property” (A p. 59). All of these are EU-wide figures. None of them is a
figure for any one state, and this note never uses one as such (section 3).

**The strategic line.** Draghi does not propose building an alternative to the US providers: “It is too late for the
EU to try and develop systematic challengers to the major US cloud providers” (A p. 36). He argues instead that “it is
important that EU companies maintain a foothold in areas where technological sovereignty is required, such as security
and encryption” (A p. 26). He also argues that “for reasons of European sovereignty, the EU should ensure that it has a
competitive domestic industry that can meet the demand for” (A p. 36) what it calls sovereign cloud solutions.

**What member states already do, as he describes it.** He writes that “More recently, several Member States have
promoted ‘secure’ cloud setups where EU-owned Infrastructure-as-a-Service providers cooperate with hyperscalers’
distribution but retain control over sensitive elements of security and encryption” (B p. 77). These setups “are
Europe’s second-best available option today for data security and territorial sovereignty” (B p. 77). He does not say
which states he means.

**The proposals that bear directly on government data.** All of them are in Part B's *EU Cloud and AI Development Act*:
- **A single procurement and residency policy.** Its central proposal is “A single EU-wide policy for public
  administrations’ procurement of cloud service and data residency requirements, requiring as a minimum EU sovereign
  control of key elements for security and encryption.” (B p. 84).
- **An exception for sensitive areas.** The policy would apply “with exceptions allowed only in nationally sensitive
  areas (e.g. defence, home affairs and justice)” (B p. 84).
- **Passporting.** Next to it: “Guarantee a Single Market passporting regime for all EU-provided cloud services,
  eliminating the possibility for Member States to ‘gold-plate’ protection requirements beyond the requirements of the
  GDPR and the AI Act.” (B p. 84).
- **Common rules with the hyperscalers.** Then “EU-wide sensitive data security policies for collaboration between
  private EU cloud providers with US hyperscalers” (B p. 84).
- **The objective behind them.** The objective he sets is to “Retain control of security, data encryption and
  residency capabilities within EU companies and institutions and facilitate the consolidation of EU cloud providers.”
  (B p. 82).
- **The procurement cost of fragmentation.** Part A gives the reason: “multiple different national rules in public
  procurement generate high ongoing costs for cloud providers” (A p. 32), so “the EU should legislate mandatory
  standards for public sector procurement, thereby levelling the playing field for EU companies against larger non-EU
  players” (A p. 36).

**Networks and connectivity.** On 5G security the report finds that “Its 2023 Implementation Report found that 14 Member
States have no restrictions on high-risk suppliers or other key measures in place.” (B p. 72). It proposes to “Enforce
compliance with the EU Toolbox for 5G security within a set timeframe and periodically evaluate Member States’ network
plans to ensure that sensitive elements are from trusted vendors, and preferably from EU providers.” (B p. 76). It also
notes that cybersecurity obligations are set state by state: “Examples include cybersecurity standards, so-called
‘Lawful Interception’ requirements” (B p. 70). For government communications, IRIS² “will provide the first SatCom
system and a secure network for EU governments protected using quantum encryption” (B p. 72), and Part B adds that
“Space assets should be recognised as critical security infrastructure and be granted the relevant level of
protection.” (B p. 185). The 14 states are not named either.

**Compute.** EuroHPC is the one place where the report names host states. It says “the EU has created a large public
infrastructure for computing capacity located across six Member States” (A p. 36). Then: “Three EU supercomputers (Lumi
in Finland, Leonardo in Italy and Mare Nostrum 5 in Spain) are in the top ten worldwide” (B p. 78). Draghi wants more of
it, spread out: “Additional cloud and storage capabilities should be physically distributed throughout Europe, also to
favour multi-location AI training” (B p. 83).

**Public administration.** For Draghi, digitalisation is a means for the state itself: “Digitalisation and the
deployment of artificial intelligence (AI) are also essential to the ability of public administrations to deliver
European public goods, for example in the field of health, justice, education, welfare, mobility and environmental
protection.” (B p. 67). Among his simplification proposals: “In parallel, full cross-border interoperability solutions
among public sector bodies should be ensured through ambitious implementation of the Interoperable Europe Act.”
(B p. 323). He also wants the ‘once only’ and ‘digital by design’ principles enforced, “including fully digitalising
business-to-authority reporting not only at the EU level, but also in Member States.” (B p. 323). On health data, which
is one of this project's holding classes: “National health data access bodies have a pivotal role as they are tasked
to decide on data access applications.” (B p. 200).

**Data protection, state by state.** The report treats national variation in the GDPR as a cost: “GDPR in particular
has been implemented with a large degree of fragmentation which undermines the EU’s digital goals” (A p. 71). Part B
explains that the GDPR gives member states “the possibility to define privacy rules in 15 areas, leading to
fragmentation and legal uncertainty” (B p. 319). It points to “inconsistent enforcement by national Data Protection
Authorities (DPAs), and the fact that some Member States have several DPAs doing so (e.g. 16 in Germany)” (B p. 319).
It also records that “However, in December 2023, Member States in the Justice and Home Affairs Council formation
resisted further harmonisation” (B p. 319). Its one worked example, the age of digital consent, is the passage that
names 26 of the 27 states (section 4).

**Defence data.** The report stays at the level of the industry, not of command systems or their hosting:
- It records that “78% of procurement spending went to non-EU suppliers, out of which 63% went to the US” (A p. 62).
- It proposes to “Introduce a reinforced European preference principle and substantive incentive mechanisms to
  valorise European defence solutions and excellence over non-EU solutions.” (B p. 169).
- It proposes to “Entrust a centralised EU Defence Industry Authority to perform an EU defence joint programming and
  procurement function, i.e. to procure centrally on behalf of Member States.” (B p. 170).

**How decisions would be taken.**
- **Coordination.** Coordination outside fiscal policy would move into a new framework: “The Competitiveness
  Coordination Framework would only address EU-level strategic priorities – ‘EU Competitiveness Priorities’ –
  formulated and adopted by the European Council.” (B p. 311).
- **Groups of states.** Multi-country projects could be run by a subset of states: “Launch multi-country industrial
  projects potentially activated only by a sub-group of interested Member States.” (B p. 312). Under the current budget
  they could be financed through “existing instruments, such as the European Digital Infrastructure Consortia and the
  reprogramming of Cohesion Policy funds and of the RRF to fulfil STEP objectives.” (B p. 312).
- **Majority voting.** “The so-called ‘passerelle’ clause could be leveraged to generalise voting by qualified
  majority in all policy areas in the Council.” (B p. 315).
- **Enhanced cooperation.** Where that fails, “the next-best option is for like-minded groups of Member States to resort
  to enhanced cooperation” (A p. 70).
- **Investment screening.** On foreign investment: “At present, FDI screening is a national competence, with Member
  States only required to exchange notifications and information.” (A p. 23).

## 3. What it means for this project

The following is the author's analysis.

**3.1 The procurement proposal sorts each state's holdings in three ways.** Take the B p. 84 proposals as a whole,
whether or not they are ever adopted. They divide what this project describes into three questions, each of which can
be answered per state from facts the project already prints:

- **The exception.** Does the holding sit in a “nationally sensitive” area? Draghi's examples are “defence, home affairs
  and justice” (B p. 84). The project's `defence_command`, `intelligence`, `police_records`, `judicial_criminal` and
  `border_control` classes fall inside that wording on any reading. The identity registers are the open case. Whether a
  civil registry, a population register or an eID scheme is “home affairs” depends on which ministry runs it, and the
  project prints that ministry as the holding's operator. Where the operator is an interior ministry, the exception
  plausibly reaches the register. Where it is a tax agency, a statistics office or a digital-affairs body, it plausibly
  does not. Section 4 gives each state's printed operator.
- **Gold-plating.** Would passporting reach a national rule? A statute that requires government data to stay under
  national jurisdiction is the project's indicator L1. A sovereign-cloud certification that requires immunity from
  non-EU law is L3. Either is the kind of national protection requirement that passporting would put in question
  outside the exception, because it eliminates “the possibility for Member States to ‘gold-plate’ protection
  requirements beyond the requirements of the GDPR and the AI Act.” (B p. 84). Where L1 or L3 is printed as Yes or
  Partly, the state has something the proposal would bear on directly.
- **The floor.** The proposal's minimum is “EU sovereign control of key elements for security and encryption”
  (B p. 84). That is EU control, not national control, and it is a minimum. A state that already runs its own
  government cloud (C2) or data centres (C1) is above it for what it hosts there. What the proposal would change for
  that state is the rule for everything else it buys from the market.

**3.2 Candidate additions, recorded and not made.** None of these is a change to the model in this note. Each is a
`TODO.md` item. Any categorical label would need the review that #79 requires.

- **A sensitive-area carve-out label per holding.** It would be derived from the printed operator, using the B p. 84
  wording.
- **The state's 5G-toolbox status.** Draghi cites the Commission's 2023 implementation report for the 14 states that
  “have no restrictions on high-risk suppliers or other key measures in place” (B p. 72), but he names none. The
  implementation report itself would have to be fetched and quoted, state by state.
- **Which states run the ‘secure’ cloud setups Draghi describes** (B p. 77). The project's C2 and L3 already cover part
  of this. The rest would need sources naming each programme.
- **What became of the B p. 84 proposals after September 2024.** This note does not say, because it fetched nothing on
  that question.

**3.3 What it does not change.** The scope rule stays as it is. Draghi's vehicles are EU-level, and the project counts
only the 27 member states as holders, so the EU institutions are not added (CLAUDE.md, scope). His figures are EU-wide,
and none of them becomes a per-state fact: an EU-wide market share says nothing about where one state's tax register
runs. The placements stay without a score (#10, #77). The report argues for the EU as one buyer, and that is not a reason
to order the states.

**3.4 Where the report names states at all.** Its digital chapter names a state only for the EuroHPC hosts, one
semiconductor example (the Netherlands) and in source notes, and its cloud section names none.
States appear mainly in its energy, pharma, skills and investment chapters, in figure notes, and in the one GDPR
footnote. An agent extracted 324 such mentions across both parts, and every one was checked against its page. Section
4 quotes the one that bears most on this project for each state, and says so when the closest is about something else.

## 4. The twenty-seven

Each entry has four parts:
- where Draghi names the state, quoted;
- the author's reading of how the B p. 84 proposals land on its holdings;
- the facts the project prints today, by claim id;
- the questions this leaves open.

### Austria (AT)

#### Where Draghi names it
Only in the GDPR footnote: “14 in Austria, Bulgaria, Cyprus, Spain, Italy, Lithuania;” (B p. 319). Austria is also named
in innovation and competition passages that do not bear on data.

#### Proposals that land on its holdings
Analysis. The civil registry and the eID registration data are run by the interior ministry, so both plausibly sit
inside the home-affairs exception. Austria runs government data centres and a government cloud, which would keep the
EU-wide policy to what it buys outside them.

#### What the project prints today
- `record:AT:civil_registry:operator` reads “Federal Minister of the Interior acts as processor of the ZPR”.
- `record:AT:digital_identity_credentials:operator` reads “Federal Minister of the Interior and the Source PIN Register Authority process E-ID registration data”.
- `indicator:AT:C1` reads “Yes”.
- `indicator:AT:C2` reads “Yes”.

#### Open questions
- A jurisdiction requirement (L1) is not yet sourced. Without it, whether passporting would bear on Austrian law cannot be said.

### Belgium (BE)

#### Where Draghi names it
Only in the GDPR footnote: “The age of consent is 13 in Belgium, Denmark, Estonia, Finland, Latvia, Malta, Portugal,
Sweden;” (B p. 319). Belgium is also named in the energy and pharma chapters.

#### Proposals that land on its holdings
Analysis. The National Register is run by the FPS Interior and plausibly sits inside the home-affairs exception. The
federal authentication service is run by BOSA, a policy-and-support body, and plausibly does not. In Belgium the B p. 84
policy would therefore likely split the identity stack between two regimes.

#### What the project prints today
- `record:BE:civil_registry:operator` reads “The National Register is managed by the Directorate-General Identity and Civil Affairs of the FPS Interior”.
- `record:BE:digital_identity_credentials:operator` reads “FPS Policy and Support (BOSA), DG Simplification and Digitization provides the FAS”.
- `indicator:BE:C1` reads “Yes”.
- `indicator:BE:C2` reads “Yes”.

#### Open questions
- L1 and L3 are not yet sourced.
- Who BOSA's subcontractors are matters under any EU-wide policy. `record:BE:digital_identity_credentials:hosting` reads
  “BOSA uses subcontractors as data processors (not named)”.

### Bulgaria (BG)

#### Where Draghi names it
Only in the GDPR footnote: “14 in Austria, Bulgaria, Cyprus, Spain, Italy, Lithuania;” (B p. 319). Bulgaria is also named
in energy passages and among the states whose R&D investment is below 1%.

#### Proposals that land on its holdings
Analysis. Bulgaria runs government data centres and a government cloud. The project prints no operator for its identity
registers, so it cannot yet say which holdings the exception would reach.

#### What the project prints today
- `indicator:BG:C1` reads “Yes”.
- `indicator:BG:C2` reads “Yes”.

#### Open questions
- The state-controlled eID indicator is withheld as disputed. Until it is corrected, the identity side cannot be read
  against the proposal.
- L1 and L3 are not yet sourced.

### Croatia (HR)

#### Where Draghi names it
Twice, and only in footnotes: the GDPR one, “16 in Germany, Hungary, Croatia, Ireland, Luxembourg, the Netherlands,
Poland, Romania, and Slovakia.” (B p. 319), and a list of energy-modernisation recipients.

#### Proposals that land on its holdings
Analysis. Croatia has a partial jurisdiction requirement, so passporting would bear on it outside the exception. Its
civil registry system is run by the state administration body for general administration, and its eID by the body for
digital transformation. Neither is plainly “home affairs”, so whether the exception reaches them turns on how the
proposal would define it.

#### What the project prints today
- `indicator:HR:L1` reads “Partly”.
- `record:HR:civil_registry:operator` reads “The state administration body for general administration sets up and runs the single information system for the civil registers”.
- `record:HR:digital_identity_credentials:operator` reads “state administration body responsible for digital transformation”.
- `indicator:HR:C2` reads “Yes”.

#### Open questions
- Which sectors the partial requirement covers decides how much of it the exception would protect.

### Cyprus (CY)

#### Where Draghi names it
Only in the GDPR footnote: “14 in Austria, Bulgaria, Cyprus, Spain, Italy, Lithuania;” (B p. 319). Cyprus is also named
in automotive and pharma data notes.

#### Proposals that land on its holdings
Analysis. The civil registry is run by the Civil Registry and Migration Department. Migration is plainly home affairs,
so the exception plausibly reaches it. The eID's printed dependency is an EU provider, which already meets an EU floor
that asks for EU, not national, control.

#### What the project prints today
- `record:CY:civil_registry:operator` reads “Civil Registry and Migration Department, with District Administration offices as registration authorities”.
- `record:CY:digital_identity_credentials:foreign_dependency` reads “EU provider”.

#### Open questions
- The capacity indicators C1 and C2 are withheld because their source is gone (HTTP 404), so whether Cyprus has its own
  government hosting cannot be read here.

### Czechia (CZ)

#### Where Draghi names it
In the GDPR footnote, as “15 in the Czech Republic, Greece, France;” (B p. 319), and in energy passages. It is named
nowhere on data or digital matters.

#### Proposals that land on its holdings
Analysis. Czechia is one of two states for which the project prints a sovereign-cloud certification as Yes. That kind
of national protection requirement is what passporting would remove outside the exception. Czechia also has a partial
jurisdiction requirement and runs its own government cloud, so B p. 84 bears on its existing rules on two counts.

#### What the project prints today
- `indicator:CZ:L1` reads “Partly”.
- `indicator:CZ:L3` reads “Yes”.
- `indicator:CZ:C2` reads “Yes”.

#### Open questions
- Whether the certification's requirements go beyond “EU sovereign control of key elements for security and encryption”
  (B p. 84). If they do, they are what the proposal calls gold-plating.

### Denmark (DK)

#### Where Draghi names it
In the GDPR footnote, “The age of consent is 13 in Belgium, Denmark, Estonia, Finland, Latvia, Malta, Portugal, Sweden;”
(B p. 319), and on regulatory burden. Denmark is also named in energy, pharma and pension passages.

#### Proposals that land on its holdings
Analysis. The CPR Office sits in the Ministry of Research, Education and Digitalisation, not in home affairs, so the
civil registry plausibly falls under the EU-wide policy and not the exception. The partial jurisdiction requirement is
what passporting would bear on.

#### What the project prints today
- `indicator:DK:L1` reads “Partly”.
- `record:DK:civil_registry:operator` reads “CPR-administrationen (CPR Office), placed in the department of the Ministry of Research, Education and Digitalisation”.
- `indicator:DK:C2` reads “Yes”.
- `record:DK:central_bank:foreign_dependency` reads “EU provider”.

#### Open questions
- Whether the CPR's hosting stays inside the government cloud. If it does, the proposal's floor matters only for what
  Denmark buys outside it.

### Estonia (EE)

#### Where Draghi names it
Only in the GDPR footnote: “The age of consent is 13 in Belgium, Denmark, Estonia, Finland, Latvia, Malta, Portugal,
Sweden;” (B p. 319). Estonia is also named in data notes on other topics.

#### Proposals that land on its holdings
Analysis. The civil registry is run by the Ministry of the Interior, so it plausibly sits inside the exception. Estonia
runs government data centres and a government cloud.

#### What the project prints today
- `record:EE:civil_registry:operator` reads “Siseministeerium (Ministry of the Interior)”.
- `indicator:EE:C1` reads “Yes”.
- `indicator:EE:C2` reads “Yes”.

#### Open questions
- L1 and L3 are not yet sourced.
- Every hosting row is still a gap, so it cannot be said what Estonia buys outside its own capacity.

### Finland (FI)

#### Where Draghi names it
As a EuroHPC host: “Three EU supercomputers (Lumi in Finland, Leonardo in Italy and Mare Nostrum 5 in Spain) are in the
top ten worldwide” (B p. 78). Finland is also named in the GDPR footnote and in energy, raw-materials and skills
passages.

#### Proposals that land on its holdings
Analysis. The Population Information System and the eID are both run by the Digital and Population Data Services
Agency, not by a home-affairs body. Both plausibly fall under the EU-wide policy rather than the exception, and the
partial jurisdiction requirement is what passporting would bear on. Draghi's wish for compute “physically distributed
throughout Europe” (B p. 83) names a capability that Finland already hosts. The project does not count that capability,
which is research rather than government data.

#### What the project prints today
- `indicator:FI:L1` reads “Partly”.
- `record:FI:civil_registry:operator` reads “Digital and Population Data Services Agency (DVV) carries the controller duties for the Population Information System”.
- `indicator:FI:C2` reads “Yes”.

#### Open questions
- Whether Finland's partial requirement covers the population data. If so, it would sit outside the exception and
  inside the proposal's reach.

### France (FR)

#### Where Draghi names it
On defence: “in France, Germany and Italy in the field of land defence) [see the Box below].” (B p. 162). France is also
named in the space, innovation-agency, GDPR and energy passages.

#### Proposals that land on its holdings
Analysis. France is the second state for which the project prints a sovereign-cloud certification as Yes, and the same
tension with passporting applies as for Czechia. The national identifier register is run by Insee, a statistics office,
and the eID by DINUM, the interministerial digital directorate. Neither is plainly home affairs.

#### What the project prints today
- `indicator:FR:L3` reads “Yes”.
- `record:FR:civil_registry:operator` reads “Insee has managed the RNIPP since its creation”.
- `record:FR:digital_identity_credentials:operator` reads “DINUM (Direction interministérielle du numérique)”.
- `indicator:FR:C2` reads “Yes”.

#### Open questions
- How the certification compares with the B p. 84 floor.
- L1 is not yet sourced.

### Germany (DE)

#### Where Draghi names it
On data-protection enforcement: “inconsistent enforcement by national Data Protection Authorities (DPAs), and the fact
that some Member States have several DPAs doing so (e.g. 16 in Germany)” (B p. 319). Of the 324 extracted mentions, 55 name Germany,
mostly in energy, space, innovation and pharma passages, some as part of an organisation's name.

#### Proposals that land on its holdings
Analysis. The national identification number is held by the Federal Central Tax Office, a tax body, so the exception
plausibly does not reach it. The partial jurisdiction requirement is what passporting would bear on. The report counts
Germany's multiple data-protection authorities as a cost of fragmentation. Seen from this project, the same federal
structure is why one German register can be hosted in several places.

#### What the project prints today
- `indicator:DE:L1` reads “Partly”.
- `record:DE:civil_registry:operator` reads “The Federal Central Tax Office (BZSt) stores the national personal identification number (Identifikationsnummer)”.
- `indicator:DE:C2` reads “Yes”.

#### Open questions
- The project describes the federal registers. Which Land-level registers an EU-wide policy would reach is outside what
  it holds.

### Greece (EL)

#### Where Draghi names it
Only in the GDPR footnote: “15 in the Czech Republic, Greece, France;” (B p. 319). Greece is also named in energy
permitting and other data notes.

#### Proposals that land on its holdings
Analysis. Authentication for gov.gr is controlled by the Ministry of Digital Governance, not home affairs, so it
plausibly falls under the EU-wide policy. Greece runs government data centres and a government cloud.

#### What the project prints today
- `record:EL:digital_identity_credentials:operator` reads “Ministry of Digital Governance is the controller for the authentication services of gov.gr”.
- `indicator:EL:C1` reads “Yes”.
- `indicator:EL:C2` reads “Yes”.

#### Open questions
- L1 and L3 are not yet sourced.

### Hungary (HU)

#### Where Draghi names it
Only in the GDPR footnote, “16 in Germany, Hungary, Croatia, Ireland, Luxembourg, the Netherlands, Poland, Romania, and
Slovakia.” (B p. 319), and in energy passages.

#### Proposals that land on its holdings
Analysis. Hungary has a partial jurisdiction requirement and, the project prints, no sovereign-cloud certification. Its
eID is provided by a designated company. Its identity registers carry printed hosting rules that restrict processing
to state bodies. Those are national rules of the kind passporting would test, unless they fall inside the exception.

#### What the project prints today
- `indicator:HU:L1` reads “Partly”.
- `indicator:HU:L3` reads “No”.
- `record:HU:digital_identity_credentials:operator` reads “IdomSoft Zrt. designated as digital citizenship service provider”.
- `record:HU:civil_registry:hosting` reads “Data processing for the SZL may only be outsourced to a state administrative body or a wholly state-owned company”.

#### Open questions
- The capacity and key indicators (C1, C2, K1, K2) are withheld as disputed, so the floor test cannot be applied yet.

### Ireland (IE)

#### Where Draghi names it
Only in the GDPR footnote: “16 in Germany, Hungary, Croatia, Ireland, Luxembourg, the Netherlands, Poland, Romania, and
Slovakia.” (B p. 319). Ireland is also named in energy permitting and R&D passages.

#### Proposals that land on its holdings
Analysis. Ireland is the one state where the project prints a holding that depends on a non-EU provider, for emergency
communications. Defence command is printed as mixed. Defence falls inside the exception. Emergency communications is
not named in the exception, and Draghi's 5G-toolbox proposal (B p. 76) is the closer fit. The civil registry is run by
the Registrar General.

#### What the project prints today
- `record:IE:emergency_communications:foreign_dependency` reads “Non-EU provider”.
- `record:IE:defence_command:foreign_dependency` reads “Mixed”.
- `record:IE:civil_registry:operator` reads “an tArd-Chláraitheoir (Registrar General)”.
- `indicator:IE:C2` reads “Yes”.

#### Open questions
- Whether emergency communications counts as “home affairs”. If it does, the one printed non-EU dependency would sit
  outside the EU-wide policy.

### Italy (IT)

#### Where Draghi names it
As a EuroHPC host: “Three EU supercomputers (Lumi in Finland, Leonardo in Italy and Mare Nostrum 5 in Spain) are in the
top ten worldwide” (B p. 78). Also on public-sector digitalisation: “Online tools and digitalisation (Netherlands, Italy,
Portugal, Spain).” (B p. 16).

#### Proposals that land on its holdings
Analysis. Italy is the one state where the project prints a jurisdiction requirement as Yes for government data
generally. Outside the exception, passporting would bear on that requirement directly. Its sovereign-cloud certification is
printed as Partly. The civil registry is run by the Ministry of the Interior and plausibly sits inside the exception.
The eID is run by an open set of accredited public and private entities, which the EU-wide policy would plainly reach.

#### What the project prints today
- `indicator:IT:L1` reads “Yes”.
- `indicator:IT:L3` reads “Partly”.
- `record:IT:civil_registry:operator` reads “Ministry of the Interior; Sogei S.p.A. provides the technical operation”.
- `record:IT:digital_identity_credentials:operator` reads “Open set of public and private entities accredited by AgID”.

#### Open questions
- Whether a government cloud is in operation (C2) is not yet sourced.

### Latvia (LV)

#### Where Draghi names it
Only in the GDPR footnote: “The age of consent is 13 in Belgium, Denmark, Estonia, Finland, Latvia, Malta, Portugal,
Sweden;” (B p. 319). Latvia is also named in energy passages.

#### Proposals that land on its holdings
Analysis. The population register's holder is the Office of Citizenship and Migration Affairs. Migration is plainly
home affairs, so the exception plausibly reaches it. Latvia's eID is split between a private provider and a state
company, and the EU-wide policy would bear on the private part. Latvia has a partial jurisdiction requirement.

#### What the project prints today
- `indicator:LV:L1` reads “Partly”.
- `record:LV:civil_registry:operator` reads “The controller and holder of the Register is PMLP (Office of Citizenship and Migration Affairs)”.
- `record:LV:digital_identity_credentials:operator` reads “two eID providers: Smart-ID and the state company LVRTC”.
- `indicator:LV:C2` reads “Yes”.

#### Open questions
- Every hosting row is still a gap.

### Lithuania (LT)

#### Where Draghi names it
Only in the GDPR footnote: “14 in Austria, Bulgaria, Cyprus, Spain, Italy, Lithuania;” (B p. 319). Lithuania is also
named in energy, R&D and Blue Card passages.

#### Proposals that land on its holdings
Analysis. Lithuania has a partial jurisdiction requirement, and it runs government data centres and a government cloud.
The project prints no operator for its identity registers, so it cannot yet say which holdings the exception would
reach.

#### What the project prints today
- `indicator:LT:L1` reads “Partly”.
- `indicator:LT:C1` reads “Yes”.
- `indicator:LT:C2` reads “Yes”.

#### Open questions
- Identity-register operators are not yet sourced.

### Luxembourg (LU)

#### Where Draghi names it
Only in the GDPR footnote: “16 in Germany, Hungary, Croatia, Ireland, Luxembourg, the Netherlands, Poland, Romania, and
Slovakia.” (B p. 319). Luxembourg is also named in an R&D passage and as the Publications Office's seat.

#### Proposals that land on its holdings
Analysis. Luxembourg's reference digital identity comes from a qualified trust-service provider, which the EU-wide
policy would plainly reach. Luxembourg runs government data centres and a government cloud.

#### What the project prints today
- `record:LU:digital_identity_credentials:operator` reads “LuxTrust is a qualified trust service provider and a reference digital-identity provider (LuxTrust credentials)”.
- `indicator:LU:C1` reads “Yes”.
- `indicator:LU:C2` reads “Yes”.

#### Open questions
- L1, L2 and L3 are not yet sourced.

### Malta (MT)

#### Where Draghi names it
Only in the GDPR footnote: “The age of consent is 13 in Belgium, Denmark, Estonia, Finland, Latvia, Malta, Portugal,
Sweden;” (B p. 319). Malta is also named in energy permitting and in data notes.

#### Proposals that land on its holdings
Analysis. Malta's eID accounts are registered by the Identity Cards Unit. The project prints too little else to read
the proposal against.

#### What the project prints today
- `record:MT:digital_identity_credentials:operator` reads “Identity Cards Unit registers e-ID (virtual) accounts”.

#### Open questions
- C1 and C2 are withheld because their source is gone (HTTP 404).
- L1, L2 and L3 are not yet sourced.
- Every hosting row is still a gap.

### Netherlands (NL)

#### Where Draghi names it
On semiconductors: “Japan and some Member States (e.g. the Netherlands) in key materials and equipment” (B p. 86). On
public-sector digitalisation: “Online tools and digitalisation (Netherlands, Italy, Portugal, Spain).” (B p. 16). Also
in the GDPR footnote.

#### Proposals that land on its holdings
Analysis. The Netherlands shows the market side of the proposal. The project prints that it has no
government cloud in operation and no sovereign-cloud certification, while it does run government data centres. Several
printed hosting facts name private operators. These are the holdings the EU-wide floor would govern. DigiD is
controlled by the interior minister (BZK), so it plausibly sits inside the exception.

#### What the project prints today
- `indicator:NL:C2` reads “No”.
- `indicator:NL:L3` reads “No”.
- `indicator:NL:C1` reads “Yes”.
- `record:NL:digital_identity_credentials:operator` reads “Minister of BZK is controller; DigiD is managed by Logius”.
- `record:NL:customs:hosting` reads “IBM modifies and manages (beheert)”.

#### Open questions
- Whether the private operators printed for customs and other holdings would meet the B p. 84 minimum is a question
  about their contracts, which the project does not hold.

### Poland (PL)

#### Where Draghi names it
Only in footnotes: the GDPR one, “16 in Germany, Hungary, Croatia, Ireland, Luxembourg, the Netherlands, Poland, Romania,
and Slovakia.” (B p. 319), and energy and Blue Card notes.

#### Proposals that land on its holdings
Analysis. Both the civil registry and the eID are run by the minister for computerisation and digital affairs, not home
affairs, so both plausibly fall under the EU-wide policy. Poland runs a government cloud.

#### What the project prints today
- `record:PL:civil_registry:operator` reads “minister właściwy do spraw informatyzacji (minister competent for computerisation)”.
- `record:PL:digital_identity_credentials:operator` reads “The digital affairs minister manages the public electronic identification system”.
- `indicator:PL:C2` reads “Yes”.

#### Open questions
- L1 and L3 are not yet sourced.
- Every hosting row is still a gap.

### Portugal (PT)

#### Where Draghi names it
On raw materials: “Unlike fossil fuels, the EU has deposits of some critical raw materials, such as lithium in
Portugal.” (A p. 60). On public-sector digitalisation: “Online tools and digitalisation (Netherlands, Italy, Portugal,
Spain).” (B p. 16). Also in the GDPR footnote.

#### Proposals that land on its holdings
Analysis. The civil registry is controlled by the President of IRN, and the project prints no parent ministry. Portugal
has a partial jurisdiction requirement and runs government data centres. Its government-cloud indicator is withheld as
disputed.

#### What the project prints today
- `indicator:PT:L1` reads “Partly”.
- `record:PT:civil_registry:operator` reads “The President of IRN, I.P. is the data controller of the civil registry database”.
- `indicator:PT:C1` reads “Yes”.

#### Open questions
- Which ministry IRN reports to decides whether the exception reaches the civil registry. The project would need a
  source for it.

### Romania (RO)

#### Where Draghi names it
Only in the GDPR footnote: “16 in Germany, Hungary, Croatia, Ireland, Luxembourg, the Netherlands, Poland, Romania, and
Slovakia.” (B p. 319). Romania is also named in energy and R&D passages.

#### Proposals that land on its holdings
Analysis. The eID was implemented by the Authority for the Digitalization of Romania, a digital body, so it plausibly
falls under the EU-wide policy. A government cloud is printed as Partly, that is announced or in pilot.

#### What the project prints today
- `record:RO:digital_identity_credentials:operator` reads “ROeID was implemented by the Authority for the Digitalization of Romania (ADR)”.
- `indicator:RO:C2` reads “Partly”.

#### Open questions
- Government data centres (C1), L1 and L3 are not yet sourced.

### Slovakia (SK)

#### Where Draghi names it
Only in the GDPR footnote: “16 in Germany, Hungary, Croatia, Ireland, Luxembourg, the Netherlands, Poland, Romania, and
Slovakia.” (B p. 319). Slovakia is also named in automotive, energy and R&D passages.

#### Proposals that land on its holdings
Analysis. The Register of Natural Persons and the authentication module are both administered by the Ministry of
Interior, so both plausibly sit inside the exception. Slovakia runs government data centres and a government cloud.

#### What the project prints today
- `record:SK:civil_registry:operator` reads “The Ministry of Interior (ministerstvo) administers the Register of Natural Persons”.
- `record:SK:digital_identity_credentials:operator` reads “The Ministry of Interior administers the authentication part of the authentication module”.
- `indicator:SK:C2` reads “Yes”.

#### Open questions
- L1 and L3 are not yet sourced.

### Slovenia (SI)

#### Where Draghi names it
Not on anything that bears on data. It is the one state the GDPR footnote omits. Its closest mention is a list of states
that generate nuclear power: “Belgium, Bulgaria, the Czech Republic, Finland, France, Hungary, the Netherlands, Romania,
Slovakia, Slovenia, Spain and Sweden, with France responsible for almost 50% of the EU‘s total generation.” (B p. 20).

#### Proposals that land on its holdings
Analysis. Slovenia's printed dependency facts read national infrastructure for seven holdings and an EU provider for
one. Its civil registry and
its trust services are run within the interior ministry, so both plausibly sit inside the exception. Its central bank
systems depend on an EU provider, which already meets an EU-level floor.

#### What the project prints today
- `record:SI:civil_registry:operator` reads “CRP is managed by the Ministry of the Interior”.
- `record:SI:digital_identity_credentials:operator` reads “SI-TRUST operates within the Ministry of the Interior and Public Administration”.
- `record:SI:central_bank:foreign_dependency` reads “EU provider”.
- `indicator:SI:C2` reads “Yes”.

#### Open questions
- L1 and L3 are not yet sourced.

### Spain (ES)

#### Where Draghi names it
As a EuroHPC host: “Three EU supercomputers (Lumi in Finland, Leonardo in Italy and Mare Nostrum 5 in Spain) are in the
top ten worldwide” (B p. 78). Also on public-sector digitalisation (B p. 16) and in the GDPR footnote.

#### Proposals that land on its holdings
Analysis. Spain's civil registry works under a directorate of the Ministry of Justice, so the justice exception plausibly
reaches it. Spain is the only state whose identity register falls under that exception rather than under home affairs.
Spain has a partial jurisdiction requirement and runs a government cloud.

#### What the project prints today
- `record:ES:civil_registry:operator` reads “Dirección General de Seguridad Jurídica y Fe Pública (Ministry of Justice)”.
- `indicator:ES:L1` reads “Partly”.
- `indicator:ES:C2` reads “Yes”.

#### Open questions
- Every hosting row is still a gap.

### Sweden (SE)

#### Where Draghi names it
On the tech sector: “The example of Sweden – which has a tech sector that is more than twice as productive as the EU
average” (B p. 255). Also in the GDPR footnote and in raw-materials, pension and capital-market passages.

#### Proposals that land on its holdings
Analysis. In Sweden the identity stack splits the other way. Population registration sits with the Tax Agency, which is
plausibly outside the exception. The eID sits with the Police Authority, which is plausibly
inside it. Sweden runs government data centres and a government cloud.

#### What the project prints today
- `record:SE:civil_registry:operator` reads “Skatteverket (Swedish Tax Agency) is responsible for population registration”.
- `record:SE:digital_identity_credentials:operator` reads “Polismyndigheten (Swedish Police Authority)”.
- `indicator:SE:C2` reads “Yes”.

#### Open questions
- The state-controlled eID indicator is withheld as disputed.
- L1 and L3 are not yet sourced.

## 5. Caveats

- **The report is from September 2024.** This note says nothing about what the Commission or the Council did with its
  proposals afterwards, because it fetched nothing on that question (TODO.md).
- **"Plausibly" is the author's word, used deliberately.** Whether a register is “home affairs” depends on how an
  adopted text would define the exception, and the report defines it only by example.
- **Draghi's figures are his, from his sources.** They are quoted, not re-checked against their originals.
- **The checks are machine checks.** The quotations were found mechanically in the PDFs, and the claim texts were
  compared with the bundle. No other model has reviewed the analysis, and no person has read it (#87 is the
  cross-model standard this note has not yet met).
- **The note reads one bundle.** It reads the bundle committed at the time of writing. When a state's facts change,
  `check` fails on any text that no longer matches, and the entry must be re-read rather than silently kept.

## Sources

- Mario Draghi, *The future of European competitiveness. Part A: A competitiveness strategy for Europe*, European
  Commission, September 2024. The PDF is from
  https://commission.europa.eu/topics/competitiveness/draghi-report_en (accessed 2026-10-23); its URL and sha256 are in
  `assets/reports/MANIFEST.csv`. CC BY 4.0, per the colophon (A p. 2).
- Mario Draghi, *The future of European competitiveness. Part B: In-depth analysis and recommendations*, European
  Commission, September 2024. Same page, same manifest.
- This project's committed bundle, `web/public/data/eu27.json`, for every claim id cited.
