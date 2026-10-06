# 15-dars. Funksiyalar va sinflar (2-qism): Sinflar, obyektlar, konstruktorlar (primary vs secondary) va metodlar

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + kod amaliyoti · **II-bob**, 15-dars (umumiy 1–102)

**Manba:** rasmiy o'quv dasturi («Funksiyalar va sinflar (2-qism): Sinflar, obyektlar, konstruktorlar (primary vs secondary) va metodlar»), o'quv qo'llanma va uslubiy ko'rsatma.

## 1. Dars rejasi

**Maqsad:** O'quvchilarga Kotlinda sinf (`class`) va obyekt tushunchasi, xossalar va metodlar, birlamchi (primary) va ikkilamchi (secondary) konstruktorlar hamda `init` blokini o'rgatish.

**Kutiladigan natija:**
- `class` e'lon qilib, undan obyekt yaratadi;
- Xossalar (`var name`) va metodlar (`sayHello()`) yozadi;
- Primary va secondary konstruktor farqini tushuntiradi;
- `this(...)` orqali secondary konstruktorni primary ga bog'laydi, `init` blokini ishlatadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 14-dars: funksiyalar, parametrlar, default va named argument |
| 5–25 daq | Yangi mavzu 1 | Sinf va obyekt, xossalar |
| 25–40 daq | Yangi mavzu 2 | Metodlar va obyektni chaqirish |
| 40–45 daq | Tanaffus | Harakatli tanaffus |
| 45–55 daq | Yangi mavzu 3 | Primary va secondary konstruktorlar, `init` |
| 55–75 daq | Amaliyot | Person sinfi: xossalar, metod va konstruktorlar |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

---

## 2. Dars konspekti

### 2.1. Sinf va obyekt
Sinf (`class`) - obyektning chizmasi: u xossalar (ma'lumotlar) va metodlar (amallar) to'plamini tavsiflaydi. Obyekt - sinfdan yaratilgan aniq nusxa: `val tom = Person()`. Xossa `var name = "Undefined"` kabi boshlang'ich qiymat bilan e'lon qilinadi.
```kotlin
class Person {
    var name = "Undefined"
    var age = 18
}

fun main() {
    val tom = Person()
    println(tom.name)
    tom.name = "Tom"
    tom.age = 37
    println("${tom.name} ${tom.age}")
}
```

### 2.2. Metodlar
Sinf ichida e'lon qilingan funksiya metod deyiladi. Metod obyektning xossalariga to'g'ridan-to'g'ri murojaat qiladi va `obyekt.metod()` ko'rinishida chaqiriladi. Har bir obyekt o'z ma'lumotlari bilan ishlaydi.
```kotlin
class Person {
    var name = "Undefined"
    var age = 18

    fun sayHello() {
        println("Hello, my name is $name")
    }
    fun personToString(): String = "$name, $age yosh"
}

fun main() {
    val tom = Person()
    tom.name = "Tom"
    tom.sayHello()
    println(tom.personToString())
}
```

### 2.3. Konstruktorlar: primary va secondary
Konstruktor obyekt yaratilganda xossalarga boshlang'ich qiymat beradi. Birlamchi (primary) konstruktor sinf nomidan keyin yoziladi: `class Person(val name: String, var age: Int)`. Ikkilamchi (secondary) konstruktor sinf ichida `constructor` bilan e'lon qilinadi va primary bo'lsa, `this(...)` orqali unga murojaat qilishi shart. Boshlang'ich amallar `init` blokiga yoziladi.
```kotlin
class Person(val name: String, var age: Int) {
    init {
        println("Obyekt yaratildi: $name")
    }
    constructor(name: String) : this(name, 18) {
        println("Yosh berilmadi, 18 olindi")
    }
}

fun main() {
    val tom = Person("Tom", 37)
    val bob = Person("Bob")
}
```

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Person sinfi (oson)
`Person` sinfini `name` (standart `"Undefined"`) va `age` (18) xossalari bilan yozing. Obyekt yaratib, qiymatlarini chiqaring.

**Yechim:**
```kotlin
class Person {
    var name = "Undefined"
    var age = 18
}

fun main() {
    val tom = Person()
    tom.name = "Tom"
    tom.age = 37
    println("${tom.name}, ${tom.age}")
}
```

### 2-topshiriq. sayHello metodi (o'rta)
`Person` ga `sayHello()` va `personToString()` metodlarini qo'shing va chaqiring.

**Yechim:**
```kotlin
class Person {
    var name = "Undefined"
    var age = 18
    fun sayHello() = println("Hello, my name is $name")
    fun personToString() = "$name, $age yosh"
}

fun main() {
    val bob = Person()
    bob.name = "Bob"
    bob.sayHello()
    println(bob.personToString())
}
```

### 3-topshiriq. Primary va secondary (qiyin)
`Person(name, age)` primary konstruktorini va `Person(name)` secondary konstruktorini (`this(name, 18)`) yozing. `init` blokida xabar chiqaring.

**Yechim:**
```kotlin
class Person(val name: String, var age: Int) {
    init {
        println("Obyekt yaratildi: $name")
    }
    constructor(name: String) : this(name, 18)
    fun info() = println("$name, $age yosh")
}

fun main() {
    Person("Tom", 37).info()
    Person("Bob").info()
}
```

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **Sinf va obyekt farqi nima?**
   - *Javob:* Sinf - chizma, obyekt - undan yaratilgan nusxa.
2. **Kotlinda obyekt yaratishda `new` kerakmi?**
   - *Javob:* Yo'q, `Person()` deb yoziladi.
3. **Metod nima?**
   - *Javob:* Sinf ichida e'lon qilingan funksiya.
4. **Primary konstruktor nechta bo'ladi?**
   - *Javob:* Faqat bitta.
5. **Secondary konstruktor primary bilan qanday bog'lanadi?**
   - *Javob:* `: this(...)` orqali.

---

## 5. Uyga vazifa

1. `Student` sinfini `ism`, `kurs` xossalari va `info()` metodi bilan yozing.
2. Primary konstruktor `Car(brand, year)` va secondary `Car(brand)` (year = 2020) ni yozing.
3. `init` blokida obyekt yaratilganda xabar chiqaring va 2 ta obyekt yarating.
