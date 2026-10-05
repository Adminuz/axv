# 11-dars. Kotlin sintaksisi: val vs var va ma’lumot turlari

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + kod amaliyoti · **II-bob**, 11-dars (umumiy 1–102)

**Manba:** rasmiy o'quv dasturi («II-BOB. Java va Kotlin dasturlash asoslari: Kotlin sintaksisi: o‘zgaruvchilar, ma'lumot turlari»), o'quv qo'llanma va uslubiy ko'rsatma.

## 1. Dars rejasi

**Maqsad:** O'quvchilarga Kotlin dasturlash tilining afzalliklari (Java bilan moslik, qisqa sintaksis, null-safety), o'zgaruvchi e'lon qilish (`val` vs `var`), asosiy ma'lumot turlari (`Int`, `Double`, `Float`, `Boolean`, `Char`, `String`) va String shablonlarini (`$nomi`, `${ifoda}`) o'rgatish.

**Kutiladigan natija:**
- Nega Google Kotlin'ni Android uchun asosiy til deb e'lon qilganini tushuntiradi;
- `val` (o'zgarmas / immutable) va `var` (o'zgaruvchan / mutable) farqini biladi va to'g'ri tanlaydi;
- Ma'lumot turlarini qat'iy va avtomatik aniqlash (Type Inference) bilan e'lon qiladi;
- String shablonlarida `$o'zgaruvchi` va `${a + b}` ifodalarini qo'llaydi;
- Tiplarni bir-biriga aylantirish (`toInt()`, `toDouble()`, `toString()`) metodlarini ishlatadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Kirish | II-bob boshlanishi. Kotlin tarixi va JetBrains/Google hamkorligi |
| 5–25 daq | Yangi mavzu 1 | `val` vs `var`: xavfsizlik va o'zgarmaslik tamoyili |
| 25–40 daq | Yangi mavzu 2 | Kotlin ma'lumot turlari: `Int`, `Double`, `Boolean`, `String` |
| 40–45 daq | Tanaffus | Harakatli tanaffus |
| 45–60 daq | Yangi mavzu 3 | String templates (`$`) va tiplarni konvertatsiya qilish |
| 60–75 daq | Amaliyot | Kotlin Playground / Android Studio'da mashqlar |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

---

## 2. Dars konspekti

### 2.1. Kotlin tili nima va nega Android'da 1-o'rinda?
Kotlin &mdash; JetBrains kompaniyasi tomonidan yaratilgan va 2017-yilda Google tomonidan Android uchun rasmiy tavsiya etilgan zamonaviy til.
- **Qisqa va ixcham:** Java'dagi 20 qatorlik kod Kotlinda 5 qatorda yoziladi.
- **Null-Safety:** Dasturlarning 70% qulashiga sabab bo'ladigan `NullPointerException` xatosini oldini oladi.
- **100% Java bilan mos:** Bitta loyiha ichida ham Java, ham Kotlin fayllarni birga ishlatish mumkin.

### 2.2. O'zgaruvchilar: `val` va `var`
- **`val` (Value):** O'zgarmas (Read-only / Immutable). Bir marta qiymat berilgach, uni boshqa o'zgartirib bo'lmaydi. Android dasturlashda 90% holatda `val` ishlatish tavsiya etiladi!
- **`var` (Variable):** O'zgaruvchan (Mutable). Qiymatini keyinchalik istalgancha o'zgartirish mumkin.

```kotlin
val pi = 3.14159
// pi = 3.14  -> XATO! val o'zgarmaydi (Val cannot be reassigned)

var ball = 85
ball = 92     // TO'G'RI! var o'zgarishi mumkin
```

### 2.3. Asosiy ma'lumot turlari
Kotlin'da barcha turlar obyekt hisoblanadi (primitiv turlar yo'q, hamma tur Katta harf bilan boshlanadi):
- `Int`: Butun sonlar (`val yosh: Int = 15`)
- `Double`: Haqiqiy o'nlik sonlar (`val narx: Double = 12500.50`)
- `Float`: Kichikroq o'nlik sonlar (`val foiz: Float = 4.5f`)
- `Boolean`: Mantiqiy qiymat (`val faol: Boolean = true`)
- `Char`: Bitta belgi (`val belgi: Char = 'A'`)
- `String`: Matn (`val nom: String = "Android"`)

**Type Inference (Turni avtomatik aniqlash):**
Kotlin qiymatga qarab o'zi turni aniqlay oladi:
```kotlin
val shahar = "Toshkent"  // Kotlin avtomatik String deb biladi
val yil = 2026           // Int deb biladi
```

### 2.4. String shablonlari (String Templates)
Matn ichiga o'zgaruvchi yoki hisob-kitobni joylash uchun `$` belgisi ishlatiladi:
```kotlin
val ism = "Sanjar"
val yosh = 16
println("Mening ismim $ism, yoshim $yosh da.")
println("Kelasi yili men ${yosh + 1} yoshga to'laman.")
```

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. O'quvchi ma'lumotlari (oson)
O'z ismingiz (`val`), yoshingiz (`var`), bo'yingiz metrda (`val`), va dasturchilikka qiziqishingiz (`val Boolean`) o'zgaruvchilarini e'lon qiling va String template bilan chiqaring.

**Yechim:**
```kotlin
fun main() {
    val ism: String = "Anvar"
    var yosh: Int = 15
    val boy: Double = 1.75
    val dasturchimi: Boolean = true

    println("O'quvchi: $ism, Yoshi: $yosh, Bo'yi: $boy m, Dasturchi: $dasturchimi")
}
```

### 2-topshiriq. Val xatosini tuzatish (o'rta)
Quyidagi kodda xatolik bor. Uni tuzating:
```kotlin
fun main() {
    val ball = 70
    ball = ball + 15
    println("Yangi ball: $ball")
}
```

**Yechim:** `val ball` ni `var ball` ga o'zgartirish kerak, chunki uning qiymati o'zgarmoqda.
```kotlin
fun main() {
    var ball = 70
    ball = ball + 15
    println("Yangi ball: $ball")
}
```

### 3-topshiriq. Tiplarni konvertatsiya qilish (qiyin)
Foydalanuvchi kiritgan string ko'rinishidagi sonlarni (`"45"` va `"12"`) butun songa o'tkazib, ularning yig'indisi va ko'paytmasini hisoblang.

**Yechim:**
```kotlin
fun main() {
    val matnSon1 = "45"
    val matnSon2 = "12"

    val son1 = matnSon1.toInt()
    val son2 = matnSon2.toInt()

    val yigindi = son1 + son2
    val kopaytma = son1 * son2

    println("Yig'indi: $son1 + $son2 = $yigindi")
    println("Ko'paytma: $son1 * $son2 = $kopaytma")
}
```

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **`val` va `var` farqi nima?**
   - *Javob:* `val` bir marta beriladigan o'zgarmas (read-only), `var` esa qiymati o'zgarishi mumkin bo'lgan o'zgaruvchi.
2. **Nega Kotlin'da `val` ishlatish tavsiya qilinadi?**
   - *Javob:* Dastur xavfsizroq bo'ladi, tasodifiy qiymat o'zgarishlari va xatolarning oldi olinadi.
3. **Kotlin'da Type Inference nima?**
   - *Javob:* O'zgaruvchi turini aniq yozmasak ham, Kotlin uning berilgan qiymatiga qarab turni o'zi aniqlashi.
4. **String Template ichida hisob-kitob qanday yoziladi?**
   - *Javob:* Jingalak qavs ichida: `${a + b}`.
5. **Stringni butun songa aylantirish uchun qaysi metod ishlatiladi?**
   - *Javob:* `.toInt()`.

---

## 5. Uyga vazifa

1. `val` va `var` yordamida o'z smartfoningiz haqidagi ma'lumotlarni (modeli, narxi, xotirasi, quvvat foizi) saqlovchi dastur yozing.
2. 3 ta fandan olingan baholarning o'rtacha arifmetik qiymatini hisoblab, `${...}` shabloni orqali chiqaring.
3. String ko'rinishidagi narxni (`val narx = "150000"`) `toInt()` orqali songa o'tkazib, 12% QQS qo‘shilgan summani hisoblang.
