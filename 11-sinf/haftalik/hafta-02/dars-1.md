# 4-dars. Git branching strategiyalari va Conventional Commits

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + chuqur amaliyot · **I-bob**, 4-dars (umumiy 4–51)

> Dasturda «Branching, Pull Request va code review metodologiyasi» mavzusiga 3 dars ajratilgan (4–6). Bo'linish: 4-dars — Git branching strategiyalari (Git Flow, GitHub Flow, Trunk-based), atomik commitlar va Conventional Commits formati; 5-dars — Pull Request madaniyati, PR shabloni (What/Why/How), PR checklist, merge turlari va konfliktlarni hal etish; 6-dars — Code review metodologiyasi, etikasi, inline sharhlar, taklif kodi va branch protection rules.

## 1. Dars rejasi

**Maqsad:** o'quvchi dasturiy ta'minot ishlab chiqishda tarmoqlash (branching) arxitekturasini tushunadi, Git Flow, GitHub Flow va Trunk-based strategiyalarini farqlaydi, kichik mantiqiy (atomik) commitlar yozishni hamda xalqaro Conventional Commits spetsifikatsiyasini amalda qo'llashni o'rganadi.

**Kutiladigan natija:**
- Nima uchun production (`main`) tarmog'iga to'g'ridan-to'g'ri commit yozish taqiqlanishini tushuntiradi.
- `git branch`, `git switch -c` (yoki `git checkout -b`), `git branch -d` buyruqlari bilan erkin ishlaydi.
- 3 ta asosiy branching strategiyasini (Git Flow, GitHub Flow, Trunk-based) tahlil qiladi va qachon qaysi birini tanlashni biladi.
- Kichik, maqsadli (atomik) commitlar falsafasini o'zlashtiradi ("bitta commit — bitta fikr").
- Conventional Commits formatida (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`) professional xabarlar yoza oladi.
- Terminalda mini-loyiha uchun feature branch ochib, Conventional Commitlar bilan tarix yaratadi va `git log --graph --oneline` da ko'radi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 1-hafta darslari (SDLC, Git asoslari, GitHub, remote, Issues) |
| 10–30 | Yangi mavzu 1 | Branching nima? Nega kerak? Git Flow, GitHub Flow, Trunk-based |
| 30–40 | Yangi mavzu 2 | Atomik commitlar va Conventional Commits spetsifikatsiyasi |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | Branch nomlash standartlari (`feature/`, `fix/`, `hotfix/`) |
| 55–75 | Amaliyot | Terminalda tarmoqlar yaratish, commitlar zanjiri, git log grafik tahlili |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, 5-darsga ko'prik |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- `git add` va `git commit -m` buyrug'ining vazifasi nima?
- Masofaviy repository (`origin`) ga kod qanday uzatiladi (`git push`)?
- Nega har bir loyihaga `.gitignore` kerak?

### 2.2. Tarmoqlash (Branching) nima va nega u zarur?
Tasavvur qiling: jamoada 5 nafar dasturchi bitta loyiha ustida ishlamoqda. Agar hamma o'zining yarim tayyor kodlarini to'g'ridan-to'g'ri `main` (asosiy) tarmoqqa push qilsa, sayt har 10 daqiqada qulab tushadi, sinovdan o'tmagan kodlar mijozlarga yetib boradi va loyiha falokatga uchraydi.

**Branch (Tarmoq)** — bu asosiy kod bazasidan vaqtincha ajralib chiqqan, mustaqil "parallel dunyo"dir.
- Dasturchi o'ziga alohida tarmoq ochadi (masalan, `feature/user-auth`);
- U yerda bemalol kod yozadi, xatolar qiladi, testlaydi — bu `main` dagi barqaror kodga zarracha ta'sir qilmaydi;
- Ish to'liq bitib, tekshirilgandan keyingina kod asosiy tarmoqqa qo'shiladi (merge).

Git da branch — og'ir fayllar nusxasi emas, balki aniq bir commitga ko'rsatib turgan **yengil ko'rsatkich (pointer)** dir (bor-yo'g'i 41 bayt). Shuning uchun Git da tarmoq ochish millisekundlarda bajariladi!

```bash
# Yangi tarmoq yaratish va unga o'tish (zamonaviy sintaksis)
git switch -c feature/add-login

# Eski sintaksis (ekvivalent)
git checkout -b feature/add-login

# Mavjud tarmoqlar ro'yxatini ko'rish
git branch

# Asosiy tarmoqqa qaytish
git switch main

# Ishi bitgan tarmoqni o'chirish
git branch -d feature/add-login
```

### 2.3. Branching strategiyalari (Workflows)

#### 1. Git Flow (Klassik, yirik korporatsiyalar uchun)
Vinsent Driessen tomonidan 2010-yilda taklif qilingan. Unda tarmoqlar qat'iy rollarga bo'linadi:
- `main` — faqat production'dagi barqaror versiyalar (v1.0, v2.0). Unga to'g'ridan-to'g'ri hech kim kod yozmaydi.
- `develop` — barcha ishlab chiqilgan funksiyalar yig'iladigan asosiy integratsiya tarmog'i.
- `feature/*` — yangi imkoniyatlar uchun `develop` dan ochiladi va yana `develop` ga qaytib qo'shiladi.
- `release/*` — yangi versiyani chiqarishdan oldin sinash va versiya raqamini belgilash uchun ochiladi.
- `hotfix/*` — production'da to'satdan xatolik (bug) chiqib qolganda shoshilinch tuzatish uchun `main` dan ochiladi va ham `main` ga, ham `develop` ga merge qilinadi.

*Qachon qo'llanadi:* Relizlari kam (oyiga yoki yiliga bir marta), qat'iy sinovdan o'tadigan, quti ko'rinishidagi dasturlarda (masalan, antiviruslar, tibbiy tizimlar, bank dasturlari).

#### 2. GitHub Flow (Zamonaviy, veb va startaplar standarti)
Oddiy, tezkor va bugungi kunda internet kompaniyalarining 90% qismida qo'llaniladigan model:
1. `main` tarmog'idagi har qanday kod istalgan soniyada serverga yuklanishi (deploy) mumkin bo'lgan darajada barqaror bo'lishi shart.
2. Har qanday yangi vazifa uchun `main` dan tavsiflovchi nom bilan branch ochiladi (masalan: `feature/telegram-bot` yoki `fix/header-logo`).
3. Dasturchi o'z branchiga commitlar qiladi va masofaviy repoga push qiladi.
4. **Pull Request (PR)** ochiladi, jamoa kodni tekshiradi (Code Review).
5. Barcha testlar o'tgach, kod `main` ga merge qilinadi va darhol deploy bo'ladi!

#### 3. Trunk-based Development (Yuqori tezlikdagi CI/CD, Google/Meta modeli)
Dasturchilar uzoq yashaydigan branchlar ochmaydi. Hamma to'g'ridan-to'g'ri `trunk` (asosiy tarmoq) ga kuniga bir necha marta kichik commitlar bilan integratsiya qiladi. Chala funksiyalar foydalanuvchiga ko'rinmasligi uchun **Feature Flags** (kod ichidagi o'chirib-yoqgichlar) ishlatiladi.

---

### 2.4. Kichik, maqsadli (Atomik) commitlar
Dasturchilarning eng yomon odati — 3 kun kod yozib, 40 ta har xil faylni o'zgartirib:
`git commit -m "ishlar qilindi va xatolar tuzatildi"` deb yozishdir.
Bu loyiha tarixini axlatxonaga aylantiradi: qaysi commit nimani buzganini topib bo'lmaydi!

**Oltin qoida (Atomic Commit):**
- Bitta commit — bitta tugallangan mantiqiy o'zgarish.
- Commit loyihani buzib qo'ymasligi, testlar har bir commitdan keyin ham ishlashi kerak.
- Kodni bo'lib-bo'lib commit qilish osonroq orqaga qaytarish (revert) imkonini beradi.

---

### 2.5. Conventional Commits spetsifikatsiyasi
Xalqaro jamoalarda commit xabarlarini barcha tushunishi va avtomatik reliz xatlarini (Changelog) shakllantirish uchun **Conventional Commits** standarti qo'llaniladi.

Struktura:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Asosiy turlar (`type`):
- `feat:` — foydalanuvchi uchun yangi funksionallik (masalan: `feat: add user login via google`).
- `fix:` — tizimdagi xatolikni tuzatish (masalan: `fix: resolve crash on empty search query`).
- `docs:` — faqat hujjatlardagi o'zgarishlar (masalan: `docs: update API endpoints in README`).
- `style:` — kod mantiqiga ta'sir qilmaydigan formatlash (bo'sh joylar, nuqta-vergul).
- `refactor:` — na yangi funksiya qo'shmaydigan, na xato tuzatmaydigan, lekin kod tuzilishini yaxshilaydigan o'zgarish.
- `perf:` — tezlik yoki resurs samaradorligini oshiruvchi o'zgarish (performance).
- `test:` — testlar qo'shish yoki mavjud testlarni tuzatish.
- `chore:` — yordamchi vositalar, paketlar, build konfiguratsiyasini yangilash.

Qoidalar:
1. Birinchi qator 50 belgidan oshmasligi ma'qul.
2. Fe'l buyruq maylida bo'ladi: `add`, `fix`, `update` (o'tgan zamon `added`, `fixed` EMAS!).
3. Birinchi qatorda oxirida nuqta qo'yilmaydi.
4. Agar o'zgarish orqaga moslikni buzsa (Breaking change): `feat!: drop support for python 3.8`.

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. Yangi tarmoq ochish va Conventional Commit
Lokal repongizda yangi tarmoq oching, faylga o'zgartirish kiriting va Conventional Commits formatida commit qiling.

**Yechim:**
```bash
# 1. Yangi tarmoqqa o'tish
git switch -c feat/user-authentication

# 2. Yangi fayl yaratish
echo "def login(): pass" > auth.py

# 3. Indeksga qo'shish va commit
git add auth.py
git commit -m "feat(auth): implement basic login function stub"
```

### 2-topshiriq. Xatolikni tuzatish (fix) va tarmoqlar o'rtasida o'tish
Auth faylidagi xatoni tuzating, fix commiti qiling, so'ng `main` ga qaytib fayl holatini tekshiring.

**Yechim:**
```bash
# 1. Kodga o'zgartirish kiritish
echo "def login(username, password): return True" > auth.py

# 2. Fix commiti
git add auth.py
git commit -m "fix(auth): add username and password arguments to login"

# 3. main ga qaytish va tekshirish
git switch main
ls -la # auth.py bu yerda ko'rinmaydi, chunki u faqat feat/user-authentication tarmog'ida mavjud!

# 4. Yana o'z tarmog'imizga qaytish
git switch feat/user-authentication
ls -la # auth.py yana paydo bo'ldi!
```

### 3-topshiriq. Chiroyli git log tahlili
Branchlar tarixini daraxt ko'rinishida ko'rish uchun maxsus alias buyrug'ini bajaring.

**Yechim:**
```bash
git log --graph --oneline --all --decorate
```
*Kutiladigan natija:* Terminalda turli tarmoqlar, ularning commitlari va boshlanish nuqtalari rangli chiziqlar bilan ko'rinadi.

---

## 4. Tezkor nazorat (5 daqiqa)

1. Nima uchun jamoada ishlab chiqish jarayonida har bir yangi vazifa alohida branchda qilinadi?
   - **Javob:** Asosiy (`main`) tarmoqdagi barqarorlikni saqlash va sinovdan o'tmagan kodlarni ajratib turish uchun.
2. Git Flow va GitHub Flow o'rtasidagi asosiy farq nima?
   - **Javob:** Git Flow ko'plab qat'iy tarmoqlarga (`develop`, `release`, `hotfix`) ega murakkab tizim; GitHub Flow esa bitta barqaror `main` va qisqa muddatli feature branchlardan iborat yengil model.
3. Conventional Commits formatida `fix:` va `refactor:` o'rtasidagi farq nima?
   - **Javob:** `fix:` foydalanuvchiga ta'sir qiluvchi xatoni tuzatadi, `refactor:` esa tashqi xatti-harakatni o'zgartirmasdan ichki kod arxitekturasini yaxshilaydi.
4. `git switch -c feature/cart` buyrug'i nima vazifani bajaradi?
   - **Javob:** `feature/cart` nomli yangi tarmoq yaratadi va darhol unga o'tadi.
5. Atomik commit deganda nimani tushunasiz?
   - **Javob:** Bitta commit ichida faqat bitta mantiqiy vazifani qamrab oluvchi, loyihaning ishlashini buzmaydigan yaxlit o'zgarish.

---

## 5. Xulosa va keyingi darsga ko'prik
Bugun biz professional dasturchilar kabi tarmoqlanish arxitekturasi va commit xabarlarini standartlashtirishni o'rgandik.
**Keyingi dars (5-dars):** Yozilgan feature branchlarni asosiy tarmoqqa qo'shish jarayoni — **Pull Request (PR)** madaniyati, PR shabloni, merge turlari va yuzaga keladigan merge konfliktlarni hal qilishni o'rganamiz!
