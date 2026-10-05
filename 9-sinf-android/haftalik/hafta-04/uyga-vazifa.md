# 4-hafta: Uyga vazifalar to'plami (Android dasturlash)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

## 10-dars. Simulyator va Emulator (2-qism): Real qurilma, ADB va Logcat
1. O'z Android telefoningizda *Developer Options* va *USB Debugging* rejimini faollashtiring.
2. Android Studio'dagi *Terminal* oynasidan `adb devices` buyrug'ini ishga tushirib, telefoningiz ro'yxatda chiqqan holati skrinshotini oling.
3. `MainActivity.kt` faylida `Log.i("UY_IShI", "Ilova real telefonda muvaffaqiyatli ishga tushdi!")` kodini qo'shib, Logcat oynasidan shu xabarni topib skrinshot qiling.

---

## 11-dars. Kotlin sintaksisi (1-qism): val vs var va ma’lumot turlari
1. `val` va `var` yordamida o'z smartfoningiz haqidagi ma'lumotlarni (modeli: String, narxi: Double, xotirasi_GB: Int, quvvat_foizi: Int, kamera_bormi: Boolean) saqlovchi Kotlin dasturini yozing.
2. 3 ta fandan olingan baholarning o'rtacha arifmetik qiymatini hisoblab, `println("O'rtacha baho: ${...}")` shabloni orqali chiqaring.
3. String ko'rinishidagi narxni (`val narx = "150000"`) `toInt()` orqali butun songa o'tkazib, 12% QQS qo'shilgan yakuniy to'lov miqdorini hisoblang.

---

## 12-dars. Kotlin sintaksisi (2-qism): if va when shart operatorlari
1. Foydalanuvchi yoshiga qarab toifani (`"Bola"`, `"O'smir"`, `"Katta"`, `"Keksa"`) aniqlovchi dasturni `when (yosh)` va `in 1..12`, `in 13..18`, `in 19..60`, `else` orqali yozing.
2. Mini-Kalkulyator dasturi: ikkita son `a = 20.0`, `b = 5.0` va amal belgisi `amal = "*"` berilganda `when (amal)` yordamida to'rtala arifmetik amalni (`+`, `-`, `*`, `/`) bajaring.
3. Do'kondagi chegirma tizimi: Xarid summasiga qarab chegirma miqdorini aniqlang (100 minggacha &mdash; 0%, 500 minggacha &mdash; 5%, 1 milliongacha &mdash; 10%, 1 milliondan yuqori &mdash; 15%) va yakuniy to'lov summasini chiqaring.

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **Real qurilma, ADB va Logcat (35 ball):**
   - Developer Options va USB Debugging'ni to'g'ri faollashtirganligi (15 ball);
   - ADB orqali qurilmani bog'lay olganligi (10 ball);
   - Logcat oynasidan kerakli log xabarlarini ajrata olganligi (10 ball).

2. **Kotlin asoslari va o'zgaruvchilar (30 ball):**
   - `val` va `var` farqini tushunib, to'g'ri tanlaganligi (15 ball);
   - Kotlin ma'lumot turlari va String Templates (`$`) dan to'g'ri foydalanishi (15 ball).

3. **Shart operatorlari va when (35 ball):**
   - `if` ni ifoda sifatida qo'llay olishi (15 ball);
   - `when` operatorida oraliqlar (`in`) va `else` blokini to'g'ri yozganligi (20 ball).
