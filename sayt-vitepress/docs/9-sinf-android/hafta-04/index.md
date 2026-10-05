---
title: "4-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "n": 4, "bob": "I-bob · Android muhiti va dasturlash asoslari", "lessons": [{"g": 10, "title": "Simulyator va Emulator: Real qurilma, ADB va Logcat", "lead": "Kompyuteringiz emulyatordan qiynalyaptimi yoki ilovangizni haqiqiy telefoningizda ushlab ko'rmoqchimisiz? Ushbu darsda o'z Android smartfoningizni dasturlash rejimiga o'tkazishni, ADB buyruqlari va Logcat vositasini o'rganamiz.", "link": "/9-sinf-android/hafta-04/dars-1", "slide": "/slaydlar/9-sinf-android/hafta-04/dars-1.html", "test": null}, {"g": 11, "title": "Kotlin sintaksisi: val vs var va ma’lumot turlari", "lead": "Android ilovalar yozishning rasmiy tili &mdash; Kotlin bilan tanishishga tayyormisiz? Ushbu darsda o'zgaruvchilarni e'lon qilish, val va var farqi hamda String shablonlarini o'rganamiz.", "link": "/9-sinf-android/hafta-04/dars-2", "slide": "/slaydlar/9-sinf-android/hafta-04/dars-2.html", "test": null}, {"g": 12, "title": "Kotlin sintaksisi: if va when shart operatorlari", "lead": "Dasturda qarorlar qabul qilish va shartlar bo'yicha turli amallarni bajarish vaqti keldi! Ushbu darsda Kotlindagi if-else ifodalari hamda eng qudratli when operatorini o'rganamiz.", "link": "/9-sinf-android/hafta-04/dars-3", "slide": "/slaydlar/9-sinf-android/hafta-04/dars-3.html", "test": null}], "test": null}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

### 10-dars. Simulyator va Emulator (2-qism): Real qurilma, ADB va Logcat
1. O'z Android telefoningizda *Developer Options* va *USB Debugging* rejimini faollashtiring.
2. Android Studio'dagi *Terminal* oynasidan `adb devices` buyrug'ini ishga tushirib, telefoningiz ro'yxatda chiqqan holati skrinshotini oling.
3. `MainActivity.kt` faylida `Log.i("UY_IShI", "Ilova real telefonda muvaffaqiyatli ishga tushdi!")` kodini qo'shib, Logcat oynasidan shu xabarni topib skrinshot qiling.

---

### 11-dars. Kotlin sintaksisi (1-qism): val vs var va ma’lumot turlari
1. `val` va `var` yordamida o'z smartfoningiz haqidagi ma'lumotlarni (modeli: String, narxi: Double, xotirasi_GB: Int, quvvat_foizi: Int, kamera_bormi: Boolean) saqlovchi Kotlin dasturini yozing.
2. 3 ta fandan olingan baholarning o'rtacha arifmetik qiymatini hisoblab, `println("O'rtacha baho: ${...}")` shabloni orqali chiqaring.
3. String ko'rinishidagi narxni (`val narx = "150000"`) `toInt()` orqali butun songa o'tkazib, 12% QQS qo'shilgan yakuniy to'lov miqdorini hisoblang.

---

### 12-dars. Kotlin sintaksisi (2-qism): if va when shart operatorlari
1. Foydalanuvchi yoshiga qarab toifani (`"Bola"`, `"O'smir"`, `"Katta"`, `"Keksa"`) aniqlovchi dasturni `when (yosh)` va `in 1..12`, `in 13..18`, `in 19..60`, `else` orqali yozing.
2. Mini-Kalkulyator dasturi: ikkita son `a = 20.0`, `b = 5.0` va amal belgisi `amal = "*"` berilganda `when (amal)` yordamida to'rtala arifmetik amalni (`+`, `-`, `*`, `/`) bajaring.
3. Do'kondagi chegirma tizimi: Xarid summasiga qarab chegirma miqdorini aniqlang (100 minggacha &mdash; 0%, 500 minggacha &mdash; 5%, 1 milliongacha &mdash; 10%, 1 milliondan yuqori &mdash; 15%) va yakuniy to'lov summasini chiqaring.

---

</div>
