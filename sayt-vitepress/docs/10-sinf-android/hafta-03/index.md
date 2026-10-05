---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Android)", "link": "/10-sinf-android/"}, "n": 3, "bob": "I-bob · Android loyihalarini boshqarish va versiya nazorati tizimlari", "lessons": [{"g": 13, "title": "7-dars: Git bilan versiya nazorati asoslari", "lead": "build.gradle faylining asosiy tuzilmasi va modullararo bog‘lanishi", "link": "/10-sinf-android/hafta-03/dars-7", "slide": "/slaydlar/10-sinf-android/hafta-03/dars-7.html", "test": "/slaydlar/10-sinf-android/hafta-03/dars-7-test.html"}, {"g": 14, "title": "8-dars: Git bilan ishlash amaliyoti (Tarmoqlar va Konfliktlar)", "lead": ">>>>>> feature-api", "link": "/10-sinf-android/hafta-03/dars-8", "slide": "/slaydlar/10-sinf-android/hafta-03/dars-8.html", "test": "/slaydlar/10-sinf-android/hafta-03/dars-8-test.html"}, {"g": 15, "title": "9-dars: GitHub’da loyihalar yaratish va boshqarish", "lead": "Gradle yordamida kutubxonalarni ulash va versiyalarni boshqarish ko‘nikmasiga ega bo‘ladi;", "link": "/10-sinf-android/hafta-03/dars-9", "slide": "/slaydlar/10-sinf-android/hafta-03/dars-9.html", "test": "/slaydlar/10-sinf-android/hafta-03/dars-9-test.html"}], "test": "/slaydlar/10-sinf-android/hafta-03/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar to'plami. Har bir vazifa 25–30 daqiqaga mo'ljallangan.

---

### 7-dars: Git bilan versiya nazorati asoslari

1. Kompyuteringiz terminalida `git config --list` buyrug'ini ishga tushiring va ismingiz hamda pochtangiz to'g'ri sozlanganini tasdiqlang.
2. Yangi papka ochib, `git init` orqali ombor yarating.
3. Loyihada `.gitignore` faylini ochib, Android uchun eng zarur qoidalarni kiriting:
   - `.gradle/`, `build/`, `app/build/`
   - `local.properties`
   - `*.apk`, `*.aab`
4. Kamida 3 ta turli fayl yaratib, ketma-ket 3 ta ma'noli commitni (`feat: ...`, `fix: ...`, `docs: ...`) amalga oshiring va `git log --oneline` buyrug'i natijasini ko'ring.

---

### 8-dars: Git bilan ishlash amaliyoti (Tarmoqlar va Konfliktlar)

1. Loyihangizda `feature-settings` nomli yangi branch oching (`git switch -c feature-settings`).
2. Yangi branchda `AppSettings.kt` faylini yarating va unga boshlang'ich sozlamalarni yozib commit qiling.
3. Asosiy `main` tarmog'iga qaytib (`git switch main`), o'zgarishlarni `git merge feature-settings` buyrug'i bilan birlashtiring. So'ngra eski branchni `git branch -d feature-settings` orqali o'chiring.
4. Bitta fayl ichida sun'iy to'qnashuv (Merge Conflict) hosil qiling, uni qo'lda to'g'rilab, to'qnashuv belgilarini o'chirib, muvaffaqiyatli merge commitini amalga oshiring.

---

### 9-dars: GitHub’da loyihalar yaratish va boshqarish

1. O'zingizning shaxsiy GitHub akkauntingizda yangi Public repozitoriy yarating.
2. Lokal kompyuteringizdagi Android loyihasini masofaviy GitHub repozitoriyasiga ulang (`git remote add origin ...`) va barcha commitlarni `git push -u origin main` orqali yuklang.
3. Loyihangiz uchun Markdown formatida chiroyli va tushunarli `README.md` faylini yozing:
   - Loyiha nomi va vazifasi;
   - Ishlatilgan kutubxonalar va texnologiyalar;
   - Qanday o'rnatish va ishga tushirish bo'yicha qo'llanma.
4. Repozitoriyda 2 ta yangi "Issue" oching: biri rejadagi funksiya haqida, ikkinchisi xatolik haqida. Ulardan birini commit xabarida `fixes #...` deb yozish orqali avtomatik yoping.

---

</div>
