import { describe, expect, it } from 'vitest'

import {
  ENGLISH,
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
 * What a member state's address serves (#111). The real tables admit no language yet, so the admitted cases
 * run against a stand-in: Belgium with French read and signed off, Dutch and German still drafts.
 */
const BELGIUM_FR: Record<string, StateLanguage[]> = {
  BE: [
    { lang: 'nl', tag: 'nl-BE', admitted: false },
    { lang: 'fr', tag: 'fr-BE', admitted: true },
    { lang: 'de', tag: 'de-BE', admitted: false },
  ],
}

describe('a state address and its language', () => {
  it('serves English while no translation is admitted', () => {
    expect(servedLanguages('de')).toEqual([ENGLISH])
    expect(resolveLang('de', undefined)).toEqual({ kind: 'ok', lang: ENGLISH })
  })

  it('sends the default spelled out, and an unadmitted official language, back to the state address', () => {
    expect(resolveLang('de', 'en')).toEqual({ kind: 'redirect' })
    expect(resolveLang('de', 'de')).toEqual({ kind: 'redirect' })
    expect(resolveLang('be', 'nl', BELGIUM_FR)).toEqual({ kind: 'redirect' })
  })

  it('has no page for a language the state does not have', () => {
    expect(resolveLang('de', 'fr')).toEqual({ kind: 'notfound' })
    expect(resolveLang('de', 'xx')).toEqual({ kind: 'notfound' })
  })

  it('serves the first admitted official language by default, and English beside it', () => {
    const fr = { lang: 'fr', tag: 'fr-BE' }
    expect(servedLanguages('be', BELGIUM_FR)).toEqual([fr, ENGLISH])
    expect(resolveLang('be', undefined, BELGIUM_FR)).toEqual({ kind: 'ok', lang: fr })
    expect(resolveLang('be', 'fr', BELGIUM_FR)).toEqual({ kind: 'redirect' })
    expect(resolveLang('be', 'en', BELGIUM_FR)).toEqual({ kind: 'ok', lang: ENGLISH })
  })

  it('reads a page language from its path, English off the state pages', () => {
    expect(langFromPath('/de')).toEqual(ENGLISH)
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
    expect(lookup('de-DE')('nav.sources')).toBe('Sources')
  })

  it('takes a keyed span from the table and an unkeyed one as written', () => {
    const t = lookup('en')
    expect(spanText({ t: 'Indicator', key: 'col.indicator' }, t)).toBe('Indicator')
    expect(spanText({ t: 'Operator' }, t)).toBe('Operator')
    expect(spanText({ t: 'Kept', key: 'not.a.key' }, t)).toBe('Kept')
  })
})
