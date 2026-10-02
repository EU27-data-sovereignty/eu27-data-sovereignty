import { Link, useParams } from 'react-router-dom'

import { DocumentView } from '@/components/DocumentView'
import { SourceList } from '@/components/SourceList'
import { submitLink } from '@/data/contribute'
import { claimsBySource, coverage, factCounts, numberSources } from '@/data/sources'
import type { Bundle } from '@/data/types'
import { NotFound } from './NotFound'
import { PageBand } from '@/components/PageBand'

/**
 * One member state, analysed on its own fundamentals (#72). The body is the content model --
 * the same document as /report/<ISO>.pdf and countries/<ISO>/GOAL.md -- so the sections, facts
 * and gaps are identical across all three; only the presentation differs.
 */
export function Country({ bundle }: { bundle: Bundle }) {
  const { iso = '' } = useParams()
  const code = iso.toUpperCase()
  const doc = bundle.documents[code]
  const country = bundle.countries[code]
  if (!doc || !country) return <NotFound />

  const numbers = numberSources([doc], bundle)
  const claims = claimsBySource([doc], bundle)
  const cov = coverage(country)
  const { facts, gaps } = factCounts(doc)

  return (
    <article className="lg:grid lg:grid-cols-[12rem_1fr] lg:gap-8">
      <nav aria-label="Contents" className="mb-6 text-sm lg:sticky lg:top-4 lg:mb-0 lg:self-start">
        <h2 className="mb-2 font-semibold text-[var(--color-fg-secondary)]">Contents</h2>
        <ol className="space-y-1">
          {doc.sections.map((s, i) => (
            <li key={s.id}>
              <a className="text-[var(--color-accent-text)] hover:underline" href={`#${s.id}`}>
                {i + 1}. {s.title}
              </a>
            </li>
          ))}
          <li>
            <a className="text-[var(--color-accent-text)] hover:underline" href="#sources">
              Sources
            </a>
          </li>
        </ol>
      </nav>

      <div>
        <p className="text-xs tracking-widest text-[var(--color-fg-muted)] uppercase">
          <Link to="/countries" className="hover:underline">
            Countries
          </Link>{' '}
          · {code}
        </p>
        <PageBand kicker={`EU-27 · Country report · ${doc.iso}`} title={doc.name} />
        <p className="mb-4 text-sm text-[var(--color-fg-secondary)]">
          {cov.verified} of {cov.total} critical holding classes verified · {facts} sourced facts
          shown · {gaps} values withheld until sourced · capacity not yet sized
        </p>
        <p className="mb-8">
          <a
            href={`/report/${code}.pdf`}
            className="inline-block rounded bg-[var(--color-accent)] px-3 py-1.5 text-sm font-semibold text-[var(--color-fg-on-accent)]"
          >
            Download the {doc.name} report (PDF)
          </a>
        </p>

        <p className="mb-8 max-w-3xl rounded border border-[var(--color-border)] px-3 py-2 text-sm">
          Know a public source for one of the {gaps} withheld values, or a better one for a fact?{' '}
          <a className="underline" href={submitLink(bundle, code)} rel="noreferrer">
            Submit a source
          </a>
          . Every fact also has a <em>Check this fact</em> link in its source entry. Submissions are
          checked by machine and then by a different person who reads the language (
          <Link to="/methodology" className="underline">
            methodology
          </Link>
          ).
        </p>

        <DocumentView doc={doc} bundle={bundle} numbers={numbers} />
        <p className="my-6 max-w-3xl text-sm">
          How each fact above was checked by a second model, the one that did not write it:{' '}
          <Link to={`/fact-check/${code}`} className="underline">
            fact check for {doc.name}
          </Link>
          .
        </p>
        <SourceList bundle={bundle} numbers={numbers} claims={claims} />
      </div>
    </article>
  )
}
