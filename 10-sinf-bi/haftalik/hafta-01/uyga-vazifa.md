# 1-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 1-dars: Ma’lumotlar muhandisligiga kirish (DIKW va Data Pipeline)

1. **DIKW tahlili:** O'zingiz tanlagan bitta real soha (masalan, yo'l harakati xavfsizligi, tibbiyot, ob-havo yoki e-tijorat) misolida DIKW piramidasining 4 ta bosqichini (Data, Information, Knowledge, Wisdom) to'liq yozib bering.
2. **Kompaniya keysi:** YouTube video platformasi foydalanuvchilar qaysi videoni yoqtirishini bilish uchun qanday ma'lumotlarni yig'adi va bu qanday qilib tavsiya tizimiga (Wisdom) aylanadi? Sxematik ko'rinishda tasvirlang.
3. **Kasbiy rollar:** Data Engineer va Data Scientist mutaxassisliklarining farqini taqqoslovchi 3 banddan iborat jadval tuzing.

---

## 2-dars: Ma'lumotlar arxitekturasi va hayot sikli

1. **Arxitektura loyihalash:** Mahalliy poliklinika yoki sport klubi uchun 6 qatlamli (Source, Ingestion, Storage, Processing, Serving, Governance) ma'lumotlar arxitekturasini qog'ozda chizing va har bir qatlamga qisqa izoh bering.
2. **Data Quality mezonlari:** Completeness, Accuracy, Consistency va Timeliness mezonlarining har biriga hayotiy misol (1 tadan to'g'ri va 1 tadan xato holat) keltiring.
3. **Resurs yuklamasi:** Agar tumandagi 10 ta maktabda 8 500 nafar o'quvchi va 340 nafar o'qituvchi bo'lsa:
   - O'quvchi / maktab yuklamasini hisoblang;
   - O'quvchi / o'qituvchi nisbatini hisoblang;
   - Tahliliy xulosa yozing.

---

## 3-dars: Ma’lumot formatlari: CSV va JSON bilan ishlash

1. **Loyiha strukturasi:** Kompyuteringizda VS Code orqali `maktab-pipeline` loyihasini oching va Medallion papkalarini yarating:
   - `data/raw/`
   - `data/bronze/`
   - `data/silver/`
   - `data/gold/`
   - `src/` va `logs/`
2. **JSON fayl yaratish:** O'zingiz yoqtirgan 3 ta fan yoki kitob haqida ierarxik (kamida bitta ichki obyekt va massiv bo'lgan) `namuna.json` faylini qo'lda yarating.
3. **Python va Pandas amaliyoti:** Python skripti yozib, o'zingiz yaratgan JSON faylni `pd.json_normalize()` orqali o'qing va ekranga `shape` hamda `head()` natijalarini chiqaring.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **1-dars vazifasi (30 ball):** DIKW piramidasi bosqichlarining to'g'ri tushunilgani, xom ma'lumot va donolik farqi hamda kasbiy rollarning to'g'ri ajratilgani.
- **2-dars vazifasi (35 ball):** Data Architecture 6 qatlami va Data Quality 4 mezonining hayotiy misollarda to'g'ri aks ettirilgani, resurs yuklamasi hisob-kitoblarining aniqligi.
- **3-dars vazifasi (35 ball):** Medallion papka strukturasining xatosiz tashkil etilgani, valid JSON strukturasi va Pandas'da `json_normalize()` ning to'g'ri qo'llangani.

### Eslatma
- O'quvchilar CSV fayllarda delimiter xatolariga va JSON fayllarda sintaksis (vergullar, qavslar yopilishi) to'g'riligiga e'tibor qaratishlarini tekshiring.
