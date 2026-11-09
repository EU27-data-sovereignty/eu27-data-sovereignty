import { useLang, useT, useTx } from '@/i18n'

/**
 * Shown on every page, not buried in the methodology. The wording comes from the bundle
 * (export_json.py), so the site, the PDFs and the briefs hedge identically (#6).
 *
 * It sat as a banner above the header; on a phone that took a quarter of the screen before any
 * content (#92). It now heads the footer of every page, in full, at every width.
 *
 * On a state page served in another language the disclaimer is printed first in that language, from the
 * admitted table (#112), and the English notice follows unchanged: it is the wording the rest of the project
 * hedges with, and the translation of the one sentence that must not be weakened stays beside its source.
 */
export function ProvenanceNotice({
  generated,
  provenance,
}: {
  generated: string
  provenance: string
}) {
  const { lang, tag } = useLang()
  const t = useT()
  const { tx } = useTx()
  return (
    <>
      {lang === 'en' ? null : (
        <p lang={tag} className="mb-2 font-semibold">
          {t('notice.disclaimer')}
        </p>
      )}
      <p className="mb-4">
        <span lang="en">{provenance}</span> {tx('Generated {date}.', { date: generated })}{' '}
        <a className="underline" href="/methodology">
          {tx('How this was built')}
        </a>
        {' · '}
        <a className="underline" href="/fact-check">
          {tx('How every fact was checked')}
        </a>
        .
      </p>
    </>
  )
}
