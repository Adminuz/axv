# 3-dars: Dependency management va versiyalar bilan ishlash (Version Catalog)

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 1-hafta, 3-dars (umumiy 3-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Android ilovalarida tashqi kutubxonalar va bog'liqliklarni (Dependencies) boshqarish arxitekturasini o'rgatish; global repozitoriylar (`google()`, `mavenCentral()`) qanday ishlashini tushuntirish; `implementation`, `api`, `compileOnly`, `testImplementation` va `androidTestImplementation` konfiguratsiyalari orasidagi farqlarni amalda ko'rsatish; sanoat standarti hisoblangan zamonaviy **Version Catalog (`gradle/libs.versions.toml`)** tizimini loyihada qo'llash, uning 4 ta asosiy bloki (`[versions]`, `[libraries]`, `[bundles]`, `[plugins]`) orqali kutubxonalar versiyalarini markazlashgan holda boshqarish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Dependency (bog'liqlik) tushunchasini va uning Android ekotizimidagi ahamiyatini tushunish;
- `google()` va `mavenCentral()` kabi masofaviy repozitoriylar vazifasini bilish;
- `implementation` va `api` konfiguratsiyalari orasidagi fundamental farqni (kompilyatsiya tezligi va modullar inkapsulyatsiyasi) tushuntira olish;
- Versiyalarni boshqarish evolyutsiyasini (Hardcoded $\to$ `ext` $\to$ `buildSrc` $\to$ Version Catalog) bilish;
- `gradle/libs.versions.toml` faylining tuzilishini va 4 ta bo'limining vazifasini bilish;
- Kutubxonalar guruhini bitta `bundle`ga birlashtirib chaqirishni amalda bajara olish;
- `build.gradle` faylida Version Catalog sintaksisidan (`libs.retrofit`, `libs.bundles.networking`) to'g'ri foydalana olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Android Studio (so'nggi barqaror versiya);
- Internet tarmog'i (Maven repozitoriylaridan kutubxonalarni yuklash uchun);
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Build Types (Debug vs Release), Product Flavors va `BuildConfig` bo'yicha savol-javob |
| **10–25 min** | Yangi mavzu: Dependencies va Repozitoriylar | Tashqi kutubxonalar mohiyati, Maven Central, Google Maven omborlari |
| **25–45 min** | Bog'liqlik konfiguratsiyalari turlari | `implementation`, `api`, `compileOnly`, `testImplementation`, `androidTestImplementation` |
| **45–60 min** | Version Catalog (`libs.versions.toml`) standarti | 4 ta blok: `[versions]`, `[libraries]`, `[bundles]`, `[plugins]`, markaziy versiya boshqaruvi |
| **60–75 min** | Amaliy mashg'ulot | `libs.versions.toml` faylini yaratish, Retrofit va Gson kutubxonalarini bundle qilib ulash |
| **75–80 min** | Xulosa va darsni yakunlash | Asosiy xulosalar, tezkor nazorat savollari va uyga vazifa |

---

## Nazariy ma'lumotlar

### 1. Dependency nima va u qayerdan keladi?

Dasturchi har safar noldan velosiped yaratmaydi. Tarmoq bilan ishlash uchun **Retrofit**, ma'lumotlar bazasi uchun **Room**, rasmlarni yuklash uchun **Coil** kabi tayyor, sinovdan o'tgan kutubxonalar qo'llaniladi. Ushbu tashqi modullar dasturlashda **Dependency (bog'liqlik)** deb ataladi.

Siz `build.gradle` fayliga quyidagi satrni yozganingizda:
```groovy
implementation 'com.squareup.retrofit2:retrofit:2.9.0'
```
Gradle quyidagi qismlarni ajratib oladi:
- **Group ID:** `com.squareup.retrofit2` (Kompaniya yoki tashkilot domeni);
- **Artifact ID:** `retrofit` (Kutubxonaning aniq nomi);
- **Version:** `2.9.0` (Versiya raqami).

Gradle ushbu ma'lumot asosida internetdagi omborxonalarga (Repositories) so'rov yuboradi:
- **Google Maven (`google()`):** Android SDK, Jetpack, Material Design kutubxonalari ombori;
- **Maven Central (`mavenCentral()`):** Dunyodagi eng yirik ochiq kodli Java va Kotlin kutubxonalari ombori.

---

### 2. Bog'liqlik turlari (Dependency Configurations)

Android loyihasida kutubxonani qanday ulash uning xavfsizligi va loyihaning yig'ilish tezligiga bevosita ta'sir qiladi:

1. **`implementation` (Eng ko'p ishlatiladigan standart):**
   - Kutubxona faqat joriy modul ichida ishlatiladi;
   - Agar boshqa modul ushbu modulga ulansa, u bu kutubxonani ko'rmaydi (inkapsulyatsiya ta'minlanadi);
   - Loyihaning qayta kompilyatsiya bo'lish vaqtini sezilarli darajada tejaydi.
2. **`api` (Tranzitiv eksport):**
   - Kutubxona joriy moduldan tashqari, unga bog'langan barcha boshqa modullarga ham ochiq bo'ladi;
   - Agar bu kutubxona yangilansa, butun loyiha qayta yig'ilishi kerak bo'ladi (yig'ish vaqti ortadi).
3. **`compileOnly`:**
   - Kutubxona faqat kod yozish va kompilyatsiya paytida kerak, yakuniy APK hajmiga kirmaydi (masalan, maxsus annotatsiyalar protsessorlari).
4. **`runtimeOnly`:**
   - Kompilyatsiya paytida ko'rinmaydi, faqat ilova telefonda ishlayotganda (runtime) kerak bo'ladi.
5. **`testImplementation`:**
   - Faqat kompyuterda ishlaydigan lokal Unit-testlar uchun (JUnit, Mockito).
6. **`androidTestImplementation`:**
   - Android qurilma yoki emulyatorda ishlaydigan UI testlar uchun (Espresso).

---

### 3. Versiyalarni boshqarish evolyutsiyasi

Android dasturlash tarixida versiyalarni boshqarish bir necha bosqichdan o'tgan:
- **1-bosqich: Hardcoded stringlar:** Versiyalar to'g'ridan-to'g'ri `build.gradle` ichida yozilgan (`"2.9.0"`). Loyihada 10 ta modul bo'lsa, har birini alohida qidirib o'zgartirish talab etilar edi.
- **2-bosqich: `ext` bloklari:** `rootProject.ext.retrofitVersion = '2.9.0'`. Biroq Android Studio kiritish paytida avtomatik to'ldirishni (autocomplete) qo'llab-quvvatlamas edi.
- **3-bosqich: `buildSrc` papkasi:** Kotlin DSL da yozilgan, avtomatik to'ldirish bor. Ammo har bir kichik versiya o'zgarishida butun loyihani boshidan to'liq yig'ishga majbur qilardi.
- **4-bosqich (Hozirgi Oltin Standart): Version Catalog (`libs.versions.toml`)** — Google tomonidan Android Studio Flamingo va undan keyingi versiyalarda rasmiy standart qilib belgilandi.

---

### 4. Version Catalog (`gradle/libs.versions.toml`) tuzilishi

`gradle/libs.versions.toml` fayli TOML formatida bo'lib, **4 ta asosiy blok**dan iborat:

```toml
[versions]
kotlin = "1.9.22"
retrofit = "2.9.0"
okhttp = "4.12.0"
room = "2.6.1"

[libraries]
# Retrofit
retrofit-core = { group = "com.squareup.retrofit2", name = "retrofit", version.ref = "retrofit" }
retrofit-converter-gson = { group = "com.squareup.retrofit2", name = "converter-gson", version.ref = "retrofit" }
okhttp-logging = { group = "com.squareup.okhttp3", name = "logging-interceptor", version.ref = "okhttp" }

[bundles]
networking = ["retrofit-core", "retrofit-converter-gson", "okhttp-logging"]

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
```

#### `build.gradle` (Module: :app) da ishlatish:
```groovy
dependencies {
    // Alohida kutubxona ulash
    implementation libs.retrofit.core

    // Yoki butun boshli tarmoq to'plamini 1 qatorda ulash (Bundle)
    implementation libs.bundles.networking
}
```

---

## Amaliy topshiriqlar va mashqlar

### 1-topshiriq. `implementation` va `api` konfiguratsiyasini taqqoslash (oson)
Loyihangizda ikkita modul mavjud:
- `:core-network` (Tarmoq kutubxonalari joylashgan modul);
- `:app` (Asosiy modul, u `:core-network` ga bog'langan: `implementation project(':core-network')`).

Agar `:core-network` moduli ichida Retrofit kutubxonasi `implementation` orqali ulansa, `:app` moduli ichidagi Kotlin fayllarida `Retrofit` klassini to'g'ridan-to'g'ri chaqirish mumkinmi? Agar `api` orqali ulansa-chi?

**Yechim:**
1. **`implementation` bo'lganda:** `:app` moduli Retrofit klasslarini ko'ra olmaydi. Chunki `implementation` kutubxonani tashqi modullardan yashiradi (inkapsulyatsiya qiladi). Bu loyihaning mustaqil bo'lishini va tezroq yig'ilishini ta'minlaydi.
2. **`api` bo'lganda:** `:app` moduli Retrofit klasslarini bemalol import qila oladi. Chunki `api` o'z bog'liqliklarini barcha tashqi modullarga ham ochiq qilib uzatadi (tranzitiv o'tish).

---

### 2-topshiriq. Version Catalog da yangi kutubxona e'lon qilish (o'rta)
Loyihangizga rasmlarni asinxron yuklovchi mashhur **Coil** kutubxonasini qo'shishingiz kerak:
- Kutubxona guruhi: `"io.coil-kt"`
- Modul nomi: `"coil-compose"`
- Versiya: `"2.6.0"`

Ushbu kutubxonani `gradle/libs.versions.toml` faylining `[versions]` va `[libraries]` bloklariga to'g'ri qo'shing va `build.gradle` faylida chaqirish kodini ko'rsating.

**Yechim:**
`gradle/libs.versions.toml` faylida:
```toml
[versions]
coil = "2.6.0"

[libraries]
coil-compose = { group = "io.coil-kt", name = "coil-compose", version.ref = "coil" }
```
`build.gradle` faylida:
```groovy
dependencies {
    implementation libs.coil.compose
}
```

---

### 3-topshiriq. Room ma'lumotlar bazasi uchun to'liq Bundle yaratish (qiyin)
Android Architecture Components tarkibidagi **Room** ma'lumotlar bazasi bilan ishlash uchun quyidagi 3 ta komponent kerak:
1. `androidx.room:room-runtime:2.6.1`
2. `androidx.room:room-ktx:2.6.1`
3. `androidx.room:room-paging:2.6.1`

Ushbu 3 ta komponentni `libs.versions.toml` faylida bitta versiya o'zgaruvchisiga bog'lang, ularni `room-bundle` nomi ostida `[bundles]` blokiga birlashtiring va `build.gradle`da 1 qator kod bilan ulang.

**Yechim:**
`gradle/libs.versions.toml` faylida:
```toml
[versions]
room = "2.6.1"

[libraries]
room-runtime = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
room-ktx = { group = "androidx.room", name = "room-ktx", version.ref = "room" }
room-paging = { group = "androidx.room", name = "room-paging", version.ref = "room" }

[bundles]
room = ["room-runtime", "room-ktx", "room-paging"]
```
`build.gradle` faylida ulash:
```groovy
dependencies {
    implementation libs.bundles.room
}
```

---

## Tezkor nazorat savollari

1. Nega `implementation` konfiguratsiyasi `api` ga qaraganda ko'proq tavsiya etiladi?
   - *Javob:* Chunki `implementation` kutubxonani faqat o'sha modul ichida yashiradi, tashqi modullarga o'tkazmaydi. Bu esa biror modul o'zgarganda butun loyihaning qayta kompilyatsiya bo'lishining oldini oladi va yig'ish tezligini oshiradi.
2. `google()` va `mavenCentral()` repozitoriylarining vazifasi nima?
   - *Javob:* Ular dunyo bo'ylab barcha tayyor kutubxonalar saqlanadigan xavfsiz internet serverlaridir. Gradle kerakli kod paketlarini aynan shu serverlardan yuklab oladi.
3. Version Catalog (`libs.versions.toml`) ning eng katta 2 ta afzalligi nima?
   - *Javob:* 1) Barcha kutubxonalar versiyalari yagona markazda saqlanadi, 2) Android Studio da to'liq avtomatik to'ldirish (autocomplete) va xatoliklarni tekshirish ishlaydi.
4. TOML faylidagi `[bundles]` bo'limi nima uchun kerak?
   - *Javob:* O'zaro bog'liq bir nechta kutubxonalarni (masalan, Retrofit + Gson + OkHttp) bitta nom ostida guruhlash va `build.gradle`da 1 qator kod bilan birgalikda ulash uchun.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Kutubxona nomidagi chiziqcha (`-`) va nuqta (`.`) chalkashligi:** `libs.versions.toml` da `retrofit-core` deb e'lon qilingan kutubxona `build.gradle`da `libs.retrofit.core` tarzida nuqta bilan chaqiriladi.
- **Transitive bog'liqliklar konfliktini e'tiborsiz qoldirish:** Bir xil kutubxonaning ikki xil versiyasi yuklanganda Gradle xatolik berishi mumkin. Buni bartaraf etish uchun markaziy Version Catalog qo'llanilishi shart.
- **Kutubxona qo'shilgach "Sync Now" bosmaslik:** Har qanday toml yoki gradle o'zgarishidan so'ng sinxronizatsiya qilish shart.
