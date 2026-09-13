import React from 'react';

export default function HingeLabsSection() {
  return (
    <section id="labs-section" className="relative w-full bg-[#fffefd] text-mirrorBlack overflow-hidden select-none scroll-mt-[5.5rem]">
      <div className="relative w-full max-w-[1024px] mx-auto min-h-[426px] flex flex-col md:flex-row items-center md:items-start justify-start pt-32 sm:pt-40 md:pt-[180px] pb-20 md:pb-[100px] box-border">
        {/* Left Column: Couple Photography */}
        <div className="w-full md:w-[491px] flex-shrink-0 px-4 md:px-0 flex justify-center md:justify-start">
          <div className="w-full max-w-[491px] h-[300px] sm:h-[350px] md:h-[393px] overflow-hidden rounded-[8px] md:rounded-l-none md:rounded-r-[8px] shadow-none">
            <img
              src="/images/hinge_labs_couple.png"
              alt="Hinge Labs researchers and daters enjoying a conversation"
              className="w-full h-full object-cover object-center"
              loading="lazy"
            />
          </div>
        </div>

        {/* Right Column: Labs Information Content */}
        <div className="w-full md:w-[533px] flex-1 flex flex-col justify-start px-6 sm:px-10 md:px-0 md:pl-[94px] pt-6 md:pt-[210px] pb-6 md:pb-0">
          {/* Category Tag */}
          <span className="font-modern font-medium text-[13.5px] leading-none text-aubergine tracking-normal antialiased block mb-[26px]">
            Hinge Labs
          </span>

          {/* Headline */}
          <h2 className="font-tiempos font-bold text-[2rem] sm:text-[2.2rem] md:text-[35.5px] leading-[1.05] tracking-[-0.015em] text-mirrorBlack antialiased mb-[34px]">
            We&rsquo;re love scientists.
          </h2>

          {/* Body Paragraph - Exactly 3 lines */}
          <p className="font-modern font-normal text-[13px] md:text-[13.5px] leading-[19px] text-stone tracking-[0.005em] antialiased">
            <span className="block md:whitespace-nowrap">Our Hinge Labs researchers, behavioral analysts, and</span>
            <span className="block md:whitespace-nowrap">matchmakers study daters and compatibility so we can</span>
            <span className="block md:whitespace-nowrap">make Hinge better for you. We&rsquo;ve gotten pretty good at it.</span>
          </p>
        </div>
      </div>
    </section>
  );
}
