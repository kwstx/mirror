import React from 'react';
import { X } from 'lucide-react';

export default function MobileMenu({ isOpen, onClose, onOpenModal, onNavigate }) {
  if (!isOpen) return null;

  const links = [
    { id: 'mission', label: 'Mission' },
    { id: 'impact', label: 'Impact' },
    { id: 'labs', label: 'Labs' },
    { id: 'newsroom', label: 'Newsroom' },
    { id: 'careers', label: 'Careers' },
  ];

  return (
    <div className="fixed inset-0 z-50 bg-[#1a1a1a] flex flex-col justify-between p-6 md:hidden animate-fade">
      {/* Header */}
      <div className="flex items-center justify-between pb-6 border-b border-stone/30">
        <div className="flex items-center">
          <span
            onClick={() => {
              onClose();
              if (onNavigate) onNavigate('home');
            }}
            className="font-tiempos font-bold text-[28px] tracking-[-0.02em] leading-none text-white select-none cursor-pointer"
          >
            Cupid
          </span>
        </div>
        <button
          onClick={onClose}
          aria-label="Close menu"
          className="text-white p-2 hover:opacity-75 focus:outline-none"
        >
          <X className="w-6 h-6" />
        </button>
      </div>

      {/* Nav List */}
      <div className="flex flex-col py-8 space-y-6">
        {links.map((link) => (
          <button
            key={link.id}
            onClick={() => {
              onClose();
              if (link.id === 'mission') {
                if (onNavigate) onNavigate('mission');
                else onOpenModal('mission');
                return;
              }
              if (link.id === 'labs') {
                if (onNavigate) {
                  onNavigate('home', 'labs-section');
                } else {
                  const el = document.getElementById('labs-section');
                  if (el) el.scrollIntoView({ behavior: 'smooth' });
                  else onOpenModal('labs');
                }
                return;
              }
              onOpenModal(link.id);
            }}
            className="text-left font-tiempos text-3xl font-normal text-white hover:text-aubergine-25 py-2 border-b border-stone/20 transition-colors focus:outline-none"
          >
            {link.label}
          </button>
        ))}
      </div>

      {/* Bottom CTA */}
      <div className="pt-6 border-t border-stone/30 space-y-4">
        <button
          onClick={() => {
            onClose();
            onOpenModal('waitlist');
          }}
          className="w-full font-modern font-bold text-center bg-white text-mirrorBlack py-3.5 rounded-full hover:bg-aubergine hover:text-white transition-colors"
        >
          Join waitlist
        </button>
        <p className="font-modern text-xs text-stone-50 text-center">
          © 2026 Cupid Inc. Designed to be deleted.
        </p>
      </div>
    </div>
  );
}
