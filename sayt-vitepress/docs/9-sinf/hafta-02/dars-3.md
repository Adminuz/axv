---
title: "6-dars. Balsamiq va Axure RP: asosiy UI komponentlar va dastlabki interfeys sxemalari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf", "link": "/9-sinf/"}, "week": {"n": 2, "link": "/9-sinf/hafta-02/"}, "g": 6, "title": "Balsamiq va Axure RP: asosiy UI komponentlar va dastlabki interfeys sxemalari", "lead": "Birgina g'oya bor, lekin uni millionlab foydalanuvchilar tushunadigan interfeysga qanday aylantirish mumkin? Ushbu darsda professional Axure RP va Balsamiq vositalarida murakkab bloklar, sahifalar navigatsiyasi, kulranglar ierarxiyasi va wireframelarni Figmaga tayyorlashni o'rganamiz.", "slide": "/slaydlar/9-sinf/hafta-02/dars-3.html", "test": "/slaydlar/9-sinf/hafta-02/dars-3-test.html", "tabs": [{"g": 4, "link": "/9-sinf/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/9-sinf/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/9-sinf/hafta-02/dars-3", "current": true}], "prev": {"g": 5, "title": "Wireframe tushunchasi va Balsamiq dasturiga kirish", "link": "/9-sinf/hafta-02/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Axure RP** — professional darajadagi murakkab wireframe, shartli mantiq va interaktiv prototiplash dasturidir.
- Balsamiq dastlabki tezkor qalamaki eskizlar uchun, Axure RP esa aniq geometriyali va batafsil texnik maketlar uchun mo'ljallangan.
- Axure RP dagi **Pages** paneli orqali barcha sahifalar ierarxik daraxt ko'rinishida tartibli boshqariladi.
- Sahifalarni to'g'ri nomlash (`Home_books`, `Search_results`, `Profile`) jamoa o'rtasida chalkashlikning oldini oladi.
- Interfeysning asosiy g'ishti — **Rectangle (To'rtburchak)** bo'lib, undan sarlavha, banner, kartalar va tugmalar yasaladi.
- Wireframe'da rang ishlatilmasa ham, **kulrang tuslar (Grayscale)** yordamida qaysi element muhimroq ekani yaqqol ko'rsatiladi.
- Tayyor bo'lgan wireframe PNG yoki SVG formatida eksport qilinib, keyingi bosqichda **Figma** dasturiga asosiy qolip (reference) sifatida yuklanadi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega Axure RP murakkab loyihalarda ajralmas?
Figma dizaynerlarga ko'proq chiroyli ko'rinish berishga yordam beradi, ammo Axure RP dasturida siz haqiqiy dasturchi kabi shartlar yozishingiz mumkin: masalan: "Agar savatdagi tovarlar soni 3 tadan oshsa, 10% chegirma ko'rinsin", "Agar login to'g'ri kiritilsa, profil ochilsin, aks holda qizil ogohlantirish chiqsin". Bu xususiyat katta bank ilovalari va korporativ tizimlarni sinashda juda qadrlanadi.

### Kulrang tuslar palitrasi (Grayscale Hierarchy)
Rangli bo'yoqlarsiz ham chuqurlik va muhimlikni ko'rsatish mumkin:
1. **Oq (#FFFFFF):** Fon yoki ustki kartalar uchun eng toza fon.
2. **Och kulrang (#F1F5F9):** Sahifaning orqa foni, bo'limlarni ajratuvchi qutilar.
3. **O'rta kulrang (#94A3B8):** Ikkilamchi matnlar, ramkalar, sanalar, muallif nomlari.
4. **To'q kulrang (#1E293B):** Asosiy sarlavhalar va eng muhim harakat tugmalari (CTA).

### Wireframeni Figmaga ko'chirish qoidasi
Axure RP yoki Balsamiqda chizilgan wireframeni to'g'ridan-to'g'ri kodga aylantirish qiyin. Shuning uchun professional ish oqimi (workflow) quyidagicha kechadi:
`Ssenariy → User Flow → Wireframe (Balsamiq/Axure) → UI Dizayn (Figma) → Front-end Kod (HTML/CSS)`.
Wireframeni PNG qilib Figmaga tashlaysiz, uning ustidan 100% bir xil proporsiyada chiroyli dizaynni chizasiz.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Axure RP | Murakkab wireframe va interaktiv prototiplar yaratish dasturi |
| Widget (Vidjet) | Axure RP dagi tayyor UI element (to'rtburchak, matn, tugma...) |
| Canvas | Markaziy pikselli ish maydoni |
| Interactions | Elementlar bosilganda sodir bo'ladigan harakatlar va hodisalar |
| Dynamic Panel | Axure RP da bir joyda bir nechta holatni (state) ko'rsatuvchi interaktiv blok |
| Grayscale | Qora, oq va kulrang tuslardan iborat rangsiz palitra |
| Export | Dasturdagi loyihani tashqi fayl (PNG, SVG, PDF) ko'rinishida saqlash |
| Reference Layer | Figmada dizayn chizish uchun fon qilib qo'yilgan asosiy qolip |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Axure RP dasturi 2002-yildan beri mavjud bo'lib, Fortune 500 ro'yxatidagi (dunyodagi eng boy 500 ta kompaniya) 80% dan ortiq IT-kompaniyalari undan foydalanadi.
- Dizaynda "Visual Weight" (Vizual og'irlik) qoidasi bor: qanchalik to'q kulrang bo'lsa, inson ko'zi unga shunchalik birinchi bo'lib qaraydi.
- Axure RP prototiplarini to'g'ridan-to'g'ri HTML sahifa sifatida saqlab, internet brauzerida xuddi haqiqiy sayt kabi ochib ko'rish mumkin!

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Sahifalarni nomlash madaniyati <Badge type="tip" text="oson" />
Elektron kutubxona sayti uchun 4 ta asosiy sahifani ingliz tilida va professional tarzda nomlang (masalan, Bosh sahifa, Qidiruv, Kitob tafsiloti, Profil).

**Kutiladigan natija:** 4 ta to'g'ri nomlangan sahifalar ro'yxati (masalan: `Home_books`, `Search_results`...).

### 2. Kulranglar palitrasi (Grayscale) <Badge type="tip" text="oson" />
Qog'ozda yoki grafik dasturda 4 xil to'rtburchak chizib, ularni oqdan to'q kulranggacha bo'yang. Har birining yoniga nima uchun ishlatilishini yozing.

**Kutiladigan natija:** 4 pog'onali kulranglar shkalasi va ularning vazifalari.

### 3. Asosiy Header bloki wireframe'i <Badge type="tip" text="oson" />
Veb-sayt uchun yuqori sarlavha (Header) blokini chizing: chapda kompaniya logotipi o'rni, o'rtada 3 ta bo'lim nomi, o'ngda esa "Kirish" tugmasi bo'lsin.

**Kutiladigan natija:** Header blokining toza wireframe chizmasi.

### 4. Axure RP va Balsamiq solishtiruvi <Badge type="tip" text="oson" />
Ikkala dasturning eng asosiy 2 tadan afzalligi va kamchiligini qisqa jadval qilib yozing.

**Kutiladigan natija:** 4 qatorli taqqoslash jadvali.

### 5. Mahsulot kartasi (Product Card) sxemasi <Badge type="warning" text="o'rta" />
Axure RP (yoki Balsamiq/Figma)da do'kon uchun tovar kartasini yarating. Unda rasm o'rni ([X]), tovar nomi, narxi (to'q kulrang) va "Savatga qo'shish" tugmasi bo'lsin.

**Kutiladigan natija:** piksellari toza tekislangan tovar kartasi skrinshoti.

### 6. Banner va CTA tugmasi <Badge type="warning" text="o'rta" />
Saytning bosh sahifasi uchun Katta Banner (Hero Section) wireframe'ini tuzing: fon uchun och kulrang to'rtburchak, katta sarlavha matni, 2 jumlalik tavsif va e'tibor tortuvchi to'q kulrang tugma.

**Kutiladigan natija:** muvozanatli joylashgan banner bloki tasviri.

### 7. Formaning Low-fi wireframe'i <Badge type="warning" text="o'rta" />
Foydalanuvchi fikr-mulohazasini qabul qiluvchi forma skeletini chizing: Ism maydoni, Baholash (1 dan 5 gacha yulduzchalar o'rni), Katta xabar yozish maydoni va "Yuborish" tugmasi.

**Kutiladigan natija:** barcha maydonlari va yozuvlari bilan to'liq forma wireframe'i.

### 8. Ikki sahifali loyiha va o'tish (Interactions) <Badge type="warning" text="o'rta" />
Axure RP da 2 ta sahifa (`Home_books` va `Book_details`) yarating. Bosh sahifadagi kitob kartasini bosganda tafsilotlar sahifasiga o'tuvchi havola (Open Link) qo'ying.

**Kutiladigan natija:** dasturdan olingan sahifalar daraxti va havola o'rnatilganlik skrinshoti.

### 9. "Home_books" to'liq veb-sahifasi wireframe'i <Badge type="danger" text="qiyin" />
Elektron kutubxona sayti bosh sahifasining to'liq wireframe'ini Axure RP yoki Balsamiqda quring:
- Header (Logo, Menyu, Profil);
- Katta qidiruv va banner bloki;
- "Hafta bestsellerlari" (3 ta kitob kartasi);
- "Yangi qo'shilganlar" (3 ta kitob kartasi);
- Footer (Aloqa va huquqlar).

**Kutiladigan natija:** eksport qilingan to'liq sahifa PNG tasviri.

### 10. Wireframeni Figmaga import qilish <Badge type="danger" text="qiyin" />
Tayyorlagan wireframengizni PNG formatida eksport qiling. So'ngra Figma dasturini ochib, yangi Frame (Desktop 1440px) yarating va rasmni uning ichiga import qilib, joylashtiring. Rasmni qulflab (Lock), ustiga sarlavhani haqiqiy shrift bilan yozing.

**Kutiladigan natija:** Figmada wireframe ustiga qo'yilgan birinchi UI elementlar skrinshoti.

### 11. Mobil ilovaning to'liq 3 ekranli oqimi <Badge type="info" text="bonus" />
"Kitob o'qish" mobil ilovasining ketma-ket 3 ta ekranini to'liq wireframe qilib chizing: 1-ekran (Kutubxona), 2-ekran (Kitob o'qish ekrani — matn, shrift o'lchami tugmalari), 3-ekran (Xatcho'plar ro'yxati). Barcha ekranlar bir xil o'lcham va uslubda bo'lsin.

**Kutiladigan natija:** 3 ta mobil ekranning yagona faylga jamlangan wireframe loyihasi (PNG yoki Figma havolasi).

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Axure RP qanday maqsadlarda Balsamiqdan ko'ra afzalroq hisoblanadi?
2. Sahifalarni nomlashda qanday umumiy qoidalarga rioya qilish kerak?
3. Axure RP da eng ko'p ishlatiladigan asosiy vidjet (widget) qaysi?
4. Kulranglar ierarxiyasida to'q kulrang qaysi elementlarga beriladi?
5. Yaratilgan wireframeni Figmaga eksport qilishdan asosiy maqsad nima?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

O'zingiz qiziqqan biror veb-sayt (masalan, yangiliklar portali yoki internet-do'kon) bosh sahifasining barcha bloklari joylashuvini ko'rsatuvchi to'liq wireframe sxemasini Axure RP, Balsamiq yoki qog'ozda chizing va uni `loyiha_wireframe.png` sifatida saqlang.

</div>

