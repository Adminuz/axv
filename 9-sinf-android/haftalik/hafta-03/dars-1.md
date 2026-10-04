# 7-dars. Android Studio va Android SDK bilan tanishuv (2-qism)

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 3-hafta  
**Dars tartibi:** 7-dars (umumiy 102 darsdan 7-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Amaliy va tahliliy laboratoriya mashg'uloti  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga Android loyihasining ichki papkalar tuzilishi (`java/kotlin`, `res`, `manifests`, `Gradle Scripts`), har bir katalogning vazifasi, `AndroidManifest.xml` faylining arxitekturadagi o'rni hamda loyiha va modul darajasidagi `build.gradle` fayllarini o'rgatish.
- **Kutiladigan natijalar:**
  - O'quvchi Android loyihasi daraxtidagi asosiy kataloglarni (`java`, `res`, `manifests`, `Gradle Scripts`) mustaqil ajrata oladi;
  - `res/` papkasi ichidagi `layout`, `drawable`, `values` (`strings.xml`, `colors.xml`) jildlarining vazifasini tushunadi;
  - `AndroidManifest.xml` faylini tahlil qila oladi: ruxsatnomalar (`<uses-permission>`), `<activity>` e'loni va `LAUNCHER` intent-filtri;
  - `minSdk`, `targetSdk` va `compileSdk` tushunchalari o'rtasidagi farqni biladi;
  - Loyihaning `build.gradle` (Project) va `build.gradle` (Module: app) fayllarining vazifasini farqlay oladi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | O'tgan haftani takrorlash va kirish | Android Studio oynalari, SDK Platforms, ADB va Build-Tools bo'yicha blits-so'rov. Muammoli savol: "Android Studio'da bitta loyihani ochganimizda nega buncha ko'p papka va fayllar chiqadi?" |
| **10–30 daq** | Yangi mavzu: java/kotlin va res kataloglari | Kotlin kodlar papkasi, `res/` resurslar strukturasi: `layout/`, `drawable/`, `values/` (`strings.xml`, `colors.xml`, `themes.xml`) |
| **30–50 daq** | Yangi mavzu: AndroidManifest.xml — Ilovaning miyasi | Ilovaning komponentlari, ruxsatnomalar, ilova ikonkasi, asosiy kirish ekrani (MAIN va LAUNCHER) |
| **50–65 daq** | Yangi mavzu: Gradle Scripts | Project vs Module `build.gradle`, `minSdk`, `targetSdk`, `compileSdk` va `dependencies` bloki |
| **65–75 daq** | Amaliy mashq va fayllar tahlili | Kompyuterda ochilgan loyihaning `AndroidManifest.xml` va `strings.xml` fayllarini o'rganish |
| **75–80 daq** | Xulosa va baholash | Dars yakunlari, o'quvchilarni baholash, uyga vazifa berish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. Android loyihasining daraxtsimon tuzilishi
Android Studio'ning chap tomonidagi "Project" panelida "Android" ko'rinishi tanlanganda, fayllar quyidagi 4 ta asosiy blokda tartiblanadi:

```
MyApp/
├── manifests/
│   └── AndroidManifest.xml       <-- Ilovaning pasporti va miyasi
├── java/ (yoki kotlin/)
│   ├── uz.edu.myapp/             <-- Asosiy dastur kodi (MainActivity.kt)
│   ├── uz.edu.myapp (androidTest)<-- Qurilmada ishlovchi UI testlar
│   └── uz.edu.myapp (test)       <-- Kompyuterda ishlovchi Unit testlar
├── res/                          <-- Barcha vizual va statik resurslar
│   ├── drawable/                 <-- Rasmlar, ikonlar, vektor grafikalar (.xml, .png)
│   ├── layout/                   <-- Ekran dizaynlari (activity_main.xml)
│   ├── mipmap/                   <-- Ilova ikonkasi (har xil ekran o'lchamlari uchun)
│   └── values/                   <-- Matnlar (strings), ranglar (colors), mavzular (themes)
└── Gradle Scripts/
    ├── build.gradle.kts (Project)<-- Butun loyiha uchun umumiy konfiguratsiya
    ├── build.gradle.kts (Module) <-- Ilovaning versiyasi, SDK va kutubxonalari
    └── settings.gradle.kts       <-- Modullar va omborlar ro'yxati
```

### 3.2. `res/` (Resources) jildi va resurslarni boshqarish
Androidda dastur kodi (mantiq) va dizayn (resurslar) qat'iy ravishda bir-biridan ajratilgan:
1. **`res/layout/`:** Ekranning XML maketlari saqlanadi (masalan, `activity_main.xml`).
2. **`res/drawable/`:** Ilovada ishlatiladigan rasmlar va vektorli SVG/XML chizmalar.
3. **`res/values/strings.xml`:** Ilovadagi barcha matnlar shu yerda saqlanadi:
   ```xml
   <resources>
       <string name="app_name">Mening Ilovam</string>
       <string name="welcome_text">Xush kelibsiz!</string>
   </resources>
   ```
   *Nima uchun matnlar alohida faylda saqlanadi?* Ilovani o'zbek, rus va ingliz tillariga oson tarjima qilish (lokalizatsiya) uchun!
4. **`res/values/colors.xml`:** Asosiy brend ranglari (HEX kodlari):
   ```xml
   <resources>
       <color name="primary">#0D47A1</color>
       <color name="accent">#00E676</color>
   </resources>
   ```

### 3.3. `AndroidManifest.xml` — ilovaning pasporti
Operatsion tizim ilovani ishga tushirishdan oldin aynan ushbu faylni o'qiydi. Unda quyidagilar e'lon qilinadi:
1. **Ruxsatnomalar (Permissions):**
   ```xml
   <uses-permission android:name="android.permission.INTERNET" />
   <uses-permission android:name="android.permission.CAMERA" />
   ```
2. **Ilova atributlari:** Ilova nomi (`android:label`), ikonkasi (`android:icon`), mavzusi (`android:theme`).
3. **Komponentlar:** Barcha Activity, Service va Receiverlar e'lon qilinadi.
4. **Boshlang'ich ekran (Launcher Activity):**
   ```xml
   <activity android:name=".MainActivity" android:exported="true">
       <intent-filter>
           <action android:name="android.intent.action.MAIN" />
           <category android:name="android.intent.category.LAUNCHER" />
       </intent-filter>
   </activity>
   ```
   Aynan `MAIN` va `LAUNCHER` bo'lgan ekran smartfon menyusida ikonka sifatida paydo bo'ladi.

### 3.4. Gradle Scripts: build.gradle tahlili
Modul darajasidagi `build.gradle` faylida ilovaning eng muhim parametrlari belgilanadi:
- **`compileSdk`:** Loyiha qaysi Android SDK versiyasi yordamida kompilyatsiya qilinadi (masalan, 34);
- **`minSdk`:** Ilova ishlay oladigan eng pastki Android versiyasi (masalan, 24 — Android 7.0). Ushbu versiyadan eski telefonlarga ilova o'rnatilmaydi;
- **`targetSdk`:** Ilova qaysi versiyaning eng so'nggi xavfsizlik va dizayn talablariga moslab sinovdan o'tkazilgan;
- **`versionCode`:** Butun son (1, 2, 3...) — Google Play uchun yangilanish tartib raqami;
- **`versionName`:** Foydalanuvchi ko'radigan versiya matni (masalan, "1.0.0");
- **`dependencies`:** Tashqi kutubxonalar ro'yxati (masalan, Material Design, Retrofit, Room).

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. Kataloglar va ularning vazifasi (Oson)
**Topshiriq:** `java/`, `res/layout/`, `res/values/strings.xml` va `AndroidManifest.xml` fayllarining har biriga bittadan asosiy vazifa yozing.

**Yechim:**
- `java/`: Ilovaning mantiqiy algoritmlari va Kotlin kodlari joylashadi;
- `res/layout/`: Ekranlarning XML dizayn maketlari saqlanadi;
- `res/values/strings.xml`: Ilovadagi barcha matnlar va tarjimalar saqlanadi;
- `AndroidManifest.xml`: Tizim ruxsatlari, ilova komponentlari va kirish ekrani e'lon qilinadi.

### 2-topshiriq. minSdk va compileSdk farqi (O'rta)
**Topshiriq:** Agar ilovada `minSdk = 26` va `compileSdk = 34` deb belgilangan bo'lsa, bu nimani anglatadi? Android 8.0 (API 26) va Android 6.0 (API 23) telefonlarida ilova qanday ishlaydi?

**Yechim:**
- `minSdk = 26`: Ilova kamida Android 8.0 (API 26) versiyasiga ega qurilmalarda ishlay oladi. Android 6.0 (API 23) telefoni Google Play'da bu ilovani ko'rmaydi va o'rnatolmaydi ("Qurilmangiz ushbu versiyaga mos kelmaydi" xatosi).
- `compileSdk = 34`: Dasturchi kod yozishda eng so'nggi Android 14 (API 34) imkoniyatlari va kutubxonalaridan foydalangan holda loyihani yig'ishi mumkin.

### 3-topshiriq. Yangi ruxsatnoma qo'shish (Qiyin)
**Topshiriq:** Ilovangiz foydalanuvchining joylashgan manzilini aniqlashi va internet orqali serverga yuborishi kerak. `AndroidManifest.xml` fayliga qaysi ruxsatnomalarni qo'shish lozim?

**Yechim:**
`manifests/AndroidManifest.xml` faylining `<application>` tegi tepasiga quyidagi qatorlar qo'shiladi:
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="uz.edu.myapp">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />

    <application ...>
    ...
```

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **Ekran dizaynlari loyihaning qaysi jildida saqlanadi?**  
   *Javob:* `res/layout/` papkasida (XML formatida).
2. **Nima uchun matnlarni to'g'ridan-to'g'ri kodda emas, `strings.xml`da saqlash tavsiya etiladi?**  
   *Javob:* Ilovani boshqa tillarga oson tarjima qilish (lokalizatsiya) va kodni toza saqlash uchun.
3. **Ilova ochilganda birinchi qaysi ekran ochilishini nima belgilaydi?**  
   *Javob:* `AndroidManifest.xml` ichidagi `MAIN` va `LAUNCHER` intent-filtri.
4. **Google Play'da yangi versiya chiqarishda qaysi ko'rsatkich oshiriladi?**  
   *Javob:* `versionCode` (masalan, 1 dan 2 ga).
5. **`minSdk` qanday vazifa bajaradi?**  
   *Javob:* Ilova o'rnatilishi mumkin bo'lgan eng minimal Android versiyasini belgilaydi.

---

## 6. Mentor uchun amaliy tavsiyalar

- O'quvchilarga loyiha daraxtini ochib ko'rsating va fayllarni "chiroyli javonlardagi kitoblar"ga qiyoslang: kiyimlar bir javonda (`res`), hujjatlar boshqasida (`manifest`), asboblar uchinchi javonda (`gradle`).
- `strings.xml` orqali matnni o'zgartirish XML maketda qanday aks etishini ko'rsatib, ularda qiziqish uyg'oting.
