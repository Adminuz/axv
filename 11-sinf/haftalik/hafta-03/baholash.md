# 3-hafta. Baholash (faqat mentor uchun)

Bitta o'quvchi uchun shablon. Maqsad: haftalar bo'yicha o'sish dinamikasini kuzatish. Har hafta shu shablon nusxalanib, «Dinamika» jadvaliga bitta qator qo'shiladi.

**O'quvchi:** ____________________  **Guruh/sinf:** 11-sinf  **Mentor:** ____________________

## Shkala va mezonlar (o'quv dasturi, 8-bo'lim)

100 ballik shkala: **90–100 — 5 (a'lo)**, **71–89 — 4 (yaxshi)**, **60–70 — 3 (qoniqarli)**, **0–59 — 2 (qoniqarsiz)**.

Dasturdagi mezonlar: mavzu bo'yicha tasavvurga ega bo'lish; mavzu mohiyatini tushunish va aytib bera olish; bilimni amalda qo'llash; ijodiy fikrlash va xulosa chiqarish; mustaqil ish bajarish.

| Mezon | Max |
|---|---|
| Mohiyatni tushunadi va aytib bera oladi (tezkor nazorat, og'zaki) | 30 |
| Amaliy topshiriq: to'g'ri va to'liq, mustaqil bajarilgan | 30 |
| Ish sifati: toza arxitektura, SOLID tamoyillari, testlar mavjudligi | 20 |
| Uyga vazifa bajarilgan va o'z vaqtida topshirilgan | 20 |
| **Jami** | **100** |

---

## 7-dars. Clean Code va SOLID: SRP hamda OCP

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | DRY/KISS/YAGNI mohiyati; nomlash odobi; SRP va OCP qoidalarini izohlay olishi | |
| Amaliyot /30 | Spaghetti funksiyani Extract Method bilan bo'lish; mas'uliyatlarni alohida sinflarga ajratish | |
| Ish sifati /20 | `abc.ABC` orqali to'g'ri abstraksiya; yangi to'lov sinfi qo'shilganda asosiy kod o'zgarmasligi | |
| Uyga vazifa /20 | `order_processor.py` to'liq refaktoring qilingan; GitHub tarmog'ida Conventional Commitlar | |
| **Jami /100** | | |

Izoh: ____________________

---

## 8-dars. SOLID: LSP, ISP, DIP va Refaktoring

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | LSP va voris sinf kafolati; ISP bo'yicha kichik interfeyslar; DIP va DI farqi | |
| Amaliyot /30 | `UserRepository` interfeysini qurish; `UserService`ga Dependency Injection qo'llash | |
| Ish sifati /20 | Bazasiz (in-memory mock) unit-test yozilgani; Code Smell'lar to'g'ri aniqlangani | |
| Uyga vazifa /20 | `test_user_service.py` to'liq o'tgan; mustaqil test natijalari mavjud | |
| **Jami /100** | | |

Izoh: ____________________

---

## 9-dars. Loyihalash andozalari: Factory va Singleton

| Mezon | Nimaga qaraladi | Ball |
|---|---|---|
| Tezkor nazorat /30 | GoF 3 toifasi; Factory Method vazifasi; Singleton ishlashi va testdagi xatarlari | |
| Amaliyot /30 | Python'da `__new__` orqali Singleton tuzish; `AppConfig` yagona nusxasini isbotlash | |
| Ish sifati /20 | Factory'da noma'lum turlar uchun istisno boshqaruvi; toza va ortiqcha yuklanmagan kod | |
| Uyga vazifa /20 | `NotificationFactory` va `AppConfig` Singleton to'liq yozilgan; PR ochilgan | |
| **Jami /100** | | |

Izoh: ____________________

---

## 3-hafta yakuni: o'sish dinamikasi

| Hafta | Darslar | O'rtacha ball | Baho | Asosiy yutuq / Aniqlangan bo'shliq |
|---|---|---|---|---|
| 1-hafta | 1–3 (SDLC, Git) | | | |
| 2-hafta | 4–6 (Branching, PR) | | | |
| 3-hafta | 7–9 (SOLID, Patterns) | | | |

**Mentor tavsiyasi:** O'quvchi professional backend arxitekturasining tamal toshlari bo'lgan Clean Code, SOLID va Creational patternlarni to'liq o'zlashtirdi. Keyingi 4-haftada Observer andozasi orqali voqealarga asoslangan tizimlar hamda zamonaviy veb-xizmatlarning poydevori &mdash; REST API va JSON arxitekturasi o'rganiladi.
