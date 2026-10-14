/**
 * How every printed fact was checked by the model that did not write it (#87): the EU-27 appendix, rendered
 * from the generated document the PDFs and briefs carry; nothing is written here. Each state's own appendix
 * is one tap away.
 */
import { Link } from 'expo-router';
import { StyleSheet, Text, View } from 'react-native';

import { DocumentView } from '@/components/DocumentView';
import { Heading, Loading, Screen } from '@/components/Screen';
import { SPACE, Type, useTheme } from '@/components/theme';
import { bundleView, indexRows } from '@/data/parts';
import { factCheckPath } from '@/data/routes';
import { useEdition } from '@/edition/EditionContext';

export default function FactCheckEu() {
  const theme = useTheme();
  const { core, loadError } = useEdition();
  if (!core) return <Loading error={loadError} />;
  const bundle = bundleView(core);
  return (
    <Screen>
      <Heading kicker="EU-27 · Cross-model check" title="Fact check" />
      <DocumentView doc={core.factcheck.eu} bundle={bundle} numbers={new Map()} />
      <Text accessibilityRole="header" style={[styles.heading, { color: theme.fgPrimary }]}>
        By member state
      </Text>
      <View style={styles.links}>
        {indexRows(core).map((r) => (
          <Link
            key={r.iso}
            href={factCheckPath(r.iso)}
            style={[styles.link, { color: theme.accentText }]}
          >
            {r.name}
          </Link>
        ))}
      </View>
    </Screen>
  );
}

const styles = StyleSheet.create({
  heading: {
    fontSize: Type.heading,
    fontWeight: '700',
    marginTop: SPACE.md,
    marginBottom: SPACE.sm,
  },
  links: { flexDirection: 'row', flexWrap: 'wrap', gap: SPACE.md },
  link: { fontSize: Type.body, textDecorationLine: 'underline', paddingVertical: 4 },
});
