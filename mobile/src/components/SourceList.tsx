/**
 * The numbered sources for a screen, ported from `web/src/components/SourceList.tsx`: each once, with what
 * makes it checkable (URL, archived copy, retrieval date, the document hash where recorded) and under it
 * every claim on this screen that rests on it, with the quote found in the document (#75). `checkKind`,
 * `host` and `claimLabel` are copied from the web file, under this comment, so a change there is a change
 * here in the same commit.
 */
import { Linking, Pressable, StyleSheet, Text, View } from 'react-native';

import { reviewLink } from '@/data/contribute';
import type { Bundle } from '@/data/types';
import { SPACE, Type, useTheme } from './theme';

/** A checklist line's kind, by its own wording: the source tier, a check passed, or a shortfall. */
function checkKind(item: string): 'tier' | 'pass' | 'short' | 'plain' {
  if (/^T\d /.test(item)) return 'tier';
  if (
    /^(no archived copy|quote found \(loose|not in the quote|not independently|secondary source)/.test(
      item
    )
  )
    return 'short';
  if (
    /^(quote found \(exact|archived copy|official source|primary source|blind review|independent review|every figure|value quoted verbatim|dataset value|authoritative statement)/.test(
      item
    )
  )
    return 'pass';
  return 'plain';
}

function host(url: string): string {
  try {
    return new URL(url).hostname.replace(/^www\./, '');
  } catch {
    return '';
  }
}

/** What a claim id names, in words: "Germany · Civil registry core · operator". From the bundle's labels. */
function claimLabel(bundle: Bundle, claim: string): string {
  const [kind, iso = '', id = '', field = ''] = claim.split(':');
  const country = bundle.countries[iso]?.name ?? iso;
  if (kind === 'indicator') {
    const ind = bundle.sovereignty.indicators.find((i) => i.id === id);
    return `${country} · ${ind?.label ?? id}`;
  }
  if (kind === 'record') {
    const h = bundle.holding_classes.find((c) => c.class_id === id);
    return `${country} · ${h?.label ?? id} · ${field.replace(/_/g, ' ')}`;
  }
  return `${country} · ${id.replace(/_/g, ' ')}`;
}

function ExternalLink({ href, label }: { href: string; label: string }) {
  const theme = useTheme();
  return (
    <Text
      accessibilityRole="link"
      onPress={() => Linking.openURL(href)}
      style={[styles.link, { color: theme.accentText }]}
    >
      {label}
    </Text>
  );
}

export function SourceList({
  bundle,
  numbers,
  claims,
  onLayoutSource,
}: {
  bundle: Bundle;
  numbers: Map<string, number>;
  claims: Map<string, string[]>;
  /** Reports where each source sits, so a [n] mark can scroll to it. */
  onLayoutSource?: (sourceId: string, y: number) => void;
}) {
  const theme = useTheme();
  if (numbers.size === 0) return null;
  const ordered = [...numbers.entries()].sort((a, b) => a[1] - b[1]);
  const chip = (kind: ReturnType<typeof checkKind>) =>
    kind === 'tier'
      ? { backgroundColor: theme.bgEmphasis, borderColor: 'transparent', color: theme.accentText }
      : kind === 'pass'
        ? { borderColor: theme.accent, color: theme.fgPrimary }
        : kind === 'short'
          ? { borderColor: theme.rank5, borderStyle: 'dashed' as const, color: theme.fgPrimary }
          : { borderColor: theme.border, color: theme.fgSecondary };
  return (
    <View style={[styles.section, { borderTopColor: theme.border }]} accessibilityLabel="Sources">
      <Text accessibilityRole="header" style={[styles.heading, { color: theme.fgPrimary }]}>
        Sources
      </Text>
      <Text style={[styles.intro, { color: theme.fgSecondary }]}>
        Each source is listed once. The hash identifies the exact document that was fetched; the
        quote under each claim is text found in it by machine, in its original language, then a
        machine translation where the source is not in English, then the checks the claim passed.
      </Text>
      <Text style={[styles.rule, { color: theme.fgMuted }]}>
        Evidence grades. {bundle.notice.grade_rule}
      </Text>
      {ordered.map(([sid, n]) => {
        const s = bundle.sources[sid];
        if (!s) return null;
        return (
          <View
            key={sid}
            onLayout={
              onLayoutSource ? (e) => onLayoutSource(sid, e.nativeEvent.layout.y) : undefined
            }
            style={[styles.card, { borderColor: theme.border, backgroundColor: theme.bgCard }]}
          >
            <View style={styles.head}>
              <Text style={[styles.number, { color: theme.accentText }]}>[{n}]</Text>
              <View style={{ flex: 1 }}>
                <Text style={[styles.title, { color: theme.fgPrimary }]}>{s.title}</Text>
                <Text style={[styles.meta, { color: theme.fgMuted }]}>
                  {[s.publisher, s.published, host(s.url)].filter(Boolean).join(' · ')} ·{' '}
                  <ExternalLink href={s.url} label="Open source" />
                  {s.archived_url ? (
                    <>
                      {' · '}
                      <ExternalLink href={s.archived_url} label="Archived copy" />
                    </>
                  ) : null}
                </Text>
              </View>
            </View>
            {s.notes ? (
              <Text style={[styles.notes, { color: theme.fgMuted }]}>{s.notes}</Text>
            ) : null}
            {(claims.get(sid) ?? []).map((claim) =>
              (bundle.claims[claim] ?? [])
                .filter((c) => c.source_id === sid)
                .map((c) => (
                  <View
                    key={claim + c.locator}
                    style={[styles.claim, { borderLeftColor: theme.accentText }]}
                  >
                    <Text style={[styles.claimLabel, { color: theme.accentText }]}>
                      {claimLabel(bundle, claim)}{' '}
                      <Text style={[styles.code, { color: theme.fgMuted }]}>{claim}</Text>
                    </Text>
                    {c.original ? (
                      <Text style={[styles.quote, { color: theme.fgPrimary }]}>“{c.original}”</Text>
                    ) : (
                      <Text style={[styles.gloss, { color: theme.fgSecondary }]}>
                        Value {c.value_as_found} at {c.locator}
                      </Text>
                    )}
                    {c.gloss ? (
                      <Text style={[styles.gloss, { color: theme.fgSecondary }]}>
                        Machine translation: “{c.gloss}”
                      </Text>
                    ) : null}
                    <View style={styles.chips}>
                      <Text
                        style={[
                          styles.chip,
                          c.grade === 'Standard'
                            ? { borderColor: theme.border, color: theme.fgPrimary }
                            : {
                                backgroundColor: theme.accent,
                                borderColor: theme.accent,
                                color: theme.fgOnAccent,
                              },
                        ]}
                      >
                        {c.grade}
                      </Text>
                      {c.checklist.map((item) => (
                        <Text key={item} style={[styles.chip, chip(checkKind(item))]}>
                          {item}
                        </Text>
                      ))}
                    </View>
                    <Text style={[styles.meta, { color: theme.fgMuted }]}>
                      retrieved {c.retrieved} ·{' '}
                      <Pressable
                        onPress={() => Linking.openURL(reviewLink(bundle, claim))}
                        accessibilityRole="link"
                      >
                        <Text style={[styles.link, { color: theme.accentText }]}>
                          Check this fact
                        </Text>
                      </Pressable>
                    </Text>
                  </View>
                ))
            )}
          </View>
        );
      })}
    </View>
  );
}

const styles = StyleSheet.create({
  section: { borderTopWidth: StyleSheet.hairlineWidth, marginTop: SPACE.xl, paddingTop: SPACE.lg },
  heading: { fontSize: Type.title, fontWeight: '700', marginBottom: SPACE.sm },
  intro: { fontSize: Type.body - 1, lineHeight: 19, marginBottom: SPACE.sm },
  rule: { fontSize: Type.axis, lineHeight: 16, marginBottom: SPACE.md },
  card: {
    borderWidth: StyleSheet.hairlineWidth,
    borderRadius: 6,
    padding: SPACE.md,
    marginBottom: SPACE.sm,
  },
  head: { flexDirection: 'row', gap: SPACE.sm },
  number: { fontWeight: '700', fontSize: Type.body },
  title: { fontSize: Type.body + 1, fontWeight: '700', lineHeight: 21 },
  meta: { fontSize: Type.axis, lineHeight: 16, marginTop: 2 },
  link: { textDecorationLine: 'underline' },
  notes: { fontFamily: 'Menlo', fontSize: 10, marginTop: SPACE.sm },
  claim: { borderLeftWidth: 3, paddingLeft: SPACE.md, marginTop: SPACE.md, gap: SPACE.xs },
  claimLabel: { fontSize: Type.axis, fontWeight: '600' },
  code: { fontFamily: 'Menlo', fontWeight: '400' },
  quote: { fontSize: Type.body + 1, lineHeight: 23, fontStyle: 'italic' },
  gloss: { fontSize: Type.body - 1, lineHeight: 19 },
  chips: { flexDirection: 'row', flexWrap: 'wrap', gap: 6 },
  chip: {
    fontSize: Type.axis,
    borderWidth: 1,
    borderRadius: 999,
    paddingHorizontal: 9,
    paddingVertical: 2,
    overflow: 'hidden',
  },
});
