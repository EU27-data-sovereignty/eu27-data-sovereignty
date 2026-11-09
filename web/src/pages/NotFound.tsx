import { Link } from 'react-router-dom'

import { PageBand } from '@/components/PageBand'
import { useT } from '@/i18n'

export function NotFound() {
  const t = useT()
  return (
    <article>
      <PageBand kicker={t('site.kicker')} title={t('notfound.title')} />
      <p className="text-[var(--color-fg-secondary)]">
        <Link className="underline" to="/">
          {t('notfound.back')}
        </Link>
      </p>
    </article>
  )
}
