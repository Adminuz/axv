# 16-dars. CSS3 selektorlari, kaskadlik va Box Model arxitekturasi

**Fan:** Advanced UX/UI dizayn va Advanced Front-end
**Sinf:** 10-sinf
**Hafta:** 6-hafta, 1-dars (umumiy 16-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` V bob (front-end bo'limi: CSS3, media so'rovlar). Selektorlar, specificity (kuchlilik) va Box Model rejadagi mavzu bo'yicha standart CSS hujjatlaridan (MDN) qo'shildi; maktab sayti misollari mualliflik.

---

## Darsning maqsadi

CSS qoidasining tuzilishini, asosiy selektor turlarini (teg, class, id, avlod, bola, atribut, pseudo-class), kaskad va specificity qoidasini, meros (inheritance) ni hamda Box Model (content, padding, border, margin) va `box-sizing: border-box` ni o'rgatish.

## Kutiladigan natija

- CSS qoidasini (selektor, xossa, qiymat) o'qiydi va yozadi;
- Teg, class, id, avlod (`a b`) va bola (`a > b`) selektorlarini ishlatadi;
- Specificity ni hisoblab, qaysi qoida g'olib bo'lishini aytadi;
- Box Model ning 4 qatlamini (content, padding, border, margin) chizadi;
- `box-sizing: border-box` ni qo'llab, o'lchamlarni to'g'ri hisoblaydi.

## Kerakli jihozlar

- Kompyuter, brauzer va matn muharriri (VS Code)
- Brauzer DevTools (Elements va Computed)
- Maktab saytining 5-haftadagi `index.html` fayli

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 15-dars: SEO va meta teglar, semantik tuzilma |
| 08–22 | Yangi mavzu 1 | CSS qoidasi va selektorlar |
| 22–32 | Yangi mavzu 2 | Kaskad, specificity va meros |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Box Model: DevTools da o'lchamlarni ko'rish va sozlash |
| 50–75 | Amaliyot | Xatolar, `border-box`, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. CSS qoidasi va selektorlar

CSS qoidasi 3 qismdan iborat: **selektor** (kimga), **xossa** (nimani) va **qiymat** (qanday): `h1 { color: navy; }`. Asosiy selektorlar: **teg** (`p`), **class** (`.card`, qayta ishlatiladi), **id** (`#logo`, sahifada bitta), **avlod** (`nav a`, ichidagi hamma `a`), **bola** (`ul > li`, faqat bevosita farzand), **atribut** (`a[href^="https"]`), **guruh** (`h1, h2`). **Pseudo-class** holatni bildiradi: `a:hover` (ustiga olib kelinganda), `:focus` (fokusda), `li:nth-child(2)` (ikkinchi element). Amalda ko'p qismi **class** bilan bezaladi: id va teg selektorlari kamroq ishlatiladi.

Class nomini vazifasiga qarab bering (`.card`, `.btn`), ko'rinishiga qarab emas (`.red`). Id ni stil uchun kam ishlating.

### 2. Kaskad, specificity va meros

Bir elementga bir nechta qoida tegsa, **kaskad** hal qiladi. Tartib: 1) **kuchlilik (specificity)**, 2) teng bo'lsa — **keyin yozilgani** g'olib. Kuchlilik: inline `style` (1000) > **id** (100) > **class, atribut, pseudo-class** (10) > **teg** (1). Masalan, `nav a.active` = 1 + 1 + 10 = 12 va `a` = 1 dan kuchli. `!important` hamma narsani bosib o'tadi, lekin kodni boshqarib bo'lmas qiladi: undan qoching. Yana bir qoida — **meros (inheritance)**: `color`, `font-family`, `line-height` kabi xossalar ichki elementlarga o'tadi (`body` ga bir marta yozish yetadi), `margin`, `border` o'tmaydi.

Qoidani tuzatish uchun kuchliroq selektor yozish o'rniga, avval DevTools da qaysi qoida bosib o'tayotganini toping.

### 3. Box Model va box-sizing

Brauzer har elementni **quti** deb hisoblaydi. Ichdan tashqariga 4 qatlam: **content** (mazmun), **padding** (ichki bo'sh joy), **border** (chegara) va **margin** (tashqi masofa). Standart (`content-box`) holda `width` faqat content ni o'lchaydi: `width: 200px; padding: 20px; border: 2px` bo'lsa, quti haqiqatan **244px** kenglikda bo'ladi. Shuning uchun loyihaga `* { box-sizing: border-box; }` yoziladi: `width` padding va border ni ham o'z ichiga oladi, 200px = 200px. Qo'shni vertikal margin lar birlashadi (margin collapse): 20px va 30px orasida 50px emas, 30px qoladi. DevTools da Box Model diagrammasi ko'rinadi.

`margin: 0 auto` blokni gorizontal markazga qo'yadi (blok kengligi berilgan bo'lsa). `padding` bo'lsa — fon ichida, `margin` — fondan tashqarida.

---

## Kod namunasi

Maktab sayti kartasi uchun CSS:

```css
* { box-sizing: border-box; }
body { font-family: Arial, sans-serif; color: #222; line-height: 1.5; }

.card {
  width: 300px;
  padding: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin: 12px auto;
}
.card:hover { box-shadow: 0 4px 12px rgba(0, 0, 0, .15); }
.card > h2 { margin: 0 0 8px; }
nav a { text-decoration: none; }
nav a:hover { color: crimson; }
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Selektor yozing
Barcha `h2` ni ko'k, `.note` ni sariq fonda bering.

**Kutiladigan natija:** Ikki qoida.

**Yechim:** h2 { color: blue; }
.note { background: #fff3b0; }

### 2-topshiriq (oson). Specificity
`nav a` va `.menu a` dan qaysi biri kuchli?

**Kutiladigan natija:** `.menu a` (11) > `nav a` (2).

**Yechim:** `.menu a`

### 3-topshiriq (o'rta). Quti hisobi
`content-box`: `width:200px; padding:20px; border:2px`. Umumiy kenglik?

**Kutiladigan natija:** 244px.

**Yechim:** 200 + 20·2 + 2·2 = 244px.

### 4-topshiriq (o'rta). border-box
Shu qutini umumiy kengligi 200px bo'ladigan qiling.

**Kutiladigan natija:** 200px.

**Yechim:** * { box-sizing: border-box; }

### 5-topshiriq (qiyin). Hover karta
`.card` ustiga kelganda soya chiqadigan qoidani yozing.

**Kutiladigan natija:** Soyali karta.

**Yechim:** .card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,.2);
}

### 6-topshiriq (qo'shimcha). Meros
`color` meros bo'ladimi, `border` ham? Misol bering.

**Kutiladigan natija:** `color` meros bo'ladi, `border` yo'q.

**Yechim:** `body { color: #222; }` hamma matnga o'tadi.

---

## Tezkor nazorat (dars oxirida)

1. CSS qoidasi qanday tuzilgan? — Selektor, xossa va qiymat.
2. Qaysi selektor kuchliroq: id yoki class? — Id (100) > class (10).
3. Box Model qatlamlari? — Content, padding, border, margin.
4. `border-box` nima beradi? — `width` ga padding va border ham kiradi.
5. Qaysi xossalar meros bo'ladi? — `color`, `font-family`, `line-height`.

## Keng tarqalgan xatolar

- Hammasiga `!important` yozish.
- Class o'rniga id ishlatish va takrorlash.
- `box-sizing` ni unutib, o'lchamlar chiqib ketishi.
- `margin` va `padding` ni aralashtirish.
- Ko'rinishga qarab class nomlash (`.red`).

## Bilasizmi? (qo'shimcha)

- Brauzerdagi `Computed` bo'limi elementning yakuniy qiymatlarini ko'rsatadi.
- `:where()` selektorning specificity sini 0 qiladi.
- Yangi CSS da `@layer` bilan kaskad tartibini boshqarish mumkin.
