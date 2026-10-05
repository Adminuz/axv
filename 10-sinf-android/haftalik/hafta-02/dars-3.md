# 6-dars: ProGuard va R8 qoidalari bilan ishlash (2-qism: Amaliyot)

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 2-hafta, 3-dars (umumiy 6-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Android ilovalarida R8 va ProGuard qoidalarini (`proguard-rules.pro`) to'g'ri yozish, koddagi refleksiya (Reflection) mexanizmlariga asoslangan kutubxonalar (Gson, Moshi, Retrofit, Room) bilan bog'liq xatoliklarning oldini olish, `@Keep` annotatsiyasidan foydalanish hamda obfuskatsiya qilingan stacktrace'larni `mapping.txt` yordamida deobfuskatsiya (Retrace) qilish amaliy ko'nikmalarini chuqur o'rgatish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- `proguard-rules.pro` faylining tuzilishi va `-keep`, `-keepclassmembers`, `-dontwarn` direktivalarining sintaksisini bilish;
- Refleksiya (Reflection) nima ekanini va nima sababdan R8 ma'lumotlar modeli (DTO / Data class) o'zgaruvchilarini o'chirib yuborishi yoki chalkashtirishi oqibatida ilova qulashini (Crash) tushunish;
- `@Keep` annotatsiyasi (`androidx.annotation.Keep`) orqali klasslar va maydonlarni R8 ta'siridan himoyalashni amalda qo'llay olish;
- `app/build/outputs/mapping/release/mapping.txt` faylining ahamiyatini, har bir versiya uchun uni saqlash qoidasini hamda chalkash stacktrace'larni o'qish (deobfuscation / retrace) mexanizmini bilish;
- Resurslarni tozalashda dinamik yuklanadigan aktivlarni saqlab qolish uchun `res/raw/keep.xml` faylini to'g'ri sozlay olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Android Studio (so'nggi barqaror versiya);
- Android SDK va emulator yoki haqiqiy Android qurilma;
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan mavzuni takrorlash | R8 va ProGuard farqlari, shrinking, optimization va obfuscation bosqichlari bo'yicha savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | ProGuard qoidalari sintaksisi, Reflection muammosi, `@Keep` annotatsiyasi va `mapping.txt` tahlili |
| **30–55 min** | Amaliy mashg'ulot (Kod yozish) | `proguard-rules.pro` ni sozlash, Gson modelini himoyalash va release build xatolarini to'g'rilash |
| **55–75 min** | Mustaqil amaliy topshiriqlar | Stacktrace deobfuskatsiyasi, `mapping.txt` orqali xatolik ildizini aniqlash |
| **75–80 min** | Xulosa va baholash | Tezkor savol-javob, yakuniy xulosalar va uyga vazifa berish |

---

## Nazariy qism (Batafsil tushuntirish)

### 1. Refleksiya muammosi nima va nima sababdan Release ilova qulaydi?

Oldingi darsda ko'rganimizdek, R8 **Tree Shaking (Daraxt silkitish)** algoritmi asosida ishlaydi. Ilovaning kirish nuqtasidan (odatda `MainActivity`) boshlab, to'g'ridan-to'g'ri chaqirilmagan barcha klasslar, metodlar va o'zgaruvchilar ortiqcha deb hisoblanadi hamda olib tashlanadi yoki nomlari bir harfli belgilarga (`a`, `b`, `c`) almashtiriladi.

Biroq ko'plab zamonaviy Android kutubxonalari — **Gson**, **Moshi**, **Retrofit**, **Room** — ma'lumotlarni o'qishda **Refleksiya (Reflection)** texnologiyasidan foydalanadi. Refleksiya obyekt maydonlariga to'g'ridan-to'g'ri kod orqali emas, balki ularning matnli nomlari (String) orqali kiradi.

Misol uchun, quyidagi DTO modelini olaylik:

```kotlin
data class UserProfile(
    val id: Long,
    val username: String,
    val emailAddress: String
)
```

Serverdan kelayotgan JSON quyidagicha:
```json
{
  "id": 101,
  "username": "coder_uz",
  "emailAddress": "dev@xorazmiy.uz"
}
```

Agar R8 optimallashtirishida ushbu klass himoyalanmasa:
1. R8 `username` va `emailAddress` maydonlarini kodda to'g'ridan-to'g'ri chaqirilmagan deb hisoblab, o'chirib tashlaydi yoki `a`, `b` ga o'zgartiradi.
2. Natijada Gson JSON'dagi `"emailAddress"` kalitini klass ichidagi `b` maydoni bilan bog'lay olmaydi.
3. Ob'yekt yaratilganda maydon `null` bo'lib qoladi yoki ilova `NullPointerException` berib, ochilishi bilanoq qulaydi (Crash).

---

### 2. `proguard-rules.pro` sintaksisi va direktivalari

Ushbu muammoni bartaraf etish uchun `app/proguard-rules.pro` faylida R8 ga aniq ko'rsatmalar beriladi.

#### Asosiy direktivalar:

1. **`-keep`**: Ko'rsatilgan klasslar va ularning a'zolarini shrinking hamda obfuskatsiyadan to'liq saqlab qoladi:
```proguard
# Butun paketdagi barcha klasslarni va ularning barcha a'zolarini saqlash
-keep class com.xorazmiy.app.data.model.** { *; }
```

2. **`-keepclassmembers`**: Klass nomini obfuskatsiya qilishga ruxsat beradi, lekin uning ichidagi maydonlar va metodlarni asl holida saqlaydi:
```proguard
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}
```

3. **`-keepattributes`**: Metadata va maxsus atributlarni saqlash (masalan, Generic turlari va annotatsiyalar):
```proguard
-keepattributes Signature
-keepattributes *Annotation*
-keepattributes InnerClasses, EnclosingMethod
```

4. **`-dontwarn`**: Tashqi kutubxonalarda mavjud bo'lgan, lekin bizning loyihamizga ta'sir qilmaydigan noo'rin kompilyatsiya ogohlantirishlarini bostirish:
```proguard
-dontwarn okio.**
-dontwarn retrofit2.**
```

---

### 3. `@Keep` annotatsiyasi (`androidx.annotation.Keep`)

Har safar `proguard-rules.pro` fayliga klass nomlarini to'liq paket yo'li bilan yozish noqulay va xatoliklarga moyil. AndroidX kutubxonasi qulay muqobil taqdim etadi — `@Keep` annotatsiyasi.

```kotlin
import androidx.annotation.Keep

@Keep
data class PaymentTransaction(
    val transactionId: String,
    val amount: Double,
    val currency: String
)
```

R8 ushbu annotatsiyani ko'rgach, avtomatik ravishda ushbu klassni va uning a'zolarini saqlab qoladi.

---

### 4. `mapping.txt` fayli va Retrace (Deobfuskatsiya)

Release APK'da obfuskatsiya ishlaganda, klass va funksiya nomlari chalkashadi. Firebase Crashlytics yoki foydalanuvchi loglarida quyidagicha xatolik paydo bo'ladi:

```text
java.lang.NullPointerException: Attempt to invoke virtual method 'void c.a.b.d.a()' on a null object reference
    at com.xorazmiy.app.ui.b.c(SourceFile:12)
    at com.xorazmiy.app.ui.MainActivity.onCreate(SourceFile:45)
```

Bu yerda `c.a.b.d.a()` qaysi klass va metod ekanini bilish uchun R8 yaratgan **xarita (mapping)** kerak bo'ladi.

- **Joylashuvi:** `app/build/outputs/mapping/release/mapping.txt`
- **Tuzilishi:** Asl klass nomlari va ularga moslashtirilgan qisqa nomlar lug'ati saqlanadi. Masalan:
  ```text
  com.xorazmiy.app.data.network.AuthService -> c.a.b.d:
      void loginUser(java.lang.String) -> a
  ```
- **Retrace vositasi:** Android SDK ichidagi `retrace` CLI dasturi yoki Google Play Console / Firebase Crashlytics tizimi ushbu faylni qabul qilib, xatolikni tushunarli holatga keltiradi:
  ```text
  java.lang.NullPointerException: Attempt to invoke virtual method 'void AuthService.loginUser(String)'
      at com.xorazmiy.app.ui.login.LoginViewModel.authenticate(LoginViewModel.kt:34)
  ```

> **Oltin qoida:** Har bir Google Play'ga chiqarilgan APK yoki AAB versiyasining `mapping.txt` fayli arxivlab saqlanishi shart! Agar bu fayl yo'qolsa, release foydalanuvchilaridagi crash sababini aniqlashning iloji bo'lmaydi.

---

### 5. Resurslarni saqlab qolish: `keep.xml`

Agar ilovada `shrinkResources true` yoqilgan bo'lsa va kodda rasmlar nomi dinamik yig'ilsa (`resources.getIdentifier("avatar_" + id, "drawable", packageName)`), R8 bu rasmlarni "ishlatilmagan" deb o'chirib yuborishi mumkin.

Buning oldini olish uchun `res/raw/keep.xml` fayli yaratiladi:
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools"
    tools:keep="@drawable/avatar_*,@raw/sound_*"
    tools:shrinkMode="strict" />
```

---

## Amaliy topshiriqlar (Sinfda bajarish uchun)

### 1-topshiriq: Gson DTO klasslarini ProGuard qoidalari orqali himoyalash

**Vazifa:** Loyihada quyidagi model klassi mavjud:
`com.xorazmiy.app.models.WeatherData`
Ushbu klass va kelgusida shu paket ostida ochiladigan barcha DTO modellari R8 tomonidan obfuskatsiya qilinmasligi uchun `proguard-rules.pro` ga mos qoidalarni yozing. Shuningdek, `@SerializedName` annotatsiyasiga ega maydonlarni saqlash qoidasini ham kiriting.

**Yechim:**
`app/proguard-rules.pro` fayliga quyidagi qoidalar yoziladi:
```proguard
# 1. Barcha modellar paketidagi klasslar va ularning maydonlarini saqlash
-keep class com.xorazmiy.app.models.** { *; }

# 2. SerializedName annotatsiyasi bilan belgilangan barcha maydonlarni saqlash
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}

# 3. Gson kutubxonasining o'zini to'g'ri ishlashi uchun zarur qoidalar
-keepattributes *Annotation*
-keepattributes Signature
```

---

### 2-topshiriq: Release build va Crashlytics logini deobfuskatsiya qilish

**Vazifa:** O'quvchiga quyidagi obfuskatsiya qilingan stacktrace taqdim etiladi:
```text
FATAL EXCEPTION: main
java.lang.ClassCastException: a.b.c cannot be cast to com.xorazmiy.app.models.WeatherData
    at com.xorazmiy.app.ui.b.a(SourceFile:28)
```
Berilgan `mapping.txt` parchasidan foydalanib, xato qaysi klass va metodda yuz berganini aniqlang:
```text
com.xorazmiy.app.ui.WeatherPresenter -> com.xorazmiy.app.ui.b:
    void renderWeather(com.xorazmiy.app.models.WeatherData) -> a
    void showError(java.lang.String) -> b
com.xorazmiy.app.network.WeatherResponse -> a.b.c:
    java.lang.String city -> a
```

**Yechim:**
1. `a.b.c` qaysi klassga tegishli ekanini qidiramiz: `mapping.txt` da `com.xorazmiy.app.network.WeatherResponse -> a.b.c`. Demak, `WeatherResponse` obyektini `WeatherData` ga to'g'ridan-to'g'ri cast qilishga urinish bo'lgan.
2. `com.xorazmiy.app.ui.b.a(SourceFile:28)` qatorini tekshiramiz: `com.xorazmiy.app.ui.WeatherPresenter` klassidagi `renderWeather` metodining 28-qatorida xatolik sodir bo'lgan.
3. Deobfuskatsiya qilingan haqiqiy stacktrace:
```text
FATAL EXCEPTION: main
java.lang.ClassCastException: com.xorazmiy.app.network.WeatherResponse cannot be cast to com.xorazmiy.app.models.WeatherData
    at com.xorazmiy.app.ui.WeatherPresenter.renderWeather(WeatherPresenter.kt:28)
```

---

### 3-topshiriq: `@Keep` annotatsiyasi yordamida modelni himoyalash va `build.gradle.kts` ni sozlash

**Vazifa:** `build.gradle.kts` faylida `release` build tipi uchun R8 optimallashtirish va resurs qisqartirishni yoqing hamda `androidx.annotation` orqali `CryptoCurrency` nomli data classni himoyalang.

**Yechim:**
1. `app/build.gradle.kts`:
```kotlin
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
}

android {
    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}

dependencies {
    implementation("androidx.annotation:annotation:1.7.1")
}
```

2. `CryptoCurrency.kt`:
```kotlin
package com.xorazmiy.app.models

import androidx.annotation.Keep

@Keep
data class CryptoCurrency(
    val symbol: String,
    val priceUsd: Double,
    val marketCap: Long
)
```

---

## Tezkor savol-javob (Quick Check)

1. **Savol:** Nima sababdan Release APK'da JSON parsing vaqtida `NullPointerException` yuzaga keladi?  
   **Javob:** Chunki R8 Tree Shaking vaqtida data class maydonlarini foydalanilmagan deb o'ylab o'chiradi yoki nomini `a, b` ga almashtiradi. Natijada Refleksiya kutubxonasi JSON kalitlarini maydonlar bilan bog'lay olmaydi.

2. **Savol:** `-keep` va `-keepclassmembers` qoidalari o'rtasidagi farq nima?  
   **Javob:** `-keep` ham klass nomini, ham uning a'zolarini o'zgarishsiz saqlaydi. `-keepclassmembers` esa klass nomini obfuskatsiya qilishga ruxsat beradi, lekin uning ichidagi belgilangan a'zolarini (maydonlar va metodlar) saqlaydi.

3. **Savol:** `mapping.txt` fayli qayerda saqlanadi va uning asosiy vazifasi nima?  
   **Javob:** U `app/build/outputs/mapping/release/mapping.txt` da joylashadi. Uning vazifasi — chalkashtirilgan klass va metod nomlarining asl nomlari bilan moslik xaritasini saqlash va stacktrace'larni deobfuskatsiya qilishdir.

4. **Savol:** `@Keep` annotatsiyasining `proguard-rules.pro` ga qoidalar yozishdan qanday afzalligi bor?  
   **Javob:** `@Keep` to'g'ridan-to'g'ri kodda yoziladi, klass nomini yoki paketini o'zgartirganda ProGuard faylini yangilab o'tirish talab etilmaydi va refaktoring vaqtida xatolik ehtimoli kamayadi.

5. **Savol:** `shrinkResources true` dinamik chaqiriladigan rasmlarni o'chirib yubormasligi uchun qaysi fayl ishlatiladi?  
   **Javob:** `res/raw/keep.xml` faylida `tools:keep` atributi orqali kerakli resurs patternlari belgilab qo'yiladi.

---

## Uyga vazifa

1. O'zingiz yaratgan yoki mavjud Android loyihangizda `release` rejimida `isMinifyEnabled = true` va `isShrinkResources = true` ni yoqing.
2. Kamida 2 ta data class yarating: bittasiga `@Keep` annotatsiyasini qo'llang, ikkinchisini esa `proguard-rules.pro` dagi `-keep` qoidasi orqali himoyalang.
3. Loyihani Release rejimida build qiling (`./gradlew assembleRelease`) va hosil bo'lgan `mapping.txt` faylini ochib, o'z klasslaringiz qanday o'zgarganini tahlil qiling.
