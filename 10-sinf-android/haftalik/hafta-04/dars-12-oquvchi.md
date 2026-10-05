# 12-dars. Continuous Integration (CI/CD) tushunchasi

> Kodni push qildingiz, robot uni o'zi tekshirdi, build qildi va xato bo'lsa xabar berdi. Bu CI/CD: dasturchining avtomatik yordamchisi.

## Dars xulosasi

- CI (Continuous Integration): kod tez-tez qo'shiladi va har safar avtomatik tekshiriladi.
- Tekshiruv: build, testlar, lint va scan tahlili.
- Continuous Delivery: ilovani tayyorlash va nashrga tayyor ushlash.
- Continuous Deployment: ilovani foydalanuvchilarga avtomatik yetkazish.
- Pipeline: avtomatik bajariladigan jarayonlar ketma-ketligi.
- GitHub Actions workflow'i YAML faylda yoziladi (`on`, `jobs`, `steps`).
- Test turlari: unit, integration, UI, performance.
- Maxfiy ma'lumotlar Secrets bo'limida saqlanadi.

## Qo'shimcha ma'lumot

### CI nima uchun kerak?

Maktab loyihasida 3 kishi ishlaydi: biri API, biri UI, biri baza. Agar haftada bir marta qo'shishsa, kodlar bir-biriga mos kelmay qoladi. CI har commitda tekshirib, mos kelmaslikni darhol ko'rsatadi.

### Zavod misoli

Telefon zavodida displey, korpus, protsessor alohida bo'limlarda yasaladi. Hamma detal tekshiruvdan o'tmasa, tayyor telefon buzuq chiqadi. Tekshiruv: CI. Bozorga chiqarish: Delivery va Deployment.

### Workflow'ni o'qish

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
      - name: Build with Gradle
        run: ./gradlew build
```

`on`: qachon ishlaydi. `jobs`: nima ishlanadi. `steps`: ketma-ket qadamlar. `run`: terminal buyrug'i. (Bu hujjatdagi namunaning qisqartirilgani.)

### MR/PR rad etilishi

CI testlar yiqilsa, Merge Request/PR tasdiqlanmaydi. "Kodim ishlayapti" degan xayol bo'lishi mumkin, CI esa real tekshiruv qiladi.

### Odatiy xatolar

- Token yoki API kalitni kodga yozish.
- Kodni juda kam birlashtirish.
- Qizil pipeline'ni e'tiborsiz qoldirish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| CI | Continuous Integration: kodni doimiy qo'shish va avtomatik tekshirish |
| CD | Continuous Delivery/Deployment: tayyorlash va yetkazishni avtomatlashtirish |
| Pipeline | Jarayonlarning avtomatik ketma-ketligi |
| Build | Ilovani yig'ish jarayoni |
| Workflow | GitHub Actions'dagi avtomatik jarayon tavsifi |
| YAML | Konfiguratsiya fayl formati |
| Job | Workflow ichidagi ishlar guruhi |
| Step | Job ichidagi bitta qadam |
| Secrets | Maxfiy ma'lumotlarni shifrlab saqlash bo'limi |
| Deployment | Ilovani foydalanuvchilarga yetkazish |

## Bilasizmi?

- Mobil o'yinlar deyarli har hafta yangilanadi: bu ortida CD ishlaydi.
- Android uchun mashhur CI/CD xizmatlari: GitHub Actions, GitLab CI/CD, Bitbucket Pipelines, Jenkins, CircleCI, Azure DevOps.
- Katta jamoalarda CI/CDsiz ishlash katta xato hisoblanadi: bitta noto'g'ri push butun jamoani to'xtatishi mumkin.
- GitHub Actions faylini GitHub'dagi "Actions" bo'limida tayyor shablondan ham tanlash mumkin.

## Topshiriqlar

### 1. CI so'zi · oson
CI qisqartmasini ochib yozing va bir jumlada izohlang.

**Kutiladigan natija:** Continuous Integration: kodni doimiy qo'shish va avtomatik tekshirish.

### 2. Bosqichlar · oson
Oddiy pipeline bosqichlarini ketma-ketlikda sanang.

**Kutiladigan natija:** checkout, build, test, deploy (yoki shunga yaqin).

### 3. Faylning formati · oson
GitHub Actions workflow fayli qaysi formatda yoziladi?

**Kutiladigan natija:** YAML.

### 4. Test turlari · oson
Pipeline'ga kirishi mumkin bo'lgan 4 xil testni yozing.

**Kutiladigan natija:** unit, integration, UI, performance.

### 5. Delivery yoki Deployment? · o'rta
Ilova foydalanuvchilarga avtomatik yetkazilishi qaysi atamaga mos?

**Kutiladigan natija:** Continuous Deployment.

### 6. Kodni o'qing · o'rta
`runs-on: ubuntu-latest` va `run: ./gradlew build` nimani bildiradi?

**Kutiladigan natija:** Ubuntu virtual mashinasida Gradle bilan ilovani yig'ish.

### 7. Qachon ishlaydi? · o'rta
`on: pull_request: branches: [ main ]` workflow'ni qachon ishga tushiradi?

**Kutiladigan natija:** main'ga PR ochilganda.

### 8. Analogiya · o'rta
CI/CD ni maktabdan bir hayotiy misol bilan tushuntiring.

**Kutiladigan natija:** o'z misolingiz (masalan, insho yoki zavod).

### 9. Workflow yozing · qiyin
Push va PR (main) da ishlaydigan, JDK 17 o'rnatib `./gradlew build` bajaradigan workflow yozing.

**Kutiladigan natija:** to'g'ri tuzilgan YAML: `name`, `on`, `jobs`, `steps`.

### 10. Xatoni toping · qiyin
Birov YAML fayliga `serviceAccountJson: abc123secret` deb yozib qo'ydi. Bu nimaga olib keladi va nimani almashtirish kerak?

**Kutiladigan natija:** maxfiy kalit ochiq qoladi; Secrets orqali chaqirish kerak.

### 11. Pipeline rejasi · qiyin
Loyihangiz uchun 5 bosqichli pipeline sxemasini daftarda chizing.

**Kutiladigan natija:** bosqichlar ketma-ketligi va xato bo'lsa nima bo'lishi.

### 12. Tadqiqot · bonus
GitHub, GitLab va Bitbucket CI/CD xizmatlari nomlarini yozing va qaysi birini tanlardingiz, sababini ayting.

**Kutiladigan natija:** 3 nom va 2-3 jumlalik asoslash.

## O'zingizni tekshiring

1. CI/CD nima va nega kerak?
2. CI qanday bosqichlardan iborat?
3. Delivery va Deployment orasida qanday farq bor?
4. Pipeline deganda nima tushuniladi?
5. GitHub Actions qanday foyda beradi?
6. Secrets bo'limi nima uchun kerak?

## Uyga vazifa

1. O'z Android loyihangiz uchun "Android CI" workflow'ini yozing.
2. CI va CD farqini va afzalliklarini qisqa yozing.
