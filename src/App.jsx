import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import MobileMenu from './components/MobileMenu';
import ActionModal from './components/ActionModal';
import ReferenceOverlay from './components/ReferenceOverlay';

export default function App() {
  const [activeModal, setActiveModal] = useState(null);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const handleOpenModal = (modalId) => {
    setActiveModal(modalId);
  };

  const handleCloseModal = () => {
    setActiveModal(null);
  };

  return (
    <div className="relative w-full min-h-screen bg-hingeBlack font-modern overflow-x-hidden">
      {/* Top Navbar */}
      <Navbar
        onOpenModal={handleOpenModal}
        onToggleMobileMenu={() => setIsMobileMenuOpen(true)}
      />

      {/* Hero Landing Section */}
      <main>
        <Hero />
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
      <ReferenceOverlay />
    </div>
  );
}
