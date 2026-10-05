# 4-hafta. Baholash (faqat mentor uchun)

Bitta o'quvchi uchun shablon. Maqsad: haftalar bo'yicha o'sish dinamikasini kuzatish. Har hafta shu shablon nusxalanib, «Dinamika» jadvaliga bitta qator qo'shiladi.

**O'quvchi:** ____________________  **Guruh/sinf:** 11-sinf  **Mentor:** ____________________

## Shkala va mezonlar (o'quv dasturi, 8-bo'lim)

100 ballik shkala: **90–100 — 5 (a'lo)**, **71–89 — 4 (yaxshi)**, **60–70 — 3 (qoniqarli)**, **0–59 — 2 (qoniqarsiz)**.

Dasturdagi mezonlar: mavzu bo'yicha tasavvurga ega bo'lish; mavzu mohiyatini tushunish va aytib bera olish; bilimni amalda qo'llash; ijodiy fikrlash va xulosa chiqarish; mustaqil ish bajarish.

| Mezon | Max |
|---|---|
| Mohiyatni tushunadi va aytib bera oladi (tezkor nazorat, og'zaki) | 30 |
| Amaliy topshiriq: to'g'ri va to'liq, mustaqil bajarilgan | 30 |
| Ish sifati: toza arxitektura, REST/JSON standartlari, xavfsizlik, testlar | 20 |
| Uyga vazifa bajarilgan va o'z vaqtida topshirilgan | 20 |
| **Jami** | **100** |

---

## 10-dars. Loyihalash andozalari: Observer va hodisalar arxitekturasi

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | Subject/Observer rollari; publish/subscribe va loose coupling mohiyati; memory leak xatarlari | |
| Amaliyot /30 | `EventBus` sinfini qurish; bir nechta kuzatuvchini ro'yxatdan o'tkazish va xabardor qilish | |
| Ish sifati /20 | `try/except` orqali xatolarni izolyatsiya qilish; `MagicMock` bilan to'liq unit testlar yozilgani | |
| Uyga vazifa /20 | `library_events.py` va `test_events.py` topshirilgan; Git commitlar to'g'ri formatlangan | |
| **Jami /100** | | |

Izoh: ____________________

---

## 11-dars. REST API va JSON asoslari: REST tamoyillari va HTTP

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | REST 5 ustuni; URI dizayni (ot + ko'plik); HTTP metodlari semantikasi va idempotentlik | |
| Amaliyot /30 | Resurslar ierarxiyasini loyihalash; 2xx/4xx/5xx status kodlarini to'g'ri tanlash | |
| Ish sifati /20 | `curl` buyruqlari sarlavhalar (`Content-Type`, `Accept`) va tana (`-d`) bilan to'g'ri ishlatilgani | |
| Uyga vazifa /20 | `docs/api_design.md` va `test_api.sh` sinov skripti to'liq tayyorlangan | |
| **Jami /100** | | |

Izoh: ____________________

---

## 12-dars. REST API va JSON asoslari: JSON formati, kontrakt va xavfsizlik

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | JSON 6 turi; ISO-8601 UTC vaqti; 401 vs 403 farqi; CORS va Rate Limit (429) tushunchalari | |
| Amaliyot /30 | Yagona Error Envelope va Paginatsiya tuzilmasini yaratish; DTO bilan xavfli maydonlarni yashirish | |
| Ish sifati /20 | Xavfsizlik intizomi (`password_hash` chiqib ketmasligi); `test_contracts.py` yashil o'tgani | |
| Uyga vazifa /20 | `contracts.py` to'liq yozilgan, barcha testlar muvaffaqiyatli, GitHub PR topshirilgan | |
| **Jami /100** | | |

Izoh: ____________________

---

## 4-hafta yakuni: o'sish dinamikasi

| Hafta | Darslar | O'rtacha ball | Baho | Asosiy yutuq / Aniqlangan bo'shliq |
|---|---|---|---|---|
| 1-hafta | 1–3 (SDLC, Git) | | | |
| 2-hafta | 4–6 (Branching, PR) | | | |
| 3-hafta | 7–9 (SOLID, Patterns) | | | |
| 4-hafta | 10–12 (Observer, REST, JSON) | | | |

**Mentor tavsiyasi:** O'quvchi I-bobning texnik qismini (Clean Code, SOLID, Creational & Behavioral Patternlar, REST API va JSON kontrakt dizayni) to'liq yakunladi. 5-haftada I-bobning yakuniy soft skills mavzulari (muloqot, liderlik, vaqt boshqaruvi) hamda **Oraliq nazorat (15-dars)** o'tkaziladi.
