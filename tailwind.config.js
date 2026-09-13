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
        society: ['Society', 'Tiempos Headline', 'Georgia', 'serif'],
        proxima: ['Proxima Nova', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
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
        mirrorBlack: '#1a1a1a',
        hingeBlack: '#1a1a1a',
        tinderRed: '#cd130a',
      },
      spacing: {
        'header-height': '4.5rem',
      },
      keyframes: {
        heroBottomToTop: {
          '0%': {
            opacity: '0',
            transform: 'translateY(65px) scale(1.02)',
            filter: 'blur(10px)',
          },
          '40%': {
            opacity: '0.85',
          },
          '100%': {
            opacity: '1',
            transform: 'translateY(0) scale(1)',
            filter: 'blur(0px)',
          },
        },
        ambientFadeIn: {
          '0%': {
            opacity: '0',
            transform: 'translateY(40px) scale(1.15)',
          },
          '100%': {
            opacity: '0.5',
            transform: 'translateY(0) scale(1.25)',
          },
        },
        headlineFadeIn: {
          '0%': {
            opacity: '0',
            transform: 'translateY(32px)',
          },
          '100%': {
            opacity: '1',
            transform: 'translateY(0)',
          },
        },
      },
      animation: {
        'hero-bg': 'heroBottomToTop 1.6s cubic-bezier(0.16, 1, 0.3, 1) forwards',
        'hero-ambient': 'ambientFadeIn 2s cubic-bezier(0.16, 1, 0.3, 1) forwards',
        'hero-headline': 'headlineFadeIn 1.3s cubic-bezier(0.16, 1, 0.3, 1) 0.35s both',
      },
    },
  },
  plugins: [],
};
