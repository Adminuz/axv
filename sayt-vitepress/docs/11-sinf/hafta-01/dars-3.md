---
title: "3-dars. GitHub: masofaviy repo, push/pull/clone, README, .gitignore, Issues va birinchi loyiha"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 1, "link": "/11-sinf/hafta-01/"}, "g": 3, "title": "GitHub: masofaviy repo, push/pull/clone, README, .gitignore, Issues va birinchi loyiha", "lead": "Bugun kodingiz birinchi marta noutbukdan chiqib, butun dunyo ko'ra oladigan joyga boradi: GitHub. Oxirida sizda ish beruvchiga ko'rsatsa bo'ladigan birinchi haqiqiy repo bo'ladi.", "slide": "/slaydlar/11-sinf/hafta-01/dars-3.html", "test": "/slaydlar/11-sinf/hafta-01/dars-3-test.html", "tabs": [{"g": 1, "link": "/11-sinf/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/11-sinf/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/11-sinf/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "Git asoslari: versiyalarni boshqarish, repozitoriy, commit, branch va merge", "link": "/11-sinf/hafta-01/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Git — kompyuteringizdagi dastur (tarixni yuritadi); GitHub — repolarni saqlaydigan va ular atrofida hamkorlik (Issues, Pull Request, review, Actions) beradigan xizmat.
- Remote — boshqa joydagi repo nusxasiga berilgan nom; odatda `origin`.
- Autentifikatsiya: HTTPS + token, SSH kalit yoki `gh auth login`. Ochiq kalit (`.pub`) ulashiladi, maxfiy kalit hech qachon.
- `git push -u origin main` yuboradi, `git fetch` yuklaydi, `git pull` yuklab qo'shadi, `git clone` to'liq nusxa oladi.
- `README.md` — reponing old eshigi: nima ekani va qanday ishga tushishi.
- `.gitignore` sirlar (`.env`), chiqindilar va mahalliy fayllarni tarixdan uzoq tutadi.
- Issue — vazifa/xato kartochkasi; commit xabaridagi `Closes #1` uni avtomatik yopadi.
- Keyingi hafta: branching strategiyalari, Pull Request va code review.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega faqat Git yetmaydi?
Git bitta kompyuterda ham ishlaydi, lekin u yerda tarix yolg'iz sizniki. Noutbuk suvga tushsa, hammasi ketadi, jamoadosh esa kodingizni ko'rolmaydi. GitHub reponing «markaziy» nusxasini saqlaydi: zaxira, hamkorlik va portfolio bir joyda. O'xshatish: Git — shaxsiy daftar, GitHub — shu daftarning umumiy kutubxonadagi nusxasi va uni muhokama qiladigan doska.

### Kalit juftligi: qulf va kalit
SSH kalit ikki fayl: ochiq (`id_ed25519.pub`) va maxfiy (`id_ed25519`). Ochiq kalit — «qulf»: uni GitHub'ga ishonib topshirasiz. Maxfiy kalit — «kalit»: faqat sizning kompyuteringizda qoladi. Qulf bilan istagan odam kelib, siz kirishingizni tekshirishi mumkin, lekin faqat kalitingiz borida eshik ochiladi.

```bash
ssh-keygen -t ed25519 -C "sizning@emailingiz"   # kalit juftligini yaratadi
cat ~/.ssh/id_ed25519.pub                        # faqat OCHIQ kalit ko'rsatiladi
ssh -T git@github.com                            # ulanishni tekshirish
```

Qoida: `cat ~/.ssh/id_ed25519` (nuqtali `.pub` siz) bilan maxfiy kalitni ekranga chiqarmang, skrinshot qilmang, repoga qo'shmang.

### Token — vaqtinchalik parol
Personal Access Token (PAT) ham parol o'rnini bosadi, lekin cheklanadi: qaysi repo, qaysi amallar, qancha muddat. Shuning uchun u oddiy paroldan xavfsizroq. Qoidalar: faqat kerakli ruxsat (least privilege), qisqa muddat, kodga/README'ga/chatga yozmaslik, sizib chiqsa darhol bekor qilish (revoke). Hammasini o'zingiz GitHub'da qilasiz; tokenni hech kimga yubormang.

### fetch va pull: ko'rib olish va qo'shish
`git fetch` — «yangilik bormi?» deb qarab, nusxani yuklab qo'yadi, lekin sizning fayllaringizga tegmaydi. `git pull` — ularni darrov joriy shoxingizga qo'shadi ham. Gumon bo'lsa, avval `fetch` qiling va `git log origin/main --oneline` bilan nima kelganini ko'ring. Push «rejected» desa — masofada sizda yo'q commit bor: majburlamang (`--force` yo'q), avval `git pull`.

### Sirlar tarixdan «yo'qolmaydi»
Faraz qiling, `.env` ichidagi kalitni commit qildingiz va push qildingiz. Keyingi commitda faylni o'chirdingiz. Kalit baribir eski commit ichida turadi va istagan odam `git log -p` bilan ko'ra oladi (ba'zi botlar GitHub'ni aynan sirlar uchun skanerlaydi). Shuning uchun tartib shunday: 1) sirni darhol bekor qiling/almashtiring; 2) `.gitignore` ga qo'shing; 3) kuzatuvdan chiqaring: `git rm --cached .env`. Eng yaxshisi: `.gitignore` ni birinchi commitdan oldin yozing.

```gitignore
# sirlar
.env
*.pem
# chiqindilar
__pycache__/
node_modules/
# OS va muharrir
.DS_Store
.vscode/
```

### Yaxshi README nimadan iborat?
Notanish odam 2 daqiqada loyihani tushunib, ishga tushira olsin. Minimal: nom, bir jumlalik tavsif, imkoniyatlar, ishga tushirish buyruqlari, muallif. Keyin skrinshot, litsenziya va badge qo'shiladi. Ish beruvchi ko'pincha kodni emas, avval README'ni o'qiydi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Repository (repo) | Loyiha fayllari va ularning to'liq tarixi saqlanadigan joy |
| Remote | Boshqa joydagi (masalan GitHub'dagi) repo nusxasiga berilgan nom |
| origin | Remote uchun odatiy nom |
| push | Lokal commitlarni masofaviy repoga yuborish |
| pull | Masofadagi yangiliklarni yuklab, joriy shoxga qo'shish (fetch + merge) |
| fetch | Yangiliklarni yuklab olish, ishchi fayllarni o'zgartirmasdan |
| clone | Masofaviy reponing to'liq nusxasini kompyuterga olish |
| PAT (token) | Paroldan xavfsizroq, cheklangan ruxsatli kirish tokeni |
| SSH kalit | Ochiq va maxfiy kalitdan iborat juftlik, parolsiz xavfsiz kirish uchun |
| README.md | Loyihani tavsiflovchi bosh fayl (Markdown) |
| .gitignore | Git kuzatmasligi kerak fayllar ro'yxati |
| Issue | Repodagi vazifa, xato yoki g'oya kartochkasi (#1, #2...) |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- GitHub nomi «Git» + «hub» (markaz) dan olingan; Git'ni 2005 yilda Linux yaratuvchisi Linus Torvalds yozgan.
- Sirlarni tasodifan GitHub'ga chiqarib yuborish juda keng tarqalgan xato: avtomatik botlar ochiq repolarni skanerlaydi va sizib chiqqan kalitni daqiqalar ichida topishi mumkin.
- Katta kompaniyalar ham GitHub'da ishlaydi; ko'plab ochiq loyihalarga (Linux, Python, VS Code) o'zingiz ham o'zgartirish taklif qila olasiz.
- Issue sarlavhasi va commit xabari bir-biriga bog'lanadi: `Closes #12` yozsangiz, #12 issue avtomatik yopiladi.
- Ish beruvchilar GitHub profilingizdagi 3–6 ta eng yaxshi (pinned) repoga qarashadi: README sifati ularda katta rol o'ynaydi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Qaysi biri qayerda? <Badge type="tip" text="oson" />
Quyidagi 8 narsadan qaysilari Git'ga, qaysilari GitHub'ga tegishli: commit, Issue, `git init`, repo sahifasi, `git add`, Pull Request, `git log`, Actions. Jadval qilib yozing.

**Kutiladigan natija:** ikki ustunli jadval, har bir narsa to'g'ri ustunda, 1 jumlalik izoh bilan.

### 2. Bu buyruq nima qiladi? <Badge type="tip" text="oson" />
Har birini bir jumlada tushuntiring: `git remote -v`, `git push -u origin main`, `git clone <manzil>`, `git fetch`.

**Kutiladigan natija:** 4 ta tushuntirish; `-u` ning vazifasi aniq yozilgan.

### 3. Hisob xavfsizligi <Badge type="tip" text="oson" />
GitHub akkauntingizda 2FA yoqing (yoki yoqilganini tekshiring) va tiklash kodlarini xavfsiz joyda saqlang. Profilga ism va qisqa bio yozing.

**Kutiladigan natija:** Settings → Password and authentication da 2FA «enabled»; kodlar parol menejerida yoki qog'ozda, ekranda ulashilmagan.

### 4. Kalit juftligi <Badge type="tip" text="oson" />
SSH kalit yarating (`ssh-keygen -t ed25519`), faqat ochiq kalitni GitHub'ga qo'shing va `ssh -T git@github.com` bilan tekshiring. (Yoki `gh auth login`.)

**Kutiladigan natija:** «successfully authenticated» xabari; maxfiy kalit hech qayerga yuborilmagan.

### 5. `dev-log` ni e'lon qiling <Badge type="warning" text="o'rta" />
Mini loyiha (masalan, vazifalar ro'yxati yoki o'zingiz tanlagan kichik dastur) uchun papka oching, `git init` qiling, dasturni, `README.md` ni va `.gitignore` ni alohida mazmunli commitlarda saqlang (kamida 3 ta). GitHub'da bo'sh repo yarating (README/.gitignore ni belgilamasdan), remote ulang va push qiling.

**Kutiladigan natija:** repo sahifasida 3 ta commit; README chiroyli ko'rinadi; chiqindi fayllar (`__pycache__/` va shunga o'xshash) repoda yo'q.

### 6. Aniq README <Badge type="warning" text="o'rta" />
README'ingizga 5 ta bo'lim qo'shing: nom, tavsif, imkoniyatlar, ishga tushirish (kod bloki bilan), muallif. Do'stingiz (yoki oila a'zosi) faqat shu matn bo'yicha loyihani ishga tushirib ko'rsin.

**Kutiladigan natija:** boshqa odam so'ramasdan dasturni ishga tushirdi; qaysi joyda qiyinchilik bo'lsa, README tuzatildi.

### 7. Issue → commit → yopish <Badge type="warning" text="o'rta" />
Repoda 2 ta Issue oching, ularga mos label bering. Bittasini commit xabaridagi `Closes #N` orqali yoping.

**Kutiladigan natija:** bitta Issue yopilgan (yopgan commit havolasi ko'rinadi), ikkinchisi ochiq.

### 8. Xatoni toping <Badge type="warning" text="o'rta" />
Do'stingiz GitHub'da repo yaratdi (README bilan), keyin kompyuterida `git init`, commit qildi va `git push -u origin main` buyrug'ini berdi. Push rad etildi. Nima uchun? Uni tuzatishning xavfsiz yo'lini yozing (`--force` ishlatmasdan).

**Kutiladigan natija:** sabab (ikki tomonda tarix mustaqil rivojlangan) va tuzatish qadamlari (pull yoki fetch, so'ng push) tushuntirilgan.

### 9. Ikkinchi nusxa <Badge type="danger" text="qiyin" />
`git clone` bilan loyihangizni boshqa papkaga yuklang. Nusxada kichik o'zgartirish qiling va push qiling. Asl papkada avval `git fetch`, `git status` va `git log origin/main --oneline` ni ishlating, keyin `git pull`. Har qadamdan keyin nima o'zgarganini yozing.

**Kutiladigan natija:** fetch'dan keyin ishchi fayllar o'zgarmagan, lekin status «behind» deydi; pull'dan keyin o'zgarish paydo bo'ldi. Fetch va pull farqi o'z so'zlaringizda yozilgan.

### 10. Sir sizib chiqish mashqi <Badge type="danger" text="qiyin" />
Faqat mashq repo'sida va faqat **soxta** qiymat bilan (haqiqiy kalit/parol HECH QACHON): `.env` fayliga `API_KEY=soxta-qiymat` yozing va uni tasodifan commit qiling. Tuzatish ketma-ketligini o'zingiz toping va bajaring. So'ng yozma javob bering: nega faqat faylni o'chirish yetmaydi va haqiqiy sirda birinchi qadam nima bo'ladi?

**Kutiladigan natija:** `.env` `.gitignore` da va kuzatuvdan chiqarilgan; yozma javobda eski commitda sir qolishi va sirni almashtirish zarurati aytilgan.

### 11. `.gitignore` ni o'zingiz loyihalang <Badge type="danger" text="qiyin" />
Tasavvur qiling, loyihangizda Python (yoki JavaScript), VS Code, API kalitlari va mahalliy ma'lumotlar bazasi fayli bor. Kerakli `.gitignore` yozing va har bir qator nima uchun borligini `#` izoh bilan tushuntiring. `git status` yordamida ishlayotganini sinab ko'ring.

**Kutiladigan natija:** kamida 8 qatorli izohli `.gitignore`; `git status` da ignor qilingan fayllar ko'rinmaydi.

### 12. Profilingiz vitrinasi <Badge type="info" text="bonus" />
GitHub profilingizga qarang: foydalanuvchi nomi professional emasmi? Bio bormi? Repolaringizdan eng yaxshisini pin qiling (Customize your pins). Boshqa dasturchining profilini (masalan, siz hurmat qiladigan ochiq loyiha muallifini) ko'rib, o'zingizga 3 ta g'oya yozib oling.

**Kutiladigan natija:** profilda bio, kamida 1 ta pin qilingan repo; 3 ta g'oya ro'yxati.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Git va GitHub farqini bir jumlada ayting.
2. `origin` nima, va `git push -u origin main` dagi `-u` nimaga kerak?
3. Ochiq va maxfiy SSH kalit farqi nima, qaysi birini GitHub'ga qo'yasiz?
4. `fetch`, `pull`, `clone` qachon ishlatiladi?
5. Nega repo yaratishda README va `.gitignore` ni belgilamaslik kerak (lokal repo allaqachon bor bo'lsa)?
6. Kalit commit qilinib push qilindi. Birinchi qadam nima va nega faylni o'chirish yetmaydi?
7. Issue'ni commit orqali qanday yopish mumkin?
8. Keyingi hafta nimani o'rganasiz va bugungi repo unga qanday tayyorlaydi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

`dev-log` repongizga yana 2 ta mazmunli commit qo'shing (masalan, yangi buyruq va README'ni yaxshilash), bitta Issue'ni `Closes #N` bilan yoping va repo havolasini mentorga yuboring (20–30 daqiqa). Parol, token va maxfiy kalit hech qachon yuborilmaydi: faqat ochiq repo havolasi.

</div>

