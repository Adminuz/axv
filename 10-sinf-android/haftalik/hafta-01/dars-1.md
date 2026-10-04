# 1-dars: Gradle konfiguratsiyasi va build tizimi asoslari

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 1-hafta, 1-dars (umumiy 1-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Android ilovalarini avtomatlashtirilgan tarzda yig'ish (Build Automation) tizimi bo'lgan **Gradle**ning arxitekturasi va uning operatsion tamoyillarini o'rgatish; loyihaning turli darajadagi konfiguratsiya fayllari (`settings.gradle`, `build.gradle (Project)`, `build.gradle (Module: :app)`, `gradle.properties`, `gradle-wrapper.properties`) o'rtasidagi farqlarni tushuntirish; `compileSdk`, `minSdk`, `targetSdk`, `versionCode` va `versionName` parametrlarining mohiyatini hamda Gradle Build Lifecycle (Initialization, Configuration, Execution) bosqichlarini amalda o'zlashtirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Gradle nima ekanini va Android ekotizimida kod, resurs va kutubxonalarni birlashtiruvchi "bosh usta" sifatidagi vazifasini tushunish;
- Project-level va Module-level `build.gradle` fayllarining vazifalarini aniq ajrata olish;
- `compileSdk`, `minSdk` va `targetSdk` orasidagi texnik farqlarni va ularning ilova mosligi (compatibility)ga ta'sirini bilish;
- `versionCode` (butun son, Google Play uchun) va `versionName` (foydalanuvchi ko'radigan qator) parametrlarini to'g'ri boshqara olish;
- Gradle Build Lifecycle ning 3 ta asosiy bosqichini (Initialization, Configuration, Execution) tushunish;
- Terminal orqali asosiy Gradle buyruqlarini (`./gradlew clean`, `./gradlew build`, `./gradlew tasks`) bajara olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (kamida 8GB RAM, tavsiya 16GB);
- Android Studio (so'nggi barqaror versiya: Ladybug yoki Koala);
- JDK 17 yoki JDK 21 o'rnatilgan muhit;
- Internet tarmog'i (repozitoriylardan kutubxona va plaginlarni yuklash uchun);
- Proyektor yoki monitor (dars taqdimoti va jonli kod namoyishi uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va kirish | Kurs dasturi bilan tanishuv, Advanced Android bosqichining maqsadlari va talablari |
| **10–25 min** | Yangi mavzu: Gradle nima va nega kerak? | Build Automation mohiyati, xomashyo (kod, XML, rasm)dan tayyor APK/AAB ga o'tish |
| **25–45 min** | Gradle fayllari arxitekturasi va asosiy bloklar | `settings.gradle`, Project vs Module `build.gradle`, `compileSdk`, `minSdk`, `targetSdk`, `defaultConfig` |
| **45–60 min** | Gradle hayot sikli va terminal buyruqlari | 3 bosqich (Initialization, Configuration, Execution), `./gradlew clean`, `./gradlew build` |
| **60–75 min** | Amaliy mashg'ulot | Android Studio'da yangi loyiha ochish, Gradle fayllarini tahlil qilish, parametrlarni o'zgartirib qayta yig'ish |
| **75–80 min** | Xulosa va darsni yakunlash | Asosiy xulosalarni mustahkamlash, tezkor savol-javob va uyga vazifa |

---

## Nazariy ma'lumotlar

### 1. Gradle nima va u Android ekotizimida nima uchun kerak?

Android ilovalari tashqi ko'rinishidan oddiy bo'lsa-da, ularning orqasida murakkab yig'ish jarayoni yotadi. Dasturchi Android Studio'da **"Run"** tugmasini bosgan paytda quyidagi jarayonlar parallel va ketma-ket sodir bo'ladi:
- Kotlin va Java kodlari kompilyatsiya qilinadi (baytkodga aylantiriladi);
- XML dizayn fayllari, rasmlar va vektorlar binar resurslarga siqiladi;
- Tashqi kutubxonalar (dependencies) keshdan yoki internet omborlaridan yuklanadi;
- Bir nechta modullarning `AndroidManifest.xml` fayllari bitta asosiy manifestga birlashtiriladi (Manifest Merging);
- Kod optimallashtiriladi va barchasi bitta o'rnatiluvchi fayl — **APK (Android Package Kit)** yoki **AAB (Android App Bundle)** ga paketlanadi.

Ushbu ulkan jarayonni boshqaruvchi tizim — **Gradle (Build Automation System)** deb ataladi.

> **Hayotiy o'xshatish:** Tasavvur qiling, siz bino qurmoqchisiz. Sizda g'isht (kod), oyna va eshiklar (resurslar), armatura (kutubxonalar) bor. Lekin bularning barchasini to'g'ri ketma-ketlikda yig'ib, tayyor uyni barpo qiluvchi bosh injener bo'lmasa, materiallar shunchaki uyum bo'lib qoladi. Android olamida ana shu bosh muhandis — **Gradle**dir.

---

### 2. Gradle fayllari arxitekturasi

Android loyihasining `Gradle Scripts` bo'limida quyidagi asosiy konfiguratsiya fayllari joylashadi:

#### A. `settings.gradle` (yoki `settings.gradle.kts`)
Loyiha tarkibidagi barcha modullar ro'yxatini belgilaydi. Agar loyihada asosiy ilova (`:app`), maxsus kutubxona moduli (`:core-network`) yoki aqlli soatlar moduli bo'lsa, Gradle ularni aynan shu fayl orqali ro'yxatga oladi:
```groovy
rootProject.name = "MyApplication"
include ':app'
include ':core-network'
```

#### B. `build.gradle (Project: MyApplication)`
Butun loyiha (barcha modullar) uchun umumiy bo'lgan global qoidalar va repozitoriylarni belgilaydi. Masalan, Google plaginlari va Kotlin versiyalari shu yerda e'lon qilinadi.

#### C. `build.gradle (Module: :app)`
Eng asosiy ish bajariladigan fayl. Ilovaning qaysi Android versiyalarida ishlashi, versiya raqami, paket nomi va ulanadigan kutubxonalar aynan shu yerda saqlanadi.

#### D. `gradle.properties`
Loyihaning global JVM parametrlari va muhit o'zgaruvchilari saqlanadi. Masalan, Gradle tezroq ishlashi uchun unga ajratiladigan operativ xotira (RAM) miqdorini oshirish mumkin:
```properties
org.gradle.jvmargs=-Xmx4096m -XX:MaxMetaspaceSize=1024m
android.useAndroidX=true
```

#### E. `gradle-wrapper.properties`
Gradle Wrapper tizimi. Bu fayl loyiha aynan qaysi Gradle versiyasida (masalan, `gradle-8.7-bin.zip`) yig'ilishi kerakligini belgilaydi. Bu boshqa dasturchi loyihani yuklab olganda, uning kompyuterida Gradle o'rnatilmagan bo'lsa ham loyihaning bir xil yig'ilishini kafolatlaydi.

---

### 3. `build.gradle (Module: :app)` faylining ichki anatomiyasi

Keling, modul darajasidagi eng muhim bloklarni batafsil tahlil qilamiz:

```groovy
plugins {
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}

android {
    namespace 'uz.axv.androidapp'
    compileSdk 34

    defaultConfig {
        applicationId "uz.axv.androidapp"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0.0"

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

#### Asosiy parametrlar va ularning farqi:
1. **`compileSdk` (Kompilyatsiya SDK darajasi):** Ilova kodini tekshirish va baytkodga aylantirishda Android SDK ning qaysi versiyasi ishlatilishini bildiradi. `compileSdk 34` bo'lsa, siz Android 14 dagi barcha yangi klasslar va funksiyalardan kodingizda bemalol foydalana olasiz.
2. **`minSdk` (Minimal SDK darajasi):** Ilova o'rnatilishi mumkin bo'lgan eng quyi Android versiyasi. Agar `minSdk 24` (Android 7.0) bo'lsa, Android 6.0 yoki 5.0 bo'lgan qurilmalarga bu ilova umuman o'rnatilmaydi.
3. **`targetSdk` (Maqsadli SDK darajasi):** Ilova qaysi tizim talablari va xavfsizlik qoidalariga moslab sinovdan o'tkazilganini bildiradi. Google Play do'koni doimiy ravishda `targetSdk`ni so'nggi versiyalarda ushlab turishni talab qiladi.
4. **`versionCode`:** Butun son (1, 2, 3...). Google Play yangilanishlarni qabul qilishda faqat shu songa qaraydi — har bir yangi yangilanishda bu son oshishi shart!
5. **`versionName`:** Matnli satr ("1.0.0", "2.1-beta"). Bu faqat foydalanuvchiga sozlamalar bo'limida ko'rsatiladigan versiya nomi.

---

### 4. Gradle Build Lifecycle (Yig'ishning hayot sikli)

Gradle o'z ishini bajarishda qat'iy **3 ta bosqich**dan o'tadi:
1. **Initialization (Initsializatsiya):** Gradle loyiha katalogidagi `settings.gradle` faylini topadi, qaysi modullar mavjudligini aniqlaydi va har bir modul uchun Project obyektini yaratadi.
2. **Configuration (Konfiguratsiya):** Barcha modullarning `build.gradle` fayllari bajariladi. Qanday kutubxonalar ulanishi, qaysi vazifalar (Tasks) bajarilishi kerakligi aniqlanib, **Vazifalar grafigi (Directed Acyclic Graph — DAG)** shakllantiriladi. Kod kompilyatsiyasi bu bosqichda hali boshlanmaydi!
3. **Execution (Bajarish):** Gradle oldingi bosqichda tuzilgan vazifalar grafigi bo'yicha amallarni ketma-ket bajaradi: kod kompilyatsiya qilinadi, resurslar siqiladi, manifestlar birlashtiriladi va yakuniy `.apk` yoki `.aab` fayli yaratiladi.

---

### 5. Terminal bilan ishlash (Gradle CLI)

Professional Android dasturchisi barcha amallarni terminal orqali bajara olishi lozim:
- `./gradlew clean` — avvalgi yig'ilgan barcha kesh va `build/` papkalarini tozalaydi.
- `./gradlew assembleDebug` — ilovaning sinov (Debug) APK faylini yaratadi.
- `./gradlew tasks` — loyihadagi barcha mavjud Gradle vazifalari ro'yxatini chiqaradi.
- `./gradlew --version` — Gradle va JVM versiyasini tekshiradi.

---

## Amaliy topshiriqlar va mashqlar

### 1-topshiriq. SDK versiyalarining mosligini tahlil qilish (oson)
Ilovangizning `build.gradle` faylida quyidagi parametrlar ko'rsatilgan:
- `compileSdk = 34`
- `minSdk = 26`
- `targetSdk = 34`

Quyidagi savollarga javob bering:
1. Android 8.0 (API 26) o'rnatilgan telefonda ushbu ilova ishlaydimi?
2. Android 7.1 (API 25) o'rnatilgan eski telefonga bu ilovani o'rnatish mumkinmi? Nega?
3. Dasturchi Android 14 (API 34) da chiqqan yangi API funksiyalarini kodda ishlata oladimi?

**Yechim:**
1. **Ha, ishlaydi.** Chunki `minSdk = 26`, Android 8.0 esa aynan API 26 ga teng bo'lib, ruxsat etilgan chegaraga kiradi.
2. **Yo'q, o'rnatib bo'lmaydi.** Chunki Android 7.1 API 25 hisoblanadi, ilovaning minimal talabi esa API 26 qilib belgilangan. Tizim paketni o'rnatishdan bosh tortadi.
3. **Ha, ishlata oladi.** Chunki `compileSdk = 34` bo'lib, kompilyator API 34 ga tegishli barcha yangi klasslar va metodlarni taniydi.

---

### 2-topshiriq. Versiyalash xatosini tuzatish va yangilanish chiqarish (o'rta)
Ilovangizning Google Play'dagi joriy versiyasi:
- `versionCode 5`
- `versionName "1.2.0"`

Dasturchi yangi xatoliklarni tuzatdi va yangilanishni yuborish uchun quyidagicha o'zgartirish kiritdi:
- `versionCode 5`
- `versionName "1.2.1"`

Google Play Console ushbu yangilanishni yuklashda xatolik berdi va rad etdi.
1. Xatolikning sababi nimada?
2. Muammoni qanday to'g'rilash kerak? To'g'ri kod variantini yozing.

**Yechim:**
1. **Xato sababi:** Google Play ilova yangilanishini faqat `versionCode` soni orqali aniqlaydi. Dasturchi faqat `versionName`ni o'zgartirgan, biroq `versionCode` o'zgarishsiz (5 holatida) qolib ketgan. Do'kon tizimida `versionCode` avvalgisidan qat'iy katta bo'lishi shart!
2. **To'g'rilangan kod:**
```groovy
defaultConfig {
    versionCode 6 // Avvalgi 5 dan katta bo'lishi shart
    versionName "1.2.1"
}
```

---

### 3-topshiriq. Maxsus Gradle Task yaratish (qiyin)
Loyiha moduli darajasidagi `build.gradle` fayliga dasturchi haqida va loyiha yig'ilgan vaqt haqida ma'lumot beruvchi `printProjectInfo` nomli maxsus Gradle vazifasini (Task) yozing:
- Vazifa ishga tushganda ilova nomi, `applicationId`, `compileSdk` va `versionName` parametrlarini terminalda chiroyli qilib chop etsin.
- Ushbu vazifani terminal orqali ishga tushirish buyrug'ini ko'rsating.

**Yechim:**
`app/build.gradle` (yoki `build.gradle.kts`) faylining oxiriga quyidagi vazifa qo'shiladi:
```groovy
tasks.register("printProjectInfo") {
    doLast {
        println("=========================================")
        println("Loyiha: " + project.name)
        println("Application ID: " + android.defaultConfig.applicationId)
        println("Compile SDK: " + android.compileSdk)
        println("Versiya nomi: " + android.defaultConfig.versionName)
        println("Yig'ish tizimi: Gradle " + gradle.gradleVersion)
        println("=========================================")
    }
}
```
**Terminal orqali ishga tushirish:**
```bash
./gradlew printProjectInfo
```

---

## Tezkor nazorat savollari

1. Gradle nima va nega u "Build Automation" tizimi deb ataladi?
   - *Javob:* Chunki u kodni kompilyatsiya qilish, resurslarni siqish, kutubxonalarni yuklash va tayyor APK yaratish jarayonlarini avtomatik tarzda bajaradi.
2. `compileSdk` bilan `minSdk` o'rtasidagi asosiy farq nimada?
   - *Javob:* `compileSdk` — kodni yozish va kompilyatsiya qilish paytidagi SDK versiyasi; `minSdk` — ilova ishlay oladigan eng quyi Android versiyasi (quyi qurilmalar uchun filtr).
3. Google Play ilovaning yangilanishini qaysi parametr orqali tekshiradi?
   - *Javob:* `versionCode` (butun son) parametri orqali. U har doim oshib borishi shart.
4. Gradle Build Lifecycle ning 3 ta bosqichini sanab bering.
   - *Javob:* 1. Initialization, 2. Configuration, 3. Execution.
5. Yangi kutubxona yoki parametr qo'shilganda nima uchun "Gradle Sync" qilish shart?
   - *Javob:* O'zgarishlar Android Studio loyiha strukturasiga tatbiq etilishi, kutubxonalar keshga yuklanishi va IDE kodni to'liq taniy olishi uchun.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **`minSdk`ni juda baland qilib qo'yish:** Agar `minSdk` 33 qilib qo'yilsa, aholining 70% dan ortig'i ilovangizni o'rnatolmaydi. O'zbekiston bozori uchun `minSdk` 24 (Android 7.0) yoki 26 (Android 8.0) tavsiya etiladi.
- **Har bir o'zgarishdan keyin "Sync Now" bosmaslik:** O'quvchilar `build.gradle`ga kod yozib, sinxronizatsiya qilmasdan kod yozishga o'tishadi va qizil xatoliklarga duch kelishadi.
- **`gradle.properties` xotirasini haddan tashqari oshirish:** 8GB RAM ga ega kompyuterda JVM ga 6GB ajratilsa, tizim qotib qoladi. Standart 2–3GB yetarli.
