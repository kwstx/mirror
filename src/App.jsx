import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import QuoteSection from './components/QuoteSection';
import HingeLabsSection from './components/HingeLabsSection';
import DoubleDateSection from './components/DoubleDateSection';
import FooterSection from './components/FooterSection';
import MobileMenu from './components/MobileMenu';
import ActionModal from './components/ActionModal';
import ReferenceOverlay from './components/ReferenceOverlay';

export default function App() {
  const [activeModal, setActiveModal] = useState(null);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [bgZoom, setBgZoom] = useState(100);
  const [animKey, setAnimKey] = useState(0);

  const handleOpenModal = (modalId) => {
    setActiveModal(modalId);
  };

  const handleCloseModal = () => {
    setActiveModal(null);
  };

  const handleReplayAnimation = () => {
    setAnimKey((prev) => prev + 1);
  };

  return (
    <div className="relative w-full min-h-screen bg-mirrorBlack font-modern overflow-x-hidden">
      {/* Top Navbar */}
      <Navbar
        onOpenModal={handleOpenModal}
        onToggleMobileMenu={() => setIsMobileMenuOpen(true)}
      />

      {/* Hero Landing Section with dynamic zoom & load animation */}
      <main>
        <Hero zoom={bgZoom} animKey={animKey} />
        {/* Pixel-Perfect Manifesto Section */}
        <QuoteSection />
        {/* Pixel-Perfect Hinge Labs Section */}
        <HingeLabsSection />
        {/* Pixel-Perfect Double Date (Party of four) Section */}
        <DoubleDateSection />
        {/* Pixel-Perfect Dark Hinge Footer Section */}
        <FooterSection onOpenModal={handleOpenModal} />
      </main>

      {/* Mobile Drawer Menu */}
      <MobileMenu
        isOpen={isMobileMenuOpen}
        onClose={() => setIsMobileMenuOpen(false)}
        onOpenModal={handleOpenModal}
      />

      {/* Interactive Detail Modals */}
      <ActionModal
        activeModal={activeModal}
        onClose={handleCloseModal}
      />

      {/* Pixel Comparison & Inspector Widget */}
      <ReferenceOverlay
        zoom={bgZoom}
        setZoom={setBgZoom}
        onReplayAnimation={handleReplayAnimation}
      />
    </div>
  );
}
