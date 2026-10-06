# 13-dars. build.gradle faylining asosiy tuzilmasi va modullararo bog'lanishi

> Run tugmasi bosilganda yuzlab jarayon ishga tushadi: bularning hammasini Gradle boshqaradi. Bugun uning fayllarini o'qishni o'rganamiz.

## Dars xulosasi

- **Gradle** — Android ilovasini quruvchi tizim; kod, resurs va kutubxonalarni APK/AAB ga aylantiradi.
- **`settings.gradle`** — modullar ro'yxati; **project-level** — umumiy sozlamalar; **module-level** — modulning o'z sozlamalari.
- **`android {}`** — `compileSdk`, `defaultConfig` (`applicationId`, `minSdk`, `targetSdk`, `versionCode`, `versionName`).
- **Modul ulash:** `include(":core")` + `implementation(project(":core"))`.
- **`Sync Now`** — o'zgarishdan keyin Gradle ni qayta sinxronlash.

## Qo'shimcha ma'lumot

### Nega Gradle dvigatel deyiladi?
Siz kod yozasiz va dizayn yaratasiz, lekin ular o'z-o'zidan ilovaga aylanmaydi. Gradle har bir bo'lakni o'z joyiga qo'yadi: resurslarni tarqatadi, kutubxonalarni yuklaydi, kodni kompilyatsiya qilib, bitta ilovaga biriktiradi.

### Groovy va Kotlin DSL
`build.gradle` (Groovy) va `build.gradle.kts` (Kotlin) bir xil ishni bajaradi. Kotlin DSL da qiymatlar `=` bilan beriladi va qatorlar qavs bilan chaqiriladi: `implementation("...")`.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Gradle | Android ilovasini quruvchi build tizimi |
| settings.gradle | Loyiha modullari ro'yxati fayli |
| Module (modul) | Loyihaning mustaqil qismi: `app`, `core` |
| compileSdk | Kompilyatsiya uchun ishlatiladigan SDK versiyasi |
| minSdk | Ilova ishlaydigan eng past Android versiyasi |
| targetSdk | Ilova moslashtirilgan Android versiyasi |
| versionCode | Ichki butun versiya raqami |
| Sync | Gradle fayllarini qayta o'qib, loyihani yangilash |

## Bilasizmi?

- Gradle nomi inglizcha «gradle» (beshik) so'zidan emas, loyiha asoschilari tomonidan tanlangan.
- Bitta Android loyihasida yuzlab modul bo'lishi mumkin — katta kompaniyalar shunday ishlaydi.
- `Run` bosilganda Android Studio pastida ko'rinadigan loglar Gradle ning ish bosqichlaridir.

## Topshiriqlar

### 1. Fayllarni sanang · oson

Loyihangizdagi barcha `.gradle` yoki `.gradle.kts` fayllarini ro'yxat qiling.

**Kutiladigan natija:** 3 ta asosiy fayl topildi.

### 2. applicationId · oson

Loyihangizning `applicationId` qiymatini toping va yozing.

**Kutiladigan natija:** Aniq qiymat (masalan, `com.example...`).

### 3. SDK qiymatlari · oson

`compileSdk`, `minSdk`, `targetSdk` qiymatlarini yozib oling.

**Kutiladigan natija:** 3 ta qiymat.

### 4. Versiya · oson

`versionCode` va `versionName` farqini 2 jumlada yozing.

**Kutiladigan natija:** Ichki raqam va ko'rinadigan nom farqi.

### 5. Plaginlar · o'rta

`plugins {}` blokida qaysi plaginlar bor? Har birining vazifasini yozing.

**Kutiladigan natija:** Kamida 2 ta plagin izohlangan.

### 6. defaultConfig o'zgartirish · o'rta

`versionName` ni `1.1` ga, `versionCode` ni 2 ga o'zgartiring va Sync qiling.

**Kutiladigan natija:** Sync muvaffaqiyatli.

### 7. Modul yaratish · o'rta

`core` Android Library modulini yarating.

**Kutiladigan natija:** Loyihada `core` papkasi paydo bo'ladi.

### 8. Natijani bashorat qiling · o'rta

`minSdk = 30` bo'lsa, Android 9 (API 28) telefoniga ilova o'rnatiladimi?

**Kutiladigan natija:** Yo'q: `minSdk` dan past versiya.

### 9. settings va include · qiyin

`core` modulini `settings.gradle.kts` ga qo'shing va nima bo'lishini kuzating.

**Kutiladigan natija:** `include(":core")` yozilgan.

### 10. Ulash · qiyin

`app` da `implementation(project(":core"))` yozing va `core` ga bitta funksiya qo'shib, uni `app` dan chaqiring.

**Kutiladigan natija:** Funksiya `app` dan ishlaydi.

### 11. Tsikl xatosi · qiyin

`core` ga ham `implementation(project(":app"))` qo'shsangiz nima bo'ladi? Sinab ko'ring.

**Kutiladigan natija:** Gradle tsiklik bog'lanish xatosini beradi.

### 12. Modul sxemasi · bonus

Do'kon ilovasi uchun `app`, `core`, `data`, `feature-cart` modullari sxemasini va ularning bog'lanishlarini chizing.

**Kutiladigan natija:** Bog'lanishlar bir yo'nalishli, tsiklsiz.

## O'zingizni tekshiring

1. Gradle nima va nima uchun kerak?
2. `settings.gradle` va module-level `build.gradle` farqi nima?
3. `minSdk`, `targetSdk`, `compileSdk` nimani bildiradi?
4. `versionCode` va `versionName` farqi nima?
5. Yangi modul qanday e'lon qilinadi?
6. `implementation(project(...))` nima qiladi?
7. `Sync Now` qachon bosiladi?

## Uyga vazifa

Loyiha fayllarini tahlil qiling va `core` modulini qo'shing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
