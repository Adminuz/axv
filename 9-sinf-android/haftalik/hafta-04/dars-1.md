# 10-dars. Simulyator va Emulator: Real qurilma, ADB va Logcat

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 10-dars (umumiy 1–102)

**Manba:** rasmiy o'quv dasturi («Simulyator va Emulator haqida tushuncha: real qurilmada testlash»), o'quv qo'llanma va uslubiy ko'rsatma («ADB va Logcat kuzatuvi»).

## 1. Dars rejasi

**Maqsad:** O'quvchilarga ilovani real Android smartfonda ishga tushirish, ishlab chiquvchi sozlamalari (Developer Options), USB Debugging (USB orqali nosozliklarni tuzatish), ADB (Android Debug Bridge) ishlash tamoyili hamda Logcat oynasida xatolar va tizim xabarlarini tahlil qilishni o'rgatish.

**Kutiladigan natija:**
- Real telefon va emulyator o'rtasidagi farqni (kamera, sensorlar, batareya) tushuntira oladi;
- Telefonda «Build Number»ni 7 marta bosib Developer Options'ni yoqa oladi;
- «USB Debugging»ni faollashtirib, RSA kalitini tasdiqlaydi;
- Terminalda `adb devices` buyrug'i bilan ulangan qurilmani ko'radi;
- Android Studio Logcat oynasida darajalar (`Verbose`, `Debug`, `Info`, `Warn`, `Error`) bo'yicha filtrlashni va `Log.d()` xabarlarini topishni biladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 9-dars: Emulyator va AVD yaratish, AVD Manager |
| 5–20 daq | Yangi mavzu 1 | Nega real qurilma? Developer Options va USB Debugging yoqish |
| 20–35 daq | Yangi mavzu 2 | ADB arxitekturasi (Client, Server, Daemon) va asosiy buyruqlar |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–55 daq | Yangi mavzu 3 | Logcat oynasi, xabar darajalari va `Log.d("TAG", "xabar")` |
| 55–75 daq | Amaliyot | Ilovani USB orqali o'z telefonida ishga tushirish va Logcat'da kuzatish |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

---

## 2. Dars konspekti

### 2.1. Nega real qurilmada testlash shart?
Emulyator qulay bo'lsa-da, kompyuter protsessori va xotirasini ko'p band qiladi. Bundan tashqari:
- **Haqiqiy sensorlar:** GPS, akselerometr, giroskop, kompas va kamera real telefonda aniq ishlaydi.
- **Tezlik va unumdorlik:** Ilova kuchsiz yoki o'rta darajadagi telefonlarda qotmasdan ishlashini faqat real qurilmada ko'rish mumkin.
- **Resurs tejamkorligi:** Zaif kompyuterlarda Android Studio bilan birga og'ir emulyatorni ochmasdan, to'g'ridan-to'g'ri USB kabel orqali telefondan foydalanish ancha samarali.

### 2.2. Telefonda Developer Options va USB Debugging yoqish
1. **Sozlamalar (Settings)** &rarr; **Telefon haqida (About Phone)** bo'limiga kiriladi.
2. **Dasturiy ta'minot ma'lumotlari (Software Information)** &rarr; **Build Number (Tuzilma raqami)** topiladi.
3. `Build Number` ustiga ketma-ket **7 marta** bosiladi («Siz endi dasturchisiz!» xabari chiqadi).
4. Sozlamalar menyusida yangi **Developer Options (Ishlab chiquvchi parametrlari)** bo'limi paydo bo'ladi.
5. U yerdan **USB Debugging (USB orqali nosozliklarni tuzatish)** yoqiladi.
6. Telefon kompyuterga ulanganda ekranga RSA barmoq izi chiqadi: «Har doim ruxsat berish (Always allow)» belgilanadi.

### 2.3. ADB (Android Debug Bridge) nima?
ADB &mdash; kompyuter bilan Android qurilmasi o'rtasida aloqa o'rnatuvchi universal buyruqlar satri vositasi.
U 3 qismdan iborat:
- **Client:** dasturchi terminalda yozadigan buyruqlar (`adb devices`, `adb install app.apk`).
- **Server:** kompyuter fonida ishlovchi jarayon (Client va Daemon o'rtasidagi ko'prik).
- **Daemon (adbd):** Android telefonining fonida ishlovchi xizmat.

### 2.4. Logcat va Log darajalari
Logcat &mdash; Android operatsion tizimi va ilovalarning barcha voqea va xatolarini real vaqtda ko'rsatuvchi jurnal (konsol).

Kotlin kodida xabar yozish:
```kotlin
import android.util.Log

Log.d("MY_APP", "Tugma bosildi va ma'lumot yuklandi!")
Log.e("MY_APP", "Internetga ulanib bo'lmadi!", exception)
```

Log darajalari:
- **V (Verbose):** Barcha mayda xabarlar (eng quyi daraja).
- **D (Debug):** Dasturchi uchun tekshirish xabarlari.
- **I (Info):** Oddiy axborot xabarlari.
- **W (Warn):** Xavf haqida ogohlantirish (ilova to'xtamaydi).
- **E (Error):** Jiddiy xatolik (ilova qulashi / Crash).

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. ADB orqali qurilmani tekshirish (oson)
Terminalda `adb devices` buyrug'ini ishga tushiring va telefoningiz ro'yxatda `device` holatida ko'rinishiga erishing.

**Yechim:**
```bash
adb devices
# List of devices attached
# R58M123456X    device
```

### 2-topshiriq. Logcat'da shaxsiy xabar chiqarish (o'rta)
`MainActivity.kt` ichidagi `onCreate()` metodida `Log.d("DARS_10", "Salom, mening birinchi ilovam ishga tushdi!")` kodini qo'shing va Logcat oynasida qidiruv orqali uni toping.

**Yechim:**
```kotlin
package uz.axv.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        Log.d("DARS_10", "Salom, mening birinchi ilovam ishga tushdi!")
    }
}
```

### 3-topshiriq. Crash (ilova qulashi) xatosini Logcat'da tutish (qiyin)
Ataylab 0 ga bo'lish amalini yozing (`val x = 10 / 0`) va Logcat'dan `ArithmeticException` qaysi qatorda yuz berganini aniqlang.

**Yechim:**
```kotlin
Log.e("DARS_10", "Xatolik ro'y berdi: java.lang.ArithmeticException: divide by zero at MainActivity.onCreate(MainActivity.kt:15)")
```

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **Developer Options menyusini qanday ochamiz?**
   - *Javob:* About phone &rarr; Build number ustiga 7 marta bosish orqali.
2. **USB Debugging nima uchun kerak?**
   - *Javob:* Android Studio kompyuterdan telefonga ilovani o'rnatishi va xatolarni tuzatishi (debug) uchun.
3. **`adb devices` buyrug'i `unauthorized` desa nima qilish kerak?**
   - *Javob:* Telefon ekranidagi «Allow USB debugging» oynasida «Allow» (Ruxsat berish) tugmasini bosish kerak.
4. **Logcat nima?**
   - *Javob:* Android tizimida barcha ilovalarning xabarlari va xatoliklarini ko'rsatuvchi markaziy jurnal oynasi.
5. **Log darajalaridan `Log.e` nimani bildiradi?**
   - *Javob:* Error &mdash; qizil rangdagi xatolik xabarlarini bildiradi.

---

## 5. Uyga vazifa

1. Uyda o'z Android telefoningizda Developer Options va USB Debugging parametrlarini yoqing.
2. Android Studio'da yaratgan «Hello World» ilovangizni USB orqali o'z telefoningizda ishga tushiring.
3. `Log.i("UY_IShI", "Ilova mening telefonimda muvaffaqiyatli ishga tushdi!")` kodini yozib, Logcat skrinshotini oling.
