---
title: "3-dars. 3-dars: Dependency management va versiyalar bilan ishlash (Version Catalog)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Android)", "link": "/10-sinf-android/"}, "week": {"n": 1, "link": "/10-sinf-android/hafta-01/"}, "g": 3, "title": "3-dars: Dependency management va versiyalar bilan ishlash (Version Catalog)", "lead": "", "slide": "/slaydlar/10-sinf-android/hafta-01/dars-3.html", "tabs": [{"g": 1, "link": "/10-sinf-android/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/10-sinf-android/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/10-sinf-android/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "2-dars: Build variantlari va Product Flavors", "link": "/10-sinf-android/hafta-01/dars-2"}, "next": null}
---

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** Dependency management va versiyalar bilan ishlash: kutubxonalar, repozitoriylar, Version Catalog (libs.versions.toml)  

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Zamonaviy Android ilovalari o'nlab tashqi kutubxonalarga (tarmoq, ma'lumotlar bazasi, UI komponentlari) tayanadi. Ushbu kutubxonalarni to'g'ri ulash, ularning versiyalarini boshqarish va loyihaning tezkor yig'ilishini ta'minlash dasturchining asosiy ko'nikmalaridandir:

1. **Dependency va Repozitoriylar:**
   - Dependency — ilovaga qo'shimcha imkoniyat beruvchi tayyor modul (masalan, Retrofit, Room, Coil);
   - Gradle kutubxonalarni xavfsiz internet omborlaridan — **Google Maven (`google()`)** va **Maven Central (`mavenCentral()`)** dan yuklab oladi.
2. **Bog'liqlik konfiguratsiyalari:**
   - `implementation`: Kutubxona faqat shu modul ichida ishlatiladi (tavsiya etilgan standart, yig'ish tezligini oshiradi);
   - `api`: Boshqa modullarga ham eksport qilinadi;
   - `testImplementation`: Faqat lokal Unit-testlar (JUnit);
   - `androidTestImplementation`: Qurilmadagi UI testlar (Espresso).
3. **Versiyalarni boshqarish evolyutsiyasi:**
   - Hardcoded stringlar $\to$ `ext` bloklari $\to$ `buildSrc` $\to$ **Version Catalog (`libs.versions.toml`)**.
4. **Version Catalog (`gradle/libs.versions.toml`) tuzilishi:**
   - `[versions]`: Barcha versiya raqamlari yagona joyda saqlanadi;
   - `[libraries]`: Kutubxonalar guruh va modullari bilan e'lon qilinadi;
   - `[bundles]`: Bog'liq kutubxonalar (masalan, Retrofit + Gson + OkHttp) bitta to'plamga birlashtiriladi;
   - `[plugins]`: Gradle plaginlari ro'yxati.
5. **Modulda chaqirish:**
   - `implementation(libs.retrofit)` yoki `implementation(libs.bundles.networking)`.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun amaliy topshiriqlar

Quyidagi 10 ta amaliy vazifani diqqat bilan o'rganing va ularni Android Studio muhitida hamda daftaringizda bajaring:

### 1-topshiriq <Badge type="tip" text="oson" />
Dependency koordinatasi hisoblangan `"com.squareup.retrofit2:retrofit:2.9.0"` satrini 3 ta asosiy qismga (Group ID, Artifact ID, Version) ajratib ko'rsating va har birining ma'nosini tushuntiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Maven Central va Google Maven repozitoriylari nima uchun kerak? Ular qayerda (loyihaning qaysi faylida) e'lon qilinadi?

### 3-topshiriq <Badge type="tip" text="oson" />
`testImplementation` va `androidTestImplementation` konfiguratsiyalari orasidagi farq nima? Qaysi biri haqiqiy telefon yoki emulyatorda ishlaydi?

### 4-topshiriq <Badge type="warning" text="o'rta" />
Ko'p modulli (multi-module) Android loyihasida nima uchun `api` o'rniga `implementation` dan foydalanish tavsiya etiladi? Bu yig'ish (build) vaqtiga qanday ijobiy ta'sir ko'rsatadi?

### 5-topshiriq <Badge type="warning" text="o'rta" />
Eski usuldagi hardcoded kutubxona yozuvlarining (`implementation 'androidx.core:core-ktx:1.12.0'`) kamchiliklarini va nega Google kompaniyasi Version Catalog tizimiga o'tishni tavsiya qilayotganini tushuntiring.

### 6-topshiriq <Badge type="warning" text="o'rta" />
`gradle/libs.versions.toml` faylining 4 ta asosiy blokini (`[versions]`, `[libraries]`, `[bundles]`, `[plugins]`) jadval ko'rinishida tavsiflang.

### 7-topshiriq <Badge type="danger" text="qiyin" />
`libs.versions.toml` fayliga JSON bilan ishlash uchun mashhur **Gson** kutubxonasini qo'shing:
- Versiya: `"2.10.1"`
- Guruh: `"com.google.code.gson"`
- Modul nomi: `"gson"`  
Kutubxonani `[versions]` va `[libraries]` bloklariga to'g'ri kiriting hamda `build.gradle` faylida chaqirish qatorini yozing.

### 8-topshiriq <Badge type="danger" text="qiyin" />
Kutubxonalar to'plami (Bundle) nima uchun kerak? Agar sizda 3 ta o'zaro bog'liq kutubxona bo'lsa, ularni `libs.versions.toml` da qanday qilib bitta `networking-bundle` nomiga birlashtirish mumkin?

### 9-topshiriq <Badge type="danger" text="qiyin" />
`libs.versions.toml` faylida e'lon qilingan `okhttp-logging-interceptor` kutubxonasi `build.gradle` faylida qanday sintaksisda chaqiriladi? Chiziqcha (`-`) belgisi Gradle faylida nima uchun nuqtaga (`.`) aylanadi?

### 10-topshiriq <Badge type="info" text="bonus" />
Android Studio'da yangi loyiha oching va unda quyidagi ishlarni bajaring:
1. `gradle/libs.versions.toml` fayliga kirib, mavjud kutubxonalar ro'yxatini ko'zdan kechiring;
2. `[versions]` bo'limiga `coil = "2.6.0"` qo'shing;
3. `[libraries]` bo'limiga `coil-compose = { group = "io.coil-kt", name = "coil-compose", version.ref = "coil" }` ni qo'shing;
4. `app/build.gradle` (yoki `.kts`) faylida `implementation libs.coil.compose` qilib ulang;
5. "Sync Now" tugmasini bosing va loyiha muvaffaqiyatli sinxronizatsiya bo'lganini tasdiqlang.

</div>

