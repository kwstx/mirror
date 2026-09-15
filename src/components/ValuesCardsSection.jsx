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

  const values = [
    {
      num: '01',
      title: 'Authenticity',
      body: 'We share \u2014 never hide \u2014 our words, actions, and intentions.',
      delay: 0,
    },
    {
      num: '02',
      title: 'Courage',
      body: 'Breakthroughs require a willingness to take risks and embrace lofty goals and tough challenges.',
      delay: 100,
    },
    {
      num: '03',
      title: 'Empathy',
      body: 'We\u2019re all humans first. So we deeply consider the perspectives of others, listen openly, and speak with care.',
      delay: 200,
    },
  ];

  return (
    <section
      ref={sectionRef}
      id="values-cards-section"
      className="relative w-full bg-white text-[#1a1a1a] overflow-hidden select-none flex justify-center items-center pt-2 pb-10 md:pt-4 md:pb-16"
    >
      {/* 1024px Container */}
      <div className="relative w-full max-w-[1024px] mx-auto px-6 sm:px-12 md:px-[81.5px] box-border">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-x-[29px] gap-y-12 md:gap-y-0">
          {values.map((item) => (
            <div
              key={item.num}
              className={`flex flex-col transition-all duration-800 ${
                isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4'
              }`}
              style={{ transitionDelay: `${item.delay}ms` }}
            >
              {/* Numeral */}
              <div className="font-tiempos font-normal text-[90px] sm:text-[115px] md:text-[138px] leading-none tracking-[-0.035em] text-[#1a1a1a] antialiased mb-4 md:mb-[44px]">
                {item.num}
              </div>
              
              {/* Title */}
              <h2 className="font-tiempos font-normal text-[28px] sm:text-[31px] md:text-[33.5px] leading-none tracking-[-0.015em] text-[#1a1a1a] antialiased m-0 p-0 mb-3 md:mb-[11px]">
                {item.title}
              </h2>
              
              {/* Body */}
              <p className="font-modern font-normal text-[11.8px] sm:text-[12.1px] md:text-[12.28px] leading-[16.5px] sm:leading-[17px] md:leading-[17.3px] tracking-[0.001em] text-[#1a1a1a] antialiased max-w-[275px] m-0 p-0">
                {item.body}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

