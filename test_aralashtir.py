#!/usr/bin/env python3
"""Test fayllaridagi variantlarni aralashtiradi, to'g'ri javob o'rni bir xil chiqmasligi uchun.

Ishlatish:  python3 test_aralashtir.py   (barcha *-test-slaydlar.html; qayta ishga tushirish xavfsiz)
To'g'ri javob (data-ok) o'rni savol tartibi bo'yicha 1,2,3,4 ... aylanadi (deterministik).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OPT = re.compile(r'[ \t]*<button class="opt"[^>]*>.*?</button>\n?', re.S)


def fix(path):
    s = path.read_text(encoding="utf-8")
    counter = [0]

    def opts_block(m):
        body = m.group(2)
        opts = OPT.findall(body)
        if len(opts) < 2 or not any("data-ok" in o for o in opts):
            return m.group(0)
        ok = next(i for i, o in enumerate(opts) if "data-ok" in o)
        target = counter[0] % len(opts)
        counter[0] += 1
        opts.insert(target, opts.pop(ok))
        indent = "      "
        items = "".join(indent + o.strip() + "\n" for o in opts)
        return m.group(1) + "\n" + items.rstrip("\n") + "\n    </div>"

    new = re.sub(r'(<div class="opts">)\s*(.*?)(\s*</div>)', opts_block, s, flags=re.S)
    if new != s:
        path.write_text(new, encoding="utf-8")
    return counter[0]


if __name__ == "__main__":
    n = 0
    for f in sorted(ROOT.glob("*/haftalik/*/*test-slaydlar.html")):
        n += fix(f)
    print(f"{n} ta savol aralashtirildi")
