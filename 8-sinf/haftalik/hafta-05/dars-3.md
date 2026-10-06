# 15-dars. Responsiv dizayn va media so'rovlar

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **II-bob**, 15-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilar moslashuvchan (responsiv) dizayn tushunchasi va afzalliklarini, `viewport` meta tegini, fluid layout va flexible grid (%, `fr`, `max-width`) g'oyasini, media so'rovlar (`@media`) sintaksisini, breakpoint tushunchasini, mobile-first (`min-width`) va desktop-first (`max-width`) yondashuvlarini hamda rasmlarni moslashtirishni (`max-width: 100%`, `height: auto`, `object-fit`) o'rganib, 13–14-darsdagi Flexbox/Grid maketini telefon, planshet va kompyuterga moslashtiradi.

**Kutiladigan natija:**
- Responsiv dizayn nima ekanini va nega kerakligini 2–3 sabab bilan tushuntiradi.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` vazifasini aytadi.
- `@media (min-width: 768px) { ... }` yozuvini o'qiydi va yozadi; `min-width` va `max-width` farqini biladi.
- Telefon / planshet / kompyuter uchun breakpointlarni tanlaydi (masalan, 576, 768, 992 px).
- Mobile-first va desktop-first yondashuvlarini farqlaydi.
- Rasmni konteynerdan toshirmaslik uchun `max-width: 100%; height: auto;` va `object-fit: cover` ni qo'llaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 daq | Takrorlash | Grid: `fr`, `repeat`, `grid-column`, Grid vs Flex |
| 8–35 daq | Yangi mavzu | Responsiv dizayn, viewport, fluid layout, `@media`, breakpoint, mobile-first, rasmlar |
| 35–40 daq | Tanaffus | Ko'z mashqlari |
| 40–70 daq | Amaliyot | Kartalar sahifasini 1 → 2 → 3 ustunga moslashtirish, DevTools'da tekshirish |
| 70–76 daq | Tezkor nazorat | 5 ta savol |
| 76–80 daq | Xulosa | Uyga vazifa, keyingi dars: responsiv maket va Figma |

> Manba: o'quv dasturi — 7-mavzu «Moslashuvchan (responsiv) dizayn va media so'rovlar va Figma» («Moslashuvchan (responsiv) dizayn tushunchasi va afzalliklari, fluid layout va flexible grid tizimlari, media so'rovlar (CSS media queries) sintaksisi va ishlatilishi (@media), turli ekran o'lchamlari uchun stil berish, breakpoints tushunchasi, mobil-first va desktop-first yondashuvlar, rasm va kontentni moslashtirish (responsive images, max-width, height: auto, object-fit)»), kutilgan natijalar: «Media queries yordamida turli ekran o'lchamlariga moslashishni biladi», «Planshet va desktop uchun alohida style yozishni biladi», «Breakpoint tushunchasini biladi», «max-width va min-width ni ishlay oladi», «Flexbox va Grid bilan responsiv layout yaratish». Uslubiy ko'rsatmada mavzu faqat nomi bilan berilgan — misollar CSS standarti asosida mentor tomonidan tuzildi. Figma qismi — 16–17-darslar.

---

## 2. Konspekt

### 2.1. Takrorlash (8 daqiqa)
- `grid-template-columns: repeat(3, 1fr)` nima beradi? `grid-column: 1 / -1`?
- O'tgan darsdagi 3 ustunli galereyani telefonda ochsak nima bo'ladi? (Rasmlar juda kichrayadi — bugun buni tuzatamiz.)

### 2.2. Responsiv dizayn nima?
- **Responsiv (moslashuvchan) dizayn** — bitta sahifa har qanday ekran kengligiga (telefon, planshet, noutbuk, katta monitor) o'zini moslashtiradi: ustunlar soni, shrift, masofalar o'zgaradi.
- Afzalliklari: bitta kod — barcha qurilmalar; foydalanuvchiga qulay (kattalashtirish va gorizontal aylantirish kerak emas); internet foydalanuvchilarining katta qismi telefondan kiradi; qidiruv tizimlari mobilga mos saytlarni yuqoriroq ko'rsatadi.

### 2.3. Viewport meta tegi
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
Bu tegsiz telefon brauzeri sahifani «kompyuter kengligida» chizib, kichraytirib ko'rsatadi — media so'rovlar kutilgandek ishlamaydi. `<head>` ichida **har doim** bo'lishi kerak.

### 2.4. Fluid layout va flexible grid
- **Fluid (oquvchan) layout** — o'lchamlar qat'iy `px` o'rniga nisbiy birliklarda: `%`, `fr`, `vw`, `rem`.
- `max-width` — kenglikni cheklaydi, lekin torroq ekranda kichrayishga ruxsat beradi:
```css
.konteyner { width: 90%; max-width: 1100px; margin: 0 auto; }
```
- **Flexible grid** — ustunlar `fr`/`%` da: `grid-template-columns: repeat(3, 1fr);` yoki Flexbox'da `flex: 1 1 250px` + `flex-wrap: wrap`.

### 2.5. Media so'rovlar (`@media`)
```css
/* sintaksis */
@media (shart) {
  selektor { xususiyat: qiymat; }
}

@media (min-width: 768px) { ... }   /* ekran 768px va undan KENG bo'lsa */
@media (max-width: 767px) { ... }   /* ekran 767px va undan TOR bo'lsa */
@media (min-width: 768px) and (max-width: 991px) { ... } /* faqat planshet */
```
Media so'rov ichidagi qoidalar **faqat shart bajarilganda** ishlaydi va pastda yozilgani uchun avvalgi qoidani bosib o'tadi (kaskad).

### 2.6. Breakpoint (to'xtash nuqtasi)
**Breakpoint** — dizayn o'zgaradigan ekran kengligi. Ko'p ishlatiladigan qiymatlar (Bootstrap'dagi bilan bir xil):

| Breakpoint | Qurilma |
|---|---|
| < 576px | telefon (tik holat) |
| ≥ 576px | katta telefon |
| ≥ 768px | planshet |
| ≥ 992px | noutbuk |
| ≥ 1200px | katta monitor |

Qoida: breakpointni qurilma nomiga emas, **dizayn «buzilgan» joyiga** qo'ying.

### 2.7. Mobile-first va desktop-first
| | Mobile-first | Desktop-first |
|---|---|---|
| Asosiy CSS | telefon uchun | kompyuter uchun |
| Media so'rov | `min-width` (kengaygan sari qo'shiladi) | `max-width` (toraygan sari o'zgaradi) |
| Afzallik | sodda asos, telefon tez yuklaydi, zamonaviy standart | eski saytlarni moslashtirishda qulay |

```css
/* MOBILE-FIRST: kartalar */
.kartalar { display: grid; grid-template-columns: 1fr; gap: 16px; }

@media (min-width: 768px) {
  .kartalar { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 992px) {
  .kartalar { grid-template-columns: repeat(3, 1fr); }
}
```

### 2.8. Rasm va kontentni moslashtirish
```css
img { max-width: 100%; height: auto; }   /* konteynerdan toshmaydi, nisbati saqlanadi */
.muqova { width: 100%; height: 200px; object-fit: cover; } /* kesib to'ldiradi */
```
- `object-fit: cover` — ramkani to'ldiradi, ortiqchasini kesadi; `contain` — to'liq ko'rinadi, bo'sh joy qolishi mumkin.
- Matn: sarlavhani telefonda kichikroq qilish — `h1 { font-size: 28px; }` va `@media (min-width: 992px) { h1 { font-size: 44px; } }`.

### 2.9. DevTools'da tekshirish
F12 → **Toggle device toolbar** (Ctrl+Shift+M) — iPhone, iPad va boshqa o'lchamlarni tanlab, breakpointlarda dizayn qanday o'zgarishini ko'rish.

### 2.10. Odatiy xatolar
- `viewport` meta tegi yo'q — telefonda sahifa mayda ko'rinadi.
- `@media` ichida qavs yoki `px` unutilgan: `@media min-width: 768` — ishlamaydi.
- Mobile-first'da `max-width` ishlatib, qoidalarni chalkashtirish.
- Media so'rovni asosiy qoidadan **oldin** yozish — pastdagi asosiy qoida uni bosib o'tadi.
- Rasmlarga qat'iy `width: 800px` berish — telefonda gorizontal aylantirish paydo bo'ladi.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Rangni o'zgartiruvchi sahifa
**Vazifa:** sahifa foni telefonda (767px gacha) och sariq, 768px dan kengda och ko'k bo'lsin. DevTools'da tekshiring.
**Kutiladigan natija:** oyna kengligi o'zgarganda fon almashadi.
**Yechim:**
```css
body { background: lightyellow; }
@media (min-width: 768px) {
  body { background: lightblue; }
}
```

### 2-topshiriq (o'rta). 1 → 2 → 3 ustunli kartalar
**Vazifa:** 6 ta kartani mobile-first usulida joylang: telefonda 1 ustun, planshetda (≥768px) 2 ustun, noutbukda (≥992px) 3 ustun. Rasmlar kartadan toshmasin.
**Kutiladigan natija:** uchta breakpointda turli ustunlar soni.
**Yechim:**
```css
* { box-sizing: border-box; }
.konteyner { width: 90%; max-width: 1100px; margin: 0 auto; }
.kartalar  { display: grid; grid-template-columns: 1fr; gap: 16px; }
.karta img { max-width: 100%; height: auto; display: block; }

@media (min-width: 768px) { .kartalar { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 992px) { .kartalar { grid-template-columns: repeat(3, 1fr); } }
```

### 3-topshiriq (qiyin). Moslashuvchan sahifa maketi
**Vazifa:** 14-darsdagi «header–sidebar–main–footer» maketini moslashtiring: telefonda hammasi bitta ustunda (sidebar main'dan keyin), 768px dan boshlab sidebar chapda (220px). Header'dagi menyu telefonda havolalari ustun bo'lib tursin, kompyuterda bir qatorda.
**Kutiladigan natija:** tor ekranda 1 ustun, keng ekranda 2 ustunli maket; menyu yo'nalishi o'zgaradi.
**Yechim:**
```css
.sahifa { display: grid; grid-template-columns: 1fr; gap: 12px; }
aside   { order: 2; }                  /* telefonda main'dan keyin */
footer  { order: 3; }                  /* footer eng oxirida qolsin */
.menyu  { display: flex; flex-direction: column; gap: 8px; }

@media (min-width: 768px) {
  .sahifa { grid-template-columns: 220px 1fr; }
  header, footer { grid-column: 1 / -1; }
  aside, footer { order: 0; }
  .menyu { flex-direction: row; gap: 24px; }
}
```
Izoh: `order` — Grid va Flex elementlarining ko'rinish tartibini HTML'ni o'zgartirmasdan almashtiradi (qo'shimcha xususiyat).

---

## 4. Tezkor nazorat savollari (javoblari bilan)
1. **Savol:** Responsiv dizayn nima?
   **Javob:** sahifaning har qanday ekran kengligiga o'zini moslashtirishi (ustunlar, shrift, masofalar o'zgaradi).
2. **Savol:** `viewport` meta tegi bo'lmasa nima bo'ladi?
   **Javob:** telefon sahifani kompyuter kengligida chizib kichraytiradi — media so'rovlar to'g'ri ishlamaydi.
3. **Savol:** `@media (min-width: 768px)` qachon ishlaydi?
   **Javob:** ekran kengligi 768px yoki undan katta bo'lganda.
4. **Savol:** Mobile-first yondashuvi nimani bildiradi?
   **Javob:** asosiy CSS telefon uchun yoziladi, kengroq ekranlar uchun `min-width` bilan qoidalar qo'shiladi.
5. **Savol:** Rasm konteynerdan toshmasligi uchun nima yoziladi?
   **Javob:** `max-width: 100%; height: auto;`.
