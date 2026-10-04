# 1-hafta. Baholash (faqat mentor uchun)

Bitta o'quvchi uchun shablon. Maqsad: haftalar bo'yicha o'sish dinamikasini kuzatish. Har hafta shu shablon nusxalanib, «Dinamika» jadvaliga bitta qator qo'shiladi.

**O'quvchi:** ____________________  **Guruh/sinf:** 11-sinf  **Mentor:** ____________________

## Shkala va mezonlar (o'quv dasturi, 8-bo'lim)

100 ballik shkala: **90–100 — 5 (a'lo)**, **71–89 — 4 (yaxshi)**, **60–70 — 3 (qoniqarli)**, **0–59 — 2 (qoniqarsiz)**.

Dasturdagi mezonlar: mavzu bo'yicha tasavvurga ega bo'lish; mavzu mohiyatini tushunish va aytib bera olish; bilimni amalda qo'llash; ijodiy fikrlash va xulosa chiqarish; mustaqil ish bajarish. 5 baho uchun mustaqil xulosa va qaror qabul qilish ham talab etiladi; 3 baho uchun bilimni amalda qo'llay olish yetarli.

Joriy nazorat (so'rovlar va bajarilgan loyiha ishini izohlash) dasturda loyiha ishi uchun 40 ball bilan belgilangan va o'quv jarayoni davomida o'tkaziladi. Quyidagi dars bo'yicha ball taqsimoti dasturda berilmagan, mentor taklif etilgan jadvalni o'zgartirishi mumkin.

| Mezon | Max |
|---|---|
| Mohiyatni tushunadi va aytib bera oladi (tezkor nazorat, og'zaki) | 30 |
| Amaliy topshiriq: to'g'ri va to'liq, mustaqil bajarilgan | 30 |
| Ish sifati: toza kod/fayl, aniq commit xabarlari, tartibli tuzilma | 20 |
| Uyga vazifa bajarilgan va o'z vaqtida topshirilgan | 20 |
| **Jami** | **100** |

Qo'shimcha: ijodiy fikrlash va mustaqil xulosa (masalan, qiyin topshiriq) mezonlar doirasida e'tiborga olinadi.

## 1-dars. IT ekotizimi va SDLC

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | 4 qatlamni misollar bilan aytadi; qatlamlash foydasi; SDLC bosqichlari va rollar | |
| Amaliyot /30 | ilova xaritasi (qatlam/komponent to'g'ri); artefaktlarni bosqichga moslash; `SRS-mini.md` boshlangan | |
| Ish sifati /20 | user story shakli to'g'ri; qabul mezonlari o'lchanadigan (mavhum emas) | |
| Uyga vazifa /20 | `SRS-mini.md` to'liq (5 story, 10+ mezon, 3 cheklov); xarita rasmi; `git --version` ishlaydi | |
| **Jami /100** | | |

Izoh: ____________________

## 2-dars. Git asoslari

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | 3 zona (working dir, staging, repo); `add`/`commit`; branch va merge nima | |
| Amaliyot /30 | `init`, `add`, `commit`, `status`, `diff`; shox ochish va merge; konfliktni hal qilish (urinish) | |
| Ish sifati /20 | commit kichik va mazmunli; Conventional Commits uslubi; `.gitignore` to'g'ri | |
| Uyga vazifa /20 | 3 ta kunlik commit; `feature/skills` merge; `log.txt` grafik bilan; `git status` toza | |
| **Jami /100** | | |

Izoh: ____________________

## 3-dars. GitHub

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | remote, push/pull/clone, `fetch` va `pull` farqi; sirlarni repoga qo'ymaslik | |
| Amaliyot /30 | repo yaratilgan va ulangan; `push -u origin main`; xavfsiz autentifikatsiya (SSH/token) sozlangan | |
| Ish sifati /20 | `README.md` mazmunli; `.gitignore` bor; Issue aniq yozilgan | |
| Uyga vazifa /20 | 2 ta yangi commit; Issue `Closes #N` bilan yopilgan; ochiq repo havolasi yuborilgan, maxfiy ma'lumot yo'q | |
| **Jami /100** | | |

Izoh: ____________________

## Hafta yakuni

| Ko'rsatkich | 1-dars | 2-dars | 3-dars | O'rtacha | Baho |
|---|---|---|---|---|---|
| Ball | | | | | |

**Kuchli tomonlari:** ____________________

**Rivojlantirish kerak:** ____________________

**Mustaqillik darajasi** (yordamsiz / ishora bilan / bosqichma-bosqich yordam): ____________________

## Dinamika (haftalar bo'yicha, har hafta bitta qator qo'shiladi)

| Hafta | Mavzu | O'rtacha ball | Baho | O'tgan haftaga nisbatan (↑ / = / ↓) | Asosiy kuzatuv |
|---|---|---|---|---|---|
| 1 | IT ekotizimi, SDLC, Git, GitHub | | | boshlang'ich nuqta | |
| 2 | | | | | |
| 3 | | | | | |

Oraliq nazorat chorak oxirida o'tkaziladi va bu haftaga to'g'ri kelmaydi. Shu haftalik ballar joriy nazorat kuzatuvi sifatida saqlanadi.

## Hafta xulosasi va 2-haftaga ko'prik

**Bu hafta:** IT ekotizimining qatlamlari, SDLC bosqichlari va jamoadagi rollar; mini-SRS; Git (repozitoriy, commit, shox, merge, `log`); GitHub (remote, push/pull/clone, README, `.gitignore`, Issues). O'quvchi birinchi ochiq repo (`dev-log`) va `dev-journal` bilan chiqdi.

**Keyingi hafta (2-hafta, 4-dars va undan keyin):** Branching strategiyalari, Pull Request va code review. Bu haftadagi bilimga to'g'ridan-to'g'ri tayanadi: `feature/skills` shoxi va merge tajribasi branching strategiyasiga, kichik commit va Issue oqimi (issue → feature branch → PR → review → merge) Pull Request'ga asos bo'ladi.

**Mentor uchun keyingi dars oldidan tekshiruv:**
- O'quvchida GitHub'ga ishlaydigan autentifikatsiya (SSH yoki token) bormi; `push` xatosiz o'tadimi?
- `dev-log` va `dev-journal` GitHub'da bormi? Pull Request mashqi uchun ulardan biri kerak bo'ladi.
- Shox ochish va merge'ni mustaqil bajara oladimi? Zaif bo'lsa, 4-dars boshida 10 daqiqalik takrorlash qo'shing.
- Commit xabarlari va Issue'lar aniqmi? Code review'da ham aniq, hurmatli fikr bildirish talab etiladi.
