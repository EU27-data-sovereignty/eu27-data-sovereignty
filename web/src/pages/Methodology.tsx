import type { Bundle } from '@/data/types'

/** How the analysis is built. Method text only: every fact lives in the documents. */
export function Methodology({ bundle }: { bundle: Bundle }) {
  return (
    <article className="max-w-3xl space-y-4">
      <h1 className="text-2xl font-semibold">Methodology</h1>

      <h2 className="text-lg font-semibold text-[var(--color-accent-text)]">
        Each country on its own fundamentals
      </h2>
      <p>
        No member state is scaled from, or compared against, another. Each is described by its own
        measured characteristics (pinned Eurostat series), the critical data holdings it keeps, and
        the legal instruments that govern them.
      </p>

      <h2 className="text-lg font-semibold text-[var(--color-accent-text)]">
        Critical data holdings
      </h2>
      <p>
        {bundle.holding_classes.length} classes of government data holding, from the identity spine
        (civil registry, biometrics, eID) through the legal, fiscal and security state to health,
        statistics and archives. For each state and class the inventory records the register or
        system, its operator, its legal basis, where it is hosted and its size, each only where a
        source states it.
      </p>
      <p className="rounded border-l-4 border-[var(--color-accent)] bg-[var(--color-bg-emphasis)] px-3 py-2 text-sm">
        {bundle.priority_rule}
      </p>

      <h2 className="text-lg font-semibold text-[var(--color-accent-text)]">
        How a source is checked
      </h2>
      <p>
        A researched claim is admitted only after the cited page or PDF is downloaded, its SHA-256
        recorded, and the quoted text found in the extracted document. An archived copy is looked up
        on the Internet Archive. A claim that fails stays out of every output. A value without an
        admitted source is withheld and shown as a gap, never as a fact.
      </p>

      <h2 className="text-lg font-semibold text-[var(--color-accent-text)]">Capacity</h2>
      <p>
        Capacity (servers, power, sites, cost) is not yet shown. It will be derived for each state
        from its own measured holdings. Earlier versions scaled one country's plan to the other 26;
        that method was withdrawn because it described no state on its own terms.
      </p>

      <p className="text-sm text-[var(--color-fg-muted)]">{bundle.national_data_note}</p>
    </article>
  )
}
