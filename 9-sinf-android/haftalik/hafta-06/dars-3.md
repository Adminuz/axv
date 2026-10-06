# 18-dars. Kotlinda OOP bilan tanishish (1-qism): obyektga yo'naltirilgan dasturlash asoslari va inkapsulyatsiya (private, protected, public)

**Fan:** Android dasturlash
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 3-dars (umumiy 18-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `uslubiy-korsatma.txt` («Inkapsulyatsiya va Access Modifiers»: `public`, `private`, `protected`, `internal`; xususiyatlarni `private` qilib, kirish uchun metodlar (getters/setters) yaratish). `private set` va maxsus `set` standart Kotlin hujjatidan qo'shildi. Kod namunalari Kotlin Playground'da tekshirilishi kerak.

---

## Darsning maqsadi

O'quvchilarga obyektga yo'naltirilgan dasturlash (OYD) g'oyasini va 4 asosiy tamoyilini, inkapsulyatsiya tushunchasini, `public`, `private`, `protected`, `internal` kirish huquqlarini, `private set` va maxsus setter bilan ma'lumotni himoyalashni o'rgatish.

## Kutilayotgan natijalar

- OYD ning 4 tamoyilini (inkapsulyatsiya, meros, polimorfizm, abstraksiya) sanaydi;
- Inkapsulyatsiya nima uchun kerakligini misol bilan tushuntiradi;
- `public`, `private`, `protected`, `internal` farqini aytadi;
- Xossani `private set` bilan tashqaridan o'zgartirishdan himoyalaydi;
- Maxsus setter bilan noto'g'ri qiymatni rad etadi.

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 15–17-dars: sinflar, kolleksiyalar, lambda |
| 08–25 | Yangi mavzu 1 | OYD g'oyasi va inkapsulyatsiya |
| 25–38 | Yangi mavzu 2 | Kirish huquqlari: public, private, protected, internal |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | private set va maxsus setter: BankHisobi |
| 58–75 | Amaliyot | Amaliyot: himoyalangan sinf, xulosa |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. OYD g'oyasi va inkapsulyatsiya

**Obyektga yo'naltirilgan dasturlash (OYD)** — dasturni real hayotdagi narsalarga o'xshash **obyektlar** to'plami sifatida tuzish: har obyektning **ma'lumoti** (xossalar) va **harakatlari** (metodlar) bor. OYD ning 4 tamoyili: **inkapsulyatsiya**, **meros**, **polimorfizm** va **abstraksiya**. Bugun birinchisi. **Inkapsulyatsiya** — obyektning ichki ma'lumotlarini himoya qilish: ma'lumotga kim va qayerdan kira olishini boshqarish. Misol: bank kartasi — pulni to'g'ridan-to'g'ri o'zgartirib bo'lmaydi, faqat «yechish» va «qo'shish» amallari orqali, ular esa qoidalarni tekshiradi. Shu tufayli noto'g'ri holat (manfiy balans) yuzaga kelmaydi va ichki tuzilmani keyin o'zgartirish oson bo'ladi.

```kotlin
class Hisob {
    var balans: Double = 0.0
}

fun main() {
    val h = Hisob()
    h.balans = -5000.0     // hech kim to'xtatmaydi!
    println(h.balans)      // -5000.0
}
```

Hamma narsa `public` bo'lsa, istalgan joydan noto'g'ri qiymat yozish mumkin. Inkapsulyatsiya shu xatolardan himoya qiladi.

### 2. Kirish huquqlari: public, private, protected, internal

Kotlinda to'rtta **kirish modifikatori** (access modifier) bor. **`public`** (standart) — hamma joydan ko'rinadi. **`private`** — faqat shu sinf ichida. **`protected`** — sinf ichida va undan meros olgan sinflarda (meros — keyingi dars). **`internal`** — faqat bitta modul (loyihaning bir qismi) ichida. Modifikator xossa, metod va konstruktor oldiga yoziladi: `private val kod = 1234`. Qoida: **eng cheklangan** huquqdan boshlang: avval `private`, kerak bo'lsa ochasiz. Odatda xossalar `private`, ularga kirish uchun esa kerakli metodlar `public` bo'ladi. Eslatma: `protected` sinfdan tashqarida (top-level) ishlatilmaydi.

```kotlin
open class Transport {
    private val kalit = "1234"        // faqat Transport ichida
    protected var tezlik = 0          // + merosxo'r sinflarda
    internal fun modulInfo() = "Modul ichida"
    fun nomi() = "Transport"          // public (standart)
}

fun main() {
    val t = Transport()
    println(t.nomi())                 // ishlaydi
    // println(t.kalit)               // XATO: private
    // println(t.tezlik)              // XATO: protected
}
```

Xato xabarini o'qing: «Cannot access 'kalit': it is private in 'Transport'». Bu kompilyatorning himoyasi: dastur ishga tushmasdan xato topiladi.

### 3. private set, maxsus setter va BankHisobi

Xossani **o'qish** hammaga ochiq, **yozish** esa faqat sinf ichida bo'lishi uchun: `var balans: Double = 0.0` ostiga `private set` yoziladi. Tashqaridan `balans` ni o'qiy olasiz, lekin `balans = 100.0` deb yoza olmaysiz — faqat sinfning metodlari orqali. Maxsus **setter** noto'g'ri qiymatni rad etadi: `set(value) { if (value in 0..100) field = value }` — `field` xossaning o'zi (backing field). Misol: `BankHisobi` — `qoshish()` va `yechish()` metodlari qoidalarni tekshiradi: summa musbat bo'lishi, balansdan oshmasligi shart. Boshqa tillardagi `getBalans()`/`setBalans()` kabi metodlar Kotlin'da xossalar bilan avtomatik hosil bo'ladi.

```kotlin
class BankHisobi(val egasi: String) {
    var balans: Double = 0.0
        private set

    fun qoshish(summa: Double) {
        if (summa > 0) balans += summa
    }

    fun yechish(summa: Double): Boolean {
        if (summa <= 0 || summa > balans) return false
        balans -= summa
        return true
    }
}
```

`val` xossa uchun setter yo'q. `var` xossada `private set` yozuvi — tashqaridan o'qish mumkin, yozish mumkin emas.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Modifikatorlarni sanang

Kotlinning 4 ta kirish modifikatorini yozing.

**Yechim:** public (standart), private, protected, internal.

### 2-topshiriq (oson). private xossa

`Sir` sinfida `kod` xossasi faqat sinf ichida ko'rinsin.

**Yechim:**
```kotlin
class Sir {
    private val kod = "1234"
}
```

### 3-topshiriq (o'rta). private set

`Hisob` da `balans` ni tashqaridan o'qish mumkin, yozish mumkin bo'lmasin.

**Yechim:**
```kotlin
class Hisob {
    var balans: Double = 0.0
        private set
}
```

### 4-topshiriq (o'rta). Maxsus setter

`baho` faqat 0 dan 100 gacha qiymat olsin.

**Yechim:**
```kotlin
class Oquvchi {
    var baho: Int = 0
        set(value) {
            if (value in 0..100) field = value
        }
}
```

### 5-topshiriq (qiyin). BankHisobi

`qoshish()` va `yechish()` metodlarini qoidalar bilan yozing.

**Yechim:**
```kotlin
class BankHisobi {
    var balans: Double = 0.0
        private set

    fun qoshish(summa: Double) {
        if (summa > 0) balans += summa
    }

    fun yechish(summa: Double): Boolean {
        if (summa <= 0 || summa > balans) return false
        balans -= summa
        return true
    }
}
```

### 6-topshiriq (bonus). Nega private?

Xossalarni nega `private` qilib, metodlar orqali ochamiz? 2 sabab yozing.

**Yechim:** Noto'g'ri qiymatdan himoya qilish; ichki tuzilmani keyin boshqalarga ta'sir qilmasdan o'zgartirish mumkin.

---

## Tezkor nazorat

1. Inkapsulyatsiya nima? **Javob:** Ichki ma'lumotni himoya qilish.
2. Standart modifikator? **Javob:** `public`.
3. `private` qayerda ko'rinadi? **Javob:** Faqat shu sinf ichida.
4. `private set` nima beradi? **Javob:** Tashqaridan o'qish mumkin, yozish mumkin emas.
5. `protected` qayerda ko'rinadi? **Javob:** Sinf va merosxo'rlarida.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
