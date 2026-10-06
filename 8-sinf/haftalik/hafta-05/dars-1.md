# 13-dars. Flexbox: elementlarni qatorga va ustunga joylash

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **II-bob**, 13-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilar Flexbox tizimini (`display: flex`) tushunadi: flex konteyner va flex element farqini, asosiy va ko'ndalang o'qni, `flex-direction`, `justify-content`, `align-items`, `align-self`, `flex-wrap`, `gap` hamda `flex-grow`/`flex-shrink`/`flex-basis` xususiyatlarini qo'llab, navigatsiya paneli va kartalar qatorini yasaydi.

**Kutiladigan natija:**
- Flex konteyner va flex elementni ajratadi, `display: flex` qayerga yozilishini biladi.
- Asosiy o'q (main axis) va ko'ndalang o'qni (cross axis) `flex-direction` ga bog'lab tushuntiradi.
- `justify-content` ning 5 qiymatini (`flex-start`, `center`, `flex-end`, `space-between`, `space-around`) ko'rsatadi.
- `align-items` va `align-self` bilan vertikal tekislaydi; elementni markazga «3 qatorda» qo'yadi.
- `flex-wrap: wrap` va `gap` bilan kartalar qatorini ko'chiradi; `flex: 1` nimani bildirishini aytadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 daq | Takrorlash | Box model, `box-sizing`, `margin: 0 auto` |
| 8–35 daq | Yangi mavzu | Konteyner va element, o'qlar, tekislash, wrap, grow/shrink/basis |
| 35–40 daq | Tanaffus | Ko'z mashqlari |
| 40–70 daq | Amaliyot | Navigatsiya paneli va 3 kartali qator |
| 70–76 daq | Tezkor nazorat | 5 ta savol |
| 76–80 daq | Xulosa | Uyga vazifa, keyingi dars: Grid |

> Manba: o'quv dasturi — 6-mavzu «Veb-sahifani tuzishda box model, flexbox va grid tizimlari» («Flexbox tizimi (display: flex, flex-direction, justify-content, align-items, align-self, flex-wrap, flex-grow/shrink/basis). Flex konteyner va Flex element farqi»), kutilgan natijalar: «Flexbox tizimi yordamida elementlarni gorizontal va vertikal joylashtirishni biladi», «Flexbox xususiyatlari (justify-content, align-items, flex-wrap) bilan ishlay oladi». Uslubiy ko'rsatmada mavzu faqat nomi bilan berilgan — konspekt va misollar CSS standarti asosida mentor tomonidan tuzildi.

---

## 2. Konspekt

### 2.1. Takrorlash (8 daqiqa)
- Box model qatlamlari? `box-sizing: border-box` nima beradi?
- Ikki kartani yonma-yon qo'yish uchun o'tgan darsda nima yetishmadi? (Bloklar ustma-ust tushadi — bugun Flexbox bilan hal qilamiz.)

### 2.2. Flex konteyner va flex element
- `display: flex` **ota elementga** (konteyner) yoziladi. Uning **bevosita bolalari** flex elementlarga aylanadi va qatorga tiziladi.
- Nevaralar flex element bo'lmaydi — ular uchun ichki blokka yana `display: flex` kerak.

```html
<div class="qator">        <!-- flex konteyner -->
  <div class="quti">1</div> <!-- flex element -->
  <div class="quti">2</div>
  <div class="quti">3</div>
</div>
```
```css
.qator { display: flex; }
```

### 2.3. O'qlar va `flex-direction`
| Qiymat | Asosiy o'q (main) | Ko'ndalang o'q (cross) |
|---|---|---|
| `row` (standart) | chapdan o'ngga → | yuqoridan pastga |
| `row-reverse` | o'ngdan chapga ← | yuqoridan pastga |
| `column` | yuqoridan pastga ↓ | chapdan o'ngga |
| `column-reverse` | pastdan yuqoriga ↑ | chapdan o'ngga |

Qoida: **`justify-content` — asosiy o'q bo'yicha, `align-items` — ko'ndalang o'q bo'yicha.** `column` da ular «joy almashadi».

### 2.4. `justify-content` — asosiy o'q bo'yicha taqsimlash
```css
justify-content: flex-start;     /* boshida (standart) */
justify-content: center;         /* o'rtada */
justify-content: flex-end;       /* oxirida */
justify-content: space-between;  /* chetlari devorga, oralar teng */
justify-content: space-around;   /* har elementning atrofida teng joy */
justify-content: space-evenly;   /* barcha bo'shliqlar teng */
```

### 2.5. `align-items` va `align-self` — ko'ndalang o'q
```css
.qator { height: 200px; align-items: center; }  /* hammasi vertikal o'rtada */
/* qiymatlar: stretch (standart), flex-start, center, flex-end, baseline */
.quti-maxsus { align-self: flex-end; }          /* faqat bitta element pastda */
```
Markazlashning «oltin uchligi»:
```css
.markaz { display: flex; justify-content: center; align-items: center; }
```

### 2.6. `flex-wrap` va `gap`
- Standart `nowrap`: elementlar sig'masa ham bitta qatorda siqiladi.
- `flex-wrap: wrap` — sig'magan element keyingi qatorga ko'chadi.
- `gap: 16px` — elementlar orasidagi masofa (margin hisoblashsiz).

### 2.7. `flex-grow`, `flex-shrink`, `flex-basis`
| Xususiyat | Ma'nosi | Standart |
|---|---|---|
| `flex-basis` | elementning boshlang'ich o'lchami | `auto` |
| `flex-grow` | bo'sh joydan qancha ulush oladi | `0` |
| `flex-shrink` | joy yetmasa qanchalik kichrayadi | `1` |

```css
.chap   { flex: 1; }   /* = flex-grow 1, shrink 1, basis 0 */
.asosiy { flex: 3; }   /* chapdan 3 baravar keng */
.logo   { flex-shrink: 0; } /* hech qachon siqilmaydi */
```
`flex: 1` va `flex: 3` → bo'sh joy 1:3 nisbatda bo'linadi (25% va 75%).

### 2.8. Odatiy xatolar
- `display: flex` ni elementlarning o'ziga yozish (konteynerga emas).
- `column` da `justify-content` ni gorizontal deb o'ylash.
- `align-items: center` ishlamaydi — konteynerning balandligi yo'q.
- `flex-wrap` siz kartalar telefonda siqilib ketadi.
- Elementlar orasiga `margin` bilan masofa berib, chetlarda ortiqcha joy qoldirish — `gap` qulayroq.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Uch quti qatorda
**Vazifa:** 3 ta rangli `.quti` ni Flexbox bilan bir qatorga qo'ying, orasida 20px masofa bo'lsin va ular sahifa markazida tursin.
**Kutiladigan natija:** 3 quti gorizontal o'rtada, oralari teng.
**Yechim:**
```css
.qator { display: flex; justify-content: center; gap: 20px; }
.quti  { width: 100px; height: 100px; background: tomato; }
```

### 2-topshiriq (o'rta). Navigatsiya paneli
**Vazifa:** chapda logotip, o'ngda 4 ta havola joylashgan `header` yasang; hammasi vertikal o'rtada bo'lsin.
**Kutiladigan natija:** logotip chap chetda, menyu o'ng chetda, balandlik 70px.
**Yechim:**
```html
<header class="nav">
  <a class="logo" href="#">AXV</a>
  <nav class="menyu">
    <a href="#">Bosh sahifa</a><a href="#">Kurslar</a>
    <a href="#">Loyihalar</a><a href="#">Aloqa</a>
  </nav>
</header>
```
```css
.nav   { display: flex; justify-content: space-between; align-items: center;
         height: 70px; padding: 0 24px; background: #1e293b; }
.menyu { display: flex; gap: 24px; }
.nav a { color: white; text-decoration: none; }
```
Izoh: `.menyu` ham flex konteyner — chunki havolalar `.nav` ning nevaralari.

### 3-topshiriq (qiyin). Ko'chadigan kartalar va sidebar
**Vazifa:** (a) 6 ta karta: har biri kamida 200px, sig'maganlari keyingi qatorga o'tsin, oralari 16px. (b) Sahifa: chapda sidebar (1 ulush), o'ngda kontent (3 ulush).
**Kutiladigan natija:** oyna torayganda kartalar ko'chadi; sidebar va kontent 1:3.
**Yechim:**
```css
.kartalar { display: flex; flex-wrap: wrap; gap: 16px; }
.karta    { flex: 1 1 200px; padding: 20px; border: 1px solid #cbd5e1; border-radius: 12px; }

.sahifa  { display: flex; gap: 20px; }
.sidebar { flex: 1; }
.kontent { flex: 3; }
```
`flex: 1 1 200px` — boshlang'ich 200px, bo'sh joy bo'lsa kengayadi, tor bo'lsa siqiladi va `wrap` tufayli ko'chadi.

---

## 4. Tezkor nazorat savollari (javoblari bilan)
1. **Savol:** `display: flex` qaysi elementga yoziladi?
   **Javob:** konteynerga (ota elementga); uning bevosita bolalari flex elementga aylanadi.
2. **Savol:** `flex-direction: column` bo'lsa, `justify-content: center` elementlarni qaysi yo'nalishda markazlaydi?
   **Javob:** vertikal — chunki asosiy o'q endi yuqoridan pastga.
3. **Savol:** `space-between` va `space-around` farqi?
   **Javob:** `space-between` da chetdagi elementlar devorga tegadi; `space-around` da har bir element atrofida teng bo'shliq, chetlarda ham joy qoladi.
4. **Savol:** Elementni ham gorizontal, ham vertikal markazga qanday qo'yamiz?
   **Javob:** konteynerga `display: flex; justify-content: center; align-items: center;` (va balandlik).
5. **Savol:** `flex: 1` va `flex: 2` li ikki element bo'sh joyni qanday bo'ladi?
   **Javob:** 1:2 nisbatda — ikkinchisi birinchisidan ikki baravar ko'p joy oladi.
