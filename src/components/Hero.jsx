import React from 'react';

export default function Hero() {
  return (
    <section className="relative w-full h-screen min-h-[640px] overflow-hidden select-none">
      {/* Pristine Master 4K Background Image */}
      <div className="absolute inset-0 w-full h-full">
        <img
          src="/images/hero_bg.jpg"
          alt="Two people sitting together by a fountain in the park"
          className="w-full h-full object-cover object-center"
          loading="eager"
          decoding="async"
        />
      </div>

      {/* Subtle top gradient vignette for crisp text contrast */}
      <div className="absolute inset-x-0 top-0 h-40 bg-gradient-to-b from-black/40 via-black/15 to-transparent pointer-events-none" />

      {/* Hero Headline Content */}
      <div className="absolute bottom-8 sm:bottom-12 md:bottom-16 lg:bottom-20 left-0 w-full z-10 pointer-events-none">
        <div className="w-full px-6 md:px-12 lg:px-16">
          <h1 className="font-tiempos font-semibold text-white tracking-[-0.012em] leading-[1.08] text-[2.75rem] sm:text-[3.5rem] md:text-[4.25rem] lg:text-[4.85rem] xl:text-[5.25rem] drop-shadow-[0_2px_8px_rgba(0,0,0,0.25)] max-w-5xl">
            The dating app<br />
            designed to be deleted<span className="inline-block text-[0.38em] align-super ml-1.5 font-modern font-normal tracking-normal select-none -translate-y-1">™</span>
          </h1>
        </div>
      </div>
    </section>
  );
}
