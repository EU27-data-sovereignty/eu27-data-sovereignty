import { useLocation } from 'react-router-dom'

import en from '../../../model/i18n/strings/en.json'
import languagesJson from '../../../model/i18n/languages.json'
import type { Span } from '@/data/types'

/**
 * The language a page is served in, and the strings it prints around the facts (#111).
 *
 * The tables are model/i18n/, written by model/i18n_admit.py: English from the strings table, and another
 * language only once a person who reads it has signed its draft off. A table is admitted whole or not at all,
 * so a lookup never falls back key by key and a page never mixes a translated label with an English one.
 * Only a member state's page has a language other than English (`/be/fr`); every other page is English.
 */

export type Key = keyof typeof en

export interface Lang {
  /** The URL segment, an ISO 639-1 subtag: `fr` in `/be/fr`. */
  lang: string
  /** The BCP 47 tag for `<html lang>`: `fr-BE`, or `en`. */
  tag: string
}

export interface StateLanguage extends Lang {
  admitted: boolean
}

export const ENGLISH: Lang = { lang: 'en', tag: 'en' }

const LANGUAGES = languagesJson as Record<string, StateLanguage[]>

const TABLES: Record<string, Record<Key, string>> = Object.fromEntries(
  Object.entries(
    import.meta.glob<Record<Key, string>>('../../../model/i18n/strings/*.json', {
      eager: true,
      import: 'default',
    }),
  ).map(([path, table]) => [path.slice(path.lastIndexOf('/') + 1, -'.json'.length), table]),
)

/** The languages a state's page can be read in: its admitted official languages, then English. */
export function servedLanguages(
  iso: string,
  languages: Record<string, StateLanguage[]> = LANGUAGES,
): Lang[] {
  const own = (languages[iso.toUpperCase()] ?? []).filter(l => l.admitted && l.lang !== 'en')
  return [...own.map(({ lang, tag }) => ({ lang, tag })), ENGLISH]
}

export type Resolved = { kind: 'ok'; lang: Lang } | { kind: 'redirect' } | { kind: 'notfound' }

/**
 * What `/<iso>/<segment>` serves. No segment: the state's first admitted official language, else English.
 * The default spelled out, or an official language not yet admitted, redirects to `/<iso>`, so each page has
 * one address; any other segment is not a page.
 */
export function resolveLang(
  iso: string,
  segment: string | undefined,
  languages: Record<string, StateLanguage[]> = LANGUAGES,
): Resolved {
  const served = servedLanguages(iso, languages)
  if (segment === undefined) return { kind: 'ok', lang: served[0]! }
  if (segment === served[0]!.lang) return { kind: 'redirect' }
  const hit = served.find(l => l.lang === segment)
  if (hit) return { kind: 'ok', lang: hit }
  const official = (languages[iso.toUpperCase()] ?? []).some(l => l.lang === segment)
  return official ? { kind: 'redirect' } : { kind: 'notfound' }
}

/** The member state whose page `pathname` is (`/be`, `/be/fr`), or null for any other page. */
export function stateOf(pathname: string): string | null {
  const [first, second, ...rest] = pathname.split('/').filter(Boolean)
  if (!first || rest.length || first !== first.toLowerCase() || !(first.toUpperCase() in LANGUAGES))
    return null
  return resolveLang(first, second).kind === 'ok' ? first : null
}

/** The language of the page at `pathname`: a state's page by its segment, anything else English. */
export function langFromPath(pathname: string): Lang {
  const iso = stateOf(pathname)
  if (!iso) return ENGLISH
  const r = resolveLang(iso, pathname.split('/').filter(Boolean)[1])
  return r.kind === 'ok' ? r.lang : ENGLISH
}

/** A lookup in the table for `tag`, which exists only if admitted; English otherwise. */
export function lookup(tag: string): (key: Key) => string {
  const table = TABLES[tag] ?? TABLES.en ?? en
  return key => table[key]
}

export function useLang(): Lang {
  return langFromPath(useLocation().pathname)
}

export function useT(): (key: Key) => string {
  return lookup(useLang().tag)
}

/** A model span's text in the page's language: by its key where the model gave one, else as written. */
export function spanText(span: Pick<Span, 't' | 'key'>, t: (key: Key) => string): string {
  return span.key && span.key in en ? t(span.key as Key) : span.t
}
