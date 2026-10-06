# 16-dars. Kotlinda ma'lumot turlari, list va maplar (1-qism): kolleksiyalar — List, MutableList, Set va Map

> Ilovada ro'yxatlar hamma joyda: kontaktlar, mahsulotlar, xabarlar. Bugun Kotlin kolleksiyalari — List, Set va Map — bilan tanishamiz va «Omborxona» ro'yxatini yaratamiz.

## Dars xulosasi

- Kolleksiya — ko'p qiymatni saqlovchi tuzilma.
- `listOf` o'zgarmas, `mutableListOf` o'zgaruvchan.
- Indeks 0 dan; xavfsiz olish — `getOrNull`.
- Set — takrorlanmas to'plam.
- Map — kalit–qiymat; kalitlar noyob.
- Aylanish: `for (x in list)` va `for ((k, v) in map)`.

## Qo'shimcha ma'lumot

### `distinct()`
Ro'yxatdan takrorlarni olib tashlaydi.

### `mapOf` vs `mutableMapOf`
O'zgarmas va o'zgaruvchan Map.

### `Pair`
`a to b` — ikki qiymatli juftlik.

### `emptyList()`
Bo'sh o'zgarmas ro'yxat.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Kolleksiya | Ko'p qiymat saqlovchi tuzilma |
| List | Tartiblangan ro'yxat |
| Set | Takrorlanmas to'plam |
| Map | Kalit–qiymat lug'ati |
| Indeks | Element tartib raqami |
| Immutable | O'zgarmas |
| Mutable | O'zgaruvchan |
| Kalit | Map dagi noyob nom |

## Bilasizmi?

- Kotlinda `val list = mutableListOf()` ning ichini o'zgartirish mumkin: `val` faqat havolani qotiradi.
- `List<String?>` ichidagi `null` larni `filterNotNull()` olib tashlaydi.
- Jetpack Compose'da ekran yangilanishi uchun `mutableStateListOf` ishlatiladi (keyingi bo'limlarda).

## Topshiriqlar

### 1. List yaratish · oson

3 ta shahar nomidan ro'yxat yarating.

**Kutiladigan natija:** `listOf(...)` bilan ro'yxat.

### 2. Birinchi element · oson

Ro'yxatning birinchi elementini chiqaring.

**Kutiladigan natija:** `list[0]`.

### 3. Mutable · oson

`mutableListOf` ga element qo'shing.

**Kutiladigan natija:** `add(...)`.

### 4. Map yaratish · oson

Ism → yosh Map yarating.

**Kutiladigan natija:** `mapOf(... to ...)`.

### 5. Xavfsiz olish · o'rta

10-indeksni xatosiz oling.

**Kutiladigan natija:** `getOrNull(10)`.

### 6. Element o'chirish · o'rta

2-indeksdagi elementni o'chiring.

**Kutiladigan natija:** `removeAt(2)`.

### 7. Set farqi · o'rta

List va Set farqini yozing.

**Kutiladigan natija:** Set takrorlanmaydi.

### 8. Map yangilash · o'rta

Map dagi bir qiymatni yangilang.

**Kutiladigan natija:** `map[kalit] = yangi`.

### 9. Takrorlarni olish · qiyin

Ro'yxatdan takrorlarni olib tashlang.

**Kutiladigan natija:** `toSet()` yoki `distinct()`.

### 10. Map aylanish · qiyin

Map ni `for` bilan chiqaring.

**Kutiladigan natija:** `for ((k, v) in map)`.

### 11. Standart qiymat · qiyin

Kalit yo'q bo'lsa 0 qaytaring.

**Kutiladigan natija:** `getOrDefault(kalit, 0)`.

### 12. Inventarizatsiya · bonus

Ro'yxat va Map bilan mini ombor dasturini yozing.

**Kutiladigan natija:** Qo'shish, narx, hisobot ishlaydi.

## O'zingizni tekshiring

1. List va MutableList farqi?
2. Indeks nima?
3. `getOrNull` nima qiladi?
4. Set nima?
5. Map da kalit?
6. Map ni qanday aylanamiz?

## Uyga vazifa

«Omborxona» dasturini yozing: List, Map va hisobot (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
