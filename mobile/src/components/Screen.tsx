/**
 * Every screen's frame: the page background, the content padding, and the provenance notice at the end,
 * which no screen may leave out (tests/test_evidence.py). A list screen uses `ScreenFooter` as its
 * FlatList footer instead; the notice is the same component either way.
 */
import { forwardRef, type ReactNode } from 'react';
import { ScrollView, StyleSheet, Text, View } from 'react-native';

import { useEdition } from '@/edition/EditionContext';
import { ProvenanceNotice } from './ProvenanceNotice';
import { SPACE, Type, useTheme } from './theme';

export function ScreenFooter() {
  const { core } = useEdition();
  if (!core) return null;
  return (
    <View style={styles.pad}>
      <ProvenanceNotice generated={core.generated} provenance={core.provenance} />
    </View>
  );
}

export const Screen = forwardRef<ScrollView, { children: ReactNode }>(function Screen(
  { children },
  ref
) {
  const theme = useTheme();
  return (
    <ScrollView
      ref={ref}
      style={{ backgroundColor: theme.bgPage }}
      contentContainerStyle={styles.pad}
    >
      {children}
      <ScreenFooter />
    </ScrollView>
  );
});

/** What a screen shows while its part of the edition loads, or when it could not be read. */
export function Loading({ error }: { error?: string | null }) {
  const theme = useTheme();
  return (
    <View style={styles.pad}>
      <Text style={{ color: theme.fgMuted, fontSize: Type.body }}>
        {error ? `This part of the edition could not be read: ${error}` : 'Loading the edition…'}
      </Text>
    </View>
  );
}

export function Heading({ kicker, title }: { kicker?: string; title: string }) {
  const theme = useTheme();
  return (
    <View style={{ marginBottom: SPACE.lg }}>
      {kicker ? (
        <Text style={[styles.kicker, { color: theme.accentText }]}>{kicker.toUpperCase()}</Text>
      ) : null}
      <Text accessibilityRole="header" style={[styles.title, { color: theme.fgPrimary }]}>
        {title}
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  pad: { padding: SPACE.lg },
  kicker: { fontSize: Type.axis, fontWeight: '600', letterSpacing: 1.2, marginBottom: SPACE.xs },
  title: { fontSize: Type.title + 4, fontWeight: '700', lineHeight: 32 },
});
