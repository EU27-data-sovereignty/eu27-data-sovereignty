import type { Span } from '@/data/types'

/** Plain helpers for reading a generated document's spans (#74): text and counts, nothing inferred. */

export const text = (spans: Span[]) => spans.map(s => s.t).join(' ')

/** A cell's integer, or NaN when it is not a plain count. */
export const num = (s: Span | undefined) => (s && /^\d+$/.test(s.t.trim()) ? Number(s.t) : NaN)

/** "supported: 66; not supported: 2" as parts; anything that does not parse is left out. */
export function verdicts(cell: string): [string, number][] {
  return cell
    .split(';')
    .map(p => /^\s*(.+?):\s*(\d+)\s*$/.exec(p))
    .filter((m): m is RegExpExecArray => Boolean(m))
    .map(m => [m[1]!, Number(m[2])])
}
