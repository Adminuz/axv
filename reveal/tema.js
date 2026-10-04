/* Qorong'i (VS Code Dark+) / yorug' (Light+) mavzu almashtirgich va slaydlarni telefonga moslash.
   <head> ichida ulanadi (miltillashsiz). Tugma sahifa yuklangach qo'yiladi:
   sahifada `.theme-slot` bo'lsa shu yerga, bo'lmasa o'ng yuqori burchakka (slaydlar). Klaviatura: T tugmasi. */
(function () {
  var KEY = 'vitepress-theme-appearance'; // VitePress bilan bir xil kalit: sayt va slaydlar mavzusi umumiy
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function cur() { return document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark'; }
  function apply(v) { document.documentElement.setAttribute('data-theme', v === 'light' ? 'light' : 'dark'); }
  function toggle() { var n = cur() === 'light' ? 'dark' : 'light'; set(n); apply(n); }
  apply(get());

  var MOON = '<svg class="moon" viewBox="0 0 24 24"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';
  var SUN = '<svg class="sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';

  document.addEventListener('DOMContentLoaded', function () {
    var b = document.createElement('button');
    b.className = 'theme-toggle';
    b.type = 'button';
    b.title = "Qorong'i / yorug' mavzu (T)";
    b.setAttribute('aria-label', 'Mavzuni almashtirish');
    b.innerHTML = MOON + SUN;
    b.addEventListener('click', function (e) { e.stopPropagation(); toggle(); });
    // Reveal tugma bosilishini slayd almashtirish deb tushunmasligi uchun
    ['touchstart', 'touchend', 'pointerdown'].forEach(function (ev) { b.addEventListener(ev, function (e) { e.stopPropagation(); }); });
    var slot = document.querySelector('.theme-slot');
    if (slot) { b.classList.add('in-page'); slot.appendChild(b); } else { document.body.appendChild(b); }
  });

  document.addEventListener('keydown', function (e) {
    if ((e.key === 't' || e.key === 'T') && !e.ctrlKey && !e.metaKey && !e.altKey &&
        !/INPUT|TEXTAREA|SELECT/.test((e.target || {}).tagName || '')) { toggle(); }
  });

  /* ---- Slaydlarni ekranga moslash (faqat Reveal bor sahifalarda) ----
     Keng ekran: 1280x720. Telefon (vertikal): mantiqiy kenglik 760, balandlik ekran nisbatiga qarab. */
  function adapt() {
    if (!window.Reveal || !Reveal.isReady || !Reveal.isReady()) return;
    var w = window.innerWidth, h = window.innerHeight;
    var portrait = h > w * 1.05 && w < 900;
    var cw = portrait ? 760 : 1280;
    var ch = portrait ? Math.max(900, Math.round(760 * h / w)) : 720;
    var c = Reveal.getConfig();
    if (c.width !== cw || c.height !== ch) {
      Reveal.configure({ width: cw, height: ch, margin: portrait ? 0.05 : 0.06 });
    }
    // gorizontal aylanadigan illyustratsiyada surish slayd almashtirmasin
    document.querySelectorAll('.illus').forEach(function (el) {
      el.setAttribute('data-prevent-swipe', '');
      var hint = el.nextElementSibling && el.nextElementSibling.classList.contains('illus-hint') ? el.nextElementSibling : null;
      if (portrait && !hint) {
        hint = document.createElement('div');
        hint.className = 'illus-hint';
        hint.textContent = "\u2194 Sxemani suring yoki telefonni yoting";
        el.parentNode.insertBefore(hint, el.nextSibling);
      }
      if (hint) hint.style.display = portrait ? '' : 'none';
    });
  }
  window.addEventListener('load', function () {
    if (!window.Reveal) return;
    if (Reveal.isReady()) adapt(); else Reveal.on('ready', adapt);
    window.addEventListener('resize', function () { setTimeout(adapt, 50); });
    window.addEventListener('orientationchange', function () { setTimeout(adapt, 250); });
  });
})();
