import { coverage, factCounts } from './sources'
import type { Bundle, Span } from './types'
import type { Tx } from '@/i18n'

/**
 * The figures a guide page may show (#102). Each is counted from the bundle when the page renders, from
 * the same spans the reports print, so a value the fact check withheld is never counted and no number is
 * written into a guide by hand. Each takes the page's `tx`, so its value and label print in the page's language.
 */
export interface Figure {
  value: string
  label: string
  /** Where the figure can be checked. */
  to: string
}

const rows = (bundle: Bundle, iso: string, section: string): Span[][] => {
  const block = bundle.documents[iso]?.sections
    .find(s => s.id === section)
    ?.blocks.find(b => b.type === 'table')
  return block?.type === 'table' ? block.rows : []
}

const isos = (bundle: Bundle) => Object.keys(bundle.documents)

/** States whose report prints a sourced "Yes" for one ranking indicator. */
function indicatorYes(bundle: Bundle, id: string): number {
  const label = bundle.sovereignty.indicators.find(i => i.id === id)?.label
  return isos(bundle).filter(iso =>
    rows(bundle, iso, 'placement').some(
      r => r[0]?.t === label && r[1]?.role === 'fact' && r[1].t === 'Yes',
    ),
  ).length
}

const of27 = (tx: Tx, n: number) => tx('{n} of 27', { n })

export const FIGURES = {
  holdingsVerified: (b: Bundle, tx: Tx): Figure => {
    const c = Object.values(b.countries).map(coverage)
    return {
      value: tx('{n} of {total}', {
        n: c.reduce((n, x) => n + x.verified, 0),
        total: c.reduce((n, x) => n + x.total, 0),
      }),
      label: tx('critical holdings with a checked source'),
      to: '/countries',
    }
  },
  tier0Hosting: (b: Bundle, tx: Tx): Figure => {
    const tier0 = isos(b).flatMap(iso =>
      rows(b, iso, 'holdings').filter(r => r[1]?.t.includes('(tier 0)')),
    )
    return {
      value: tx('{n} of {total}', {
        n: tier0.filter(r => r[4]?.role === 'fact').length,
        total: tier0.length,
      }),
      label: tx('tier 0 holdings whose hosting a source states'),
      to: '/infrastructure',
    }
  },
  lowRecoverability: (b: Bundle, tx: Tx): Figure => {
    const all = Object.values(b.countries).flatMap(c => c.national_data)
    return {
      value: tx('{n} of {total}', {
        n: all.filter(e => e.recoverability === 'low').length,
        total: all.length,
      }),
      label: tx('holdings classed as hard to rebuild'),
      to: '/methodology#m-calculations',
    }
  },
  gaps: (b: Bundle, tx: Tx): Figure => ({
    value: Object.values(b.documents)
      .reduce((n, d) => n + factCounts(d).gaps, 0)
      .toLocaleString('en'),
    label: tx('values withheld as gaps or disputed, each one a question'),
    to: '/countries',
  }),
  sources: (b: Bundle, tx: Tx): Figure => ({
    value: Object.keys(b.sources).length.toLocaleString('en'),
    label: tx('checked sources, each hashed and quoted'),
    to: '/sources',
  }),
  statesWithHosting: (b: Bundle, tx: Tx): Figure => ({
    value: of27(tx, new Set(hostingRows(b).map(r => r[0]!.t)).size),
    label: tx('states with any sourced hosting'),
    to: '/infrastructure',
  }),
  notNational: (b: Bundle, tx: Tx): Figure => ({
    value: String(
      hostingRows(b).filter(r => r[5]?.role === 'fact' && !r[5].t.startsWith('National')).length,
    ),
    label: tx('holdings sourced to an EU provider or mixed hosting'),
    to: '/infrastructure',
  }),
  jurisdictionLaw: (b: Bundle, tx: Tx): Figure => ({
    value: of27(tx, indicatorYes(b, 'L1')),
    label: tx('states with a sourced jurisdiction requirement'),
    to: '/sovereignty#indicators',
  }),
  certification: (b: Bundle, tx: Tx): Figure => ({
    value: of27(tx, indicatorYes(b, 'L3')),
    label: tx('states with a sourced sovereign cloud certification'),
    to: '/sovereignty#indicators',
  }),
  trustAnchor: (b: Bundle, tx: Tx): Figure => ({
    value: of27(tx, indicatorYes(b, 'K1')),
    label: tx('states with a sourced state-controlled trust anchor'),
    to: '/sovereignty#indicators',
  }),
  eid: (b: Bundle, tx: Tx): Figure => ({
    value: of27(tx, indicatorYes(b, 'K2')),
    label: tx('states with a sourced state-controlled eID'),
    to: '/sovereignty#indicators',
  }),
  dataCentres: (b: Bundle, tx: Tx): Figure => ({
    value: of27(tx, indicatorYes(b, 'C1')),
    label: tx('states with sourced government data centres'),
    to: '/sovereignty#indicators',
  }),
  holdingClasses: (b: Bundle, tx: Tx): Figure => ({
    value: String(b.holding_classes.length),
    label: tx('holding classes in {n} tiers, one taxonomy for all 27', {
      n: new Set(b.holding_classes.map(h => h.tier)).size,
    }),
    to: '/holdings',
  }),
  lowConfidence: (b: Bundle, tx: Tx): Figure => ({
    value: of27(
      tx,
      Object.values(b.sovereignty.placements).filter(p => p.confidence === 'Low').length,
    ),
    label: tx('placements still at Low confidence'),
    to: '/sovereignty',
  }),
} satisfies Record<string, (b: Bundle, tx: Tx) => Figure>

export type FigureId = keyof typeof FIGURES

/** The rows of the hosting overview (#95): state, holding, register, operator, hosting, dependency. */
function hostingRows(bundle: Bundle): Span[][] {
  const block = bundle.infrastructure.sections
    .find(s => s.id === 'hosting')
    ?.blocks.find(b => b.type === 'table')
  return block?.type === 'table' ? block.rows : []
}
