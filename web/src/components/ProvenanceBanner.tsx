/**
 * Shown on every page, not buried in the methodology. The wording comes from the bundle
 * (export_json.py), so the site, the PDFs and the briefs hedge identically (#6).
 */
export function ProvenanceBanner({
  generated,
  provenance,
}: {
  generated: string
  provenance: string
}) {
  return (
    <p className="border-b border-[var(--color-border)] bg-[var(--color-bg-emphasis)] px-4 py-2 text-xs text-[var(--color-fg-secondary)]">
      {provenance} Generated {generated}.{' '}
      <a className="underline" href="/methodology">
        How this was built
      </a>
      .
    </p>
  )
}
