# 10-sinf (BI va Machine Learning): 2-hafta baholash qaydnomasi

**Mavzular:**
1. Ma’lumot formatlari: Parquet va Columnar saqlash formati (Snappy siqish, Row Groups, Column Chunks, Projection/Predicate pushdown, CSV vs Parquet)
2. Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash (Binar format, JSON Schema, Schema Evolution, Kafka oqimlari, Big 4 chuqur tahlili)
3. Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari (Fayllar vs DB, Edgar Codd modeli, PK/FK yaxlitligi, ACID tamoyillari, ERD, Python `sqlite3` va `INNER JOIN`)

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Parquet & Columnar tahlil** | Ustunli saqlash mohiyati, Snappy siqish, Pushdown optimizatsiyalarini tushunish va CSV vs Parquet benchmarki | 30 ball |
| **Avro & Katta taqqoslash** | Avro arxitekturasi, Schema Evolution qoidalari, Kafka streamingdagi o'rni va Big 4 formatlar tahlili | 35 ball |
| **RDBMS, ACID & SQLite JOIN** | Edgar Codd relyatsion modeli, PK/FK cheklovlari, ACID kafolatlari, ERD chizish va SQLite da JOIN so'rovlari | 35 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Parquet & Benchmark (30) | Avro & Sxema (35) | RDBMS, ACID & JOIN (35) | Jami ball (100) | Izoh |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

---

## Mentor qaydlari va tahlil

- **Darsdagi asosiy qiyinchiliklar:**
  - O'quvchilar ko'pincha CSV va Parquet o'rtasidagi farqni kichik datasetlarda sinab ko'rib, "Parquet nega kattaroq hajm oldi?" degan savol berishadi. Ularga Parquet metadatasining (Footer) o'lchami borligi va ustunli saqlashning haqiqiy kuchi faqat minglab/millionlab qatorlarda namoyon bo'lishini tushuntirish lozim.
  - Avro formatida Schema Evolution (moslashuvchanlik) qoidalarida default qiymatsiz yangi maydon qo'shish xatolikka olib kelishini alohida ta'kidlash zarur.
  - SQLite'da `PRAGMA foreign_keys = ON;` qatori yozilmasa, SQLite sukut bo'yicha chet el kalitlarini tekshirmasligini amalda ko'rsatish talab etiladi.
