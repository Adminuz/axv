# 5-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 13-dars: build.gradle tuzilmasi va modullar

1. O'z Android loyihangizdagi `settings.gradle`, project-level va module-level fayllarni ochib, har birining 3 ta asosiy qatorini daftarga yozing va izohlang.
2. `defaultConfig` dagi `applicationId`, `minSdk`, `targetSdk`, `versionCode`, `versionName` qiymatlarini yozib, har birining vazifasini bir jumlada tushuntiring.
3. Loyihaga `core` kutubxona modulini qo'shing va `app` ga ulang; Sync muvaffaqiyatli o'tganini skrinshot qiling.

---

## 14-dars: Build variantlar: debug va release

1. O'z loyihangizda `debug` ga `applicationIdSuffix = ".debug"`, `release` ga `isMinifyEnabled = true` qo'shing va Sync qiling.
2. `buildConfigField` yordamida `BASE_URL` ni debug va release uchun turlicha bering; Kotlin kodida `Log.d` bilan qiymatni chiqaring va Logcat skrinshotini oling.
3. `free` va `paid` flavorlarini qo'shing; Build Variants oynasida 4 ta variantni ko'rsatadigan skrinshot oling.

---

## 15-dars: Kutubxonalar va versiyalar

1. O'z loyihangizga Retrofit (`2.9.0`) va Coil (`2.3.0`) ni ulang va Sync muvaffaqiyatli o'tganini skrinshot qiling.
2. Ikkala kutubxonani `gradle/libs.versions.toml` ga ko'chiring va `dependencies` da `libs...` yozuvidan foydalaning.
3. Kutubxona versiyasini ataylab noto'g'ri yozib (masalan, `2.9.99`), Gradle xatosini ko'ring va xatoning sababini bir jumlada yozing.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **13-dars vazifasi (35 ball):** fayllar vazifasining to'g'ri izohi, `defaultConfig` qiymatlarini tushunish, `core` modulining to'g'ri ulanishi va muvaffaqiyatli Sync.
- **14-dars vazifasi (30 ball):** `debug` va `release` sozlamalari, `BASE_URL` ning variantga mos chiqishi, flavor va 4 ta variant.
- **15-dars vazifasi (35 ball):** kutubxonalarning to'g'ri ulanishi, `libs.versions.toml` ga ko'chirish, xato logini to'g'ri izohlash.

### Eslatma
- Gradle faylini o'zgartirgach `Sync Now` bosilganini tekshiring.
- Versiya raqamidagi harf va nuqtalarga e'tibor bering (`2.9.0`).
- Agar loyihada Groovy (`.gradle`) ishlatilsa, Kotlin DSL (`.kts`) yozuvini moslab qabul qiling.
