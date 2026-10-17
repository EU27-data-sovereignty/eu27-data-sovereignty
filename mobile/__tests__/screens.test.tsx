/**
 * Render tests on the edition inside the binary: the screens put the model's real content on the screen.
 *
 * Asserting concrete content rather than "renders without crashing" is the point, and it is what
 * `web/e2e/app.spec.ts` does for the site: a screen that renders an empty list, or one wired to a
 * placeholder, passes any test that only checks for the absence of an exception. Every screen must also
 * carry the provenance notice (tests/test_evidence.py).
 */
import { fireEvent, screen, waitFor, within } from '@testing-library/react-native';

import About from '../app/(tabs)/about';
import Countries from '../app/(tabs)/index';
import Infrastructure from '../app/(tabs)/infrastructure';
import Method from '../app/(tabs)/method';
import Sovereignty from '../app/(tabs)/sovereignty';
import CountryScreen from '../app/country/[iso]';
import FactCheckCountry from '../app/fact-check/[iso]';
import FactCheckEu from '../app/fact-check/index';
import { BUNDLED_MANIFEST, bundledPart } from '../src/data/bundled';
import type { CorePart, CountryPart } from '../src/data/parts';
import { fakeAppUpdates, makeStore, renderWithEdition } from './support';

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

const core = bundledPart('eu27.core.json') as CorePart;
const de = bundledPart('eu27.DE.json') as CountryPart;
const notice = core.notice.disclaimer.slice(0, 40);

async function provenanceShown() {
  await waitFor(() =>
    expect(screen.getAllByText(notice, { exact: false }).length).toBeGreaterThan(0)
  );
}

describe('countries', () => {
  it('lists the 27 member states by name with their evidence counts', async () => {
    await renderWithEdition(<Countries />);
    await waitFor(() => expect(screen.getByText('27 member states')).toBeTruthy());
    // FlatList renders a window, not all 27 rows: assert the first rows in alphabetical order.
    expect(screen.getByText('Austria')).toBeTruthy();
    expect(screen.getByText('Belgium')).toBeTruthy();
    const at = core.index.AT!;
    expect(
      screen.getAllByText(`Holdings verified ${at.holdings_verified} of ${at.holdings_total}`, {
        exact: false,
      }).length
    ).toBeGreaterThan(0);
    await provenanceShown();
  });
});

describe('country report', () => {
  it('shows every section of the German document and its first fact with a source mark', async () => {
    await renderWithEdition(<CountryScreen />);
    await waitFor(() => expect(screen.getByText('Germany')).toBeTruthy());
    const doc = de.documents.DE!;
    for (const s of doc.sections) expect(screen.getAllByText(s.title).length).toBeGreaterThan(0);
    expect(screen.getAllByText('[1]', { exact: false }).length).toBeGreaterThan(0);
    expect(screen.getByText('Sources')).toBeTruthy();
    expect(screen.getByText(de.factcheck.lines.DE!, { exact: false })).toBeTruthy();
    await provenanceShown();
  });
});

describe('infrastructure', () => {
  it('renders the generated overview with its sources', async () => {
    await renderWithEdition(<Infrastructure />);
    await waitFor(() => expect(screen.getByText(core.infrastructure.name)).toBeTruthy());
    expect(screen.getByText('Sources')).toBeTruthy();
    await provenanceShown();
  });
});

describe('ranking', () => {
  it('shows every group by label and no numeral on any state chip', async () => {
    await renderWithEdition(<Sovereignty />);
    await waitFor(() => expect(screen.getByText('Data-sovereignty ranking')).toBeTruthy());
    for (const g of core.sovereignty.groups) expect(screen.getByText(g.label)).toBeTruthy();
    for (const [iso, p] of Object.entries(core.sovereignty.placements)) {
      const chip = screen.getByLabelText(
        `${core.index[iso]!.name}, ${p.confidence} confidence, open its report`
      );
      expect(within(chip).queryAllByText(/\d/)).toEqual([]);
    }
    expect(screen.getByText(core.sovereignty.guardrail)).toBeTruthy();
    await provenanceShown();
  });
});

describe('method and fact check', () => {
  it('renders the methodology document', async () => {
    await renderWithEdition(<Method />);
    await waitFor(() => expect(screen.getByText(core.methodology.sections[0]!.title)).toBeTruthy());
    expect(screen.getByText(core.national_data_note)).toBeTruthy();
    await provenanceShown();
  });

  it('renders the EU appendix with a link per state, and a state appendix', async () => {
    await renderWithEdition(<FactCheckEu />);
    await waitFor(() =>
      expect(screen.getByText(core.factcheck.eu.sections[0]!.title)).toBeTruthy()
    );
    expect(screen.getAllByText('Germany').length).toBeGreaterThan(0);
    await provenanceShown();
    await renderWithEdition(<FactCheckCountry />);
    await waitFor(() => expect(screen.getByText('Fact check: Germany')).toBeTruthy());
    expect(screen.getByText(de.factcheck.countries.DE!.sections[0]!.title)).toBeTruthy();
  });
});

describe('about this edition', () => {
  it('shows the edition id, the disclaimer, and that no channel is configured', async () => {
    await renderWithEdition(<About />);
    await waitFor(() => expect(screen.getByText(BUNDLED_MANIFEST.edition)).toBeTruthy());
    expect(screen.getByText(core.notice.disclaimer)).toBeTruthy();
    expect(screen.getByText(core.generated)).toBeTruthy();
    expect(screen.getByText('Inside the app, as installed')).toBeTruthy();
    expect(screen.getByText('Not checked since launch.')).toBeTruthy();
    expect(
      screen.getByText('Over-the-air app updates are not enabled in this build.')
    ).toBeTruthy();
    expect(screen.getByText('Privacy policy')).toBeTruthy();
    await provenanceShown();
  });

  it('checks for a newer app build only in the same tap as the edition check, then offers a restart (#115)', async () => {
    const { port, calls } = fakeAppUpdates({ available: true });
    await renderWithEdition(<About />, makeStore({ configured: true }).store, port);
    await waitFor(() => expect(screen.getByText(BUNDLED_MANIFEST.edition)).toBeTruthy());
    expect(screen.getByText('App build not checked since launch.')).toBeTruthy();
    expect(calls).toEqual([]);
    fireEvent.press(screen.getByText('Check for a newer edition'));
    await waitFor(() =>
      expect(screen.getByText('A newer app build is downloaded. Restart to use it.')).toBeTruthy()
    );
    expect(calls).toEqual(['check', 'fetch']);
    fireEvent.press(screen.getByText('Restart to apply'));
    await waitFor(() => expect(calls).toEqual(['check', 'fetch', 'reload']));
  });
});
