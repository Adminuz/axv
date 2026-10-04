---
title: "2-dars. Git asoslari: versiyalarni boshqarish, repozitoriy, commit, branch va merge"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 1, "link": "/11-sinf/hafta-01/"}, "g": 2, "title": "Git asoslari: versiyalarni boshqarish, repozitoriy, commit, branch va merge", "lead": "Bugun siz kodingiz uchun «vaqt mashinasi» yasaysiz: terminalda birinchi repozitoriyni yaratib, har o'zgarishni saqlaysiz, parallel shox ochasiz va konfliktni yechasiz. Professional dasturchilar har kuni shu buyruqlar bilan ishlaydi.", "slide": "/slaydlar/11-sinf/hafta-01/dars-2.html", "tabs": [{"g": 1, "link": "/11-sinf/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/11-sinf/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/11-sinf/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "IT ekotizimi qatlamlari, SDLC bosqichlari va jamoadagi rollar", "link": "/11-sinf/hafta-01/dars-1"}, "next": {"g": 3, "title": "GitHub: masofaviy repo, push/pull/clone, README, .gitignore, Issues va birinchi loyiha", "link": "/11-sinf/hafta-01/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Versiyalarni boshqarish tizimi (VCS) fayllar tarixini yozib boradi: kim, qachon, nima uchun o'zgartirgan.
- Git taqsimlangan VCS: har kompyuterda to'liq tarix bor, internetsiz ham ishlaydi. GitHub esa alohida xizmat (3-dars).
- Sozlash: `git config --global user.name` va `user.email`, `init.defaultBranch main`.
- `git init` papkada yashirin `.git/` yaratadi; tarix shu yerda saqlanadi.
- Uch zona: Working directory → (`git add`) → Staging → (`git commit`) → Repository.
- Commit: muallif, vaqt, xabar, snapshot, parent va noyob hash. Xabar Conventional Commits uslubida: `feat: ...`, `fix: ...`.
- Branch — commit'ga ko'rsatkich: `git switch -c`, `git merge`, `git branch -d`. Merge fast-forward yoki merge commit bo'ladi.
- Konflikt: Git to'xtaydi, siz qo'lda yechasiz. Tarix: `git log --oneline --graph`. Qaytarish: `git restore`, `git revert`.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Git «diff» emas, «snapshot» saqlaydi
Ko'pchilik Git «o'zgarishlarni» saqlaydi deb o'ylaydi. Aslida har commit loyihaning o'sha paytdagi to'liq holatiga ishora qiladi (o'zgarmagan fayllar qayta saqlanmaydi, eski nusxaga havola qilinadi). `git diff` esa ikki snapshotni solishtirib farqni hisoblaydi. Shu sabab istalgan commitga bir lahzada o'tish mumkin: Git «hamma o'zgarishni ketma-ket qayta qo'llamaydi».

Tasavvur qiling: har commit — kitobning qotirilgan nusxasi, har bir nusxada «oldingi nusxa» (parent) belgisi bor. Shu belgilar zanjiri tarixni hosil qiladi.

### Nega staging zonasi bor?
«To'g'ridan-to'g'ri ishchi papkadan commit qilsak bo'lmasmidi?» Staging — savatga yig'ish. Siz bir soatda uch narsani o'zgartirgan bo'lsangiz (xatoni tuzatdingiz, matn yozdingiz, yangi funksiya boshladingiz), ularni uchta alohida commit qilasiz, har birining o'z xabari bilan. Tarix o'qiladigan bo'ladi va xato bo'lsa faqat bittasini bekor qilasiz.

```bash
git add hello.py            # faqat shu fayl
git commit -m "fix: correct typo in greeting"
git add README.md
git commit -m "docs: describe project"
```

### Branch nusxa emas, ko'rsatkich
Yangi shox ochganda Git papkani nusxalamaydi. U shunchaki commit'ga yangi nom (ko'rsatkich) qo'yadi. Shuning uchun shox yaratish bir lahza oladi va ularni ko'p ochish odatiy ishdir: bir vazifa — bir shox. `HEAD` esa «hozir men qaysi shoxdaman» belgisi. `git switch` HEAD'ni ko'chiradi va ishchi papka fayllarini shu shox holatiga almashtiradi.

### Fast-forward va merge commit
- `main` da yangi commit bo'lmasa, Git shunchaki `main` ko'rsatkichini oldinga suradi: yangi commit yaratilmaydi, tarix to'g'ri chiziq (fast-forward).
- Ikkala shoxda ham yangi commit bor bo'lsa, Git ikkala tarixni bog'laydigan yangi **merge commit** yaratadi. Unda ikkita parent bo'ladi. Grafikda `|\` va `|/` shaklida ko'rinadi.

### Konflikt: Git «xato» emas, so'rayapti
Ikki shox bitta qatorni turlicha o'zgartirsa, Git qaysi biri to'g'riligini bilmaydi va to'xtaydi. Faylda belgilar paydo bo'ladi:

```
<<<<<<< HEAD
bu — hozirgi shoxdagi (main) variant
=======
bu — birlashtirilayotgan shoxdagi variant
>>>>>>> feature/nom
```

Siz yakuniy matnni qoldirasiz, uchta belgi qatorini o'chirasiz, so'ng `git add` va `git commit`. Adashsangiz: `git merge --abort` hammasini merge'dan oldingi holatga qaytaradi. Kamdan-kam konflikt uchun qoida: kichik commitlar, qisqa umrli shoxlar.

### Xato qilsam-chi?
| Vaziyat | Buyruq |
|---|---|
| Faylni oxirgi commit holatiga qaytarish (saqlanmagan o'zgarish yo'qoladi!) | `git restore fayl` |
| Faylni stagingdan chiqarish (o'zgarish fayl ichida qoladi) | `git restore --staged fayl` |
| Commitni bekor qilish (yangi teskari commit qo'shadi) | `git revert <hash>` |

`git restore` ehtiyot bo'lishni talab qiladi: Git saqlanmagan o'zgarishni hech qayerda saqlamaydi. Commit qilingan narsani esa deyarli doim qaytarish mumkin.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| VCS | Version Control System: fayl o'zgarishlari tarixini yurituvchi tizim |
| Repository (repo) | Loyiha fayllari va butun tarixi (`.git/` papkasi) |
| Working directory | Ishchi papka: fayllarni tahrirlaydigan joy |
| Staging area (index) | Keyingi commitga kiradigan o'zgarishlar «savati» |
| Commit | Muallif, vaqt, xabar va snapshot'ni saqlovchi tarix nuqtasi |
| Hash | Commitning noyob SHA-1 identifikatori (masalan `3280c5a`) |
| Branch | Commit'ga ko'rsatkich: mustaqil ish yo'lagi |
| HEAD | Hozir qaysi shox/commitda ekanligingizni bildiruvchi ko'rsatkich |
| Merge | Ikki shoxni birlashtirish |
| Fast-forward | Yangi commit yaratmasdan shox ko'rsatkichini oldinga surish |
| Conflict | Ikki shox bitta joyni turlicha o'zgartirgani; qo'lda yechiladi |
| Conventional Commits | Commit xabari formati: `tur: tavsif` (`feat`, `fix`, `docs`) |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Git'ni 2005-yilda Linus Torvalds, Linux yadrosi dasturchilari ishlayotgan vosita to'xtab qolgach, taxminan ikki haftada yozib chiqqan.
- «Hash» sizning kompyuteringizda hisoblanadi va faqat commit mazmuni, muallifi va ota commitdan kelib chiqadi: shuning uchun tarixni jimgina o'zgartirib bo'lmaydi.
- Git'da `master` o'rniga `main` nomi so'nggi yillarda standartga aylandi: hozirgi platformalar yangi repolarda `main` ni afzal ko'radi.
- `git log --graph` ni terminalda ko'rish mumkin, ammo professionallar ko'pincha `git lg` kabi alias yaratib oladi.
- `.git/` papkasini boshqa joyga nusxalasangiz, butun loyiha tarixini ko'chirgan bo'lasiz.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

Barcha topshiriqlarni terminalda `dev-journal` repozitoriysida bajaring. Hash'lar sizda boshqacha bo'ladi.

### 1. Birinchi repozitoriy <Badge type="tip" text="oson" />
`dev-journal` papkasini yarating, `git init -b main` qiling. `README.md` («# Dev Journal») va `hello.py` (`print("Salom, Git!")`) yarating va ikkita alohida commit qiling, xabarlar Conventional Commits uslubida bo'lsin.

**Kutiladigan natija:** `git log --oneline` da 2 ta commit, `git status` da «working tree clean».

### 2. Bu qanday ko'rinadi? <Badge type="tip" text="oson" />
Bashorat qiling: quyidagi buyruqlardan keyin `git status -s` nima chiqaradi?

```bash
echo "a" > a.txt
git add a.txt
echo "b" >> a.txt
```

**Kutiladigan natija:** bashoratingiz va tekshiruv natijasi; nega fayl ikki holatda ekanini bir jumlada tushuntiring.

### 3. Config'ni o'qing <Badge type="tip" text="oson" />
`git config --global --list` ni ishga tushiring. Keyin faqat `dev-journal` uchun boshqa `user.email` o'rnating (bayroqsiz). Repo ichida va tashqarisida `git config user.email` nima chiqaradi?

**Kutiladigan natija:** ikki xil email va nega shunday bo'lishining izohi (local global'dan kuchli).

### 4. Diff qaysi zonada? <Badge type="tip" text="oson" />
`hello.py` ga bitta qator qo'shing. `git diff`, `git add hello.py`, yana `git diff` va `git diff --staged` ni ishga tushiring.

**Kutiladigan natija:** qaysi buyruq nimani ko'rsatgani va nima uchun bitta `git diff` bo'sh qolganini tushuntirish.

### 5. Birinchi feature shoxi <Badge type="warning" text="o'rta" />
`feature/skills` shoxida `skills.md` fayl yarating (3 ta ko'nikma), kamida 2 ta commit qiling. `main` ga qaytib, faylning yo'qligini tekshiring, keyin merge qiling va shoxni o'chiring.

**Kutiladigan natija:** merge'dan oldin `ls` da `skills.md` yo'q, keyin bor; shox ro'yxatida faqat `main`.

### 6. Ikkita alohida commit <Badge type="warning" text="o'rta" />
Bir vaqtda `hello.py` ga ham, `README.md` ga ham o'zgartirish kiriting. Staging yordamida ularni ikki alohida commitga ajrating.

**Kutiladigan natija:** `git log --stat -n 2` da har commitda faqat bitta fayl o'zgargan.

### 7. Restore yoki revert? <Badge type="warning" text="o'rta" />
`hello.py` ni ataylab buzing. Avval `git restore` bilan qaytaring. Keyin yana buzing, commit qiling va `git revert HEAD` bilan bekor qiling. Log'da farqni toping.

**Kutiladigan natija:** ikkala usulning farqi: qaysi biri tarixga iz qoldiradi va qachon qaysi biri xavfsiz (bir-ikki jumla).

### 8. Grafikni o'qing <Badge type="warning" text="o'rta" />
Quyida tarix grafigi berilgan. Nechta shox ochilgan, nechta merge commit bor va qaysi commit ikki parentli?

```
*   79a25f9 Merge branch 'feature/bye'
|\
| * 03c5311 feat: add goodbye
* | d76ee7f docs: describe project
|/
* 245556f feat: greet by name
* 3280c5a feat: add second line
```

**Kutiladigan natija:** to'g'ri sanalgan shox va merge, ikki parentli commit hash'i.

### 9. Konflikt yarating va yeching <Badge type="danger" text="qiyin" />
`main` va `feature/title` shoxlarida `README.md` ning birinchi qatorini turlicha o'zgartiring va birlashtiring. Konfliktni qo'lda yeching: yakuniy sarlavha ikkala g'oyani o'zida jamlasin. Tekshiruv: faylda `<<<<<<<` qolmasin.

**Kutiladigan natija:** merge commit, `git log --oneline --graph` da ikki shox, `grep '<<<<' README.md` natijasi bo'sh.

### 10. Merge'ni bekor qilish <Badge type="danger" text="qiyin" />
9-topshiriqdagi konfliktni yana yarating (yangi shox nomi bilan), lekin yechmasdan `git merge --abort` qiling. Fayl va `git status` qanday bo'ldi? Qanday holatda abort, qanday holatda yechish to'g'ri ekanini yozing.

**Kutiladigan natija:** abortdan keyingi toza holat tavsifi va 3–4 jumlali muhokama.

### 11. Tarix bo'ylab sayohat <Badge type="danger" text="qiyin" />
`git log --oneline` dan eski commit hash'ini tanlang. `git show <hash>` bilan nimani o'zgartirganini ko'ring, `git switch --detach <hash>` bilan o'sha holatga o'ting, faylni ko'ring va `git switch main` bilan qayting. Tadqiq: detached HEAD'da commit qilsangiz nima bo'ladi?

**Kutiladigan natija:** o'sha paytdagi fayl mazmuni va nazariy javob (commit qaysi shoxda qoladi).

### 12. Bonus: shaxsiy alias <Badge type="info" text="bonus" />
`git lg` nomli alias yarating, u `git log --oneline --graph --all` ni bajarsin. Yana bitta o'zingizga foydali alias o'ylab toping (masalan, `git st` = `git status -s`).

**Kutiladigan natija:** ikkala alias ishlaydi; `git config --global --get-regexp alias` ro'yxati.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Git va GitHub o'rtasidagi farq nima?
2. Working directory, staging va repository qanday bog'langan? Qaysi buyruq qaysi zonadan qaysi zonaga o'tkazadi?
3. Commit nimalardan iborat va nega xabarini yaxshi yozish kerak?
4. `git add` qilmasdan `git commit -m "..."` yozsangiz nima bo'ladi? `git commit -am` esa nima qiladi?
5. Fast-forward merge va merge commit qachon bo'ladi?
6. Konflikt belgilari (`<<<<<<<`, `=======`, `>>>>>>>`) nimani bildiradi?
7. `git restore` va `git revert` farqi nima?
8. `git config` ning global va local darajasi qanday farq qiladi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

**`dev-journal` ni boyiting** (20–30 daqiqa): `.gitignore` yarating (kamida `.env` va `__pycache__/` qatorlari). Uch kun uchun `notes/kun-1.md`, `kun-2.md`, `kun-3.md` yozuvlarini yozing: har biri alohida commit bo'lsin, xabarlar Conventional Commits uslubida. `feature/skills` shoxini ochib bitta o'zgarish qiling va `main` ga merge qiling. `git log --oneline --graph` natijasini `log.txt` fayliga saqlang va commit qiling. Keyingi darsda bu repoz GitHub'ga yuklanadi.

</div>

