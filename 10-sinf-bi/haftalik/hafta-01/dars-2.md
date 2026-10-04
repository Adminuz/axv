# 2-dars: Ma'lumotlar arxitekturasi va hayot sikli (Data Architecture & Data Lifecycle)

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 1-hafta, 2-dars (umumiy 2-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga zamonaviy **Ma'lumotlar arxitekturasi (Data Architecture)** ning asosiy qatlamlari (Source, Ingestion, Storage, Processing, Serving, Governance), **Ma'lumotlar hayot sikli (Data Lifecycle)** ning 7 ta bosqichi (Collect, Store, Validate, Transform, Serve, Monitor, Archive), ma'lumotlar sifati mezonlari (**Data Quality: Completeness, Accuracy, Consistency, Timeliness**) hamda real "Maktab tahliliy platformasi" misolida foydalanuvchi rollari (Direktor, Analitik, Metodist, Administrator) va ularning ssenariylarini loyihalashni o'rgatish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Ma'lumotlar arxitekturasining 6 ta asosiy qatlamini ajrata olish va ularning vazifasini tushuntirish;
- Ma'lumotlar hayot siklining 7 bosqichini ketma-ketlikda tushunish va xom ma'lumot qanday bosqichlardan o'tishini bilish;
- Data Quality (Ma'lumot sifati)ning 4 asosiy mezonini (To'liqlik, Aniqlik, Izchillik, O'z vaqtidalik) aniqlash va tekshirish;
- "Maktab tahliliy platformasi" keysi misolida turli foydalanuvchi rollari (Direktor, Analitik, Administrator) talablarini tahlil qilish;
- Administrator (Data Operator) uchun ma'lumotlarni qabul qilish, profiling, validation va tozalash ssenariysini tuza olish;
- Python va Pandas yordamida birlamchi data validation (null, duplicate, manfiy qiymatlar tekshiruvi) amallarini bajarish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun kompyuter (kamida 8 GB RAM);
- Internet tarmog'iga ulanish;
- Proyektor yoki monitor;
- Python 3, Pandas kutubxonasi va Jupyter Notebook (yoki VS Code muhiti).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan mavzuni takrorlash | DIKW piramidasi va Data Pipeline bosqichlari bo'yicha tezkor savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | Data Architecture qatlamlari, Data Lifecycle 7 bosqichi, Data Quality mezonlari |
| **30–50 min** | Keys tahlili: Maktab tahliliy platformasi | Foydalanuvchi rollari (Direktor, Analitik, Administrator) va ssenariylarni loyihalash |
| **50–70 min** | Amaliy mashg'ulot (Python bilan Data Validation) | Xom maktab ma'lumotlarida validation tekshiruvlarini (null, manfiy qiymat, duplikat) kodda bajarish |
| **70–80 min** | Xulosa va baholash | Tezkor test savollari, xulosalar va uyga vazifa |

---

## Nazariy qism (Batafsil tushuntirish)

### 1. Ma'lumotlar arxitekturasi (Data Architecture) tushunchasi

**Ma’lumotlar arxitekturasi** — bu ma’lumotlar tizimining yuqori darajadagi loyihasi (blueprints) bo‘lib, u quyidagi fundamental savollarga javob beradi:
1. Ma’lumot qayerdan paydo bo‘ladi va qanday yig‘iladi?
2. Ma’lumot qayerda va qaysi formatda saqlanadi?
3. U qanday qayta ishlanadi, tozalanadi va birlashtiriladi?
4. Yakuniy ma’lumot kimga, qanday xavfsizlik qoidalari bilan taqdim etiladi?

Zamonaviy ma'lumotlar arxitekturasi 6 ta asosiy qatlamdan iborat:

```text
[ 1. Source Layer ]     --> LMS, SIS, CSV, Excel jurnallar, API, Sensorlar
        │
[ 2. Ingestion Layer ]  --> Batch import, File upload, Streaming API
        │
[ 3. Storage Layer ]    --> Raw Data Lake (xom fayllar) & DWH ombor
        │
[ 4. Processing Layer ] --> Tozalash, Validatsiya, Normalizatsiya (ETL/ELT)
        │
[ 5. Serving Layer ]    --> Data Mart, BI Dashboard, ML Feature Store
        │
[ 6. Governance & Observability ] --> Monitoring, Logging, Data Quality, Access Control
```

- **Source layer (Manbalar):** Maktab LMS tizimi, kundalik jurnallari, davlat statistik portali eksportlari, CSV/Excel fayllar.
- **Ingestion layer (Yig‘ish):** Ma'lumotlarni qabul qilish jarayoni (fayl yuklash, avtomatik API orqali tortish).
- **Storage layer (Saqlash):** Xom ma'lumotlar saqlanadigan Raw zona (Data Lake) va tahlilga tayyor DWH (Data Warehouse).
- **Processing/Transform layer (Qayta ishlash):** Duplikatlarni o'chirish, bo'shliqlarni to'ldirish, hisob-kitoblar va agregatsiyalar.
- **Serving layer (Taqdim etish):** Tayyor ma'lumotlarni foydalanuvchilarga taqdim etish (Power BI, Tableau, SQL jadvallari, ML modellari).
- **Governance & Observability (Nazorat):** Pipeline faoliyati, xatolar monitoringi va xavfsizlikni boshqarish.

---

### 2. Ma’lumotlar hayot sikli (Data Lifecycle) - 7 bosqich

Ma’lumot ham tirik mavjudot kabi paydo bo‘ladi, rivojlanadi, xizmat qiladi va nihoyat arxivga yuboriladi:

1. **Collect / Ingest (Yig'ish):** Ma’lumotni manbalardan qabul qilib olish (masalan, hududiy maktablardan yillik CSV eksportlar).
2. **Store (Saqlash):** Olingan xom ma’lumotni hech o'zgartirmasdan `data/raw` papkasiga (Raw zone) arxivlab qo'yish va versiyalash.
3. **Validate / Clean (Tekshirish va tozalash):** Sifat tekshiruvlari: bo'sh kataklar (null), takrorlangan satrlar (duplicate), manfiy sonlar, noto'g'ri sanalarni tuzatish.
4. **Transform (O'zgartirish):** Biznes qoidalari asosida ustunlarni formatlash, hisoblashlar kiritish (masalan, o'quvchi/o'qituvchi nisbatini chiqarish).
5. **Serve / Publish (Taqdim etish):** Tayyor toza ma’lumotlarni analitiklarga, hisobotlarga va dashboardlarga chiqarish.
6. **Monitor / Log (Kuzatish):** Har bir yuklash jarayonini log qilish (nechta qator o'qildi, qancha vaqt ketdi, xatoliklar bormi).
7. **Archive / Retention (Arxivlash):** Eski yoki kam ishlatiladigan ma'lumotlarni uzoq muddatli arzon saqlash omborlariga ko'chirish yoki xavfsiz o'chirish siyosati.

---

### 3. Data Quality (Ma'lumotlar sifati)ning 4 ta ustuni

BI va Machine Learning modellarining to'g'ri ishlashi uchun ma'lumotlar quyidagi 4 mezonni qanoatlantirishi shart:

| Mezon | Inglizcha | Tavsif | Salbiy misol (Muammo) |
|---|---|---|---|
| **To'liqlik** | **Completeness** | Ma'lumotlar to'liq, muhim ustunlarda bo'sh (null/NaN) joylar bo'lmasligi kerak | Maktab o'quvchilari soni ustuni bo'sh qolib ketgan |
| **Aniqlik** | **Accuracy** | Qiymatlar haqiqatga to'g'ri kelishi, mantiqiy chegaralarda bo'lishi kerak | O'quvchilar soni `-150` yoki o'qituvchi yoshi `300` deb yozilgan |
| **Izchillik** | **Consistency** | Turli jadvallar va manbalarda bir xil standart va format qo'llanishi kerak | Bitta faylda "Toshkent", boshqasida "г. Ташкент", uchinchisida "TAS" deb yozilgan |
| **O'z vaqtidalik** | **Timeliness** | Ma'lumot kerakli vaqtda yangilangan va eskirib qolmagan bo'lishi kerak | 2026-yilgi darsliklar taqsimoti 2021-yilgi ma'lumotlar asosida rejalashtirilmoqda |

---

### 4. Loyiha keysi: "Maktab tahliliy platformasi"

Davlat ta'lim tizimida resurslarni to'g'ri taqsimlash uchun tahliliy platforma ishlab chiqilmoqda. Platformaning asosiy foydalanuvchi rollari:

#### 1) Direktor / MMTB rahbari:
- **Maqsadi:** Hudud (viloyat/tuman) kesimida maktablar, o‘quvchilar va o‘qituvchilar ko‘rsatkichlarini ko‘rish, resurs yuklamasini baholash.
- **Asosiy savollari:**
  - *"Qaysi hududlarda o‘quvchi/maktab ko‘rsatkichi juda yuqori?"* (resurs bosimi)
  - *"Qaysi hududlarda o‘quvchi/o‘qituvchi ko‘rsatkichi yuqori?"* (kadrlar yetishmovchiligi)
  - *"Bitiruvchilar soni dinamikasi qanday?"*

#### 2) Analitik (O'quv bo'limi):
- **Maqsadi:** Yillar bo'yicha trendlarni (YoY o'sish/pasayish), hududlar reytingini (RANK) va 3 yillik harakatlanuvchi o'rtacha (moving average) ko'rsatkichlarini hisoblash.
- **Asosiy savollari:**
  - *"Oxirgi 5 yilda o'quvchilar soni eng tez o'sayotgan TOP-3 hudud qaysi?"*

#### 3) Administrator (Data Operator / Engineer):
- **Maqsadi:** Xom fayllarni qabul qilish (`data/raw/`), Profiling o'tkazish, Validation qoidalarini tekshirish, Cleaning bajarish va DWH/Parquet bazasiga yuklash.
- **Pipeline tekshiruvlari:**
  - Null va duplicate mavjud emasmi?
  - Yil oralig'i to'g'rimi (2000–2026)?
  - Soni manfiy emasmi?

---

### 5. Foydalanuvchi ssenariylari

#### Direktor ssenariysi:
`Bosh sahifa` → `Dashboard` → `Filtr (Hudud / Yil)` → `KPI kartalar (Maktab, O'quvchi, O'qituvchi)` → `Yuklama tahlili (O'quvchi / O'qituvchi)` → `Reyting jadvali` → `Hisobotni yuklab olish (CSV/Excel)`

#### Administrator (Data Pipeline) ssenariysi:
`Raw CSV yuklash` → `Raw Profiling (.shape, .dtypes)` → `Validation (Null, Duplicate, Manfiy son)` → `Cleaning (strip, to_numeric)` → `Processed CSV saqlash` → `Parquet konvertatsiya` → `SQL bazaga yuklash` → `Monitoring & Loglar`

---

## Amaliy mashg'ulot (Python kod misoli)

Quyida administrator uchun xom ma'lumotlarni tekshirish (Data Validation) skripti keltirilgan:

```python
import pandas as pd
import numpy as np

# 1. Xom ma'lumotlar bilan DataFrame hosil qilamiz (xatolar bilan birga)
xom_malumot = {
    'maktab_id': [101, 102, 103, 104, 104, 105], # 104 takrorlangan (duplicate)
    'hudud': ['Toshkent', 'Samarqand', 'Andijon', 'Buxoro', 'Buxoro', None], # Bo'sh qiymat
    'oquvchilar_soni': [850, 1200, -45, 980, 980, 600], # Manfiy son (-45)
    'oqituvchilar_soni': [42, 60, 20, 50, 50, 30],
    'yil': [2024, 2024, 2024, 2024, 2024, 2024]
}

df = pd.DataFrame(xom_malumot)
print("--- Xom ma'lumotlar ---")
print(df)

# 2. DATA VALIDATION (Sifat tekshiruvi)
print("\n--- 1. Bo'sh qiymatlar (Completeness) ---")
print(df.isna().sum())

print("\n--- 2. Duplikatlar (Takrorlangan qatorlar) ---")
print(f"Duplikatlar soni: {df.duplicated().sum()}")

print("\n--- 3. Mantiqsiz qiymatlar (Accuracy) ---")
manfiy_sonlar = df[df['oquvchilar_soni'] < 0]
print(f"Manfiy qiymatli satrlar:\n{manfiy_sonlar}")

# 3. DATA CLEANING (Tozalash)
# a) Duplikatlarni o'chirish
df_clean = df.drop_duplicates().copy()

# b) Manfiy qiymatlarni to'g'rilash (masalan, modulini olish yoki filtr qilish)
df_clean['oquvchilar_soni'] = df_clean['oquvchilar_soni'].apply(lambda x: abs(x) if x < 0 else x)

# c) Bo'sh qiymatlarni to'ldirish
df_clean['hudud'] = df_clean['hudud'].fillna("Noma'lum hudud")

# d) Yangi ko'rsatkich hisoblash: Yuklama (o'quvchi / o'qituvchi nisbati)
df_clean['yuklama'] = (df_clean['oquvchilar_soni'] / df_clean['oqituvchilar_soni']).round(1)

print("\n--- Tozalangan va hisoblangan ma'lumotlar (Serving qatlami) ---")
print(df_clean)
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq: Arxitektura qatlamlarini moslashtirish
Maktab tahliliy tizimidagi quyidagi amallarni Data Architecture'ning 6 ta qatlamiga moslashtiring:
1. Hududiy ta'lim bo'limlaridan har oqshom CSV fayllarni serverga yuklash.
2. Direktor uchun Power BI'da o'quvchi/o'qituvchi nisbati interaktiv grafigini ko'rsatish.
3. Xom CSV fayllarni o'zgartirmasdan `s3://data-lake/raw/` papkasida saqlash.
4. Python orqali ustunlardagi manfiy sonlarni va bo'sh kataklarni tekshirish.
5. Har bir ETL jarayoni boshlangan va tugagan vaqtini log faylga yozib borish.
6. Maktabning elektron kundalik tizimi (Kundalik/e-Maktab bazasi).

**Yechim:**
1. Ingestion layer (Yig'ish qatlami)
2. Serving layer (Taqdim etish qatlami)
3. Storage layer (Saqlash qatlami - Raw zone)
4. Processing/Transform layer (Qayta ishlash qatlami)
5. Governance & Observability layer (Nazorat va monitoring)
6. Source layer (Manbalar qatlami)

---

### 2-topshiriq: Data Quality mezonlarini aniqlash
Quyidagi 4 ta muammoning har biri Data Quality'ning qaysi mezoniga (Completeness, Accuracy, Consistency, Timeliness) zid kelishini aniqlang:
- a) O'quvchining tug'ilgan yili `2085-yil` deb kiritilgan.
- b) Samarqand viloyati bitta faylda `Samarqand`, boshqa faylda `Samarkand reg.`, uchinchisida `SAM` deb yozilgan.
- c) O'qituvchilar ro'yxatida 50 nafar o'qituvchining mutaxassislik fan fani ustuni bo'sh qolgan.
- d) 2026-yilgi darslik taqsimoti 2019-yilgi o'quvchilar soni asosida tayyorlangan.

**Yechim:**
- a) **Accuracy (Aniqlik):** Haqiqiy hayotga mos kelmaydigan kelajakdagi sana kiritilgan.
- b) **Consistency (Izchillik):** Yagona standartlashtirilgan nomlash formatiga amal qilinmagan.
- c) **Completeness (To'liqlik):** Ma'lumotlar to'liq emas, muhim qiymatlar yetishmayapti (null/NaN).
- d) **Timeliness (O'z vaqtidalik):** Ma'lumotlar eskirgan, o'z vaqtida yangilanmagan.

---

### 3-topshiriq: Administrator validation skriptini yozish
Maktablar bo'yicha berilgan quyidagi satrlardan qaysi birlari xato ekanini aniqlang va sababini tushuntiring:
- Qator 1: `ID: 101, Nomi: "1-maktab", O'quvchilar: 1100, Yil: 2024`
- Qator 2: `ID: 102, Nomi: "2-maktab", O'quvchilar: -350, Yil: 2024`
- Qator 3: `ID: 103, Nomi: "3-maktab", O'quvchilar: 890, Yil: 1890`
- Qator 4: `ID: 101, Nomi: "1-maktab", O'quvchilar: 1100, Yil: 2024`

**Yechim:**
- Qator 2 xato: O'quvchilar soni manfiy bo'lishi mumkin emas (`-350`), bu **Accuracy** qoidasiga zid.
- Qator 3 xato: Yil mantiqsiz (`1890`), zamonaviy ta'lim monitoringi 2000–2026 yillarni qamrab oladi.
- Qator 4 xato: Qator 1 ning to'liq dublikati (`ID: 101`), birlamchi kalit (Primary Key) takrorlangan, bu **Uniqueness** va **Completeness** buzilishidir.

---

## Tezkor savol-javob (Quick Check)

1. **Savol:** Ma'lumotlar arxitekturasida Ingestion va Serving qatlamlarining asosiy farqi nimada?  
   **Javob:** Ingestion ma'lumotlarni tashqi manbalardan tizimga olib kiradi (kiruvchi oqim), Serving esa qayta ishlangan ma'lumotlarni tahlilchilar va dashboardlarga yetkazib beradi (chiquvchi oqim).

2. **Savol:** Nega xom ma'lumotni darhol tozalab, eski holatini o'chirib yuborish xato hisoblanadi?  
   **Javob:** Xom ma'lumot (Raw zone) asl haqiqat manbai hisoblanadi. Agar tozalash algoritmidagi xatolik aniqlansa, xom nusxa bo'lmasa ma'lumotni qayta tiklab bo'lmaydi.

3. **Savol:** Data Lifecycle ning 7 bosqichidan qaysi biri ma'lumotning o'chirilishi yoki arxivlanishini nazorat qiladi?  
   **Javob:** Archive / Retention bosqichi.

4. **Savol:** Agar dashboardda ko'rsatkichlar noto'g'ri chiqsa, muammo qaysi qatlamda bo'lishi mumkin?  
   **Javob:** Muammo manbadan (Source), noto'g'ri tozalashdan (Processing) yoki eskirgan ma'lumotdan (Storage/Ingestion) kelib chiqqan bo'lishi mumkin.
