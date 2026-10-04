# 2-dars. Git asoslari: versiyalarni boshqarish, repozitoriy, commit, branch va merge

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + terminal amaliyoti · **I-bob**, 2-dars

> Dasturda «Axborot texnologiyalari ekotizimi, SDLC va versiyalarni boshqarish (Git/GitHub)» mavzusiga 3 dars ajratilgan (1–3). Bo'linish: 1-dars — IT ekotizimi qatlamlari va SDLC bosqichlari; **2-dars — Git asoslari (lokal, terminalda)**; 3-dars — GitHub (remote, push/pull, README, .gitignore, Issues, PR'ga kirish). Bu dars faqat o'z kompyuteringizdagi repozitoriy bilan ishlaydi: internet va akkaunt kerak emas.

## 1. Dars rejasi

**Maqsad:** o'quvchi Git'ni o'rnatib sozlaydi, terminalda repozitoriy yaratadi, uch zonali modelni (working directory → staging → repository) tushunib commit qiladi, shox ochib birlashtiradi, konfliktni yechadi va tarixni o'qiydi.

**Kutiladigan natija:**
- Version control nima va Git nega taqsimlangan tizim ekanini tushuntiradi.
- `git config`, `git init`, `git status`, `git add`, `git commit`, `git diff`, `git log` ni ishlatadi.
- Commit nima ekanini (snapshot, hash, muallif, xabar, parent) biladi; yaxshi commit xabari yozadi.
- `git switch -c`, `git merge`, `git branch -d` bilan ishlaydi; fast-forward va merge commit farqini ko'radi.
- Konflikt belgilarini (`<<<<<<<`, `=======`, `>>>>>>>`) o'qib, qo'lda yechadi.
- `git restore` va `git revert` bilan o'zgarishni qaytarishni biladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 | Takrorlash va ko'prik | 1-dars: SDLC bosqichlari, «Kod» bosqichi; uyga vazifa (bo'lsa) |
| 8–28 | Yangi mavzu 1 | Nega Git, o'rnatish va config, `init`, 3 zona, `add`/`commit`, `status`, `diff` |
| 28–35 | Tanaffus | |
| 35–55 | Yangi mavzu 2 | Branch, merge (ff va merge commit), konflikt, `log`, `restore`/`revert` |
| 55–75 | Amaliyot | `dev-journal` mini-loyihasi (3 daraja) |
| 75–80 | Tezkor nazorat va xulosa | |

**Mini-loyiha:** o'quvchi butun kurs davomida `dev-journal` repozitoriyini yuritadi (kunlik IT yozuvlari + kichik Python fayl). 3-darsda u GitHub'ga yuklanadi, keyin portfolio (IV bob) tarkibiga kiradi.

**Oldindan tayyorlik (mentor):** o'quvchi kompyuterida `git --version` ishlashi kerak. Windowsda Git Bash (Git for Windows bilan keladi), macOS'da `git --version` (Xcode Command Line Tools so'raydi), Linuxda `sudo apt install git`. Dars boshida tekshirib, kerak bo'lsa tanaffusda o'rnating. Matn muharriri ixtiyoriy (VS Code, nano).

## 2. Konspekt

### 2.1. Takrorlash va ko'prik (8 daqiqa)
Savollar (1-darsdan): SDLC bosqichlarini ayting. «Kod yozish» bosqichida qanday artefaktlar paydo bo'ladi (kod bazasi, konfiguratsiya, testlar)? Ko'prik: dasturlash «asosiy ish» ko'rinsa ham, SDLC ning bir bo'lagi. Bu bo'lakda kod xavfsiz saqlanishi, o'zgarishlari kuzatilishi va jamoada to'qnashmasligi kerak. Shu uchun Git.

### 2.2. Nega versiyalarni boshqarish kerak?
Muammo: `hisobot_final_v3_HAQIQIY.docx` papkalari. Qaysi biri oxirgi? Kim nimani o'zgartirdi? Eski holatga qanday qaytamiz? Ikki kishi bir faylni o'zgartirsa nima bo'ladi?

**Version control system (VCS)** — fayllar o'zgarishlarini vaqt bo'yicha yozib boradigan tizim. Imkoniyatlari: har o'zgarish tarixi (kim, qachon, nega), istalgan eski holatga qaytish, xatoni tez topish, parallel ishlash (branch), jamoada birlashtirish.

| | Markazlashgan (SVN) | Taqsimlangan (Git) |
|---|---|---|
| Tarix | bitta serverda | har kompyuterda to'liq nusxa |
| Internetsiz | deyarli ishlamaydi | commit, branch, log ishlaydi |
| Server qulasa | ish to'xtaydi | har bir klon zaxira |

**Git** — 2005-yilda Linus Torvalds Linux yadrosi uchun yaratgan taqsimlangan VCS. Qo'llanma bo'yicha, Git kodning yakuniy holatini emas, **o'zgarishlar tarixini** (commitlar grafigini) saqlaydi. Aniqlik: ichki tuzilishida har commit fayllarning to'liq snapshot'iga ishora qiladi (diff'lar zanjiri emas), diff esa shu snapshotlarni solishtirib hisoblanadi.

**Git ≠ GitHub.** Git — kompyuteringizdagi dastur (buyruqlar). GitHub — Git repozitoriylarini internetda saqlaydigan va hamkorlik (PR, review, Issues) qo'shadigan xizmat. Bugun faqat Git.

### 2.3. O'rnatish va sozlash
```bash
git --version                                   # o'rnatilganini tekshirish
git config --global user.name  "Aziz Karimov"   # commit muallifi
git config --global user.email "aziz@example.com"
git config --global init.defaultBranch main     # yangi repo shoxi "main" bo'lsin
git config --list --show-origin                 # barcha sozlamalar va qayerdan kelgani
```
- Config 3 darajada: `--system` (butun kompyuter), `--global` (foydalanuvchi, `~/.gitconfig`), local (repo ichida `.git/config`, bayroqsiz). Mahalliy global'ni bosib o'tadi.
- `user.email` ni 3-darsda GitHub akkaunt emailiga moslab qo'yamiz (aks holda GitHub commitlarni profilga bog'lamaydi).
- Eslatma: `init.defaultBranch` Git 2.28 dan; `git switch/restore` Git 2.23 dan. Eski versiyada `git checkout` ishlatiladi.

### 2.4. Repozitoriy va `git init`
```bash
mkdir dev-journal && cd dev-journal
git init -b main
```
`git init` papkada yashirin `.git/` katalogini yaratadi: u yerda `objects/` (barcha commit va fayl ma'lumotlari), `refs/` (shox va tag nomlari), `HEAD` (hozirgi shox), `index` (staging), `config`. `.git/` o'chirilsa, tarix yo'qoladi. Shuning uchun `.git` ichiga qo'lda tegmaymiz.

### 2.5. Uch zona va commit
1. **Working directory** — ishchi papka: fayllarni tahrirlaysiz.
2. **Staging area (index)** — keyingi commitga kiradigan o'zgarishlar «savati».
3. **Repository (.git)** — saqlangan commitlar tarixi.

`git add` ishchi papkadan stagingga, `git commit` stagingdan tarixga o'tkazadi. Nega staging? Bir ishda turli narsalarni o'zgartirgan bo'lsangiz, ularni mantiqan alohida commitlarga ajratasiz.

**Commit** — muallif, vaqt, xabar, fayllar snapshot'i va ota commitga (parent) havolani saqlovchi tarixiy nuqta. Har commitga noyob **hash** (SHA-1, 40 belgi; odatda 7 belgi ko'rsatiladi) beriladi.

**Yaxshi commit xabari:** nima o'zgardi va nega; buyruq maylida; ~50 belgi. **Conventional Commits** formati: `tur: qisqa tavsif` (`feat`, `fix`, `docs`, `refactor`, `test`). Yomon: `ozgardi`, `fix`, `asdf`. Yaxshi: `feat: add greeting by name`. Mayda va maqsadli commitlar qo'llanma ham tavsiya etadi.

`git status -s` belgilari: `??` kuzatilmaydi; `A ` stagingga qo'shildi; ` M` o'zgardi, stagingda emas; `M ` o'zgardi va stagingda.

`git diff` — ishchi papka va staging farqi; `git diff --staged` — staging va oxirgi commit farqi.

### 2.6. Branch va merge
**Branch (shox)** — commit'ga ko'rsatkich. Yaratish bir lahzada, fayllar nusxalanmaydi. Asosiy kod `main` da; yangi ish alohida shoxda (`feature/...`, `fix/...`). `HEAD` — hozir qaysi shoxdasiz.

```bash
git switch -c feature/greeting   # yarat va o'tish
git switch main                  # asosiy shoxga qaytish
git branch                       # shoxlar ro'yxati (* hozirgi)
git merge feature/greeting       # feature'ni main'ga birlashtirish (main'da turib)
git branch -d feature/greeting   # birlashgan shoxni o'chirish
```
- **Fast-forward:** main'da yangi commit yo'q bo'lsa, Git main ko'rsatkichini oldinga suradi.
- **Merge commit:** ikkala shoxda yangi commit bor bo'lsa, Git ikki ota-onali yangi commit yaratadi (`Merge branch '...'`).
- **Rebase** (qo'llanmada): feature commitlarini main uchiga qayta tikadi, tarix tekis bo'ladi. Qoida: umumiy repoga yuborilgan tarixni rebase qilmaymiz. Bugun faqat tanishuv uchun eslatamiz, amaliyot 2-haftada (Branching, PR).

**Konflikt:** ikkala shox bitta joyni turlicha o'zgartirsa, Git to'xtab, faylga belgilar qo'yadi:
```
<<<<<<< HEAD
# Dasturchi kundaligi
=======
# Aziz Dev Journal
>>>>>>> feature/title
```
`HEAD` ustidagi qism — hozirgi shox (main); `=======` dan keyin — birlashtirilayotgan shox. Yechish: faylni tahrirlab yakuniy matnni qoldiring, belgilarni o'chiring, `git add`, `git commit`. Chiqish: `git merge --abort`. Konfliktdan qochish: mayda commitlar, tez-tez sinxronlash (3-darsda `fetch`/`pull`).

### 2.7. Tarix va qaytarish
```bash
git log                        # to'liq tarix
git log --oneline --graph      # bir qatorli, shoxlar grafigi
git log --oneline --all -n 5   # barcha shoxlar, oxirgi 5 ta
git show 3280c5a               # bitta commit tafsiloti
git restore hello.py           # saqlanmagan ishchi o'zgarishni bekor qilish
git restore --staged hello.py  # stagingdan chiqarish (o'zgarish fayl ichida qoladi)
git revert <hash>              # commitni teskari commit bilan bekor qilish
```
`git restore` saqlanmagan o'zgarishni **qaytarib bo'lmaydigan** o'chiradi. `git revert` tarixni buzmaydi (yangi commit qo'shadi), shuning uchun umumiy shoxlarda xavfsiz. `git reset --hard` va `rebase` kabi tarixni o'zgartiruvchi buyruqlar keyingi darslarda ehtiyotkorlik bilan.

Git'ning boshqa imkoniyatlari (kelgusi darslarda eslatiladi): `git bisect` (xato kiritilgan commitni topish), `git tag` (release nuqtasi), `git reflog` («vaqt mashinasi»).

## 3. Kod namunalari (haqiqiy ishga tushirilgan, git 2.50)

**Namuna 1 — birinchi commitlar (hash'lar har kimda boshqacha):**
```
$ mkdir dev-journal && cd dev-journal
$ git init -b main
Initialized empty Git repository in /.../dev-journal/.git/
$ echo "# Dev Journal" > README.md
$ git status -s
?? README.md
$ git add README.md
$ git status -s
A  README.md
$ git commit -m "docs: add README"
[main (root-commit) bd42656] docs: add README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

**Namuna 2 — o'zgartirish, diff, commit, log:**
```
$ printf 'print("Salom, Git!")\n' > hello.py
$ git add hello.py && git commit -m "feat: add hello.py"
$ echo 'print("Ikkinchi qator")' >> hello.py
$ git diff
--- a/hello.py
+++ b/hello.py
@@ -1 +1,2 @@
 print("Salom, Git!")
+print("Ikkinchi qator")
$ git status -s
 M hello.py
$ git commit -am "feat: add second line"
$ git log --oneline
3280c5a feat: add second line
5284414 feat: add hello.py
bd42656 docs: add README
```
(`git diff` sarlavhasidagi `diff --git`, `index` qatorlari qisqartirildi.)

**Namuna 3 — fast-forward merge:**
```
$ git switch -c feature/greeting
Switched to a new branch 'feature/greeting'
$ printf 'name = "Aziz"\nprint(f"Salom, {name}!")\n' > hello.py
$ git commit -am "feat: greet by name"
$ git switch main
$ git merge feature/greeting
Updating 3280c5a..245556f
Fast-forward
 hello.py | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
$ git branch -d feature/greeting
Deleted branch feature/greeting (was 245556f).
```

**Namuna 4 — ikkala shoxda commit bor: merge commit:**
```
$ git switch -c feature/bye
$ echo 'print("Xayr!")' >> hello.py
$ git commit -am "feat: add goodbye"
$ git switch main
$ echo "Kunlik yozuvlar: Git o'rganyapman." >> README.md
$ git commit -am "docs: describe project"
$ git merge feature/bye --no-edit
Merge made by the 'ort' strategy.
 hello.py | 1 +
$ git log --oneline --graph
*   79a25f9 Merge branch 'feature/bye'
|\
| * 03c5311 feat: add goodbye
* | d76ee7f docs: describe project
|/
* 245556f feat: greet by name
* 3280c5a feat: add second line
* 5284414 feat: add hello.py
* bd42656 docs: add README
```
(Oddiy `git merge` muharrir ochadi: xabarni saqlab chiqing. `--no-edit` standart xabarni qabul qiladi.)

**Namuna 5 — konflikt va uni yechish:**
```
$ git switch -c feature/title
$ sed -i '' '1s/.*/# Aziz Dev Journal/' README.md        # macOS; Linux: sed -i '1s/.*/.../'
$ git commit -am "docs: personal title"
$ git switch main
$ sed -i '' '1s/.*/# Dasturchi kundaligi/' README.md
$ git commit -am "docs: uzbek title"
$ git merge feature/title
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
$ git status -s
UU README.md
```
README.md ichi (belgilar bilan) yuqorida 2.6 bo'limida. Yechim: faylni muharrirda ochib, birinchi qatorni `# Aziz — Dasturchi kundaligi` qilib belgilarsiz qoldiring, so'ng:
```
$ git add README.md
$ git commit --no-edit
[main 2b17e98] Merge branch 'feature/title'
```
(`sed -i` farqi: macOS'da `-i ''`, Linuxda `-i`. O'quvchi qo'lda muharrirda tahrirlasa, shu farq kerak bo'lmaydi: afzal.)

## 4. Amaliy topshiriqlar

Hammasi `dev-journal` repozitoriysida (yoki 1-topshiriqda yaratilganida).

### Oson 1 — Birinchi repo
`~/dev-journal` yarating, `git init -b main`, `README.md` («# Dev Journal») va `hello.py` (`print("Salom, Git!")`) yarating. Ikki alohida commit qiling (xabarlari Conventional Commits uslubida). `git log --oneline` ko'rsating.
**Kutiladigan natija:** log'da 2 ta commit, `git status` — «nothing to commit, working tree clean».
**Yechim:**
```bash
mkdir dev-journal && cd dev-journal
git init -b main
echo "# Dev Journal" > README.md
git add README.md && git commit -m "docs: add README"
echo 'print("Salom, Git!")' > hello.py
git add hello.py && git commit -m "feat: add hello.py"
git log --oneline
git status
```

### Oson 2 — Bashorat qiling
Quyidagi qatorlardan keyin `git status -s` nima ko'rsatadi? Avval yozing, keyin tekshiring.
```bash
echo "a" > a.txt
git add a.txt
echo "b" >> a.txt
```
**Kutiladigan natija:** o'quvchi bir faylning ikki holatini tushunadi.
**Yechim:** `AM a.txt`: fayl stagingga «a» bilan qo'shilgan (A), ishchi papkada esa keyin «b» qo'shilgan, u hali stagingda emas (M). Agar hozir `git commit` qilinsa, faqat «a» saqlanadi. Ikkinchi ustundagi `M` ishchi papka o'zgarishini bildiradi.

### Oson 3 — Config
`git config --global --list` bilan `user.name`, `user.email`, `init.defaultBranch` qiymatlarini tekshiring. Faqat `dev-journal` ichida (global'ga tegmay) `user.email` ni boshqa qiymatga o'zgartiring va qaysi qiymat ishlatilayotganini isbotlang.
**Kutiladigan natija:** `git config user.email` repo ichida local qiymatni, repodan tashqarida global'ni ko'rsatadi.
**Yechim:**
```bash
git config --global --list
cd dev-journal
git config user.email "local@example.com"     # --global yo'q: faqat shu repo
git config --show-origin user.email            # file:.git/config  local@example.com
cd .. && git config user.email                 # global qiymat
```

### Oson 4 — Diff'ni o'qing
`hello.py` ga bitta qator qo'shing. `git diff` ni ko'ring (qaysi qator `+` bilan?), `git add`, keyin `git diff` (bo'sh) va `git diff --staged` (qator ko'rinadi) ni ishga tushiring. Nega ikkinchi `git diff` bo'sh?
**Kutiladigan natija:** o'quvchi diff ikki zona orasidagi farq ekanini aytadi.
**Yechim:** `git add` dan keyin ishchi papka va staging bir xil, shuning uchun `git diff` bo'sh. O'zgarish endi staging va oxirgi commit orasida: `git diff --staged` ko'rsatadi.

### O'rta 1 — Birinchi feature shoxi
`feature/skills` shoxini oching, `skills.md` yarating (3 ta ko'nikma ro'yxati), ikki commit qiling (har ko'nikma yoki bo'lim uchun alohida), `main` ga qaytib birlashtiring, shoxni o'chiring. `main` da `skills.md` ko'rinmaydigan lahzani ham tekshiring.
**Kutiladigan natija:** merge'dan oldin `main` da `ls` skills.md ni ko'rsatmaydi, keyin ko'rsatadi; log'da 2 ta yangi commit.
**Yechim:**
```bash
git switch -c feature/skills
printf '# Ko'"'"'nikmalarim\n- Git\n' > skills.md
git add skills.md && git commit -m "docs: add skills list"
echo "- Terminal" >> skills.md
git commit -am "docs: add terminal skill"
git switch main
ls                      # skills.md yo'q
git merge feature/skills
ls                      # skills.md bor
git branch -d feature/skills
```
(Birinchi qatordagi `'"'"'` — shell'da `'` belgisi; muharrirda yozish osonroq.)

### O'rta 2 — Staging bilan alohida commitlar
Bir vaqtda ikkita bog'liq bo'lmagan o'zgarish qiling: `hello.py` ga qator va `README.md` ga qator. Ularni **ikki alohida commit**ga ajrating (har birining o'z xabari bilan).
**Kutiladigan natija:** `git log --stat` har commitda faqat bitta fayl o'zgarganini ko'rsatadi.
**Yechim:**
```bash
echo 'print("Yangi")' >> hello.py
echo "Qisqa tavsif" >> README.md
git add hello.py && git commit -m "feat: add new print"
git add README.md && git commit -m "docs: add short description"
git log --stat -n 2
```

### O'rta 3 — Xatoni qaytarish
Ataylab `hello.py` ni buzing (`print(` ni qoldiring). 1) Saqlanmagan o'zgarishni `git restore` bilan qaytaring. 2) Keyin xatoni commit qiling, so'ng `git revert HEAD` bilan bekor qiling. Ikkala holatda log'da nima farq qiladi?
**Kutiladigan natija:** restore tarixga iz qoldirmaydi; revert yangi «Revert ...» commit qo'shadi.
**Yechim:**
```bash
echo 'print(' >> hello.py
git restore hello.py                  # o'zgarish yo'q bo'ldi, log o'zgarmadi
echo 'print(' >> hello.py
git commit -am "feat: broken change"
git revert HEAD --no-edit             # yangi commit: Revert "feat: broken change"
git log --oneline -n 3
```

### O'rta 4 — Tarixni o'qing
O'z repongizda `git log --oneline --graph --all` ishga tushiring. Eng so'nggi merge commitni toping, `git show <hash>` bilan ko'ring: nechta `Merge:` (ota) hash bor? Fast-forward merge bo'lsa grafikda qanday ko'rinadi?
**Kutiladigan natija:** merge commitda 2 ota; fast-forward grafikda to'g'ri chiziq (alohida «bo'lak» yo'q).
**Yechim:** `git show` da `Merge: c39973a dba9416` ko'rinishidagi qator (2 ta hash). Fast-forward'da yangi commit yaratilmaydi, shuning uchun grafik tekis chiziq bo'lib qoladi.

### Qiyin 1 — Konflikt yarating va yeching
Ataylab konflikt hosil qiling: `README.md` ning birinchi qatorini `main` da ham, `feature/title` shoxida ham turlicha o'zgartiring, birlashtiring va yeching. Yakuniy sarlavha ikkala g'oyani birlashtirsin. `git log --oneline --graph` bilan isbotlang.
**Kutiladigan natija:** merge commit va grafikda ikki shox ko'rinadi; faylda `<<<<<<<` belgilari qolmagan (`grep '<<<<' README.md` bo'sh).
**Yechim:**
```bash
git switch -c feature/title
# README.md 1-qatorini muharrirda: "# Aziz Dev Journal"
git commit -am "docs: personal title"
git switch main
# README.md 1-qatorini muharrirda: "# Dasturchi kundaligi"
git commit -am "docs: uzbek title"
git merge feature/title          # CONFLICT
# muharrirda: "# Aziz: dasturchi kundaligi" qoldirib, belgilarni o'chiring
git add README.md
git commit --no-edit
grep '<<<<' README.md            # bo'sh bo'lishi kerak
git log --oneline --graph
```

### Qiyin 2 — Merge'ni bekor qilish
Yuqoridagi konflikt holatini yana yarating, lekin yechish o'rniga `git merge --abort` bilan to'xtating. Bundan keyin `git status` va fayl holatini tekshiring. Qachon abort, qachon yechish to'g'ri?
**Kutiladigan natija:** abortdan keyin repo merge'dan oldingi holatda, belgilar yo'q.
**Yechim:** `git merge --abort` hammasini qaytaradi: `git status` — clean. Abort — nima birlashtirayotganingiz noaniq bo'lsa yoki noto'g'ri shoxni merge qilgan bo'lsangiz; yechish — o'zgarishlarni aniq tushunib, ikkalasidan ham kerakli qismni qoldirmoqchi bo'lsangiz.

### Qiyin 3 — Hash orqali sayohat
`git log --oneline` dan eski commit hash'ini oling. 1) `git show <hash>` — nima o'zgargan? 2) `git switch --detach <hash>` bilan o'sha holatga o'ting va fayllarni ko'ring (Git «detached HEAD» deydi). 3) `git switch main` bilan qaytib keling. Detached HEAD'da commit qilsangiz nima bo'ladi (nazariy javob)?
**Kutiladigan natija:** o'quvchi tarixga xavfsiz «sayohat» qila oladi va asosiy shoxga qaytadi.
**Yechim:**
```bash
git log --oneline
git show 5284414
git switch --detach 5284414
cat hello.py
git switch main
```
Detached HEAD'da qilingan commit hech qanday shoxda emas; boshqa shoxga o'tganingizda unga havola yo'qoladi (faqat `git reflog` orqali topiladi). Saqlash uchun: `git switch -c yangi-shox`.

### Bonus — Bir qatorli alias
`git lg` nomli alias yarating, u `git log --oneline --graph --all` ni ishga tushirsin.
**Kutiladigan natija:** `git lg` buyrug'i grafik tarixni chiqaradi.
**Yechim:**
```bash
git config --global alias.lg "log --oneline --graph --all"
git lg
```

## 5. Tezkor nazorat
1. Git va GitHub o'rtasidagi farq nima? *(Git — lokal VCS dasturi; GitHub — repozitoriylarni saqlaydigan va hamkorlik qo'shadigan xizmat.)*
2. Uch zonani va ularni bog'laydigan buyruqlarni ayting. *(Working directory → `git add` → staging → `git commit` → repository.)*
3. Commit nimalardan iborat? *(Hash, muallif, vaqt, xabar, fayllar snapshot'i, parent.)*
4. Fast-forward merge va merge commit qachon bo'ladi? *(Main'da yangi commit yo'q bo'lsa — ff; ikkala shoxda yangi commit bor bo'lsa — merge commit.)*
5. Konflikt belgilari nimani bildiradi va qanday yechiladi? *(`HEAD` — hozirgi shox, `=======` dan keyin — birlashtirilayotgan; tahrirlab, belgilarni o'chirib, `add` + `commit`.)*

## 6. Uyga vazifa (20–30 daqiqa)
`uyga-vazifa.md` dagi 2-dars vazifasi. Qisqacha: `dev-journal` da `.gitignore` (kamida `.env` va `__pycache__/`) yarating; 3 kunlik yozuv uchun 3 ta commit (`notes/kun-1.md` ...); `feature/skills` shoxini ochib merge qiling; `git log --oneline --graph` natijasini `log.txt` ga saqlang (u keyingi darsda GitHub'ga yuklanadi). Eslatma: uyga-vazifa.md alohida agent tomonidan yoziladi; agar mosligi buzilsa, shu bandni moslashtiring.

## 7. Mentor uchun izohlar
- Hash'lar har kimda boshqacha: o'quvchi o'z hash'ini ishlatsin, namunadagini ko'chirmasin.
- Windows: Git Bash'da buyruqlar bir xil; PowerShell'da `printf`, `sed` farq qiladi. Matn faylni muharrirda yozdirish yengilroq.
- Konflikt tajribasida o'quvchi birinchi marta qo'rqishi mumkin: `git merge --abort` xavfsiz chiqish yo'li ekanini darrov ayting.
- Rebase, bisect, tag, reflog dasturda bor (qo'llanma 1.4-jadval), lekin bu darsda faqat tanishuv: chuqur o'tish 2-haftada (Branching, PR) va kerak bo'lsa keyin.
