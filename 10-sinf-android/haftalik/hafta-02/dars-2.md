# 5-dars: ProGuard va R8 yordamida kodni optimallashtirish (1-qism)

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 2-hafta, 2-dars (umumiy 5-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Android ilovalarini chiqarish (Release) oldidan optimallashtirish, xavfsizlikni oshirish va hajmni keskin kamaytirish vositalari bo'lgan **ProGuard** va **R8** tizimlarining arxitekturasini o'rgatish; R8 kompilyatorining ProGuard dan afzalliklari (D8 bilan integratsiya, tezkorlik)ni tushuntirish; optimallashtirishning 4 ta fundamental bosqichi — **Code Shrinking (Tree Shaking)**, **Resource Shrinking**, **Optimization** va **Obfuscation (kodni chalkashtirish)** tamoyillarini o'zlashtirish; `minifyEnabled true` va `shrinkResources true` parametrlarini amalda qo'llash ko'nikmalarini rivojlantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- ProGuard va R8 vositalarining maqsadi hamda ular orasidagi farqni (R8 ning D8 bilan birlashtirilgan zamonaviy standart ekanini) tushunish;
- Code Shrinking (Tree Shaking) mexanizmini va ishlatilmagan kodlar qanday aniqlanib o'chirilishini bilish;
- Resource Shrinking (`shrinkResources true`) qanday qilib foydalanilmagan rasm va dizayn fayllarini APK dan chiqarib tashlashini tushunish;
- Obfuscation (kodni chalkashtirish) nima ekanini va klass, metod nomlarini `a, b, c` ga aylantirish ilova kiberxavfsizligini qanday ta'minlashini bilish;
- `build.gradle` faylining `release` blokida `minifyEnabled true` parametrini to'g'ri faollashtira olish;
- Optimallashtirish orqali APK hajmini 30–50% gacha qisqartirish va telefonning RAM xotirasini tejash afzalliklarini tushunish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Android Studio (so'nggi barqaror versiya);
- APK Analyzer vositasi (Android Studio ichiga o'rnatilgan);
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Tranzitiv bog'liqliklar, versiya ziddiyatlari va `exclude` qoidalari bo'yicha savol-javob |
| **10–25 min** | Yangi mavzu: Nega ilovani optimallashtirish shart? | Katta hajmli APK zararlari, ilovani dekompilyatsiya qilish xavfi, ProGuard vs R8 |
| **25–45 min** | R8 optimallashtirishning 4 ta bosqichi | Code Shrinking (Tree shaking), Resource Shrinking, Optimization va Obfuscation |
| **45–60 min** | `minifyEnabled` va `shrinkResources` sozlamalari | `build.gradle`da yoqish, `proguard-android-optimize.txt` standart qoidalari |
| **60–75 min** | Amaliy mashg'ulot (APK Analyzer) | Release APK yig'ish, APK Analyzer yordamida `classes.dex` faylini va chalkashtirilgan nomlarni tekshirish |
| **75–80 min** | Xulosa va darsni yakunlash | Asosiy xulosalarni mustahkamlash, tezkor nazorat savollari va uyga vazifa |

---

## Nazariy ma'lumotlar

### 1. Nega optimallashtirish zarur? ProGuard vs R8

Ilova qanchalik chiroyli bo'lmasin, agar uning hajmi juda katta bo'lsa (masalan, 60–80 MB), foydalanuvchilar uni mobil internet orqali yuklab olishni xohlamaydi. Bundan tashqari, oddiy APK faylini dekompilyatsiya qilib (JADX yoki APKTool yordamida), uning ichidagi barcha Kotlin/Java kodlarini va server bilan bog'lanuvchi maxfiy API logikalarini osonlikcha o'g'irlash mumkin.

Ushbu ikki muammoni (hajm va xavfsizlik) hal qiluvchi vosita — **R8 (ilgari ProGuard)** hisoblanadi:
- **ProGuard:** Ko'p yillar davomida Android'da standart bo'lgan. Ammo u Java baytkodini tahlil qiluvchi alohida tashqi vosita sifatida ishlagan va build vaqtini ancha cho'zib yuborgan.
- **R8:** Google tomonidan ishlab chiqilgan yangi avlod optimallashtiruvchisi. U to'g'ridan-to'g'ri **D8 DEX kompilyatori** ichiga o'rnatilgan bo'lib, Kotlin/Java kodini bir vaqtning o'zida ham qisqartiradi, ham DEX baytkodga aylantiradi. Natijada yig'ish vaqti 2–3 barobar tejaladi.

---

### 2. R8 optimallashtirishning 4 ta bosqichi

R8 yig'ish jarayonida quyidagi **4 ta operatsiyani** ketma-ket bajaradi:

#### A. Code Shrinking (Tree Shaking — Kodni qisqartirish)
Ilovangizga katta kutubxona ulangan bo'lsa (masalan, Google Play Services yoki Room), siz undagi 1000 ta klassdan faqat 10 tasini ishlatishingiz mumkin. R8 dasturning kirish nuqtasidan (`MainActivity`) boshlab butun loyihani tahlil qiladi (buni daraxtni silkitishga o'xshatishadi). Hech qayerda chaqirilmagan, keraksiz "qurigan shoxlar" — o'zgaruvchilar, metodlar va butun boshli klasslar ilova ichidan butunlay olib tashlanadi!

#### B. Resource Shrinking (Resurslarni siqish)
`shrinkResources true` parametri yoqilganda, loyihadagi `res/` papkasi tekshiriladi. Agar biror rasm, audio yoki XML fayl kodda ishlatilmagan bo'lsa, u APK paketidan olib tashlanadi yoki minimal 1 baytli bo'sh fayl bilan almashtiriladi.

#### C. Optimization (Kodni optimallashtirish)
R8 kodning ichki mantiqiy tuzilmasini yaxshilaydi:
- Hech qachon bajarilmaydigan shartlarni (`if (false)`) o'chiradi;
- Kichik funksiyalarni inline qiladi (funksiya chaqiruvini to'g'ridan-to'g'ri uning tanasi bilan almashtiradi);
- Klasslar ierarxiyasini soddalashtiradi.

#### D. Obfuscation (Kodni chalkashtirish)
Bu ilovaning kiberxavfsizlik qalqonidir. Odam o'qishi uchun qulay bo'lgan uzun va ma'noli nomlar qisqa harflarga almashtiriladi:
- `UserDataManager` $\to$ `class a`
- `calculateTaxAmount()` $\to$ `fun b()`
- `paymentAuthToken` $\to$ `var c`

Natijada kiberhujumchi ilovani buzib ochganida ham, tushunarsiz harflar to'plamiga duch keladi va ilovaning biznes mantig'ini tushuna olmaydi.

---

### 3. `build.gradle` faylida R8 ni yoqish

Modul darajasidagi `build.gradle` faylining `buildTypes` bo'limida Release rejimini quyidagicha sozlaymiz:

```groovy
android {
    ...
    buildTypes {
        release {
            // Kodni siqish va chalkashtirishni yoqish
            minifyEnabled true

            // Ishlatilmagan resurslarni (rasmlarni) tozalash
            shrinkResources true

            // Standart optimallashtirish qoidalari va o'zimizning qoidalarimiz
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

> **Eslatma:** `shrinkResources true` ishlashi uchun albatta `minifyEnabled true` bo'lishi shart! Chunki resurslar qaysi kodda ishlatilganini aniqlash uchun avval kod siqilishi kerak.

---

## Amaliy topshiriqlar va mashqlar

### 1-topshiriq. Minifikatsiyadan keyingi kod ko'rinishini tahlil qilish (oson)
Quyidagi Kotlin kodini ko'rib chiqing:
```kotlin
class PaymentProcessor {
    private val secretApiKey: String = "KEY_999"

    fun processUserTransaction(amount: Double): Boolean {
        return amount > 0
    }
}
```
Agar ushbu klass R8 orqali to'liq minifikatsiya va obfuskatsiya qilinsa, uning taxminiy ko'rinishi qanday bo'ladi?

**Yechim:**
R8 klass nomi, metod nomi va maydon nomlarini qisqa belgilarga almashtiradi:
```kotlin
class a {
    private val a: String = "KEY_999"

    fun a(b: Double): Boolean {
        return b > 0.0
    }
}
```
Klass nomi `a`ga, parametr `b`ga, metod esa `a`ga aylantiriladi. Kod hajmi qisqaradi va tashqi kuzatuvchi uchun tushunarsiz holatga keladi.

---

### 2-topshiriq. `shrinkResources` xatosini tuzatish (o'rta)
Yangi dasturchi o'z loyihasida APK hajmini kichiklashtirish uchun `build.gradle` fayliga quyidagi sozlamani kiritdi:
```groovy
buildTypes {
    release {
        shrinkResources true
    }
}
```
Loyihani yig'ish paytida Gradle xatolik berdi va yig'ish to'xtadi.
1. Xatolikning sababi nimada?
2. Ushbu sozlamani qanday to'g'rilash kerak?

**Yechim:**
1. **Xato sababi:** `shrinkResources true` mustaqil ishlay olmaydi. U ishlashi uchun albatta `minifyEnabled true` (kodni siqish) yoqilgan bo'lishi shart! R8 avval ishlatilmagan kodlarni o'chirib, qaysi resurslar (rasmlar, stringlar) haqiqatdan ham kerak emasligini aniqlagachgina resurslarni siqa oladi.
2. **To'g'rilangan kod:**
```groovy
buildTypes {
    release {
        minifyEnabled true
        shrinkResources true
        proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
    }
}
```

---

### 3-topshiriq. APK Analyzer orqali DEX hajmini taqqoslash (qiyin)
Android Studio'ning **APK Analyzer** (Build $\to$ Analyze APK) vositasidan foydalanib:
1. `minifyEnabled false` bo'lgandagi Debug APK ning `classes.dex` hajmini;
2. `minifyEnabled true` va `shrinkResources true` qilingandagi Release APK ning `classes.dex` hajmini tahlil qiling.
Farq nima hisobiga hosil bo'lganini 3 ta aniq omil bilan asoslang.

**Yechim:**
Release APK dagi `classes.dex` hajmi Debug APK ga nisbatan 40–60% ga kichik bo'ladi.
Buning 3 ta asosiy sababi:
1. **Unused Code Removal:** Kutubxonalar va loyihadagi ishlatilmagan yuzlab metod va klasslar olib tashlangan;
2. **Name Shortening (Obfuscation):** `com.example.service.NetworkPaymentManager` kabi 40 baytli uzun nomlar `a.b.c` kabi 5 baytli nomlarga almashtirilgan (DEX faylidagi String pool hajmi keskin kamayadi);
3. **Dead Code Elimination & Inlining:** Bo'sh yoki bir marta chaqiriluvchi kichik funksiyalar inline qilingan.

---

## Tezkor nazorat savollari

1. ProGuard bilan R8 o'rtasidagi asosiy farq nima va nega hozir R8 ishlatiladi?
   - *Javob:* ProGuard alohida tashqi dastur sifatida ishlagan, R8 esa D8 DEX kompilyatori bilan birlashtirilgan. R8 ancha tez ishlaydi, kam xotira talab qiladi va build vaqtini qisqartiradi.
2. Code Shrinking (Tree Shaking) qanday ishlaydi?
   - *Javob:* Dastur boshlanish nuqtasidan barcha chaqiruvlarni tahlil qiladi va hech qayerda ishlatilmagan o'lik kodlarni (klass, metod, parametrlar) olib tashlaydi.
3. Obfuscation nima va uning asosiy maqsadi nima?
   - *Javob:* Klass, metod va o'zgaruvchilar nomlarini tushunarsiz harflarga (`a, b, c`) almashtirish orqali kodni dekompilyatsiya qilishdan va kiberhujumlardan himoyalash.
4. `shrinkResources true` parametri nima uchun `minifyEnabled true` siz ishlamaydi?
   - *Javob:* Chunki resurslar qaysi kodda ishlatilganini bilish uchun avval kod qisqartirilishi va keraksiz kodlar o'chirilishi kerak.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Debug rejimida `minifyEnabled true`ni yoqib qo'yish:** Bu dasturchining ishini sekinlashtiradi — har safar "Run" bosganda yig'ish vaqti cho'ziladi va Logcat tahlil qilish imkonsiz bo'lib qoladi. Minifikatsiya faqat `release` rejimida yoqilishi shart.
- **Standart optimallashtirish faylini ko'rsatmaslik:** `getDefaultProguardFile('proguard-android-optimize.txt')` yozilmasa, Google tomonidan tavsiya etilgan yuzlab standart optimallashtirish qoidalari chetda qolib ketadi.
