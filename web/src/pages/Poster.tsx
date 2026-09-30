import { useEffect, useRef } from 'react'
import { useParams } from 'react-router-dom'

import { SpanView } from '@/components/DocumentView'
import { coverage, numberSources } from '@/data/sources'
import type { Block, Bundle, Document } from '@/data/types'
import { NotFound } from './NotFound'

/**
 * A one-page summary of a country's document, exported to countries/<ISO>/<ISO>-infographic.png
 * by model/export_artifacts.py. It shows a subset of the same spans the country page and PDF
 * show -- the fundamentals and the tier 0 holdings -- with its own numbered source list, so a
 * fact on the poster is as traceable as one in the report (#75).
 */
function table(doc: Document, id: string): Extract<Block, { type: 'table' }> | undefined {
  const b = doc.sections.find(s => s.id === id)?.blocks.find(x => x.type === 'table')
  return b && b.type === 'table' ? b : undefined
}

export function Poster({ bundle }: { bundle: Bundle }) {
  const { iso = '' } = useParams()
  const ref = useRef<HTMLElement>(null)
  // The exporter reads this to size the screenshot to the content (export_artifacts.measure_height).
  // Hooks run before the not-found guard below: they must not sit after an early return.
  useEffect(() => {
    if (ref.current) {
      ref.current.setAttribute('data-poster-height', String(Math.ceil(ref.current.scrollHeight)))
    }
  })
  const code = iso.toUpperCase()
  const doc = bundle.documents[code]
  const country = bundle.countries[code]
  if (!doc || !country) return <NotFound />

  const fundamentals = table(doc, 'fundamentals')
  const holdings = table(doc, 'holdings')
  const tier0 = (holdings?.rows ?? []).filter(r => r[1]?.t.endsWith('(tier 0)'))
  const shown: Document = {
    ...doc,
    sections: [
      {
        id: 'poster',
        title: '',
        blocks: [
          ...(fundamentals ? [fundamentals] : []),
          ...(holdings ? [{ ...holdings, rows: tier0 }] : []),
        ],
      },
    ],
  }
  const numbers = numberSources([shown], bundle)
  const cov = coverage(country)
  const H = 'mb-2 text-[11px] font-semibold tracking-wide text-[var(--color-accent-text)] uppercase'

  return (
    <article
      ref={ref}
      style={{ width: 1024 }}
      className="mx-auto bg-[var(--color-bg-page)] p-8 text-[var(--color-fg-primary)]"
    >
      <header className="mb-5 border-b-4 border-[var(--color-highlight)] pb-3">
        <div className="text-[10px] font-semibold tracking-[0.18em] text-[var(--color-accent-text)] uppercase">
          EU-27 · Critical data holdings · {code}
        </div>
        <h1 className="text-[34px] leading-tight font-semibold">{doc.name}</h1>
        <p className="mt-1 text-[12px] text-[var(--color-fg-secondary)]">
          {cov.verified} of {cov.total} critical holding classes verified · {cov.tier0} of{' '}
          {cov.tier0Total} tier 0 · capacity not yet sized
        </p>
      </header>

      <div className="grid grid-cols-[1fr_1.6fr] gap-6">
        <section>
          <h2 className={H}>Fundamentals</h2>
          <dl className="space-y-1 text-[12px]">
            {fundamentals?.rows.map(r => (
              <div
                key={r[0]!.t}
                className="flex justify-between gap-3 border-b border-dotted border-[var(--color-border)] pb-[2px]"
              >
                <dt className="text-[var(--color-fg-secondary)]">{r[0]!.t}</dt>
                <dd className="text-right">
                  <SpanView span={r[1]!} numbers={numbers} bundle={bundle} />
                </dd>
              </div>
            ))}
          </dl>
        </section>

        <section>
          <h2 className={H}>Tier 0: the identity spine</h2>
          <table className="w-full text-[11px]">
            <tbody>
              {tier0.map(r => (
                <tr key={r[1]!.t} className="border-b border-[var(--color-border)] align-top">
                  <th scope="row" className="py-1 pr-2 text-left font-normal">
                    {r[1]!.t.replace(' (tier 0)', '')}
                  </th>
                  <td className="py-1">
                    <SpanView span={r[2]!} numbers={numbers} bundle={bundle} />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </div>

      <footer className="mt-6 border-t border-[var(--color-border)] pt-2 text-[9px] leading-snug text-[var(--color-fg-muted)]">
        <p className="mb-1">
          <strong className="text-[var(--color-fg-secondary)]">
            Independent research, not affiliated with any government or EU body.
          </strong>{' '}
          Every fact is footnoted to a checked source; values in italics are withheld until sourced.
          Generated {bundle.generated}. Full report: /report/{code}.pdf
        </p>
        <ol className="flex flex-wrap gap-x-4">
          {[...numbers.entries()].map(([sid, n]) => (
            <li key={sid}>
              [{n}] {bundle.sources[sid]?.label}
            </li>
          ))}
        </ol>
      </footer>
    </article>
  )
}
