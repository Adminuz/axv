#!/usr/bin/env python3
"""VitePress sayti uchun kontent tayyorlash (sayt-vitepress/docs/).

Ishlatish (loyiha papkasidan):
    python3 vitepress_yigish.py            # barcha tayyor haftalar
    python3 vitepress_yigish.py --gacha 5  # faqat 1–5-haftalar
Keyin:
    cd sayt-vitepress && npm run dev       # ko'rish (kontentni o'zi yangilaydi)
    cd sayt-vitepress && npm run build     # tayyor papka: sayt-vitepress/docs/.vitepress/dist

Bu skript faqat KONTENT yaratadi (qo'lda tahrirlanmaydi, har safar qaytadan yaratiladi):
  docs/index.md, docs/<sinf>/..., docs/public/slaydlar/, docs/public/reveal/, docs/public/ikonlar/,
  docs/.vitepress/generated.json
Qo'lda tahrirlanadigan fayllar: docs/.vitepress/config.mts, docs/.vitepress/theme/* (dizayn), sayt_sozlama.json.

Sahifa ma'lumotlari (sinflar, haftalar, darslar) har sahifaning frontmatter'iga JSON bo'lib yoziladi;
ularni theme/components/*.vue chizadi (kartalar, tugmalar). O'quvchi matni esa Markdown bo'lib qoladi.

Saytga NIMA chiqadi:  o'quvchi sahifalari (dars-K-oquvchi.md), uyga vazifa, slaydlar.
Saytga NIMA chiqmaydi: yechimlar (**Yechim...** kesiladi), mentor izohlari (slayd notes), "## Mentor uchun",
                        mentor fayllari (dars-K.md, baholash.md).
"""
import argparse
import html
import json
import re
import shutil
from pathlib import Path

from slayd_yigish import wrap

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "sayt-vitepress"
DOCS = SITE / "docs"
PUB = DOCS / "public"
REVEAL = ROOT / "reveal"

DARS_HAFTADA = 3

SOZLAMA = {
    "tashkilot": "Muhammad al-Xorazmiy vorislari",
    "bosh_matn": "O'quvchilar uchun darslar",
    "bosh_kichik_matn": "Slaydlar · qo'shimcha ma'lumot · topshiriqlar",
    "podval": "",
}
_cfg = ROOT / "sayt_sozlama.json"
if _cfg.exists():
    SOZLAMA.update({k: v for k, v in json.loads(_cfg.read_text(encoding="utf-8")).items() if not k.startswith("_")})

# papka, nomi, fan, ikonka, choraklar (nom, boshlang'ich hafta, oxirgi hafta)
SINFLAR = [
    # 8-sinf
    ("8-sinf", "8-sinf", "Web Full-stack dasturlash", "globe",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("8-sinf-cs", "8-sinf (Foundation)", "Computer Science Foundation", "laptop",
     [("I chorak", 1, 12)]),

    # 9-sinf
    ("9-sinf", "9-sinf", "UX/UI dizayn va Advanced Front-end", "palette",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("9-sinf-backend", "9-sinf (Back-end)", "Advanced Back-end va DevOps", "server",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("9-sinf-android", "9-sinf (Android)", "Android dasturlash", "smartphone",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("9-sinf-bi", "9-sinf (BI)", "Business Intelligence: Ma'lumotlar tahlili", "chart-column",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("9-sinf-game", "9-sinf (Game)", "Game Design", "gamepad-2",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("9-sinf-iot", "9-sinf (IoT)", "IoT (Internet of Things) — Buyumlar Interneti", "cpu",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),

    # 10-sinf
    ("10-sinf-python", "10-sinf (Python)", "Advanced Python Back-end va Prompt Engineering", "terminal",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("10-sinf-cyber", "10-sinf (Cyber)", "Kiberxavfsizlik (Ethical Hacking)", "shield",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("10-sinf-uxui", "10-sinf (UX/UI)", "Advanced UX/UI dizayn va Advanced Front-end", "palette",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("10-sinf-android", "10-sinf (Android)", "Advanced Android dasturlash", "smartphone",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("10-sinf-bi", "10-sinf (BI & ML)", "BI (Ma'lumotlar muhandisligi va ML)", "brain",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),
    ("10-sinf-devops", "10-sinf (DevOps)", "DevOps", "cloud",
     [("I chorak", 1, 9), ("II chorak", 10, 16), ("III chorak", 17, 26), ("IV chorak", 27, 34)]),

    # 11-sinf
    ("11-sinf", "11-sinf", "Professional IT development", "rocket", []),
]

SECTION_ICONS = [  # o'quvchi sahifasi bo'limlari uchun ikonkalar (sarlavha boshlanishi bo'yicha)
    ("dars xulosasi", "list-checks"), ("xulosa", "list-checks"), ("qo'shimcha", "book-open"),
    ("atamalar", "languages"), ("bilasizmi", "sparkles"), ("topshiriq", "clipboard-list"),
    ("o'zingizni", "circle-question-mark"), ("tekshir", "circle-question-mark"), ("uyga", "house"),
]

LEVELS = {"oson": "easy", "o'rta": "mid", "qiyin": "hard", "bonus": "bonus"}


def strip_solutions(md):
    """**Yechim...** bloklarini kesadi (bo'sh qator yoki sarlavhagacha; kod bloki ichida to'xtamaydi)."""
    out, skipping, fence = [], False, False
    for line in md.split("\n"):
        if skipping:
            if line.startswith("```"):
                fence = not fence
                continue
            if fence:
                continue
            if not line.strip() or line.startswith("#"):
                skipping = False
                out.append(line)
            continue
        if line.startswith("**Yechim") or line.startswith("**Javob"):
            skipping = True
            continue
        out.append(line)
    return "\n".join(out)


def md_title(md):
    m = re.search(r"^# (.*)$", md, flags=re.M)
    return m.group(1).strip() if m else ""


def clean_title(t):
    return re.sub(r"^\d+-dars\.\s*", "", t).strip()


def parse_karta(path):
    """karta.md → {dars_raqami: (bob_nomi, mavzu, holat)} va umumiy hafta soni."""
    if not path.exists():
        return {}, 0
    lessons, bob = {}, ""
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"## ([IVX]+)-bob\.\s*(.*?)\s*\(\d+ dars\)", line)
        if m:
            bob = f"{m.group(1)}-bob · {m.group(2)}"
            continue
        m = re.match(r"\|\s*(\d+)(?:–(\d+))?\s*\|\s*[\d–]+\s*\|\s*(.*?)\s*\|\s*(\S+)\s*\|", line)
        if m and bob:
            a = int(m.group(1))
            b = int(m.group(2) or a)
            for n in range(a, b + 1):
                lessons[n] = (bob, m.group(3), m.group(4))
    total = -(-max(lessons) // DARS_HAFTADA) if lessons else 0
    return lessons, total


def glob_lesson(n_week, k):
    return DARS_HAFTADA * (n_week - 1) + k


def lead_of(stu):
    m = re.search(r"^>\s*(.+)$", stu, flags=re.M)
    return m.group(1).strip() if m else ""


def load_week(week_dir):
    n = int(week_dir.name.split("-")[1])
    lessons = []
    for md_path in sorted(week_dir.glob("dars-[0-9].md")):
        k = int(md_path.stem.split("-")[1])
        md = md_path.read_text(encoding="utf-8")
        stu = week_dir / f"dars-{k}-oquvchi.md"
        lessons.append({
            "k": k, "g": glob_lesson(n, k), "title": clean_title(md_title(md)),
            "md": md, "stu": stu.read_text(encoding="utf-8") if stu.exists() else "",
            "slide": (week_dir / f"dars-{k}-slaydlar.html"),
        })
    return n, lessons
DOCS = SITE / "docs"
PUB = DOCS / "public"
REVEAL = ROOT / "reveal"

BADGE = {"easy": "tip", "mid": "warning", "hard": "danger", "bonus": "info"}
UI_ICONS = ["play", "layers", "chevron-right", "chevron-left", "lock", "calendar-days", "timer", "house",
            "list-checks", "book-open", "languages", "sparkles", "clipboard-list", "circle-question-mark",
            "file-text", "presentation", "arrow-right", "arrow-left", "graduation-cap"]


def esc_text(line):
    """Kod bo'lmagan joyda HTML/Vue belgilarini bexatar qiladi (`<`, `{{`)."""
    parts = re.split(r"(`[^`]*`)", line)
    for i in range(0, len(parts), 2):
        p = parts[i].replace("<", "&lt;")
        p = p.replace("{{", "&#123;&#123;").replace("}}", "&#125;&#125;")
        parts[i] = p
    return "".join(parts)


def safe_md(md):
    """Markdown ni VitePress uchun xavfsiz qiladi; kod bloklariga tegmaydi."""
    out, fence = [], False
    for line in md.split("\n"):
        if line.startswith("```"):
            fence = not fence
            out.append(line)
        elif fence:
            out.append(line)
        else:
            out.append(esc_text(line))
    return "\n".join(out)


def badge_headings(md):
    """`### 3. Nomi · oson` → `### 3. Nomi <Badge type="tip" text="oson" />`."""
    def rep(m):
        lv = m.group(3).lower()
        if lv not in LEVELS:
            return m.group(0)
        return f'{m.group(1)}{m.group(2)} <Badge type="{BADGE[LEVELS[lv]]}" text="{lv}" />'
    return re.sub(r"^(#{2,4} )(.*?)\s+·\s+(oson|o'rta|qiyin|bonus)\s*$", rep, md, flags=re.M | re.I)


def as_blocks(md, shift=0):
    """`## Bo'lim` larni karta (`<div class="blk">`) ichiga o'raydi; sarlavhaga ikonka qo'yadi."""
    parts = re.split(r"^## (.*)$", md, flags=re.M)
    out = parts[0].strip() + "\n" if parts[0].strip() else ""
    for j in range(1, len(parts), 2):
        title, body = parts[j].strip(), parts[j + 1].strip()
        icon = next((v for key, v in SECTION_ICONS if title.lower().startswith(key)), "file-text")
        out += f'\n<div class="blk">\n\n## <Icon name="{icon}" /> {title}\n\n{body}\n\n</div>\n'
    return out


def plain(t):
    """Sarlavhadagi `kod` belgilari (backtick) ko'rsatishda xalaqit bermasin."""
    return t.replace("`", "")


def fm(data):
    """Frontmatter (JSON ham to'g'ri YAML)."""
    return "---\n" + "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in data.items()) + "\n---\n"


def build_sinf(sinf_dir, sinf_name, fan, icon, choraklar, gacha):
    karta, total = parse_karta(ROOT / sinf_dir / "karta.md")
    base = ROOT / sinf_dir / "haftalik"
    weeks = {}
    if base.exists():
        for w in sorted(base.glob("hafta-[0-9][0-9]")):
            n = int(w.name.split("-")[1])
            if gacha is not None and n > gacha:
                continue
            loaded = load_week(w)
            if loaded[1]:  # darslari bo'lmagan (bo'sh) hafta saytga chiqmaydi
                weeks[n] = (w, *loaded)
    if not weeks:
        return None
    total = max(total, max(weeks))
    out_dir = DOCS / sinf_dir
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    sinf_link = f"/{sinf_dir}/"

    for n, (wdir, _, lessons) in sorted(weeks.items()):
        wout = out_dir / f"hafta-{n:02d}"
        wout.mkdir()
        wlink = f"/{sinf_dir}/hafta-{n:02d}/"
        bob = karta.get(lessons[0]["g"], ("", "", ""))[0]
        cards, entries = [], []
        for L in lessons:
            has_slide = L["slide"].exists()
            slide_url = f"/slaydlar/{sinf_dir}/hafta-{n:02d}/dars-{L['k']}.html" if has_slide else None
            if has_slide:
                content = re.sub(r"<aside class=\"notes\">.*?</aside>", "", L["slide"].read_text(encoding="utf-8"), flags=re.S)
                dst = PUB / "slaydlar" / sinf_dir / f"hafta-{n:02d}" / f"dars-{L['k']}.html"
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(wrap(content, "../../../"), encoding="utf-8")
            link = f"/{sinf_dir}/hafta-{n:02d}/dars-{L['k']}"
            lead = lead_of(L["stu"]) or karta.get(L["g"], ("", "", ""))[1]
            cards.append({"g": L["g"], "title": plain(L["title"]), "lead": plain(lead), "link": link, "slide": slide_url})
            entries.append((L, link, slide_url, lead))

        for idx, (L, link, slide_url, lead) in enumerate(entries):
            body = re.sub(r"^# .*\n", "", L["stu"], count=1, flags=re.M)
            body = re.sub(r"^>.*\n", "", body, count=1, flags=re.M)
            body = as_blocks(badge_headings(safe_md(strip_solutions(body))))
            prev_l = {"g": entries[idx - 1][0]["g"], "title": plain(entries[idx - 1][0]["title"]), "link": entries[idx - 1][1]} if idx > 0 else None
            next_l = {"g": entries[idx + 1][0]["g"], "title": plain(entries[idx + 1][0]["title"]), "link": entries[idx + 1][1]} if idx + 1 < len(entries) else None
            data = {
                "title": plain(f'{L["g"]}-dars. {L["title"]}'),
                "layout": "doc", "sidebar": False, "aside": False, "outline": False,
                "kind": "dars",
                "dars": {"sinf": {"name": sinf_name, "link": sinf_link}, "week": {"n": n, "link": wlink},
                         "g": L["g"], "title": plain(L["title"]), "lead": plain(lead), "slide": slide_url,
                         "tabs": [{"g": c["g"], "link": c["link"], "current": c["g"] == L["g"]} for c in cards],
                         "prev": prev_l, "next": next_l},
            }
            (wout / f"dars-{L['k']}.md").write_text(fm(data) + "\n" + body + "\n", encoding="utf-8")

        hw = wdir / "uyga-vazifa.md"
        hw_md = ""
        if hw.exists():
            t = hw.read_text(encoding="utf-8")
            t = re.sub(r"^# .*\n", "", t, count=1)
            t = re.split(r"^## Mentor uchun", t, flags=re.M)[0]
            t = re.sub(r"^## (\d+-dars)", r"### \1", t, flags=re.M)
            hw_md = f'\n<div class="blk">\n\n## <Icon name="house" /> Uyga vazifa\n\n{badge_headings(safe_md(strip_solutions(t))).strip()}\n\n</div>\n'
        data = {
            "title": f"{n}-hafta", "layout": "doc", "sidebar": False, "aside": False, "outline": False,
            "kind": "hafta",
            "hafta": {"sinf": {"name": sinf_name, "link": sinf_link}, "n": n, "bob": bob, "lessons": cards},
        }
        (wout / "index.md").write_text(fm(data) + hw_md, encoding="utf-8")

    quarters = []
    for qname, a, b in (choraklar or [("Haftalik reja", 1, total)]):
        if a > total:
            continue
        b = min(b, total)
        wl = []
        for w in range(a, b + 1):
            gs = [glob_lesson(w, k) for k in range(1, DARS_HAFTADA + 1)]
            rows = [karta.get(g) for g in gs]
            seen, topics = set(), []
            for g, r in zip(gs, rows):
                if r and r[1] not in seen:
                    seen.add(r[1])
                    topics.append({"g": g, "t": plain(r[1])})
            wl.append({"n": w, "bob": next((r[0] for r in rows if r), ""), "topics": topics,
                       "link": f"/{sinf_dir}/hafta-{w:02d}/" if w in weeks else None,
                       "done": all(r and r[2] == "✅" for r in rows)})
        quarters.append({"name": qname, "range": f"{a}–{b}-haftalar", "weeks": wl})
    data = {
        "title": sinf_name, "layout": "doc", "sidebar": False, "aside": False, "outline": False,
        "kind": "sinf",
        "sinf": {"name": sinf_name, "fan": fan, "icon": icon, "open": len(weeks), "total": total,
                 "facts": [{"icon": "calendar-days", "text": f"{total} hafta"},
                           {"icon": "layers", "text": f"{total * DARS_HAFTADA} dars"},
                           {"icon": "timer", "text": f"haftasiga {DARS_HAFTADA} dars · 80 daqiqa"}],
                 "quarters": quarters},
    }
    (out_dir / "index.md").write_text(fm(data), encoding="utf-8")
    return {"weeks": len(weeks), "total": total}


def copy_icon(name):
    src = REVEAL / "lucide" / f"{name}.svg"
    if src.exists():
        dst = PUB / "ikonlar" / f"{name}.svg"
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dst)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gacha", type=int, default=None)
    args = ap.parse_args()

    if (PUB / "slaydlar").exists():
        shutil.rmtree(PUB / "slaydlar")
    PUB.mkdir(parents=True, exist_ok=True)
    for rel in ["dist/reveal.css", "dist/reveal.js", "dist/theme/black.css", "dist/plugin/highlight.js",
                "dist/plugin/highlight/monokai.css", "dist/plugin/notes.js", "dars.css", "tema.js",
                "logo.png", "ikonlar.js", "interaktiv.js", "LICENSE"]:
        dst = PUB / "reveal" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REVEAL / rel, dst)
    shutil.copy(REVEAL / "logo.png", PUB / "logo.png")
    for n in UI_ICONS:
        copy_icon(n)

    classes, nav_items = [], []
    for sinf_dir, sinf_name, fan, icon, choraklar in SINFLAR:
        copy_icon(icon)
        res = build_sinf(sinf_dir, sinf_name, fan, icon, choraklar, args.gacha)
        classes.append({"name": sinf_name, "fan": fan, "icon": icon,
                        "link": f"/{sinf_dir}/" if res else None,
                        "done": res["weeks"] if res else 0, "total": res["total"] if res else 0})
        if res:
            nav_items.append({"text": sinf_name, "link": f"/{sinf_dir}/"})

    home = {
        "title": SOZLAMA["tashkilot"], "layout": "doc", "sidebar": False, "aside": False, "outline": False,
        "kind": "home",
        "home": {"org": SOZLAMA["tashkilot"], "tag": SOZLAMA["bosh_matn"], "tag2": SOZLAMA["bosh_kichik_matn"],
                 "classes": classes},
    }
    (DOCS / "index.md").write_text(fm(home), encoding="utf-8")

    gen = {"tashkilot": SOZLAMA["tashkilot"], "podval": SOZLAMA["podval"],
           "nav": [{"text": "Sinflar", "items": nav_items}] if nav_items else []}
    (DOCS / ".vitepress").mkdir(parents=True, exist_ok=True)
    (DOCS / ".vitepress" / "generated.json").write_text(json.dumps(gen, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Tayyor:", DOCS)


if __name__ == "__main__":
    main()
