# 14-dars. Git va GitHub bilan tanishuv (1-qism): versiya nazorati, repository va commit

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **II-bob**, 8-dars (hafta ichida 2-dars)

> Manba: o'quv dasturi, 12-mavzu «Git va GitHub bilan tanishuv»: «Git va GitHub tushunchasi, Version Control tizimi. Repository, commit, branch va README fayllari bilan ishlash. GitHub akkaunt yaratish va loyihani repositoryga joylash. Git asosiy buyruqlari: init, add, commit, status, log, clone, push, pull.» Metodlar: tadqiqot va izlanish (GitHub platformasi bilan tanishish), Peer Learning, amaliy mashqlar; baholashda — «GitHub laboratoriya ishlari», «GitHub Repository». Mavzu 4 darsga bo'lingan: 14-dars — tushunchalar va GitHub veb-interfeysi; 15-dars — kompyuterda Git (init, status, add, commit, log); 16–17-darslar — clone, push, pull, branch. Tarixiy faktlar (Git — 2005, GitHub — 2008) va GitHub'ning yosh talabi (13 yosh) — rasmiy manbalardan qo'shimcha ma'lumot.

## 1. Dars rejasi

**Maqsad:** o'quvchilar versiya nazorati tizimi (VCS) nima uchun kerakligini, Git va GitHub farqini, repository, commit, branch va README tushunchalarini o'rganadi; GitHub akkaunt yaratish tartibini biladi va veb-interfeysda birinchi repository'ni README bilan yaratib, commit qiladi.

**Kutiladigan natija:**
- Versiya nazorati tizimining 3 ta afzalligini aytadi (tarix, orqaga qaytish, jamoaviy ish).
- Git (kompyuterdagi dastur) va GitHub (bulutdagi xizmat) farqini tushuntiradi.
- Repository, commit, branch, README atamalariga ta'rif beradi va kundalik misol bilan bog'laydi.
- Yaxshi va yomon commit xabarini ajratadi.
- GitHub'da repository yaratadi, README'ni Markdown'da tahrirlaydi va commit tarixini ochadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va muammo | Versiya tarixi (13-dars); «`referat_oxirgi_ROSTDAN_v3.docx`» muammosi |
| 10–30 daq | Yangi mavzu | VCS, Git va GitHub, repository, commit, branch, README, Markdown |
| 30–35 daq | Tanaffus | Harakatli tanaffus |
| 35–68 daq | Amaliyot | GitHub akkaunt (yoki mentor akkaunti), birinchi repository, README, commit tarixi |
| 68–75 daq | Tezkor nazorat | 5 ta savol |
| 75–80 daq | Xulosa va uyga vazifa | Keyingi dars: Git kompyuterda |

---

## 2. Dars konspekti

### 2.1. Muammo: qaysi fayl oxirgisi?
`referat.docx`, `referat_yangi.docx`, `referat_oxirgi.docx`, `referat_oxirgi_ROSTDAN_v3.docx` — tanish holatmi? Qaysi biri to'g'ri? Kecha nima o'zgardi? Do'stingiz bilan bitta faylni qanday birga yozasiz? Dasturchilar minglab fayllar bilan aynan shu muammoga duch keladi.

### 2.2. Versiya nazorati tizimi (Version Control System, VCS)
**VCS** — fayllardagi har bir o'zgarishni saqlab boradigan tizim:
- **Tarix** — kim, qachon, nimani o'zgartirgani va nega;
- **Orqaga qaytish** — istalgan eski holatga qaytish («vaqt mashinasi»);
- **Jamoaviy ish** — bir necha kishi bitta loyiha ustida bir vaqtda ishlaydi va o'zgarishlarni birlashtiradi;
- **Xavfsiz tajriba** — yangi g'oyani asosiy loyihani buzmasdan sinash (branch).

O'xshatish: kompyuter o'yinidagi **saqlash nuqtalari (save point)** — xato qilsangiz, oxirgi saqlangan joydan davom etasiz.

### 2.3. Git va GitHub — bir xil narsa emas

| | Git | GitHub |
|---|---|---|
| Nima | versiya nazorati **dasturi** | Git repository'lari uchun **bulutli xizmat (sayt)** |
| Qayerda ishlaydi | sizning kompyuteringizda | internetda, github.com |
| Internet kerakmi | yo'q | ha |
| Kim yaratgan | Linus Torvalds, 2005 (Linux yadrosi uchun) | 2008-yil; 2018-yildan Microsoft'ga tegishli |
| Vazifasi | o'zgarishlarni saqlash (commit), tarix | kodni saqlash, ulashish, jamoa bilan ishlash, portfolio |
| O'xshashlari | — | GitLab, Bitbucket |

O'xshatish: **Git — fotoapparat** (o'zgarishlarni «suratga oladi»), **GitHub — onlayn foto-albom** (suratlarni bulutda saqlab, boshqalarga ko'rsatadi). Bu — 11–13-darslardagi bulut g'oyasining dasturchilar uchun versiyasi.

### 2.4. Asosiy atamalar

| Atama | Ma'nosi | Kundalik o'xshatish |
|---|---|---|
| **Repository (repo)** | loyiha papkasi + uning butun o'zgarishlar tarixi | tarixli loyiha papkasi |
| **Commit** | loyihaning ma'lum paytdagi saqlangan holati (surat) + xabar, muallif, vaqt, noyob ID | o'yindagi saqlash nuqtasi |
| **Branch** | asosiy loyihadan ajralgan parallel ish yo'li; asosiysi — `main` | daraxt shoxi |
| **README** | loyiha haqida tavsif fayli (`README.md`), repo sahifasida birinchi ko'rinadi | kitob muqovasidagi annotatsiya |

### 2.5. Yaxshi commit xabari
Commit xabari — «nima o'zgardi?» savoliga qisqa javob.

| Yomon | Yaxshi |
|---|---|
| `asdf` | `README ga loyiha maqsadi qo'shildi` |
| `o'zgarish` | `Bosh sahifaga rasm qo'shildi` |
| `fix` | `Kalkulyatordagi bo'lish xatosi tuzatildi` |

### 2.6. README va Markdown
README odatda **Markdown** (`.md`) da yoziladi — oddiy belgilar bilan formatlash:
```markdown
# Mening birinchi repom          ← katta sarlavha
## Men haqimda                   ← kichik sarlavha
Men **8-sinf** o'quvchisiman.    ← qalin matn
- Sevimli fanim: informatika     ← ro'yxat
- Orzuim: dasturchi bo'lish
```

### 2.7. GitHub akkaunt yaratish
1. **github.com** → **Sign up**.
2. Email, kuchli parol (13-dars qoidalari), **username** (masalan, `alisher-dev`) — u profil manzili bo'ladi: `github.com/alisher-dev`.
3. Emailga kelgan kodni kiritib tasdiqlash.
4. GitHub foydalanish shartlariga ko'ra — **kamida 13 yosh**; akkauntni ota-ona ruxsati bilan oching.

### 2.8. Veb-interfeysda birinchi repository
1. O'ng yuqorida **+** → **New repository**.
2. **Repository name:** `mening-birinchi-repom` (bo'sh joysiz, kichik harflar, `-` bilan).
3. **Public** (hamma ko'radi) yoki **Private** (faqat siz va taklif qilinganlar).
4. ✔ **Add a README file** → **Create repository**.
5. README'ni ochish → qalam (**Edit**) → Markdown'da yozish → **Commit changes** → xabar yozish → tasdiqlash.
6. **Commits** (soat belgisi) — barcha commitlar ro'yxati: xabar, muallif, vaqt, ID.

---

## 3. Amaliy mashg'ulotlar

> Akkaunt ochish uchun o'quvchilarning emaili va ota-ona roziligi kerak. Agar akkaunt bo'lmasa, mentor o'z akkauntida sinf repository'sini ochib, o'quvchilarni navbat bilan commit qildiradi yoki qadamlar qog'ozda «commit kartochkalari» bilan modellashtiriladi.

### 1-mashq (oson). Git yoki GitHub?
**Vazifa:** Har bir gapni Git yoki GitHub ga ajrating: (a) kompyuterda internetsiz ishlaydi; (b) sayt, unda profil va repository'lar bor; (c) Linus Torvalds yaratgan; (d) Microsoft'ga tegishli; (e) o'zgarishlarni commit qilib saqlaydi.

**Yechim:** (a) Git; (b) GitHub; (c) Git; (d) GitHub; (e) Git (GitHub'da ham commit qilish mumkin, lekin commit — Git tushunchasi).

### 2-mashq (oson). Atamani toping
**Vazifa:** (1) loyiha haqidagi tavsif fayli; (2) loyihaning saqlangan holati; (3) asosiy loyihadan ajralgan parallel yo'l; (4) loyiha papkasi va uning tarixi.

**Yechim:** (1) README; (2) commit; (3) branch; (4) repository.

### 3-mashq (o'rta). Commit xabarlarini yaxshilang
**Vazifa:** `123`, `yangi`, `ishladi!!!`, `rasm` xabarlarini aniq va tushunarli qilib qayta yozing.

**Yechim (namuna):** `Loyiha uchun birinchi fayllar qo'shildi`; `README ga muallif haqida bo'lim qo'shildi`; `Tugma bosilganda xabar chiqishi tuzatildi`; `Bosh sahifaga maktab rasmi qo'shildi`.

### 4-mashq (qiyin). Birinchi repository
**Vazifa:** GitHub'da `mening-birinchi-repom` repository'sini README bilan yarating. README'ga Markdown'da: sarlavha, «Men haqimda» bo'limi, qalin matn va 3 bandli ro'yxat yozing. Kamida **2 ta commit** qiling va commit tarixini ochib, ID'larini daftarga yozing.

**Yechim (tekshiruv):** repo sahifasida formatlangan README ko'rinadi; Commits sahifasida kamida 2 ta (yaratish + tahrir) commit, har birida tushunarli xabar; ID — 7 belgili qisqa kod (masalan, `a1b2c3d`).

### 5-mashq (bonus). Mashhur repository'lar
**Vazifa:** GitHub qidiruvida `freeCodeCamp` yoki `vscode` repository'sini toping. Nechta commit, nechta yulduzcha (star) bor? README'da nima yozilgan?

**Yechim:** Raqamlar doimo o'zgarib turadi — o'quvchi hozirgi qiymatlarni yozadi; asosiy maqsad — repo sahifasining tuzilishini (fayllar, README, commitlar soni, star) tanish.

---

## 4. Tezkor savollar (Checklist)

1. Versiya nazorati tizimi nima uchun kerak?
   - **Javob:** O'zgarishlar tarixini saqlash, eski holatga qaytish va jamoa bo'lib ishlash uchun.
2. Git va GitHub farqi?
   - **Javob:** Git — kompyuterdagi versiya nazorati dasturi; GitHub — Git repository'larini bulutda saqlaydigan sayt.
3. Commit nima?
   - **Javob:** Loyihaning ma'lum paytdagi saqlangan holati: xabar, muallif, vaqt va ID bilan.
4. README fayli nima uchun kerak?
   - **Javob:** Loyiha nima ekanini, qanday ishlatilishini tushuntiradi; repo sahifasida birinchi ko'rinadi.
5. Public va Private repository farqi?
   - **Javob:** Public — hamma ko'radi; Private — faqat egasi va taklif qilingan odamlar.

## 5. Kuchli o'quvchi uchun qo'shimcha

- README'ga Markdown'da jadval (`| Fan | Baho |`) va havola (`[matn](manzil)`) qo'shing.
- `username/username` nomli maxsus repository yarating — uning README'si GitHub profilingiz sahifasida chiqadi (profil README).

## 6. Mentor uchun eslatmalar

- Akkaunt ochishni dars oldidan uyga vazifa sifatida (ota-ona bilan) berish vaqtni tejaydi; email tasdiqlash ba'zan 5–10 daqiqa oladi.
- Shaxsiy ma'lumot qoidasi: README'ga telefon raqami, manzil, maktab raqami yozilmasin — repo ochiq bo'lishi mumkin.
- «Git = GitHub» xatosini darsda kamida 2 marta qaytaring; fotoapparat va foto-albom o'xshatishidan foydalaning.
- Keyingi darsda Git kompyuterga o'rnatiladi — sinf kompyuterlarida Git (git-scm.com) oldindan o'rnatilganini tekshiring.
