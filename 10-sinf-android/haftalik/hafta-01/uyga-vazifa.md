# 1-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 1-dars: Gradle konfiguratsiyasi va build tizimi asoslari

1. Android Studio'da yangi bo'sh loyiha yarating va `app/build.gradle` (yoki `.kts`) faylidagi quyidagi parametrlarni o'zgartiring:
   - `minSdk` qiymatini 24 qilib belgilang;
   - `targetSdk` va `compileSdk` qiymatlarini 34 qilib o'rnating;
   - `versionCode`ni 1, `versionName`ni esa `"1.0.0-alpha"` deb belgilang.
2. "Sync Now" tugmasini bosing va loyihani sinxronizatsiya qiling.
3. Terminal ochib, `./gradlew tasks` buyrug'ini ishga tushiring va ekranda chiqqan asosiy task guruhlaridan (masalan, `Build tasks`, `Verification tasks`) 3 tasini daftaringizga yozib qo'ying.

---

## 2-dars: Build variantlari va Product Flavors

1. O'zingiz yaratgan loyihaning `build.gradle` fayliga `productFlavors` blokini qo'shing:
   - `flavorDimensions "edition"` deb o'lchov guruhini e'lon qiling;
   - `free` flavorni yarating: `applicationIdSuffix ".free"` va `buildConfigField "boolean", "IS_PAID", "false"`;
   - `pro` flavorni yarating: `applicationIdSuffix ".pro"` va `buildConfigField "boolean", "IS_PAID", "true"`.
2. Loyihani sinxronizatsiya qilib, Android Studio'ning "Build Variants" panelidan navbatma-navbat `freeDebug` va `proDebug` variantlarini tanlang.
3. `MainActivity.kt` faylida `BuildConfig.IS_PAID` qiymatini tekshiruvchi sodda shart yozing va emulyatorda ishga tushiring.

---

## 3-dars: Dependency management va versiyalar bilan ishlash (Version Catalog)

1. Loyihangizning `gradle/libs.versions.toml` fayliga kiring va quyidagi yangi kutubxona parametrlarini kiriting:
   - `[versions]` bo'limida: `retrofit = "2.9.0"`;
   - `[libraries]` bo'limida: `retrofit-core = { group = "com.squareup.retrofit2", name = "retrofit", version.ref = "retrofit" }` va `retrofit-gson = { group = "com.squareup.retrofit2", name = "converter-gson", version.ref = "retrofit" }`;
   - `[bundles]` bo'limida: `networking = ["retrofit-core", "retrofit-gson"]`.
2. `app/build.gradle` faylining `dependencies` blokida butun to'plamni bitta qatorda ulang:
   - `implementation libs.bundles.networking`
3. "Sync Now" bosib, kutubxonalar muvaffaqiyatli yuklanganiga ishonch hosil qiling.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **1-dars vazifasi (30 ball):** SDK parametrlarining to'g'ri tanlangani, Gradle Wrapper tushunchasi va terminal buyruqlarining amalda bajarilgani.
- **2-dars vazifasi (35 ball):** `flavorDimensions` va `productFlavors` sintaksisi xatosiz yozilgani, `applicationIdSuffix` va `buildConfigField` to'g'ri ishlashi.
- **3-dars vazifasi (35 ball):** Version Catalog (`libs.versions.toml`) strukturasi to'liq shakllantirilgani, `[bundles]` to'g'ri tuzilgani va loyihaning xatosiz sinxronlashgani.

### Eslatma
- O'quvchilar `buildConfigField`da String qiymatlarni ekranlashni (`\"...\"`) unutmasliklari hamda `libs.versions.toml` da chiziqcha (`-`) bilan yozilgan nomlar Gradle faylida nuqta (`.`) bilan chaqirilishini to'g'ri tushunganliklarini tekshiring.
