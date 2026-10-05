# 12-dars. Continuous Integration (CI/CD) tushunchasi

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 4-hafta, 3-dars (umumiy 12-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (Continuous Integration (CI/CD) tushunchasi ma'ruzasi), `oquv-dasturi.txt`, `uslubiy-korsatma.txt` (GitHub Actions bo'limi)

---

## Darsning maqsadi

CI/CD tamoyilini, Continuous Integration jarayonini, Continuous Delivery va Deployment farqini, build va test avtomatlashtirishni, pipeline tushunchasini, GitHub Actions (YAML) misolini va Android loyihalarida CI/CD qo'llashni tushuntirish.

## Kutilayotgan natijalar

- CI va CD tushunchalarining mohiyatini ayta oladi;
- Pipeline bosqichlarini (build, test, deploy) sanaydi;
- GitHub Actions YAML faylining tuzilishini (`name`, `on`, `jobs`, `steps`) o'qiydi;
- Pipeline'da qaysi test turlari ishlashini biladi;
- Secrets nima uchun kerakligini tushunadi.

## Jihozlar

Kompyuter, internet, (ixtiyoriy) GitHub akkaunti.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 11-dars: branch, merge, konflikt, PR |
| 08–25 | CI | Qo'lda ishlash muammosi, CI mohiyati, analogiyalar |
| 25–38 | CD va pipeline | Delivery vs Deployment, xizmatlar, test turlari, MR rad etilishi |
| 38–43 | Tanaffus | |
| 43–58 | GitHub Actions | YAML tahlili, release workflow, Secrets |
| 58–75 | Amaliyot | Workflow yozish, tahlil |
| 75–80 | Xulosa | Nazorat, uyga vazifa, 5-hafta anonsi |

---

## Konspekt

### 1. Nega CI/CD?

Kod yozish, o'zgartirish, xato tuzatish, test, build va yetkazish: har bosqichda inson xatosi bo'lishi mumkin (muhim fayl unutiladi, test o'tkazilmaydi, noto'g'ri versiya chiqadi, moslashmagan kod push qilinadi). CI/CD jarayonni avtomatlashtiradi, xatolarni kamaytiradi va ilova sifatini doim saqlaydi.

### 2. Continuous Integration (CI)

Barcha dasturchilar kodni tez-tez, doimiy ravishda asosiy loyihaga qo'shib boradi. Kod qo'shilgan zahoti avtomatik tizim uni tekshiradi: build qiladi, testlardan o'tkazadi, lint va scan vositalari bilan tahlil qiladi. Xato topilsa, dasturchiga darhol xabar beradi.

Misol: uch dasturchi (API, UI, ma'lumotlar bazasi). Haftada bir qo'shsa, ulkan konfliktlar. CI esa har kuni, hatto har commitda tekshiradi, konfliktlar kichik bosqichda topiladi.

Analogiya: uch o'quvchi bitta insho yozadi. Oy oxirida birlashtirsa, chalkash chiqadi, har kuni birlashtirsa, xatolar tez ko'rinadi.

### 3. Continuous Delivery va Deployment

- **Continuous Delivery**: CI davomi; ilovani tayyorlash, sinovga chiqarish va nashr jarayonlarini avtomatlashtiradi, ilova doim tayyor turadi.
- **Continuous Deployment**: jarayonni yanada rivojlantirib, ilovani avtomatik foydalanuvchilarga yetkazadi.

Analogiya (hujjatdan): telefon zavodida har detal testdan o'tadi (CI), tayyor telefonni bozorga chiqarish (Delivery va Deployment).

### 4. Pipeline va xizmatlar

Pipeline: jarayonlarning ketma-ketligi, avtomatik bajariladi. Xizmatlar: GitHub Actions, GitLab CI/CD, Bitbucket Pipelines, Jenkins, CircleCI, Azure DevOps. GitHub Actions har Push yoki PR'da: loyiha fayllarini yuklaydi, Android SDK'ni o'rnatadi, Gradle bilan build qiladi, unit testlarni ishga tushiradi, natijani qaytaradi.

GitLab CI har Merge Request'da standart testlarni avtomatik o'tkazadi; muvaffaqiyatsiz bo'lsa MR rad etiladi.

Test turlari: unit (ViewModel, Repository), integration, UI (Compose, Activity/Fragment), performance (resurs).

### 5. GitHub Actions (hujjatdan)

Fayl `.github/workflows` papkasida (uslubiy ko'rsatma). Namuna:

```yaml
name: Android CI
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up JDK
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'
      - name: Build with Gradle
        run: ./gradlew build
```

Izoh: `on` push va PR hodisalari; `runs-on` virtual mashina; `steps` ketma-ket qadamlar; `./gradlew build` ilovani yig'adi. Bu har PR ochilganda Android loyihasini avtomatik build qiladi.

**Release (CD) misoli** (hujjatdan, qisqartirilgan):

```yaml
name: Release Build
on:
  push:
    tags:
      - 'v*'
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Build Release
        run: ./gradlew bundleRelease
      - name: Upload to Play Store
        uses: r0adkll/upload-google-play@v1
        with:
          serviceAccountJson: ${{ secrets.PLAY_STORE_KEY }}
```

Har safar `v*` tag qo'yilganda AAB fayl yig'iladi va Play Store test kanaliga yuklanadi.

**Secrets**: API kalitlari, tokenlar, maxfiy fayllar kodda turmaydi, GitHub Actions/GitLab CI'dagi "Secrets" bo'limida shifrlangan saqlanadi.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Atamalar

CI, CD va Deployment atamalarini bir jumlada izohlang.

**Yechim:** CI: kodni doimiy qo'shish va avtomatik tekshirish. CD (Delivery): ilovani tayyorlash va nashrga yetkazishni avtomatlashtirish. Deployment: ilovani foydalanuvchilarga avtomatik yetkazish.

### 2-topshiriq (o'rta). Workflow yozish

`.github/workflows/android.yml` faylida PR va push (main) da ishlaydigan, JDK 17 o'rnatib `./gradlew build` bajaradigan workflow yozing.

**Yechim:** Yuqoridagi "Android CI" namunasi.

### 3-topshiriq (o'rta). Qatorlarni tushuntirish

`runs-on: ubuntu-latest` va `uses: actions/checkout@v3` nimani bildiradi?

**Yechim:** Birinchisi: job ishlaydigan virtual mashina turi (Ubuntu). Ikkinchisi: repozitoriya fayllarini yuklaydigan tayyor qadam (action).

### 4-topshiriq (qiyin). Test qadamini qo'shish

Workflow'ga unit testlar uchun qadam qo'shing.

**Yechim:**
```yaml
      - name: Run unit tests
        run: ./gradlew test
```
Test yiqilsa qadam xato bilan tugaydi, pipeline qizil bo'ladi va PR tasdiqlanmaydi. (`./gradlew test` hujjatdagi `./gradlew build` bilan bir xil Gradle chaqiruvi uslubida; alohida test qadami illyustrativ misol.)

### 5-topshiriq (qiyin). Secrets

Nega Play Store kalitini YAML ichiga yozmaymiz? Qanday yo'l bor?

**Yechim:** Repozitoriya ochiq bo'lsa, kalit hammaga ko'rinadi. "Secrets" bo'limida shifrlangan saqlanadi va YAML'da `${{ secrets.PLAY_STORE_KEY }}` ko'rinishida chaqiriladi.

---

## Tezkor nazorat

1. CI nima? **Javob:** Kodni doimiy asosiy loyihaga qo'shish va har qo'shilganda avtomatik build/test qilish tamoyili.
2. Delivery va Deployment farqi? **Javob:** Delivery: tayyorlash va nashrga tayyor holda ushlash; Deployment: foydalanuvchilarga avtomatik yetkazish.
3. Pipeline nima? **Javob:** Avtomatik bajariladigan jarayonlar ketma-ketligi.
4. GitHub Actions fayli qaysi formatda? **Javob:** YAML.
5. Secrets nima uchun kerak? **Javob:** Maxfiy ma'lumotlarni shifrlangan saqlash uchun.

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
