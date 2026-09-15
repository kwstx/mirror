import React, { useEffect } from 'react';
import { Heart, Sparkles, Shield, Compass, Users } from 'lucide-react';
import FooterSection from './FooterSection';
import ValuesCardsSection from './ValuesCardsSection';
import DifferenceSection from './DifferenceSection';

export default function MissionPage({ onNavigate, onOpenModal }) {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="relative w-full min-h-screen bg-white text-[#1a1a1a] font-modern flex flex-col justify-between overflow-x-hidden pt-[5.5rem] md:pt-[6.5rem]">
      
      {/* Main Mission Page Container */}
      <main className="relative w-full flex-1 flex flex-col items-center">
        
        {/* Mission Intro Section */}
        <section
          id="mission-section"
          className="relative w-full bg-white text-[#1a1a1a] overflow-hidden select-none flex justify-center items-center pt-10 pb-6 md:pt-16 md:pb-8"
        >
          <div className="relative w-full max-w-[1024px] mx-auto px-6 sm:px-12 md:px-[81px] box-border">
            
            {/* Eyebrow Label: Our Values */}
            <div className="font-modern font-medium text-[12.1px] tracking-[0.005em] text-[#705a6e] leading-none antialiased mb-7 md:mb-8">
              Our Values
            </div>

            {/* Headline */}
            <h1 className="font-tiempos font-normal text-[28px] sm:text-[31px] md:text-[33.5px] leading-[1.08] md:leading-[35.8px] tracking-[-0.015em] text-[#1a1a1a] antialiased m-0 p-0 mb-7 md:mb-8">
              Relationships are at the core
              <br />
              of everything we do.
            </h1>

            {/* Body Paragraph 1 */}
            <p className="font-modern font-normal text-[13px] sm:text-[13.2px] md:text-[13.5px] leading-[18.5px] sm:leading-[19px] md:leading-[19.5px] tracking-[0.001em] text-[#1a1a1a] antialiased max-w-[90%] md:max-w-none m-0 p-0 mb-4 md:mb-5">
              And not just the romantic kind. We can&rsquo;t accomplish really hard things
              <br className="hidden md:inline" />
              {' '}alone&mdash;so we make great relationships the foundation of our
              <br className="hidden md:inline" />
              {' '}teamwork.
            </p>

            {/* Body Paragraph 2 */}
            <p className="font-modern font-normal text-[13px] sm:text-[13.2px] md:text-[13.5px] leading-[18px] sm:leading-[18.5px] md:leading-[19.0px] tracking-[0.001em] text-[#1a1a1a] antialiased max-w-[90%] md:max-w-none m-0 p-0">
              We believe these three core values are what it takes to build those
              <br className="hidden md:inline" />
              {' '}great relationships.
            </p>

          </div>
        </section>

        {/* Pixel-Perfect 3 Values Cards Section (1024x374) */}
        <ValuesCardsSection />

        {/* Pixel-Perfect The Hinge Difference Section (1024x460) */}
        <DifferenceSection />

        {/* Back to Home Action Bar */}
        <section className="relative w-full max-w-[1024px] mx-auto px-6 sm:px-12 md:px-[81px] pt-10 pb-16 box-border text-center">
          <button
            onClick={() => onNavigate && onNavigate('home')}
            className="inline-flex items-center space-x-2 font-modern text-xs font-semibold px-6 py-3 rounded-full bg-[#1a1a1a] text-white hover:bg-aubergine hover:text-white transition-all shadow-md active:scale-95"
          >
            <span>Back to Home</span>
          </button>
        </section>

      </main>

      {/* Page Footer - Remains black */}
      <FooterSection theme="dark" onOpenModal={onOpenModal} onNavigate={onNavigate} />
    </div>
  );
}
