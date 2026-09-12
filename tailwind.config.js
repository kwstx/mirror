/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        modern: ['Modern Era', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        tiempos: ['Tiempos Headline', 'Georgia', 'serif'],
        'tiempos-narrow': ['Tiempos Text Narrow', 'Georgia', 'serif'],
      },
      colors: {
        aubergine: {
          DEFAULT: '#67295f',
          25: '#d9c9d7',
        },
        stone: {
          DEFAULT: '#484848',
          25: '#d1d1d1',
          50: '#a3a3a3',
          75: '#767676',
        },
        offWhite: '#f5f5f2',
        hingeBlack: '#1a1a1a',
      },
      spacing: {
        'header-height': '4.5rem',
      },
    },
  },
  plugins: [],
};
