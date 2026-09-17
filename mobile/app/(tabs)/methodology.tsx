/**
 * Methodology: the assumptions the model runs on, its provenance, and the disclaimer.
 *
 * The disclaimer is not decoration. The capacity figures are openly scaled placeholders and the
 * legal entries are unverified assertions about 27 real jurisdictions, which is exactly why the
 * site is not indexed (`VERIFICATION.md`, `DECISIONS.md` #25). A reader that dropped the caveat
 * would be the one place those figures appear as though they were checked.
 */
import { ScrollView, StyleSheet, Text, useColorScheme, View } from 'react-native';

import { Text as Type, themeFor } from '@/constants/Colors';
import { bundle } from '@/data/bundle';

export default function Methodology() {
  const theme = themeFor(useColorScheme());

  return (
    <ScrollView style={{ backgroundColor: theme.bgPage }} contentContainerStyle={styles.page}>
      <View style={[styles.notice, { borderColor: theme.accent, backgroundColor: theme.bgEmphasis }]}>
        <Text style={[styles.noticeTitle, { color: theme.fgPrimary }]}>Not yet verified</Text>
        <Text style={[styles.body, { color: theme.fgSecondary }]}>
          The capacity figures are openly scaled placeholders. The legal and regulatory entries are
          assertions about what 27 real jurisdictions require, researched from public policy
          documents by one person and not yet checked against primary sources. Treat every figure
          here as a planning hypothesis, not a finding.
        </Text>
      </View>

      <Text style={[styles.heading, { color: theme.fgPrimary }]}>Provenance</Text>
      <Text style={[styles.body, { color: theme.fgSecondary }]}>{bundle.provenance}</Text>
      <Text style={[styles.meta, { color: theme.fgMuted }]}>
        Bundle schema {bundle.schema_version}, generated {bundle.generated}.
      </Text>

      <Text style={[styles.heading, { color: theme.fgPrimary }]}>Assumptions</Text>
      {bundle.assumptions.map((a, i) => {
        const [first, ...rest] = Object.values(a);
        return (
          <View key={i} style={[styles.assumption, { borderColor: theme.border }]}>
            <Text style={[styles.assumptionKey, { color: theme.fgPrimary }]}>{first}</Text>
            <Text style={[styles.body, { color: theme.fgSecondary }]}>{rest.join(' · ')}</Text>
          </View>
        );
      })}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  page: { padding: 16, paddingBottom: 48 },
  notice: { borderWidth: 1, borderRadius: 8, padding: 12, marginBottom: 20 },
  noticeTitle: { fontSize: Type.heading, fontWeight: '600', marginBottom: 4 },
  heading: { fontSize: Type.heading, fontWeight: '600', marginTop: 20, marginBottom: 6 },
  body: { fontSize: Type.body, lineHeight: 20 },
  meta: { fontSize: Type.axis, marginTop: 6 },
  assumption: { borderTopWidth: 1, paddingVertical: 8 },
  assumptionKey: { fontSize: Type.body, fontWeight: '600', marginBottom: 2 },
});
