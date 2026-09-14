import React, { useState, useEffect, useRef } from 'react';

export default function QuoteSection() {
  const [isVisible, setIsVisible] = useState(false);
  const sectionRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.15 }
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

  // Global char index tracker so each letter animates sequentially starting from top left
  let globalCharIndex = 0;

  const renderAnimatedLine = (text) => {
    // Split line into words to preserve natural word wrapping while animating each character
    const words = text.split(' ');

    return (
      <span className="inline">
        {words.map((word, wordIdx) => {
          const letters = word.split('');
          const renderedWord = (
            <span key={wordIdx} className="inline-block whitespace-nowrap">
              {letters.map((char, charIdx) => {
                const delay = (globalCharIndex++) * 0.015; // 15ms per character for smooth fluid reveal
                return (
                  <span
                    key={charIdx}
                    className={`inline-block ${
                      isVisible ? 'letter-fade-in' : 'opacity-0'
                    }`}
                    style={{
                      animationDelay: `${delay}s`,
                    }}
                  >
                    {char}
                  </span>
                );
              })}
            </span>
          );

          // Add spacing after each word except last
          if (wordIdx < words.length - 1) {
            globalCharIndex++; // Count space in sequence for natural rhythm
            return (
              <React.Fragment key={wordIdx}>
                {renderedWord}
                <span className="inline-block">&nbsp;</span>
              </React.Fragment>
            );
          }

          return renderedWord;
        })}
      </span>
    );
  };

  return (
    <section
      ref={sectionRef}
      id="quote-section"
      className="relative w-full bg-white text-black overflow-hidden select-none scroll-mt-[5.5rem]"
    >
      {/* Subtle top transitional gradient matching capture */}
      <div
        className="absolute inset-x-0 top-0 h-20 pointer-events-none opacity-90"
        style={{
          background:
            'radial-gradient(ellipse 65% 100% at 50% 0%, rgba(226, 226, 226, 0.42) 0%, rgba(255, 255, 255, 0) 100%)',
        }}
        aria-hidden="true"
      />

      <div className="relative w-full max-w-[1024px] mx-auto px-6 sm:px-12 md:px-16 lg:px-[99px] pt-20 sm:pt-28 md:pt-[130px] pb-10 sm:pb-12 md:pb-[39px] box-border">
        {/* Main Body Statement */}
        <div className="font-tiempos font-bold text-[1.65rem] sm:text-[1.95rem] md:text-[35.5px] leading-[1.06] sm:leading-[1.06] md:leading-[36.5px] tracking-[-0.015em] antialiased">
          {/* Paragraph 1 */}
          <p className="mb-4 sm:mb-4 md:mb-[19px]">
            {renderAnimatedLine("The person you’ve been looking for")}
            <br className="hidden sm:inline" />
            <span className="sm:hidden"> </span>
            {renderAnimatedLine("might be closer than you think.")}
          </p>

          {/* Paragraph 2 */}
          <p className="mb-14 sm:mb-20 md:mb-[96px]">
            {renderAnimatedLine("Less swiping. Better matches.")}
            <br className="hidden sm:inline" />
            <span className="sm:hidden"> </span>
            {renderAnimatedLine("More reasons to believe your next date")}
            <br className="hidden sm:inline" />
            <span className="sm:hidden"> </span>
            {renderAnimatedLine("could be different.")}
          </p>
        </div>

        {/* Signature Line */}
        <div className="font-tiempos italic font-bold text-[1.45rem] sm:text-[1.75rem] md:text-[34px] leading-tight tracking-[-0.01em] antialiased">
          {renderAnimatedLine("—Welcome to dating, reimagined.")}
        </div>
      </div>
    </section>
  );
}

