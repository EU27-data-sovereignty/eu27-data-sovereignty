/**
 * The reader's languages (DECISIONS.md #117). The shipped catalogue holds English and every admitted language;
 * these tests run the screens on a fixture catalogue with two made-up translations, so the wiring is proven
 * before any real language is admitted: every key the app uses exists in English, a language shows only where
 * the catalogue has it, a fact is never translated, and the reader's choice is stored only on the device.
 */
import { fireEvent, render, screen, waitFor } from '@testing-library/react-native';
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
import type { ReactElement } from 'react';

import About from '../app/(tabs)/about';
import CountryScreen from '../app/country/[iso]';
import { bundledPart } from '../src/data/bundled';
import type { CountryPart } from '../src/data/parts';
import { EditionProvider } from '../src/edition/EditionContext';
import { MemoryFileStore } from '../src/edition/memoryFiles';
import { utf8Decode } from '../src/edition/utf8';
import {
  CATALOGUE,
  fill,
  pickLanguage,
  stateLanguage,
  translator,
  type Catalogue,
} from '../src/i18n/catalogue';
import { LanguageProvider } from '../src/i18n/LanguageContext';
import { makeStore } from './support';

jest.mock('expo-constants', () => {
  const { expo } = jest.requireActual('../app.json');
  return { __esModule: true, default: { expoConfig: expo } };
});

jest.mock('expo-router', () => {
  const React = require('react');
  const { Text } = require('react-native');
  return {
    Link: ({ children, asChild }: { children: React.ReactNode; asChild?: boolean }) =>
      asChild ? children : React.createElement(Text, { accessibilityRole: 'link' }, children),
    Stack: { Screen: () => null },
    useLocalSearchParams: () => ({ iso: 'DE' }),
  };
});

const en = CATALOGUE.languages.en!.strings;
const de = bundledPart('eu27.DE.json') as CountryPart;

/** A catalogue with made-up German and Irish: every string prefixed, so a translated one is recognisable. */
function fixture(): Catalogue {
  const mark = (p: string) =>
    Object.fromEntries(Object.entries(en).map(([k, v]) => [k, `${p}${v}`]));
  return {
    states: CATALOGUE.states,
    languages: {
      en: CATALOGUE.languages.en!,
      de: {
        lang: 'de',
        name: 'Deutsch',
        strings: mark('DE·'),
        overlays: { AT: { 'app.tab.countries': 'AT·Countries' } },
        provenance: [
          {
            iso: 'DE',
            tag: 'de-DE',
            drafted: 'agent A',
            reviewed: 'agent B',
            read: 'native speaker, 2026-10-19',
          },
        ],
      },
      ga: {
        lang: 'ga',
        name: 'Gaeilge',
        strings: mark('GA·'),
        overlays: {},
        provenance: [],
      },
    },
  };
}

function renderIn(ui: ReactElement, catalogue: Catalogue, files = new MemoryFileStore()) {
  const { store } = makeStore({ configured: false });
  return render(
    <LanguageProvider files={files} device={[]} catalogue={catalogue}>
      <EditionProvider store={store}>{ui}</EditionProvider>
    </LanguageProvider>
  );
}

function sources(dir: string): string[] {
  return readdirSync(dir).flatMap((name) => {
    const p = join(dir, name);
    return statSync(p).isDirectory() ? sources(p) : /\.tsx?$/.test(name) ? [p] : [];
  });
}

describe('the catalogue', () => {
  it('has every key the app asks for, in English', () => {
    const root = join(__dirname, '..');
    const used = new Set<string>();
    for (const f of [...sources(join(root, 'app')), ...sources(join(root, 'src'))]) {
      for (const m of readFileSync(f, 'utf8').matchAll(/\bt\(\s*'([a-z0-9_.]+)'/g)) used.add(m[1]!);
    }
    expect(used.size).toBeGreaterThan(80);
    expect([...used].filter((k) => !(k in en))).toEqual([]);
    // The keys built from a state's kind, in describe() and describeAppUpdate().
    for (const kind of ['idle', 'unconfigured', 'checking', 'unreachable', 'up_to_date'])
      expect(en[`app.update.${kind}`]).toBeTruthy();
    for (const kind of [
      'disabled',
      'idle',
      'checking',
      'up_to_date',
      'downloading',
      'ready',
      'unreachable',
    ])
      expect(en[`app.appupdate.${kind}`]).toBeTruthy();
  });

  it('ships English and only what model/i18n.py admitted', () => {
    expect(CATALOGUE.languages.en!.strings['app.tab.countries']).toBe('Countries');
    for (const [lang, l] of Object.entries(CATALOGUE.languages)) {
      expect(l.lang).toBe(lang);
      if (lang !== 'en') expect(l.provenance.every((p) => p.read)).toBe(true);
    }
  });

  it('falls back to English per key, fills placeholders, and applies a state overlay', () => {
    const cat = fixture();
    delete cat.languages.de!.strings['app.tab.hosting'];
    const t = translator(cat, 'de').t;
    expect(t('app.tab.ranking')).toBe('DE·Ranking');
    expect(t('app.tab.hosting')).toBe('Hosting');
    expect(t('app.countries.some', { n: 3 })).toBe('DE·3 of 27 member states');
    expect(translator(cat, 'de', 'AT').t('app.tab.countries')).toBe('AT·Countries');
    expect(translator(cat, 'xx').lang).toBe('en');
    expect(fill('{a} and {b}', { a: 1 })).toBe('1 and {b}');
  });

  it('translates content by its exact English text, and only labels, gaps, titles and the disclaimer', () => {
    const tx = translator(fixture(), 'de').tx;
    expect(tx('Not yet sourced')).toBe('DE·Not yet sourced');
    expect(tx('Fundamentals')).toBe('DE·Fundamentals');
    expect(tx('Germany')).toBe('DE·Germany');
    // An app string's English is not content: matching it by text would translate a fact that happens to read the same.
    expect(tx('Countries')).toBe('Countries');
    expect(tx('a sentence nobody drafted')).toBe('a sentence nobody drafted');
  });

  it('picks the reader’s admitted choice, else the device’s, else English', () => {
    const cat = fixture();
    const device = [
      { languageCode: 'fr', regionCode: 'BE' },
      { languageCode: 'de', regionCode: 'AT' },
    ];
    expect(pickLanguage(cat, { lang: 'ga' }, device)).toEqual({ lang: 'ga', region: null });
    expect(pickLanguage(cat, { lang: 'xx' }, device)).toEqual({ lang: 'de', region: 'AT' });
    expect(pickLanguage(cat, null, [])).toEqual({ lang: 'en', region: null });
    expect(stateLanguage(cat, 'DE')).toBe('de');
    expect(stateLanguage(cat, 'FR')).toBeNull();
    expect(stateLanguage(cat, 'IE')).toBe('ga');
  });
});

describe('the screens in another language', () => {
  it('translate the country report’s titles, labels and gaps, never its facts', async () => {
    const files = new MemoryFileStore();
    await files.write('language.json', JSON.stringify({ lang: 'de', region: null }));
    await renderIn(<CountryScreen />, fixture(), files);
    await waitFor(() => expect(screen.getByText('DE·Germany')).toBeTruthy());
    const doc = de.documents.DE!;
    for (const s of doc.sections)
      expect(screen.getAllByText(`DE·${s.title}`).length).toBeGreaterThan(0);
    expect(screen.getAllByText('DE·Not yet sourced').length).toBeGreaterThan(0);
    expect(screen.getByText('DE·Sources')).toBeTruthy();
    const fact = doc.sections
      .flatMap((s) => s.blocks)
      .flatMap((b) => (b.type === 'table' ? b.rows.flat() : b.type === 'p' ? b.spans : []))
      .find((s) => s.role === 'fact' && s.k === 'categorical');
    expect(fact).toBeTruthy();
    expect(screen.queryAllByText(`DE·${fact!.t}`)).toEqual([]);
    expect(screen.getAllByText(fact!.t, { exact: false }).length).toBeGreaterThan(0);
  });

  it('offers a state’s own language on its report, and stores the choice on the device only', async () => {
    const files = new MemoryFileStore();
    await renderIn(<CountryScreen />, fixture(), files);
    const button = await screen.findByText('Read in Deutsch');
    fireEvent.press(button);
    await waitFor(() => expect(screen.getByText('DE·Germany')).toBeTruthy());
    expect(JSON.parse(utf8Decode((await files.read('language.json'))!))).toEqual({
      lang: 'de',
      region: 'DE',
    });
    expect(files.requests).toEqual([]);
  });

  it('lists only the catalogue’s languages, with who drafted, reviewed and read the one on screen', async () => {
    const files = new MemoryFileStore();
    await files.write('language.json', JSON.stringify({ lang: 'de', region: null }));
    await renderIn(<About />, fixture(), files);
    await waitFor(() => expect(screen.getByText('DE·Language')).toBeTruthy());
    expect(screen.getAllByRole('radio').map((r) => r.props.accessibilityState?.checked)).toEqual([
      false,
      true,
      false,
    ]);
    expect(screen.getByText('English')).toBeTruthy();
    expect(screen.getByText('Gaeilge')).toBeTruthy();
    expect(
      screen.getByText(
        'DE·Translated by agent A, reviewed by agent B, read by native speaker, 2026-10-19.',
        {
          exact: false,
        }
      )
    ).toBeTruthy();
    fireEvent.press(screen.getByText('Gaeilge'));
    await waitFor(() => expect(screen.getByText('GA·Language')).toBeTruthy());
  });

  it('shows English alone, and says why, while no other language is admitted', async () => {
    await renderIn(<About />, {
      states: CATALOGUE.states,
      languages: { en: CATALOGUE.languages.en! },
    });
    await waitFor(() => expect(screen.getByText('Language')).toBeTruthy());
    expect(screen.getAllByRole('radio')).toHaveLength(1);
    expect(screen.getByText(en['app.language.pending']!)).toBeTruthy();
  });
});
