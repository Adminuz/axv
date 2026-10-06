# 15-dars. Gradle yordamida kutubxonalarni ulash va versiyalarni boshqarish

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 5-hafta, 3-dars (umumiy 15-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (Dependency management va versiyalar bo'limi), `oquv-dasturi.txt`, `uslubiy-korsatma.txt`

---

## Darsning maqsadi

`dependencies {}` bloki orqali kutubxonalarni ulashni, versiya raqami (`major.minor.patch`, alpha, beta, stable) ma'nosini, version catalog (`libs.versions.toml`) bilan versiyalarni markaziy boshqarishni, ziddiyatlarni `force` va transitive bog'liqlikni `exclude` bilan hal qilishni tushuntirish.

## Kutilayotgan natijalar

- Kutubxonani `implementation("guruh:nom:versiya")` bilan ulaydi;
- Versiya raqamining (stable, beta, alpha) ma'nosini tushuntiradi;
- `libs.versions.toml` bilan versiyalarni markaziy boshqaradi;
- Versiya ziddiyatini `force` va keraksiz bog'liqlikni `exclude` bilan hal qiladi.

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 14-dars: debug, release, `buildConfigField`, flavor |
| 08–25 | Yangi mavzu 1 | `dependencies {}` va kutubxona ulash |
| 25–38 | Yangi mavzu 2 | Versiya raqamlari va ziddiyatlar: `force`, transitive, `exclude` |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | Version catalog: `libs.versions.toml` |
| 58–75 | Amaliyot | Retrofit va Coil ni ulash, katalogga ko'chirish |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. `dependencies {}` va kutubxona ulash

Ko'p funksiya tashqi kutubxonalar bilan qo'shiladi: Retrofit — tarmoq so'rovlari, Room — ma'lumotlar bazasi, Coil — rasm yuklash. Kutubxona module-level `build.gradle` dagi `dependencies {}` blokiga `implementation("guruh:nom:versiya")` shaklida yoziladi. Gradle uni internetdagi omborlardan (`google()`, `mavenCentral()`) yuklab, loyihaga biriktiradi. Yozgandan keyin `Sync Now` bosiladi.

```kotlin
dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.9.0")
    implementation("io.coil-kt:coil-compose:2.3.0")
}

// settings.gradle.kts
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
    }
}
```

Qator tuzilishi: `guruh:nom:versiya`. Versiya yozilmasa yoki noto'g'ri yozilsa, build to'xtaydi.

### 2. Versiya raqamlari va ziddiyatlar

Versiya raqami (masalan, `2.9.0`, `1.0.0-beta03`, `0.28.1-alpha`) kutubxona qaysi bosqichda ekanini bildiradi: `alpha` va `beta` hali to'liq sinalmagan, stable (qo'shimchasiz) nashrga tayyor. Kutubxonalar bir-biriga bog'liq: Retrofit ichida OkHttp ni olib keladi (transitive dependency). Ziddiyat bo'lsa, Gradle eng yuqori versiyani tanlaydi; aniq versiya kerak bo'lsa `force(...)`, keraksiz bog'liqlikni olib tashlash uchun `exclude(...)` ishlatiladi.

```kotlin
configurations.all {
    resolutionStrategy {
        force("com.squareup.okhttp3:okhttp:4.9.3")
    }
}

dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.9.0") {
        exclude(group = "org.example", module = "unused-module")
    }
}
```

`force` ni ehtiyotkorlik bilan ishlating: majburiy versiya boshqa kutubxonani buzishi mumkin. `exclude` loyiha hajmini kamaytiradi.

### 3. Version catalog: `libs.versions.toml`

Katta loyihada har kutubxona versiyasini alohida yozish noqulay. Version catalog barcha versiyalarni bitta `gradle/libs.versions.toml` faylida saqlaydi: `[versions]` (versiya raqamlari) va `[libraries]` (kutubxonalar). Keyin `dependencies` da faqat `implementation(libs.retrofit)` yoziladi. Versiyani yangilash uchun bitta joyni o'zgartirish yetadi. Alohida eslatma: `minSdk`, `targetSdk` va `compileSdk` ham versiyadir; `compileSdk` ni so'nggi barqaror versiyada tutish tavsiya qilinadi.

```toml
[versions]
retrofit = "2.9.0"
coil = "2.3.0"

[libraries]
retrofit = { module = "com.squareup.retrofit2:retrofit", version.ref = "retrofit" }
coil-compose = { module = "io.coil-kt:coil-compose", version.ref = "coil" }

# app/build.gradle.kts
# implementation(libs.retrofit)
# implementation(libs.coil.compose)
```

Katalogdagi `coil-compose` nomi kodda `libs.coil.compose` bo'lib yoziladi (defis nuqtaga aylanadi).

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Retrofit ulash

Module-level faylga Retrofit 2.9.0 ni ulang.

**Yechim:**
```kotlin
dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.9.0")
}
```

### 2-topshiriq (o'rta). Versiya ma'nosi

`2.9.0`, `1.0.0-beta03`, `0.28.1-alpha` versiyalarining qaysi birini nashr uchun tanlaysiz va nega?

**Yechim:** `2.9.0` — stable, nashrga tayyor; beta va alpha hali to'liq sinovdan o'tmagan bo'lishi mumkin.

### 3-topshiriq (o'rta). Katalog yozish

Retrofit va Coil ni `libs.versions.toml` ga ko'chiring va `dependencies` da `libs...` bilan ishlating.

**Yechim:**
```kotlin
[versions]
retrofit = "2.9.0"
coil = "2.3.0"

[libraries]
retrofit = { module = "com.squareup.retrofit2:retrofit", version.ref = "retrofit" }
coil-compose = { module = "io.coil-kt:coil-compose", version.ref = "coil" }

# build.gradle.kts:
# implementation(libs.retrofit)
# implementation(libs.coil.compose)
```

### 4-topshiriq (qiyin). OkHttp ziddiyati

Retrofit bilan kelgan OkHttp versiyasini 4.9.3 ga majburlang.

**Yechim:**
```kotlin
configurations.all {
    resolutionStrategy {
        force("com.squareup.okhttp3:okhttp:4.9.3")
    }
}
```

### 5-topshiriq (qiyin). Transitive ni olib tashlash

Retrofit dan `org.example:unused-module` bog'liqligini chiqarib tashlang.

**Yechim:**
```kotlin
implementation("com.squareup.retrofit2:retrofit:2.9.0") {
    exclude(group = "org.example", module = "unused-module")
}
```

---

## Tezkor nazorat

1. Kutubxona qaysi blokda ulanadi? **Javob:** Module-level `build.gradle` dagi `dependencies {}` blokida.
2. `implementation("a:b:1.0")` da `a`, `b`, `1.0` nima? **Javob:** Guruh, nom va versiya.
3. Alpha va beta qanday versiya? **Javob:** Hali to'liq sinovdan o'tmagan, barqaror emas.
4. Version catalog nima beradi? **Javob:** Barcha versiyalarni bitta faylda markaziy boshqarish.
5. `exclude` nima qiladi? **Javob:** Keraksiz transitive bog'liqlikni olib tashlaydi.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
