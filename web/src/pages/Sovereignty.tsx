import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'

import { EuMap } from '@/charts/EuMap'
import { GROUP_FILL } from '@/charts/groups'
import { SpanView } from '@/components/DocumentView'
import { SourceList } from '@/components/SourceList'
import { claimsBySource, numberSources } from '@/data/sources'
import type { Bundle, Document, GroupId, Placement, Span } from '@/data/types'

type Confidence = 'All' | Placement['confidence']

/** The group range as five cells, the placed group marked: the confidence, drawn. */
function RangeBar({ p, order }: { p: Placement; order: GroupId[] }) {
  return (
    <span className="inline-flex gap-px align-middle" aria-hidden="true">
      {order.map(g => (
        <span
          key={g}
          className="h-2 w-2.5"
          style={{
            background: p.range.includes(g) ? GROUP_FILL[g] : 'var(--color-bg-emphasis)',
            outline: g === p.group ? '1.5px solid var(--color-fg-primary)' : undefined,
          }}
        />
      ))}
    </span>
  )
}

const CHIP: Record<Placement['confidence'], string> = {
  High: 'border-solid',
  Medium: 'border-dashed',
  Low: 'border-dotted',
}

/** The placement table rows from a country's document: indicator label -> finding span. */
function findings(doc: Document | undefined): Span[][] {
  const table = doc?.sections.find(s => s.id === 'placement')?.blocks.find(b => b.type === 'table')
  return table && table.type === 'table' ? table.rows : []
}

/**
 * The data-sovereignty ranking (#77): groups by a published rule, never a score. Each state's
 * confidence is the range of groups its open evidence could still move it to; the ladder is the
 * table view of the map, so nothing here is conveyed by colour alone.
 */
export function Sovereignty({ bundle }: { bundle: Bundle }) {
  const sov = bundle.sovereignty
  const [filter, setFilter] = useState<Confidence>('All')
  const [selected, setSelected] = useState<string | null>(null)
  const [sortBy, setSortBy] = useState<string>('name')

  const names = useMemo(
    () => Object.fromEntries(Object.values(bundle.documents).map(d => [d.iso, d.name])),
    [bundle],
  )
  const labels = Object.fromEntries(sov.groups.map(g => [g.id, g.label]))
  const order = sov.groups.map(g => g.id)
  const visible = Object.entries(sov.placements).filter(
    ([, p]) => filter === 'All' || p.confidence === filter,
  )

  const gridRows = useMemo(() => {
    const rows = Object.keys(sov.placements).map(iso => ({
      iso,
      cells: findings(bundle.documents[iso]).map(r => r[1]!),
    }))
    const rank = { Yes: 0, Partly: 1, No: 2 } as Record<string, number>
    const idx = sov.indicators.findIndex(i => i.id === sortBy)
    return rows.sort((a, b) =>
      idx < 0
        ? names[a.iso]!.localeCompare(names[b.iso]!)
        : (rank[a.cells[idx]?.t ?? ''] ?? 3) - (rank[b.cells[idx]?.t ?? ''] ?? 3) ||
          names[a.iso]!.localeCompare(names[b.iso]!),
    )
  }, [bundle, sov, sortBy, names])

  const docs: Document[] = gridRows.map(r => ({
    iso: r.iso,
    name: names[r.iso]!,
    sections: [{ id: 'grid', title: '', blocks: [{ type: 'list', items: [r.cells] }] }],
  }))
  const numbers = numberSources(docs, bundle)
  const claims = claimsBySource(docs, bundle)
  const sel = selected ? sov.placements[selected] : null

  return (
    <article>
      <h1 className="mb-1 text-2xl font-semibold">Data-sovereignty ranking</h1>
      <p className="mb-2 max-w-3xl border-l-4 border-[var(--color-highlight)] bg-[var(--color-bg-emphasis)] px-3 py-2 text-sm">
        {sov.guardrail}
      </p>
      <p className="mb-4 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        States are placed in groups by a published rule, not scored. An input without a checked
        source counts as not demonstrated. The bar beside each state shows the groups it could still
        reach once its open evidence is settled; that range is its confidence.{' '}
        <Link to="/methodology" className="underline">
          The rule in full
        </Link>
        .
      </p>

      <fieldset className="mb-4 flex flex-wrap items-center gap-2 text-sm">
        <legend className="sr-only">Show placements by confidence</legend>
        <span className="mr-1">Confidence:</span>
        {(['All', 'High', 'Medium', 'Low'] as Confidence[]).map(c => (
          <button
            key={c}
            type="button"
            aria-pressed={filter === c}
            onClick={() => setFilter(c)}
            className={`rounded border px-2 py-0.5 ${
              filter === c
                ? 'border-[var(--color-accent)] bg-[var(--color-accent)] text-[var(--color-fg-on-accent)]'
                : 'border-[var(--color-border)]'
            }`}
          >
            {c}
          </button>
        ))}
      </fieldset>

      <div className="mb-10 grid gap-6 lg:grid-cols-2">
        <section aria-label="Groups">
          {sov.groups.map(g => {
            const members = visible
              .filter(([, p]) => p.group === g.id)
              .sort((a, b) => names[a[0]]!.localeCompare(names[b[0]]!))
            return (
              <div key={g.id} className="mb-3 border-b border-[var(--color-border)] pb-2">
                <h2 className="mb-1 flex items-center gap-2 text-sm font-semibold">
                  <span
                    aria-hidden="true"
                    className="inline-block h-3 w-3"
                    style={{ background: GROUP_FILL[g.id] }}
                  />
                  {g.label}
                  <span className="font-normal text-[var(--color-fg-muted)]">
                    ({members.length})
                  </span>
                </h2>
                <ul className="flex flex-wrap gap-1.5">
                  {members.map(([iso, p]) => (
                    <li key={iso}>
                      <button
                        type="button"
                        onClick={() => setSelected(iso)}
                        aria-pressed={selected === iso}
                        className={`flex items-center gap-1.5 rounded border-2 border-[var(--color-border)] bg-[var(--color-bg-card)] px-1.5 py-0.5 text-xs ${CHIP[p.confidence]} ${
                          selected === iso ? 'border-[var(--color-accent)]' : ''
                        }`}
                      >
                        {names[iso]}
                        <span className="text-[var(--color-fg-muted)]">{p.confidence}</span>
                        <RangeBar p={p} order={order} />
                      </button>
                    </li>
                  ))}
                  {members.length === 0 ? (
                    <li className="text-xs text-[var(--color-fg-muted)] italic">None</li>
                  ) : null}
                </ul>
              </div>
            )
          })}
        </section>

        <section aria-label="Map">
          <EuMap
            placements={Object.fromEntries(visible)}
            labels={labels}
            names={names}
            selected={selected}
            onSelect={setSelected}
          />
          <p className="mt-1 text-xs text-[var(--color-fg-muted)]">
            Hatched: Low confidence. Select a state for its explanation.
          </p>
        </section>
      </div>

      {sel && selected ? (
        <section
          aria-live="polite"
          className="mb-10 rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-4"
        >
          <h2 className="text-lg font-semibold">{names[selected]}</h2>
          <p className="mb-2 text-sm">
            <strong>{labels[sel.group]}</strong> · {sel.confidence} confidence · could still reach{' '}
            {labels[sel.range[0]!]}
            {sel.range.length > 1 ? ` to ${labels[sel.range[sel.range.length - 1]!]}` : ''}
          </p>
          <h3 className="text-sm font-semibold">What could move it</h3>
          <ul className="mb-2 list-disc pl-5 text-sm">
            {sel.could_move.map((m, i) => (
              <li key={i}>
                {m.input === 'holdings'
                  ? `If any of ${m.count} tier 0/1 holdings with unsourced hosting runs on non-EU infrastructure`
                  : `If ${sov.indicators.find(x => x.id === m.input)?.label.toLowerCase()} is found to be ${m.if}`}
                : {labels[m.group]}
              </li>
            ))}
          </ul>
          <Link to={`/country/${selected}`} className="text-sm underline">
            Full analysis of {names[selected]}
          </Link>
        </section>
      ) : null}

      <section aria-label="Indicators">
        <h2 className="mb-2 text-lg font-semibold text-[var(--color-accent-text)]">
          The indicators
        </h2>
        <div className="scroll-x">
          <table className="w-full min-w-[40rem] border-collapse text-sm">
            <thead>
              <tr className="border-b-2 border-[var(--color-accent)] bg-[var(--color-bg-emphasis)]">
                <th scope="col" className="px-2 py-1.5 text-left">
                  <button type="button" onClick={() => setSortBy('name')} className="font-semibold">
                    State{sortBy === 'name' ? ' ▾' : ''}
                  </button>
                </th>
                {sov.indicators.map(ind => (
                  <th
                    key={ind.id}
                    scope="col"
                    className="px-2 py-1.5 text-left"
                    title={ind.question}
                  >
                    <button
                      type="button"
                      onClick={() => setSortBy(ind.id)}
                      className="font-semibold"
                    >
                      {ind.label}
                      {sortBy === ind.id ? ' ▾' : ''}
                    </button>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {gridRows.map(r => (
                <tr key={r.iso} className="border-b border-[var(--color-border)]">
                  <th scope="row" className="px-2 py-1.5 text-left font-normal">
                    <Link
                      to={`/country/${r.iso}`}
                      className="text-[var(--color-accent-text)] underline"
                    >
                      {names[r.iso]}
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
      </section>
      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
