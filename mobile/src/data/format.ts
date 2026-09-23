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

/**
 * The flag emoji for a two-letter country code, e.g. 'NL' -> the Dutch flag.
 *
 * Derived, never stored in the bundle: a glyph is presentation, and adding a key to
 * eu27.json would mark all 54 tracked artefacts stale for a character that must not
 * appear on any of them (DECISIONS.md #47). `model/emoji.py` carries the same
 * derivation for the markdown briefs, and both are asserted against the same table.
 *
 * Use in tables of contents, indexes and navigation only. The flag is decorative and
 * sits beside the country name, never instead of it — mark it `aria-hidden`.
 */
const FLAG_OVERRIDES: Record<string, string> = {
  // Eurostat writes Greece as EL; the regional-indicator sequence needs ISO alpha-2 GR.
  EL: 'GR',
}

const REGIONAL_INDICATOR_A = 0x1f1e6
const FLAG_OFFSET = REGIONAL_INDICATOR_A - 'A'.charCodeAt(0)

export function flagEmoji(iso: string): string {
  const upper = iso.toUpperCase()
  const code = FLAG_OVERRIDES[upper] ?? upper
  if (!/^[A-Z]{2}$/.test(code)) throw new Error(`not a two-letter ISO country code: ${iso}`)
  return [...code].map(ch => String.fromCodePoint(FLAG_OFFSET + ch.charCodeAt(0))).join('')
}
