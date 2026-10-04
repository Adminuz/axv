---
title: "7-dars. Android Studio va Android SDK bilan tanishuv (2-qism)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "week": {"n": 3, "link": "/9-sinf-android/hafta-03/"}, "g": 7, "title": "Android Studio va Android SDK bilan tanishuv (2-qism)", "lead": "Android Studio va Android SDK bilan tanishuv (2-qism): Loyiha strukturasi (java/kotlin, res, AndroidManifest.xml, Gradle)", "slide": "/slaydlar/9-sinf-android/hafta-03/dars-1.html", "tabs": [{"g": 7, "link": "/9-sinf-android/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/9-sinf-android/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf-android/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "Android Studio va Android SDK bilan tanishuv (3-qism)", "link": "/9-sinf-android/hafta-03/dars-2"}}
---

Bugungi darsda biz Android Studio loyihasining ichki tuzilishi — ya'ni loyiha papkalari nima uchun kerakligini o'rganamiz. Kotlin kodi qayerda yoziladi, rasmlar va dizaynlar qayerda saqlanadi, `AndroidManifest.xml` fayli nega ilovaning "miyasi" deb atalishini bilib olamiz.

---

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar

- **Loyiha daraxti (Project Structure)** — loyihadagi barcha kodlar, dizaynlar va sozlamalar tartiblangan fayllar ierarxiyasi.
- **`java/` (yoki `kotlin/`)** — ilovaning mantiqiy algoritmlari va dastur kodi (`MainActivity.kt`) saqlanadigan asosiy papka.
- **`res/` (Resources)** — ilovaning barcha vizual materiallari (ekran maketlari, rasmlar, ranglar, matnlar) jildi.
- **`strings.xml`** — ilovadagi barcha so'z va jumlalarni saqlash hamda bir nechta tilga tarjima qilish uchun maxsus fayl.
- **`AndroidManifest.xml`** — ilovaning pasporti; unda ruxsatnomalar, ilova ikonkasi va boshlang'ich ochiluvchi ekran e'lon qilinadi.
- **`build.gradle`** — ilovaning versiyasi (`minSdk`, `targetSdk`) va tashqi kutubxonalarni boshqaruvchi skript.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. Loyihaning 4 ta asosiy qismi

Android Studio loyihasini ochganingizda, chap tomonda 4 ta asosiy bo'limni ko'rasiz:

```
MyApp/
├── manifests/              <-- AndroidManifest.xml (ilovaning miyasi)
├── java/                   <-- MainActivity.kt (dastur kodi)
├── res/                    <-- Dizayn maketlari, rasmlar va matnlar
└── Gradle Scripts/         <-- Loyiha sozlamalari va kutubxonalar
```

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. `res/` (Resources) jildi: Dizayn xazinasi

Androidda qat'iy qoida bor: **dastur kodi va vizual dizayn alohida saqlanishi kerak!**
- **`res/layout/`:** Ekranning XML dizayn maketlari saqlanadi (masalan, `activity_main.xml`). Tugmalar, matnlar qayerda turishi shu yerda chiziladi.
- **`res/drawable/`:** Ilovada ishlatiladigan barcha rasmlar, fonlar va vektor ikonlar.
- **`res/values/strings.xml`:** Ilovadagi matnlar:
  ```xml
  &lt;resources>
      &lt;string name="app_name">Mening Birinchi Ilovam&lt;/string>
      &lt;string name="btn_login">Tizimga kirish&lt;/string>
  &lt;/resources>
  ```
  Matnlarni alohida faylda saqlash ilovani o'zbek, rus va ingliz tillariga bir zumda tarjima qilish imkonini beradi!
- **`res/values/colors.xml`:** Ilovaning ranglar palitrasi (HEX formatida).

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. `AndroidManifest.xml`: Ilovaning pasporti

Operatsion tizim ilovani ishga tushirishdan oldin aynan ushbu faylni o'qiydi:
1. **Ruxsatnomalar:** Ilova internet, kamera yoki GPS'dan foydalanishi uchun ruxsat e'lon qilinadi:
   ```xml
   &lt;uses-permission android:name="android.permission.INTERNET" />
   ```
2. **Ilova atributlari:** Ilova nomi, ikonkasi va dizayn mavzusi.
3. **Boshlang'ich ekran (Launcher):** Telefon menyusidagi ikonka bosilganda birinchi qaysi ekran ochilishi:
   ```xml
   &lt;intent-filter>
       &lt;action android:name="android.intent.action.MAIN" />
       &lt;category android:name="android.intent.category.LAUNCHER" />
   &lt;/intent-filter>
   ```

---

</div>

<div class="blk">

## <Icon name="file-text" /> 4. Gradle sozlamalari: `minSdk`, `targetSdk`, `compileSdk`

Modul darajasidagi `build.gradle` faylida uchta muhim ko'rsatkich mavjud:
- **`minSdk` (Minimal SDK):** Ilova ishlay oladigan eng pastki Android versiyasi (masalan, 24 — Android 7.0). Ushbu versiyadan eski telefonlarga ilova o'rnatilmaydi.
- **`targetSdk`:** Ilova eng so'nggi qaysi Android talablariga moslab sinovdan o'tkazilgani (masalan, 34).
- **`compileSdk`:** Loyihani yig'ishda qaysi Android SDK vositasidan foydalanilayotgani.
- **`dependencies`:** Loyihaga tashqi kutubxonalarni (masalan, rasm yuklovchi Glide yoki ma'lumotlar bazasi Room) ulash bo'limi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

1. **Loyiha papkalarini sanang** `· oson`  
   Android Studio loyihasidagi 4 ta asosiy katalog nomini yozing.

2. **Dastur kodi qayerda yoziladi?** `· oson`  
   Kotlin yoki Java fayllari loyihaning qaysi papkasida joylashadi?

3. **strings.xml faylining foydasi** `· oson`  
   Nima uchun matnlarni kod ichida to'g'ridan-to'g'ri yozib ketmasdan, `strings.xml` faylida saqlash tavsiya etiladi?

4. **Ekran dizaynlari qayerda saqlanadi?** `· o'rta`  
   Ilova ekranlarining XML maketlari qaysi jildda turishini va fayl kengaytmasini yozing.

5. **Internet ruxsatnomasi kodi** `· o'rta`  
   Ilovangiz internetdan ma'lumot yuklashi uchun `AndroidManifest.xml` fayliga qaysi ruxsatnoma qatori qo'shilishi kerak? Kodini yozing.

6. **minSdk va eski telefonlar** `· o'rta`  
   Agar loyihada `minSdk = 26` (Android 8.0) deb belgilangan bo'lsa, Android 7.0 o'rnatilgan telefonga bu ilovani Google Play'dan o'rnatib bo'ladimi? Nega?

7. **Boshlang'ich ekranni aniqlang** `· o'rta`  
   `AndroidManifest.xml` faylida aynan qaysi ikki kalit so'z ekranning asosiy boshlang'ich oyna (Launcher) ekanligini bildiradi?

8. **dependencies bloki tahlili** `· qiyin`  
   `build.gradle` faylidagi `dependencies` bo'limi nima vazifa bajaradi? Unga yangi kutubxona qo'shilgach, Android Studio'da qaysi tugmani (harakatni) bosish shart?

9. **Kop tilli ilova yaratish keysi** `· qiyin`  
   Ilovangiz ham o'zbek, ham ingliz tilida ishlashi uchun `res/` jildi ichida qanday papkalar va fayllar yaratilishi kerakligini tushuntiring.

10. **Tadqiqotchi dasturchi** `· bonus`  
    `versionCode` va `versionName` farqini tushuntiring. Nima uchun Google Play do'koni `versionName` ga emas, aynan `versionCode` raqamiga qarab yangilanishni aniqlaydi?

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Android tizimida dunyo tillarini qo'llab-quvvatlash juda oson: agar siz `res/values-uz/strings.xml` va `res/values-ru/strings.xml` fayllarini yaratsangiz, foydalanuvchi telefon tilini o'zgartirishi bilan ilova tili ham bir zumda avtomatik o'zgaradi!
- `AndroidManifest.xml` faylida agar bitta harf yoki yopuvchi teg noto'g'ri yozilsa, butun ilova ishga tushmaydi va qizil xatolik beradi. Shuning uchun dasturchilar bu faylni "muqaddas kodeks" deb ham atashadi.

---

</div>

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Android loyihasi aniq arxitekturaga ega: kod `java/`da, dizayn va matnlar `res/`da, pasport esa `manifests/`da saqlanadi.
- `strings.xml` ko'p tilli ilovalar yaratishning asosi hisoblanadi.
- `AndroidManifest.xml` ilovaning barcha huquqlari va kirish ekranini e'lon qiladi.
- `build.gradle` ilovaning minimal versiyasi (`minSdk`) va kerakli kutubxonalarini belgilaydi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Ekran XML fayllari qaysi jildda saqlanadi?
2. `strings.xml` fayli qaysi papkada joylashgan?
3. Ilovaning pasporti hisoblangan fayl qanday nomlanadi?
4. `minSdk` ko'rsatkichi nimani anglatadi?
5. Yangi ruxsatnomalar qaysi faylga yoziladi?

</div>

