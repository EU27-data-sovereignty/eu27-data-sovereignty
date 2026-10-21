import { useMemo, useState } from 'react'

import { SourceList } from '@/components/SourceList'
import type { Bundle } from '@/data/types'
import { PageBand } from '@/components/PageBand'
import { BUTTON_OUTLINE, CARD, FIELD } from '@/components/ui'
import { m, useTx } from '@/i18n'

const PAGE = 20

const TIERS: [number, string][] = [
  [1, m('T1 · authoritative original')],
  [2, m('T2 · competent public body')],
  [3, m('T3 · other institution or company')],
  [4, m('T4 · secondary (press, mirror)')],
]

/** One distribution as a stacked bar with its legend: counts, never a score. */
function Split({ title, parts }: { title: string; parts: [string, number, string][] }) {
  const { tx, num } = useTx()
  const total = parts.reduce((n, p) => n + p[1], 0) || 1
  return (
    <div className={`${CARD} p-5`}>
      <p className="text-xs font-semibold tracking-[0.12em] text-[var(--color-accent-text)] uppercase">
        {title}
      </p>
      <div className="my-3.5 flex h-3.5 gap-0.5 overflow-hidden rounded-full" aria-hidden="true">
        {parts.map(([label, n, fill]) =>
          n ? <span key={label} style={{ flex: n, background: fill }} /> : null,
        )}
      </div>
      <dl className="grid gap-1.5 text-sm">
        {parts.map(([label, n, fill]) => (
          <div key={label} className="grid grid-cols-[minmax(0,1fr)_auto] items-center gap-2.5">
            <dt className="flex items-center gap-2.5 text-[var(--color-fg-secondary)]">
              <span
                className="h-3 w-3 shrink-0 rounded-sm"
                style={{ background: fill }}
                aria-hidden="true"
              />
              {label}
            </dt>
            <dd className="font-semibold tabular-nums">{num(n)}</dd>
          </div>
        ))}
      </dl>
      <p className="mt-2 text-xs text-[var(--color-fg-muted)]">
        {tx('{n, plural, one {# citation} other {# citations}}', { n: total })}
      </p>
    </div>
  )
}

/** The whole register of checked sources, each with every claim in the bundle it supports. */
export function Sources({ bundle }: { bundle: Bundle }) {
  const { tx, num } = useTx()
  const [query, setQuery] = useState('')
  const [iso, setIso] = useState('')
  const [tier, setTier] = useState('')
  const [grade, setGrade] = useState('')
  // Entries beyond the limit are hidden, not unmounted: every source stays in the list and keeps its number.
  const [limit, setLimit] = useState(PAGE)

  const ids = Object.keys(bundle.sources).sort((a, b) =>
    bundle.sources[a]!.title.localeCompare(bundle.sources[b]!.title),
  )
  const numbers = new Map(ids.map((sid, i) => [sid, i + 1]))
  const claims = new Map<string, string[]>()
  for (const [claim, cites] of Object.entries(bundle.claims)) {
    for (const c of cites) claims.set(c.source_id, [...(claims.get(c.source_id) ?? []), claim])
  }

  // What each source can be found by: its countries, tiers, grades and text. Read from the bundle.
  const index = useMemo(() => {
    const out = new Map<
      string,
      { isos: Set<string>; tiers: Set<string>; grades: Set<string>; text: string }
    >()
    for (const [claim, cites] of Object.entries(bundle.claims)) {
      for (const c of cites) {
        const s = bundle.sources[c.source_id]
        if (!s) continue
        const e = out.get(c.source_id) ?? {
          isos: new Set<string>(),
          tiers: new Set<string>(),
          grades: new Set<string>(),
          text: [s.title, s.publisher, s.url].join(' ').toLowerCase(),
        }
        e.isos.add(claim.split(':')[1] ?? '')
        e.tiers.add(String(c.checks.tier ?? ''))
        e.grades.add(c.grade)
        e.text += ' ' + [claim, c.original, c.gloss].join(' ').toLowerCase()
        out.set(c.source_id, e)
      }
    }
    return out
  }, [bundle])

  const all = Object.values(bundle.claims).flat()
  const tierCounts = TIERS.map(([t]) => all.filter(c => c.checks.tier === t).length)
  const grades = (['Verified', 'Strong', 'Standard'] as const).map(
    g => [g, all.filter(c => c.grade === g).length] as const,
  )

  const term = query.trim().toLowerCase()
  const hidden = new Set(
    ids.filter(sid => {
      const e = index.get(sid)
      if (!e) return Boolean(term || iso || tier || grade)
      return (
        (iso && !e.isos.has(iso)) ||
        (tier && !e.tiers.has(tier)) ||
        (grade && !e.grades.has(grade)) ||
        (term && !e.text.includes(term))
      )
    }),
  )
  const matching = ids.filter(sid => !hidden.has(sid))
  for (const sid of matching.slice(limit)) hidden.add(sid)
  const shown = Math.min(limit, matching.length)
  const strong = Object.values(bundle.claims).filter(cs =>
    cs.some(c => c.grade !== 'Standard'),
  ).length
  const names = Object.fromEntries(Object.values(bundle.countries).map(c => [c.iso2, c.name]))

  return (
    <article>
      <PageBand
        kicker={tx('EU-27 · Evidence')}
        title={tx('Sources')}
        facts={[
          [num(ids.length), tx('checked sources')],
          [num(Object.keys(bundle.claims).length), tx('claims they support')],
          [num(strong), tx('claims graded Strong or better')],
        ]}
      >
        <p className="mt-3 max-w-3xl text-[var(--color-fg-secondary)]">
          {tx(
            '{sources, plural, one {# source supports} other {# sources support}} {claims, plural, one {# claim} other {# claims}}. A source is admitted only after its document was fetched, its SHA-256 recorded and the quoted text found in it; failures stay out and are recorded in the repository.',
            { sources: ids.length, claims: Object.keys(bundle.claims).length },
          )}
        </p>
      </PageBand>

      <div className="mb-8 grid gap-4 md:grid-cols-2">
        <Split
          title={tx('Source tier of each citation')}
          parts={TIERS.map(([, label], i) => [
            tx(label),
            tierCounts[i]!,
            [
              'var(--color-rank-1)',
              'var(--color-rank-2)',
              'var(--color-rank-3)',
              'var(--color-baseline)',
            ][i]!,
          ])}
        />
        <Split
          title={tx('Evidence grade of each citation')}
          parts={grades.map(([g, n]) => [
            g,
            n,
            g === 'Verified'
              ? 'var(--color-rank-1)'
              : g === 'Strong'
                ? 'var(--color-rank-2)'
                : 'var(--color-rank-3)',
          ])}
        />
      </div>

      <div role="search" className="mb-3 flex flex-wrap items-center gap-3">
        <label htmlFor="source-search" className="sr-only">
          {tx('Search sources')}
        </label>
        <input
          id="source-search"
          type="search"
          value={query}
          onChange={e => {
            setQuery(e.target.value)
            setLimit(PAGE)
          }}
          placeholder={tx('Search titles, publishers, quotes or holdings')}
          className={`${FIELD} min-w-0 flex-[1_1_18rem]`}
        />
        <label htmlFor="source-country" className="sr-only">
          {tx('Country')}
        </label>
        <select
          id="source-country"
          value={iso}
          onChange={e => {
            setIso(e.target.value)
            setLimit(PAGE)
          }}
          className={FIELD}
        >
          <option value="">{tx('All countries')}</option>
          {Object.entries(names)
            .sort((a, b) => a[1].localeCompare(b[1]))
            .map(([code, name]) => (
              <option key={code} value={code}>
                {name}
              </option>
            ))}
        </select>
        <label htmlFor="source-tier" className="sr-only">
          {tx('Source tier')}
        </label>
        <select
          id="source-tier"
          value={tier}
          onChange={e => {
            setTier(e.target.value)
            setLimit(PAGE)
          }}
          className={FIELD}
        >
          <option value="">{tx('All tiers')}</option>
          {TIERS.map(([t, label]) => (
            <option key={t} value={String(t)}>
              {tx(label)}
            </option>
          ))}
        </select>
        <label htmlFor="source-grade" className="sr-only">
          {tx('Evidence grade')}
        </label>
        <select
          id="source-grade"
          value={grade}
          onChange={e => {
            setGrade(e.target.value)
            setLimit(PAGE)
          }}
          className={FIELD}
        >
          <option value="">{tx('All grades')}</option>
          <option>Strong</option>
          <option>Standard</option>
        </select>
      </div>
      <p aria-live="polite" className="text-sm text-[var(--color-fg-muted)] tabular-nums">
        {matching.length
          ? matching.length < ids.length
            ? tx('Showing {shown} of {total} matching sources', {
                shown: num(shown),
                total: num(matching.length),
              })
            : tx('Showing {shown} of {total} sources', {
                shown: num(shown),
                total: num(matching.length),
              })
          : tx('No source matches these filters.')}
      </p>
      <SourceList bundle={bundle} numbers={numbers} claims={claims} hidden={hidden} />
      {matching.length > limit ? (
        <div className="mt-5 flex justify-center">
          <button type="button" onClick={() => setLimit(l => l + PAGE)} className={BUTTON_OUTLINE}>
            {tx('Show {n} more', { n: Math.min(PAGE, matching.length - limit) })}
          </button>
        </div>
      ) : null}
    </article>
  )
}
