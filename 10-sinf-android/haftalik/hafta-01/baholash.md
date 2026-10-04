# 10-sinf (Advanced Android): 1-hafta baholash qaydnomasi

**Mavzular:**
1. Gradle konfiguratsiyasi va build tizimi asoslari: `settings.gradle`, `build.gradle`, `compileSdk`, `minSdk`, `targetSdk`, `versionCode`
2. Build variantlari va Product Flavors: Debug vs Release, ProGuard/R8, `flavorDimensions`, Free vs Paid, `BuildConfig`
3. Dependency management va versiyalar bilan ishlash: Repozitoriylar, `implementation` vs `api`, Version Catalog (`libs.versions.toml`)

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Gradle & SDK Parametrlari** | `settings.gradle` va `build.gradle` arxitekturasi, SDK darajalari (compile/min/target), `versionCode` yangilanish qoidalari va Gradle lifecycle | 30 ball |
| **Build Types & Flavors** | Debug vs Release, R8 optimallashtirish, `productFlavors` (Free vs Pro), `applicationIdSuffix` va `buildConfigField` orqali kodni boshqarish | 35 ball |
| **Dependency & Version Catalog** | `implementation` vs `api` farqi, `gradle/libs.versions.toml` ning 4 ta bloki, kutubxonalar to'plami (`[bundles]`) va xatosiz Gradle Sync | 35 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Gradle & SDK (30) | Flavors & Build (35) | Dependencies & TOML (35) | Jami ball (100) | Izoh |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

---

## Mentor qaydlari va tahlil

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar ko'pincha `build.gradle` fayliga yangi qator kiritgandan so'ng "Sync Now" qilishni unutishadi va kod yozish paytida kutubxona topilmadi degan qizil xatoliklarga duch kelishadi. Har bir o'zgarishdan keyin sinxronizatsiya intizomini shakllantirish zarur.
- **Flavors tushunchasi:** O'quvchilar boshida Free va Pro ilovalarni alohida ikki xil loyiha deb o'ylashadi. Ularga bitta kod bazasidan bir necha daqiqada ikki xil ilova hosil qilish mumkinligini Android Studio'dagi "Build Variants" paneli orqali jonli ko'rsatib berish tavsiya etiladi.
