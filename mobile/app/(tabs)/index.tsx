/** The country list: all 27, filterable, each row carrying the two figures that size the case. */
import { Link } from 'expo-router';
import { useMemo, useState } from 'react';
import { FlatList, StyleSheet, Text, TextInput, useColorScheme, View } from 'react-native';

import { Text as Type, themeFor } from '@/constants/Colors';
import { bundle, search } from '@/data/bundle';
import { eur, mw, num } from '@/data/format';

export default function Countries() {
  const theme = themeFor(useColorScheme());
  const [query, setQuery] = useState('');
  const rows = useMemo(() => search(query), [query]);

  return (
    <View style={[styles.page, { backgroundColor: theme.bgPage }]}>
      <TextInput
        value={query}
        onChangeText={setQuery}
        placeholder="Filter by country or code"
        placeholderTextColor={theme.fgMuted}
        autoCorrect={false}
        accessibilityLabel="Filter countries"
        style={[
          styles.filter,
          { borderColor: theme.border, color: theme.fgPrimary, backgroundColor: theme.bgCard },
        ]}
      />

      <FlatList
        data={rows}
        keyExtractor={c => c.iso2}
        ListHeaderComponent={
          <Text style={[styles.total, { color: theme.fgSecondary }]}>
            {num(bundle.totals.servers)} servers · {bundle.totals.design_mw.toFixed(1)} MW ·{' '}
            {bundle.totals.sites} sites across {Object.keys(bundle.countries).length} member states
          </Text>
        }
        ListEmptyComponent={
          <Text style={[styles.total, { color: theme.fgMuted }]}>No country matches that.</Text>
        }
        renderItem={({ item }) => (
          <Link href={{ pathname: '/country/[iso]', params: { iso: item.iso2 } }} asChild>
            <View
              accessibilityRole="link"
              accessibilityLabel={item.name}
              style={[styles.row, { borderColor: theme.border, backgroundColor: theme.bgCard }]}
            >
              <View style={styles.rowMain}>
                <Text style={[styles.name, { color: theme.fgPrimary }]}>{item.name}</Text>
                <Text style={[styles.meta, { color: theme.fgSecondary }]}>
                  {item.iso2} · {num(item.capacity.total_servers)} servers · {item.capacity.sites}{' '}
                  sites
                </Text>
              </View>
              <View>
                <Text style={[styles.figure, { color: theme.accentText }]}>
                  {mw(item.capacity.design_mw)}
                </Text>
                <Text style={[styles.meta, { color: theme.fgMuted, textAlign: 'right' }]}>
                  {eur(item.capacity.capex_total)}
                </Text>
              </View>
            </View>
          </Link>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  page: { flex: 1, paddingHorizontal: 16 },
  filter: {
    borderWidth: 1,
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 8,
    marginVertical: 12,
    fontSize: Type.body,
  },
  total: { fontSize: Type.axis, marginBottom: 12 },
  row: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderWidth: 1,
    borderRadius: 8,
    padding: 12,
    marginBottom: 8,
  },
  rowMain: { flexShrink: 1, paddingRight: 12 },
  name: { fontSize: Type.heading, fontWeight: '600' },
  meta: { fontSize: Type.axis, marginTop: 2 },
  figure: { fontSize: Type.heading, fontWeight: '600', textAlign: 'right' },
});
