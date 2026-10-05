# Umumiy qoidalar (barcha sinf agentlari uchun)

Bu fayl `<sinf>` = `8-sinf`, `9-sinf` yoki `11-sinf` uchun bir xil. Sinfga xos ma'lumotlar (xarita, manbalar, o'quvchilar soni, daraja) agentning o'z faylida. Quyida `<sinf>` o'rniga o'z sinf papkangni qo'y.

## Vazifa

Mentor hafta raqamini (masalan «5-hafta») yoki mavzuni beradi. Hafta raqami berilsa, dastur bo'yicha shu haftaga to'g'ri keladigan 3 ta darsni (jami 3 × 80 daqiqa) aniqla. Oldingi haftalarning materiallari `<sinf>/haftalik/` ichida bo'lsa, ularni o'qi va mavzularning ketma-ketligini buzma.

Har bir dars uchun:

1. **Dars rejasi** — maqsad, kutiladigan natija, daqiqalar bo'yicha taqsimot (takrorlash → yangi mavzu → amaliyot → xulosa, tanaffus 5–10 daqiqa).
2. **Konspekt** — mentor o'quvchilarga tushuntiradigan matn, sodda til, shu sinf yoshiga mos misollar.
3. **Kod namunalari** — ishlaydigan, izohli. Yozishdan oldin mantiqan tekshir (imkon bo'lsa Bash orqali).
4. **Amaliy topshiriqlar** — 3 daraja: oson, o'rta, qiyin (kuchli o'quvchi uchun qo'shimcha). Har biriga kutiladigan natija va yechim (`dars-K.md` da; `**Yechim:**` belgisi bilan boshla, sayt generatori shu belgi bo'yicha yechimlarni kesadi).
5. **Tezkor nazorat** — 3–5 ta savol dars oxiri uchun.
6. **Uyga vazifa** — qisqa, 20–30 daqiqalik.
7. **O'quvchi sahifasi** (`dars-K-oquvchi.md`) va **slaydlar** — pastdagi qoidalar bo'yicha.

Haftalik umumiy qism:
- Hafta xulosasi va keyingi haftaga ko'prik.
- Dasturdagi baholash mezonlariga mos baholash jadvali (guruhdagi o'quvchilar soniga mos bo'sh shablon; o'quvchilar soni sinf agentida ko'rsatilgan).
- Agar bu haftada oraliq yoki yakuniy nazorat/loyiha ishi bo'lsa, topshiriq va baholash mezonini alohida tayyorla.

## Asosiy qoida: Ma'lumot manbai (Hujjatga qat'iy tayanish)

1. **Barcha asosiy materiallar — FAQAT o'zimizning rasmiy hujjatlarimizdan olinadi:**
   Har bir sinf va yo'nalishning o'z papkasida rasmiy tasdiqlangan hujjatlari mavjud (`<sinf>/_matn/*.txt` va `.docx`).
   - Dars mavzulari va rejasi;
   - Nazariy ma'lumotlar, ta'riflar va qoidalar;
   - Rasmiy texnik atamalar va tushunchalar;
   - Kod namunalari, sintaksis va arxitektura;
   - Amaliy topshiriqlar va mashqlar
   **FAQAT VA FAQAT** shu sinf/yo'nalishning rasmiy hujjatlaridan olinishi shart! Hujjatda yo'q narsalarni asosiy mavzuga to'qib chiqarish, o'zboshimchalik bilan mavzuni o'zgartirish yoki tashqi dasturlardan mavzu kiritish qat'iyan man etiladi.

2. **Qo'shimcha ma'lumotlar (Internetdan foydalanish chegarasi):**
   Internetdan FAQAT ikkinchi darajali, darsni boyituvchi qo'shimcha elementlar uchungina foydalanish mumkin:
   - `## Bilasizmi?` bo'limi uchun qiziqarli faktlar va IT statistikasi;
   - Mavzuni o'quvchilarga sodda tushuntirish uchun hayotiy o'xshatishlar (analogiyalar);
   - Zamonaviy sohadagi qiziqarli keyslar va amaliy kontekst.
   Lekin darsning barcha asosiy o'zagi va o'rgatiladigan materiallari 100% o'zimizning rasmiy hujjatimizga tayanishi shart!

## Chiqish formati

Fayllarni mana bunday saqla (papkalarni o'zing yarat):

```
/Users/dev/AXV Mentor/<sinf>/haftalik/hafta-NN/
  dars-1.md            mentor uchun: reja, konspekt, kod, topshiriqlar YECHIMLARI bilan, nazorat javoblari
  dars-2.md
  dars-3.md
  dars-1-oquvchi.md    O'QUVCHI uchun sahifa (saytda alohida ekran ochiladi). Yechimlar YO'Q
  dars-2-oquvchi.md
  dars-3-oquvchi.md
  dars-1-slaydlar.html slaydlar: FAQAT <section>lar (qobiqsiz). Mentor izohlari saytga chiqmaydi
  dars-2-slaydlar.html
  dars-3-slaydlar.html
  dars-K-slayd.html    to'liq sahifa: slayd_yigish.py o'zi yaratadi (qo'lda yozilmaydi, tahrirlanmaydi)
  uyga-vazifa.md       "## Mentor uchun" bo'limidan tashqari hammasi saytga chiqadi
  baholash.md          faqat mentor uchun, saytga chiqmaydi
```

Raqamlash: fayl nomidagi K = haftadagi dars (1–3). Xaritadagi umumiy dars raqami = 3 × (hafta − 1) + K. `dars-K.md` va `dars-K-oquvchi.md` sarlavhasi (H1) umumiy raqam bilan boshlanadi: `# 4-dars. Mavzu nomi`. Slayddagi belgi: `<N>-hafta · <umumiy raqam>-dars`.

Markdown yoz, kodni ``` bloklarida ber.

## O'quvchi sahifasi (`dars-K-oquvchi.md`)

Sayt har bir darsni alohida ekran qilib ochadi, uning mazmuni shu fayldan olinadi. Bu sahifa slaydning nusxasi EMAS: slaydda yo'q qo'shimcha ma'lumot va ko'p topshiriq beradi. O'quvchi (siz deb murojaat qil, qiziqarli va aniq yoz) uni uyda o'qib, mashq qiladi. Fayl OCHIQ internetga chiqadi, shuning uchun yechim, to'liq javob kodi, mentor izohi yozma.

Tuzilma (shu tartib va aniq `##` sarlavhalar):

1. `# <umumiy raqam>-dars. <mavzu>`, undan keyin bitta `> ...` qator: darsning 1–2 jumlalik qiziqarli tavsifi (saytda kartada ko'rinadi).
2. `## Dars xulosasi` — 5–8 qisqa band: darsda nima o'rganildi.
3. `## Qo'shimcha ma'lumot` — slaydda yo'q chuqurroq tushuntirish: 3–5 ta `###` mini-bo'lim, hayotiy o'xshatishlar, izohli kod namunalari, «nega shunday?» javoblari, odatiy xatolar.
4. `## Atamalar lug'ati` — jadval: `| Atama | Ma'nosi |`, 6–12 ta atama (terminlar glossariy bilan bir xil).
5. `## Bilasizmi?` — 3–5 qiziqarli fakt (ro'yxat).
6. `## Topshiriqlar` — **kamida 10 ta**: 4 oson, 4 o'rta, 3 qiyin, 1 bonus. Har bir topshiriq sarlavhasi aynan shunday: `### 3. Nomi · oson` (daraja qo'shimchasi: ` · oson`, ` · o'rta`, ` · qiyin`, ` · bonus`; sayt buni rangli belgi qiladi). Har birida aniq shart va `**Kutiladigan natija:** ...`. Topshiriqlar turli xil: kod yozish, xatoni topish, bashorat qilish («bu kod nima chiqaradi?»), kichik mini-loyiha, tadqiqot. Yechim YOZMA (yechimlar faqat `dars-K.md` da).
7. `## O'zingizni tekshiring` — 5–8 savol, javobsiz.
8. `## Uyga vazifa` — `uyga-vazifa.md` dagi shu dars vazifasi qisqacha (20–30 daqiqa).

## Slaydlar (reveal.js)

Har bir dars uchun `dars-K-slaydlar.html` yarat. Unda **faqat `<section>` slaydlar** bo'ladi: `<!doctype>`, `<head>`, `<script>`, logo, `<div class="reveal">` YOZMA. Bularning hammasi (uslublar, reveal sozlamalari, logo, mavzu tugmasi, ikonkalar) umumiy qobiqda: `shablon/slayd-qobiq.html`; `python3 slayd_yigish.py` har slayd faylini shu qobiqqa o'rab to'liq `dars-K-slayd.html` yaratadi.

Boshlang'ich fayl: `/Users/dev/AXV Mentor/shablon/slaydlar.html` (14 xil slayd NAMUNASI: sarlavha, bo'lim, kartalar, statistika, SVG sxema, vaqt chizig'i, vs, kod, auto-animate, qadamlar, vertikal slayd, topshiriq, xulosa). Kerakli bloklarni nusxalab, mazmunni almashtir, keraksizlarini o'chir. Rasm yo'li uchun `{{UP}}` belgisi: masalan `<img class="logo-big" src="{{UP}}reveal/logo.png" alt="AXV">` (sarlavha slaydida bo'lishi shart). Sarlavha (`<title>`) birinchi `<h1>` dan olinadi. Avval namunani va `reveal/dars.css` ni o'qi: faqat tayyor sinflardan foydalan, o'z CSS'ingni yozma (bitta-ikkita `style` atributi mumkin).

**Maqsad: ko'rkam, keng ko'lamli, jonli slaydlar, primitiv emas.** Kino/taqdimot darajasida: katta illyustratsiyalar, bosqichma-bosqich paydo bo'lish, silliq o'tishlar. Oddiy «sarlavha + 4 band» slaydlar ko'p bo'lmasin.

Hajm va tuzilma: **20–28 slayd** (gorizontal), 80 daqiqalik dars uchun. Tartib: sarlavha (`hero`) → bo'lim slaydlari (`sec`, 01/02/03... har katta qism oldidan) → nazariya + vizual → kod → odatiy xato → amaliyot (`task`, 3 daraja, vaqt bilan) → xulosa. Har slaydda **bitta fikr**; ekranga sig'sin (1280×720): matn 6 bandgacha, kod 12 qatorgacha.

Majburiy vizual ish (har darsda):
- **Kamida 4 ta katta SVG illyustratsiya** (`<div class="illus"><svg viewBox="...">`): sxema, jarayon, anatomiya (teg, manzil, fayl strukturasi), «ichki ko'rinish», o'xshatish rasmi. Qismlarini `<g class="fragment">` bilan birin-ketin chiqar. Oqimlar uchun `class="... flowing"` (harakatlanuvchi chiziq), diqqat uchun `pulse`.
- **SVG ranglari FAQAT sinflar orqali** (tema almashganda mos tushishi uchun): to'ldirish `fa` (ko'k), `fb` (to'q sariq), `fc` (feruza), `fg` (yashil), `fn` (neytral); chiziq `la lb lc lg ln`; strelka uchi `ar-a ar-b ar-c ar-g`; matn `t-head`, `t-accent`, `t-muted`. `#hex` rang va `rgba(...)` ishlatma (faqat `.browser` ichidagi sahifa maketi bundan mustasno).
- Qo'shimcha bloklar (shablonda namunasi bor): `.cards` (+ `.two/.three/.four`, `fragment fade-up`), `.stats` (katta raqamlar), `.timeline`, `.vs` (taqqoslash), `.steps-n` (raqamli qadamlar), `.quote` (o'xshatish), `.flow` (jarayon), `.chips`, `.browser` (brauzer maketi), jadval, `callout tip/warn/bad`.
- **Animatsiya**: `fragment` (fade-up, grow, highlight-current-blue) bilan bosqichma-bosqich ochish; kod uchun `data-line-numbers="1-5|3|4"` (qatorlarni birin-ketin ajratish); `data-auto-animate` bilan ikki slayd orasida elementlar silliq o'tishi (kod o'zgarishi, kattalashuvchi maket) — kamida 1 joyda.
- **Vertikal slaydlar** (ichma-ich `<section>`): asosiy fikr tepada, pastga bosganda chuqurroq «qo'shimcha» slaydlar. Mavzuga 2–3 joyda qo'lla.
- Quiz/savol slaydi: savol → fragment bilan javob (bitta-ikkita).
- Mavzuni o'quvchi hayotiga bog'la (o'yinlar, Telegram, Instagram, maktab sayti, ish bozori). Ma'lumotli bo'lsin: ta'rif, real misol, taqqoslash, «nega kerak?».
- Mavzuga mos tayyor maketlar: `.browser` (veb-sahifa), `.terminal` (buyruq qatori: DevOps, Git, Linux), `.phone` (ilova ekrani: UX/UI), `.swatches` (rang palitrasi). Namunalar shablonda emas, lekin `reveal/dars.css` da tayyor: sinflarni shu yerdan ko'r.

Ikonkalar va logo:
- **Emoji ISHLATMA.** Faqat Lucide ikonkalari: `<i data-ic="globe"></i>`. Nom = `/Users/dev/AXV Mentor/reveal/lucide/<nom>.svg` fayl nomi (globe, laptop, server, lock, target, puzzle, rocket, lightbulb, triangle-alert, circle-check, timer, book-open, code-xml, search, link, folder, file-text, settings...). Aniq bo'lmasa `ls reveal/lucide | grep <so'z>`. Ikonkalar oddiy chiziqli, fonsiz, rangi urg'u rangida. Joylashuv: kartada `<div class="icon"><i data-ic="..."></i></div>`, jarayonda `<span class="icon">...</span>`, strelkada `<div class="arrow"><i data-ic="arrow-right"></i></div>`, izohda matn oldidan. SVG illyustratsiya ichida ikonka kerak bo'lsa: Lucide faylidagi elementlarni ichki `<svg x y width height viewBox="0 0 24 24" class="ic-s" stroke-width="1.6">` ichiga joyla.
- Slaydlarni yozgach: `cd "/Users/dev/AXV Mentor" && python3 slayd_yigish.py` (ikonkalarni `reveal/ikonlar.js` ga yig'adi, noto'g'ri ikonka nomini ko'rsatadi va to'liq `dars-K-slayd.html` ni yaratadi). Usiz ikonkalar va to'liq sahifa bo'lmaydi.
- **Logo**: sarlavha slaydidagi `logo-big` ni o'zgartirma/o'chirma (burchakdagi kichik logo va mavzu tugmasi qobiqdan avtomatik keladi). Tashqi rasm, CDN, tashqi URL ishlatma; yo'llar uchun faqat `{{UP}}reveal/...`.
- Mentor izohlari `<aside class="notes">` ichida: nima deyish, qayerda to'xtab savol berish, taxminiy vaqt. Ular saytga chiqmaydi.

Telefonga moslik (majburiy): slayd telefonda (vertikal) avtomatik 760 px kenglikda ko'rinadi, `.cards`, `.stats`, `.vs`, `.cols`, `.flow` ustunga aylanadi. Shuning uchun: (a) tartib faqat shu bloklar bilan, qat'iy `px` kenglikli element qo'yma (SVG va `.browser` bundan mustasno); (b) SVG `viewBox` ~1000×(260–420) bo'lsin, matnlar `font-size` 22 dan kichik bo'lmasin; (c) katta tablitsa va 12 qatordan uzun kod qo'yma; (d) bitta slaydga 6 bandgacha matn. SVG telefonda gorizontal suriladi (tema.js shuni o'zi qiladi).

Tekshiruv (majburiy):
1. Strukturani tekshir: har `<section>` yopilgan, kodda `<` `>` escape qilingan, emoji yo'q, `slayd_yigish.py` xatosiz tugagan.
2. Imkon bo'lsa brauzerda ko'r: `cd "/Users/dev/AXV Mentor" && python3 -m http.server <port> &` → `mcp__Claude_Browser__navigate` (`hafta-NN/dars-K-slayd.html` ni oching; agar `tab-2` kabi tab bor bo'lsa uning `tabId` sini ber) → har slaydda `Reveal.slide(i)` qilib, `document.querySelector('.present').scrollHeight > 720` yoki ichidagi element ostki chegaradan chiqib ketayotganini tekshir. Kamida 5 ta turli slaydni skrinshot qil. Qorong'i va yorug' mavzuda (`document.documentElement.dataset.theme='light'`) ham bir-ikkitasini ko'r. Telefon o'lchamida (`resize_window preset mobile`, sahifani qayta yukla) 2–3 slaydni ko'r. Eslatma: brauzer skrinshoti 1–2 soniya kechikishi mumkin, slaydni almashtirgach 2–3 soniya kut. Server va emulyatsiyani oxirida to'xtat (`pkill -f "http.server <port>"`, `resize_window preset desktop`).
3. Brauzer tool'i yo'q bo'lsa, buni hisobotda aniq yoz («vizual tekshirilmadi»).

Sayt: yangi hafta tayyor bo'lgach saytni O'ZING qayta yig'ma va hech qayerga yuklama. Mentor `/sayt` buyrug'ini o'zi ishga tushiradi. Hisobotda shuni eslat.


## Animatsiya va interaktiv bloklar (majburiy)

Slaydlar jonli bo'lishi kerak. Barcha bloklarning namunasi: `shablon/slaydlar.html` (15–20-slaydlar). Har darsda **kamida**: 3 ta animatsiyali ikonka, 1 ta mini-test (`.quiz`) va yana 2 ta boshqa interaktiv blok (`.flip`, `.stepper`, `.swap`, `[data-tip]` izohli SVG, `.count`).

- **Animatsiyali ikonka:** `<i data-ic="rocket" data-anim="float"></i>`. `data-anim`: `float`, `pulse`, `spin`, `bounce`, `wiggle`, `blink`, `draw` (slayd ochilganda kontur chiziladi). Ma'noga mos tanla: `pulse` (signal, jonli), `spin` (jarayon), `float` (kartadagi bosh ikonka), `draw` (muhim tushuncha).
- **`.flip`** — bosilganda aylanadigan karta (termin → ta'rif). `<div class="flip"><div class="flip-in"><div class="face front">…</div><div class="face back">…</div></div></div>`.
- **`.quiz`** — mini-test: `<div class="quiz"><p class="q">…</p><div class="opts"><button class="opt" type="button">…</button><button class="opt" type="button" data-ok>…</button></div><div class="explain">…</div></div>`. To'g'ri javobga `data-ok`.
- **`.stepper`** — qadam-baqadam: ichida `<div class="stp on">…</div><div class="stp">…</div>`; tugmalar avtomatik.
- **`.swap`** — «oldin / keyin»: `.swap-tabs` ichida 2 ta `button`, keyin 2 ta `.swap-p`.
- **`data-tip="izoh"`** — SVG `<g>` yoki istalgan element ustiga olib borilganda/bosilganda izoh chiqadi. SVG qismlarini tushuntirish uchun ishlat.
- **`.count`** — `<span class="count" data-to="5" data-suf=" mlrd+">0</span>`: raqam slayd ochilganda 0 dan sanaladi.
- Interaktiv blokdagi tugmalar telefonda ham bosiladi. Boshqa JavaScript YOZMA: `<script>` qo'shish mumkin emas, hammasi `reveal/interaktiv.js` da.

## Sinflarni o'ylab topma (majburiy)

Faqat `reveal/dars.css` da bor CSS sinflarini ishlat. `browser-bar`, `vs-a`, `text-sm`, `mb-2`, `grid-2`, `term-prompt`, `logo-hero` kabi sinflar YO'Q: ular slaydni buzadi. Brauzer maketi: `.browser > .bar > i,i,i,span` + `.page` (namuna shablonda). Terminal: `<pre class="terminal"><code class="language-bash">`. Ketma-ket tekshiruv:

1. `python3 slayd_lint.py <sinf>/haftalik/hafta-NN` — noma'lum sinflar, birinchi slayd `hero`/`logo-big`, ikonka nomlari, emoji, rang va URL. Muammo bo'lsa tuzatmay topshirma.
2. Brauzerda `shablon/slayd_audit.js` (fayl boshidagi izohga qara): ekrandan chiqish, kesilgan matn, bir-birini bosgan matn, SVG matn chegarasi, juda kichik shrift, topilmagan ikonka.


## Testlar (har dars uchun va haftalik)

Har tayyor hafta uchun **4 ta test fayli** yoziladi (slaydlar bilan bir papkada, xuddi shu qoidalar: faqat `<section>`lar, `.quiz` bloki):

- `dars-K-test-slaydlar.html` — shu darsning **10 ta** savoli (K = 1–3).
- `hafta-test-slaydlar.html` — butun haftaning **20 ta** savoli: har darsdan 5–6 ta (darsdagi testlarni takrorlama, yangi savollar) + 3–4 ta darslarni bog'laydigan savol.

Tuzilma: 1-slayd `hero` (logo-big, sarlavha «N-dars testi» / «N-hafta testi», 10 yoki 20 savol, taxminiy vaqt) → har savol alohida `<section>` (`<h2>Savol i/10</h2>` + `.quiz`) → oxirgi `<section>`: xulosa (`Natijangiz`, nimani takrorlash kerak).

Savol qoidalari:
- Mazmun faqat shu hafta darslaridan (`dars-K.md`, `dars-K-oquvchi.md`, slaydlar) va rasmiy hujjatdan (`_matn`). Tashqaridan savol yo'q.
- 4 ta variant, bittasi to'g'ri (`data-ok`); to'g'ri javob o'rni savollar bo'ylab aralash bo'lsin (hammasi 2-variant bo'lmasin). Noto'g'ri variantlar ishonarli (odatiy xatolar), kulgili emas.
- `.explain` da nega to'g'ri ekani 1–2 jumlada. Savol 2 qatordan oshmasin, variant 1 qatordan; kod bo'lsa 4 qatorgacha.
- Daraja: ~4 ta oson (atama), ~4 ta o'rta (tushunish/kod o'qish), ~2 ta qiyin (vaziyat/xato topish).
- Yechimlar uyga vazifa yechimi emas, shuning uchun `.explain` ochiq bo'lishi mumkin. Emoji, `#hex`, tashqi URL yo'q.
- Yozgach: `python3 slayd_yigish.py && python3 slayd_lint.py <hafta papkasi>`.
