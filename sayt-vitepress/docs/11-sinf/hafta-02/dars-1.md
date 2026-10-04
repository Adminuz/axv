---
title: "4-dars. Git branching strategiyalari va Conventional Commits"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 2, "link": "/11-sinf/hafta-02/"}, "g": 4, "title": "Git branching strategiyalari va Conventional Commits", "lead": "Bir vaqtning o'zida yuzlab muhandislar bitta loyihada bir-biriga xalaqit bermasdan qanday ishlaydi? Nega professional dasturchilar commit xabarlariga \"ishladi\" deb emas, qat'iy xalqaro standartda yozishadi? Ushbu darsda Git tarmoqlanish arxitekturasi va Conventional Commits madaniyatini o'rganamiz.", "slide": "/slaydlar/11-sinf/hafta-02/dars-1.html", "tabs": [{"g": 4, "link": "/11-sinf/hafta-02/dars-1", "current": true}, {"g": 5, "link": "/11-sinf/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/11-sinf/hafta-02/dars-3", "current": false}], "prev": null, "next": {"g": 5, "title": "Pull Request (PR) madaniyati, PR shabloni va Merge konfliktlar", "link": "/11-sinf/hafta-02/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Branch (Tarmoq)** — asosiy kod bazasidan vaqtincha ajralgan, parallel va xavfsiz tajribalar o'tkazish maydoni.
- Asosiy (`main`) tarmoqqa to'g'ridan-to'g'ri commit qilish professional jamoalarda taqiqlanadi — har bir yangi vazifa alohida branchda qilinadi.
- Zamonaviy Git da tarmoq ochish va unga o'tish uchun `git switch -c <nom>` buyrug'i qo'llaniladi (eski ekvivalenti: `git checkout -b <nom>`).
- **Git Flow** — relizlari kam bo'lgan yirik korporativ loyihalar uchun qat'iy tarmoqlanish modeli (`main`, `develop`, `feature`, `release`, `hotfix`).
- **GitHub Flow** — zamonaviy veb va startaplar standarti bo'lib, har doim barqaror bitta `main` va qisqa muddatli feature branchlarga asoslanadi.
- **Trunk-based development** — jamoa kuniga bir necha marta asosiy tarmoqqa kichik commitlar bilan integratsiya qiladigan yuqori tezlikdagi model.
- **Atomik commit (Atomic Commit)** — "bitta commit — bitta tugallangan fikr" qoidasi.
- **Conventional Commits** — commit xabarlarini standartlashtirish qoidasi: `type(scope): description` (masalan: `feat: add user login`, `fix: handle null pointer`).

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Git da Branch qanday ishlaydi? (Ichki ko'rinish)
Ko'pchilik branch ochilganda loyihadagi barcha fayllar yangi papkaga to'liq nusxalanadi deb o'ylaydi. Agar shunday bo'lganida, 1 GB hajmli loyihada 10 ta branch ochish kompyuterni qotirib qo'ygan bo'lardi.
Aslida Git da branch — bu bor-yo'g'i 41 baytlik oddiy matn fayli! U shunchaki eng oxirgi commitning 40 belgili SHA-1 xesh-kodiga ko'rsatib turuvchi ko'rsatkich (pointer)dir. Siz yangi branch ochganingizda, Git shunchaki yangi ko'rsatkich yaratadi va bu 0.001 soniya vaqt oladi!

### Conventional Commits turlari va ularning ma'nosi
Xalqaro jamoalarda commit turi quyidagi kalit so'zlar bilan boshlanadi:
- `feat:` — foydalanuvchi ko'radigan yangi imkoniyat (New Feature).
- `fix:` — tizimdagi nosozlik yoki xatoni tuzatish (Bug Fix).
- `docs:` — faqat hujjatlashtirish (README, izohlar, Wiki).
- `style:` — kod mantiqiga ta'sir qilmaydigan o'zgarishlar (formatlash, probellar, qator tashlash).
- `refactor:` — kod arxitekturasini tozalash (yangi funksiya ham qo'shilmaydi, xato ham tuzatilmaydi, lekin kod o'qilishi osonlashadi).
- `perf:` — unumdorlikni (tezlik yoki xotira tejamkorligini) oshiruvchi kod (Performance).
- `test:` — avtomatlashtirilgan unit yoki integratsion testlar qo'shish.
- `chore:` — kutubxonalarni yangilash, build sozlamalari yoki yordamchi skriptlar.

### Breaking Change (Orqaga moslikni buzuvchi o'zgarish)
Agar siz yozgan kod loyihaning oldingi versiyalari bilan ishlamay qolsa (masalan, funksiya argumentlari butunlay o'zgarsa yoki eski API o'chirilsa), commit turidan keyin darhol undov belgisi `!` qo'yiladi:
`feat!: change authentication api from cookies to jwt tokens`
Bu belgi avtomatlashtirilgan tizimlarga loyihaning SemVer versiyasida asosiy (Major) raqamni oshirish kerakligini bildiradi (masalan: `v1.4.2` dan `v2.0.0` ga).

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Branch (Tarmoq) | Loyihaning asosiy oqimidan ajralgan mustaqil ishlab chiqish tarmog'i |
| `main` / `master` | Loyihaning asosiy, ishlab turgan barqaror kodi saqlanadigan bosh tarmoq |
| `git switch` | Mavjud tarmoqlar orasida almashish yoki yangi tarmoq ochish buyrug'i |
| Git Flow | Yirik tizimlar uchun qat'iy rolli 5 ta tarmoqdan iborat boshqaruv modeli |
| GitHub Flow | Veb-loyihalar uchun qisqa muddatli feature branchlarga asoslangan yengil model |
| Trunk-based Development | Barcha dasturchilar bitta asosiy tarmoqqa tez-tez commit qiladigan model |
| Atomic Commit | Faqat bitta yaxlit vazifani o'z ichiga oluvchi kichik, mustaqil commit |
| Conventional Commits | Commit xabarlarini mashina va inson tushunadigan formatda yozish standarti |
| Semantic Versioning (SemVer) | Dastur versiyalarini `MAJOR.MINOR.PATCH` formatida raqamlash qoidasi |
| HEAD | Siz ayni paytda qaysi commit yoki branch ustida turganingizni ko'rsatuvchi ko'rsatkich |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Google kompaniyasida 25 000 dan ortiq muhandis Trunk-based development modelida bitta ulkan monorepo (monolit repozitoriy) ustida ishlaydi va har kuni asosiy tarmoqqa 16 000 dan ortiq commit qo'shiladi!
- Git tizimini 2005-yilda Linux operatsion tizimi asoschisi Linus Torvalds bor-yo'g'i ikki hafta ichida yozib chiqqan. Uning asosiy maqsadi — tarmoqlar ochish va birlashtirishni dunyodagi eng tez jarayonga aylantirish edi.
- Agar siz Conventional Commits formatiga qat'iy amal qilsangiz, `semantic-release` kabi vositalar loyihaning versiya raqamini o'zi oshirib, `CHANGELOG.md` faylini bir soniyada avtomatik yozib beradi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Terminalda yangi tarmoq ochish <Badge type="tip" text="oson" />
O'z loyihangizda `git switch -c feat/header-component` buyrug'i orqali yangi tarmoq oching va `git branch` bilan qaysi tarmoqda turganingizni tekshiring.

**Kutiladigan natija:** terminalda yangi branch yaratilgani va uning yonida yulduzcha `*` belgisi turgani.

### 2. Birinchi Conventional Commit <Badge type="tip" text="oson" />
Loyihadagi `README.md` fayliga o'z ismingizni qo'shing va uni `docs:` prefiksi bilan commit qiling.

**Kutiladigan natija:** `git log -1` da to'g'ri formatlangan commit xabari.

### 3. Tarmoqlar orasida sakrash <Badge type="tip" text="oson" />
Yangi tarmoqda bitta fayl yarating va commit qiling. So'ngra `git switch main` qilib asosiy tarmoqqa o'ting. Nega yangi yaratilgan fayl `main` da ko'rinmayotganini tushuntiring.

**Kutiladigan natija:** tarmoqlar izolyatsiyasini isbotlovchi terminal amaliyoti va 1 jumlalik izoh.

### 4. Tarmoqni o'chirish <Badge type="tip" text="oson" />
Keraksiz bo'lgan sinov tarmog'ini `git branch -d <nom>` buyrug'i orqali o'chirib tashlang.

**Kutiladigan natija:** tarmoq xavfsiz o'chirilganligi haqida Git xabari.

### 5. Xato commit xabarlarini tuzating <Badge type="warning" text="o'rta" />
Quyidagi 3 ta noto'g'ri commit xabarini Conventional Commits standartiga moslab qayta yozing:
1. `fixed bug in payment`;
2. `added new button and changed colors and updated readme`;
3. `re-written everything to react`.

**Kutiladigan natija:** 3 ta to'g'ri formatdagi, buyruq maylida yozilgan commit xabari.

### 6. Git Flow va GitHub Flow taqqoslash <Badge type="warning" text="o'rta" />
Tasavvur qiling, siz 3 kishilik jamoa bilan yangi startap (onlayn kuryerlik xizmati) boshlayapsiz. Siz loyihada Git Flow'dan foydalanasizmi yoki GitHub Flow'dan? Nima uchun? Qaroringizni 3 ta dalil bilan asoslang.

**Kutiladigan natija:** yarim sahifalik asoslangan muhandislik tahlili.

### 7. Branch nomlash konvensiyasi <Badge type="warning" text="o'rta" />
Jamoangiz uchun tarmoqlarni nomlash qoidalarini (standart) ishlab chiqing. Kamida 4 xil holat uchun misol keltiring: yangi imkoniyat, xatolikni tuzatish, shoshilinch hotfix, tajriba (experiment).

**Kutiladigan natija:** jamoaviy Branch Naming Guide hujjati.

### 8. Atomik commitlar zanjiri <Badge type="warning" text="o'rta" />
Kichik loyihada ketma-ket 3 ta atomik commit qiling:
1. `feat(user): add user registration model`;
2. `test(user): add validation unit tests for email`;
3. `docs(user): document registration api endpoint`.

**Kutiladigan natija:** `git log --oneline` da ko'rinuvchi 3 ta toza va bir-birini to'ldiruvchi commitlar tarixi.

### 9. Masofaviy repoga yangi tarmoqni yuborish (Push upstream) <Badge type="danger" text="qiyin" />
Lokalda ochilgan yangi feature branchni GitHub'dagi masofaviy repoga `git push -u origin <branch-nomi>` buyrug'i bilan yuboring. GitHub veb-interfeysida yangi tarmoq paydo bo'lganini tekshiring.

**Kutiladigan natija:** GitHub sahifasida yangi branch va uning oxirgi commiti aks etgan skrinshot.

### 10. `git log` chiroyli daraxtini yaratish <Badge type="danger" text="qiyin" />
Terminalda tarmoqlanish chiziqlarini rangli daraxt shaklida ko'rsatuvchi buyruqni ishga tushiring:
`git log --graph --oneline --all --decorate`
Ushbu buyruqni kelgusida bitta so'z bilan (`git tree` yoki `git graph`) chaqirish uchun Git alias sozlamasini bajaring.

**Kutiladigan natija:** terminalda chiroyli grafik daraxt ko'rinishi va o'rnatilgan alias buyrug'i.

### 11. Breaking Change laboratoriyasi <Badge type="info" text="bonus" />
O'z kutubxonangiz yoki API kodingizda orqaga moslikni buzuvchi o'zgarish kiriting va uni Conventional Commits ning `!` belgisi hamda `BREAKING CHANGE:` izoh qismi bilan commit qiling. `git show` yordamida ushbu commitning to'liq tafsilotini ko'rsating.

**Kutiladigan natija:** xalqaro spetsifikatsiyaga 100% mos bo'lgan Breaking Change commitining to'liq ko'rinishi.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Nima uchun production (`main`) tarmog'iga to'g'ridan-to'g'ri kod yozish xavfli hisoblanadi?
2. `git switch` va eski `git checkout` buyruqlari o'rtasidagi farq nima?
3. Conventional Commits formatining umumiy strukturasi qanday?
4. Atomik commit tushunchasi dasturchiga qanday qulaylik yaratadi?
5. Qachon Git Flow o'rniga GitHub Flow tanlangan ma'qul?
6. Commit xabarida `!` belgisi nimani anglatadi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

O'zingizning portfolio mini-loyihangizda `main` tarmog'idan `feat/profile-settings` nomli yangi tarmoq oching. Unda foydalanuvchi sozlamalari faylini yarating, kamida 2 ta Conventional Commit (`feat:` va `docs:`) bajaring, so'ngra branchni GitHub repozitoriyangizga push qiling.

</div>

