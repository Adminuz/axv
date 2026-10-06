# 14-dars. Funksiyalar va sinflar (1-qism): Funksiya e'lon qilish, parametrlar, standart qiymatlar va nomlangan argumentlar

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + kod amaliyoti · **II-bob**, 14-dars (umumiy 1–102)

**Manba:** rasmiy o'quv dasturi («Funksiyalar va sinflar (1-qism): Funksiya e'lon qilish, parametrlar, standart qiymatlar va nomlangan argumentlar»), o'quv qo'llanma va uslubiy ko'rsatma.

## 1. Dars rejasi

**Maqsad:** O'quvchilarga Kotlinda funksiya e'lon qilish (`fun`), parametr va argumentlar, qiymat qaytarish, standart qiymatli parametrlar va nomlangan argumentlar bilan ishlashni o'rgatish.

**Kutiladigan natija:**
- `fun` kalit so'zi bilan funksiya e'lon qilib, `main` dan chaqira oladi;
- Parametrli funksiya yozadi va parametr qiymati o'zgarmasligini (`val`) biladi;
- Standart qiymatli (`age: Int = 18`) parametrlarni qo'llaydi;
- Nomlangan argumentlar bilan funksiyani tartibdan qat'i nazar chaqiradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 13-dars: `for`, `while`, `break`, `continue` |
| 5–25 daq | Yangi mavzu 1 | Funksiya e'lon qilish: `fun`, `main`, chaqirish |
| 25–40 daq | Yangi mavzu 2 | Parametrlar va qiymat qaytarish |
| 40–45 daq | Tanaffus | Harakatli tanaffus |
| 45–55 daq | Yangi mavzu 3 | Standart qiymatlar va nomlangan argumentlar |
| 55–75 daq | Amaliyot | Funksiya yozish: salomlashish, yosh tekshiruvi, hisoblagich |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

---

## 2. Dars konspekti

### 2.1. Funksiyani e'lon qilish va chaqirish
Funksiya - nomlangan kod bloki. U `fun` kalit so'zi bilan e'lon qilinadi, nomidan keyin qavs `()` va jingalak qavs ichida tana yoziladi. Funksiya e'lon qilinishi uni ishlatmaydi: uni nomi bilan chaqirish kerak. Dastur `main` funksiyasidan boshlanadi.
```kotlin
fun hello() {
    println("Hello Kotlin")
}

fun main() {
    hello()
    hello()
}
```

### 2.2. Parametrlar va argumentlar
Parametr funksiyaga tashqaridan ma'lumot uzatadi: `nom: Tur` ko'rinishida yoziladi. Chaqirishda berilgan qiymat argument deyiladi. Bir nechta parametr vergul bilan ajratiladi. Parametrlar `val` hisoblanadi: funksiya ichida ularni o'zgartirib bo'lmaydi (`n = n * 2` xato).
```kotlin
fun showMessage(message: String) {
    println(message)
}

fun displayUser(name: String, age: Int) {
    println("Name: $name  Age: $age")
}

fun main() {
    showMessage("Salom, Kotlin!")
    displayUser("Tom", 36)
}
```

### 2.3. Standart qiymatlar va nomlangan argumentlar
Parametrga `= qiymat` yozsak, u standart qiymat oladi va chaqirishda uni tushirib qoldirish mumkin. Nomlangan argumentda parametr nomi aniq yoziladi: `displayUser("Tom", position = "Manager", age = 28)`. Qoida: birinchi nomlangan argumentdan keyingi hamma argument ham nomlangan bo'lishi kerak.
```kotlin
fun displayUser(name: String, age: Int = 18, position: String = "Intern") {
    println("$name, $age yosh, $position")
}

fun main() {
    displayUser("Bob")
    displayUser("Tom", position = "Manager", age = 28)
}
```

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Salomlashish funksiyasi (oson)
`showMessage(message: String)` funksiyasini yozing va unga ikki xil matn bering.

**Yechim:**
```kotlin
fun showMessage(message: String) {
    println(message)
}

fun main() {
    showMessage("Salom, Kotlin!")
    showMessage("Bugun 14-dars")
}
```

### 2-topshiriq. Foydalanuvchi ma'lumoti (o'rta)
`displayUser(name: String, age: Int = 18)` funksiyasini yozing. Uni `"Bob"` va `"Tom", 28` bilan chaqiring.

**Yechim:**
```kotlin
fun displayUser(name: String, age: Int = 18) {
    println("Name: $name  Age: $age")
}

fun main() {
    displayUser("Bob")
    displayUser("Tom", 28)
}
```

### 3-topshiriq. Nomlangan argumentlar (qiyin)
`displayUser(name, age = 18, position = "Intern")` funksiyasini yozing. Uni faqat ism, keyin `position` va `age` nom bilan, oxirida `age` ni tushirib chaqiring.

**Yechim:**
```kotlin
fun displayUser(name: String, age: Int = 18, position: String = "Intern") {
    println("$name, $age yosh, $position")
}

fun main() {
    displayUser("Bob")
    displayUser("Tom", position = "Manager", age = 28)
    displayUser("Ali", position = "Developer")
}
```

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **Funksiya qaysi kalit so'z bilan e'lon qilinadi?**
   - *Javob:* `fun`.
2. **Parametr va argument farqi nima?**
   - *Javob:* Parametr - e'londagi o'zgaruvchi, argument - chaqirishda beriladigan qiymat.
3. **Funksiya parametrini ichkarida o'zgartirish mumkinmi?**
   - *Javob:* Yo'q, parametrlar `val` hisoblanadi.
4. **Standart qiymat qanday beriladi?**
   - *Javob:* `age: Int = 18` shaklida.
5. **Nomlangan argumentdan keyin nomlanmagan argument yozish mumkinmi?**
   - *Javob:* Yo'q, birinchi nomlangandan keyin hammasi nomlangan bo'lishi kerak.

---

## 5. Uyga vazifa

1. `salomlash(ism: String)` funksiyasini yozing va 3 ta ism bilan chaqiring.
2. `tekshir(yosh: Int, chegara: Int = 18)` funksiyasi yosh chegaradan katta yoki kichikligini chiqarsin.
3. `talaba(ism, kurs = 1, guruh = "A")` funksiyasini nomlangan argumentlar bilan 3 xil usulda chaqiring.
