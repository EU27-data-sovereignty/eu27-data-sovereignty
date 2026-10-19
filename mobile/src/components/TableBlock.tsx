/**
 * A table of the content model on a phone: each row becomes a card, the first cell its title and every
 * other cell a `column: cell` line. Every cell is the table's own span, rendered by SpanView with its
 * source marks, so a table says exactly what it says on the web and in the PDF, only stacked.
 */
import { StyleSheet, Text, View } from 'react-native';

import type { Block } from '@/data/types';
import { useLanguage } from '@/i18n/LanguageContext';
import { SpanView, type SpanProps } from './DocumentView';
import { SPACE, Type, useTheme } from './theme';

export function TableBlock({
  block,
  ...rest
}: { block: Extract<Block, { type: 'table' }> } & Omit<SpanProps, 'span'>) {
  const theme = useTheme();
  const { tx } = useLanguage();
  return (
    <View style={styles.table} accessibilityLabel={block.columns.map((c) => tx(c.t)).join(', ')}>
      {block.rows.map((row, r) => (
        <View
          key={r}
          style={[styles.card, { borderColor: theme.border, backgroundColor: theme.bgCard }]}
        >
          <View style={styles.title}>
            <Text style={[styles.column, { color: theme.fgMuted }]}>
              {tx(block.columns[0]?.t ?? '')}
            </Text>
            <SpanView
              span={row[0]!}
              {...rest}
              style={[styles.titleText, { color: theme.fgPrimary }]}
            />
          </View>
          {row.slice(1).map((cell, i) => (
            <View key={i} style={styles.line}>
              <Text style={[styles.column, { color: theme.fgMuted }]}>
                {tx(block.columns[i + 1]?.t ?? '')}
              </Text>
              <View style={{ flex: 1 }}>
                <SpanView span={cell} {...rest} style={[styles.cell, { color: theme.fgPrimary }]} />
              </View>
            </View>
          ))}
        </View>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  table: { marginBottom: SPACE.lg },
  card: {
    borderWidth: StyleSheet.hairlineWidth,
    borderRadius: 6,
    padding: SPACE.md,
    marginBottom: SPACE.sm,
  },
  title: { marginBottom: SPACE.sm },
  titleText: { fontSize: Type.body + 1, fontWeight: '700', lineHeight: 21 },
  line: { flexDirection: 'row', marginBottom: SPACE.xs },
  column: { width: 118, fontSize: Type.axis, fontWeight: '600', letterSpacing: 0.4, paddingTop: 3 },
  cell: { fontSize: Type.body, lineHeight: 20 },
});
