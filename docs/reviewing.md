# Reviewing: how a person verifies a fact

A fact is **verified by a person** when someone on the reviewer roster confirms it under the
**two-person rule** (DECISIONS #85). This page is for reviewers. To contribute a source instead, see
[`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Becoming a reviewer

Open a pull request that adds one line to [`model/contrib/reviewers.csv`](../model/contrib/reviewers.csv):

```
handle,languages,countries,added,decision
your-github-handle,nl;en,NL,2026-10-01,#85
```

| Column | What it holds |
|---|---|
| `languages` | The languages you read well enough to judge a legal or official text, as ISO 639-1 codes separated by `;` |
| `countries` | Optional: the member states you know |
| `added` | The date |
| `decision` | Always `#85` |

The maintainer reviews the pull request. A pseudonym is fine. The roster exists so that one person
cannot pose as several, not to know who you are. Say in the pull request if you work for a government
body, an operator or a vendor in this field. That doesn't disqualify you, but you must then declare a
conflict on any fact concerning them.

## Reviewing a fact

1. Use **Check this fact** on the site, next to a fact's source, or in a PDF appendix. For a citizen's
   submission, enter its issue number (`#123`) in the form.
2. **Open the source yourself.** Don't rely on the quote shown: find it on the page.
3. **Answer one question: does the quote, on that page, establish the printed value?**
   - *Confirmed:* the quote is on the page, and it says what the value says.
   - *Rejected:* the quote is missing, or it doesn't establish the value. A wrong number, a different
     register or an outdated statement all count.
   - *Can't tell:* for example, the page won't load for you. This counts neither way.
4. Give the languages you read, and **declare any conflict of interest**. A declared conflict means the
   review is recorded but doesn't count. That's the rule doing its job, not a mark against you.

## What your review does

| Reviews of a fact (eligible reviewers only) | The fact |
|---|---|
| One confirmation, no rejection | **Verified**: the top grade, if it was already Strong |
| One rejection | **Disputed**: withheld, with your reason shown, until a second reviewer looks |
| Two rejections | **Withdrawn**: shown as a gap |
| Two confirmations against one rejection | Verified |

A review counts only if all of these hold:
- you are on the roster;
- you did not submit the fact;
- you declared that you read the source's language;
- you declared no conflict.

Each reviewer counts once per fact, however many times they review it. `python3 model/contrib.py status`
shows every fact's state, and why any review was not counted.

## The audit

Some review requests come from the **audit sample**: a seeded random sample of printed facts that nobody
has reviewed yet, drawn by state (`python3 model/contrib.py audit-sample`). Reviewing the sample is how
the project measures its own error rate. Please review audit facts exactly as you would any other.
