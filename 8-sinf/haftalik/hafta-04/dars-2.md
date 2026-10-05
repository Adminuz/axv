# 11-dars. CSS: rang va shrift bilan ishlash, meros olish

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **II-bob**, 11-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilar CSS da rang berish usullarini (nom, hex, rgb/rgba, hsl, gradient), shrift xususiyatlarini (`font-family`, `font-size`, `font-weight`, `font-style`, `text-decoration`, `line-height`, `letter-spacing`, `text-align`) o'rganadi va inheritance (meros olish) qoidasini tushunadi.

**Kutiladigan natija:**
- `color` va `background-color` xususiyatlarini farqlaydi.
- Rangni nom, hex, rgb, rgba va hsl shaklida yoza oladi.
- `linear-gradient` bilan oddiy gradient fon yasay oladi.
- Shrift va matn xususiyatlarini birgalikda qo'llab, o'qish uchun qulay matn yarata oladi.
- Meros olish nima ekanini va qaysi xususiyatlar bola elementlarga o'tishini tushunadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 daq | Takrorlash | Selektorlar, ulash usullari, ustuvorlik |
| 8–35 daq | Yangi mavzu | Ranglar, gradient, shrift va matn xususiyatlari, meros |
| 35–40 daq | Tanaffus | Ko'z mashqlari |
| 40–70 daq | Amaliyot | «Shaxsiy vizitka» sahifasini bezash |
| 70–76 daq | Tezkor nazorat | 5 ta savol |
| 76–80 daq | Xulosa | Uyga vazifa, keyingi dars: Box model |

---

## 2. Konspekt

### 2.1. Takrorlash (8 daqiqa)
- `.karta` va `#logo` farqi nima? `nav a` nimani tanlaydi?
- `p { color: red; }` va `.x { color: green; }` to'qnashsa kim yutadi?
- Mini-mashq: doskada `<link>` bilan CSS ulanishini yozdiring.

### 2.2. Rang bilan ishlash
Ikkita asosiy xususiyat: **`color`** (matn rangi) va **`background-color`** (fon rangi).
```css
h1 {
  color: white;
  background-color: darkblue;
}
```
Rang berish usullari:
| Usul | Misol | Izoh |
|---|---|---|
| Nom bilan | `red`, `navy`, `tomato` | tayyor ranglar nomi |
| Hex | `#ff0000`, `#0a84ff` | `#` + 6 ta belgi (qizil, yashil, ko'k) |
| rgb | `rgb(255, 0, 0)` | har kanal 0 dan 255 gacha |
| rgba | `rgba(0, 0, 0, 0.5)` | oxirgi son: shaffoflik (0 dan 1 gacha) |
| hsl | `hsl(210, 80%, 50%)` | rang burchagi, to'yinganlik, yorqinlik |

```css
p { color: #0a84ff; }
.fon { background-color: rgba(0, 0, 0, 0.5); }
.rang { color: hsl(210, 80%, 50%); }
```

**Gradient** — ikki va undan ortiq rang orasidagi silliq o'tish:
```css
.banner {
  background: linear-gradient(to right, royalblue, orange);
}
```

### 2.3. Shrift (font) bilan ishlash
| Xususiyat | Vazifasi | Misol |
|---|---|---|
| `font-family` | shrift turi | `font-family: Arial, sans-serif;` |
| `font-size` | o'lcham | `font-size: 18px;` |
| `font-weight` | qalinlik | `font-weight: bold;` yoki `700` |
| `font-style` | qiyshiqlik | `font-style: italic;` |
| `text-decoration` | chiziq | `none`, `underline`, `line-through` |
| `text-align` | tekislash | `left`, `center`, `right` |
| `line-height` | qator balandligi | `line-height: 1.6;` |
| `letter-spacing` | harflar oralig'i | `letter-spacing: 2px;` |

`font-family` da bir nechta shrift vergul bilan beriladi: birinchisi topilmasa, keyingisi olinadi (zaxira ro'yxat). Oxirgisi odatda umumiy turdagi (`sans-serif`, `serif`).
```css
body {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 18px;
  line-height: 1.6;
}
h1 {
  font-weight: bold;
  letter-spacing: 2px;
  text-align: center;
}
a { text-decoration: none; }
```

### 2.4. Meros olish (inheritance)
Ba'zi xususiyatlar ota-elementdan bola elementlarga **o'tadi** (masalan `color`, `font-family`, `font-size`, `line-height`, `text-align`). Shu sababli `body` ga bir marta shrift berish butun sahifaga yetadi.
```css
body { color: #333; font-family: Arial, sans-serif; }
```
Bola elementga o'zining qoidasi berilsa, u merosdan kuchli bo'ladi. Fon, chegara va masofa kabi xususiyatlar esa meros bo'lib o'tmaydi.

### 2.5. Odatiy xatolar
- `color: #ff00` kabi hex ni to'liq yozmaslik (3 yoki 6 ta belgi kerak).
- `font-family` da bo'sh joyli nomni qo'shtirnoqsiz yozish: `"Times New Roman"`.
- Matn va fon bir xil rangda bo'lib qolishi (matn ko'rinmaydi).
- `line-height` ni birliksiz va birlik bilan aralashtirish: `1.6` (qatorga nisbatan) ko'p qulay.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq (oson). Matn va fon rangi
**Vazifa:** `h1` ga oq matn va to'q ko'k fon, `p` ga hex rang bering.
**Kutiladigan natija:** sarlavha to'q ko'k fonda oq matn bilan, abzats ko'k hex rangda.
**Yechim:**
```css
h1 {
  color: white;
  background-color: darkblue;
}
p { color: #0a84ff; }
```

### 2-topshiriq (o'rta). Shaxsiy vizitka
**Vazifa:** `body` ga shrift va qator balandligi, `h1` ni markazga, harflar orasini kengaytirib, `a` dan tagchiziqni olib tashlang. Fon uchun `linear-gradient` ishlating.
**Kutiladigan natija:** gradient fonli, o'qish uchun qulay vizitka.
**Yechim:**
```css
body {
  font-family: Arial, sans-serif;
  font-size: 18px;
  line-height: 1.6;
  background: linear-gradient(to right, lightblue, lavender);
}
h1 {
  text-align: center;
  letter-spacing: 2px;
}
a { text-decoration: none; color: crimson; }
```

### 3-topshiriq (qiyin). Meros nazorati
**Vazifa:** `body` ga `color: #333`, ichidagi bitta `<p>` ga `color: crimson` bering. Qaysi matn qaysi rangda bo'lishini oldindan ayting. `body` ga `background-color: yellow` bersangiz, `p` fonlari nima bo'ladi?
**Kutiladigan natija:** `p` qizil, qolgani `#333`. Fon meros bo'lmaydi, lekin `p` shaffof bo'lgani uchun orqadagi sariq ko'rinadi.
**Yechim:**
```css
body { color: #333; background-color: yellow; }
p.alohida { color: crimson; }
```
Bola elementning o'z qoidasi merosdan kuchli. `background-color` meros bo'lib o'tmaydi: u `transparent` (shaffof) turadi, shuning uchun ota fon ko'rinadi.

---

## 4. Tezkor nazorat savollari (javoblari bilan)
1. **Savol:** Matn rangi va fon rangi uchun qaysi xususiyatlar ishlatiladi?
   **Javob:** `color` va `background-color`.
2. **Savol:** `rgba(0, 0, 0, 0.5)` dagi oxirgi son nimani bildiradi?
   **Javob:** shaffoflikni (0 dan 1 gacha), bu yerda 50%.
3. **Savol:** `font-family` da bir nechta shrift nega yoziladi?
   **Javob:** birinchisi topilmasa, keyingisi ishlatiladi (zaxira ro'yxat).
4. **Savol:** `a { text-decoration: none; }` nima qiladi?
   **Javob:** havola tagidagi chiziqni olib tashlaydi.
5. **Savol:** Meros olish nima? Misol keltiring.
   **Javob:** ota-elementdagi ba'zi xususiyatlar (masalan `color`, `font-family`) bola elementlarga o'tadi.
