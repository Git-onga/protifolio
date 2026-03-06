/* ===================================================================
   Bildad Gitonga — Portfolio JavaScript
   Hamburger menu, smooth scroll, scroll reveal, typed text, active nav
   =================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  /* ── Elements ────────────────────────────────────────────────────── */
  const header     = document.querySelector('.header');
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks   = document.querySelector('.nav-links');
  const navAnchors = document.querySelectorAll('.nav-links a');
  const sections   = document.querySelectorAll('section[id]');
  const reveals    = document.querySelectorAll('.reveal, .reveal-left, .reveal-right');
  const typedEl    = document.getElementById('typed-text');

  /* ── Hamburger Menu ──────────────────────────────────────────────── */
  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      navLinks.classList.toggle('open');
      document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
    });

    // Close menu when a link is clicked
    navAnchors.forEach(link => {
      link.addEventListener('click', () => {
        menuToggle.classList.remove('active');
        navLinks.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ── Header Scroll Effect ────────────────────────────────────────── */
  const onScroll = () => {
    if (window.scrollY > 60) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ── Active Nav Highlighting ─────────────────────────────────────── */
  const highlightNav = () => {
    const scrollY = window.scrollY + 120;

    sections.forEach(section => {
      const top    = section.offsetTop;
      const height = section.offsetHeight;
      const id     = section.getAttribute('id');

      if (scrollY >= top && scrollY < top + height) {
        navAnchors.forEach(a => a.classList.remove('active'));
        const active = document.querySelector(`.nav-links a[href="#${id}"]`);
        if (active) active.classList.add('active');
      }
    });
  };
  window.addEventListener('scroll', highlightNav, { passive: true });
  highlightNav();

  /* ── Scroll Reveal (IntersectionObserver) ─────────────────────────── */
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    reveals.forEach(el => observer.observe(el));
  } else {
    // Fallback: show everything if IO not supported
    reveals.forEach(el => el.classList.add('revealed'));
  }

  /* ── Typed Text Effect ───────────────────────────────────────────── */
  if (typedEl) {
    const roles = [
      'IT Student',
      'Certified 3D Animator',
      'Mobile App Developer',
      'UI/UX Designer',
      'Machine Learning Enthusiast'
    ];
    let roleIndex  = 0;
    let charIndex  = 0;
    let isDeleting = false;
    const TYPING_SPEED   = 80;
    const DELETING_SPEED = 40;
    const PAUSE_AFTER    = 2000;

    function typeEffect() {
      const currentRole = roles[roleIndex];

      if (isDeleting) {
        typedEl.textContent = currentRole.substring(0, charIndex - 1);
        charIndex--;
      } else {
        typedEl.textContent = currentRole.substring(0, charIndex + 1);
        charIndex++;
      }

      let delay = isDeleting ? DELETING_SPEED : TYPING_SPEED;

      if (!isDeleting && charIndex === currentRole.length) {
        delay = PAUSE_AFTER;
        isDeleting = true;
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        delay = 400;
      }

      setTimeout(typeEffect, delay);
    }

    typeEffect();
  }

  /* ── Smooth Scroll for anchor links ──────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });
});
