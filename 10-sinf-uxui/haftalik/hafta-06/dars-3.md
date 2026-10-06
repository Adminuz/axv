# 18-dars. CSS Grid layout tizimi va murakkab sahifa to'rlari

**Fan:** Advanced UX/UI dizayn va Advanced Front-end
**Sinf:** 10-sinf
**Hafta:** 6-hafta, 3-dars (umumiy 18-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (3.2 «Grid tizimlari va kompozitsiya»: grid ning mazmuni va 6 turi (Baseline, Column, Modular, Manuscript, Pixel, Hierarchical), mobilda 3 ustun va desktopda 12 ustun yondashuvi, 8pt grid, CSS Grid). CSS Grid xossalari (`grid-template-columns`, `fr`, `repeat`, `minmax`, `grid-template-areas`) standart CSS hujjatlaridan (MDN) qo'shildi.

---

## Darsning maqsadi

`display: grid` bilan qator va ustunlardan iborat ikki o'lchamli to'rni, `grid-template-columns`, `fr`, `repeat()`, `minmax()`, `gap`, `grid-template-areas` va `repeat(auto-fit, minmax(...))` yordamida responsiv kartalar to'rini yasashni hamda Grid va Flexbox ni qachon tanlashni o'rgatish.

## Kutiladigan natija

- `display: grid` va `grid-template-columns` bilan ustunlar yaratadi;
- `fr`, `repeat()` va `minmax()` dan foydalanadi;
- `grid-template-areas` bilan sahifa maketi (header, sidebar, main, footer) yasaydi;
- `repeat(auto-fit, minmax(200px, 1fr))` bilan responsiv to'r quradi;
- Grid va Flexbox farqini ayta oladi va to'g'ri tanlaydi.

## Kerakli jihozlar

- Kompyuter, brauzer va VS Code
- DevTools da Grid belgisi (`grid` badge) va setka ko'rinishi
- Maktab saytining `style.css` fayli (16–17-darslar)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 17-dars: Flexbox, navbar, kartalar |
| 08–22 | Yangi mavzu 1 | Grid tushunchasi, ustunlar, `fr` va `gap` |
| 22–32 | Yangi mavzu 2 | `repeat()`, `minmax()`, `auto-fit` bilan responsiv to'r |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | `grid-template-areas`: sahifa maketi |
| 50–75 | Amaliyot | Grid va Flexbox tanlovi, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. display: grid, fr va gap

**Grid** — ikki o'lchamli tizim: bir vaqtda **ustun** ham, **qator** ham boshqariladi. Konteynerga `display: grid` beriladi, ustunlar `grid-template-columns` bilan aniqlanadi. Maxsus birlik **`fr`** (fraction) — bo'sh joyning ulushi: `1fr 2fr` — ikkinchi ustun birinchisidan 2 baravar keng. `repeat(3, 1fr)` — 3 ta teng ustun. Oraliq `gap` bilan beriladi. Qo'llanmadagi grid tamoyillari (ustunlar, gutter, tekislash) aynan shu: dizaynerlar 12 ustunli to'r bilan ishlaydi, mobilda esa 3–4 ustunga o'tadi.

`fr` mavjud bo'sh joyni bo'ladi, `gap` hisobga olinadi. Qatorlar elementlar soniga qarab avtomatik qo'shiladi.

### 2. grid-template-areas bilan sahifa maketi

Sahifaning katta qismlarini nomlab, maketni **xarita** ko'rinishida yozish mumkin: **`grid-template-areas`**. Har qatorda ustun nomlari yoziladi, bir xil nom birlashadi (kenglik bo'ylab cho'ziladi). Elementga `grid-area: nom` beriladi. Maktab sayti uchun: yuqorida `header`, chapda `sidebar`, o'rtada `main`, pastda `footer`. Mobil versiyada media-so'rov ichida `areas` ni ustun ko'rinishiga o'zgartirish yetarli (keyingi dars: Mobile First). Bu usul kod o'qilishini keskin yaxshilaydi: maketni darrov ko'rasiz.

Har qatordagi ustunlar soni bir xil bo'lishi kerak va nomlar to'rtburchak shakl hosil qilsin (L shakl mumkin emas).

### 3. repeat(auto-fit, minmax()) va Grid yoki Flex tanlovi

Media-so'rovsiz moslashuvchan to'r: **`grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))`**. `minmax(200px, 1fr)` — ustun kamida 200px, ko'pi bilan teng ulush; `auto-fit` — sig'gancha ustun joylaydi, oyna torayganda ustunlar kamayadi (mobilda 1 ta). Yana: `grid-column: span 2` elementni 2 ustunga yoyadi (masalan, asosiy yangilik kartasi). **Tanlov:** bir yo'nalishli tekislash (navbar, tugmalar qatori, kartaning ichki qismi) — **Flexbox**; ikki yo'nalishli maket (sahifa, galereya, kartalar to'ri) — **Grid**. Ikkalasi birga ishlatiladi: sahifa — Grid, navbar — Flexbox.

`auto-fit` o'rniga `auto-fill` bo'sh ustunlarni saqlab qoladi; kartalar uchun odatda `auto-fit` qulayroq.

---

## Kod namunasi

Maktab sayti: sahifa maketi va kartalar to'ri

```css
body {
  display: grid;
  grid-template-columns: 220px 1fr;
  grid-template-areas:
    "header  header"
    "sidebar main"
    "footer  footer";
  min-height: 100vh;
  gap: 16px;
}
header { grid-area: header; }
aside  { grid-area: sidebar; }
main   { grid-area: main; }
footer { grid-area: footer; }

.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
}
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). 3 ustun
Konteynerda 3 ta teng ustun va 16px oraliq yarating.

**Kutiladigan natija:** Uch ustunli to'r.

**Yechim:** .grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

### 2-topshiriq (oson). fr hisobi
`1fr 3fr` da ikkinchi ustun nechta marta keng?

**Kutiladigan natija:** 3 marta.

**Yechim:** `1fr 3fr`: ikkinchi ustun 3 baravar keng.

### 3-topshiriq (o'rta). Sidebar maket
Chap ustun 220px, o'ng ustun qolgan joyni olsin.

**Kutiladigan natija:** Sidebar va asosiy qism.

**Yechim:** .layout {
  display: grid;
  grid-template-columns: 220px 1fr;
}

### 4-topshiriq (o'rta). Areas
header, sidebar, main, footer maketini `areas` bilan yozing.

**Kutiladigan natija:** To'rt qismli sahifa.

**Yechim:** grid-template-areas:
  "header header"
  "sidebar main"
  "footer footer";

### 5-topshiriq (qiyin). Responsiv kartalar
Kartalar kamida 200px bo'lib, oynaga qarab ustun sonini o'zgartirsin.

**Kutiladigan natija:** Ustun soni avtomatik o'zgaradi.

**Yechim:** grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));

### 6-topshiriq (qo'shimcha). Yoyilgan karta
Birinchi kartani 2 ustunga yoying.

**Kutiladigan natija:** Katta karta.

**Yechim:** .card:first-child { grid-column: span 2; }

---

## Tezkor nazorat (dars oxirida)

1. Grid nechta o'lchamli? — Ikki o'lchamli: ustun va qator.
2. `fr` nima? — Bo'sh joyning ulushi.
3. `repeat(3, 1fr)` nima beradi? — Uchta teng ustun.
4. `grid-area` nima uchun? — Elementni nomlangan sohaga joylashtirish.
5. Grid va Flexbox qachon? — Ikki yo'nalish — Grid; bir yo'nalish — Flexbox.

## Keng tarqalgan xatolar

- Sahifa maketi uchun Flexbox ni majburlash.
- `grid-template-areas` da qatorlar uzunligi har xil bo'lishi.
- `gap` o'rniga margin ishlatib, chetda ortiqcha bo'sh joy qoldirish.
- `fr` ni piksel bilan aralashtirib hisoblashda adashish.
- Mobil uchun to'r o'zgartirishni unutish.

## Bilasizmi? (qo'shimcha)

- DevTools da Grid belgisi bosilsa, setka chiziqlari va nomlari ko'rinadi.
- Qo'llanmadagi 6 turdagi gridlar: Baseline, Column, Modular, Manuscript, Pixel, Hierarchical.
- Qo'llanma tavsiyasi: oraliqlar uchun 8pt grid (8, 16, 24, 32 piksel).
