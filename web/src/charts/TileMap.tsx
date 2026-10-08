import { useState } from 'react'
import { Link } from 'react-router-dom'

import { Dots } from '@/components/ui'

/** Each state as one tile, placed roughly where it lies: [column, row] on a 7 × 7 grid. */
const POS: Record<string, [number, number]> = {
  SE: [4, 0],
  FI: [5, 0],
  IE: [0, 1],
  DK: [3, 1],
  EE: [5, 1],
  NL: [2, 2],
  DE: [3, 2],
  PL: [4, 2],
  LV: [5, 2],
  BE: [1, 3],
  LU: [2, 3],
  CZ: [3, 3],
  SK: [4, 3],
  LT: [5, 3],
  FR: [1, 4],
  AT: [3, 4],
  HU: [4, 4],
  RO: [5, 4],
  PT: [0, 5],
  ES: [1, 5],
  IT: [2, 5],
  SI: [3, 5],
  HR: [4, 5],
  BG: [5, 5],
  MT: [2, 6],
  EL: [5, 6],
  CY: [6, 6],
}

export interface TileState {
  iso: string
  name: string
  holdings: number
  holdingsTotal: number
  tier0: number
  tier0Total: number
  facts: number
}

type Metric = 'holdings' | 'tier0' | 'facts'

/**
 * The 27 as a tile map on the front page, shaded gold by how much verified evidence each has (#99).
 * Shade is never the only cue: each tile prints its number, and its label reads it out. It counts
 * evidence; it is not a ranking of how sovereign a state is (#77).
 */
export function TileMap({ states }: { states: TileState[] }) {
  const [metric, setMetric] = useState<Metric>('holdings')
  const [sel, setSel] = useState('DE')
  const by = Object.fromEntries(states.map(s => [s.iso, s]))
  const maxFacts = Math.max(1, ...states.map(s => s.facts))
  const value = (s: TileState) =>
    metric === 'holdings'
      ? [s.holdings, s.holdingsTotal]
      : metric === 'tier0'
        ? [s.tier0, s.tier0Total]
        : [s.facts, maxFacts]
  const cells: (TileState | null)[] = []
  for (let r = 0; r < 7; r++)
    for (let c = 0; c < 7; c++) {
      const iso = Object.keys(POS).find(k => POS[k]![0] === c && POS[k]![1] === r)
      cells.push(iso && by[iso] ? by[iso]! : null)
    }
  const s = by[sel] ?? states[0]!

  return (
    <div className="rounded border border-white/10 bg-[var(--color-night)]/60 p-4 backdrop-blur-[3px] sm:p-5">
      <div className="mb-3.5 flex flex-wrap items-center justify-between gap-3">
        <span className="text-xs font-semibold tracking-[0.14em] text-white/75 uppercase">
          Verified evidence by state
        </span>
        <div role="group" aria-label="Measure" className="flex rounded bg-white/10 p-0.5">
          {(
            [
              ['holdings', 'Holdings'],
              ['tier0', 'Tier 0'],
              ['facts', 'Facts'],
            ] as [Metric, string][]
          ).map(([m, label]) => (
            <button
              key={m}
              type="button"
              aria-pressed={metric === m}
              onClick={() => setMetric(m)}
              className={`rounded px-2.5 py-1 text-xs font-medium ${
                metric === m ? 'bg-[var(--color-eu-blue)] text-white' : 'text-white/75'
              }`}
            >
              {label}
            </button>
          ))}
        </div>
      </div>
      <div role="group" aria-label="Member states" className="grid grid-cols-7 gap-1 sm:gap-1.5">
        {cells.map((t, i) => {
          if (!t) return <span key={i} />
          const [v, max] = value(t)
          const share = max ? v! / max! : 0
          return (
            <button
              key={t.iso}
              type="button"
              aria-pressed={sel === t.iso}
              onClick={() => setSel(t.iso)}
              aria-label={`${t.name}: ${t.holdings} of ${t.holdingsTotal} holdings verified, ${t.tier0} of ${t.tier0Total} tier 0, ${t.facts} sourced facts`}
              className={`flex aspect-square flex-col items-center justify-center rounded text-[0.66rem] font-bold tracking-wide transition-transform hover:-translate-y-0.5 sm:text-xs ${
                share > 0.55 ? 'text-[var(--color-night)]' : 'text-white'
              } ${sel === t.iso ? 'ring-2 ring-white' : ''}`}
              style={{
                background: `color-mix(in oklab, var(--color-eu-gold) ${Math.round(12 + share * 88)}%, rgb(255 255 255 / 0.06))`,
              }}
            >
              {t.iso}
              <span className="hidden text-[0.72em] font-medium opacity-80 tabular-nums sm:block">
                {metric === 'facts' ? v : `${v}/${max}`}
              </span>
            </button>
          )
        })}
      </div>
      <div className="mt-3 flex items-center gap-2.5 text-xs text-white/60">
        <span>Less evidence</span>
        <span className="h-2 w-32 rounded bg-gradient-to-r from-white/10 to-[var(--color-eu-gold)]" />
        <span>More</span>
      </div>
      <div
        aria-live="polite"
        className="mt-3.5 flex flex-wrap items-end justify-between gap-3 border-t border-white/10 pt-3.5"
      >
        <div>
          <p className="font-display text-xl font-bold text-white">{s.name}</p>
          <p className="text-sm text-white/75 tabular-nums">
            {s.holdings} of {s.holdingsTotal} holdings verified · {s.facts} sourced facts
          </p>
          <div className="mt-1.5">
            <Dots
              value={s.tier0}
              max={s.tier0Total}
              title={`${s.tier0} of ${s.tier0Total} tier 0 holdings verified`}
            />
          </div>
        </div>
        <Link
          to={`/country/${s.iso}`}
          className="text-sm font-semibold whitespace-nowrap text-[var(--color-eu-gold)] hover:underline"
        >
          Open country →
        </Link>
      </div>
      <p className="mt-3 text-xs text-white/55">
        Counts of verified evidence, not a ranking of how sovereign a state is.
      </p>
    </div>
  )
}
