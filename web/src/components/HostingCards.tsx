import { useState } from 'react'

import { SpanView } from './DocumentView'
import { CARD, FIELD } from './ui'
import type { Block, Bundle, Span } from '@/data/types'

type Dep = 'national' | 'eu' | 'mixed' | 'none' | 'disputed'

/** The dependency cell's own words decide its chip; nothing is inferred beyond them. */
function depOf(cell: Span | undefined): Dep {
  if (!cell) return 'none'
  if (cell.role === 'disputed') return 'disputed'
  if (cell.role !== 'fact') return 'none'
  if (cell.t.startsWith('National')) return 'national'
  if (cell.t.startsWith('EU provider')) return 'eu'
  if (cell.t.startsWith('Mixed')) return 'mixed'
  return 'none'
}

const CHIP: Record<Dep, string> = {
  national: 'bg-[var(--color-eu-blue)] text-white border-[var(--color-eu-blue)]',
  eu: 'bg-[var(--color-eu-gold)]/15 text-[var(--color-accent-text)] border-transparent',
  mixed: 'border-[var(--color-eu-blue)] text-[var(--color-accent-text)]',
  none: 'border-[var(--color-border)] text-[var(--color-fg-muted)]',
  disputed:
    'border-[var(--color-eu-gold)]/60 text-[var(--color-accent-text)] bg-[repeating-linear-gradient(135deg,color-mix(in_srgb,var(--color-eu-gold)_25%,transparent)_0_3px,transparent_3px_6px)]',
}

const NOTE: Record<Dep, string> = {
  national: 'A source says the system runs on state infrastructure.',
  eu: 'Run by a provider or platform based elsewhere in the EU.',
  mixed: 'National data centres with cloud access where required.',
  none: 'The source names the system but not where it runs.',
  disputed: 'The fact check could not confirm it; withheld until rechecked.',
}

const LABEL: Record<Dep, string> = {
  national: 'National infrastructure',
  eu: 'EU provider',
  mixed: 'Mixed',
  none: 'Not stated',
  disputed: 'Disputed',
}

/**
 * The hosting table of the infrastructure overview (#95) as cards grouped by state (#99 layout). Every
 * cell is the table's own span, rendered by SpanView with its footnote, so nothing new is said here.
 */
export function HostingCards({
  block,
  bundle,
  numbers,
}: {
  block: Extract<Block, { type: 'table' }>
  bundle: Bundle
  numbers: Map<string, number>
}) {
  const [state, setState] = useState('')
  const [dep, setDep] = useState<Dep | 'any'>('any')
  const [query, setQuery] = useState('')
  const [tier, setTier] = useState('')
  const heads = block.columns.map(c => c.t)
  const rows = block.rows.map(r => ({ cells: r, dep: depOf(r[5]) }))
  const states = [...new Set(rows.map(r => r.cells[0]!.t))]
  const tierOf = (r: (typeof rows)[0]) => /\(tier (\d)\)/.exec(r.cells[1]!.t)?.[1] ?? ''
  const term = query.trim().toLowerCase()
  const shown = rows.filter(
    r =>
      (!state || r.cells[0]!.t === state) &&
      (dep === 'any' || r.dep === dep) &&
      (!tier || tierOf(r) === tier) &&
      (!term || r.cells.some(c => c.t.toLowerCase().includes(term))),
  )
  const counts = Object.fromEntries(
    (Object.keys(LABEL) as Dep[]).map(d => [d, rows.filter(r => r.dep === d).length]),
  )

  return (
    <div className="mb-6">
      <div
        role="group"
        aria-label="Infrastructure dependency"
        className="mb-5 grid grid-cols-2 gap-2.5 md:grid-cols-3 lg:grid-cols-5"
      >
        {(Object.keys(LABEL) as Dep[]).map(d => (
          <button
            key={d}
            type="button"
            aria-pressed={dep === d}
            onClick={() => setDep(dep === d ? 'any' : d)}
            className={`${CARD} flex flex-col gap-1.5 p-3.5 text-left text-sm text-[var(--color-fg-secondary)] hover:border-[var(--color-fg-muted)] ${
              dep === d
                ? 'border-[var(--color-eu-gold)] shadow-[inset_0_0_0_1px_var(--color-eu-gold)]'
                : ''
            }`}
          >
            <span
              className={`self-start rounded-full border px-2.5 py-0.5 text-xs font-semibold ${CHIP[d]}`}
            >
              {LABEL[d]}
            </span>
            <span className="font-display text-2xl leading-none font-bold text-[var(--color-fg-primary)] tabular-nums">
              {counts[d]}
            </span>
            <span>{NOTE[d]}</span>
          </button>
        ))}
      </div>
      <div className="mb-4 flex flex-wrap items-center gap-3">
        <label htmlFor="hosting-search" className="sr-only">
          Search registers, operators or providers
        </label>
        <input
          id="hosting-search"
          type="search"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Search registers, operators or providers"
          className={`${FIELD} min-w-0 flex-[1_1_16rem]`}
        />
        <label htmlFor="hosting-state" className="sr-only">
          Member state
        </label>
        <select
          id="hosting-state"
          value={state}
          onChange={e => setState(e.target.value)}
          className={FIELD}
        >
          <option value="">All member states</option>
          {states.map(s => (
            <option key={s}>{s}</option>
          ))}
        </select>
        <label htmlFor="hosting-tier" className="sr-only">
          Tier
        </label>
        <select
          id="hosting-tier"
          value={tier}
          onChange={e => setTier(e.target.value)}
          className={FIELD}
        >
          <option value="">All tiers</option>
          {['0', '1', '2', '3'].map(t => (
            <option key={t} value={t}>
              Tier {t}
            </option>
          ))}
        </select>
        <span aria-live="polite" className="text-sm text-[var(--color-fg-muted)] tabular-nums">
          {shown.length} of {rows.length} rows
        </span>
      </div>
      {shown.length === 0 ? (
        <p className="text-[var(--color-fg-muted)]">No rows match these filters.</p>
      ) : null}
      {[...new Set(shown.map(r => r.cells[0]!.t))].map(s => {
        const group = shown.filter(r => r.cells[0]!.t === s)
        return (
          <section key={s} aria-label={s} className="mb-6">
            <h3 className="mb-2.5 flex items-baseline gap-3 font-display text-xl font-bold">
              {s}
              <span className="font-sans text-sm font-normal text-[var(--color-fg-muted)]">
                {group.length} {group.length === 1 ? 'holding' : 'holdings'}
              </span>
            </h3>
            <ul className="grid gap-2.5">
              {group.map((r, i) => (
                <li
                  key={i}
                  className={`${CARD} grid gap-3 p-4 md:grid-cols-[minmax(0,200px)_minmax(0,1fr)_auto] md:gap-5`}
                >
                  <div className="font-semibold">
                    <SpanView span={r.cells[1]!} numbers={numbers} bundle={bundle} />
                  </div>
                  <dl className="grid grid-cols-[7.5rem_minmax(0,1fr)] gap-x-3 gap-y-1.5 text-sm">
                    {[2, 3, 4].map(k => (
                      <div key={k} className="contents">
                        <dt className="text-[var(--color-fg-muted)]">{heads[k]}</dt>
                        <dd>
                          <SpanView span={r.cells[k]!} numbers={numbers} bundle={bundle} />
                        </dd>
                      </div>
                    ))}
                    {r.dep === 'disputed' ? (
                      <div className="contents">
                        <dt className="text-[var(--color-fg-muted)]">{heads[5]}</dt>
                        <dd>
                          <SpanView span={r.cells[5]!} numbers={numbers} bundle={bundle} />
                        </dd>
                      </div>
                    ) : null}
                  </dl>
                  <span
                    className={`self-start rounded-full border px-2.5 py-0.5 text-xs font-semibold whitespace-nowrap ${CHIP[r.dep]}`}
                  >
                    {r.dep === 'national' || r.dep === 'eu' || r.dep === 'mixed' ? (
                      <SpanView span={r.cells[5]!} numbers={numbers} bundle={bundle} />
                    ) : (
                      LABEL[r.dep]
                    )}
                  </span>
                </li>
              ))}
            </ul>
          </section>
        )
      })}
    </div>
  )
}
