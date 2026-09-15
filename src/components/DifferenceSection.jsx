import React, { useState, useEffect, useRef } from 'react';

export default function DifferenceSection({ theme = 'dark' }) {
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
        threshold: 0.1,
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

  const isLight = theme === 'light';

  const cards = [
    {
      title: 'Detailed Profiles',
      body: 'Go ahead, be picky. Hinge profiles encourage you to share your religion, education, and day-to-day life so we can introduce you to the best people for you.',
    },
    {
      title: 'Proven Prompts',
      body: 'Answer three prompts to activate your profile, and switch them up any time. We review our prompts and keep the ones that are most likely to get you out on a date.',
    },
    {
      title: 'Conversation Starters',
      body: 'Our research found that liking specific pictures or prompts leads to better matches and more dates than liking a profile in general. So now users must like a specific part of a Hinge profile—they can even add a comment to their like to kickstart a conversation.',
    },
    {
      title: 'Matchmaking Algorithm',
      body: 'Hinge uses a Nobel-Prize-winning algorithm that helps you go on better quality dates, not just more dates. You’re eight times more likely to have a great date with our Most Compatible suggestions, aka the people we think you’ll like the most.',
    },
    {
      title: 'Meaningful Likes',
      body: 'Research has shown us that eight is the magic number. When our members had more free likes per day, their matches were worse. When they had fewer, they were paying to send more. So now everyone gets eight for free every day.',
    },
    {
      title: 'Transparent Likes',
      body: 'No anonymous likes—we show you who has liked you, so you don’t miss out on a potential match.',
    },
  ];

  return (
    <section
      ref={sectionRef}
      id="difference-section"
      className={`relative w-full ${isLight ? 'bg-white text-[#1a1a1a]' : 'bg-[#1a1a1a] text-white'} overflow-hidden select-none flex justify-center items-center pt-[20px] pb-[48px] md:pt-[20px] md:pb-[56px]`}
    >
      {/* 1024px Container matching reference coordinates & spacing */}
      <div className="relative w-full max-w-[1024px] mx-auto px-6 sm:px-12 md:px-[78.5px] box-border">
        
        {/* Headline: The Hinge Difference */}
        <h2
          className={`font-tiempos font-normal text-[36px] sm:text-[40px] md:text-[43.5px] leading-none tracking-[-0.018em] ${
            isLight ? 'text-[#1a1a1a]' : 'text-[#fffefd]'
          } antialiased m-0 p-0 mb-[62px] md:mb-[65px] transition-all duration-700 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-3'
          }`}
        >
          The Hinge Difference
        </h2>

        {/* Dividing Horizontal Line */}
        <div
          className={`w-full h-[1px] ${
            isLight ? 'bg-[#e5e5e5]' : 'bg-[#353535]'
          } mb-[23px]`}
        />

        {/* 3-Column Grid for 6 Difference Cards */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-x-[29px] gap-y-10 md:gap-y-[44px]">
          {cards.map((card, idx) => (
            <div
              key={card.title}
              className={`flex flex-col transition-all duration-700 ${
                isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-3'
              }`}
              style={{ transitionDelay: `${100 + idx * 50}ms` }}
            >
              <h3
                className={`font-modern font-bold text-[13px] sm:text-[13.2px] md:text-[13.5px] leading-none tracking-[0.005em] ${
                  isLight ? 'text-[#1a1a1a]' : 'text-[#fffefd]'
                } antialiased m-0 p-0 mb-[18px]`}
              >
                {card.title}
              </h3>
              <p
                className={`font-modern font-normal text-[11.8px] sm:text-[12.1px] md:text-[12.28px] leading-[16.5px] sm:leading-[17px] md:leading-[17.3px] tracking-[0.001em] ${
                  isLight ? 'text-[#1a1a1a]' : 'text-[#fffefd]'
                } antialiased m-0 p-0`}
              >
                {card.body}
              </p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}

