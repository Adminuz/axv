# 18-dars. implementation, api, compileOnly kabi dependency turlari

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 6-hafta, 3-dars (umumiy 18-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `uslubiy-korsatma.txt` (bog'liqlik turlari: implementation, api, testImplementation, androidTestImplementation), `oquv-qollanma.txt` (implementation, api, compileOnly farqlari, transitive dependency). `runtimeOnly` va ko'p modulli misol standart Gradle bilimidan qo'shildi.

---

## Darsning maqsadi

`implementation`, `api`, `compileOnly`, `runtimeOnly`, `testImplementation` va `androidTestImplementation` turlarining farqini, ular nimani ko'rinadigan qilishini, ko'p modulli loyihada tanlash qoidasini va noto'g'ri tanlov build tezligiga qanday ta'sir qilishini tushuntirish.

## Kutilayotgan natijalar

- `implementation` ni asosiy tur sifatida tushuntiradi;
- `api` ni qachon ishlatishni (kutubxona moduli) biladi;
- `compileOnly` va `runtimeOnly` farqini aytadi;
- Test turlarini (`testImplementation`, `androidTestImplementation`) to'g'ri tanlaydi;
- Ko'p modulli loyihada tur tanlash qoidasini qo'llaydi.

## Jihozlar

Kompyuter, Android Studio (Gradle sinxronlash uchun internet), namunaviy loyiha.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 17-dars: repository, BOM, versiya, ziddiyat |
| 08–25 | Yangi mavzu 1 | `implementation` va `api` |
| 25–38 | Yangi mavzu 2 | `compileOnly` va `runtimeOnly` |
| 38–43 | Tanaffus | |
| 43–58 | Yangi mavzu 3 | Test turlari, tur tanlash qoidasi |
| 58–75 | Amaliyot | `app` va `core` modullarida turlarni qo'llash |
| 75–80 | Xulosa | Nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. `implementation` va `api` farqi

**`implementation`** — eng ko'p ishlatiladigan tur: kutubxona faqat joriy modul ichida ko'rinadi. **`api`** — kutubxona modulni ishlatayotgan boshqa modullarga ham «ochiladi». Misol: `core` moduli `retrofit` ni `api` bilan ulasa, `app` ham `retrofit` sinflarini ko'radi; `implementation` bilan ulansa, ko'rmaydi. Qoida: avval `implementation`; `api` ni faqat boshqa modul shu kutubxona sinflarini ochiq API sifatida ishlatishi kerak bo'lsagina yozing. `implementation` build ni tezlashtiradi, chunki o'zgarish kamroq modulni qayta yig'ishga majbur qiladi.

```kotlin
// core/build.gradle.kts
dependencies {
    implementation("com.google.code.gson:gson:2.10.1")   // faqat core ichida
    api("com.squareup.retrofit2:retrofit:2.9.0")         // app ham ko'radi
}

// app/build.gradle.kts
dependencies {
    implementation(project(":core"))
}
```

Shubhalansangiz, `implementation` yozing. `api` keraksiz yozilsa, modullar orasida ortiqcha bog'liqlik va sekin build paydo bo'ladi.

### 2. `compileOnly` va `runtimeOnly`

**`compileOnly`** — kutubxona faqat kompilyatsiya vaqtida kerak, APK ga qo'shilmaydi. Masalan, annotatsiya kutubxonalari yoki ish vaqtida boshqa joydan keladigan kutubxona. **`runtimeOnly`** — aksincha: kompilyatsiyada kod uni ko'rmaydi, lekin ilova ishlayotganda kerak (masalan, ish vaqtida ulanadigan drayver). Ikkalasi kamdan-kam ishlatiladi, lekin «farqi nima?» savoli suhbatlarda ko'p so'raladi. Xulosa: `implementation` — kompilyatsiya va ish vaqti ikkalasi uchun; `compileOnly` — faqat kompilyatsiya; `runtimeOnly` — faqat ish vaqti.

```kotlin
dependencies {
    implementation("io.coil-kt:coil-compose:2.3.0")    // kompilyatsiya + ish vaqti
    compileOnly("javax.annotation:jsr250-api:1.0")     // faqat kompilyatsiya
    runtimeOnly("org.postgresql:postgresql:42.7.3")   // faqat ish vaqti
}
```

`compileOnly` kutubxonasi APK ga tushmaydi: ish vaqtida kerak bo'lsa, ilova «class topilmadi» xatosi beradi.

### 3. `testImplementation` va `androidTestImplementation`

Test kutubxonalarini ilova ichiga qo'shib yubormaslik uchun alohida turlar bor. **`testImplementation`** — faqat unit testlar (kompyuterdagi JVM da) uchun, masalan JUnit. **`androidTestImplementation`** — Android qurilmada ishlaydigan testlar uchun, masalan Espresso. Bu turlar yozilgan kutubxona release APK ga tushmaydi. Qoidalar: 1) default — `implementation`; 2) boshqa modullarga ochish kerak — `api`; 3) faqat kompilyatsiya — `compileOnly`; 4) faqat ish vaqti — `runtimeOnly`; 5) testlar uchun — `testImplementation` yoki `androidTestImplementation`.

```kotlin
dependencies {
    implementation("io.coil-kt:coil-compose:2.3.0")
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
}
```

JUnit ni `implementation` bilan yozsangiz, u release APK ga tushadi va hajmni oshiradi.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Turni tanlang

JUnit, Coil, annotatsiya va drayver uchun tur tanlang.

**Yechim:** JUnit — `testImplementation`; Coil — `implementation`; annotatsiya — `compileOnly`; drayver — `runtimeOnly`.

### 2-topshiriq (oson). implementation yoki api

`core` dagi Gson faqat `core` ichida ishlatiladi. Qaysi tur to'g'ri?

**Yechim:** `implementation`: boshqa modullarga ochish shart emas.

### 3-topshiriq (o'rta). Retrofit ni oching

`core` Retrofit ni `app` ga ochishi kerak. Yozing.

**Yechim:**
```kotlin
dependencies {
    api("com.squareup.retrofit2:retrofit:2.9.0")
}
```

### 4-topshiriq (o'rta). Test kutubxonalari

JUnit va Espresso ni to'g'ri turlar bilan yozing.

**Yechim:**
```kotlin
dependencies {
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")
}
```

### 5-topshiriq (qiyin). Ikki modul

`core` da Retrofit (`api`), Gson (`implementation`); `app` `core` ga bog'lansin.

**Yechim:**
```kotlin
// core
dependencies {
    api("com.squareup.retrofit2:retrofit:2.9.0")
    implementation("com.google.code.gson:gson:2.10.1")
}
// app
dependencies {
    implementation(project(":core"))
}
```

### 6-topshiriq (qiyin). Xatoni tushuntiring

`app` Gson ni ishlatdi, `core` da u `implementation`. Nima bo'ladi, qanday tuzatasiz?

**Yechim:** Kompilyatsiya xatosi: sinf topilmadi. Tuzatish: Gson ni `app` ga alohida `implementation` qiling yoki `core` da `api` ga o'zgartiring.

### 7-topshiriq (bonus). runtimeOnly

Farqini yozing.

**Yechim:** `compileOnly` faqat kompilyatsiyada ko'rinadi, APK ga tushmaydi; `runtimeOnly` kodda ko'rinmaydi, lekin ish vaqtida kerak.

---

## Tezkor nazorat

1. `implementation` va `api` farqi? **Javob:** `implementation` faqat joriy modulda, `api` boshqa modullarga ham ochadi.
2. `compileOnly` nima? **Javob:** Faqat kompilyatsiya vaqtida kerak, APK ga tushmaydi.
3. `runtimeOnly` nima? **Javob:** Faqat ish vaqtida kerak.
4. JUnit qaysi turda? **Javob:** `testImplementation`.
5. Default qaysi tur? **Javob:** `implementation`.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
