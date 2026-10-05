# 8-dars: Grid tizimlari va kompozitsiya

**Sinf:** 10-sinf  
**Yo'nalish:** Advanced UX/UI dizayn va Advanced Front-end  
**Hafta:** 3-hafta, 2-dars  

---

## Darsning qisqacha mazmuni

Ushbu darsda biz raqamli interfeysning ko'rinmas skeleti — **Grid (panjara) tizimlari** va kompozitsiya qoidalari bilan tanishamiz. Siz 6 ta asosiy grid turini (Baseline, Column, Modular, Manuscript, Pixel, Hierarchical), 12 ustunli responsiv panjara anatomiyasini (Columns, Gutter, Margin) hamda zamonaviy dizayn sanoatining qat'iy standarti bo'lgan **8pt spacing tizimi**ni o'rganasiz.

---

## Asosiy tushunchalar va atamalar

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

## Nazariy xulosa

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

## Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq · oson
Grid tizimining UX/UI dizayndagi asosiy vazifasini 2 jumlada tushuntiring: u dizaynerga qanday yordam beradi?

### 2-topshiriq · oson
Column Grid dagi "Gutter" nima va nima sababdan Gutter bo'shlig'i ustiga biron-bir matn yoki rasm qo'yish taqiqlanadi?

### 3-topshiriq · oson
Desktop (kompyuter), planshet va mobil telefon ekranlari uchun standart bo'yicha nechtadan ustun (columns) ishlatiladi?

### 4-topshiriq · o'rta
Baseline Grid qanday vazifani bajaradi? U maktabdagi qanday buyumga o'xshatiladi?

### 5-topshiriq · o'rta
Modular Grid va Column Grid o'rtasidagi asosiy farq nimada? Modular grid qanday turdagi raqamli mahsulotlarda (masalan, dashboardlar) ko'proq qo'llanadi?

### 6-topshiriq · o'rta
Nima uchun UI dizaynda 8pt (8 piksel) spacing tizimi qo'llaniladi? Uning Retina ekranlar va dasturchilar (Frontend) uchun qanday qulayliklari bor?

### 7-topshiriq · o'rta
12 ustunli Desktop gridda 6 ta teng hajmdagi hamkor kompaniyalar logotiplarini joylashtirmoqchisiz. Har bir logotip necha ustun kenglikni egallashi kerak?

### 8-topshiriq · qiyin
Kichik mahsulot kartochkasi ichidagi quyidagi xato piksellarni 8pt tizimiga muvofiq qayta to'g'rilang:
- Kartochkaning ichki chetlari (padding): `11px`;
- Tovar rasmi va narx orasidagi masofa: `6px`;
- Narx va "Savatga qo'shish" tugmasi orasidagi masofa: `21px`.

### 9-topshiriq · qiyin
Elektron do'konning bosh sahifasidagi 4 ta tovar kartochkasining responsiv o'zgarishini tavsiflang:
- Desktopda (12 ustun) qanday joylashadi?
- Planshetda (8 ustun) qanday o'zgaradi?
- Mobilda (4 ustun) qanday ko'rinishga keladi?

### 10-topshiriq · bonus
Figma dasturida 1440px kenglikdagi Frame yarating, unga 12 ustunli Layout Grid (Gutter: 24px, Margin: 80px) o'rnating va ushbu grid ustida 3 ta xizmatlar kartochkasini mukammal tekislab joylashtiring.
