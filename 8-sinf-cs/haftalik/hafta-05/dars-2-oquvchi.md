# 14-dars. Git va GitHub bilan tanishuv (1-qism)

> `referat_oxirgi.docx`, `referat_oxirgi_ROSTDAN_v3.docx`... Qaysi biri to'g'ri? Dasturchilar bu muammoni ancha oldin hal qilgan: ular har bir o'zgarishni «saqlash nuqtasi» sifatida yozib boradi. Bugun bu tizim — Git va uning bulutdagi uyi — GitHub bilan tanishasiz.

## Dars xulosasi

- **Versiya nazorati tizimi (VCS)** — har bir o'zgarishni saqlaydi: tarix, orqaga qaytish, jamoaviy ish.
- **Git** — kompyuterdagi versiya nazorati dasturi (Linus Torvalds, 2005).
- **GitHub** — Git repository'larini bulutda saqlaydigan sayt (github.com).
- **Repository** — loyiha papkasi va uning butun tarixi.
- **Commit** — loyihaning saqlangan holati: xabar, muallif, vaqt, ID.
- **Branch** — parallel ish yo'li; asosiysi `main`.
- **README.md** — loyiha tavsifi, Markdown'da yoziladi.

## Qo'shimcha ma'lumot

### 1. Fotoapparat va foto-albom
**Git** — fotoapparat: loyihangizning har bir muhim holatini «suratga oladi» (commit). **GitHub** — onlayn foto-albom: suratlarni bulutda saqlaydi, do'stlaringizga ko'rsatadi va ular ham albomga qo'sha oladi. Fotoapparatsiz albom bo'sh, albomsiz suratlar faqat sizda qoladi.

### 2. Commit — o'yindagi saqlash nuqtasi
O'yinda qiyin bosqichdan oldin saqlaysiz: yutqazsangiz, shu joydan boshlaysiz. Commit ham shunday: kod buzilsa, oxirgi ishlagan commitga qaytasiz. Har commitda:
- **xabar** — nima o'zgardi;
- **muallif** — kim o'zgartirdi;
- **vaqt** — qachon;
- **ID** — noyob kod, masalan `a1b2c3d`.

### 3. Yaxshi commit xabari

| Yomon | Yaxshi |
|---|---|
| `asdf` | `README ga loyiha maqsadi qo'shildi` |
| `fix` | `Bo'lish xatosi tuzatildi` |
| `yangi` | `Bosh sahifaga rasm qo'shildi` |

### 4. Markdown — 1 daqiqada
```markdown
# Katta sarlavha
## Kichik sarlavha
**qalin matn**
- ro'yxat bandi
```

### 5. Birinchi repository
1. **+** → **New repository**.
2. Nom: `mening-birinchi-repom`.
3. **Public** yoki **Private**.
4. ✔ **Add a README file** → **Create repository**.
5. README → qalam (Edit) → yozing → **Commit changes**.

### 6. Odatiy xatolar
- «Git va GitHub — bitta narsa» deb o'ylash.
- Commit xabariga `123` yozish.
- Repo nomida bo'sh joy va katta harflar ishlatish.
- Ochiq README'ga telefon raqami yoki uy manzilini yozish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| VCS | Versiya nazorati tizimi |
| Git | Kompyuterdagi versiya nazorati dasturi |
| GitHub | Git repository'lari uchun bulutli sayt |
| Repository (repo) | Loyiha papkasi va uning tarixi |
| Commit | Loyihaning saqlangan holati |
| Commit xabari | O'zgarishning qisqa tavsifi |
| Branch | Parallel ish yo'li (shox) |
| main | Asosiy branch nomi |
| README.md | Loyiha haqida tavsif fayli |
| Markdown | `#`, `**`, `-` belgilari bilan formatlash tili |
| Public / Private | Ochiq / yopiq repository |

## Bilasizmi?

- Linus Torvalds Git'ning birinchi versiyasini 2005-yilda bir necha hafta ichida yozgan — Linux yadrosi ustida ishlayotgan minglab dasturchilar uchun.
- GitHub logotipidagi mushuk-sakkizoyoq «Octocat» deb ataladi.
- 2020-yilda GitHub ochiq kodlarning nusxasini Arktikadagi (Shpitsbergen oroli) yer osti omboriga ming yil saqlash uchun joylashtirgan — «Arctic Code Vault».

## Topshiriqlar

### 1. Git yoki GitHub? · oson
5 ta gapni ajrating: internetsiz ishlaydi; profil sahifasi bor; Linus Torvalds yaratgan; Microsoft'ga tegishli; commit qiladi.
**Kutiladigan natija:** 5 ta javob.

### 2. Atamalar · oson
Repository, commit, branch, README — har biriga bir jumlalik ta'rif yozing.
**Kutiladigan natija:** 4 ta ta'rif.

### 3. Kundalik o'xshatish · oson
Commit va branch uchun o'zingizning kundalik o'xshatishingizni toping.
**Kutiladigan natija:** 2 ta o'xshatish.

### 4. VCS afzalliklari · oson
Versiya nazorati tizimining 3 ta afzalligini yozing.
**Kutiladigan natija:** 3 bandli ro'yxat.

### 5. Commit xabarlari · o'rta
`123`, `yangi`, `ishladi!!!`, `rasm` xabarlarini aniq qilib qayta yozing.
**Kutiladigan natija:** 4 ta yaxshi xabar.

### 6. Markdown · o'rta
O'zingiz haqingizda Markdown'da qisqa README yozing: sarlavha, kichik sarlavha, qalin matn, 3 bandli ro'yxat.
**Kutiladigan natija:** to'g'ri belgilangan matn.

### 7. Git va GitHub jadvali · o'rta
5 mezon bo'yicha jadval: nima, qayerda, internet kerakmi, yaratuvchi, vazifasi.
**Kutiladigan natija:** 5 qatorli jadval.

### 8. Public yoki Private? · o'rta
(a) maktab portfoliosi; (b) shaxsiy kundalik; (c) sinf loyihasi kodi — qaysi biri qanday bo'lishi kerak?
**Kutiladigan natija:** 3 ta asoslangan javob.

### 9. Birinchi repository · qiyin
GitHub'da `mening-birinchi-repom` ni README bilan yarating va kamida 2 ta commit qiling.
**Kutiladigan natija:** repo havolasi.

### 10. Commit tarixi · qiyin
Repo'ingizning Commits sahifasini oching va har commitning xabari, vaqti va ID'sini yozing.
**Kutiladigan natija:** jadval.

### 11. Muammoni hal qiling · qiyin
4 ta `referat_...docx` fayli bor. Agar referat Git'da bo'lganida, bu muammo qanday hal bo'lardi? 4–5 jumla yozing.
**Kutiladigan natija:** commit va tarix bilan tushuntirish.

### 12. Mashhur repo · bonus
GitHub'da `vscode` yoki `freeCodeCamp` repository'sini toping: commitlar va yulduzchalar sonini, README mazmunini yozing.
**Kutiladigan natija:** 3 ta ma'lumot.

## O'zingizni tekshiring

1. Versiya nazorati tizimi nima?
2. Git va GitHub farqi nimada?
3. Repository nima?
4. Commit'da qanday ma'lumotlar saqlanadi?
5. Branch nima uchun kerak?
6. README.md nima va u qayerda ko'rinadi?
7. Yaxshi commit xabari qanday bo'ladi?

## Uyga vazifa

GitHub'da repository yarating (yoki daftarda «commit kartochkalari»ni chizing), README'ni Markdown'da to'ldiring va kamida 2 ta commit qiling. 20–30 daqiqa. Batafsil — haftalik uyga vazifada.
