import { Link } from 'react-router-dom'

import { DocumentView } from '@/components/DocumentView'
import { PageBand } from '@/components/PageBand'
import { SourceList } from '@/components/SourceList'
import { claimsBySource, numberSources } from '@/data/sources'
import type { Bundle } from '@/data/types'

/**
 * Where each state's key registers are hosted, and by whom (#95). The body is the generated overview
 * (document.infrastructure), whose cells are the spans the country reports print, so a fact here
 * carries the same source and the same fact check as on its country page. Nothing is written here.
 */
export function Infrastructure({ bundle }: { bundle: Bundle }) {
  const doc = bundle.infrastructure
  const numbers = numberSources([doc], bundle)
  const claims = claimsBySource([doc], bundle)

  return (
    <article>
      <PageBand kicker="EU-27 · Key infrastructure" title={doc.name} />
      <p className="mb-6 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        {bundle.notice.disclaimer} The same overview is in the{' '}
        <a className="underline" href="/eu27-report.pdf">
          EU-27 report
        </a>
        ; each holding in full is on its{' '}
        <Link to="/countries" className="underline">
          country page
        </Link>
        .
      </p>
      <DocumentView doc={doc} bundle={bundle} numbers={numbers} />
      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
