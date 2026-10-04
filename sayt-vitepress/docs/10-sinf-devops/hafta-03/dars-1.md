---
title: "7-dars. Git branchlar va masofaviy repozitoriylar (GitHub, Push, Pull, Merge)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "week": {"n": 3, "link": "/10-sinf-devops/hafta-03/"}, "g": 7, "title": "Git branchlar va masofaviy repozitoriylar (GitHub, Push, Pull, Merge)", "lead": "Jamoaviy dasturlash san'ati: parallel rivojlanish tarmoqlari (branches), birlashtirish (merge), ziddiyatlarni yechish hamda GitHub orqali masofaviy hamkorlik.", "slide": "/slaydlar/10-sinf-devops/hafta-03/dars-1.html", "tabs": [{"g": 7, "link": "/10-sinf-devops/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/10-sinf-devops/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/10-sinf-devops/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "Kompyuter tarmoqlari asoslari: OSI 7 qatlamli modeli va TCP/IP steki", "link": "/10-sinf-devops/hafta-03/dars-2"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Git branch (tarmoq) — bu loyihaning asosiy kodiga xalaqit bermasdan parallel ravishda yangi funksiyalar yoki sinovlarni ishlab chiqish imkonini beruvchi yengil ko'rsatkichdir.
- `git branch` barcha tarmoqlarni ko'rsatadi, `git switch -c [nom]` yangi branch ochib unga darhol o'tadi.
- Yangi funksiya tayyor bo'lgach, u `git merge` orqali asosiy `main` branchga xavfsiz birlashtiriladi.
- Agar ikkita branchda bir xil faylning bir xil qatorlari o'zgartirilgan bo'lsa, **Merge Conflict** yuzaga keladi va uni dasturchi qo'lda hal qilishi talab etiladi.
- GitHub va GitLab — bu Git repozitoriyalarini bulutda saqlash va butun dunyo dasturchilari bilan jamoada ishlash imkonini beruvchi xizmatlardir.
- `git remote add origin [url]` lokal repozitoriyani bulutdagi GitHub manziliga bog'laydi.
- `git push` mahalliy kommitlarni masofaviy serverga yuklaydi, `git pull` esa serverdagi yangilanishlarni lokal kompyuterga ko'chirib oladi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega Git'da branchlar bunchalik tez ochiladi?
Eski versiya tizimlarida branch yaratish butun loyiha papkasini boshqa joyga to'liq nusxalashni talab qilgan (bu gigabaytlab joy va daqiqalar vaqt olgan).
Git'da esa har bir commit o'zining 40 belgili SHA-1 xeshiga ega. Branch — bu shunchaki `.git/refs/heads/` ichida saqlanadigan 41 baytlik kichik matn fayli bo'lib, uning ichida eng so'nggi commit xeshi yozilgan bo'ladi! Yangi branch ochganingizda Git shunchaki yangi faylchaga o'sha xeshni yozib qo'yadi. Shu sababli branch ochish bir millisekund vaqt oladi.

### 2. Git Flow va Feature Branch madaniyati
Professional DevOps va dasturlash jamoalarida quyidagi qoidaga qat'iy amal qilinadi:
- `main` (yoki `production`): Faqatgina 100% sinovdan o'tgan, foydalanuvchilar ishlatayotgan tayyor kod saqlanadi.
- `feature/...` branchlari: Har bir yangi vazifa uchun alohida ochiladi (masalan: `feature/user-auth`, `feature/dark-mode`).
- Kod yozib bo'lingach, u to'g'ridan-to'g'ri `main` ga merge qilinmaydi, balki **Pull Request (PR)** ochiladi. Boshqa jamoa a'zolari kodni tekshirib (Code Review), sinovlar (CI/CD) muvaffaqiyatli o'tgachgina birlashtirishga ruxsat berishadi.

### 3. Merge Conflict bilan to'g'ri ishlash san'ati
Mojaro yuzaga kelganda qo'rqish kerak emas:
1. Terminalda qaysi faylda konflikt chiqqani ko'rsatiladi.
2. Faylni ochganingizda Git sizga ikkala variantni chiroyli ko'rsatib turadi (`HEAD` sizniki, `branch_nomi` esa ikkinchi tomonniki).
3. Siz jamoangiz bilan kelishgan holda to'g'ri variantni qoldirasiz, keraksizini va maxsus belgilarni (`<<<<`, `====`, `>>>>`) o'chirib tashlaysiz.
4. Faylni saqlab, `git add [fayl]` va `git commit` qilsangiz, ziddiyat to'liq bartaraf etiladi!

### 4. SSH kalitlar orqali GitHub'ga xavfsiz ulanish
GitHub xavfsizlik sababli oddiy parollar bilan `git push` qilishni taqiqlagan. Buning o'rniga zamonaviy assimetrik kriptografiya — **SSH kalitlar** ishlatiladi:
1. `ssh-keygen -t ed25519 -C "email@example.com"` orqali shaxsiy va ochiq kalitlar juftligi hosil qilinadi.
2. Ochiq kalit (`cat ~/.ssh/id_ed25519.pub`) nusxalanib, GitHub sozlamalaridagi **SSH and GPG keys** bo'limiga kiritiladi.
3. Shundan so'ng parol kiritmasdan xavfsiz va bir zumda kodlarni push qilish mumkin bo'ladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Branch (Tarmoq)** | Asosiy kod bazasidan mustaqil ravishda parallel rivojlanuvchi o'zgarishlar yo'nalishi. |
| **Merge (Birlashtirish)** | Bir branchdagi kommitlar tarixini ikkinchi branch tarkibiga qo'shish operatsiyasi. |
| **Merge Conflict** | Ikki xil branchda bitta faylning ayni bir qatoriga bir-biriga zid o'zgarishlar kiritilganda yuzaga keladigan holat. |
| **Remote (Masofaviy ombor)** | Mahalliy kompyuterdan tashqarida, internetdagi serverda (masalan, GitHub) joylashgan repozitoriya. |
| **Origin** | Loyiha bog'langan asosiy masofaviy repozitoriyaga beriladigan standart nom. |
| **Push** | Lokal kompyuterdagi yangi kommitlarni masofaviy GitHub repozitoriyasiga yuklash buyrug'i. |
| **Pull** | Masofaviy serverdagi eng yangi o'zgarishlarni yuklab olib, joriy branchga birlashtirish amali. |
| **Clone** | Masofaviy repozitoriyaning to'liq nusxasini (barcha branchlari va tarixi bilan) lokal kompyuterga yuklab olish. |
| **Pull Request (PR)** | Dasturchi o'z branchidagi o'zgarishlarni asosiy loyihaga birlashtirishni so'rab jamoaga yuboradigan taklifi. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- 2020-yilgacha Git'da standart asosiy branch nomi `master` bo'lgan, ammo inklyuzivlik va madaniy me'yorlar sababli butun dunyo bo'yicha u `main` ga o'zgartirildi.
- Dunyodagi eng yirik ochiq kodli repozitoriyalardan biri bo'lgan Linux yadrosi repozitoriyasida 1 milliondan ortiq commitlar va minglab branchlar mavjud.
- GitHub'da joylashtirilgan ochiq kodlar Arktika muzliklari ostida (Arctic World Archive) joylashgan maxsus yerosti omborida ming yildan ortiq saqlanishi uchun plyonkalarga yozib ko'mib qo'yilgan.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Mavjud branchlarni ko'rish <Badge type="tip" text="oson" />
O'z loyihangizda `git branch` buyrug'ini bering va joriy faol branch nomini aniqlang.
**Kutiladigan natija:** Ekranda `* main` yozuvi chiqadi.

### 2. Yangi branch yaratish va o'tish <Badge type="tip" text="oson" />
`git switch -c feature-header` buyrug'i orqali yangi branch oching va avtomatik unga o'ting.
**Kutiladigan natija:** «Switched to a new branch 'feature-header'» xabari chiqadi.

### 3. Yangi branchda fayl commit qilish <Badge type="tip" text="oson" />
`feature-header` branchida `header.html` faylini yarating, uni `git add` va `git commit` orqali saqlang.
**Kutiladigan natija:** Commit faqat yangi branchda aks etadi.

### 4. Main branchga qaytish va farqni ko'rish <Badge type="tip" text="oson" />
`git switch main` orqali asosiy branchga qayting va `ls` buyrug'ini bering. Nega `header.html` ko'rinmayotganini tahlil qiling.
**Kutiladigan natija:** `main` branchda yangi fayl hali yo'q ekanligi tasdiqlanadi.

### 5. Fast-forward merge qilish <Badge type="warning" text="o'rta" />
`main` branchda turgan holda `git merge feature-header` buyrug'ini bajaring va uning natijasini tahlil qiling.
**Kutiladigan natija:** `header.html` fayli `main` ga tezkor qo'shiladi (Fast-forward).

### 6. Birlashtirilgan branchni xavfsiz o'chirish <Badge type="warning" text="o'rta" />
`git branch -d feature-header` buyrug'i orqali vazifasi yakunlangan branchni o'chirib tashlang.
**Kutiladigan natija:** «Deleted branch feature-header» xabari chiqadi.

### 7. Masofaviy repozitoriya manzilini tekshirish <Badge type="warning" text="o'rta" />
`git remote -v` buyrug'ini ishga tushiring va loyihaga qanday remote manzillar bog'langanini aniqlang.
**Kutiladigan natija:** Bog'langan bo'lsa `origin` URL manzillari chiqadi, bo'lmasa bo'sh qaytadi.

### 8. Git log orqali tarmoqlar daraxtini ko'rish <Badge type="warning" text="o'rta" />
`git log --oneline --graph --all` buyrug'ini bajaring va commitlar zanjirining chiroyli grafik ko'rinishini tahlil qiling.
**Kutiladigan natija:** Terminalda rangli tarmoqlangan daraxt belgilar bilan chiziladi.

### 9. Merge konfliktini yuzaga keltirish va to'g'rilash <Badge type="danger" text="qiyin" />
Bitta faylning ayni bir qatoriga ikkita alohida branchda turli o'zgartirishlar kiriting, ularni merge qilish orqali konflikt hosil qiling va faylni tahrirlab muammoni hal qiling.
**Kutiladigan natija:** Merge conflict yuzaga keladi, qo'lda to'g'rilanib yangi commit qilinadi.

### 10. Ommaviy repozitoriyani klonlash (git clone) <Badge type="danger" text="qiyin" />
GitHub'dagi ochiq manbali biror mashhur kichik loyihani (masalan, biror o'quv qo'llanmasini) `git clone [url]` buyrug'i bilan o'z kompyuteringizga yuklab oling va uning tarixini `git log` bilan ko'ring.
**Kutiladigan natija:** Masofaviy loyiha barcha fayllari va commitlar tarixi bilan birga yuklab olinadi.

### 11. SSH kalit yaratish (Tadqiqot) <Badge type="info" text="bonus" />
`ssh-keygen -t ed25519` buyrug'i yordamida o'z kompyuteringizda xavfsiz SSH kalitlar juftligini hosil qiling va `~/.ssh/id_ed25519.pub` fayli mazmunini o'rganing.
**Kutiladigan natija:** Yangi zamonaviy SSH kalit muvaffaqiyatli yaratiladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Branch yaratish nima uchun diskda ortiqcha xotira egallamaydi?
2. Fast-forward merge bilan oddiy 3-way merge ning qanday farqi bor?
3. Merge conflict yuzaga kelganda Git qanday belgilarni qo'shadi va ular nimani anglatadi?
4. `git clone` bilan `git pull` ning qanday farqi bor?
5. Nima uchun GitHub'ga parollar o'rniga SSH kalitlar orqali ulanish xavfsizroq hisoblanadi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. O'tgan darsda ochilgan `my_git_lab` repozitoriyasida `login-system` nomli yangi branch yarating.
2. Yangi branchda `login.py` faylini ochib, oddiy autentifikatsiya funksiyasini yozing va commit qiling.
3. Asosiy `main` branchga qaytib, yangi branchni birlashtiring (`git merge`).
4. `git log --oneline --graph` buyrug'ini bajarib, hosil bo'lgan natijani konspektingizga ko'chirib yozing (taxminiy vaqt: 25 daqiqa).

</div>

