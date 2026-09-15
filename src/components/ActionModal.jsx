import React from 'react';
import { X, Heart, Sparkles, Award, Globe, Briefcase, Download, ExternalLink } from 'lucide-react';

export default function ActionModal({ activeModal, onClose }) {
  if (!activeModal) return null;

  const contentMap = {
    mission: {
      title: 'Our Philosophy',
      subtitle: 'Dating shouldn’t feel like shopping',
      icon: Heart,
      body: (
        <div className="space-y-4 text-stone-25 font-modern text-[14.5px] leading-relaxed">
          <p className="text-white font-tiempos text-xl leading-snug">
            Dating shouldn&rsquo;t feel like shopping.
          </p>
          <p>
            You shouldn&rsquo;t have to judge hundreds of faces, play games, or hope an algorithm eventually gets lucky. We believe finding someone should be about understanding people deeply&mdash;and making fewer, better introductions.
          </p>
          <p>
            We believe these three principles are what make better dating possible.
          </p>
          <div className="bg-[#242424] p-4 rounded-xl border border-stone/30 mt-4">
            <span className="text-xs uppercase tracking-widest text-aubergine-25 font-bold block mb-1">Our Philosophy</span>
            <p className="font-modern text-sm text-stone-50">
              Measuring success not by time spent in the app, but by genuine, lasting human connection in the real world.
            </p>
          </div>
        </div>
      ),
    },
    impact: {
      title: 'One More Hour',
      subtitle: 'Our commitment to social connection',
      icon: Globe,
      body: (
        <div className="space-y-4 text-stone-25 font-modern text-[15px] leading-relaxed">
          <p>
            Loneliness has become an epidemic among Gen Z and young adults. Through our <strong>One More Hour</strong> initiative, Cupid is mobilizing resources and grants to help people spend more time connecting in real life.
          </p>
          <p>
            We partner with community spaces, cultural venues, and local hubs to facilitate meaningful, tech-free human interactions.
          </p>
          <div className="grid grid-cols-2 gap-3 mt-4">
            <div className="bg-[#242424] p-3.5 rounded-xl border border-stone/30 text-center">
              <span className="font-tiempos text-2xl text-aubergine-25 block font-semibold">$5M+</span>
              <span className="text-xs text-stone-50">Social Connection Grants</span>
            </div>
            <div className="bg-[#242424] p-3.5 rounded-xl border border-stone/30 text-center">
              <span className="font-tiempos text-2xl text-aubergine-25 block font-semibold">1M+</span>
              <span className="text-xs text-stone-50">In-Person Hours Sparked</span>
            </div>
          </div>
        </div>
      ),
    },
    labs: {
      title: 'Cupid Labs',
      subtitle: 'Building a better way to date',
      icon: Sparkles,
      body: (
        <div className="space-y-4 text-stone-25 font-modern text-[15px] leading-relaxed">
          <p>
            Our in-house team of relationship researchers, behavioral scientists, and matchmakers study what makes daters click. We analyze date outcomes, communication patterns, and connection signals.
          </p>
          <p>
            Key findings from Cupid Labs have helped eliminate ghosting, introduce voice prompts, and develop "We Met" feedback to continually refine match quality.
          </p>
          <div className="bg-[#242424] p-4 rounded-xl border border-stone/30 mt-4">
            <span className="text-xs uppercase tracking-widest text-aubergine-25 font-bold block mb-1">Key Stat</span>
            <p className="font-tiempos text-base text-white">
              "3 out of 4 second dates on Cupid lead to ongoing relationships."
            </p>
          </div>
        </div>
      ),
    },
    newsroom: {
      title: 'Newsroom & Press',
      subtitle: 'Cupid in the headlines',
      icon: Award,
      body: (
        <div className="space-y-4 text-stone-25 font-modern text-[15px] leading-relaxed">
          <p>
            Access official press releases, brand assets, executive bios, and research publications from the Cupid team.
          </p>
          <div className="space-y-2 mt-4">
            <div className="p-3 bg-[#242424] rounded-lg border border-stone/30 flex items-center justify-between">
              <div>
                <span className="text-xs text-stone-50">September 2026</span>
                <p className="text-white text-sm font-medium">Cupid Expands Global Connection Initiative</p>
              </div>
              <ExternalLink className="w-4 h-4 text-stone-50" />
            </div>
            <div className="p-3 bg-[#242424] rounded-lg border border-stone/30 flex items-center justify-between">
              <div>
                <span className="text-xs text-stone-50">August 2026</span>
                <p className="text-white text-sm font-medium">Annual Dating Trends Report: Authenticity First</p>
              </div>
              <ExternalLink className="w-4 h-4 text-stone-50" />
            </div>
          </div>
        </div>
      ),
    },
    careers: {
      title: 'Work at Cupid',
      subtitle: "Let's work together",
      icon: Briefcase,
      body: (
        <div className="space-y-4 text-stone-25 font-modern text-[15px] leading-relaxed">
          <p>
            We are looking for passionate engineers, designers, researchers, and operators who want to make dating effective, not addictive.
          </p>
          <p>
            Enjoy flexible remote/hybrid hubs, generous wellness stipends, relationship coaching benefits, and meaningful equity.
          </p>
          <div className="bg-[#242424] p-4 rounded-xl border border-stone/30 mt-4 text-center">
            <p className="text-white font-medium mb-2">Explore Open Positions</p>
            <span className="inline-block bg-aubergine text-white text-xs font-bold px-4 py-2 rounded-full cursor-pointer hover:bg-aubergine/80 transition-colors">
              View 24 Open Roles
            </span>
          </div>
        </div>
      ),
    },
    download: {
      title: 'Download Cupid',
      subtitle: 'Scan with your phone to get the app',
      icon: Download,
      body: (
        <div className="space-y-4 text-stone-25 font-modern text-[15px] leading-relaxed text-center">
          <div className="mx-auto w-44 h-44 bg-white p-3 rounded-2xl flex items-center justify-center shadow-lg my-2">
            {/* SVG QR Code Simulation */}
            <svg viewBox="0 0 100 100" className="w-full h-full fill-black">
              <rect width="100" height="100" fill="white" />
              {/* Corner 1 */}
              <rect x="10" y="10" width="25" height="25" fill="#1a1a1a" />
              <rect x="14" y="14" width="17" height="17" fill="white" />
              <rect x="18" y="18" width="9" height="9" fill="#1a1a1a" />
              {/* Corner 2 */}
              <rect x="65" y="10" width="25" height="25" fill="#1a1a1a" />
              <rect x="69" y="14" width="17" height="17" fill="white" />
              <rect x="73" y="18" width="9" height="9" fill="#1a1a1a" />
              {/* Corner 3 */}
              <rect x="10" y="65" width="25" height="25" fill="#1a1a1a" />
              <rect x="14" y="69" width="17" height="17" fill="white" />
              <rect x="18" y="73" width="9" height="9" fill="#1a1a1a" />
              {/* Data matrix dots */}
              <rect x="42" y="12" width="6" height="6" fill="#1a1a1a" />
              <rect x="52" y="12" width="6" height="6" fill="#1a1a1a" />
              <rect x="42" y="22" width="6" height="6" fill="#1a1a1a" />
              <rect x="52" y="26" width="6" height="6" fill="#1a1a1a" />
              <rect x="12" y="42" width="6" height="6" fill="#1a1a1a" />
              <rect x="22" y="42" width="6" height="6" fill="#1a1a1a" />
              <rect x="32" y="42" width="6" height="6" fill="#1a1a1a" />
              <rect x="42" y="42" width="16" height="16" fill="#67295f" rx="3" />
              <rect x="65" y="42" width="6" height="6" fill="#1a1a1a" />
              <rect x="75" y="42" width="6" height="6" fill="#1a1a1a" />
              <rect x="85" y="42" width="6" height="6" fill="#1a1a1a" />
              <rect x="12" y="52" width="6" height="6" fill="#1a1a1a" />
              <rect x="65" y="52" width="6" height="6" fill="#1a1a1a" />
              <rect x="85" y="52" width="6" height="6" fill="#1a1a1a" />
              <rect x="42" y="65" width="6" height="6" fill="#1a1a1a" />
              <rect x="52" y="65" width="6" height="6" fill="#1a1a1a" />
              <rect x="75" y="65" width="6" height="6" fill="#1a1a1a" />
              <rect x="42" y="75" width="6" height="6" fill="#1a1a1a" />
              <rect x="65" y="75" width="6" height="6" fill="#1a1a1a" />
              <rect x="85" y="75" width="6" height="6" fill="#1a1a1a" />
              <rect x="42" y="85" width="6" height="6" fill="#1a1a1a" />
              <rect x="52" y="85" width="6" height="6" fill="#1a1a1a" />
              <rect x="75" y="85" width="6" height="6" fill="#1a1a1a" />
              <rect x="85" y="85" width="6" height="6" fill="#1a1a1a" />
            </svg>
          </div>
          <p className="text-xs text-stone-50">
            Available on iOS App Store & Google Play Store
          </p>
        </div>
      ),
    },
  };

  const item = contentMap[activeModal];
  if (!item) return null;

  const IconComponent = item.icon;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-sm animate-fade"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-lg bg-[#1a1a1a] border border-stone/30 rounded-2xl p-6 sm:p-8 shadow-2xl text-white overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Close Button */}
        <button
          onClick={onClose}
          aria-label="Close modal"
          className="absolute top-5 right-5 text-stone-50 hover:text-white transition-colors p-1"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Header */}
        <div className="flex items-center space-x-3 mb-4">
          <div className="w-10 h-10 rounded-full bg-aubergine/30 flex items-center justify-center text-aubergine-25">
            <IconComponent className="w-5 h-5" />
          </div>
          <div>
            <h3 className="font-tiempos text-2xl font-semibold text-white">
              {item.title}
            </h3>
            <p className="font-modern text-xs text-stone-50">{item.subtitle}</p>
          </div>
        </div>

        {/* Content Body */}
        <div className="mt-4">{item.body}</div>

        {/* Footer */}
        <div className="mt-6 pt-4 border-t border-stone/20 flex justify-end">
          <button
            onClick={onClose}
            className="font-modern text-xs font-semibold px-4 py-2 rounded-full bg-stone/30 hover:bg-stone/50 text-white transition-colors"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
