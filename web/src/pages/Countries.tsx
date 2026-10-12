import { useMemo, useState } from 'react'
import { Link, useLocation } from 'react-router-dom'

import { coverage, factCounts, spans } from '@/data/sources'
import type { Bundle } from '@/data/types'
import type { ReportSection } from '@/data/guides'
import { PageBand } from '@/components/PageBand'
import { CARD, Dots, FIELD, Bar, Segmented } from '@/components/ui'
import { countryPath } from '@/utils/routes'

type SortKey = 'name' | 'verified' | 'tier0' | 'facts'

/**
 * All 27 as cards, sortable and searchable -- the web's advantage over the PDF's fixed table. Each card
 * reports evidence, not judgement: how much of each state's inventory has a verified source (#99 layout).
 */
export function Countries({ bundle }: { bundle: Bundle }) {
  const [query, setQuery] = useState('')
  const [sort, setSort] = useState<SortKey>('name')
  // A guide's step may name the section of the report to open once a state is chosen (#102).
  const section = (useLocation().state as { section?: ReportSection } | null)?.section
  // Its heading, in the report's own words, from any country's document.
  const sectionTitle = section
    ? Object.values(bundle.documents)[0]?.sections.find(s => s.id === section)?.title
    : undefined
  const report = (iso: string) => `${countryPath(iso)}${sectionTitle ? `#${section}` : ''}`

  const rows = useMemo(() => {
    const all = Object.values(bundle.countries).map(c => {
      const cov = coverage(c)
      const doc = bundle.documents[c.iso2]
      const withheld = doc ? [...spans(doc)].filter(x => x.role === 'disputed').length : 0
      return { c, cov, facts: doc ? factCounts(doc).facts : 0, withheld }
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

  return (
    <article>
      <PageBand kicker="EU-27 · Member states" title="Countries">
        <p className="mt-3 max-w-3xl text-[var(--color-fg-secondary)]">
          Each member state analysed on its own fundamentals. The cards count verified evidence;
          they are not a ranking of how sovereign a state is.
        </p>
      </PageBand>
      {sectionTitle ? (
        <p
          role="status"
          className="mb-5 rounded border-l-4 border-[var(--color-accent-text)] bg-[var(--color-bg-emphasis)] px-4 py-3 text-sm font-medium"
        >
          Choose a member state to open its report at “{sectionTitle}”.
        </p>
      ) : null}
      <div className="mb-5 flex flex-wrap items-center gap-3">
        <label htmlFor="country-search" className="sr-only">
          Find a country
        </label>
        <input
          id="country-search"
          type="search"
          placeholder="Find a country"
          value={query}
          onChange={e => setQuery(e.target.value)}
          className={`${FIELD} min-w-0 flex-[1_1_14rem]`}
        />
        <Segmented<SortKey>
          label="Sort by"
          value={sort}
          onChange={setSort}
          options={[
            ['name', 'A–Z'],
            ['verified', 'Holdings verified'],
            ['tier0', 'Tier 0 verified'],
            ['facts', 'Sourced facts'],
          ]}
        />
      </div>
      {rows.length === 0 ? (
        <p className="py-6 text-[var(--color-fg-muted)]">No member state matches that name.</p>
      ) : null}
      <ul className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3" aria-label="Member states">
        {rows.map(({ c, cov, facts, withheld }) => (
          <li
            key={c.iso2}
            className={`${CARD} flex flex-col gap-3 p-5 transition-colors hover:border-[var(--color-accent-text)]`}
          >
            <div className="flex items-baseline justify-between gap-3">
              <h2 className="font-display text-xl font-bold">
                <Link to={report(c.iso2)} className="hover:underline">
                  {c.name}
                </Link>
              </h2>
              <span className="text-xs font-bold tracking-wider text-[var(--color-fg-muted)]">
                {c.iso2}
              </span>
            </div>
            <div className="grid grid-cols-[7.5em_minmax(0,1fr)] items-center gap-2.5 text-sm text-[var(--color-fg-secondary)]">
              <span>Holdings</span>
              <Bar value={cov.verified} max={cov.total} />
              <span>Tier 0</span>
              <Dots
                value={cov.tier0}
                max={cov.tier0Total}
                title={`${cov.tier0} of ${cov.tier0Total} tier 0 holdings verified`}
              />
              <span>Sourced facts</span>
              <span className="font-semibold text-[var(--color-fg-primary)] tabular-nums">
                {facts}
              </span>
            </div>
            <div className="mt-auto flex items-center justify-between border-t border-[var(--color-border)] pt-3 text-sm">
              <span className="text-[var(--color-fg-muted)]">
                {withheld ? `${withheld} withheld as disputed` : 'Nothing withheld as disputed'}
              </span>
              <a
                className="font-semibold text-[var(--color-accent-text)] hover:underline"
                href={`/report/${c.iso2}.pdf`}
              >
                PDF
              </a>
            </div>
          </li>
        ))}
      </ul>
    </article>
  )
}
