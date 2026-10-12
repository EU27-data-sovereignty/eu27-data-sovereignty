import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'

import { App } from './App'
// Manrope, the site's one family (#101), self-hosted: the CSP allows fonts from this origin only.
import '@fontsource/manrope/latin-400.css'
import '@fontsource/manrope/latin-500.css'
import '@fontsource/manrope/latin-600.css'
import '@fontsource/manrope/latin-700.css'
import '@fontsource/manrope/latin-800.css'
import '@fontsource/manrope/latin-ext-400.css'
import '@fontsource/manrope/latin-ext-500.css'
import '@fontsource/manrope/latin-ext-600.css'
import '@fontsource/manrope/latin-ext-700.css'
import '@fontsource/manrope/latin-ext-800.css'
// Quoted sources are shown in their original language: Greek and Bulgarian need their own subsets, which
// the browser fetches only on a page that uses them.
import '@fontsource/manrope/greek-400.css'
import '@fontsource/manrope/greek-700.css'
import '@fontsource/manrope/cyrillic-400.css'
import '@fontsource/manrope/cyrillic-700.css'
import './styles/index.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
