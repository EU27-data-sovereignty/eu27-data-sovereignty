import { PageBand } from '@/components/PageBand'
import { CORRECTIONS_URL } from '@/data/contribute'

/**
 * What this project collects, and from whom (#116). One page for every surface: the site, `/ask`, and the
 * mobile reader, whose store listings must point at a privacy policy and whose About tab links here. Every
 * sentence below is a statement the tree can be held to: the reader's `__tests__/security.test.ts` asserts
 * the app's claims, and `tests/test_privacy.py` that this page names each processor the plans name.
 */
const processors: [string, string, string, string][] = [
  [
    'Vercel',
    'Hosts the site and runs /ask',
    'Your network address, browser and the time of each request, in its logs',
    'United States company; the site is served from its edge network',
  ],
  [
    'Anthropic',
    'Answers the question you type on /ask',
    'The text of your question and the passages of the report it is answered from, nothing else',
    'United States; the project uses a workspace with no training on its traffic',
  ],
  [
    'Supabase',
    'Serves a newer edition to the mobile reader when you ask for one',
    'Your network address, the app’s user agent and the time, in its logs',
    'EU region project; read-only for the app',
  ],
  [
    'Expo (EAS)',
    'Serves a newer build of the mobile reader’s code when you ask for one',
    'Your network address, the app’s user agent, its runtime version and the time, in its logs',
    'United States',
  ],
  [
    'Apple, Google',
    'Distribute the mobile reader through their stores',
    'What their stores collect under their own policies; the app sends them nothing',
    'Their regions',
  ],
]

export function Privacy() {
  return (
    <article className="max-w-3xl">
      <PageBand kicker="EU-27 · Privacy" title="What this project collects" />

      <p className="mb-6 text-[var(--color-fg-secondary)]">
        Nothing it can avoid. There are no accounts, no analytics, no advertising and no tracking on
        the site, in the mobile reader or in the documents. This page lists the few things that do
        reach a server, when, and who runs that server. It is the privacy policy the app stores link
        to.
      </p>

      <h2 className="mt-8 mb-2 text-lg font-semibold text-[var(--color-fg-primary)]">The site</h2>
      <p className="mb-4 text-[var(--color-fg-secondary)]">
        eu27.cloud is a static site. Reading it sends the ordinary web requests to the host, which
        keeps the usual request logs. The site sets no cookies and loads no third-party scripts;
        your choice of light or dark theme is stored in your own browser only.
      </p>

      <h2 className="mt-8 mb-2 text-lg font-semibold text-[var(--color-fg-primary)]">Ask</h2>
      <p className="mb-4 text-[var(--color-fg-secondary)]">
        A question typed on the Ask page is sent to a language model to be answered from the
        report’s own text. The question and the passages it is answered from are what the model
        receives; no identity, no account, no history. Do not type anything about yourself or
        another person into it.
      </p>

      <h2 className="mt-8 mb-2 text-lg font-semibold text-[var(--color-fg-primary)]">
        The mobile reader
      </h2>
      <p className="mb-4 text-[var(--color-fg-secondary)]">
        The app carries the whole edition inside it and reads with no network at all. It asks for no
        permission, collects nothing, stores nothing about you, and in its default configuration
        makes no request. Two controls on its About tab reach the network, both off until you use
        them: a tap on “Check for a newer edition”, or the switch that repeats that check at launch.
        One check sends one request for a small pointer to the project’s edition channel and, if
        there is a newer edition, up to 29 more for its files, every one verified against its
        published hash before a single value is shown; then one request to Expo’s update service for
        a newer build of the app’s code. Each host sees your network address, the app’s user agent
        and the time, as any host does. Apple’s App Store and Google Play collect what their own
        policies say when you install or update the app; the app itself sends them nothing.
      </p>

      <h2 className="mt-8 mb-2 text-lg font-semibold text-[var(--color-fg-primary)]">
        Who runs the servers
      </h2>
      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-left text-sm">
          <thead>
            <tr className="border-b border-[var(--color-border)] text-[var(--color-fg-muted)]">
              <th className="py-2 pr-3 font-medium">Processor</th>
              <th className="py-2 pr-3 font-medium">Purpose</th>
              <th className="py-2 pr-3 font-medium">What it sees</th>
              <th className="py-2 font-medium">Where</th>
            </tr>
          </thead>
          <tbody>
            {processors.map(([who, purpose, sees, where]) => (
              <tr key={who} className="border-b border-[var(--color-border)] align-top">
                <td className="py-2 pr-3 font-medium text-[var(--color-fg-primary)]">{who}</td>
                <td className="py-2 pr-3 text-[var(--color-fg-secondary)]">{purpose}</td>
                <td className="py-2 pr-3 text-[var(--color-fg-secondary)]">{sees}</td>
                <td className="py-2 text-[var(--color-fg-secondary)]">{where}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <h2 className="mt-8 mb-2 text-lg font-semibold text-[var(--color-fg-primary)]">
        Corrections and contact
      </h2>
      <p className="mb-4 text-[var(--color-fg-secondary)]">
        Sources and corrections arrive through{' '}
        <a className="underline" href={CORRECTIONS_URL}>
          the public forms on the project’s repository
        </a>
        , under your GitHub handle, which is public by its nature; nothing further is asked.
        Questions about this page go the same way. The project is independent research by one
        person, not affiliated with any government or EU body; a foundation that would become the
        controller of anything collected is planned, and this page will name it when it exists.
      </p>
    </article>
  )
}
