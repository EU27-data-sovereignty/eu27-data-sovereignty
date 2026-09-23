# Distribution and trust: what sovereign infrastructure can borrow from CDN architecture

**Authored note, 2026-09-22. Not generated, and not part of the model, the JSON bundle or the web app.**
It argues one thing the rest of the repository does not yet address: how widely sovereign
infrastructure can be spread, and how thoroughly it must be encrypted and audited, are the same
question rather than two.

Read the [caveats](#caveats) before quoting anything here. This note proposes; it does not measure.
Nothing in it is sourced to the standard `VERIFICATION.md` sets for the model's per-country cells,
and nothing in it scores or orders any member state — #10 is untouched. The bounded exception that
lets an authored note exist at all is #59; #64 records why this one was written.

---

## Contents

- [The thesis](#the-thesis)
- [What Netflix and Cloudflare actually do](#what-netflix-and-cloudflare-actually-do)
- [What transfers, and what does not](#what-transfers-and-what-does-not)
- [Tier 0 is the shape a CDN is good at](#tier-0-is-the-shape-a-cdn-is-good-at)
- [Full encryption](#full-encryption)
- [Democratic accountability](#democratic-accountability)
- [Auditability](#auditability)
- [Why the three are one argument](#why-the-three-are-one-argument)
- [What the model would have to change](#what-the-model-would-have-to-change)
- [Caveats](#caveats)
- [Status and next steps](#status-and-next-steps)

---

## The thesis

The model currently treats a sovereign estate as a small number of large sites. `sites =
max(sites_by_mw, min_sites)`, and #12 records that the hand-set floor binds for 24 of 27 countries —
so site count today is, in the register's own words, "mostly a *political* parameter, not an
engineering result."

Nothing about that is wrong, but it forecloses a question worth asking: what would it take to run
the sovereign state on *many small* sites instead? The industries that have already answered that
question are the content and edge networks, and their answer is not "buy more buildings." It is a
set of architectural commitments — separate the control plane from the data plane, make every site
identical, pin jurisdiction as a first-class property — that a sovereign estate could adopt without
adopting the business model.

The catch is that distribution multiplies the number of places the state's data physically sits. A
CDN can be relaxed about that because its payload is a cache of licensed content. A civil registry
replica is not a cache. What makes wide distribution survivable for state data is that the data is
inert without keys held somewhere else, and that every access leaves a record someone outside the
operator can verify. That is why encryption and auditability belong in the same note as topology:
they are the preconditions that make the topology safe, not separate good ideas.

`TIER0-TIER1-SIZING.md` reaches the same junction from the other direction. Having established
that Tier 0/1 replication is nearly free, it concludes: "There is no capacity argument for
economising on Tier 0 durability. Budget for paranoid replication and spend the design effort on
key custody and audit instead."

## What Netflix and Cloudflare actually do

**Netflix Open Connect** places purpose-built appliances inside ISP networks and at internet
exchanges, rather than serving from a small number of origin datacentres. Content is *pre-positioned*
during off-peak fill windows according to predicted demand, so the request path is a local disk read.
The commercial logic is that the ISP saves transit and Netflix saves origin egress.

The architecturally interesting part is the split. Open Connect is a distributed **data plane**; the
control plane — catalogue, entitlement, recommendation, playback authorisation — stays centralised.
The thing that is spread everywhere is bulk and replaceable. The thing that is small, stateful and
consequential stays where it can be governed.

**Cloudflare** takes the homogeneity further. Every point of presence announces the same anycast
prefixes, so routing sends a request to a nearby site without a DNS-based region concept, and every
server in every site runs every service rather than specialising. Compute at the edge uses V8
isolates rather than containers, which drives per-tenant overhead low enough that "run it everywhere"
is affordable. Notably, having built all of that, Cloudflare then had to reintroduce geography
deliberately: its Durable Objects support jurisdictional restrictions so that stateful objects can be
constrained to, for example, the EU.

That last move is the one worth dwelling on. The most distributed architecture in commercial use
still needed jurisdiction as an explicit, enforceable primitive. It was not an afterthought bolted on
for compliance; it is a placement constraint in the scheduler.

References: Netflix Open Connect (<https://openconnect.netflix.com/>), Cloudflare Workers and Durable
Objects documentation (<https://developers.cloudflare.com/durable-objects/>). These are vendor
descriptions of their own systems, used here as an analogy — see the caveats.

## What transfers, and what does not

**Transfers:**

- **Control plane / data plane separation.** Keep the small, consequential, hard-to-replicate state
  in a governed core; let the bulk spread. This maps onto the tiering this project already uses.
- **A homogeneous fleet.** Every site runs the same stack. Sovereign estates are small — three or
  four sites for most member states under the current floor — and cannot afford per-site
  specialisation or the operational knowledge silos that come with it.
- **Placement as an explicit constraint.** Jurisdiction, and for a state also classification, should
  be a property the scheduler enforces, not a deployment convention someone remembers.
- **Pre-positioning.** Predictable, ahead-of-demand replication rather than on-demand fetch, which is
  also what makes an air-gapped or degraded-link site useful rather than useless.

**Does not transfer:**

- **Read-mostly assumptions.** CDN payloads are written once and read enormously. Registries,
  benefits, tax and judicial systems are transactional and write-heavy, and correctness depends on
  consistency in a way a cache never does.
- **Loss tolerance.** Losing a CDN node costs a cache miss. Losing a registry replica is a
  correctness and continuity event; losing *control* of one is a breach.
- **The consistency budget.** Spreading writable state across many sites costs either latency or
  consistency. CDNs mostly avoid this problem rather than solving it; a state cannot.
- **The economics.** Netflix can give hardware to ISPs because it captures the transit saving. A
  state has no equivalent externality to monetise, so every additional site is cost with no offset —
  which is precisely what the current model cannot express (see below).

## Tier 0 is the shape a CDN is good at

The one place where the analogy holds tightly is the tier this project has already sized.

`TIER0-TIER1-SIZING.md` establishes the asymmetry as its central finding: "Tiers 2 and 3 are where
the *bytes* are. Tiers 0 and 1 are where the *sovereignty* is." Tier 0 alone is roughly 50 TB — "one
rack, air-gappable, physically containable in a hardened facility" — and Tier 0+1 together sit at a
fraction of a percent of the facility power budget.

Identity and authorisation lookups are small, read-dominated, latency-sensitive and cheap to
over-replicate. That is the Open Connect workload profile almost exactly. It is also the workload
whose unavailability stops the state functioning within minutes rather than days.

So the tiering suggests opposite topologies for opposite tiers:

| | Tier 0/1 — identity and legal-fiscal spine | Tier 2/3 — health, genomics, archives |
|---|---|---|
| Size | Tiny | Where essentially all bytes are |
| Access shape | Read-dominated, latency-sensitive | Mixed, throughput-bound |
| Cost of replication | Near-free | The dominant cost |
| Topology it wants | Many small sites, widely spread | Few large sites |
| Posture | Absolute national control | Looser, if keys are held nationally |

The right-hand column is `TIER0-TIER1-SIZING.md`'s own item 4, which proposed "absolute national
control over Tier 0/1, and a looser posture (EU-federated, or commercially hosted with
sovereign-held keys) for the Tier 2/3 bulk", and noted it was "worth developing as a section in the
country write-ups." This note is a step toward that, and the mechanism the proposal was missing is
in the next section.

## Full encryption

The repository currently contains one substantive sentence about encryption — "encryption in
transit", a single bullet in the reference case's network section. The three states of data each
need a different answer.

- **At rest.** Necessary and nearly meaningless on its own. If the operator holds the keys, is the
  same legal entity as the custodian, and sits in the same jurisdiction, encryption at rest protects
  against a stolen disk and against nothing else that matters here.
- **In transit.** Already assumed. The open question is not whether, but whose certificate authority
  and whose key material — which is a sovereignty question, not a cryptographic one.
- **In use.** Absent from the repository entirely. Confidential computing — memory encryption plus
  remote attestation — is what allows a workload to run on infrastructure whose operator is not
  trusted to read it. Attestation is the load-bearing half: it lets a relying party verify *what
  code is running* before releasing keys to it.

**Key custody is the hinge**, and the project has already written the sentence that makes this the
central issue. Every one of the 26 generated briefs carries it: "Data residency in-country is
therefore necessary but not sufficient; what matters is who holds the keys and who can be
compelled." Nothing in the project currently follows from that sentence. What should follow:

1. **Custody separated from operation.** The entity that holds key material should not be the entity
   that runs the compute, so that compelling one does not yield the other.
2. **No single administrator can decrypt.** Threshold or quorum key release, so that unilateral
   access by any one operator, official or successful intruder is not possible by construction
   rather than by policy.
3. **Attestation before release.** Keys released to a workload only on proof of what that workload
   is — which is what makes "commercially hosted with sovereign-held keys" a real posture rather
   than a contractual promise.

Point 3 is the missing mechanism in the Tier 2/3 proposal above. It is also what makes wide
distribution tolerable: a replica in a site that is seized, or whose operator is compelled, is
inert.

## Democratic accountability

The reference case's governance section poses four questions and answers none: which ministry or
independent authority owns the operator, how independent it should be from ordinary procurement
cycles, how agencies are compelled or incentivised to migrate, and how defence and intelligence
governance should differ.

The concrete gap in the repository is narrower and more fixable. `model/institutions.py` already
defines a `scrutiny` function — "parliamentary committee, court of audit, statutory IT reviewer" —
and `model/institutions.csv` currently has zero data rows. The schema anticipated accountability;
the register is empty.

Proposals, offered as proposals:

- **Statutory body, not a directorate.** An operator inside a ministry inherits that ministry's
  procurement cycle and its incentive to under-report. A statutory footing makes existence and
  mandate a legislative act rather than an administrative one.
- **Multi-year funding.** Infrastructure that must be trustworthy across a decade cannot be renewed
  annually against the political weather.
- **A published placement register.** Which classes of workload run in which sites, under whose
  operation, published by default. This is the accountability analogue of the placement constraint
  above: the scheduler enforces it, the register discloses it.
- **Standing access for scrutiny bodies.** A parliamentary committee and a court of audit with
  continuous access to audit output, not incident reports after the fact. This is where the empty
  `scrutiny` rows would become useful rather than decorative.

#11 already names "operator ownership structure (who operates the sovereign cloud, and on whose
technology)" as a dimension the project wants and lacks. That is the same gap seen from the model's
side.

## Auditability

An audit trail the operator can rewrite is not an audit trail. The requirement is not "comprehensive
audit logs" — the reference case's existing bullet — but logs whose completeness can be verified by
someone who does not trust the party producing them.

- **Tamper-evident structure.** Append-only logs with Merkle-tree inclusion and consistency proofs,
  as Certificate Transparency does, so that an omitted or altered entry is detectable rather than a
  matter of trust.
- **Independent witnesses.** Proofs countersigned by parties other than the operator — a scrutiny
  body, another member state, an EU institution — so that verification does not depend on the
  operator's cooperation at the time of the question.
- **Reproducible builds.** So the binary running in the estate is demonstrably the source that was
  published and reviewed. Without this, code review is an assertion about a different artefact than
  the one deployed.
- **Access records for Tier 0/1 specifically.** Who read the identity spine, when and under what
  authorisation, is a higher-value record than most of what the spine contains.

Worth stating plainly, because it is a check on the whole argument: **this repository already
practises a small version of what this section asks for.** `ARTEFACTS.csv` records the hash of every
tracked deliverable together with the hash of the data bundle it was rendered from, so a stale
artefact fails the suite rather than going unnoticed. `model/fetch_manifest.csv` records a sha256 for
every fetched source document. PDF creation dates are pinned so the rendering is byte-reproducible
(#53). None of that is expensive, and all of it is the same posture at a scale where it can be
checked by running `./test.sh`.

## Why the three are one argument

Distribution multiplies the number of physical places state data sits, and therefore the number of
places it can be seized, compelled or stolen. Taken alone, that is a straightforward loss.

Each of the other two closes one gap:

- **Encryption** makes a seized replica worthless without key material held elsewhere, which is what
  converts "more copies" from exposure into resilience.
- **Auditability** makes an unauthorised access *detectable* by someone outside the operator, which
  is what stops distribution from diffusing responsibility along with the data.
- **Accountability** makes detection consequential. A tamper-evident log nobody has standing to read
  is theatre.

Remove any one and the other two degrade. Encryption without auditability means nobody can tell
whether the keys were used. Auditability without accountability means the record exists and changes
nothing. Accountability without encryption means the oversight body is supervising a system whose
data any sufficiently motivated third party can already read.

Run in the other direction, the argument delivers what `TIER0-TIER1-SIZING.md` asked for: if custody
and audit are strong enough, *where* the Tier 2/3 bulk physically sits stops carrying the whole
sovereignty burden — which decouples the political argument from the expensive capacity argument,
exactly as item 4 proposed.

## What the model would have to change

Nothing in this note is modelled, and it deliberately contains no figures, because the model has no
term that could produce one. Making distribution an engineering result rather than a political
parameter needs, at minimum:

1. **A cost relationship for site count.** `Critical-load MW per site` is a flat 12.0 MW constant, so
   raising site count today only shrinks `avg_mw_per_site`. There is no per-site fixed overhead and
   no economy-of-scale penalty, which means the model cannot express a tradeoff it does not have.
2. **Workload-to-topology affinity.** Which classes belong in many small sites and which in few large
   ones — the table above, made computable.
3. **Failure domains.** Something better than a flat 20% design headroom standing in for resilience.

The roadmap entry under `## Planned` carries the full ripple: sizing math, the schema through both
TypeScript type files, the golden results file, and the `min_sites` bound.

## Caveats

1. **Nothing here is sourced to the project's standard.** `VERIFICATION.md` sets a tiered bar for the
   model's per-country cells; this note makes no per-country claim and therefore does not engage
   that bar. It should not be cited as if it did.
2. **No member state is named anywhere in this note, and that is deliberate.** Every claim is about
   architecture, or about this repository's own contents. Nothing here asserts anything about any
   state's law, procurement or certification posture — those claims belong in the sourcing ledger,
   under `VERIFICATION.md`'s rules, not in an authored note.
3. **The vendor architectures are an analogy, not a specification.** They are described from public
   material, they change without notice, and neither organisation designed for the constraints a
   state operates under.
4. **These are proposals, not findings.** The governance questions in the reference case remain open.
   This note offers answers to argue with; it does not settle them.
5. **No numbers, deliberately.** Any figure for edge site counts, latency or replication cost would
   be invented, because no term in the model produces one.
6. **The Tier 0/1 claim inherits its parent's status.** The sizing it rests on is
   `TIER0-TIER1-SIZING.md`'s, with that document's own caveats.

## Status and next steps

| Step | State |
|---|---|
| Note drafted — topology, encryption, accountability, auditability | ✅ 2026-09-22 |
| Recorded as an authored note under #59's conditions | ✅ `DECISIONS.md` #64 |
| Distribution as a modelled dimension | ⬜ `ROADMAP.md`, Planned |
| Populate `model/institutions.csv` `scrutiny` rows | ⬜ Not started |
| Develop the Tier 0/1 vs Tier 2/3 posture split for the country write-ups | ⬜ Open — `TIER0-TIER1-SIZING.md` item 4 |
| Decide whether key custody becomes a sovereignty-matrix dimension | ⬜ Open — relates to #11 |

Progress on these is tracked in `ROADMAP.md`, and changes to this note are logged in `CHANGELOG.md`.
