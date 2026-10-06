# 16-dars. Kotlinda ma'lumot turlari, list va maplar (1-qism): kolleksiyalar — List, MutableList, Set va Map

**Fan:** Android dasturlash
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 1-dars (umumiy 16-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (List, `listOf`, `get`, `getOrNull`, `getOrElse`, `mutableListOf`, Map, `mapOf`, `getOrDefault`) va `uslubiy-korsatma.txt` (Mutable vs Immutable List, Map, «Inventarizatsiya tizimi»). Set bo'limi shu mavzudagi standart Kotlin hujjatidan qo'shildi. Kod namunalari Android Studio / Kotlin Playground'da tekshirilishi kerak.

---

## Darsning maqsadi

O'quvchilarga Kotlinda kolleksiya tushunchasini, o'zgarmas (`listOf`) va o'zgaruvchan (`mutableListOf`) ro'yxatlar farqini, indeks bilan ishlash va xavfsiz olish usullarini (`getOrNull`, `getOrElse`), Set (takrorlanmas to'plam) va Map (kalit–qiymat juftligi) ni hamda ularni sikl bilan aylanib chiqishni o'rgatish.

## Kutilayotgan natijalar

- List va MutableList farqini (`listOf` va `mutableListOf`) tushuntiradi;
- Element olishda indeks va `getOrNull()` dan foydalanadi;
- Set yordamida takrorlanmas qiymatlarni saqlaydi;
- Map da kalit orqali qiymatni topadi, qo'shadi va yangilaydi;
- Kolleksiyalarni `for` sikli bilan aylanib chiqadi (jumladan, `for ((k, v) in map)`).

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 15-dars: sinflar, obyektlar, konstruktorlar |
| 08–25 | Yangi mavzu 1 | List va MutableList: indeks, qo'shish, o'chirish |
| 25–38 | Yangi mavzu 2 | Set: takrorlanmas to'plam |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | Map: kalit–qiymat juftligi |
| 58–75 | Amaliyot | Amaliyot: «Omborxona» ro'yxati, xulosa |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. List va MutableList

**Kolleksiya** — ko'p qiymatni bitta o'zgaruvchida saqlovchi tuzilma. **List** — tartiblangan ro'yxat: har elementning **indeksi** bor (0 dan boshlanadi), qiymatlar takrorlanishi mumkin. `listOf(...)` — **o'zgarmas** (immutable) ro'yxat: element qo'shib yoki o'chirib bo'lmaydi. `mutableListOf(...)` — **o'zgaruvchan**: `add`, `removeAt`, `addAll` ishlaydi. Element olish: `list[0]` yoki `list.get(0)`; indeks chegaradan chiqsa — xato (istisno). Xavfsiz usul: `getOrNull(i)` (yo'q bo'lsa `null`) va `getOrElse(i) { ... }`. `val` bilan e'lon qilingan `mutableListOf` ning ichini o'zgartirish mumkin: `val` faqat o'zgaruvchining boshqa ro'yxatga almashishini taqiqlaydi. Maslahat: iloji bo'lsa o'zgarmas ro'yxat ishlating.

```kotlin
val people = listOf("Tom", "Sam", "Kate")
println(people[0])               // Tom
println(people.getOrNull(10))    // null

val tasks = mutableListOf("Kod yozish", "Test")
tasks.add("Deploy")
tasks.removeAt(1)
println(tasks)                   // [Kod yozish, Deploy]
```

`people[10]` dasturni to'xtatadi (IndexOutOfBounds), `getOrNull(10)` esa `null` qaytaradi. Foydalanuvchi kiritgan indeks bilan doim xavfsiz usulni ishlating.

### 2. Set: takrorlanmas qiymatlar

**Set** — takrorlanmaydigan qiymatlar to'plami. Bir xil elementni ikki marta qo'shsangiz, u bitta bo'lib qoladi. Indeks yo'q: «shu element bormi?» degan savol asosiy ish (`contains` yoki `in`). `setOf(...)` — o'zgarmas, `mutableSetOf(...)` — o'zgaruvchan to'plam; `add` qo'shilganini `true`/`false` bilan bildiradi. Amaliy foyda: ro'yxatdagi takrorlarni olib tashlash: `list.toSet()` yoki `list.distinct()`. Misol: kiritilgan teglar, tashrif buyurgan foydalanuvchilar ID lari. Qachon qaysi birini tanlash: tartib va takror kerak bo'lsa — List; faqat noyob qiymatlar kerak bo'lsa — Set.

```kotlin
val tags = mutableSetOf("kotlin", "android")
println(tags.add("kotlin"))      // false: allaqachon bor
println(tags.add("compose"))     // true
println(tags.size)               // 3
println("android" in tags)       // true

val unique = listOf(1, 2, 2, 3, 3).toSet()
println(unique)                  // [1, 2, 3]
```

Set'da elementga `set[0]` deb bo'lmaydi. Tartib kerak bo'lsa, `toList()` bilan ro'yxatga aylantiring.

### 3. Map: kalit–qiymat juftligi

**Map** (lug'at) — ma'lumotni indeks bilan emas, **kalit** (key) bilan saqlaydi: har kalitga bitta **qiymat** (value) mos. Kalitlar **noyob**; mavjud kalit bilan yangi qiymat yozsangiz, eskisi almashadi. Qiymatlar takrorlanishi mumkin. `mapOf("a" to 1)` — o'zgarmas, `mutableMapOf(...)` — o'zgaruvchan; yangilash: `map[kalit] = qiymat`. Olish: `map[kalit]` — kalit yo'q bo'lsa `null` qaytaradi; `getOrDefault(kalit, standart)` — standart qiymat beradi; `containsKey(kalit)` — kalit bormi. Aylanish: `for ((kalit, qiymat) in map)`; `map.keys` va `map.values` — alohida kalitlar va qiymatlar. Misol: mahsulot nomi → narxi, pasport ID → ism.

```kotlin
val prices = mutableMapOf("Laptop" to 1200.0, "Phone" to 800.0)
prices["Phone"] = 750.0
println(prices["Tablet"])                    // null
println(prices.getOrDefault("Tablet", 0.0))  // 0.0
println(prices.containsKey("Laptop"))        // true
for ((name, price) in prices) println("$name: $price")
```

Kalit yo'q bo'lsa `map[kalit]` `null` qaytaradi. Natijani ishlatishdan oldin `?:` (Elvis) yoki `getOrDefault` bilan standart qiymat bering.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Ro'yxat yarating

3 ta ismdan o'zgarmas ro'yxat yarating va birinchisini chiqaring.

**Yechim:**
```kotlin
val names = listOf("Ali", "Vali", "Gulnora")
println(names[0])
```

### 2-topshiriq (oson). Mahsulot qo'shing

`mutableListOf` ga yangi mahsulot qo'shing va ro'yxatni chiqaring.

**Yechim:**
```kotlin
val products = mutableListOf("Laptop", "Phone")
products.add("Tablet")
println(products)
```

### 3-topshiriq (o'rta). Xavfsiz olish

Ro'yxatning 10-elementini xatosiz oling; yo'q bo'lsa «Yo'q» chiqsin.

**Yechim:**
```kotlin
val names = listOf("Ali", "Vali")
println(names.getOrElse(10) { "Yo'q" })
```

### 4-topshiriq (o'rta). Takrorlarni olib tashlash

`listOf(1, 2, 2, 3, 3)` dan takrorsiz to'plam oling.

**Yechim:**
```kotlin
println(listOf(1, 2, 2, 3, 3).toSet())   // [1, 2, 3]
```

### 5-topshiriq (qiyin). Narxlar lug'ati

Mahsulot → narx Map yarating, bir narxni yangilang va hisobot chiqaring.

**Yechim:**
```kotlin
val prices = mutableMapOf("Laptop" to 1200.0, "Phone" to 800.0)
prices["Phone"] = 750.0
for ((name, price) in prices) println("$name: $price")
```

### 6-topshiriq (bonus). Qidiruv funksiyasi

Narxni nom bo'yicha topadigan funksiya yozing: topilmasa «Topilmadi» qaytarsin.

**Yechim:**
```kotlin
fun narxniTop(prices: Map<String, Double>, nom: String): String {
    val narx = prices[nom] ?: return "Topilmadi"
    return "$nom: $narx"
}
```

---

## Tezkor nazorat

1. `listOf` va `mutableListOf` farqi? **Javob:** O'zgarmas va o'zgaruvchan ro'yxat.
2. Birinchi elementning indeksi? **Javob:** 0.
3. Set ning asosiy xususiyati? **Javob:** Takrorlanmaydi.
4. Map da kalit qanday bo'ladi? **Javob:** Noyob.
5. Kalit yo'q bo'lsa `map[kalit]` nima qaytaradi? **Javob:** `null`.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
