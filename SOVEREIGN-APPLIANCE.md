# The sovereign appliance: state-owned data boxes in facilities that already exist

**Authored note, 2026-10-12. Not generated, and not part of the model, the JSON bundle, the web app, the PDFs or
`/ask`.** `run.sh data` never touches it. It proposes a physical unit for the identity and legal-fiscal record of a
member state and a way of placing it, and it does not measure anything. Its evidentiary standard is low and is
stated here: nothing in it is sourced to `VERIFICATION.md`'s bar for the model's per-country cells, that bar is
not engaged rather than met, and nothing here has been machine-checked by the project's evidence pipeline (#82,
#87) or verified by a person. Every page it cites carries the URL and the access date; a page that did not answer
an automated request is marked **[unverified]** on its line. The bounded exception that lets an authored note
exist at all is #59; #104 records why this one was written and what it may not contain.

**It ranks nothing.** No member state is scored or ordered (#10, #77). No member state is named outside the
[Precedents](#precedents) section, and there only with a cited page. No cost figure, no site count and no latency
figure appears anywhere, because no term in the model produces one (#72, #73). Every figure in the text is quoted
from [`TIER0-TIER1-SIZING.md`](TIER0-TIER1-SIZING.md), with that note's caveats, or from a cited page.

**The question.** `DISTRIBUTION-AND-TRUST.md` (#64) argued that the identity spine wants many small identical
sites, and that encryption, key custody and audit are what make that safe. It stopped short of three things: the
physical unit, the facilities it would sit in, and the contract with whoever runs those facilities. This note
takes those three up, starting from one commercial precedent, the content-delivery appliance that one streaming
company places inside other parties' networks.

---

## Contents

- [The idea](#the-idea)
- [What Open Connect does, and the one part that transfers](#what-open-connect-does-and-the-one-part-that-transfers)
- [What the box holds in phase one](#what-the-box-holds-in-phase-one)
- [Why existing facilities](#why-existing-facilities)
- [Where it differs, and what has to change](#where-it-differs-and-what-has-to-change)
- [The security model of the box](#the-security-model-of-the-box)
- [Precedents](#precedents)
- [The host contract](#the-host-contract)
- [What this adds to the repository](#what-this-adds-to-the-repository)
- [Caveats](#caveats)
- [Status and next steps](#status-and-next-steps)
- [Sources](#sources)

---

## The idea

A state builds, or has built to its specification, a sealed appliance that holds the record without which it
cannot say who exists and what each person owes and is owed. The state owns the box, holds its keys, administers
it remotely and is the only party that can read what is on it. The box is then racked in facilities that already
exist on the national internet infrastructure: a commercial colocation hall, an internet exchange point, a network
operator's point of presence, a ministry's or municipality's own server room. The host supplies a locked cage,
power, cooling and a port. It never has logical access, and a box removed from its cage holds nothing legible.

Phase one holds text, identifiers and numbers only: the civil register, the identity-document and credential
history, the legal-fiscal relationship between each person and the state. That is the project's tier 0 and tier 1.
Nothing with images, imaging, audio or bulk archives goes on the phase-one box.

The appeal is that the hard part of sovereign hosting, the building, is skipped. The facilities exist, they are
on the network already, and the constraint moves from floor space and construction to three things a state can
specify in a contract and verify on a visit: power, a port and a lock.

## What Open Connect does, and the one part that transfers

Open Connect is the content-delivery network of one streaming company. Its own overview describes two placements
for its appliances: inside internet exchange points, and "directly inside ISP networks", where "We provide the
server hardware and the ISPs provide power, space, and connectivity"
([Open Connect overview](https://openconnect.netflix.com/Open-Connect-Overview.pdf), accessed 2026-10-12). The
appliances are "provided free of charge for ISP partners who meet our basic requirements", are "based on commodity
PC components, assembled in custom cases by our suppliers", and run "the FreeBSD operating system and the NGINX web
server" ([Open Connect appliances](https://openconnect.netflix.com/en/appliances/), accessed 2026-10-12). The owner
runs them from a distance: all deployments "are constantly monitored by the Open Connect Operations team", and
"We troubleshoot and proactively fix most issues remotely with minimal input required from our ISP partners"
(overview, accessed 2026-10-12). Content arrives before demand: updates are deployed "proactively during
off-peak fill windows" (overview, accessed 2026-10-12). The appliances hold no customer data; they "do not store
client data (for example - viewing history, DRM info, or member data)", and the steering, fill and telemetry logic
sits in "control plane services" elsewhere (overview, accessed 2026-10-12). The host's side is small: the appliances
"require a small amount of data center rack space, power, and connectivity"
([Open Connect](https://openconnect.netflix.com/en/), accessed 2026-10-12).

The part that transfers is the split of responsibilities, not the business. The owner of the data owns, builds,
fills, monitors and repairs the box. The host of the facility supplies rack space, power and a port, and nothing
else. Management interfaces are separated from the serving path and access to them is restricted (appliances page,
accessed 2026-10-12). The control plane, the small and consequential state, stays where the owner governs it. That
is exactly the division #64 asked for, with the physical unit named.

The part that does not transfer is the reason the host agrees. The streaming company's host saves transit costs
by carrying the traffic locally, so the box is free and the host is glad of it. A state's box brings the host no
traffic to save on. The host's incentive has to come from payment or from statute, and the contract below is
written on that assumption.

## What the box holds in phase one

`TIER0-TIER1-SIZING.md` defines tier 0 as the identity spine, "without it the state cannot say who exists", and
tier 1 as the legal and fiscal state, "the enforceable relationship between citizen and state". Its central finding
is the asymmetry: "Tiers 2 and 3 are where the *bytes* are. Tiers 0 and 1 are where the *sovereignty* is." For its
worked example it puts tier 0 at "~50 TB" logical, "one rack, air-gappable, physically containable in a hardened
facility", and tier 0 and 1 together, with its redundancy multiplier, at "1–2 racks per site". It also says what
media the tier wants: "Specify flash, not capacity HDD", because the workload is "identity lookups, authentication,
benefit eligibility checks", "IOPS-bound, not capacity-bound".

That is the phase-one box: a rack or two of flash holding structured rows and small write-once blobs, serving
lookups. It is deliberately not the health record, the imaging, the genomics, the archives or any AI workload.
Those are the tiers where the bytes are, and #64 argues they can sit under a looser posture if the keys are held
nationally. The box is for the tier whose loss stops the state within minutes rather than days, and whose size
makes paranoid replication nearly free: the sizing note's own conclusion is "Budget for paranoid replication and
spend the design effort on key custody and audit instead."

The sizing note's figures are order-of-magnitude estimates from public schema documentation, not from any
national statistics office, and it says so. Nothing here tightens them.

## Why existing facilities

A sovereign estate modelled as a few large new buildings is the model's current shape, and #12 records that the
site count in it is "mostly a *political* parameter, not an engineering result". A box the size of a rack does not
need a building. It needs a place that already has the four things a rack needs, and those places exist in every
member state, in several classes:

| Facility class | What it offers | What it lacks |
|---|---|---|
| Commercial colocation | Certified halls, cages, dual power feeds, carrier-neutral connectivity, staffed access control, an existing contract form | A private operator, possibly foreign-owned, with its own staff on the floor; a landlord relationship rather than a sovereign one |
| Internet exchange point | The densest point on the national network; many operators one cross-connect away; often run by a neutral association | Space is scarce and built for network gear; the exchange is not an operator of secure rooms and may not want to be |
| Network operator's point of presence | Nationwide footprint, down to regional and municipal sites; already carries the traffic that would reach the box | Variable physical security; the operator is a regulated private party with a commercial interest in the arrangement |
| Existing government rooms | The state already owns them; no new counterparty; the legal questions are the state's own | Variable build quality, power and connectivity; often exactly the rooms the sovereign-cloud discussion wants to close |

None of these classes is named, and no facility is proposed for any state. The claim is only that the set is
non-empty everywhere, and that a specification written for a cage, a feed and a port can be met in more than one
class, which is what gives the state a choice of counterparties and a credible exit from any one of them.

Two consequences follow. First, the control plane does not need to be in any of these. #64's split puts the
primary, the key custody and the scheduler in a governed core, which can be a government room of the state's own,
while the boxes in the field are replicas. Second, "on the national internet infrastructure" is a condition the
state can write down and check: a port on a national exchange or a national operator's network, and a documented
path from the box to the people it serves that does not leave the jurisdiction unless the state chooses that it
should.

## Where it differs, and what has to change

The streaming appliance is a cache of licensed, public, read-mostly content. A seized or compromised one leaks
nothing of consequence and is replaced. A register replica is none of those things, so three things change.

**Writable state.** Registers are written to. #64 lists the consistency budget as what does not transfer from a
CDN. The phase-one design keeps writes in the governed core: a box in the field is a read replica, fed before
demand the way the appliance is filled, and a change to a record is made once, in the core, and propagated. A
field box that cannot reach the core keeps serving what it has and accepts no writes. Where a state wants writes
to survive the loss of the core, that is a quorum design across several boxes, and it is a later phase.

**Confidential payload.** The appliance's content is encrypted for licensing, not for secrecy, and it "does not
store client data". The box's whole payload is personal data of the highest consequence. So the box never holds
its keys in a form the host or a thief could use: the disks are encrypted, the keys are released to the box only
after it has proved what it is and what it is running, and the release comes from a custodian that is not the
operator (#64, "Key custody is the hinge"). A box pulled from its cage is inert. That is the property that turns
"more copies" from exposure into resilience, and it is the property the streaming design never needed.

**The host as processor at most, never controller.** The host supplies a cage and never sees a record. In data
protection terms that keeps the host out of the role of controller, and if it is a processor at all it is one with
no access to the data it hosts. The contract has to say this, and the box has to make it true by construction, so
that the contract is describing a fact rather than asking for a promise.

A fourth difference is organisational rather than technical. The streaming company's host has no stake in the
content. A facility operator hosting a state's register has a stake in the state's trust, and the state has a
stake in the operator's ownership. Who owns the host, and who can compel it, is the question #96's operator
register is being built to answer, and the box does not make it go away. It narrows what compulsion yields.

## The security model of the box

This section builds on #64's "Full encryption" and "Auditability" sections and adds what a sealed unit in a
third party's cage needs beyond them. Nothing here is a product specification, and every mechanism named is in
public use.

- **Measured boot and attestation before key release.** The box boots a measured chain and presents evidence of
  what it is running to a verifier the state operates. Remote attestation is a standardised architecture: one
  peer, "the Attester", "produces believable information about itself" so that a remote peer can appraise it, with
  the roles of Attester, Verifier and Relying Party defined
  ([RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html), accessed 2026-10-12). Keys are released only to a box
  whose evidence the verifier accepts. A box running anything else gets nothing.
- **Sealed storage, keys held elsewhere.** The payload is encrypted at rest with keys that never sit on the box
  in the clear. Release is from a custodian separated from the operator, by quorum, so that no single
  administrator, official or intruder can decrypt (#64's three custody rules).
- **No local console.** There is no keyboard, display or serial path that yields a shell. Local hands can replace
  a power supply or a disk; they cannot log in. This is the streaming appliance's "separate serving and management
  functions, restrict access to management interfaces" (appliances page, accessed 2026-10-12), taken to its end.
- **Tamper response.** Opening the case, moving the box or losing power beyond a threshold zeroises the key
  material held in the box's secure element, so the next boot needs a fresh release from the custodian, which
  needs fresh attestation. A box in someone else's cage must assume it will one day be handled by someone else.
- **A tamper-evident access log, witnessed outside the operator.** Every read of the record is appended to a log
  structured so that an omitted or altered entry is detectable. The public precedent is the certificate
  transparency log, where "The append-only property of each log is achieved using Merkle Trees", and monitors
  outside the operator inspect every entry ([RFC 9162](https://www.rfc-editor.org/rfc/rfc9162.html), accessed
  2026-10-12). The witnesses are the scrutiny bodies #64 names: a parliamentary committee, a court of audit, another
  member state or an EU institution.
- **Reproducible builds.** The software on the box is demonstrably the source that was reviewed, so that
  attestation measures something a third party can check rather than a vendor's blob.
- **Pre-positioned, read-only replicas.** The field box is filled from the core before demand and serves reads.
  It does not accept writes in phase one. That removes most of the consistency problem and all of the question of
  what a compromised field box could have changed.

What this buys is the sentence every one of the generated briefs already carries, made operational: residency is
necessary but not sufficient, what matters is who holds the keys and who can be compelled. A box designed this way
can sit in a facility the state does not run, because compelling the facility yields a sealed unit, and compelling
the facility's operator yields nothing the operator ever had.

## Precedents

This is the one section that names member states, because the precedent is a real one with a published
agreement. Every line that names a state carries the page it was read from and the access date.

**Estonia's data embassy in Luxembourg.** On 20 June 2017 Estonia and Luxembourg signed an "Agreement between
the Grand Duchy of Luxembourg and the Republic of Estonia on the hosting of data and information systems"
([Luxembourg Chamber of Deputies, dossier 7185](https://wdocs-pub.chd.lu/docs/compilation/docpa/pdf/7185_Dossier_Complet.pdf),
accessed 2026-10-12). The text annexed to that dossier is the relevant one here, because it is a host contract
between a data owner and a facility owner, written as a treaty:

- Luxembourg provides "a dedicated data centre space" (Article 1(b)) "for the lease cost as set out in the
  conditions agreed upon by the competent authorities" (Article 2(2)), and gives access "to the authorised
  representative of the Republic of Estonia" (Article 2(3); [dossier 7185](https://wdocs-pub.chd.lu/docs/compilation/docpa/pdf/7185_Dossier_Complet.pdf), accessed 2026-10-12).
- The premises "shall be inviolable and thus exempt from search, requisition, attachment or execution"
  (Article 3(1)), and no Luxembourg official "shall enter the premises without the prior approval of the
  authorised representative of the Republic of Estonia" (Article 3(2); [dossier 7185](https://wdocs-pub.chd.lu/docs/compilation/docpa/pdf/7185_Dossier_Complet.pdf), accessed 2026-10-12).
- The equipment "put in place on the premises by the Republic of Estonia shall be regarded as assets of the
  Republic of Estonia and shall enjoy immunity from every form of legal process" (Article 5; [dossier 7185](https://wdocs-pub.chd.lu/docs/compilation/docpa/pdf/7185_Dossier_Complet.pdf), accessed 2026-10-12).
- The data "shall be regarded as archives of the Republic of Estonia" and are "inviolable" (Article 6(1), 6(2)),
  and Estonia "shall be entitled to use any code and encryption in its official communications" (Article 6(4); [dossier 7185](https://wdocs-pub.chd.lu/docs/compilation/docpa/pdf/7185_Dossier_Complet.pdf), accessed 2026-10-12).
- The host's duty is physical: Luxembourg "shall take all appropriate measures to protect the premises against
  any intrusion or damage" (Article 4; [dossier 7185](https://wdocs-pub.chd.lu/docs/compilation/docpa/pdf/7185_Dossier_Complet.pdf), accessed 2026-10-12).

Luxembourg's Conseil d'État, in its opinion on the approving bill, recorded that the privileges and immunities are
comparable to an embassy's without being identical, that the Vienna Convention does not apply, and that they
attach "exclusivement à l'inviolabilité des locaux et des données stockées", not to persons
([Avis 52.413, 10 October 2017](https://conseil-etat.public.lu/fr/avis/2017/Octobre2017/10102017/52413.html),
accessed 2026-10-12). The Estonian publication of the agreement is in Riigi Teataja
([Eesti Vabariigi ja Luksemburgi Suurhertsogiriigi vaheline andmete ja infosüsteemide majutamise kokkulepe](https://www.riigiteataja.ee/akt/228032018002), accessed 2026-10-12) **[unverified]**:
the page refused this project's automated request, so its text was not read
here, and the quotations above are from the Luxembourg dossier.

What the precedent shows is the shape of the contract: owner's equipment, owner's keys, owner's exclusive access,
host's premises and physical protection, and a legal status for the space that puts it beyond the host's own
compulsory process. What it does not show is the appliance: the precedent is a dedicated space in one foreign
state's government data centre, and the agreement says nothing about the hardware's design. The box proposed here
is what would let the same contract be signed for a cage in a commercial hall, because the inviolability would
then rest on the box's construction as well as on the agreement's text.

## The host contract

The minimum a state would write into any host agreement, whichever facility class it signs with. These are the
obligations the precedent's treaty carries, translated to a commercial or administrative counterparty, plus what
a sealed box makes checkable.

1. **A dedicated, locked space** that only the state's authorised representative may open; the host's staff enter
   it only escorted and only on the state's request, with fire and life-safety exceptions written down.
2. **Power and cooling** to a stated service level, with the box's own tamper thresholds set to survive the
   host's documented maintenance windows.
3. **A port on the national internet infrastructure**, with the path from the box to the people it serves
   documented and the host forbidden to re-route it outside the jurisdiction without the state's consent.
4. **No logical access**, stated as a fact about the box and as an obligation on the host: the host holds no
   credentials, keys or console, and asks for none.
5. **Physical protection** of the space to at least the level the host gives its own most sensitive tenant, and
   notification to the state of any intrusion, attempt, or request by a third party or authority to access it.
6. **An audit right** for the state's scrutiny bodies: unannounced visits, the host's own access records for the
   space, and the right to publish findings.
7. **Exit and return**: the state may remove its equipment at any time, the host returns any component it
   replaced, and any data storage device that leaves the space leaves zeroised or under the state's seal.
8. **Ownership disclosure**: the host declares its ultimate owner and any change of control, so the state's
   operator register (#96) stays true for it.

Payment or statute supplies the host's incentive; the contract above does not assume the host gains anything else.

## What this adds to the repository

Nothing in this note is modelled. What it adds is a word the planned operator register lacks and a question the
hosting pass could ask.

- **A hosting model.** `docs/hosting-operators.md` (#96) plans a `model` field for each hosting row with the
  values own data centre, state shared service, outsourced operation, public cloud and private cloud. State-owned,
  state-keyed hardware in a facility the state does not run is none of those, so the planned enum gains
  `colocated_appliance`. The value is recorded in that design, not built; the register itself is not built either.
- **A per-holding question for a later pass.** When the hosting pass reaches a holding whose host is a facility
  rather than an operator, the question "is the facility on the national internet infrastructure, and who owns
  it" is the one this note cares about, and the operator register's ownership links are where the answer would go.
- **No model change.** The capacity model still has no term for a site smaller than its per-site constant, and
  #64's "What the model would have to change" is still unbuilt. This note gives that work a concrete unit to size
  if it is ever taken up, and no figure for it.

## Caveats

1. **Nothing here is sourced to the project's standard.** The model's per-country cells are held to
   `VERIFICATION.md`'s tiered bar; this note makes no per-country claim and does not engage that bar. It should
   not be cited as if it did.
2. **No member state is named outside the Precedents section, and that is deliberate.** Every other claim is
   about architecture, about a vendor's published description of its own system, or about this repository's own
   contents. Nothing here asserts anything about any state's law, procurement or certification posture; those
   claims belong in the sourcing ledger under `VERIFICATION.md`'s rules.
3. **The vendor architecture is an analogy, not a specification.** The streaming company's pages describe its own
   system, change without notice, and were written for a workload with none of the constraints a state's register
   has. Its URLs are deliberately kept out of `model/sources/`.
4. **The precedent is a treaty, not an appliance.** The agreement quoted above governs a dedicated space in a
   government data centre between two states. Whether its inviolability clauses could be reproduced for a cage
   in a commercial facility, by contract or by statute, is a legal question this note does not answer.
5. **These are proposals, not findings.** The security model lists mechanisms in public use and does not claim
   that any assembled product provides all of them, or that a state has procured one.
6. **No new figures.** Every number in the text is quoted from `TIER0-TIER1-SIZING.md`, with that note's own
   caveats and its stated confidence, or from a cited page. Any site count, replica count, latency or cost would
   be invented, because no term in the model produces one.
7. **Pages that refused.** One cited page, the gazette publication in the Precedents section, refused an automated request and is marked
   **[unverified]**. The link register `docs/sovereign-appliance-links.csv` records the status of every URL.

## Status and next steps

| Step | State |
|---|---|
| Note drafted: the unit, the facility classes, the differences from the commercial precedent, the security model, the treaty precedent, the host contract | ✅ 2026-10-12 |
| Recorded as an authored note under #59's conditions | ✅ `DECISIONS.md` #104 |
| `colocated_appliance` added to the planned hosting model enum | ✅ `docs/hosting-operators.md` |
| Second-model review of the quotations against their pages (#87's rule applied to prose) | ⬜ Not run |
| Operators as entities, with the facility's owner as a link | ⬜ `docs/hosting-operators.md` (#96), planned |
| Distribution as a modelled dimension, with the box as the unit | ⬜ `ROADMAP.md`, "Then — make distribution a modelled dimension" |
| The legal question in caveat 4 | ⬜ Open, not this project's to answer |

Changes to this note are logged in `CHANGELOG.md`; the working log is `docs/plans/sovereign-appliance-log.md`.

## Sources

Every URL below is in `docs/sovereign-appliance-links.csv` with the status it answered on the date shown.

- Open Connect overview, PDF: https://openconnect.netflix.com/Open-Connect-Overview.pdf (accessed 2026-10-12)
- Open Connect, partner page: https://openconnect.netflix.com/en/ (accessed 2026-10-12)
- Open Connect appliances: https://openconnect.netflix.com/en/appliances/ (accessed 2026-10-12)
- Chambre des Députés du Luxembourg, dossier 7185, consolidated, with the agreement text annexed:
  https://wdocs-pub.chd.lu/docs/compilation/docpa/pdf/7185_Dossier_Complet.pdf (accessed 2026-10-12)
- Conseil d'État du Luxembourg, Avis 52.413 of 10 October 2017:
  https://conseil-etat.public.lu/fr/avis/2017/Octobre2017/10102017/52413.html (accessed 2026-10-12)
- Riigi Teataja, the Estonian publication of the agreement: https://www.riigiteataja.ee/akt/228032018002 (accessed 2026-10-12) **[unverified]**
- RFC 9334, Remote ATtestation procedureS (RATS) Architecture: https://www.rfc-editor.org/rfc/rfc9334.html
  (accessed 2026-10-12)
- RFC 9162, Certificate Transparency Version 2.0: https://www.rfc-editor.org/rfc/rfc9162.html
  (accessed 2026-10-12)
