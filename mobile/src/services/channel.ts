/**
 * The edition channel's addresses (#111): the public URL of `latest.json` and of each object under an
 * edition id, in the bucket `editions` of the configured Supabase project. This is the only place in the
 * app a URL is built, and every one is derived from the configured project, never written down: a reader
 * of the code can see that the app talks to one host, and `__tests__/security.test.ts` checks that no
 * other file hands a URL to the file store.
 */
import { LATEST } from '@/edition/manifest';
import { getSupabase } from './supabase';

export const BUCKET = 'editions';

export interface Channel {
  latestUrl(): string;
  objectUrl(edition: string, name: string): string;
}

/** The channel, or null when Supabase is not configured: then there is nothing to check. */
export function channel(): Channel | null {
  const client = getSupabase();
  if (!client) return null;
  const url = (path: string) => client.storage.from(BUCKET).getPublicUrl(path).data.publicUrl;
  return {
    latestUrl: () => url(LATEST),
    objectUrl: (edition, name) => url(`${edition}/${name}`),
  };
}
