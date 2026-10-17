/**
 * The site's addresses the app may open in the system browser (#116): the privacy policy Apple and Google
 * require to be reachable from the app. Read from `app.json` (`extra.siteUrl`, `extra.privacyPath`), never
 * written down here, so `__tests__/security.test.ts` still finds no host in the code, and the one place a
 * site URL is built is this file.
 */
import Constants from 'expo-constants';

const extra = (): Record<string, unknown> =>
  (Constants.expoConfig?.extra ?? {}) as Record<string, unknown>;

/** The site, or null when the config names none: then the link is not shown. */
export function siteUrl(): string | null {
  const url = extra().siteUrl;
  return typeof url === 'string' && url.startsWith('https://') ? url.replace(/\/$/, '') : null;
}

export function privacyUrl(): string | null {
  const site = siteUrl();
  const path = extra().privacyPath;
  if (!site || typeof path !== 'string' || !path.startsWith('/')) return null;
  return `${site}${path}`;
}
