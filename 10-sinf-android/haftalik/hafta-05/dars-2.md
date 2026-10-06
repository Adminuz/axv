# 14-dars. Build variantlar (debug, release) va ularning farqi

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 5-hafta, 2-dars (umumiy 14-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (Gradle konfiguratsiyasi va build variantlari; ProGuard va R8 bo'limi), `oquv-dasturi.txt`, `uslubiy-korsatma.txt`

---

## Darsning maqsadi

Android loyihada `debug` va `release` build turlarining farqini, `buildTypes {}` blokini, `buildConfigField` bilan har variantga alohida qiymat berishni, R8/ProGuard (`minify`) va `productFlavors` tushunchasini tushuntirish.

## Kutilayotgan natijalar

- `debug` va `release` build turlarini farqlaydi;
- `buildTypes {}` blokini yozadi va `minify` ni yoqadi;
- `buildConfigField` bilan `BASE_URL` ni variant bo'yicha belgilaydi va `BuildConfig` dan o'qiydi;
- `productFlavors` va build variant (flavor + type) tushunchasini ayta oladi.

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 13-dars: Gradle fayllari, `defaultConfig`, modullar |
| 08–25 | Yangi mavzu 1 | Debug va release: nima farq qiladi |
| 25–38 | Yangi mavzu 2 | `buildTypes {}` va `buildConfigField` |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | `productFlavors` va build variantlar (`freeDebug`, `paidRelease`) |
| 58–75 | Amaliyot | Namunaviy loyihada variantlar yaratish va ishga tushirish |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. Debug va Release build turlari

Android loyihada build ikki xil bajariladi. **Debug** dasturchi uchun: xatolar ochiq ko'rinadi, Logcat orqali kuzatiladi, tez yig'iladi, avtomatik debug kaliti bilan imzolanadi. **Release** foydalanuvchi uchun: kod R8 yoki ProGuard bilan optimallashtiriladi (keraksiz qismlar olib tashlanadi, nomlar qisqartiriladi), ilova o'z kaliti bilan imzolanadi va tezroq ishlaydi.

```kotlin
android {
    buildTypes {
        debug {
            applicationIdSuffix = ".debug"
            isDebuggable = true
        }
        release {
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

`isMinifyEnabled = true` bo'lgach R8 ishlaydi. Manba hujjatda Groovy yozuvi `minifyEnabled true`, Kotlin DSL da esa `isMinifyEnabled = true` yoziladi.

### 2. `buildTypes {}` va `buildConfigField`

Har bir build turi uchun alohida konstanta berish mumkin. Masalan, debug da test serveri manzili, release da haqiqiy server. Buning uchun `buildConfigField("tur", "NOM", "qiymat")` yoziladi, Gradle esa `BuildConfig` sinfini yaratadi. Kotlin kodida: `val url = BuildConfig.BASE_URL`. Yangi AGP versiyalarida `buildFeatures { buildConfig = true }` yoqilishi kerak.

```kotlin
android {
    buildFeatures { buildConfig = true }
    buildTypes {
        debug {
            buildConfigField("String", "BASE_URL", "\"https://test.api.com\"")
        }
        release {
            buildConfigField("String", "BASE_URL", "\"https://prod.api.com\"")
            isMinifyEnabled = true
        }
    }
}

// Kotlin kodida
val url = BuildConfig.BASE_URL
```

Qiymat ichidagi tirnoqlar `\"` bilan yoziladi, chunki Gradle uni kod sifatida yaratadi. Debug da test, release da prod manzil chiqadi.

### 3. `productFlavors` va build variantlar

Product flavor — bir kod bazasidan bir nechta versiya (masalan, `free` va `paid`) yaratish imkoniyati. Har bir flavor o'z `applicationIdSuffix`, nomi va resurslariga ega bo'lishi mumkin. Build variant = flavor + build turi: `freeDebug`, `freeRelease`, `paidDebug`, `paidRelease`. Android Studio dagi **Build Variants** oynasida kerakli variant tanlanadi. Flavor yozilganda `flavorDimensions` majburiy.

```kotlin
android {
    flavorDimensions += "tarif"
    productFlavors {
        create("free") {
            dimension = "tarif"
            applicationIdSuffix = ".free"
        }
        create("paid") {
            dimension = "tarif"
            applicationIdSuffix = ".paid"
        }
    }
}
// Variantlar: freeDebug, freeRelease, paidDebug, paidRelease
```

Ikki `flavor` va ikki `build type` — jami 4 variant. Variant tanlash: `View > Tool Windows > Build Variants`.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Farqlar

Debug va release farqini 3 ta xususiyat bo'yicha yozing.

**Yechim:** Debug — dasturchi uchun, xatolar ochiq, optimallashtirishsiz; Release — foydalanuvchi uchun, R8 yoqilgan, o'z kaliti bilan imzolangan.

### 2-topshiriq (o'rta). buildTypes yozish

`debug` ga `applicationIdSuffix = ".debug"`, `release` ga `isMinifyEnabled = true` qo'shing.

**Yechim:**
```kotlin
buildTypes {
    debug {
        applicationIdSuffix = ".debug"
    }
    release {
        isMinifyEnabled = true
    }
}
```

### 3-topshiriq (o'rta). BASE_URL

Debug da `https://test.api.com`, release da `https://prod.api.com` manzillarini `buildConfigField` bilan bering.

**Yechim:**
```kotlin
android {
    buildFeatures { buildConfig = true }
    buildTypes {
        debug {
            buildConfigField("String", "BASE_URL", "\"https://test.api.com\"")
        }
        release {
            buildConfigField("String", "BASE_URL", "\"https://prod.api.com\"")
        }
    }
}
```

### 4-topshiriq (qiyin). Flavor qo'shish

`free` va `paid` flavorlarini yarating. Hosil bo'lgan 4 ta variant nomini yozing.

**Yechim:**
```kotlin
flavorDimensions += "tarif"
productFlavors {
    create("free") { dimension = "tarif" }
    create("paid") { dimension = "tarif" }
}
// freeDebug, freeRelease, paidDebug, paidRelease
```

### 5-topshiriq (qiyin). Xatoni toping

`BuildConfig.BASE_URL` da `Unresolved reference` xatosi chiqdi. 2 ta sababni yozing.

**Yechim:** (1) `buildFeatures { buildConfig = true }` yoqilmagan; (2) `buildConfigField` yozilgan, lekin Gradle `Sync Now` qilinmagan yoki nomi (`BASE_URL`) xato.

---

## Tezkor nazorat

1. Debug va release farqi nima? **Javob:** Debug dasturchi uchun (xatolar ochiq), release foydalanuvchi uchun (optimallashtirilgan, o'z kaliti bilan imzolangan).
2. R8 nima qiladi? **Javob:** Kodni qisqartiradi, keraksiz qismlarni olib tashlaydi va nomlarni qisqartiradi.
3. `buildConfigField` nima uchun kerak? **Javob:** Har variantga alohida konstanta (masalan, `BASE_URL`) berish uchun.
4. Build variant nimadan tashkil topadi? **Javob:** Flavor va build type birikmasidan: `freeDebug`.
5. `applicationIdSuffix` nima qiladi? **Javob:** `applicationId` oxiriga qo'shimcha qo'shadi, shu sababli ikki variant bir telefonga o'rnatiladi.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
