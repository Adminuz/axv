# 15-dars. Funksiyalar va sinflar (2-qism): Sinflar, obyektlar, konstruktorlar (primary vs secondary) va metodlar

> Real dunyo obyektlardan iborat: talaba, telefon, avtomobil. Bugun Kotlinda ularni sinf va obyektlar bilan yozishni o'rganamiz.

## Dars xulosasi

- **Sinf (`class`):** obyekt chizmasi; xossalar va metodlardan iborat.
- **Obyekt:** sinfdan yaratilgan nusxa; `new` kerak emas (`Person()`).
- **Metodlar:** sinf ichidagi funksiyalar; `obyekt.metod()` bilan chaqiriladi.
- **Primary konstruktor:** sinf sarlavhasida, bitta (`class Person(val name: String)`).
- **Secondary konstruktor:** `constructor(...) : this(...)`; **`init`** bloki obyekt yaratilganda ishlaydi.

## Qo'shimcha ma'lumot

### `val` va `var` konstruktor parametrida
`class Person(val name: String, var age: Int)` - parametr oldiga `val` yoki `var` yozilsa, u avtomatik xossaga aylanadi. Yozilmasa u faqat konstruktor ichida ishlatiladi.

### Obyektlar mustaqil
`tom` va `bob` bir sinfdan yaratilsa ham o'z ma'lumotlariga ega: biriga o'zgartirish ikkinchisiga ta'sir qilmaydi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Class (Sinf) | Obyekt chizmasi |
| Object (Obyekt) | Sinfdan yaratilgan nusxa |
| Property (Xossa) | Obyektning ma'lumoti |
| Method (Metod) | Sinf ichidagi funksiya |
| Constructor | Obyekt yaratilganda ishlaydigan maxsus blok |
| Primary constructor | Sinf sarlavhasidagi asosiy konstruktor |
| Secondary constructor | Sinf ichidagi qo'shimcha konstruktor |
| init | Obyekt yaratilganda ishlovchi blok |

## Bilasizmi?

- Android'da `MainActivity` ham sinf: `class MainActivity : AppCompatActivity()`.
- Kotlin'da bitta fayl ichida bir nechta sinf yozish mumkin.

## Topshiriqlar

### 1. Bo'sh sinf · oson

`class Car` e'lon qiling va undan `val c = Car()` obyektini yarating.

**Kutiladigan natija:** Dastur xatosiz ishlaydi.

### 2. Xossalar · oson

`Person` ga `name = "Undefined"` va `age = 18` xossalarini qo'shib, qiymatlarini chiqaring.

**Kutiladigan natija:** `Undefined` va `18`.

### 3. Xossani o'zgartirish · oson

`tom.name = "Tom"`, `tom.age = 37` qilib, natijani chiqaring.

**Kutiladigan natija:** `Tom 37`.

### 4. Ikki obyekt · oson

`tom` va `bob` obyektlarini yarating, har biriga o'z ismini bering.

**Kutiladigan natija:** Obyektlar bir-biriga ta'sir qilmaydi.

### 5. sayHello · o'rta

`sayHello()` metodini yozing: «Hello, my name is ...» chiqarsin.

**Kutiladigan natija:** Ism to'g'ri chiqadi.

### 6. personToString · o'rta

`personToString(): String` metodi `name, age yosh` qaytarsin.

**Kutiladigan natija:** `Tom, 37 yosh`.

### 7. Primary konstruktor · o'rta

`class Person(val name: String, var age: Int)` ni yozing va `Person("Tom", 37)` yarating.

**Kutiladigan natija:** Xossalar konstruktor orqali to'ldiriladi.

### 8. Natijani bashorat qiling · o'rta

Javob bering:

```kotlin
class A(val x: Int) {
    init { println("init $x") }
}
A(5)
```

**Kutiladigan natija:** `init 5`.

### 9. Secondary konstruktor · qiyin

`constructor(name: String) : this(name, 18)` qo'shing va `Person("Bob")` ni chaqiring.

**Kutiladigan natija:** `age` = 18.

### 10. Xatoni toping · qiyin

Nega xato? Tuzating:

```kotlin
class P(val name: String) {
    constructor(n: String, a: Int) { }
}
```

**Kutiladigan natija:** Secondary `this(...)` bilan primary ga bog'lanmagan; `: this(n)` qo'shilgan.

### 11. init tartibi · qiyin

Primary, `init` va secondary konstruktorlarga `println` qo'ying va ishlash tartibini kuzating.

**Kutiladigan natija:** Tartib: primary, `init`, secondary tanasi.

### 12. Student sinfi · bonus

`Student(ism, kurs)` sinfini yozing: `info()` metodi, secondary konstruktor (kurs = 1) bilan.

**Kutiladigan natija:** 3 ta obyekt to'g'ri ishlaydi.

## O'zingizni tekshiring

1. Sinf va obyekt farqi nima?
2. Obyekt qanday yaratiladi?
3. Xossa va metod nima?
4. Primary konstruktor qayerda yoziladi?
5. Secondary konstruktor qanday e'lon qilinadi?
6. `this(...)` nima uchun kerak?
7. `init` bloki qachon ishlaydi?

## Uyga vazifa

`Student`, `Car` va `init` vazifalarini yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
