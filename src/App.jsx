import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import QuoteSection from './components/QuoteSection';
import HingeLabsSection from './components/HingeLabsSection';
import DoubleDateSection from './components/DoubleDateSection';
import FooterSection from './components/FooterSection';
import MobileMenu from './components/MobileMenu';
import ActionModal from './components/ActionModal';
import ReferenceOverlay from './components/ReferenceOverlay';
import MissionPage from './components/MissionPage';

export default function App() {
  const getInitialPage = () => {
    if (typeof window === 'undefined') return 'home';
    const path = window.location.pathname.toLowerCase();
    const hash = window.location.hash.toLowerCase();
    if (path.includes('mission') || hash.includes('mission')) {
      return 'mission';
    }
    return 'home';
  };

  const [currentPage, setCurrentPage] = useState(getInitialPage);
  const [activeModal, setActiveModal] = useState(null);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [bgZoom, setBgZoom] = useState(100);
  const [animKey, setAnimKey] = useState(0);

  useEffect(() => {
    const handlePopState = () => {
      const path = window.location.pathname.toLowerCase();
      const hash = window.location.hash.toLowerCase();
      if (path.includes('mission') || hash.includes('mission')) {
        setCurrentPage('mission');
      } else {
        setCurrentPage('home');
      }
    };

    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, []);

  const handleNavigate = (page, targetSectionId = null) => {
    setCurrentPage(page);
    const newPath = page === 'mission' ? '/mission' : '/';
    if (window.location.pathname !== newPath) {
      window.history.pushState({}, '', newPath);
    }
    if (page === 'home') {
      if (targetSectionId) {
        setTimeout(() => {
          const el = document.getElementById(targetSectionId);
          if (el) el.scrollIntoView({ behavior: 'smooth' });
        }, 80);
      } else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    } else if (page === 'mission') {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

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
    <div className={`relative w-full min-h-screen ${currentPage === 'mission' ? 'bg-white text-[#1a1a1a]' : 'bg-mirrorBlack text-white'} font-modern overflow-x-hidden transition-colors duration-200`}>
      {/* Top Navbar */}
      <Navbar
        currentPage={currentPage}
        onNavigate={handleNavigate}
        onOpenModal={handleOpenModal}
        onToggleMobileMenu={() => setIsMobileMenuOpen(true)}
      />

      {/* Main Content: Completely Separate Mission Page vs Home Landing Page */}
      {currentPage === 'mission' ? (
        <MissionPage
          onNavigate={handleNavigate}
          onOpenModal={handleOpenModal}
        />
      ) : (
        <main>
          {/* Hero Landing Section with dynamic zoom & load animation */}
          <Hero zoom={bgZoom} animKey={animKey} />
          {/* Pixel-Perfect Manifesto Section */}
          <QuoteSection />
          {/* Pixel-Perfect Hinge Labs Section */}
          <HingeLabsSection />
          {/* Pixel-Perfect Double Date (Party of four) Section */}
          <DoubleDateSection />
          {/* Pixel-Perfect Dark Hinge Footer Section */}
          <FooterSection onOpenModal={handleOpenModal} onNavigate={handleNavigate} />
        </main>
      )}

      {/* Mobile Drawer Menu */}
      <MobileMenu
        isOpen={isMobileMenuOpen}
        onClose={() => setIsMobileMenuOpen(false)}
        onOpenModal={handleOpenModal}
        onNavigate={handleNavigate}
      />

      {/* Interactive Detail Modals */}
      <ActionModal
        activeModal={activeModal}
        onClose={handleCloseModal}
      />

      {/* Pixel Comparison & Inspector Widget */}
      <ReferenceOverlay
        currentPage={currentPage}
        onNavigate={handleNavigate}
        zoom={bgZoom}
        setZoom={setBgZoom}
        onReplayAnimation={handleReplayAnimation}
      />
    </div>
  );
}
