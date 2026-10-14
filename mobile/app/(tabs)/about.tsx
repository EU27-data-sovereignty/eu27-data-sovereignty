/**
 * This edition: its id (the sha256 of the bundle it was split from), when it was generated, where it came
 * from, what it counts, what the project can honestly say about its evidence, and the one control that
 * reaches the network: a check for a newer edition (#110, #111). Every sentence about evidence comes from
 * the edition's `notice`; the privacy sentence is the app’s own and says exactly what one check sends.
 */
import Constants from 'expo-constants';
import { Pressable, StyleSheet, Switch, Text, View } from 'react-native';

import { Heading, Loading, Screen } from '@/components/Screen';
import { SPACE, Type, useTheme } from '@/components/theme';
import { useEdition } from '@/edition/EditionContext';
import type { UpdateState } from '@/edition/EditionStore';

function describe(update: UpdateState): string {
  switch (update.kind) {
    case 'idle':
      return 'Not checked since launch.';
    case 'unconfigured':
      return 'This build has no edition channel configured; it reads only the edition inside the app.';
    case 'checking':
      return 'Checking…';
    case 'up-to-date':
      return 'This is the latest published edition.';
    case 'downloading':
      return `Downloading ${update.name} (${update.done + 1} of ${update.total})…`;
    case 'ready':
      return `A newer edition (${update.edition.slice(0, 16)}…) is downloaded and verified.`;
    case 'rejected':
      return `Rejected: ${update.reason}. Nothing of it was kept.`;
    case 'unreachable':
      return 'The edition channel could not be reached. The app keeps the edition it has.';
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
    autoCheck,
    setAutoCheck,
    integrityNotice,
  } = useEdition();
  if (!core) return <Loading error={loadError} />;
  const totals = Object.values(core.index).reduce(
    (t, e) => ({ facts: t.facts + e.facts, withheld: t.withheld + e.withheld }),
    { facts: 0, withheld: 0 }
  );
  const busy = update.kind === 'checking' || update.kind === 'downloading';
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
      <Heading kicker="EU-27 · This edition" title="About this edition" />
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
      {row('Edition (sha256 of the bundle)', edition.id, true)}
      {row('Generated', core.generated)}
      {row('Schema', String(core.schema_version))}
      {row(
        'Source',
        edition.source === 'bundled'
          ? 'Inside the app, as installed'
          : `Downloaded from the edition channel${edition.published ? ` · published ${edition.published.published_at}` : ''}${edition.published?.commit ? ` · commit ${edition.published.commit.slice(0, 7)}` : ''}`
      )}
      {row('Facts shown', `${totals.facts} across 27 member states`)}
      {row('Withheld as disputed', String(totals.withheld))}
      {row(
        'App',
        `${Constants.expoConfig?.name ?? ''} ${Constants.expoConfig?.version ?? ''}`.trim()
      )}

      <Text accessibilityRole="header" style={[styles.heading, { color: theme.fgPrimary }]}>
        What this edition can say about its evidence
      </Text>
      <Text style={[styles.small, { color: theme.fgPrimary }]}>{core.notice.disclaimer}</Text>
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
        Newer editions
      </Text>
      <Text style={[styles.small, { color: theme.fgSecondary }]}>{describe(update)}</Text>
      <View style={styles.actions}>
        <Pressable
          accessibilityRole="button"
          disabled={busy || update.kind === 'unconfigured'}
          onPress={() => void checkForUpdate()}
          style={[styles.button, { backgroundColor: theme.accent, opacity: busy ? 0.6 : 1 }]}
        >
          <Text style={{ color: theme.fgOnAccent, fontWeight: '600' }}>
            Check for a newer edition
          </Text>
        </Pressable>
        {update.kind === 'ready' ? (
          <Pressable
            accessibilityRole="button"
            onPress={() => void switchToInstalled()}
            style={[styles.button, { borderWidth: 1, borderColor: theme.accent }]}
          >
            <Text style={{ color: theme.accentText, fontWeight: '600' }}>Use it now</Text>
          </Pressable>
        ) : null}
      </View>
      <View style={styles.toggle}>
        <Text style={[styles.small, { color: theme.fgPrimary, flex: 1 }]}>
          Check automatically at launch
        </Text>
        <Switch
          accessibilityLabel="Check automatically at launch"
          value={autoCheck}
          onValueChange={(on) => void setAutoCheck(on)}
          disabled={update.kind === 'unconfigured'}
        />
      </View>
      <Text style={[styles.small, { color: theme.fgMuted, marginTop: SPACE.sm }]}>
        A check sends one request for a 200-byte pointer to the project’s edition channel, and up to
        29 more for the files of a newer edition. The host sees the network address, the app’s user
        agent and the time, in its request logs. Nothing identifies the reader; nothing about the
        reader is stored. Every downloaded file is checked against its published hash before a
        single value from it is shown.
      </Text>
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
});
