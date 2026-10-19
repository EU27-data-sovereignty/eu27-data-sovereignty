/**
 * The device's preferred languages, from expo-localization: the only file that imports it, read once at
 * launch, never stored or sent (`__tests__/security.test.ts`).
 */
import { getLocales } from 'expo-localization';

import type { Locale } from './catalogue';

export function deviceLocales(): Locale[] {
  try {
    return getLocales().map((l) => ({ languageCode: l.languageCode, regionCode: l.regionCode }));
  } catch {
    return [];
  }
}
