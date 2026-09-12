import React, { useState } from 'react';
import { Sliders, Eye, EyeOff, Layers, CheckCircle2 } from 'lucide-react';

export default function ReferenceOverlay({ zoom, setZoom }) {
  const [isOpen, setIsOpen] = useState(false);
  const [opacity, setOpacity] = useState(50);
  const [isOverlayActive, setIsOverlayActive] = useState(false);
  const [blendMode, setBlendMode] = useState('normal'); // 'normal' or 'difference'

  return (
    <>
      {/* Reference Image Layer Overlay */}
      {isOverlayActive && (
        <div
          className="fixed inset-0 z-30 pointer-events-none select-none transition-opacity duration-150"
          style={{
            opacity: opacity / 100,
            mixBlendMode: blendMode,
          }}
        >
          <img
            src="/images/reference.jpg"
            alt="Reference screenshot"
            className="w-full h-full object-cover object-center"
          />
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

            {/* Background Zoom Slider */}
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

            {/* Toggle Overlay */}
            <div className="flex items-center justify-between pt-1">
              <span className="text-stone-25">Reference Overlay:</span>
              <button
                onClick={() => setIsOverlayActive(!isOverlayActive)}
                className={`flex items-center space-x-1.5 px-3 py-1 rounded-full text-xs font-bold transition-colors ${
                  isOverlayActive
                    ? 'bg-aubergine text-white'
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

            <p className="text-[10px] text-stone-50 pt-1 leading-tight">
              Adjust background zoom or toggle the reference overlay 1:1 on top of live rendered HTML elements.
            </p>
          </div>
        )}
      </div>
    </>
  );
}
