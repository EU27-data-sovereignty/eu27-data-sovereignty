/**
 * The methodology, rendered from the generated document (model/methodology.py) the PDFs carry as their
 * appendix. Nothing is written here: a hand-written method page drifts from the method.
 */
import { Link } from 'expo-router';
import { StyleSheet, Text } from 'react-native';

import { DocumentView } from '@/components/DocumentView';
import { Heading, Loading, Screen } from '@/components/Screen';
import { SPACE, Type, useTheme } from '@/components/theme';
import { bundleView } from '@/data/parts';
import { factCheckPath } from '@/data/routes';
import { useEdition } from '@/edition/EditionContext';

export default function Method() {
  const theme = useTheme();
  const { core, loadError } = useEdition();
  if (!core) return <Loading error={loadError} />;
  const bundle = bundleView(core);
  return (
    <Screen>
      <Heading kicker="EU-27 · How we know" title="Methodology" />
      <Text style={[styles.small, { color: theme.fgSecondary, marginBottom: SPACE.lg }]}>
        How every printed fact was checked by the model that did not write it:{' '}
        <Link href={factCheckPath()} style={[styles.link, { color: theme.accentText }]}>
          the fact-check appendix
        </Link>
        .
      </Text>
      <DocumentView doc={core.methodology} bundle={bundle} numbers={new Map()} />
      <Text style={[styles.small, { color: theme.fgMuted }]}>{core.national_data_note}</Text>
    </Screen>
  );
}

const styles = StyleSheet.create({
  small: { fontSize: Type.body - 1, lineHeight: 19 },
  link: { textDecorationLine: 'underline' },
});
