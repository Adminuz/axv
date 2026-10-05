# 11-dars. Kotlin sintaksisi: val vs var va ma’lumot turlari

> Android ilovalar yozishning rasmiy tili &mdash; Kotlin bilan tanishishga tayyormisiz? Ushbu darsda o'zgaruvchilarni e'lon qilish, `val` va `var` farqi hamda String shablonlarini o'rganamiz.

## Dars xulosasi

- **Kotlin** &mdash; zamonaviy, xavfsiz va qisqa sintaksisga ega bo'lgan, Google tomonidan Android uchun 1-raqamli deb tan olingan dasturlash tili.
- **`val` (Value):** O'zgarmas (Read-only / Immutable) qiymat. Bir marta qiymat berilgach, uni o'zgartirib bo'lmaydi.
- **`var` (Variable):** O'zgaruvchan (Mutable) qiymat. Dastur davomida qiymatini xohlagancha o'zgartirish mumkin.
- **Asosiy turlar:**
  - `Int` &mdash; butun sonlar (`10, -5`);
  - `Double` / `Float` &mdash; kasr va o'nlik sonlar (`3.14`, `2.5f`);
  - `Boolean` &mdash; mantiqiy qiymat (`true`, `false`);
  - `Char` &mdash; bitta belgi (`'A'`);
  - `String` &mdash; matn (`"Android"`).
- **String Templates:** Matn ichiga o'zgaruvchini `$ism` yoki murakkab ifodani `${yosh + 1}` ko'rinishida to'g'ridan-to'g'ri joylash mumkin.

## Qo'shimcha ma'lumot

### Nega Kotlin'da `val` ko'proq ishlatiladi?
Dasturlashda ko'p uchraydigan xatolardan biri &mdash; o'zgaruvchi qiymatining tasodifan boshqa joyda o'zgarib ketishidir. `val` dan foydalanish kodni "xavfsiz" qiladi va kutilmagan xatoliklarning oldini oladi.

### Tipni ko'rsatish shartmi? (Type Inference)
Kotlinda quyidagi ikkala yozuv ham bir xil ishlaydi:
```kotlin
val yosh: Int = 16   // Tip aniq ko'rsatilgan
val yosh = 16        // Kotlin o'zi Int ekanini tushunadi
```

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Kotlin | Android dasturlash uchun Google tomonidan tan olingan asosiy til |
| val | O'zgarmas o'zgaruvchi (Value / Read-only) |
| var | O'zgaruvchan o'zgaruvchi (Variable / Mutable) |
| Type Inference | O'zgaruvchi turini avtomatik aniqlash mexanizmi |
| String Template | Matn ichida `$o'zgaruvchi` shablonlarini ishlatish usuli |
| Type Casting | Ma'lumot turini boshqa turga aylantirish (`toInt()`, `toString()`) |

## Bilasizmi?

- Kotlin tili Sankt-Peterburg yaqinidagi Kotlin oroli sharafiga nomlangan (Java tili ham Yava oroli sharafiga nomlangan).
- Google Play'dagi eng mashhur 1000 ta ilovaning 95% dan ortig'i aynan Kotlin tilida yozilgan!

## Topshiriqlar

### 1. val yoki var? · oson

Har biri uchun `val` yoki `var` tanlang: tug'ilgan yil, joriy ball, ism, telefon quvvati foizi, pi soni, savatdagi mahsulotlar soni.

**Kutiladigan natija:** 6 ta javob: o'zgarmaydiganlar `val`, o'zgaradiganlar `var`.

### 2. Ma'lumot turlari · oson

Har qiymatning Kotlin turini yozing: `15`, `12500.50`, `4.5f`, `true`, `'A'`, `"Android"`.

**Kutiladigan natija:** `Int`, `Double`, `Float`, `Boolean`, `Char`, `String`.

### 3. O'quvchi kartochkasi · oson

Ismingiz (`val`), yoshingiz (`var`), bo'yingiz (`val`, `Double`) va `val dasturchimi: Boolean` ni e'lon qilib, bitta `println` bilan chiqaring.

**Kutiladigan natija:** bitta qatorda barcha ma'lumotlar `$` shabloni orqali chiqadi.

### 4. Type inference · oson

Turini yozmasdan `val shahar = "Toshkent"`, `val yil = 2026`, `val narx = 9.99` e'lon qiling. Android Studio'da o'zgaruvchi ustiga sichqonchani olib borib turini ko'ring.

**Kutiladigan natija:** Kotlin turlarni o'zi aniqlagan: `String`, `Int`, `Double`.

### 5. Xatoni toping · o'rta

Bu kod nega ishlamaydi? Tuzating:

```kotlin
val ball = 70
ball = ball + 15
println("Yangi ball: $ball")
```

**Kutiladigan natija:** xato sababi (`Val cannot be reassigned`) va tuzatilgan kod `85` ni chiqaradi.

### 6. Natijani bashorat qiling · o'rta

Ishga tushirmasdan oldin natijani yozing, keyin tekshiring:

```kotlin
val a = 7
val b = 3
println("$a + $b = ${a + b}")
println("$a + $b")
```

**Kutiladigan natija:** ikki qator natija va nega ikkinchisida yig'indi hisoblanmagani tushuntirilgan.

### 7. Konvertatsiya · o'rta

`val s1 = "45"` va `val s2 = "12"` matnlarini `toInt()` bilan songa o'tkazing, yig'indi va ko'paytmani chiqaring. `s1 + s2` nima berishini ham tekshiring.

**Kutiladigan natija:** `57` va `540`; `s1 + s2` esa `"4512"` (matnlar ulanadi).

### 8. Telefon ma'lumotlari · o'rta

Smartfoningiz modeli (`String`), narxi (`Double`), xotirasi (`Int`), quvvat foizi (`var Int`) va kamerasi borligi (`Boolean`) uchun o'zgaruvchilar yarating. Quvvatni 15 ga kamaytirib, qayta chiqaring.

**Kutiladigan natija:** ikki marta chiqarilgan ma'lumot: quvvat foizi o'zgargan, qolganlari bir xil.

### 9. O'rtacha baho · qiyin

3 ta fandan baholarni `Int` da saqlang va o'rtachasini `${...}` ichida hisoblab chiqaring. Nega `(5 + 4 + 4) / 3` butun son beradi? Qanday qilib aniq o'nlik natija olasiz?

**Kutiladigan natija:** to'g'ri o'rtacha `4.33...`: `toDouble()` yoki `/ 3.0` ishlatilgan.

### 10. Xavfli konvertatsiya · qiyin

`"abc".toInt()` ni ishga tushiring. Qanday xato chiqadi? `toIntOrNull()` bilan sinab ko'ring va farqni yozing.

**Kutiladigan natija:** `NumberFormatException` va `toIntOrNull()` ning `null` qaytarishi tushuntirilgan.

### 11. QQS hisoblash · qiyin

`val narx = "150000"` ni songa o'tkazib, 12% QQS qo'shilgan yakuniy summani hisoblang va chiroyli qilib chiqaring.

**Kutiladigan natija:** `Jami: 168000.0 so'm` kabi natija.

### 12. Mini-profil · bonus

O'zingiz haqingizda 6 ta turdagi (`Int`, `Double`, `Float`, `Boolean`, `Char`, `String`) o'zgaruvchi yarating va ularni ramka ichida chiroyli profil qilib chiqaring.

**Kutiladigan natija:** bir nechta qatorli chiroyli profil, har turdan kamida bitta qiymat.

## O'zingizni tekshiring

1. Kotlin'ni kim yaratgan va Google uni qachon Android uchun tavsiya qilgan?
2. `val` va `var` farqi nima?
3. Nega ko'p hollarda `val` tavsiya etiladi?
4. Kotlin'dagi 6 ta asosiy turni sanang.
5. Type inference nima?
6. String shablonida `$ism` va `${a + b}` qachon ishlatiladi?
7. Matnni songa qanday aylantirasiz?

## Uyga vazifa

Smartfoningiz ma'lumotlari uchun `val`/`var` o'zgaruvchilar, 3 ta baho o'rtachasi va matnli narxga 12% QQS qo'shish dasturlarini yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
