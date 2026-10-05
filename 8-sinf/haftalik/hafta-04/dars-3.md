# 12-dars. CSS Box model: content, padding, border, margin

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **II-bob**, 12-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilar har bir HTML elementi «quti» (box) ekanini, quti to'rt qismdan (content, padding, border, margin) iborat ekanini tushunadi, element o'lchamlarini (`width`, `height`) boshqaradi va `box-sizing` xususiyatining ahamiyatini biladi.

**Kutiladigan natija:**
- Box model ning 4 qismini tartib bilan sanaydi va rasmda ko'rsatadi.
- `padding` (ichki masofa) va `margin` (tashqi masofa) farqini ajratadi.
- `border` ni yozadi (qalinlik, tur, rang).
- `margin`/`padding` qisqa yozuvini (1, 2, 4 qiymat) o'qiy oladi.
- `box-sizing: border-box` nima uchun kerakligini tushuntiradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 daq | Takrorlash | Rang, shrift, meros |
| 8–35 daq | Yangi mavzu | Quti modeli, 4 qism, o'lcham, box-sizing |
| 35–40 daq | Tanaffus | Ko'z mashqlari |
| 40–70 daq | Amaliyot | Karta (card) maketini yasash |
| 70–76 daq | Tezkor nazorat | 5 ta savol |
| 76–80 daq | Xulosa | Uyga vazifa, keyingi dars: Flexbox |

---

## 2. Konspekt

### 2.1. Takrorlash (8 daqiqa)
- `color` va `background-color` nima qiladi? `rgba` dagi `a` nima?
- Qaysi xususiyatlar meros bo'lib o'tadi, qaysilari yo'q? (Eslatma: `border` va `background-color` o'tmaydi.)

### 2.2. Box model nima?
Brauzer uchun har bir element — to'rtburchak **quti** (box). Ichkaridan tashqariga qarab to'rt qatlam:
1. **Content** — mazmun (matn, rasm);
2. **Padding** — mazmun va chegara orasidagi ichki masofa;
3. **Border** — chegara chizig'i;
4. **Margin** — chegaradan tashqaridagi masofa (boshqa elementlargacha).

O'xshatish: sovg'a qutisi. Sovg'a — content, qutidagi yumshoq qog'oz — padding, quti devori — border, javondagi qo'shni qutilargacha bo'sh joy — margin.

```css
.karta {
  width: 300px;
  padding: 20px;
  border: 2px solid navy;
  margin: 15px;
}
```

### 2.3. Padding va margin
- `padding` — fon rangi padding ni ham qoplaydi; `margin` esa shaffof (fon yo'q).
- Qisqa yozuv:
```css
padding: 10px;                /* to'rt tomon */
padding: 10px 20px;           /* tepa-past | chap-o'ng */
padding: 10px 20px 5px 0;     /* tepa, o'ng, past, chap (soat mili bo'yicha) */
margin-top: 30px;             /* alohida tomon */
margin: 0 auto;               /* gorizontal markazlash (width berilganda) */
```

### 2.4. Border
```css
border: 3px solid crimson;      /* qalinlik, tur, rang */
border-radius: 12px;            /* yumaloq burchaklar */
border-bottom: 1px dashed gray; /* faqat bitta tomon */
```
Turlari: `solid`, `dashed`, `dotted`, `double`, `none`.

### 2.5. Element o'lchamlari va box-sizing
`width` va `height` odatda faqat **content** o'lchamini beradi. Padding va border qo'shilsa, quti kattalashadi:

`width: 300px` + `padding: 20px` + `border: 2px` = jami 300 + 40 + 4 = **344px** (ikki tomonda).

Buni oldini olish uchun:
```css
* {
  box-sizing: border-box;
}
```
`border-box` da `width` padding va border ni ham o'z ichiga oladi: quti aniq 300px bo'ladi. Shuning uchun deyarli har bir loyihada `box-sizing: border-box` yoziladi.

### 2.6. Odatiy xatolar
- `margin` va `padding` ni almashtirish.
- Box-sizing ni yozmaslik: quti o'lchami kutilganidan katta chiqadi.
- `margin: 0 auto` ni `width` bermasdan yozish: markazlanmaydi.
- Chegara qiymatlaridan birini (`solid`) tushirib qoldirish: chegara chizilmaydi.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Quti qismlari
**Vazifa:** `div` ga `padding`, `border`, `margin` bering va F12 (DevTools) da Box model rasmini ko'ring.
**Kutiladigan natija:** to'rt rangli qatlam ko'rinadi.
**Yechim:**
```css
div {
  width: 200px;
  padding: 20px;
  border: 3px solid navy;
  margin: 30px;
  background-color: lightyellow;
}
```

### 2-topshiriq (o'rta). Karta maketi
**Vazifa:** `.karta` yarating: kengligi 300px, ichki masofa 20px, yumaloq burchak, chegara, ikki karta orasida 15px masofa.
**Kutiladigan natija:** ikki tartibli karta, orasida masofa bor.
**Yechim:**
```css
* { box-sizing: border-box; }
.karta {
  width: 300px;
  padding: 20px;
  border: 2px solid royalblue;
  border-radius: 12px;
  margin: 15px;
  background-color: white;
}
```
```html
<div class="karta"><h3>Birinchi</h3><p>Matn</p></div>
<div class="karta"><h3>Ikkinchi</h3><p>Matn</p></div>
```

### 3-topshiriq (qiyin). Jami o'lcham
**Vazifa:** `width: 200px; padding: 10px; border: 5px solid; margin: 20px;` bo'lsa (content-box), quti jami nechi piksel joy egallaydi va ko'rinadigan kengligi qancha? `border-box` da-chi?
**Kutiladigan natija:** hisoblash.
**Yechim:**
- content-box: ko'rinadigan kenglik 200 + 2·10 + 2·5 = **230px**; margin bilan 230 + 2·20 = **270px**.
- border-box: ko'rinadigan kenglik **200px**; margin bilan 200 + 40 = **240px**.

---

## 4. Tezkor nazorat savollari (javoblari bilan)
1. **Savol:** Box model qismlarini ichkaridan tashqariga ayting.
   **Javob:** content, padding, border, margin.
2. **Savol:** `padding` va `margin` farqi nima?
   **Javob:** padding — chegara ichidagi masofa (fon bilan qoplanadi); margin — chegaradan tashqaridagi masofa.
3. **Savol:** `padding: 10px 20px;` nimani anglatadi?
   **Javob:** tepa va past 10px, chap va o'ng 20px.
4. **Savol:** `box-sizing: border-box` nima beradi?
   **Javob:** `width` padding va border ni ham o'z ichiga oladi, quti belgilangan o'lchamda qoladi.
5. **Savol:** `margin: 0 auto;` nima uchun ishlatiladi?
   **Javob:** o'lchami berilgan blokni gorizontal markazlash uchun.
