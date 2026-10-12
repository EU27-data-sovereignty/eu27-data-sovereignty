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
 * Four shades, not a continuous ramp: a tile mixed half and half is a mid-blue on which neither the light
 * nor the dark label reaches 4.5:1 (the first #101 deploy failed on exactly that). Each step's mix was
 * checked against its label colour in both themes; the lowest ratio is 5.5:1.
 */
const STEPS = [
  { below: 0.4, mix: 12, dark: false },
  { below: 0.65, mix: 26, dark: false },
  { below: 0.85, mix: 82, dark: true },
  { below: Infinity, mix: 100, dark: true },
]

/**
 * The 27 as a tile map on the front page, shaded blue by how much verified evidence each has (#99, #101).
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
    <div className="rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-4 sm:p-5">
      <div className="mb-3.5 flex flex-wrap items-center justify-between gap-3">
        <span className="text-xs font-bold tracking-[0.14em] text-[var(--color-accent-text)] uppercase">
          Verified evidence by state
        </span>
        <div
          role="group"
          aria-label="Measure"
          className="flex rounded bg-[var(--color-bg-emphasis)] p-0.5"
        >
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
                metric === m
                  ? 'bg-[var(--color-eu-blue)] text-white'
                  : 'text-[var(--color-fg-secondary)]'
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
          const step = STEPS.find(x => share < x.below) ?? STEPS[STEPS.length - 1]!
          return (
            <button
              key={t.iso}
              type="button"
              aria-pressed={sel === t.iso}
              onClick={() => setSel(t.iso)}
              aria-label={`${t.name}: ${t.holdings} of ${t.holdingsTotal} holdings verified, ${t.tier0} of ${t.tier0Total} tier 0, ${t.facts} sourced facts`}
              className={`flex aspect-square flex-col items-center justify-center rounded text-[0.66rem] font-bold tracking-wide transition-transform hover:-translate-y-0.5 sm:text-xs ${
                step.dark ? 'text-[var(--color-bg-card)]' : 'text-[var(--color-fg-primary)]'
              } ${sel === t.iso ? 'ring-2 ring-[var(--color-accent)] ring-offset-2 ring-offset-[var(--color-bg-card)]' : ''}`}
              style={{
                background: `color-mix(in srgb, var(--color-accent-text) ${step.mix}%, var(--color-bg-emphasis))`,
              }}
            >
              {t.iso}
              <span className="hidden text-[0.72em] font-medium tabular-nums sm:block">
                {metric === 'facts' ? v : `${v}/${max}`}
              </span>
            </button>
          )
        })}
      </div>
      <div className="mt-3 flex items-center gap-2.5 text-xs text-[var(--color-fg-muted)]">
        <span>Less evidence</span>
        <span className="h-2 w-32 rounded bg-[linear-gradient(90deg,color-mix(in_srgb,var(--color-accent-text)_12%,var(--color-bg-emphasis))_0_25%,color-mix(in_srgb,var(--color-accent-text)_26%,var(--color-bg-emphasis))_25%_50%,color-mix(in_srgb,var(--color-accent-text)_82%,var(--color-bg-emphasis))_50%_75%,var(--color-accent-text)_75%)]" />
        <span>More</span>
      </div>
      <div
        aria-live="polite"
        className="mt-3.5 flex flex-wrap items-end justify-between gap-3 border-t border-[var(--color-border)] pt-3.5"
      >
        <div>
          <p className="font-display text-xl font-bold">{s.name}</p>
          <p className="text-sm text-[var(--color-fg-secondary)] tabular-nums">
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
          className="text-sm font-semibold whitespace-nowrap text-[var(--color-accent-text)] hover:underline"
        >
          Open country →
        </Link>
      </div>
      <p className="mt-3 text-xs text-[var(--color-fg-muted)]">
        Counts of verified evidence, not a ranking of how sovereign a state is.
      </p>
    </div>
  )
}
