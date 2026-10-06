# 15-dars. Gradle yordamida kutubxonalarni ulash va versiyalarni boshqarish

> Zamonaviy ilova tayyor kutubxonalarsiz yozilmaydi. Bugun ularni Gradle orqali ulashni va versiyalarni tartibda boshqarishni o'rganamiz.

## Dars xulosasi

- **`dependencies {}`** — kutubxonalar bloki; `implementation("guruh:nom:versiya")`.
- **Ombor:** `google()` va `mavenCentral()` dan Gradle yuklaydi; so'ng `Sync Now`.
- **Versiya:** stable — nashrga tayyor; `alpha` va `beta` — barqaror emas.
- **Ziddiyat:** Gradle eng yuqori versiyani oladi; `force(...)` aniq versiyani majburlaydi, `exclude(...)` olib tashlaydi.
- **Version catalog:** `libs.versions.toml` + `implementation(libs.retrofit)`.

## Qo'shimcha ma'lumot

### Transitive dependency
Retrofit ni qo'shsangiz, u talab qiladigan OkHttp ham avtomatik yuklanadi. Bunday bog'liqlik transitive deyiladi. Ba'zan u loyihani keraksiz kattalashtiradi — shunda `exclude` ishlatiladi.

### MVVM loyihasining odatiy ro'yxati
Lifecycle ViewModel va LiveData, Room (runtime va ktx, kompilyator `kapt` bilan), Retrofit va `converter-gson` — kichik MVVM loyiha ham shuncha kutubxona talab qiladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Dependency | Tashqi kutubxonaga bog'liqlik |
| implementation | Kutubxonani ulash konfiguratsiyasi |
| Maven Central / Google | Kutubxonalar omborlari |
| Stable / beta / alpha | Versiya barqarorlik darajalari |
| Version catalog | Versiyalarni markaziy boshqaruvchi `libs.versions.toml` fayli |
| Transitive dependency | Kutubxona bilan birga keluvchi bog'liqlik |
| force | Aniq versiyani majburlash |
| exclude | Bog'liqlikni chiqarib tashlash |

## Bilasizmi?

- Retrofit nomi «retro» + «fit» dan, ya'ni «yaxshilash» ma'nosida; u Square kompaniyasi tomonidan yaratilgan.
- Bitta Android ilovasi o'nlab, ba'zan yuzlab kutubxonaga tayanadi.
- Ko'p jamoalar kutubxona versiyalarini yangilashni avtomatlashtiradigan botlardan foydalanadi.

## Topshiriqlar

### 1. Retrofit · oson

Loyihaga Retrofit `2.9.0` ni ulang.

**Kutiladigan natija:** Sync muvaffaqiyatli o'tdi.

### 2. Coil · oson

Loyihaga Coil Compose `2.3.0` ni ulang.

**Kutiladigan natija:** Sync muvaffaqiyatli.

### 3. Qator tuzilishi · oson

`guruh:nom:versiya` qismlarini Retrofit uchun ajrating.

**Kutiladigan natija:** `com.squareup.retrofit2`, `retrofit`, `2.9.0`.

### 4. Omborlar · oson

`repositories` blokini toping: qaysi omborlar bor?

**Kutiladigan natija:** `google()` va `mavenCentral()`.

### 5. Versiya turlari · o'rta

`alpha`, `beta`, `stable` farqini jadvalda yozing.

**Kutiladigan natija:** 3 qatorli jadval.

### 6. Katalog yaratish · o'rta

`libs.versions.toml` ga Retrofit va Coil ni yozing.

**Kutiladigan natija:** `[versions]` va `[libraries]` bo'limlari.

### 7. Katalogdan ulash · o'rta

`dependencies` da `libs.retrofit` va `libs.coil.compose` dan foydalaning.

**Kutiladigan natija:** Sync muvaffaqiyatli.

### 8. Natijani bashorat qiling · o'rta

Ikki kutubxona OkHttp ning 4.9.0 va 4.12.0 versiyalarini talab qilsa, Gradle qaysini oladi?

**Kutiladigan natija:** 4.12.0: yuqori versiya.

### 9. force · qiyin

OkHttp ni 4.9.3 versiyasiga majburlang va nega ehtiyotkorlik kerakligini yozing.

**Kutiladigan natija:** `force` yozilgan va xavf izohlangan.

### 10. exclude · qiyin

Retrofit dan bitta transitive modulni chiqarib tashlang.

**Kutiladigan natija:** `exclude(group, module)` yozilgan.

### 11. Noto'g'ri versiya · qiyin

Versiyani `2.9.99` deb yozing va Gradle xatosini o'qing.

**Kutiladigan natija:** `Could not find ...` xatosi tushuntirilgan.

### 12. Versiyalarni yangilash · bonus

Katalogda Retrofit versiyasini yangilab, bitta joy o'zgarishi hamma modulga ta'sir qilishini tekshiring.

**Kutiladigan natija:** Bitta o'zgarish hamma joyda ishlaydi.

## O'zingizni tekshiring

1. Kutubxona qaysi blokda ulanadi?
2. `guruh:nom:versiya` nimani bildiradi?
3. Alpha, beta, stable farqi nima?
4. Version catalog nima uchun kerak?
5. `force` nima qiladi?
6. `exclude` nima qiladi?
7. Transitive dependency nima?

## Uyga vazifa

Retrofit va Coil ni ulang, katalogga ko'chiring (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
