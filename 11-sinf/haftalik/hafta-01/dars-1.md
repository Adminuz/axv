# 1-dars. IT ekotizimi qatlamlari, SDLC bosqichlari va jamoadagi rollar

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 1-dars (umumiy 1–51)

> Dasturda «Axborot texnologiyalari ekotizimi, SDLC va versiyalarni boshqarish (Git/GitHub)» mavzusiga 3 dars ajratilgan (1–3). Bo'linish: 1-dars — IT ekotizimi qatlamlari, SDLC bosqichlari, artefaktlar, jamoa rollari; 2-dars — Git asoslari (repository, commit, branch, merge, lokal amaliyot); 3-dars — GitHub (remote, push/pull/clone, README, .gitignore, Issues).

## 1. Dars rejasi

**Maqsad:** o'quvchi har qanday zamonaviy ilovani qatlamlarga ajratib tasvirlaydi, SDLC ning 6 bosqichini, ularning artefakt va rollarini biladi, o'z mini-loyihasi uchun birinchi hujjatni (mini-SRS) yozadi.

**Kutiladigan natija:**
- IT ekotizimi qatlamlarini (klient — ilova — platforma — infratuzilma) va ular o'rtasidagi aloqani (API, so'rov) tushuntiradi.
- SDLC ning 6 bosqichini (talab, dizayn, kod, test, deploy, monitoring/ekspluatatsiya), har bosqichning asosiy savoli va artefaktini aytadi.
- Waterfall va Agile (iteratsiya) farqini, SDLC «sikl» ekanini tushunadi.
- Jamoadagi asosiy rollarni (PO, analitik, arxitektor, dasturchi, QA, DevOps/SRE) farqlaydi.
- Kurs davomida rivojlantiriladigan **portfolio mini-loyihasi** uchun 5 ta user story + qabul mezoni yozadi.
- Kompyuterida `git` o'rnatilganini tekshiradi (2-dars uchun tayyorgarlik).

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 | Kirish | Kurs yo'li (17 hafta, 4 bob), mini-loyiha g'oyasi, diagnostika savollari |
| 5–25 | Yangi mavzu 1 | IT ekotizimi: 4 qatlam, qatlamlash nima uchun kerak, so'rov yo'li |
| 25–30 | Tanaffus | |
| 30–50 | Yangi mavzu 2 | SDLC: 6 bosqich, artefaktlar, Waterfall vs Agile, rollar |
| 50–72 | Amaliyot | Ilova xaritasi, mini-SRS, terminal tekshiruvi |
| 72–80 | Tezkor nazorat va xulosa | 5 savol, uyga vazifa, 2-darsga ko'prik |

## 2. Konspekt

### 2.1. Kirish va diagnostika (5 daqiqa)
Kursni tanishtiring: 51 dars, 4 bob — dasturiy ta'minot ishlab chiqish asoslari → DevOps/CI → bulut va deploy → freelance va startap. Maqsad: «kod yozadigan o'quvchi»dan «jamoada ishlay oladigan, loyihani yetkazib bera oladigan muhandis»ga o'sish. Shu kurs oxirida o'quvchida GitHub'da jonli portfolio bo'ladi.

Diagnostika (og'zaki, baholanmaydi): Telegram'da xabar yuborganingizda nima sodir bo'ladi? Dasturlash tilini bilish — dasturchi bo'lish uchun yetarlimi? GitHub'ni eshitganmisiz, ishlatganmisiz? Javoblar sizga o'quvchi darajasini ko'rsatadi: 2-3-darslar tempini shunga moslang.

### 2.2. IT ekotizimi nima?
**IT ekotizimi** — texnik infratuzilma, dasturiy ta'minot, ma'lumotlar, xavfsizlik mexanizmlari, tarmoqlar va foydalanuvchi xizmatlari bir-birini to'ldirib, yagona maqsadga xizmat qiladigan tizim. «Ekotizim» so'zi tasodifiy emas: har bir komponent (brauzer, mobil ilova, API, ma'lumotlar bazasi, bulut, kuzatuv tizimi) o'z rolini bajaradi va boshqalari bilan uyg'un ishlashi kerak.

**Nega qatlamlash?** Qatlamlash (layering) — murakkablikni boshqarishning eng samarali yo'li. Har qatlamning o'z mas'uliyat chegarasi bor va u faqat qo'shni qatlam bilan aniq interfeys orqali gaplashadi. Natijada: (1) muammo izolyatsiya qilinadi; (2) kengaytirish (scalability) va almashtirish (replaceability) osonlashadi; (3) xavfsizlik, monitoring va operatsion intizom soddalashadi.

> Eslatma (manbadagi farq): o'quv qo'llanma ekotizimni avval 3 qatlam deb (infratuzilma, platforma/dasturiy, foydalanuvchi xizmatlari), keyin amaliy tahlilda 4 qatlam deb beradi; o'quv dasturi esa «foydalanuvchi–ilova–platforma–infratuzilma» deydi. Dars 4 qatlamli modelni oladi; xaritadagi «ilova–platforma–infratuzilma» uchligi uning ichida, klient qatlami esa «ilova»ning ko'rinadigan yuzi.

| № | Qatlam | Tarkibi | Vazifasi |
|---|---|---|---|
| 1 | Foydalanuvchi / Klient | Web, mobil ilova, UI, brauzer | Foydalanuvchi bilan muloqot |
| 2 | Ilova (application) | Backend, API, biznes mantiq | Amaliy funksiyalarni bajarish |
| 3 | Platforma | DB, Redis (kesh), message queue, search | Ma'lumot va xizmatlarni boshqarish |
| 4 | Infratuzilma | Serverlar, bulut, tarmoq, OS | Resurslar, xavfsizlik, barqarorlik |

Qatlamlar bo'yicha:
- **Klient.** Foydalanuvchi ko'radigan qism. Tezlik, qulaylik, dizayn butun tizim sifatini belgilaydi. Sahifalar serverda tayyorlanishi (SSR/MPA) yoki brauzerda dinamik shakllanishi (SPA) mumkin.
- **Ilova.** Tizimning «miyasi»: buyurtma, to'lov, ro'yxatdan o'tish kabi biznes qoidalari. Monolit, modulli monolit, mikroxizmat yoki serverless bo'lishi mumkin. Qatlamlar bilan REST API, GraphQL yoki gRPC orqali gaplashadi. Autentifikatsiya, loglash, keshlash shu yerda.
- **Platforma.** Ilovaning tayanchi: ma'lumotlar bazasi (PostgreSQL, MySQL, MongoDB), kesh (Redis), navbat, qidiruv, obyekt saqlash. Tezlik va ishonchlilikka ta'sir qiladi. Misol: buyurtmalar relatsion DB'da, katalog keshda, hodisalar navbatda.
- **Infratuzilma.** Poydevor: serverlar, bulut (AWS, Azure, GCP), konteynerlar (Docker, Kubernetes), OS (Linux, Windows Server), tarmoq. Resurslar IaC (Terraform, Ansible) orqali ta'riflanadi; xavfsizlik WAF, IAM, TLS sertifikatlari bilan.

**Misol (soddalashtirilgan, o'quvchi hayotidan).** Telegram'ga rasm yuborasiz:
1. Klient: ilova rasmni siqadi va yuboradi.
2. Ilova: server so'rovni qabul qilib, kim kimga yuborayotganini tekshiradi.
3. Platforma: xabar ma'lumotlar bazasiga yoziladi, fayl saqlashga tushadi.
4. Infratuzilma: bularning hammasi ma'lumot markazlaridagi serverlarda ishlaydi.
Telegram ichki tuzilishi aynan shunday emas, misol faqat qatlam g'oyasini ko'rsatadi; buni o'quvchiga ayting.

**Mentor uchun nuqta:** bu qatlamlar kursning keyingi boblariga mos: 1-bob — ilova; 2-bob (Docker, Nginx, CI) — infratuzilma va platforma; 3-bob (bulut) — infratuzilma. «Hozir xaritani ko'rsatyapman, qo'lingizda qayerdaligingizni ko'rib turing.»

### 2.3. SDLC nima?
**SDLC (Software Development Life Cycle)** — dasturiy ta'minotning g'oyadan boshlab foydalanuvchiga yetkazilishi, ekspluatatsiyasi va oxirida arxivlanishi yoki yangisi bilan almashtirilishigacha bo'lgan bosqichlar ketma-ketligi. Asosiy fikr: **kod yozish SDLC ning faqat bitta bo'lagi.** Har bosqichning maqsadi, kirishi, chiqishi va **artefakti** (aniq, tekshiriladigan natija) bor; u keyingi bosqichga tayanch bo'ladi.

| № | Bosqich | Asosiy savol | Artefaktlar | Asosiy ishtirokchilar |
|---|---|---|---|---|
| 1 | Talablarni tahlil qilish | Nima qurmoqchimiz? | SRS, user stories, use-case diagrammalar | Product owner, biznes analitik, mijoz vakili |
| 2 | Loyihalash (Design) | Qanday quramiz? | Arxitektura diagrammalari, DB modeli (ERD), API spetsifikatsiyasi | Arxitektor, lead developer, DevOps, security engineer |
| 3 | Dasturlash (Development) | Kodda qanday ifodalaymiz? | Kod bazasi, konfiguratsiya, migratsiyalar, unit testlar | Backend/Frontend/Mobile developerlar, code reviewerlar |
| 4 | Testlash (Testing) | Ishlayaptimi va to'g'rimi? | Test ssenariylari, protokollar, bug-raportlar | QA, automation engineer, developer |
| 5 | Deploy/Release | Qayerda va qanday ishlatamiz? | Docker image, CI/CD YAML, release note, monitoring sozlamalari | DevOps, SRE, arxitektor, PO (release qarori) |
| 6 | Qo'llab-quvvatlash (Maintenance) / Monitoring | Qanday ushlab turamiz va rivojlantiramiz? | Loglar, metrikalar, patch versiyalar, changelog, runbook | SRE, support, monitoring jamoasi, PO |

(Dastur bu bosqichni «monitoring» yoki «ekspluatatsiya» deydi — bir xil narsa.)

**Axborot oqimi:** talab hujjatidan dizayn, dizayndan kod, koddan test natijalari, testdan release qarori, ekspluatatsiyadan yangi talablar. Oxirgi o'q halqani yopadi: **SDLC bir marta bajariladigan chizma emas, takrorlanadigan sikl.**

Bosqichlar bo'yicha qisqa tafsilot:
- **Talab.** Biznes maqsad, foydalanuvchi ehtiyoji, cheklovlar, muvaffaqiyat mezoni. Usullar: intervyu, workshop, mavjud yechimlarni o'rganish. Yaxshi talab aniq, o'lchanadigan va testlanadigan. Agile'da: *user story* («Foydalanuvchi sifatida men ... xohlayman, shunda ...») + *acceptance criteria* (qabul mezoni).
- **Dizayn.** «Nima?» dan «qanday?» ga o'tish: qatlamlar, servislar aloqasi, DB modeli, kesh/navbat strategiyasi, API. Monolit yoki mikroxizmat variantlari baholanadi.
- **Kod.** Dizayn kodga aylanadi. Kod Git repozitoriyda branch orqali boshqariladi, commitlar mazmunli xabar bilan, unit testlar bilan birga. Konfiguratsiya koddan ajratiladi (dev/stage/prod muhitlari).
- **Test.** Testlash piramidasi: pastda ko'p unit testlar, o'rtada integration, tepada kam end-to-end. Xavfsizlik, yuklama, performance testlari ham bor. Buglar issue-trackerda yuritiladi, testlar CI'da avtomatlashtiriladi (har commit/PR uchun «sifat darvozasi»).
- **Deploy/Release.** *Deploy* — texnik: artefaktni muhitga joylash. *Release* — foydalanuvchiga qaysi versiya ko'rinishi qarori. Usullar: blue-green, canary, feature flag. Artefaktlar: release note, versiya raqami (semver), alert, **rollback rejasi**.
- **Monitoring/qo'llab-quvvatlash.** Loglar, metrikalar (kechikish, xatoliklar, throughput), foydalanuvchi fikri. Qaysi sahifa sekin? Qaysi funksiyadan foydalanilmayapti? Bu ma'lumot yana talablarga qaytadi.

### 2.4. Waterfall va Agile
- **Waterfall:** bosqichlar ketma-ket qat'iy oqim (talab tugamaguncha dizayn boshlanmaydi). Talab aniq va o'zgarmaydigan loyihalarda qulay, lekin kech xato qimmatga tushadi.
- **Agile (Scrum, Kanban):** o'sha bosqichlar qisqa iteratsiyalar (sprint) ichida takrorlanadi; foydalanuvchi fikri tezroq keladi.
Metodologiya nima bo'lishidan qat'i nazar, **bosqichlar deyarli o'zgarmaydi; farq — ularning tashkil etilishida.** Muhim qoida: har bosqich «hissiyot» bilan emas, tekshiriladigan artefakt bilan tugaydi. (Agile/Scrum 49-darsda batafsil.)

### 2.5. Rollar
SDLC faqat texnika emas, tashkiliy tuzilma ham. Kichik jamoada (yoki freelance'da) bir odam bir necha rolni bajaradi; shuning uchun o'quvchi barchasini tushunishi kerak:
- **Product owner** — nima qurilishi va nima muhimligini hal qiladi.
- **Biznes analitik** — talablarni yig'adi, hujjatlaydi.
- **Arxitektor** — qatlam va texnologiyalarni tanlaydi.
- **Developer** (backend/frontend/mobile) — kod yozadi, bir-birining kodini review qiladi.
- **QA / automation engineer** — sifatni tekshiradi, testlarni avtomatlashtiradi.
- **DevOps / SRE** — deploy, infratuzilma, monitoring, ishonchlilik.
- **Security engineer** — xavfsizlik.
Savol: «Siz yolg'iz portfolio loyiha qilsangiz, qaysi rollarni bajarasiz?» (javob: hammasini; shuning uchun hujjat va tartib muhim).

### 2.6. Mini-loyiha: «portfolio» (amaliyot uchun kontekst)
Kurs davomida o'quvchi bitta loyihani rivojlantiradi: **shaxsiy portfolio-loyiha** (o'quvchi o'zi nom beradi; masalan, portfolio-sayt + loyihalar ro'yxatini beradigan oddiy API). Har hafta unga yangi professional element qo'shiladi: SDLC hujjati → Git repo → GitHub → PR → CI → deploy → case study. Bu 43–44-darslardagi «Portfolio, GitHub va case study» mavzusiga olib boradi. Texnologiya tanlovi o'quvchiniki (8–9-sinf kursidagi HTML/CSS/JS yoki Python — nimani bilsa); bugun texnologiya tanlash shart emas.

## 3. Namunalar

**Namuna 1 — so'rov qatlamlar orqali (terminal, real tekshiruv).** Klient (terminaldagi `curl`) ilova qatlamiga (GitHub API) so'rov yuboradi:
```bash
curl -s https://api.github.com/zen
# Mind your words, they are important.   (javob har safar boshqacha bo'lishi mumkin)

curl -sI https://api.github.com | head -3
# HTTP/2 200
# date: ...
# cache-control: public, max-age=60, s-maxage=60
```
Muhokama: bu qaysi qatlam? (`curl` — klient; `api.github.com` — ilova/API; ichkarida DB va serverlar — o'quvchi ko'rmaydi: bu qatlamlash.) Bu buyruqlar internet talab qiladi; ulanish bo'lmasa, `curl` o'rniga brauzerda `https://api.github.com/zen` ni oching.

**Namuna 2 — muhit tekshiruvi (2-dars uchun):**
```bash
git --version        # masalan: git version 2.50.1
python3 --version    # ixtiyoriy
```
Agar `git` yo'q bo'lsa: macOS — `xcode-select --install`; Windows — Git for Windows (git-scm.com); Linux — `sudo apt install git`. O'rnatishni mentor ko'rsatadi (dars vaqtini yemasligi uchun 2-dars boshidan oldin).

**Namuna 3 — user story shabloni va qabul mezoni:**
```
User story:
  Tashrif buyuruvchi sifatida men portfoliodagi loyihalar ro'yxatini
  ko'rishni xohlayman, shunda egasining ishlarini baholay olaman.

Qabul mezoni (acceptance criteria):
  1. Bosh sahifada kamida 3 ta loyiha kartasi ko'rinadi.
  2. Har bir kartada nom, qisqa tavsif va GitHub havolasi bor.
  3. Sahifa telefon ekranida ham o'qiladi (gorizontal surish yo'q).
```
Yaxshi mezon: aniq, o'lchanadigan, testlanadigan. Yomon: «sayt chiroyli bo'lsin».

**Namuna 4 — artefaktlar zanjiri (mini-loyiha uchun):**
```
Talab:    SRS-mini.md (5 user story)
Dizayn:   arxitektura sxemasi (qatlamlar), sahifalar ro'yxati
Kod:      Git repozitoriy (2-3-darslarda)
Test:     qo'lda test ro'yxati (checklist)
Deploy:   GitHub Pages / hosting (keyingi boblarda)
Monitoring: tashrif/xato kuzatuvi (keyingi boblarda)
```

## 4. Amaliy topshiriqlar

### Oson — Ilova xaritasi (10 daqiqa)
O'zingiz kunda ishlatadigan ilovani tanlang (Telegram, Instagram, Click/Payme, o'yin). Daftarga 4 qatlamli jadval chizing va har qatlamga kamida 2 ta komponent yozing (nimaligini taxmin qilsangiz bo'ladi, lekin «taxmin» deb belgilang).
**Kutiladigan natija:** 4 qatlam × 2 komponent; klient ↔ ilova o'rtasidagi aloqa nomi (API/so'rov) ko'rsatilgan.
**Yechim:** Namuna (Instagram, taxmin): Klient — mobil ilova, veb-sayt; Ilova — API serveri, rasm yuklash xizmati; Platforma — ma'lumotlar bazasi (profil, izohlar), kesh (lentani tezlatish), fayl saqlash (rasmlar); Infratuzilma — ma'lumot markazlaridagi serverlar, tarmoq/yuklama balansirovkasi. Klient↔ilova: HTTPS orqali API so'rovlari. Qabul qilish mezoni: har komponent bitta qatlamga to'g'ri joylangan; masalan «DB» ni klientga qo'ysa — qatlam vazifasini qayta tushuntiring.

### O'rta — Mini-SRS (20 daqiqa)
`SRS-mini.md` yarating (matn muharriri, hozircha Git'siz). Portfolio-loyiha uchun: bir jumla maqsad; 5 ta user story; har birida kamida 2 ta qabul mezoni; «loyiha nimani qilmaydi» (3 ta cheklov).
**Kutiladigan natija:** fayl 5 user story, 10+ qabul mezoni bilan; mezonlar o'lchanadigan.
**Yechim:** Namuna:
```markdown
# Portfolio-loyiha: mini-SRS
**Maqsad:** o'zimning loyihalarimni ish beruvchi/mijozga ko'rsatadigan sahifa.

## User stories
1. Tashrif buyuruvchi sifatida men loyihalar ro'yxatini ko'rishni xohlayman, shunda ishlarni baholayman.
   - Bosh sahifada kamida 3 karta; har kartada nom, tavsif, GitHub havolasi.
2. Tashrif buyuruvchi sifatida men egasi bilan bog'lanishni xohlayman.
   - Kontakt bo'limida Telegram va email havolalari bor.
   - Havolalar bosilganda ishlaydi.
3. Tashrif buyuruvchi sifatida men sahifani telefonda ochmoqchiman.
   - 360 px kenglikda gorizontal surish yo'q; matn o'qiladi.
4. Egasi sifatida yangi loyiha qo'shishni xohlayman.
   - Yangi loyiha bitta faylga yozuv qo'shish bilan chiqadi (kodni o'zgartirmasdan).
   - Noto'g'ri yozuv sahifani buzmaydi.
5. Egasi sifatida sahifa tez ochilishini xohlayman.
   - Bosh sahifa 3 soniyadan kam ochiladi (oddiy aloqada).
   - Rasmlar 300 KB dan katta emas.

## Cheklovlar (qilmaydi)
- Foydalanuvchi ro'yxatdan o'tmaydi.
- To'lov yo'q.
- Izohlar/forum yo'q.
```
Baholashda: mezonlar «chiroyli», «tez» kabi mavhum bo'lsa qaytaring; son va tekshiriladigan shart so'rang.

### O'rta — SDLC va artefakt moslash (10 daqiqa)
Berilgan 8 artefaktni bosqichga mos qiling: ERD; bug-raport; release note; user story; Docker image; unit test; changelog; API spetsifikatsiyasi.
**Kutiladigan natija:** to'g'ri moslik.
**Yechim:** ERD — dizayn; bug-raport — test; release note — deploy/release; user story — talab; Docker image — deploy/release; unit test — kod (dasturlash artefakti; bajarilishi testda); changelog — qo'llab-quvvatlash; API spetsifikatsiyasi — dizayn. (Unit test yozilishi bahsli: qo'llanma uni dasturlash artefakti sifatida beradi.)

### Qiyin — Qaysi bosqichda xato? (10 daqiqa, kuchli o'quvchi uchun)
Uchta voqea: (a) mijoz «men buni so'ramagan edim» deydi; (b) ilova 100 foydalanuvchida qulaydi; (c) yangi versiya chiqdi, lekin eski versiyaga qaytib bo'lmayapti. Har biri qaysi bosqichdagi qanday kamchilikdan, qanday artefakt yetishmaganidan kelib chiqqanini va qanday oldini olishni yozing.
**Kutiladigan natija:** har voqea uchun bosqich + sabab + chora.
**Yechim:** (a) talab bosqichi: aniq SRS/qabul mezoni yo'q, mijoz bilan tasdiqlanmagan; chora: user story + qabul mezoni, kichik iteratsiya va tez demo. (b) dizayn va test: yuklama (load) testi va arxitektura (kesh, masshtablash) e'tiborga olinmagan; chora: load test, platforma qatlamini (kesh) loyihalash, monitoring. (c) deploy/release: rollback rejasi yo'q; chora: release artefaktlarida rollback rejasi, versiyalash (semver), blue-green/canary.

## 5. Tezkor nazorat
1. IT ekotizimining 4 qatlamini ayting va har biriga bittadan misol keltiring. *(Klient — brauzer; ilova — backend/API; platforma — DB, Redis; infratuzilma — server, bulut, OS.)*
2. Qatlamlashning kamida ikkita foydasi nima? *(Muammo izolyatsiyasi; kengaytirish/almashtirish osonligi; xavfsizlik va monitoring soddaligi.)*
3. SDLC ning 6 bosqichini tartib bilan ayting. *(Talab, dizayn, kod, test, deploy/release, monitoring/qo'llab-quvvatlash.)*
4. Nega SDLC «sikl»? *(Ekspluatatsiya va monitoringdan yangi talablar keladi; halqa yopiladi.)*
5. Deploy va release farqi nima? *(Deploy — texnik joylash; release — foydalanuvchiga qaysi versiya ko'rinishi qarori.)*

## 6. Uyga vazifa
`uyga-vazifa.md` dagi 1-dars vazifasi: mini-SRS ni yakunlash va ekotizim xaritasini toza chizib topshirish. Git o'rnatilganini tekshirish (`git --version`).

## Mentor uchun eslatmalar
- Birinchi dars: o'quvchi bilan kontakt va temp o'rnatilishi muhim. Diagnostikadan darajani aniqlang; agar 8–9-sinf kursini o'tgan bo'lsa, HTML/CSS/JS ga tayanib misol keltiring.
- Qatlam sonidagi farq (3 yoki 4) manbada bor; o'quvchi chalkashsa, «ilova–platforma–infratuzilma + ularning ustidagi klient» deb tushuntiring.
- Namuna 1 internet talab qiladi. `git` o'rnatilmagan bo'lsa, o'rnatishni tanaffusda bajaring.
- Telegram/Instagram misollari taxminiy: o'quv materialida bu kompaniyalar arxitekturasi berilmagan; aniq faktdek aytmang.
