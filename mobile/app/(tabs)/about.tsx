/**
 * This edition: its id (the sha256 of the bundle it was split from), when it was generated, where it came
 * from, what it counts, what the project can honestly say about its evidence, and the one control that
 * reaches the network: a check for a newer edition (#110, #111), which in the same tap also asks for a
 * newer build of the app itself (#115). Every sentence about evidence comes from the edition's `notice`;
 * the privacy sentences are the app’s own and say exactly what one check sends, and to whom. The privacy
 * policy the stores require is linked from here (#116). The reader chooses the app's language here, from the
 * languages the catalogue has admitted, and sees who drafted, reviewed and read the one on screen (#117).
 */
import Constants from 'expo-constants';
import { Linking, Pressable, StyleSheet, Switch, Text, View } from 'react-native';

import { Heading, Loading, Screen } from '@/components/Screen';
import { SPACE, Type, useTheme } from '@/components/theme';
import { useEdition } from '@/edition/EditionContext';
import type { UpdateState } from '@/edition/EditionStore';
import type { Translator } from '@/i18n/catalogue';
import { useLanguage } from '@/i18n/LanguageContext';
import { privacyUrl } from '@/services/site';
import { describeAppUpdate } from '@/update/appUpdate';

function describe(update: UpdateState, t: Translator['t']): string {
  switch (update.kind) {
    case 'idle':
    case 'unconfigured':
    case 'checking':
    case 'unreachable':
      return t(`app.update.${update.kind}`);
    case 'up-to-date':
      return t('app.update.up_to_date');
    case 'downloading':
      return t('app.update.downloading', {
        name: update.name,
        done: update.done + 1,
        total: update.total,
      });
    case 'ready':
      return t('app.update.ready', { edition: update.edition.slice(0, 16) });
    case 'rejected':
      return t('app.update.rejected', { reason: update.reason });
  }
}

export default function About() {
  const theme = useTheme();
  const {
    core,
    loadError,
    edition,
    update,
    checkForUpdate,
    switchToInstalled,
    appUpdate,
    build,
    restartToApply,
    autoCheck,
    setAutoCheck,
    integrityNotice,
  } = useEdition();
  const { t, tx, lang, languages, provenance, choose, catalogue } = useLanguage();
  if (!core) return <Loading error={loadError} />;
  const totals = Object.values(core.index).reduce(
    (t, e) => ({ facts: t.facts + e.facts, withheld: t.withheld + e.withheld }),
    { facts: 0, withheld: 0 }
  );
  const busy =
    update.kind === 'checking' ||
    update.kind === 'downloading' ||
    appUpdate.kind === 'checking' ||
    appUpdate.kind === 'downloading';
  const privacy = privacyUrl();
  const row = (label: string, value: string, mono = false) => (
    <View style={styles.row} key={label}>
      <Text style={[styles.label, { color: theme.fgMuted }]}>{label}</Text>
      <Text selectable style={[styles.value, mono && styles.mono, { color: theme.fgPrimary }]}>
        {value}
      </Text>
    </View>
  );
  return (
    <Screen>
      <Heading kicker={t('app.about.kicker')} title={t('app.about.title')} />
      {integrityNotice ? (
        <View
          style={[
            styles.callout,
            { borderLeftColor: theme.rank5, backgroundColor: theme.bgEmphasis },
          ]}
        >
          <Text style={[styles.small, { color: theme.fgPrimary }]}>{integrityNotice}</Text>
        </View>
      ) : null}
      {row(t('app.about.edition'), edition.id, true)}
      {row(t('app.about.generated'), core.generated)}
      {row(t('app.about.schema'), String(core.schema_version))}
      {row(
        t('app.about.source'),
        edition.source === 'bundled'
          ? t('app.about.source_bundled')
          : [
              t('app.about.source_downloaded'),
              edition.published
                ? t('app.about.published', { date: edition.published.published_at })
                : '',
              edition.published?.commit
                ? t('app.about.commit', { commit: edition.published.commit.slice(0, 7) })
                : '',
            ]
              .filter(Boolean)
              .join(' · ')
      )}
      {row(t('app.about.facts'), t('app.about.facts_value', { n: totals.facts }))}
      {row(t('app.about.withheld'), String(totals.withheld))}
      {row(
        t('app.about.app'),
        `${Constants.expoConfig?.name ?? ''} ${Constants.expoConfig?.version ?? ''}`.trim()
      )}
      {row(
        t('app.about.build'),
        build.updateId
          ? `${t('app.about.build_update', {
              id: build.updateId.slice(0, 8),
              runtime: build.runtimeVersion ?? '?',
            })}${build.channel ? ` (${build.channel})` : ''}`
          : [
              t('app.about.build_installed'),
              build.runtimeVersion
                ? t('app.about.build_runtime', { runtime: build.runtimeVersion })
                : '',
            ]
              .filter(Boolean)
              .join(', ')
      )}

      <Text accessibilityRole="header" style={[styles.heading, { color: theme.fgPrimary }]}>
        {t('app.about.evidence')}
      </Text>
      <Text style={[styles.small, { color: theme.fgPrimary }]}>{tx(core.notice.disclaimer)}</Text>
      <Text style={[styles.small, { color: theme.fgSecondary, marginTop: SPACE.sm }]}>
        {core.notice.withheld}
      </Text>
      <Text style={[styles.small, { color: theme.fgSecondary, marginTop: SPACE.sm }]}>
        {core.notice.grade_rule}
      </Text>
      {core.notice.checks.map((c) => (
        <View key={c.name} style={styles.check}>
          <Text style={[styles.small, { color: theme.fgPrimary, fontWeight: '600' }]}>
            {c.name}
          </Text>
          <Text style={[styles.small, { color: theme.fgSecondary }]}>{c.what}</Text>
        </View>
      ))}

      <Text accessibilityRole="header" style={[styles.heading, { color: theme.fgPrimary }]}>
        {t('app.about.newer')}
      </Text>
      <Text style={[styles.small, { color: theme.fgSecondary }]}>{describe(update, t)}</Text>
      <Text style={[styles.small, { color: theme.fgSecondary, marginTop: SPACE.xs }]}>
        {describeAppUpdate(appUpdate, t)}
      </Text>
      <View style={styles.actions}>
        <Pressable
          accessibilityRole="button"
          disabled={busy || update.kind === 'unconfigured'}
          onPress={() => void checkForUpdate()}
          style={[styles.button, { backgroundColor: theme.accent, opacity: busy ? 0.6 : 1 }]}
        >
          <Text style={{ color: theme.fgOnAccent, fontWeight: '600' }}>{t('app.about.check')}</Text>
        </Pressable>
        {update.kind === 'ready' ? (
          <Pressable
            accessibilityRole="button"
            onPress={() => void switchToInstalled()}
            style={[styles.button, { borderWidth: 1, borderColor: theme.accent }]}
          >
            <Text style={{ color: theme.accentText, fontWeight: '600' }}>
              {t('app.about.use_now')}
            </Text>
          </Pressable>
        ) : null}
        {appUpdate.kind === 'ready' ? (
          <Pressable
            accessibilityRole="button"
            onPress={() => void restartToApply()}
            style={[styles.button, { borderWidth: 1, borderColor: theme.accent }]}
          >
            <Text style={{ color: theme.accentText, fontWeight: '600' }}>
              {t('app.about.restart')}
            </Text>
          </Pressable>
        ) : null}
      </View>
      <View style={styles.toggle}>
        <Text style={[styles.small, { color: theme.fgPrimary, flex: 1 }]}>
          {t('app.about.auto')}
        </Text>
        <Switch
          accessibilityLabel={t('app.about.auto')}
          value={autoCheck}
          onValueChange={(on) => void setAutoCheck(on)}
          disabled={update.kind === 'unconfigured'}
        />
      </View>
      <Text style={[styles.small, { color: theme.fgMuted, marginTop: SPACE.sm }]}>
        {t('app.about.privacy_note')}
      </Text>
      {privacy ? (
        <Pressable
          accessibilityRole="link"
          onPress={() => void Linking.openURL(privacy)}
          style={styles.link}
        >
          <Text
            style={[styles.small, { color: theme.accentText, textDecorationLine: 'underline' }]}
          >
            {t('app.about.privacy')}
          </Text>
        </Pressable>
      ) : null}

      <Text accessibilityRole="header" style={[styles.heading, { color: theme.fgPrimary }]}>
        {t('app.language.heading')}
      </Text>
      <View style={styles.actions} accessibilityRole="radiogroup">
        {languages.map((l) => (
          <Pressable
            key={l.lang}
            accessibilityRole="radio"
            accessibilityState={{ checked: l.lang === lang }}
            onPress={() => void choose(l.lang)}
            style={[
              styles.button,
              { borderWidth: 1, borderColor: theme.accent },
              l.lang === lang && { backgroundColor: theme.accent },
            ]}
          >
            <Text
              style={{
                color: l.lang === lang ? theme.fgOnAccent : theme.accentText,
                fontWeight: '600',
              }}
            >
              {l.name}
            </Text>
          </Pressable>
        ))}
      </View>
      <Text style={[styles.small, { color: theme.fgSecondary, marginTop: SPACE.sm }]}>
        {t('app.language.scope')}
      </Text>
      {provenance.map((p) => (
        <Text key={p.iso} style={[styles.small, { color: theme.fgMuted, marginTop: SPACE.xs }]}>
          {p.tag}:{' '}
          {t('app.language.provenance', {
            drafted: p.drafted ?? '',
            reviewed: p.reviewed ?? '',
            read: p.read ?? '',
          })}
        </Text>
      ))}
      {Object.values(catalogue.states).some((ls) => ls.some((l) => !catalogue.languages[l])) ? (
        <Text style={[styles.small, { color: theme.fgMuted, marginTop: SPACE.sm }]}>
          {t('app.language.pending')}
        </Text>
      ) : null}
    </Screen>
  );
}

const styles = StyleSheet.create({
  row: { marginBottom: SPACE.md },
  label: { fontSize: Type.axis, fontWeight: '600', letterSpacing: 0.6, textTransform: 'uppercase' },
  value: { fontSize: Type.body, lineHeight: 20, marginTop: 2 },
  mono: { fontFamily: 'Menlo', fontSize: Type.axis + 1 },
  heading: {
    fontSize: Type.heading,
    fontWeight: '700',
    marginTop: SPACE.lg,
    marginBottom: SPACE.sm,
  },
  small: { fontSize: Type.body - 1, lineHeight: 19 },
  check: { marginTop: SPACE.sm },
  callout: { borderLeftWidth: 4, borderRadius: 4, padding: SPACE.md, marginBottom: SPACE.md },
  actions: { flexDirection: 'row', flexWrap: 'wrap', gap: SPACE.sm, marginTop: SPACE.md },
  button: { paddingVertical: 10, paddingHorizontal: 16, borderRadius: 6 },
  toggle: { flexDirection: 'row', alignItems: 'center', gap: SPACE.md, marginTop: SPACE.md },
  link: { marginTop: SPACE.md, alignSelf: 'flex-start' },
});
