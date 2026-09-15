import React, { useState } from 'react';
import { Sliders, Eye, EyeOff, Layers, CheckCircle2, RotateCcw } from 'lucide-react';

export default function ReferenceOverlay({ zoom, setZoom, onReplayAnimation, currentPage, onNavigate }) {
  const [isOpen, setIsOpen] = useState(false);
  const [opacity, setOpacity] = useState(50);
  const [isOverlayActive, setIsOverlayActive] = useState(false);
  const [blendMode, setBlendMode] = useState('normal'); // 'normal' or 'difference'
  const [activeSection, setActiveSection] = useState('mission'); // default to mission or current

  const handleSelectSection = (section) => {
    setActiveSection(section);
    if (section === 'mission' || section === 'cards') {
      if (currentPage !== 'mission' && onNavigate) {
        onNavigate('mission');
      }
      setTimeout(() => {
        const targetId = section === 'cards' ? 'values-cards-section' : 'mission-section';
        const el = document.getElementById(targetId);
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 80);
      return;
    }

    if (currentPage === 'mission' && onNavigate) {
      let targetId = 'hero-section';
      if (section === 'quote') targetId = 'quote-section';
      if (section === 'labs') targetId = 'labs-section';
      if (section === 'music' || section === 'doubledate') targetId = 'double-date-section';
      if (section === 'footer') targetId = 'footer-section';
      onNavigate('home', targetId);
      return;
    }

    let targetId = 'hero-section';
    if (section === 'quote') targetId = 'quote-section';
    if (section === 'labs') targetId = 'labs-section';
    if (section === 'music' || section === 'doubledate') targetId = 'double-date-section';
    if (section === 'footer') targetId = 'footer-section';
    const el = document.getElementById(targetId) || document.getElementById('music-mode-section');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  };

  return (
    <>
      {/* Reference Image Layer Overlay */}
      {isOverlayActive && (
        <div
          className="fixed inset-0 z-30 pointer-events-none select-none transition-opacity duration-150 overflow-hidden"
          style={{
            opacity: opacity / 100,
            mixBlendMode: blendMode,
          }}
        >
          {activeSection === 'hero' ? (
            <img
              src="/images/reference.jpg"
              alt="Reference screenshot"
              className="w-full h-full object-cover object-center"
            />
          ) : activeSection === 'mission' ? (
            <div className="w-full h-full flex justify-center items-start">
              <div className="w-full max-w-[1024px] pointer-events-none">
                <img
                  src="/images/mission_reference.png"
                  alt="Mission reference screenshot"
                  className="w-full h-auto object-contain object-top"
                />
              </div>
            </div>
          ) : activeSection === 'cards' ? (
            <div className="w-full h-full flex justify-center items-start">
              <div className="w-full max-w-[1024px] pointer-events-none">
                <img
                  src="/images/values_cards_reference.png"
                  alt="Values cards reference screenshot"
                  className="w-full h-auto object-contain object-top"
                />
              </div>
            </div>
          ) : activeSection === 'footer' ? (
            <div className="w-full h-full flex justify-center items-start">
              <div className="w-full max-w-[1024px] pointer-events-none">
                <img
                  src="/images/footer_reference.png"
                  alt="Footer reference screenshot"
                  className="w-full h-auto object-contain object-top"
                />
              </div>
            </div>
          ) : activeSection === 'music' || activeSection === 'doubledate' ? (
            <div className="w-full h-full flex justify-center items-start">
              <div className="w-full max-w-[1024px] pointer-events-none">
                <img
                  src="/images/party_of_four_reference.png"
                  alt="Double Date Party of four reference screenshot"
                  className="w-full h-auto object-contain object-top"
                />
              </div>
            </div>
          ) : activeSection === 'labs' ? (
            <div className="w-full h-full flex justify-center items-start">
              <div className="w-full max-w-[1024px] pointer-events-none">
                <img
                  src="/images/hinge_labs_reference.png"
                  alt="Hinge Labs reference screenshot"
                  className="w-full h-auto object-contain object-top"
                />
              </div>
            </div>
          ) : (
            <div className="w-full h-full flex justify-center items-start">
              <div className="w-full max-w-[1024px] pointer-events-none">
                <img
                  src="/images/quote_reference.png"
                  alt="Quote reference screenshot"
                  className="w-full h-auto object-contain object-top"
                />
              </div>
            </div>
          )}
        </div>
      )}

      {/* Floating Inspector Control Panel */}
      <div className="fixed bottom-4 right-4 z-50 select-none">
        {!isOpen ? (
          <button
            onClick={() => setIsOpen(true)}
            className="flex items-center space-x-2 bg-black/80 hover:bg-black text-white px-3.5 py-2 rounded-full border border-white/20 shadow-xl backdrop-blur-md text-xs font-modern font-semibold transition-all hover:scale-105"
            title="Inspect Pixel Match with Original Screenshot"
          >
            <Layers className="w-3.5 h-3.5 text-aubergine-25" />
            <span>Pixel Match Inspector</span>
          </button>
        ) : (
          <div className="bg-[#1a1a1a]/95 text-white border border-white/20 p-4 rounded-2xl shadow-2xl backdrop-blur-md w-72 space-y-3.5 animate-fade text-xs font-modern">
            <div className="flex items-center justify-between pb-2 border-b border-stone/30">
              <div className="flex items-center space-x-1.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span className="font-bold text-sm">Pixel Perfect Inspector</span>
              </div>
              <button
                onClick={() => setIsOpen(false)}
                className="text-stone-50 hover:text-white transition-colors"
              >
                ✕
              </button>
            </div>

            {/* Target Section Selector */}
            <div className="space-y-1.5">
              <span className="text-stone-25 text-[11px]">Compare Section:</span>
              <div className="grid grid-cols-4 gap-1">
                <button
                  onClick={() => handleSelectSection('hero')}
                  className={`py-1 px-1 rounded-md font-bold text-[10px] transition-colors ${
                    activeSection === 'hero'
                      ? 'bg-aubergine text-white shadow-sm'
                      : 'bg-stone/30 text-stone-50 hover:text-white'
                  }`}
                >
                  Hero
                </button>
                <button
                  onClick={() => handleSelectSection('quote')}
                  className={`py-1 px-1 rounded-md font-bold text-[10px] transition-colors ${
                    activeSection === 'quote'
                      ? 'bg-tinderRed text-white shadow-sm'
                      : 'bg-stone/30 text-stone-50 hover:text-white'
                  }`}
                >
                  Quote
                </button>
                <button
                  onClick={() => handleSelectSection('music')}
                  className={`py-1 px-1 rounded-md font-bold text-[10px] transition-colors ${
                    activeSection === 'music'
                      ? 'bg-[#5a000f] text-white shadow-sm ring-1 ring-white/40'
                      : 'bg-stone/30 text-stone-50 hover:text-white'
                  }`}
                >
                  Party 4
                </button>
                <button
                  onClick={() => handleSelectSection('labs')}
                  className={`py-1 px-1 rounded-md font-bold text-[10px] transition-colors ${
                    activeSection === 'labs'
                      ? 'bg-aubergine text-white shadow-sm'
                      : 'bg-stone/30 text-stone-50 hover:text-white'
                  }`}
                >
                  Labs
                </button>
                <button
                  onClick={() => handleSelectSection('mission')}
                  className={`py-1 px-1 rounded-md font-bold text-[10px] transition-colors ${
                    activeSection === 'mission'
                      ? 'bg-aubergine text-white shadow-sm ring-1 ring-white/40'
                      : 'bg-stone/30 text-stone-50 hover:text-white'
                  }`}
                >
                  Mission
                </button>
                <button
                  onClick={() => handleSelectSection('cards')}
                  className={`py-1 px-1 rounded-md font-bold text-[10px] transition-colors ${
                    activeSection === 'cards'
                      ? 'bg-aubergine text-white shadow-sm ring-1 ring-white/40'
                      : 'bg-stone/30 text-stone-50 hover:text-white'
                  }`}
                >
                  Cards
                </button>
                <button
                  onClick={() => handleSelectSection('footer')}
                  className={`py-1 px-1 rounded-md font-bold text-[10px] transition-colors ${
                    activeSection === 'footer'
                      ? 'bg-white text-black shadow-sm'
                      : 'bg-stone/30 text-stone-50 hover:text-white'
                  }`}
                >
                  Footer
                </button>
              </div>
            </div>

            {/* Background Zoom Slider (Hero only) */}
            {activeSection === 'hero' && (
              <div className="space-y-1.5 pt-0.5">
                <div className="flex justify-between text-[11px] text-stone-25">
                  <span>Background Zoom</span>
                  <span className="font-bold text-white">{zoom}%</span>
                </div>
                <input
                  type="range"
                  min="70"
                  max="120"
                  value={zoom}
                  onChange={(e) => setZoom(Number(e.target.value))}
                  className="w-full h-1.5 bg-stone/40 rounded-lg appearance-none cursor-pointer accent-aubergine"
                />
              </div>
            )}

            {/* Toggle Overlay */}
            <div className="flex items-center justify-between pt-1">
              <span className="text-stone-25">Reference Overlay:</span>
              <button
                onClick={() => setIsOverlayActive(!isOverlayActive)}
                className={`flex items-center space-x-1.5 px-3 py-1 rounded-full text-xs font-bold transition-colors ${
                  isOverlayActive
                    ? activeSection === 'quote' ? 'bg-tinderRed text-white' : 'bg-aubergine text-white'
                    : 'bg-stone/40 text-stone-50 hover:text-white'
                }`}
              >
                {isOverlayActive ? (
                  <>
                    <Eye className="w-3.5 h-3.5" />
                    <span>ON</span>
                  </>
                ) : (
                  <>
                    <EyeOff className="w-3.5 h-3.5" />
                    <span>OFF</span>
                  </>
                )}
              </button>
            </div>

            {/* Opacity Slider */}
            {isOverlayActive && (
              <div className="space-y-1.5 pt-1">
                <div className="flex justify-between text-[11px] text-stone-50">
                  <span>Overlay Opacity</span>
                  <span className="font-bold text-white">{opacity}%</span>
                </div>
                <input
                  type="range"
                  min="0"
                  max="100"
                  value={opacity}
                  onChange={(e) => setOpacity(Number(e.target.value))}
                  className="w-full h-1.5 bg-stone/40 rounded-lg appearance-none cursor-pointer accent-aubergine"
                />
              </div>
            )}

            {/* Blend Mode Toggle */}
            {isOverlayActive && (
              <div className="flex items-center justify-between pt-1">
                <span className="text-stone-25">Blend Mode:</span>
                <div className="flex space-x-1">
                  <button
                    onClick={() => setBlendMode('normal')}
                    className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                      blendMode === 'normal'
                        ? 'bg-white text-black'
                        : 'bg-stone/30 text-stone-50'
                    }`}
                  >
                    Normal
                  </button>
                  <button
                    onClick={() => setBlendMode('difference')}
                    className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                      blendMode === 'difference'
                        ? 'bg-white text-black'
                        : 'bg-stone/30 text-stone-50'
                    }`}
                  >
                    Difference
                  </button>
                </div>
              </div>
            )}

            {/* Replay Intro Animation Control */}
            {onReplayAnimation && (
              <div className="pt-1">
                <button
                  onClick={() => {
                    onReplayAnimation();
                    const el = document.getElementById('hero-section');
                    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                  }}
                  className="w-full flex items-center justify-center space-x-2 py-2 px-3 rounded-lg bg-gradient-to-r from-aubergine to-pink-900 hover:opacity-90 text-white font-bold text-xs transition-all shadow-md active:scale-95"
                >
                  <RotateCcw className="w-3.5 h-3.5 text-white" />
                  <span>Replay Load Animation</span>
                </button>
              </div>
            )}

            <p className="text-[10px] text-stone-50 pt-1 leading-tight">
              Toggle reference overlay 1:1 on top of the live page to inspect pixel perfection.
            </p>
          </div>
        )}
      </div>
    </>
  );
}
