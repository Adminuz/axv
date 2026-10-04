---
title: "15-dars. 9-dars: GitHub’da loyihalar yaratish va boshqarish"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (Android)", "link": "/10-sinf-android/"}, "week": {"n": 3, "link": "/10-sinf-android/hafta-03/"}, "g": 15, "title": "9-dars: GitHub’da loyihalar yaratish va boshqarish", "lead": "Gradle yordamida kutubxonalarni ulash va versiyalarni boshqarish ko‘nikmasiga ega bo‘ladi;", "slide": "/slaydlar/10-sinf-android/hafta-03/dars-9.html", "tabs": [{"g": 13, "link": "/10-sinf-android/hafta-03/dars-7", "current": false}, {"g": 14, "link": "/10-sinf-android/hafta-03/dars-8", "current": false}, {"g": 15, "link": "/10-sinf-android/hafta-03/dars-9", "current": true}], "prev": {"g": 14, "title": "8-dars: Git bilan ishlash amaliyoti (Tarmoqlar va Konfliktlar)", "link": "/10-sinf-android/hafta-03/dars-8"}, "next": null}
---

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Mavzu:** GitHub’da loyihalar yaratish va boshqarish (Remote repozitoriy, push, pull, issues, README)

---

<div class="blk">

## <Icon name="file-text" /> Nazariy konspekt

### 1. Git va GitHub farqi
- **Git** — bu sizning kompyuteringizda ishlaydigan lokal versiya nazorati dasturi.
- **GitHub** — bu internetdagi global platforma. U sizning Git omborlaringizni bulutda saqlaydi, jamoa bilan birgalikda kod yozish va butun dunyoga o'z portfoliosini ko'rsatish imkonini beradi.

---

### 2. Masofaviy ombor (Remote Repository) buyruqlari

| Buyruq | Vazifasi |
|---|---|
| `git remote add origin <url>` | Masofaviy GitHub repozitoriyasini `origin` nomi bilan lokal loyihaga ulaydi |
| `git remote -v` | Ulangan barcha server manzillarini ko'rsatadi |
| `git branch -M main` | Asosiy tarmoq nomini `main` ga o'zgartiradi |
| `git push -u origin main` | Birinchi marta barcha commitlarni GitHub'ga yuklaydi |
| `git push` | Keyingi yangi commitlarni serverga jo'natadi |
| `git pull origin main` | GitHub'dagi yangiliklarni kompyuterga yuklab oladi |
| `git clone <url>` | Serverdagi tayyor loyihani kompyuterga ko'chirib oladi |

---

### 3. Public vs Private
- **Public:** Barcha foydalanuvchilar kodni ko'ra oladi va yuklab oladi. Portfolio va o'quv ishlari uchun tavsiya etiladi.
- **Private:** Faqat siz va siz taklif qilgan jamoa a'zolari ko'radi. Tijoriy maxfiy loyihalar uchun mo'ljallangan.

---

### 4. `README.md` faylining kuchi
`README.md` fayli repozitoriyning bosh sahifasida avtomatik ko'rinadi. U Markdown tilida yoziladi va unda:
- Ilova nomi va nima vazifa bajarishi;
- Ekran rasmlari (skrinshotlar);
- Foydalanilgan kutubxonalar (Kotlin, Compose, Retrofit, Room);
- Loyihani qanday ishga tushirish yo'riqnomasi bo'lishi shart.

---

### 5. Issues (Muammolar va Vazifalar)
GitHub Issues orqali jamoa a'zolari:
- Topilgan xatoliklar (Bugs) haqida hisobot qoldirishadi;
- Kelgusi yangi rejalarni (Tasks) ro'yxatga oladilar;
- Commit xabarida `fixes #1` deb yozilsa, GitHub o'sha xatoni avtomatik tarzda yopadi (Close).

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1-topshiriq: GitHub akkauntiga kirish va profilni tekshirish <Badge type="tip" text="oson" />
github.com saytiga kiring, profilingizni oching va uning rasmiy havolasini (masalan, `https://github.com/sizning_nomingiz`) aniqlang.

### 2-topshiriq: Yangi repozitoriy ochish <Badge type="tip" text="oson" />
GitHub'da "New" tugmasini bosing, `android-basics-portfolio` nomli yangi Public repozitoriy yarating. Boshlang'ich README qo'shmang (bo'sh qoldiring).

### 3-topshiriq: Lokal loyihani remote ga ulash <Badge type="tip" text="oson" />
Terminalda o'z loyihangiz papkasiga kiring va `git remote add origin <url>` buyrug'i orqali loyihani GitHub bilan bog'lang.

### 4-topshiriq: Ulangan manzilni tekshirish <Badge type="tip" text="oson" />
`git remote -v` buyrug'ini ishga tushirib, `fetch` va `push` manzillari to'g'ri o'rnatilganini tasdiqlang.

### 5-topshiriq: Birinchi marta kodni yuklash (Push) <Badge type="warning" text="o'rta" />
`git branch -M main` va `git push -u origin main` buyruqlari yordamida barcha lokal commitlaringizni GitHub serveriga yuboring.

### 6-topshiriq: README.md faylini yozish va yuklash <Badge type="warning" text="o'rta" />
Loyiha papkasida `README.md` faylini yarating. Loyiha nomini `#` bilan, texnologiyalarni esa ro'yxat shaklida yozib, commit va push qiling.

### 7-topshiriq: GitHub veb-interfeysida o'zgarish kiritish va pull qilish <Badge type="warning" text="o'rta" />
GitHub saytining o'zida `README.md` faylini tahrirlab yangi satr qo'shing. So'ngra terminalda `git pull origin main` buyrug'ini bering va fayl kompyuteringizda yangilanganini ko'ring.

### 8-topshiriq: Yangi Issue ochish <Badge type="danger" text="qiyin" />
GitHub repozitoriyangizning "Issues" bo'limiga o'ting va loyihaga kiritilishi kerak bo'lgan vazifa bo'yicha yangi masala oching.

### 9-topshiriq: Commit orqali Issue'ni avtomatik yopish <Badge type="danger" text="qiyin" />
Kompyuteringizda tegishli o'zgarishni qiling va commit xabariga `fixes #1` (yoki o'z issue raqamingizni) yozib push qiling. Issue avtomatik yopilganini kuzating.

### 10-topshiriq: Android Studio VCS orqali repozitoriy ulash <Badge type="info" text="bonus" />
Android Studio menyusidan **Settings > Version Control > GitHub** bo'limiga kiring va o'z hisobingizni IDE bilan to'liq integratsiya qiling.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'zini tekshirish uchun savollar

1. Git va GitHub orasidagi farqni bitta jumla bilan qanday tushuntirish mumkin?
2. `git remote add origin` buyrug'idagi `origin` nima?
3. Nima uchun portfoliosi kuchli bo'lishini xohlagan dasturchi o'quv loyihalarini Public qilishi kerak?
4. `README.md` faylida `#` va `-` belgilari nimani anglatadi?
5. `git push` va `git pull` buyruqlarining ishlash yo'nalishini tushuntiring.

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. GitHub'da o'zingizning Android loyihangiz uchun yangi Public repozitoriy yarating.
2. Unda to'liq `README.md` faylini shakllantiring (loyiha tavsifi, texnologiyalar, skrinshotlar).
3. Kamida 2 ta Issue yarating va ulardan birini maxsus commit xabari orqali avtomatik yoping.

</div>

