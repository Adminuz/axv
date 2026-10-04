---
title: "14-dars. 8-dars: Grid tizimlari va kompozitsiya"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (UX/UI)", "link": "/10-sinf-uxui/"}, "week": {"n": 3, "link": "/10-sinf-uxui/hafta-03/"}, "g": 14, "title": "8-dars: Grid tizimlari va kompozitsiya", "lead": "Formalar, validatsiya va interfeys elementlari semantikasi", "slide": "/slaydlar/10-sinf-uxui/hafta-03/dars-8.html", "tabs": [{"g": 13, "link": "/10-sinf-uxui/hafta-03/dars-7", "current": false}, {"g": 14, "link": "/10-sinf-uxui/hafta-03/dars-8", "current": true}, {"g": 15, "link": "/10-sinf-uxui/hafta-03/dars-9", "current": false}], "prev": {"g": 13, "title": "7-dars: Ranglar psixologiyasi va tipografiya", "link": "/10-sinf-uxui/hafta-03/dars-7"}, "next": {"g": 15, "title": "9-dars: Ikonka, tugma va navigatsiya elementlarini dizayni (UI Kit)", "link": "/10-sinf-uxui/hafta-03/dars-9"}}
---

**Sinf:** 10-sinf  
**Yo'nalish:** Advanced UX/UI dizayn va Advanced Front-end  
**Hafta:** 3-hafta, 2-dars  

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Ushbu darsda biz raqamli interfeysning ko'rinmas skeleti — **Grid (panjara) tizimlari** va kompozitsiya qoidalari bilan tanishamiz. Siz 6 ta asosiy grid turini (Baseline, Column, Modular, Manuscript, Pixel, Hierarchical), 12 ustunli responsiv panjara anatomiyasini (Columns, Gutter, Margin) hamda zamonaviy dizayn sanoatining qat'iy standarti bo'lgan **8pt spacing tizimi**ni o'rganasiz.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar va atamalar

| Atama | Inglizcha | Tavsif |
|---|---|---|
| **Grid tizimi** | Grid System | Sahifadagi barcha elementlarni tartibga soluvchi vertikal va gorizontal chiziqlar to'ri |
| **Columns** | Columns (Ustunlar) | Kontent va kartochkalar joylashtiriladigan vertikal maydonlar |
| **Gutter** | Gutter | Ustunlar orasidagi ajratuvchi bo'shliq masofasi (odatda 16px yoki 24px) |
| **Margin** | Margin | Ekranning o'ng va chap chegaralaridagi xavfsiz bo'shliq |
| **8pt Grid** | 8pt Spacing System | Barcha o'lcham va oraliqlarni 8 ga karrali (4, 8, 16, 24, 32, 48px) qilib belgilash qoidasi |
| **Baseline Grid** | Baseline Grid | Matn satrlarining pastki qismini tekislovchi gorizontal chiziqlar to'plami |
| **Modular Grid** | Modular Grid | Ustunlar va qatorlar kesishmasidan tashkil topgan modulli kataklar panjarasi |

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy xulosa

### 1. 6 ta asosiy grid turi
1. **Baseline Grid:** Gorizontal matn chiziqlari (daftar katagi kabi).
2. **Column Grid:** Vertikal ustunlar (veb va mobil interfeyslar asosi).
3. **Modular Grid:** Ustun + qatorlar (murakkab jadvallar va dashboardlar).
4. **Manuscript Grid:** Bitta katta blok (kitoblar va maqolalar).
5. **Pixel Grid:** Piksel darajasidagi to'r (ikonkalar chizish).
6. **Hierarchical Grid:** Kontent ehtiyojidan kelib chiqadigan erkin panjara.

### 2. Responsiv ustunlar standarti
- **Desktop:** 12 ta ustun;
- **Planshet (Tablet):** 8 ta ustun;
- **Mobil (Mobile):** 4 ta ustun.

### 3. Oltin qoidalar
- Elementlar ustun ichida boshlanib, ustun ichida tugaydi.
- Gutterga element joylashtirilmaydi.
- Oraliq masofalar tasodifiy sonlar (13px, 17px) emas, 8pt tizimi (8, 16, 24, 32px) bo'yicha beriladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Grid tizimining UX/UI dizayndagi asosiy vazifasini 2 jumlada tushuntiring: u dizaynerga qanday yordam beradi?

### 2-topshiriq <Badge type="tip" text="oson" />
Column Grid dagi "Gutter" nima va nima sababdan Gutter bo'shlig'i ustiga biron-bir matn yoki rasm qo'yish taqiqlanadi?

### 3-topshiriq <Badge type="tip" text="oson" />
Desktop (kompyuter), planshet va mobil telefon ekranlari uchun standart bo'yicha nechtadan ustun (columns) ishlatiladi?

### 4-topshiriq <Badge type="warning" text="o'rta" />
Baseline Grid qanday vazifani bajaradi? U maktabdagi qanday buyumga o'xshatiladi?

### 5-topshiriq <Badge type="warning" text="o'rta" />
Modular Grid va Column Grid o'rtasidagi asosiy farq nimada? Modular grid qanday turdagi raqamli mahsulotlarda (masalan, dashboardlar) ko'proq qo'llanadi?

### 6-topshiriq <Badge type="warning" text="o'rta" />
Nima uchun UI dizaynda 8pt (8 piksel) spacing tizimi qo'llaniladi? Uning Retina ekranlar va dasturchilar (Frontend) uchun qanday qulayliklari bor?

### 7-topshiriq <Badge type="warning" text="o'rta" />
12 ustunli Desktop gridda 6 ta teng hajmdagi hamkor kompaniyalar logotiplarini joylashtirmoqchisiz. Har bir logotip necha ustun kenglikni egallashi kerak?

### 8-topshiriq <Badge type="danger" text="qiyin" />
Kichik mahsulot kartochkasi ichidagi quyidagi xato piksellarni 8pt tizimiga muvofiq qayta to'g'rilang:
- Kartochkaning ichki chetlari (padding): `11px`;
- Tovar rasmi va narx orasidagi masofa: `6px`;
- Narx va "Savatga qo'shish" tugmasi orasidagi masofa: `21px`.

### 9-topshiriq <Badge type="danger" text="qiyin" />
Elektron do'konning bosh sahifasidagi 4 ta tovar kartochkasining responsiv o'zgarishini tavsiflang:
- Desktopda (12 ustun) qanday joylashadi?
- Planshetda (8 ustun) qanday o'zgaradi?
- Mobilda (4 ustun) qanday ko'rinishga keladi?

### 10-topshiriq <Badge type="info" text="bonus" />
Figma dasturida 1440px kenglikdagi Frame yarating, unga 12 ustunli Layout Grid (Gutter: 24px, Margin: 80px) o'rnating va ushbu grid ustida 3 ta xizmatlar kartochkasini mukammal tekislab joylashtiring.

</div>

