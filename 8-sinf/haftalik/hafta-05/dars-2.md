# 14-dars. CSS Grid: satr va ustunlardan iborat to'r

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **II-bob**, 14-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilar CSS Grid tizimini (`display: grid`) o'rganadi: `grid-template-columns`, `grid-template-rows`, `fr` birligi, `repeat()`, `gap` (`grid-gap`), elementni bir nechta katakka cho'zish (`grid-column`, `grid-row`), kataklar ichida tekislash (`justify-items`, `align-items`, `place-items`) va Grid hamda Flexbox farqini amaliy sahifa maketida qo'llaydi.

**Kutiladigan natija:**
- Grid konteyner, grid element, satr (row), ustun (column), katak (cell) va chiziq (line) tushunchalarini ajratadi.
- `grid-template-columns: 1fr 2fr 1fr` va `repeat(3, 1fr)` yozuvini o'qiydi va natijani chizadi.
- `grid-column: 1 / 3` va `grid-column: span 2` bilan elementni cho'zadi.
- `place-items: center` — `justify-items` va `align-items` ning qisqa yozuvi ekanini biladi.
- Qachon Grid (ikki o'lchamli maket), qachon Flexbox (bir o'qli qator) tanlashni asoslaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 daq | Takrorlash | Flexbox: o'qlar, justify/align, wrap |
| 8–35 daq | Yangi mavzu | Grid to'r, fr, repeat, gap, cho'zish, tekislash, Grid vs Flex |
| 35–40 daq | Tanaffus | Ko'z mashqlari |
| 40–70 daq | Amaliyot | Galereya va «header–sidebar–main–footer» maketi |
| 70–76 daq | Tezkor nazorat | 5 ta savol |
| 76–80 daq | Xulosa | Uyga vazifa, keyingi dars: responsiv dizayn |

> Manba: o'quv dasturi — 6-mavzu «Veb-sahifani tuzishda box model, flexbox va grid tizimlari» («Grid tizimi (display: grid, grid-template-rows, grid-template-columns, grid-gap, grid-row, grid-column, justify-items, align-items, place-items). Grid va Flex farqlari va ularni amaliy veb-sahifa tuzishda qo'llash usullari»), kutilgan natijalar: «Grid tizimi yordamida murakkab layoutlarni tuzishni biladi», «Grid xususiyatlari (grid-template-columns, grid-template-rows, gap) bilan ishlay oladi». Uslubiy ko'rsatmada mavzu faqat nomi bilan berilgan — konspekt va misollar CSS standarti asosida mentor tomonidan tuzildi. `grid-template-areas` — qo'shimcha (dasturda nomlanmagan) bilim.

---

## 2. Konspekt

### 2.1. Takrorlash (8 daqiqa)
- `display: flex` qayerga yoziladi? `justify-content` va `align-items` qaysi o'qda ishlaydi?
- Flexbox bilan «3 ustun × 2 satr» galereyani aniq to'r qilib qurish qiyin — nega? (Flex bir o'qda ishlaydi; satrlar o'zaro tekislanmaydi.)

### 2.2. Grid nima?
Grid — **ikki o'lchamli** (satr va ustun) maket tizimi. Konteynerga `display: grid` yoziladi, bolalari kataklarga joylashadi.

| Atama | Ma'nosi |
|---|---|
| Grid konteyner | `display: grid` yozilgan ota element |
| Grid element | konteynerning bevosita bolasi |
| Ustun (column) / satr (row) | vertikal / gorizontal yo'lak |
| Katak (cell) | satr va ustun kesishgan joy |
| Chiziq (line) | ustunlar/satrlar orasidagi raqamlangan chegara: 1, 2, 3 ... |

### 2.3. Ustun va satrlar
```css
.galereya {
  display: grid;
  grid-template-columns: 200px 200px 200px;  /* 3 ta 200px ustun */
  grid-template-rows: 150px 150px;           /* 2 ta satr */
  gap: 16px;                                 /* eski nomi: grid-gap */
}
```
- **`fr`** (fraction — ulush) — bo'sh joyning ulushi: `1fr 2fr 1fr` → 25% · 50% · 25%.
- **`repeat(3, 1fr)`** = `1fr 1fr 1fr`.
- Aralash: `grid-template-columns: 250px 1fr;` — chap ustun qat'iy, o'ng ustun qolgan joy.
- `gap: 20px 10px` — satrlar orasi 20, ustunlar orasi 10 (`row-gap`, `column-gap`).

### 2.4. Elementni cho'zish: `grid-column` va `grid-row`
Chiziqlar 1 dan boshlab raqamlanadi: 3 ustunli to'rda 4 ta vertikal chiziq bor.
```css
.katta  { grid-column: 1 / 3; }   /* 1-chiziqdan 3-chiziqqacha = 2 ustun */
.uzun   { grid-row: 1 / 3; }      /* 2 satr balandlikda */
.keng   { grid-column: span 2; }  /* turgan joyidan 2 ustun */
.butun  { grid-column: 1 / -1; }  /* butun kenglik (-1 — oxirgi chiziq) */
```

### 2.5. Kataklar ichida tekislash
| Xususiyat | Yo'nalish | Qiymatlar |
|---|---|---|
| `justify-items` | katak ichida gorizontal | `stretch` (standart), `start`, `center`, `end` |
| `align-items` | katak ichida vertikal | `stretch`, `start`, `center`, `end` |
| `place-items` | ikkalasi birga | `place-items: center;` |

Bitta element uchun: `justify-self`, `align-self`.

### 2.6. Sahifa maketi
```css
.sahifa {
  display: grid;
  grid-template-columns: 220px 1fr;
  grid-template-rows: 70px 1fr 60px;
  gap: 12px;
  min-height: 100vh;
}
header { grid-column: 1 / -1; }
footer { grid-column: 1 / -1; }
```
Qo'shimcha: `grid-template-areas` bilan maketni «rasm» qilib yozish mumkin:
```css
.sahifa { grid-template-areas: "header header" "sidebar main" "footer footer"; }
header { grid-area: header; }
```

### 2.7. Grid va Flexbox farqi
| | Flexbox | Grid |
|---|---|---|
| O'lchamlar | bir o'q (qator **yoki** ustun) | ikki o'q (qator **va** ustun) |
| Yondashuv | kontentdan: elementlar o'lchamiga qarab joylashadi | maketdan: avval to'r, keyin elementlar |
| Qachon | menyu, tugmalar qatori, karta ichidagi joylashuv | butun sahifa maketi, galereya, dashboard |

Amalda **birga** ishlatiladi: sahifa — Grid, header ichidagi menyu — Flex.

### 2.8. Odatiy xatolar
- `grid-template-column` (s harfisiz) — xususiyat ishlamaydi.
- Chiziq va ustunni adashtirish: `grid-column: 1 / 3` — 3 ta emas, **2 ta** ustun.
- `fr` ni `%` bilan aralashtirib, `gap` ni hisobga olmaslik — `%` + `gap` toshib ketadi, `fr` esa gap'ni hisobga oladi.
- Bitta qatordagi menyu uchun Grid ishlatib, keraksiz murakkablashtirish.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). 3 × 2 galereya
**Vazifa:** 6 ta rasm (yoki rangli `div`) ni 3 ustun, 2 satrli to'rga joylang, oralari 16px, ustunlar teng.
**Kutiladigan natija:** teng 6 ta katak.
**Yechim:**
```css
.galereya { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.galereya img { width: 100%; height: 160px; object-fit: cover; border-radius: 8px; }
```

### 2-topshiriq (o'rta). Katta birinchi rasm
**Vazifa:** galereyadagi 1-rasm 2 ustun va 2 satrni egallasin.
**Kutiladigan natija:** chap yuqorida katta rasm, qolganlari atrofida.
**Yechim:**
```css
.galereya img:first-child { grid-column: span 2; grid-row: span 2; height: 100%; }
```
Izoh: `height: 100%` — katta katakni to'liq to'ldirish uchun (1-topshiriqdagi 160px ni bekor qiladi).

### 3-topshiriq (qiyin). Sahifa maketi
**Vazifa:** header (butun kenglik, 70px), chapda sidebar (220px), o'ngda main (qolgan joy), footer (butun kenglik, 60px). Header ichida logotip va menyu Flexbox bilan.
**Kutiladigan natija:** klassik 4 qismli maket; header ichida menyu o'ng chetda.
**Yechim:**
```html
<div class="sahifa">
  <header><b>AXV</b><nav><a href="#">Kurslar</a> <a href="#">Aloqa</a></nav></header>
  <aside>Sidebar</aside>
  <main>Asosiy kontent</main>
  <footer>© 2025</footer>
</div>
```
```css
.sahifa { display: grid; grid-template-columns: 220px 1fr;
          grid-template-rows: 70px 1fr 60px; gap: 12px; min-height: 100vh; }
header, footer { grid-column: 1 / -1; }
header { display: flex; justify-content: space-between; align-items: center; padding: 0 20px; }
```

---

## 4. Tezkor nazorat savollari (javoblari bilan)
1. **Savol:** Grid va Flexbox ning asosiy farqi?
   **Javob:** Flexbox — bir o'qli (qator yoki ustun), Grid — ikki o'qli (satr va ustun birga).
2. **Savol:** `grid-template-columns: 1fr 2fr 1fr;` qanday ustunlar beradi?
   **Javob:** 3 ustun, o'rtadagisi chetdagilardan 2 baravar keng (25% · 50% · 25% bo'sh joydan).
3. **Savol:** `repeat(4, 1fr)` nimaga teng?
   **Javob:** `1fr 1fr 1fr 1fr` — 4 ta teng ustun.
4. **Savol:** `grid-column: 1 / 3` element nechta ustunni egallaydi?
   **Javob:** 2 ta (1-chiziqdan 3-chiziqqacha).
5. **Savol:** `place-items: center` nima qiladi?
   **Javob:** har bir katak ichidagi elementni gorizontal (`justify-items`) va vertikal (`align-items`) markazga qo'yadi.
