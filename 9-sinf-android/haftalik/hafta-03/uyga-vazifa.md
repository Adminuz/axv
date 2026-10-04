# 3-hafta: Uyga vazifalar to'plami (Android dasturlash)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

## 7-dars. Android Studio va Android SDK bilan tanishuv (2-qism)
1. Android loyihasidagi 4 ta asosiy katalog va fayllarning (`java/`, `res/layout/`, `res/values/strings.xml`, `AndroidManifest.xml`) vazifasini daftaringizga yozing.
2. Ilovada yangi til (masalan, rus tili yoki ingliz tili) qo'shish uchun `res/` papkasida qanday fayllar yaratilishini tushuntiring.
3. `minSdk`, `targetSdk` va `compileSdk` nima ekanini va nima sababdan `minSdk` ilova o'rnatilishi mumkin bo'lgan telefonlar doirasini cheklashini bayon qiling.

---

## 8-dars. Android Studio va Android SDK bilan tanishuv (3-qism)
1. Kompyuteringizda Android Studio orqali `MeningBirinchiIlovam` loyihasini yarating. Ekranga o'z ism-familiyangizni va sinfingizni chiqaring.
2. Ekrondagi `TextView` matnini 28sp qilib, rangini to'q yashil (`#2E7D32`) qilib sozlang.
3. `Alt + Enter` (Extract string resource) orqali matnni `strings.xml` fayliga o'tkazing va `strings.xml` fayli skrinshotini oling.
4. "Run" tugmasi bosilganda nima sodir bo'lishini (Gradle build, aapt2, d8, APK va ADB) bosqichma-bosqich yozing.

---

## 9-dars. Simulyator va Emulator haqida tushuncha (1-qism)
1. Simulyator va Emulyator o'rtasidagi 2 ta eng muhim texnik farqni yozma tushuntiring.
2. Android Studio'da AVD (Android Virtual Device) yaratish qadamlarini (Device, System Image: Google APIs, RAM ajratish) tasvirlang.
3. Nima uchun kompyuter BIOS sozlamalarida apparat virtualizatsiyasi (Intel VT-x / AMD-V) yoqilgan bo'lishi shartligini tushuntiring.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Loyiha tuzilmasi va resurslar (30 ball):**
   - Loyiha kataloglari vazifalarini to'g'ri tushuntirishi (10 ball);
   - `AndroidManifest.xml` va ruxsatnomalar rolini bilishi (10 ball);
   - `strings.xml` va lokalizatsiya tamoyillarini to'g'ri qo'llay olishi (10 ball).

2. **Birinchi ilova va XML dizayn (35 ball):**
   - Loyihani xatosiz yaratishi va parametrlarni to'g'ri sozlashi (10 ball);
   - `TextView` atributlari (`textSize`, `textColor`) va `sp` birligidan to'g'ri foydalanishi (15 ball);
   - Gradle build bosqichlarini va `setContentView` vazifasini tushunishi (10 ball).

3. **Emulyator va virtualizatsiya (35 ball):**
   - Simulyator va Emulyator farqini ilmiy asoslay olishi (15 ball);
   - AVD sozlamalari va Google APIs ahamiyatini bilishi (10 ball);
   - CPU virtualizatsiyasi (VT-x / AMD-V) vazifasini tushunishi (10 ball).

### Kutiladigan namunaviy natijalar
- O'quvchi matn o'lchov birligi sifatida `dp` emas, balki `sp` (scale-independent pixels) ishlatilishining sababini to'g'ri asoslay olishi shart;
- Emulyator apparat ta'minotini to'liq modellashtirishi va nima sababdan BIOS'da virtualizatsiya talab etilishi aniq ifodalanishi kerak.
