/**
 * Supabase: one public, read-only bucket, read anonymously (#111).
 *
 * The app ships the fact-checked edition inside its binary and renders it with no backend. What Supabase
 * is *for* is the edition channel: `latest.json` and the parts of a newer edition, which `src/edition/`
 * downloads and verifies against their hashes before a single span of them is shown. That is the app's
 * only network path, and `src/services/channel.ts` is the only place a URL is built.
 *
 * Two things this file deliberately does not do:
 *
 * - **It does not construct a client at import time.** The template's version builds one with a
 *   placeholder URL when the environment is unset, which means an unconfigured app holds a client pointed
 *   at a domain nobody owns. Here, unconfigured means `null`: the app reads its bundled edition and makes
 *   no request at all.
 * - **It does not touch auth.** There are no accounts. `persistSession` is off, so nothing about a reader
 *   is written to device storage.
 *
 * Only `EXPO_PUBLIC_*` variables reach the client bundle, and only the anon key may ever be one: Expo
 * inlines these at build time, so a service-role key placed here would ship inside the JavaScript. The
 * anon key unlocks nothing: the bucket's one policy is a public `select`, and nothing else is granted
 * (`supabase/migrations/`). `__tests__/security.test.ts` enforces the names.
 */
import 'react-native-url-polyfill/auto';
import { createClient, type SupabaseClient } from '@supabase/supabase-js';

const url = process.env.EXPO_PUBLIC_SUPABASE_URL;
const anonKey = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY;

export const isSupabaseConfigured = Boolean(url && anonKey);

let client: SupabaseClient | null = null;

/** The client, or null when the app is running as it does by default: with no backend. */
export function getSupabase(): SupabaseClient | null {
  if (!isSupabaseConfigured) return null;
  client ??= createClient(url as string, anonKey as string, {
    auth: { persistSession: false, autoRefreshToken: false, detectSessionInUrl: false },
    global: { headers: { 'X-Client-Info': 'eu27-data-sovereignty-mobile' } },
  });
  return client;
}
