# 15-dars. Git va GitHub bilan tanishuv (2-qism): kompyuterda Git — init, status, add, commit, log

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** amaliyot (laboratoriya ishi) · **II-bob**, 9-dars (hafta ichida 3-dars)

> Manba: o'quv dasturi, 12-mavzu «Git va GitHub bilan tanishuv»: «Repository, commit, branch va README fayllari bilan ishlash... Git asosiy buyruqlari: init, add, commit, status, log, clone, push, pull.» Baholashda — «GitHub laboratoriya ishlari». Bu dars — mavzuning 2-qismi: Git'ni o'rnatish va lokal ish jarayoni (`init`, `status`, `add`, `commit`, `log`). `git config` va «uch hudud» (ishchi papka, staging, repository) — buyruqlarni to'g'ri ishlatish uchun zarur qo'shimcha tushunchalar (Git rasmiy hujjatlari asosida). `clone`, `push`, `pull` va `branch` — 16–17-darslarda.

## 1. Dars rejasi

**Maqsad:** o'quvchilar Git'ni kompyuterga o'rnatish va sozlash (`git --version`, `git config`) tartibini biladi; terminalda papkani repository'ga aylantiradi (`git init`), fayllar holatini tekshiradi (`git status`), o'zgarishlarni tayyorlaydi (`git add`) va saqlaydi (`git commit -m`), tarixni ko'radi (`git log`); «ishchi papka → staging → repository» yo'lini tushunadi.

**Kutiladigan natija:**
- Git o'rnatilganini `git --version` bilan tekshiradi; `user.name` va `user.email` ni sozlaydi.
- `git init` dan keyin yashirin `.git` papkasi paydo bo'lishini va uning vazifasini aytadi.
- `git status` natijasidagi «untracked», «modified», «staged» holatlarini o'qiydi.
- `git add` va `git commit -m "..."` bilan kamida 3 ta commit qiladi.
- `git log` va `git log --oneline` natijasidan commit ID, muallif, sana va xabarni topadi.
- Uch hudud sxemasini chizib, har bir buyruq faylni qayerdan qayerga ko'chirishini ko'rsatadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–8 daq | Takrorlash | Git va GitHub farqi, repo, commit, README |
| 8–28 daq | Yangi mavzu | Terminal, o'rnatish va sozlash, uch hudud, 5 ta buyruq |
| 28–33 daq | Tanaffus | Harakatli tanaffus |
| 33–68 daq | Laboratoriya ishi | «Kundalik» loyihasi: init → 3 ta commit → log |
| 68–75 daq | Tezkor nazorat | 5 ta savol |
| 75–80 daq | Xulosa va uyga vazifa | Keyingi hafta: GitHub'ga push, clone, pull, branch |

---

## 2. Dars konspekti

### 2.1. Takrorlash (8 daqiqa)
- Git — qayerda ishlaydi? GitHub-chi?
- Commit'da qanday ma'lumot bor? (xabar, muallif, vaqt, ID)
- O'tgan darsda commitni sayt orqali qildik. Bugun — o'z kompyuterimizda, internetsiz.

### 2.2. Terminal va Git'ni o'rnatish
- **Terminal** — kompyuterga matnli buyruq beradigan oyna. Windows'da Git bilan birga **Git Bash** o'rnatiladi.
- O'rnatish: **git-scm.com** → Download → standart sozlamalar bilan Next.
- Tekshirish:
```bash
git --version
# git version 2.4x.x  — raqam boshqacha bo'lishi mumkin
```
- Kerakli terminal buyruqlari: `pwd` (qayerdaman), `ls` (papkada nima bor), `cd papka` (papkaga kirish), `mkdir papka` (papka yaratish).

### 2.3. Bir martalik sozlash
Git har bir commitga muallif ismini va emailini yozadi:
```bash
git config --global user.name "Alisher Karimov"
git config --global user.email "alisher@example.com"
git config --list          # sozlamalarni ko'rish
```
Email — GitHub akkauntidagi email bilan bir xil bo'lsa, commitlar profilingizga bog'lanadi.

### 2.4. Uch hudud
| Hudud | Nima | O'xshatish |
|---|---|---|
| **Ishchi papka** (working directory) | fayllarni tahrirlayotgan papkangiz | stol ustidagi qog'ozlar |
| **Staging** (tayyorlash hududi) | keyingi commitga kiradigan o'zgarishlar | konvertga solingan qog'ozlar |
| **Repository** (`.git`) | saqlangan commitlar tarixi | pochta qutisiga tashlangan konvert |

`git add` — ishchi papkadan staging'ga; `git commit` — staging'dan repository'ga.

### 2.5. Beshta buyruq

| Buyruq | Vazifasi |
|---|---|
| `git init` | joriy papkani repository'ga aylantiradi (yashirin `.git` papkasi yaratiladi) |
| `git status` | fayllar holati: yangi (untracked), o'zgargan (modified), tayyor (staged) |
| `git add fayl` | faylni staging'ga qo'shadi; `git add .` — barcha o'zgarishlarni |
| `git commit -m "xabar"` | staging'dagi o'zgarishlarni commit sifatida saqlaydi |
| `git log` | commitlar tarixi; `git log --oneline` — har commit bir qatorda |

### 2.6. To'liq ish jarayoni
```bash
mkdir kundalik            # papka yaratish
cd kundalik               # papkaga kirish
git init                  # repository'ga aylantirish
# README.md faylini yaratib, ichiga yozamiz
git status                # README.md — untracked (qizil)
git add README.md         # staging'ga
git status                # Changes to be committed (yashil)
git commit -m "README qo'shildi"
git log --oneline         # a1b2c3d README qo'shildi
```
Keyin faylni o'zgartirsak: `git status` → **modified** → `git add` → `git commit -m "..."`.

### 2.7. `git status` ni o'qish
- `Untracked files` — Git bu faylni hali kuzatmayapti (yangi fayl).
- `Changes not staged for commit` — fayl o'zgargan, lekin `add` qilinmagan.
- `Changes to be committed` — staging'da, commitga tayyor.
- `nothing to commit, working tree clean` — hammasi saqlangan.

### 2.8. Odatiy xatolar
- `git commit` dan oldin `git add` ni unutish — «nothing added to commit».
- `-m` siz `git commit` — matn muharriri (Vim) ochiladi; chiqish: `Esc`, keyin `:wq` va Enter.
- `git init` ni noto'g'ri papkada (masalan, butun «Hujjatlar»da) bajarish — `pwd` bilan tekshiring.
- `git config` qilinmagan — Git commit qilishga ruxsat bermaydi va ism so'raydi.
- Buyruqni katta harf bilan yozish: `Git Status` — ishlamaydi.

---

## 3. Amaliy mashg'ulotlar (laboratoriya ishi)

> Har bir o'quvchi o'z kompyuterida ishlaydi. Git o'rnatilmagan bo'lsa — mentor ekranida birga bajariladi yoki brauzerdagi Git mashq trenajyorlaridan foydalaniladi; terminal natijalari daftarga yoziladi.

### 1-mashq (oson). Tekshirish va sozlash
**Vazifa:** `git --version` bilan Git'ni tekshiring, `user.name` va `user.email` ni sozlang, `git config --list` bilan ko'ring.

**Yechim:**
```bash
git --version
git config --global user.name "Ism Familiya"
git config --global user.email "email@example.com"
git config --list
```
Natijada `user.name=...` va `user.email=...` qatorlari ko'rinadi.

### 2-mashq (oson). Buyruq va vazifa
**Vazifa:** Buyruqlarni vazifasi bilan juftlang: `init`, `status`, `add`, `commit`, `log` — (a) tarixni ko'rsatadi; (b) staging'ga qo'shadi; (c) repository yaratadi; (d) holatni ko'rsatadi; (e) saqlaydi.

**Yechim:** init — (c); status — (d); add — (b); commit — (e); log — (a).

### 3-mashq (o'rta). «Kundalik» repository'si
**Vazifa:** `kundalik` papkasini yarating, `git init` qiling, `README.md` ga «# Mening kundaligim» yozing va birinchi commitni qiling. Har qadamdan keyin `git status` natijasini daftarga yozing.

**Yechim:**
```bash
mkdir kundalik && cd kundalik
git init                       # Initialized empty Git repository in .../kundalik/.git/
echo "# Mening kundaligim" > README.md
git status                     # Untracked files: README.md
git add README.md
git status                     # Changes to be committed: new file: README.md
git commit -m "README qo'shildi"
git status                     # nothing to commit, working tree clean
```

### 4-mashq (qiyin). Uch commit va tarix
**Vazifa:** `kundalik` ga yana 2 ta commit qo'shing: (1) `dushanba.txt` fayli; (2) README'ga yangi qator. `git log --oneline` natijasini yozing va eng birinchi commit ID'sini toping.

**Yechim:**
```bash
echo "Bugun Git o'rgandim" > dushanba.txt
git add dushanba.txt
git commit -m "Dushanba yozuvi qo'shildi"
echo "Muallif: Alisher" >> README.md
git status                     # modified: README.md
git add .
git commit -m "README ga muallif qo'shildi"
git log --oneline
# c3d4e5f README ga muallif qo'shildi
# b2c3d4e Dushanba yozuvi qo'shildi
# a1b2c3d README qo'shildi       ← eng birinchisi (pastda)
```
`git log` da eng yangi commit **yuqorida**, eng eskisi **pastda**.

### 5-mashq (bonus). Uch hudud sxemasi
**Vazifa:** Ishchi papka, staging va repository'ni 3 ta quti qilib chizing va `git add`, `git commit` strelkalarini qo'ying. `git status` har bir holatda nima deyishini yozing.

**Yechim:** Ishchi papka →(`git add`)→ Staging →(`git commit`)→ Repository. Status: ishchi papkada yangi fayl — «Untracked»; o'zgargan fayl — «Changes not staged»; staging'da — «Changes to be committed»; hammasi commit qilingan — «working tree clean».

---

## 4. Tezkor savollar (Checklist)

1. `git init` nima qiladi?
   - **Javob:** Joriy papkani Git repository'siga aylantiradi va yashirin `.git` papkasini yaratadi.
2. `git add` va `git commit` farqi?
   - **Javob:** `add` — o'zgarishni staging'ga tayyorlaydi; `commit` — staging'dagi o'zgarishlarni tarixga saqlaydi.
3. `git status` «Untracked files» desa, bu nimani bildiradi?
   - **Javob:** Fayl yangi, Git uni hali kuzatmayapti — `git add` kerak.
4. Commitda muallif ismi qayerdan olinadi?
   - **Javob:** `git config --global user.name` va `user.email` sozlamalaridan.
5. `git log --oneline` nima ko'rsatadi?
   - **Javob:** Har bir commitni bir qatorda: qisqa ID va xabar; eng yangisi yuqorida.

## 5. Kuchli o'quvchi uchun qo'shimcha

- `git diff` buyrug'i bilan commitdan oldin faylda aynan nima o'zgarganini ko'ring (yashil — qo'shilgan, qizil — o'chirilgan qatorlar).
- `.gitignore` fayli yaratib, unga `*.tmp` yozing va `test.tmp` fayli `git status` da ko'rinmasligini tekshiring.

## 6. Mentor uchun eslatmalar

- Darsdan oldin barcha kompyuterlarda Git o'rnatilganini va Git Bash ishga tushishini tekshiring; aks holda o'rnatishga 15–20 daqiqa ketadi.
- Windows'da `echo ... > fayl` Git Bash'da ishlaydi; oddiy CMD'da farq qilishi mumkin — darsda faqat Git Bash'dan foydalaning yoki fayllarni Notepad'da yarating.
- `.git` papkasi yashirin — Explorer'da «Yashirin elementlar» ni yoqib ko'rsating va uni **o'chirmaslik** kerakligini tushuntiring (butun tarix o'chadi).
- `git commit` dagi Vim tuzog'iga tushganlar uchun doskaga `Esc` → `:wq` → Enter yozib qo'ying.
- Laboratoriya ishi natijasi — `git log --oneline` skrinshoti yoki daftardagi yozuvi; 16-darsda shu `kundalik` repository'si GitHub'ga push qilinadi, shuning uchun papkani saqlab qo'ying.
