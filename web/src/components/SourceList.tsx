import { reviewLink } from '@/data/contribute'
import type { Bundle } from '@/data/types'

/**
 * The numbered sources for a page: each once, with what makes it checkable -- the URL, an
 * archived copy, the retrieval date, the document hash where one was recorded, and under it
 * every claim on this page that rests on it, with the quote found in the document (#75).
 */
export function SourceList({
  bundle,
  numbers,
  claims,
}: {
  bundle: Bundle
  numbers: Map<string, number>
  claims: Map<string, string[]>
}) {
  if (numbers.size === 0) return null
  const ordered = [...numbers.entries()].sort((a, b) => a[1] - b[1])
  return (
    <section id="sources" className="mt-12 border-t border-[var(--color-border)] pt-6">
      <h2 className="mb-2 text-lg font-semibold text-[var(--color-accent-text)]">Sources</h2>
      <p className="mb-4 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        Each source is listed once. The hash identifies the exact document that was fetched; the
        quote under each claim is text found in it by machine, in its original language, then a
        machine translation where the source is not in English, then the checks the claim passed.
      </p>
      <p className="mb-4 max-w-3xl text-xs text-[var(--color-fg-muted)]">
        Evidence grades. {bundle.notice.grade_rule}
      </p>
      <ol className="space-y-4 text-sm">
        {ordered.map(([sid, n]) => {
          const s = bundle.sources[sid]
          if (!s) return null
          return (
            <li
              key={sid}
              id={`src-${n}`}
              className="scroll-mt-4 rounded [overflow-wrap:anywhere] target:bg-[var(--color-bg-emphasis)]"
            >
              <div>
                <span className="mr-2 font-semibold text-[var(--color-accent-text)]">[{n}]</span>
                <strong>{s.title}</strong>. {s.publisher}
                {s.published ? `, ${s.published}` : ''}.{' '}
                <a className="break-all underline" href={s.url} rel="noreferrer">
                  {s.url}
                </a>
                {s.archived_url ? (
                  <>
                    {' '}
                    (
                    <a className="underline" href={s.archived_url} rel="noreferrer">
                      archived copy
                    </a>
                    )
                  </>
                ) : null}
                {s.notes ? <span className="text-[var(--color-fg-muted)]"> {s.notes}.</span> : null}
              </div>
              <ul className="mt-1 space-y-1 pl-8">
                {(claims.get(sid) ?? []).map(claim =>
                  (bundle.claims[claim] ?? [])
                    .filter(c => c.source_id === sid)
                    .map(c => (
                      <li key={claim + c.locator}>
                        <code className="text-xs text-[var(--color-fg-muted)]">{claim}</code>
                        <div className="text-[var(--color-fg-secondary)]">
                          {c.original ? (
                            <q>{c.original}</q>
                          ) : (
                            <>
                              Value {c.value_as_found} at {c.locator}
                            </>
                          )}
                          {c.gloss ? (
                            <div className="text-[var(--color-fg-muted)]">
                              Machine translation: <q>{c.gloss}</q>
                            </div>
                          ) : null}
                          <div className="text-xs text-[var(--color-fg-muted)]">
                            <strong>{c.grade}</strong>: {c.checklist.join('; ')}; retrieved{' '}
                            {c.retrieved}.{' '}
                            <a
                              className="underline"
                              href={reviewLink(bundle, claim)}
                              rel="noreferrer"
                            >
                              Check this fact
                            </a>
                          </div>
                        </div>
                      </li>
                    )),
                )}
              </ul>
            </li>
          )
        })}
      </ol>
    </section>
  )
}
