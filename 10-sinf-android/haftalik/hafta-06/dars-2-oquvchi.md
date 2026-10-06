# 17-dars. build.gradle da kutubxonalarni ulash va boshqarish

> Ilova kutubxonalarsiz yashamaydi, lekin noto'g'ri ulangan kutubxona build ni buzadi. Bugun kutubxonalarni ongli ulashni o'rganamiz.

## Dars xulosasi

- Kutubxona repository dan yuklanadi: `google()`, `mavenCentral()`, Jitpack.
- Koordinata: `guruh:nom:versiya`; o'zgargach Sync Now.
- BOM bir oila kutubxonalar versiyasini birga boshqaradi.
- `ksp` — `kapt` ning tez va zamonaviy o'rnini bosuvchisi.
- SemVer: Major, Minor, Patch; dinamik versiya (`1.2.+`) ishlatilmaydi.
- Ziddiyatda `app:dependencies`, keyin `exclude` yoki `force`.

## Qo'shimcha ma'lumot

### Eng yangisi yutadi
Retrofit OkHttp 4.9.0 ni, boshqa kutubxona 3.12.0 ni talab qilsa, Gradle odatda 4.9.0 ni tanlaydi. Lekin eski kutubxona yangi versiya bilan ishlamasligi mumkin.

### Transitive bog'liqlik
Kutubxonaning o'zi talab qiladigan boshqa kutubxonalar daraxtda ichki qatorlarda ko'rinadi.

### Jitpack
GitHub dagi kutubxonani release yoki tag orqali ulash imkonini beradi.

### Versiya turlari
Stable nashr uchun; alpha va beta hali to'liq sinovdan o'tmagan.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Repository | Kutubxona manbasi |
| Dependency | Tashqi kutubxona |
| BOM | Bill of Materials |
| kapt | Eski annotation processing |
| ksp | Tez annotation processing |
| SemVer | Major.Minor.Patch |
| Transitive | Ichki bog'liqlik |
| exclude | Chiqarib tashlash |
| force | Versiyani majburlash |

## Bilasizmi?

- Gradle ziddiyatda odatda «eng yangisi yutadi» strategiyasini qo'llaydi.
- Google kutubxonalarni KSP ga o'tkazishni tavsiya qiladi.
- SemVer: Major o'zgarsa, kodingiz buzilishi ehtimoli yuqori.

## Topshiriqlar

### 1. Repository · oson

Uchta asosiy repository nomini va vazifasini yozing.

**Kutiladigan natija:** google, mavenCentral, jitpack.

### 2. Koordinata · oson

`com.squareup.retrofit2:retrofit:2.9.0` ni qismlarga ajrating.

**Kutiladigan natija:** Guruh, nom, versiya.

### 3. Sync · oson

`dependencies` o'zgargach nima qilinadi?

**Kutiladigan natija:** Sync Now.

### 4. SemVer · oson

2.9.0 da Major, Minor, Patch ni ayting.

**Kutiladigan natija:** 2, 9, 0.

### 5. Kutubxona ulang · o'rta

Coil ni ulang.

**Kutiladigan natija:** `implementation(...)`.

### 6. ksp · o'rta

`kapt` ni `ksp` ga o'zgartiring.

**Kutiladigan natija:** `ksp(...)`.

### 7. Dinamik versiya · o'rta

`lib:1.+` xavfini 2 jumlada yozing.

**Kutiladigan natija:** Takrorlanmas build.

### 8. BOM sabab · o'rta

BOM da kutubxona nima uchun versiyasiz yoziladi?

**Kutiladigan natija:** Versiyani BOM belgilaydi.

### 9. Daraxt · qiyin

`app:dependencies` ni ishga tushiring va bitta kutubxonaning ichki qatorlarini yozing.

**Kutiladigan natija:** Transitive qatorlar.

### 10. Ziddiyat · qiyin

Ikki versiya ziddiyatini `force` bilan hal qiling.

**Kutiladigan natija:** `resolutionStrategy`.

### 11. exclude · qiyin

Ichki kutubxonani `exclude` qiling.

**Kutiladigan natija:** `exclude(group, module)`.

### 12. Jitpack · bonus

GitHub kutubxonasini Jitpack orqali ulash qadamlarini yozing.

**Kutiladigan natija:** Repository, koordinata, Sync.

## O'zingizni tekshiring

1. Repository nima?
2. `guruh:nom:versiya`?
3. BOM nima?
4. `kapt` va `ksp` farqi?
5. Dinamik versiya nega xavfli?
6. Ziddiyatni qanday hal qilasiz?

## Uyga vazifa

2 ta kutubxona ulang va daraxtni tahlil qiling (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
