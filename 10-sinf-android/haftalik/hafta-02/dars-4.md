# 4-dars: Dependency management va ziddiyatlarni hal qilish

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 2-hafta, 1-dars (umumiy 4-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Android ilovalarida murakkab tashqi kutubxonalar va ularning zanjirli bog'liqliklari — **Tranzitiv bog'liqliklar (Transitive Dependencies)** mexanizmini o'rgatish; Gradle'da kutubxonalar o'rtasida yuzaga keladigan versiya to'qnashuvlari (Dependency Conflicts) sabablarini tahlil qilish; `./gradlew app:dependencies` buyrug'i yordamida bog'liqliklar daraxtini o'qish; keraksiz modullarni chiqarib tashlash uchun `exclude` qoidalari hamda ziddiyatli holatlarda `resolutionStrategy` va `force` vositalari orqali versiyalarni boshqarish amaliy ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Tranzitiv bog'liqlik nima ekanini va bitta kutubxona loyihaga o'nlab qo'shimcha modullarni ergashtirib kelishini tushunish;
- Kutubxonalar o'rtasida versiya ziddiyati (Conflict) qanday paydo bo'lishini va Gradle standart holda qaysi versiyani tanlashini (eng yuqori versiya strategiyasi) bilish;
- Terminalda `./gradlew app:dependencies` buyrug'i orqali bog'liqliklar daraxtini (Dependency Tree) tahlil qila olish;
- Keraksiz yoki eskirgan tranzitiv kutubxonalarni loyihadan chiqarib tashlash uchun `exclude(group = "...", module = "...")` sintaksisidan foydalana olish;
- `resolutionStrategy` yordamida ma'lum bir kutubxona versiyasini barcha modullar uchun majburiy (force) qilib belgilashni bilish;
- BOM (Bill of Materials) tushunchasini va uning kutubxonalar mosligini kafolatlashdagi rolini tushunish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Android Studio (so'nggi barqaror versiya);
- Internet tarmog'i;
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Version Catalog (`libs.versions.toml`), `implementation` vs `api` bo'yicha savol-javob |
| **10–25 min** | Yangi mavzu: Tranzitiv bog'liqliklar mohiyati | Zanjirli kutubxonalar (Retrofit $\to$ OkHttp $\to$ Okio), yashirin modullar |
| **25–45 min** | Versiya ziddiyatlari va Dependency Tree | Ziddiyat sabablari, `./gradlew app:dependencies` daraxti, Gradle resolution mexanizmi |
| **45–60 min** | Konfliktlarni hal qilish: exclude va force | `exclude` qoidalari, `resolutionStrategy.force`, BOM (Bill of Materials) afzalligi |
| **60–75 min** | Amaliy mashg'ulot | Terminalda bog'liqliklar daraxtini tekshirish, ziddiyatli kutubxonani `exclude` qilib tozalash |
| **75–80 min** | Xulosa va darsni yakunlash | Asosiy xulosalar, tezkor nazorat savollari va uyga vazifa |

---

## Nazariy ma'lumotlar

### 1. Tranzitiv bog'liqliklar (Transitive Dependencies) nima?

Dasturchi `build.gradle` fayliga faqat bitta kutubxona qo'shadi, masalan:
```groovy
implementation 'com.squareup.retrofit2:retrofit:2.9.0'
```
Biroq loyiha yig'ilganda, ilovaga nafaqat Retrofit, balki uning ishlashi uchun zarur bo'lgan **OkHttp**, uning orqasidan esa **Okio** kutubxonalari ham avtomatik tarzda yuklab olinadi. 

> **Ta'rif:** Bitta kutubxona o'z faoliyati uchun boshqa kutubxonalarga tayansa va ular zanjirsimon tarzda loyihaga qo'shilsa, bu **Tranzitiv bog'liqlik (Transitive Dependency)** deb ataladi.

Bu juda qulay mexanizm — dasturchi har bir mayda yordamchi modulni alohida qidirib yurishi shart emas. Ammo loyiha kattalashgani sari turli kutubxonalar bitta yordamchi modulning har xil versiyalarini talab qila boshlaydi va bu **versiya ziddiyati (conflict)**ga olib keladi.

---

### 2. Versiya ziddiyati (Dependency Conflict) va Gradle yechimi

Tasavvur qiling, loyihangizda ikkita mashhur kutubxona ulangan:
1. `Kutubxona A` o'zi bilan `OkHttp 3.14.9` versiyasini talab qiladi;
2. `Kutubxona B` esa yangi `OkHttp 4.12.0` versiyasiga tayanadi.

Bitta loyiha ichida bitta klassning ikkita har xil versiyasi bir vaqtda yashay olmaydi. Gradle bu muammoni qanday hal qiladi?

- **Standart Gradle strategiyasi:** Gradle ziddiyatli holatda avtomatik ravishda **eng yuqori versiyani (Newest Version Wins)** tanlaydi (bizning misolda `4.12.0`).
- **Muammo:** Ba'zida eski kutubxona yangi versiya bilan mos kelmasligi mumkin (chunki yangi versiyada ba'zi metodlar o'chirilgan bo'lishi mumkin). Natijada ilova ishga tushganda `NoSuchMethodError` yoki `ClassNotFoundException` kabi kutilmagan runtime xatoliklar yuzaga keladi.

---

### 3. Bog'liqliklar daraxtini tekshirish (`./gradlew app:dependencies`)

Loyihangizda qaysi kutubxonalar o'rnatilganini va qaysi biri ziddiyat keltirib chiqarayotganini bilish uchun Android Studio terminalida quyidagi buyruq ishga tushiriladi:

```bash
./gradlew app:dependencies --configuration releaseRuntimeClasspath
```

Chiqish natijasida Gradle daraxtsimon strukturani ko'rsatadi:
```text
+--- com.squareup.retrofit2:retrofit:2.9.0
|    \--- com.squareup.okhttp3:okhttp:3.14.9 -> 4.12.0 (*)
\--- com.squareup.okhttp3:logging-interceptor:4.12.0
     \--- com.squareup.okhttp3:okhttp:4.12.0 (*)
```
E'tibor bering: `-> 4.12.0 (*)` belgisi Gradle eski `3.14.9` versiyasini yangi `4.12.0` versiyasiga avtomatik ko'targanini bildiradi.

---

### 4. Muammolarni hal qilish usullari

#### A. Keraksiz tranzitiv modulni chiqarib tashlash (`exclude`)
Agar biror kutubxona o'zi bilan ortiqcha yoki ziddiyatli modulni sudrab kelayotgan bo'lsa, uni `exclude` orqali to'sib qo'yish mumkin:

```groovy
implementation('com.squareup.retrofit2:retrofit:2.9.0') {
    exclude group: 'com.squareup.okhttp3', module: 'okhttp'
}
```
Bu holda Retrofit o'zining OkHttp versiyasini yuklamaydi va loyihada dasturchi ko'rsatgan asosiy OkHttp ishlatiladi.

#### B. Butun loyiha uchun versiyani majburlash (`resolutionStrategy.force`)
Agar ma'lum bir kutubxona versiyasini barcha modullar va tranzitiv bog'liqliklar uchun qat'iy majburiy qilib belgilash kerak bo'lsa:

```groovy
android {
    ...
    configurations.all {
        resolutionStrategy {
            force 'com.squareup.okhttp3:okhttp:4.12.0'
            failOnVersionConflict() // Agar xohlasak, ziddiyatda loyihani to'xtatish
        }
    }
}
```

#### C. BOM (Bill of Materials) dan foydalanish
Firebase va Jetpack Compose kabi yirik ekotizimlarda o'nlab modullarning versiyalarini alohida yozish xatoliklarga sabab bo'ladi. Google buning uchun **BOM** mexanizmini taklif qiladi:

```groovy
dependencies {
    // BOM faqat versiyalarni muvofiqlashtiradi
    implementation platform('com.google.firebase:firebase-bom:32.7.0')

    // Modullarda versiya raqami yozilmaydi!
    implementation 'com.google.firebase:firebase-auth'
    implementation 'com.google.firebase:firebase-firestore'
}
```
BOM barcha ichki kutubxonalarning 100% bir-biriga mos keluvchi versiyalarini avtomatik tanlab beradi.

---

## Amaliy topshiriqlar va mashqlar

### 1-topshiriq. Tranzitiv zanjirni aniqlash (oson)
Quyidagi bog'liqliklar zanjirini tahlil qiling:
- Ilova `coil-compose:2.6.0` kutubxonasini ulaydi;
- `coil-compose` o'z navbatida `coil-base` va `androidx.compose.foundation` modullarini talab qiladi;
- `coil-base` esa `okhttp` kutubxonasiga tayanadi.

1. Ushbu zanjirda tranzitiv kutubxonalar qaysilar?
2. Agar dasturchi faqat `coil-compose`ni o'chirsa, qolgan modullar loyihada qoladimi?

**Yechim:**
1. **Tranzitiv kutubxonalar:** `coil-base`, `androidx.compose.foundation` va `okhttp`. Dasturchi ularni bevosita qo'shmagan, ular `coil-compose` sababli avtomatik kirib kelgan.
2. **Qolmaydi:** Agar boshqa hech bir kutubxona ularni talab qilmayotgan bo'lsa, Gradle ularni build jarayonidan avtomatik olib tashlaydi.

---

### 2-topshiriq. `exclude` qoidasini to'g'ri yozish (o'rta)
Loyihangizga eski bir kutubxona ulangan:
```groovy
implementation 'com.example.analytics:tracker:1.5.0'
```
Ushbu kutubxona o'zi bilan juda eski `com.google.code.gson:gson:2.2.4` modulini yuklamoqda. Loyihangizda esa allaqachon yangi Gson `2.10.1` ishlatiladi.
Eski Gson moduli loyihaga kirib kelmasligi uchun `exclude` qoidasini to'g'ri yozing.

**Yechim:**
```groovy
implementation('com.example.analytics:tracker:1.5.0') {
    exclude group: 'com.google.code.gson', module: 'gson'
}
```
Shunda `tracker` kutubxonasi o'zining eski Gson versiyasidan voz kechadi va loyihadagi yangi `2.10.1` versiyasiga tayanadi.

---

### 3-topshiriq. Firebase BOM integratsiyasi (qiyin)
Android loyihasida Firebase xizmatlarining versiya ziddiyatlarini bartaraf etish uchun:
1. `firebase-bom` platformasini `32.8.0` versiyada ulang;
2. Autentifikatsiya (`firebase-auth-ktx`) va Ma'lumotlar bazasi (`firebase-firestore-ktx`) kutubxonalarini versiya ko'rsatmasdan qo'shing;
3. Nima uchun individual kutubxonalarda versiya yozilmaganini tushuntiring.

**Yechim:**
`app/build.gradle` faylining `dependencies` blokida:
```groovy
dependencies {
    // 1. Firebase BOM platformasi
    implementation platform('com.google.firebase:firebase-bom:32.8.0')

    // 2. Modullarni versiyasiz ulash
    implementation 'com.google.firebase:firebase-auth-ktx'
    implementation 'com.google.firebase:firebase-firestore-ktx'
}
```
3. **Tushuntirish:** BOM (Bill of Materials) barcha rasmiy Firebase kutubxonalarining bir-biri bilan 100% sinovdan o'tgan mos versiyalar xaritasini o'z ichiga oladi. Dasturchi faqat bitta BOM versiyasini boshqaradi, qolgan barcha modullar avtomatik ravishda mos versiyani qabul qiladi.

---

## Tezkor nazorat savollari

1. Tranzitiv bog'liqlik nima?
   - *Javob:* Siz ulagan kutubxona o'z faoliyati uchun talab qiladigan va loyihaga avtomatik ravishda qo'shiladigan qo'shimcha yordamchi kutubxonalardir.
2. Ikkita kutubxona bir xil modulning har xil versiyasini talab qilsa, Gradle odatda qaysi birini tanlaydi?
   - *Javob:* Standart strategiya bo'yicha eng yuqori (eng yangi) versiyani tanlaydi.
3. Bog'liqliklar daraxtini terminal orqali ko'rish buyrug'i qanday?
   - *Javob:* `./gradlew app:dependencies`.
4. `exclude` parametri nima maqsadda ishlatiladi?
   - *Javob:* Tranzitiv kutubxonalar ichidan keraksiz, eskirgan yoki ziddiyat keltirib chiqarayotgan modullarni chiqarib tashlash uchun.
5. Firebase BOM nima uchun kerak?
   - *Javob:* O'nlab Firebase modullari orasida versiyalar chalkashligi va ziddiyatlarini oldini olish uchun yagona mos versiyalar to'plamini taqdim etadi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Bir kutubxonaning ikki xil versiyasini qo'lda kiritish:** Masalan, ham `okhttp:3.12.0` ham `okhttp:4.12.0` yozish. Bu tushunmovchilikka olib keladi.
- **`exclude` qilgandan keyin ilova ishlashini tekshirmaslik:** Agar chiqarib tashlangan modul kutubxonaga hayotiy zarur bo'lsa, `NoClassDefFoundError` xatosi chiqishi mumkin. O'rniga loyihada mos versiya mavjudligiga ishonch hosil qiling.
