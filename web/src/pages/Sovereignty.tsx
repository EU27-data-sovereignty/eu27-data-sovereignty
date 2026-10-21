import { useEffect, useMemo, useRef, useState } from 'react'
import { Link } from 'react-router-dom'

import { EuMap } from '@/charts/EuMap'
import { GROUP_FILL } from '@/charts/groups'
import { SpanView } from '@/components/DocumentView'
import { SourceList } from '@/components/SourceList'
import { claimsBySource, numberSources } from '@/data/sources'
import type { Bundle, Document, GroupId, Placement, Span } from '@/data/types'
import { PageBand } from '@/components/PageBand'
import { useTx } from '@/i18n'
import { countryPath } from '@/utils/routes'

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
  const { tx, txr } = useTx()
  // The filter's and the explanation's words for a confidence level, one sentence each.
  const level = (c: Confidence) =>
    ({ All: tx('All'), High: tx('High'), Medium: tx('Medium'), Low: tx('Low') })[c]
  const levelPhrase = (c: Placement['confidence']) =>
    ({ High: tx('High confidence'), Medium: tx('Medium confidence'), Low: tx('Low confidence') })[c]
  const finding = (k: 'Yes' | 'Partly' | 'No') =>
    ({ Yes: tx('Yes'), Partly: tx('Partly'), No: tx('No') })[k]
  const [filter, setFilter] = useState<Confidence>('All')
  const [selected, setSelected] = useState<string | null>(null)
  const detailRef = useRef<HTMLElement>(null)
  // A state picked from the group list on a phone has its explanation below the map, out of sight: bring it
  // into view. "nearest" leaves the page still when the explanation is already visible.
  useEffect(() => {
    if (!selected) return
    const reduce = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches
    detailRef.current?.scrollIntoView({ block: 'nearest', behavior: reduce ? 'auto' : 'smooth' })
  }, [selected])
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
        kicker={tx('EU-27 · Ranking by published rule')}
        title={tx('Data-sovereignty ranking')}
        facts={sov.groups
          .map(
            g => [g, Object.values(sov.placements).filter(p => p.group === g.id).length] as const,
          )
          .filter(([, n]) => n > 0)
          .map(([g, n]) => [String(n), g.label])}
      />
      <p className="mb-3 max-w-3xl rounded border-l-4 border-[var(--color-accent-text)] bg-[var(--color-bg-emphasis)] px-4 py-3 text-sm">
        {sov.guardrail}
      </p>
      <p className="mb-4 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        {tx('States are placed in groups by a published rule, not scored.')}{' '}
        {tx('An input without a checked source counts as not demonstrated.')}{' '}
        {tx(
          'The bar beside each state shows the groups it could still reach once its open evidence is settled; that range is its confidence.',
        )}{' '}
        <Link to="/methodology#m-calculations" className="underline">
          {tx('The rule in full')}
        </Link>
        .
      </p>

      <fieldset className="mb-4 flex flex-wrap items-center gap-2 text-sm">
        <legend className="sr-only">{tx('Show placements by confidence')}</legend>
        <span className="mr-1">{tx('Confidence:')}</span>
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
            {level(c)}
          </button>
        ))}
      </fieldset>

      <div className="mb-10 grid gap-6 lg:grid-cols-2 lg:items-start">
        <section aria-label={tx('Groups')}>
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
                        className={`flex items-center gap-1.5 rounded border-2 border-[var(--color-border)] bg-[var(--color-bg-emphasis)] px-2 py-1 text-sm hover:border-[var(--color-accent-text)] ${CHIP[p.confidence]} ${
                          selected === iso ? 'border-[var(--color-accent)]' : ''
                        }`}
                      >
                        {names[iso]}
                        <span className="text-[var(--color-fg-muted)]">{level(p.confidence)}</span>
                        <RangeBar p={p} order={order} />
                      </button>
                    </li>
                  ))}
                  {members.length === 0 ? (
                    <li className="text-xs text-[var(--color-fg-muted)] italic">{tx('None')}</li>
                  ) : null}
                </ul>
              </div>
            )
          })}
        </section>

        <section aria-label={tx('Map')} className="self-start lg:sticky lg:top-6">
          <EuMap
            placements={Object.fromEntries(visible)}
            labels={labels}
            names={names}
            selected={selected}
            onSelect={setSelected}
          />
          <p className="mt-1 text-xs text-[var(--color-fg-muted)]">
            {tx('Hatched: Low confidence.')} {tx('Select a state for its explanation.')}
          </p>
          {/* The explanation sits under the map, so it is read where the state was picked */}
          {sel && selected ? (
            <section
              ref={detailRef}
              aria-live="polite"
              className="mt-4 scroll-mt-6 rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-5 shadow-[inset_0_3px_0_var(--color-accent-text)] sm:p-6"
            >
              <h2 className="font-display text-2xl font-bold">{names[selected]}</h2>
              <p className="mb-2 text-sm">
                <strong>{labels[sel.group]}</strong> · {levelPhrase(sel.confidence)} ·{' '}
                {sel.range.length > 1
                  ? tx('could still reach {from} to {to}', {
                      from: labels[sel.range[0]!] ?? '',
                      to: labels[sel.range[sel.range.length - 1]!] ?? '',
                    })
                  : tx('could still reach {from}', { from: labels[sel.range[0]!] ?? '' })}
              </p>
              <h3 className="text-sm font-semibold">{tx('What could move it')}</h3>
              <ul className="mb-2 list-disc pl-5 text-sm">
                {sel.could_move.map((m, i) => (
                  <li key={i}>
                    {m.input === 'holdings'
                      ? tx(
                          '{n, plural, one {If the # tier 0/1 holding with unsourced hosting runs on non-EU infrastructure: {group}} other {If any of # tier 0/1 holdings with unsourced hosting runs on non-EU infrastructure: {group}}}',
                          { n: m.count ?? 0, group: String(labels[m.group]) },
                        )
                      : tx('If {indicator} is found to be {value}: {group}', {
                          indicator: String(
                            sov.indicators.find(x => x.id === m.input)?.label.toLowerCase(),
                          ),
                          value: String(m.if),
                          group: String(labels[m.group]),
                        })}
                  </li>
                ))}
              </ul>
              <Link to={countryPath(selected)} className="text-sm underline">
                {tx('Full analysis of {name}', { name: names[selected] ?? '' })}
              </Link>
            </section>
          ) : null}
        </section>
      </div>

      <section id="indicators" aria-label={tx('Indicators')} className="scroll-mt-6">
        <h2 className="mb-2 font-display font-bold text-xl text-[var(--color-accent-text)]">
          {tx('The indicators')}
        </h2>
        <div className="scroll-x rounded border border-[var(--color-border)] bg-[var(--color-bg-card)]">
          <table className="w-full min-w-[40rem] border-collapse text-sm">
            <thead>
              <tr className="bg-[var(--color-bg-emphasis)] text-xs font-semibold tracking-wider text-[var(--color-fg-primary)] uppercase shadow-[inset_0_-2px_0_var(--color-accent-text)]">
                <th scope="col" className="px-3.5 py-2.5 text-left">
                  <button type="button" onClick={() => setSortBy('name')} className="font-semibold">
                    {tx('State')}
                    {sortBy === 'name' ? ' ▾' : ''}
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
                      to={countryPath(r.iso)}
                      className="text-[var(--color-accent-text)] underline"
                    >
                      {names[r.iso]}
                    </Link>
                  </th>
                  {r.cells.map((cell, i) => (
                    <td key={i} className="px-3.5 py-2.5">
                      <span className={PILL[cell.t] ?? ''}>
                        <SpanView span={cell} numbers={numbers} bundle={bundle} compact />
                      </span>
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <ul
          aria-label={tx('Key')}
          className="mt-3 flex flex-wrap gap-x-4 gap-y-2 text-sm text-[var(--color-fg-secondary)]"
        >
          {(['Yes', 'Partly', 'No'] as const).map(k => (
            <li key={k}>
              <span className={PILL[k]}>{finding(k)}</span>
            </li>
          ))}
          <li>
            {txr('{term}: a gap, never a no', {
              term: <em className="text-[var(--color-fg-muted)]">{tx('Not yet sourced')}</em>,
            })}
          </li>
          <li>
            {txr('{term}: withheld until corrected and checked again', {
              term: (
                <em className="border-b border-dashed border-[var(--color-gap-mark)] text-[var(--color-fg-muted)]">
                  {tx('Disputed')}
                </em>
              ),
            })}
          </li>
        </ul>
      </section>
      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
