/**
 * Renders the content model (model/document.py), ported from `web/src/components/DocumentView.tsx`: the
 * same document the PDF typesets and the site shows.
 *
 * A fact carries its numbered sources as pressable [n] marks that jump to the source list below; a gap is
 * set in muted italics, and a disputed value in muted italics with a dashed underline, so a withheld value
 * reads as a gap and never as a fact (#75, #89). Nothing here adds a sentence: a renderer that writes
 * content becomes a second source. `__tests__/document-view.test.tsx` checks that the rendered text, minus
 * the [n] marks, is exactly the spans' text.
 *
 * In a language the catalogue has admitted (#117), a label or gap span, and a section title, is shown in that
 * language when the catalogue has its exact English text; a fact, a disputed value or an explanation never is.
 */
import { StyleSheet, Text, View, type StyleProp, type TextStyle } from 'react-native';

import type { Block, Bundle, Document, Span } from '@/data/types';
import { useLanguage } from '@/i18n/LanguageContext';
import { TableBlock } from './TableBlock';
import { SPACE, Type, useTheme } from './theme';

export interface SpanProps {
  span: Span;
  numbers: Map<string, number>;
  bundle: Bundle;
  /** Jump to a numbered source; absent when the screen has no source list. */
  onSource?: (sourceId: string) => void;
  style?: StyleProp<TextStyle>;
}

export function SpanView({ span, numbers, bundle, onSource, style }: SpanProps) {
  const theme = useTheme();
  const { t, tx } = useLanguage();
  if (span.role === 'gap') {
    return <Text style={[style, styles.muted, { color: theme.fgMuted }]}>{tx(span.t)}</Text>;
  }
  if (span.role === 'disputed') {
    return (
      <Text
        style={[
          style,
          styles.muted,
          styles.disputed,
          { color: theme.fgMuted, textDecorationColor: theme.gapMark },
        ]}
      >
        {span.t}
      </Text>
    );
  }
  if (span.role === 'label') return <Text style={style}>{tx(span.t)}</Text>;
  if (span.role !== 'fact') return <Text style={style}>{span.t}</Text>;
  const ids = [
    ...new Set(
      (span.c ?? []).flatMap((claim) => (bundle.claims[claim] ?? []).map((c) => c.source_id))
    ),
  ];
  return (
    <Text style={style}>
      {span.t}
      {ids.map((sid) => {
        const n = numbers.get(sid);
        return (
          <Text
            key={sid}
            accessibilityRole="link"
            accessibilityLabel={t('app.sources.mark', {
              n: n ?? '',
              label: bundle.sources[sid]?.label ?? sid,
              grade: span.g ?? '',
            })}
            onPress={onSource ? () => onSource(sid) : undefined}
            style={[styles.mark, { color: theme.accentText }]}
          >
            {' '}
            [{n}]
          </Text>
        );
      })}
    </Text>
  );
}

export function Spans({ spans, style, ...rest }: { spans: Span[] } & Omit<SpanProps, 'span'>) {
  const theme = useTheme();
  return (
    <Text style={[styles.body, { color: theme.fgPrimary }, style]}>
      {spans.map((s, i) => (
        <Text key={i}>
          {i > 0 ? ' ' : null}
          <SpanView span={s} {...rest} />
        </Text>
      ))}
    </Text>
  );
}

function BlockView({ block, ...rest }: { block: Block } & Omit<SpanProps, 'span'>) {
  const theme = useTheme();
  switch (block.type) {
    case 'p':
      return (
        <View style={styles.block}>
          <Spans spans={block.spans} {...rest} />
        </View>
      );
    case 'callout': {
      const tone =
        block.tone === 'gap'
          ? { borderLeftColor: theme.gapMark, backgroundColor: theme.bgEmphasis }
          : block.tone === 'method'
            ? { borderLeftColor: theme.method, backgroundColor: theme.methodWash }
            : { borderLeftColor: theme.accent, backgroundColor: theme.bgEmphasis };
      return (
        <View style={[styles.block, styles.callout, tone]}>
          <Spans spans={block.spans} {...rest} style={{ fontSize: Type.body - 1 }} />
        </View>
      );
    }
    case 'list':
      return (
        <View style={styles.block}>
          {block.items.map((item, i) => (
            <View key={i} style={styles.item}>
              <Text style={[styles.bullet, { color: theme.fgMuted }]}>•</Text>
              <View style={{ flex: 1 }}>
                <Spans spans={item} {...rest} />
              </View>
            </View>
          ))}
        </View>
      );
    case 'table':
      return <TableBlock block={block} {...rest} />;
  }
}

/**
 * A document, section by section. `tables` lets a screen draw one section's table its own way, and `blocks`
 * any block; both may only draw what the block already holds, never a new sentence (as on the web).
 */
export function DocumentView({
  doc,
  tables = {},
  blocks,
  ...rest
}: {
  doc: Document;
  tables?: Record<string, (block: Extract<Block, { type: 'table' }>) => React.ReactNode>;
  blocks?: (block: Block, section: string) => React.ReactNode | undefined;
} & Omit<SpanProps, 'span'>) {
  const theme = useTheme();
  const { t, tx } = useLanguage();
  return (
    <View>
      {doc.sections.map((s, i) => (
        <View key={s.id} style={styles.section} accessibilityLabel={tx(s.title)}>
          <Text style={[styles.sectionNo, { color: theme.accentText }]}>
            {t('app.section_no', { n: i + 1 })}
          </Text>
          <Text
            accessibilityRole="header"
            style={[styles.sectionTitle, { color: theme.fgPrimary }]}
          >
            {tx(s.title)}
          </Text>
          {s.blocks.map((b, j) => {
            if (b.type === 'table' && tables[s.id]) return <View key={j}>{tables[s.id]!(b)}</View>;
            const own = blocks?.(b, s.id);
            if (own !== undefined) return <View key={j}>{own}</View>;
            return <BlockView key={j} block={b} {...rest} />;
          })}
        </View>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  body: { fontSize: Type.body, lineHeight: 21 },
  muted: { fontStyle: 'italic' },
  disputed: { textDecorationLine: 'underline', textDecorationStyle: 'dashed' },
  mark: { fontSize: Type.axis, fontWeight: '600' },
  block: { marginBottom: SPACE.md },
  callout: {
    borderLeftWidth: 4,
    borderRadius: 4,
    paddingHorizontal: SPACE.md,
    paddingVertical: SPACE.sm,
  },
  item: { flexDirection: 'row', marginBottom: SPACE.xs },
  bullet: { width: 14, fontSize: Type.body, lineHeight: 21 },
  section: { marginBottom: SPACE.xl },
  sectionNo: { fontSize: Type.axis, fontWeight: '600', letterSpacing: 1.2 },
  sectionTitle: { fontSize: Type.title, fontWeight: '700', marginBottom: SPACE.md, lineHeight: 28 },
});
