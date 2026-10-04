---
title: "3-dars. BI tizimlari turlari, mutaxassislik rollari va Excel analitik platformasi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (BI)", "link": "/9-sinf-bi/"}, "week": {"n": 1, "link": "/9-sinf-bi/hafta-01/"}, "g": 3, "title": "BI tizimlari turlari, mutaxassislik rollari va Excel analitik platformasi", "lead": "Katta biznes qanday boshqariladi: BI tizimlarining turlari, jamoaviy rollar va barcha tahlillar poydevori bo'lgan Microsoft Excel bilan yaqindan tanishing.", "slide": "/slaydlar/9-sinf-bi/hafta-01/dars-3.html", "tabs": [{"g": 1, "link": "/9-sinf-bi/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/9-sinf-bi/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/9-sinf-bi/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "Business Intelligence (BI) asoslari: Katta to'rtlik va hayotiy sikl", "link": "/9-sinf-bi/hafta-01/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- BI tizimlari o'z qo'llanilish maqsadi va tezligiga ko'ra 4 asosiy turga bo'linadi: Operatsional, Strategik, Self-Service va Integratsiyalashgan (Embedded) BI.
- Operatsional BI real vaqt rejimida kundalik operatsiyalarni nazorat qilish uchun, Strategik BI esa uzoq muddatli rejalashtirish uchun xizmat qiladi.
- Self-Service BI (Power BI, Tableau) har bir mutaxassisga IT yordamisiz mustaqil hisobotlar yaratish imkonini beradi.
- BI sohasidagi asosiy rollar: Data Engineer (infratuzilma), Data Analyst (tahlil va xulosalar), BI Developer (dashboard dizayni) va Business User (qaror qabul qiluvchi rahbar).
- Microsoft Excel — ma'lumotlar tahlilining fundamental platformasi bo'lib, analitik tafakkur va jadval gigiyenasini shakllantiradi.
- Excel ishchi kitobi (Workbook) varaqlar (Worksheets), ustunlar (Columns), qatorlar (Rows) va kataklardan (Cells) tashkil topadi.
- Ma'lumot turlarini (Text, Number, Date, Currency, Percentage) to'g'ri tanlash hisob-kitoblar aniqligining garovidir.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega Self-Service BI juda muhim?
Ilgari korxonalarda har qanday kichik hisobot yoki grafik uchun dasturchilarga yozma talabnoma yuborilar edi. Dasturchilar esa haftalab band bo'lib, oddiy marketing hisoboti o'z vaqtida tayyor bo'lmasdi.
Self-Service BI dasturlari (masalan, Power BI Desktop) interfeysni shunchalik soddalashtirdiki, endi iqtisodchi, sotuvchi yoki marketolog sichqoncha yordamida o'zi xohlagan grafikni bir necha daqiqada yasab oladi. Bu esa ma'lumotlarning "demokratlashuvi" deb ataladi.

### 2. BI jamoasining hamkorlik zanjiri
Biror yirik bankni tasavvur qiling:
1. **Data Engineer:** Millionlab bank tranzaksiyalarini xavfsiz tozalab, omborga yig'adi.
2. **Data Analyst:** Qaysi viloyatlarda kredit to'lash kechikayotgani sabablarini aniqlaydi.
3. **BI Developer:** Boshqaruv kengashi uchun qulay va chiroyli interaktiv panel yaratadi.
4. **Bank Boshqaruvi:** Panelni ko'rib, foiz stavkalarini o'zgartirish yoki yangi filial ochish to'g'risida qaror qabul qiladi.

### 3. Excelda kataklar manzili va ma'lumot turlari
Excelda har bir katak o'zining unikal manziliga ega:
- Masalan, `C5` — bu 3-ustun (C) va 5-qator kesishmasidagi katakdir.
- **Katta xato:** Raqamli ma'lumotlarni matn sifatida saqlash! Agar siz katakka `15000 so'm` deb so'z qo'shib yozsangiz, Excel buni matn (Text) deb qabul qiladi va matematik qo'shish (SUM) amalini bajara olmaydi. To'g'ri usul — faqat `15000` sonini yozib, katak formatini Currency (Valyuta) qilib belgilashdir.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Operational BI** | Kundalik jarayonlarni real vaqtda kuzatish va tezkor qarorlar qabul qilish tizimi. |
| **Strategic BI** | Kompaniyaning uzoq muddatli rivojlanish strategiyasi va maqsadlarini tahlil qilish tizimi. |
| **Self-Service BI** | Texnik bo'lmagan xodimlar tomonidan mustaqil hisobotlar yaratish imkoniyati. |
| **Embedded BI** | Analitikaning boshqa ilova (CRM, ERP) ichiga to'g'ridan-to'g'ri o'rnatilishi. |
| **Data Analyst** | Ma'lumotlarni tahlil qilib, biznes uchun qimmatli tushunchalar (insights) chiqaruvchi mutaxassis. |
| **Data Engineer** | Ma'lumot quvurlari (ETL) va omborlar infratuzilmasini quruvchi muhandis. |
| **Workbook** | Microsoft Excel dasturidagi umumiy ishchi fayl (.xlsx). |
| **Worksheet** | Ishchi kitob ichidagi alohida elektron jadval varag'i. |
| **Cell (Katak)** | Ustun va qator kesishmasidagi asosiy ma'lumot birligi (masalan, B2). |
| **Data Type** | Katakka kiritilgan qiymatning turi (son, matn, sana, mantiqiy). |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Microsoft Excel dasturining birinchi versiyasi 1985 yilda dastlab faqat Apple Macintosh kompyuterlari uchun chiqarilgan!
- Bitta zamonaviy Excel varag'ida **1 048 576 ta qator** va **16 384 ta ustun** (jami 17 milliarddan ortiq katak) mavjud.
- Dunyodagi har 10 ta yirik kompaniyadan 9 tasi bugungi kunda ham birlamchi hisob-kitoblar uchun Exceldan keng foydalanadi.
- Excelda 500 dan ortiq tayyor matematik, moliyaviy va statistik funksiyalar mavjud.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. BI turini aniqlash <Badge type="tip" text="oson" />
Quyidagi vaziyat BI tizimining qaysi turiga kirishini aniqlang:
*"Bank ilovasida foydalanuvchi o'zining oylik xarajatlari qaysi toifalarga (oziq-ovqat, transport, kiyim) sarflanganini ko'rsatuvchi doiraviy grafikni ko'rmoqda".*
**Kutiladigan natija:** To'g'ri BI turi nomi va 1 jumlalik asos.

### 2. Mutaxassislik vazifalarini taqsimlash <Badge type="tip" text="oson" />
Quyidagi vazifani qaysi mutaxassis (Data Engineer yoki Data Analyst) bajarishi kerakligini aniqlang:
a) Do'kon serverlaridagi ma'lumotlar bazasini har kecha zaxiralash va xatosiz uzatish;
b) Xaridorlarning yoshi va ularning o'rtacha xarid summasi o'rtasidagi bog'liqlikni aniqlash.
**Kutiladigan natija:** Har bir bandga mos mutaxassislik nomi.

### 3. Excel katak manzillarini topish <Badge type="tip" text="oson" />
Daftaringizga quyidagi kataklar koordinatasini yozing:
- 4-ustun va 8-qator kesishmasi;
- 1-ustun va 1-qator kesishmasi;
- 26-ustun (alfabitning oxirgi harfi) va 100-qator kesishmasi.
**Kutiladigan natija:** 3 ta katakning standart kodi (masalan: D8...).

### 4. Ma'lumot turini to'g'ri tanlash <Badge type="tip" text="oson" />
Quyidagi ma'lumotlar uchun Excelda qaysi ma'lumot turini tanlash kerak:
1. Xarid qilingan nonning narxi (`4000 so'm`)
2. Maktab direktori ismi (`Anvar Rahimov`)
3. Shartnoma imzolangan kun (`2026-10-04`)
4. O'quvchining fan bo'yicha o'zlashtirish ko'rsatkichi (`92%`)
**Kutiladigan natija:** Har biriga mos format turi (Currency, Text, Date, Percentage).

### 5. Strategik vs Operatsional BI taqqosi <Badge type="warning" text="o'rta" />
Katta aviakompaniya misolida Strategik BI va Operatsional BI qanday ishlashini tushuntiring:
- Aviakompaniya dispetcheri nima uchun operatsional paneldan foydalanadi?
- Aviakompaniya rahbari yangi samolyotlar sotib olish uchun qanday hisobotlarni ko'radi?
**Kutiladigan natija:** 2 ta BI turining aviakompaniya faoliyatidagi real vazifalari.

### 6. Embedded BI ning qulayligi <Badge type="warning" text="o'rta" />
Nima uchun xodimlar alohida tahlil dasturiga kirmasdan, to'g'ridan-to'g'ri CRM yoki Telegram-bot ichida grafik va ko'rsatkichlarni ko'rishni ma'qul ko'rishadi?
**Kutiladigan natija:** Foydalanuvchi qulayligi (UX) va ish unumdorligi bo'yicha 2-3 jumlalik xulosa.

### 7. Excelda xatolikni aniqlash <Badge type="warning" text="o'rta" />
Sotuvchi Excelda quyidagicha jadval tuzdi:
- A1: "Mahsulot", B1: "Narx", C1: "Miqdor", D1: "Jami"
- A2: "Daftar", B2: "5 000 so'm", C2: "10 dona", D2: `=B2*C2`
Natijada D2 katagida `#VALUE!` xatoligi paydo bo'ldi. Nima sababdan bu xato yuz berdi va uni qanday to'g'rilash kerak?
**Kutiladigan natija:** Xatolik sababi va to'g'ri kiritish qoidasi.

### 8. Futbol klubi uchun BI jamoasi <Badge type="danger" text="qiyin" />
Professional futbol klubida ma'lumotlar tahlili jamoasi tuzilmoqda. Jamoa futbolchilarning o'yindagi yugurish masofasi, paslar aniqligi va jarohat olish xavfini tahlil qilishi kerak.
Ushbu loyihada Data Engineer, Data Analyst va BI Developer qanday vazifalarni bajarishini rejalashtiring.
**Kutiladigan natija:** Futbol klubi misolida har bir mutaxassisning aniq vazifalar ro'yxati.

### 9. O'quv markazi hisobot jadvalini loyihalash <Badge type="danger" text="qiyin" />
O'quv markazi uchun Excelda o'quvchilar reytingi jadvalini loyihalashtiring:
- Kamida 6 ta ustun (ID, Ism, Guruh, Sinov 1, Sinov 2, O'rtacha ball).
- Har bir ustunning turi va o'rtacha ballni hisoblash formulasini ko'rsating.
**Kutiladigan natija:** To'liq jadval arxitekturasi va formulasi.

### 10. Mini-tadqiqot: Qaysi kasb sizga yaqinroq? <Badge type="info" text="bonus" />
Data Engineer (ma'lumotlar muhandisi) va Data Analyst (ma'lumotlar tahlilchisi) kasblarini o'rganib chiqing. Kelajakda ularning qaysi biri sizning qiziqishingizga (dasturiy infratuzilma qurishmi yoki ma'lumotlardan qonuniyatlar topishmi) ko'proq mos kelishini asoslab bering.
**Kutiladigan natija:** O'z qiziqishlaringiz tahlil qilingan kichik insho (10-15 jumla).

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Operatsional BI va Strategik BI o'rtasidagi asosiy vaqt farqi nimada?
2. Self-Service BI atamasidagi "Self-Service" (o'z-o'ziga xizmat) nimani anglatadi?
3. Nima uchun Data Engineer bo'lmasa, Data Analyst sifatli ishlay olmaydi?
4. Excel ishchi kitobi (Workbook) va ishchi varag'i (Worksheet) o'rtasida qanday farq bor?
5. Excelda katak nima va uning manzili qanday belgilanadi?
6. Nega katakdagi son yoniga qo'lda so'z (masalan "so'm") yozish hisob-kitobni buzadi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Excel dasturida o'zingizning 5 nafar do'stingiz haqida kichik jadval tuzing. Unda "Ism", "Tug'ilgan sana", "Bo'yi (sm)", "Sevimli fani" degan 4 ta ustun bo'lsin. Har bir ustun uchun to'g'ri formatni (Text, Date, Number) belgilang va ekranni rasmga olib (skrinshot) mentorga ko'rsating.

</div>

