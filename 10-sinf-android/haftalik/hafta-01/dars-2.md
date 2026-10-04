# 2-dars: Build variantlari va Product Flavors

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 1-hafta, 2-dars (umumiy 2-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Android ilovalarini turli muhitlar va foydalanuvchilar toifalari uchun moslashtirish mexanizmi bo'lgan **Build Types** va **Product Flavors** tushunchalarini o'rgatish; `debug` va `release` yig'ish turlarining texnik farqlarini (kodni siqish, R8/ProGuard, disk raskadrovka loglari) tushuntirish; bitta kod bazasidan (single codebase) bir nechta mustaqil ilovalarni (masalan, Free va Paid) chiqarish uchun `productFlavors`, `flavorDimensions`, `applicationIdSuffix` hamda `buildConfigField` parametrlaridan professional darajada foydalanish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- `buildTypes` (Debug vs Release) ning vazifasi va xavfsizlik talablarini tushunish;
- `minifyEnabled true` va ProGuard/R8 qoidalarining Release rejimida kodni himoyalash va siqishdagi ahamiyatini bilish;
- `productFlavors` nima ekanini va nima uchun bitta loyihadan bir nechta versiya (Free/Paid, Demo/Pro) chiqarishda kodni nusxalash (copy-paste) qat'iyan taqiqlanishini tushunish;
- `Build Variant` qanday shakllanishini ($\text{Build Type} \times \text{Product Flavor}$) hisoblay olish;
- Gradle tomonidan generatsiya qilinadigan `BuildConfig` klassidan foydalanib, kod ichida turli muhitlar uchun shartli mantiq (`if (BuildConfig.IS_PAID)`) yoza olish;
- Android Studio'dagi *Build Variants* oynasi orqali aktiv variantni almashtirishni bilish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Android Studio (so'nggi barqaror versiya);
- Android Emulator yoki USB orqali ulangan real Android qurilma;
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Gradle nima, `settings.gradle` va `build.gradle` tuzilishi, SDK versiyalari bo'yicha savol-javob |
| **10–25 min** | Yangi mavzu: Build Types (Debug vs Release) | Dasturchi rejimi vs Tayyor mahsulot, `debuggable`, `minifyEnabled`, R8 optimallashtirish |
| **25–45 min** | Product Flavors va Build Variants | `flavorDimensions`, Free vs Paid, `applicationIdSuffix`, bitta telefonda 2 ta ilovani parallel o'rnatish |
| **45–60 min** | `BuildConfig` va `resValue` bilan ishlash | Kodga Gradle orqali o'zgaruvchilar uzatish, turli API manzillar (Staging vs Production) |
| **60–75 min** | Amaliy mashg'ulot | `build.gradle`da Free va Paid flavorlarini sozlash, turli nom va logikali APK larni yig'ish |
| **75–80 min** | Xulosa va darsni yakunlash | Mavzuni mustahkamlash, tezkor savollar va uyga vazifa |

---

## Nazariy ma'lumotlar

### 1. Build Types (Yig'ish turlari): Debug vs Release

Android loyihasida `buildTypes` bloki ilovaning qanday maqsadda yig'ilayotganini belgilaydi. Standart holda har bir Android loyihasida ikkita asosiy build turi mavjud:

```groovy
android {
    ...
    buildTypes {
        debug {
            debuggable true
            applicationIdSuffix ".debug"
            versionNameSuffix "-DEBUG"
        }
        release {
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

#### Asosiy farqlar:
1. **Debug (Nosozliklarni qidirish rejimi):**
   - Dasturchi kod yozayotgan va sinovdan o'tkazayotgan paytda ishlatiladi;
   - Kod kompilyatsiyasi maksimal tezlikda bo'ladi, kod siqilmaydi va o'zgartirilmaydi;
   - Barcha loglar (Logcat) ochiq, dasturchi breakpoint qo'yib, xotirani tahlil qila oladi;
   - `applicationIdSuffix ".debug"` qo'shilsa, bitta telefonga original Release ilova bilan bir vaqtda Debug ilovani ham o'rnatish mumkin bo'ladi!
2. **Release (Tayyor mahsulot rejimi):**
   - Google Play do'koniga yuklanadigan va oxirgi foydalanuvchiga taqdim etiladigan yakuniy versiya;
   - `minifyEnabled true`: R8 optimallashtiruvchisi ishga tushadi, ishlatilmagan ortiqcha kodlar o'chirib tashlanadi;
   - **Obfuscation (Kodni chalkashtirish):** Xavfsizlik maqsadida barcha klass va funksiya nomlari qisqa tushunarsiz harflarga (`a`, `b`, `c`) almashtiriladi, ilovani dekompilyatsiya qilishdan himoyalaydi;
   - Debug qilish taqiqlanadi (`debuggable false`).

---

### 2. Product Flavors (Mahsulot variantlari)

Real hayotda ko'pincha bitta ilovaning bir nechta versiyasini chiqarishga to'g'ri keladi:
- Bepul versiya (reklama bilan, cheklangan funksiyalar) va Pullik VIP versiya (reklamasiz, barcha darslar ochiq);
- Mijoz ilovasi (Client App) va Kuryer/Haydovchi ilovasi (Driver App);
- Test serveriga ulanadigan versiya (Staging) va Haqiqiy bank serveriga ulanadigan versiya (Production).

Agar dasturchi bu versiyalar uchun alohida 2 ta loyiha ochib, kodni nusxalasa (copy-paste), keyinchalik har bitta xatolikni tuzatish uchun ikkala loyihada ham o'zgartirish kiritishiga to'g'ri keladi. Bu juda xavfli va samarasiz usul.

**To'g'ri yechim — Product Flavors!**

```groovy
android {
    ...
    flavorDimensions "tier"

    productFlavors {
        free {
            dimension "tier"
            applicationIdSuffix ".free"
            versionNameSuffix "-free"
            buildConfigField "boolean", "IS_PAID", "false"
            buildConfigField "String", "BASE_URL", "\"https://sandbox.api.myservice.uz/\""
        }
        paid {
            dimension "tier"
            applicationIdSuffix ".paid"
            versionNameSuffix "-pro"
            buildConfigField "boolean", "IS_PAID", "true"
            buildConfigField "String", "BASE_URL", "\"https://api.myservice.uz/\""
        }
    }
}
```

---

### 3. Build Variants matematikasi

Build Variant — bu bitta **Product Flavor** va bitta **Build Type**ning kombinatsiyasidir:

$$\text{Build Variants} = \text{Product Flavors soni} \times \text{Build Types soni}$$

Yuqoridagi misolda bizda:
- 2 ta Flavor: `free`, `paid`
- 2 ta Build Type: `debug`, `release`

Natijada **4 ta alohida Build Variant** hosil bo'ladi:
1. `freeDebug` — Sinov uchun mo'ljallangan bepul versiya;
2. `freeRelease` — Google Play uchun bepul versiya;
3. `paidDebug` — Sinov uchun to'liq VIP versiya;
4. `paidRelease` — Google Play uchun pullik VIP versiya.

Android Studio oynasining chap pastki burchagidagi **"Build Variants"** oynasi orqali dasturchi bir soniyada joriy variantni o'zgartirishi mumkin.

---

### 4. `BuildConfig` klassi orqali kodni boshqarish

Gradle loyihani yig'ayotgan paytda avtomatik ravishda `BuildConfig.java` faylini yaratadi. Biz `build.gradle` orqali unga maxsus parametrlar uzata olamiz:

```groovy
buildConfigField "boolean", "IS_PAID", "true"
buildConfigField "String", "API_KEY", "\"SECRET_KEY_12345\""
```

Kotlin kodida esa bu o'zgaruvchini quyidagicha tekshirish mumkin:

```kotlin
if (BuildConfig.IS_PAID) {
    // VIP foydalanuvchilar uchun maxsus funksiyalarni ochish
    showProFeatures()
} else {
    // Bepul foydalanuvchilarga reklama ko'rsatish
    showBannerAd()
}
```

Bu dasturchiga kod ichida hech narsani qo'lda o'zgartirmasdan, faqat build variantini almashtirish orqali ilova xulq-atvorini butunlay o'zgartirish imkonini beradi.

---

## Amaliy topshiriqlar va mashqlar

### 1-topshiriq. Build Variantlar sonini hisoblash (oson)
Loyiha moduli `build.gradle` faylida quyidagi konfiguratsiya mavjud:
- Build Types: `debug`, `release`, `staging` (jami 3 ta);
- Product Flavors: `demo`, `standard`, `enterprise` (jami 3 ta).

1. Ushbu loyihada jami nechta Build Variant hosil bo'ladi?
2. Barcha hosil bo'lgan Build Variant nomlarini to'liq yozib chiqing.

**Yechim:**
1. **Jami variantlar soni:** $3 \times 3 = 9$ ta Build Variant hosil bo'ladi.
2. **Variantlar ro'yxati:**
   - `demoDebug`, `demoRelease`, `demoStaging`
   - `standardDebug`, `standardRelease`, `standardStaging`
   - `enterpriseDebug`, `enterpriseRelease`, `enterpriseStaging`

---

### 2-topshiriq. Staging va Production muhitlari uchun API URL sozlash (o'rta)
Ilovangiz ikkita server bilan ishlaydi:
- Sinov (Debug va Staging) paytida: `"https://dev-api.fintech.uz/v1/"`
- Haqiqiy foydalanuvchilar (Release) uchun: `"https://api.fintech.uz/v1/"`

Ushbu shartni `buildTypes` bloki orqali `buildConfigField` yordamida to'g'ri sozlang. So'ngra Kotlin kodida ushbu URL qanday chaqirilishini ko'rsating.

**Yechim:**
`app/build.gradle` faylida:
```groovy
buildTypes {
    debug {
        buildConfigField "String", "BASE_URL", "\"https://dev-api.fintech.uz/v1/\""
    }
    release {
        minifyEnabled true
        proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        buildConfigField "String", "BASE_URL", "\"https://api.fintech.uz/v1/\""
    }
}
```
**Kotlin kodida chaqirish:**
```kotlin
val currentApiUrl = BuildConfig.BASE_URL
println("So'rov yuborilayotgan server: $currentApiUrl")
```

---

### 3-topshiriq. Parallel o'rnatiluvchi Free va Pro versiyalarni yaratish (qiyin)
Bitta smartfonga bir vaqtning o'zida ham Free, ham Pro versiyasini o'rnatish imkonini beruvchi to'liq `productFlavors` blokini yozing:
- Boshlang'ich paket nomi: `"uz.kitobxon.app"`
- Free versiya uchun ilova ID: `"uz.kitobxon.app.free"` va `versionNameSuffix "-FREE"`
- Pro versiya uchun ilova ID: `"uz.kitobxon.app.pro"` va `versionNameSuffix "-PRO"`
- Free versiyada maksimal kitob yuklash soni (`MAX_DOWNLOADS`) 3 ta, Pro versiyada esa 100 ta bo'lsin (`int` turida).

**Yechim:**
```groovy
android {
    ...
    flavorDimensions "edition"

    productFlavors {
        free {
            dimension "edition"
            applicationIdSuffix ".free"
            versionNameSuffix "-FREE"
            buildConfigField "int", "MAX_DOWNLOADS", "3"
        }
        pro {
            dimension "edition"
            applicationIdSuffix ".pro"
            versionNameSuffix "-PRO"
            buildConfigField "int", "MAX_DOWNLOADS", "100"
        }
    }
}
```

---

## Tezkor nazorat savollari

1. `buildTypes` bilan `productFlavors` o'rtasidagi asosiy farq nima?
   - *Javob:* `buildTypes` ilovani qanday yig'ishni (texnik rejim: Debug/Release, optimallashtirish, xavfsizlik) belgilaydi; `productFlavors` esa turli foydalanuvchilar uchun mahsulotning har xil funksional ko'rinishlarini (Free/Paid) belgilaydi.
2. `minifyEnabled true` parametri nima vazifani bajaradi va u nega faqat Release da yoqiladi?
   - *Javob:* R8 orqali ishlatilmagan kodlarni o'chiradi va kodni chalkashtiradi (obfuscation). Debug da yoqilmasligining sababi — yig'ish vaqtini cho'zib yuboradi va nosozliklarni tahlil qilishni qiyinlashtiradi.
3. Nega `applicationIdSuffix ".debug"` qo'shish qulay hisoblanadi?
   - *Javob:* Chunki Android operatsion tizimi ilovalarni faqat `applicationId` orqali ajratadi. Suffix qo'shilsa, bitta telefonda ham rasmiy Release ilova, ham sinovdagi Debug ilova yonma-yon o'rnatilishi mumkin bo'ladi.
4. `BuildConfig` klassi qanday hosil bo'ladi va undan qanday maqsadda foydalaniladi?
   - *Javob:* Gradle tomonidan avtomatik yaratiladi. U orqali Gradle sozlamalaridagi o'zgaruvchilarni (masalan, API URL, versiya, boolean bayroqlar) Kotlin/Java kodiga xavfsiz uzatish uchun foydalaniladi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **String qiymatlarni `buildConfigField`da qo'shtirnoqsiz yozish:** `buildConfigField "String", "URL", "https://..."` deb yozilsa xato bo'ladi. To'g'ri sintaksis: `\"https://...\"` (ekranlangan qo'shtirnoqlar bilan).
- **`flavorDimensions` e'lon qilishni unutish:** Agar productFlavors yozilib, `flavorDimensions` ko'rsatilmasa, Gradle *"All flavors must now belong to a named flavor dimension"* xatoligini beradi.
- **Release variantida parollarni ochiq kodda qoldirish:** API maxfiy kalitlarini to'g'ridan-to'g'ri `build.gradle`da ochiq qoldirmasdan, `local.properties` faylida saqlash lozim.
