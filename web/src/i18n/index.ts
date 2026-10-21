import { useSyncExternalStore } from 'react'
import { useLocation } from 'react-router-dom'

import en from '../../../model/i18n/strings/en.json'
import languagesJson from '../../../model/i18n/languages.json'
import siteJson from '../../../model/i18n/site.json'
import type { Span } from '@/data/types'

/**
 * The language a page is served in, and the strings it prints (#111, #112, #113).
 *
 * The tables are model/i18n/, written by model/i18n_admit.py: English from the strings table, and another
 * language once its draft is fully cross-reviewed on two models with no fix open (#112). `read` says whether a
 * person who reads the language has checked it; a page in an unread language says so.
 *
 * Which language a page is in (#113): a state page's explicit segment (`/be/fr`) first; then the reader's
 * remembered choice, where the page has it; then the page's default, the state's first admitted language on a
 * state page and English everywhere else. The choice is kept by the browser and never in the address, so a
 * shared link opens in the reader's own language.
 */

export type Key = keyof typeof en

export interface Lang {
  /** The ISO 639-1 subtag: `fr`, and the URL segment in `/be/fr`. */
  lang: string
  /** The BCP 47 tag of the table it reads, and `<html lang>`: `fr-BE`, or `en`. */
  tag: string
  /** Whether a person who reads the language has checked its strings. English is the source. */
  read: boolean
}

export interface StateLanguage extends Lang {
  admitted: boolean
}

export const ENGLISH: Lang = { lang: 'en', tag: 'en', read: true }

const LANGUAGES = languagesJson as Record<string, StateLanguage[]>
const SITE = siteJson as StateLanguage[]

const TABLES: Record<string, Record<Key, string>> = Object.fromEntries(
  Object.entries(
    import.meta.glob<Record<Key, string>>('../../../model/i18n/strings/*.json', {
      eager: true,
      import: 'default',
    }),
  ).map(([path, table]) => [path.slice(path.lastIndexOf('/') + 1, -'.json'.length), table]),
)

const strip = ({ lang, tag, read }: Lang): Lang => ({ lang, tag, read })

/** The languages the whole site can be read in (#113): the admitted site languages, then English. */
export function siteLanguages(site: StateLanguage[] = SITE): Lang[] {
  return [...site.filter(l => l.admitted).map(strip), ENGLISH]
}

/** The languages a state's page has an address for: its admitted official languages, and English. */
export function servedLanguages(
  iso: string,
  languages: Record<string, StateLanguage[]> = LANGUAGES,
): Lang[] {
  // Where English is official (IE, MT) admission lists it first, as en-IE; elsewhere English comes last.
  const served = (languages[iso.toUpperCase()] ?? []).filter(l => l.admitted).map(strip)
  return served.some(l => l.lang === 'en') ? served : [...served, ENGLISH]
}

/** What a reader can switch a page to: a state's own languages first, then the site languages it lacks. */
export function choices(
  iso: string | null,
  languages: Record<string, StateLanguage[]> = LANGUAGES,
  site: StateLanguage[] = SITE,
): Lang[] {
  const own = iso ? servedLanguages(iso, languages) : []
  const rest = siteLanguages(site).filter(l => !own.some(o => o.lang === l.lang))
  return [...own, ...rest]
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

/** The language of the page at `pathname` for a reader who chose `chosen` (a subtag, or null). */
export function pageLang(
  pathname: string,
  chosen: string | null,
  languages: Record<string, StateLanguage[]> = LANGUAGES,
  site: StateLanguage[] = SITE,
): Lang {
  const iso = stateOf(pathname)
  const offered = choices(iso, languages, site)
  if (iso) {
    const segment = pathname.split('/').filter(Boolean)[1]
    const r = resolveLang(iso, segment, languages)
    if (segment !== undefined) return r.kind === 'ok' ? r.lang : ENGLISH
    return offered.find(l => l.lang === chosen) ?? (r.kind === 'ok' ? r.lang : ENGLISH)
  }
  return offered.find(l => l.lang === chosen) ?? ENGLISH
}

// The reader's choice. Stored like the theme; every reader of it re-renders when it changes.
const KEY = 'eu27-lang'
const listeners = new Set<() => void>()

export function chosenLang(): string | null {
  try {
    return localStorage.getItem(KEY)
  } catch {
    // Private browsing and blocked site-data both throw: no choice, so each page's default.
    return null
  }
}

export function chooseLang(lang: string) {
  try {
    localStorage.setItem(KEY, lang)
  } catch {
    // Non-fatal: the choice holds until the next page load.
  }
  memory = lang
  listeners.forEach(l => l())
}

let memory: string | null = null
const read = () => chosenLang() ?? memory
const subscribe = (l: () => void) => {
  listeners.add(l)
  const other = (e: StorageEvent) => e.key === KEY && l()
  window.addEventListener('storage', other)
  return () => {
    listeners.delete(l)
    window.removeEventListener('storage', other)
  }
}

/**
 * An ICU message with its arguments filled in: `{name}` by value, and `{name, plural, …}` by the branch
 * `Intl.PluralRules` picks for `tag` (an exact `=n` branch first), with `#` as the number in that language's
 * digits. The subset the strings table uses; the drafts checker holds every pattern to it.
 */
export function format(
  pattern: string,
  args: Record<string, string | number>,
  tag: string,
): string {
  let out = ''
  let i = 0
  while (i < pattern.length) {
    const open = pattern.indexOf('{', i)
    if (open < 0) {
      out += pattern.slice(i)
      break
    }
    out += pattern.slice(i, open)
    let depth = 0
    let close = open
    for (; close < pattern.length; close++) {
      if (pattern[close] === '{') depth++
      else if (pattern[close] === '}' && --depth === 0) break
    }
    const inner = pattern.slice(open + 1, close)
    const comma = inner.indexOf(',')
    const name = (comma < 0 ? inner : inner.slice(0, comma)).trim()
    const value = args[name]
    if (comma < 0) out += value === undefined ? `{${inner}}` : String(value)
    else out += plural(inner.slice(inner.indexOf(',', comma + 1) + 1), Number(value), args, tag)
    i = close + 1
  }
  return out
}

function plural(
  body: string,
  n: number,
  args: Record<string, string | number>,
  tag: string,
): string {
  const branches = new Map<string, string>()
  let depth = 0
  let name = ''
  let text = ''
  for (const ch of body) {
    if (ch === '{' && depth++ === 0) continue
    if (ch === '}' && --depth === 0) {
      branches.set(name.trim(), text)
      name = text = ''
      continue
    }
    if (depth === 0) name += ch
    else text += ch
  }
  const chosen =
    branches.get(`=${n}`) ??
    branches.get(new Intl.PluralRules(tag).select(n)) ??
    branches.get('other') ??
    ''
  return format(chosen.replaceAll('#', new Intl.NumberFormat(tag).format(n)), args, tag)
}

/** The count form #112 shipped: `{count, plural, …}` alone. */
export function formatCount(pattern: string, count: number, tag: string): string {
  return format(pattern, { count }, tag)
}

export type Args = number | Record<string, string | number>
export type T = (key: Key, args?: Args) => string

/** A lookup in the table for `tag`, which exists only if admitted; English otherwise. */
export function lookup(tag: string): T {
  const table = TABLES[tag] ?? TABLES.en ?? en
  const used = TABLES[tag] ? tag : 'en'
  return (key, args) => {
    const text = table[key]
    if (args === undefined) return text
    return format(text, typeof args === 'number' ? { count: args } : args, used)
  }
}

/** The language of a path for the reader's stored choice, outside React (the loading message). */
export function langFromPath(pathname: string): Lang {
  return pageLang(pathname, chosenLang())
}

export function useChosenLang(): string | null {
  return useSyncExternalStore(subscribe, read, () => null)
}

export function useLang(): Lang {
  return pageLang(useLocation().pathname, useChosenLang())
}

export function useT(): T {
  return lookup(useLang().tag)
}

/** A model span's text in the page's language: by its key where the model gave one, else as written. */
export function spanText(span: Pick<Span, 't' | 'key'>, t: T): string {
  return span.key && span.key in en ? t(span.key as Key) : span.t
}
