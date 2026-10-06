# 17-dars. Flexbox layout tizimi va bir o'lchamli joylashuv

**Fan:** Advanced UX/UI dizayn va Advanced Front-end
**Sinf:** 10-sinf
**Hafta:** 6-hafta, 2-dars (umumiy 17-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (3.2 «Grid tizimlari va kompozitsiya»: Flexbox va CSS Grid grid tamoyillariga asoslanadi; moslashuvchan gridlar). Flexbox xossalari (`flex-direction`, `justify-content`, `align-items`, `gap`, `flex-wrap`, `flex`) rejadagi mavzu bo'yicha standart CSS hujjatlaridan (MDN) qo'shildi.

---

## Darsning maqsadi

`display: flex` bilan konteyner va elementlar tushunchasini, bosh va ko'ndalang o'qni, `flex-direction`, `justify-content`, `align-items`, `gap`, `flex-wrap` xossalarini, `flex` (grow, shrink, basis) qisqa yozuvini va navbar hamda kartalar qatorini yasashni o'rgatish.

## Kutiladigan natija

- `display: flex` ni konteynerga berib, elementlarni qatorga joylashtiradi;
- Bosh o'q (`flex-direction`) va ko'ndalang o'qni farqlaydi;
- `justify-content` va `align-items` bilan tekislaydi, `gap` bilan oraliq beradi;
- `flex-wrap` va `flex: 1` bilan kartalar qatorini moslashuvchan qiladi;
- Navbar ni `margin-left: auto` bilan yasaydi.

## Kerakli jihozlar

- Kompyuter, brauzer va VS Code
- DevTools da Flexbox belgisi (`flex` badge)
- Maktab saytining `style.css` fayli (16-dars)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 16-dars: selektorlar, kaskad, Box Model |
| 08–22 | Yangi mavzu 1 | Flex konteyner va elementlar, ikki o'q |
| 22–32 | Yangi mavzu 2 | `justify-content`, `align-items`, `gap`, `flex-wrap` |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | `flex: 1`, grow/shrink/basis; navbar va kartalar qatori |
| 50–75 | Amaliyot | Tipik xatolar va xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. display: flex va ikki o'q

Oddiy `div` lar ustma-ust turadi. Konteynerga **`display: flex`** bersangiz, uning bevosita bolalari (flex elementlari) **bir qatorga** tizadi. Flexbox **bir o'lchamli**: bir vaqtda faqat bitta yo'nalishda (qator yoki ustun) ishlaydi. **Bosh o'q** (main axis) — elementlar tizilgan yo'nalish: `flex-direction: row` (standart, chapdan o'ngga) yoki `column` (yuqoridan pastga). **Ko'ndalang o'q** (cross axis) — unga perpendikulyar. Tekislash xossalari shu o'qlarga bog'langan, shuning uchun `flex-direction: column` qilsangiz, `justify-content` va `align-items` rollari almashadi.

`display: flex` ni **ota** (konteyner) ga yozasiz, bolalarga emas. Faqat bevosita bolalar flex elementi bo'ladi.

### 2. justify-content, align-items, gap, flex-wrap

**`justify-content`** bosh o'q bo'ylab taqsimlaydi: `flex-start`, `center`, `flex-end`, `space-between` (chetga surib, oraliq teng), `space-around`, `space-evenly`. **`align-items`** ko'ndalang o'q bo'ylab tekislaydi: `stretch` (standart), `center`, `flex-start`, `flex-end`. **`gap`** elementlar orasida bo'sh joy beradi (margin kerak emas). Elementlar sig'masa, **`flex-wrap: wrap`** ularni keyingi qatorga o'tkazadi, aks holda ular siqiladi. Klassik masala: elementni to'liq markazlash: `display:flex; justify-content:center; align-items:center;`.

`align-items: center` vertikal markazlash uchun konteynerning balandligi bo'lishi kerak (`min-height` yoki `height`).

### 3. flex: grow, shrink, basis va navbar

Har bir flex elementiga ham xossa beriladi. **`flex-grow`** — bo'sh joyni qancha olishi, **`flex-shrink`** — joy yetmaganda siqilishi, **`flex-basis`** — boshlang'ich o'lchami. Qisqa yozuv `flex: grow shrink basis`. Eng ko'p ishlatiladigani **`flex: 1`** — barcha elementlar bo'sh joyni teng bo'lishadi. Navbar yasashda logotip chapda, havolalar o'ngda bo'lishi uchun havolalar blokiga **`margin-left: auto`** beriladi: avtomatik margin barcha bo'sh joyni oladi. Yana: `order` (tartibni o'zgartirish), `align-self` (bitta elementni alohida tekislash).

`flex: 1 1 200px` + `flex-wrap: wrap` — mobilda kartalar avtomatik pastga tushadi (kamida 200px kenglikda).

---

## Kod namunasi

HTML (3 ta quti)

```html
<div class="row">
  <div class="box">1</div>
  <div class="box">2</div>
  <div class="box">3</div>
</div>
```

Maktab sayti: navbar va kartalar qatori

```css
nav {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 24px;
  background: #1a3a6b;
}
nav a { color: #fff; text-decoration: none; }
nav .links { margin-left: auto; display: flex; gap: 16px; }

.cards { display: flex; flex-wrap: wrap; gap: 16px; padding: 24px; }
.card { flex: 1 1 220px; padding: 16px; border: 1px solid #ddd; border-radius: 8px; }
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Qatorga tizing
3 ta `.box` ni qatorga qo'yib, oralariga 16px bering.

**Kutiladigan natija:** Yonma-yon 3 quti.

**Yechim:** .row { display: flex; gap: 16px; }

### 2-topshiriq (oson). Markazlash
`.hero` ichidagi matnni gorizontal va vertikal markazlang.

**Kutiladigan natija:** Markazdagi matn.

**Yechim:** 
```css
.hero {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px;
}
```

### 3-topshiriq (o'rta). Navbar
Logo chapda, havolalar o'ngda turadigan navbar yozing.

**Kutiladigan natija:** Havolalar o'ngga suriladi.

**Yechim:** 
```css
nav { display: flex; align-items: center; }
nav .links { margin-left: auto; }
```

### 4-topshiriq (o'rta). Teng kartalar
3 ta karta bo'sh joyni teng bo'lishsin.

**Kutiladigan natija:** Teng kenglikdagi kartalar.

**Yechim:** .card { flex: 1; }

### 5-topshiriq (qiyin). Moslashuvchan qator
Kartalar kamida 220px bo'lsin va mobilda pastga tushsin.

**Kutiladigan natija:** Qatorlarga bo'linadi.

**Yechim:** 
```css
.cards { display: flex; flex-wrap: wrap; gap: 16px; }
.card { flex: 1 1 220px; }
```

### 6-topshiriq (qo'shimcha). Tartib
`order` bilan 3-elementni birinchi qiling.

**Kutiladigan natija:** 3-element birinchi turadi.

**Yechim:** .box:nth-child(3) { order: -1; }

---

## Tezkor nazorat (dars oxirida)

1. `display: flex` nimaga yoziladi? — Konteynerga (otaga).
2. Bosh o'q nima? — Elementlar tizilgan yo'nalish.
3. `justify-content` va `align-items` farqi? — Birinchisi bosh o'q, ikkinchisi ko'ndalang o'q bo'ylab.
4. `flex-wrap: wrap` nima qiladi? — Sig'masa, elementlarni keyingi qatorga o'tkazadi.
5. Navbar da havolalarni o'ngga qanday suramiz? — `margin-left: auto`.

## Keng tarqalgan xatolar

- `display: flex` ni bolalarga yozish.
- `align-items` ni balandliksiz konteynerda kutish.
- `flex-wrap` ni unutib, mobilda elementlar siqilib ketishi.
- Margin o'rniga `gap` ishlatmaslik.
- `flex-direction: column` da `justify` va `align` rollarini adashtirish.

## Bilasizmi? (qo'shimcha)

- DevTools da flex konteynerning yonida `flex` belgisi chiqadi; bosganda o'qlar ko'rinadi.
- `gap` avval faqat Grid da edi, hozir Flexbox da ham ishlaydi.
- Flexbox 1 o'lchamli, Grid esa 2 o'lchamli joylashuv uchun.
