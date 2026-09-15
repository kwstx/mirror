import React, { useState, useEffect, useRef } from 'react';

export default function MissionSection() {
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
      id="mission-section"
      className="relative w-full bg-[#1a1a1a] text-white overflow-hidden select-none scroll-mt-20 flex justify-center items-center"
    >
      {/* 1024px Canvas Container matching exact coordinates */}
      <div className="relative w-full max-w-[1024px] h-[378px] min-h-[378px] mx-auto box-border">
        
        {/* Eyebrow Label: Our Philosophy */}
        <div
          className={`absolute top-[45px] left-6 sm:left-12 md:left-[81px] font-modern font-medium text-[12.1px] tracking-[0.005em] text-[#d9c9d7] leading-none antialiased transition-all duration-700 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-3'
          }`}
        >
          Our Philosophy
        </div>

        {/* Headline: Dating shouldn't feel like shopping. */}
        <h2
          className={`absolute top-[85px] left-6 sm:left-12 md:left-[81px] font-tiempos font-normal text-[28px] sm:text-[31px] md:text-[33.5px] leading-[1.08] md:leading-[35.8px] tracking-[-0.015em] text-[#fffefd] antialiased m-0 p-0 transition-all duration-800 delay-100 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          Dating shouldn&rsquo;t feel like shopping.
        </h2>

        {/* Body Paragraph 1 */}
        <p
          className={`absolute top-[155px] left-6 sm:left-12 md:left-[81px] font-modern font-normal text-[13px] sm:text-[13.2px] md:text-[13.5px] leading-[18.5px] sm:leading-[19px] md:leading-[19.5px] tracking-[0.001em] text-[#fffefd] antialiased max-w-[90%] md:max-w-[800px] m-0 p-0 transition-all duration-800 delay-200 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          You shouldn&rsquo;t have to judge hundreds of faces, play games, or hope an algorithm eventually gets lucky. We believe finding someone should be about understanding people deeply&mdash;and making fewer, better introductions.
        </p>

        {/* Body Paragraph 2 */}
        <p
          className={`absolute top-[245px] left-6 sm:left-12 md:left-[81px] font-modern font-normal text-[13px] sm:text-[13.2px] md:text-[13.5px] leading-[18px] sm:leading-[18.5px] md:leading-[19.0px] tracking-[0.001em] text-[#fffefd] antialiased max-w-[90%] md:max-w-[800px] m-0 p-0 transition-all duration-800 delay-300 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          We believe these three principles are what make better dating possible.
        </p>

      </div>
    </section>
  );
}
