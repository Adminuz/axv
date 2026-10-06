# 17-dars. build.gradle da kutubxonalarni ulash va boshqarish

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 6-hafta, 2-dars (umumiy 17-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (Dependency management: repository manbalari, BOM, konfliktlar), `uslubiy-korsatma.txt` (kapt va ksp, SemVer, dinamik versiyalar, resolutionStrategy, `app:dependencies`).

---

## Darsning maqsadi

Kutubxona qayerdan yuklanishini (`google()`, `mavenCentral()`, Jitpack) tushuntirish, `dependencies {}` ga kutubxona qo'shish va yangilash, BOM bilan bir oila kutubxonalarning versiyalarini birga boshqarish, `kapt` dan `ksp` ga o'tish, dinamik versiyalar (`1.2.+`) xavfini va `./gradlew app:dependencies` bilan daraxtni tahlil qilishni o'rgatish.

## Kutilayotgan natijalar

- `repositories` ga `google()`, `mavenCentral()` va Jitpack ni to'g'ri qo'shadi;
- Kutubxonani rasmiy hujjatdan topib, `dependencies {}` ga ulaydi va Sync qiladi;
- BOM nima ekanini va nima uchun versiyasiz yozilishini tushuntiradi;
- `kapt` va `ksp` farqini aytadi, dinamik versiyadan qochadi;
- Dependency daraxtini ko'rib, ziddiyatni `exclude` yoki `force` bilan hal qiladi.

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 16-dars: Gradle tasks, xatolarni o'qish |
| 08–25 | Yangi mavzu 1 | Repositories: `google()`, `mavenCentral()`, Jitpack |
| 25–38 | Yangi mavzu 2 | Kutubxona ulash, BOM, `kapt` va `ksp` |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | Versiya qoidalari, dependency tree, ziddiyatlar |
| 58–75 | Amaliyot | Loyihaga 2 ta kutubxona ulash va daraxtni tahlil qilish |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. Repository manbalari

Gradle kutubxonani **repository** dan yuklaydi. `google()` — Android va Jetpack kutubxonalari; `mavenCentral()` — Retrofit, OkHttp, Coil kabi ko'pchilik ochiq kutubxonalar; **Jitpack** — GitHub dagi kutubxonalarni to'g'ridan-to'g'ri ulash uchun. Repository ro'yxatda bo'lmasa, kutubxona «topilmadi» xatosi chiqadi. Kutubxona koordinatasi uchta qismdan iborat: `guruh:nom:versiya`. Repositoriyalarni odatda `settings.gradle.kts` dagi `dependencyResolutionManagement` da yozasiz.

```kotlin
// settings.gradle.kts
dependencyResolutionManagement {
    repositories {
        google()
        mavenCentral()
        maven { url = uri("https://jitpack.io") }
    }
}
```

Jitpack ni faqat kerak bo'lganda qo'shing: ishonchsiz manbalar xavfsizlik xavfini oshiradi.

### 2. Kutubxona ulash, BOM, `kapt` va `ksp`

Kutubxona rasmiy hujjatdan olinadi va module-level `dependencies {}` ga yoziladi, so'ng Sync Now. **BOM** (Bill of Materials) bir oila kutubxonalar versiyalarini birga boshqaradi: `platform(...)` yozilgach, shu oiladagi kutubxonalarni versiyasiz yozasiz, versiyalar bir-biriga mos bo'ladi. Annotation processing uchun ikki yo'l bor: **`kapt`** eski va sekin (Kotlin kodini Java stublariga o'giradi); **`ksp`** zamonaviy va tez. Google kutubxonalarni KSP ga o'tkazishni tavsiya qiladi.

```kotlin
dependencies {
    implementation(platform("androidx.compose:compose-bom:2024.06.00"))
    implementation("androidx.compose.material3:material3")

    implementation("com.squareup.retrofit2:retrofit:2.9.0")

    implementation("androidx.room:room-runtime:2.6.1")
    ksp("androidx.room:room-compiler:2.6.1")
}
```

BOM dagi kutubxonalarga versiya yozmaysiz: versiyani BOM belgilaydi. `kapt` o'rniga `ksp` ishlating (plaginni ulash kerak).

### 3. Versiya qoidalari va ziddiyatlarni hal qilish

Versiya SemVer ga bo'ysunadi: **Major** (katta o'zgarish, kod buzilishi mumkin), **Minor** (yangi imkoniyat, eski kod ishlaydi), **Patch** (faqat xato tuzatish). **Oltin qoida:** dinamik versiya (`1.2.+`) yozmang: ertaga muallif buzilgan versiya chiqarsa, ilovangiz ham ishlamay qoladi. Ikki kutubxona bir kutubxonaning turli versiyasini talab qilsa, Gradle odatda eng yangisini tanlaydi. `./gradlew app:dependencies` daraxtni ko'rsatadi; kerak bo'lsa `exclude` (ichki kutubxonani chiqarish) yoki `resolutionStrategy.force` (aniq versiyani majburlash) ishlatiladi.

```kotlin
implementation(libs.boshqa.kutubxona) {
    exclude(group = "com.squareup.okhttp3", module = "okhttp")
}

configurations.all {
    resolutionStrategy {
        force("com.squareup.okhttp3:okhttp:4.12.0")
    }
}
```

Ataylab aniq versiya yozing: `2.9.0`. `2.9.+` yoki `latest.release` — xavfli.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Repository qo'shing

`settings.gradle.kts` ga `google()` va `mavenCentral()` ni yozing.

**Yechim:**
```kotlin
repositories {
    google()
    mavenCentral()
}
```

### 2-topshiriq (oson). Kutubxona ulang

Module-level faylga Coil `2.3.0` (`io.coil-kt:coil-compose`) ni ulang.

**Yechim:**
```kotlin
dependencies {
    implementation("io.coil-kt:coil-compose:2.3.0")
}
```

### 3-topshiriq (o'rta). kapt dan ksp ga

`kapt("androidx.room:room-compiler:2.6.1")` ni KSP ga almashtiring va farqini yozing.

**Yechim:**
```kotlin
ksp("androidx.room:room-compiler:2.6.1")
// ksp tezroq; kapt Kotlin kodini avval Java stublariga o'giradi.
```

### 4-topshiriq (o'rta). Dinamik versiya

`retrofit:2.+` nima uchun xavfli? Qanday tuzatasiz?

**Yechim:** `+` har safar eng oxirgi versiyani oladi, build takrorlanmaydi. Tuzatish: `retrofit:2.9.0`.

### 5-topshiriq (qiyin). BOM bilan

Compose BOM ni ulang va `material3` ni versiyasiz yozing.

**Yechim:**
```kotlin
dependencies {
    implementation(platform("androidx.compose:compose-bom:2024.06.00"))
    implementation("androidx.compose.material3:material3")
}
```

### 6-topshiriq (qiyin). Ziddiyatni hal qiling

`./gradlew app:dependencies` da OkHttp ning ikki xil versiyasi ko'rinmoqda. `force` bilan `4.12.0` ni tanlang.

**Yechim:**
```kotlin
configurations.all {
    resolutionStrategy {
        force("com.squareup.okhttp3:okhttp:4.12.0")
    }
}
```

### 7-topshiriq (bonus). exclude

Ichki `okhttp` ni `exclude` qiling.

**Yechim:**
```kotlin
implementation(libs.boshqa.kutubxona) {
    exclude(group = "com.squareup.okhttp3", module = "okhttp")
}
```

---

## Tezkor nazorat

1. Kutubxona qayerdan yuklanadi? **Javob:** Repository dan: `google()`, `mavenCentral()`, Jitpack.
2. BOM nima? **Javob:** Bir oila kutubxonalarning mos versiyalari to'plami.
3. kapt va ksp farqi? **Javob:** kapt eski va sekin; ksp zamonaviy va tez.
4. Nima uchun `1.2.+` xavfli? **Javob:** Har safar boshqa versiya yuklanishi mumkin.
5. Ziddiyatni qanday ko'rasiz? **Javob:** `./gradlew app:dependencies` bilan.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
