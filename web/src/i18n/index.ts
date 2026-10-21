import { useLocation } from 'react-router-dom'

import en from '../../../model/i18n/strings/en.json'
import languagesJson from '../../../model/i18n/languages.json'
import type { Span } from '@/data/types'

/**
 * The language a page is served in, and the strings it prints around the facts (#111).
 *
 * The tables are model/i18n/, written by model/i18n_admit.py: English from the strings table, and another
 * language once its draft is fully cross-reviewed on two models with no fix open (#112). A table is admitted
 * whole or not at all, so a lookup never falls back key by key and a page never mixes a translated label with
 * an English one. `read` says whether a person who reads the language has checked it; a page in an unread
 * language says so. Only a member state's page has a language other than English (`/be/fr`).
 */

export type Key = keyof typeof en

export interface Lang {
  /** The URL segment, an ISO 639-1 subtag: `fr` in `/be/fr`. */
  lang: string
  /** The BCP 47 tag for `<html lang>`: `fr-BE`, or `en`. */
  tag: string
  /** Whether a person who reads the language has checked its strings. English is the source. */
  read: boolean
}

export interface StateLanguage extends Lang {
  admitted: boolean
}

export const ENGLISH: Lang = { lang: 'en', tag: 'en', read: true }

const LANGUAGES = languagesJson as Record<string, StateLanguage[]>

const TABLES: Record<string, Record<Key, string>> = Object.fromEntries(
  Object.entries(
    import.meta.glob<Record<Key, string>>('../../../model/i18n/strings/*.json', {
      eager: true,
      import: 'default',
    }),
  ).map(([path, table]) => [path.slice(path.lastIndexOf('/') + 1, -'.json'.length), table]),
)

/** The languages a state's page can be read in: its admitted official languages, and English. */
export function servedLanguages(
  iso: string,
  languages: Record<string, StateLanguage[]> = LANGUAGES,
): Lang[] {
  // Where English is official (IE, MT) admission lists it first, as en-IE; elsewhere English comes last.
  const own = (languages[iso.toUpperCase()] ?? []).filter(l => l.admitted)
  const served = own.map(({ lang, tag, read }) => ({ lang, tag, read }))
  return served.some(l => l.lang === 'en') ? served : [...served, ENGLISH]
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

const PLURAL_HEAD = '{count, plural,'

/**
 * An ICU plural pattern with `count` filled in: the exact `=n` branch if there is one, else the branch
 * `Intl.PluralRules` picks for `tag`, with `#` as the count in that language's digits and separators. Only the
 * `{count, plural, …}` form the strings table uses; the drafts checker holds every pattern to it.
 */
export function formatCount(pattern: string, count: number, tag: string): string {
  if (!pattern.startsWith(PLURAL_HEAD)) return pattern
  const branches = new Map<string, string>()
  const body = pattern.slice(PLURAL_HEAD.length, -1)
  let depth = 0
  let name = ''
  let text = ''
  for (const ch of body) {
    if (ch === '{') {
      if (depth++ === 0) continue
    } else if (ch === '}') {
      if (--depth === 0) {
        branches.set(name.trim(), text)
        name = text = ''
        continue
      }
    }
    if (depth === 0) name += ch
    else text += ch
  }
  const chosen =
    branches.get(`=${count}`) ??
    branches.get(new Intl.PluralRules(tag).select(count)) ??
    branches.get('other') ??
    ''
  return chosen.replaceAll('#', new Intl.NumberFormat(tag).format(count))
}

export type T = (key: Key, count?: number) => string

/** A lookup in the table for `tag`, which exists only if admitted; English otherwise. */
export function lookup(tag: string): T {
  const table = TABLES[tag] ?? TABLES.en ?? en
  const used = TABLES[tag] ? tag : 'en'
  return (key, count) => (count === undefined ? table[key] : formatCount(table[key], count, used))
}

export function useLang(): Lang {
  return langFromPath(useLocation().pathname)
}

export function useT(): T {
  return lookup(useLang().tag)
}

/** A model span's text in the page's language: by its key where the model gave one, else as written. */
export function spanText(span: Pick<Span, 't' | 'key'>, t: T): string {
  return span.key && span.key in en ? t(span.key as Key) : span.t
}
