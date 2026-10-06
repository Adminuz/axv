# 16-dars. Gradle so'rovlarini (tasks) bajarish va xatoliklarni aniqlash

> Loyiha yig'ilmay qolsa, kod haqida emas, Gradle haqida gap ketadi. Bugun Gradle qanday ishlashini va xatoni qanday topishni o'rganamiz.

## Dars xulosasi

- Gradle 3 bosqichdan o'tadi: Initialization, Configuration, Execution.
- Task — Gradle ning eng kichik ish birligi.
- `./gradlew clean`, `assembleDebug`, `bundleRelease`, `tasks` asosiy buyruqlar.
- APK o'rnatiladi; AAB Google Play uchun.
- Xatoda Build oynasidagi birinchi qizil qatorni o'qing.
- `--stacktrace` va `--info` batafsil ma'lumot beradi; `build.gradle` o'zgargach Sync Now.

## Qo'shimcha ma'lumot

### Gradle Wrapper
`gradle-wrapper.properties` va `gradlew` loyiha bilan birga saqlanadi. Boshqa dasturchining kompyuterida Gradle o'rnatilganmi-yo'qmi, farqi yo'q.

### Manifest Merging
Gradle bir nechta modullardagi `AndroidManifest.xml` fayllarini bitta asosiy faylga birlashtiradi.

### Dependency conflict
Ikki kutubxona bir kutubxonaning turli versiyasini talab qilsa, ziddiyat bo'ladi. Gradle odatda eng yangi versiyani tanlaydi.

### Xatolar tartibi
Avval birinchi qizil qator, keyin `--stacktrace`: odatda birinchi xabarda asosiy sabab bo'ladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Task | Gradle ish birligi |
| Gradle Wrapper | Bir xil Gradle versiyasi uchun skript |
| APK | Android ilova fayli |
| AAB | Android App Bundle |
| Sync | build.gradle o'zgarishini qo'llash |
| Stacktrace | Xatoning to'liq izi |
| Compiling | Kodni baytkodga o'tkazish |
| Manifest Merging | Manifestlarni birlashtirish |

## Bilasizmi?

- Gradle Wrapper bo'lgani uchun loyihani ochgan har bir dasturchi bir xil Gradle versiyasidan foydalanadi.
- Qo'llanmaga ko'ra AAB format ilova hajmini 35% gacha kamaytirishi mumkin.
- Ko'p jamoalar CI da aynan shu `./gradlew` buyruqlarini ishlatadi.

## Topshiriqlar

### 1. 3 bosqich · oson

Gradle ning 3 bosqichini ketma-ket yozing.

**Kutiladigan natija:** Initialization, Configuration, Execution.

### 2. Buyruqlar · oson

`clean`, `assembleDebug`, `bundleRelease` vazifasini 1 jumlada yozing.

**Kutiladigan natija:** 3 ta to'g'ri jumla.

### 3. APK va AAB · oson

APK va AAB farqini yozing.

**Kutiladigan natija:** O'rnatish va Play.

### 4. Task nima? · oson

Task nima? Misol keltiring.

**Kutiladigan natija:** Gradle ning eng kichik ish birligi.

### 5. Bosqichni taxmin qiling · o'rta

`settings.gradle` da yo'q modul `include` qilingan. Qaysi bosqichda xato chiqadi?

**Kutiladigan natija:** Initialization.

### 6. Xato turi · o'rta

«Could not find ...coil...» xatosi qaysi turga kiradi?

**Kutiladigan natija:** Dependency/Sync xatosi.

### 7. Tozalash · o'rta

Qachon `clean` ishlatiladi? 2 holat yozing.

**Kutiladigan natija:** Ishlamay qolganda; eski fayllar bilan yig'ishda.

### 8. Bayroqlar · o'rta

`--stacktrace` va `--info` farqi?

**Kutiladigan natija:** Iz va batafsil log.

### 9. Debug APK · qiyin

Terminaldan Debug APK yasang va APK qayerda saqlanganini toping.

**Kutiladigan natija:** `app/build/outputs/apk/debug`.

### 10. Ataylab xato · qiyin

Imlo xatosi qiling, xatoni o'qing va tuzating.

**Kutiladigan natija:** Sababi yozilgan.

### 11. Wrapper · qiyin

`gradlew` va `gradle` farqini yozing.

**Kutiladigan natija:** Wrapper bir xil versiyani kafolatlaydi.

### 12. Dependency daraxti · bonus

`./gradlew app:dependencies` natijasidan transitive bog'liqlikni toping.

**Kutiladigan natija:** Bitta transitive kutubxona.

## O'zingizni tekshiring

1. Gradle ning 3 bosqichi?
2. `clean` nima qiladi?
3. APK va AAB farqi?
4. Build xatosini qanday o'qiysiz?
5. `--stacktrace` nima?
6. Gradle Wrapper nima?

## Uyga vazifa

Gradle buyruqlarini ishga tushiring va bitta xatoni toping (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
