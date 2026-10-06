# 6-hafta: Uyga vazifa

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: Gradle tasks va xatolar · qiyin

1. Terminalda `./gradlew tasks`, `clean` va `assembleDebug` ni ishga tushiring; natijani skrinshot qiling.
2. Kutubxona nomini yoki versiyasini ataylab noto'g'ri yozing, `--stacktrace` bilan xatoni ko'ring va sababini bir jumlada yozing.
3. APK va AAB farqini 3 jumlada yozing.

---

## Topshiriq 2: Kutubxonalarni ulash va boshqarish · o'rta

1. Loyihangizga Coil (`2.3.0`) va yana bitta kutubxona (Gson yoki Retrofit) ulang va Sync ni tasdiqlang.
2. `./gradlew app:dependencies` natijasidan bitta kutubxonaning ichki kutubxonalarini 3 qatorda yozing.
3. Qo'lda yozilgan `kapt` bo'lsa, `ksp` ga o'tkazish rejasini yozing (3 qadam).

---

## Topshiriq 3: Dependency turlari · oson

1. Ikki modulli loyihada (`app`, `core`) Retrofit ni `core` da `api`, Gson ni `implementation` bilan ulang va `app` dan ikkalasini ishlatib ko'ring.
2. Natijani 3 jumlada yozing: qaysi biri ko'rindi va nima uchun.
3. JUnit va Espresso ni to'g'ri turlar bilan ulang.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: Gradle buyruqlari va xatoni topish | 3 |
| 17-dars: 2 ta kutubxonani ulash va daraxtni tahlil qilish | 3 |
| 18-dars: turlarni core va app modullarida qo'llash | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: --stacktrace nima uchun?? Javobi: Xatoning to'liq izini ko'rsatadi.
- 17-dars: Ziddiyatni qanday ko'rasiz?? Javobi: ./gradlew app:dependencies bilan.
- 18-dars: Default qaysi tur?? Javobi: implementation.

**Keng tarqalgan xatolar:**
- 16-dars: Avval birinchi qizil qator, keyin --stacktrace: odatda birinchi xabarda asosiy sabab bo'ladi.
- 17-dars: Stable nashr uchun; alpha va beta hali to'liq sinovdan o'tmagan.
- 18-dars: app odatda core, data, feature modullariga implementation(project(...)) bilan bog'lanadi.
