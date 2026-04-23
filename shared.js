/* ═══════════════════════════════════════════
   EL-SHIMY — Shared JavaScript
   ═══════════════════════════════════════════ */

(function () {
  const nav = document.getElementById('nav');
  const scrollTop = document.getElementById('scroll-top');
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');

  /* Sticky nav + scroll-to-top visibility */
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 20);
    if (scrollTop) scrollTop.classList.toggle('visible', window.scrollY > 400);
  });

  /* Hamburger */
  if (hamburger) {
    hamburger.addEventListener('click', () => mobileMenu.classList.toggle('open'));
    document.querySelectorAll('.mobile-link').forEach(link =>
      link.addEventListener('click', () => mobileMenu.classList.remove('open'))
    );
  }

  /* Scroll-to-top */
  if (scrollTop) scrollTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* Fade-in on scroll */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  /* 3D Tilt Cards */
  document.querySelectorAll('.tilt-card').forEach(card => {
    card.addEventListener('mouseenter', () => { card.style.transition = 'transform .08s ease-out'; });
    card.addEventListener('mousemove', (e) => {
      const r = card.getBoundingClientRect();
      const rx = (((e.clientY - r.top)  / r.height) - .5) * -18;
      const ry = (((e.clientX - r.left) / r.width)  - .5) *  18;
      card.style.transform = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg) translateZ(10px) scale(1.02)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transition = 'transform .45s ease-out';
      card.style.transform  = 'perspective(900px) rotateX(0) rotateY(0) translateZ(0) scale(1)';
    });
  });

  /* Animated stat counters */
  function animateCounter(el) {
    const target = parseFloat(el.dataset.target);
    const suffix = el.dataset.suffix || '';
    const prefix = el.dataset.prefix || '';
    const decimals = el.dataset.decimals ? parseInt(el.dataset.decimals) : 0;
    const duration = 1800;
    const step = 16;
    const increment = target / (duration / step);
    let current = 0;
    const timer = setInterval(() => {
      current += increment;
      if (current >= target) { current = target; clearInterval(timer); }
      el.textContent = prefix + (decimals ? current.toFixed(decimals) : Math.floor(current)) + suffix;
    }, step);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting && !e.target.dataset.counted) {
        e.target.dataset.counted = '1';
        animateCounter(e.target);
      }
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('[data-target]').forEach(el => counterObserver.observe(el));

  /* Quote form */
  const form = document.getElementById('quote-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = form.querySelector('.form-submit');
      btn.innerHTML = '<span class="material-symbols-outlined" style="font-size:20px">check_circle</span> Inquiry Sent!';
      btn.style.background = '#25D366'; btn.style.color = '#fff'; btn.disabled = true;
      setTimeout(() => {
        btn.innerHTML = '<span class="material-symbols-outlined" style="font-size:20px">send</span> Send Inquiry';
        btn.style.background = ''; btn.style.color = ''; btn.disabled = false;
        form.reset();
      }, 4000);
    });
  }

  /* Season tabs (products page) */
  document.querySelectorAll('.season-tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.season-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.season-panel').forEach(p => p.classList.remove('active'));
      tab.classList.add('active');
      const panel = document.getElementById('panel-' + tab.dataset.season);
      if (panel) panel.classList.add('active');
    });
  });

  /* FAQ accordion */
  document.querySelectorAll('.faq-item').forEach(item => {
    const question = item.querySelector('.faq-question');
    if (question) {
      question.addEventListener('click', () => {
        const isOpen = item.classList.contains('open');
        document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
        if (!isOpen) item.classList.add('open');
      });
    }
  });

  /* Active nav highlight based on current page */
  const page = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    if (a.getAttribute('href') === page) a.classList.add('active');
  });

})();
