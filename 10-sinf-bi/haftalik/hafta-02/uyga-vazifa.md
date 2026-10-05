# 2-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar (Parquet, Avro va RDBMS asoslari) bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 4-dars: Ma’lumot formatlari: Parquet va Columnar saqlash formati

1. **Format konvertatsiyasi:** O'zingiz qiziqqan soha (futbol statistikasi, ob-havo, e-tijorat yoki maktab baholari) bo'yicha kamida 50 000 qatorlik CSV dataset toping yoki yarating. Uni Python Pandas yordamida Parquet (`compression='snappy'`) formatiga o'tkazing.
2. **Benchmark tahlili:** `os.path.getsize()` va `time` moduli yordamida ikkala fayl hajmini hamda bitta ustun bo'yicha o'rtacha qiymat (`mean()`) hisoblash vaqtini o'lchang.
3. **Hisobot:** CSV va Parquet natijalarini (hajm, tezlik, tejalgan disk maydoni foizi) taqqoslovchi kichik 1 betlik tahliliy hisobot tayyorlang.

---

## 5-dars: Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash

1. **Avro sxemasi loyihalash:** Foydalanuvchi profili uchun `user.avsc` JSON sxemasini yozing. Unda: `user_id` (long), `username` (string), `email` (string), `status` (enum: "ACTIVE", "BANNED", "PENDING") va ixtiyoriy `telefon` (union: ["null", "string"], default: null) bo'lsin.
2. **fastavro amaliyoti:** Python `fastavro` kutubxonasi yordamida kamida 3 nafar namunaviy foydalanuvchini ushbu sxema asosida `users.avro` fayliga yozing va qayta o'qib konsolga chiqaring.
3. **Formatlar tanlovi:** 3 xil real ssenariy (Streaming loglar, Data Warehouse analitikasi, Foydalanuvchi mobil sozlamalari) uchun mos formatni (CSV, JSON, Parquet, Avro) tanlang va sababini tushuntiring.

---

## 6-dars: Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari

1. **ERD loyihalash:** O'zingiz bilgan real tizim (kutubxona, avtosalon, poliklinika yoki mehmonxona) uchun kamida 3 ta jadvaldan iborat relyatsion model (ER-diagramma) chizing.
2. **Kalitlar va cheklovlar:** Modelda qaysi ustunlar Primary Key, qaysilari Foreign Key ekanligini aniq ko'rsating va relyatsion yaxlitlik qoidalarini belgilang.
3. **Python va SQLite amaliyoti:** Python `sqlite3` moduli yordamida ushbu 3 ta jadvalni yaratuvchi, har biriga kamida 2 tadan yozuv qo'shuvchi va `INNER JOIN` orqali birlashgan hisobot chiqaruvchi skript yozing.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **4-dars vazifasi (30 ball):** CSV dan Parquet ga muvaffaqiyatli konvertatsiya qilingani, Snappy siqish qo'llangani, hajm va tezlik benchmarki aniq raqamlarda ko'rsatilgani.
- **5-dars vazifasi (35 ball):** Valid Avro sxemasi (`.avsc`) yaratilgani, `fastavro` orqali binar serializatsiya va deserializatsiyaning xatosiz ishlashi, Big 4 formatlar qiyosiy tahlili to'g'riligi.
- **6-dars vazifasi (35 ball):** ERD loyihasi to'g'ri chizilgani (1:N bog'lanishlar), SQLite da PK va FK cheklovlari xatosiz o'rnatilgani, ma'lumotlar to'g'ri kiritilgani va `INNER JOIN` so'rovi to'g'ri yozilgani.

### Eslatma
- O'quvchilarga SQLite'da `PRAGMA foreign_keys = ON;` qatori ishlatilmasa, Foreign Key cheklovlari tekshirilmay ketishi mumkinligini doimo eslatib turing.
- Avro fayllarni oddiy matn muharririda ochib bo'lmasligi, binar format ekanligi haqida tushuncha bering.
