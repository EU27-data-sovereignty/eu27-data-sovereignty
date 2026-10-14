/**
 * Where a reader checks a fact or submits a source (#85). The URL templates come from the bundle, so this
 * file holds no address of its own: `__tests__/security.test.ts` bans a literal URL anywhere in the app.
 */
import type { Bundle } from './types';

/** A prefilled "Check a fact" form for one claim. */
export function reviewLink(bundle: Bundle, claim: string): string {
  return bundle.contribute.review.replaceAll('{claim}', encodeURIComponent(claim));
}

/** A prefilled "Submit a source" form for one member state. */
export function submitLink(bundle: Bundle, iso: string): string {
  return bundle.contribute.submit.replaceAll('{iso}', encodeURIComponent(iso));
}
