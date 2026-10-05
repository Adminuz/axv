# 10-dars. GitLab va Bitbucket'da jamoaviy ish jarayonlari

**Fan:** Advanced Android dasturlash
**Sinf:** 10-sinf
**Hafta:** 4-hafta, 1-dars (umumiy 10-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `oquv-qollanma.txt` (GitLab va Bitbucket'da jamoaviy ish jarayonlari ma'ruzasi), `oquv-dasturi.txt` (kutilayotgan natijalar)

---

## Darsning maqsadi

GitLab va Bitbucket platformalarining vazifasini va GitHub'dan farqini tushuntirish; loyihani klonlash, guruh (Group) va jamoa (Team) bilan ishlash, access va roles boshqaruvi, Issue tracker va Kanban doskasi, Merge Request va Code Review jarayonlari hamda pipeline tushunchasini berish.

## Kutilayotgan natijalar

- GitLab va Bitbucket nima uchun kerakligini va GitHub bilan umumiy/farqli tomonlarini ayta oladi;
- `git clone` bilan loyihani olib, alohida branchda ishlay oladi;
- Group, Team, Role (access) tushunchalarini izohlaydi;
- Issue tracker va Kanban (To Do, In Progress, Done) ishlash tamoyilini biladi;
- Merge Request (GitLab'da) = Pull Request (GitHub'da) ekanini biladi;
- Code Review foydasini va pipeline nima ekanini tushuntiradi.

## Jihozlar

Kompyuter, internet, Git, Android Studio, (ixtiyoriy) GitLab yoki Bitbucket akkaunti. Akkaunt bo'lmasa, topshiriqlar daftarda sxema ko'rinishida bajariladi.

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| 00–08 | Takrorlash | 9-dars: Git vs GitHub, remote, push/pull, Issues. Savol-javob |
| 08–25 | Yangi mavzu 1 | Platformalar (GitHub, GitLab, Bitbucket), klonlash, Group va Team, access va roles |
| 25–40 | Yangi mavzu 2 | Issue tracker, Kanban, Merge Request, Code Review (slaydlar bilan) |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | CI/CD pipeline'ni sozlash (umumiy tushuncha va o'quv namunasi) |
| 55–75 | Amaliyot | Sxema chizish, branch nomlash, MR sharhi yozish |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa, keyingi dars anonsi |

---

## Konspekt

### 1. Platformalar

Git sizning kompyuteringizdagi dastur. Uni internetga chiqaradigan "uy"lar esa bir nechta: **GitHub**, **GitLab**, **Bitbucket**. Hujjat ularni "onlayn platformalar, jamoaviy dastur ishlab chiqishni tashkil etadi" deydi. Remote repository ular birortasida turishi mumkin; Android dasturchilari odatda GitHub'dan foydalanadi (bepul va qulay).

Umumiy funksiyalar (hujjatning reja bandlari): repository boshqaruvi, guruh va jamoalar bilan ishlash, Issue tracker va Kanban doskalari, CI/CD pipeline sozlash, Code Review.

Farq: GitHub eng yirik "ijtimoiy tarmoq" (profil, Star, Fork). GitLab'da PR o'rniga **Merge Request (MR)** deyiladi va GitLab DevOps imkoniyatlari bilan ajralib turadi (pipeline). Bitbucket jamoalar uchun repository va pipeline beradi.

> Aniqlik: hujjatda GitLab va Bitbucket bo'yicha tafsilot (menyular, tarif, rollar nomlari) kam. Biz faqat reja bandlari va umumiy tamoyillarni o'rgatamiz. Rollar nomlari (Guest, Reporter, Developer, Maintainer, Owner) hujjatda yo'q, shuning uchun darsda "qo'shimcha ma'lumot" sifatida aytiladi.

### 2. Loyihani klonlash

```bash
git clone https://gitlab.com/guruh/maktab-jadvali.git
cd maktab-jadvali
git checkout -b feature/lessons-screen
git remote -v
```

`git clone` serverdagi loyihaning to'liq nusxasini (tarixi bilan) kompyuterga tushiradi. Platforma farqi yo'q: havola o'zgaradi, buyruq bir xil. Keyin jamoada asosiy kodga tegmay, alohida branch ochiladi.

### 3. Group, Team, access va roles

- **Group**: bir nechta loyiha va odamni bir joyda boshqarish.
- **Team**: loyiha ustida ishlaydigan a'zolar.
- **Access / Role**: har bir a'zoga alohida huquq (kim ko'radi, kim o'zgartiradi, kim merge qiladi). Tamoyil: kerakli minimum huquq beriladi, asosiy branchga to'g'ridan-to'g'ri yozish cheklanadi, o'zgarish MR orqali kiradi.

### 4. Issue tracker va Kanban

Issue: xato, vazifa yoki taklif. Teglar (bug, enhancement, help-wanted), mas'ul shaxs va muddat qo'yiladi. Kanban doskasi: vazifalar **To Do**, **In Progress**, **Done** ustunlari bo'ylab ko'chadi. Vazifalar bo'linishi uchrashuvsiz, onlayn amalga oshadi.

### 5. Merge Request va Code Review

MR (GitLab) = PR (GitHub): bir branchdagi o'zgarishni boshqasiga qo'shish uchun rasmiy so'rov. Jarayon: branch push qilinadi, MR ochiladi, jamoa a'zolari satrma-satr sharh qoldiradi, muallif tuzatadi, tasdiqlangach (approve) merge qilinadi. Review nimani tekshiradi: kod toza yozilganmi, takrorlanish yo'qmi, xavfsizlik xatolari, arxitektura qoidalari, UI kutilgan natijani beradimi.

### 6. Pipeline

Pipeline: jarayonlarning ketma-ketligi (masalan Commit → Build → Test → Review → Deploy), hammasi avtomatik. GitLab CI har bir MR'da standart testlarni avtomatik ishga tushiradi; test yiqilsa MR rad etiladi (hujjat bo'yicha). Keyingi darslarda batafsil.

O'quv namunasi (hujjatda GitLab CI fayli ko'rsatilmagan, bu illyustrativ misol, `.gitlab-ci.yml`):

```yaml
stages:
  - build
  - test
build_job:
  stage: build
  script:
    - ./gradlew assembleDebug
test_job:
  stage: test
  script:
    - ./gradlew test
```

### Branch nomlash (hujjatdan)

`feature/login`, `bugfix/profile-crash`, `hotfix/payment-error`, `refactor/home-screen`.

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Jamoa sxemasi

Daftarda `Group` ichida 2 ta loyiha va 4 ta a'zo sxemasini chizing, har a'zoga rol yozing.

**Yechim:** Group: "maktab-it-jamoasi". Loyihalar: maktab-jadvali, oshxona-menyu. A'zolar: mentor (to'liq huquq, merge qiladi), 3 o'quvchi (o'z branchiga yozadi, MR ochadi, asosiy branchga to'g'ridan-to'g'ri yozmaydi). Asosiy fikr: huquq vazifaga mos.

### 2-topshiriq (oson). Branch nomlari

feature, bugfix, hotfix, refactor uchun bittadan nom yozing.

**Yechim:** `feature/lessons-screen`, `bugfix/profile-crash`, `hotfix/payment-error`, `refactor/home-screen`.

### 3-topshiriq (o'rta). Klonlash va branch

Quyidagi buyruqlarni ketma-ket yozing: loyihani klonlash, papkaga kirish, yangi branch ochish, remote'ni tekshirish.

**Yechim:**
```bash
git clone https://gitlab.com/guruh/maktab-jadvali.git
cd maktab-jadvali
git checkout -b feature/lessons-screen
git remote -v
```

### 4-topshiriq (o'rta). Kanban doskasi

5 ta vazifani To Do / In Progress / Done ustunlariga joylang va bir vazifaning yo'lini tushuntiring.

**Yechim:** Masalan: "Login ekrani" (To Do) → boshlanganda In Progress → MR merge qilingach Done. Har bir ustunda vazifa soni ko'rinib turadi.

### 5-topshiriq (qiyin). Konstruktiv MR sharhi

Hujjatdagi misolga o'xshash 3 ta konstruktiv sharh yozing ("UI zo'r, lekin rang sxemasini Material3 ga moslang" kabi).

**Yechim:** Namuna: 1) "Funksiya nomi aniq, yaxshi. `loadUser` va `loadUserData` takrorlanyapti, bittasini qoldiring." 2) "Rang sxemasini Material3 ga moslang." 3) "Commit xabari ma'noli, rahmat; PR hajmi ozgina katta, ikkiga bo'lish mumkinmi?" Mezon: aniq, hurmatli, taklif beruvchi.

### 6-topshiriq (qiyin). Pipeline rejasi

Android loyihangiz uchun pipeline bosqichlarini ketma-ket yozing va test yiqilsa nima bo'lishini ayting.

**Yechim:** Commit → Build (`./gradlew assembleDebug`) → Test (`./gradlew test`) → Review → Deploy. Test yiqilsa MR rad etiladi, muallif tuzatadi.

---

## Tezkor nazorat

1. GitLab'da Pull Request qanday ataladi? **Javob:** Merge Request.
2. Kanban doskasining 3 ustuni? **Javob:** To Do, In Progress, Done.
3. `git clone` nima qiladi? **Javob:** Serverdagi loyihaning to'liq nusxasini kompyuterga tushiradi.
4. Nega a'zolarga minimal huquq beriladi? **Javob:** Tasodifiy xato asosiy kodni buzmasligi uchun.
5. Pipeline nima? **Javob:** Avtomatik bajariladigan jarayonlar ketma-ketligi (build, test, deploy).

## Uyga vazifa

`uyga-vazifa.md` ga qarang.
