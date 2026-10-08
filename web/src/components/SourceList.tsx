import { reviewLink } from '@/data/contribute'
import type { Bundle } from '@/data/types'

/** A checklist line's kind, by its own wording: the source tier, a check passed, or a shortfall. */
function checkKind(item: string): 'tier' | 'pass' | 'short' | 'plain' {
  if (/^T\d /.test(item)) return 'tier'
  if (
    /^(no archived copy|quote found \(loose|not in the quote|not independently|secondary source)/.test(
      item,
    )
  )
    return 'short'
  if (
    /^(quote found \(exact|archived copy|official source|primary source|blind review|independent review|every figure|value quoted verbatim|dataset value|authoritative statement)/.test(
      item,
    )
  )
    return 'pass'
  return 'plain'
}

const CHECK = {
  tier: 'border-transparent bg-[var(--color-eu-gold)]/15 text-[var(--color-accent-text)]',
  pass: 'border-[var(--color-eu-blue)]/40 text-[var(--color-fg-primary)]',
  short: 'border-dashed border-[var(--color-rank-5)] text-[var(--color-fg-primary)]',
  plain: 'border-[var(--color-border)] text-[var(--color-fg-secondary)]',
}

function host(url: string): string {
  try {
    return new URL(url).hostname.replace(/^www\./, '')
  } catch {
    return ''
  }
}

/** What a claim id names, in words: "Germany · Civil registry core · operator". From the bundle's labels. */
function claimLabel(bundle: Bundle, claim: string): string {
  const [kind, iso = '', id = '', field = ''] = claim.split(':')
  const country = bundle.countries[iso]?.name ?? iso
  if (kind === 'indicator') {
    const ind = bundle.sovereignty.indicators.find(i => i.id === id)
    return `${country} · ${ind?.label ?? id}`
  }
  if (kind === 'record') {
    const h = bundle.holding_classes.find(c => c.class_id === id)
    return `${country} · ${h?.label ?? id} · ${field.replace(/_/g, ' ')}`
  }
  return `${country} · ${id.replace(/_/g, ' ')}`
}

/**
 * The numbered sources for a page: each once, with what makes it checkable -- the URL, an
 * archived copy, the retrieval date, the document hash where one was recorded, and under it
 * every claim on this page that rests on it, with the quote found in the document (#75).
 */
export function SourceList({
  bundle,
  numbers,
  claims,
  hidden,
}: {
  bundle: Bundle
  numbers: Map<string, number>
  claims: Map<string, string[]>
  /** Sources a filter on the page has hidden; they stay in the list, so numbering never shifts. */
  hidden?: Set<string>
}) {
  if (numbers.size === 0) return null
  const ordered = [...numbers.entries()].sort((a, b) => a[1] - b[1])
  return (
    <section id="sources" className="mt-12 border-t border-[var(--color-border)] pt-6">
      <h2 className="mb-2 font-display text-2xl font-bold tracking-tight">Sources</h2>
      <p className="mb-4 max-w-3xl text-sm text-[var(--color-fg-secondary)]">
        Each source is listed once. The hash identifies the exact document that was fetched; the
        quote under each claim is text found in it by machine, in its original language, then a
        machine translation where the source is not in English, then the checks the claim passed.
      </p>
      <p className="mb-4 max-w-3xl text-xs text-[var(--color-fg-muted)]">
        Evidence grades. {bundle.notice.grade_rule}
      </p>
      <ol className="space-y-3 text-sm">
        {ordered.map(([sid, n]) => {
          const s = bundle.sources[sid]
          if (!s) return null
          return (
            <li
              key={sid}
              id={`src-${n}`}
              hidden={hidden?.has(sid)}
              className="scroll-mt-4 rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-4 [overflow-wrap:anywhere] target:border-[var(--color-eu-gold)] target:bg-[var(--color-bg-emphasis)] sm:p-5"
            >
              <div className="flex items-baseline gap-3">
                <span className="font-semibold text-[var(--color-accent-text)] tabular-nums">
                  [{n}]
                </span>
                <div className="min-w-0">
                  <strong className="font-display text-base">{s.title}</strong>
                  <div className="mt-0.5 text-xs text-[var(--color-fg-muted)]">
                    {[s.publisher, s.published, host(s.url)].filter(Boolean).join(' · ')} ·{' '}
                    <a className="underline" href={s.url} rel="noreferrer">
                      Open source
                    </a>
                    {s.archived_url ? (
                      <>
                        {' '}
                        ·{' '}
                        <a className="underline" href={s.archived_url} rel="noreferrer">
                          Archived copy
                        </a>
                      </>
                    ) : null}
                  </div>
                </div>
              </div>
              {s.notes ? (
                <p className="mt-2 font-mono text-[0.7rem] break-all text-[var(--color-fg-muted)]">
                  {s.notes}
                </p>
              ) : null}
              <ul className="mt-3 space-y-3">
                {(claims.get(sid) ?? []).map(claim =>
                  (bundle.claims[claim] ?? [])
                    .filter(c => c.source_id === sid)
                    .map(c => (
                      <li
                        key={claim + c.locator}
                        className="grid gap-2 border-l-[3px] border-[var(--color-eu-gold)] pl-4"
                      >
                        <span className="text-xs font-semibold text-[var(--color-accent-text)]">
                          {claimLabel(bundle, claim)}{' '}
                          <code className="font-normal text-[var(--color-fg-muted)]">{claim}</code>
                        </span>
                        {c.original ? (
                          <blockquote className="font-serif text-base leading-relaxed">
                            “{c.original}”
                          </blockquote>
                        ) : (
                          <p className="text-[var(--color-fg-secondary)]">
                            Value {c.value_as_found} at {c.locator}
                          </p>
                        )}
                        {c.gloss ? (
                          <p className="text-[var(--color-fg-secondary)]">
                            Machine translation: <q>{c.gloss}</q>
                          </p>
                        ) : null}
                        <div className="flex flex-wrap items-center gap-1.5 text-xs">
                          <span
                            className={`rounded-full px-2.5 py-0.5 font-semibold ${
                              c.grade === 'Standard'
                                ? 'border border-[var(--color-border)]'
                                : 'bg-[var(--color-eu-gold)] text-[var(--color-eu-deep)]'
                            }`}
                          >
                            {c.grade}
                          </span>
                          {c.checklist.map(item => (
                            <span
                              key={item}
                              className={`rounded-full border px-2.5 py-0.5 ${CHECK[checkKind(item)]}`}
                            >
                              {item}
                            </span>
                          ))}
                          <span className="text-[var(--color-fg-muted)]">
                            retrieved {c.retrieved} ·{' '}
                            <a
                              className="underline"
                              href={reviewLink(bundle, claim)}
                              rel="noreferrer"
                            >
                              Check this fact
                            </a>
                          </span>
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
