# 17-dars. Git va GitHub bilan tanishuv (4-qism): clone, pull va branch

**Fan:** Computer Science Foundation
**Sinf:** 8-sinf
**Hafta:** 6-hafta, 2-dars (umumiy 17-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** O'quv dasturi, 12-mavzu «Git va GitHub bilan tanishuv»: «Repository, commit, branch va README fayllari bilan ishlash... Git asosiy buyruqlari: init, add, commit, status, log, clone, push, pull.» Buyruqlar (`clone`, `pull`, `switch -c`, `merge`) sinov muhitida mahalliy «masofaviy» repo bilan tekshirilgan.

---

## Darsning maqsadi

O'quvchilarga `git clone` bilan GitHub'dagi repository'ning nusxasini kompyuterga olishni, `git pull` bilan yangilanishlarni yuklab olishni, branch (parallel yo'l) tushunchasini va `git switch -c`, `git merge` buyruqlarini hamda README.md faylini Markdown bilan chiroyli yozishni o'rgatish.

## Kutiladigan natija

- `git clone URL` bilan repository nusxasini kompyuterga oladi;
- `git pull` bilan GitHub'dagi yangi commitlarni yuklab oladi;
- Branch nima ekanini va `main` bilan farqini tushuntiradi;
- Yangi branch yaratib, unda ishlaydi va `git merge` bilan `main` ga qo'shadi;
- README.md ni Markdown (sarlavha, ro'yxat, qalin matn) bilan yozadi.

## Kerakli jihozlar

- Kompyuter, internet va brauzer
- 16-darsda GitHub'ga yuklangan `kundalik` repository'si
- Juft bo'lib ishlash uchun sinfdosh repository manzili (Public)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 16-dars: remote, push |
| 08–22 | Yangi mavzu 1 | clone: nusxa olish |
| 22–32 | Yangi mavzu 2 | pull va push: ikki tomonlama yangilash |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | branch va merge: parallel yo'l |
| 50–75 | Amaliyot | README.md va Markdown, xatolar, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. clone va pull

**clone** — GitHub'dagi repository'ning to'liq nusxasini (fayllar va butun commit tarixi) kompyuterga olish: `git clone URL`. Natijada repo nomli papka yaratiladi, ichida `.git` ham bor, `git init` va `remote` kerak emas (`origin` avtomatik ulanadi). Clone — yangi kompyuterda ishni davom ettirish yoki boshqaning ochiq loyihasini ko'rish usuli. **pull** — GitHub'dagi yangi commitlarni kompyuterdagi nusxaga yuklab olish: `git pull`. Qoida: ishni boshlashdan oldin `git pull`, tugatgach `git push`. Shunda sizda eng yangi versiya bo'ladi.

Ochiq repo'ni clone qilish — uni o'qish va o'rganish uchun. Boshqa odamning repo'iga to'g'ridan-to'g'ri push qila olmaysiz: buning uchun egasi ruxsat berishi kerak.

### 2. Branch va merge

**Branch** (shox) — asosiy loyihadan ajralib chiqqan parallel ish yo'li. Asosiy branch odatda **main** deb ataladi. Yangi g'oyani sinab ko'rish uchun alohida branch ochasiz: agar yoqmasa, `main` buzilmaydi. `git branch` — branchlar ro'yxati (joriysi `*` bilan), `git switch -c nom` — yangi branch yaratib, unga o'tish, `git switch main` — qaytish. Branchdagi ish tayyor bo'lgach, `main` ga o'tib `git merge nom` qilinadi: o'zgarishlar asosiy loyihaga qo'shiladi. Branch nomini ishning mazmuniga qarab bering: `yangi-sahifa`, `rasm-qoshish`.

Branch almashtirishdan oldin o'zgarishlarni commit qiling. Joriy branch qaysi ekanini `git branch` yoki `git status` ko'rsatadi.

### 3. README.md: Markdown bilan

**README.md** — repo sahifasida birinchi ko'rinadigan fayl: loyiha nima haqida ekani, kim yaratgani, qanday ishlatilishi yoziladi. `.md` — **Markdown** formati, oddiy belgilar bilan matnni bezaydi: `#` — katta sarlavha, `##` — kichikroq, `-` — ro'yxat, `**matn**` — qalin, `[matn](havola)` — havola. README'ni o'zgartirib, commit va push qilsangiz, GitHub sahifasida darhol chiroyli ko'rinadi. Eslatma: ochiq README'ga telefon raqami, uy manzili va maktab raqamini yozmang. Faqat ism (yoki laqab), loyiha maqsadi va qiziqishlaringizni yozing.

Markdown'ni GitHub'da to'g'ridan-to'g'ri qalam belgisi (Edit) orqali tahrirlash mumkin. Shunda GitHub'da yangi commit paydo bo'ladi, kompyuterda esa `git pull` kerak bo'ladi.

---

## Kod namunasi

Ikki tomonlama ish: GitHub ↔ kompyuter, branch bilan:

```bash
git clone https://github.com/username/kundalik.git
cd kundalik

git pull                          # ish oldidan yangilash
git switch -c rasm-qoshish        # yangi branch
echo "![rasm](rasm.png)" >> README.md
git add .
git commit -m "README'ga rasm qo'shildi"

git switch main
git merge rasm-qoshish
git push                          # main ni GitHub'ga yuborish
git branch                        # joriy branchni tekshirish
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). clone yoki pull?
Yangi kompyuterda loyiha yo'q. Qaysi buyruq kerak?

**Kutiladigan natija:** `clone`.

**Yechim:** 
```bash
git clone https://github.com/ali/kundalik.git
```

### 2-topshiriq (oson). Branch ro'yxati
Qaysi buyruq branchlarni ko'rsatadi va joriysini belgilaydi?

**Kutiladigan natija:** `git branch`.

**Yechim:** 
```bash
git branch
```

### 3-topshiriq (o'rta). Yangi branch
`yangi-sahifa` branch'ini yarating va unga o'ting.

**Kutiladigan natija:** Branch yaratildi.

**Yechim:** 
```bash
git switch -c yangi-sahifa
```

### 4-topshiriq (o'rta). Merge
Branchdagi ishni `main` ga qo'shing.

**Kutiladigan natija:** Merge bajarildi.

**Yechim:** 
```bash
git switch main
git merge yangi-sahifa
```

### 5-topshiriq (qiyin). README
README.md ga sarlavha, 3 bandli ro'yxat va muallifni yozing.

**Kutiladigan natija:** Chiroyli README.

**Yechim:** 
```bash
# Mening loyiham

- Git
- GitHub
- Branch

Muallif: Ali
```

### 6-topshiriq (qo'shimcha). Yangilanish
GitHub'da README'ni o'zgartirdingiz. Kompyuteringizda uni qanday olasiz?

**Kutiladigan natija:** `git pull`.

**Yechim:** 
```bash
git pull
```

---

## Tezkor nazorat (dars oxirida)

1. clone nima qiladi? — To'liq nusxa oladi.
2. pull nima qiladi? — Yangi commitlarni yuklab oladi.
3. Branch nima? — Parallel ish yo'li.
4. Branch'ni qaysi buyruq qo'shadi? — `git merge`.
5. README qaysi formatda? — Markdown (`.md`).

## Keng tarqalgan xatolar

- `clone` dan keyin papkaga `cd` bilan kirishni unutish.
- Ishni `pull` qilmasdan boshlash.
- Branch'da ekanini unutib, `main` deb o'ylash.
- `merge` ni `main` da emas, boshqa branchda bajarish.
- README'ga shaxsiy ma'lumot yozish.

## Bilasizmi? (qo'shimcha)

- Katta kompaniyalarda `main` ga to'g'ridan-to'g'ri yozilmaydi: ish branchlarda bajarilib, tekshirilgach qo'shiladi.
- GitHub'da Pull Request orqali o'zgarishni taklif qilish mumkin: buni keyingi bosqichda o'rganasiz.
- Pull paytida ziddiyat (conflict) chiqishi mumkin: ikki kishi bir qatorni o'zgartirsa. Bu odatiy holat.
