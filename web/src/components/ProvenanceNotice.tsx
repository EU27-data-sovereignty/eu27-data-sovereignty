/**
 * Shown on every page, not buried in the methodology. The wording comes from the bundle
 * (export_json.py), so the site, the PDFs and the briefs hedge identically (#6).
 *
 * It sat as a banner above the header; on a phone that took a quarter of the screen before any
 * content (#92). It now heads the footer of every page, in full, at every width.
 */
export function ProvenanceNotice({
  generated,
  provenance,
}: {
  generated: string
  provenance: string
}) {
  return (
    <p className="mb-4">
      {provenance} Generated {generated}.{' '}
      <a className="underline" href="/methodology">
        How this was built
      </a>
      {' · '}
      <a className="underline" href="/fact-check">
        How every fact was checked
      </a>
      .
    </p>
  )
}
