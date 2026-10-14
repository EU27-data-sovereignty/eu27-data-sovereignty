/**
 * One member state, analysed on its own fundamentals (#72). The body is the content model, the same document
 * as /report/<ISO>.pdf, countries/<ISO>/GOAL.md and the site's country page, so the sections, facts and gaps
 * are identical; only the presentation differs. The state's part of the edition is loaded on demand.
 */
import { Link, Stack, useLocalSearchParams } from 'expo-router';
import { useRef } from 'react';
import { Linking, ScrollView, StyleSheet, Text, View } from 'react-native';

import { DocumentView } from '@/components/DocumentView';
import { Heading, Loading, Screen } from '@/components/Screen';
import { SourceList } from '@/components/SourceList';
import { SPACE, Type, useTheme } from '@/components/theme';
import { submitLink } from '@/data/contribute';
import { bundleView } from '@/data/parts';
import { factCheckPath } from '@/data/routes';
import { claimsBySource, coverage, factCounts, numberSources } from '@/data/sources';
import { useCountry, useEdition } from '@/edition/EditionContext';

export default function CountryScreen() {
  const theme = useTheme();
  const { iso = '' } = useLocalSearchParams<{ iso: string }>();
  const code = String(iso).toUpperCase();
  const { core } = useEdition();
  const { part, error } = useCountry(code);
  const scroll = useRef<ScrollView>(null);
  const sourcesTop = useRef(0);
  const positions = useRef(new Map<string, number>());

  if (!core || !part) return <Loading error={error} />;
  const bundle = bundleView(core, part);
  const doc = bundle.documents[code];
  const country = bundle.countries[code];
  if (!doc || !country) return <Loading error={`no member state ${code} in this edition`} />;

  const numbers = numberSources([doc], bundle);
  const claims = claimsBySource([doc], bundle);
  const cov = coverage(country);
  const { facts, gaps } = factCounts(doc);
  const jump = (sid: string) => {
    const y = positions.current.get(sid);
    if (y !== undefined) scroll.current?.scrollTo({ y: sourcesTop.current + y, animated: true });
  };

  return (
    <Screen ref={scroll}>
      <Stack.Screen options={{ title: doc.name }} />
      <Heading kicker={`EU-27 · Country report · ${doc.iso}`} title={doc.name} />
      <Text style={[styles.summary, { color: theme.fgSecondary }]}>
        {cov.verified} of {cov.total} critical holding classes verified · {facts} sourced facts
        shown · {gaps} values withheld until sourced · capacity not yet sized
      </Text>
      <View style={[styles.contribute, { borderColor: theme.border }]}>
        <Text style={[styles.small, { color: theme.fgPrimary }]}>
          Know a public source for one of the {gaps} withheld values, or a better one for a fact?{' '}
          <Text
            accessibilityRole="link"
            onPress={() => Linking.openURL(submitLink(bundle, code))}
            style={[styles.link, { color: theme.accentText }]}
          >
            Submit a source
          </Text>
          . Every fact also has a <Text style={{ fontStyle: 'italic' }}>Check this fact</Text> link
          in its source entry.
        </Text>
      </View>
      <DocumentView doc={doc} bundle={bundle} numbers={numbers} onSource={jump} />
      <Text style={[styles.small, { color: theme.fgPrimary }]}>
        {bundle.factcheck.lines[code]}{' '}
        <Link href={factCheckPath(code)} style={[styles.link, { color: theme.accentText }]}>
          Fact check for {doc.name}
        </Link>
        .
      </Text>
      <View onLayout={(e) => (sourcesTop.current = e.nativeEvent.layout.y)}>
        <SourceList
          bundle={bundle}
          numbers={numbers}
          claims={claims}
          onLayoutSource={(sid, y) => positions.current.set(sid, y)}
        />
      </View>
    </Screen>
  );
}

const styles = StyleSheet.create({
  summary: { fontSize: Type.body - 1, lineHeight: 19, marginBottom: SPACE.md },
  contribute: {
    borderWidth: StyleSheet.hairlineWidth,
    borderRadius: 6,
    padding: SPACE.md,
    marginBottom: SPACE.xl,
  },
  small: { fontSize: Type.body - 1, lineHeight: 19 },
  link: { textDecorationLine: 'underline' },
});
