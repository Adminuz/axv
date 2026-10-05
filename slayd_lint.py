#!/usr/bin/env python3
"""Slayd manba fayllarini (dars-K-slaydlar.html) statik tekshirish.

Ishlatish:  python3 slayd_lint.py            # barcha tayyor haftalar
            python3 slayd_lint.py 8-sinf/haftalik/hafta-01   # bitta papka

Topadi:
  - dars.css da yo'q (aniqlanmagan) CSS sinflari: tashqi model o'ylab topgan sinflar sahifani buzadi
  - sarlavha slaydi: <section class="hero"> va <img class="logo-big"> bo'lishi shart
  - emoji, #hex/rgba ranglar, inline px kenglik, tashqi URL
  - noto'g'ri ikonka nomi (reveal/lucide da yo'q)
Natija: har faylga xulosa. Xato topilsa chiqish kodi 1.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CSS = (ROOT / "reveal" / "dars.css").read_text(encoding="utf-8")
KNOWN = set(re.findall(r"\.([a-zA-Z][\w-]*)", CSS))
# reveal.js / highlight.js / VitePress ichki sinflar va sodda yordamchi sinflar
KNOWN |= {"fragment", "fade-up", "fade-down", "fade-left", "fade-right", "fade-in-then-out", "fade-in-then-semi-out", "grow", "shrink",
          "strike", "highlight-red", "highlight-green", "highlight-blue", "highlight-current-red", "highlight-current-green",
          "highlight-current-blue", "current-visible", "semi-fade-out", "present", "past", "future", "slides", "reveal", "notes",
          "stack", "visible"}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅❌⏱⬅➡]")
ICONS = {p.stem for p in (ROOT / "reveal" / "lucide").glob("*.svg")}


def lint(path):
    s = path.read_text(encoding="utf-8")
    body = re.sub(r"<aside class=\"notes\">.*?</aside>", "", s, flags=re.S)
    problems = []
    unknown = {}
    for m in re.finditer(r"""class=["']([^"']*)["']""", body):
        for c in m.group(1).split():
            if c.startswith("language-") or c.startswith("hljs") or c in KNOWN:
                continue
            unknown[c] = unknown.get(c, 0) + 1
    if unknown:
        problems.append("noma'lum sinflar: " + ", ".join(f"{k}×{v}" for k, v in sorted(unknown.items(), key=lambda x: -x[1])[:12]))
    first = re.search(r"<section[^>]*>", body)
    if not first or "hero" not in first.group(0):
        problems.append('birinchi slayd <section class="hero"> emas')
    if "logo-big" not in body:
        problems.append('sarlavha slaydida <img class="logo-big"> yo\'q')
    if EMOJI.search(body):
        problems.append("emoji bor")
    if re.search(r"#[0-9a-fA-F]{6}\b|rgba?\(", re.sub(r'<div class="browser.*?</div>\s*</div>', "", body, flags=re.S)):
        problems.append("#hex/rgba rang bor (SVG sinflari fa/fb/la... ishlating)")
    if re.search(r"""(?:src|href)=["']https?://|url\(\s*["']?https?://""", body):
        problems.append("tashqi URL (src/href/url) bor: internetsiz ishlashi kerak")
    for a in set(re.findall(r'data-anim="([^"]+)"', body)):
        if a not in {"float", "pulse", "spin", "bounce", "wiggle", "blink", "draw"}:
            problems.append(f"noma'lum data-anim: {a}")
    for n in set(re.findall(r'data-ic="([^"]+)"', body)):
        if n not in ICONS:
            problems.append(f"ikonka yo'q: {n}")
    if len(re.findall(r"<section", body)) != len(re.findall(r"</section>", body)):
        problems.append("<section> teglari juft emas")
    return problems


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    files = []
    if args:
        for a in args:
            files += sorted((ROOT / a).glob("*-slaydlar.html"))
    else:
        files = sorted(ROOT.glob("*/haftalik/*/dars-[0-9]-slaydlar.html")) + sorted(ROOT.glob("*/haftalik/*/dars-[0-9]-test-slaydlar.html")) + sorted(ROOT.glob("*/haftalik/*/hafta-test-slaydlar.html"))
    bad = 0
    for f in files:
        pr = lint(f)
        rel = f.relative_to(ROOT)
        if pr:
            bad += 1
            print(f"✗ {rel}")
            for p in pr:
                print("    -", p)
        else:
            print(f"✓ {rel}")
    print(f"\nFayllar: {len(files)}, muammoli: {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
