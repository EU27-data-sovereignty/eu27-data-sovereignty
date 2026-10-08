import type { ReactNode } from 'react'

/**
 * Small display pieces the EU27.CLOUD layouts share (#99). They draw numbers the page already has;
 * none of them computes or states a fact of its own.
 */

/** A horizontal bar with its value beside it: `value of max`. */
export function Bar({
  value,
  max,
  label,
  faded = false,
}: {
  value: number
  max: number
  label?: string
  faded?: boolean
}) {
  const pct = max > 0 ? Math.min(100, (value / max) * 100) : 0
  return (
    <span className="flex min-w-36 items-center gap-2.5">
      <span className="h-1.5 flex-1 overflow-hidden rounded-full bg-[var(--color-bg-emphasis)]">
        <span
          className={`block h-full rounded-full ${faded ? 'bg-[var(--color-eu-gold)]/45' : 'bg-[var(--color-eu-gold)]'}`}
          style={{ width: `${pct}%` }}
        />
      </span>
      <span className="min-w-16 text-right text-sm text-[var(--color-fg-secondary)] tabular-nums">
        {label ?? `${value} of ${max}`}
      </span>
    </span>
  )
}

/** `value` of `max` as a row of dots, for small counts such as the nine tier 0 holdings. */
export function Dots({ value, max, title }: { value: number; max: number; title: string }) {
  return (
    <span className="flex gap-1" role="img" aria-label={title} title={title}>
      {Array.from({ length: max }, (_, i) => (
        <span
          key={i}
          className={`h-2.5 w-2.5 rounded-full border ${
            i < value
              ? 'border-[var(--color-eu-gold)] bg-[var(--color-eu-gold)]'
              : 'border-[var(--color-border)] bg-[var(--color-bg-emphasis)]'
          }`}
        />
      ))}
    </span>
  )
}

/** A row of mutually exclusive buttons: the selected one is filled EU blue. */
export function Segmented<T extends string>({
  label,
  options,
  value,
  onChange,
}: {
  label: string
  options: [T, string][]
  value: T
  onChange: (v: T) => void
}) {
  return (
    <div
      role="group"
      aria-label={label}
      className="flex flex-wrap rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-0.5"
    >
      {options.map(([v, text]) => (
        <button
          key={v}
          type="button"
          aria-pressed={value === v}
          onClick={() => onChange(v)}
          className={`rounded px-3 py-1.5 text-sm font-medium ${
            value === v
              ? 'bg-[var(--color-eu-blue)] text-white'
              : 'text-[var(--color-fg-secondary)] hover:text-[var(--color-fg-primary)]'
          }`}
        >
          {text}
        </button>
      ))}
    </div>
  )
}

/** A section heading with its gold eyebrow, and an optional line of context on the right. */
export function SectionHead({
  eyebrow,
  title,
  aside,
}: {
  eyebrow: string
  title: ReactNode
  aside?: ReactNode
}) {
  return (
    <div className="mb-5 flex flex-wrap items-end justify-between gap-x-6 gap-y-2">
      <div>
        <p className="mb-1.5 text-xs font-semibold tracking-[0.14em] text-[var(--color-accent-text)] uppercase">
          {eyebrow}
        </p>
        <h2 className="font-display text-2xl font-bold tracking-tight sm:text-3xl">{title}</h2>
      </div>
      {aside ? (
        <div className="max-w-md text-sm text-[var(--color-fg-secondary)]">{aside}</div>
      ) : null}
    </div>
  )
}

/** The card surface every panel on the site uses. */
export const CARD = 'rounded border border-[var(--color-border)] bg-[var(--color-bg-card)]'

/** Inputs and selects. 16 px: iPhone Safari zooms into any field set smaller (#92). */
export const FIELD =
  'rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] px-3 py-2 text-base text-[var(--color-fg-primary)] placeholder:text-[var(--color-fg-muted)]'
