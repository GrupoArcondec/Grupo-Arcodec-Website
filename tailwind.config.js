/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        navy: '#08182B',
        'navy-2': '#0C2238',
        'navy-3': '#103052',
        cobalt: '#1B3FA0',
        electric: '#3D6BF5',
        'electric-soft': '#6E96FF',
        amp: '#FFC20E',
        'amp-deep': '#E6A800',
        ice: '#CFE3F5',
        paper: '#EEF1F6',
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
        body: ['Manrope', 'system-ui', 'sans-serif'],
        mono: ['"Space Mono"', 'ui-monospace', 'monospace'],
      },
      maxWidth: {
        wrap: '1280px',
      },
    },
  },
  plugins: [],
}
