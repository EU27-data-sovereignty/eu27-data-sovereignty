import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'

import { coverage, factCounts } from '@/data/sources'
import type { Bundle } from '@/data/types'
import { PageBand } from '@/components/PageBand'

type SortKey = 'name' | 'verified' | 'tier0' | 'facts'

/**
 * All 27, sortable and searchable -- the web's advantage over the PDF's fixed table. Columns
 * report evidence, not judgement: how much of each state's inventory has a verified source.
 */
export function Countries({ bundle }: { bundle: Bundle }) {
  const [query, setQuery] = useState('')
  const [sort, setSort] = useState<SortKey>('name')

  const rows = useMemo(() => {
    const all = Object.values(bundle.countries).map(c => {
      const cov = coverage(c)
      const doc = bundle.documents[c.iso2]
      return { c, cov, facts: doc ? factCounts(doc).facts : 0 }
    })
    const q = query.trim().toLowerCase()
    const filtered = q
      ? all.filter(r => r.c.name.toLowerCase().includes(q) || r.c.iso2.toLowerCase() === q)
      : all
    const by: Record<SortKey, (a: (typeof all)[0], b: (typeof all)[0]) => number> = {
      name: (a, b) => a.c.name.localeCompare(b.c.name),
      verified: (a, b) => b.cov.verified - a.cov.verified || a.c.name.localeCompare(b.c.name),
      tier0: (a, b) => b.cov.tier0 - a.cov.tier0 || a.c.name.localeCompare(b.c.name),
      facts: (a, b) => b.facts - a.facts || a.c.name.localeCompare(b.c.name),
    }
    return [...filtered].sort(by[sort])
  }, [bundle, query, sort])

  const header = (key: SortKey, label: string, right = false) => (
    <th
      scope="col"
      aria-sort={sort === key ? (key === 'name' ? 'ascending' : 'descending') : 'none'}
      className={`px-2 py-1.5 ${right ? 'text-right' : 'text-left'}`}
    >
      <button type="button" onClick={() => setSort(key)} className="font-semibold hover:underline">
        {label}
        {sort === key ? ' ▾' : ''}
      </button>
    </th>
  )

  return (
    <article>
      <PageBand kicker="EU-27 · Member states" title="Countries" />
      <p className="mb-4 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        Each member state analysed on its own fundamentals. The columns count verified evidence;
        they are not a ranking of how sovereign a state is.
      </p>
      <label className="mb-4 block text-sm">
        <span className="mr-2">Find a country</span>
        <input
          type="search"
          value={query}
          onChange={e => setQuery(e.target.value)}
          className="rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] px-2 py-1"
        />
      </label>
      <div className="scroll-x">
        <table className="w-full min-w-[36rem] border-collapse text-sm">
          <thead>
            <tr className="border-b-2 border-[var(--color-accent)] bg-[var(--color-bg-emphasis)]">
              {header('name', 'Country')}
              <th scope="col" className="px-2 py-1.5 text-left font-semibold">
                ISO
              </th>
              {header('verified', 'Holdings verified', true)}
              {header('tier0', 'Tier 0 verified', true)}
              {header('facts', 'Sourced facts', true)}
              <th scope="col" className="px-2 py-1.5 text-left font-semibold">
                Report
              </th>
            </tr>
          </thead>
          <tbody>
            {rows.map(({ c, cov, facts }) => (
              <tr key={c.iso2} className="border-b border-[var(--color-border)]">
                <th scope="row" className="px-2 py-1.5 text-left font-normal">
                  <Link
                    to={`/country/${c.iso2}`}
                    className="text-[var(--color-accent-text)] underline"
                  >
                    {c.name}
                  </Link>
                </th>
                <td className="px-2 py-1.5">{c.iso2}</td>
                <td className="px-2 py-1.5 text-right tabular-nums">
                  {cov.verified} of {cov.total}
                </td>
                <td className="px-2 py-1.5 text-right tabular-nums">
                  {cov.tier0} of {cov.tier0Total}
                </td>
                <td className="px-2 py-1.5 text-right tabular-nums">{facts}</td>
                <td className="px-2 py-1.5">
                  <a className="underline" href={`/report/${c.iso2}.pdf`}>
                    PDF
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </article>
  )
}
