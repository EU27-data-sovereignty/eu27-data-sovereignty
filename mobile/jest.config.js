module.exports = {
  preset: 'jest-expo',
  setupFiles: ['<rootDir>/jest.setup.js'],
  // Only *.test.* files are suites; __tests__/support.tsx is a helper.
  testMatch: ['**/__tests__/**/*.test.[jt]s?(x)'],
  transformIgnorePatterns: [
    'node_modules/(?!((jest-)?react-native|@react-native(-community)?)|expo(nent)?|@expo(nent)?/.*|react-navigation|@react-navigation/.*|@unimodules/.*|unimodules|sentry-expo|native-base|react-native-svg)',
  ],
  // The live round-trip against local Supabase runs only from test.sh --integration.
  testPathIgnorePatterns: ['/node_modules/', '\\.integration\\.test\\.tsx?$'],
  // Measure every source file, not only the ones a test happens to import. The three parity-pinned copies
  // of web/ files, the generated tokens and the device-only file store are excluded: the first are the
  // web's to cover, the tokens are data, and the last needs a device (mobile/test.sh --integration drives
  // the same store on MemoryFileStore).
  collectCoverageFrom: [
    'app/**/*.{ts,tsx}',
    'src/**/*.{ts,tsx}',
    '!src/data/types.ts',
    '!src/data/format.ts',
    '!src/data/sources.ts',
    '!src/data/bundled.ts',
    '!src/constants/Colors.ts',
    '!src/edition/expoFiles.ts',
    '!src/edition/defaults.ts',
    '!src/edition/hash.ts',
  ],
  // Floors set under the first green run's baseline: a drop fails ./test.sh and CI. Raise them as coverage
  // grows; never lower them to make a change pass.
  coverageThreshold: {
    global: { statements: 70, branches: 55, functions: 65, lines: 70 },
  },
};
