/* EL-SHIMY site script: nav, reveals, product filters, quote form. No dependencies. */
(function () {
  'use strict';
  var doc = document, root = doc.documentElement;
  root.classList.add('js');
  /* Analytics: push events to the GTM dataLayer. No personal data (names, emails) is ever pushed. */
  var dl = window.dataLayer = window.dataLayer || [];
  var track = function (name, params) { var o = { event: name, page_language: root.lang || '' }; for (var k in params) o[k] = params[k]; dl.push(o); };
  doc.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]'); if (!a) return;
    var h = a.getAttribute('href') || '', m = null;
    if (h.indexOf('tel:') === 0) m = 'phone'; else if (h.indexOf('mailto:') === 0) m = 'email'; else if (h.indexOf('wa.me') > -1) m = 'whatsapp';
    else if (h.indexOf('linkedin.com') > -1) m = 'linkedin'; else if (h.indexOf('maps.app.goo.gl') > -1 || h.indexOf('google.com/maps') > -1) m = 'map';
    if (m) { track('contact_click', { contact_method: m, link_location: a.closest('footer') ? 'footer' : 'page' }); return; }
    if (a.classList.contains('lang')) track('language_switch', { to_language: a.getAttribute('hreflang') || '' });
    else if (/\/contact\/(\?|$)/.test(h)) track('quote_cta_click', { link_text: (a.textContent || '').trim().slice(0, 60), link_url: h });
  });

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Mobile navigation */
  var btn = doc.querySelector('.menu-btn'), nav = doc.getElementById('nav');
  if (btn && nav) {
    var set = function (open) { nav.classList.toggle('open', open); btn.setAttribute('aria-expanded', String(open)); };
    btn.addEventListener('click', function () { set(!nav.classList.contains('open')); });
    doc.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { set(false); btn.focus(); } });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) set(false); });
  }

  /* Scroll reveal */
  var items = doc.querySelectorAll('.reveal');
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    items.forEach(function (el) { io.observe(el); });
  } else { items.forEach(function (el) { el.classList.add('in'); }); }

  /* Product filters (cards are server-rendered, so everything is crawlable without JS) */
  var groups = doc.getElementById('p-groups');
  if (groups) {
    var state = { cat: 'all', form: 'all', q: '' };
    var qp = new URLSearchParams(location.search);
    if (['veg', 'fruit', 'frozen'].indexOf(qp.get('cat')) > -1) state.cat = qp.get('cat');
    var cards = Array.prototype.slice.call(groups.querySelectorAll('.card'));
    var empty = doc.getElementById('p-empty'), search = doc.getElementById('p-search');
    var match = function (c, st) {
      return (st.cat === 'all' || c.dataset.cat === st.cat) && (st.form === 'all' || c.dataset.form === st.form) && (!st.q || c.dataset.name.indexOf(st.q) > -1);
    };
    var setChip = function (b, count, pressed) {
      var cnt = b.querySelector('.cnt');
      if (!cnt) { cnt = doc.createElement('span'); cnt.className = 'cnt'; b.appendChild(cnt); }
      cnt.textContent = count;
      b.setAttribute('aria-pressed', String(pressed));
      /* a chip that would give zero results with the other active filters is disabled instead of leading to an empty page */
      var dead = count === 0 && !pressed;
      b.classList.toggle('is-off', dead);
      if (dead) b.setAttribute('aria-disabled', 'true'); else b.removeAttribute('aria-disabled');
    };
    var apply = function () {
      var shown = 0;
      cards.forEach(function (c) { var ok = match(c, state); c.hidden = !ok; if (ok) shown++; });
      groups.querySelectorAll('.group').forEach(function (g) { g.hidden = !g.querySelector('.card:not([hidden])'); });
      empty.hidden = shown > 0;
      doc.querySelectorAll('[data-filter-cat]').forEach(function (b) {
        var k = b.dataset.filterCat, n = cards.filter(function (c) { return match(c, { cat: k, form: state.form, q: state.q }); }).length;
        setChip(b, n, k === state.cat);
      });
      doc.querySelectorAll('[data-filter-form]').forEach(function (b) {
        var k = b.dataset.filterForm, n = cards.filter(function (c) { return match(c, { cat: state.cat, form: k, q: state.q }); }).length;
        setChip(b, n, k === state.form);
      });
    };
    var pick = function (key) { return function () { if (this.getAttribute('aria-disabled') === 'true') return; state[key] = this.dataset[key === 'cat' ? 'filterCat' : 'filterForm']; apply(); }; };
    doc.querySelectorAll('[data-filter-cat]').forEach(function (b) { b.addEventListener('click', pick('cat')); });
    doc.querySelectorAll('[data-filter-form]').forEach(function (b) { b.addEventListener('click', pick('form')); });
    search.addEventListener('input', function () { state.q = search.value.trim().toLowerCase(); apply(); });
    var reset = doc.getElementById('p-reset');
    if (reset) reset.addEventListener('click', function () { state.cat = 'all'; state.form = 'all'; state.q = ''; search.value = ''; apply(); });
    apply();
  }

  /* Quote form */
  var form = doc.getElementById('quote-form');
  if (form) {
    var M = JSON.parse(form.dataset.msgs);
    var summary = doc.getElementById('form-summary'), status = doc.getElementById('form-status');
    var pre = new URLSearchParams(location.search).get('product');
    var sel = form.elements.product;
    if (pre && sel.querySelector('option[value="' + pre.replace(/[^a-z0-9-]/gi, '') + '"]')) sel.value = pre.replace(/[^a-z0-9-]/gi, '');

    /* Topic prefill (?topic=freight|sea|air|land|quality|certificate, ?tpl=1) */
    var qs = new URLSearchParams(location.search), msgEl = form.elements.message, topic = qs.get('topic');
    try {
      var topics = JSON.parse(form.dataset.topics || '{}');
      if (msgEl && !msgEl.value) {
        if (qs.get('tpl')) msgEl.value = JSON.parse(form.dataset.tpl || '""');
        else if (topic && Object.prototype.hasOwnProperty.call(topics, topic) && topics[topic]) msgEl.value = topics[topic] + (topic === 'certificate' ? '' : '\n');
      }
      if (topic && !pre && ['freight', 'sea', 'air', 'land', 'quality', 'certificate'].indexOf(topic) > -1 && !sel.value) sel.value = 'other';
    } catch (err) { /* prefill is a convenience only */ }

    var fieldErr = function (el) {
      var msg = '';
      if (el.required && !el.value.trim()) msg = M.required;
      else if (el.type === 'email' && el.value && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(el.value.trim())) msg = M.email;
      var box = doc.getElementById(el.id + '-err');
      if (box) { box.textContent = msg; box.hidden = !msg; }
      el.setAttribute('aria-invalid', msg ? 'true' : 'false');
      el.closest('.field').classList.toggle('invalid', !!msg);
      return msg;
    };
    form.querySelectorAll('input[required],select[required],input[type=email]').forEach(function (el) {
      el.addEventListener('blur', function () { fieldErr(el); });
      el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') fieldErr(el); });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.textContent = ''; status.className = 'status';
      var bad = [];
      form.querySelectorAll('input,select,textarea').forEach(function (el) {
        if (el.name === 'website') return;
        if (fieldErr(el)) bad.push(el);
      });
      if (bad.length) {
        summary.hidden = false;
        summary.innerHTML = M.summary + '<ul>' + bad.map(function (el) { return '<li><a href="#' + el.id + '">' + form.querySelector('label[for=' + el.id + ']').textContent.replace('*', '').trim() + '</a></li>'; }).join('') + '</ul>';
        summary.focus(); return;
      }
      summary.hidden = true;
      if (form.elements.website.value) return; /* honeypot */
      track('generate_lead', { lead_product: form.elements.product.value, lead_method: form.dataset.endpoint ? 'form' : 'email_draft', lead_topic: new URLSearchParams(location.search).get('topic') || '' });
      var data = {}; new FormData(form).forEach(function (v, k) { if (k !== 'website') data[k] = v; });
      data.product_label = sel.options[sel.selectedIndex].text; data.language = form.dataset.lang; data.page = location.href;
      var endpoint = form.dataset.endpoint, submit = form.querySelector('[type=submit]');
      if (endpoint) {
        submit.disabled = true; status.textContent = M.sending;
        fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
          .then(function (r) { if (!r.ok) throw new Error(r.status); status.textContent = M.ok_endpoint; status.className = 'status ok'; form.reset(); })
          .catch(function () { status.innerHTML = M.fail + ' <a href="mailto:' + M.email_addr + '">' + M.email_addr + '</a>.'; status.className = 'status bad'; })
          .then(function () { submit.disabled = false; });
      } else {
        /* No form backend configured: open a pre-filled email draft instead of pretending the message was sent. */
        var body = ['Name: ' + data.name, 'Company: ' + data.company, 'Email: ' + data.email, 'Phone: ' + (data.phone || '-'), 'Country: ' + data.country,
                    'Product: ' + data.product_label, 'Quantity: ' + (data.qty || '-'), '', data.message || ''].join('\n');
        location.href = 'mailto:' + form.dataset.email + '?subject=' + encodeURIComponent('Quote request: ' + data.product_label) + '&body=' + encodeURIComponent(body);
        status.innerHTML = M.ok_mailto + ' <a href="mailto:' + M.email_addr + '">' + M.email_addr + '</a>.'; status.className = 'status ok';
      }
    });
  }

  /* Copy-to-clipboard buttons */
  doc.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = doc.querySelector(b.dataset.copy); if (!t) return;
      var done = function () { var old = b.innerHTML; b.textContent = b.dataset.done; setTimeout(function () { b.innerHTML = old; }, 1800); };
      var legacy = function () { var r = doc.createRange(); r.selectNodeContents(t); var s = getSelection(); s.removeAllRanges(); s.addRange(r); try { if (doc.execCommand('copy')) done(); } catch (e) { /* selection stays visible so the user can copy manually */ } };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t.textContent).then(done, legacy);
      else legacy();
    });
  });
})();
