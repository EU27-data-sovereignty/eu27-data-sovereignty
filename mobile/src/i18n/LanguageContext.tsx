/**
 * The reader's language (DECISIONS.md #117): the reader's own choice, stored on the device in one small file,
 * else the device's language if the catalogue has admitted it, else English. Only admitted languages can be
 * chosen. The choice is never sent anywhere; it sits next to the edition in the app's own documents folder.
 */
import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from 'react';

import type { FileStore } from '@/edition/EditionStore';
import { utf8Decode } from '@/edition/utf8';
import {
  CATALOGUE,
  english,
  pickLanguage,
  translator,
  type Catalogue,
  type Language,
  type Locale,
  type Translator,
} from './catalogue';

const CHOICE = 'language.json';

export interface LanguageApi extends Translator {
  /** Every admitted language, English first. */
  languages: Pick<Language, 'lang' | 'name'>[];
  /** Who drafted, reviewed and read the language on screen; empty for English, the source. */
  provenance: Record<string, string>[];
  catalogue: Catalogue;
  choose(lang: string, region?: string | null): Promise<void>;
}

export const LanguageContext = createContext<LanguageApi | null>(null);

export function LanguageProvider({
  files,
  device,
  catalogue = CATALOGUE,
  children,
}: {
  files: FileStore;
  device: Locale[];
  catalogue?: Catalogue;
  children: ReactNode;
}) {
  const [choice, setChoice] = useState(() => pickLanguage(catalogue, null, device));

  useEffect(() => {
    let cancelled = false;
    (async () => {
      let stored: { lang: string; region?: string | null } | null = null;
      try {
        const bytes = await files.read(CHOICE);
        if (bytes) stored = JSON.parse(utf8Decode(bytes));
      } catch {
        stored = null;
      }
      if (!cancelled && stored) setChoice(pickLanguage(catalogue, stored, device));
    })();
    return () => {
      cancelled = true;
    };
  }, [files, catalogue, device]);

  const choose = useCallback(
    async (lang: string, region: string | null = null) => {
      if (!catalogue.languages[lang]) return;
      setChoice({ lang, region });
      await files.write(CHOICE, JSON.stringify({ lang, region }));
    },
    [files, catalogue]
  );

  const value = useMemo<LanguageApi>(() => {
    const tr = translator(catalogue, choice.lang, choice.region);
    const languages = Object.values(catalogue.languages)
      .map(({ lang, name }) => ({ lang, name }))
      .sort((a, b) => (a.lang === 'en' ? -1 : b.lang === 'en' ? 1 : a.name.localeCompare(b.name)));
    return {
      ...tr,
      languages,
      provenance: tr.lang === 'en' ? [] : (catalogue.languages[tr.lang]?.provenance ?? []),
      catalogue,
      choose,
    };
  }, [catalogue, choice, choose]);
  return <LanguageContext.Provider value={value}>{children}</LanguageContext.Provider>;
}

/** The reader's language; English, with no way to choose, outside a provider (a test of one component). */
export function useLanguage(): LanguageApi {
  return (
    useContext(LanguageContext) ?? {
      ...english,
      languages: [{ lang: 'en', name: 'English' }],
      provenance: [],
      catalogue: CATALOGUE,
      choose: async () => {},
    }
  );
}
