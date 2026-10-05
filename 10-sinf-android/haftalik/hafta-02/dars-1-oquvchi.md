# 4-dars: Dependency management va ziddiyatlarni hal qilish

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** Dependency management va ziddiyatlarni hal qilish: Tranzitiv bog'liqliklar, exclude, resolutionStrategy va BOM  

---

## Darsning qisqacha mazmuni

Katta hajmdagi mobil loyihalarda o'nlab kutubxonalar ishlatiladi va ularning har biri o'z navbatida boshqa kichik modullarga tayanadi. Ushbu darsda biz murakkab bog'liqliklar zanjirini tushunish va versiyalar to'qnashuvini bartaraf etishni o'rganamiz:

1. **Tranzitiv bog'liqliklar (Transitive Dependencies):**
   - Kutubxonaning o'zi talab qiladigan va loyihaga avtomatik kirib keladigan yordamchi modullar zanjiri (masalan: Retrofit $\to$ OkHttp $\to$ Okio);
   - Loyihaning kutilmaganda og'irlashib ketishi yoki versiyalar ziddiyatiga sabab bo'lishi mumkin.
2. **Versiya ziddiyatlari (Conflicts) va Gradle strategiyasi:**
   - Turli kutubxonalar bitta modulning turli versiyasini so'raganda, Gradle odatda eng yuqori (Newest) versiyani tanlaydi;
   - Agar yangi versiyada eski metodlar olib tashlangan bo'lsa, `NoSuchMethodError` kabi runtime xatoliklar yuzaga keladi.
3. **Bog'liqliklar daraxti (Dependency Tree):**
   - Terminal orqali `./gradlew app:dependencies` buyrug'i bilan barcha yashirin modullarni ko'rish va tahlil qilish.
4. **Ziddiyatlarni bartaraf etish mexanizmlari:**
   - **`exclude` qoidasi:** Ortiqcha yoki eskirgan tranzitiv modulni chiqarib tashlash (`exclude group: '...', module: '...'`);
   - **`resolutionStrategy.force`:** Butun loyiha bo'ylab bitta qat'iy versiyani majburlash;
   - **BOM (Bill of Materials):** Firebase va Compose uchun barcha modullarning 100% mos versiyalari xaritasini avtomatik ta'minlovchi platforma.

---

## Mustaqil bajarish uchun amaliy topshiriqlar

Quyidagi 10 ta amaliy vazifani diqqat bilan o'rganing va ularni Android Studio muhitida hamda daftaringizda bajaring:

### 1-topshiriq · oson
Tranzitiv bog'liqlik (Transitive Dependency) nima ekanini oddiy hayotiy misol (masalan, mashina sotib olganda uning ichidagi ehtiyot qismlar) yordamida tushuntiring.

### 2-topshiriq · oson
Android Studio terminalida `./gradlew app:dependencies` buyrug'i nima natija qaytaradi? Loyihangizda qaysi kutubxona qanday yordamchi modullarni sudrab kelganini bilish nega muhim?

### 3-topshiriq · oson
Agar bitta loyihada `Kutubxona A` OkHttp `3.12.0` ni, `Kutubxona B` esa OkHttp `4.10.0` ni talab qilsa, Gradle standart holda qaysi versiyani tanlaydi?

### 4-topshiriq · o'rta
Gradle avtomatik ravishda eng yuqori versiyani tanlagan taqdirda ham ilovada nega kutilmagan runtime crash (to'xtab qolish) xatoliklari kelib chiqishi mumkin?

### 5-topshiriq · o'rta
`build.gradle` faylida `exclude` parametri nima vazifani bajaradi? U qaysi hollarda qo'llaniladi?

### 6-topshiriq · o'rta
Loyihangizga quyidagi kutubxona ulangan:
```groovy
implementation 'com.example.library:network-tool:3.0.0'
```
Ushbu kutubxona ichidagi `commons-logging` modulini loyihadan butunlay chiqarib tashlash uchun `exclude` qoidasini yozing.

### 7-topshiriq · qiyin
BOM (Bill of Materials) tushunchasini tushuntiring. Nima uchun Firebase kutubxonalarini ulayotganda alohida modullarda (masalan, `firebase-auth`, `firebase-firestore`) versiya raqami yozilmaydi?

### 8-topshiriq · qiyin
Agar sizning loyihangizda barcha modullar uchun `kotlinx-coroutines-core` kutubxonasining aynan `1.8.0` versiyasidan foydalanish qat'iy talab etilsa, `configurations.all` va `resolutionStrategy.force` yordamida ushbu shartni qanday ta'minlash mumkin? Kod namunasini yozing.

### 9-topshiriq · qiyin
`./gradlew app:dependencies` natijasida chiqqan `com.squareup.okio:okio:2.8.0 -> 3.0.0 (*)` yozuvi nimani anglatadi? Strelka (`->`) va yulduzcha `(*)` belgilarining ma'nosi nima?

### 10-topshiriq · bonus
Android Studio'da yangi loyiha oching. Terminalda `./gradlew app:dependencies --configuration releaseRuntimeClasspath` buyrug'ini ishga tushiring:
1. Chiqqan bog'liqliklar daraxtidan bitta tranzitiv kutubxonani aniqlang;
2. Ushbu kutubxona qaysi asosiy modul tomonidan chaqirilganini yozing;
3. `build.gradle` faylida ushbu tranzitiv modulni `exclude` qilib ko'ring va qayta sinxronizatsiya qilib natijani tekshiring.
