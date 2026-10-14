/** The last resort: a render error shows a message and a retry instead of a blank screen. */
import { Component, type ReactNode } from 'react';
import { Appearance, Pressable, StyleSheet, Text, View } from 'react-native';

import { Text as Type, themeFor } from '@/constants/Colors';

type Props = { children: ReactNode };
type State = { error: Error | null };

export class ErrorBoundary extends Component<Props, State> {
  state: State = { error: null };

  static getDerivedStateFromError(error: Error): State {
    return { error };
  }

  private reset = () => this.setState({ error: null });

  render() {
    if (this.state.error) {
      const theme = themeFor(Appearance.getColorScheme());
      return (
        <View style={[styles.container, { backgroundColor: theme.bgPage }]}>
          <Text style={[styles.title, { color: theme.fgPrimary }]} accessibilityRole="header">
            Something went wrong
          </Text>
          {/* Raw error text helps in development but can leak internals to readers. */}
          <Text style={[styles.message, { color: theme.fgSecondary }]}>
            {__DEV__ ? this.state.error.message : 'Please try again.'}
          </Text>
          <Pressable
            onPress={this.reset}
            accessibilityRole="button"
            style={[styles.button, { backgroundColor: theme.accent }]}
          >
            <Text style={{ color: theme.fgOnAccent, fontWeight: '600' }}>Try again</Text>
          </Pressable>
        </View>
      );
    }
    return this.props.children;
  }
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: 'center', justifyContent: 'center', padding: 24 },
  title: { fontSize: Type.title, fontWeight: '700', marginBottom: 8 },
  message: { fontSize: Type.body, textAlign: 'center' },
  button: { marginTop: 20, paddingVertical: 12, paddingHorizontal: 20, borderRadius: 8 },
});
