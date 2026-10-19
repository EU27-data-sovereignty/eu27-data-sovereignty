/**
 * The data-sovereignty ranking (#77): groups by a published rule, never a score. Each state’s confidence is
 * the range of groups its open evidence could still move it to, drawn as a bar; each group's rule is taken
 * from the methodology's own words, as on the web. Tapping a state opens its report, whose Placement section
 * says what could move it. No number appears on any chip (tests/test_sovereignty.py).
 */
import { Link } from 'expo-router';
import { useMemo } from 'react';
import { StyleSheet, Text, View } from 'react-native';

import { RangeBar, groupFill } from '@/components/RangeBar';
import { Heading, Loading, Screen } from '@/components/Screen';
import { SPACE, Type, useTheme } from '@/components/theme';
import { countryPath } from '@/data/routes';
import { useEdition } from '@/edition/EditionContext';
import { useLanguage } from '@/i18n/LanguageContext';

export default function Sovereignty() {
  const theme = useTheme();
  const { core, loadError } = useEdition();
  const { t, tx } = useLanguage();
  const rule = useMemo(() => {
    const out: Record<string, string> = {};
    if (!core) return out;
    for (const sec of core.methodology.sections)
      for (const b of sec.blocks)
        if (b.type === 'list')
          for (const item of b.items) {
            const text = item.map((x) => x.t).join(' ');
            const g = core.sovereignty.groups.find((x) => text.startsWith(`${x.label}: `));
            if (g) out[g.id] = text.slice(g.label.length + 2);
          }
    return out;
  }, [core]);
  if (!core) return <Loading error={loadError} />;
  const sov = core.sovereignty;
  const fill = groupFill(theme);
  const order = sov.groups.map((g) => g.id);
  const name = (iso: string) => tx(core.index[iso]?.name ?? iso);
  return (
    <Screen>
      <Heading kicker={t('app.ranking.kicker')} title={t('app.ranking.title')} />
      <View
        style={[
          styles.callout,
          { borderLeftColor: theme.accentText, backgroundColor: theme.bgEmphasis },
        ]}
      >
        <Text style={[styles.small, { color: theme.fgPrimary }]}>{sov.guardrail}</Text>
      </View>
      <Text style={[styles.small, styles.intro, { color: theme.fgSecondary }]}>
        {t('app.ranking.intro')}
      </Text>
      {sov.groups.map((g) => {
        const members = Object.entries(sov.placements)
          .filter(([, p]) => p.group === g.id)
          .sort((a, b) => name(a[0]).localeCompare(name(b[0])));
        return (
          <View
            key={g.id}
            style={[styles.group, { borderColor: theme.border, backgroundColor: theme.bgCard }]}
          >
            <View style={[styles.stripe, { backgroundColor: fill[g.id] }]} />
            <Text
              accessibilityRole="header"
              style={[styles.groupTitle, { color: theme.fgPrimary }]}
            >
              {g.label}
            </Text>
            {rule[g.id] ? (
              <Text style={[styles.rule, { color: theme.fgMuted }]}>{rule[g.id]}</Text>
            ) : null}
            <View style={styles.chips}>
              {members.map(([iso, p]) => (
                <Link key={iso} href={countryPath(iso)} asChild>
                  <View
                    accessibilityRole="button"
                    accessibilityLabel={t('app.ranking.chip', {
                      name: name(iso),
                      confidence: p.confidence,
                    })}
                    style={[
                      styles.chip,
                      { borderColor: theme.border, backgroundColor: theme.bgEmphasis },
                    ]}
                  >
                    <Text style={[styles.chipText, { color: theme.fgPrimary }]}>{name(iso)}</Text>
                    <Text style={[styles.chipText, { color: theme.fgMuted }]}>{p.confidence}</Text>
                    <RangeBar p={p} order={order} />
                  </View>
                </Link>
              ))}
              {members.length === 0 ? (
                <Text style={[styles.rule, { color: theme.fgMuted, fontStyle: 'italic' }]}>
                  {t('app.ranking.none')}
                </Text>
              ) : null}
            </View>
          </View>
        );
      })}
      <Text accessibilityRole="header" style={[styles.heading, { color: theme.accentText }]}>
        {t('app.ranking.indicators')}
      </Text>
      {sov.indicators.map((ind) => (
        <View key={ind.id} style={styles.indicator}>
          <Text style={[styles.small, { color: theme.fgPrimary, fontWeight: '600' }]}>
            {ind.id} · {ind.label}
          </Text>
          <Text style={[styles.small, { color: theme.fgSecondary }]}>{ind.question}</Text>
        </View>
      ))}
      <Text style={[styles.small, { color: theme.fgSecondary, marginTop: SPACE.md }]}>
        {t('app.ranking.findings')}{' '}
        <Text style={{ color: theme.fgMuted, fontStyle: 'italic' }}>{tx('Not yet sourced')}</Text>:{' '}
        {t('app.ranking.gap')}{' '}
        <Text
          style={{
            color: theme.fgMuted,
            fontStyle: 'italic',
            textDecorationLine: 'underline',
            textDecorationStyle: 'dashed',
          }}
        >
          {t('app.ranking.disputed_word')}
        </Text>
        : {t('app.ranking.disputed')}
      </Text>
    </Screen>
  );
}

const styles = StyleSheet.create({
  small: { fontSize: Type.body - 1, lineHeight: 19 },
  intro: { marginBottom: SPACE.lg },
  callout: { borderLeftWidth: 4, borderRadius: 4, padding: SPACE.md, marginBottom: SPACE.md },
  group: {
    borderWidth: StyleSheet.hairlineWidth,
    borderRadius: 6,
    padding: SPACE.md,
    paddingLeft: SPACE.lg,
    marginBottom: SPACE.md,
    overflow: 'hidden',
  },
  stripe: { position: 'absolute', left: 0, top: 0, bottom: 0, width: 4 },
  groupTitle: { fontSize: Type.heading, fontWeight: '700', marginBottom: SPACE.xs },
  rule: { fontSize: Type.axis + 1, lineHeight: 17, marginBottom: SPACE.sm },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: 6 },
  chip: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    borderWidth: 1,
    borderRadius: 6,
    paddingHorizontal: 8,
    paddingVertical: 6,
  },
  chipText: { fontSize: Type.axis + 1 },
  heading: {
    fontSize: Type.heading,
    fontWeight: '700',
    marginTop: SPACE.lg,
    marginBottom: SPACE.sm,
  },
  indicator: { marginBottom: SPACE.sm },
});
