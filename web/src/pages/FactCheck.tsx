import { Link, useParams } from 'react-router-dom'

import { DocumentView } from '@/components/DocumentView'
import { methodBlocks } from '@/utils/methodBlocks'
import { MethodFrame } from '@/components/MethodFrame'
import type { Bundle } from '@/data/types'
import { useCountryName, useTx } from '@/i18n'
import { countryPath } from '@/utils/routes'

/**
 * How every printed fact was checked by the model that did not write it (#87): the EU-27 appendix at
 * /fact-check, a country's at /fact-check/:iso. Rendered from the generated document
 * (model/factcheck_appendix.py) the PDFs and briefs carry as their appendix; nothing is written here.
 */
export function FactCheck({ bundle }: { bundle: Bundle }) {
  const { iso } = useParams()
  const { tx } = useTx()
  const countryName = useCountryName()
  const code = iso?.toUpperCase()
  const doc = code ? bundle.factcheck.countries[code] : bundle.factcheck.eu
  if (!doc) {
    return <p>{tx('No fact-check appendix for {iso}.', { iso: iso ?? '' })}</p>
  }
  const english = code ? bundle.documents[code]?.name : undefined
  const name = code && english ? countryName(code, english) : undefined
  return (
    <MethodFrame
      title={name ? tx('Fact check: {name}', { name }) : tx('Fact check')}
      sections={doc.sections}
    >
      {name && code && (
        <p className="mb-4 text-sm">
          <Link to={countryPath(code)} className="underline">
            {tx('Back to {name}', { name })}
          </Link>{' '}
          ·{' '}
          <Link to="/fact-check" className="underline">
            {tx('All member states')}
          </Link>
        </p>
      )}
      <DocumentView doc={doc} bundle={bundle} numbers={new Map()} blocks={methodBlocks(bundle)} />
    </MethodFrame>
  )
}
