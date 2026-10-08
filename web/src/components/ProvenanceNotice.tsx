/**
 * Shown on every page, not buried in the methodology. The wording comes from the bundle
 * (export_json.py), so the site, the PDFs and the briefs hedge identically (#6).
 *
 * On a phone the full notice took a quarter of the screen before any content (#92). There its first
 * sentence, the one that matters most, stays visible on every page, and the rest is one tap away; from
 * the `sm` breakpoint up the whole notice shows, as before.
 */
export function ProvenanceBanner({
  generated,
  provenance,
}: {
  generated: string
  provenance: string
}) {
  const cut = provenance.indexOf('. ')
  const lead = cut > 0 ? provenance.slice(0, cut + 1) : provenance
  const rest = cut > 0 ? provenance.slice(cut + 2) : ''
  const links = (
    <>
      Generated {generated}.{' '}
      <a className="underline" href="/methodology">
        How this was built
      </a>
      {' · '}
      <a className="underline" href="/fact-check">
        How every fact was checked
      </a>
      .
    </>
  )
  return (
    <div className="border-b border-[var(--color-border)] bg-[var(--color-bg-emphasis)] px-4 py-2 text-xs text-[var(--color-fg-secondary)]">
      <p className="hidden sm:block">
        {provenance} {links}
      </p>
      <details className="sm:hidden">
        <summary className="cursor-pointer py-1">
          <strong className="font-semibold text-[var(--color-fg-primary)]">{lead}</strong>{' '}
          <span className="underline">Read the full notice</span>
        </summary>
        <p className="mt-1">
          {rest} {links}
        </p>
      </details>
    </div>
  )
}
