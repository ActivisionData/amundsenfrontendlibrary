module.exports = {
  coverageThreshold: {
      './js/config': {
          branches: 50, // 100
          functions: 0, // 100
          lines: 50, // 100
          statements: 50, // 100
      },
      './js/components': {
          branches: 40, // 75
          functions: 45, // 75
          lines: 50, // 75
          statements: 50, // 75
      },
      './js/ducks': {
          branches: 35, // 75
          functions: 30, // 75
          lines: 35, // 75
          statements: 35, // 75
      },
      './js/fixtures': {
          branches: 100,
          functions: 100,
          lines: 100,
          statements: 100,
      },
  },
  roots: [
    '<rootDir>/js',
  ],
  setupFiles: [
    '<rootDir>/test-setup.ts',
  ],
  transform: {
    '^.+\\.tsx?$': 'ts-jest',
    '^.+\\.js$': 'babel-jest',
    '^.+\\.(css|scss)$': '<rootDir>/node_modules/jest-css-modules',
  },
  testRegex: '(/tests/.*|(\\.|/)(test|spec))\\.(j|t)sx?$',
  moduleDirectories: ['node_modules', 'js'],
  moduleFileExtensions: [
    'ts',
    'tsx',
    'js',
    'jsx',
    'json',
  ],
  globals: {
    'ts-jest': {
      diagnostics: false,
    },
  },
};
