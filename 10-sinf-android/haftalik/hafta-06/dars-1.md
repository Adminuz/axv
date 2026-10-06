# 16-dars. Gradle so'rovlarini (tasks) bajarish va xatoliklarni aniqlash

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 6-hafta, 1-dars (umumiy 16-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `uslubiy-korsatma.txt` (Gradle Build Lifecycle, Gradle Commands, Amaliy xulosalar), `oquv-dasturi.txt`. `--stacktrace`, `--info` va `tasks` buyrug'i standart Gradle bilimidan qo'shildi.

---

## Darsning maqsadi

`Gradle` ning 3 bosqichli hayotiy siklini (Initialization, Configuration, Execution), task tushunchasini, terminaldan `./gradlew clean`, `assembleDebug`, `bundleRelease`, `tasks` buyruqlarini bajarishni va Build oynasidagi xatoni o'qib, sababini aniqlashni o'rgatish.

## Kutilayotgan natijalar

- Gradle ning 3 bosqichini ketma-ket aytadi va xato qaysi bosqichda bo'lganini taxmin qiladi;
- `./gradlew clean`, `assembleDebug`, `bundleRelease`, `tasks` buyruqlarini bajaradi;
- APK va AAB farqini tushuntiradi;
- Build xatosini o'qiydi: qaysi fayl, qaysi qator, qaysi task;
- `--stacktrace` va `--info` bayroqlarini ishlatadi.

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 15-dars: kutubxonalar, versiyalar, `force`, `exclude` |
| 08–25 | Yangi mavzu 1 | Gradle hayotiy sikli: 3 bosqich |
| 25–38 | Yangi mavzu 2 | Tasks va `gradlew` buyruqlari, APK va AAB |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | Xatoni o'qish: Build oynasi, `--stacktrace`, `--info` |
| 58–75 | Amaliyot | Ataylab xato yasab, uni topish |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. Initialization, Configuration, Execution

Gradle ishga tushganda 3 bosqichdan o'tadi. **Initialization** — `settings.gradle` o'qiladi va qaysi modullar borligi aniqlanadi. **Configuration** — har bir modulning `build.gradle` fayli o'qiladi: qaysi kutubxona, qaysi versiya, qaysi variant. **Execution** — rejalashtirilgan vazifalar (tasks) birin-ketin bajariladi: kod kompilyatsiya qilinadi, resurslar bog'lanadi, APK yasaladi. Bosqichni bilsangiz, xato qayerda ekanini tez taxmin qilasiz: fayl topilmasa — initialization, `build.gradle` sintaksisi — configuration, kod xatosi — execution.

```kotlin
// 1. Initialization: settings.gradle.kts
include(":app", ":core")

// 2. Configuration: app/build.gradle.kts
dependencies {
    implementation("io.coil-kt:coil-compose:2.3.0")
}

// 3. Execution: terminalda
// ./gradlew assembleDebug
```

Task — Gradle bajaradigan eng kichik ish birligi: masalan, «rasmlarni siq» yoki «kodni tekshir».

### 2. Terminaldan Gradle ni boshqarish

Tajribali dasturchi Gradle ni faqat Android Studio tugmalari bilan emas, terminaldan ham boshqaradi. **`./gradlew clean`** eski yig'ilgan fayllarni o'chiradi: «nega ishlamayapti?» deb qolganda birinchi shu. **`./gradlew assembleDebug`** Debug APK yasaydi. **`./gradlew bundleRelease`** Google Play uchun AAB tayyorlaydi. **`./gradlew tasks`** mavjud tasklar ro'yxatini ko'rsatadi. `gradlew` — Gradle Wrapper: boshqa kompyuterda Gradle o'rnatilmagan bo'lsa ham, loyiha bir xil versiyada ochiladi.

```bash
./gradlew tasks
./gradlew clean
./gradlew assembleDebug
./gradlew test
./gradlew bundleRelease
```

Windows da `gradlew.bat clean` yoki `.\gradlew clean` yoziladi. APK — to'g'ridan-to'g'ri o'rnatiladigan fayl; AAB — Play ga yuklanadigan format.

### 3. Build xatosini o'qish

Xato chiqqanda panikaga tushmang: Build oynasidagi **birinchi** qizil qatorni o'qing. U ko'pincha fayl nomi, qator raqami va sababni aytadi. Keyin xato turini aniqlang: **Sync xatosi** (kutubxona topilmadi, noto'g'ri versiya), **kompilyatsiya xatosi** (kod xatosi), **dependency conflict** (ikki kutubxona bir kutubxonaning turli versiyasini talab qiladi). Ko'proq ma'lumot kerak bo'lsa, `--stacktrace` (xatoning to'liq izi) va `--info` (batafsil log) bayroqlarini qo'shing. `build.gradle` ni o'zgartirgach, Sync Now ni bosish shart.

```bash
./gradlew assembleDebug --stacktrace
./gradlew assembleDebug --info
./gradlew app:dependencies
```

Qo'llanmaga ko'ra, Sync Now bosilmasa o'zgarishlar kuchga kirmaydi. Doim aniq xato matnini o'qing, taxmin qilmang.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Bosqichni toping

Xato: `settings.gradle` da yozilgan modul papkasi topilmadi. Qaysi bosqichda xato chiqdi?

**Yechim:** Initialization: modullar ro'yxati shu bosqichda o'qiladi.

### 2-topshiriq (oson). Buyruqni tanlang

Ilovani sinash uchun APK yasash, Google Play uchun AAB yasash va eski fayllarni tozalash buyruqlarini yozing.

**Yechim:**
```kotlin
./gradlew assembleDebug
./gradlew bundleRelease
./gradlew clean
```

### 3-topshiriq (o'rta). Xatoni tuzating

`implementaton("io.coil-kt:coil-compose:2.3.0")` yozilgan. Xatoning sababi va tuzatish?

**Yechim:** `implementation` so'zida harf tushib qolgan: `implementaton`. To'g'ri yozuv: `implementation(...)`.

### 4-topshiriq (o'rta). Tasklar ro'yxati

`tasks` ro'yxatidan `assembleDebug` va `bundleRelease` vazifasini yozing.

**Yechim:** `assembleDebug` — Debug APK; `bundleRelease` — Play uchun Release AAB.

### 5-topshiriq (qiyin). Ataylab xato

Kutubxona versiyasini ataylab noto'g'ri yozing (`coil-compose:2.3.99`), `./gradlew assembleDebug --stacktrace` ishga tushiring va xato matnidan sababni toping.

**Yechim:** Birinchi qizil qator: kutubxona topilmadi (Could not find ...). Sabab: bunday versiya mavjud emas. Tuzatish: `2.3.0`.

### 6-topshiriq (bonus). Daraxt

Daraxtdan bitta ichki kutubxonani toping.

**Yechim:** Daraxtda kutubxona ostida transitive bog'liqliklar ko'rinadi.

---

## Tezkor nazorat

1. Gradle ning 3 bosqichi? **Javob:** Initialization, Configuration, Execution.
2. `clean` nima qiladi? **Javob:** Eski yig'ilgan fayllarni o'chiradi.
3. APK va AAB farqi? **Javob:** APK o'rnatiladi; AAB Google Play ga yuklanadi.
4. Xatoni qanday o'qiysiz? **Javob:** Build oynasidagi birinchi qizil qatordan boshlab.
5. `--stacktrace` nima uchun? **Javob:** Xatoning to'liq izini ko'rsatadi.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
