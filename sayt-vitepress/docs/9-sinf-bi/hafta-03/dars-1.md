---
title: "7-dars. Ma’lumotlarni tozalash (Data Cleaning) va transformatsiya"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (BI)", "link": "/9-sinf-bi/"}, "week": {"n": 3, "link": "/9-sinf-bi/hafta-03/"}, "g": 7, "title": "Ma’lumotlarni tozalash (Data Cleaning) va transformatsiya", "lead": "Tahlilchining eng muhim mahorati: ortiqcha bo'shliqlar, xato formatlar va dublikatlardan xoli, 100% toza va sifatli ma'lumotlar to'plamini yaratish san'ati.", "slide": "/slaydlar/9-sinf-bi/hafta-03/dars-1.html", "tabs": [{"g": 7, "link": "/9-sinf-bi/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/9-sinf-bi/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf-bi/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi", "link": "/9-sinf-bi/hafta-03/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Ma’lumotlarni tozalash (Data Cleaning) — xom ma'lumotlardagi xatoliklar, noaniqliklar, takroriy qatorlar va noto'g'ri formatlarni to'g'rilash jarayonidir.
- Tahlilchilar o'z ish vaqtining 70-80 foizini ma'lumotlarni tozalash va tahlilga tayyorlashga sarflaydilar.
- GIGO (Garbage In, Garbage Out) qoidasi: agar tahlilga xato va sifatsiz ma'lumot kiritilsa, olingan qaror ham muqarrar xato bo'ladi.
- `TRIM` funksiyasi so'zlar orasidagi bittadan tashqari barcha ortiqcha bo'shliqlarni olib tashlaydi.
- `PROPER` funksiyasi barcha so'zlarning birinchi harfini bosh harfga (katta harfga) aylantiradi; `UPPER` va `LOWER` registrni to'liq o'zgartiradi.
- `Flash Fill` (`Ctrl + E`) — bitta namuna asosida butun ustundagi matnlarni aqlli ajratish yoki birlashtirish vositasidir.
- `Text-to-Columns` vositasi bitta katakdagi matnni belgilangan ajratgich (vergul, defis, probel) orqali bir nechta ustunga bo'lib beradi.
- Power Query muhiti barcha tozalash qadamlarini ketma-ketlikda (Applied Steps) xotirada saqlaydi va bir bosishda avtomatik yangilash imkonini beradi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega ortiqcha bo'sh joy (space) katta xato tug'diradi?
Kompyuter uchun matn bu simvollar ketma-ketligidir.
Agar 1-xodim `"Toshkent"` deb yozsa, 2-xodim esa bexosdan oxiriga bitta probel qo'shib `"Toshkent "` deb kiritgan bo'lsa, Excel bu ikkalasini butunlay ikki xil shahar deb biladi!
Natijada `COUNTIF` yoki `SUMIF` orqali Toshkent bo'yicha tushumni hisoblaganingizda raqamlar 2 ga bo'linib, hisobot buziladi.
`=TRIM()` funksiyasi aynan shu ko'rinmas bo'shliqlarni yo'qotadi.

### 2. Flash Fill (Ctrl + E) sehrli imkoniyatlari
Flash Fill quyidagi vazifalarni bir zumda bajaradi:
- To'liq ismdan faqat familiyani ajratib olish;
- Telefon raqamlariga qavs va chiziqlar qo'shish (masalan: `901234567` $\to$ `(90) 123-45-67`);
- Matnlar ichidan faqat sonlarni yoki email domenlarini ajratish.
Buning uchun yangi ustunning birinchi satriga kerakli natijani qo'lda yozib, `Ctrl + E` ni bosish kifoya.

### 3. Power Query: Takrorlanmaydigan avtomatlashtirish
Har oy sizga yangi savdo hisoboti kelsa, Excelda har safar qo'lda TRIM, PROPER va dublikatlarni o'chirish juda zerikarli.
Power Query'da bu amallar bir marta bajariladi. Keyingi oyda faqat yangi faylni papkaga tashlab, `Data > Refresh All` bosilsa, Power Query barcha 10 ta tozalash bosqichini 1 soniyada o'zi qaytadan bajaradi!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Data Cleaning** | Xom ma'lumotlardagi xatoliklar, nuqsonlar va dublikatlarni bartaraf etish jarayoni. |
| **GIGO (Garbage In, Garbage Out)** | Noto'g'ri kiritilgan ma'lumot noto'g'ri natijaga olib kelishini ifodalovchi universal qoida. |
| **TRIM** | Matndagi barcha ortiqcha bo'sh joylarni (probellarni) olib tashlovchi funksiya. |
| **PROPER** | Har bir so'zning bosh harfini katta, qolganlarini kichik harfga aylantiruvchi funksiya. |
| **Flash Fill (Ctrl+E)** | Ko'rsatilgan namuna asosida butun ustunni avtomatik to'ldiruvchi intellektual vosita. |
| **Text-to-Columns** | Matnni ajratuvchi belgilar bo'yicha bir nechta alohida ustunlarga bo'lish usuli. |
| **Delimiter** | Matnlarni ajratib turuvchi maxsus belgi (vergul, nuqta-vergul, chiziqcha, bo'shliq). |
| **Remove Duplicates** | Jadvaldagi aynan takrorlangan yozuvlarni bir zumda tozalovchi Excel vositasi. |
| **Power Query** | Ma'lumotlarni yig'ish, tozalash va o'zgartirish uchun mo'ljallangan ETL platformasi. |
| **Applied Steps** | Power Query'da ma'lumotlar ustida bajarilgan barcha amallar xronologik ro'yxati. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Xalqaro so'rovnomalarga ko'ra, ma'lumotlar tahlilchilari ish vaqtining **qariyb 80% qismi** ma'lumotlarni tozalash (data munging/wrangling)ga sarflanadi.
- Noto'g'ri va sifatsiz ma'lumotlar tufayli AQSh iqtisodiyoti har yili **3.1 trillion dollar** zarar ko'radi (IBM statistikasi).
- Exceldagi `Flash Fill` texnologiyasi Microsoft Research tomonidan sun'iy intellektning "Programming by Example" (Namuna asosida dasturlash) algoritmi asosida yaratilgan.
- `CLEAN` funksiyasi matndan 32 ta kompyuterning ko'rinmas tizimli belgilari (ASCII 0 dan 31 gacha bo'lgan chop etilmaydigan kodlar)ni tozalab tashlaydi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. TRIM bilan bo'shliqlarni tozalash <Badge type="tip" text="oson" />
A ustunidagi katakda `"   Samarqand   "` yozilgan. Formuladan foydalanib boshidagi va oxiridagi bo'shliqlarni olib tashlang.
**Kutiladigan natija:** Toza `"Samarqand"` matni chiqarilgan formula.

### 2. Katta-kichik harflarni to'g'rilash <Badge type="tip" text="oson" />
Ism-familiyasi kichik harflar bilan kiritilgan 4 nafar o'quvchi ro'yxatini (`"ali valiyev"`, `"hasan husanov"`) `PROPER` funksiyasi yordamida to'g'rilang.
**Kutiladigan natija:** Bosh harflari to'g'rilangan ismlar ro'yxati.

### 3. Flash Fill bilan ismni ajratish <Badge type="tip" text="oson" />
Bitta ustunda `F.I.Sh.` yozilgan (`"Aziz Rahimov"`). Yangi ustunda birinchi qatorga faqat `"Aziz"` deb yozing va `Ctrl + E` orqali qolgan barcha ismlarni avtomatik ajrating.
**Kutiladigan natija:** Faqat ismlar ajratilgan yangi ustun.

### 4. Dublikatlarni o'chirish <Badge type="tip" text="oson" />
8 ta qatordan iborat savdo ro'yxatida bir xil buyurtmalar 2 martadan takrorlangan. `Data > Remove Duplicates` vositasi orqali takroriylarni o'chiring.
**Kutiladigan natija:** Faqat unikal yozuvlar qolgan qisqargan jadval.

### 5. Formulalarni birlashtirish: TRIM + PROPER <Badge type="warning" text="o'rta" />
Katakda `"   dilshod   zaripov   "` kabi bir vaqtning o'zida ham ortiqcha bo'shliqlar, ham kichik harflar bor. Bitta formulada ikkala muammoni hal qiling.
**Kutiladigan natija:** `=PROPER(TRIM(...))` formulasining ishlagan natijasi.

### 6. Text-to-Columns bilan manzilni bo'lish <Badge type="warning" text="o'rta" />
Bitta ustunda `"Toshkent, Chilonzor, 15-uy"` ko'rinishida yozilgan manzillarni `Text-to-Columns` vositasi orqali vergul ajratgichi bo'yicha 3 ta alohida ustunga bo'ling.
**Kutiladigan natija:** Shahar, Tuman va Uy ustunlariga ajratilgan jadval.

### 7. Find & Replace bilan bo'sh qiymatlarni to'ldirish <Badge type="warning" text="o'rta" />
Savdo jadvalining `Chegirma` ustunida ba'zi kataklar bo'sh qolib ketgan. `Ctrl + H` (Find & Replace) vositasi yordamida barcha bo'sh kataklarga `0%` qiymatini kiriting.
**Kutiladigan natija:** Bo'sh joylari nol bilan to'ldirilgan ustun.

### 8. Power Query'da Split Column <Badge type="danger" text="qiyin" />
Excelda `Data > From Sheet` orqali jadvalni Power Query oynasiga yuklang. Undagi `To'liq Manzil` ustunini `Split Column by Delimiter` orqali alohida qismlarga ajrating va `Close & Load` orqali Excelga qaytaring.
**Kutiladigan natija:** Power Query orqali tozalangan yangi ishchi varaq.

### 9. Katta-kichik harfga sezgir bo'lmagan dublikatlar <Badge type="danger" text="qiyin" />
Jadvalda `"Apple"` va `"apple"` so'zlari bor. Oddiy Excel ularni ba'zan har xil deb bilishi mumkin. Power Query muhitida `Comparer.OrdinalIgnoreCase` mantiqini qo'llab, barcha harf variantlarini yagona unikal holatga keltiring.
**Kutiladigan natija:** Barcha registr variantlari tozalangan unikal natija.

### 10. Mini-loyiha: Iflos datasetni to'liq tozalash <Badge type="info" text="bonus" />
Internetdan yoki mentor bergan namunadan 10 qatordan iborat "Mijozlar bazasi"ni oling: unda ortiqcha bo'shliqlar, noto'g'ri registr, telefon raqamlari har xil formatda va dublikatlar bor. Barcha o'rganilgan vositalarni qo'llab, uni 100% toza Tidy shaklga keltiring.
**Kutiladigan natija:** Barcha nuqsonlari to'g'rilangan toza ishchi jadval.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Data Cleaning nima va nima sababdan u tahlilchi vaqtining asosiy qismini oladi?
2. `TRIM` funksiyasi matn ichidagi qaysi bo'shliqlarga ta'sir qilmaydi?
3. `Flash Fill` vositasini chaqiruvchi klaviatura birikmasi qaysi?
4. `Text-to-Columns` qanday hollarda qo'llaniladi va ajratgich (delimiter) nima?
5. GIGO qoidasi nimani anglatadi?
6. Nega Power Query tozalash jarayonini an'anaviy qo'lda tozalashdan ko'ra ustun qiladi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Excelda 6 nafar xaridordan iborat jadval tuzing. Unda ismlar katta-kichik harflar va ortiqcha bo'shliqlar bilan aralash kiritilgan bo'lsin (masalan: `"  NODIR   ALIEV  "`). Formulalar yoki matn vositalari orqali ularni toza `"Nodir Aliev"` ko'rinishiga keltirib, mentorga topshiring.

</div>

