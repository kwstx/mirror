import React, { useState, useEffect, useRef } from 'react';

export default function MusicModeSection() {
  const [isVisible, setIsVisible] = useState(false);
  const sectionRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        } else {
          setIsVisible(false);
        }
      },
      {
        threshold: 0.15,
        rootMargin: '0px 0px -50px 0px',
      }
    );

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => {
      if (sectionRef.current) {
        observer.unobserve(sectionRef.current);
      }
    };
  }, []);

  return (
    <section
      ref={sectionRef}
      id="music-mode-section"
      className="relative w-full bg-[#f1e6ef] text-[#360524] overflow-hidden select-none scroll-mt-[5.5rem]"
    >
      <div className="relative w-full max-w-[1024px] mx-auto pt-16 sm:pt-20 md:pt-[72px] pb-6 md:pb-[11px] box-border flex flex-col items-center">
        {/* Top Header Group (Icon + Title + Subtitle) */}
        <div
          className={`flex flex-col items-center text-center px-4 transition-all duration-700 ${
            isVisible ? 'music-fade-in-up' : 'opacity-0 translate-y-8'
          }`}
        >
          {/* Magenta Music Note Icon */}
          <div className="w-[35px] h-[35px] flex items-center justify-center mb-[14px] hover:scale-110 transition-transform duration-300">
            <img
              src="/images/music_note_transparent.png"
              alt="Music Mode Note Icon"
              className="w-[35px] h-[35px] object-contain drop-shadow-[0_2px_4px_rgba(254,0,155,0.15)]"
              loading="lazy"
            />
          </div>

          {/* Section Headline */}
          <h2 className="font-tiempos font-bold text-[28px] sm:text-[32px] md:text-[35.5px] leading-[1.05] tracking-[-0.015em] text-[#350322] antialiased mb-[13px]">
            No skips
          </h2>

          {/* Section Description Paragraph */}
          <p className="font-modern font-normal text-[13px] md:text-[13.5px] leading-[17px] text-[#360524] tracking-[0.002em] max-w-[500px] antialiased">
            <span className="block md:whitespace-nowrap">
              Put what you're listening to on your profile.{' '}
              <strong className="font-bold text-[#350322]">Music Mode</strong> shows you people who
            </span>
            <span className="block md:whitespace-nowrap">
              are out there with similar good taste. Forget "hey," your playlist just became your
            </span>
            <span className="block md:whitespace-nowrap">best opener.</span>
          </p>
        </div>

        {/* Bottom Photo Collage Showcase (Bottom to top reveal + interactive subtle hover) */}
        <div
          className={`relative w-full max-w-[1024px] mt-10 md:mt-[55px] px-2 sm:px-4 md:px-0 overflow-visible transition-all duration-1000 ${
            isVisible ? 'music-fade-in-up-delayed' : 'opacity-0 translate-y-12'
          }`}
        >
          <div className="relative w-full overflow-visible flex justify-center items-end">
            <img
              src="/images/music_mode_collage.png"
              alt="Music Mode dating profiles collage with speech bubbles"
              className="w-full h-auto max-w-[1024px] object-contain object-bottom pointer-events-none select-none transition-transform duration-700 ease-out hover:scale-[1.01]"
              loading="lazy"
            />
          </div>
        </div>
      </div>
    </section>
  );
}
