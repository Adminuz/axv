# 10-dars. Prototip va ularning turlari (Low-fidelity vs High-fidelity)

**Fan:** Advanced UX/UI dizayn va Advanced Front-end
**Sinf:** 10-sinf
**Hafta:** 4-hafta, 1-dars (umumiy 10-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `_matn/oquv-qollanma.txt`, IV bob, 4.1 «Prototip va ularning turlari» (taxminan 1246–1356-qatorlar)

---

## Darsning maqsadi

O'quvchi prototip nima ekanini, nega u vaqt va resursni tejashini, prototiplash jarayonining 4 bosqichini hamda prototip turlarini (statik: qog'oz, wireframe, grafik muharrir rasmlari; dinamik: interaktiv) ajrata oladi. Qora-oq wireframe (past detallashgan) va rangli interaktiv prototip (vizual dizaynga asoslangan) o'rtasidagi farqni tushuntiradi. Sahifa tartibining asosiy qurilish bloklarini (navigatsiya, axborot, xizmat, dizayner, reklama) biladi va qog'oz prototipida joylashtira oladi.

## Kutiladigan natija

- Prototipni 1–2 jumlada ta'riflaydi va 3 ta real hayotiy misol keltiradi;
- Prototipning 5 ta maqsadini sanaydi;
- 4 bosqichni to'g'ri tartibda aytadi: Konseptual dizayn, O'zaro ta'sir dizayni, Ekran dizayni, Sinovdan o'tkazish;
- Statik va dinamik prototipni taqqoslaydi, qog'oz prototipining 3 afzalligini biladi;
- Navigatsiya dizayni hal qilishi kerak bo'lgan 3 muammoni tushuntiradi;
- Qog'ozda oddiy sahifa prototipini chizadi.

## Kerakli jihozlar

- Proyektor/monitor (slaydlar), A4 qog'oz, qalam, rangli markerlar;
- Ixtiyoriy: Figma (faqat ko'rsatish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 3-hafta: UI Kit, 8pt, grid. Savol: «Tugma holatlari nechta?», «Desktopda necha ustun?» |
| 08–25 | Prototip nima va nega | Ta'rif, 3 hayotiy misol, vaqt va resurs tejash, 5 maqsad, 4 bosqich |
| 25–42 | Prototip turlari | Statik (qog'oz, wireframe, grafik rasm), oraliq «hikoyalar taxtasi», dinamik prototip, qora-oq vs rangli |
| 42–48 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 48–60 | Sahifa tartibining qurilish bloklari | Navigatsiya (3 muammo + bloklar), axborot, xizmat, dizayner, reklama |
| 60–75 | Amaliyot | Maktab sayti bosh sahifasining qog'oz prototipi |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Prototip nima?

> Dastlabki loyihalashda tizimning barcha funksiyalari, sahifalari va elementlari haqida tasavvur paydo bo'ladi. Ammo eng tajribali mutaxassislar ham xato qilishi mumkin, ayniqsa jamoada. Shuning uchun aqlli jamoalar mahsulot foydalanuvchiga yetib borishidan oldin prototip yaratadi.

**Prototip** — mahsulotning soddalashtirilgan namunasi. U asosiy funksiyalar va foydalanuvchi bilan o'zaro ta'sir qanday bo'lishini ko'rsatadi. Vaqt va pul sarflamasdan oldin g'oyani tekshirish mumkin.

Hujjatdagi real hayotiy misollar:
- arxitektor **maket** yaratadi;
- aviatsiya muhandisi **aerodinamik quvurda** model sinaydi;
- dasturchi va dizayner interfeys **prototipini** yaratadi.

**Sahifa prototipi** — sahifadagi barcha elementlarning joylashuvi va tuzilishini ko'rsatuvchi eskiz.

### 2. Nega prototiplash muhim?

Asosiy sabab — vaqt va resurslarni tejash:
- prototip arzon va tez tayyorlanadi;
- xatolar erta bosqichda topiladi;
- yaxshi ishlamaydigan g'oyani vaqt sarflamay rad etish mumkin.

Mentor uchun: o'xshatish — uy qurishdan oldin karton maket. Maketni o'zgartirish bir daqiqa, qurib bo'lingan devorni buzish esa qimmat.

### 3. Prototipning 5 ta maqsadi

1. Dizayn g'oyalarini ishlab chiqish va yaxshilash;
2. Jamoa ichida umumiy tushuncha yaratish;
3. Menejer yoki mijozni dizayn g'oyalariga ishontirish;
4. Texnik imkoniyatlarni tekshirish;
5. Foydalanuvchilar bilan dizaynni sinab ko'rish.

**Muhim:** ko'pgina birinchi prototiplar noto'g'ri chiqadi, bu tabiiy. Avval eng oddiy variant yaratiladi, sinovdan o'tkaziladi, keyin asta-sekin takomillashtiriladi (iteratsiya).

### 4. Prototiplash jarayonining 4 bosqichi

| № | Bosqich | Nima qilinadi |
|---|---|---|
| 1 | Konseptual dizayn | Dastlabki g'oya, yondashuv, asosiy tuzilma |
| 2 | O'zaro ta'sir dizayni (Interaction Design) | Ekranlar orasidagi bog'liqlik, o'tishlar, foydalanuvchi yo'li |
| 3 | Ekran dizayni | Har bir sahifaning ko'rinishi, elementlar joylashuvi, interfeys shakli |
| 4 | Sinovdan o'tkazish | Foydalanuvchilar bilan tekshirish, mutaxassislar evristik tahlili, yangi iteratsiya |

### 5. Prototip turlari

**A) Statik prototiplar** (o'zgarmaydigan, bosma yoki rasm ko'rinishida):
- **Qog'oz prototipi** — ekranlar qo'lda chiziladi, o'zgartirish juda oson;
- **Kontur (wireframe) prototipi** — interfeysning eng soddalashtirilgan skeleti;
- **Grafik muharrirlardagi statik rasmlar** — Figma, Photoshop, Illustrator va boshqalar.

Qog'oz prototipining afzalliklari: o'zgartirish oson va tez; e'tibor bezaklarga emas, mazmun va mantiqqa qaratiladi; arzon, vaqt talab qilmaydi.

**Oraliq bosqich — statik (passiv) hikoyalar taxtasi (storyboard):** interfeys xuddi shunday chiziladi, lekin qog'ozda emas, elektron ofis vositalarida (hujjat misoli: Microsoft Visio va PowerPoint kombinatsiyasi). Bu elektron va qog'oz prototiplari o'rtasidagi bosqich.

**B) Dinamik (interaktiv) prototiplar:** statik hikoyalar taxtasining rivoji. Har bir ekran alohida slayd, tugmalarni bosish natijasi ular orasidagi o'tishlar bilan taqlid qilinadi. Bu — elektron prototip. Tez va arzon yaratiladi, vizual dizayn tugashini kutmasdan foydalanish imkoniyatini tekshirish mumkin. Murakkabroq o'zaro ta'sirni sinash mumkin, lekin topilgan xatolarni tuzatish **ancha mashaqqatli**. Hujjat vositalar misoli: Axure RP Pro, Microsoft Expression Blend, MS Visio.

### 6. Low-fidelity va High-fidelity (qora-oq va rangli)

Hujjat prototip ishlab chiqishning ikki yondashuvini keltiradi:
1. **Sahifa sxemalariga asoslangan qora-oq prototip (wireframe)** — past detallashgan (low-fidelity) yondashuv;
2. **Mijoz qabul qilgan vizual dizaynga asoslangan rangli prototip** — yuqori detallashgan (high-fidelity) yondashuv, ko'pincha interaktiv.

| Belgi | Low-fidelity (qog'oz, wireframe) | High-fidelity (rangli interaktiv) |
|---|---|---|
| Ko'rinish | Qora-oq, oddiy shakllar | Rang, shrift, rasm, yakuniyga yaqin |
| Tezlik/narx | Eng tez va arzon | Ko'proq vaqt talab qiladi |
| O'zgartirish | Juda oson | Xatolarni tuzatish mashaqqatli |
| Fokus | Tuzilma, mazmun, mantiq | Yakuniy natijaga o'xshash model |
| Qachon | Dastlabki g'oya, tezkor sinov | Mijoz, ishlab chiquvchi bilan muloqot |

Hujjat fikri: yakuniy natijaga imkon qadar o'xshash interfeys modeliga ega bo'lish mijoz, foydalanuvchi va ishlab chiquvchilar bilan muloqotni osonlashtiradi.

> Eslatma (noaniqlik): hujjatda «high-fidelity» so'zi aniq ishlatilmaydi; «low-fidelity design» atamasi 4.3 bo'limining kalit so'zlarida bor. Mentor tushuntirishda hujjatdagi «qora-oq wireframe» va «rangli interaktiv prototip» juftligiga tayansin.

### 7. Sahifa tartibining asosiy qurilish bloklari

Asosiy bloklar: **navigatsiya, ma'lumot (axborot), xizmat ko'rsatish, dizayn, reklama.**

**Navigatsiya dizayni bir vaqtda 3 muammoni hal qilishi kerak:**
1. Foydalanuvchi uchun sahifaning bir nuqtasidan boshqasiga o'tish yo'lini ta'minlash (har bir sahifani har biriga bog'lab bo'lmaydi, shuning uchun elementlar tanlanadi; havolalar ishlashi shart);
2. Ichki navigatsiya elementlari orasidagi munosabatni aks ettirish (qaysi biri muhimroq, farqi nima);
3. Elementlar mazmuni va foydalanuvchi ko'rib turgan sahifa o'rtasidagi munosabatni aks ettirish.

**Navigatsiya bloklari:**
1. «Asosiy sahifaga» — logotip/kompaniya nomi havolasi, odatda yuqori chapda, barcha sahifada takrorlanadi;
2. Qidiruv va tezkor navigatsiya — kiritish maydoni + tugma, odatda yuqori o'ngda, yashirish tavsiya etilmaydi;
3. Gorizontal menyu — asosiy bo'limlarga havolalar ro'yxati (matn, belgi: uy, savat, konvert);
4. Vertikal menyu — odatda chapda; statik yoki ochiladigan daraxt;
5. Ikkilamchi navigatsiya — menyuning kesilgan varianti, ko'pincha kompaniya haqida;
6. Tanlov navigatsiyasi — rasm, havola, qidiruv natijalari orasida yurish; joriy fragment ta'kidlanadi;
7. Avtorizatsiya — foydalanuvchi o'zini identifikatsiya qiladigan joy;
8. «Podval» (footer) — matnli havolalar, tez yuklanishi kerak;
9. Navigatsiya paneli (breadcrumbs) — joriy sahifaga yo'l; uzun bo'lsa oraliqlar ellips (...) bilan almashtiriladi.

**Axborot bloklari:** mundarija; joriy ma'lumotlar; «Bo'lim» (e'lon, yangilik, so'rovnoma — nomi, mazmuni, to'liq variantga havola); rasmlar (galereya) — bir nechta kichik rasm bitta kattadan afzal, chunki tez yuklanadi.

**Xizmat bloklari:** tilni tanlash; «bo'sh blok»; «bosma versiya» (printer belgisi).

**Dizayner bloki:** bezash uchun rasm, kontentning asosiy elementi emas; boshqa bloklar foni bo'lishi mumkin.

**Reklama bloklari:** «Nom va shior»; «Mualliflik huquqi».

---

## Kod namunasi

Bu darsda dasturlash kodi yo'q. Nazariyani HTML maketida ko'rsatish uchun (ixtiyoriy, slayddagi `.browser` maketidagi kabi) wireframe skeleti:

```html
<!-- Past detallashgan (low-fidelity) sahifa skeleti: faqat tuzilma, rangsiz -->
<header>Logo | Menyu | Qidiruv | Kirish</header>
<nav>Bosh sahifa &gt; Yangiliklar &gt; Maqola</nav>   <!-- breadcrumbs -->
<main>Sarlavha va asosiy mazmun</main>
<aside>Joriy ma'lumotlar</aside>
<footer>Havolalar | Mualliflik huquqi</footer>
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Statik yoki dinamik?
Har biri qaysi turga kirishini yozing: (a) qo'lda chizilgan ekranlar; (b) tugmalar bosilganda ekranlar o'zgaradigan Figma taqdimoti; (c) Figma'dagi bitta qora-oq maket rasmi; (d) PowerPoint'da tugmalar orqali bog'langan slaydlar.

**Kutiladigan natija:** to'g'ri turkumlash va sababi.

**Yechim:** (a) statik, qog'oz prototipi; (b) dinamik (interaktiv); (c) statik, grafik muharrirdagi rasm/wireframe; (d) dinamik, interaktiv hikoyalar taxtasi (har ekran alohida slayd, tugma bosish o'tishni taqlid qiladi).

### 2-topshiriq (o'rta). Bloklarni turkumlash
Quyidagilarni 5 turdan biriga ajrating: logotip havolasi, til tanlash, «Biz klassikani hurmat qilamiz» shiori, yangiliklar bo'limi, breadcrumbs, bosma versiya, mualliflik huquqi, qidiruv maydoni.

**Kutiladigan natija:** 8 ta blok to'g'ri turkumda.

**Yechim:** logotip havolasi — navigatsiya; til tanlash — xizmat; shior — reklama («Nom va shior»); yangiliklar — axborot («Bo'lim»); breadcrumbs — navigatsiya (navigatsiya paneli); bosma versiya — xizmat; mualliflik huquqi — reklama; qidiruv — navigatsiya.

### 3-topshiriq (qiyin). Maktab sayti bosh sahifasining qog'oz prototipi
A4 qog'ozga maktab sayti bosh sahifasini chizing. Kamida 7 blok: logotip, gorizontal menyu, qidiruv, yangiliklar, galereya, til tanlash, podval. Har blokning turini yozing va nega shu joyga qo'yganingizni 1 jumlada izohlang. Keyin sherigingiz «foydalanuvchi» bo'lib, «Qabul qoidalarini topish» vazifasini bajarsin va sizning prototipingizda qayerga bosishini ko'rsatsin.

**Kutiladigan natija:** 7+ blok, to'g'ri joylashuv (logotip chapda yuqorida, qidiruv o'ngda yuqorida, podval pastda), sinov natijasi bo'yicha 1 ta tuzatish.

**Yechim (namuna):** tepada: chapda logotip («Asosiy sahifaga»), o'rtada gorizontal menyu (Maktab haqida, Qabul, Yangiliklar, Aloqa), o'ngda qidiruv va til tanlash. Ostida breadcrumbs. Markazda «Yangiliklar» («Bo'lim»), yonida galereya (bir nechta kichik rasm). Pastda podval: matnli havolalar + mualliflik huquqi. Sinovda «Qabul» menyusi topilsa — yaxshi; topilmasa, menyu nomini aniqlashtirish yoki ajratib ko'rsatish tuzatish bo'ladi.

### 4-topshiriq (qo'shimcha). Iteratsiya
Birinchi chizmangizdagi bitta kamchilikni toping va ikkinchi variantni 5 daqiqada qayta chizing. (Hujjat: birinchi prototip noto'g'ri chiqishi tabiiy, o'zgartirish oson.)

---

## Tezkor nazorat (dars oxirida)

1. Prototip nima? — Mahsulotning soddalashtirilgan namunasi, asosiy funksiyalar va o'zaro ta'sirni ko'rsatadi.
2. Prototiplashning 4 bosqichi? — Konseptual dizayn, O'zaro ta'sir dizayni, Ekran dizayni, Sinovdan o'tkazish.
3. Qog'oz prototipining bitta afzalligi? — O'zgartirish oson va tez; e'tibor mazmunga qaratiladi; arzon.
4. Dinamik prototipning statikdan farqi? — Tugma bosilganda ekranlar orasidagi o'tishlar taqlid qilinadi (interaktiv); xatoni tuzatish mashaqqatliroq.
5. Navigatsiya dizayni hal qilishi kerak bo'lgan 3 muammodan birini ayting. — Sahifalar orasida yo'l; ichki elementlar orasidagi munosabat; element mazmuni va joriy sahifa orasidagi munosabat.

## Keng tarqalgan xatolar

- «Prototip = tayyor sayt» deb o'ylash. Prototip soddalashtirilgan namuna.
- Birinchi prototipni mukammal qilishga urinish. Avval oddiy, keyin takomillashtirish.
- Wireframega rang va rasm qo'shib, e'tiborni mazmundan chalg'itish.
- Qidiruvni «chiroyli bo'lsin» deb yashirish (hujjat yashirishni tavsiya etmaydi).

## Bilasizmi? (Internetdan, qo'shimcha)

- «Prototip» so'zi yunoncha «protos» (birinchi) va «typos» (nusxa, shakl) so'zlaridan olingan.
- Avtomobil kompaniyalari yangi modelni avval loydan yoki kartondan yasalgan to'liq o'lchamli maket sifatida ko'rsatadi.
