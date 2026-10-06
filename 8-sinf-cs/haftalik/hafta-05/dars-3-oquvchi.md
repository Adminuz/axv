# 15-dars. Git va GitHub bilan tanishuv (2-qism): kompyuterda Git

> O'tgan darsda commitni sayt orqali qildingiz. Haqiqiy dasturchilar esa o'z kompyuterida, terminalda ishlaydi — internetsiz ham. Bugun beshta buyruq bilan o'z «kundalik» repository'ingizni yaratasiz va uning tarixini ko'rasiz.

## Dars xulosasi

- Git'ni tekshirish: `git --version`; sozlash: `git config --global user.name` va `user.email`.
- `git init` — papkani repository'ga aylantiradi (yashirin `.git` papkasi).
- `git status` — fayllar holati: untracked, modified, staged.
- `git add fayl` (yoki `git add .`) — o'zgarishni **staging**'ga tayyorlash.
- `git commit -m "xabar"` — staging'dagi o'zgarishlarni saqlash.
- `git log` / `git log --oneline` — commitlar tarixi (eng yangisi yuqorida).
- Uch hudud: **ishchi papka → staging → repository**.

## Qo'shimcha ma'lumot

### 1. Konvert va pochta qutisi
Ishchi papka — stol ustidagi qog'ozlar. `git add` — kerakli qog'ozlarni **konvertga solish** (staging). `git commit` — konvertni **pochta qutisiga tashlash**: endi u tarixda abadiy saqlanadi. Konvertga nimani solishni o'zingiz tanlaysiz — shuning uchun `add` va `commit` alohida qadamlar.

### 2. Terminalda kerakli 4 buyruq

| Buyruq | Vazifasi |
|---|---|
| `pwd` | hozir qaysi papkadaman |
| `ls` | papkada nima bor |
| `cd papka` | papkaga kirish (`cd ..` — orqaga) |
| `mkdir papka` | yangi papka yaratish |

### 3. To'liq jarayon
```bash
mkdir kundalik
cd kundalik
git init
# README.md yaratib, ichiga yozing
git status                         # Untracked: README.md
git add README.md
git commit -m "README qo'shildi"
git log --oneline                  # a1b2c3d README qo'shildi
```

### 4. `git status` nima deydi?

| Xabar | Ma'nosi | Nima qilish kerak |
|---|---|---|
| `Untracked files` | yangi fayl, Git kuzatmayapti | `git add` |
| `Changes not staged for commit` | fayl o'zgargan | `git add` |
| `Changes to be committed` | commitga tayyor | `git commit -m` |
| `working tree clean` | hammasi saqlangan | dam oling |

### 5. Odatiy xatolar
- `add` siz `commit` — «nothing added to commit».
- `-m` siz `git commit` — Vim muharriri ochiladi: `Esc`, `:wq`, Enter.
- `.git` papkasini o'chirish — butun tarix yo'qoladi!
- `git config` qilinmagan — Git ismingizni so'raydi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Terminal | Matnli buyruqlar oynasi |
| Git Bash | Windows uchun Git terminali |
| git config | Git sozlamalari (ism, email) |
| git init | Repository yaratish |
| .git | Tarix saqlanadigan yashirin papka |
| Ishchi papka | Fayllarni tahrirlayotgan joy |
| Staging | Commitga tayyorlangan o'zgarishlar hududi |
| Untracked | Git kuzatmayotgan yangi fayl |
| Modified | O'zgargan, hali tayyorlanmagan fayl |
| git log | Commitlar tarixi |
| Commit ID (hash) | Har commitning noyob kodi |

## Bilasizmi?

- Commit ID aslida 40 belgili uzun kod (masalan, `a1b2c3d4e5...`); `--oneline` uning faqat birinchi 7 belgisini ko'rsatadi — bu odatda farqlash uchun yetarli.
- «Git» so'zi inglizcha jargonda «injiq odam» degan ma'noni beradi — Linus Torvalds dasturini hazil bilan shunday atagan.
- Git barcha tarixni sizning kompyuteringizda saqlaydi — shuning uchun GitHub ishlamay qolsa ham, ishingiz yo'qolmaydi.

## Topshiriqlar

### 1. Git bormi? · oson
`git --version` buyrug'ini bajaring va natijani yozing.
**Kutiladigan natija:** Git versiyasi raqami.

### 2. Sozlash · oson
`user.name` va `user.email` ni sozlang, `git config --list` bilan tekshiring.
**Kutiladigan natija:** 2 ta qator ko'rinadi.

### 3. Juftlang · oson
`init`, `status`, `add`, `commit`, `log` ni vazifasi bilan juftlang.
**Kutiladigan natija:** 5 ta juftlik.

### 4. Terminal · oson
`mkdir`, `cd`, `ls`, `pwd` bilan `mashq` papkasini yarating, unga kiring va qayerda ekaningizni ko'rsating.
**Kutiladigan natija:** papka yo'li yozilgan.

### 5. Birinchi repository · o'rta
`kundalik` papkasida `git init` qiling va `.git` papkasini toping (yashirin elementlarni yoqib).
**Kutiladigan natija:** `.git` papkasi skrinshoti.

### 6. Birinchi commit · o'rta
`README.md` yarating, `add` va `commit` qiling. Har qadamdan keyin `git status` ni yozing.
**Kutiladigan natija:** 3 ta status natijasi.

### 7. Status o'qish · o'rta
4 ta status xabari (untracked, not staged, to be committed, clean) uchun «nima qilish kerak»ni yozing.
**Kutiladigan natija:** 4 ta javob.

### 8. Uch hudud · o'rta
Ishchi papka, staging va repository'ni chizing va strelkalarga buyruqlarni yozing.
**Kutiladigan natija:** sxema.

### 9. Uch commit · qiyin
`kundalik` ga yana 2 ta commit qo'shing va `git log --oneline` natijasini yozing.
**Kutiladigan natija:** 3 qatorli tarix.

### 10. Xatoni toping · qiyin
O'quvchi `git commit -m "yangi fayl"` yozdi va «nothing added to commit» xabarini oldi. Sabab nima? Tuzating.
**Kutiladigan natija:** `git add` unutilgan.

### 11. Tarix detektivi · qiyin
`git log` (to'liq) natijasidan eng birinchi commitning muallifi, sanasi va xabarini toping.
**Kutiladigan natija:** 3 ta ma'lumot.

### 12. git diff · bonus
Faylni o'zgartirib, `git diff` bilan o'zgarishni ko'ring va nimani ko'rganingizni tushuntiring.
**Kutiladigan natija:** skrinshot va izoh.

## O'zingizni tekshiring

1. Git o'rnatilganini qanday tekshirasiz?
2. Nega `git config` kerak?
3. `git init` dan keyin papkada nima paydo bo'ladi?
4. `git add` va `git commit` farqi nimada?
5. Staging nima?
6. `git status` dagi «Untracked» nimani bildiradi?
7. `git log --oneline` da eng yangi commit qayerda?

## Uyga vazifa

`kundalik` repository'sini kamida 4 ta commit bilan davom ettiring va `git log --oneline` natijasini saqlang. 20–30 daqiqa. Batafsil — haftalik uyga vazifada.
