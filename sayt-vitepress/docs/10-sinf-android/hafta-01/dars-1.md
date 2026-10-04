---
title: "1-dars. 1-dars: Gradle konfiguratsiyasi va build tizimi asoslari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Android)", "link": "/10-sinf-android/"}, "week": {"n": 1, "link": "/10-sinf-android/hafta-01/"}, "g": 1, "title": "1-dars: Gradle konfiguratsiyasi va build tizimi asoslari", "lead": "", "slide": "/slaydlar/10-sinf-android/hafta-01/dars-1.html", "tabs": [{"g": 1, "link": "/10-sinf-android/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/10-sinf-android/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/10-sinf-android/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "2-dars: Build variantlari va Product Flavors", "link": "/10-sinf-android/hafta-01/dars-2"}}
---

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** Gradle konfiguratsiyasi va build tizimi asoslari: settings.gradle, build.gradle, SDK versiyalari  

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Har bir professional mobil dasturchining faoliyatida kod yozish qanchalik muhim bo'lsa, loyihani yig'ish (Build Automation) tizimini to'g'ri boshqarish ham shunchalik hal qiluvchi ahamiyatga ega. Ushbu darsda biz Android Studio'ning yuragi bo'lgan **Gradle** tizimi bilan chuqur tanishamiz:

1. **Gradle nima va uning roli:**
   - Gradle — bu kodlar (Kotlin/Java), dizayn fayllari (XML), rasmlar va tashqi kutubxonalarni birlashtirib, foydalanuvchi telefoniga o'rnatiladigan tayyor **APK** yoki **AAB** fayliga aylantirib beruvchi yig'ish tizimidir.
2. **Gradle fayllari arxitekturasi:**
   - `settings.gradle`: Loyihadagi barcha modullar ro'yxati;
   - `build.gradle (Project)`: Butun loyiha uchun umumiy bo'lgan qoidalar va repozitoriylar;
   - `build.gradle (Module: :app)`: Ilovaning asosiy konfiguratsiyasi (SDK versiyalari, paket nomi, kutubxonalar);
   - `gradle.properties`: Global sozlamalar va operativ xotira (RAM) boshqaruvi;
   - `gradle-wrapper.properties`: Barcha jamoa a'zolari bir xil Gradle versiyasida ishlashini ta'minlovchi tizim.
3. **SDK va versiyalash parametrlari:**
   - `compileSdk`: Kompilyatsiya qilinadigan Android versiyasi (yangi API imkoniyatlarini ochadi);
   - `minSdk`: Ilova ishlay oladigan eng quyi Android versiyasi (quyi qurilmalar uchun filtr);
   - `targetSdk`: Ilova qaysi versiya xavfsizlik va xulq-atvor qoidalariga moslab sinovdan o'tkazilgani;
   - `versionCode` (butun son, Google Play yangilanishlarini tekshiradi) va `versionName` (foydalanuvchiga ko'rinadigan matn).
4. **Gradle Build Lifecycle (Yig'ish hayot sikli):**
   - **Initialization** (modullar aniqlanadi) $\to$ **Configuration** (vazifalar grafigi tuziladi) $\to$ **Execution** (kod kompilyatsiya qilinib APK yasaladi).
5. **Terminal buyruqlari:**
   - `./gradlew clean`, `./gradlew assembleDebug`, `./gradlew tasks`.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun amaliy topshiriqlar

Quyidagi 10 ta amaliy vazifani diqqat bilan o'rganing va ularni Android Studio muhitida hamda daftaringizda bajaring:

### 1-topshiriq <Badge type="tip" text="oson" />
Android loyihasining `settings.gradle` va `build.gradle (Project)` fayllari orasidagi farqni tushuntiring. Yangi modul (masalan, `:database`) qo'shilganda qaysi faylga o'zgartirish kiritiladi?

### 2-topshiriq <Badge type="tip" text="oson" />
Quyidagi SDK parametrlarini diqqat bilan o'rganing:
- `compileSdk = 34`
- `minSdk = 28`
- `targetSdk = 34`  
Ushbu ilovani quyidagi telefonlarga o'rnatish mumkinmi? Har bir holat uchun "Ha" yoki "Yo'q" deb yozing va sababini tushuntiring:
1. Samsung Galaxy S9 (Android 9.0 — API 28);
2. Xiaomi Redmi Note 4 (Android 7.0 — API 24);
3. Google Pixel 8 (Android 14 — API 34).

### 3-topshiriq <Badge type="tip" text="oson" />
Android ilovangiz uchun `versionCode` va `versionName` parametrlarini quyidagi talablarga mos holda qanday belgilash kerakligini yozing:
- Ilova birinchi marta ommaga taqdim etilmoqda;
- Ilovaning versiyasi: "1.0.0-alpha";
- Keyinchalik birinchi yangilanish chiqarilganda qaysi parametr majburiy oshiriladi?

### 4-topshiriq <Badge type="warning" text="o'rta" />
Dasturchi `build.gradle` fayliga yangi qator kod qo'shdi, biroq Android Studio oynasining yuqori qismida chiqqan *"Sync Now"* tugmasini bosmadi. Bu holatda dasturchi yangi kutubxonadan foydalanib kod yoza oladimi? Qanday xatolik yuz beradi?

### 5-topshiriq <Badge type="warning" text="o'rta" />
Gradle Build Lifecycle ning 3 ta bosqichini (Initialization, Configuration, Execution) o'z ichiga olgan sxema yoki jadval tuzing. Nima uchun Configuration bosqichida kod kompilyatsiyasi hali boshlanmagan bo'ladi?

### 6-topshiriq <Badge type="warning" text="o'rta" />
Loyihangiz kompyuteringizda juda sekin yig'ilmoqda (build jarayoni 4–5 daqiqa davom etmoqda). `gradle.properties` faylida qaysi parametr orqali Gradle'ga ajratiladigan JVM operativ xotirasi (RAM) miqdorini oshirish mumkin? Misol tariqasida 3GB xotira ajratish kodini yozing.

### 7-topshiriq <Badge type="danger" text="qiyin" />
Android Studio terminalida quyidagi 3 ta buyruq nima vazifani bajarishini amalda sinab ko'ring va natijasini yozing:
1. `./gradlew clean`
2. `./gradlew assembleDebug`
3. `./gradlew --version`  
`clean` buyrug'i loyihaning qaysi papkalarini tozalashini aniqlang.

### 8-topshiriq <Badge type="danger" text="qiyin" />
Ilovangizning `defaultConfig` blokida `applicationId` qiymati `"uz.mycompany.taxi"` deb ko'rsatilgan. 
- `applicationId` nima va u dunyo bo'ylab nima uchun yagona bo'lishi shart?
- Agar boshqa bir dasturchi xuddi shu ID bilan Google Play'ga ilova yuklagan bo'lsa, siz o'z ilovangizni yuklay olasizmi?

### 9-topshiriq <Badge type="danger" text="qiyin" />
`gradle-wrapper.properties` faylining vazifasini tushuntiring. Nima uchun professional jamoaviy loyihalarda Gradle tizimini global o'rnatish o'rniga aynan Gradle Wrapper (`gradlew`) vositasidan foydalanish qat'iy tavsiya etiladi?

### 10-topshiriq <Badge type="info" text="bonus" />
Android Studio'da yangi bo'sh loyiha yarating. Loyiha moduli `build.gradle` faylining oxiriga maxsus Gradle Task yozing:
- Vazifa nomi: `showAppConfig`;
- Vazifa terminalda sizning ism-familiyangiz, ilovaning `compileSdk` darajasi va `minSdk` darajasini chiroyli ramkada chop etsin.
- Vazifani terminaldan `./gradlew showAppConfig` orqali ishga tushiring va skrinshot yoki konsol matnini taqdim eting.

</div>

