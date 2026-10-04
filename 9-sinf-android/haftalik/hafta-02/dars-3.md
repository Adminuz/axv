# 6-dars. Android Studio va Android SDK bilan tanishuv (1-qism)

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 2-hafta  
**Dars tartibi:** 6-dars (umumiy 102 darsdan 6-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Amaliy va laboratoriya mashg'uloti  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga Android ilovalari yaratishning rasmiy dasturlash muhiti — Android Studio interfeysi, uning ichki tuzilishi, Android SDK arxitekturasi (Platform-Tools, Build-Tools, SDK Platforms) hamda ADB vositasi bilan ishlash asoslarini o'rgatish.
- **Kutiladigan natijalar:**
  - O'quvchi Android Studio interfeysining asosiy oynalari (Project Explorer, Editor, Logcat, Gradle) vazifasini biladi;
  - Android SDK (Software Development Kit) arxitekturasining 3 ta asosiy tarkibiy qismini tushunadi;
  - SDK Manager oynasi orqali kerakli Android platformalari va vositalarini boshqara oladi;
  - ADB (Android Debug Bridge) vositasining vazifasini va asosiy buyruqlarini (`adb devices`, `adb logcat`) biladi;
  - Build-Tools tarkibidagi `aapt2` va `d8` kompilyatorlarining kodni yig'ishdagi rolini anglaydi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | O'tgan mavzuni takrorlash va kirish | SHA-1 kalitlari, google-services.json va AAB formati bo'yicha blits-savol. Muammoli savol: "Dasturchi kod yozganda uni telefonda ishlaydigan dasturga kim aylantiradi?" |
| **10–30 daq** | Yangi mavzu: Android Studio muhiti | JetBrains va Google hamkorligi, IntelliJ IDEA negizi, Android Studio interfeysi bo'ylab ekskursiya |
| **30–50 daq** | Yangi mavzu: Android SDK arxitekturasi | SDK nima, SDK Platforms (API versiyalari), SDK Platform-Tools (ADB), SDK Build-Tools (aapt2, d8/r8) |
| **50–65 daq** | Amaliy mashq: SDK Manager va ADB | SDK Manager oynasini ochish, o'rnatilgan paketlarni ko'rish, terminalda `adb version` va `adb devices` buyruqlarini tekshirish |
| **65–75 daq** | Mustahkamlash va test sinovi | Asosiy terminlar va qisqa amaliy topshiriqlar tahlili |
| **75–80 daq** | Xulosa va 2-hafta sarhisobi | Darsni yakunlash, 2-hafta bo'yicha baholash va uyga vazifa berish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. Android Studio — rasmiy dasturlash muhiti (IDE)
Android Studio — bu Google tomonidan JetBrains kompaniyasining IntelliJ IDEA muhiti negizida ishlab chiqilgan rasmiy integratsiyalashgan dasturlash muhitidir (Integrated Development Environment — IDE).
Asosiy qulayliklari:
1. **Intellektual kod muharriri:** Kotlin va Java kodini avtomatik to'ldirish (Code Completion), sintaktik xatolarni real vaqtda ko'rsatish;
2. **Kengaytirilgan Layout Editor:** XML va Jetpack Compose interfeyslarini vizual va kod ko'rinishida loyihalash;
3. **Logcat konsoli:** Ilovaning ishlash jarayonidagi barcha xabarlar va xatoliklarni kuzatuvchi oyna;
4. **Gradle tizimi:** Loyihaning barcha tashqi kutubxonalari va yig'ish parametrlarini avtomatlashtiruvchi dvigatel.

### 3.2. Android SDK nima va uning tarkibi
**Android SDK (Software Development Kit)** — bu operatsion tizim bilan muloqot qilish, kodni kompilyatsiya qilish va ilovani yig'ish uchun zarur bo'lgan barcha texnik asbob-uskunalar to'plamidir.
U 3 ta asosiy ustundan iborat:

#### 1. SDK Platforms
- Har bir Android versiyasi (masalan, Android 14 — API 34, Android 15 — API 35) uchun mo'ljallangan platforma kutubxonalari (`android.jar`).
- Dasturchi qaysi versiya uchun kod yozmoqchi bo'lsa, SDK Manager orqali o'sha platformani yuklab oladi.

#### 2. SDK Platform-Tools (ADB)
- Eng asosiysi — **ADB (Android Debug Bridge)**.
- ADB kompyuter va Android qurilma (yoki emulyator) o'rtasida ma'lumot uzatuvchi mijoz-server ko'prigidir:
  - `adb devices` — kompyuterga ulangan barcha telefon va virtual qurilmalar ro'yxatini ko'rsatadi;
  - `adb install app.apk` — kompyuterdan telefonga ilovani o'rnatadi;
  - `adb logcat` — telefon ichidagi xatolar va tizim loglarini to'g'ridan-to'g'ri terminalga oqim sifatida chiqaradi;
  - `adb shell` — telefonning Linux buyruqlar qatoriga (terminaliga) kirish imkonini beradi.

#### 3. SDK Build-Tools
Loyihani kompilyatsiya qilish va APK/AAB fayliga aylantirish asboblari:
- **`aapt2` (Android Asset Packaging Tool 2):** Loyihaning barcha resurslarini (XML maketlar, ranglar, rasmlar) tekshirib, binar formatga paketlaydi;
- **`d8` / `r8`:** Java baytkodini (`.class`) Android Runtime tushunadigan `.dex` baytkodiga o'tkazuvchi va keraksiz kodlarni tozalovchi (Shrinking & Obfuscation) zamonaviy kompilyatordir.

### 3.3. SDK Manager bilan ishlash
Android Studio yuqori o'ng burchagidagi "SDK Manager" belgisi orqali boshqariladi:
- **SDK Platforms yorlig'i:** Kerakli Android API darajalarini tanlash va o'rnatish;
- **SDK Tools yorlig'i:** Android SDK Build-Tools, Android Emulator, Android SDK Platform-Tools, Google Play Services komponentlarini yangilash.

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. Android SDK tarkibiy qismlari matritsasi (Oson)
**Topshiriq:** SDK Platforms, SDK Platform-Tools va SDK Build-Tools o'rtasidagi farqni bittadan aniq vosita misolida jadvalga yozing.

**Yechim:**
| SDK qismi | Asosiy vazifasi | Tarkibidagi vosita / misol |
|---|---|---|
| **SDK Platforms** | Muayyan Android versiyasining API kutubxonalari | Android 14 (API 34) `android.jar` |
| **SDK Platform-Tools** | Qurilma bilan aloqa va testlash | `adb` (Android Debug Bridge) |
| **SDK Build-Tools** | Resurslarni paketlash va kodni kompilyatsiya qilish | `aapt2`, `d8` kompilyatori |

### 2-topshiriq. ADB buyruqlari tahlili (O'rta)
**Topshiriq:** Quyidagi 3 ta ADB buyrug'i nima vazifa bajarishini tushuntiring:
1. `adb devices`
2. `adb install myapp.apk`
3. `adb logcat -s "MyAppTag"`

**Yechim:**
1. `adb devices`: Kompyuterga USB yoki Wi-Fi orqali ulangan barcha faol Android qurilmalar va emulyatorlar ro'yxatini va ularning holatini (`device` yoki `unauthorized`) chiqaradi.
2. `adb install myapp.apk`: Ko'rsatilgan APK faylini to'g'ridan-to'g'ri ulangan telefonga o'rnatadi.
3. `adb logcat -s "MyAppTag"`: Telefondan kelayotgan ulkan tizim xabarlari oqimidan faqat `MyAppTag` belgisi qo'yilgan xabarlarni filtrlab terminalda ko'rsatadi.

### 3-topshiriq. aapt2 va d8 kompilyatorlari zanjiri (Qiyin)
**Topshiriq:** Dasturchi "Run" (Ishga tushirish) tugmasini bosgandan to APK hosil bo'lguncha `aapt2` va `d8` qanday ketma-ketlikda ishtirok etadi? Sxema ko'rinishida yozing.

**Yechim:**
1. **1-bosqich:** Dasturchi yozgan Kotlin/Java kodi `kotlinc` / `javac` tomonidan `.class` baytkodiga aylanadi.
2. **2-bosqich (`aapt2`):** Loyihaning barcha XML fayllari, rasmlari va resurslari tekshirilib, binar formatga o'tkaziladi va `R.java` fayli yaratiladi.
3. **3-bosqich (`d8`):** Barcha `.class` fayllari va tashqi kutubxonalar Android tushunadigan `.dex` (Dalvik Executable) formatiga o'giriladi.
4. **4-bosqich:** `.dex` kodlari va `aapt2` tayyorlagan resurslar birlashtirilib, raqamli imzo bilan bitta APK/AAB paketi yig'iladi.

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **Android Studio qaysi mashhur IDE negizida yaratilgan?**  
   *Javob:* JetBrains IntelliJ IDEA negizida.
2. **ADB qisqartmasi nimani anglatadi?**  
   *Javob:* Android Debug Bridge (Android nosozliklarni tuzatish ko'prigi).
3. **Qurilma bilan kompyuter aloqasini tekshirish uchun qaysi buyruq kiritiladi?**  
   *Javob:* `adb devices`.
4. **XML resurslarni paketlash uchun SDK tarkibidagi qaysi vosita mas'ul?**  
   *Javob:* `aapt2` (Android Asset Packaging Tool 2).
5. **Java baytkodini `.dex` kodga qaysi zamonaviy vosita o'tkazadi?**  
   *Javob:* `d8` kompilyatori (yoki kodni qisqartiruvchi `r8`).

---

## 6. Mentor uchun amaliy tavsiyalar

- Sinf kompyuterida Android Studio dasturini ochib, SDK Manager oynasini ekranda jonli ko'rsating.
- Terminalda `adb version` buyrug'ini ishlatib ko'rsatish orqali, o'quvchilarda buyruqlar satri bilan ishlashga nisbatan qo'rquvni yo'qoting.
- Keyingi haftada loyihaning ichki fayl tuzilmasi (java, res, manifest, gradle) va birinchi «Hello World» dasturini yaratishimizni aytib o'ting.
