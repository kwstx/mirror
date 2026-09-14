import React from 'react';

export default function FooterSection({ onOpenModal }) {
  return (
    <footer
      id="footer-section"
      className="relative w-full bg-[#1a1a1a] text-white select-none scroll-mt-10"
    >
      {/* 1024px Max Width Canvas matching exact layout coordinates */}
      <div className="relative w-full max-w-[1024px] mx-auto px-6 md:px-[78px] pt-[30px] pb-16 md:pb-[56px] box-border">
        
        {/* Top Dividing Line (y=30, x=78..935, width=858px) */}
        <div className="w-full max-w-[858px] h-[1px] bg-[#353535] mx-auto" />

        {/* Main Content Grid (Starts at y=128, exactly 98px below divider) */}
        <div className="relative w-full pt-[98px] flex flex-col md:flex-row justify-between items-start">
          
          {/* Left Column: Brand Logo + Bottom Copyright & Language */}
          <div className="w-full md:w-[429px] flex flex-col justify-between self-stretch mb-10 md:mb-0">
            {/* Brand Wordmark (Hinge) at x=78, y=128 */}
            <div>
              <a
                href="/"
                className="inline-block hover:opacity-90 transition-opacity focus:outline-none"
                aria-label="Hinge Homepage"
              >
                <span className="font-tiempos font-bold text-[25.5px] leading-none tracking-[-0.015em] text-white antialiased">
                  Hinge
                </span>
              </a>
            </div>

            {/* Bottom Row: Copyright + Language Selector (at y=366) */}
            <div className="mt-12 md:mt-[215px] flex flex-wrap items-center gap-[18px]">
              <span className="font-modern font-normal text-[11px] text-[#a1a0a0] leading-none antialiased">
                &copy; 2026 Hinge Inc.
              </span>
              <button
                onClick={() => onOpenModal && onOpenModal('language')}
                className="flex items-center gap-[5px] text-white hover:text-white/80 transition-colors focus:outline-none group"
                aria-label="Language selector: English (UK)"
              >
                <img
                  src="/images/footer_icon_globe_transparent.png"
                  alt="Globe icon"
                  className="w-[11.5px] h-[11.5px] object-contain select-none pointer-events-none group-hover:scale-110 transition-transform"
                  loading="lazy"
                />
                <span className="font-modern font-bold text-[11px] leading-none text-white antialiased">
                  English (UK)
                </span>
              </button>
            </div>
          </div>

          {/* Right 3 Navigation Columns (Width: 429px total, 143px each at x=507, 650, 793) */}
          <div className="w-full md:w-[429px] grid grid-cols-1 sm:grid-cols-3 gap-8 sm:gap-4 md:gap-0">
            
            {/* Column 1: Index (x=507, width=143px) */}
            <div className="w-full md:w-[143px] md:pr-2">
              <h3 className="font-modern font-normal text-[12px] text-[#a1a2a3] leading-none mb-[16px] antialiased">
                Index
              </h3>
              <ul className="space-y-[13px] m-0 p-0 list-none">
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('mission')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Mission
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('careers')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Careers
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => {
                      const el = document.getElementById('labs-section');
                      if (el) el.scrollIntoView({ behavior: 'smooth' });
                      else if (onOpenModal) onOpenModal('labs');
                    }}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Labs
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('newsroom')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Newsroom
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('success')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Success Stories
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('history')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    History
                  </button>
                </li>
                <li>
                  <div className="flex items-center gap-[7px]">
                    <button
                      onClick={() => onOpenModal && onOpenModal('contact')}
                      className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                    >
                      Contact
                    </button>
                    <a
                      href="https://twitter.com/hinge"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="hover:opacity-75 transition-opacity inline-flex items-center"
                      aria-label="Hinge on Twitter / X"
                    >
                      <img
                        src="/images/footer_icon_twitter_transparent.png"
                        alt="Twitter"
                        className="w-[12px] h-[10px] object-contain select-none pointer-events-none"
                        loading="lazy"
                      />
                    </a>
                    <a
                      href="https://instagram.com/hinge"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="hover:opacity-75 transition-opacity inline-flex items-center"
                      aria-label="Hinge on Instagram"
                    >
                      <img
                        src="/images/footer_icon_instagram_transparent.png"
                        alt="Instagram"
                        className="w-[11px] h-[10px] object-contain select-none pointer-events-none"
                        loading="lazy"
                      />
                    </a>
                  </div>
                </li>
              </ul>
            </div>

            {/* Column 2: Resources (x=650, width=143px) */}
            <div className="w-full md:w-[143px] md:pr-2">
              <h3 className="font-modern font-normal text-[12px] text-[#a1a2a3] leading-none mb-[16px] antialiased">
                Resources
              </h3>
              <ul className="space-y-[13px] m-0 p-0 list-none">
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('dating_tips')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Safe Dating Tips
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('faq')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    FAQ
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('trust_safety')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Trust & Safety
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('press')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Press Resources
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('how_we_connect')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-[1.3] text-left focus:outline-none"
                  >
                    <span className="block">How We Connect</span>
                    <span className="block">Daters</span>
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('nfaq')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-[1.3] text-left focus:outline-none"
                  >
                    <span className="block">NFAQ (Not-so</span>
                    <span className="block">Frequently Asked</span>
                    <span className="block">Questions)</span>
                  </button>
                </li>
              </ul>
            </div>

            {/* Column 3: Legal (x=793, width=143px) */}
            <div className="w-full md:w-[143px]">
              <h3 className="font-modern font-normal text-[12px] text-[#a1a2a3] leading-none mb-[16px] antialiased">
                Legal
              </h3>
              <ul className="space-y-[13px] m-0 p-0 list-none">
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('security')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Security
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('terms')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Terms
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('privacy')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Privacy
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('cookie_policy')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Cookie Policy
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('consumer_health')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-[1.3] text-left focus:outline-none"
                  >
                    <span className="block">Consumer Health Data</span>
                    <span className="block">Privacy Policy</span>
                  </button>
                </li>
                <li>
                  <div className="flex items-center gap-[5px]">
                    <button
                      onClick={() => onOpenModal && onOpenModal('privacy_choices')}
                      className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                    >
                      Your Privacy Choices
                    </button>
                    <img
                      src="/images/privacy_pill_icon_transparent.png"
                      alt="Privacy choices badge"
                      className="w-[15px] h-[9px] object-contain select-none pointer-events-none"
                      loading="lazy"
                    />
                  </div>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('colorado_safety')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-[1.3] text-left focus:outline-none"
                  >
                    <span className="block">Colorado Safety Policy</span>
                    <span className="block">Information</span>
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('australia_safety')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Australia Safety Page
                  </button>
                </li>
                <li>
                  <button
                    onClick={() => onOpenModal && onOpenModal('accessibility')}
                    className="font-modern font-bold text-[12px] text-white hover:text-white/80 transition-colors leading-none text-left focus:outline-none"
                  >
                    Accessibility Statement
                  </button>
                </li>
              </ul>
            </div>

          </div>

        </div>

      </div>
    </footer>
  );
}
