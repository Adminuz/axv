# 14-dars. CSS Grid: satr va ustunlardan iborat to'r

> Shaxmat taxtasi, Excel jadvali, telefoningizdagi ilovalar ekrani — hammasi to'r. Bugun CSS Grid bilan sahifani xuddi shunday to'rga bo'lib, butun maketni bir necha qatorda quramiz.

## Dars xulosasi

- `display: grid` — **ikki o'lchamli** maket: satrlar va ustunlar birga.
- `grid-template-columns` / `grid-template-rows` — ustun va satrlar o'lchami.
- **`fr`** — bo'sh joy ulushi; `repeat(3, 1fr)` — 3 ta teng ustun.
- `gap` (eski nomi `grid-gap`) — kataklar orasidagi masofa.
- `grid-column: 1 / 3` yoki `span 2` — elementni bir nechta ustunga cho'zish; `1 / -1` — butun kenglik.
- `justify-items`, `align-items`, `place-items` — katak ichida tekislash.
- **Grid** — sahifa maketi, galereya; **Flexbox** — menyu, bir qator elementlar. Ko'pincha birga.

## Qo'shimcha ma'lumot

### 1. Chiziqlar — raqamli «panjara»
3 ustunli to'rda 4 ta vertikal chiziq bor: 1, 2, 3, 4. `grid-column: 1 / 3` — «1-chiziqdan 3-chiziqqacha», ya'ni **2 ta** ustun. `-1` — har doim oxirgi chiziq.

```
| 1-ustun | 2-ustun | 3-ustun |
1         2         3         4   ← chiziqlar
```

### 2. `fr` — pitsani bo'lish
`grid-template-columns: 1fr 2fr 1fr` — pitsani 4 bo'lakka bo'lib, o'rtadagi ustunga 2 bo'lak, chetdagilarga 1 tadan berish. `gap` avval ajratiladi, qolgan joy bo'linadi — shuning uchun `fr` hech qachon toshib ketmaydi.

### 3. Butun sahifa 5 qatorda
```css
.sahifa {
  display: grid;
  grid-template-columns: 220px 1fr;
  grid-template-rows: 70px 1fr 60px;
  gap: 12px;
}
header, footer { grid-column: 1 / -1; }
```

### 4. Grid yoki Flex?

| Vaziyat | Tanlov |
|---|---|
| Menyu havolalari bir qatorda | Flexbox |
| 3 × 3 rasm galereyasi | Grid |
| Header, sidebar, main, footer | Grid |
| Karta ichida rasm va matn yonma-yon | Flexbox |

### 5. Odatiy xatolar
- `grid-template-column` — oxiridagi **s** unutilgan.
- `grid-column: 1 / 3` ni 3 ustun deb o'ylash.
- Ustunlarni `%` bilan berib, `gap` tufayli toshib ketish — `fr` ishlating.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| CSS Grid | Ikki o'lchamli maket tizimi |
| Grid konteyner | `display: grid` yozilgan element |
| Katak (cell) | Satr va ustun kesishgan joy |
| Chiziq (line) | Ustun/satrlar orasidagi raqamlangan chegara |
| fr | Bo'sh joy ulushi (fraction) |
| repeat() | Bir xil o'lchamni takrorlash funksiyasi |
| gap | Kataklar orasidagi masofa |
| grid-column / grid-row | Element egallaydigan ustun/satrlar |
| span | «Shuncha katakka cho'z» |
| place-items | `align-items` + `justify-items` qisqa yozuvi |

## Bilasizmi?

- CSS Grid barcha asosiy brauzerlarda 2017-yilda deyarli bir vaqtda ishlay boshladi — bu CSS tarixida kamdan-kam uchraydigan holat.
- Grid g'oyasi gazeta va jurnal sahifalarini ustunlarga bo'lish an'anasidan olingan.
- F12 asboblarida grid konteyner yonidagi **grid** belgisini bossangiz, chiziq raqamlari to'g'ridan-to'g'ri sahifada ko'rinadi.
- «Grid Garden» — sabzilarni sug'orish orqali Grid xususiyatlarini o'rgatadigan bepul o'yin.

## Topshiriqlar

### 1. Birinchi to'r · oson
6 ta rangli `div` ni `display: grid` va 3 ta 150px ustun bilan joylang.
**Kutiladigan natija:** 3 × 2 to'r.

### 2. Oraliq · oson
To'rga `gap: 16px` qo'shing.
**Kutiladigan natija:** kataklar orasi ochilgan.

### 3. fr birligi · oson
Ustunlarni `repeat(3, 1fr)` ga almashtiring va oynani kengaytiring-toraytiring.
**Kutiladigan natija:** ustunlar oynaga qarab cho'ziladi.

### 4. Turli kenglik · oson
`1fr 2fr 1fr` yozing va o'rtadagi ustunni o'lchang (F12).
**Kutiladigan natija:** o'rtadagi ustun chetdagidan 2 baravar keng.

### 5. Cho'zilgan katak · o'rta
1-elementni `grid-column: span 2` bilan 2 ustunga cho'zing.
**Kutiladigan natija:** birinchi element keng.

### 6. Chiziqlar · o'rta
Elementni `grid-column: 2 / 4` va `grid-row: 1 / 3` ga joylang. U qayerga tushdi?
**Kutiladigan natija:** o'ng yuqorida 2 × 2 katak.

### 7. Markazdagi belgilar · o'rta
9 ta katakli to'rda har bir raqamni `place-items: center` bilan markazga qo'ying.
**Kutiladigan natija:** raqamlar kataklar o'rtasida.

### 8. Galereya · o'rta
6 ta rasmli galereya: `repeat(3, 1fr)`, `object-fit: cover`, `border-radius`.
**Kutiladigan natija:** bir xil o'lchamli rasmlar to'ri.

### 9. Sahifa maketi · qiyin
Header, sidebar, main, footer maketini Grid bilan quring (header va footer butun kenglikda).
**Kutiladigan natija:** 4 qismli sahifa.

### 10. Grid + Flex · qiyin
9-topshiriqdagi header ichiga logotip va menyuni Flexbox bilan joylang.
**Kutiladigan natija:** menyu o'ng chetda, vertikal o'rtada.

### 11. Xatoni toping · qiyin
```css
.tor { display: grid; grid-template-column: 1fr 1fr; }
```
Nega elementlar ustma-ust turibdi? Tuzating.
**Kutiladigan natija:** `grid-template-columns` (s bilan).

### 12. Grid Garden · bonus
«Grid Garden» o'yinida kamida 15 ta bosqichni o'ting.
**Kutiladigan natija:** oxirgi bosqich skrinshoti.

## O'zingizni tekshiring

1. Grid Flexbox dan nimasi bilan farq qiladi?
2. `fr` birligi nima?
3. `repeat(4, 1fr)` nimaga teng?
4. `grid-column: 1 / 3` nechta ustun?
5. `grid-column: 1 / -1` nima beradi?
6. `place-items: center` qaysi ikki xususiyatning qisqa yozuvi?
7. Menyu uchun Grid yoki Flex — qaysi biri qulay va nega?

## Uyga vazifa

Grid bilan «header–sidebar–main–footer» maketi va 6 ta rasmli galereya yasang. 20–30 daqiqa. Batafsil — haftalik uyga vazifada.
