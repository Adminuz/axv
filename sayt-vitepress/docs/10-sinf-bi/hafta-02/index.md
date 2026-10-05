---
title: "2-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "n": 2, "bob": "I-bob · Ma’lumotlar muhandisligiga kirish va ma’lumotlarni boshqarish", "lessons": [{"g": 4, "title": "4-dars: Ma’lumot formatlari: Parquet va Columnar saqlash formati (Snappy siqish, CSV vs Parquet)", "lead": "Katta hajmdagi ma'lumotlar olamida saqlash joyi va o'qish tezligi hal qiluvchi ahamiyatga ega. Ushbu darsda biz zamonaviy analitika poydevori bo'lgan Apache Parquet formatining ichki mo'jizalarini, ustunli saqlash tamoyilini va Snappy siqish qudratini o'rganamiz.", "link": "/10-sinf-bi/hafta-02/dars-1", "slide": "/slaydlar/10-sinf-bi/hafta-02/dars-1.html", "test": "/slaydlar/10-sinf-bi/hafta-02/dars-1-test.html"}, {"g": 5, "title": "5-dars: Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash", "lead": "Real-time rejimida millionlab voqealarni uzatishda har bir bayt hisobda turadi. Ushbu darsda biz Apache Kafka va oqimli tizimlarning sevimlisi bo'lgan Apache Avro formatini hamda Data Engineeringdagi \"Katta to'rtlik\" (CSV, JSON, Parquet, Avro) formatlarining o'zaro raqobatini o'rganamiz.", "link": "/10-sinf-bi/hafta-02/dars-2", "slide": "/slaydlar/10-sinf-bi/hafta-02/dars-2.html", "test": "/slaydlar/10-sinf-bi/hafta-02/dars-2-test.html"}, {"g": 6, "title": "6-dars: Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari", "lead": "Bugungi raqamli iqtisodiyot — bu milliardlab bog'langan ma'lumotlar oqimidir. Har bir bank o'tkazmasi, har bir xarid va har bir avtorizatsiya ortida ma'lumotlar bazasi va uning qat'iy qoidalari turadi. Ushbu darsda biz nima uchun fayllar davri o'tib, RDBMS (Relatsion ma'lumotlar bazalari) dunyoni boshqarayotganini, Edgar Codd kashfiyotini, ACID tamoyillarini hamda SQL qudratini o'rganamiz.", "link": "/10-sinf-bi/hafta-02/dars-3", "slide": "/slaydlar/10-sinf-bi/hafta-02/dars-3.html", "test": "/slaydlar/10-sinf-bi/hafta-02/dars-3-test.html"}], "test": "/slaydlar/10-sinf-bi/hafta-02/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Mazkur haftada o'tilgan darslar (Parquet, Avro va RDBMS asoslari) bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

### 4-dars: Ma’lumot formatlari: Parquet va Columnar saqlash formati

1. **Format konvertatsiyasi:** O'zingiz qiziqqan soha (futbol statistikasi, ob-havo, e-tijorat yoki maktab baholari) bo'yicha kamida 50 000 qatorlik CSV dataset toping yoki yarating. Uni Python Pandas yordamida Parquet (`compression='snappy'`) formatiga o'tkazing.
2. **Benchmark tahlili:** `os.path.getsize()` va `time` moduli yordamida ikkala fayl hajmini hamda bitta ustun bo'yicha o'rtacha qiymat (`mean()`) hisoblash vaqtini o'lchang.
3. **Hisobot:** CSV va Parquet natijalarini (hajm, tezlik, tejalgan disk maydoni foizi) taqqoslovchi kichik 1 betlik tahliliy hisobot tayyorlang.

---

### 5-dars: Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash

1. **Avro sxemasi loyihalash:** Foydalanuvchi profili uchun `user.avsc` JSON sxemasini yozing. Unda: `user_id` (long), `username` (string), `email` (string), `status` (enum: "ACTIVE", "BANNED", "PENDING") va ixtiyoriy `telefon` (union: ["null", "string"], default: null) bo'lsin.
2. **fastavro amaliyoti:** Python `fastavro` kutubxonasi yordamida kamida 3 nafar namunaviy foydalanuvchini ushbu sxema asosida `users.avro` fayliga yozing va qayta o'qib konsolga chiqaring.
3. **Formatlar tanlovi:** 3 xil real ssenariy (Streaming loglar, Data Warehouse analitikasi, Foydalanuvchi mobil sozlamalari) uchun mos formatni (CSV, JSON, Parquet, Avro) tanlang va sababini tushuntiring.

---

### 6-dars: Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari

1. **ERD loyihalash:** O'zingiz bilgan real tizim (kutubxona, avtosalon, poliklinika yoki mehmonxona) uchun kamida 3 ta jadvaldan iborat relyatsion model (ER-diagramma) chizing.
2. **Kalitlar va cheklovlar:** Modelda qaysi ustunlar Primary Key, qaysilari Foreign Key ekanligini aniq ko'rsating va relyatsion yaxlitlik qoidalarini belgilang.
3. **Python va SQLite amaliyoti:** Python `sqlite3` moduli yordamida ushbu 3 ta jadvalni yaratuvchi, har biriga kamida 2 tadan yozuv qo'shuvchi va `INNER JOIN` orqali birlashgan hisobot chiqaruvchi skript yozing.

---

</div>
