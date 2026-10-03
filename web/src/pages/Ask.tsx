import { useRef, useState } from 'react'

import { SourceList } from '@/components/SourceList'
import type { Bundle } from '@/data/types'
import { PageBand } from '@/components/PageBand'

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
  const [question, setQuestion] = useState('')
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
    <article className="max-w-3xl">
      <PageBand kicker="EU-27 · Ask" title="Ask about data sovereignty in the EU" />
      <p className="mb-4 text-sm text-[var(--color-fg-secondary)]">
        Answers come only from this project’s sourced findings, with a citation for every fact. When
        the findings don’t cover a question, the answer says so.
      </p>

      <form
        onSubmit={e => {
          e.preventDefault()
          if (question.trim()) void ask(question.trim())
        }}
      >
        <label htmlFor="question" className="mb-1 block text-sm font-semibold">
          Your question
        </label>
        <textarea
          id="question"
          value={question}
          maxLength={MAX}
          rows={3}
          onChange={e => setQuestion(e.target.value)}
          // 16 px: iPhone Safari zooms the whole page into any field set smaller (#92).
          className="w-full rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-2 text-base"
        />
        <div className="mt-1 flex items-center justify-between text-xs text-[var(--color-fg-muted)]">
          <span>
            {question.length} / {MAX}
          </span>
          <button
            type="submit"
            disabled={status === 'asking' || !question.trim()}
            className="rounded bg-[var(--color-accent)] px-3 py-1.5 text-sm font-semibold text-[var(--color-fg-on-accent)] disabled:opacity-50"
          >
            {status === 'asking' ? 'Answering…' : 'Ask'}
          </button>
        </div>
      </form>

      <p className="mt-2 text-xs text-[var(--color-fg-muted)]">
        Your question is sent to Anthropic’s API to generate the answer. This site does not store
        it. Answers may be incomplete: they reflect only what has been verified so far.
      </p>

      <section aria-label="Example questions" className="mt-4">
        <h2 className="mb-1 text-sm font-semibold">Try</h2>
        <ul className="flex flex-wrap gap-2">
          {EXAMPLES.map(q => (
            <li key={q}>
              <button
                type="button"
                onClick={() => setQuestion(q)}
                className="rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] px-2 py-1 text-left text-xs hover:border-[var(--color-accent)]"
              >
                {q}
              </button>
            </li>
          ))}
        </ul>
      </section>

      <section aria-live="polite" aria-label="Answer" className="mt-6">
        {status === 'error' ? (
          <p className="rounded border-l-4 border-[var(--color-highlight)] bg-[var(--color-bg-emphasis)] px-3 py-2 text-sm">
            {message}
          </p>
        ) : null}
        {segments.length ? (
          <div className="rounded border border-[var(--color-border)] bg-[var(--color-bg-card)] p-4 leading-relaxed whitespace-pre-wrap">
            {segments.map((s, i) =>
              'text' in s ? (
                <span key={i}>{s.text}</span>
              ) : (
                <sup key={i} className="ml-0.5">
                  {s.cite.map(n => (
                    <a
                      key={n}
                      href={`#src-${n}`}
                      className="text-[var(--color-accent-text)] no-underline hover:underline"
                      aria-label={`Source ${n}`}
                    >
                      [{n}]
                    </a>
                  ))}
                </sup>
              ),
            )}
            {status === 'asking' ? <span className="text-[var(--color-fg-muted)]"> …</span> : null}
          </div>
        ) : status === 'asking' ? (
          <p className="text-sm text-[var(--color-fg-muted)]">Reading the sourced findings…</p>
        ) : null}
      </section>

      <SourceList bundle={bundle} numbers={numbers} claims={claims} />
    </article>
  )
}
