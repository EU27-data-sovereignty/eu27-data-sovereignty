import { SourceList } from '@/components/SourceList'
import type { Bundle } from '@/data/types'

/** The whole register of checked sources, each with every claim in the bundle it supports. */
export function Sources({ bundle }: { bundle: Bundle }) {
  const ids = Object.keys(bundle.sources).sort((a, b) =>
    bundle.sources[a]!.title.localeCompare(bundle.sources[b]!.title),
  )
  const numbers = new Map(ids.map((sid, i) => [sid, i + 1]))
  const claims = new Map<string, string[]>()
  for (const [claim, cites] of Object.entries(bundle.claims)) {
    for (const c of cites) claims.set(c.source_id, [...(claims.get(c.source_id) ?? []), claim])
  }
  return (
    <article>
      <h1 className="mb-1 text-2xl font-semibold">Sources</h1>
      <p className="max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        {ids.length} sources support {Object.keys(bundle.claims).length} claims. A source is
        admitted only after its document was fetched, its SHA-256 recorded and the quoted text found
        in it; failures stay out and are recorded in the repository.
      </p>
      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
