# Contributing

This project maps, for each EU member state, the critical government data holdings it keeps, who
operates them, and where they run. It is built **bottom-up**: anyone in any member state can add a
source or check a fact. You know where your government publishes things, and you read its language.

There are two ways to help. Neither needs any code.

## 1. Submit a source

**[Submit a source](https://github.com/pieteradejong/sovereign-data-centers/issues/new?template=submit-source.yml)**,
or use the *Submit a source* link on any country page. Submit:
- a source for a value the report withholds;
- a better source for a printed fact;
- newer information;
- or a correction.

What makes a submission usable:

| Needed | Why |
|---|---|
| **A public document** at an exact `https://` URL, which anyone can open without logging in | A reader must be able to check it |
| **An official source where possible:** the law portal or gazette, the ministry or agency, the operator's own site, the statistics office or the audit office | Only official sources (tiers T1/T2) are admitted. Press, encyclopedias and unofficial copies of laws are not |
| **A verbatim quote** of 8 to 60 words, copied from the page in its own language | A machine fetches the page and looks for these exact words |
| **A value** that the quote alone establishes | Every number and date in the value must be in the quote |

**Never submit:**
- confidential, classified or leaked material;
- anything behind a login;
- anyone's personal data.

Submissions that break these rules are closed, not processed.

## 2. Check a fact

Every fact on the site, and in the PDF appendices, has a **Check this fact** link. It opens a short
form: open the source, find the quote, and say whether it establishes the printed value. You can also
check a citizen's submission by its issue number.

**Anyone may report a problem this way.** For a check to count as *human verification*, the reviewer
must be on the reviewer roster: see [`docs/reviewing.md`](docs/reviewing.md).

## What happens next: the two-person rule

1. **A machine checks it.** The page is fetched and fingerprinted, and the quote must be on it. Every
   number in the value must be in the quote, and the source's tier is recorded. The outcome is noted on
   your issue.
2. **A different person checks it.** A reviewer on the roster, who reads the source's language and
   declares no conflict of interest, confirms or rejects it. **You can never review your own
   submission.**
3. **The rules admit it.** A confirmed submission is admitted. If it disagrees with a printed fact, a
   higher-tier source wins, and so does a later statement by the same authority. Otherwise both are
   shown as *disputed*, and neither is printed as fact. Nobody decides by judgement, including the
   maintainer.

Every step is public in the issue thread, and reproducible from the repository (`./run.sh admit
--check`).

## Your contribution's terms

- By submitting, you license your contribution under **[CC BY 4.0](LICENSE-DATA)**, the same licence
  as the dataset. You sign it off under the **[Developer Certificate of Origin](https://developercertificate.org)**:
  you have the right to submit it. You keep your copyright; nothing is assigned.
- **Pseudonymous is fine.** Your GitHub handle is stored, because the two-person rule needs to know who
  submitted and who reviewed. It is shown in the outputs only if you tick *Credit me*.
- The project is independent and unaffiliated. See the [editorial policy](docs/editorial-policy.md) for
  how it is run and funded.

## Code

Code changes are welcome as pull requests. `./test.sh` must pass, and [`CLAUDE.md`](CLAUDE.md) lists the
commands and the rules that must not be bent. Code is MIT-licensed ([`LICENSE`](LICENSE)).
