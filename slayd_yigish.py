#!/usr/bin/env python3
"""Slaydlarni umumiy qobiqqa o'rab, to'liq HTML qiladi.

Slayd mualliflari (agentlar) faqat `dars-K-slaydlar.html` yozadi: u faqat <section> slaydlardan iborat.
Qobiq (head, uslublar, skriptlar, logo, reveal sozlamalari) bitta joyda: shablon/slayd-qobiq.html.
Qobiqni o'zgartirsangiz, shu skriptni qayta ishga tushiring: hamma slaydga ta'sir qiladi.

Ishlatish (loyiha papkasidan):  python3 slayd_yigish.py
Natija: har `dars-K-slaydlar.html` yoniga to'liq `dars-K-slayd.html` (brauzerda ochish va dars o'tish uchun).
Saytga chiqarishda esa vitepress_yigish.py shu funksiyalardan o'zi foydalanadi.
"""
import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHELL = ROOT / "shablon" / "slayd-qobiq.html"


def title_of(content):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", content, flags=re.S)
    t = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "Dars"
    return html.unescape(t)


def wrap(content, up, title=None, is_quiz=False):
    """content: faqat <section>lar. up: reveal/ papkasigacha nisbiy yo'l prefiksi (masalan '../../../')."""
    if is_quiz:  # test fayllari: slayd emas, telefonga mos quiz sahifasi
        from quiz_yigish import build as quiz_build
        return quiz_build(content, up)
    shell = SHELL.read_text(encoding="utf-8")
    title = title or title_of(content)
    return (shell.replace("{{TITLE}}", html.escape(title, quote=False))
                 .replace("{{SLIDES}}", content.replace("{{UP}}", up))
                 .replace("{{UP}}", up))


def main():
    subprocess.run([sys.executable, str(ROOT / "ikon_yigish.py")], check=True)
    n = 0
    srcs = sorted(ROOT.glob("*/haftalik/*/dars-[0-9]-slaydlar.html")) \
        + sorted(ROOT.glob("*/haftalik/*/dars-[0-9]-test-slaydlar.html")) \
        + sorted(ROOT.glob("*/haftalik/*/hafta-test-slaydlar.html"))
    for src in srcs:
        dst = src.with_name(src.name.replace("-slaydlar", "-slayd"))
        is_quiz = "-test" in src.name
        dst.write_text(wrap(src.read_text(encoding="utf-8"), "../../../", is_quiz=is_quiz), encoding="utf-8")
        n += 1
    print(f"{n} ta slayd fayli yig'ildi (dars-K-slayd.html)")


if __name__ == "__main__":
    main()
