---
title: "8-dars. 5-dars: ProGuard va R8 yordamida kodni optimallashtirish (1-qism)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Android)", "link": "/10-sinf-android/"}, "week": {"n": 2, "link": "/10-sinf-android/hafta-02/"}, "g": 8, "title": "5-dars: ProGuard va R8 yordamida kodni optimallashtirish (1-qism)", "lead": "", "slide": "/slaydlar/10-sinf-android/hafta-02/dars-5.html", "tabs": [{"g": 7, "link": "/10-sinf-android/hafta-02/dars-4", "current": false}, {"g": 8, "link": "/10-sinf-android/hafta-02/dars-5", "current": true}, {"g": 9, "link": "/10-sinf-android/hafta-02/dars-6", "current": false}], "prev": {"g": 7, "title": "4-dars: Dependency management va ziddiyatlarni hal qilish", "link": "/10-sinf-android/hafta-02/dars-4"}, "next": {"g": 9, "title": "6-dars: ProGuard va R8 qoidalari bilan ishlash (2-qism: Amaliyot)", "link": "/10-sinf-android/hafta-02/dars-6"}}
---

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** ProGuard va R8 yordamida kodni optimallashtirish: Shrinking, Obfuscation, Optimization va Resource Shrinking  

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Ilovani Google Play do'koniga chiqarishdan oldin uning hajmini kichraytirish va kodini xakerlardan himoyalash eng muhim bosqichlardan biridir. Android ekotizimida bu vazifani **R8 (ProGuard)** optimallashtirish tizimi bajaradi:

1. **R8 ning ProGuard dan afzalligi:**
   - ProGuard eski alohida vosita bo'lgan bo'lsa, R8 to'g'ridan-to'g'ri D8 (DEX kompilyatori) ichiga birlashtirilgan;
   - Build jarayonini 2–3 barobar tezlashtiradi va kamroq xotira talab qiladi.
2. **Optimallashtirishning 4 ta asosiy bosqichi:**
   - **Code Shrinking (Tree Shaking):** Ishlatilmagan ortiqcha klasslar, metodlar va o'zgaruvchilarni ilovadan butunlay o'chirib tashlaydi;
   - **Resource Shrinking (`shrinkResources true`):** Foydalanilmagan rasmlar, animatsiyalar va XML dizaynlarni tozalaydi;
   - **Optimization:** Kod tuzilmasini tahlil qilib, bo'sh shartlarni o'chiradi va kichik funksiyalarni inline qiladi;
   - **Obfuscation (Kodni chalkashtirish):** Klass va metodlarning uzun nomlarini qisqa tushunarsiz harflarga (`a, b, c`) almashtirib, kodni o'g'irlashdan himoyalaydi.
3. **`build.gradle` sozlamalari:**
   - `minifyEnabled true`: R8 optimallashtirishini yoqish;
   - `shrinkResources true`: Resurslarni siqish (faqat `minifyEnabled true` bilan ishlaydi).
4. **Hosil bo'ladigan natija:**
   - APK hajmi 30–50% gacha qisqaradi, ilova tezroq yuklanadi va telefonning RAM xotirasi tejaladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun amaliy topshiriqlar

Quyidagi 10 ta amaliy vazifani diqqat bilan o'rganing va ularni Android Studio muhitida hamda daftaringizda bajaring:

### 1-topshiriq <Badge type="tip" text="oson" />
Nima uchun ilovani Google Play'ga yuklashdan oldin albatta optimallashtirish kerak? 40 MB hajmdagi ilova bilan 15 MB hajmdagi ilova o'rtasida foydalanuvchi uchun qanday farq bor?

### 2-topshiriq <Badge type="tip" text="oson" />
ProGuard bilan R8 o'rtasidagi asosiy texnik farqni tushuntiring. Nima uchun Google zamonaviy Android Studio versiyalarida aynan R8 dan foydalanadi?

### 3-topshiriq <Badge type="tip" text="oson" />
Code Shrinking (Tree Shaking) mexanizmini tushuntiring. Nima uchun katta kutubxona ulanganida uning barcha kodlari APK ga kirmaydi?

### 4-topshiriq <Badge type="warning" text="o'rta" />
Obfuscation (kodni chalkashtirish) qanday ishlaydi? Agar dasturchi yozgan `class BankAccountManager` klassi obfuskatsiya qilinsa, u qanday ko'rinishga keladi? Bu qanday xavfsizlik afzalligini beradi?

### 5-topshiriq <Badge type="warning" text="o'rta" />
`shrinkResources true` parametri nima vazifani bajaradi va u nega albatta `minifyEnabled true` bilan birga ishlatilishi shart?

### 6-topshiriq <Badge type="warning" text="o'rta" />
Nima uchun `minifyEnabled true` sozlamasi dasturchi kod yozayotgan paytda (Debug rejimida) yoqilmaydi? Debug da minifikatsiyani yoqish qanday 2 ta jiddiy noqulaylikni keltirib chiqaradi?

### 7-topshiriq <Badge type="danger" text="qiyin" />
`app/build.gradle` faylining `buildTypes` blokidagi `release` qismini to'liq yozing:
- Unda kodni siqish va obfuskatsiya yoqilgan bo'lsin;
- Ishlatilmagan resurslar siqilsin;
- Standart `proguard-android-optimize.txt` va `proguard-rules.pro` fayllari biriktirilsin.

### 8-topshiriq <Badge type="danger" text="qiyin" />
Android Studio'ning **APK Analyzer** (Build $\to$ Analyze APK) vositasining vazifasini tushuntiring. U orqali tayyor APK ichidagi `classes.dex`, `resources.arsc` va `res/` papkalari hajmini qanday tekshirish mumkin?

### 9-topshiriq <Badge type="danger" text="qiyin" />
Inlining (funksiyalarni inline qilish) optimallashtirish jarayonida qanday amalga oshadi? Bo'sh shartlar (`if (false)`) nima uchun kompilyatsiyadan so'ng o'chirib tashlanadi?

### 10-topshiriq <Badge type="info" text="bonus" />
Android Studio'da mavjud loyihangiz uchun ikkita APK yig'ing:
1. `minifyEnabled false` qilib Debug APK yig'ing va uning hajmini qayd eting;
2. `minifyEnabled true` va `shrinkResources true` qilib Release APK yig'ing va uning hajmini qayd eting;
3. APK Analyzer orqali ikkala fayl hajmini taqqoslang va necha foiz hajm tejalganini hisoblab yozing.

</div>

