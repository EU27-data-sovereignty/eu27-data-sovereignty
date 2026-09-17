/**
 * Supabase, wired but idle.
 *
 * Nothing in the app reads from Supabase today: the model ships as a bundled asset (see
 * `src/data/bundle.ts`), so a reader that renders it needs no backend. What Supabase is *for*
 * is the roadmap path in `ROADMAP.md` -- a read-only mirror of the same bundle, so a data
 * correction can reach installed apps without a store release.
 *
 * Two things this file deliberately does not do:
 *
 * - **It does not construct a client at import time.** The template's version builds one with
 *   a placeholder URL when the environment is unset, which means an unconfigured app holds a
 *   client pointed at a domain nobody owns. Here, unconfigured means `null`, and every caller
 *   has to decide what to do about that.
 * - **It does not touch auth.** There are no accounts. `persistSession` is off, so nothing
 *   about a viewer is written to device storage.
 *
 * Only `EXPO_PUBLIC_*` variables reach the client bundle, and only the anon key may ever be
 * one: Expo inlines these at build time, so a service-role key placed here would ship inside
 * the JavaScript. `__tests__/security.test.ts` enforces that.
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
    global: { headers: { 'X-Client-Info': 'sovereign-data-centers-mobile' } },
  });
  return client;
}
