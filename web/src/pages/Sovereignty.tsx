import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'

import { EuMap } from '@/charts/EuMap'
import { GROUP_FILL } from '@/charts/groups'
import { SpanView } from '@/components/DocumentView'
import { SourceList } from '@/components/SourceList'
import { claimsBySource, numberSources } from '@/data/sources'
import type { Bundle, Document, GroupId, Placement, Span } from '@/data/types'
import { PageBand } from '@/components/PageBand'

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

/** Indicator findings as pills; the word stays, so colour is never the only cue. */
const PILL: Record<string, string> = {
  Yes: 'rounded-full bg-[var(--color-eu-blue)] px-2.5 py-0.5 text-xs font-semibold text-white',
  Partly:
    'rounded-full border border-[var(--color-eu-blue)] px-2.5 py-0.5 text-xs font-semibold text-[var(--color-accent-text)]',
  No: 'rounded-full border-2 border-[var(--color-rank-5)] px-2.5 py-0.5 text-xs font-semibold',
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
  // Each group's rule, in the methodology's own words (model/methodology.py), not restated here.
  const rule = useMemo(() => {
    const out: Record<string, string> = {}
    for (const sec of bundle.methodology.sections)
      for (const b of sec.blocks)
        if (b.type === 'list')
          for (const item of b.items) {
            const text = item.map(x => x.t).join(' ')
            const g = sov.groups.find(x => text.startsWith(`${x.label}: `))
            if (g) out[g.id] = text.slice(g.label.length + 2)
          }
    return out
  }, [bundle, sov])
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
      <PageBand
        kicker="EU-27 · Ranking by published rule"
        title="Data-sovereignty ranking"
        facts={sov.groups
          .map(
            g => [g, Object.values(sov.placements).filter(p => p.group === g.id).length] as const,
          )
          .filter(([, n]) => n > 0)
          .map(([g, n]) => [String(n), g.label])}
      />
      <p className="mb-3 max-w-3xl rounded border-l-4 border-[var(--color-highlight)] bg-[var(--color-bg-emphasis)] px-4 py-3 text-sm">
        {sov.guardrail}
      </p>
      <p className="mb-4 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        States are placed in groups by a published rule, not scored. An input without a checked
        source counts as not demonstrated. The bar beside each state shows the groups it could still
        reach once its open evidence is settled; that range is its confidence.{' '}
        <Link to="/methodology#m-calculations" className="underline">
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
            className={`rounded border px-3 py-1 ${
              filter === c
                ? 'border-[var(--color-eu-blue)] bg-[var(--color-eu-blue)] text-white'
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
              <div
                key={g.id}
                className="relative mb-2.5 overflow-hidden rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] py-3.5 pr-4 pl-5"
              >
                <span
                  aria-hidden="true"
                  className="absolute inset-y-0 left-0 w-1"
                  style={{ background: GROUP_FILL[g.id] }}
                />
                <h2 className="mb-2 flex items-center gap-2 font-display text-base font-bold">
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
                {rule[g.id] ? (
                  <p className="mb-2.5 max-w-xl text-sm text-[var(--color-fg-muted)] first-letter:uppercase">
                    {rule[g.id]}
                  </p>
                ) : null}
                <ul className="flex flex-wrap gap-1.5">
                  {members.map(([iso, p]) => (
                    <li key={iso}>
                      <button
                        type="button"
                        onClick={() => setSelected(iso)}
                        aria-pressed={selected === iso}
                        className={`flex items-center gap-1.5 rounded border-2 border-[var(--color-border)] bg-[var(--color-bg-emphasis)] px-2 py-1 text-sm hover:border-[var(--color-eu-gold)] ${CHIP[p.confidence]} ${
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
          className="mb-10 rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-5 shadow-[inset_0_3px_0_var(--color-eu-gold)] sm:p-6"
        >
          <h2 className="font-display text-2xl font-bold">{names[selected]}</h2>
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
        <h2 className="mb-2 font-display font-bold text-xl text-[var(--color-accent-text)]">
          The indicators
        </h2>
        <div className="scroll-x rounded border border-[var(--color-border)] bg-[var(--color-bg-card)]">
          <table className="w-full min-w-[40rem] border-collapse text-sm">
            <thead>
              <tr className="bg-[var(--color-bg-emphasis)] text-xs tracking-wider text-[var(--color-fg-muted)] uppercase shadow-[inset_0_-2px_0_var(--color-eu-blue)]">
                <th scope="col" className="px-3.5 py-2.5 text-left">
                  <button type="button" onClick={() => setSortBy('name')} className="font-semibold">
                    State{sortBy === 'name' ? ' ▾' : ''}
                  </button>
                </th>
                {sov.indicators.map(ind => (
                  <th
                    key={ind.id}
                    scope="col"
                    className="px-3.5 py-2.5 text-left"
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
                <tr key={r.iso} className="border-t border-[var(--color-border)]">
                  <th scope="row" className="px-3.5 py-2.5 text-left font-normal">
                    <Link
                      to={`/country/${r.iso}`}
                      className="text-[var(--color-accent-text)] underline"
                    >
                      {names[r.iso]}
                    </Link>
                  </th>
                  {r.cells.map((cell, i) => (
                    <td key={i} className="px-3.5 py-2.5">
                      <span className={PILL[cell.t] ?? ''}>
                        <SpanView span={cell} numbers={numbers} bundle={bundle} />
                      </span>
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <ul
          aria-label="Key"
          className="mt-3 flex flex-wrap gap-x-4 gap-y-2 text-sm text-[var(--color-fg-secondary)]"
        >
          {(['Yes', 'Partly', 'No'] as const).map(k => (
            <li key={k}>
              <span className={PILL[k]}>{k}</span>
            </li>
          ))}
          <li>
            <em className="text-[var(--color-fg-muted)]">Not yet sourced</em>: a gap, never a no
          </li>
          <li>
            <em className="border-b border-dashed border-[var(--color-highlight)] text-[var(--color-fg-muted)]">
              Disputed
            </em>
            : withheld until corrected and checked again
          </li>
        </ul>
      </section>
      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
