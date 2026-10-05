# 4-dars: Ma’lumot formatlari: Parquet va Columnar saqlash formati (Snappy siqish, CSV vs Parquet)

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 2-hafta, 1-dars (umumiy 4-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga katta hajmdagi ma'lumotlarni tahlil qilishda zamonaviy sanoat standarti bo'lgan **Apache Parquet** formati va **ustunli (Columnar)** saqlash tamoyilini o'rgatish; an'anaviy satrli (Row-based: CSV, JSON) va ustunli saqlash arxitekturasi o'rtasidagi farqni tushuntirish; **Snappy** va **Gzip** siqish algoritmlari, **Projection pushdown** (kerakli ustunlarni saralab o'qish) va **Predicate pushdown** (filtrlarni disk darajasida bajarish) mexanizmlarining mohiyatini yetkazish hamda Python (`pandas`, `pyarrow`) yordamida CSV fayllarni Parquet formatiga konvertatsiya qilish, hajm va o'qish tezligini solishtirish amaliy ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Satrli (Row-based) va ustunli (Columnar) saqlash arxitekturasi farqini hamda OLAP (analitika) tizimlarida nima uchun ustunli format ustunlik qilishini tushunish;
- Apache Parquet faylining ichki tuzilishini (Header, Row Group, Column Chunk, Page, Footer/Metadata) bilish;
- Snappy siqish algoritmining tezlik va hajm bo'yicha afzalliklarini tushunish;
- Projection pushdown va Predicate pushdown tushunchalarini va ularning disk I/O operatsiyalarini qanday qisqartirishini bilish;
- Python'da `pd.to_parquet()` va `pd.read_parquet()` yordamida ma'lumotlarni yozish, o'qish va ma'lumot turlarini (schema) tekshirish;
- CSV va Parquet formatlarining diskdagi hajmi va o'qilish vaqtini Python orqali solishtirib, tahliliy hisobot tayyorlay olish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun shaxsiy kompyuter (kamida 8 GB RAM);
- Python 3.10+, VS Code yoki Jupyter Notebook muhiti;
- O'rnatilgan kutubxonalar: `pandas`, `pyarrow`, `fastparquet`;
- 1-haftada tayyorlangan `data/raw/maktab.csv` yoki 100 000+ qatordan iborat sinov datasetlari.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | CSV va JSON formatlari, tabular vs nested struktura, Medallion arxitekturasi bo'yicha savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | Row-based vs Columnar saqlash, Parquet ichki arxitekturasi, Snappy siqish, Pushdown optimizatsiyalari |
| **30–50 min** | Amaliy namoyish (Mentor bilan) | CSV faylni Parquet formatiga o'tkazish (`to_parquet`), ustunlarni saralab o'qish (Projection pushdown) |
| **50–70 min** | Mustaqil amaliy mashg'ulot | CSV va Parquet fayllarining hajmini (`os.path.getsize`) va o'qish tezligini (`time.time()`) solishtirish |
| **70–80 min** | Dars xulosasi va nazorat | Tezkor savol-javob, topshiriqlarni tekshirish va uyga vazifani tushuntirish |

---

## Nazariy qism (Batafsil konspekt)

### 1. Satrli (Row-based) vs Ustunli (Columnar) saqlash

Ma'lumotlar muhandisligida ma'lumotlarni xotirada yoki diskda qanday tartibda saqlash tahlil tezligiga bevosita ta'sir qiladi:

1. **Satrli saqlash (Row-oriented: CSV, JSON, an'anaviy RDBMS):**
   - Ma'lumotlar diskda satrma-satr yoziladi: `(1, Ali, Toshkent, 85), (2, Vali, Samarqand, 90)...`
   - **Afzalligi:** Yangi qator qo'shish (INSERT) va butun bitta yozuvni barcha ustunlari bilan o'qish (OLTP) juda tez.
   - **Kamchiligi:** Agar jadvalda 50 ta ustun bo'lsa va biz faqat bitta `baho` ustunining o'rtacha qiymatini hisoblamoqchi bo'lsak ham, diskdan barcha 50 ta ustunning ma'lumoti o'qib chiqiladi (ortiqcha disk I/O sarfi).

2. **Ustunli saqlash (Columnar: Apache Parquet, ORC):**
   - Bitta ustunga tegishli barcha qiymatlar ketma-ket bitta blokda saqlanadi:
     - `id: [1, 2, 3...]`
     - `ism: [Ali, Vali, Gani...]`
     - `viloyat: [Toshkent, Samarqand, Farg'ona...]`
     - `baho: [85, 90, 78...]`
   - **Afzalligi:**
     - **Selektiv o'qish (Projection Pushdown):** Faqat `baho` ustuni kerak bo'lsa, qolgan 49 ta ustun hatto diskdan o'qilmaydi.
     - **Yuqori darajada siqilish (High Compression):** Bir xil turdagi ma'lumotlar (masalan, faqat sonlar yoki faqat matnlar) yonma-yon turgani sababli siqish algoritmlari (Snappy, Gzip) fayl hajmini 70–85% gacha qisqartiradi.

---

### 2. Apache Parquet faylining ichki arxitekturasi

Apache Parquet — bu ochiq kodli, platformalarga bog'liq bo'lmagan, taqsimlangan tahlil tizimlari (Spark, Hive, Presto, DuckDB, Pandas) uchun maxsus yaratilgan ikkilik (binary) ustunli formatdir.

Parquet fayli quyidagi tarkibiy qismlardan iborat:
- **File Header:** Faylning Parquet ekanligini bildiruvchi 4 baytlik sehrli belgi (`PAR1`).
- **Row Groups (Satr guruhlari):** Katta datasetlar mantiqiy satr guruhlariga bo'linadi (odatda 128 MB dan 512 MB gacha). Har bir guruh ichida bir necha yuz ming qator bo'ladi.
- **Column Chunks:** Har bir Row Group ichida har bir ustun uchun alohida Column Chunk ajratiladi.
- **Pages (Sahifalar):** Column Chunk bir nechta sahifalarga bo'linadi (Data Page va Dictionary Page). Siqish va shifrlash aynan Page darajasida bajariladi.
- **File Footer (Metadata):** Faylning eng oxirida joylashadi. Unda butun jadvalning sxemasi (schema), har bir Row Group'ning joylashuvi hamda ustunlar bo'yicha **Min/Max statistikalar** saqlanadi.

> **Nega Metadata fayl oxirida (Footer) joylashadi?**  
> Chunki faylga ma'lumotlar yozilayotganda statistikalar (qatorlar soni, min/max) faqat yozib bo'lingach ma'lum bo'ladi. Footer oxirida bo'lsa, faylni bir o'tishda yozish (single-pass streaming write) mumkin bo'ladi.

---

### 3. Snappy siqish va Pushdown optimizatsiyalari

1. **Snappy siqish algoritmi:**
   - Google tomonidan ishlab chiqilgan, juda yuqori tezlikka yo'naltirilgan siqish algoritmi.
   - Parquet'da standart (default) siqish turi hisoblanadi. U Gzip kabi maksimal darajada siqmasligi mumkin, biroq dekompressiya (ochish) tezligi bir necha barobar yuqori bo'lib, CPU'ga deyarli yuklama bermaydi.

2. **Projection Pushdown (Ustunlarni surish):**
   - So'rovda ko'rsatilgan ustunlar ro'yxatiga qarab, diskdan faqat kerakli Column Chunk'lar o'qiladi. Masalan: `pd.read_parquet('data.parquet', columns=['ism', 'baho'])`.

3. **Predicate Pushdown (Shartlarni surish):**
   - Footer'dagi Min/Max statistikalar tufayli so'rov shartiga to'g'ri kelmaydigan butun boshli Row Group'lar o'qilmasdan tashlab ketiladi. Masalan, agar `yil == 2024` deb filtr berilsa va 1-Row Group'da yillar 2020–2022 oralig'ida bo'lsa, o'sha 128 MB lik blok hatto xotiraga yuklanmaydi.

---

### 4. CSV va Parquet solishtirma tahlili

| Xususiyati | CSV (Comma-Separated) | Apache Parquet |
|---|---|---|
| **Saqlash turi** | Satrli (Row-based, text) | Ustunli (Columnar, binary) |
| **Inson o'qiy olishi** | Ha (Notepad, Excel) | Yo'q (maxsus kutubxona kerak) |
| **Schema va Types** | Saqlanmaydi (hammasi matn) | Ichki metadata (qat'iy tiplar) |
| **Fayl hajmi** | Katta (siqilmagan holda) | Juda kichik (Snappy orqali 3–5 barobar kichik) |
| **O'qish tezligi (OLAP)** | Sekin (barcha ustunlar o'qiladi) | O'ta tez (faqat kerakli ustunlar) |
| **Qo'llanish doirasi** | Raw ma'lumot, tezkor eksport | Data Lake (Silver/Gold), DWH, Big Data |

---

## Kod namunalari

### 1-namuna: CSV dan Parquet yaratish va o'qish (Pandas va PyArrow)

```python
import pandas as pd
import numpy as np
import os
import time

# 1. 200 000 qatorlik namunaviy tahliliy dataset yaratamiz
n = 200_000
np.random.seed(42)

df = pd.DataFrame({
    'id': range(1, n + 1),
    'maktab_id': np.random.randint(1, 100, size=n),
    'viloyat': np.random.choice(['Toshkent', 'Samarqand', 'Buxoro', 'Fargona'], size=n),
    'fan': np.random.choice(['Matematika', 'Fizika', 'Informatika', 'Ingliz tili'], size=n),
    'baho': np.random.randint(55, 101, size=n),
    'davomat_foiz': np.random.uniform(70.0, 100.0, size=n).round(1)
})

# Papkalarni yaratamiz
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/silver', exist_ok=True)

csv_path = 'data/raw/maktab_baholar.csv'
parquet_path = 'data/silver/maktab_baholar.parquet'

# CSV formatda saqlash
df.to_csv(csv_path, index=False)
print("CSV fayl saqlandi.")

# Parquet formatda Snappy siqish bilan saqlash
df.to_parquet(parquet_path, engine='pyarrow', compression='snappy', index=False)
print("Parquet fayl saqlandi.")
```

### 2-namuna: Hajm va tezlikni taqqoslash testi

```python
# 1. Fayl hajmini solishtirish (Bayt va Megabaytlarda)
csv_size = os.path.getsize(csv_path) / (1024 * 1024)
parquet_size = os.path.getsize(parquet_path) / (1024 * 1024)

print(f"CSV hajmi: {csv_size:.2f} MB")
print(f"Parquet hajmi: {parquet_size:.2f} MB")
print(f"Iqtisod qilingan hajm: {((csv_size - parquet_size) / csv_size * 100):.1f}%")

# 2. Barcha ma'lumotlarni o'qish tezligi
start_time = time.time()
df_csv = pd.read_csv(csv_path)
csv_read_time = time.time() - start_time

start_time = time.time()
df_parquet = pd.read_parquet(parquet_path)
parquet_read_time = time.time() - start_time

print(f"CSV to'liq o'qish vaqti: {csv_read_time:.4f} sek")
print(f"Parquet to'liq o'qish vaqti: {parquet_read_time:.4f} sek")

# 3. Projection Pushdown testi (Faqat 2 ta ustunni o'qish)
start_time = time.time()
df_csv_cols = pd.read_csv(csv_path, usecols=['viloyat', 'baho'])
csv_cols_time = time.time() - start_time

start_time = time.time()
df_parq_cols = pd.read_parquet(parquet_path, columns=['viloyat', 'baho'])
parq_cols_time = time.time() - start_time

print(f"CSV 2 ustun o'qish vaqti: {csv_cols_time:.4f} sek")
print(f"Parquet 2 ustun o'qish vaqti: {parq_cols_time:.4f} sek (Ustunli o'qish samarasi!)")
```

---

## Amaliy topshiriqlar

### 1-topshiriq: Row vs Columnar saqlash farqini tahlil qilish (Oson)
Tushuntirib bering: Nega 100 ta ustunli jadvalda faqat 1 ta ustun bo'yicha `SUM()` hisoblash kerak bo'lganda, Parquet CSV ga nisbatan 20 barobar tezroq ishlaydi?

**Kutiladigan natija:** O'quvchi Projection pushdown tushunchasini tushuntiradi.  
**Yechim:**  
CSV row-based bo'lgani uchun xotiraga barcha 100 ta ustun o'qiladi (barcha satrlar to'liq baytma-bayt skanerlanadi). Parquet columnar format bo'lgani uchun diskdan faqat o'sha bitta ustunning Column Chunk'i o'qiladi, qolgan 99 ta ustun hatto ochilmaydi. Bu esa disk I/O operatsiyalarini deyarli 99% ga tejaydi.

---

### 2-topshiriq: Siqish algoritmlarini sinash (O'rta)
Berilgan DataFrame'ni uch xil usulda saqlang:
1. Siqishsiz (`compression=None`);
2. Snappy siqish bilan (`compression='snappy'`);
3. Gzip siqish bilan (`compression='gzip'`).
Uchala fayl hajmini `os.path.getsize` yordamida konsolga chiqaring.

**Kutiladigan natija:** Har bir siqish turining hajmi chiqariladi.  
**Yechim:**  
```python
df.to_parquet('test_none.parquet', compression=None)
df.to_parquet('test_snappy.parquet', compression='snappy')
df.to_parquet('test_gzip.parquet', compression='gzip')

print("None:", os.path.getsize('test_none.parquet'), "bayt")
print("Snappy:", os.path.getsize('test_snappy.parquet'), "bayt")
print("Gzip:", os.path.getsize('test_gzip.parquet'), "bayt")
# Gzip eng kichik hajm beradi, lekin Snappy tezroq yoziladi va o'qiladi.
```

---

### 3-topshiriq: Parquet metadata va sxemasini o'rganish (Qiyin)
`pyarrow.parquet` moduli yordamida Parquet faylining metadatasini o'qing: faylda nechta Row Group borligi, qatorlar soni va har bir ustunning ma'lumot turini konsolga chiqaring.

**Kutiladigan natija:** Faylning texnik parametrlari pyarrow orqali chiqariladi.  
**Yechim:**  
```python
import pyarrow.parquet as pq

table = pq.read_table('data/silver/maktab_baholar.parquet')
metadata = table.schema
print("Sxema:")
print(metadata)

parquet_file = pq.ParquetFile('data/silver/maktab_baholar.parquet')
print("\nFayl metadatasi:")
print("Row Groups soni:", parquet_file.num_row_groups)
print("Jami qatorlar soni:", parquet_file.metadata.num_rows)
print("Format versiyasi:", parquet_file.metadata.format_version)
```

---

## Tezkor nazorat savollari

1. Parquet fayli nima uchun matn muharririda (masalan, Notepad) ochilganda tushunarsiz belgilar ko'rinadi?  
   *Javob:* Chunki Parquet binary (ikkilik) formatda saqlanadi va siqish algoritmlari bilan kodlangan.
2. Parquet arxitekturasida File Metadata (Footer) nega faylning boshida emas, balki oxirida joylashgan?  
   *Javob:* Streaming rejimida ma'lumotlar yozilayotganda qatorlar soni va min/max statistikalar faqat yozuv tugagach aniqlanadi.
3. Projection pushdown nima?  
   *Javob:* So'rovda ko'rsatilgan ustunlarni disk darajasida aniqlab, faqat o'sha ustunlarni xotiraga o'qish imkoniyati.
4. Snappy siqish algoritmining Gzip'dan asosiy ustunligi nimada?  
   *Javob:* Snappy dekompressiya (ochish) va kompressiya jarayonida ancha yuqori tezlikka ega va CPU resurslarini kamroq sarflaydi.

---

## Uyga vazifa

1. O'zingiz topgan yoki yaratgan kamida 50 000 qatorlik CSV faylni olib, uni Pandas yordamida Snappy siqish bilan Parquet formatiga o'tkazing.
2. Ikkala fayl hajmini o'lchab, Parquet necha foiz joy tejaganini hisoblang.
3. Butun faylni o'qish va faqat 2 ta ustunni o'qish vaqtlarini solishtirib, qisqa xulosa yozing.
