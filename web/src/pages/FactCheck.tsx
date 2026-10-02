import { Link, useParams } from 'react-router-dom'

import { DocumentView } from '@/components/DocumentView'
import type { Bundle } from '@/data/types'

/**
 * How every printed fact was checked by the model that did not write it (#87): the EU-27 appendix at
 * /fact-check, a country's at /fact-check/:iso. Rendered from the generated document
 * (model/factcheck_appendix.py) the PDFs and briefs carry as their appendix; nothing is written here.
 */
export function FactCheck({ bundle }: { bundle: Bundle }) {
  const { iso } = useParams()
  const code = iso?.toUpperCase()
  const doc = code ? bundle.factcheck.countries[code] : bundle.factcheck.eu
  if (!doc) {
    return <p>No fact-check appendix for {iso}.</p>
  }
  const name = code ? bundle.documents[code]?.name : undefined
  return (
    <article className="max-w-5xl">
      <h1 className="mb-4 text-2xl font-semibold">Fact check{name ? `: ${name}` : ''}</h1>
      {name && (
        <p className="mb-4 text-sm">
          <Link to={`/country/${code}`} className="underline">
            Back to {name}
          </Link>{' '}
          ·{' '}
          <Link to="/fact-check" className="underline">
            All member states
          </Link>
        </p>
      )}
      <DocumentView doc={doc} bundle={bundle} numbers={new Map()} />
    </article>
  )
}
