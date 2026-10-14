/**
 * One member state's fact-check appendix (#87), from its part of the edition: the generated document the
 * PDF and the brief carry. Nothing is written here.
 */
import { Link, Stack, useLocalSearchParams } from 'expo-router';
import { StyleSheet, Text } from 'react-native';

import { DocumentView } from '@/components/DocumentView';
import { Heading, Loading, Screen } from '@/components/Screen';
import { SPACE, Type, useTheme } from '@/components/theme';
import { bundleView } from '@/data/parts';
import { countryPath, factCheckPath } from '@/data/routes';
import { useCountry, useEdition } from '@/edition/EditionContext';

export default function FactCheckCountry() {
  const theme = useTheme();
  const { iso = '' } = useLocalSearchParams<{ iso: string }>();
  const code = String(iso).toUpperCase();
  const { core } = useEdition();
  const { part, error } = useCountry(code);
  if (!core || !part) return <Loading error={error} />;
  const bundle = bundleView(core, part);
  const doc = bundle.factcheck.countries[code];
  const name = bundle.documents[code]?.name;
  if (!doc || !name) return <Loading error={`no fact-check appendix for ${code}`} />;
  return (
    <Screen>
      <Stack.Screen options={{ title: `Fact check: ${name}` }} />
      <Heading kicker={`EU-27 · Cross-model check · ${code}`} title={`Fact check: ${name}`} />
      <Text style={[styles.small, { color: theme.fgSecondary, marginBottom: SPACE.lg }]}>
        <Link href={countryPath(code)} style={[styles.link, { color: theme.accentText }]}>
          Back to {name}
        </Link>
        {' · '}
        <Link href={factCheckPath()} style={[styles.link, { color: theme.accentText }]}>
          All member states
        </Link>
      </Text>
      <DocumentView doc={doc} bundle={bundle} numbers={new Map()} />
    </Screen>
  );
}

const styles = StyleSheet.create({
  small: { fontSize: Type.body - 1, lineHeight: 19 },
  link: { textDecorationLine: 'underline' },
});
