# 12-dars. Kotlin sintaksisi: if va when shart operatorlari

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + kod amaliyoti · **II-bob**, 12-dars (umumiy 1–102)

**Manba:** rasmiy o'quv dasturi («Kotlin sintaksisi: shart operatorlari (if, when) va ularning ifoda sifatida qo'llanilishi»), o'quv qo'llanma va uslubiy ko'rsatma.

## 1. Dars rejasi

**Maqsad:** O'quvchilarga Kotlinda `if-else` shart operatori, `if` ni ifoda (expression) sifatida qiymat qaytarishda qo'llash, zamonaviy `when` operatori (Java'dagi switch o'rniga), oraliqlar (`in 1..10`) va shartlar bo'yicha tarmoqlanishni o'rgatish.

**Kutiladigan natija:**
- Standart `if-else` va `if-else if` zanjirini yoza oladi;
- Ternar operator (`?:`) o'rniga `val max = if (a > b) a else b` ifodasini qo'llaydi;
- `when` operatorini qiymat, oraliq (`in`), tur (`is`) va shartsiz shaklda ishlatadi;
- `when` ni ifoda sifatida o'zgaruvchiga tenglab, `else` shartini to'g'ri qo'yadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 11-dars: `val` vs `var`, ma'lumot turlari, `$shablon` |
| 5–25 daq | Yangi mavzu 1 | `if-else` operatori va `if` ifoda sifatida (Expression) |
| 25–40 daq | Yangi mavzu 2 | `when` operatori (switch o'rniga): qiymat va oraliqlar (`in`) |
| 40–45 daq | Tanaffus | Harakatli tanaffus |
| 45–55 daq | Yangi mavzu 3 | `when` ifoda sifatida va xavfsiz `else` |
| 55–75 daq | Amaliyot | Baholash va yosh toifasi dasturlarini tuzish |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

---

## 2. Dars konspekti

### 2.1. `if` operatori va `if` ifoda sifatida (Expression)
Kotlinda boshqa tillardagi an'anaviy `if-else` to'liq ishlaydi:
```kotlin
val yosh = 17
if (yosh >= 18) {
    println("Xush kelibsiz!")
} else {
    println("Kirish taqiqlanadi.")
}
```

**Kotlinda Ternary Operator (`condition ? a : b`) yo'q!**
Uning o'rniga `if` ning o'zi ifoda (expression) sifatida qiymat qaytaradi:
```kotlin
val a = 15
val b = 25
val kattasi = if (a > b) a else b
println("Katta son: $kattasi")
```

### 2.2. `when` operatori &mdash; Zamonaviy tanlash vositasi
Java'dagi `switch` operatori o'rniga Kotlinda ancha qudratli `when` operatori ishlatiladi. `break` yozish umuman shart emas!

```kotlin
val fasl = 2
when (fasl) {
    1 -> println("Qish")
    2 -> println("Bahor")
    3 -> println("Yoz")
    4 -> println("Kuz")
    else -> println("Noto'g'ri fasl raqami")
}
```

### 2.3. `when` imkoniyatlari: oraliqlar (`in`) va ko'p qiymatlar
`when` operatorida bir nechta qiymatlarni vergul bilan yoki oraliq (`in`) bilan tekshirish mumkin:
```kotlin
val ball = 88

val baho = when (ball) {
    in 90..100 -> "5 (A'lo)"
    in 70..89  -> "4 (Yaxshi)"
    in 60..69  -> "3 (Qoniqarli)"
    in 0..59   -> "2 (Qoniqarsiz)"
    else       -> "Noto'g'ri ball"
}
println("Natija: $baho")
```

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Juft yoki toq son (oson)
Berilgan sonning juft yoki toq ekanligini `if-else` ifodasi orqali aniqlang va natijani `val tur = if (...) ... else ...` shaklida saqlang.

**Yechim:**
```kotlin
fun main() {
    val son = 24
    val tur = if (son % 2 == 0) "Juft" else "Toq"
    println("$son soni &mdash; $tur son.")
}
```

### 2-topshiriq. Hafta kuni nomi (o'rta)
1 dan 7 gacha bo'lgan son berilgan. `when` operatori orqali hafta kunining nomini (1 &mdash; Dushanba, ..., 7 &mdash; Yakshanba) aniqlang.

**Yechim:**
```kotlin
fun main() {
    val kun = 4
    val kunNomi = when (kun) {
        1 -> "Dushanba"
        2 -> "Seshanba"
        3 -> "Chorshanba"
        4 -> "Payshanba"
        5 -> "Juma"
        6 -> "Shanba"
        7 -> "Yakshanba"
        else -> "Bunday hafta kuni yo'q"
    }
    println("$kun-kun: $kunNomi")
}
```

### 3-topshiriq. Svetofor va tezlik monitoringi (qiyin)
Svetofor rangi (`"Qizil"`, `"Sariq"`, `"Yashil"`) va avtomobil tezligi (`Int`) berilgan. `when` va `if` kombinatsiyasi yordamida haydovchiga to'g'ri ko'rsatma beruvchi xavfsizlik modulini yozing.

**Yechim:**
```kotlin
fun main() {
    val chiroq = "Yashil"
    val tezlik = 65

    when (chiroq) {
        "Qizil" -> println("TO'XTANG! Harakatlanish taqiqlanadi.")
        "Sariq" -> println("DIQQAT! Harakatga tayyorlaning.")
        "Yashil" -> {
            if (tezlik > 60) {
                println("OGOHLANTIRISH: Yashil chiroq, lekin tezlik me'yordan yuqori ($tezlik km/soat)!")
            } else {
                println("Harakatlanishga ruxsat etiladi ($tezlik km/soat).")
            }
        }
        else -> println("Noma'lum svetofor signali.")
    }
}
```

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **Kotlinda ternary operator (`? :`) bormi?**
   - *Javob:* Yo'q, uning o'rniga `if-else` ifoda sifatida qo'llaniladi (`val x = if (a) b else c`).
2. **`when` operatorida `break` yozish kerakmi?**
   - *Javob:* Yo'q, Kotlin shart bajarilgach avtomatik blokdan chiqadi.
3. **`when` da oraliqni qanday tekshiramiz?**
   - *Javob:* `in 1..10 -> ...` orqali.
4. **`when` ifoda sifatida ishlatilganda nima shart?**
   - *Javob:* Barcha mumkin bo'lgan holatlar qamrab olinishi yoki majburiy `else` bloki bo'lishi shart.
5. **`if` ifoda sifatida ishlatilganda `else` qismi shartmi?**
   - *Javob:* Ha, o'zgaruvchiga qiymat yuklashda `else` shart.

---

## 5. Uyga vazifa

1. Foydalanuvchi yoshiga qarab toifani (`"Bola"`, `"O'smir"`, `"Katta"`, `"Keksa"`) aniqlovchi dasturni `when (yosh) in ...` orqali yozing.
2. Oddiy mini-kalkulyator: ikkita son va amal (`"+"`, `"-"`, `"*"`, `"/"`) berilganda `when` orqali natijani hisoblang.
3. Do'konda xarid summasiga qarab chegirma hisoblang (100 minggacha &mdash; 0%, 500 minggacha &mdash; 5%, 1 milliongacha &mdash; 10%, 1 milliondan ko'p &mdash; 15%).
