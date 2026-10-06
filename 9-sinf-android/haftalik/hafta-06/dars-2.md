# 17-dars. Kotlinda ma'lumot turlari, list va maplar (2-qism): lambda ifodalar va kolleksiyalarni filtrlash (filter, map, forEach)

**Fan:** Android dasturlash
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 2-dars (umumiy 17-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `uslubiy-korsatma.txt` (Kolleksiyalarni saralash va filtrdan o'tkazish: `filter`, `map`, `sortedBy`; `filterNotNull`, `firstOrNull`; «Inventarizatsiya tizimi»); `oquv-qollanma.txt` (`getOrElse` dagi lambda). Lambda sintaksisi va `forEach` standart Kotlin hujjatiga ko'ra qo'shildi. Kod namunalari Kotlin Playground'da tekshirilishi kerak.

---

## Darsning maqsadi

O'quvchilarga lambda ifoda (nomsiz funksiya) sintaksisini, bitta parametr uchun `it` ni, kolleksiyalar uchun `forEach`, `filter`, `map` funksiyalarini, ularni zanjirlab ishlatishni va Map ni filtrlashni o'rgatish.

## Kutilayotgan natijalar

- Lambda ifodasini `{ x -> x * 2 }` ko'rinishida yozadi va o'zgaruvchiga saqlaydi;
- Bitta parametrli lambdada `it` ni ishlatadi;
- `forEach` bilan elementlar ustida amal bajaradi;
- `filter` bilan shartga mos elementlarni tanlaydi;
- `map` bilan har elementni o'zgartiradi va `filter` + `map` ni zanjirlaydi.

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 16-dars: List, Set, Map |
| 08–25 | Yangi mavzu 1 | Lambda ifoda: sintaksis va `it` |
| 25–38 | Yangi mavzu 2 | forEach va filter |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | map va zanjir; Map ni filtrlash |
| 58–75 | Amaliyot | Amaliyot: mahsulotlarni filtrlash, xulosa |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. Lambda ifoda va `it`

**Lambda** — nomsiz funksiya: uni o'zgaruvchiga saqlash yoki boshqa funksiyaga parametr sifatida berish mumkin. Sintaksis: `{ parametr -> tana }`. Masalan, `val kvadrat = { x: Int -> x * x }` — chaqirish `kvadrat(5)` natijasi 25. Oxirgi ifoda lambdaning natijasi bo'ladi. Agar lambdada **bitta parametr** bo'lsa, uni nomlamasdan **`it`** deb ishlatish mumkin: `{ it * 2 }`. Funksiyaning oxirgi parametri lambda bo'lsa, uni qavsdan tashqariga chiqarish mumkin: `list.filter { it > 3 }`. Siz buni oldin ham ko'rgansiz: `getOrElse(7) { "Invalid index $it" }` dagi `{ ... }` — lambda. Android'da lambda tugma bosilganda nima bo'lishini belgilaydi (`onClick = { ... }`).

```kotlin
val kvadrat = { x: Int -> x * x }
println(kvadrat(5))               // 25

val ikkilash: (Int) -> Int = { it * 2 }
println(ikkilash(7))              // 14

val salom = { ism: String -> "Salom, $ism!" }
println(salom("Ali"))             // Salom, Ali!
```

`(Int) -> Int` — funksiya turi: «Int oladi, Int qaytaradi». Lambdaning turi kompilyatorga ma'lum bo'lsa, `it` ni ishlatsangiz kod qisqa bo'ladi.

### 2. forEach va filter

**`forEach`** har bir elementga lambdani qo'llaydi (sikl o'rniga): `sonlar.forEach { println(it) }`. U hech narsa qaytarmaydi, faqat amal bajaradi. **`filter`** — shartga mos elementlardan **yangi ro'yxat** qaytaradi: `sonlar.filter { it % 2 == 0 }` — faqat juft sonlar. Asl ro'yxat o'zgarmaydi. Shart `true`/`false` qaytaradigan lambda bo'ladi. Qo'shimcha foydali funksiyalar: `count { ... }` (nechtasi mos), `any { ... }` (kamida bittasi mos), `firstOrNull { ... }` (birinchi mosi yoki `null`), `sortedBy { ... }` (tartiblash). Map uchun ham ishlaydi: `narxlar.filter { it.value > 500 }` — narxi 500 dan yuqori juftliklar.

```kotlin
val sonlar = listOf(1, 2, 3, 4, 5, 6)
sonlar.forEach { println(it) }
val juft = sonlar.filter { it % 2 == 0 }
println(juft)                          // [2, 4, 6]
println(sonlar.count { it > 3 })       // 3
println(sonlar.any { it > 5 })         // true

val narxlar = mapOf("Laptop" to 1200.0, "Phone" to 800.0, "Watch" to 250.0)
println(narxlar.filter { it.value > 500 })   // {Laptop=1200.0, Phone=800.0}
```

`filter` yangi ro'yxat qaytaradi, asl ro'yxatni o'zgartirmaydi. Natijani o'zgaruvchiga saqlashni unutmang.

### 3. map va funksiyalar zanjiri

**`map`** har elementni o'zgartirib, **yangi ro'yxat** qaytaradi: `nomlar.map { it.uppercase() }` — hamma nom katta harflarda; `sonlar.map { it * it }` — kvadratlar. Ro'yxat uzunligi o'zgarmaydi. Funksiyalarni **zanjirlash** mumkin: `sonlar.filter { it > 2 }.map { it * 10 }` — avval tanlaydi, keyin o'zgartiradi. Ko'p ishlatiladigan kombinatsiya: `filter` + `map` + `sum()` yoki `forEach`. Yana: ro'yxatda `null` bo'lsa, `filterNotNull()` ularni olib tashlaydi. Zanjirni o'qish tartibi chapdan o'ngga: «tanla → o'zgartir → hisobla». Juda uzun zanjirni bir necha qatorga bo'ling.

```kotlin
val nomlar = listOf("ali", "vali", "gulnora")
println(nomlar.map { it.uppercase() })   // [ALI, VALI, GULNORA]

val sonlar = listOf(1, 2, 3, 4, 5, 6)
println(sonlar.map { it * it })          // [1, 4, 9, 16, 25, 36]

val jami = sonlar.filter { it > 2 }.map { it * 10 }.sum()
println(jami)                            // 180
```

`map` natijasi — yangi ro'yxat: uni o'zgaruvchiga saqlang yoki `println` ga bering. Asl ro'yxat o'zgarmaydi.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Lambda yozing

Sonni 3 ga ko'paytiradigan lambda yozing va 4 ni bering.

**Yechim:**
```kotlin
val uch = { x: Int -> x * 3 }
println(uch(4))   // 12
```

### 2-topshiriq (oson). forEach

Ism ro'yxatini `forEach` bilan chiqaring.

**Yechim:**
```kotlin
val names = listOf("Ali", "Vali")
names.forEach { println(it) }
```

### 3-topshiriq (o'rta). Juft sonlar

`1..10` dan juft sonlarni `filter` bilan oling.

**Yechim:**
```kotlin
val juft = (1..10).filter { it % 2 == 0 }
println(juft)   // [2, 4, 6, 8, 10]
```

### 4-topshiriq (o'rta). Kvadratlar

`listOf(1, 2, 3, 4)` kvadratlari ro'yxatini `map` bilan oling.

**Yechim:**
```kotlin
println(listOf(1, 2, 3, 4).map { it * it })   // [1, 4, 9, 16]
```

### 5-topshiriq (qiyin). Qimmat mahsulotlar

Narxi 500 dan yuqori mahsulotlar nomlarini katta harflarda chiqaring.

**Yechim:**
```kotlin
val narxlar = mapOf("Laptop" to 1200.0, "Phone" to 800.0, "Watch" to 250.0)
narxlar.filter { it.value > 500 }
    .map { it.key.uppercase() }
    .forEach { println(it) }
```

### 6-topshiriq (bonus). Zanjir yig'indisi

3 dan katta sonlarni 10 ga ko'paytirib, yig'indisini hisoblang.

**Yechim:**
```kotlin
val jami = listOf(1, 2, 3, 4, 5, 6)
    .filter { it > 3 }
    .map { it * 10 }
    .sum()
println(jami)   // 150
```

---

## Tezkor nazorat

1. Lambda nima? **Javob:** Nomsiz funksiya.
2. `it` nima? **Javob:** Bitta parametrli lambdaning standart nomi.
3. `filter` nima qiladi? **Javob:** Shartga mos elementlarni tanlaydi.
4. `map` nima qiladi? **Javob:** Har elementni o'zgartiradi.
5. `forEach` nima qaytaradi? **Javob:** Hech narsa (Unit).

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
