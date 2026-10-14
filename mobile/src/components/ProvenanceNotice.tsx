/**
 * Shown on every screen, as `web/src/components/ProvenanceNotice.tsx` shows it on every page. The wording
 * comes from the edition (`notice`, `provenance` in eu27.core.json), so the app, the site, the PDFs and the
 * briefs hedge identically (#6, #82): nothing here claims a check that did not run.
 */
import { Link } from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

import { factCheckPath } from '@/data/routes';
import { SPACE, Type, useTheme } from './theme';

export function ProvenanceNotice({
  generated,
  provenance,
}: {
  generated: string;
  provenance: string;
}) {
  const theme = useTheme();
  return (
    <View style={[styles.box, { borderTopColor: theme.border }]} accessibilityRole="summary">
      <Text style={[styles.text, { color: theme.fgSecondary }]}>
        {provenance} Generated {generated}.{' '}
        <Link href="/method" style={[styles.link, { color: theme.accentText }]}>
          How this was built
        </Link>
        {' · '}
        <Link href={factCheckPath()} style={[styles.link, { color: theme.accentText }]}>
          How every fact was checked
        </Link>
        .
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  box: {
    borderTopWidth: StyleSheet.hairlineWidth,
    marginTop: SPACE.xl,
    paddingTop: SPACE.lg,
    paddingBottom: SPACE.xl,
  },
  text: { fontSize: Type.axis + 1, lineHeight: 17 },
  link: { textDecorationLine: 'underline' },
});
