---
title: "10-dars. Simulyator va Emulator: Real qurilma, ADB va Logcat"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "week": {"n": 4, "link": "/9-sinf-android/hafta-04/"}, "g": 10, "title": "Simulyator va Emulator: Real qurilma, ADB va Logcat", "lead": "Kompyuteringiz emulyatordan qiynalyaptimi yoki ilovangizni haqiqiy telefoningizda ushlab ko'rmoqchimisiz? Ushbu darsda o'z Android smartfoningizni dasturlash rejimiga o'tkazishni, ADB buyruqlari va Logcat vositasini o'rganamiz.", "slide": "/slaydlar/9-sinf-android/hafta-04/dars-1.html", "test": null, "tabs": [{"g": 10, "link": "/9-sinf-android/hafta-04/dars-1", "current": true}, {"g": 11, "link": "/9-sinf-android/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/9-sinf-android/hafta-04/dars-3", "current": false}], "prev": null, "next": {"g": 11, "title": "Kotlin sintaksisi: val vs var va ma’lumot turlari", "link": "/9-sinf-android/hafta-04/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Real qurilma afzalligi:** Emulyatorga qaraganda ancha tez ishlaydi, kompyuter xotirasini tejaydi va barcha sensorlar (kamera, GPS, akselerometr) haqiqiy ishlaydi.
- **Developer Options (Dasturchi sozlamalari):** Sozlamalar &rarr; *About Phone* &rarr; *Build Number* ustiga ketma-ket **7 marta** bosish orqali ochiladi.
- **USB Debugging (USB orqali nosozliklarni tuzatish):** Android Studio kompyuterdan telefonga ilovani to'g'ridan-to'g'ri o'rnatishi va boshqarishi uchun kerak.
- **ADB (Android Debug Bridge):** Kompyuter va telefon o'rtasidagi ko'prik vazifasini bajaruvchi buyruqlar satri vositasi (`Client`, `Server`, `Daemon`).
- **Logcat:** Android operatsion tizimi va ilovalar xabarlarini, xatolarini real vaqtda ko'rsatuvchi oyna.
- **Log darajalari:**
  - `Log.v()` &mdash; Verbose (barcha mayda xabarlar)
  - `Log.d()` &mdash; Debug (dasturchi sinov xabarlari)
  - `Log.i()` &mdash; Info (axborot)
  - `Log.w()` &mdash; Warn (ogohlantirish)
  - `Log.e()` &mdash; Error (xatolik)

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega "Build number" 7 marta bosiladi?
Google bu menyuni oddiy foydalanuvchilar bilmasdan telefon tizim sozlamalarini buzib qo'ymasliklari uchun yashirib qo'ygan. Faqat haqiqiy dasturchi yoki qiziquvchigina bu usulni bilib, tizimni ochadi.

### ADB simsiz (Wi-Fi orqali) ishlashi mumkinmi?
Ha! Android 11 va undan yuqori versiyalarda Android Studio'da *Pair Devices Using Wi-Fi* (QR-kod orqali) funksiyasi mavjud. Bu orqali kabel ulamasdan ham bir xil Wi-Fi tarmog'ida ilovani ishga tushirish mumkin.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Developer Options | Dasturchilar uchun yashirin tizim sozlamalari menyusi |
| USB Debugging | USB kabeli orqali ilovalarni boshqarish va testlash ruxsati |
| ADB | Android Debug Bridge &mdash; Android boshqaruv ko'prigi |
| Logcat | Tizim voqealari va xatolar jurnali oynasi |
| Crash | Dasturning kutilmagan xatolik tufayli to'xtab qolishi (qulashi) |
| RSA Key | Kompyuter va telefon o'rtasidagi xavfsiz ulanish raqamli kaliti |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Google Play do'koniga yuklanadigan barcha ilovalar nashrdan oldin yuzlab real qurilmalardan iborat maxsus "Firebase Test Lab" robot-fermalarida avtomatik sinovdan o'tkaziladi.
- Logcat har bir soniyada minglab tizim xabarlarini chiqaradi. Kerakli xabarni topish uchun `tag:MY_TAG` yoki `package:mine` filtrlari qo'llaniladi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

1. **Dasturchi rejimini yoqish · oson**  
   O'z Android smartfoningizda *Build Number* ustiga 7 marta bosib, *Developer Options* menyusini faollashtiring.

2. **USB Debugging ruxsati · oson**  
   Yangi ochilgan *Developer Options* menyusiga kirib, *USB Debugging* tugmachasini yoqing.

3. **Kompyuterga ulash · oson**  
   Smartfonni USB kabel orqali kompyuterga ulang va ekranga chiqqan *Allow USB Debugging?* oynasida *Always allow* qilib tasdiqlang.

4. **ADB bilan tekshirish · oson**  
   Android Studio'dagi *Terminal* oynasini ochib, `adb devices` buyrug'ini tering. Natijada qurilmangiz kodi va `device` so'zi chiqqanini tekshiring.

5. **Ilovani telefonda ishga tushirish · oson**  
   Android Studio yuqori panelida emulyator o'rniga o'z telefoningiz nomini tanlang va yashil `Run` (&blacktriangleright;) tugmasini bosing.

6. **Log.d xabarini qo'shish · o'rta**  
   `MainActivity.kt` fayliga `Log.d("MENING_ILOVAM", "Salom, bu mening birinchi log xabarim!")` kodini yozing.

7. **Logcat qidiruvidan foydalanish · o'rta**  
   Android Studio'dagi *Logcat* oynasini oching va qidiruv satriga `tag:MENING_ILOVAM` deb yozib, o'z xabaringizni toping.

8. **Log darajalari bilan tajriba · o'rta**  
   Dasturda bir vaqtning o'zida `Log.i()`, `Log.w()`, `Log.e()` xabarlarini yuboring va ularning Logcat oynasida qanday ranglarda (ko'k, sariq, qizil) chiqishini kuzating.

9. **Crash xatosini tahlil qilish · qiyin**  
   Kodingizga ataylab xato yozing (`val a = 5 / 0`) va ilovani ishga tushiring. Ilova yopilib ketgach, Logcat oynasidagi qizil xabardan xatolik qaysi fayl va qaysi qatorda bo'lganini aniqlang.

10. **Ekran o'lchamlarini logda chiqarish · bonus**  
    `resources.displayMetrics` yordamida telefoningiz ekran kengligi va balandligini pikselda aniqlab, `Log.i("EKRAN", "Kenglik: $width, Balandlik: $height")` ko'rinishida Logcat'ga chiqaring.

</div>

