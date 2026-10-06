# 18-dars. Git va GitHub (1-qism): versiya nazorati, commit va GitHub'ga push

**Fan:** Web Full-stack dasturlash
**Sinf:** 8-sinf
**Hafta:** 6-hafta, 3-dars (umumiy 18-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** O'quv dasturi, 8-mavzu «Git va Github, hosting va SEO»: «Git tushunchasi va versiya nazorati. Asosiy Git buyruqlari (init, clone, add, commit, push, pull, branch, merge). GitHub platformasi va repository yaratish, remote repository bilan ishlash.» Birinchi qism: init, add, commit, log, remote, push (buyruqlar sinov muhitida tekshirilgan). clone, pull, branch, merge — 19-darsda.

---

## Darsning maqsadi

O'quvchilarga versiya nazorati (VCS) va Git tushunchasini, uch hudud (ishchi papka, staging, repository)ni, `git init`, `status`, `add`, `commit`, `log` buyruqlarini, `.gitignore` faylini, GitHub'da repository yaratib `remote add origin` va `push` bilan loyihani yuborishni o'rgatish.

## Kutiladigan natija

- Versiya nazorati nima uchun kerakligini 3 sabab bilan aytadi;
- `git init`, `status`, `add`, `commit` bilan loyihaga commit qiladi;
- `git log --oneline` natijasini o'qiydi;
- `.gitignore` bilan keraksiz fayllarni Git'dan chiqaradi;
- GitHub'da repository yaratib, `push` bilan loyihani yuboradi.

## Kerakli jihozlar

- Kompyuter, internet va Git (git-scm.com)
- GitHub akkaunti (ota-ona yoki mentor yordami bilan)
- «Maktab sayti» loyiha papkasi (15–16-darslar)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 17-dars: Figma |
| 08–22 | Yangi mavzu 1 | Versiya nazorati va uch hudud |
| 22–32 | Yangi mavzu 2 | Commit zanjiri: init, add, commit, log |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | GitHub: remote va push |
| 50–75 | Amaliyot | Tekshirish, xatolar, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Versiya nazorati va uch hudud

**Versiya nazorati** (VCS) — fayllardagi har bir o'zgarishni saqlab boradigan tizim: xato qilsangiz eski holatga qaytasiz, kim, qachon, nimani o'zgartirganini ko'rasiz, jamoada birga ishlaysiz. **Git** — eng mashhur VCS (2005, Linus Torvalds), kompyuteringizda ishlaydi, internet shart emas. **GitHub** — Git repository'larini internetda saqlaydigan platforma. **Repository** (repo) — loyiha papkasi va uning butun tarixi (yashirin `.git` papkasi). **Commit** — loyihaning ma'lum paytdagi saqlangan «surati» (xabar, muallif, vaqt, noyob ID bilan). Uch hudud: **ishchi papka** (siz tahrirlaysiz) → **staging** (`git add` bilan commitga tayyorlangan) → **repository** (`git commit` bilan saqlangan).

Git bir marta sozlanadi. Email — GitHub akkauntidagi email bilan bir xil bo'lsa, commitlar profilingizga bog'lanadi.

### 2. init, status, add, commit, log

Loyiha papkasida `git init` — papkani repository'ga aylantiradi (`.git` yaratiladi). `git status` fayllar holatini ko'rsatadi: **untracked** (yangi), **modified** (o'zgargan), **staged** (commitga tayyor). `git add fayl` (yoki `git add .` — hammasini) faylni staging'ga qo'shadi. `git commit -m "xabar"` staging'dagini tarixga saqlaydi. `git log --oneline` — commitlar tarixi: har biri qisqa ID va xabar bilan, eng yangisi tepada. Commit xabari nima o'zgarganini aniq aytishi kerak: «Menyu qo'shildi», «Karta rasmi tuzatildi», «asdf» emas. Kichik, mantiqiy qadamlar bilan tez-tez commit qiling.

`-m` ni unutsangiz, matn muharriri (Vim) ochiladi: chiqish — `Esc`, so'ng `:wq` va Enter. Commitdan oldin `git status` bilan nima yuborilishini tekshiring.

### 3. .gitignore, remote va push

Ba'zi fayllar tarixga tushmasligi kerak: parollar va kalitlar (`.env`), tizim fayllari (`.DS_Store`), og'ir kutubxona papkalari (`node_modules/`). Ular `.gitignore` faylida ro'yxatga olinadi, Git ularni kuzatmaydi. Keyin GitHub'da **New repository** orqali **bo'sh** repo yarating (README qo'shmang). Kompyuterdagi repo'ni unga ulang: `git remote add origin URL`, branch nomini `git branch -M main` bilan `main` qiling va `git push -u origin main` bilan yuboring (`-u` — keyingi safar faqat `git push`). Birinchi push'da brauzer orqali GitHub'ga kirish so'ralishi mumkin. Keyingi o'zgarishlarda: `add` → `commit` → `push`.

Parol, token va `.env` fayllarini hech qachon GitHub'ga yuklamang, ayniqsa Public repo'ga: ular butun dunyoga ko'rinadi. Tasodifan yuklangan bo'lsa, parolni darhol almashtiring.

---

## Kod namunasi

«Maktab sayti» ni Git bilan boshqarish va GitHub'ga yuborish:

```bash
# bir martalik sozlash
git config --global user.name "Alisher Karimov"
git config --global user.email "alisher@example.com"

cd maktab-sayti
git init
echo ".env" >> .gitignore
echo "node_modules/" >> .gitignore
git status
git add .
git commit -m "Sahifa strukturasi va gitignore qo'shildi"

# CSS o'zgartirilgandan keyin
git add style.css
git commit -m "Kartalar uchun responsiv CSS qo'shildi"
git log --oneline

# GitHub'ga yuborish (bo'sh repo yaratilgan)
git remote add origin https://github.com/username/maktab-sayti.git
git branch -M main
git push -u origin main
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Sozlash
Git'ga ismingiz va emailingizni kiriting.

**Kutiladigan natija:** Sozlash bajarildi.

**Yechim:** 
```bash
git config --global user.name "Ism Familiya"
git config --global user.email "email@example.com"
```

### 2-topshiriq (oson). Holatni o'qish
`git status` «Untracked files» desa, nima qilish kerak?

**Kutiladigan natija:** Fayl add qilinadi.

**Yechim:** Fayl Git tomonidan kuzatilmayapti: `git add fayl`, so'ng `git commit`.

### 3-topshiriq (o'rta). Birinchi commit
Papkani repo qiling va birinchi commitni yarating.

**Kutiladigan natija:** Commit yaratildi.

**Yechim:** 
```bash
git init
git add .
git commit -m "Birinchi commit"
```

### 4-topshiriq (o'rta). Tarixni ko'rish
Commitlar tarixini qisqa ko'rinishda chiqaring.

**Kutiladigan natija:** Tarix ko'rindi.

**Yechim:** 
```bash
git log --oneline
```

### 5-topshiriq (qiyin). gitignore
.env faylini va node_modules papkasini Git'dan chiqaring.

**Kutiladigan natija:** Fayllar ignor qilindi.

**Yechim:** 
```bash
echo ".env" >> .gitignore
echo "node_modules/" >> .gitignore
git add .gitignore
git commit -m ".gitignore qo'shildi"
```

### 6-topshiriq (qo'shimcha). GitHub'ga yuborish
Loyihani bo'sh GitHub repo'siga yuboring.

**Kutiladigan natija:** Push bajarildi.

**Yechim:** 
```bash
git remote add origin https://github.com/username/maktab-sayti.git
git branch -M main
git push -u origin main
```

---

## Tezkor nazorat (dars oxirida)

1. Git va GitHub farqi? — Git — dastur, GitHub — platforma.
2. Uch hudud? — Ishchi papka, staging, repository.
3. Faylni staging'ga qaysi buyruq qo'shadi? — `git add`.
4. `.gitignore` nima qiladi? — Fayllarni kuzatuvdan chiqaradi.
5. Push nimani yuboradi? — Commit qilinganlarni.

## Keng tarqalgan xatolar

- `add` dan keyin `commit` ni unutish.
- Mazmunsiz xabar yozish («fix», «asdf»).
- `.env` va parollarni repo'ga yuklash.
- `git init` ni noto'g'ri papkada bajarish (`pwd` bilan tekshiring).
- Repo'ni README bilan yaratib, mahalliy tarix bilan to'qnashtirish.

## Bilasizmi? (qo'shimcha)

- Commit ID — 40 belgili kod; `--oneline` da faqat boshidagi 7 belgi ko'rinadi.
- `git diff` commitdan oldin nima o'zgarganini ko'rsatadi.
- Git'ni 2005-yilda Linus Torvalds Linux yadrosi uchun yaratgan.
