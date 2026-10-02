import { Link } from 'react-router-dom'

import { PageBand } from '@/components/PageBand'

export function NotFound() {
  return (
    <article>
      <PageBand kicker="EU-27" title="Page not found" />
      <p className="text-[var(--color-fg-secondary)]">
        <Link className="underline" to="/">
          Back to the overview
        </Link>
      </p>
    </article>
  )
}
