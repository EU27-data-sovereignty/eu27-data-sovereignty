# Editorial policy

How this project decides what to publish, how it corrects itself, and who is behind it. The rules are
enforced by code and tests wherever they can be. Where a rule is a matter of conduct, it is written down
here so that anyone can hold the project to it.

## Who is behind it

- **Ownership.** The project is run by one person, Pieter de Jong, in a personal capacity. It is
  **independent and unaffiliated**: no government, EU body, cloud provider or vendor commissions, funds
  or reviews it.
- **Funding.** *[Owner to confirm before publication:* the project is self-funded and takes no grants,
  donations or sponsorship.*]* If that changes, the funder, the amount and the terms will be stated on
  this page before any money is accepted.
- **Legal entity.** No legal entity yet. Moving the project into a Dutch foundation (*stichting*) is
  intended and recorded as deferred (DECISIONS #86). The licences and contributor terms are built so
  that move needs no contributor's consent.
- **Conflicts of interest.** *[Owner to confirm before publication:* the owner has no financial interest
  in any cloud provider, operator or vendor named in the findings.*]* Any future interest will be declared
  here.

## What is published

- **Only what a public source states.** Every fact is cited to a public document, with a verbatim quote
  that a machine has found on the page. Every number and date in a printed value must be in that quote.
  Anything else is shown as a **gap**, never estimated, and a gap means *not yet sourced*, never *does not
  exist*.
- **Official sources only.** A fact must rest on a T1 or T2 source: an official law portal or gazette, a
  statistics office, a ministry or agency, the operator itself, or an audit office. Press, encyclopedias
  and unofficial copies of laws are recorded but not admitted.
- **No judgement presented as fact.** The placement of states in groups follows a published rule. There
  is no score, and a placement's confidence is shown beside it.
- **How much was checked by a person is stated, in numbers.** Every output says which facts were
  verified by a person under the two-person rule, and that the rest were checked by machine only.
- **Never:** confidential, classified or leaked material; personal data; anything behind a login.

## Corrections

- **Anyone can challenge any fact, on equal terms.** That includes a government, an operator or a
  vendor. Use **Check this fact** or **Submit a source**, which are public GitHub issue forms. There is no
  private channel, so there is no special treatment.
- **A fact is never silently changed.** A rejection by an eligible reviewer makes it **disputed**: shown,
  with the reason and the issue number, and not printed as fact. A newer or higher-tier source supersedes
  a fact under the published rule, and the earlier source stays in the record. Contradictions that no
  rule settles stay disputed, showing both sources.
- **The maintainer is bound by the same rules.** Registers are produced by admission, and
  `./run.sh admit --check` fails if one is edited by hand. Every change is in the public git history, and
  `CHANGELOG.md` records each one, including the project's own mistakes.

## Contributors and reviewers

- **Contributors may be pseudonymous.** Trust comes from the evidence, not from who submitted it.
- **Reviewers are on a public roster** (`model/contrib/reviewers.csv`), added by a reviewed pull request,
  and they must:
  - declare the languages they read;
  - never review their own submission;
  - declare any conflict of interest (employment by, or a financial interest in, a body or company the
    fact concerns), which makes their review not count.
- **No incentives.** Contributors and reviewers are not paid, and do not pay. Attribution is optional.

## The limits, stated plainly

- Most facts are checked by machine only, and the share verified by a person is in every output.
- The automated reviewer in agent research runs is the same model as the agent researcher.
- English wording of a non-English source is machine-translated. Its figures are checked against the
  original; its words are not.
- The classification of sources into tiers was drawn up by an agent and is open to correction like
  anything else.
