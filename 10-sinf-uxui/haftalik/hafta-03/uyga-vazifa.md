# 3-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 7-dars: Ranglar psixologiyasi va tipografiya

1. O'zingiz tanlagan bitta veb-sayt yoki mobil ilova loyihasi uchun **60-30-10 qoidasi** bo'yicha ranglar palitrasini tuzing:
   - 60% — Asosiy fon rangi;
   - 30% — Ikkilamchi strukturaviy rang (kartochkalar, matn, menyu);
   - 10% — Aksent rang (harakatga chaqiruvchi tugmalar va diqqatni tortuvchi elementlar).
2. Tanlagan aksent rang va uning ustidagi matn kontrasti **WCAG AA (kamida 4.5 : 1)** talabiga to'liq javob berishini kontrast tekshiruvchi vosita (masalan, WebAIM Contrast Checker) orqali tekshirib, natijasini yozing.
3. Shrift o'lchamlari uchun **Modular Scale (1.250 — Major Third)** asosida o'lchamlar ierarxiyasini tuzing: Body (16px), Subtitle (20px), H3 (25px), H2 (31px), H1 (39px).

---

## 8-dars: Grid tizimlari va kompozitsiya

1. Desktop ekran (12 ustunli grid) uchun quyidagi sahifa strukturasini loyihalang va har bir blok necha ustun egallashini yozing:
   - Chap tomondagi doimiy navigatsiya paneli (sidebar);
   - O'rtadagi asosiy kontent va maqolalar bloki;
   - O'ng tomondagi tezkor bildirishnomalar va tavsiyalar bloki.
2. Sanoat standarti bo'lgan **8pt spacing (panjara) tizimi**dan foydalanib, bitta mahsulot kartochkasi ichidagi barcha masofalarni (ichki padding, rasm va sarlavha orasi, matn va tugma orasi) faqat 8 ga karrali (4, 8, 16, 24, 32px) o'lchamlarda belgilang.
3. 12 ustunli desktop grididan 4 ustunli mobil gridga o'tganda kartochkalar qanday qayta joylashishini 2-3 jumlada tushuntiring.

---

## 9-dars: Ikonka, tugma va navigatsiya elementlarini dizayni (UI Kit)

1. Figma dasturida **Auto Layout (`Shift + A`)** yordamida bitta Primary va bitta Secondary tugma yarating:
   - Matn: Inter / Roboto, 16px, Semibold;
   - Ichki padding: Horizontal — 24px, Vertical — 12px;
   - Burchak radiusi: 8px;
   - Minimal balandlik kamida 44px bo'lishini ta'minlang.
2. Yaratingan Primary tugma uchun 5 ta holatni (Enabled, Hover, Focus, Active, Disabled) loyihalashtiring va ularni bitta Component Set (Variants) sifatida birlashtiring.
3. Yangi mobil ilova uchun 4 ta universal navigatsiya piktogrammasini (Bosh sahifa, Qidiruv, Xabarlar, Profil) 24×24px freymlar ichida tartibga keltiring.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **7-dars vazifasi (30 ball):** 60-30-10 qoidasi to'g'ri qo'llangani, kontrast koeffitsienti 4.5:1 dan yuqori ekani va modular scale tipografik pog'onalari to'g'ri hisoblangani.
- **8-dars vazifasi (35 ball):** 12 ustunli gridda bloklar taqsimoti matematik to'g'ri yig'ilgani ($Sidebar + Content + Aside = 12$), 8pt spacing qat'iy saqlangani va responsiv mantiq tushunilgani.
- **9-dars vazifasi (35 ball):** Figma Auto Layout to'g'ri ishlashi, 44px me'yoriga rioya qilingani, tugmaning barcha 5 ta holati xatosiz ko'rsatilgani va universal ikonalar tanlangani.

### Eslatma
- O'quvchilar tugma ichiga matn yozayotganda noaniq jumlalardan qochishi va Auto Layout parametrlarida qat'iy 8pt qoidasiga (padding 24x12px) amal qilishini tekshiring.
