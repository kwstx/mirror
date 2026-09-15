import React, { useState } from 'react';

export default function Navbar({ onOpenModal, onToggleMobileMenu, onNavigate, currentPage }) {
  return (
    <header className="fixed top-0 left-0 w-full z-40 h-[4.75rem] md:h-[5.5rem] transition-all duration-300">
      {/* Top subtle dark gradient */}
      <div className="absolute inset-0 bg-gradient-to-b from-black/45 via-black/15 to-transparent pointer-events-none" />

      <div className="relative w-full h-full px-6 md:px-12 lg:px-16 flex items-center justify-between">
        
        {/* Mobile Hamburger (Visible on small screens) */}
        <div className="flex md:hidden items-center">
          <button
            onClick={onToggleMobileMenu}
            aria-label="Toggle Navigation Menu"
            className="text-white p-2 focus:outline-none hover:opacity-80 transition-opacity"
          >
            <div className="w-6 h-4 flex flex-col justify-between">
              <span className="w-full h-[2px] bg-white rounded-full"></span>
              <span className="w-full h-[2px] bg-white rounded-full"></span>
            </div>
          </button>
        </div>

        {/* Desktop Left Nav Links */}
        <nav className="hidden md:flex items-center space-x-9 lg:space-x-11">
          <button
            onClick={() => {
              if (onNavigate) {
                onNavigate('mission');
              } else {
                onOpenModal('mission');
              }
            }}
            className={`font-modern font-medium text-[15.5px] tracking-[0.005em] transition-colors focus:outline-none ${
              currentPage === 'mission' ? 'text-aubergine-25 font-semibold' : 'text-white hover:text-white/80'
            }`}
          >
            Mission
          </button>
          <button
            onClick={() => onOpenModal('impact')}
            className="font-modern font-medium text-[15.5px] tracking-[0.005em] text-white hover:text-white/80 transition-colors focus:outline-none"
          >
            Impact
          </button>
          <button
            onClick={() => {
              if (currentPage === 'mission' && onNavigate) {
                onNavigate('home', 'labs-section');
              } else {
                const el = document.getElementById('labs-section');
                if (el) {
                  el.scrollIntoView({ behavior: 'smooth' });
                } else {
                  onOpenModal('labs');
                }
              }
            }}
            className="font-modern font-medium text-[15.5px] tracking-[0.005em] text-white hover:text-white/80 transition-colors focus:outline-none"
          >
            Labs
          </button>
        </nav>

        {/* Centered Cupid Brand Logo */}
        <div className="absolute left-1/2 -translate-x-1/2 flex items-center justify-center">
          <a
            href="/"
            onClick={(e) => {
              e.preventDefault();
              if (onNavigate) onNavigate('home');
              else window.scrollTo({ top: 0, behavior: 'smooth' });
            }}
            aria-label="Cupid Homepage"
            className="inline-block hover:opacity-95 transition-opacity select-none cursor-pointer"
          >
            <span className="font-tiempos font-bold text-[30px] md:text-[36px] tracking-[-0.02em] leading-none text-white drop-shadow-[0_1px_3px_rgba(0,0,0,0.3)]">
              Cupid
            </span>
          </a>
        </div>

        {/* Desktop Right Nav Links */}
        <nav className="hidden md:flex items-center space-x-9 lg:space-x-11">
          <button
            onClick={() => onOpenModal('newsroom')}
            className="font-modern font-medium text-[15.5px] tracking-[0.005em] text-white hover:text-white/80 transition-colors focus:outline-none"
          >
            Newsroom
          </button>
          <button
            onClick={() => onOpenModal('careers')}
            className="font-modern font-medium text-[15.5px] tracking-[0.005em] text-white hover:text-white/80 transition-colors focus:outline-none"
          >
            Careers
          </button>
        </nav>

        {/* Mobile Download CTA */}
        <div className="flex md:hidden items-center">
          <button
            onClick={() => onOpenModal('download')}
            className="font-modern font-bold text-xs bg-white text-mirrorBlack px-3.5 py-1.5 rounded-full hover:bg-aubergine hover:text-white transition-colors"
          >
            Download
          </button>
        </div>

      </div>
    </header>
  );
}
