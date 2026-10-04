# 8-dars. Android Studio va Android SDK bilan tanishuv (3-qism)

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 3-hafta  
**Dars tartibi:** 8-dars (umumiy 102 darsdan 8-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Amaliy dasturlash va laboratoriya mashg'uloti  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga Android Studio muhitida yangi loyiha yaratish, parametrlarini to'g'ri sozlash, «Hello World» birinchi mobil ilovasini tayyorlash, `MainActivity.kt` va `activity_main.xml` o'rtasidagi bog'liqlikni hamda Gradle build mexanizmini amalda o'rgatish.
- **Kutiladigan natijalar:**
  - O'quvchi "New Project" oynasida to'g'ri shablon (Empty Views Activity), Package Name va Minimum SDK tanlashni biladi;
  - Layout Editor oynasining "Code", "Split" va "Design" rejimlaridan foydalana oladi;
  - `activity_main.xml` faylida `TextView` komponentining matni, o'lchami va rangini o'zgartira oladi;
  - Hardcoded matnlarni `Alt + Enter` orqali `strings.xml` resursiga ko'chirishni (Extract String Resource) o'zlashtiradi;
  - `MainActivity.kt` ichidagi `setContentView(R.layout.activity_main)` funksiyasi vazifasini tushunadi;
  - "Run" tugmasi bosilganda yuz beradigan Gradle build bosqichlarini izohlay oladi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | O'tgan mavzuni takrorlash va kirish | Loyiha papkalari (java, res, manifest, gradle) bo'yicha blits-so'rov. Dars maqsadi: "Bugun har birimiz ilk mobil ilovamizni yaratamiz!" |
| **10–30 daq** | Amaliy namoyish: Yangi loyiha yaratish | "Empty Views Activity" shablonini tanlash, `uz.edu.salomdunyo` package name, Kotlin tili, API 24 tanlash, Gradle Sync jarayoni |
| **30–50 daq** | Amaliy kodlash: XML dizayn bilan ishlash | `activity_main.xml`ni ochish, Split rejimi, `TextView` atributlari (`textSize`, `textColor`), `strings.xml`ga matn chiqarish |
| **50–65 daq** | Yangi mavzu: MainActivity va Gradle Build | `MainActivity.kt` strukturasi, `setContentView` nima qiladi? "Run" bosilganda Gradle nimalarni bajaradi? |
| **65–75 daq** | Mustaqil amaliyot | O'quvchilar o'z kompyuterlarida loyihani yaratib, o'z ism-familiyalarini ekranga chiqarishadi |
| **75–80 daq** | Xulosa va baholash | Bajarilgan ishlarni ko'rib chiqish, baholash, uyga vazifa berish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. Yangi loyiha yaratish parametrlari
Android Studio ochilganda "New Project" tugmasi bosiladi va quyidagi oynalar to'ldiriladi:
1. **Shablon tanlash:** "Empty Views Activity" (klassik XML + Kotlin modeli).
2. **Loyiha nomi (Name):** Masalan, `SalomDunyo`.
3. **Package Name:** Global unikal nom, masalan: `uz.edu.salomdunyo`.
4. **Save location:** Loyiha kompyuter xotirasida qaysi papkada saqlanishi (yo'lda ruscha yoki bo'sh joy harflari bo'lmasligi kerak).
5. **Language:** `Kotlin` (Google tomonidan Android uchun rasmiy tavsiya etilgan til).
6. **Minimum SDK:** `API 24: Android 7.0 (Nougat)` — bu parametr tanlansa, ilova dunyodagi qurilmalarning 96% dan ko'prog'ida ishlaydi.

### 3.2. Layout Editor va `activity_main.xml`
Ilovaning vizual ko'rinishi `res/layout/activity_main.xml` faylida belgilanadi.
Oynaning yuqori o'ng burchagida 3 ta rejim mavjud:
- **Code:** Faqat XML kodini ko'rsatadi;
- **Split:** Chap tomonda XML kodi, o'ng tomonda telefon ekrani (Preview) bir vaqtda ko'rinadi (eng qulay rejim);
- **Design:** Faqat vizual ekranni ko'rsatadi, elementlarni sichqoncha bilan surish mumkin.

**TextView komponenti kodi:**
```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:id="@+id/tvHello"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/hello_message"
        android:textSize="24sp"
        android:textColor="#0D47A1"
        android:textStyle="bold"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

### 3.3. `strings.xml`ga matn chiqarish (Extract String Resource)
Agar matn XML fayl ichida to'g'ridan-to'g'ri `android:text="Salom, Dunyo!"` deb yozilsa, Android Studio "Hardcoded string" degan sariq ogohlantirish beradi.
- **Tuzatish usuli:** Kursorni matn ustiga olib borib, `Alt + Enter` (Mac'da `Option + Return`) bosiladi -> **Extract string resource** tanlanadi -> Resource name: `hello_message` kiritiladi.
- Natijada matn avtomatik ravishda `res/values/strings.xml` fayliga yoziladi:
  ```xml
  <string name="hello_message">Salom, Dunyo! Men Android dasturchiman!</string>
  ```

### 3.4. `MainActivity.kt` fayli tahlili
```kotlin
package uz.edu.salomdunyo

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
```
- `AppCompatActivity`: Eski va yangi Android versiyalarida ekranlarning bir xil chiroyli ishlashini ta'minlovchi baza sinfi;
- `onCreate()`: Ekran xotirada yaratilayotgan paytda operatsion tizim tomonidan eng birinchi chaqiriladigan funksiya;
- `setContentView(R.layout.activity_main)`: **Eng muhim qator!** U Kotlin kodini `activity_main.xml` dizayn fayli bilan bog'laydi va ekranga chizib beradi.

### 3.5. "Run" bosilganda nima sodir bo'ladi? (Gradle Build mexanizmi)
Yuqori paneldagi yashil "Run" tugmasi bosilganda:
1. **Gradle tasklar ishga tushadi:** Loyiha tekshiriladi;
2. **aapt2:** XML maketlar va rasmlar binar holatga paketlanadi va `R` sinfi yaratiladi;
3. **kotlinc va d8:** Kotlin kodi `.class` baytkodiga, so'ngra `.dex` fayliga kompilyatsiya qilinadi;
4. **Paketlash:** Barcha qismlar bitta APK fayliga yig'ilib, debug kaliti bilan imzolanadi;
5. **ADB orqali yetkazish:** `adb install` buyrug'i bilan APK telefonga yoki emulyatorga yuboriladi;
6. **Ishga tushirish:** `am start` (Activity Manager) buyrug'i orqali `MainActivity` ekranda ochiladi.

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. TextView o'lchami va rangini sozlash (Oson)
**Topshiriq:** `activity_main.xml` faylidagi `TextView` matnini 28sp qilib, rangini to'q ko'k (`#0D47A1`) qilib o'zgartiring.

**Yechim:**
```xml
android:textSize="28sp"
android:textColor="#0D47A1"
```
(Eslatma: Androidda matn o'lchamlari doimo `sp` (scale-independent pixels) birligida, boshqa elementlar o'lchami esa `dp` (density-independent pixels) birligida belgilanadi).

### 2-topshiriq. setContentView vazifasini tushuntirish (O'rta)
**Topshiriq:** Agar `MainActivity.kt` ichidagi `setContentView(R.layout.activity_main)` qatori o'chirib tashlansa yoki izohga (`//`) olinsa, ilova ishga tushganda ekranda nima paydo bo'ladi?

**Yechim:**
Ilova halokatsiz (crashsiz) ochiladi, ammo ekranda hech qanday matn yoki tugma ko'rinmaydi — to'liq bo'sh oq (yoki qorong'u rejimda to'liq qora) ekran paydo bo'ladi. Chunki mantiqiy Activity ekrani o'ziga qaysi XML maketni chizish kerakligini bilmay qoladi.

### 3-topshiriq. R sinfi mexanizmi tahlili (Qiyin)
**Topshiriq:** Kodda ishlatiladigan `R.layout.activity_main` yoki `R.string.hello_message` yozuvidagi `R` harfi nima va u qanday hosil bo'ladi?

**Yechim:**
`R` — bu `aapt2` vositasi tomonidan loyihani yig'ish (build) paytida avtomatik tarzda yaratiladigan maxsus Java/Kotlin sinfidir (`Resource Index`). 
U `res/` jildidagi har bir resursga (har bir rasm, matn, XML maket va id ga) butun sonli unikal identifikator (masalan, `0x7f0b0021`) biriktiradi. Dasturchi kod ichida ushbu resurslarga `R.nomi.fayl` orqali oson va xatosiz murojaat qiladi.

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **Androidda matn o'lchami qaysi o'lchov birligida beriladi?**  
   *Javob:* `sp` (scale-independent pixels).
2. **Kodni XML dizayn bilan qaysi funksiya bog'laydi?**  
   *Javob:* `setContentView(R.layout.activity_main)`.
3. **Hardcoded matnni `strings.xml`ga o'tkazishning tezkor klavishlar kombinatsiyasi qaysi?**  
   *Javob:* `Alt + Enter` (Mac'da `Option + Return`).
4. **Layout Editor'da kod va vizual ekranni yonma-yon ko'rsatuvchi rejim qanday ataladi?**  
   *Javob:* Split rejimi.
5. **Ekran xotirada yaratilganda eng birinchi ishga tushuvchi hayotiy sikl metodi qaysi?**  
   *Javob:* `onCreate()`.

---

## 6. Mentor uchun amaliy tavsiyalar

- Barcha o'quvchilar o'z kompyuterlarida loyihani yaratib, matnni o'zgartirishi va natijani Preview ekranida ko'rishini nazorat qiling.
- Matn birligi sifatida `dp` emas, aynan `sp` ishlatilishi kerakligini ta'kidlang (chunki foydalanuvchi telefon sozlamalaridan shriftni kattalashtirganda faqat `sp` birligi unga moslashadi).
