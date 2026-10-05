---
title: "6-dars. Android Studio va Android SDK bilan tanishuv (1-qism)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "week": {"n": 2, "link": "/9-sinf-android/hafta-02/"}, "g": 6, "title": "Android Studio va Android SDK bilan tanishuv (1-qism)", "lead": "Android Studio va Android SDK bilan tanishuv (1-qism): Android Studio interfeysi, SDK Manager va SDK Build-Tools", "slide": "/slaydlar/9-sinf-android/hafta-02/dars-3.html", "test": "/slaydlar/9-sinf-android/hafta-02/dars-3-test.html", "tabs": [{"g": 4, "link": "/9-sinf-android/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/9-sinf-android/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/9-sinf-android/hafta-02/dars-3", "current": true}], "prev": {"g": 5, "title": "Android ekotizimi va Google xizmatlari (2-qism)", "link": "/9-sinf-android/hafta-02/dars-2"}, "next": null}
---

Bugungi darsda biz mobil ilovalar yaratishning eng asosiy quroli — **Android Studio** dasturi va uning yuragi hisoblangan **Android SDK** (Software Development Kit) bilan yaqindan tanishamiz. Dasturchilar kompyuter orqali telefonni qanday boshqarishi va ADB vositasi qanday ishlashini o'rganamiz.

---

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar

- **Android Studio** — Google tomonidan IntelliJ IDEA asosida yaratilgan, Android ilovalarini ishlab chiqishning rasmiy dasturlash muhiti (IDE).
- **Android SDK (Software Development Kit)** — operatsion tizim bilan muloqot qilish, kodni kompilyatsiya qilish va ilovani yig'ish vositalari to'plami.
- **SDK Platforms** — har bir Android versiyasi (Android 14, 15) uchun mo'ljallangan tizim kutubxonalari.
- **ADB (Android Debug Bridge)** — kompyuter bilan Android smartfon o'rtasida aloqa o'rnatuvchi universal buyruqlar ko'prigi.
- **aapt2** — XML maketlar va rasmlarni binar formatga paketlovchi maxsus vosita.
- **d8 / r8** — Java baytkodini Android Runtime tushunadigan `.dex` kodiga aylantiruvchi va kodni optimallashtiruvchi zamonaviy kompilyator.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. Android Studio: Dasturchining bosh ustaxonasi

Android Studio — bu oddiy matn muharriri emas, balki mobil dasturchiga kerak bo'ladigan barcha asboblarni yagona oynada birlashtirgan qudratli majmuadir:
- **Intellektual kod muharriri:** Siz kod yozayotganingizda maslahatlar beradi va xatolarni darhol qizil to'lqinli chiziq bilan ko'rsatadi;
- **Layout Editor:** Ekranni xuddi rasm chizgandek vizual yoki to'g'ridan-to'g'ri kod orqali loyihalash imkonini beradi;
- **Logcat konsoli:** Telefondagi barcha jarayonlar, hodisalar va dastur xatolarini real vaqtda kuzatish oynasi;
- **Gradle avtomatlashtirish tizimi:** Barcha kutubxonalarni internetdan avtomatik yuklab olib, loyihani yig'ib beradi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. Android SDK arxitekturasi: 3 ta asosiy ustun

Android SDK loyihani yozishdan to uni telefonda ishga tushirishgacha bo'lgan barcha bosqichlarga javob beradi:

```
+-------------------------------------------------------+
|                    Android SDK                        |
+-------------------------------------------------------+
| 1. SDK Platforms     | Android 14, 15 API kutubxonalari|
| 2. Platform-Tools    | ADB (Android Debug Bridge)      |
| 3. Build-Tools       | aapt2, d8/r8 kompilyatorlari    |
+-------------------------------------------------------+
```

### 1. SDK Platforms
Har bir Android versiyasining o'z API raqami bo'ladi (masalan, Android 14 — bu API 34). Agar siz eng yangi imkoniyatlardan foydalanmoqchi bo'lsangiz, SDK Manager orqali o'sha versiyaning platformasini yuklab olasiz.

### 2. SDK Platform-Tools va ADB
**ADB (Android Debug Bridge)** — dasturchi uchun eng sevimli qurol! U kompyuter terminali orqali telefon bilan muloqot qiladi:
- `adb devices` — kompyuterga ulangan barcha telefonlarni ko'rsatadi;
- `adb install app.apk` — kompyuterdagi ilovani telefonga o'rnatadi;
- `adb logcat` — telefon xotirasidagi barcha xabarlarni terminalda chiqaradi;
- `adb shell` — telefonning ichki Linux tizimiga kirish imkonini beradi.

### 3. SDK Build-Tools
Kodni haqiqiy ishchi ilovaga aylantiruvchi "zavod":
- **`aapt2`:** Barcha XML interfeys fayllari va rasmlarni tekshirib, binar shaklga keltiradi;
- **`d8`:** Kompyuter baytkodini Android telefoni tushunadigan `.dex` fayliga o'giradi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. SDK Manager nima?

Android Studio yuqori panelida joylashgan **SDK Manager** oynasi orqali siz:
- Yangi Android versiyalarini o'rnatishingiz;
- Build-Tools yangilanishlarini yuklab olishingiz;
- Virtual telefon (Emulator) drayverlarini boshqarishingiz mumkin.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

1. **Android Studio qaysi dastur asosida yaratilgan?** `· oson`  
   Android Studio qaysi kompaniyaning qaysi IDE dasturi negizida ishlab chiqilganini va Google nega aynan shu muhitni tanlaganini yozing.

2. **SDK Platforms nima uchun kerak?** `· oson`  
   SDK Manager oynasida "Android 14 (API 34)" yozuvi nimani anglatishini tushuntiring.

3. **ADB qisqartmasi ma'nosi** `· oson`  
   ADB so'zining to'liq inglizcha va o'zbekcha nomini daftaringizga yozing.

4. **adb devices buyrug'ini tahlil qiling** `· o'rta`  
   Kompyuteringizga telefonni USB kabel orqali ulab, terminalda `adb devices` buyrug'ini yozsangiz, u qanday ma'lumotni chiqarib beradi?

5. **aapt2 vositasining roli** `· o'rta`  
   Nima uchun ilovadagi XML dizayn fayllari to'g'ridan-to'g'ri emas, balki `aapt2` orqali binar formatga paketlanishi kerak?

6. **d8 va r8 farqi** `· o'rta`  
   Java baytkodini `.dex` kodiga o'giruvchi `d8` va undan ham aqlli bo'lgan `r8` (keraksiz kodni o'chiruvchi) kompilyatori vazifasini tushuntiring.

7. **SDK ning 3 ta asosiy ustunini chizing** `· o'rta`  
   SDK Platforms, SDK Platform-Tools va SDK Build-Tools o'rtasidagi bog'liqlikni sxematik bloklar ko'rinishida tasvirlang.

8. **Logcat nima uchun kerak?** `· qiyin`  
   Ilovangiz telefonda to'satdan yopilib ketganda (Crash bo'lganda), dasturchi xatoning aynan qaysi qatorda ekanini qaysi oyna orqali topadi? Bu jarayon qanday nomlanadi?

9. **Terminal orqali APK o'rnatish** `· qiyin`  
   Dasturchi kompyuterida turgan `game.apk` faylini USB orqali ulangan smartfonga sichqonchasiz, faqat ADB buyrug'i orqali qanday o'rnatishi mumkin? Aniq buyruq sintaksisini yozing.

10. **Tadqiqotchi dasturchi** `· bonus`  
    Kompyuteringiz operatsion tizimida `ANDROID_HOME` tizim o'zgaruvchisi (Environment Variable) nima uchun kerak? Agar bu o'zgaruvchi sozlanmasa, terminalda qanday xatolik yuzaga keladi?

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Android Studio dastlab 2013-yilda Google I/O anjumanida e'lon qilingan. Bungacha barcha Android dasturchilari "Eclipse" nomli dasturda ishlashga majbur edilar. Android Studio Eclipse'dan 10 barobar qulayroq va tezroq bo'lib chiqdi!
- ADB yordamida hatto ekrani sinib qolgan va sensorli teginish ishlamayotgan Android telefonini kompyuter klaviaturasi orqali to'liq boshqarish va undagi barcha rasmlarni kompyuterga ko'chirib olish mumkin!

---

</div>

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Android Studio — Android ilovalari yaratish uchun Google va JetBrains tomonidan ishlab chiqilgan rasmiy dasturdir.
- Android SDK 3 ta asosiy ustunga ega: SDK Platforms (tizim kutubxonalari), Platform-Tools (ADB) va Build-Tools (aapt2, d8).
- ADB kompyuter va telefon o'rtasidagi xavfsiz ko'prik bo'lib, ilovalarni o'rnatish va diagnostika qilish imkonini beradi.
- `aapt2` resurslarni paketlaydi, `d8` esa kodni `.dex` baytkodiga aylantiradi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Android Studio qaysi IDE negizida yaratilgan?
2. Android SDK tarkibidagi 3 ta asosiy komponentni ayting.
3. ADB yordamida telefonga ilovani qanday buyruq bilan o'rnatiladi?
4. `aapt2` vositasi nima vazifa bajaradi?
5. `d8` kompilyatori kodni qaysi formatga o'tkazadi?

</div>

