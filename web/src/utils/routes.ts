/**
 * One member state, one top-level path: `/de`, `/fr`, `/el` (#105). The code is the EU-27 ISO code the
 * bundle keys on (Eurostat's, so Greece is `EL`), lowercased. Every link to a country page is built here so
 * the shape changes in one place.
 */
export const countryPath = (iso: string) => `/${iso.toLowerCase()}`

/** The country page before #105, kept as a redirect so printed and shared links still land. */
export const LEGACY_COUNTRY_PREFIX = '/country/'
