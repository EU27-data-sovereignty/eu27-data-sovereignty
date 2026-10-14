/**
 * All 27 member states, filterable, from the edition's index: the same counts the web's Countries page
 * derives, computed by the model (#110). Each row reports evidence, not judgement: how much of a state's
 * inventory has a verified source, and how many values are withheld. Opening a row loads that state's part.
 */
import { Link } from 'expo-router';
import { useMemo, useState } from 'react';
import { FlatList, StyleSheet, Text, TextInput, View } from 'react-native';

import { Heading, Loading, ScreenFooter } from '@/components/Screen';
import { SPACE, Type, useTheme } from '@/components/theme';
import { flagEmoji } from '@/data/format';
import { indexRows } from '@/data/parts';
import { countryPath } from '@/data/routes';
import { useEdition } from '@/edition/EditionContext';

export default function Countries() {
  const theme = useTheme();
  const { core, loadError } = useEdition();
  const [query, setQuery] = useState('');
  const rows = useMemo(() => {
    if (!core) return [];
    const q = query.trim().toLowerCase();
    return indexRows(core).filter(
      (r) => !q || r.name.toLowerCase().includes(q) || r.iso.toLowerCase() === q
    );
  }, [core, query]);

  if (!core) return <Loading error={loadError} />;
  return (
    <FlatList
      style={{ backgroundColor: theme.bgPage }}
      contentContainerStyle={styles.pad}
      data={rows}
      keyExtractor={(r) => r.iso}
      ListHeaderComponent={
        <View>
          <Heading kicker="EU-27 · Member states" title="Countries" />
          <Text style={[styles.intro, { color: theme.fgSecondary }]}>
            Each member state analysed on its own fundamentals. The rows count verified evidence;
            they are not a ranking of how sovereign a state is.
          </Text>
          <TextInput
            accessibilityLabel="Find a country"
            placeholder="Find a country"
            placeholderTextColor={theme.fgMuted}
            value={query}
            onChangeText={setQuery}
            autoCorrect={false}
            style={[
              styles.field,
              { borderColor: theme.border, color: theme.fgPrimary, backgroundColor: theme.bgCard },
            ]}
          />
          <Text style={[styles.count, { color: theme.fgMuted }]}>
            {rows.length === 27 ? '27 member states' : `${rows.length} of 27 member states`}
          </Text>
        </View>
      }
      ListEmptyComponent={
        <Text style={{ color: theme.fgMuted }}>No member state matches that name.</Text>
      }
      ListFooterComponent={<ScreenFooter />}
      renderItem={({ item: r }) => (
        <Link href={countryPath(r.iso)} asChild>
          <View
            accessibilityRole="button"
            accessibilityLabel={`${r.name}, country report`}
            style={[styles.card, { borderColor: theme.border, backgroundColor: theme.bgCard }]}
          >
            <View style={styles.row}>
              <Text style={styles.flag} accessibilityElementsHidden importantForAccessibility="no">
                {flagEmoji(r.iso)}
              </Text>
              <Text style={[styles.name, { color: theme.fgPrimary }]}>{r.name}</Text>
              <Text style={[styles.iso, { color: theme.fgMuted }]}>{r.iso}</Text>
            </View>
            <Text style={[styles.line, { color: theme.fgSecondary }]}>
              Holdings verified {r.holdings_verified} of {r.holdings_total} · Tier 0{' '}
              {r.tier0_verified} of {r.tier0_total} · Sourced facts {r.facts}
            </Text>
            <Text style={[styles.line, { color: theme.fgMuted }]}>
              {r.withheld ? `${r.withheld} withheld as disputed` : 'Nothing withheld as disputed'}
            </Text>
          </View>
        </Link>
      )}
    />
  );
}

const styles = StyleSheet.create({
  pad: { padding: SPACE.lg },
  intro: { fontSize: Type.body, lineHeight: 21, marginBottom: SPACE.md },
  field: {
    borderWidth: 1,
    borderRadius: 6,
    paddingHorizontal: SPACE.md,
    paddingVertical: 10,
    fontSize: 16,
  },
  count: { fontSize: Type.axis, marginVertical: SPACE.sm },
  card: {
    borderWidth: StyleSheet.hairlineWidth,
    borderRadius: 6,
    padding: SPACE.md,
    marginBottom: SPACE.sm,
  },
  row: { flexDirection: 'row', alignItems: 'baseline', gap: SPACE.sm, marginBottom: SPACE.xs },
  flag: { fontSize: 18 },
  name: { flex: 1, fontSize: Type.heading, fontWeight: '700' },
  iso: { fontSize: Type.axis, fontWeight: '700', letterSpacing: 1 },
  line: { fontSize: Type.axis + 1, lineHeight: 17 },
});
