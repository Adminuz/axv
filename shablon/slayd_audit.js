/* Slaydlarni avtomatik tekshirish (brauzerda ishlaydi).
 *
 * Ishlatish: loyiha papkasini `python3 -m http.server 8767` bilan oching, brauzer sahifasida (shu origin):
 *   const src = await (await fetch('/shablon/slayd_audit.js')).text(); eval(src);
 *   const res = await auditFile('/8-sinf/haftalik/hafta-01/dars-1-slayd.html', {mobile:false});
 * `mobile:true` telefon (375x812, vertikal) ko'rinishini tekshiradi.
 *
 * Har slaydda (barcha fragmentlar ochilgan holda) topadi:
 *   overflow     element ekran chegarasidan chiqib ketgan
 *   clipped      matn quti ichida kesilgan (overflow hidden/scroll bilan sig'maydi)
 *   overlap      ikki matn bloki bir-birini bosgan
 *   svg-clip     SVG matni o'z rasmidan tashqariga chiqqan
 *   svg-overlap  SVG ichida ikki matn bir-birini bosgan
 *   tiny         matn juda kichik (haqiqiy o'lcham < 12 px)
 *   icon         ikonka topilmagan yoki rasm yuklanmagan
 *   fragment     fragment oxirigacha ochilgandan keyin ham ko'rinmaydi
 *   empty        slaydda deyarli matn yo'q
 */
async function auditFile(url, opts = {}) {
  const mobile = !!opts.mobile;
  const fr = document.createElement('iframe');
  fr.style.cssText = `position:fixed;left:0;top:0;width:${mobile ? 375 : 1280}px;height:${mobile ? 812 : 720}px;opacity:0;pointer-events:none;border:0`;
  fr.src = url;
  document.body.appendChild(fr);
  await new Promise(r => (fr.onload = r));
  await new Promise(r => setTimeout(r, 1000));
  const win = fr.contentWindow, d = fr.contentDocument, R = win.Reveal;
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const out = { url, mobile, slides: 0, issues: [] };
  if (!R) { out.issues.push({ s: '-', type: 'fatal', msg: 'Reveal yuklanmadi' }); fr.remove(); return out; }
  R.configure({ transition: 'none', backgroundTransition: 'none', autoAnimate: false });
  const st = d.createElement('style');
  st.textContent = '*{transition:none !important;animation:none !important}';
  d.head.appendChild(st);
  const W = win.innerWidth, H = win.innerHeight;
  const desc = e => (e.tagName.toLowerCase() + (e.className && e.className.baseVal === undefined && e.className ? '.' + String(e.className).trim().split(/\s+/).slice(0, 2).join('.') : '')) +
    (e.textContent ? ' «' + e.textContent.trim().replace(/\s+/g, ' ').slice(0, 28) + '»' : '');
  const visible = e => { const cs = win.getComputedStyle(e); return cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0'; };
  const inter = (a, b) => Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)) * Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
  const area = r => Math.max(1, r.width * r.height);

  const hs = R.getHorizontalSlides();
  for (let h = 0; h < hs.length; h++) {
    const vs = hs[h].querySelectorAll(':scope > section');
    const nv = Math.max(1, vs.length);
    for (let v = 0; v < nv; v++) {
      R.slide(h, v, 99);
      await sleep(130);
      out.slides++;
      const pres = d.querySelector('.slides section.present:not(.stack)');
      if (!pres) continue;
      const title = (pres.querySelector('h1,h2,h3')?.textContent || '').trim().slice(0, 40);
      const S = `${h + 1}${vs.length ? '.' + (v + 1) : ''} «${title}»`;
      const add = (type, msg) => out.issues.push({ s: S, type, msg });

      const all = [...pres.querySelectorAll('*')].filter(e => !e.closest('aside'));
      // overflow
      for (const e of all) {
        if (!visible(e)) continue;
        if (e.closest('svg') && e.tagName.toLowerCase() !== 'svg') continue;
        if (mobile && e.closest('.illus')) continue;
        if (e.closest('pre') && e.tagName.toLowerCase() !== 'pre') continue;
        const r = e.getBoundingClientRect();
        if (r.width === 0 && r.height === 0) continue;
        const o = Math.max(r.bottom - H, r.right - W, -r.top, -r.left);
        if (o > 2) { add('overflow', `${desc(e)} chegaradan +${Math.round(o)}px`); break; }
      }
      // clipped
      for (const e of all) {
        if (!visible(e)) continue;
        const tag = e.tagName.toLowerCase();
        if (['svg', 'pre', 'code', 'section', 'html', 'body'].includes(tag) || e.closest('svg') || e.closest('pre')) continue;
        if (mobile && e.closest('.illus')) continue;
        const cs = win.getComputedStyle(e);
        const clip = ['hidden', 'auto', 'scroll', 'clip'];
        if ((clip.includes(cs.overflowX) && e.scrollWidth > e.clientWidth + 3) || (clip.includes(cs.overflowY) && e.scrollHeight > e.clientHeight + 3)) {
          add('clipped', `${desc(e)} (${e.scrollWidth}x${e.scrollHeight} > ${e.clientWidth}x${e.clientHeight})`); break;
        }
      }
      // HTML matn bloklari bir-birini bosgan
      const leaves = all.filter(e => visible(e) && !e.closest('svg') && !e.closest('pre') && !e.closest('.flip') && !e.closest('.stepper .stp:not(.on)') &&
        [...e.childNodes].some(n => n.nodeType === 3 && n.nodeValue.trim().length > 1) &&
        !['svg', 'code', 'strong', 'em', 'b', 'i', 'span', 'a', 'sub', 'sup', 'kbd', 'mark'].includes(e.tagName.toLowerCase()));
      for (let i = 0; i < leaves.length; i++) {
        for (let j = i + 1; j < leaves.length; j++) {
          const a = leaves[i], b = leaves[j];
          if (a.contains(b) || b.contains(a)) continue;
          const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
          const ia = inter(ra, rb);
          if (ia > 0.3 * Math.min(area(ra), area(rb)) && ia > 150) { add('overlap', `${desc(a)} ↔ ${desc(b)}`); i = leaves.length; break; }
        }
      }
      // SVG
      const svgs = [...pres.querySelectorAll('svg')].filter(s => !s.classList.contains('ic') && !s.closest('svg:not(:scope)') && s.parentElement.closest('svg') === null && s.querySelector('text'));
      for (const sv of svgs) {
        const sr = sv.getBoundingClientRect();
        const texts = [...sv.querySelectorAll('text')].filter(t => visible(t) && t.textContent.trim());
        const boxes = texts.map(t => ({ t, r: t.getBoundingClientRect() }));
        for (const { t, r } of boxes) {
          if (r.left < sr.left - 2 || r.right > sr.right + 2 || r.top < sr.top - 2 || r.bottom > sr.bottom + 2) {
            add('svg-clip', `«${t.textContent.trim().slice(0, 30)}» rasm chegarasidan chiqdi`); break;
          }
        }
        for (const { t, r } of boxes) {
          if (r.height < 10 && r.height > 0 && !mobile) { add('tiny', `SVG matn «${t.textContent.trim().slice(0, 24)}» ~${Math.round(r.height)}px`); break; }
        }
        for (let i = 0; i < boxes.length; i++) {
          let hit = false;
          for (let j = i + 1; j < boxes.length; j++) {
            const ia = inter(boxes[i].r, boxes[j].r);
            if (ia > 0.25 * Math.min(area(boxes[i].r), area(boxes[j].r)) && ia > 20) {
              add('svg-overlap', `«${boxes[i].t.textContent.trim().slice(0, 22)}» ↔ «${boxes[j].t.textContent.trim().slice(0, 22)}»`); hit = true; break;
            }
          }
          if (hit) break;
        }
      }
      // kichik matn
      const sc = R.getScale();
      for (const e of leaves) {
        const fs = parseFloat(win.getComputedStyle(e).fontSize) * sc;
        if (fs < 12 && !mobile) { add('tiny', `${desc(e)} ${fs.toFixed(1)}px`); break; }
      }
      // ikonka/rasm
      if (pres.querySelector('i[data-ic]')) add('icon', 'ikonkaga aylanmagan i[data-ic] bor (nom noto\'g\'ri?)');
      const bad = [...pres.querySelectorAll('img')].find(i => i.complete && i.naturalWidth === 0);
      if (bad) add('icon', `rasm yuklanmadi: ${bad.getAttribute('src')}`);
      // fragment
      const hid = [...pres.querySelectorAll('.fragment')].find(f => !visible(f) && f.closest('section') === pres);
      if (hid) add('fragment', `fragment ko'rinmaydi: ${desc(hid)}`);
      // bo'sh slayd
      if (pres.textContent.trim().length < 6 && !pres.querySelector('img,svg')) add('empty', 'slaydda matn yo\'q');
    }
  }
  fr.remove();
  return out;
}
