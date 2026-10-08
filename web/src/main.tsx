import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'

import { App } from './App'
// The print serif for display type (#91), self-hosted: the CSP allows fonts from this origin only.
import '@fontsource/libertinus-serif/latin-400.css'
import '@fontsource/libertinus-serif/latin-ext-400.css'
// The EU27.CLOUD display sans for headings and page bands, self-hosted for the same reason.
import '@fontsource/montserrat/latin-700.css'
import '@fontsource/montserrat/latin-ext-700.css'
import './styles/index.css'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
