---
title: "5-dars. Pull Request (PR) madaniyati, PR shabloni va Merge konfliktlar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 2, "link": "/11-sinf/hafta-02/"}, "g": 5, "title": "Pull Request (PR) madaniyati, PR shabloni va Merge konfliktlar", "lead": "Kod yozish — ishning bor-yo'g'i yarmi. Uni jamoaga to'g'ri taqdim etish, tushuntirish va xatolarsiz asosiy tarmoqqa birlashtirish haqiqiy muhandislik mahoratidir. Ushbu darsda professional Pull Request (PR) ochish, PR shablonlari, merge turlari va qo'rqinchli ko'ringan Merge Konfliktlarni oson hal qilishni o'rganamiz.", "slide": "/slaydlar/11-sinf/hafta-02/dars-2.html", "test": "/slaydlar/11-sinf/hafta-02/dars-2-test.html", "tabs": [{"g": 4, "link": "/11-sinf/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/11-sinf/hafta-02/dars-2", "current": true}, {"g": 6, "link": "/11-sinf/hafta-02/dars-3", "current": false}], "prev": {"g": 4, "title": "Git branching strategiyalari va Conventional Commits", "link": "/11-sinf/hafta-02/dars-1"}, "next": {"g": 6, "title": "Code Review metodologiyasi, etikasi va Branch Protection", "link": "/11-sinf/hafta-02/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Pull Request (PR)** — ishlab chiqilgan tarmoqni (feature branch) asosiy tarmoqqa (`main`) birlashtirishni so'rab jamoaga yuboriladigan rasmiy so'rov.
- PR shunchaki texnik amal emas: u jamoaviy muhokama, xavfsizlik filtri va loyihaning tirik hujjatidir.
- Yaxshi PR uchta asosiy savolga javob beradi: **Why?** (Nima uchun bu o'zgarish kerak?), **What?** (Nimalar o'zgardi?), **How?** (Qanday amalga oshirildi?).
- PR tavsifida `Closes #12` yozilsa, PR merge bo'lishi bilanoq 12-raqamli Issue avtomatik yopiladi.
- `.github/pull_request_template.md` fayli har safar yangi PR ochilganda avtomatik standart tavsif va checklist chiqarib beradi.
- GitHub'da 3 xil merge strategiyasi mavjud: **Create a merge commit** (to'liq tarix), **Squash and merge** (bitta toza commitga siqish), **Rebase and merge** (chiziqli tarix).
- **Merge Conflict** — bitta faylning ayni bir xil qatoriga ikki tarmoqda turlicha o'zgartirish kiritilganda sodir bo'ladi va uni muhandis qo'lda yechishi shart.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega tajribali dasturchilar PR hajmini kichik (Small PRs) ushlaydi?
Google muhandislik amaliyotida mashhur qoida bor:
*"10 qatorlik o'zgarishdan iborat PR ni 10 ta muhandis sinchkovlik bilan tekshiradi. 1000 qatorlik ulkan PR ni esa hamma o'qib o'tirmasdan 'Looks good to me' (LGTM) deb tasdiqlab yuboradi!"*
Katta PR lar ko'rib chiqishga haftalab vaqt oladi, undagi xatolar ko'zdan qochadi va merge konfliktlar ehtimoli 10 barobar oshadi. Ideal PR — 200–300 qatordan oshmasligi kerak.

### Dalillash madaniyati (Evidence / Proof)
PR ochganda unga skrinshot, GIF animatsiya yoki terminal logini ilova qilish — hamkasblarga bo'lgan eng katta hurmatdir. Reviewer (tekshiruvchi) kodni o'z kompyuteriga ko'chirib, loyihani qayta yig'ib o'tirmasdan, bir qarashda funksiya ishlayotganini ko'radi.

### Merge turlari farqi: Qachon qaysi biri ishlatiladi?
1. **Squash and merge:** Feature branchda "tuzatdim", "yana bitta xato", "ishladi" kabi 15 ta xom commit bo'lsa, ularning barchasini bitta `feat: implement user settings` commiti qilib asosiy tarmoqqa yozadi. Eng keng tarqalgan zamonaviy standart!
2. **Create a merge commit:** Katta subsystems relizlari yoki Git Flow'da `develop` ni `main` ga qo'shganda, butun tarixni aynan saqlash uchun ishlatiladi.
3. **Rebase and merge:** Tarix chiziqli (linear) bo'lishini xohlovchi qat'iy jamoalarda qo'llaniladi.

### Merge Conflict belgilari
Git konflikt yuz bergan fayl ichiga maxsus ajratgichlarni yozib qo'yadi:
- `<<<<<<< HEAD` — siz ayni paytda turgan tarmoqdagi joriy kod;
- `=======` — ajratuvchi chegara chizig'i;
- `>>>>>>> branch-nomi` — qo'shilayotgan tarmoqdagi yangi kod.
Sizning vazifangiz — ikkala qismni tahlil qilib, kerakli kodni qoldirish va ushbu belgilarni o'chirib tashlashdir.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Pull Request (PR) | Kodni birlashtirish taklifi va muhokama maydoni |
| PR Template | Yangi ochilgan PR uchun avtomatik chiqadigan tavsif shabloni |
| Checklist | PR birlashtirilishidan oldin bajarilishi shart bo'lgan tekshiruvlar ro'yxati |
| Squash and Merge | Barcha commitlarni bitta yaxlit commitga jamlab asosiy tarmoqqa qo'shish |
| Merge Conflict | Bir xil qatorlardagi ziddiyatli o'zgarishlar to'qnashuvi |
| Conflict Markers | Git tomonidan qo'yiladigan maxsus ajratuvchi belgilar (`<<<<<<<`, `=======`) |
| Issue Auto-close | PR tavsifidagi `Closes #N` orqali vazifani avtomatik yopish |
| Reviewer | PR dagi kod sifatini tekshirish uchun tayinlangan hamkasb |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Pull Request tushunchasini ilk bor 2008-yilda GitHub platformasi ixtiro qilgan. Ungacha ochiq manbali dasturchilar bir-birlariga kod o'zgarishlarini elektron pochta orqali `.patch` fayl shaklida yuborishgan!
- Dunyodagi eng katta ochiq manbali loyihalardan biri bo'lgan Linux yadrosida yiliga 70 000 dan ortiq o'zgarishlar so'rovi qayta ishlanadi.
- Zamonaviy loyihalarda inson ko'rib chiqishidan oldin sun'iy intellekt (botlar) PR dagi xavfsizlik teshiklari va xatolarni avtomatik topib, sharh qoldiradi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. PR shablonini sozlash <Badge type="tip" text="oson" />
Loyihangizda `.github/pull_request_template.md` faylini yarating. Unda Tavsif, Nega kerak (Why) va 3 bandli Checklist bo'lsin.

**Kutiladigan natija:** loyiha repozitoriyasiga qo'shilgan va push qilingan shablon fayli.

### 2. Birinchi rasmiy PR ochish <Badge type="tip" text="oson" />
O'z loyihangizda yangi feature branch oching, kichik o'zgarish kiriting, GitHub'ga push qiling va brauzerda birinchi Pull Request'ni oching.

**Kutiladigan natija:** GitHub'da ochilgan PR havolasi yoki skrinshoti.

### 3. Issue bilan bog'lash <Badge type="tip" text="oson" />
GitHub'da yangi Issue oching (masalan, `#1: Add footer copyright`). So'ngra yangi PR ochib, uning tavsifiga `Closes #1` deb yozing. PR merge bo'lganda Issue avtomatik yopilganini tekshiring.

**Kutiladigan natija:** avtomatik yopilgan Issue skrinshoti.

### 4. Skrinshot dalili qo'shish <Badge type="tip" text="oson" />
Ochilgan PR tavsifiga ekrandagi o'zgarishni isbotlovchi rasm (skrinshot) biriktiring (drag-and-drop orqali).

**Kutiladigan natija:** rasmli dalil bilan boyitilgan tushunarli PR tavsifi.

### 5. Sun'iy konflikt yaratish <Badge type="warning" text="o'rta" />
Terminalda bitta faylning 1-qatorini ikkita turli branchda har xil qilib o'zgartiring va `git merge` orqali ataylab konflikt hosil qiling.

**Kutiladigan natija:** terminalda `CONFLICT (content): Merge conflict in...` xabari chiqqani.

### 6. VS Code yordamida konfliktni hal qilish <Badge type="warning" text="o'rta" />
Hosil bo'lgan konfliktli faylni VS Code da oching. Undagi "Accept Current Change", "Accept Incoming Change" yoki "Accept Both" tugmalaridan foydalanib, mantiqan to'g'ri variantni tanlang va mergeni yakunlang.

**Kutiladigan natija:** tozalangan fayl va yakuniy merge commiti.

### 7. Squash and Merge amaliyoti <Badge type="warning" text="o'rta" />
Feature branchda 3 ta kichik commit qiling. GitHub'da PR ni "Squash and merge" usulida birlashtiring. `main` ga o'tib, `git pull` qiling va `git log` da faqat bittagina chiroyli commit qo'shilganini tekshiring.

**Kutiladigan natija:** asosiy tarmoqda yagona toza commitga aylangan tarix.

### 8. Katta PR tahlili va uni bo'laklarga ajratish <Badge type="warning" text="o'rta" />
Tasavvur qiling, hamkasbingiz 1500 qatordan iborat bitta ulkan PR ochdi (Auth, Database, UI, Testlar hammasi bitta joyda). Siz unga bu PR ni qaysi 3 ta kichik PR ga bo'lishni tavsiya qilasiz?

**Kutiladigan natija:** muhandislik tahlili va 3 ta mustaqil kichik PR rejasining tavsifi.

### 9. Terminal orqali konfliktli Rebase o'tkazish <Badge type="danger" text="qiyin" />
Feature branchda turib `git rebase main` buyrug'ini bering. Konflikt yuz berganda uni hal qiling, `git add` qilib, so'ng `git rebase --continue` orqali rebaseni yakunlang.

**Kutiladigan natija:** rebase jarayoni va chiziqli tarix hosil bo'lganligi.

### 10. PR Checklist auditini o'tkazish <Badge type="danger" text="qiyin" />
Jamoangiz uchun to'liq "Pre-Merge Checklist" ishlab chiqing: xavfsizlik (secret keys, tokens), linter, testlar qamrovi, responsivlik, SEO va hujjatlar bo'yicha kamida 8 ta qat'iy band yozing.

**Kutiladigan natija:** professional darajadagi jamoaviy PR tekshiruv standarti hujjati.

### 11. Murakkab 3 tomonlama konflikt laboratoriyasi <Badge type="info" text="bonus" />
Uchta turli tarmoq (`feat-a`, `feat-b`, `main`) o'rtasida bir xil konfiguratsiya faylida bir necha joyda ziddiyatli o'zgarishlar qiling. Ularni birma-bir ketma-ketlikda barcha funksionallikni yo'qotmagan holda qo'lda birlashtiring va to'liq ishchi holatga keltiring.

**Kutiladigan natija:** barcha o'zgarishlar uyg'unlashgan, konflikt belgilari tozalangan yakuniy ishchi kod.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Pull Request nima uchun jamoaviy sifat eshigi hisoblanadi?
2. PR tavsifida nima uchun What, Why, How savollariga javob berish shart?
3. `Closes #issue_number` buyrug'i qanday vazifani bajaradi?
4. Squash and merge strategiyasi odatiy Merge commitdan nimasi bilan farq qiladi?
5. Merge konflikt nima uchun sodir bo'ladi va undagi `<<<<<<< HEAD` nimani anglatadi?
6. Katta hajmdagi PR larning asosiy xavflari nimalardan iborat?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Portfolio loyihangizda ochilgan `feat/profile-settings` tarmog'i uchun GitHub'da to'liq PR shabloniga asoslangan Pull Request oching. Tavsifga nima qilingani, nima uchun kerakligi va skrinshot dalilini ilova qiling. So'ngra uni "Squash and merge" orqali asosiy `main` tarmoqqa birlashtiring.

</div>

