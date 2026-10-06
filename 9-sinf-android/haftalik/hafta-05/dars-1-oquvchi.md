# 13-dars. Kotlin sintaksisi (3-qism): Sikllar va oraliqlar

> Kompyuter takrorlashni yaxshi ko'radi! Bugun 100 ta `println` yozmasdan, bir necha qatorli sikllar bilan ishni qilamiz.

## Dars xulosasi

- **`for` sikli:** oraliq (`1..9`) bo'yicha takrorlaydi; `until` oxirgi chegarani kiritmaydi.
- **`downTo` va `step`:** teskari sanash va qadamni belgilash (`10 downTo 1`, `1..20 step 5`).
- **`while` va `do-while`:** shart bo'yicha takrorlash; `do-while` kamida 1 marta ishlaydi.
- **`break` va `continue`:** siklni to'xtatish va qadamni o'tkazib yuborish.
- **Ichma-ich sikl:** tashqi siklning har qadamida ichki sikl to'liq aylanadi.

## Qo'shimcha ma'lumot

### Sikl o'zgaruvchisi `val` hisoblanadi
`for (n in 1..9)` dagi `n` ni sikl ichida o'zgartirib bo'lmaydi (`n = n + 1` xato). Har aylanishda Kotlin unga yangi qiymat beradi.

### Cheksiz sikl xavfi
`while (true)` yoki shart hech qachon noto'g'ri bo'lmasa, dastur to'xtamaydi. `while` ichida o'zgaruvchini yangilashni (`i--`) unutmang.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Loop (Sikl) | Amalni takror bajaruvchi konstruksiya |
| Range (Oraliq) | Sonlar ketma-ketligi: `1..9` |
| until | Oxirgi chegarani kiritmaydigan oraliq |
| downTo | Kamayish tartibidagi oraliq |
| step | Oraliqdagi qadam |
| break | Siklni to'xtatish |
| continue | Joriy qadamni o'tkazib yuborish |

## Bilasizmi?

- Kotlinda `1..9` yozuvi aslida `IntRange` obyekti bo'lib, `in` bilan ham ishlatiladi: `if (x in 1..9)`.
- Android ilovalarida ro'yxat elementlarini ekranga chiqarish ham sikl asosida ishlaydi.

## Topshiriqlar

### 1. Kvadratlar · oson

`for (n in 1..9)` bilan sonlarning kvadratlarini chiqaring.

**Kutiladigan natija:** 9 qator: `1 * 1 = 1` dan `9 * 9 = 81` gacha.

### 2. 1 dan 10 gacha · oson

`for` va `..` yordamida 1 dan 10 gacha sonlarni bir qatorda chiqaring.

**Kutiladigan natija:** `1 2 3 4 5 6 7 8 9 10`.

### 3. until bilan · oson

`1 until 6` oralig'ini chiqaring va `1..6` bilan farqini yozing.

**Kutiladigan natija:** `1 2 3 4 5` va farq tushuntirilgan.

### 4. Teskari hisob · oson

`10 downTo 1` bilan teskari sanang, oxirida «Start!» yozing.

**Kutiladigan natija:** 10 dan 1 gacha va «Start!».

### 5. Qadamli sanash · o'rta

`1..20 step 5` va `20 downTo 0 step 4` ni chiqaring.

**Kutiladigan natija:** `1 6 11 16` va `20 16 12 8 4 0`.

### 6. while bilan yig'indi · o'rta

`while` yordamida 1 dan 100 gacha sonlar yig'indisini hisoblang.

**Kutiladigan natija:** Natija: `5050`.

### 7. Natijani bashorat qiling · o'rta

Ishga tushirmasdan javob bering:

```kotlin
var j = -1
do {
    println("j = $j")
    j--
} while (j > 0)
```

**Kutiladigan natija:** `j = -1` bir marta chop etiladi: `do-while` shartni keyin tekshiradi.

### 8. continue bilan · o'rta

1 dan 10 gacha sonlardan faqat toqlarini `continue` yordamida chiqaring.

**Kutiladigan natija:** `1 3 5 7 9`.

### 9. Xatoni toping · qiyin

Nega bu kod xato beradi? Tuzating:

```kotlin
for (n in 1..5) {
    n = n * 2
}
```

**Kutiladigan natija:** Sabab: sikl o'zgaruvchisi `val`; yangi `val k = n * 2` ishlatilgan.

### 10. Ko'paytirish jadvali · qiyin

Ichma-ich sikl bilan 1 dan 9 gacha ko'paytirish jadvalini chiqaring (har qatorda 9 ta son).

**Kutiladigan natija:** 9 ta qator, har birida 9 ta natija.

### 11. Sonni topish · qiyin

1 dan 50 gacha sonlardan 7 ga bo'linadigan birinchi sonni toping va `break` bilan siklni to'xtating.

**Kutiladigan natija:** `7` topiladi va sikl to'xtaydi.

### 12. Faktorial · bonus

`while` yoki `for` yordamida 1 dan 10 gacha faktorialni hisoblang (`1 * 2 * ... * n`).

**Kutiladigan natija:** `10! = 3628800`.

## O'zingizni tekshiring

1. `1..9` va `1 until 9` o'rtasidagi farq nima?
2. `downTo` va `step` nima uchun ishlatiladi?
3. `while` va `do-while` farqi nima?
4. `do-while` qaysi holatda kamida bir marta ishlaydi?
5. `break` va `continue` farqi?
6. Sikl o'zgaruvchisini sikl ichida o'zgartirish mumkinmi?
7. Ichma-ich sikl qanday ishlaydi?

## Uyga vazifa

1 dan 20 gacha juft sonlar, teskari hisob va 1–100 yig'indisi dasturlarini yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
