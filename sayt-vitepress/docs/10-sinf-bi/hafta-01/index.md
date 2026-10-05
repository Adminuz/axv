---
title: "1-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "n": 1, "bob": "I-bob · Ma’lumotlar muhandisligiga kirish va ma’lumotlarni boshqarish", "lessons": [{"g": 1, "title": "1-dars: Ma’lumotlar muhandisligiga kirish (Data Engineering asoslari)", "lead": "**\"Garbage In, Garbage Out\" qoidasi:** Agar tizimga kiruvchi ma'lumot xato yoki iflos bo'lsa, eng mukammal sun'iy intellekt ham xato natija beradi. Shuning uchun Data Engineering — butun AI va analitikaning poydevoridir.", "link": "/10-sinf-bi/hafta-01/dars-1", "slide": "/slaydlar/10-sinf-bi/hafta-01/dars-1.html", "test": "/slaydlar/10-sinf-bi/hafta-01/dars-1-test.html"}, {"g": 2, "title": "2-dars: Ma'lumotlar arxitekturasi va hayot sikli (Data Architecture & Data Lifecycle)", "lead": "Ma'lumotlar arxitekturasi va hayot sikli (6 qatlam, 7 bosqich, Data Quality mezonlari)", "link": "/10-sinf-bi/hafta-01/dars-2", "slide": "/slaydlar/10-sinf-bi/hafta-01/dars-2.html", "test": "/slaydlar/10-sinf-bi/hafta-01/dars-2-test.html"}, {"g": 3, "title": "3-dars: Ma’lumot formatlari: CSV va JSON bilan ishlash", "lead": "Ma’lumot formatlari: CSV va JSON bilan ishlash (Tabular vs Nested, Medallion arxitekturasi)", "link": "/10-sinf-bi/hafta-01/dars-3", "slide": "/slaydlar/10-sinf-bi/hafta-01/dars-3.html", "test": "/slaydlar/10-sinf-bi/hafta-01/dars-3-test.html"}], "test": "/slaydlar/10-sinf-bi/hafta-01/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

### 1-dars: Ma’lumotlar muhandisligiga kirish (DIKW va Data Pipeline)

1. **DIKW tahlili:** O'zingiz tanlagan bitta real soha (masalan, yo'l harakati xavfsizligi, tibbiyot, ob-havo yoki e-tijorat) misolida DIKW piramidasining 4 ta bosqichini (Data, Information, Knowledge, Wisdom) to'liq yozib bering.
2. **Kompaniya keysi:** YouTube video platformasi foydalanuvchilar qaysi videoni yoqtirishini bilish uchun qanday ma'lumotlarni yig'adi va bu qanday qilib tavsiya tizimiga (Wisdom) aylanadi? Sxematik ko'rinishda tasvirlang.
3. **Kasbiy rollar:** Data Engineer va Data Scientist mutaxassisliklarining farqini taqqoslovchi 3 banddan iborat jadval tuzing.

---

### 2-dars: Ma'lumotlar arxitekturasi va hayot sikli

1. **Arxitektura loyihalash:** Mahalliy poliklinika yoki sport klubi uchun 6 qatlamli (Source, Ingestion, Storage, Processing, Serving, Governance) ma'lumotlar arxitekturasini qog'ozda chizing va har bir qatlamga qisqa izoh bering.
2. **Data Quality mezonlari:** Completeness, Accuracy, Consistency va Timeliness mezonlarining har biriga hayotiy misol (1 tadan to'g'ri va 1 tadan xato holat) keltiring.
3. **Resurs yuklamasi:** Agar tumandagi 10 ta maktabda 8 500 nafar o'quvchi va 340 nafar o'qituvchi bo'lsa:
   - O'quvchi / maktab yuklamasini hisoblang;
   - O'quvchi / o'qituvchi nisbatini hisoblang;
   - Tahliliy xulosa yozing.

---

### 3-dars: Ma’lumot formatlari: CSV va JSON bilan ishlash

1. **Loyiha strukturasi:** Kompyuteringizda VS Code orqali `maktab-pipeline` loyihasini oching va Medallion papkalarini yarating:
   - `data/raw/`
   - `data/bronze/`
   - `data/silver/`
   - `data/gold/`
   - `src/` va `logs/`
2. **JSON fayl yaratish:** O'zingiz yoqtirgan 3 ta fan yoki kitob haqida ierarxik (kamida bitta ichki obyekt va massiv bo'lgan) `namuna.json` faylini qo'lda yarating.
3. **Python va Pandas amaliyoti:** Python skripti yozib, o'zingiz yaratgan JSON faylni `pd.json_normalize()` orqali o'qing va ekranga `shape` hamda `head()` natijalarini chiqaring.

---

</div>
