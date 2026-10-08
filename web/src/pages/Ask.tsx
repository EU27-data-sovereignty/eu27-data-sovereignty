import { useRef, useState } from 'react'
import { useLocation } from 'react-router-dom'

import { SourceList } from '@/components/SourceList'
import type { Bundle } from '@/data/types'
import { PageBand } from '@/components/PageBand'
import { CARD } from '@/components/ui'

const MAX = 500

const EXAMPLES = [
  'Which member states have a law keeping government data under national jurisdiction?',
  'Who operates Germany’s population register, and under which law?',
  'Which holdings are still unverified for Estonia?',
  'How does the data-sovereignty ranking work, and how confident is it?',
  'Is it known where Belgium’s critical registers are hosted?',
  'What does "not demonstrated" mean in the ranking?',
]

type Segment = { text: string } | { cite: number[] }
type Status = 'idle' | 'asking' | 'done' | 'error'

/**
 * Ask a question; the answer comes only from this project's sourced data (#78). Each citation
 * the model makes is resolved to the claims it rests on and shown as a numbered marker that
 * jumps to the same source card the rest of the site uses: quote, URL, hash, archived copy.
 */
export function Ask({ bundle }: { bundle: Bundle }) {
  // A question typed into the front page's search box arrives as router state, never in the URL.
  const passed = (useLocation().state as { question?: string } | null)?.question ?? ''
  const [question, setQuestion] = useState(passed.slice(0, MAX))
  const [segments, setSegments] = useState<Segment[]>([])
  const [status, setStatus] = useState<Status>('idle')
  const [message, setMessage] = useState('')
  const [numbers, setNumbers] = useState<Map<string, number>>(new Map())
  const [claims, setClaims] = useState<Map<string, string[]>>(new Map())
  const abort = useRef<AbortController | null>(null)

  async function ask(q: string) {
    abort.current?.abort()
    const ctrl = new AbortController()
    abort.current = ctrl
    setSegments([])
    setMessage('')
    setStatus('asking')
    const nums = new Map<string, number>()
    const bySource = new Map<string, string[]>()

    try {
      const res = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ question: q }),
        signal: ctrl.signal,
      })
      if (!res.ok || !res.body) {
        const body = (await res.json().catch(() => ({}))) as { error?: string }
        setMessage(
          res.status === 429
            ? 'Too many questions from here right now. Please try again later.'
            : (body.error ?? 'Something went wrong. Please try again.'),
        )
        setStatus('error')
        return
      }
      const reader = res.body.getReader()
      const decoder = new TextDecoder()
      let buffer = ''
      for (;;) {
        const { value, done } = await reader.read()
        if (done) break
        buffer += decoder.decode(value, { stream: true })
        const chunks = buffer.split('\n\n')
        buffer = chunks.pop() ?? ''
        for (const chunk of chunks) {
          if (!chunk.startsWith('data: ')) continue
          const ev = JSON.parse(chunk.slice(6)) as {
            type: string
            text?: string
            claims?: string[]
            code?: string
            message?: string
            stop_reason?: string | null
          }
          if (ev.type === 'text' && ev.text) {
            setSegments(s => [...s, { text: ev.text! }])
          } else if (ev.type === 'cite') {
            const marks: number[] = []
            for (const claim of ev.claims ?? []) {
              for (const cite of bundle.claims[claim] ?? []) {
                if (!nums.has(cite.source_id)) nums.set(cite.source_id, nums.size + 1)
                const n = nums.get(cite.source_id)!
                if (!marks.includes(n)) marks.push(n)
                const list = bySource.get(cite.source_id) ?? []
                if (!list.includes(claim)) list.push(claim)
                bySource.set(cite.source_id, list)
              }
            }
            if (marks.length) setSegments(s => [...s, { cite: marks }])
            setNumbers(new Map(nums))
            setClaims(new Map(bySource))
          } else if (ev.type === 'error') {
            setMessage(ev.message ?? 'Something went wrong.')
            setStatus('error')
            return
          } else if (ev.type === 'done') {
            if (ev.stop_reason === 'refusal') {
              setMessage('This question could not be answered. Please rephrase it.')
              setStatus('error')
              return
            }
          }
        }
      }
      setStatus('done')
    } catch (e) {
      if ((e as Error).name === 'AbortError') return
      setMessage('Could not reach the answering service. Please try again.')
      setStatus('error')
    }
  }

  return (
    <article>
      <PageBand kicker="EU-27 · Ask" title="Ask about data sovereignty in the EU">
        <p className="mt-3 max-w-3xl text-white/85">
          Answers come only from this project’s sourced findings, with a citation for every fact.
          When the findings don’t cover a question, the answer says so.
        </p>
      </PageBand>

      <div className="grid items-start gap-8 lg:grid-cols-[minmax(0,1fr)_300px]">
        <div className="min-w-0">
          <form
            onSubmit={e => {
              e.preventDefault()
              if (question.trim()) void ask(question.trim())
            }}
          >
            <label htmlFor="question" className="sr-only">
              Your question
            </label>
            <div
              className={`${CARD} p-1.5 transition-colors focus-within:border-[var(--color-eu-gold)]`}
            >
              <textarea
                id="question"
                value={question}
                maxLength={MAX}
                rows={4}
                placeholder="Ask about a member state, a holding or the ranking"
                onChange={e => setQuestion(e.target.value)}
                // 16 px: iPhone Safari zooms the whole page into any field set smaller (#92).
                className="w-full resize-y bg-transparent p-3 text-base outline-none placeholder:text-[var(--color-fg-muted)]"
              />
              <div className="flex items-center justify-between gap-3 px-3 pb-1.5">
                <span className="text-xs text-[var(--color-fg-muted)] tabular-nums">
                  {question.length} / {MAX}
                </span>
                <button
                  type="submit"
                  disabled={status === 'asking' || !question.trim()}
                  className="rounded bg-[var(--color-eu-gold)] px-5 py-2 text-sm font-semibold text-[var(--color-eu-deep)] disabled:opacity-50"
                >
                  {status === 'asking' ? 'Answering…' : 'Ask'}
                </button>
              </div>
            </div>
          </form>

          <p className="mt-2.5 max-w-2xl text-xs text-[var(--color-fg-muted)]">
            Your question is sent to Anthropic’s API to generate the answer. This site does not
            store it. Answers may be incomplete: they reflect only what has been verified so far.
          </p>

          <section aria-live="polite" aria-label="Answer" className="mt-6">
            {status === 'error' ? (
              <p className="rounded border-l-4 border-[var(--color-highlight)] bg-[var(--color-bg-emphasis)] px-3 py-2 text-sm">
                {message}
              </p>
            ) : null}
            {segments.length ? (
              <div className={`${CARD} p-5 leading-relaxed whitespace-pre-wrap sm:p-6`}>
                {segments.map((s, i) =>
                  'text' in s ? (
                    <span key={i}>{s.text}</span>
                  ) : (
                    <sup key={i} className="ml-0.5">
                      {s.cite.map(n => (
                        <a
                          key={n}
                          href={`#src-${n}`}
                          className="font-semibold text-[var(--color-accent-text)] no-underline hover:underline"
                          aria-label={`Source ${n}`}
                        >
                          [{n}]
                        </a>
                      ))}
                    </sup>
                  ),
                )}
                {status === 'asking' ? (
                  <span className="text-[var(--color-fg-muted)]"> …</span>
                ) : null}
              </div>
            ) : status === 'asking' ? (
              <p className="text-sm text-[var(--color-fg-muted)]">Reading the sourced findings…</p>
            ) : null}
          </section>
        </div>

        <section aria-label="Example questions">
          <h2 className="mb-2.5 text-xs font-semibold tracking-[0.12em] text-[var(--color-accent-text)] uppercase">
            Try
          </h2>
          <ul>
            {EXAMPLES.map(q => (
              <li key={q} className="border-t border-[var(--color-border)]">
                <button
                  type="button"
                  onClick={() => setQuestion(q)}
                  className="block w-full py-3 text-left text-sm text-[var(--color-fg-secondary)] hover:text-[var(--color-fg-primary)]"
                >
                  {q} <span className="text-[var(--color-accent-text)]">→</span>
                </button>
              </li>
            ))}
          </ul>
        </section>
      </div>

      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
