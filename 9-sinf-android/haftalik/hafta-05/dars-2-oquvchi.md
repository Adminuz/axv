# 14-dars. Funksiyalar va sinflar (1-qism): Funksiya e'lon qilish, parametrlar, standart qiymatlar va nomlangan argumentlar

> Bir kodni qayta-qayta yozish zerikarli! Bugun funksiyalar bilan kodni bo'laklarga ajratib, kerak joyda chaqirishni o'rganamiz.

## Dars xulosasi

- **Funksiya:** `fun nom() { ... }` shaklida e'lon qilinadi va nomi bilan chaqiriladi.
- **Parametrlar:** `nom: Tur` ko'rinishida; funksiya ichida ular `val` hisoblanadi.
- **Standart qiymat:** `age: Int = 18` bo'lsa, argumentni tushirib qoldirish mumkin.
- **Nomlangan argumentlar:** `displayUser("Tom", age = 28)`; tartib muhim emas.
- **Qoida:** birinchi nomlangan argumentdan keyin hammasi nomlangan bo'lishi kerak.

## Qo'shimcha ma'lumot

### Funksiya `main` dan tashqarida
Funksiyalar fayl darajasida (top-level) e'lon qilinadi va `main` dan chaqiriladi. E'lon qilish va chaqirish ikki xil amal.

### Nega parametr o'zgarmas?
Argument qiymati funksiyaga nusxa sifatida o'tadi. Kotlin tasodifiy o'zgartirishlardan saqlash uchun parametrlarni `val` qiladi. Massiv elementini o'zgartirish esa mumkin.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Funksiya | Nomlangan, qayta ishlatiladigan kod bloki |
| fun | Funksiya e'lon qilish kalit so'zi |
| Parametr | Funksiya e'lonidagi o'zgaruvchi |
| Argument | Chaqirishda beriladigan qiymat |
| Default qiymat | Berilmagan parametrning standart qiymati |
| Named argument | Nomi bilan berilgan argument |
| Top-level | Sinfdan tashqarida, fayl darajasidagi e'lon |

## Bilasizmi?

- Kotlinda `main` ham oddiy funksiya, faqat dastur aynan shundan boshlanadi.
- Android'da `onCreate()` kabi hayotiy sikl metodlari ham aslida funksiyalar.

## Topshiriqlar

### 1. hello funksiyasi · oson

`hello()` funksiyasini yozing: u «Hello Kotlin» chiqarsin. Uni ikki marta chaqiring.

**Kutiladigan natija:** Xabar ikki marta chiqadi.

### 2. showMessage · oson

`showMessage(message: String)` funksiyasini yozing va 3 xil matn bilan chaqiring.

**Kutiladigan natija:** 3 ta xabar chiqadi.

### 3. Ism va yosh · oson

`displayUser(name: String, age: Int)` funksiyasini yozing: «Tom, 36 yosh» ko'rinishida chiqarsin.

**Kutiladigan natija:** To'g'ri formatdagi qator.

### 4. Qo'shish · oson

`yigindi(a: Int, b: Int)` funksiyasi ikki sonning yig'indisini chiqarsin. 3 xil juftlik bilan sinang.

**Kutiladigan natija:** Har juftlik uchun to'g'ri yig'indi.

### 5. Standart qiymat · o'rta

`displayUser` da `age` ga standart 18 bering. `displayUser("Bob")` ni chaqiring.

**Kutiladigan natija:** `Bob, 18 yosh`.

### 6. Nomlangan argument · o'rta

`displayUser("Tom", position = "Manager", age = 28)` chaqiruvini yozing va funksiyani to'ldiring.

**Kutiladigan natija:** Qiymatlar to'g'ri joylashadi.

### 7. Natijani bashorat qiling · o'rta

Javob bering:

```kotlin
fun f(a: Int, b: Int = 5) = println(a + b)
f(2)
f(2, 10)
```

**Kutiladigan natija:** `7` va `12`.

### 8. Tartib o'zgartirish · o'rta

`displayUser(age = 20, name = "Ali")` chaqiruvi ishlaydimi? Sinab ko'ring.

**Kutiladigan natija:** Ishlaydi: nomlangan argumentlar tartibga bog'liq emas.

### 9. Xatoni toping · qiyin

Nega xato? Tuzating:

```kotlin
fun double(n: Int) {
    n = n * 2
    println(n)
}
```

**Kutiladigan natija:** Parametr `val`; `val k = n * 2` yangi o'zgaruvchi ishlatilgan.

### 10. Noto'g'ri chaqiruv · qiyin

`displayUser(name = "Tom", 28)` nega xato bo'lishi mumkin? Qoidani yozing.

**Kutiladigan natija:** Nomlangandan keyin nomlanmagan argument bo'lmaydi.

### 11. Kalkulyator funksiyasi · qiyin

`hisobla(a: Double, b: Double, amal: String = "+")` funksiyasini `when` bilan yozing.

**Kutiladigan natija:** `+`, `-`, `*`, `/` uchun to'g'ri natija.

### 12. Talaba kartasi · bonus

`talaba(ism, kurs = 1, guruh = "A")` funksiyasini yozing va 4 xil chaqiruv usulini sinang.

**Kutiladigan natija:** 4 xil chaqiruv, hammasi to'g'ri.

## O'zingizni tekshiring

1. Funksiya qanday e'lon qilinadi?
2. Parametr va argument farqi nima?
3. Parametrni funksiya ichida o'zgartirish mumkinmi?
4. Standart qiymat qanday beriladi?
5. Nomlangan argument nima?
6. Nomlangan argumentdan keyin qanday qoida bor?
7. Funksiyani chaqirish nima uchun kerak?

## Uyga vazifa

`salomlash`, `tekshir` va `talaba` funksiyalarini yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
