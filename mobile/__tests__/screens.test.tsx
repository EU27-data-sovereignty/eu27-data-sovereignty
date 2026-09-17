/**
 * Render smoke tests: the screens put the model's real figures on the screen.
 *
 * Asserting concrete numbers rather than "renders without crashing" is the point, and it is what
 * `web/e2e/app.spec.ts` does for the site: a screen that renders an empty list, or one wired to a
 * placeholder, passes any test that only checks for absence of an exception.
 */
import { render, screen } from '@testing-library/react-native';
import React from 'react';

import Countries from '../app/(tabs)/index';
import CountryScreen from '../app/country/[iso]';
import { bundle } from '../src/data/bundle';

jest.mock('expo-router', () => {
  const { Text } = require('react-native');
  return {
    Link: ({ children }: { children: React.ReactNode }) => children,
    Stack: { Screen: () => null },
    useRouter: () => ({ setParams: jest.fn(), push: jest.fn() }),
    useLocalSearchParams: () => ({ iso: 'NL' }),
    Tabs: Object.assign(({ children }: { children: React.ReactNode }) => children, {
      Screen: () => <Text>tab</Text>,
    }),
  };
});

describe('country list', () => {
  it('lists all 27 member states with the model totals', async () => {
    await render(<Countries />);
    // FlatList renders a window, not all 27 rows, so assert on the header total plus the first
    // rows in alphabetical order rather than on a country that starts life off-screen.
    expect(screen.getByText(/27 member states/)).toBeTruthy();
    expect(screen.getByText('Austria')).toBeTruthy();
    expect(screen.getAllByText(/servers/).length).toBeGreaterThan(5);
  });
});

describe('country screen', () => {
  it('renders the Dutch reference case as the model has it', async () => {
    const nl = bundle.countries.NL;
    await render(<CountryScreen />);

    // The NL case is the hand-built reference the other 26 are derived from; these two figures
    // are the ones the briefing leads with, and they come from the Dutch xlsx.
    expect(nl.capacity.total_servers).toBe(5691);
    expect(screen.getByText(/5,691/)).toBeTruthy();
    expect(screen.getByText(`${nl.capacity.design_mw.toFixed(1)} MW`)).toBeTruthy();
  });

  it('shows every section heading', async () => {
    await render(<CountryScreen />);
    for (const title of [
      'Starting point',
      'What is structurally different',
      'Capacity',
      'Proposed geography',
      'Legal and regulatory posture',
      'Current state and provider landscape',
      'Migration path and cost',
      'Sovereignty matrix',
      'Geography and threat notes',
    ]) {
      // The heading is one Text with a nested Text for the number, so the string is split.
      expect(screen.getByText(new RegExp(title))).toBeTruthy();
    }
  });
});
