# 11-dars. UX flow diagrammalari va axborot arxitekturasi

**Fan:** Advanced UX/UI dizayn va Advanced Front-end
**Sinf:** 10-sinf
**Hafta:** 4-hafta, 2-dars (umumiy 11-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `_matn/oquv-qollanma.txt`, IV bob, 4.2 «UX flow diagrammalari» (taxminan 1377–1478-qatorlar); axborot arxitekturasi bo'yicha: II bob, karta tartiblash va daraxt testi (taxminan 530–540 va 637–660-qatorlar); navigatsiya bloklari: 4.1 bo'lim (10-dars).

---

## Darsning maqsadi

O'quvchi user flow nima ekanini, uning 3 turini (task flow, wireflow, user flow), flowchart shakllarini (romb — qaror, to'rtburchak — amal) biladi va oddiy vazifa uchun oqim diagrammasini chizadi. Axborot arxitekturasi (IA) tushunchasini karta tartiblash (Card Sorting) va daraxt testi orqali bog'laydi: sayt bo'limlari foydalanuvchi mantiqiga mos guruhlanadi.

## Kutiladigan natija

- User flowni ta'riflaydi va nega kerakligini 3 holat bo'yicha tushuntiradi;
- Flowchart shakllarini ajratadi: romb («Ha»/«Yo'q»), to'rtburchak (amal);
- Task flow, wireflow va user flow farqini aytadi;
- User flow UX jarayonining qaysi bosqichida tuzilishini va undan oldin nimalar bajarilgan bo'lishini biladi;
- Karta tartiblashning 3 turini (ochiq, gibrid, yopiq) sanaydi;
- «Parolni tiklash» yoki «Maktab saytida ro'yxatdan o'tish» uchun task flow chizadi.

## Kerakli jihozlar

- Proyektor/monitor (slaydlar), A4 qog'oz, qalam, rangli stikerlar yoki kichik qog'oz kartalar (karta tartiblash uchun);
- Ixtiyoriy: Figma (faqat ko'rsatish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 10-dars: prototip, 4 bosqich, statik/dinamik, navigatsiya muammolari. Savol: «Breadcrumbs nima uchun kerak?» |
| 08–25 | User flow nima | Ta'rif, kirish nuqtasi va maqsad, flowchart shakllari (romb va to'rtburchak), nega kerak (3 holat) |
| 25–40 | User flow turlari | Task flow, wireflow, user flow; qaysi bosqichda tuziladi; oldingi hujjatlar |
| 40–46 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 46–56 | Axborot arxitekturasi | Karta tartiblash (ochiq/gibrid/yopiq), daraxt testi, navigatsiya bilan aloqasi |
| 56–75 | Amaliyot | «Parolni tiklash» task flow, so'ng karta tartiblash mini-sessiyasi |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. User flow nima?

> Biror mahsulotdan foydalanayotganda foydalanuvchi bir nechta turli yo'nalishlarda harakat qilishi mumkin. User flow — foydalanuvchi ilova yoki veb-saytdan foydalanganda bosib o'tishi mumkin bo'lgan barcha yo'llarni ko'rsatuvchi vizual tasvir. U yozma tarzda yoki maxsus diagramma shaklida tuzilishi mumkin.

**Flowchart (oqim diagrammasi)** foydalanuvchining mahsulotga **kirish nuqtasidan** (onboarding ekrani yoki bosh sahifa) boshlanadi va **yakuniy harakatga** (sotib olish, ro'yxatdan o'tish, hisob yaratish) yetguncha davom etadi. Bu dizaynerga foydalanuvchi tajribasini baholash va optimallashtirish imkonini beradi (hujjat: bu mijozlar konversiyasini oshiradi).

**Shakllar** (diagrammadagi har bir nuqta — yo'ldagi alohida bosqich):
- **Romb** — qaror qabul qilish nuqtasi; undan «Ha» yoki «Yo'q» yo'nalishlari chiqadi;
- **To'rtburchak** — bajarilishi kerak bo'lgan amal: «Kirish», «Sotib olish», «Arizani yuborish».

Mentor uchun o'xshatish: user flow — shahar metrosi sxemasi. Yo'lovchi qaysi bekatdan kirishi, qayerda ko'chib o'tishi va qayerda tushishini sxema oldindan ko'rsatadi.

### 2. UX dizaynda user flowdan nega foydalanamiz?

User flow yangi mahsulot yaratishda ham, mavjud interfeysni yangilashda ham foydali. Hujjatdagi holatlar:

1. **Intuitiv interfeys yaratish.** Yaxshi loyihalangan mahsulot foydalanuvchini «o'z holatiga sho'ng'ish»ga (flow state) tez olib kiradi, kerakli amalni bajarish ehtimoli oshadi. Maqsadga ko'pincha bir nechta yo'l bor; user flow ularning samaradorligini baholashga imkon beradi.
2. **Mavjud interfeyslarni tahlil qilish.** Foydalanuvchilar qayerda qiynalayotganini aniqlaydi. Savollar: sahifalar mantiqan bog'langanmi? Jarayon ketma-ketligi tushunarlimi? Blueprint (chizmaga o'xshash oqim) to'xtab qolish joylarini ko'rsatadi.
3. **Mahsulotni mijoz yoki jamoaga taqdim qilish.** Hamkasblar bilan bir xil tushunchani ta'minlaydi va dizayn qarorlarini asoslashga yordam beradi.

### 3. User flow turlari

| Tur | Nimani ko'rsatadi | Xususiyat |
|---|---|---|
| **Task flow** (vazifa oqimi) | Bitta aniq vazifani bajarish: «Hisob yaratish», «Parolni tiklash», «Mahsulotni xarid qilish» | Odatda bitta asosiy yo'l; hamma bir xil bajaradi deb faraz qilinadi |
| **Wireflow** | Wireframe + flowchart aralashmasi | Oqim chizig'ida har sahifaga mos wireframe; mobil ilovalar uchun qulay; har sahifada foydalanuvchi nimani ko'rishini aniq ko'rsatadi |
| **User flow** (foydalanuvchi oqimi) | Turli yo'llar | Har xil personalar va turli kirish nuqtalari (home, reklama banneri, qidiruv natijalari); bitta vazifaga bir nechta ssenariy |

### 4. Qaysi bosqichda tuziladi?

User flow dizayn jarayonining **dastlabki rejalashtirish bosqichida** yaratiladi, foydalanuvchi tadqiqotlari (user research) tugallangan bo'ladi. U orqali aniqlanadi: nechta ekran kerak, ular qanday ketma-ketlikda, qaysi elementlar zarur. Bu bosqichga kelguncha bajarilgan bo'ladi: empatiya xaritalari, affinity diagrammalar, persona, asosiy ssenariylar (2-hafta darslari bilan bog'lang). User flow loyiha yakunida mijozga beriladigan asosiy deliverable hujjatlardan biri; mavjud interfeysni yaxshilash uchun ham qayta ko'rib chiqiladi.

Foyda (hujjat): interfeysni soddalashtirish, jamoa bilan bir xil qarash, mijozga loyihani tushuntirish. Foydalanuvchi chalkashliksiz harakatlansa, mamnun bo'ladi, qayta tashrif buyuradi va kerakli amalni bajaradi.

### 5. Axborot arxitekturasi (IA): hujjatdagi asos

Axborot arxitekturasi — mahsulotdagi axborot qanday guruhlangani va tartiblangani. Hujjatda IA alohida bo'lim sifatida berilmagan, u tadqiqot usullari orqali keladi (2-hafta, 4-dars):

- **Karta tartiblash (Card Sorting):** foydalanuvchilar axborot va g'oyalarni o'zlariga mantiqan to'g'ri keladigan guruhlarga ajratadi; mahsulotdagi axborot arxitekturasini **intuitiv** shakllantiradi. Karta ustiga mavzu yoziladi, foydalanuvchi uni ma'noli toifalarga ajratadi. Loyihaning boshida o'tkaziladi. Turlari:
  - **Ochiq (Open):** ishtirokchilar mavzularni o'zlari toifalab, nom berishadi;
  - **Gibrid (Hybrid):** tayyor toifalar bor, lekin yangisini yaratish ham mumkin;
  - **Yopiq (Closed):** faqat berilgan toifalarga ajratish.
  Qog'oz indeks kartalari yoki raqamli vosita (hujjat misoli: Maze) bilan o'tkaziladi. Kamchiligi: real hayotdagi qarorlarni har doim to'liq aks ettirmasligi mumkin.
- **Daraxt testi (Tree test):** soddalashtirilgan axborot arxitekturasida foydalanuvchi axborotni topa olish qobiliyatini baholaydi (dizayn yoki qayta dizayn boshida).
- **Navigatsiya bilan aloqa:** 10-darsdagi navigatsiya bloklari (menyu, breadcrumbs, footer) IA ni foydalanuvchiga ko'rsatadigan qatlam. Karta tartiblash «menyuda nima qaysi bo'limga tushadi» savoliga javob beradi, user flow esa «bo'limlar orasida qanday yuriladi» savoliga.

> Eslatma (noaniqlik): hujjatda «axborot arxitekturasi» (IA) atamasi karta tartiblash va daraxt testi tavsifida uchraydi, alohida ta'rif va sitemap bo'limi yo'q. Mentor «sitemap» kabi hujjatda bo'lmagan atamalarni asosiy o'quv materiali sifatida o'rgatmasin.

### 6. Hujjatning nazorat savollari

User flow nima va nega muhim; task flow va full user flow farqi; wireflow vazifasi; romb va to'rtburchak; user flow uchun avval qaysi ma'lumotlar aniqlanishi kerak; jamoa va mijozga foyda; qachon qayta ko'rib chiqiladi.

---

## Kod namunasi

Bu darsda dasturlash kodi yo'q. Oqim diagrammasini matn ko'rinishida yozish namunasi (mentor doskaga yozishi mumkin):

```text
[Kirish nuqtasi: Login ekrani]
        |
 [Parolni unutdim bosiladi]
        |
 [Telefon/Email kiritiladi]
        |
 <Hisob topildimi?> --Yo'q--> [Xato xabari] --> (qayta kiritish)
        |
       Ha
        |
 [Kod yuboriladi] --> [Kod kiritiladi] --> <Kod to'g'rimi?> --Yo'q--> [Qayta urinish]
        |
       Ha
        |
 [Yangi parol o'rnatiladi]  --> (Maqsad: Parol tiklandi)
```

(To'rtburchak `[ ]` — amal, romb `< >` — qaror. Misol o'quv maqsadida tuzilgan va hujjatdagi «Parolni tiklash» task flow misoliga tayanadi.)

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Shaklni toping
Quyidagilar uchun qaysi shakl (romb yoki to'rtburchak) kerak: (a) «Kirish» tugmasi bosiladi; (b) «Parol to'g'rimi?»; (c) «Arizani yuborish»; (d) «Foydalanuvchi ro'yxatdan o'tganmi?»

**Kutiladigan natija:** to'g'ri shakllar va sabab.

**Yechim:** (a) to'rtburchak (amal); (b) romb (Ha/Yo'q qaror); (c) to'rtburchak; (d) romb.

### 2-topshiriq (o'rta). Qaysi tur?
Har bir vaziyat uchun task flow, wireflow yoki user flow ni tanlang: (a) faqat «Parolni tiklash» jarayoni, bitta yo'l; (b) mobil ilovaning har ekrani chizmasi va ular orasidagi o'qlar; (c) bir vazifaga ikki xil persona va uch xil kirish nuqtasidan boriladi.

**Kutiladigan natija:** 3 ta to'g'ri javob, har biriga 1 jumla sabab.

**Yechim:** (a) task flow; (b) wireflow (har sahifaga wireframe qo'yilgan flowchart); (c) user flow (turli personalar va kirish nuqtalari).

### 3-topshiriq (qiyin). «Maktab saytida ro'yxatdan o'tish» task flow
Kirish nuqtasidan maqsadgacha kamida 5 to'rtburchak va 2 romb bilan task flow chizing. Sherigingiz diagrammada qayerda to'xtab qolish mumkinligini toping.

**Kutiladigan natija:** kirish nuqtasi, maqsad, 2 qaror nuqtasi (har birida Ha va Yo'q yo'li), sherik topgan 1 ta to'siq.

**Yechim (namuna):** Bosh sahifa → «Ro'yxatdan o'tish» bosiladi → Ma'lumot kiritiladi → <Ma'lumotlar to'g'rimi?> Yo'q → xato xabari va tuzatish; Ha → Kod yuboriladi → Kod kiritiladi → <Kod to'g'rimi?> Yo'q → qayta urinish; Ha → Profil sahifasi (maqsad). Mumkin bo'lgan to'siq: kod kelmasa nima qilish kerakligi (qayta yuborish tugmasi yo'q) — diagrammaga tuzatish sifatida qo'shiladi.

### 4-topshiriq (qo'shimcha). Karta tartiblash
12 ta kartaga maktab sayti mavzularini yozing (Qabul, Dars jadvali, Yangiliklar, O'qituvchilar, To'garaklar, Bayram tadbirlari, Hujjatlar, Aloqa, Galereya, Direktor murojaati, Imtihonlar, Ota-onalar uchun). Juftlikda ochiq karta tartiblash o'tkazing (o'zingiz toifa nomlarini bering), keyin yopiq variantni 4 ta berilgan toifa bilan sinang.

**Kutiladigan natija:** toifalar va ularning nomlari, ochiq va yopiq natijalar farqi haqida 2 jumla.

**Yechim (namuna):** ochiq tartiblashda toifalar turlicha chiqishi mumkin, masalan «Ta'lim» (Dars jadvali, Imtihonlar, O'qituvchilar), «Hayot» (To'garaklar, Bayram tadbirlari, Galereya), «Ma'lumot» (Qabul, Hujjatlar, Ota-onalar uchun), «Aloqa» (Aloqa, Direktor murojaati), «Yangiliklar». Muhim: kartani qaysi toifaga tushirish haqida kelishmovchilik bo'lsa, shu nom/joylashuv navigatsiyada muammo bo'lishi mumkin.

---

## Tezkor nazorat (dars oxirida)

1. User flow nima? — Foydalanuvchi mahsulot ichida bosib o'tishi mumkin bo'lgan yo'llarning vizual tasviri.
2. Flowchartda romb nimani bildiradi? — Qaror qabul qilish nuqtasi (Ha/Yo'q).
3. To'rtburchak-chi? — Bajariladigan amal.
4. Task flow bilan user flow farqi? — Task flowda bitta asosiy yo'l; user flowda turli personalar va kirish nuqtalari.
5. Karta tartiblashning 3 turi? — Ochiq, gibrid, yopiq.

## Keng tarqalgan xatolar

- Diagrammaga barcha mumkin bo'lgan sahifalarni qo'yish. Task flow bitta vazifaga qaratiladi.
- Romb o'rniga to'rtburchak ishlatish va Ha/Yo'q yo'llarini ko'rsatmaslik.
- Kirish nuqtasi yoki maqsadni belgilamaslik.
- User flowni user research dan oldin chizish (hujjat: tadqiqot, persona, ssenariylardan keyin).
- Karta tartiblash natijasini «yagona haqiqat» deb qabul qilish (hujjat: real qarorlarni to'liq aks ettirmasligi mumkin).

## Bilasizmi? (Internetdan, qo'shimcha)

- Oqim diagrammalarining standart shakllari (romb — qaror, to'rtburchak — amal) dasturlashda algoritm blok-sxemalari uchun ham qo'llanadi.
- Metro sxemalari ham geografik aniq emas, faqat bog'lanishlarni ko'rsatadi: user flow ham xuddi shunday «yo'llar xaritasi».
