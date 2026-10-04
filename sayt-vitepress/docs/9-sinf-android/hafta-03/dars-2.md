---
title: "8-dars. Android Studio va Android SDK bilan tanishuv (3-qism)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "week": {"n": 3, "link": "/9-sinf-android/hafta-03/"}, "g": 8, "title": "Android Studio va Android SDK bilan tanishuv (3-qism)", "lead": "", "slide": "/slaydlar/9-sinf-android/hafta-03/dars-2.html", "tabs": [{"g": 7, "link": "/9-sinf-android/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/9-sinf-android/hafta-03/dars-2", "current": true}, {"g": 9, "link": "/9-sinf-android/hafta-03/dars-3", "current": false}], "prev": {"g": 7, "title": "Android Studio va Android SDK bilan tanishuv (2-qism)", "link": "/9-sinf-android/hafta-03/dars-1"}, "next": {"g": 9, "title": "Simulyator va Emulator haqida tushuncha (1-qism)", "link": "/9-sinf-android/hafta-03/dars-3"}}
---

Bugungi darsda biz barcha dasturchilar bosib o'tadigan eng hayajonli qadamni qo'yamiz: Android Studio'da o'zimizning birinchi mobil ilovamizni — **«Salom, Dunyo!» (Hello World)** dasturini noldan yaratamiz! XML maketlar bilan ishlash, matnlarni chiroyli qilish va "Run" tugmasi bosilganda nima sodir bo'lishini o'rganamiz.

---

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar

- **Empty Views Activity** — klassik XML dizayn va Kotlin mantiqiga ega bo'lgan toza boshlang'ich loyiha shabloni.
- **Layout Editor (Split rejimi)** — bir vaqtning o'zida ham XML kodini, ham telefon ekranidagi natijani ko'rsatuvchi eng qulay ishchi rejim.
- **TextView** — ekranga matn chiqaruvchi asosiy vizual komponent.
- **sp (Scale-independent Pixels)** — foydalanuvchi tizim sozlamalariga moslashuvchi maxsus shrift o'lchov birligi.
- **setContentView()** — Kotlin dastur kodini XML dizayn fayli bilan biriktiruvchi "sehrli" funksiya.
- **Extract String Resource** — matnni XML ichidan `res/values/strings.xml` fayliga avtomatik ko'chirish usuli.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. Yangi loyiha yaratish qadamlari

1. Android Studio'ni ochib, **«New Project»** tugmasini bosing;
2. Shablonlar orasidan **«Empty Views Activity»** ni tanlang va «Next» bosing;
3. Sozlamalarni to'ldiring:
   - **Name:** `SalomDunyo`
   - **Package name:** `uz.edu.salomdunyo`
   - **Language:** `Kotlin`
   - **Minimum SDK:** `API 24: Android 7.0 (Nougat)`
4. **«Finish»** tugmasini bosing va Gradle loyihani yig'ib bo'lishini (Gradle Sync) kuting.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. Dizayn bilan tanishuv: `activity_main.xml`

Loyiha ochilgach, `app/res/layout/activity_main.xml` faylini oching. Oynaning yuqori o'ng burchagidagi **«Split»** tugmasini bosing:

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
        android:text="Salom, Dunyo!"
        android:textSize="26sp"
        android:textColor="#0D47A1"
        android:textStyle="bold"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. Matnni `strings.xml`ga o'tkazish

Agar matnni to'g'ridan-to'g'ri `android:text="Salom, Dunyo!"` deb yozsangiz, sariq ogohlantirish chiqadi.
- Kursorni matn ustiga qo'ying;
- Klaviatirada **`Alt + Enter`** (Mac'da `Option + Return`) tugmalarini bosing;
- Chiqqan menyudan **«Extract string resource»** ni tanlang;
- Resurs nomiga `salom_matni` deb yozing va OK bosing.
- Endi matningiz `res/values/strings.xml` faylida xavfsiz saqlanadi!

---

</div>

<div class="blk">

## <Icon name="file-text" /> 4. `MainActivity.kt` qanday ishlaydi?

`app/java/uz/edu/salomdunyo/MainActivity.kt` faylini oching:

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

- `onCreate()` — ilova ekrani ochilayotganda birinchi bo'lib chaqiriladi.
- `setContentView(R.layout.activity_main)` — bu qator biz chizgan `activity_main.xml` dizaynini ekranga chiqaradi!

---

</div>

<div class="blk">

## <Icon name="file-text" /> 5. "Run" bosilganda nima sodir bo'ladi?

Yashil **«Run»** tugmasini bosganingizda:
1. **Gradle** loyihani yig'adi;
2. **aapt2** rasmlar va XML fayllarni binar paketlaydi;
3. **d8** kompilyatori kodni `.dex` baytkodiga aylantiradi;
4. Barcha qismlar bitta **APK** fayliga birlashadi;
5. **ADB** vositasi APK'ni telefonga o'rnatadi va ochib beradi!

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

1. **Birinchi loyihani yarating** `· oson`  
   Android Studio'da `MeningBirinchiIlovam` nomli yangi loyiha oching. Minimum SDK qilib API 24 ni tanlang.

2. **Split rejimini yoqing** `· oson`  
   `activity_main.xml` faylini ochib, Split rejimiga o'ting. Preview oynasida telefon maketini ko'ring.

3. **Matnni o'zgartiring** `· oson`  
   Ekrondagi matnni o'z ism-familiyangizga va sinfingizga o'zgartiring (masalan: "Ali Valiyev — 9-sinf dasturchisi").

4. **Matn o'lchami va rangini sozlang** `· o'rta`  
   `TextView` komponentiga `android:textSize="28sp"` va `android:textColor="#2E7D32"` (to'q yashil) parametrlarini qo'shing.

5. **sp va dp farqi** `· o'rta`  
   Nima uchun matnlar o'lchami faqat `sp` da, boshqa tugma va rasmlar o'lchami esa `dp` da berilishini tushuntiring.

6. **Extract string resource amalini bajaring** `· o'rta`  
   `Alt + Enter` yordamida ekrandagi matnni `strings.xml` fayliga o'tkazing va `strings.xml` faylini ochib, uning qanday yozilganini ko'ring.

7. **setContentView'ni sinab ko'ring** `· o'rta`  
   `MainActivity.kt` ichidagi `setContentView(...)` qatorini vaqtincha izohga (`//`) olib, ilovani ishga tushiring. Ekranda nima o'zgarganini daftaringizga yozing.

8. **Ikkinchi TextView qo'shing** `· qiyin`  
   Ekraningizga ikkinchi `TextView` komponentini qo'shing. Unda maktabingiz nomi yozilsin va u birinchi matnning ostida joylashsin.

9. **Gradle build bosqichlarini tasvirlang** `· qiyin`  
   "Run" tugmasi bosilgandan to ilova ochilguncha yuz beradigan 5 ta asosiy qadamni zanjir ko'rinishida yozing.

10. **Tadqiqotchi dasturchi** `· bonus`  
    `ConstraintLayout` nima ekanini va undagi `layout_constraint...` parametrlari matnni ekran markazida ushlab turish uchun qanday ishlashini tadqiq qiling.

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- «Hello, World!» dasturini birinchi bo'lib 1978-yilda afsonaviy muhandis Brayan Kernigan o'zining «C dasturlash tili» kitobida kiritgan. O'shandan beri dunyodagi barcha dasturchilar yangi til yoki platformani o'rganishni aynan shu jumlani ekranga chiqarishdan boshlashadi!

---

</div>

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- «Empty Views Activity» — yangi boshlovchilar uchun eng qulay boshlang'ich modeldir.
- Ekranning vizual qismi `activity_main.xml`da, mantiqiy kodi esa `MainActivity.kt`da yoziladi.
- Matnlar doimo `sp` birligida va `strings.xml` faylida saqlanishi kerak.
- `setContentView()` kodi XML dizaynni ekranga chizib beradi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Yangi loyiha yaratishda qaysi shablon tanlanadi?
2. Matn o'lchami qaysi birlikda beriladi?
3. Matnni `strings.xml`ga chiqarish uchun qaysi klavishlar bosiladi?
4. Kod va dizaynni bog'lovchi funksiya qaysi?
5. "Run" bosilganda loyihani kim yig'adi?

</div>

