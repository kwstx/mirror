import React, { useState, useEffect, useRef } from 'react';

export default function DifferenceSection({ theme = 'light' }) {
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
      title: 'Deep Understanding',
      body: 'Forget filling out endless boxes. Talk to your AI matchmaker about who you are, what you want, how you love, and what actually matters to you. The more it understands, the better it can match you.',
    },
    {
      title: 'AI Matchmaker',
      body: 'You don\u2019t browse the dating pool. Your AI does. It analyzes compatible people, weighs personality, values, lifestyle, attraction, and relationship goals, then brings you the few it genuinely thinks you should meet.',
    },
    {
      title: 'Mutual Matches',
      body: 'We don\u2019t believe one person should have to chase another. When our AI finds a promising connection, it recommends you to both people independently. Only when you\u2019re both interested do you get introduced.',
    },
    {
      title: 'Why You Two',
      body: 'Every introduction comes with a reason. See exactly what your AI noticed\u2014from shared values and relationship goals to complementary personalities and unexpected chemistry.',
    },
    {
      title: 'Beyond Your Type',
      body: 'Your stated preferences aren\u2019t the whole story. Our AI learns from your conversations, dates, feedback, and relationships to discover patterns you might never notice yourself. Sometimes, the person you need isn\u2019t the person you thought you wanted.',
    },
    {
      title: 'Fewer, Better Introductions',
      body: 'No infinite feeds. No hundreds of profiles waiting to be judged. We filter the noise and give you a small number of people worth your attention.',
    },
    {
      title: 'Date Feedback',
      body: 'Tell us what happened after you meet. Chemistry, attraction, conversation, comfort, and whether you\u2019d see them again all help your matchmaker understand what actually works for you.',
    },
    {
      title: 'A Matchmaker That Learns',
      body: 'Every interaction makes your recommendations smarter. The goal isn\u2019t to keep you dating forever\u2014it\u2019s to get better at finding someone you genuinely want to stop dating apps for.',
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
        
        {/* Headline: The Cupid Difference */}
        <h2
          className={`font-tiempos font-normal text-[36px] sm:text-[40px] md:text-[43.5px] leading-none tracking-[-0.018em] ${
            isLight ? 'text-[#1a1a1a]' : 'text-[#fffefd]'
          } antialiased m-0 p-0 mb-[62px] md:mb-[65px] transition-all duration-700 ${
            isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-3'
          }`}
        >
          The Cupid Difference
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

