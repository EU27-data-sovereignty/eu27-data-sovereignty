import { Link, useParams } from 'react-router-dom'

import { PageBand } from '@/components/PageBand'
import { SpanView } from '@/components/DocumentView'
import { SourceList } from '@/components/SourceList'
import type { Bundle, Document, Span } from '@/data/types'
import { claimsBySource, numberSources } from '@/data/sources'
import { NotFound } from './NotFound'

/** Every holding class with how many states have a verified source for it. */
export function HoldingsIndex({ bundle }: { bundle: Bundle }) {
  const countries = Object.values(bundle.countries)
  return (
    <article>
      <PageBand kicker="EU-27 · Critical holdings" title="Critical holdings" />
      <p className="mb-4 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        The {bundle.holding_classes.length} kinds of government data holding this project
        inventories, in tier order: tier 0 is the identity spine, tier 1 the legal, fiscal and
        security state. Open one to compare it across all 27 member states.
      </p>
      <div className="scroll-x">
        <table className="w-full min-w-[28rem] border-collapse text-sm">
          <thead>
            <tr className="border-b-2 border-[var(--color-accent)] bg-[var(--color-bg-emphasis)]">
              <th scope="col" className="px-2 py-1.5 text-left">
                Holding
              </th>
              <th scope="col" className="px-2 py-1.5 text-left">
                Domain
              </th>
              <th scope="col" className="px-2 py-1.5 text-right">
                Tier
              </th>
              <th scope="col" className="px-2 py-1.5 text-right">
                States verified
              </th>
            </tr>
          </thead>
          <tbody>
            {bundle.holding_classes.map(h => {
              const n = countries.filter(c =>
                c.national_data.some(
                  e => e.record_class === h.class_id && e.status !== 'unrecorded',
                ),
              ).length
              return (
                <tr key={h.class_id} className="border-b border-[var(--color-border)]">
                  <th scope="row" className="px-2 py-1.5 text-left font-normal">
                    <Link
                      to={`/holdings/${h.class_id}`}
                      className="text-[var(--color-accent-text)] underline"
                    >
                      {h.label}
                    </Link>
                  </th>
                  <td className="px-2 py-1.5">{h.domain}</td>
                  <td className="px-2 py-1.5 text-right tabular-nums">{h.tier}</td>
                  <td className="px-2 py-1.5 text-right tabular-nums">{n} of 27</td>
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
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
      <div className="scroll-x">
        <table className="w-full min-w-[40rem] border-collapse text-sm">
          <thead>
            <tr className="border-b-2 border-[var(--color-accent)] bg-[var(--color-bg-emphasis)]">
              {['Country', ...columns].map(h => (
                <th key={h} scope="col" className="px-2 py-1.5 text-left">
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {rows.map(r => (
              <tr key={r.iso} className="border-b border-[var(--color-border)] align-top">
                <th scope="row" className="px-2 py-1.5 text-left font-normal">
                  <Link
                    to={`/country/${r.iso}`}
                    className="text-[var(--color-accent-text)] underline"
                  >
                    {r.name}
                  </Link>
                </th>
                {r.cells.map((cell, i) => (
                  <td key={i} className="px-2 py-1.5">
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
