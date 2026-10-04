# 5-dars. Android ekotizimi va Google xizmatlari (2-qism)

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 2-hafta  
**Dars tartibi:** 5-dars (umumiy 102 darsdan 5-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Amaliy va xavfsizlikka yo'naltirilgan mashg'ulot  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga Google xizmatlarini (Firebase, Google Cloud) mobil loyihaga professional darajada ulash tartibi, SHA-1 raqamli barmoq izini olish, `google-services.json` fayli bilan ishlash, API kalitlari xavfsizligi hamda APK va AAB formatlari farqini o'rgatish.
- **Kutiladigan natijalar:**
  - O'quvchi ilovaning noyob identifikatori (`applicationId` / Package Name) nima ekanini biladi;
  - Terminal orqali `./gradlew signingReport` buyrug'i bilan SHA-1 va SHA-256 barmoq izlarini mustaqil ola biladi;
  - `google-services.json` faylining vazifasi va loyiha papkasidagi o'rnini (`app/` katalogi) tushunadi;
  - API kalitlarini ochiq kodda qoldirmasdan `local.properties` orqali xavfsiz saqlash amaliyotini o'zlashtiradi;
  - APK va AAB (Android App Bundle) formatlari o'rtasidagi farqni va nima uchun Google Play AAB talab qilishini tushuntira oladi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | O'tgan mavzuni takrorlash va kirish | AOSP vs GMS, Google Play Services vazifalari bo'yicha blits-so'rov. Muammoli savol: "Google sizning ilovangiz aynan sizga tegishli ekanini qayerdan biladi?" |
| **10–30 daq** | Yangi mavzu: Identifikatsiya va SHA-1 | `applicationId` tuzilmasi, Keystore tushunchasi, `./gradlew signingReport` buyrug'i orqali SHA-1 olish |
| **30–50 daq** | Yangi mavzu: google-services.json va xavfsizlik | Firebase Console, `google-services.json` faylining strukturasi, API kalitlarini `local.properties`da yashirish |
| **50–65 daq** | Yangi mavzu: APK vs AAB | An'anaviy APK va zamonaviy Android App Bundle (AAB), Play Store'ning dinamik yetkazib berish (Dynamic Delivery) mexanizmi |
| **65–75 daq** | Amaliy mashq va keys tahlili | SHA-1 kalitini tahlil qilish, loyiha fayllari ierarxiyasida to'g'ri joylashtirish mashqi |
| **75–80 daq** | Xulosa va baholash | Dars yakunlari, o'quvchilarni baholash, uyga vazifa berish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. Ilova identifikatori: `applicationId`
Har bir Android ilovasi global miqyosda (Google Play'da) yagona bo'lgan identifikatorga ega bo'lishi shart. U domen nomining teskari ko'rinishida (Reverse Domain Name notation) belgilanadi:
- `com.companyname.appname` (masalan, `uz.click.clickuz`, `com.payme.uz`).
- Ushbu nom ilova o'rnatilganda Linux foydalanuvchisi va uning shaxsiy ma'lumotlar papkasi nomini belgilaydi (`/data/data/uz.click.clickuz/`).

### 3.2. Raqamli barmoq izi: SHA-1 va SHA-256
Ilovani Google Cloud yoki Firebase'ga ulash uchun uning "raqamli shaxsini" tasdiqlash talab etiladi. Buning uchun kompyuterdagi debug yoki release kalitining (Keystore) xesh qiymati olinadi.
- **Qanday olinadi?** Android Studio ichidagi terminal oynasida:
  ```bash
  ./gradlew signingReport
  ```
- **Natija:**
  ```text
  Variant: debugAndroidTest
  Config: debug
  Store: /Users/dev/.android/debug.keystore
  Alias: AndroidDebugKey
  MD5:  A1:B2:C3:...
  SHA1: 4B:12:8A:99:32:DE:01:...
  SHA-256: 7F:89:AB:...
  ```
Ushbu SHA-1 kaliti Firebase Console yoki Google Cloud Console'ga kiritiladi. Bu boshqa hech kim sizning nomingizdan API so'rov yubora olmasligini kafolatlaydi.

### 3.3. `google-services.json` fayli
Google loyihani ro'yxatdan o'tkazgach, dasturchiga maxsus `google-services.json` faylini beradi. Bu fayl loyihaning "guvohnomasi" bo'lib, quyidagilarni o'z ichiga oladi:
- `project_id` — Firebase loyihasi nomi;
- `current_key` — API kalitlar;
- `firebase_url` — ma'lumotlar bazasi manzili;
- `package_name` — sizning `applicationId`ingiz.

**Joylashuvi:** Fayl qat'iy ravishda Android loyihasining `app/` papkasi ichiga joylashtirilishi shart! Agar u noto'g'ri joyga qo'yilsa, Gradle loyihani yig'ishdan bosh tortadi.

### 3.4. API kalitlari va xavfsizlik (Security Best Practices)
Google Maps yoki boshqa xizmatlarning API kalitlarini hech qachon ochiq kodda (`MainActivity.kt`) yoki `AndroidManifest.xml`da to'g'ridan-to'g'ri yozib qoldirmaslik kerak!
- **Sababi:** Agar kod GitHubga yuklansa, xakerlar maxsus botlar orqali kalitni bir necha soniyada o'g'irlab oladi va sizning billing hisobingizdan minglab dollar sarflab yuborishi mumkin.
- **Xavfsiz usul:** API kalitlarni `local.properties` faylida saqlash:
  ```properties
  MAPS_API_KEY=AIzaSyD-namuna-kalit-12345
  ```
  `local.properties` fayli avtomatik tarzda `.gitignore` ro'yxatiga kiritilgan bo'lib, GitHubga yuklanmaydi. Gradle orqali esa ushbu kalit xavfsiz holda `BuildConfig` orqali kodga uzatiladi.

### 3.5. APK vs AAB (Android App Bundle)
- **APK (Android Package Kit):**
  - An'anaviy arxiv fayl (.zip formatida).
  - Barcha protsessor arxitekturalari (arm64-v8a, armeabi-v7a, x86_64) va barcha ekran o'lchamlari (hdpi, xhdpi, xxhdpi) resurslarini bitta faylda saqlaydi. Hajmi katta bo'ladi (masalan, 60 MB).
- **AAB (Android App Bundle):**
  - 2021-yil avgust oyidan boshlab Google Play barcha yangi ilovalar uchun AAB formatini majburiy qilib qo'ydi.
  - AAB Google Play do'koniga yuklanadi. Play Store har bir foydalanuvchining telefon modelini aniqlaydi va unga faqat o'sha telefon tushunadigan kod va rasmlarni jo'natadi (**Dynamic Delivery**).
  - Natijada ilova hajmi **30-50% ga qisqaradi** (masalan, 60 MB o'rniga telefon 25 MB yuklab oladi).

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. `applicationId` tuzish qoidalari (Oson)
**Topshiriq:** Maktabingiz uchun «Kutubxona» nomli mobil ilova yaratmoqchisiz. Domen: `navoiy-maktab.uz`. Ushbu ilova uchun to'g'ri `applicationId` yozing.

**Yechim:**
Domen teskari tartibda yoziladi:
`uz.navoiy_maktab.kutubxona` yoki `uz.navoiyschool.library`.
(Eslatma: nomda bo'sh joy va chiziqcha `-` ishlatilmaydi, faqat kichik lotin harflari, raqamlar va tagchiziq `_` bo'lishi mumkin).

### 2-topshiriq. SHA-1 olish va vazifasi (O'rta)
**Topshiriq:** `./gradlew signingReport` buyrug'i qanday ishlaydi va undan olingan SHA-1 nimani kafolatlaydi?

**Yechim:**
Buyruq Gradle orqali kompyuterdagi `.android/debug.keystore` faylini ochadi va uning ochiq kalit sertifikatining SHA-1 xeshini chiqarib beradi. Ushbu xesh Firebase yoki Google Cloud'ga kiritilganda, Google faqat shu kompyuterda imzolangan ilova so'rovlarini qabul qiladi, boshqa noma'lum manbadan kelgan so'rovlarni rad etadi.

### 3-topshiriq. APK va AAB taqqoslashi (Qiyin)
**Topshiriq:** Nima uchun Google Play dasturchilardan tayyor APK o'rniga AAB formatini talab qiladi? Foydalanuvchi va dasturchi nuqtai nazaridan afzalliklarini tushuntiring.

**Yechim:**
1. **Foydalanuvchi uchun:** Ilova hajmi 30-50% kichik bo'ladi. Mobil internet trafiki tejaladi, telefon xotirasi to'lib qolmaydi va ilova tezroq o'rnatiladi.
2. **Dasturchi uchun:** Dasturchi har bir protsessor (ARM, x86) va ekran zichligi uchun alohida 5-6 xil APK yig'ib o'tirmaydi. U bitta umumiy AAB faylini yuklaydi, qolgan hamma optimallashuvni Google Play Store avtomatlashtiradi.

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **Android Studio terminalida SHA-1 olish buyrug'i qaysi?**  
   *Javob:* `./gradlew signingReport` (Windowsda `gradlew signingReport`).
2. **`google-services.json` fayli loyihaning qaysi jildiga qo'yiladi?**  
   *Javob:* `app/` papkasi ichiga.
3. **Nima uchun maxfiy API kalitlarni `MainActivity`da qoldirish xavfli?**  
   *Javob:* Kod GitHubga yoki begona qo'lga tushganda, kalit o'g'irlanib, billing hisobidan noqonuniy foydalanilishi mumkin.
4. **API kalitlarini xavfsiz saqlash uchun qaysi fayldan foydalaniladi?**  
   *Javob:* `local.properties` faylidan (chunki u `.gitignore`da bo'ladi).
5. **AAB qisqartmasi nimani anglatadi?**  
   *Javob:* Android App Bundle.

---

## 6. Mentor uchun amaliy tavsiyalar

- O'quvchilarga terminalda `./gradlew signingReport` buyrug'ining ishlashini ekranda amalda ko'rsating.
- SHA-1 kalitini "raqamli pasport"ga, `google-services.json` faylini esa "viza ruxsatnomasi"ga qiyoslab tushuntiring.
