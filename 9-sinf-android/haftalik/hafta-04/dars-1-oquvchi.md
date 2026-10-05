# 10-dars. Simulyator va Emulator: Real qurilma, ADB va Logcat

> Kompyuteringiz emulyatordan qiynalyaptimi yoki ilovangizni haqiqiy telefoningizda ushlab ko'rmoqchimisiz? Ushbu darsda o'z Android smartfoningizni dasturlash rejimiga o'tkazishni, ADB buyruqlari va Logcat vositasini o'rganamiz.

## Dars xulosasi

- **Real qurilma afzalligi:** Emulyatorga qaraganda ancha tez ishlaydi, kompyuter xotirasini tejaydi va barcha sensorlar (kamera, GPS, akselerometr) haqiqiy ishlaydi.
- **Developer Options (Dasturchi sozlamalari):** Sozlamalar &rarr; *About Phone* &rarr; *Build Number* ustiga ketma-ket **7 marta** bosish orqali ochiladi.
- **USB Debugging (USB orqali nosozliklarni tuzatish):** Android Studio kompyuterdan telefonga ilovani to'g'ridan-to'g'ri o'rnatishi va boshqarishi uchun kerak.
- **ADB (Android Debug Bridge):** Kompyuter va telefon o'rtasidagi ko'prik vazifasini bajaruvchi buyruqlar satri vositasi (`Client`, `Server`, `Daemon`).
- **Logcat:** Android operatsion tizimi va ilovalar xabarlarini, xatolarini real vaqtda ko'rsatuvchi oyna.
- **Log darajalari:**
  - `Log.v()` &mdash; Verbose (barcha mayda xabarlar)
  - `Log.d()` &mdash; Debug (dasturchi sinov xabarlari)
  - `Log.i()` &mdash; Info (axborot)
  - `Log.w()` &mdash; Warn (ogohlantirish)
  - `Log.e()` &mdash; Error (xatolik)

## Qo'shimcha ma'lumot

### Nega "Build number" 7 marta bosiladi?
Google bu menyuni oddiy foydalanuvchilar bilmasdan telefon tizim sozlamalarini buzib qo'ymasliklari uchun yashirib qo'ygan. Faqat haqiqiy dasturchi yoki qiziquvchigina bu usulni bilib, tizimni ochadi.

### ADB simsiz (Wi-Fi orqali) ishlashi mumkinmi?
Ha! Android 11 va undan yuqori versiyalarda Android Studio'da *Pair Devices Using Wi-Fi* (QR-kod orqali) funksiyasi mavjud. Bu orqali kabel ulamasdan ham bir xil Wi-Fi tarmog'ida ilovani ishga tushirish mumkin.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Developer Options | Dasturchilar uchun yashirin tizim sozlamalari menyusi |
| USB Debugging | USB kabeli orqali ilovalarni boshqarish va testlash ruxsati |
| ADB | Android Debug Bridge &mdash; Android boshqaruv ko'prigi |
| Logcat | Tizim voqealari va xatolar jurnali oynasi |
| Crash | Dasturning kutilmagan xatolik tufayli to'xtab qolishi (qulashi) |
| RSA Key | Kompyuter va telefon o'rtasidagi xavfsiz ulanish raqamli kaliti |

## Bilasizmi?

- Google Play do'koniga yuklanadigan barcha ilovalar nashrdan oldin yuzlab real qurilmalardan iborat maxsus "Firebase Test Lab" robot-fermalarida avtomatik sinovdan o'tkaziladi.
- Logcat har bir soniyada minglab tizim xabarlarini chiqaradi. Kerakli xabarni topish uchun `tag:MY_TAG` yoki `package:mine` filtrlari qo'llaniladi.

## Topshiriqlar

### 1. Dasturchi rejimini yoqish · oson

Telefoningizda *Sozlamalar → Telefon haqida → Build Number* ustiga 7 marta bosing.

**Kutiladigan natija:** «Siz endi dasturchisiz!» xabari chiqadi va sozlamalarda *Developer Options* bo'limi paydo bo'ladi.

### 2. USB Debugging · oson

*Developer Options* ichida *USB Debugging* ni yoqing, telefonni kabel bilan ulang va RSA oynasida *Always allow* ni belgilang.

**Kutiladigan natija:** kompyuter telefonga ruxsat oldi, oyna qayta chiqmaydi.

### 3. adb devices · oson

Android Studio *Terminal* oynasida `adb devices` buyrug'ini tering.

**Kutiladigan natija:** ro'yxatda qurilma kodi va yonida `device` so'zi (`unauthorized` emas).

### 4. Telefonda ishga tushirish · oson

Yuqori paneldagi qurilmalar ro'yxatidan emulyator o'rniga telefoningizni tanlab, `Run` tugmasini bosing.

**Kutiladigan natija:** ilova telefon ekranida ochiladi.

### 5. Birinchi log xabari · o'rta

`MainActivity.kt` dagi `onCreate` ichiga `Log.d("MENING_ILOVAM", "Salom, bu mening birinchi log xabarim!")` qatorini qo'shing va `import android.util.Log` ni unutmang.

**Kutiladigan natija:** ilova ishga tushganda Logcat'da shu xabar chiqadi.

### 6. Logcat filtri · o'rta

Logcat qidiruv satriga `tag:MENING_ILOVAM` yozing. Keyin `level:error` filtrini sinab ko'ring.

**Kutiladigan natija:** birinchi filtrda faqat sizning xabaringiz, ikkinchisida faqat xatolar qoladi.

### 7. Log darajalari · o'rta

Bir vaqtda `Log.v`, `Log.d`, `Log.i`, `Log.w`, `Log.e` xabarlarini yuboring va Logcat'da qanday ko'rinishini kuzating.

**Kutiladigan natija:** 5 ta xabar; har darajaning harfi (V, D, I, W, E) va rangi farq qiladi. Jadvalga yozing.

### 8. Qaysi daraja? · o'rta

Har vaziyatga mos darajani tanlang: a) tugma bosildi (tekshirish uchun); b) internet sekin, lekin ilova ishlayapti; c) server javob bermadi va ilova yopildi; d) foydalanuvchi profili yuklandi.

**Kutiladigan natija:** 4 ta javob va har biriga bitta jumla sabab.

### 9. Crash tahlili · qiyin

Kodga ataylab xato yozing (`val a = 5 / 0`) va ilovani ishga tushiring. Logcat'dagi qizil xabardan xato turi, fayl nomi va qator raqamini toping.

**Kutiladigan natija:** `ArithmeticException` va xato bo'lgan `MainActivity.kt` qatori aniqlangan.

### 10. Emulyator yoki real qurilma? · qiyin

Uchta vaziyatda nima tanlaysiz: a) GPS orqali yo'l chizish; b) kompyuter juda kuchsiz; c) 5 xil ekran o'lchamida tez ko'rish. Har birini asoslang.

**Kutiladigan natija:** jadval: vaziyat, tanlov (emulyator / real qurilma), sabab.

### 11. ADB qismlari · qiyin

ADB ning 3 qismini (Client, Server, Daemon) sxema qilib chizing: qaysi biri kompyuterda, qaysi biri telefonda ishlaydi va buyruq qanday yo'l bosadi?

**Kutiladigan natija:** strelkali sxema: terminal → server (kompyuter) → adbd (telefon).

### 12. Ekran o'lchami logda · bonus

`resources.displayMetrics` yordamida telefon ekranining kengligi va balandligini pikselda oling va `Log.i("EKRAN", "Kenglik: $w, Balandlik: $h")` ko'rinishida chiqaring.

**Kutiladigan natija:** Logcat'da telefoningizning haqiqiy ekran o'lchamlari.

## O'zingizni tekshiring

1. Nega ilovani real qurilmada ham sinash kerak? 3 ta sabab ayting.
2. Developer Options qanday yoqiladi?
3. ADB qanday 3 qismdan iborat?
4. `adb devices` natijasida `unauthorized` chiqsa nima qilasiz?
5. Logcat nima?
6. Log darajalarini quyidan yuqoriga sanang.

## Uyga vazifa

Telefoningizda USB Debugging ni yoqing, `adb devices` natijasi va Logcat'dagi `Log.i("UY_IShI", ...)` xabarining skrinshotini oling (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
