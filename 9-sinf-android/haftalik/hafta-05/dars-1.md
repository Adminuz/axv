# 13-dars. Kotlin sintaksisi (3-qism): Sikllar va oraliqlar

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + kod amaliyoti · **II-bob**, 13-dars (umumiy 1–102)

**Manba:** rasmiy o'quv dasturi («Kotlin sintaksisi (3-qism): Sikllar (for, while, do-while) va oraliqlar (ranges: in, downTo, step)»), o'quv qo'llanma va uslubiy ko'rsatma.

## 1. Dars rejasi

**Maqsad:** O'quvchilarga Kotlinda takrorlanuvchi amallarni bajarish: `for` sikli va oraliqlar (`..`, `until`, `downTo`, `step`), `while` va `do-while` sikllari, `break` va `continue` operatorlari hamda ichma-ich sikllarni o'rgatish.

**Kutiladigan natija:**
- `for` siklini oraliq (`1..9`) va `until` bilan yoza oladi;
- `downTo` va `step` yordamida teskari va qadamli sanashni bajaradi;
- `while` va `do-while` farqini (shart oldin yoki keyin tekshirilishini) tushuntiradi;
- `break` va `continue` yordamida siklni boshqaradi, ichma-ich sikl bilan jadval chiqaradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 12-dars: `if-else`, `when`, `in` oraliqlari |
| 5–25 daq | Yangi mavzu 1 | `for` sikli va oraliqlar (`..`, `until`) |
| 25–40 daq | Yangi mavzu 2 | `downTo`, `step`, `while` va `do-while` sikllari |
| 40–45 daq | Tanaffus | Harakatli tanaffus |
| 45–55 daq | Yangi mavzu 3 | `break`, `continue` va ichma-ich sikllar |
| 55–75 daq | Amaliyot | Kvadratlar, ko'paytirish jadvali va teskari hisob dasturlari |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

---

## 2. Dars konspekti

### 2.1. `for` sikli va oraliqlar
Bir xil amalni ko'p marta bajarish uchun sikl ishlatiladi. `for` sikli oraliq (range) yoki kolleksiya elementlari bo'yicha yuradi. `1..9` yozuvi 1 dan 9 gacha (9 ham kiradi), `1 until 10` esa 10 kirmaydigan oraliqni bildiradi.
```kotlin
for (n in 1..9) {
    println("$n * $n = ${n * n}")
}
```

### 2.2. `downTo`, `step`, `while` va `do-while`
`downTo` kamayish tartibida, `step` esa berilgan qadam bilan sanaydi. `while` sikli shartni tana bajarilishidan **oldin**, `do-while` esa **keyin** tekshiradi, shuning uchun `do-while` kamida bir marta ishlaydi.
```kotlin
var i = 10
while (i > 7) {
    println(i)
    i--
}
var j = -1
do {
    println("j = $j")
    j--
} while (j > 0)
```

### 2.3. `break`, `continue` va ichma-ich sikllar
`break` siklni darhol to'xtatadi, `continue` esa joriy qadamni o'tkazib yuborib keyingisiga o'tadi. Sikl ichida boshqa sikl yozish mumkin: tashqi sikl bir marta aylansa, ichki sikl to'liq aylanib chiqadi.
```kotlin
for (n in 1..7) {
    if (n == 5) continue
    print("$n ")
}
println()
for (a in 1..3) {
    for (b in 1..3) print("${a * b}\t")
    println()
}
```

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Kvadratlar jadvali (oson)
`for` va `1..9` oralig'i bilan 1 dan 9 gacha sonlarning kvadratlarini chiqaring.

**Yechim:**
```kotlin
fun main() {
    for (n in 1..9) {
        println("$n * $n = ${n * n}")
    }
}
```

### 2-topshiriq. Teskari hisob va qadam (o'rta)
`10 downTo 1` bilan teskari sanang, so'ng `1..20 step 5` bilan har 5-sonni chiqaring.

**Yechim:**
```kotlin
fun main() {
    for (i in 10 downTo 1) print("$i ")
    println()
    for (j in 1..20 step 5) print("$j ")
    println()
}
```

### 3-topshiriq. Ko'paytirish jadvali va to'xtatish (qiyin)
Ichma-ich sikl bilan 1 dan 5 gacha ko'paytirish jadvalini chiqaring. Natija 20 dan oshsa ichki siklni `break` bilan to'xtating, 3 ga bo'linadigan natijani `continue` bilan tashlab o'ting.

**Yechim:**
```kotlin
fun main() {
    for (a in 1..5) {
        for (b in 1..5) {
            val natija = a * b
            if (natija > 20) break
            if (natija % 3 == 0) continue
            print("$natija\t")
        }
        println()
    }
}
```

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **`1..5` va `1 until 5` farqi nima?**
   - *Javob:* `1..5` da 5 kiradi, `until` da kirmaydi.
2. **Kamayish tartibida sanash uchun nima ishlatiladi?**
   - *Javob:* `downTo`, masalan `10 downTo 1`.
3. **`step` nima qiladi?**
   - *Javob:* Oraliqda qadamni belgilaydi: `1..10 step 3`.
4. **`while` va `do-while` farqi?**
   - *Javob:* `while` shartni oldin, `do-while` keyin tekshiradi; `do-while` kamida bir marta ishlaydi.
5. **`break` va `continue` farqi?**
   - *Javob:* `break` siklni to'xtatadi, `continue` joriy qadamni o'tkazib keyingisiga o'tadi.

---

## 5. Uyga vazifa

1. 1 dan 20 gacha faqat juft sonlarni `step` yordamida chiqaruvchi dastur yozing.
2. 10 dan 1 gacha teskari hisob va oxirida «Start!» yozuvini chiqaring.
3. `while` yordamida 1 dan 100 gacha sonlar yig'indisini hisoblang.
