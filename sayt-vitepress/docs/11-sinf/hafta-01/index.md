---
title: "1-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "n": 1, "bob": "I-bob · Dasturiy ta'minot ishlab chiqish asoslari", "lessons": [{"g": 1, "title": "IT ekotizimi qatlamlari, SDLC bosqichlari va jamoadagi rollar", "lead": "Siz har kuni ishlatadigan ilova ortida ko'zga ko'rinmaydigan butun bir «shahar» bor: qatlamlar, serverlar va jamoa. Bugun uni xaritaga tushiramiz va o'z portfolio-loyihangiz uchun birinchi professional hujjatni yozamiz.", "link": "/11-sinf/hafta-01/dars-1", "slide": "/slaydlar/11-sinf/hafta-01/dars-1.html", "test": "/slaydlar/11-sinf/hafta-01/dars-1-test.html"}, {"g": 2, "title": "Git asoslari: versiyalarni boshqarish, repozitoriy, commit, branch va merge", "lead": "Bugun siz kodingiz uchun «vaqt mashinasi» yasaysiz: terminalda birinchi repozitoriyni yaratib, har o'zgarishni saqlaysiz, parallel shox ochasiz va konfliktni yechasiz. Professional dasturchilar har kuni shu buyruqlar bilan ishlaydi.", "link": "/11-sinf/hafta-01/dars-2", "slide": "/slaydlar/11-sinf/hafta-01/dars-2.html", "test": "/slaydlar/11-sinf/hafta-01/dars-2-test.html"}, {"g": 3, "title": "GitHub: masofaviy repo, push/pull/clone, README, .gitignore, Issues va birinchi loyiha", "lead": "Bugun kodingiz birinchi marta noutbukdan chiqib, butun dunyo ko'ra oladigan joyga boradi: GitHub. Oxirida sizda ish beruvchiga ko'rsatsa bo'ladigan birinchi haqiqiy repo bo'ladi.", "link": "/11-sinf/hafta-01/dars-3", "slide": "/slaydlar/11-sinf/hafta-01/dars-3.html", "test": "/slaydlar/11-sinf/hafta-01/dars-3-test.html"}], "test": "/slaydlar/11-sinf/hafta-01/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Har bir vazifa 20–30 daqiqa. Parol, token, maxfiy kalit va shaxsiy ma'lumotlarni hech kimga yubormang va fayllarga yozmang: topshirishda faqat fayl yoki ochiq repo havolasi kerak.

### 1-dars uchun (IT ekotizimi va SDLC)
**1-topshiriq: «Portfolio-loyiha: talab»**
1. Darsda boshlagan `SRS-mini.md` faylini yakunlang. Unda bo'lishi kerak: bir jumlalik maqsad; 5 ta user story; har bir user story uchun kamida 2 ta qabul mezoni; «loyiha nimani qilmaydi» bo'limida 3 ta cheklov.
2. Qabul mezonlarini o'lchanadigan qilib yozing: «chiroyli», «tez» kabi mavhum so'zlar o'rniga son yoki tekshiriladigan shart yozing.
3. Sevimli ilovangizning 4 qatlamli xaritasini (klient, ilova, platforma, infratuzilma) toza chizing: har qatlamda kamida 2 ta komponent bo'lsin. Rasm yoki foto qiling.
4. Terminalda `git --version` buyrug'ini ishga tushiring va natijani tekshiring: keyingi darsda Git bilan ishlaymiz.

**Kutiladigan natija:** `SRS-mini.md` (5 user story, 10 dan ortiq o'lchanadigan qabul mezoni, 3 cheklov); ilova xaritasining rasmi; `git --version` versiya raqamini chiqaradi.
**Topshirish:** `SRS-mini.md` fayli, xarita rasmi va `git --version` natijasining skrinshoti yoki ko'chirilgan matni.

### 2-dars uchun (Git asoslari: commit, branch, merge)
**2-topshiriq: `dev-journal` ni boyiting**
1. `dev-journal` repozitoriyasida `.gitignore` faylini yarating. Unda kamida `.env` va `__pycache__/` qatorlari bo'lsin.
2. Uch kun uchun `notes/kun-1.md`, `notes/kun-2.md`, `notes/kun-3.md` yozuvlarini yozing. Har bir fayl alohida commit bo'lsin, xabarlar Conventional Commits uslubida (masalan, `docs: ...`).
3. `feature/skills` shoxini oching, unda bitta o'zgarish qiling va commit qiling, so'ng uni `main` ga merge qiling.
4. `git log --oneline --graph` natijasini `log.txt` fayliga saqlang va shu faylni ham commit qiling.

**Kutiladigan natija:** `git log` da 3 ta kunlik yozuv commiti, `.gitignore` commiti, merge va `log.txt` commiti ko'rinadi; grafikda `feature/skills` shoxi `main` ga qo'shilgani bilinadi; `git status` toza.
**Topshirish:** `log.txt` fayli va `git status` natijasi. Keyingi darsda bu repoz GitHub'ga yuklanadi.

### 3-dars uchun (GitHub)
**3-topshiriq: `dev-log` ni davom ettiring**
1. Darsda yaratgan `dev-log` repongizga yana 2 ta mazmunli commit qo'shing (masalan, `todo.py` ga yangi buyruq va `README.md` ni yaxshilash). Commit xabari nima o'zgarganini aniq aytsin.
2. GitHub'da bitta Issue oching va uni commit xabaridagi `Closes #N` (o'z Issue raqamingiz) orqali yoping.
3. O'zgarishlarni `git push` bilan GitHub'ga yuboring va repo ochiq (public) ekanini tekshiring.
4. Repo havolasini mentorga yuboring.

**Kutiladigan natija:** GitHub'dagi `dev-log` da yangi 2 ta commit; Issue `Closed` holatida va uni yopgan commitga havola bor; `README.md` va `.gitignore` joyida; repo havolasi brauzerda (kirmasdan) ochiladi.
**Topshirish:** faqat ochiq repo havolasi (`https://github.com/<nom>/dev-log`). Parol, token yoki kalit yubormang.

</div>
