/**
 * The flag table, asserted against literal glyphs rather than the same arithmetic twice.
 *
 * `flagEmoji()` computes its glyphs from codepoints, so a test that recomputed them the same
 * way would pass on any self-consistent bug — an off-by-one in the offset would yield a full
 * set of wrong flags and agree with itself. The expected values are therefore written out as
 * real characters and read by eye.
 *
 * `model/emoji.py` carries the same derivation for the markdown briefs and is checked against
 * the same 27 pairs in `tests/test_emoji.py`. Two implementations, one table, asserted twice.
 *
 * Mobile inherits this file byte-for-byte (`mobile/__tests__/parity.test.ts`), so this covers
 * the reader too.
 */
import { describe, expect, it } from 'vitest'

import { flagEmoji } from '../utils/format'

const EXPECTED: Record<string, string> = {
  AT: '🇦🇹',
  BE: '🇧🇪',
  BG: '🇧🇬',
  HR: '🇭🇷',
  CY: '🇨🇾',
  CZ: '🇨🇿',
  DK: '🇩🇰',
  EE: '🇪🇪',
  FI: '🇫🇮',
  FR: '🇫🇷',
  DE: '🇩🇪',
  EL: '🇬🇷', // Eurostat's EL for Greece, the Greek flag
  HU: '🇭🇺',
  IE: '🇮🇪',
  IT: '🇮🇹',
  LV: '🇱🇻',
  LT: '🇱🇹',
  LU: '🇱🇺',
  MT: '🇲🇹',
  NL: '🇳🇱',
  PL: '🇵🇱',
  PT: '🇵🇹',
  RO: '🇷🇴',
  SK: '🇸🇰',
  SI: '🇸🇮',
  ES: '🇪🇸',
  SE: '🇸🇪',
}

describe('flagEmoji', () => {
  it('covers all 27 member states', () => {
    expect(Object.keys(EXPECTED)).toHaveLength(27)
  })

  it.each(Object.entries(EXPECTED))('maps %s to its own flag', (iso, expected) => {
    expect(flagEmoji(iso)).toBe(expected)
  })

  it('treats EL as Greece, the only code Eurostat and ISO disagree on', () => {
    expect(flagEmoji('EL')).toBe(flagEmoji('GR'))
  })

  it('accepts lowercase', () => {
    expect(flagEmoji('nl')).toBe(flagEmoji('NL'))
  })

  it.each(['', 'N', 'NLD', 'N1', 'ÑL'])('throws on %s rather than rendering boxes', bad => {
    expect(() => flagEmoji(bad)).toThrow()
  })

  it('emits exactly two regional indicators', () => {
    for (const iso of Object.keys(EXPECTED)) {
      const chars = [...flagEmoji(iso)]
      expect(chars).toHaveLength(2)
      for (const ch of chars) {
        expect(ch.codePointAt(0)).toBeGreaterThanOrEqual(0x1f1e6)
        expect(ch.codePointAt(0)).toBeLessThanOrEqual(0x1f1ff)
      }
    }
  })
})
