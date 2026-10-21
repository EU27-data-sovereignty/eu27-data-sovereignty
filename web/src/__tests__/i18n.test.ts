import { describe, expect, it } from 'vitest'

import {
  ENGLISH,
  formatCount,
  langFromPath,
  lookup,
  resolveLang,
  servedLanguages,
  spanText,
  stateOf,
  type StateLanguage,
} from '@/i18n'
import { countryPath } from '@/utils/routes'

/**
 * What a member state's address serves (#111, #112), against a stand-in so the cases hold whatever the real
 * tables admit: Belgium with French admitted, Dutch and German not; Malta with nothing admitted.
 */
const STANDIN: Record<string, StateLanguage[]> = {
  BE: [
    { lang: 'nl', tag: 'nl-BE', admitted: false, read: false },
    { lang: 'fr', tag: 'fr-BE', admitted: true, read: false },
    { lang: 'de', tag: 'de-BE', admitted: false, read: false },
  ],
  MT: [{ lang: 'mt', tag: 'mt-MT', admitted: false, read: false }],
}
const FR = { lang: 'fr', tag: 'fr-BE', read: false }

describe('a state address and its language', () => {
  it('serves English where nothing is admitted', () => {
    expect(servedLanguages('mt', STANDIN)).toEqual([ENGLISH])
    expect(resolveLang('mt', undefined, STANDIN)).toEqual({ kind: 'ok', lang: ENGLISH })
    expect(resolveLang('mt', 'mt', STANDIN)).toEqual({ kind: 'redirect' })
  })

  it('serves the first admitted official language by default, and English beside it', () => {
    expect(servedLanguages('be', STANDIN)).toEqual([FR, ENGLISH])
    expect(resolveLang('be', undefined, STANDIN)).toEqual({ kind: 'ok', lang: FR })
    expect(resolveLang('be', 'en', STANDIN)).toEqual({ kind: 'ok', lang: ENGLISH })
  })

  it('sends the default spelled out, and an official language not admitted, back to the state address', () => {
    expect(resolveLang('be', 'fr', STANDIN)).toEqual({ kind: 'redirect' })
    expect(resolveLang('be', 'nl', STANDIN)).toEqual({ kind: 'redirect' })
  })

  it('has no page for a language the state does not have', () => {
    expect(resolveLang('be', 'it', STANDIN)).toEqual({ kind: 'notfound' })
    expect(resolveLang('be', 'xx', STANDIN)).toEqual({ kind: 'notfound' })
  })

  it('reads the state and the language from a path, English off the state pages', () => {
    expect(langFromPath('/sources')).toEqual(ENGLISH)
    expect(stateOf('/de')).toBe('de')
    expect(stateOf('/DE')).toBeNull()
    expect(stateOf('/de/xx')).toBeNull()
    expect(stateOf('/holdings/health')).toBeNull()
  })

  it('builds the address with the language as a second segment', () => {
    expect(countryPath('BE')).toBe('/be')
    expect(countryPath('BE', 'fr')).toBe('/be/fr')
  })
})

describe('lookup', () => {
  it('prints English for English and for any tag without an admitted table', () => {
    expect(lookup('en')('nav.sources')).toBe('Sources')
    expect(lookup('xx-XX')('nav.sources')).toBe('Sources')
  })

  it('takes a keyed span from the table and an unkeyed one as written', () => {
    const t = lookup('en')
    expect(spanText({ t: 'Indicator', key: 'col.indicator' }, t)).toBe('Indicator')
    expect(spanText({ t: 'Operator' }, t)).toBe('Operator')
    expect(spanText({ t: 'Kept', key: 'not.a.key' }, t)).toBe('Kept')
  })

  it('fills a count into the English pattern', () => {
    const t = lookup('en')
    expect(t('fact.withheld', 1)).toBe('1 value withheld until sourced')
    expect(t('fact.withheld', 1204)).toBe('1,204 values withheld until sourced')
  })
})

describe('formatCount', () => {
  // Polish has four forms; which one a number takes is CLDR's rule, applied by Intl.PluralRules.
  const PL =
    '{count, plural, one {# wartość} few {# wartości} many {# wartości!} other {# wartości?}}'

  it("picks the branch the language's plural rules give", () => {
    expect(formatCount(PL, 1, 'pl-PL')).toBe('1 wartość')
    expect(formatCount(PL, 3, 'pl-PL')).toBe('3 wartości')
    expect(formatCount(PL, 5, 'pl-PL')).toBe('5 wartości!')
    expect(formatCount(PL, 1.5, 'pl-PL')).toBe('1,5 wartości?')
  })

  it('prefers an exact =n branch, and prints the count in the language', () => {
    const p = '{count, plural, =0 {nothing} one {# thing} other {# things}}'
    expect(formatCount(p, 0, 'en')).toBe('nothing')
    expect(formatCount(p, 2500, 'de-DE')).toBe('2.500 things')
  })

  it('leaves a string that is not a pattern as it is', () => {
    expect(formatCount('Sources', 3, 'en')).toBe('Sources')
  })
})
