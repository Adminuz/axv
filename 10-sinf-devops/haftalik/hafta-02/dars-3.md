# 6-dars. Git va versiya boshqaruvi tizimlariga kirish (Git asoslari)

**Darsning maqsadi:** O'quvchilarga versiya boshqaruvi tizimlari (VCS) tushunchasi, taqsimlangan arxitektura (Distributed VCS), Git'ning 3 ta asosiy ishchi hududi (Working Directory, Staging Area, Git Repository), boshlang'ich sozlash (`git config`), repozitoriya ochish (`git init`), o'zgarishlarni qayd etish (`status`, `add`, `commit`, `log`) hamda `.gitignore` fayli orqali keraksiz fayllarni chetlab o'tishni amaliy o'rgatish.

**Vaqt taqsimoti:**
- O'tgan darsni takrorlash (Disklar va paket menejerlari): 10 daqiqa
- Yangi mavzu: VCS tushunchasi, Git 3 ta hududi va kommitlar anatomiyasi: 25 daqiqa
- Yangi mavzu: Git asosiy buyruqlari zanjiri va .gitignore qoidalari: 15 daqiqa
- Amaliy mashg'ulot (Git repozitoriyasini ochish, kommitlar qilish va loglarni tahlil qilish): 25 daqiqa
- Dars xulosasi va tezkor nazorat: 5 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. Versiya boshqaruvi tizimi (VCS) nima?
Dasturlashda ko'pchilik boshlovchilar loyiha nusxalarini `project_final.zip`, `project_final_v2.zip`, `project_oxirgi_variant.zip` deb saqlashadi. Bu usul chalkashlik, kod yo'qolishi va jamoada parallel ishlashning imkonsizligiga olib keladi.
- **VCS (Version Control System)** — loyihadagi har bir faylga kiritilgan o'zgarishlar tarixini (kim, qachon, nima o'zgartirdi) avtomatik va aniq yozib boruvchi maxsus tizimdir.
- **Markazlashgan (Centralized - SVN, CVS)** vs **Taqsimlangan (Distributed - Git)**:
  - SVN da markaziy server o'chib qolsa, hech kim ishlay olmaydi.
  - Git'da har bir dasturchining kompyuterida butun loyihaning to'liq tarixi (lokal repozitoriya) mavjud bo'ladi. Internet bo'lmaganda ham bemalol kommitlar qilish mumkin.

### 1.2. Git'ning 3 ta asosiy hududi (The Three States)
Git fayllarni uchta mantiqiy bosqichda boshqaradi:
1. **Working Directory (Ishchi katalog)**: Diskda ko'rib turgan, tahrirlayotgan oddiy fayllaringiz.
2. **Staging Area / Index (Tayyorgarlik maydoni)**: Keyingi saqlanishi (commit) rejalashtirilgan o'zgarishlar ro'yxati. `git add` orqali fayllar shu yerga o'tadi.
3. **Git Repository (Mahalliy ombor - `.git`)**: Loyihaning butun tarixi, ob'yektlari va commitlari siqilgan holda saqlanadigan ma'lumotlar bazasi. `git commit` orqali ma'lumotlar bu yerga muhrlanadi.

### 1.3. Git konfiguratsiyasi (Birinchi sozlash)
Git'ni o'rnatgach, har bir commit kim tomonidan qilinganini bilish uchun foydalanuvchi ma'lumotlari kiritiladi:
```bash
git config --global user.name "Ali Valiyev"
git config --global user.email "ali@example.com"
git config --global init.defaultBranch main
```
Sozlamalarni tekshirish: `git config --list`.

### 1.4. Asosiy ish oqimi (Git Workflow)
1. `git init` — joriy katalogda yangi bo'sh Git repozitoriyasini yaratadi (yashirin `.git` papkasi hosil bo'ladi).
2. `git status` — loyihaning hozirgi holatini ko'rsatadi (qaysi fayllar o'zgargan, qaysi biri kuzatuvda emas — untracked).
3. `git add [fayl]` — o'zgarishlarni Staging Area'ga qo'shish:
   - `git add index.html` — bitta faylni tayyorlash.
   - `git add .` — barcha o'zgargan fayllarni birvarakayiga tayyorlash.
4. `git commit -m "[izoh]"` — tayyorlangan o'zgarishlarni Git tarixiga bir zumlik fotosurat (snapshot) sifatida yozish.
   - Har bir commit o'zining noyob **SHA-1 hash** kodiga (masalan: `c3b2f1a...`), muallifiga, sanasiga va aniq izohiga ega bo'ladi.
5. `git log` — barcha amalga oshirilgan commitlar tarixini ko'rish:
   - `git log --oneline` — har bir commitni bir qatorda ixcham ko'rsatish.
6. `git diff` — fayllarda aynan qaysi qatorlar o'zgarganini (yashil `+` va qizil `-`) ko'rsatish.

### 1.5. `.gitignore` faylining vazifasi
Loyihada Git tarixiga kirishi kerak bo'lmagan fayllar bo'ladi:
- Maxfiy parollar va kalitlar (`.env`, `private.pem`).
- Katta kutubxonalar (`node_modules/`, `venv/`).
- Kompilyatsiya natijalari va loglar (`*.log`, `dist/`, `build/`).
Loyiha ildizida `.gitignore` nomli matn fayli ochiladi va uning ichiga e'tibor berilmasligi kerak bo'lgan andozalar yoziladi:
```
# Loglar va muhit fayllari
*.log
.env
node_modules/
```

---

## 2. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. Git boshlang'ich sozlamalarini kiritish
O'z ismingiz, elektron pochtangizni Git sozlamalariga kiriting va `git config --list` orqali ularni tekshiring.

**Yechim:**
```bash
git config --global user.name "DevOps O'quvchi"
git config --global user.email "student@devops.uz"
git config --global init.defaultBranch main

# Tekshirish
git config --list | grep user
```

### 2-topshiriq. Yangi repozitoriya ochish va birinchi commit
`my_website` papkasini oching, uni Git repozitoriyasiga aylantiring (`git init`), ichida `index.html` faylini yaratib, uni «feat: dastlabki index.html yaratildi» izohi bilan commit qiling.

**Yechim:**
```bash
# 1. Papka ochish va repozitoriya yaratish
mkdir my_website && cd my_website
git init

# 2. Fayl yaratish
echo "<h1>Mening birinchi saytim</h1>" > index.html

# 3. Holatni ko'rish
git status
# Natija: Untracked files: index.html

# 4. Staging area ga qo'shish va commit qilish
git add index.html
git commit -m "feat: dastlabki index.html yaratildi"

# 5. Tarixni tekshirish
git log --oneline
```

### 3-topshiriq. Faylga o'zgartirish kiritish va diff tahlili
`index.html` fayliga yangi `<p>DevOps kurslari</p>` qatorini qo'shing. `git diff` orqali o'zgarishlarni ko'ring va yangi commit amalga oshiring.

**Yechim:**
```bash
# 1. Matn qo'shish
echo "<p>DevOps kurslari</p>" >> index.html

# 2. Farqni ko'rish
git diff

# 3. Commit qilish
git add index.html
git commit -m "docs: kurslar haqida ma'lumot qo'shildi"

# 4. Loglarni ko'rish
git log --oneline
```

### 4-topshiriq. `.gitignore` faylini sozlash
Loyihangizda `server.log` va `.env` fayllarini yarating. Ularni Git e'tiborsiz qoldirishi uchun `.gitignore` fayliga kiriting va `git status` da ular chiqmayotganini tasdiqlang.

**Yechim:**
```bash
# 1. Maxfiy va log fayllarni yaratish
touch server.log .env

# 2. .gitignore yaratish
echo "*.log" >> .gitignore
echo ".env" >> .gitignore

# 3. Tekshirish
git status
# Natijada server.log va .env ko'rinmaydi, faqat .gitignore ko'rinadi!

# 4. .gitignore faylini commit qilish
git add .gitignore
git commit -m "chore: .gitignore sozlandi"
```

---

## 3. Tezkor nazorat savollari (Dars yakuni)

1. **Markazlashgan VCS (SVN) bilan Taqsimlangan VCS (Git) ning asosiy farqi nimada?**
   *Javob:* Git'da har bir ishlab chiquvchining kompyuterida loyihaning to'liq tarixi mavjud bo'ladi, internet bo'lmaganda ham mahalliy kommitlar qilish mumkin.
2. **Git'dagi 3 ta asosiy hudud qaysilar?**
   *Javob:* Working Directory (ishchi papka), Staging Area (tayyorgarlik maydoni) va Git Repository (`.git` ombori).
3. **`git add` buyrug'ining vazifasi nima?**
   *Javob:* O'zgartirilgan fayllarni Staging Area'ga (keyingi commit uchun tayyorgarlik ro'yxatiga) o'tkazish.
4. **`.gitignore` fayli nima uchun kerak?**
   *Javob:* Maxfiy kalitlar, vaqtinchalik loglar va yirik kutubxonalar kabi Git omboriga tushishi kerak bo'lmagan fayllarni kuzatuvdan chetlatish uchun.
