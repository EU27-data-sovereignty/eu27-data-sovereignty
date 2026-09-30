import type { Bundle, CountryData, Document, Span } from './types'

/** Every span in a document, in reading order. */
export function* spans(doc: Document): Generator<Span> {
  for (const s of doc.sections) {
    for (const b of s.blocks) {
      if (b.type === 'p' || b.type === 'callout') yield* b.spans
      else if (b.type === 'list') for (const item of b.items) yield* item
      else {
        yield* b.columns
        for (const row of b.rows) yield* row
      }
    }
  }
}

/**
 * Source numbers for one page, in first-citation order -- the same rule the PDF uses, so
 * footnote [3] on the web and [S3] in that country's PDF name the same document.
 */
export function numberSources(docs: Document[], bundle: Bundle): Map<string, number> {
  const order = new Map<string, number>()
  for (const doc of docs) {
    for (const span of spans(doc)) {
      for (const claim of span.c ?? []) {
        for (const cite of bundle.claims[claim] ?? []) {
          if (!order.has(cite.source_id)) order.set(cite.source_id, order.size + 1)
        }
      }
    }
  }
  return order
}

/** The claims each numbered source supports on this page, for the source list. */
export function claimsBySource(docs: Document[], bundle: Bundle): Map<string, string[]> {
  const out = new Map<string, string[]>()
  for (const doc of docs) {
    for (const span of spans(doc)) {
      for (const claim of span.c ?? []) {
        for (const cite of bundle.claims[claim] ?? []) {
          const list = out.get(cite.source_id) ?? []
          if (!list.includes(claim)) list.push(claim)
          out.set(cite.source_id, list)
        }
      }
    }
  }
  return out
}

export interface Coverage {
  verified: number
  total: number
  tier0: number
  tier0Total: number
  measured: number
}

/** How much of a country's critical-holdings inventory has a verified source. */
export function coverage(c: CountryData): Coverage {
  const e = c.national_data
  return {
    verified: e.filter(x => x.status !== 'unrecorded').length,
    total: e.length,
    tier0: e.filter(x => x.status !== 'unrecorded' && x.tier === 0).length,
    tier0Total: e.filter(x => x.tier === 0).length,
    measured: e.filter(x => x.record_count || x.data_size).length,
  }
}

/** How many of a document's facts are shown, and how many values are withheld as gaps. */
export function factCounts(doc: Document): { facts: number; gaps: number } {
  let facts = 0
  let gaps = 0
  for (const s of spans(doc)) {
    if (s.role === 'fact') facts++
    else if ((s.role === 'gap' || s.role === 'disputed') && s.t !== '—') gaps++
  }
  return { facts, gaps }
}
