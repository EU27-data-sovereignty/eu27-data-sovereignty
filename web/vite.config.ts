import { fileURLToPath, URL } from 'node:url'

import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// Tailwind 4 is configured in CSS (@theme in src/styles/index.css), so there is no
// tailwind.config.ts and no postcss.config.js here.
export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) },
  },
  // The language tables live in model/i18n/ (#111, #113), outside web/; the site catalogs are served from there as
  // files, so the dev server and the tests must be allowed to read that folder.
  server: {
    port: 5173,
    host: true,
    fs: { allow: ['.', fileURLToPath(new URL('../model/i18n', import.meta.url))] },
  },
  preview: { port: 4173, host: true },
  build: {
    outDir: 'dist',
    // d3 is the only heavy dependency; splitting it keeps the entry chunk small.
    rollupOptions: {
      output: {
        manualChunks(id: string) {
          if (id.includes('node_modules/d3') || id.includes('topojson')) return 'd3'
          if (id.includes('node_modules/react')) return 'react'
          return undefined
        },
      },
    },
  },
})
