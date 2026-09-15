import React, { useState, useEffect, useRef } from 'react';

export default function DoubleDateSection() {
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
      id="double-date-section"
      className="relative w-full bg-[#5a000f] text-white overflow-hidden select-none scroll-mt-[5.5rem]"
    >
      <div className="relative w-full max-w-[1024px] h-[425px] mx-auto pt-[18px] md:pt-[3.5px] pb-[18px] box-border flex flex-col items-center">
        {/* Top Header & Copy Group */}
        <div
          className={`flex flex-col items-center text-center px-4 transition-all duration-700 ${
            isVisible ? 'doubledate-fade-in-up' : 'opacity-0 translate-y-6'
          }`}
        >
          {/* Section Headline */}
          <h2 className="font-society font-bold text-[25px] sm:text-[27px] md:text-[27.6px] leading-[28px] md:leading-[28px] tracking-[-0.012em] text-white antialiased mb-[12.5px] md:translate-x-[1.5px]">
            Party of <span className="italic">four</span>
          </h2>

          {/* Section Body Text Paragraphs */}
          <div className="font-modern font-normal text-[11px] sm:text-[11.1px] md:text-[11.15px] leading-[16px] md:leading-[16px] tracking-[-0.002em] text-white text-center antialiased max-w-[620px]">
            <p className="m-0 p-0 sm:whitespace-nowrap">
              First dates don't have to feel like job interviews.
            </p>
            <p className="m-0 p-0 sm:whitespace-nowrap">
              <strong className="font-bold">Double Date</strong> changes the math: you bring your person, they bring theirs, and
            </p>
            <p className="m-0 p-0 sm:whitespace-nowrap">
              suddenly it's just four people at a table seeing what happens. Less pressure.
            </p>
            <p className="m-0 p-0 sm:whitespace-nowrap">
              More fun. The kind of night that's good either way.
            </p>
          </div>
        </div>

        {/* 4 Photos Collage Showcase */}
        <div
          className={`relative w-full max-w-[1024px] mt-[36px] md:mt-[50px] px-4 md:px-0 flex justify-center items-center overflow-visible transition-all duration-1000 ${
            isVisible ? 'doubledate-fade-in-up-delayed' : 'opacity-0 translate-y-10'
          }`}
        >
          <div className="relative w-[340px] sm:w-[370px] md:w-[396px] h-auto md:h-[250px] md:translate-x-[3.5px] overflow-visible flex justify-center items-center">
            <img
              src="/images/party_of_four_cards.png"
              alt="Party of four Double Date daters smiling and laughing together"
              className="w-full h-auto object-contain pointer-events-none select-none transition-transform duration-500 ease-out hover:scale-[1.02]"
              loading="lazy"
            />
          </div>
        </div>
      </div>
    </section>
  );
}
