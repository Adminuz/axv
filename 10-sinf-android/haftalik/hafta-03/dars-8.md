# 8-dars: Git bilan ishlash amaliyoti (Tarmoqlar va Konfliktlar)

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta, 2-dars (umumiy 8-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga Git tizimida tarmoqlar (**Branches**) bilan ishlash falsafasi va afzalliklarini tushuntirish, asosiy kodni buzmasdan parallel rivojlanish uchun yangi tarmoq ochish (`git branch`, `git checkout -b` / `git switch -c`), o'zgarishlarni satr darajasida taqqoslash (`git diff`), tarmoqlarni birlashtirish (**Merge**) hamda jamoaviy ishlashda eng ko'p uchraydigan to'qnashuvlarni (**Merge Conflicts**) qo'lda xatosiz hal qilish, shuningdek, o'zgarishlarni vaqtinchalik saqlash (`git stash`) va xatoliklarni bekor qilish (`git revert`, `git reset`) amaliy ko'nikmalarini chuqur shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Tarmoqlanish (Branching) tushunchasini va uning asosiy kod bazasini (`main`) barqaror saqlashdagi rolini tushunish;
- Yangi branch ochish, branchlar orasida o'tish (`git checkout`, `git switch`) va keraksiz tarmoqlarni o'chirish (`git branch -d`) buyruqlarini bilish;
- `git diff` buyrug'i orqali qaysi satrlar qo'shilgan (`+`) yoki o'chirilganini (`-`) tahlil qila olish;
- Fast-forward va 3-way merge tushunchalarini farqlash;
- Merge Conflict (to'qnashuv) nima sababdan kelib chiqishini bilish, `<<<<<<< HEAD`, `=======`, `>>>>>>>` belgilarini tushunish va ziddiyatni qo'lda hal qilib commit qila olish;
- `git stash` yordamida chala kodlarni saqlab turish hamda `git revert` orqali xato commitlarni xavfsiz bekor qilishni amalda qo'llay olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Git o'rnatilgan tizim (Git Bash, macOS/Linux Terminal);
- Android Studio yoki VS Code kod muharriri;
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | `git init`, 3 ta maydon, commit va `.gitignore` bo'yicha savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | Tarmoqlar falsafasi, `git diff`, `git merge`, Merge Conflict kelib chiqish sabablari va `git stash` |
| **30–55 min** | Amaliy mashg'ulot (Terminalda) | Yangi branch ochish, mustaqil o'zgarish kiritish, main bilan merge qilish |
| **55–75 min** | Amaliy laboratoriya (Konfliktni hal qilish) | Sun'iy merge conflict hosil qilish va uni qo'lda tahrirlab muvaffaqiyatli commit qilish |
| **75–80 min** | Xulosa va baholash | Tezkor savol-javob, dars xulosalari va uyga vazifa |

---

## Nazariy qism (Batafsil tushuntirish)

### 1. Tarmoqlar (Branches) nima va nima uchun kerak?

Tasavvur qiling, siz do'kon ilovasida ishlab turgan to'lov tizimiga egasiz. Siz ilovaga yangi "Bonus ballari" funksiyasini qo'shmoqchisiz. Agar siz bevosita `main` (asosiy) tarmoqda kod yozishni boshlasangiz va hali chala bo'lgan kod tufayli ilova buzilsa, butun jamoaning ishi to'xtab qoladi yoki foydalanuvchilar buzilgan ilovaga duch keladi.

Git bu muammoni **Tarmoqlar (Branches)** orqali hal qiladi.
- Branch — bu asosiy loyihadan ajralib chiquvchi "parallel olam".
- Siz yangi tarmoqda xohlagan tajribangizni o'tkazishingiz, kod yozishingiz, commitlar qilishingiz mumkin. Bu vaqtda `main` tarmog'i 100% tinch va barqaror turadi.
- Funksiya to'liq tayyor bo'lib, sinovdan o'tgach, uni asosiy tarmoqqa birlashtirasiz (**Merge**).

---

### 2. Branch buyruqlari

#### Mavjud branchlarni ko'rish:
```bash
git branch
```
(Yulduzcha va yashil rang joriy faol branch'ni ko'rsatadi).

#### Yangi branch yaratish va unga o'tish:
```bash
# Eski usul:
git checkout -b feature-bonus

# Zamonaviy qulay usul (Git 2.23+):
git switch -c feature-bonus
```

#### Branchlar orasida o'tish:
```bash
git switch main
# yoki
git checkout main
```

#### Ishlatib bo'lingan branchni o'chirish:
```bash
git branch -d feature-bonus
```

---

### 3. O'zgarishlarni taqqoslash: `git diff`

Faylda aynan qaysi satrlar qo'shilgan yoki o'chirilganini commit qilishdan oldin ko'rish dasturchi uchun juda muhim:
```bash
git diff
```
Terminalda:
- **Yashil rang va `+` belgisi:** Yangi qo'shilgan satrlar;
- **Qizil rang va `-` belgisi:** O'chirilgan yoki almashtirilgan eski satrlar.

Ikkita branch orasidagi farqni ko'rish:
```bash
git diff main feature-bonus
```

---

### 4. Birlashtirish (Merge) va To'qnashuvlar (Merge Conflicts)

Ish tugagach, o'zgarishlarni asosiy tarmoqqa qo'shish uchun:
1. Avvalo `main` tarmog'iga o'tiladi: `git switch main`
2. Birlashtirish buyrug'i beriladi: `git merge feature-bonus`

#### Merge Conflict (To'qnashuv) qachon yuzaga keladi?
Agar ikkita turli tarmoqda ayni bir faylning **bir xil satri** ikki xil o'zgartirilgan bo'lsa, Git qaysi variant to'g'ri ekanini o'zi mustaqil hal qila olmaydi va jarayonni to'xtatadi:
```text
CONFLICT (content): Merge conflict in MainActivity.kt
Automatic merge failed; fix conflicts and then commit the result.
```

Git fayl ichiga maxsus ajratuvchi belgilarni yozib qo'yadi:
```kotlin
<<<<<<< HEAD
val appTitle = "Xorazmiy E-Commerce (Main versiya)"
=======
val appTitle = "Xorazmiy Smart Shop (Bonus versiya)"
>>>>>>> feature-bonus
```
- `<<<<<<< HEAD` dan `=======` gacha: Joriy branch'dagi (masalan, `main`) kod.
- `=======` dan `>>>>>>> feature-bonus` gacha: Qo'shilayotgan branch'dagi kod.

#### Konfliktni hal qilish tartibi:
1. Faylni Android Studio yoki VS Code'da ochish;
2. Kerakli to'g'ri satrni qoldirib, qolgan keraksiz variantni va Git ajratuvchi belgilarini (`<<<<<<<`, `=======`, `>>>>>>>`) o'chirib tashlash;
3. Faylni saqlash;
4. `git add MainActivity.kt` buyrug'i orqali sahnaga olish;
5. `git commit -m "merge: to'qnashuv bartaraf etildi va tarmoqlar birlashtirildi"` orqali merge'ni yakunlash.

---

### 5. `git stash` va xatolarni bekor qilish

#### Chala ishlarni vaqtinchalik yashirish: `git stash`
Aytaylik, siz `feature-bonus` ustida ishlayapsiz, lekin shoshilinch ravishda `main` dagi jiddiy xatoni tuzatishingiz kerak. Hali commit qilishga tayyor bo'lmagan chala kodni vaqtinchalik "xaltaga" solib qo'yish uchun:
```bash
git stash              # Chala o'zgarishlarni yashirish
git switch main        # Asosiy tarmoqqa o'tib xatoni to'g'irlash
git switch feature-bonus
git stash pop          # Yashirilgan o'zgarishlarni qaytarib chiqarish
```

#### Xato commitni bekor qilish: `git revert`
Agar allaqachon commit qilib bo'lingan bo'lsa va uni bekor qilish kerak bo'lsa, tarixni buzmasdan, o'sha commitga qarama-qarshi yangi commit yaratiladi:
```bash
git revert <commit-hash>
```

---

## Amaliy topshiriqlar (Sinfda bajarish uchun)

### 1-topshiriq: Yangi branch yaratish va o'zgarish kiritish

**Vazifa:** `AndroidNotes` loyihasida `feature-notes-search` nomli yangi branch oching. Unda `SearchManager.kt` faylini yarating, ichiga oddiy qidiruv funksiyasini yozing va commit qiling. So'ng `main` branch'ga qaytib, fayl yo'qolib qolganini tahlil qiling.

**Yechim:**
```bash
# 1. Yangi branch ochamiz va unga o'tamiz
git switch -c feature-notes-search

# 2. Yangi fayl yaratamiz
echo "class SearchManager { fun search(q: String) = true }" > SearchManager.kt

# 3. Commit qilamiz
git add SearchManager.kt
git commit -m "feat: eslatmalarni qidirish moduli yaratildi"

# 4. Asosiy tarmoqqa qaytamiz
git switch main

# 5. Papkani tekshiramiz (SearchManager.kt ko'rinmaydi, chunki u boshqa tarmoqda)
ls
```

---

### 2-topshiriq: Fast-forward merge jarayonini amalga oshirish

**Vazifa:** 1-topshiriqda yaratilgan `feature-notes-search` tarmog'ini `main` tarmog'iga birlashtiring va endi `SearchManager.kt` fayli `main` ga ham qo'shilganini tekshiring. So'ngra ortiqcha branchni o'chiring.

**Yechim:**
```bash
# 1. Hozir main tarmog'ida ekanimizga ishonch hosil qilamiz
git branch

# 2. feature-notes-search tarmog'ini main'ga birlashtiramiz
git merge feature-notes-search

# 3. Fayllar ro'yxatini ko'ramiz (SearchManager.kt endi main'da ham bor)
ls

# 4. Vazifani bajargan branchni o'chirib tashlaymiz
git branch -d feature-notes-search
```

---

### 3-topshiriq: Sun'iy to'qnashuv (Merge Conflict) hosil qilish va uni hal etish

**Vazifa:**
1. `main` tarmog'ida `Settings.kt` faylini ochib, ichiga `val THEME = "LIGHT"` deb yozing va commit qiling.
2. `dark-mode` nomli yangi branch oching va shu fayldagi satrni `val THEME = "DARK"` ga o'zgartirib commit qiling.
3. `main` ga qaytib, o'sha satrni `val THEME = "SYSTEM"` deb o'zgartiring va commit qiling.
4. `main` da turib `git merge dark-mode` qiling va yuzaga kelgan konfliktni hal eting.

**Yechim:**
```bash
# 1. main da Settings.kt yaratamiz
echo 'val THEME = "LIGHT"' > Settings.kt
git add Settings.kt
git commit -m "feat: standart tema kiritildi"

# 2. dark-mode branch ochamiz va o'zgartiramiz
git switch -c dark-mode
echo 'val THEME = "DARK"' > Settings.kt
git commit -am "feat: tungi tema sozlandi"

# 3. main ga qaytamiz va boshqacha o'zgartiramiz
git switch main
echo 'val THEME = "SYSTEM"' > Settings.kt
git commit -am "feat: tizim temasi sozlandi"

# 4. Merge qilamiz (KONFLIKT CHIQADI)
git merge dark-mode

# 5. Settings.kt faylini ochib qaraymiz:
# <<<<<<< HEAD
# val THEME = "SYSTEM"
# =======
# val THEME = "DARK"
# >>>>>>> dark-mode

# 6. Bizga ikkalasi ham kerak deb qaror qilib, faylni to'g'rilaymiz:
# val THEME = "AUTO_DARK"
echo 'val THEME = "AUTO_DARK"' > Settings.kt

# 7. Hal qilingan faylni sahnaga qo'shib commit qilamiz
git add Settings.kt
git commit -m "merge: dark-mode tarmog'i birlashtirildi, tema avtomatlashtirildi"
```

---

## Tezkor savol-javob (Quick Check)

1. **Savol:** Nima sababdan dasturchilar barcha yangi funksiyalarni `main` da emas, alohida branch'da yozadilar?  
   **Javob:** Asosiy kod bazasini barqaror saqlash, boshqa dasturchilarning ishiga xalaqit bermaslik va sinovdan o'tmagan chala kodlar ilovani buzib qo'ymasligi uchun.

2. **Savol:** `git checkout -b yangi-branch` va `git switch -c yangi-branch` buyruqlarining farqi bormi?  
   **Javob:** Har ikkalasi ham yangi branch ochib unga o'tadi. `git switch` yangiroq va maxsus branchlar uchun moslashtirilgan qulay sintaksisdir.

3. **Savol:** Merge Conflict nima sababdan sodir bo'ladi?  
   **Javob:** Ikkita branchda bir xil faylning ayni bir satri ikki xil tahrir qilinganda va Git qaysi birini saqlashni bilmay qolganda sodir bo'ladi.

4. **Savol:** `git diff` buyrug'ida yashil `+` va qizil `-` nimani anglatadi?  
   **Javob:** Yashil `+` yangi qo'shilgan kod satrlarini, qizil `-` esa o'chirilgan yoki almashtirilgan eski satrlarni bildiradi.

5. **Savol:** Ish tugallanmagan chala kodni saqlab, boshqa branchga shoshilinch o'tish uchun qaysi buyruq yordam beradi?  
   **Javob:** `git stash` (keyinchalik `git stash pop` orqali qaytarib olinadi).

---

## Uyga vazifa

1. O'z loyihangizda `feature-profile` nomli branch oching va yangi ekran kodini yozib commit qiling.
2. `main` branchga qaytib, o'zgarishlarni muvaffaqiyatli merge qiling.
3. Sinfdagi kabi sun'iy merge conflict hosil qiling va uni mustaqil ravishda qo'lda bartaraf etib, yakuniy commit qiling.
