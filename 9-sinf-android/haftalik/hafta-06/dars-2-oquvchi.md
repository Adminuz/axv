# 17-dars. Kotlinda ma'lumot turlari, list va maplar (2-qism): lambda ifodalar va kolleksiyalarni filtrlash (filter, map, forEach)

> Ro'yxatdan faqat kerakli elementlarni tanlash va o'zgartirish — dasturchining kundalik ishi. Bugun lambda va `filter`, `map`, `forEach` yordamida sikl yozmasdan buni bir qatorda bajarishni o'rganamiz.

## Dars xulosasi

- Lambda — nomsiz funksiya: `{ x -> ... }`.
- Bitta parametr bo'lsa — `it`.
- `forEach` har elementga amal bajaradi.
- `filter` shartga mosini tanlaydi (yangi ro'yxat).
- `map` har elementni o'zgartiradi (yangi ro'yxat).
- Funksiyalarni zanjirlash: `filter { } .map { }`.

## Qo'shimcha ma'lumot

### `sortedBy`
Elementlarni mezon bo'yicha tartiblaydi.

### `firstOrNull`
Birinchi mosi yoki `null`.

### `filterNotNull`
`null` larni olib tashlaydi.

### `reduce`
Elementlarni bitta qiymatga yig'adi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Lambda | Nomsiz funksiya |
| it | Yagona parametr nomi |
| forEach | Har biri uchun amal |
| filter | Tanlash |
| map | O'zgartirish |
| Zanjir | Funksiyalarni ketma-ket chaqirish |
| Predicate | true/false qaytaruvchi shart |
| Unit | Qiymat qaytarmaslik turi |

## Bilasizmi?

- `it` faqat bitta parametr bo'lganda ishlaydi; ikkita parametr bo'lsa `{ a, b -> a + b }` yoziladi.
- `sequence` uzun zanjirlarni oraliq ro'yxatlarsiz bajaradi (katta ma'lumotlar uchun).
- Jetpack Compose'da `Button(onClick = { ... })` aynan lambda.

## Topshiriqlar

### 1. Lambda sintaksisi · oson

Lambda sintaksisini yozing.

**Kutiladigan natija:** `{ x -> tana }`.

### 2. it · oson

`it` qachon ishlatiladi?

**Kutiladigan natija:** Bitta parametrda.

### 3. forEach · oson

Ro'yxatni `forEach` bilan chiqaring.

**Kutiladigan natija:** `forEach { println(it) }`.

### 4. filter nima · oson

`filter` nima qaytaradi?

**Kutiladigan natija:** Yangi ro'yxat.

### 5. Juft sonlar · o'rta

Ro'yxatdan juft sonlarni oling.

**Kutiladigan natija:** `filter { it % 2 == 0 }`.

### 6. Kvadratlar · o'rta

Sonlar kvadratini oling.

**Kutiladigan natija:** `map { it * it }`.

### 7. Soni · o'rta

3 dan katta sonlar sonini toping.

**Kutiladigan natija:** `count { it > 3 }`.

### 8. Bor-yo'q · o'rta

5 dan katta son bormi?

**Kutiladigan natija:** `any { it > 5 }`.

### 9. Zanjir · qiyin

Filtrlab, 10 ga ko'paytiring.

**Kutiladigan natija:** `filter {..}.map {..}`.

### 10. Map filtri · qiyin

Narxi 500 dan yuqori mahsulotlarni toping.

**Kutiladigan natija:** `filter { it.value > 500 }`.

### 11. Nomlar · qiyin

Nomlarni katta harfga o'tkazing.

**Kutiladigan natija:** `map { it.uppercase() }`.

### 12. Mini hisobot · bonus

Mahsulotlardan qimmatlarini tanlab hisobot chiqaring.

**Kutiladigan natija:** Zanjir ishlaydi.

## O'zingizni tekshiring

1. Lambda nima?
2. `it` nima?
3. `filter` va `map` farqi?
4. `forEach` nima qiladi?
5. Zanjir qanday yoziladi?
6. Map ni qanday filtrlaymiz?

## Uyga vazifa

Mahsulotlarni filter va map bilan qayta ishlang (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
