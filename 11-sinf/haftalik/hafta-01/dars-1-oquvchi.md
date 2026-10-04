# 1-dars. IT ekotizimi qatlamlari, SDLC bosqichlari va jamoadagi rollar

> Siz har kuni ishlatadigan ilova ortida ko'zga ko'rinmaydigan butun bir «shahar» bor: qatlamlar, serverlar va jamoa. Bugun uni xaritaga tushiramiz va o'z portfolio-loyihangiz uchun birinchi professional hujjatni yozamiz.

## Dars xulosasi

- IT ekotizimi — foydalanuvchi, ilova, ma'lumotlar, tarmoq va infratuzilma bir butun bo'lib ishlaydigan tizim.
- 4 qatlam: klient (brauzer, mobil ilova), ilova (backend, API), platforma (DB, kesh, navbat), infratuzilma (server, bulut, OS).
- Qatlamlash murakkablikni boshqaradi: muammo izolyatsiya qilinadi, qatlamni almashtirish va kengaytirish osonlashadi.
- SDLC — dasturiy ta'minotning hayotiy sikli: talab, dizayn, kod, test, deploy/release, monitoring.
- Har bosqich aniq artefakt bilan tugaydi (SRS, ERD, kod, test protokoli, release note, loglar).
- Kod yozish SDLC ning faqat bitta bo'lagi; monitoringdan yangi talablar keladi, sikl takrorlanadi.
- Waterfall — ketma-ket oqim; Agile — shu bosqichlarning qisqa takrorlanishi (sprint).
- Jamoada rollar bor (PO, analitik, arxitektor, developer, QA, DevOps/SRE); yolg'iz ishlasangiz hammasini siz bajarasiz.

## Qo'shimcha ma'lumot

### Nega «ekotizim» deyiladi?
Tabiiy ekotizimda har bir tur o'z vazifasini bajaradi va boshqalarga bog'liq. IT'da ham shunday: brauzer, API, ma'lumotlar bazasi, bulut, kuzatuv tizimi o'z rolini bajaradi. Bittasi uzilsa, boshqalar ta'sirlanadi. Shuning uchun muhandis «mening kodim» bilan emas, butun tizim bilan fikrlashi kerak.

### Restoran o'xshatishi
Restoranni tasavvur qiling. **Klient** — zal va menyu (mehmon ko'radigan qism). **Ilova** — oshpaz va ofitsiantlar: buyurtmani qabul qilib, qoidalar bo'yicha bajaradi. **Platforma** — ombor, muzlatgich, retseptlar daftari (ma'lumot va xizmatlar). **Infratuzilma** — bino, gaz, elektr, suv. Mehmon oshxonaga kirmaydi, oshpaz binoning elektr simini bilmaydi: har biri o'z qatlamida. Shu tufayli oshxonani almashtirsangiz ham zal o'zgarmay qolishi mumkin.

### So'rov qatlamlarni qanday kesib o'tadi?
Terminalda quyidagini sinab ko'ring (internet kerak):

```bash
curl -s https://api.github.com/zen
curl -sI https://api.github.com | head -3
```

`curl` — klient. `api.github.com` — ilova (API) qatlami: u so'rovni qabul qilib, javob qaytaradi. Ichkarida GitHub ma'lumotlar bazasi va minglab server bor, lekin siz ularni ko'rmaysiz. Buning o'zi qatlamlashning foydasi: siz faqat interfeysni (API) bilasiz.

### Artefakt nima va nega muhim?
Artefakt — bosqich natijasida paydo bo'ladigan **aniq, tekshiriladigan narsa**: hujjat, diagramma, kod, test natijasi. «Talabni tushundim» — hissiyot; `SRS.md` — artefakt. Artefakt bo'lmasa, keyingi bosqich nimaga tayanishini bilmaydi, tushunmovchilik va qayta ish ko'payadi.

```
Yomon talab:  «Sayt tez va chiroyli bo'lsin»
Yaxshi talab: «Bosh sahifa oddiy aloqada 3 soniyadan kam ochiladi;
               360 px ekranda gorizontal surish chiqmaydi»
```

Yaxshi talab **aniq, o'lchanadigan va testlanadigan** bo'ladi.

### Deploy va release bir narsa emas
*Deploy* — kodni serverga joylash (texnik amal). *Release* — foydalanuvchilarga yangi versiyani ko'rsatish qarori. Ikkalasi bir vaqtda bo'lishi shart emas: kod deploy qilingan, ammo «feature flag» orqali hozircha yashirilgan bo'lishi mumkin. Release'ga albatta **rollback rejasi** (agar xato chiqsa, qanday qaytamiz) kiradi.

### Odatiy xatolar
- «Dasturchi = kod yozuvchi» deb o'ylash. Real loyihada vaqtning katta qismi talab, review, test va muloqotga ketadi.
- Talab bosqichini tashlab, to'g'ridan-to'g'ri kodlashga o'tish: eng qimmat xato kech topiladi.
- SDLC ni «bir marta o'tiladigan yo'l» deb tushunish. Ish ekspluatatsiyada tugamaydi, yangi sikl boshlanadi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| IT ekotizimi | Texnik infratuzilma, ilovalar, ma'lumotlar va foydalanuvchi xizmatlarining o'zaro bog'langan majmuasi |
| Qatlamlash (layering) | Tizimni mas'uliyati aniq ajratilgan qatlamlarga bo'lish |
| API | Qatlamlar/dasturlar bir-biri bilan gaplashadigan aniq interfeys |
| Backend | Server tomonidagi ilova mantig'i (biznes qoidalari) |
| Infratuzilma | Serverlar, bulut, tarmoq, OS: tizimning texnik poydevori |
| SDLC | Software Development Life Cycle: dasturiy ta'minotning hayotiy sikli |
| Artefakt | Bosqich natijasi: hujjat, diagramma, kod, test protokoli |
| SRS | Software Requirements Specification: dasturiy talablar spetsifikatsiyasi |
| User story | «Foydalanuvchi sifatida men ... xohlayman, shunda ...» ko'rinishidagi talab |
| Qabul mezoni | Talab bajarilganini tekshiradigan aniq shart (acceptance criteria) |
| Waterfall / Agile | Ketma-ket oqim modeli / qisqa takrorlanuvchi iteratsiyalar modeli |
| Deploy / Release | Kodni muhitga joylash / foydalanuvchilarga versiyani ochish qarori |

## Bilasizmi?

- «Bug» so'zi bilan bog'liq mashhur rivoyat bor: 1947 yilda Harvard Mark II kompyuterida haqiqiy kuya (moth) topilgan va daftarga yopishtirib qo'yilgan. Bu tarixiy hikoya, lekin so'zning o'zi undan oldin ham ishlatilgan.
- Dasturiy ta'minot bir necha yil yashaydi: yozishdan ko'ra uni qo'llab-quvvatlashga ko'proq vaqt ketadi, shuning uchun SDLC da oxirgi bosqich ham bor.
- Katta kompaniyalarda SRE (Site Reliability Engineer) degan alohida kasb bor: uning ishi tizim ishonchliligini ta'minlash.
- Bir kishilik freelance loyihada ham siz birdaniga product owner, dasturchi, QA va DevOps bo'lasiz. Shuning uchun hamma rolni tushunish ish beruvchi oldida ustunlik.
- Testlash piramidasida asosni ko'p miqdordagi kichik, tez unit testlar tashkil qiladi, tepada esa kam sonli «oxirigacha» (end-to-end) testlar turadi.

## Topshiriqlar

### 1. Qatlam nomlari · oson
Quyidagi 8 ta narsani 4 qatlamga ajrating: Chrome brauzeri, PostgreSQL, Linux serveri, Redis, mobil ilova, REST API serveri, AWS bulut, admin panel.

**Kutiladigan natija:** to'rtta ro'yxat, har birida 2 ta element.

### 2. Bu qaysi bosqich? · oson
Har bir artefakt qaysi SDLC bosqichida paydo bo'ladi? ERD, bug-raport, release note, user story, changelog.

**Kutiladigan natija:** 5 ta artefakt va ularning bosqichi.

### 3. Birinchi curl · oson
Terminalda `curl -s https://api.github.com/zen` ni ishga tushiring. Uch marta qaytaring. Natija har safar bir xilmi? Bu so'rovda qaysi qatlam klient, qaysi biri ilova?

**Kutiladigan natija:** olingan gaplar va ikki jumlali izoh. Internet bo'lmasa, brauzerda shu manzilni oching.

### 4. Gitni tekshiring · oson
Terminalda `git --version` ni yozing. Chiqqan versiyani daftaringizga yozing. Agar xato chiqsa, ekrandagi xabarni nusxalab qo'ying va mentorga ko'rsating.

**Kutiladigan natija:** o'rnatilgan Git versiyasi (yoki aniq xato matni).

### 5. Sevimli ilovangiz xaritasi · o'rta
Sevimli ilovangizni tanlang (o'yin, Telegram, bank ilovasi). 4 qatlam bo'yicha jadval tuzing: har qatlamda kamida 3 komponent. Taxmin qilgan joylaringizni «?» bilan belgilang. Foydalanuvchi bitta tugmani bosganda (masalan, «to'lov») so'rov qatlamlar orqali qanday o'tishini strelkalar bilan chizing.

**Kutiladigan natija:** jadval + 4–6 qadamli yo'l sxemasi.

### 6. Yomon talabni tuzating · o'rta
Quyidagi talablar yomon. Har birini aniq, o'lchanadigan va testlanadigan qilib qayta yozing: (a) «Ilova tez ishlasin». (b) «Dizayn chiroyli bo'lsin». (c) «Xavfsiz bo'lsin».

**Kutiladigan natija:** har talab uchun kamida 2 ta qabul mezoni.

### 7. Waterfall yoki Agile? · o'rta
Ikki holat: (a) davlat idorasi uchun talablari qat'iy belgilangan va o'zgarmaydigan hisobot tizimi; (b) yangi mobil o'yin: foydalanuvchi fikriga qarab har hafta o'zgaradi. Har birida qaysi yondashuv qulay va nega? Bir kamchiligini ham yozing.

**Kutiladigan natija:** har holat uchun tanlov, 2 sabab va 1 kamchilik.

### 8. Rollar xaritasi · o'rta
Siz portfolio-loyihada yolg'iz ishlayapsiz. SDLC ning 6 bosqichi uchun jadval tuzing: bosqich — qaysi rolda ishlaysiz — bu rolda qiladigan konkret ishingiz.

**Kutiladigan natija:** 6 qatorli jadval.

### 9. Mini-SRS · qiyin
`SRS-mini.md` faylini yarating: bir jumla maqsad, portfolio-loyiha uchun 5 ta user story, har biriga kamida 2 ta qabul mezoni, 3 ta «nimani qilmaydi» cheklovi. Mezonlarda son yoki tekshiriladigan shart bo'lsin.

**Kutiladigan natija:** to'liq fayl; hech bir mezon «chiroyli», «tez» kabi mavhum emas.

### 10. Xato qaysi bosqichda? · qiyin
Uch voqea: (a) mijoz tayyor ilovani ko'rib «men buni so'ramagan edim» dedi. (b) Yangilanishdan keyin ilova ishlamay qoldi va eskisiga qaytib bo'lmayapti. (c) Ilovada qaysi funksiyadan foydalanishayotgani umuman noma'lum. Har biri uchun: qaysi bosqichda nima yetishmagan, qaysi artefakt yordam berardi, bir chora.

**Kutiladigan natija:** 3 voqea × (bosqich, sabab, artefakt, chora).

### 11. SDLC halqasi sxemasi · qiyin
Portfolio-loyihangiz uchun SDLC ni halqa shaklida chizing (qo'lda yoki oddiy vosita): har bosqichga bitta konkret artefakt nomini yozing (fayl nomi bilan), keyin monitoringdan talabga qaytuvchi o'q ustida bitta real «fikr-mulohaza» misoli (masalan, «tashrifchilar kontakt tugmasini topolmayapti»).

**Kutiladigan natija:** bitta sxema, 6 bosqich, 6 artefakt, 1 ta qaytish o'qi misoli bilan.

### 12. Bonus: ish e'lonlarini tadqiq qiling · bonus
Ish qidirish saytlaridan (masalan, hh.uz yoki LinkedIn) 3 ta Junior developer e'lonini toping. Ularda keltirilgan talablardan nechtasi bugungi mavzu bilan (Git, SDLC, Agile, CI/CD, testlash, jamoada ishlash) bog'liq? Eng ko'p uchraydigan 3 ta atamani sanab chiqing.

**Kutiladigan natija:** 3 e'lon havolasi, atamalar jadvali va bir jumlali xulosa.

## O'zingizni tekshiring

1. IT ekotizimining 4 qatlamini ayting va har biriga misol keltiring.
2. Qatlamlash nima uchun foydali? Kamida ikkita sabab ayting.
3. SDLC ning 6 bosqichini tartib bilan sanang.
4. Artefakt nima va nega «hissiyot» bilan bosqichni tugatib bo'lmaydi?
5. Nima uchun SDLC «sikl» deyiladi?
6. Deploy va release o'rtasida qanday farq bor?
7. Yaxshi talab qanday xususiyatlarga ega?
8. Waterfall va Agile asosiy farqi nimada?

## Uyga vazifa

**«Portfolio-loyiha: talab» (20–30 daqiqa).** Darsda boshlagan `SRS-mini.md` ni yakunlang (5 user story, mezonlar, cheklovlar). Qo'shimcha: sevimli ilovangizning 4 qatlamli xaritasini toza chizib, rasmini yoki fotosini saqlang. Oxirida `git --version` ishlashini tekshiring: keyingi darsda Git bilan ishlaymiz.
