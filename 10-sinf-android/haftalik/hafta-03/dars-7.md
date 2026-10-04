# 7-dars: Git bilan versiya nazorati asoslari

**Fan:** Advanced Android dasturlash  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta, 1-dars (umumiy 7-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga dasturiy ta'minot ishlab chiqishda versiyalarni boshqarish tizimlari (VCS), xususan, tarqoq (distributed) versiya nazorati tizimi hisoblangan **Git**ning vazifasi, ishlash mexanizmlari, terminal orqali birlamchi konfiguratsiyalarni amalga oshirish (`git config`), yangi repozitoriy yaratish (`git init`), Gitning 3 ta asosiy maydoni (**Working Directory**, **Staging Area**, **Repository**), o'zgarishlarni kuzatish va saqlash (`git status`, `git add`, `git commit`, `git log`) hamda Android loyihalarida keraksiz build artefaktlarini hisobga olmaslik uchun `.gitignore` faylini to'g'ri sozlash ko'nikmalarini chuqur o'rgatish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Versiya nazorati nima uchun kerakligini va Gitning loyihalar uchun "vaqt mashinasi" vazifasini bajarishini tushunish;
- Gitning tarqoq (distributed) arxitekturasi va markazlashgan tizimlardan afzalliklarini bilish;
- `git config --global user.name` va `user.email` buyruqlari orqali shaxsiy mualliflik parametrlarini sozlay olish;
- Gitning 3 holatini aniq farqlash: Working Directory (ishchi papka) -> Staging Area (sahna/tayyorlash) -> Repository (doimiy ombor);
- `git init`, `git status`, `git add`, `git commit -m "..."`, `git log --oneline` buyruqlarini terminalda erkin qo'llash;
- Android Studio loyihalari uchun `.gitignore` qoidalarini tuzish: `/build`, `/.gradle`, `/local.properties`, `*.apk`, `*.aab` kabi fayllarni Git nazoratidan chiqarib tashlash.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Git o'rnatilgan tizim (Git Bash, macOS/Linux Terminal);
- Android Studio yoki VS Code muharriri;
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va yangi modulga kirish | ProGuard/R8 mavzusi xulosasi, versiya nazorati nima va nima uchun dasturchiga Git shart ekani bo'yicha kirish |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | Git arxitekturasi, 3 holat falsafasi, asosiy terminal buyruqlari va Android `.gitignore` |
| **30–55 min** | Amaliy mashg'ulot (Terminalda ishlash) | Yangi loyiha ochish, `git init`, fayl yaratish, status tekshirish, add va birinchi commit |
| **55–75 min** | Mustaqil laboratoriya ishi | Android loyihasida `.gitignore` sozlash va commit tarixini (`git log`) shakllantirish |
| **75–80 min** | Xulosa va baholash | Tezkor savol-javob, xulosalar va uyga vazifa |

---

## Nazariy qism (Batafsil tushuntirish)

### 1. Git nima va u nega har bir Android dasturchisiga shart?

Dasturlash jarayonida loyiha to'xtovsiz rivojlanadi: yangi ekranlar qo'shiladi, API integratsiya qilinadi, xatolar tuzatiladi. Odatda yangi boshlovchilar loyiha nusxalarini `Loyiha_final`, `Loyiha_final_2`, `Loyiha_eng_oxirgi` deb saqlashga urinishadi. Bu usul juda xavfli, chalkash va jamoaviy ishlashga mutlaqo yaroqsizdir.

**Git** — bu loyihadagi har bir bayt, har bir fayl va satr darajasidagi o'zgarishlarni vaqt bo'yicha qayd etib boruvchi **Tarqoq Versiya Nazorati Tizimi (Distributed Version Control System — DVCS)**dir.
- **Vaqt mashinasi:** Istalgan daqiqada kechagi, o'tgan haftadagi yoki bir yil oldingi ishchi holatga bitta buyruq bilan qaytish mumkin.
- **Xavfsizlik:** Yangi funksiya yozayotganda butun loyihani buzib qo'yishdan qo'rqmaysiz.
- **Tarqoqlik:** Har bir dasturchining kompyuterida butun loyiha tarixi to'liq saqlanadi. Internet bo'lmaganda ham bemalol ishlash mumkin.

---

### 2. Gitni sozlash (Birlamchi konfiguratsiya)

Git o'rnatilgach, kompyuterda eng birinchi navbatda dasturchining ismi va elektron pochtasi kiritiladi. Bu har bir commit ostida kim kod yozganini muhrlash uchun shart:

```bash
git config --global user.name "Ali Valiyev"
git config --global user.email "ali.valiyev@xorazmiy.uz"
```

Sozlamalarni tekshirish:
```bash
git config --list
```

---

### 3. Gitning 3 holati (Three States)

Git arxitekturasi 3 ta asosiy maydondan iborat bo'lib, fayllar shu bosqichlardan o'tadi:

1. **Working Directory (Ishchi maydon):** Kompyuteringizdagi real fayllar va papkalar. Siz kod yozayotgan, tahrirlayotgan joy.
2. **Staging Area / Index (Tayyorlash maydoni):** Keyingi "suratga olish" (commit) uchun belgilab qo'yilgan o'zgarishlar sahnasi.
3. **Repository (.git ombori):** Loyihaning barcha commitlari, tarixi va metama'lumotlari xavfsiz siqilgan holda saqlanadigan doimiy ma'lumotlar bazasi.

---

### 4. Asosiy terminal buyruqlari

#### Repozitoriy yaratish:
```bash
git init
```
Bu buyruq joriy papkada yashirin `.git` papkasini ochadi. Ushbu papkani aslo o'chirib yubormaslik kerak, chunki unda loyihaning butun o'tmishi yotadi.

#### Holatni tekshirish:
```bash
git status
```
- **Qizil rangda:** Kuzatilmayotgan (Untracked) yoki o'zgartirilgan, lekin sahnaga kiritilmagan fayllar.
- **Yashil rangda:** Staging areaga o'tgan (Staged), commit qilishga tayyor fayllar.

#### Sahnaga qo'shish:
```bash
git add MainActivity.kt      # Bitta faylni qo'shish
git add .                     # Barcha o'zgarishlarni qo'shish
```

#### Tarixga muhrlash (Commit):
```bash
git commit -m "Bosh sahifa UI elementlari yaratildi"
```
Har bir commit ma'noli, tushunarli va aniq xabar bilan yozilishi shart.

#### Tarixni ko'rish:
```bash
git log
git log --oneline --graph     # Qisqa va chiroyli ko'rinish
```

---

### 5. Android loyihalari uchun `.gitignore` faylining o'rni

Android loyihasini kompilyatsiya qilganda Gradle yuzlab gigabaytlik vaqtinchalik fayllar, keshlar va binary fayllar (`.class`, `.dex`, `.apk`, `.aab`) yaratadi. Shuningdek, `local.properties` faylida dasturchining shaxsiy SDK yo'li yoki maxfiy kalitlari (API Keys) saqlanadi.

Bu fayllarni Gitga qo'shish mutlaqo **TAQIQLANADI**!
Chunki:
1. Repozitoriy hajmi sun'iy ravishda yuzlab megabaytga oshib ketadi;
2. Boshqa kompyuterda SDK yo'li boshqacha bo'lgani uchun loyiha ochilmay qoladi;
3. Maxfiy API kalitlar xakerlar qo'liga tushishi mumkin.

Loyihaning ildiz papkasida `.gitignore` fayli yaratiladi:
```gitignore
# Gradle kesh va build chiqishlari
.gradle/
build/
app/build/

# Shaxsiy SDK va konfiguratsiya fayllari
local.properties
.idea/caches/
.idea/libraries/

# Android Studio vaqtincha fayllari
*.iml
.DS_Store

# Yig'ilgan APK va AAB fayllari
*.apk
*.aab
```

---

## Amaliy topshiriqlar (Sinfda bajarish uchun)

### 1-topshiriq: Yangi repozitoriy ochish va birinchi commit

**Vazifa:** Terminalda `AndroidNotes` nomli yangi papka oching, uni Git repozitoriyasiga aylantiring. `README.md` faylini yaratib, ichiga loyiha tavsifini yozing va birinchi commitni amalga oshiring.

**Yechim:**
Terminalda ketma-ket quyidagi buyruqlar bajariladi:
```bash
# 1. Yangi papka yaratish va ichiga kirish
mkdir AndroidNotes
cd AndroidNotes

# 2. Git repozitoriyasini ishga tushirish
git init

# 3. README.md faylini yaratish
echo "# Android Notes loyihasi" > README.md

# 4. Holatni tekshirish (fayl qizil bo'lib chiqadi)
git status

# 5. Sahnaga chiqarish (yashil bo'ladi)
git add README.md

# 6. Tarixga yozish
git commit -m "docs: loyiha tavsifi va README fayli yaratildi"

# 7. Tarixni ko'rish
git log --oneline
```

---

### 2-topshiriq: Android loyihasi uchun `.gitignore` qoidalarini tuzish

**Vazifa:** O'quvchiga quyidagi fayllar ro'yxati beriladi. Ulardan qaysilari Gitga commit qilinishi kerak va qaysilari `.gitignore` ga qo'shilishi lozimligini ajrating hamda to'g'ri `.gitignore` faylini yozing:
1. `app/src/main/java/com/app/MainActivity.kt`
2. `app/build/outputs/apk/debug/app-debug.apk`
3. `local.properties`
4. `gradle/libs.versions.toml`
5. `.gradle/8.4/checksums/checksums.lock`
6. `app/build.gradle.kts`

**Yechim:**
- **Gitga kiritiladigan (Tracked) fayllar:**
  - `app/src/main/java/com/app/MainActivity.kt` (Manba kodi)
  - `gradle/libs.versions.toml` (Bog'liqliklar katalogi)
  - `app/build.gradle.kts` (Build skripti)
- **`.gitignore` ga kiritiladigan (Ignored) fayllar:**
  - `app/build/` va `*.apk` (Kompilyatsiya natijasi)
  - `local.properties` (Lokal SDK sozlamalari)
  - `.gradle/` (Gradle kesh fayllari)

`.gitignore` fayli tarkibi:
```gitignore
# Gradle keshlari
.gradle/

# Build natijalari va APK lar
build/
app/build/
*.apk

# Shaxsiy SDK sozlamalari
local.properties
```

---

### 3-topshiriq: Bir nechta fayllar bilan ishlash va Git holatlarini tahlil qilish

**Vazifa:** `AndroidNotes` loyihasida ikkita fayl yarating: `NotesAdapter.kt` va `NoteEntity.kt`. Faqat `NoteEntity.kt` faylini commit qiling, `NotesAdapter.kt` esa Working Directory'da qolishini ta'minlang. Har bir qadamda `git status` natijasini tahlil qiling.

**Yechim:**
```bash
# 1. Ikkita fayl yaratamiz
touch NoteEntity.kt
touch NotesAdapter.kt

# 2. Statusni ko'ramiz (ikkalasi ham qizil rangda - Untracked)
git status

# 3. Faqat NoteEntity.kt faylini sahnaga qo'shamiz
git add NoteEntity.kt

# 4. Statusni ko'ramiz (NoteEntity yashil, NotesAdapter esa qizil)
git status

# 5. Commit qilamiz
git commit -m "feat: NoteEntity ma'lumotlar modeli yaratildi"

# 6. Statusni qayta tekshiramiz: NoteEntity omborga kirdi, NotesAdapter hali ham untracked holatda qoldi
git status
```

---

## Tezkor savol-javob (Quick Check)

1. **Savol:** Git nima va u markazlashgan tizimlardan nimasi bilan farq qiladi?  
   **Javob:** Git — tarqoq (distributed) versiya nazorati tizimidir. Unda har bir foydalanuvchining kompyuterida butun loyiha tarixi to'liq saqlanadi, server bilan uzluksiz internet aloqasi talab etilmaydi.

2. **Savol:** `git add` va `git commit` buyruqlarining farqi nimada?  
   **Javob:** `git add` o'zgartirilgan fayllarni sahnaga (Staging Area) olib chiqadi, `git commit` esa sahnadagi o'zgarishlarni doimiy omborga (Repository) tarixiy nusxa sifatida muhrlaydi.

3. **Savol:** Nima sababdan `local.properties` va `build/` papkalarini Gitga qo'shish taqiqlanadi?  
   **Javob:** `local.properties` dasturchining shaxsiy SDK yo'lini saqlaydi (boshqa kompyuterda ishlamaydi), `build/` esa vaqtinchalik og'ir kompilyatsiya fayllari bo'lib, repozitoriy hajmini behuda kattalashtiradi.

4. **Savol:** Gitda qilingan o'zgarishlar ro'yxatini va commitlar tarixini ko'rish uchun qaysi buyruq ishlatiladi?  
   **Javob:** `git log` (yoki qisqa ko'rinishda `git log --oneline`).

5. **Savol:** `git init` buyrug'i qanday fayl yoki papka hosil qiladi va uni o'chirsa nima bo'ladi?  
   **Javob:** U yashirin `.git` papkasini yaratadi. Agar u o'chirilsa, loyihaning barcha o'tmishi, commitlari va versiya tarixi butunlay yo'qoladi.

---

## Uyga vazifa

1. O'z kompyuteringizda Git o'rnatilganini tekshiring (`git --version`) va `git config` orqali ism hamda elektron pochtangizni sozlang.
2. O'zingiz yoqtirgan biror Android loyihangiz papkasiga kiring va uning ichidagi `.gitignore` faylini ochib, undagi har bir qator nimani anglatishini tahlil qiling.
3. Yangi sinov papkasi ochib, unda 3 ta ketma-ket commit qiling va `git log` orqali natijani skrinshot qilib mentorga yuboring.
