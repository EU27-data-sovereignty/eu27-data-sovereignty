import type { Bundle } from './types'

/** A prefilled "Check a fact" form for one claim (#85). The template comes from the bundle. */
export function reviewLink(bundle: Bundle, claim: string): string {
  return bundle.contribute.review.replaceAll('{claim}', encodeURIComponent(claim))
}

/** A prefilled "Submit a source" form for one member state. */
export function submitLink(bundle: Bundle, iso: string): string {
  return bundle.contribute.submit.replaceAll('{iso}', encodeURIComponent(iso))
}

/** The general corrections form, for a reader who has no single claim in hand. */
export const CORRECTIONS_URL =
  'https://github.com/EU27-data-sovereignty/eu27-data-sovereignty/issues/new?template=data-correction.yml'
