export const meta = {
  name: 'vet-eu27-facts',
  description: 'Vet every printed fact against top-tier sources, look for newer info, then fill gaps; blind review per state',
  phases: [
    { title: 'Research', detail: 'one researcher per state: upgrade, corroborate, supersede, contradict, fill gaps' },
    { title: 'Blind review', detail: 'one reviewer per state; sees URL and quote, never the proposed value' },
  ],
}

const MIRRORS = 'net.jogtar.hu, zakonyprolidi.cz, zakony.judikaty.info, lawspot.gr, zakon.hr, etaamb.openjustice.be, cylaw.org, wikipedia, wikisource, news sites'

const FINDINGS = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          claim: { type: 'string', description: 'the claim id from the input, unchanged' },
          question: { type: 'string', description: 'the "what" text of that input fact or gap, copied unchanged' },
          relation: { type: 'string', enum: ['upgrade', 'corroborates', 'supersedes', 'contradicts', 'fills_gap'] },
          url: { type: 'string', description: 'the exact https URL whose text contains the quote' },
          quote: { type: 'string', description: 'verbatim, 8-60 words, in the language of the page' },
          quote_english: { type: 'string', description: 'English translation of the quote; empty if the page is English' },
          value: { type: 'string', description: 'the value this quote establishes for the claim; every number in it must be in the quote' },
          published: { type: 'string', description: 'YYYY-MM-DD, YYYY-MM or YYYY the document was published or last consolidated; empty if not stated' },
          title: { type: 'string' },
          publisher: { type: 'string' },
          doc_type: { type: 'string', enum: ['legislation', 'official_page', 'annual_report', 'audit_report', 'statistics', 'procurement', 'eu_document'] },
          note: { type: 'string', description: 'one sentence: why this is better, newer, or what it contradicts' },
        },
        required: ['claim', 'question', 'relation', 'url', 'quote', 'quote_english', 'value', 'published', 'title', 'publisher', 'doc_type', 'note'],
      },
    },
    outcomes: {
      type: 'array',
      description: 'one entry for EVERY input fact and gap',
      items: {
        type: 'object',
        properties: {
          claim: { type: 'string' },
          status: { type: 'string', enum: ['found', 'no_better_found', 'not_reached'] },
        },
        required: ['claim', 'status'],
      },
    },
  },
  required: ['findings', 'outcomes'],
}

const VERDICTS = {
  type: 'object',
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'integer' },
          quote_found: { type: 'boolean', description: 'you fetched the URL and the quote appears in it verbatim' },
          established: { type: 'string', description: 'the value the quote itself establishes for the question; empty if it establishes none' },
          reason: { type: 'string' },
        },
        required: ['id', 'quote_found', 'established', 'reason'],
      },
    },
    reviewer_model: { type: 'string', description: 'your model id' },
  },
  required: ['verdicts', 'reviewer_model'],
}

function researchPrompt(s) {
  return `You are vetting the published findings of an independent research project about ${s.name} (${s.iso}): which critical government data holdings the state keeps, who operates them, where they run, and data-sovereignty indicators. Every value below was found by an earlier agent on one source. Your job is to find TOP-QUALITY sources and NEWER information. You are not editing anything: do not write or modify any file. Use WebSearch and WebFetch (load them with ToolSearch if they are deferred).

Source quality, best first:
- T1: the official law portal or official gazette of ${s.name} (consolidated text), EUR-Lex, the national statistics office, the operator's own official website.
- T2: the competent ministry, agency or regulator; the national audit office; an official annual report on a government domain.
- Never cite: ${MIRRORS}. They are copies, not sources. Only https URLs.

PART 1 — the printed facts (weakest source first). For each fact:
1. If it rests on a T3/T4 source (e.g. an unofficial law mirror), find the SAME statement on a T1/T2 source: relation "upgrade" (for a statute: the same provision on the official law portal).
2. Otherwise, if you can find an INDEPENDENT T1/T2 source stating the same thing: relation "corroborates".
3. Look for NEWER information than the source date: an amendment, a newer consolidated text, a newer annual figure, a renamed register or operator. Same authority, later date: relation "supersedes".
4. If a T1/T2 source states something DIFFERENT from the printed value: relation "contradicts".
Do not return a finding that uses the same URL as the current source.

PART 2 — the gaps. For each, find a T1/T2 source that establishes it: relation "fills_gap". For a holding: the official name of the register or system (value), and in separate findings with the same claim id pattern where you can: record:${s.iso}:<class>:operator, :count, :foreign_dependency (value one of national, eu_provider, non_eu_provider, mixed; only if the source says where the infrastructure runs). For an indicator: value yes, partial or no exactly as defined.

Rules for every finding:
- FETCH the URL yourself and copy the quote VERBATIM from the page text, 8-60 words, in the page's language. A quote that is not literally on that page will be rejected by a machine check.
- The value must be supported by the quote alone. Every number and date in the value must appear in the quote. No article numbers, second figures or commentary in the value; put context in "note".
- For a register or operator name, write the name as the quote gives it, followed by an English rendering in parentheses when the page is not English.
- For counts, give the figure and its unit as the quote states them, e.g. "10.4 million records".

Return findings, and an outcome for EVERY input fact and gap: found, no_better_found (you searched and found nothing better or newer), or not_reached (you ran out of time). Work in the given order.

INPUT: read the JSON file ${s.path} with the Read tool. It holds "facts" (${s.n_facts}) and "gaps" (${s.n_gaps}). Each has a claim id and a "what" describing the question; copy "what" into each finding's "question".`
}

function reviewPrompt(s, items) {
  return `You are an independent, skeptical reviewer for a research project about ${s.name} (${s.iso}). For each item below you get a question, a URL and a quotation someone claims is on that page. You are NOT told what answer they drew from it. Do not write or modify any file. Use WebFetch (load it with ToolSearch if deferred).

For each item:
1. Fetch the URL. quote_found = true only if the quotation appears on the page verbatim (ignoring whitespace and quote-mark style).
2. From the quotation alone, and the page context around it, state what it establishes as the answer to the question: a name, an operator, a count with its unit, one of national / eu_provider / non_eu_provider / mixed, or yes / partial / no for an indicator as defined in the question. If it establishes no answer, leave "established" empty. Do not use outside knowledge. Be strict: a quote that mentions a register without saying who operates it does not establish an operator.
3. Give a one-sentence reason.

Also report your model id in reviewer_model.

ITEMS (JSON):
${JSON.stringify(items)}`
}

const states = args
log(`${states.length} states, ${states.reduce((n, s) => n + s.n_facts, 0)} facts, ${states.reduce((n, s) => n + s.n_gaps, 0)} gaps`)

const results = await pipeline(
  states,
  s => agent(researchPrompt(s), { label: `research:${s.iso}`, phase: 'Research', schema: FINDINGS }),
  (found, s) => {
    if (!found) return { iso: s.iso, research: null, review: null }
    const items = found.findings.map((f, id) => ({
      id,
      question: f.question || f.claim,
      url: f.url,
      quote: f.quote,
    }))
    if (!items.length) return { iso: s.iso, research: found, review: { verdicts: [], reviewer_model: '' } }
    return agent(reviewPrompt(s, items), { label: `review:${s.iso}`, phase: 'Blind review', schema: VERDICTS })
      .then(review => ({ iso: s.iso, research: found, review, review_items: items }))
  },
)

const done = results.filter(r => r && r.research)
log(`research returned for ${done.length}/${states.length}; findings ${done.reduce((n, r) => n + r.research.findings.length, 0)}`)
return results
