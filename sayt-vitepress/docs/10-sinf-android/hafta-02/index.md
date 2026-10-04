---
title: "2-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Android)", "link": "/10-sinf-android/"}, "n": 2, "bob": "I-bob · Android loyihalarini boshqarish va versiya nazorati tizimlari", "lessons": [{"g": 7, "title": "4-dars: Dependency management va ziddiyatlarni hal qilish", "lead": "Git bilan versiya nazorati asoslari: Git repository, commit, log, .gitignore", "link": "/10-sinf-android/hafta-02/dars-4", "slide": "/slaydlar/10-sinf-android/hafta-02/dars-4.html"}, {"g": 8, "title": "5-dars: ProGuard va R8 yordamida kodni optimallashtirish (1-qism)", "lead": "Git bilan ishlash amaliyoti: fayllar holati, diff, checkout, reset, revert", "link": "/10-sinf-android/hafta-02/dars-5", "slide": "/slaydlar/10-sinf-android/hafta-02/dars-5.html"}, {"g": 9, "title": "6-dars: ProGuard va R8 qoidalari bilan ishlash (2-qism: Amaliyot)", "lead": "GitHub’da loyihalar yaratish va boshqarish: remote repozitoriy, push, pull, issues, README", "link": "/10-sinf-android/hafta-02/dars-6", "slide": "/slaydlar/10-sinf-android/hafta-02/dars-6.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar to'plami. Har bir vazifa 25–30 daqiqaga mo'ljallangan.

---

### 4-dars: Dependency management va ziddiyatlarni hal qilish (Tranzitiv bog'liqliklar)

1. Android Studio loyihangiz terminalida `./gradlew app:dependencies --configuration releaseRuntimeClasspath` buyrug'ini ishga tushiring.
2. Natijada chiqqan bog'liqliklar daraxtidan bitta tranzitiv bog'liqlikni (masalan, `androidx.core:core` yoki `kotlinx-coroutines`) aniqlang va u qaysi asosiy kutubxona orqali loyihaga kirib kelganini daftaringizga yozing.
3. Loyihada sun'iy ravishda versiya ziddiyati hosil qiling va `app/build.gradle` faylida `exclude group:` yoki `resolutionStrategy.force` yordamida uni yagona barqaror versiyaga moslashtiring.

---

### 5-dars: ProGuard va R8 yordamida kodni optimallashtirish (1-qism)

1. Android Studio'da `app/build.gradle` (yoki `.kts`) faylini oching va `buildTypes.release` blokiga quyidagi sozlamalarni kiriting:
   - `isMinifyEnabled = true` (yoki Groovy'da `minifyEnabled true`)
   - `isShrinkResources = true` (yoki Groovy'da `shrinkResources true`)
2. Terminalda `./gradlew assembleRelease` buyrug'i orqali Release APK hosil qiling.
3. Android Studio menyusidan **Build > Analyze APK...** bo'limini oching va yaratilgan Release APK'ni kiring:
   - Debug va Release APK hajmini solishtiring;
   - `classes.dex` ichidagi klass nomlari qanday qisqarganini (masalan, `a.b.c`) ko'zdan kechiring.

---

### 6-dars: ProGuard va R8 qoidalari bilan ishlash (2-qism: Amaliyot)

1. Loyihangizda serverdan keladigan ma'lumotlar uchun kamida 2 ta data class yarating:
   - `UserProfile(val id: Long, val name: String, val role: String)`
   - `OrderDetails(val orderId: String, val totalSum: Double)`
2. `UserProfile` klassini `app/proguard-rules.pro` faylida `-keep class ... { *; }` qoidasi orqali himoyalang.
3. `OrderDetails` klassiga esa `androidx.annotation.Keep` kutubxonasidagi `@Keep` annotatsiyasini qo'llang.
4. Loyihani qayta Release build qiling va `app/build/outputs/mapping/release/mapping.txt` faylini ochib, ushbu klasslar qanday saqlanganini tekshiring.

---

</div>
