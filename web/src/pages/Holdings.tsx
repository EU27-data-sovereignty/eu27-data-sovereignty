import { useState } from 'react'
import { Link, useParams } from 'react-router-dom'

import { PageBand } from '@/components/PageBand'
import { Bar, CARD } from '@/components/ui'
import { SpanView } from '@/components/DocumentView'
import { SourceList } from '@/components/SourceList'
import type { Bundle, Document, Span } from '@/data/types'
import { claimsBySource, numberSources } from '@/data/sources'
import { NotFound } from './NotFound'

const TIER_NOTE: Record<number, string> = {
  0: 'The identity spine: civil registry, biometrics, eID, PKI',
  1: 'The legal, fiscal and security state',
  2: 'Health records, public health, statistics',
  3: 'Geospatial base data, digital archives',
}

/** Every holding class with how many states have a verified source for it, by tier (#99 layout). */
export function HoldingsIndex({ bundle }: { bundle: Bundle }) {
  const [domain, setDomain] = useState('all')
  const countries = Object.values(bundle.countries)
  const rows = bundle.holding_classes.map(h => ({
    h,
    n: countries.filter(c =>
      c.national_data.some(e => e.record_class === h.class_id && e.status !== 'unrecorded'),
    ).length,
  }))
  const tiers = [...new Set(bundle.holding_classes.map(h => h.tier))].sort()
  const domains = [...new Set(bundle.holding_classes.map(h => h.domain))]
  const shown = rows.filter(r => domain === 'all' || r.h.domain === domain)
  const half = countries.length / 2

  return (
    <article>
      <PageBand kicker="EU-27 · Critical holdings" title="Critical holdings">
        <p className="mt-3 max-w-3xl text-white/85">
          The {bundle.holding_classes.length} kinds of government data holding this project
          inventories, in tier order: tier 0 is the identity spine, tier 1 the legal, fiscal and
          security state. Open one to compare it across all 27 member states.
        </p>
      </PageBand>

      <ul className="mb-7 grid grid-cols-2 gap-3 lg:grid-cols-4" aria-label="Holdings by tier">
        {tiers.map(t => (
          <li key={t} className={`${CARD} p-4`}>
            <span className="text-xs font-semibold tracking-[0.1em] text-[var(--color-accent-text)] uppercase">
              Tier {t}
            </span>
            <span className="block font-display text-3xl font-bold tabular-nums">
              {bundle.holding_classes.filter(h => h.tier === t).length}
            </span>
            <span className="text-sm text-[var(--color-fg-secondary)]">{TIER_NOTE[t] ?? ''}</span>
          </li>
        ))}
      </ul>

      <div role="group" aria-label="Filter by domain" className="mb-4 flex flex-wrap gap-1.5">
        {['all', ...domains].map(d => (
          <button
            key={d}
            type="button"
            aria-pressed={domain === d}
            onClick={() => setDomain(d)}
            className={`rounded-full border px-3 py-1 text-sm capitalize ${
              domain === d
                ? 'border-[var(--color-eu-blue)] bg-[var(--color-eu-blue)] text-white'
                : 'border-[var(--color-border)] text-[var(--color-fg-secondary)] hover:text-[var(--color-fg-primary)]'
            }`}
          >
            {d === 'all' ? 'All domains' : d}
          </button>
        ))}
      </div>

      <div className={`scroll-x ${CARD}`}>
        <table className="w-full min-w-[34rem] border-collapse text-sm">
          <thead>
            <tr className="bg-[var(--color-bg-emphasis)] text-xs tracking-wider text-[var(--color-fg-muted)] uppercase shadow-[inset_0_-2px_0_var(--color-eu-blue)]">
              <th scope="col" className="px-4 py-2.5 text-left font-semibold">
                Holding
              </th>
              <th scope="col" className="px-4 py-2.5 text-left font-semibold">
                Domain
              </th>
              <th scope="col" className="px-4 py-2.5 text-left font-semibold">
                States verified
              </th>
            </tr>
          </thead>
          {tiers.map(t => {
            const group = shown.filter(r => r.h.tier === t)
            if (!group.length) return null
            return (
              <tbody key={t}>
                <tr>
                  <th
                    colSpan={3}
                    scope="colgroup"
                    className="bg-[var(--color-bg-emphasis)]/60 px-4 py-2 text-left text-xs font-semibold tracking-[0.1em] text-[var(--color-accent-text)] uppercase"
                  >
                    Tier {t} · {TIER_NOTE[t] ?? ''}
                  </th>
                </tr>
                {group.map(({ h, n }) => (
                  <tr key={h.class_id} className="border-t border-[var(--color-border)]">
                    <th scope="row" className="px-4 py-2.5 text-left font-medium">
                      <Link to={`/holdings/${h.class_id}`} className="hover:underline">
                        {h.label}
                      </Link>
                    </th>
                    <td className="px-4 py-2.5 text-[var(--color-fg-muted)] capitalize">
                      {h.domain}
                    </td>
                    <td className="px-4 py-2.5">
                      <Bar value={n} max={countries.length} faded={n < half} />
                    </td>
                  </tr>
                ))}
              </tbody>
            )
          })}
        </table>
      </div>
      <p className="mt-3 text-sm text-[var(--color-fg-muted)]">
        Faded bars: fewer than half the member states verified. A gap means not yet sourced, never
        that the holding does not exist.
      </p>
    </article>
  )
}

/**
 * One holding class across the 27. The cells are the same spans the country documents show
 * for that row, so a fact here carries the same source as on the country page.
 */
export function Holding({ bundle }: { bundle: Bundle }) {
  const { cls = '' } = useParams()
  const meta = bundle.holding_classes.find(h => h.class_id === cls)
  if (!meta) return <NotFound />

  const rows: { iso: string; name: string; cells: Span[] }[] = []
  let columns: string[] = []
  for (const doc of Object.values(bundle.documents).sort((a, b) => a.name.localeCompare(b.name))) {
    const table = doc.sections.find(s => s.id === 'holdings')?.blocks.find(b => b.type === 'table')
    if (!table || table.type !== 'table') continue
    columns = table.columns.slice(2).map(c => c.t)
    const row = table.rows.find(r => r[1]?.t.startsWith(`${meta.label} (`))
    if (row) rows.push({ iso: doc.iso, name: doc.name, cells: row.slice(2) })
  }
  // A synthetic one-section document per row, so footnote numbering follows this page.
  const docs: Document[] = rows.map(r => ({
    iso: r.iso,
    name: r.name,
    sections: [{ id: 'row', title: '', blocks: [{ type: 'list', items: [r.cells] }] }],
  }))
  const numbers = numberSources(docs, bundle)
  const claims = claimsBySource(docs, bundle)

  return (
    <article>
      <p className="text-xs tracking-widest text-[var(--color-fg-muted)] uppercase">
        <Link to="/holdings" className="hover:underline">
          Critical holdings
        </Link>{' '}
        · tier {meta.tier}
      </p>
      <PageBand kicker="EU-27 · Critical holding" title={meta.label} />
      <div className="scroll-x rounded border border-[var(--color-border)] bg-[var(--color-bg-card)]">
        <table className="w-full min-w-[40rem] border-collapse text-sm">
          <thead>
            <tr className="bg-[var(--color-bg-emphasis)] text-xs tracking-wider text-[var(--color-fg-muted)] uppercase shadow-[inset_0_-2px_0_var(--color-eu-blue)]">
              {['Country', ...columns].map(h => (
                <th key={h} scope="col" className="px-3.5 py-2.5 text-left">
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map(r => (
              <tr key={r.iso} className="border-t border-[var(--color-border)] align-top">
                <th scope="row" className="px-3.5 py-2.5 text-left font-normal">
                  <Link
                    to={`/country/${r.iso}`}
                    className="text-[var(--color-accent-text)] underline"
                  >
                    {r.name}
                  </Link>
                </th>
                {r.cells.map((cell, i) => (
                  <td key={i} className="px-3.5 py-2.5">
                    <SpanView span={cell} numbers={numbers} bundle={bundle} />
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
