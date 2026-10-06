# 13-dars. build.gradle faylining asosiy tuzilmasi va modullararo bog'lanishi

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 5-hafta, 1-dars (umumiy 13-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (Gradle konfiguratsiyasi va build variantlari bo'limi), `oquv-dasturi.txt` (Gradle fayllarining tuzilmasi), `uslubiy-korsatma.txt`

---

## Darsning maqsadi

Gradle ning Android loyihadagi rolini, `settings.gradle`, project-level va module-level `build.gradle` fayllarining vazifasini, `android {}` va `defaultConfig` sozlamalarini hamda modullar o'rtasidagi bog'lanishni (`include`, `project(":core")`) tushuntirish.

## Kutilayotgan natijalar

- Gradle ning vazifasini (kod, resurs va kutubxonalarni ilovaga aylantirish) tushuntiradi;
- `settings.gradle`, project-level va module-level `build.gradle` farqini ayta oladi;
- `android {}` bloki va `defaultConfig` parametrlarini o'qiydi;
- Yangi modul qo'shib, uni `include` va `implementation(project(...))` bilan bog'laydi.

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 12-dars: CI/CD, pipeline, GitHub Actions |
| 08–25 | Yangi mavzu 1 | Gradle va loyiha fayllari tuzilmasi |
| 25–38 | Yangi mavzu 2 | Module-level `build.gradle`: `plugins`, `android {}`, `defaultConfig` |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | Modullararo bog'lanish: `include`, `project(...)` |
| 58–75 | Amaliyot | Namunaviy loyihada fayllarni tahlil qilish va modul qo'shish |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. Gradle va loyiha fayllari tuzilmasi

Gradle — Android ilovasini quruvchi tizim: u kodni kompilyatsiya qiladi, resurslarni birlashtiradi, kutubxonalarni yuklaydi va natijani APK yoki AAB ga aylantiradi. Konfiguratsiya ikki darajada bo'ladi: butun loyiha uchun `settings.gradle` va project-level `build.gradle`, hamda har bir modul (odatda `app`) uchun module-level `build.gradle`. Birinchisi binoning bosh rejasiga, ikkinchisi har bir qavatning ichki loyihasiga o'xshaydi.

```text
MyApp/
  settings.gradle.kts      <- modullar ro'yxati
  build.gradle.kts         <- project-level
  gradle/libs.versions.toml
  app/
    build.gradle.kts       <- module-level (eng muhim)
    src/main/...
```

Faylning kengaytmasi `.gradle` (Groovy) yoki `.gradle.kts` (Kotlin DSL) bo'lishi mumkin; mazmuni bir xil, sintaksis biroz farq qiladi.

### 2. Module-level `build.gradle`: `plugins`, `android {}`, `defaultConfig`

Module-level fayl `plugins {}` (qaysi turdagi modul: `com.android.application` yoki `com.android.library`), `android {}` (SDK versiyalari, ilova identifikatori), `dependencies {}` (kutubxonalar) bloklaridan iborat. `defaultConfig` ichida: `applicationId` — ilovaning noyob nomi, `minSdk` — eng past Android versiyasi, `targetSdk` — moslashtirilgan versiya, `versionCode` — butun son (har nashrda oshadi), `versionName` — foydalanuvchiga ko'rinadigan versiya. `compileSdk` — kompilyatsiya uchun ishlatiladigan SDK.

```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "com.example.advanced"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.advanced"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }
}
```

`minSdk` ni noto'g'ri tanlash ilovaning eski telefonlarda ishlamasligiga olib keladi. Har nashrda `versionCode` oshirilishi shart.

### 3. Modullararo bog'lanish

Katta loyiha modullarga bo'linadi: `app` (UI), `core` (umumiy kod), `data` va boshqalar. Modul `settings.gradle` da `include(":core")` bilan e'lon qilinadi. Kutubxona moduli `com.android.library` plaginidan foydalanadi. `app` modulida unga `implementation(project(":core"))` bilan ulaniladi; shundan keyin `core` dagi sinflarni `app` ichida ishlatish mumkin. Bog'lanish bir tomonlama bo'lishi kerak (tsiklik bog'lanish xato beradi).

```kotlin
// settings.gradle.kts
include(":app")
include(":core")

// core/build.gradle.kts
plugins {
    id("com.android.library")
    id("org.jetbrains.kotlin.android")
}

// app/build.gradle.kts
dependencies {
    implementation(project(":core"))
}
```

Fayllarni o'zgartirgach Android Studio dagi `Sync Now` tugmasini bosing. `app` -> `core` yo'nalishi to'g'ri, teskarisi (`core` -> `app`) tsikl hosil qiladi.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Atamalar

`settings.gradle`, project-level va module-level `build.gradle` vazifasini bir jumlada yozing.

**Yechim:** `settings.gradle` — modullar ro'yxati; project-level — umumiy plaginlar; module-level — modul SDK, versiya va kutubxonalari.

### 2-topshiriq (o'rta). defaultConfig o'qish

Berilgan `defaultConfig` ni o'qing va `minSdk`, `versionName` qiymatlarini ayting.

**Yechim:**
```kotlin
defaultConfig {
    applicationId = "com.example.shop"
    minSdk = 26
    targetSdk = 34
    versionCode = 3
    versionName = "1.2"
}
// minSdk = 26 (Android 8.0 va yuqori), versionName = "1.2", versionCode = 3
```

### 3-topshiriq (o'rta). Modul qo'shish

`core` kutubxona modulini yarating va `app` ga ulang.

**Yechim:**
```kotlin
// settings.gradle.kts
include(":app", ":core")

// core/build.gradle.kts
plugins { id("com.android.library") }

// app/build.gradle.kts
dependencies { implementation(project(":core")) }
```

### 4-topshiriq (qiyin). Xatoni toping

`app` moduli `core` ni ishlatmoqda, lekin `Unresolved reference` xatosi chiqdi. 2 ta mumkin bo'lgan sababni yozing.

**Yechim:** (1) `settings.gradle` da `include(":core")` unutilgan; (2) `app` da `implementation(project(":core"))` yo'q yoki `Sync Now` bosilmagan.

### 5-topshiriq (qiyin). versionCode siyosati

Ilovaning 1.0 (kod 1), 1.1 va 2.0 versiyalari uchun `versionCode` va `versionName` ni yozing.

**Yechim:**
```kotlin
// 1.0
versionCode = 1; versionName = "1.0"
// 1.1
versionCode = 2; versionName = "1.1"
// 2.0
versionCode = 3; versionName = "2.0"
```

---

## Tezkor nazorat

1. Gradle nima? **Javob:** Android ilovasini quruvchi tizim: kod, resurs va kutubxonalarni APK/AAB ga aylantiradi.
2. Qaysi fayl modullar ro'yxatini saqlaydi? **Javob:** `settings.gradle(.kts)`.
3. `minSdk` va `targetSdk` farqi? **Javob:** `minSdk` — eng past versiya, `targetSdk` — moslashtirilgan versiya.
4. `versionCode` nima uchun kerak? **Javob:** Har nashrni ajratish uchun butun son; har nashrda oshiriladi.
5. Moduldan modulga qanday ulanadi? **Javob:** `implementation(project(":core"))` bilan.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
