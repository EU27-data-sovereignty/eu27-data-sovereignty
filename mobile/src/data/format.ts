/**
 * Formatting helpers. Copied verbatim from `web/src/utils/format.ts` so a figure reads the
 * same on the phone as on the site; `__tests__/parity.test.ts` fails if the two drift.
 */

const nf = new Intl.NumberFormat('en-GB')

export const num = (v: number) => nf.format(Math.round(v))

export const mw = (v: number) => `${v.toFixed(1)} MW`

/** Money is always EUR millions in this model (capacity_model.py works in EUR mm). */
export function eur(millions: number): string {
  if (millions >= 1000) return `EUR ${(millions / 1000).toFixed(2)} bn`
  return `EUR ${Math.round(millions)} m`
}

export const pct = (v: number, digits = 0) => `${(v * 100).toFixed(digits)}%`

/** Title-cases an ordinal label like 'operational' for display. */
export const titleCase = (s: string) => s.charAt(0).toUpperCase() + s.slice(1)
