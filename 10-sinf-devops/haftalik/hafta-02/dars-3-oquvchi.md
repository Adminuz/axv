# 6-dars. Git va versiya boshqaruvi tizimlariga kirish (Git asoslari)

> Dasturiy ta'minotning vaqt mashinasi: Git versiya boshqaruvi, 3 ta hudud (Working, Staging, Repository), commitlar anatomiyasi va .gitignore sirlari.

---

## Dars xulosasi

- Versiya boshqaruvi tizimlari (VCS) kodga kiritilgan har bir o'zgarishni (kim, qachon, nima qildi) aniq qayd etib boruvchi vositadir.
- Git — butun dunyo bo'ylab eng ko'p qo'llaniladigan taqsimlangan (Distributed VCS) tizim bo'lib, u Linux muallifi Linus Torvalds tomonidan yaratilgan.
- Git fayllarni 3 ta bosqichda boshqaradi: Working Directory (ishchi papka), Staging Area (tayyorgarlik maydoni) va Git Repository (tarix saqlanuvchi `.git` ombori).
- `git config` orqali muallif ismi va emaili o'rnatiladi, `git init` orqali yangi repozitoriya hosil qilinadi.
- `git status` loyihaning joriy holatini ko'rsatadi, `git add` fayllarni tayyorgarlik maydoniga kiritadi, `git commit` esa o'zgarishlarni tarixga muhrlaydi.
- Har bir commit noyob SHA-1 hash kodiga ega bo'lib, u loyihaning ma'lum bir vaqtdagi to'liq «fotosurati» (snapshot) hisoblanadi.
- `.gitignore` fayli orqali maxfiy kalitlar (`.env`), loglar (`*.log`) va yirik kutubxonalar (`node_modules/`) Git tarixiga tushishining oldi olinadi.

---

## Qo'shimcha ma'lumot

### 1. Nega Git «Snapshot» (Fotosurat) deyiladi?
Eski versiya boshqaruvi tizimlari (masalan, CVS) fayllarning faqatgina «o'zgargan qatorlari farqini» (delta-based) saqlagan.
Git esa har bir commit qilinganda loyihaning o'sha paytdagi butun holatini bir zumlik fotosurat (snapshot) sifatida yozib qo'yadi. Agar biror fayl o'zgarmagan bo'lsa, Git uni qayta saqlamaydi, balki oldingi mavjud nusxasiga havola (link) qo'yadi. Shu sababli Git boshqa barcha tizimlarga qaraganda yuzlab barobar tezroq ishlaydi.

### 2. Staging Area (Index) nima uchun kerak?
Nega o'zgarishlarni to'g'ridan-to'g'ri commit qilib bo'lmaydi?
Tasavvur qiling, siz bir vaqtning o'zida ikkita vazifani bajardingiz:
1. Sayt dizaynidagi xatoni to'g'riladingiz (`style.css`).
2. Yangi login funksiyasini yozdingiz (`login.js`).
Staging Area sizga ularni alohida-alohida commit qilish imkonini beradi:
- `git add style.css` → `git commit -m "fix: dizayndagi xato tuzatildi"`
- `git add login.js` → `git commit -m "feat: yangi login sahifasi qo'shildi"`
Bu loyiha tarixining toza va mantiqiy bo'lishini ta'minlaydi.

### 3. Commit xabarlari madaniyati (Conventional Commits)
DevOps jamoalarida commit izohlarini to'g'ri yozish juda muhim. Standart qolip:
- `feat:` yangi imkoniyat (feature) qo'shilganda.
- `fix:` xatolik (bug) tuzatilganda.
- `docs:` hujjatlar yoki izohlar o'zgarganda.
- `refactor:` kod mantig'i o'zgarmagan holda arxitekturasi yaxshilanganda.
- `chore:` yordamchi sozlamalar yoki `.gitignore` o'zgarganda.

### 4. SHA-1 Hash nima?
Har bir commit oxirida `c3b2f1a8e9d0...` ko'rinishidagi 40 belgili kod paydo bo'ladi. Bu kommitning barcha ma'lumotlari (fayllar mazmuni, sana, muallif, oldingi commit kodi) asosida hisoblangan matematik xeshdir. Agar kod ichida bitta nuqta o'zgarsa ham, butun xesh butunlay boshqa songa aylanadi — bu Git tarixini soxtalashtirib bo'lmasligini kafolatlaydi!

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **VCS (Version Control System)** | Fayllar va kodlarga kiritilgan o'zgarishlar tarixini avtomatik yozib boruvchi tizim. |
| **Git** | Yuqori tezlik va barqarorlikka ega zamonaviy taqsimlangan versiya boshqaruvi tizimi. |
| **Working Directory** | Kompyuter diskida foydalanuvchi bevosita ko'rib tahrirlayotgan fayllar hududi. |
| **Staging Area (Index)** | Keyingi commitga kiritilishi rejalashtirilgan o'zgarishlar saqlanadigan oraliq maydon. |
| **Commit** | Loyihaning ma'lum bir vaqtdagi to'liq holatini Git tarixiga muhrlovchi operatsiya. |
| **SHA-1 Hash** | Har bir commit uchun generatsiya qilinadigan noyob 40 belgili kriptografik identifikator. |
| **Untracked** | Ishchi papkada mavjud, lekin hali Git kuzatuviga (`git add`) olinmagan yangi fayllar. |
| **.gitignore** | Git tomonidan e'tiborsiz qoldirilishi kerak bo'lgan fayl va papkalar andozalari ro'yxati. |

---

## Bilasizmi?

- Git tizimi 2005-yilda Linus Torvalds tomonidan atigi 10 kun ichida ishlab chiqilgan bo'lib, uning maqsadi Linux yadrosi ustida butun dunyo dasturchilari bilan birgalikda ishlash bo'lgan.
- Git so'zi inglizcha so'zlashuv tilida «yoqimsiz, injiq odam» degan ma'noni anglatadi — Linus o'z xarakteriga hazil tarzida shu nomni tanlagan.
- Agar siz `.git` papkasini loyiha ichidan o'chirib yuborsangiz, loyihaning butun versiyalar tarixi bir zumda yo'qoladi va u oddiy papkaga aylanib qoladi.

---

## Topshiriqlar

### 1. Git versiyasini va sozlamalarni tekshirish · oson
`git --version` va `git config --list` buyruqlarini bajarib, tizimingizda Git o'rnatilganini hamda foydalanuvchi ma'lumotlarini aniqlang.
**Kutiladigan natija:** Git versiyasi va konfiguratsiya parametrlari ekranda chiqadi.

### 2. Yangi Git repozitoriyasini ochish · oson
`my_project` nomli katalog yarating, uning ichiga o'ting va `git init` orqali uni rasmiy Git omboriga aylantiring.
**Kutiladigan natija:** «Initialized empty Git repository in ...» xabari chiqadi.

### 3. Loyiha holatini tekshirish · oson
Yangi repozitoriy ichida `git status` buyrug'ini bering va hech qanday kommitlar yo'qligini ko'ring.
**Kutiladigan natija:** «On branch main / No commits yet / nothing to commit» holati ko'rinadi.

### 4. Yangi fayl yaratish va holatni kuzatish · oson
`echo "DevOps asoslari" > README.md` faylini yarating va `git status` da u qanday rangda (Untracked) ko'rinishini tahlil qiling.
**Kutiladigan natija:** Fayl qizil rangda «Untracked files» bo'limida chiqadi.

### 5. Staging maydoniga qo'shish · o'rta
`git add README.md` buyrug'ini bajaring va `git status` orqali faylning yashil rangga (Changes to be committed) aylanganini ko'ring.
**Kutiladigan natija:** Fayl muvaffaqiyatli Staging Area'ga o'tadi.

### 6. Birinchi commitni amalga oshirish · o'rta
`git commit -m "docs: README fayli yaratildi"` buyrug'i bilan o'zgarishlarni tarixga yozing.
**Kutiladigan natija:** Commit yaratiladi, SHA xesh kodi va o'zgargan fayllar statistikasi chiqadi.

### 7. Tarixni ko'rish (git log) · o'rta
`git log` va `git log --oneline` buyruqlarini bajarib, yaratilgan commit ma'lumotlarini (muallif, sana, izoh) o'rganing.
**Kutiladigan natija:** Yaratilgan commit tarixi ro'yxati chiqadi.

### 8. Kod farqlarini tahlil qilish (git diff) · o'rta
`README.md` fayliga yangi qator qo'shing va `git diff` buyrug'i orqali aynan qaysi qator qo'shilganini (yashil `+`) ko'ring.
**Kutiladigan natija:** O'zgartirilgan qatorlar terminalda aniq rangli formatda aks etadi.

### 9. .gitignore faylini sozlash · qiyin
Loyihangizda `secrets.txt` va `app.log` fayllarini yarating. Loyiha ildizida `.gitignore` ochib, ularni e'tiborsiz qoldirish qoidasini yozing va `git status` bilan tasdiqlang.
**Kutiladigan natija:** Maxfiy fayllar `git status` da mutlaqo ko'rinmaydi.

### 10. Bir nechta fayllarni guruhlab commit qilish · qiyin
`app.py` va `config.json` fayllarini yarating, `git add .` orqali barchasini birdaniga tayyorlang va «feat: dastlabki ilova fayllari qo'shildi» izohi bilan commit qiling.
**Kutiladigan natija:** Bir nechta fayllar yagona commit snapshotiga birlashadi.

### 11. Staging maydonidan faylni qaytarish (restore) · bonus
Faylni o'zgartirib `git add` qiling, so'ngra `git restore --staged [fayl]` buyrug'i yordamida uni commit qilmasdan yana oddiy ishchi hududga qaytarishni amalda sinang.
**Kutiladigan natija:** Fayl Staging maydonidan yana oddiy o'zgargan holatga qaytadi.

---

## O'zingizni tekshiring

1. Working Directory, Staging Area va Git Repository o'rtasidagi farqlar nimada?
2. `git add .` bilan `git add filename` ning qanday farqi bor?
3. Nima uchun har bir commitga tushunarli va standart qolipdagi izoh (commit message) yozish shart?
4. `.gitignore` fayliga qanday fayllar kiritilishi qat'iy tavsiya etiladi?
5. `git log --oneline` buyrug'i qachon qulay hisoblanadi?

---

## Uyga vazifa

1. O'z kompyuteringizda `my_first_git_repo` nomli papka oching va uni Git omboriga aylantiring.
2. Ichida `main.py`, `notes.txt` va `temp.log` fayllarini yarating.
3. `.gitignore` faylini yaratib, `*.log` kengaytmali barcha fayllarni e'tiborsiz qoldiring.
4. Qolgan fayllarni 2 ta alohida mantiqiy commit bilan Git tarixiga yozing.
5. `git log` natijasini daftaringizga ko'chirib yozing (taxminiy vaqt: 25 daqiqa).
