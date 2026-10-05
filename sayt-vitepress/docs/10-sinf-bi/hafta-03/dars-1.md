---
title: "7-dars. 7-dars: Relyatsion jadvallar, Primary Key, Foreign Key va relyatsion yaxlitlik"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 3, "link": "/10-sinf-bi/hafta-03/"}, "g": 7, "title": "7-dars: Relyatsion jadvallar, Primary Key, Foreign Key va relyatsion yaxlitlik", "lead": "Ma'lumotlar bazasining go'zalligi uning tartibida va qat'iy intizomidadir. Agar jadvalda to'g'ri kalitlar va cheklovlar o'rnatilmasa, u tez orada tartibsiz raqamlar uyumiga aylanadi. Ushbu darsda biz relyatsion arxitekturaning asosi bo'lgan cheklovlar, Primary Key turlari, Composite kalitlar hamda bog'langan yozuvlar xavfsizligini ta'minlashni o'rganamiz.", "slide": "/slaydlar/10-sinf-bi/hafta-03/dars-1.html", "test": "/slaydlar/10-sinf-bi/hafta-03/dars-1-test.html", "tabs": [{"g": 7, "link": "/10-sinf-bi/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/10-sinf-bi/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/10-sinf-bi/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "8-dars: R-diagrammalar (ERD) loyihalash va SQLite bilan ishlash", "link": "/10-sinf-bi/hafta-03/dars-2"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Jadval sxemasi (Schema):** Jadvallarning ustunlari, ularning ma'lumot turlari va majburiy qoidalari to'plami.
- **Constraints (Cheklovlar):** Ma'lumotlar sifatini (Data Quality) baza darajasida himoyalovchi to'siqlar:
  - `NOT NULL`: Ustunda bo'sh qiymat bo'lishini taqiqlaydi;
  - `UNIQUE`: Takrorlanuvchi yozuvlarni qabul qilmaydi;
  - `CHECK`: Qiymatning mantiqiy diapazonda bo'lishini tekshiradi (masalan, `balans >= 0`);
  - `DEFAULT`: Qiymat kiritilmaganda avtomatik standart qiymat o'rnatadi.
- **Primary Key (PK):** Satrni yagona (unikal) aniqlovchi kalit. U har doim `UNIQUE` va `NOT NULL` bo'lishi shart.
- **Natural vs Surrogate Key:** 
  - *Natural Key:* Hayotiy real identifikator (JSHSHIR, pasport, VIN, ISBN);
  - *Surrogate Key:* Baza tomonidan avtomatik yaratiladigan ketma-ket sun'iy son (`id AUTOINCREMENT`).
- **Composite Primary Key (Murakkab kalit):** Bitta ustun unikal bo'la olmaganda, ikki yoki undan ortiq ustunlar birikmasidan tashkil topgan kalit (masalan, ta'lim statistikasida `PRIMARY KEY (hudud, yil)`).
- **Foreign Key (FK) va Relyatsion yaxlitlik:** Bola jadvaldagi FK faqat ota jadvalda mavjud bo'lgan PK ga havola qilishi mumkin.
- **ON DELETE xatti-harakatlari:**
  - `RESTRICT`: Ota yozuvga bog'liq bolalar mavjud bo'lsa, uni o'chirish taqiqlanadi;
  - `CASCADE`: Ota yozuv o'chirilishi bilan unga tegishli barcha bolalar yozuvlari ham avtomatik o'chiriladi;
  - `SET NULL`: Ota yozuv o'chirilganda, bolalar jadvalidagi havola `NULL` ga aylanadi.
- **Relyatsion anomaliyalar:** Jadval normalizatsiya qilinmaganda yuzaga keladigan muammolar — Insertion (qo'shish), Update (yangilash) va Deletion (o'chirish) anomaliyalari.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega yirik korxonalarda Surrogate Key afzal ko'riladi?
Natural Key (masalan, pasport seriyasi yoki telefon raqami) tabiiy ko'rinsa-da, real hayotda odamlar pasportini almashtiradi yoki telefon raqamini yangilaydi. Agar pasport raqami 20 ta bog'langan jadvalda Foreign Key qilib ishlatilgan bo'lsa, uni o'zgartirish ulkan tizimli resurs talab qiladi. Surrogate Key (`id`) esa shunchaki ichki raqam bo'lib, tashqi dunyo bilan bog'liq emas va hech qachon o'zgarmaydi.

### 2. SQLite da `PRAGMA foreign_keys = ON;` siri
Tarixiy sabablarga ko'ra va eski dasturlar bilan orqaga moslikni saqlash maqsadida SQLite o'zining standart holatida Foreign Key cheklovlarini tekshirmaydi! Ya'ni, agar siz maxsus buyruq bermasangiz, mavjud bo'lmagan mijozga bemalol buyurtma qo'shib qo'yishingiz mumkin. Shuning uchun Python'da SQLite ga ulanish bilanoq eng birinchi bo'lib `cursor.execute("PRAGMA foreign_keys = ON;")` buyrug'ini ishga tushirish majburiydir.

### 3. Normalizatsiya nima uchun kerak?
Tasavvur qiling, bitta jadvalda o'quvchi ismi, maktabi, maktab direktori va maktab manzili bitta qatorda yoziladi. Agar maktabda 1 000 ta o'quvchi bo'lsa, direktorning ismi 1 000 marta takroran yoziladi. Agar direktor almashsa, barcha 1 000 ta qatordagi ismni o'zgartirish kerak bo'ladi (Update anomaly). Agar bitta xat ketsa, baza ikkiga bo'linadi. Relatsion model buni 2 ta jadvalga (`maktablar` va `oquvchilar`) ajratish orqali hal qiladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Constraint** | Baza jadvali ustunlariga qo'yiladigan majburiy shart yoki cheklov |
| **Natural Key** | Haqiqiy hayotiy obyektga tegishli tabiiy identifikator (pasport, ISBN) |
| **Surrogate Key** | Baza tomonidan generatsiya qilinadigan sun'iy identifikator (`id`) |
| **Composite Key** | Ikki yoki undan ortiq ustunlar birikmasidan yasalgan kalit |
| **Referential Integrity** | Bog'langan jadvallar o'rtasidagi ma'lumotlar uyg'unligi va qonuniyligi |
| **ON DELETE CASCADE** | Ota yozuv o'chirilganda, unga bog'liq barcha bolalar yozuvlarini ham o'chirish qoidasi |
| **ON DELETE RESTRICT** | Bog'langan bolalari mavjud bo'lgan ota yozuvni o'chirishni taqiqlovchi qoida |
| **Insertion Anomaly** | Mustaqil ma'lumotni kiritish uchun keraksiz boshqa ma'lumotni kiritishga majbur bo'lish |
| **Update Anomaly** | Bitta ma'lumot o'zgarganda ko'plab qatorlarni o'zgartirish zaruriyati |
| **Deletion Anomaly** | Bitta ma'lumot o'chirilganda, unga aloqador boshqa qimmatli ma'lumotlarning yo'qolib ketishi |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- **Composite Key va O'zbekiston statistikasi:** Davlat statistika qo'mitasi ochiq ma'lumotlarida maktablar, tibbiyot va qishloq xo'jaligi bo'yicha deyarli barcha jadvallar `(hudud, yil)` juftligi orqali birlashtiriladi.
- **B-Tree va PK:** Har qanday relyatsion bazada Primary Key yaratilishi bilan tizim uning ustiga avtomatik ravishda B-Tree indeksini quradi. Shu sababli ID bo'yicha qidirish millionlab satrlar ichidan 1 millisekunddan kam vaqt oladi.
- **Instagram va Snowflake ID:** Instagram kabi ulkan tarmoqlarda har kuni milliardlab postlar kiritiladi. Ular oddiy `AUTOINCREMENT` o'rniga vaqt (timestamp), server ID si va generatsiyalangan sonni o'z ichiga olgan 64-bitli Snowflake ID lardan Surrogate Key sifatida foydalanadi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Cheklovlar mantiqini aniqlash <Badge type="tip" text="oson" />
Elektron tijorat tizimidagi `mahsulotlar` jadvali uchun quyidagi talablarga mos SQL cheklovlarini yozing:
- Mahsulot nomi bo'sh bo'lmasligi shart;
- Mahsulot narxi 0 dan katta bo'lishi shart;
- Ombordagi qoldiq soni manfiy bo'lmasligi (kamida 0) shart;
- Mahsulot holati odatiy holatda `'Mavjud'` bo'lishi lozim.  
**Kutiladigan natija:** Har bir talab uchun to'g'ri constraint turi (`NOT NULL`, `CHECK`, `DEFAULT`) aniqlanadi.

### 2. Natural vs Surrogate Key bahsi <Badge type="tip" text="oson" />
Nima uchun foydalanuvchining elektron pochta manzili (`email`) har doim unikal bo'lsa ham, ko'plab dasturchilar uni Primary Key qilmasdan, alohida `user_id` sun'iy kalitini kiritishadi? 2 ta asosiy sabab keltiring.  
**Kutiladigan natija:** Xotira samaradorligi va email o'zgarishi ehtimoli bo'yicha mantiqiy asoslash.

### 3. Maktab bazasi: PRAGMA tekshiruvi <Badge type="tip" text="oson" />
Python `sqlite3` orqali xotirada (`:memory:`) yangi baza yarating. `PRAGMA foreign_keys;` so'rovini bajarib, odatiy holatda uning qiymati `0` (o'chirilgan) ekanligini konsolga chiqaring. So'ngra uni yoqing (`ON`) va qiymat `1` ga o'zgarganini tekshiring.  
**Kutiladigan natija:** SQLite da xorijiy kalitlar tekshiruvini faollashtirish kodi yoziladi.

### 4. CHECK xatosini dasturiy tutib olish <Badge type="warning" text="o'rta" />
`xodimlar` jadvalini yarating: `(xodim_id PK, ism NOT NULL, maosh REAL CHECK(maosh >= 3000000))`. Python'da `try-except` blokidan foydalanib, 2 500 000 so'm maosh bilan xodim kiritishga urinib ko'ring va yuzaga kelgan `sqlite3.IntegrityError` xabarini chiroyli formatda konsolga chiqaring.  
**Kutiladigan natija:** Dastur to'xtab qolmasdan xatolik xabarini qayd etadi.

### 5. UNIQUE cheklovi va takrorlanmaslik <Badge type="warning" text="o'rta" />
`talabalar` jadvalida `pasport_seriya` ustuniga `UNIQUE` cheklovi o'rnating. Ikkita bir xil pasport seriyali talabani kiritishga urinib, bazaning takroriy yozuvga yo'l qo'ymasligini amalda isbotlang.  
**Kutiladigan natija:** Ikkinchi kiritishda xatolik yuzaga keladi.

### 6. ON DELETE RESTRICT amaliyoti <Badge type="warning" text="o'rta" />
`shahar (shahar_id PK, nom)` va `filiallar (filial_id PK, shahar_id FK)` jadvallarini yarating. Foreign Key ga `ON DELETE RESTRICT` qoidasini bering. Shaharga tegishli filiallar mavjud bo'lgan holda shaharni o'chirib ko'ring va tizim o'chirishga ruxsat bermasligini kuzating.  
**Kutiladigan natija:** Bog'liq bolalar borligi sababli ota yozuv o'chirilmaydi.

### 7. ON DELETE CASCADE bilan avtomatik tozalash <Badge type="warning" text="o'rta" />
Yuqoridagi mashqni `ON DELETE CASCADE` bilan qayta bajaring. Shahar o'chirilganda unga qarashli barcha filiallar avtomatik tarzda bazadan yo'qolishini `SELECT COUNT(*)` orqali tekshiring.  
**Kutiladigan natija:** Shahar o'chirilishi bilan filiallar soni 0 ga aylanadi.

### 8. Composite Primary Key yaratish <Badge type="warning" text="o'rta" />
Ta'lim statistikasi bo'yicha `viloyat_yillik_hisobot` jadvalini tuzing. Unda ustunlar: `viloyat TEXT`, `yil INTEGER`, `maktablar_soni INTEGER`. Jadvalga `PRIMARY KEY (viloyat, yil)` cheklovini bering. Bitta viloyatning bir xil yilini ikki marta kiritish xato berishini, lekin turli yillarini kiritish muvaffaqiyatli o'tishini sinang.  
**Kutiladigan natija:** Composite key qoidasining to'g'ri ishlashi tekshiriladi.

### 9. 3 ta relyatsion anomaliyani modellashtirish <Badge type="danger" text="qiyin" />
Tasavvur qiling, barcha ma'lumotlar bitta jadvalda saqlanmoqda: `talaba_kurs (talaba_id, ism, kurs_nomi, xona_raqami, uqituvchi_ismi)`. Ushbu jadvalda Insertion, Update va Deletion anomaliyalari qanday yuz berishini aniq ssenariylar bilan yozma bayon eting.  
**Kutiladigan natija:** Uchala anomaliyaning kelib chiqish sabablari tahlil qilinadi.

### 10. Jadvallarni normalizatsiya qilish <Badge type="danger" text="qiyin" />
9-topshiriqdagi anomaliyalarga ega `talaba_kurs` jadvalini 3 ta normalizatsiyalangan relyatsion jadvalga ajrating (`talabalar`, `kurslar`, `talaba_kurslari`). Ularning PK va FK larini aniqlang va anomaliyalar qanday yo'qolganini izohlang.  
**Kutiladigan natija:** To'g'ri relyatsion model loyihasi taklif etiladi.

### 11. Xatoni toping va tuzating <Badge type="danger" text="qiyin" />
Quyidagi DDL buyrug'ida xatolik bor:
```sql
CREATE TABLE buyurtmalar (
    id INTEGER,
    mijoz_id INTEGER,
    summa REAL CHECK summa > 0,
    PRIMARY KEY id,
    FOREIGN KEY mijoz_id REFERENCES mijozlar(id) ON DELETE CASCADE
);
```
Ushbu SQL kodidagi barcha sintaktik xatolarni (qavslar va kalit so'zlar) topib, ishchi holatga keltiring.  
**Kutiladigan natija:** Xatolardan tozalangan to'g'ri DDL kodi yoziladi.

### 12. Kompleks Maktab Tahliliy Modeli <Badge type="info" text="bonus" />
O'zbekiston ta'lim tizimi uchun 3 ta jadvaldan iborat to'liq relyatsion model yarating:
1. `hududlar (hudud_id PK, hudud_nomi UNIQUE, markaz)`
2. `maktablar (maktab_id PK, hudud_id FK, maktab_raqam, sigim CHECK > 0)`
3. `yillik_statistika (hudud_id FK, yil, oquvchilar_soni, oqituvchilar_soni, PRIMARY KEY(hudud_id, yil))`  
Python skripti orqali jadvallarni yarating, namunaviy ma'lumotlar kiriting, va hudud o'chirilganda maktablar o'chishi (`CASCADE`), lekin statistik ma'lumotlar bloklanishi (`RESTRICT`) mantiqini tekshiring.  
**Kutiladigan natija:** Murakkab relyatsion arxitektura va turli xil `ON DELETE` qoidalari to'liq sinovdan o'tkaziladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Jadval ustunlariga `CHECK` cheklovi qo'yish ma'lumotlar muhandisiga qanday foyda beradi?
2. Natural Key va Surrogate Key larning qaysi biri tizim arxitekturasi uchun xavfsizroq va nima uchun?
3. Composite Primary Key qachon ishlatiladi va unga bitta real hayotiy misol keltiring.
4. `ON DELETE CASCADE` qoidasini qo'llashda qanday xavf-xatarlar mavjud bo'lishi mumkin?
5. Insertion Anomaly nima va uni qanday qilib relyatsion model yordamida bartaraf etish mumkin?
6. Nima uchun SQLite da har bir yangi ulanishda `PRAGMA foreign_keys = ON;` buyrug'ini chaqirish tavsiya etiladi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Elektron kutubxona uchun 2 ta bog'langan jadval (`kitoblar` va `ijaralar`) sxemasini barcha cheklovlar (`NOT NULL`, `CHECK`, `UNIQUE`, `DEFAULT`) bilan loyihalang.
2. `ijaralar` jadvalida bitta kitobni ayni bir vaqtda faqat bitta kitobxon olib ketishi qoidasini va `ON DELETE RESTRICT` bog'lanishini ta'minlang.
3. Python `sqlite3` da ushbu jadvallarni yarating va cheklovlar to'g'ri ishlayotganini xatolar keltirib chiqarish orqali sinab ko'ring.

</div>

