# 7-dars. Git branchlar va masofaviy repozitoriylar (GitHub, Push, Pull, Merge)

**Darsning maqsadi:** O'quvchilarga Git tarmoqlari (Branches), parallel ishlab chiqish konsepsiyasi (`feature branch` workflow), branchlarni yaratish va almashtirish (`git branch`, `git switch`), birlashtirish (`git merge`), ziddiyatlar (merge conflicts) va ularni hal qilish hamda masofaviy repozitoriylar (GitHub / GitLab, `remote`, `clone`, `push`, `pull`) bilan ishlash ko'nikmalarini amaliy o'rgatish.

**Vaqt taqsimoti:**
- O'tgan mavzuni takrorlash (Git asoslari va 3 ta hudud): 10 daqiqa
- Yangi mavzu: Branching mantig'i, Fast-forward va 3-way merge, ziddiyatlarni hal qilish: 25 daqiqa
- Yangi mavzu: Masofaviy repozitoriya (Remote origin), GitHub, Push, Pull va PR: 15 daqiqa
- Amaliy mashg'ulot (Branch ochish, konflikt yuzaga keltirish, hal qilish va GitHub'ga yuklash): 25 daqiqa
- Dars xulosasi va tezkor nazorat: 5 daqiqa

---

## 1. Dars konspekti (Mentor uchun)

### 1.1. Git Branch (Tarmoq) nima?
Asosiy ishlab chiqarish kodi (Production) doimo barqaror va xatosiz bo'lishi shart. Yangi funksiya (feature) qo'shish yoki sinov o'tkazishda bevosita `main` branchda ishlash xavflidir.
- **Branch** — bu loyiha tarixidagi ma'lum bir commitga yo'naltirilgan yengil, harakatlanuvchi ko'rsatkichdir (pointer).
- Branch ochish yangi fayllarni diskda qayta nusxalamaydi — shunchaki 40 baytlik yangi havola hosil qiladi, shu sababli Git'da branch yaratish bir necha millisekund vaqt oladi.
- Standart branch nomi: `main` (eski tizimlarda `master`).

### 1.2. Branchlar bilan ishlash buyruqlari
1. `git branch` — barcha mavjud branchlar ro'yxatini ko'rsatadi (joriy branch yashil rangda va `*` bilan belgilanadi).
2. `git branch [nom]` — yangi branch yaratish (masalan: `git branch feature-login`).
3. `git switch [nom]` yoki `git checkout [nom]` — boshqa branchga o'tish.
4. `git switch -c [nom]` yoki `git checkout -b [nom]` — yangi branch yaratib, darhol unga o'tish (eng ko'p ishlatiladigan qisqa buyruq!).
5. `git branch -d [nom]` — birlashtirib bo'lingan branchni xavfsiz o'chirish.
6. `git branch -D [nom]` — birlashtirilmagan bo'lsa ham majburiy o'chirish.

### 1.3. Branchlarni birlashtirish (Merge)
Ish tugallangach, yangi branchni asosiy `main` ga qo'shish lozim:
1. Avval qabul qiluvchi branchga o'tiladi: `git switch main`.
2. Birlashtirish buyrug'i beriladi: `git merge feature-login`.
- **Fast-forward merge**: Agar `main` branchda siz ajralib chiqqaningizdan beri yangi kommitlar bo'lmagan bo'lsa, Git shunchaki `main` ko'rsatkichini eng oldingi commitga siljitib qo'yadi.
- **3-way merge**: Agar siz o'z branchedingizda ishlayotganingizda, `main` da ham boshqalar yangi commitlar qilgan bo'lsa, Git ikkala yo'lni birlashtiruvchi maxsus «Merge commit» yaratadi.

### 1.4. Merge Conflicts (Mojarolar) va ularni hal qilish
Agar ikkita turli branchda bir xil faylning aynan bir xil qatorlari har xil qilib o'zgartirilsa, Git qaysi birini saqlab qolishni o'zi hal qila olmaydi va jarayonni to'xtatadi: `CONFLICT (content): Merge conflict in ...`
Fayl ichida Git quyidagi maxsus belgilarni qoldiradi:
```
<<<<<<< HEAD
<h1>Bizning Asosiy Sayt</h1>
=======
<h1>Bizning Yangi Zamonaviy Sayt</h1>
>>>>>>> feature-login
```
- `<<<<<<< HEAD` dan `=======` gacha — joriy branchdagi kod.
- `=======` dan `>>>>>>>` gacha — qo'shilayotgan branchdagi kod.
- **Yechish algoritmi**: Faylni qo'lda ochib, kerakli kodni qoldirish, belgilarni (`<<<`, `===`, `>>>`) o'chirib tashlash, so'ngra `git add [fayl]` va `git commit` qilish.

### 1.5. Masofaviy repozitoriyalar (Remote: GitHub / GitLab)
Jamoada kod almashish uchun markaziy bulut serveri ishlatiladi:
1. `git remote add origin https://github.com/user/repo.git` — lokal repozitoriyaga masofaviy server manzilini bog'lash (`origin` — standart nom).
2. `git remote -v` — bog'langan masofaviy manzillarni ko'rish.
3. `git push -u origin main` — lokal kommitlarni masofaviy GitHub serveriga yuklash (`-u` upstream bog'lanishini o'rnatadi).
4. `git pull` — GitHub'dagi eng yangi kommitlarni o'z kompyuteringizga yuklab olib, darhol lokal branchga birlashtirish (`git fetch` + `git merge`).
5. `git clone [url]` — masofaviy GitHub repozitoriyasining to'liq nusxasini o'z kompyuteringizga ko'chirib olish.

---

## 2. Amaliy topshiriqlar va yechimlari (Mentor uchun)

### 1-topshiriq. Yangi branch ochish va alohida commit qilish
`my_website` repozitoriyasida `feature-contact` nomli yangi branch oching, unga o'ting, `contact.html` faylini yarating va commit qiling.

**Yechim:**
```bash
# 1. Yangi branch yaratib unga o'tish
git switch -c feature-contact

# 2. Yangi fayl yaratish
echo "<p>Aloqa: info@devops.uz</p>" > contact.html

# 3. Qo'shish va commit qilish
git add contact.html
git commit -m "feat: contact sahifasi qo'shildi"

# 4. Branchlarni ko'rish
git branch
# * feature-contact
#   main
```

### 2-topshiriq. Fast-forward merge amaliyoti
Asosiy `main` branchga qayting va `feature-contact` branchini `main` ga birlashtiring (`merge`), so'ngra eskirgan branchni o'chirib tashlang.

**Yechim:**
```bash
# 1. Asosiy branchga qaytish
git switch main

# 2. Birlashtirish
git merge feature-contact
# Natija: Fast-forward ... 1 file changed, 1 insertion(+)

# 3. Birlashtirilgan branchni o'chirish
git branch -d feature-contact
```

### 3-topshiriq. Merge konfliktini yuzaga keltirish va bartaraf etish
`main` branchda `header.txt` faylining 1-qatoriga «Version 1.0» deb yozib commit qiling. So'ngra yangi `test-branch` ochib, xuddi shu qatorni «Version 2.0-beta» deb o'zgartirib commit qiling. `main` ga qaytib, `test-branch` ni merge qilishga urining va konfliktni hal qiling.

**Yechim:**
```bash
# 1. Main branchda fayl yaratish va commit
echo "Version 1.0" > header.txt
git add header.txt
git commit -m "chore: header versiya 1.0"

# 2. Yangi branch ochib o'zgartirish
git switch -c test-branch
echo "Version 2.0-beta" > header.txt
git add header.txt
git commit -m "chore: header versiya 2.0-beta"

# 3. Main branchda ham boshqa matn yozish
git switch main
echo "Version 1.1-release" > header.txt
git add header.txt
git commit -m "chore: header versiya 1.1-release"

# 4. Birlashtirishga urinish
git merge test-branch
# Natija: CONFLICT (content): Merge conflict in header.txt

# 5. Faylni tahrirlab to'g'irlash (masalan nano bilan)
# Fayl ichini "Version 2.0-final" qilib to'g'rilaymiz
echo "Version 2.0-final" > header.txt

# 6. Mojaroni hal qilib commit qilish
git add header.txt
git commit -m "fix: merge konflikti bartaraf etildi"
```

### 4-topshiriq. Masofaviy repozitoriy ulanishini tekshirish
Lokal repozitoriyaga test masofaviy URL manzilini biriktiring va `git remote -v` orqali tekshiring.

**Yechim:**
```bash
git remote add origin https://github.com/myuser/my_website.git
git remote -v
# origin  https://github.com/myuser/my_website.git (fetch)
# origin  https://github.com/myuser/my_website.git (push)
```

---

## 3. Tezkor nazorat savollari (Dars yakuni)

1. **Nima uchun dasturchilar to'g'ridan-to'g'ri `main` branchda ishlamasliklari kerak?**
   *Javob:* `main` branch doimo ishchi va barqaror bo'lishi shart. Yangi tajribalar yoki funksiyalar alohida tarmoqlarda (`feature branches`) sinovdan o'tkazilib, faqat tekshirilgach `main` ga qo'shiladi.
2. **Fast-forward merge qanday vaziyatda sodir bo'ladi?**
   *Javob:* Agar asosiy branchda yangi branch ajralib chiqqanidan beri hech qanday yangi commitlar amalga oshirilmagan bo'lsa.
3. **Merge conflict nima sababdan kelib chiqadi?**
   *Javob:* Bir vaqtning o'zida ikkita turli branchda bitta faylning aynan bir xil qatorlariga turlicha o'zgartirishlar kiritilganda.
4. **`git push` bilan `git pull` ning vazifalari qanday farq qiladi?**
   *Javob:* `git push` lokal kommitlarni masofaviy GitHub serveriga yuboradi, `git pull` esa masofaviy serverdagi eng yangi o'zgarishlarni lokal kompyuterga yuklab olib birlashtiradi.
