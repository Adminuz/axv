# 2-dars: Build variantlari va Product Flavors

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** Build variantlari va Product Flavors: Debug vs Release, ProGuard/R8 faollashtirish, BuildConfig  

---

## Darsning qisqacha mazmuni

Professional dasturiy ta'minot ishlab chiqishda bitta ilovaning sinov (Debug) va yakuniy (Release) versiyalari yoki bepul (Free) va pullik (Paid) variantlari bo'lishi odatiy hol hisoblanadi. Kodni nusxalab yangi loyiha ochish o'rniga, Android Gradle tizimi bizga **Build Types** va **Product Flavors** mexanizmlarini taqdim etadi:

1. **Build Types (Yig'ish turlari):**
   - **Debug:** Dasturchi kod yozishi va sinashi uchun qulay rejim. Barcha loglar ochiq, tez yig'iladi, disk raskadrovka qilish mumkin;
   - **Release:** Google Play'ga chiqariladigan tayyor versiya. `minifyEnabled true` orqali R8 tizimi ishga tushadi, keraksiz kodlar o'chiriladi va klasslar chalkashtiriladi (Obfuscation).
2. **Product Flavors (Mahsulot variantlari):**
   - Bitta kod bazasidan (single codebase) bir nechta turli funksional ilovalarni (Free vs Paid, Client vs Driver) yaratish imkoniyati;
   - Har bir flavor uchun alohida `applicationIdSuffix`, resurslar va sozlamalar berish mumkin.
3. **Build Variants formulasi:**
   - $\text{Build Variants} = \text{Product Flavors} \times \text{Build Types}$;
   - Masalan: 2 ta flavor (`free`, `paid`) va 2 ta build turi (`debug`, `release`) jami 4 ta variantni hosil qiladi (`freeDebug`, `freeRelease`, `paidDebug`, `paidRelease`).
4. **`BuildConfig` imkoniyatlari:**
   - Gradle orqali Kotlin kodiga o'zgaruvchilar yuborish: `buildConfigField "boolean", "IS_PAID", "true"`;
   - Kod ichida `if (BuildConfig.IS_PAID)` orqali funksiyalarni boshqarish.

---

## Mustaqil bajarish uchun amaliy topshiriqlar

Quyidagi 10 ta amaliy vazifani diqqat bilan o'rganing va ularni Android Studio muhitida hamda daftaringizda bajaring:

### 1-topshiriq · oson
`buildTypes` blokidagi `debug` va `release` rejimlarining 3 ta asosiy farqini (yig'ish tezligi, xavfsizlik va loglar bo'yicha) jadval ko'rinishida yozing.

### 2-topshiriq · oson
Loyiha `build.gradle` faylida quyidagi konfiguratsiya berilgan:
- Build Types: `debug`, `release` (2 ta);
- Product Flavors: `free`, `pro`, `enterprise` (3 ta).  
Ushbu loyihada jami nechta Build Variant hosil bo'ladi va ularning nomlari qanday nomlanadi?

### 3-topshiriq · oson
Nima uchun Debug rejimida `applicationIdSuffix ".debug"` qo'shish tavsiya etiladi? Bu qaysi amaliy qulaylikni ta'minlaydi?

### 4-topshiriq · o'rta
Release rejimida `minifyEnabled true` parametri nima vazifani bajaradi? Obfuscation (kodni chalkashtirish) tushunchasini hayotiy misol bilan tushuntirib bering.

### 5-topshiriq · o'rta
Dasturchi `productFlavors` blokini yozdi, ammo `flavorDimensions` parametrini e'lon qilishni unutdi. Gradle sinxronizatsiya paytida qanday xatolik beradi va bu xatolik qanday tuzatiladi?

### 6-topshiriq · o'rta
Loyihangiz uchun `buildConfigField` yordamida quyidagi 2 ta o'zgaruvchini `build.gradle` fayliga qo'shing:
- `IS_PRO_USER` (boolean turida, qiymati `true`);
- `APP_VERSION_NAME` (String turida, qiymati `"2.0-advanced"`).  
Nima uchun String qiymatlar qo'shtirnoq ichida ekranlanishi (`\"...\"`) shartligini tushuntiring.

### 7-topshiriq · qiyin
Bitta ilovaning ikki xil serverga ulanuvchi variantlarini yarating:
1. `dev` flavor: `BASE_URL` qiymati `"https://dev-server.uz/api/"`;
2. `prod` flavor: `BASE_URL` qiymati `"https://main-server.uz/api/"`.  
Kotlin kodida ushbu URL qanday chaqirilishini va ekranga chiqarilishini ko'rsating.

### 8-topshiriq · qiyin
Android Studio oynasida joylashgan **"Build Variants"** paneli vazifasini tushuntiring. Qanday qilib dasturchi dastur kodini o'zgartirmasdan, bir soniya ichida `freeDebug` variantidan `paidDebug` variantiga o'tishi mumkin?

### 9-topshiriq · qiyin
Kompaniyangiz ikkita ilova chiqarmoqda: "Mijoz Taxi" va "Haydovchi Taxi".
- Ikkala ilova uchun ham umumiy kodlar (tarmoq, ma'lumotlar bazasi, dizayn) 80% bir xil;
- Ushbu holatda 2 ta alohida yangi loyiha ochish to'g'rimi yoki `productFlavors`dan foydalanishmi? Tanlovingizning 3 ta ustunligini yozing.

### 10-topshiriq · bonus
Android Studio'da yangi loyiha oching va `build.gradle` faylida quyidagi shartlarni bajaring:
1. `flavorDimensions "tier"` yarating;
2. `free` va `vip` nomli ikkita flavor qo'shing;
3. `free` versiyada `applicationIdSuffix ".free"` va `resValue "string", "app_name", "Mening Ilovam Free"` bo'lsin;
4. `vip` versiyada `applicationIdSuffix ".vip"` va `resValue "string", "app_name", "Mening Ilovam VIP"` bo'lsin;
5. Har ikkala variantni navbatma-navbat emulyatorda ishga tushirib, telefon ekranida bir vaqtning o'zida ikkita turli nomdagi ilova belgisi (icon) paydo bo'lganini tekshiring.
