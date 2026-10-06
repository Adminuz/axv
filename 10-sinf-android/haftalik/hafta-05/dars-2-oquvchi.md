# 14-dars. Build variantlar (debug, release) va ularning farqi

> Do'stingizga bergan sinov APK va Play Market dagi nashr bir xil emas. Bugun debug va release farqini, variantlarni qanday yaratishni o'rganamiz.

## Dars xulosasi

- **Debug** — dasturchi uchun; xatolar ochiq, tez yig'iladi, debug kaliti.
- **Release** — foydalanuvchi uchun; R8 (`isMinifyEnabled = true`), o'z kaliti bilan imzolanadi.
- **`buildConfigField`** — har variantga alohida konstanta; kodda `BuildConfig.BASE_URL`.
- **`productFlavors`** — `free`/`paid` kabi versiyalar; `flavorDimensions` majburiy.
- **Build variant** = flavor + build type (`freeDebug`, `paidRelease`).

## Qo'shimcha ma'lumot

### R8 va ProGuard
R8 — Android Studio dagi standart vosita: kodni qisqartiradi (shrink), nomlarni qisqartiradi (obfuscate) va optimallashtiradi. Qoidalar `proguard-rules.pro` faylida yoziladi, masalan: `-keep class com.example.model.** { *; }`.

### Nega release ni alohida sinash kerak?
R8 ba'zan kerakli sinflarni olib tashlashi mumkin; shuning uchun release build ni nashrdan oldin real telefonda sinab ko'ring.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Build type | Build turi: debug, release |
| Debug | Ishlab chiqish rejimi |
| Release | Nashr rejimi |
| R8 / ProGuard | Kodni qisqartirish va optimallashtirish vositasi |
| BuildConfig | Gradle yaratadigan konstantalar sinfi |
| Product flavor | Ilovaning versiyasi (free, paid) |
| Build variant | Flavor va build type birikmasi |
| Keystore | Release ilovani imzolash kaliti |

## Bilasizmi?

- Debug APK ni ham, release APK ni ham bir telefonga o'rnatish mumkin, agar `applicationIdSuffix` berilgan bo'lsa.
- Release build odatda debug nikidan sezilarli kichik va tezroq bo'ladi.
- Katta kompaniyalar `dev`, `staging`, `prod` flavorlaridan foydalanadi.

## Topshiriqlar

### 1. Debug sifatlari · oson

Debug build ning 3 ta xususiyatini yozing.

**Kutiladigan natija:** 3 ta to'g'ri xususiyat.

### 2. Release sifatlari · oson

Release build ning 3 ta xususiyatini yozing.

**Kutiladigan natija:** 3 ta to'g'ri xususiyat.

### 3. buildTypes toping · oson

Loyihangizdagi `buildTypes {}` blokini toping va ichidagi turlarni yozing.

**Kutiladigan natija:** Mavjud turlar (`debug`, `release`) ro'yxati.

### 4. Variantlar oynasi · oson

Android Studio da Build Variants oynasini oching va variantni tanlang.

**Kutiladigan natija:** Skrinshotda tanlangan variant.

### 5. applicationIdSuffix · o'rta

`debug` ga `.debug` qo'shing. Ikkala build bitta telefonga o'rnatilishini tekshiring.

**Kutiladigan natija:** Ikki ilova o'rnatilgan.

### 6. minify yoqish · o'rta

`release` da `isMinifyEnabled = true` qiling va APK ni yig'ing.

**Kutiladigan natija:** Build muvaffaqiyatli.

### 7. BASE_URL · o'rta

Ikki variant uchun `BASE_URL` yarating va kodda chiqaring.

**Kutiladigan natija:** Debug da test, release da prod manzil.

### 8. Natijani bashorat qiling · o'rta

3 flavor va 2 build type bo'lsa, nechta variant bo'ladi?

**Kutiladigan natija:** 6.

### 9. Flavor yaratish · qiyin

`free` va `paid` flavorlarini yarating, `flavorDimensions` ni yozing.

**Kutiladigan natija:** 4 ta variant.

### 10. Xatoni toping · qiyin

`productFlavors` yozdim, lekin Sync xato berdi: `dimension` yo'q. Nega?

**Kutiladigan natija:** `flavorDimensions` va `dimension` majburiy.

### 11. R8 qoidasi · qiyin

`proguard-rules.pro` ga model sinflarini saqlovchi qoida yozing.

**Kutiladigan natija:** `-keep class com.example.model.** { *; }`.

### 12. Dev, staging, prod · bonus

Uchta flavor (`dev`, `staging`, `prod`) uchun turli `BASE_URL` yarating va jadvalda tushuntiring.

**Kutiladigan natija:** 3 flavor, 3 manzil.

## O'zingizni tekshiring

1. Debug va release farqi nima?
2. R8 nima qiladi?
3. `buildConfigField` nima uchun kerak?
4. `BuildConfig` ga qanday murojaat qilinadi?
5. `productFlavors` nima?
6. Build variant nima?
7. `applicationIdSuffix` nima uchun kerak?

## Uyga vazifa

Debug/release sozlamasi, `BASE_URL` va flavor vazifalarini bajaring (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
