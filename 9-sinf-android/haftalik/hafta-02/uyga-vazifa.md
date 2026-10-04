# 2-hafta: Uyga vazifalar to'plami (Android dasturlash)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

## 4-dars. Android ekotizimi va Google xizmatlari (1-qism)
1. AOSP va GMS tushunchalari o'rtasidagi asosiy farqlarni ko'rsatuvchi taqqoslash jadvali tuzing (litsenziya, narxi, tarkibi).
2. Nima sababdan telefon batareyasini tejash uchun ilovalar to'g'ridan-to'g'ri GPS'ga emas, balki Google Play Services tarkibidagi Fused Location Provider'ga murojaat qiladi?
3. Huawei smartfonlarida GMS o'rniga qanday muqobil tizim ishlatilishini va dasturchi bu muammoni kod orqali qanday hal qilishini yozma bayon qiling.

---

## 5-dars. Android ekotizimi va Google xizmatlari (2-qism)
1. Shaxsiy tasavvuringizdagi mobil ilova uchun to'g'ri va unikal `applicationId` yozing (masalan, `uz.edu.myquiz`). Nega ushbu nomni keyinchalik o'zgartirib bo'lmasligini tushuntiring.
2. Terminalda SHA-1 barmoq izini olish buyrug'ini yozing va ushbu kalit nima maqsadda ishlatilishini tushuntiring.
3. Maxfiy API kalitlarini (masalan, Google Maps API key) nima uchun ochiq kodda qoldirish xavfli va ularni `local.properties`da saqlashning afzalligi nimada?
4. APK va AAB formatlari o'rtasidagi farqni tushuntiring: Dynamic Delivery qanday qilib ilova hajmini 30–50% ga qisqartiradi?

---

## 6-dars. Android Studio va Android SDK bilan tanishuv
1. Android Studio interfeysidagi 4 ta asosiy ishchi oynani (Project Explorer, Editor, Logcat, Gradle) va ularning vazifalarini daftaringizga yozing.
2. Android SDK arxitekturasining 3 ta asosiy ustunini (SDK Platforms, Platform-Tools, Build-Tools) chizib, har biriga bittadan misol keltiring.
3. ADB vositasining 3 ta eng muhim buyrug'ini (`adb devices`, `adb install`, `adb logcat`) yozing va nima ish qilishini bayon qiling.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **AOSP va GMS ekotizimi tahlili (30 ball):**
   - AOSP va GMS farqini to'g'ri tushuntirishi (10 ball);
   - Google Play Services, Fused Location va FCM vazifalarini bilishi (10 ball);
   - GMS bo'lmagan qurilmalar uchun muqobil yechimlarni asoslashi (10 ball).

2. **Identifikatsiya, xavfsizlik va paketlash (35 ball):**
   - `applicationId` va SHA-1 barmoq izi vazifasini tushunishi (10 ball);
   - `google-services.json` fayli va `local.properties` xavfsizlik qoidalarini bilishi (15 ball);
   - APK va AAB farqi hamda Dynamic Delivery mexanizmini to'g'ri ifodalashi (10 ball).

3. **Android Studio va SDK bilimlari (35 ball):**
   - Android Studio oynalari vazifalarini ajrata olishi (10 ball);
   - SDK Platforms, Platform-Tools va Build-Tools farqini tushunishi (15 ball);
   - `aapt2`, `d8` va ADB buyruqlarining amaliy ahamiyatini bilishi (10 ball).

### Kutiladigan namunaviy natijalar
- O'quvchi API kalitlarni ochiq kodda qoldirish xavfli ekanini va nima sababdan `local.properties`dan foydalanish kerakligini aniq asoslab berishi kerak;
- AAB formati barcha protsessorlar kodini bitta faylga to'plamasdan, har bir telefonga faqat kerakli qismini berishini to'g'ri ifodalashi lozim.
