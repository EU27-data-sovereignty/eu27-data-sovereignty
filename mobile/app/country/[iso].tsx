/**
 * One member state, analysed on its own fundamentals (#72). The body is the content model, the same document
 * as /report/<ISO>.pdf, countries/<ISO>/GOAL.md and the site's country page, so the sections, facts and gaps
 * are identical; only the presentation differs. The state's part of the edition is loaded on demand.
 */
import { Link, Stack, useLocalSearchParams } from 'expo-router';
import { useRef } from 'react';
import { Linking, Pressable, type ScrollViewInstance, StyleSheet, Text, View } from 'react-native';

import { DocumentView } from '@/components/DocumentView';
import { Heading, Loading, Screen } from '@/components/Screen';
import { SourceList } from '@/components/SourceList';
import { SPACE, Type, useTheme } from '@/components/theme';
import { submitLink } from '@/data/contribute';
import { bundleView } from '@/data/parts';
import { factCheckPath } from '@/data/routes';
import { claimsBySource, coverage, factCounts, numberSources } from '@/data/sources';
import { useCountry, useEdition } from '@/edition/EditionContext';
import { stateLanguage } from '@/i18n/catalogue';
import { useLanguage } from '@/i18n/LanguageContext';

export default function CountryScreen() {
  const theme = useTheme();
  const { iso = '' } = useLocalSearchParams<{ iso: string }>();
  const code = String(iso).toUpperCase();
  const { core } = useEdition();
  const { t, tx, lang, catalogue, choose } = useLanguage();
  const { part, error } = useCountry(code);
  const scroll = useRef<ScrollViewInstance>(null);
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
  const own = stateLanguage(catalogue, code);
  const jump = (sid: string) => {
    const y = positions.current.get(sid);
    if (y !== undefined) scroll.current?.scrollTo({ y: sourcesTop.current + y, animated: true });
  };

  return (
    <Screen ref={scroll}>
      <Stack.Screen options={{ title: tx(doc.name) }} />
      <Heading kicker={t('app.country.kicker', { iso: doc.iso })} title={tx(doc.name)} />
      {own && own !== lang ? (
        <Pressable
          accessibilityRole="button"
          onPress={() => void choose(own, code)}
          style={[styles.readIn, { borderColor: theme.accent }]}
        >
          <Text style={{ color: theme.accentText, fontWeight: '600' }}>
            {t('app.language.read_in', { language: catalogue.languages[own]?.name ?? own })}
          </Text>
        </Pressable>
      ) : null}
      <Text style={[styles.summary, { color: theme.fgSecondary }]}>
        {t('app.country.summary', { verified: cov.verified, total: cov.total, facts, gaps })}
      </Text>
      <View style={[styles.contribute, { borderColor: theme.border }]}>
        <Text style={[styles.small, { color: theme.fgPrimary }]}>
          {t('app.country.contribute', { gaps })}{' '}
          <Text
            accessibilityRole="link"
            onPress={() => Linking.openURL(submitLink(bundle, code))}
            style={[styles.link, { color: theme.accentText }]}
          >
            {t('app.country.submit')}
          </Text>
          . {t('app.country.check_hint')}
        </Text>
      </View>
      <DocumentView doc={doc} bundle={bundle} numbers={numbers} onSource={jump} />
      <Text style={[styles.small, { color: theme.fgPrimary }]}>
        {bundle.factcheck.lines[code]}{' '}
        <Link href={factCheckPath(code)} style={[styles.link, { color: theme.accentText }]}>
          {t('app.country.factcheck', { name: tx(doc.name) })}
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
  readIn: {
    alignSelf: 'flex-start',
    borderWidth: 1,
    borderRadius: 6,
    paddingVertical: 8,
    paddingHorizontal: 14,
    marginBottom: SPACE.md,
  },
  link: { textDecorationLine: 'underline' },
});
