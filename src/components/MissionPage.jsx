import React, { useEffect } from 'react';
import { Heart, Sparkles, Shield, Compass, Users } from 'lucide-react';
import FooterSection from './FooterSection';

export default function MissionPage({ onNavigate, onOpenModal }) {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="relative w-full min-h-screen bg-[#1a1a1a] text-white font-modern flex flex-col justify-between overflow-x-hidden pt-[4.75rem] md:pt-[5.5rem]">
      
      {/* Main Mission Page Container */}
      <main className="relative w-full flex-1 flex flex-col items-center">
        
        {/* Pixel-Perfect Reference Canvas Section (1024x378) */}
        <section
          id="mission-section"
          className="relative w-full bg-[#1a1a1a] text-white overflow-hidden select-none flex justify-center items-center"
        >
          <div className="relative w-full max-w-[1024px] h-[378px] min-h-[378px] mx-auto box-border">
            
            {/* Eyebrow Label: Our Values */}
            <div
              className="absolute top-[45px] left-6 sm:left-12 md:left-[81px] font-modern font-medium text-[12.1px] tracking-[0.005em] text-[#d9c9d7] leading-none antialiased"
            >
              Our Values
            </div>

            {/* Headline: Relationships are at the core of everything we do. */}
            <h1
              className="absolute top-[85px] left-6 sm:left-12 md:left-[81px] font-tiempos font-normal text-[28px] sm:text-[31px] md:text-[33.5px] leading-[1.08] md:leading-[35.8px] tracking-[-0.015em] text-[#fffefd] antialiased m-0 p-0"
            >
              Relationships are at the core
              <br />
              of everything we do.
            </h1>

            {/* Body Paragraph 1 */}
            <p
              className="absolute top-[175px] left-6 sm:left-12 md:left-[81px] font-modern font-normal text-[13px] sm:text-[13.2px] md:text-[13.5px] leading-[18.5px] sm:leading-[19px] md:leading-[19.5px] tracking-[0.001em] text-[#fffefd] antialiased max-w-[90%] md:max-w-none m-0 p-0"
            >
              And not just the romantic kind. We can&rsquo;t accomplish really hard things
              <br className="hidden md:inline" />
              {' '}alone&mdash;so we make great relationships the foundation of our
              <br className="hidden md:inline" />
              {' '}teamwork.
            </p>

            {/* Body Paragraph 2 */}
            <p
              className="absolute top-[253px] left-6 sm:left-12 md:left-[81px] font-modern font-normal text-[13px] sm:text-[13.2px] md:text-[13.5px] leading-[18px] sm:leading-[18.5px] md:leading-[19.0px] tracking-[0.001em] text-[#fffefd] antialiased max-w-[90%] md:max-w-none m-0 p-0"
            >
              We believe these three core values are what it takes to build those
              <br className="hidden md:inline" />
              {' '}great relationships.
            </p>

          </div>
        </section>

        {/* Extended Values Cards Grid */}
        <section className="relative w-full max-w-[1024px] mx-auto px-6 sm:px-12 md:px-[81px] pt-4 pb-20 box-border">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-6 border-t border-[#303030]">
            
            {/* Card 1: Authenticity */}
            <div className="bg-[#222222] border border-[#333333] rounded-2xl p-7 hover:border-aubergine-25/50 transition-colors">
              <div className="w-10 h-10 rounded-full bg-aubergine/40 flex items-center justify-center text-aubergine-25 mb-4">
                <Heart className="w-5 h-5" />
              </div>
              <h3 className="font-tiempos text-xl font-semibold text-white mb-2">
                Authenticity
              </h3>
              <p className="font-modern text-[13.5px] leading-relaxed text-stone-25">
                We share&mdash;never hide&mdash;our words, actions, and intentions. We believe real connections begin with truth and vulnerability.
              </p>
            </div>

            {/* Card 2: Courage */}
            <div className="bg-[#222222] border border-[#333333] rounded-2xl p-7 hover:border-aubergine-25/50 transition-colors">
              <div className="w-10 h-10 rounded-full bg-aubergine/40 flex items-center justify-center text-aubergine-25 mb-4">
                <Compass className="w-5 h-5" />
              </div>
              <h3 className="font-tiempos text-xl font-semibold text-white mb-2">
                Courage
              </h3>
              <p className="font-modern text-[13.5px] leading-relaxed text-stone-25">
                Breakthroughs require a willingness to take risks, challenge convention, and build something designed to be deleted.
              </p>
            </div>

            {/* Card 3: Empathy */}
            <div className="bg-[#222222] border border-[#333333] rounded-2xl p-7 hover:border-aubergine-25/50 transition-colors">
              <div className="w-10 h-10 rounded-full bg-aubergine/40 flex items-center justify-center text-aubergine-25 mb-4">
                <Users className="w-5 h-5" />
              </div>
              <h3 className="font-tiempos text-xl font-semibold text-white mb-2">
                Empathy
              </h3>
              <p className="font-modern text-[13.5px] leading-relaxed text-stone-25">
                We deeply consider others&rsquo; perspectives and recognize that everyone is human first. Dating is vulnerable; kindness is non-negotiable.
              </p>
            </div>

          </div>

          {/* Return Home Link */}
          <div className="mt-14 text-center">
            <button
              onClick={() => onNavigate && onNavigate('home')}
              className="inline-flex items-center space-x-2 font-modern text-xs font-semibold px-6 py-3 rounded-full bg-white text-mirrorBlack hover:bg-aubergine hover:text-white transition-all shadow-md active:scale-95"
            >
              <span>Back to Home</span>
            </button>
          </div>
        </section>

      </main>

      {/* Page Footer */}
      <FooterSection onOpenModal={onOpenModal} onNavigate={onNavigate} />
    </div>
  );
}
