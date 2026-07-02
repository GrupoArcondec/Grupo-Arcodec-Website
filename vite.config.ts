import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// base './' → el build funciona en cualquier ruta (Vercel, Netlify o abierto local)
export default defineConfig({
  base: './',
  plugins: [react()],
})
