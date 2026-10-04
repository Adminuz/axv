#!/usr/bin/env python3
"""Slaydlar va sayt uchun reveal/ikonlar.js ni yig'adi.

Ishlatish (loyiha papkasidan):  python3 ikon_yigish.py

Slaydlarda ikonka shunday yoziladi:  <i data-ic="globe"></i>
Ikonka nomlari Lucide to'plamidan (reveal/lucide/<nom>.svg). Skript barcha
`dars-*-slaydlar.html`, `shablon/slaydlar.html` va sayt shablonlaridagi data-ic nomlarini
topib, faqat kerakli ikonkalarni bitta `reveal/ikonlar.js` fayliga joylaydi.
Yangi slayd yozgandan keyin (yoki ikonka qo'shganda) shuni qayta ishga tushiring.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LUCIDE = ROOT / "reveal" / "lucide"
OUT = ROOT / "reveal" / "ikonlar.js"
# Sayt (vitepress_yigish.py) ishlatadigan ikonkalar:
EXTRA = {"globe", "code-xml", "house", "graduation-cap", "book-open", "chevron-left", "chevron-right", "presentation",
         "layers", "lock", "list-checks", "languages", "sparkles", "clipboard-list", "circle-question-mark", "calendar-days",
         "timer", "file-text", "palette", "rocket"}

LOADER = """
(function () {
  function run() {
    document.querySelectorAll('i[data-ic]').forEach(function (el) {
      var p = window.IKON[el.getAttribute('data-ic')];
      if (!p) { console.warn('Ikonka topilmadi:', el.getAttribute('data-ic')); return; }
      var an = el.getAttribute('data-anim');
      var extra = (el.getAttribute('class') ? ' ' + el.getAttribute('class') : '') + (an ? ' anim-' + an : '');
      if (an === 'draw') { p = p.replace(/<(path|circle|rect|line|polyline|polygon|ellipse)\\b/g, '<$1 pathLength="1"'); }
      el.outerHTML = '<svg class="ic' + extra + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + p + '</svg>';
    });
  }
  run();
  document.addEventListener('DOMContentLoaded', run);
})();
"""


def main():
    names = set(EXTRA)
    files = list(ROOT.glob("*/haftalik/*/dars-*-slaydlar.html")) + [ROOT / "shablon" / "slaydlar.html"]
    for f in files:
        if f.exists():
            names |= set(re.findall(r'data-ic="([a-z0-9-]+)"', f.read_text(encoding="utf-8")))
    icons, missing = {}, []
    for n in sorted(names):
        p = LUCIDE / f"{n}.svg"
        if not p.exists():
            missing.append(n)
            continue
        inner = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
        inner = re.sub(r"^\s*<svg[^>]*>", "", inner, flags=re.S)
        inner = re.sub(r"</svg>\s*$", "", inner)
        icons[n] = re.sub(r"\s+", " ", inner).strip()
    import json
    OUT.write_text("window.IKON = " + json.dumps(icons, ensure_ascii=False) + ";\n" + LOADER, encoding="utf-8")
    print(f"{len(icons)} ta ikonka yozildi: {OUT.relative_to(ROOT)}")
    if missing:
        print("TOPILMADI (Lucide'da bunday nom yo'q):", ", ".join(missing))
        sys.exit(1)


if __name__ == "__main__":
    main()
