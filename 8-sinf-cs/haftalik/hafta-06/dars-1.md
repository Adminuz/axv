# 16-dars. Git va GitHub bilan tanishuv (3-qism): GitHub akkaunti va loyihani repositoryga joylash

**Fan:** Computer Science Foundation
**Sinf:** 8-sinf
**Hafta:** 6-hafta, 1-dars (umumiy 16-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** O'quv dasturi, 12-mavzu «Git va GitHub bilan tanishuv»: «GitHub akkaunt yaratish va loyihani repositoryga joylash... Git asosiy buyruqlari: ... clone, push, pull.» Buyruqlar (`remote`, `push -u`) sinov muhitida (mahalliy «masofaviy» repo bilan) tekshirilgan; GitHub interfeysi qadamlari umumiy tavsif.

---

## Darsning maqsadi

O'quvchilarga GitHub akkaunti nima uchun kerakligini, akkauntni xavfsiz ochish tartibini (13 yosh, ota-ona ruxsati, kuchli parol, 2 bosqichli tekshiruv), GitHub'da yangi repository yaratishni, `git remote add origin` va `git push -u origin main` bilan kompyuterdagi «Kundalik» loyihasini GitHub'ga joylashni o'rgatish.

## Kutiladigan natija

- GitHub akkauntini xavfsiz sozlash qoidalarini (parol, 2FA, ommaviy profil) aytadi;
- GitHub'da bo'sh repository yaratadi (nom, Public/Private);
- `git remote add origin` bilan mahalliy repo'ni GitHub'ga ulaydi;
- `git push -u origin main` bilan commitlarni GitHub'ga yuboradi;
- GitHub sahifasida fayllar va commitlar paydo bo'lganini tekshiradi.

## Kerakli jihozlar

- Kompyuter, internet va brauzer
- Git o'rnatilgan, `kundalik` loyihasi 3 ta commit bilan (15-dars)
- Elektron pochta manzili (ota-ona ruxsati bilan)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 15-dars: init, add, commit, log |
| 08–22 | Yangi mavzu 1 | GitHub akkaunt: ochish va xavfsizlik |
| 22–32 | Yangi mavzu 2 | Yangi repository yaratish |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | remote va push: loyiha internetga chiqadi |
| 50–75 | Amaliyot | Tekshirish, xatolar, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. GitHub akkaunt va xavfsizlik

Git — kompyuterdagi dastur, **GitHub** esa loyihalarni internetda saqlaydigan sayt (github.com). Kompyuter buzilsa ham, loyiha GitHub'da saqlanib qoladi. Akkaunt ochish: github.com → **Sign up** → email, parol, **username** (ommaviy bo'ladi!). GitHub qoidasi bo'yicha akkaunt egasi kamida **13 yoshda** bo'lishi kerak, shuning uchun akkauntni ota-onangiz bilan birga oching. Username'ga ism-familiya va tug'ilgan yilni emas, neytral nom tanlang (masalan, `alisher-codes`). Parol uzun va noyob bo'lsin, akkauntda **2 bosqichli tekshiruv** (2FA) yoqilsin. Profilga telefon raqami va uy manzilini yozmang.

Commit email'i GitHub akkauntidagi email bilan bir xil bo'lsa, commitlar profilingizga bog'lanadi. Xohlasangiz, GitHub'ning yashirin (noreply) email manzilidan foydalaning.

### 2. GitHub'da repository yaratish

Akkauntga kirgach, tepadagi **+ → New repository** ni bosing. To'ldiriladi: **Repository name** (masalan, `kundalik`), ixtiyoriy **Description**, ko'rinish: **Public** (hamma ko'radi) yoki **Private** (faqat siz va taklif qilinganlar). O'quv loyihalar uchun Public qulay, lekin ichida shaxsiy ma'lumot bo'lmasligi shart. Muhim: kompyuterda loyiha va commitlar allaqachon bor, shuning uchun **«Add a README file» belgisini qo'ymang**, repository bo'sh bo'lsin, aks holda GitHub'dagi va kompyuterdagi tarix farq qilib qoladi. **Create repository** ni bosgach, GitHub manzil (URL) ko'rsatadi: `https://github.com/username/kundalik.git`. Shu manzil kerak bo'ladi.

Repository nomini kichik harf va chiziqcha bilan yozing (`mening-kundaligim`): bo'sh joy va maxsus belgilar GitHub'da chiziqchaga aylanadi.

### 3. remote va push: yuklash

Kompyuterdagi repo'ni GitHub bilan bog'lash uchun **remote** (masofaviy manzil) qo'shiladi. Odatda uni **origin** deb nomlashadi: `git remote add origin MANZIL`. `git remote -v` ulanishni ko'rsatadi. Keyin `git branch -M main` asosiy branch nomini `main` qiladi, `git push -u origin main` esa commitlarni GitHub'ga **yuboradi** (`-u` — keyingi safar faqat `git push` yozish yetishini eslab qoladi). Birinchi push'da brauzer ochilib, GitHub'ga kirishingiz so'ralishi mumkin: o'z akkauntingiz bilan tasdiqlang. Parolni terminalga yozish o'rniga shu usuldan foydalaning. Push tugagach, GitHub sahifasini yangilang: fayllar va commitlar ko'rinadi. Keyin har safar: `add` → `commit` → `push`.

Keyingi o'zgarishlarda: `git add .` → `git commit -m "xabar"` → `git push`. Commit qilmagan o'zgarish push bilan yuklanmaydi.

---

## Kod namunasi

«Kundalik» loyihasini GitHub'ga yuklash (to'liq ketma-ketlik):

```bash
cd kundalik
git status                       # working tree clean bo'lishi kerak
git remote add origin https://github.com/username/kundalik.git
git remote -v                    # origin (fetch) va origin (push)
git branch -M main
git push -u origin main          # brauzerda GitHub'ga kirishni tasdiqlang

# keyingi kunlarda:
echo "Seshanba: GitHub'ni o'rgandim" > seshanba.txt
git add .
git commit -m "Seshanba yozuvi qo'shildi"
git push
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Akkaunt qoidalari
GitHub akkauntini xavfsiz ochishning 4 qoidasini yozing.

**Kutiladigan natija:** 4 qoida.

**Yechim:** 13+ yosh (ota-ona bilan), kuchli parol, 2FA, shaxsiy ma'lumotsiz username.

### 2-topshiriq (oson). Manzilni o'qing
`github.com/ali/kundalik.git` da egasi va repo nomi qaysi?

**Kutiladigan natija:** Ega va nom.

**Yechim:** Egasi `ali`, repository nomi `kundalik`.

### 3-topshiriq (o'rta). Remote ulash
`kundalik` repo'sini GitHub manziliga ulang.

**Kutiladigan natija:** Ulangan remote.

**Yechim:** 
```bash
git remote add origin https://github.com/ali/kundalik.git
git remote -v
```

### 4-topshiriq (o'rta). Birinchi push
Branch nomini `main` qilib, birinchi marta yuboring.

**Kutiladigan natija:** Commitlar GitHub'da.

**Yechim:** 
```bash
git branch -M main
git push -u origin main
```

### 5-topshiriq (qiyin). Keyingi o'zgarish
README'ga qator qo'shing va GitHub'ga yuboring.

**Kutiladigan natija:** GitHub'da yangi commit.

**Yechim:** 
```bash
echo "Muallif: Ali" >> README.md
git add .
git commit -m "README: muallif qo'shildi"
git push
```

### 6-topshiriq (qo'shimcha). Public yoki Private
Shaxsiy kundalik uchun qaysi ko'rinishni tanlaysiz? Nega?

**Kutiladigan natija:** Asoslangan javob.

**Yechim:** Private: kundalikni faqat o'zim ko'raman. Public — faqat shaxsiy ma'lumotsiz portfolio uchun.

---

## Tezkor nazorat (dars oxirida)

1. GitHub akkauntini kim ochishi mumkin? — 13 yoshdan boshlab; ota-ona bilan birga ochgan ma'qul.
2. Repository nima uchun bo'sh yaratiladi? — Kompyuterdagi tarix to'g'ridan-to'g'ri yuklansin.
3. origin nima? — Remote'ning odatiy nomi.
4. `push -u` dagi `-u` nima beradi? — Keyingi safar faqat `git push` yetadi.
5. Push nimani yuboradi? — Faqat commit qilinganlarni.

## Keng tarqalgan xatolar

- Push oldidan `git commit` qilishni unutish.
- Repo'ni «Add a README» bilan yaratib, tarixlar farq qilib qolishi.
- Remote'ni ikki marta qo'shish («remote origin already exists»).
- Username yoki README'ga shaxsiy ma'lumot yozish.
- Parolni terminal yoki kodga yozib qo'yish.

## Bilasizmi? (qo'shimcha)

- GitHub 2018-yildan Microsoft'ga tegishli, Git esa ochiq dastur.
- Terminalda parol o'rniga ko'pincha brauzer orqali kirish yoki maxsus token ishlatiladi.
- Shaxsiy kalit yoki parolni hech qachon GitHub'ga yuklamang.
