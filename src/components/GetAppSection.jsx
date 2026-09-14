import React, { useState, useEffect, useRef } from 'react';

export default function GetAppSection({ onOpenModal }) {
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
        rootMargin: '0px 0px -40px 0px',
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
      id="get-app-section"
      className="relative w-full bg-[#ffffff] py-7 md:py-[27px] px-4 md:px-[55px] flex justify-center items-center select-none overflow-hidden scroll-mt-20"
    >
      {/* Main Responsive Container */}
      <div className="relative w-full max-w-[1024px] flex justify-center items-center">
        {/* Yellow Card Banner (Exact 913px x 300px matching reference) */}
        <div
          className={`relative w-full max-w-[914px] min-h-[300px] h-[300px] bg-[#FFDB5B] rounded-[24px] overflow-hidden flex items-stretch shadow-none transition-all duration-700 ${
            isVisible ? 'getapp-fade-in-up' : 'opacity-0 translate-y-8'
          }`}
        >
          {/* Left Content (Title, Subtitle, QR Code) */}
          <div className="relative z-10 flex flex-col justify-start pl-[30px] pt-[33px] pb-[28px] max-w-[480px]">
            {/* Header: 'Get the app' */}
            <h2 className="font-modern font-bold text-[38px] md:text-[39.5px] leading-[1.02] tracking-[-0.025em] text-[#202020] antialiased m-0 p-0">
              Get the app
            </h2>

            {/* Subtitle */}
            <p className="font-modern font-normal text-[13.5px] leading-[1.25] tracking-[-0.005em] text-[#202020] mt-[16px] mb-0 antialiased">
              Just scan the QR code to get started.
            </p>

            {/* QR Code Container */}
            <div className="mt-[17px] inline-block">
              <div
                onClick={() => onOpenModal && onOpenModal('download')}
                className="w-[145px] h-[145px] bg-white rounded-[16px] overflow-hidden cursor-pointer shadow-sm hover:scale-[1.03] active:scale-[0.98] transition-transform duration-300 flex items-center justify-center group"
                title="Scan to download Bumble app"
              >
                <img
                  src="/images/bumble_qr_code_card.png"
                  alt="QR code to download the Bumble app"
                  className="w-[145px] h-[145px] object-contain select-none pointer-events-none group-hover:opacity-95 transition-opacity"
                  loading="lazy"
                  draggable={false}
                />
              </div>
            </div>
          </div>

          {/* Right Phone Mockup Collage (Anchored to bottom right) */}
          <div className="absolute right-[20px] md:right-[44px] bottom-0 w-[340px] sm:w-[380px] md:w-[400px] h-[278px] pointer-events-none select-none overflow-visible flex items-end justify-end">
            <img
              src="/images/bumble_phones.png"
              alt="Bumble mobile app interface preview screens"
              className="w-full h-auto max-h-[278px] object-contain object-bottom pointer-events-none select-none transition-transform duration-500 ease-out hover:scale-[1.01]"
              loading="lazy"
              draggable={false}
            />
          </div>
        </div>
      </div>
    </section>
  );
}
