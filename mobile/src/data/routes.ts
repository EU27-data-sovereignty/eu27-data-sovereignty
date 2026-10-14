/**
 * Every link to a country screen is built here, as `web/src/utils/routes.ts` does for the site (#105). The
 * app's routes are its own: `/country/EL` for Greece, by the EU-27 code the bundle keys on (Eurostat's, never
 * GR). The web's two-letter top-level path is a Vercel routing constraint, not part of the content model.
 */
export const countryPath = (iso: string) => `/country/${iso.toUpperCase()}` as const;

export const factCheckPath = (iso?: string) =>
  iso ? (`/fact-check/${iso.toUpperCase()}` as const) : ('/fact-check' as const);
