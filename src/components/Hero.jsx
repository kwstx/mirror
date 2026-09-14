import React, { useState, useEffect } from 'react';

export default function Hero({ zoom = 100, animKey = 0 }) {
  const [isReady, setIsReady] = useState(false);
  const scaleValue = zoom / 100;

  useEffect(() => {
    setIsReady(false);
    const frame = requestAnimationFrame(() => {
      const timer = setTimeout(() => {
        setIsReady(true);
      }, 40);
      return () => clearTimeout(timer);
    });
    return () => cancelAnimationFrame(frame);
  }, [animKey]);

  return (
    <section id="hero-section" className="relative w-full h-screen min-h-[640px] overflow-hidden select-none bg-[#1a282c]">
      {/* Ambient backdrop to seamlessly blend zoomed-out edges */}
      <div className="absolute inset-0 w-full h-full overflow-hidden bg-[#1a282c]">
        <img
          key={`ambient-${animKey}`}
          src="/images/hero_bg.jpg"
          alt=""
          aria-hidden="true"
          className={`w-full h-full object-cover object-center scale-125 blur-3xl pointer-events-none ${
            isReady ? 'hero-ambient-animating' : 'opacity-0'
          }`}
        />
      </div>

      {/* Main Hero Image with fade-in from bottom to top animation on load */}
      <div className="absolute inset-0 w-full h-full flex items-center justify-center overflow-hidden">
        <div
          key={`hero-bg-${animKey}`}
          className={`w-full h-full origin-bottom flex items-center justify-center ${
            isReady ? 'hero-bg-animating' : 'opacity-0 translate-y-16'
          }`}
        >
          <img
            src="/images/hero_bg.jpg"
            alt="Couple standing in a blooming wildflower field looking out at mountains"
            style={{ transform: `scale(${scaleValue})` }}
            className="w-full h-full object-cover object-center transition-transform duration-500 ease-out origin-center"
            loading="eager"
            decoding="async"
          />
        </div>
      </div>

      {/* Subtle top gradient vignette for crisp text contrast */}
      <div className="absolute inset-x-0 top-0 h-40 bg-gradient-to-b from-black/40 via-black/15 to-transparent pointer-events-none" />

      {/* Hero Headline Content */}
      <div
        key={`headline-${animKey}`}
        className={`absolute bottom-8 sm:bottom-12 md:bottom-16 lg:bottom-20 left-0 w-full z-10 pointer-events-none ${
          isReady ? 'hero-headline-animating' : 'opacity-0 translate-y-8'
        }`}
      >
        <div className="w-full px-6 md:px-12 lg:px-16">
          <h1 className="font-tiempos font-semibold text-white tracking-[-0.012em] leading-[1.08] text-[2.75rem] sm:text-[3.5rem] md:text-[4.25rem] lg:text-[4.85rem] xl:text-[5.25rem] drop-shadow-[0_2px_8px_rgba(0,0,0,0.25)] max-w-5xl">
            The dating app<br />
            that finds your person<span className="inline-block text-[0.38em] align-super ml-1.5 font-modern font-normal tracking-normal select-none -translate-y-1">™</span>
          </h1>
        </div>
      </div>
    </section>
  );
}
