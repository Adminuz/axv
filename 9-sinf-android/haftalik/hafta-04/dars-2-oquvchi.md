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

1. **O'zgarmas o'zgaruvchi · oson**  
   `val mamlakat = "O'zbekiston"` o'zgaruvchisini e'lon qiling va uni `println()` bilan chiqaring.

2. **O'zgaruvchan ball · oson**  
   `var ball = 50` deb e'lon qiling, keyingi qatorda unga 30 ball qo'shing va yangi qiymatni chiqaring.

3. **String shabloni · oson**  
   `ism` va `familiya` o'zgaruvchilarini yarating va `$ism $familiya` shabloni orqali to'liq ismni ekranga chiqaring.

4. **Yosh hisobi · oson**  
   Tug'ilgan yilingizni `val tugilganYil = 2010` deb saqlang va `${2026 - tugilganYil}` shabloni orqali joriy yoshingizni chiqaring.

5. **To'g'ri tur tanlash · oson**  
   Quyidagi ma'lumotlar uchun to'g'ri turni tanlab o'zgaruvchilar yarating:  
   a) Do'kondagi non narxi (Double);  
   b) Maktabdagi sinf raqami (Int);  
   c) Dars boshlanganmi (Boolean).

6. **Val xatosini topish · o'rta**  
   Quyidagi kod nega xato berishini tushuntiring va uni to'g'rilang:  
   ```kotlin
   val tezlik = 60
   tezlik = 80
   println(tezlik)
   ```

7. **Matndan songa o'tkazish · o'rta**  
   `val str1 = "100"` va `val str2 = "250"` satrlarini `.toInt()` yordamida butun songa o'tkazing va ularning yig'indisini hisoblang.

8. **Doira yuzi · o'rta**  
   `val pi = 3.14159` va `val radius = 5.0` berilgan. Doira yuzini ($S = \pi \cdot r^2$) hisoblang va natijani ekranga chiqaring.

9. **Valyuta konvertori · qiyin**  
   AQSH dollarining so'mdagi kursi `val kurs = 12800.0` berilgan. Foydalanuvchining dollar miqdori (`val dollar = 150`) uchun so'mdagi umumiy summani va uning 12% daromad solig'ini hisoblab chiqaring.

10. **Karta ma'lumotlarini formatlash · bonus**  
    16 xonali plastik karta raqamini (`val karta = "8600123456789012"`) faqat oxirgi 4 ta raqamini ochiq qoldirib (`"**** **** **** 9012"`), xavfsiz ko'rinishda String Template orqali shakllantiring.
