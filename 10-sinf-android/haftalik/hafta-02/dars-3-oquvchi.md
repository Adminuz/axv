# 6-dars: ProGuard va R8 qoidalari bilan ishlash (Amaliyot)

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** ProGuard va R8 qoidalari bilan ishlash (`proguard-rules.pro`, `-keep` qoidalari, Gson/Moshi refleksiya muammolari, `mapping.txt` va deobfuskatsiya)

---

## Nazariy konspekt

### 1. Refleksiya (Reflection) va Release Crash muammosi
Android loyihangiz Debug rejimida mukammal ishlashi mumkin. Ammo `build.gradle` da `minifyEnabled = true` qilib, Release APK yig'ganingizda ilova ochilishi bilanoq yoki tarmoqdan ma'lumot olib kelganda to'satdan qulab tushishi (Crash) mumkin.

**Buning sababi:**
- R8 **Tree Shaking** algoritmi orqali ilovani tozalaydi.
- Agar siz JSON modelidagi (DTO) maydonlarni kod ichida to'g'ridan-to'g'ri chaqirmagan bo'lsangiz, R8 ularni "keraksiz" deb hisoblab o'chiradi yoki nomini `a, b, c` ga aylantiradi.
- **Gson, Moshi, Retrofit** kutubxonalari JSON kalitlarini obyekt maydonlari bilan bog'lashda **Refleksiya (Reflection)**dan foydalanadi (nomiga qarab topadi).
- Klass yoki maydon nomi o'zgargach, kutubxona ma'lumotni to'g'ri joylay olmaydi, natijada qiymatlar `null` bo'lib qoladi yoki `NullPointerException` sodir bo'ladi.

---

### 2. `proguard-rules.pro` qoidalar sintaksisi

`app/proguard-rules.pro` fayli orqali biz R8 ga qaysi qismlarga teginmaslik kerakligini buyuramiz:

```proguard
# Butun paketni va uning ichidagi barcha klasslar va maydonlarni saqlash
-keep class com.xorazmiy.app.models.** { *; }

# Klass nomini obfuskatsiya qilish, ammo SerializedName bor maydonlarni saqlash
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}

# Generic va annotatsiya ma'lumotlarini saqlash
-keepattributes Signature
-keepattributes *Annotation*

# Tashqi kutubxonaning noo'rin ogohlantirishlarini bostirish
-dontwarn okio.**
```

---

### 3. `@Keep` annotatsiyasi

AndroidX kutubxonasidagi `@Keep` annotatsiyasi qoidalarni alohida faylda yozib o'tirmasdan, to'g'ridan-to'g'ri Kotlin kodida himoyalash imkonini beradi:

```kotlin
import androidx.annotation.Keep

@Keep
data class ProductItem(
    val id: String,
    val title: String,
    val price: Double
)
```

R8 `@Keep` qo'yilgan barcha elementlarni avtomatik tarzda o'zgarishsiz qoldiradi.

---

### 4. `mapping.txt` va Stacktrace Deobfuskatsiyasi

Obfuskatsiya natijasida xatolik hisobotlarida klass va metod nomlari quyidagicha ko'rinadi:
```text
java.lang.NullPointerException: at c.a.b.d.a(Unknown Source)
```

R8 har safar release yig'ilganda `app/build/outputs/mapping/release/mapping.txt` faylini yaratadi. Bu fayl "asl nom -> qisqartirilgan nom" xaritasidir.

Ushbu xarita yordamida:
- Google Play Console yoki Firebase Crashlytics xatoliklarni avtomatik tarzda asl kod ko'rinishiga aylantiradi (Retrace).
- Har bir chiqarilgan versiya uchun `mapping.txt` faylini arxivlab saqlash shart!

---

### 5. Dinamik resurslarni saqlash (`keep.xml`)

Agar kodda resurslar dinamik nom orqali yuklansa, `res/raw/keep.xml` fayli yaratilib, quyidagicha ko'rsatiladi:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools"
    tools:keep="@drawable/icon_*,@raw/audio_*"
    tools:shrinkMode="strict" />
```

---

## Amaliy topshiriqlar

### 1-topshiriq: Loyihada ProGuard qoidalar faylini ochish · oson
Android Studio loyihangizning `app` modulida `proguard-rules.pro` faylini toping va uning ichidagi boshlang'ich izohlarni tahlil qiling.

### 2-topshiriq: User data modelini -keep bilan himoyalash · oson
`com.xorazmiy.app.data.model.User` data klassi uchun `proguard-rules.pro` faylida `-keep` direktivasini to'g'ri sintaksis bilan yozing.

### 3-topshiriq: SerializedName annotatsiyasi uchun qoida · oson
Gson kutubxonasining `@SerializedName` annotatsiyasiga ega barcha maydonlarni R8 tomonidan o'chirilishdan saqlovchi `-keepclassmembers` qoidasini kiriting.

### 4-topshiriq: Retrofit xizmat interfeysini saqlash · o'rta
`com.xorazmiy.app.network.ApiService` nomli Retrofit interfeysining barcha metodlarini R8 tomonidan inlining yoki o'chirilishdan saqlaydigan qoidani tuzing.

### 5-topshiriq: `@Keep` annotatsiyasini ulash va sinash · o'rta
`build.gradle.kts` ga `androidx.annotation:annotation` kutubxonasini qo'shing va yangi yaratilgan `CourseInfo` klassiga `@Keep` annotatsiyasini qo'llab ko'ring.

### 6-topshiriq: `mapping.txt` faylini topish va tahlil qilish · o'rta
Android Studio terminalida `./gradlew assembleRelease` buyrug'ini ishga tushiring. `app/build/outputs/mapping/release/mapping.txt` faylini ochib, qaysi klass qanday harfga o'zgarganini ko'rib chiqing.

### 7-topshiriq: Obfuskatsiya qilingan stacktrace'ni qo'lda ochish · o'rta
Berilgan xato qatori: `at a.b.c.a(SourceFile:15)`. `mapping.txt` parchasidan foydalanib, asl klass va metod nomini aniqlang.

### 8-topshiriq: `res/raw/keep.xml` faylini yaratish · qiyin
Loyihangizda `res/raw/` papkasini oching va `keep.xml` faylini yarating. Unda `avatar_` bilan boshlanuvchi barcha rasmlarni resurs qisqartirishdan himoyalash qoidasini yozing.

### 9-topshiriq: Reflection xatosini sun'iy hosil qilish va bartaraf etish · qiyin
Data class modelini yarating va uni Gson orqali JSON'ga o'giring. `minifyEnabled = true` qilganda yuzaga keladigan xatolikni kuzating, so'ngra `proguard-rules.pro` orqali uni bartaraf qiling.

### 10-topshiriq: Retrace CLI vositasi bilan ishlash · bonus
Android SDK ichida joylashgan `cmdline-tools/.../retrace` vositasidan foydalanib, terminalda shifrlangan stacktrace faylini `mapping.txt` orqali asl holiga keltiring.

---

## O'zini tekshirish uchun savollar

1. Nima sababdan Debug rejimda xatosiz ishlagan model Release versiyada qulab tushishi mumkin?
2. `-keep` va `-keepclassmembers` qoidalarining farqi nimada?
3. Barcha quyi paketlarni qamrab olish uchun qaysi belgi ishlatiladi: `*` yoki `**`?
4. `@Keep` annotatsiyasi qaysi kutubxonada joylashgan?
5. `mapping.txt` faylini har bir chiqarilgan dastur versiyasi uchun nima sababdan ehtiyotkorlik bilan saqlash kerak?

---

## Uyga vazifa

1. Android loyihangizda kamida 3 ta turli DTO klasslarini (`User`, `Order`, `Transaction`) yarating.
2. Ularning bir qismini `@Keep` annotatsiyasi bilan, qolganlarini esa `proguard-rules.pro` dagi `-keep` direktivasi orqali himoyalang.
3. Release APK hosil qiling va `mapping.txt` faylida ushbu klasslar o'zgarishsiz qolganini tekshiring.
