import React, { useState, useEffect, useRef } from 'react';

export default function HingeLabsSection() {
  const [isVisible, setIsVisible] = useState(false);
  const sectionRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        } else {
          // Reset when scrolled out of view so animation activates again on next scroll into Labs
          setIsVisible(false);
        }
      },
      {
        threshold: 0.2,
        rootMargin: '0px 0px -100px 0px',
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
      id="labs-section"
      className="relative w-full bg-[#fffefd] text-mirrorBlack overflow-hidden select-none scroll-mt-[5.5rem]"
    >
      <div className="relative w-full max-w-[1024px] mx-auto min-h-[426px] flex flex-col md:flex-row items-center md:items-start justify-start pt-32 sm:pt-40 md:pt-[180px] pb-20 md:pb-[100px] box-border">
        {/* Left Column: Couple Photography (Bottom to Top Fade In) */}
        <div
          className={`w-full md:w-[491px] flex-shrink-0 px-4 md:px-0 flex justify-center md:justify-start transition-opacity duration-300 ${
            isVisible ? 'labs-fade-in-up' : 'opacity-0'
          }`}
        >
          <div className="w-full max-w-[491px] h-[300px] sm:h-[350px] md:h-[393px] overflow-hidden rounded-[8px] md:rounded-l-none md:rounded-r-[8px] shadow-none">
            <img
              src="/images/hinge_labs_couple.png"
              alt="Hinge Labs researchers and daters enjoying a conversation"
              className="w-full h-full object-cover object-center"
              loading="lazy"
            />
          </div>
        </div>

        {/* Right Column: Labs Information Content (Bottom to Top Fade In with slight stagger) */}
        <div
          className={`w-full md:w-[533px] flex-1 flex flex-col justify-start px-6 sm:px-10 md:px-0 md:pl-[94px] pt-6 md:pt-[150px] pb-6 md:pb-0 transition-opacity duration-300 ${
            isVisible ? 'labs-fade-in-up-delayed' : 'opacity-0'
          }`}
        >
          {/* Headline */}
          <h2 className="font-tiempos font-bold text-[2.25rem] sm:text-[2.65rem] md:text-[42px] leading-[1.08] tracking-[-0.015em] text-mirrorBlack antialiased mb-6 md:mb-[28px]">
            We&rsquo;re building a better way to date.
          </h2>

          {/* Body Paragraph */}
          <p className="font-modern font-normal text-[15px] sm:text-[16.5px] md:text-[17.5px] leading-[24px] sm:leading-[26px] md:leading-[27px] text-stone tracking-[0.005em] antialiased max-w-[440px]">
            Our AI learns who you are, understands what you want, and searches for the people most compatible with you. You don&rsquo;t swipe. You don&rsquo;t search. We do.
          </p>
        </div>
      </div>
    </section>
  );
}

