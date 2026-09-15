import React, { useState, useEffect, useRef } from 'react';

export default function ValuesCardsSection() {
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
      id="values-cards-section"
      className="relative w-full bg-[#1a1a1a] text-white overflow-hidden select-none flex justify-center items-center"
    >
      {/* 1024px x 374px Exact Coordinate Canvas matching uploaded reference */}
      <div className="relative w-full max-w-[1024px] h-[374px] min-h-[374px] mx-auto box-border">
        
        {/* Column 1: 01 / Authenticity */}
        <div
          className={`absolute top-[54px] left-6 sm:left-12 md:left-[81.5px] font-tiempos font-normal text-[90px] sm:text-[115px] md:text-[138px] leading-none tracking-[-0.035em] text-[#fffefd] antialiased transition-all duration-800 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          01
        </div>
        <h2
          className={`absolute top-[236.5px] left-6 sm:left-12 md:left-[81.5px] font-tiempos font-normal text-[28px] sm:text-[31px] md:text-[33.5px] leading-none tracking-[-0.015em] text-[#fffefd] antialiased m-0 p-0 transition-all duration-800 delay-100 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          Authenticity
        </h2>
        <p
          className={`absolute top-[281.5px] left-6 sm:left-12 md:left-[81.5px] font-modern font-normal text-[11.8px] sm:text-[12.1px] md:text-[12.28px] leading-[16.5px] sm:leading-[17px] md:leading-[17.3px] tracking-[0.001em] text-[#fffefd] antialiased max-w-[265px] md:max-w-none m-0 p-0 transition-all duration-800 delay-200 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          We share &mdash; never hide &mdash; our words, actions,
          <br className="hidden md:inline" />
          {' '}and intentions.
        </p>

        {/* Column 2: 02 / Courage */}
        <div
          className={`absolute top-[54px] left-[38%] sm:left-[38%] md:left-[378px] font-tiempos font-normal text-[90px] sm:text-[115px] md:text-[138px] leading-none tracking-[-0.035em] text-[#fffefd] antialiased transition-all duration-800 delay-100 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          02
        </div>
        <h2
          className={`absolute top-[236.5px] left-[38%] sm:left-[38%] md:left-[378px] font-tiempos font-normal text-[28px] sm:text-[31px] md:text-[33.5px] leading-none tracking-[-0.015em] text-[#fffefd] antialiased m-0 p-0 transition-all duration-800 delay-200 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          Courage
        </h2>
        <p
          className={`absolute top-[281.5px] left-[38%] sm:left-[38%] md:left-[378px] font-modern font-normal text-[11.8px] sm:text-[12.1px] md:text-[12.28px] leading-[16.5px] sm:leading-[17px] md:leading-[17.3px] tracking-[0.001em] text-[#fffefd] antialiased max-w-[265px] md:max-w-none m-0 p-0 transition-all duration-800 delay-300 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          Breakthroughs require a willingness to take risks
          <br className="hidden md:inline" />
          {' '}and embrace lofty goals and tough challenges.
        </p>

        {/* Column 3: 03 / Empathy */}
        <div
          className={`absolute top-[54px] left-[70%] sm:left-[70%] md:left-[674px] font-tiempos font-normal text-[90px] sm:text-[115px] md:text-[138px] leading-none tracking-[-0.035em] text-[#fffefd] antialiased transition-all duration-800 delay-200 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          03
        </div>
        <h2
          className={`absolute top-[236.5px] left-[70%] sm:left-[70%] md:left-[674px] font-tiempos font-normal text-[28px] sm:text-[31px] md:text-[33.5px] leading-none tracking-[-0.015em] text-[#fffefd] antialiased m-0 p-0 transition-all duration-800 delay-300 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          Empathy
        </h2>
        <p
          className={`absolute top-[281.5px] left-[70%] sm:left-[70%] md:left-[674px] font-modern font-normal text-[11.8px] sm:text-[12.1px] md:text-[12.28px] leading-[16.5px] sm:leading-[17px] md:leading-[17.3px] tracking-[0.001em] text-[#fffefd] antialiased max-w-[275px] md:max-w-none m-0 p-0 transition-all duration-800 delay-400 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
          }`}
        >
          We&rsquo;re all humans first. So we deeply consider the
          <br className="hidden md:inline" />
          {' '}perspectives of others, listen openly, and speak
          <br className="hidden md:inline" />
          {' '}with care.
        </p>

      </div>
    </section>
  );
}
