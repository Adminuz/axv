# 3-dars: Ma’lumot formatlari: CSV va JSON bilan ishlash

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 1-hafta, 3-dars (umumiy 3-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga zamonaviy axborot tizimlarida ma'lumotlarni saqlash va almashishning eng ommabop formatlari — **CSV (Comma-Separated Values)** va **JSON (JavaScript Object Notation)** ning ichki tuzilishi, satrli (tabular) va ierarxik (nested) ma'lumotlar farqi, Data Engineeringda loyiha papkalari ierarxiyasi (**Medallion arxitekturasi: raw, bronze, silver, gold**), ma'lumotlarni o'qishda uchraydigan kodlash (**encoding: UTF-8 va CP1251**) muammolari hamda Python va **Pandas** kutubxonasi yordamida CSV/JSON fayllarni o'qish, profillash (`info()`, `describe()`, `isna()`) va `json_normalize()` orqali tekislash amallarini o'rgatish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- CSV va JSON formatlarining afzalliklari, kamchiliklari va qo'llanish sohalarini aniq tushunish;
- Satrli (tabular) va ichma-ich ierarxik (nested) ma'lumotlar tuzilishining farqini bilish;
- Data Engineering loyihalarida `data/raw`, `data/bronze`, `data/silver`, `data/gold`, `src` va `logs` papkalarining vazifalarini bilish;
- CSV fayllarda uchraydigan delimiter (ajratgich: vergul, nuqta-vergul, tab) va encoding (`UnicodeDecodeError`, `cp1251` vs `utf-8`) xatoliklarini dasturiy hal qilish;
- Python va Pandas yordamida CSV va JSON fayllarni o'qish, ustunlarni tekshirish va birlamchi profillashni bajarish;
- `pd.json_normalize()` funksiyasi orqali murakkab nested JSON obyektlarini munosabatli jadval ko'rinishiga keltira olish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun shaxsiy kompyuter (kamida 8 GB RAM);
- Internet tarmog'iga ulanish;
- Python 3, Pandas kutubxonasi, Jupyter Notebook yoki VS Code muhiti;
- Namuna CSV va JSON fayllar to'plami.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va o'tgan darsni takrorlash | Data Architecture qatlamlari va Data Quality 4 mezoni bo'yicha savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | CSV va JSON formati, tabular vs nested struktura, Medallion arxitekturasi, encoding muammolari |
| **30–50 min** | Amaliy namoyish (O'qituvchi bilan birgalikda) | VS Code loyiha strukturasi, CSV faylni o'qish, encoding xatosini `try-except` bilan yechish |
| **50–70 min** | Mustaqil amaliy mashg'ulot | JSON faylni yuklash, `json_normalize()` orqali ichma-ich tuzilmani jadvalga aylantirish |
| **70–80 min** | Dars xulosasi va baholash | Tezkor savol-javob, 1-hafta umumiy xulosalari va uyga vazifa topshirish |

---

## Nazariy qism (Batafsil tushuntirish)

### 1. CSV (Comma-Separated Values) formati

**CSV** — bu jadval ko'rinishidagi ma'lumotlarni oddiy matn (plain text) shaklida satrlar bo'yicha saqlovchi eng sodda va keng tarqalgan formatdir.

- Har bir satr bitta yozuvga (record) to'g'ri keladi;
- Ustunlar ajratgich (delimiter) orqali bo'linadi: odatda vergul (`,`), ba'zan nuqta-vergul (`;`) yoki tabulyatsiya (`\t`);
- Birinchi qatorda ko'pincha ustun nomlari (header) joylashadi.

```text
maktab_id,nomi,viloyat,oquvchilar_soni
101,1-IDUM,Toshkent,1250
102,5-maktab,Samarqand,890
103,12-maktab,Farg'ona,1100
```

#### Afzalliklari:
1. Juda sodda, inson tomonidan oddiy matn muharririda ham o'qilishi mumkin;
2. Har qanday tahliliy dastur (Excel, Google Sheets, Python, SQL) tomonidan oson ochiladi;
3. Boshqa tizimlar bilan ma'lumot almashish uchun universal vosita.

#### Kamchiliklari:
1. **Schema (ma'lumot turlari) saqlanmaydi:** CSV faqat matn saqlaydi, qaysi ustun butun son (integer), qaysi biri sana (date) ekani yozilmaydi;
2. **Katta hajm:** Ma'lumotlar siqilmagan holda saqlanadi, ko'p disk maydonini egallaydi;
3. **Ajratgich xatolari:** Agar matn ichida vergul kelsa (masalan `"Qodirov, Ali"`), CSV tushunmovchiligi yuzaga keladi;
4. **Encoding muammolari:** Turli operatsion tizimlarda UTF-8, Windows CP1251 yoki Latin-1 chalkashliklari matnlarni tushunarsiz belgilarga aylantirib qo'yishi mumkin.

---

### 2. JSON (JavaScript Object Notation) formati

**JSON** — bu kalit-qiymat (key-value) juftliklari va ro'yxatlar (arrays) asosida tashkil topgan, yengil va ierarxik ma'lumotlar formati.

Zamonaviy veb-saytlar, mobil ilovalar, REST API'lar va server loglarining deyarli 95% qismi ma'lumotlarni JSON ko'rinishida uzatadi.

```json
{
  "viloyat": "Toshkent",
  "maktab_id": 101,
  "faol": true,
  "direktor": {
    "ism": "Alisher",
    "familiya": "Qodirov",
    "telefon": "+998901234567"
  },
  "sinflar": [
    {"nomi": "10-A", "oquvchilar": 32},
    {"nomi": "10-B", "oquvchilar": 28}
  ]
}
```

#### Afzalliklari:
1. **Ierarxik (Nested) tuzilma:** Bir obyekt ichida boshqa obyektlar va massivlarni erkin saqlash imkoniyati;
2. **Yarim-strukturalashgan (Semi-structured):** Har bir satrda bir xil ustunlar bo'lishi shart emas, yangi maydonlarni qo'shish oson;
3. **Web va API standarti:** Barcha dasturlash tillari va zamonaviy ma'lumotlar bazalari (MongoDB, PostgreSQL JSONB) bilan mukammal integratsiyalashgan.

#### Kamchiliklari:
1. **Analitika (BI) uchun noqulay:** Power BI va SQL jadvalli (satr va ustun) tuzilmani yoqtiradi, nested JSON bilan to'g'ridan-to'g'ri ishlash qiyin;
2. **Katta ortiqcha hajm (Overhead):** Har bir obyekt uchun kalit nomi (`"viloyat"`, `"maktab_id"`) takror va takror yoziladi;
3. Tahlil qilishdan oldin `json_normalize()` orqali tekislash (flattening) talab qilinadi.

---

### 3. CSV vs JSON: Qachon qaysi biri ishlatiladi?

| Ko'rsatkich | CSV | JSON |
|---|---|---|
| **Tuzilishi** | Satrli (2D jadval) | Ierarxik (Daraxtsimon, nested) |
| **Moslashuvchanlik** | Qat'iy satr/ustun | Har bir obyekt har xil bo'lishi mumkin |
| **Qo'llanish sohasi** | Statistik hisobotlar, eksportlar, ML jadvallari | Veb API'lar, ilovalar loglari, mikroxizmatlar |
| **Hajmi** | Matnli, kichikroq | Kalit nomlari sabab kattaroq |
| **BI mosligi** | To'g'ridan-to'g'ri mos | Tekislash (normalize) talab qiladi |

---

### 4. Data Engineering Loyiha Strukturasi (Medallion arxitekturasi)

Professional Data Engineer o'z kompyuterida va serverda ma'lumotlarni quyidagi tartibda tashkil qiladi:

```text
maktab-pipeline/
├── data/
│   ├── raw/          <-- Birlamchi xom CSV va JSON fayllar (o'zgartirilmaydi)
│   ├── bronze/       <-- Minimal tekshirilgan va qabul qilingan nusxalar
│   ├── silver/       <-- Tozalangan, normalizatsiya qilingan Parquet/CSV
│   └── gold/         <-- Yakuniy hisoblangan tahliliy jadvallar (Data Marts)
├── src/              <-- Python skriptlari (extract.py, clean.py, pipeline.py)
├── logs/             <-- Barcha tekshiruvlar va xatoliklar jurnali
└── requirements.txt  <-- Kutubxonalar ro'yxati (pandas, pyarrow va h.k.)
```

---

## Amaliy mashg'ulot (Python va Pandas)

### 1. CSV faylni o'qish va Encoding muammosini hal qilish

Ko'pincha eski ma'lumotlar yoki Excel'dan olingan fayllar `cp1251` (kirill) kodlashida bo'ladi va Python `UnicodeDecodeError` beradi. Buning to'g'ri yechimi:

```python
import pandas as pd
from pathlib import Path

fayl_yoli = Path("data/raw/maktablar.csv")

try:
    # Standart UTF-8 da o'qishga urinib ko'ramiz
    df = pd.read_csv(fayl_yoli, encoding="utf-8")
    print("Fayl UTF-8 formatida muvaffaqiyatli o'qildi.")
except UnicodeDecodeError:
    # Agar xatolik bersa, Windows CP1251 da o'qiymiz
    df = pd.read_csv(fayl_yoli, encoding="cp1251")
    print("Fayl CP1251 formatida o'qildi.")

# Birlamchi profiling (tahlil)
print("\n--- Fayl shakli (qatorlar, ustunlar) ---")
print(df.shape)

print("\n--- Dastlabki 3 ta satr ---")
print(df.head(3))

print("\n--- Ma'lumot turlari va bo'sh kataklar ---")
print(df.info())
```

---

### 2. JSON faylni o'qish va `json_normalize` bilan tekislash

Nested (ichma-ich) tuzilgan JSON faylni tahlil qilish uchun uni tekis jadvalga aylantiramiz:

```python
import json
import pandas as pd

# 1. Nested JSON ma'lumotlar namunasi
maktab_json = [
    {
        "id": 101,
        "maktab": "1-IDUM",
        "joylashuv": {"viloyat": "Toshkent", "tuman": "Chilonzor"},
        "sinflar": [
            {"nomi": "10-A", "oquvchilar": 30},
            {"nomi": "10-B", "oquvchilar": 28}
        ]
    },
    {
        "id": 102,
        "maktab": "24-maktab",
        "joylashuv": {"viloyat": "Samarqand", "tuman": "Pastdarg'om"},
        "sinflar": [
            {"nomi": "10-A", "oquvchilar": 35}
        ]
    }
]

# 2. json_normalize orqali tekislash
df_maktablar = pd.json_normalize(
    maktab_json,
    record_path=["sinflar"],
    meta=["id", "maktab", ["joylashuv", "viloyat"], ["joylashuv", "tuman"]],
    meta_prefix=""
)

print("--- Tekislangan (Flattened) DataFrame ---")
print(df_maktablar)
```

Natija jadval ko'rinishida hosil bo'ladi:
```text
  nomi  oquvchilar   id      maktab joylashuv.viloyat joylashuv.tuman
0 10-A          30  101      1-IDUM          Toshkent        Chilonzor
1 10-B          28  101      1-IDUM          Toshkent        Chilonzor
2 10-A          35  102   24-maktab         Samarqand      Pastdarg'om
```

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq: Delimiter muammosini aniqlash
Quyidagi CSV satrini tahlil qiling:  
`101;"Alisher Navoiy nomidagi 1-maktab, Toshkent";1250;2024`  
Ushbu satrda qaysi belgi ajratgich (delimiter) vazifasini bajarmoqda va standart `pd.read_csv('fayl.csv')` chaqirilsa nima yuz beradi?

**Yechim:**  
Ushbu satrda ajratgich sifatida nuqta-vergul (`;`) ishlatilgan. Agar `sep=';'` ko'rsatilmasa, standart `read_csv()` vergul (`,`) qidiradi va butun satrni bitta ustun deb hisoblaydi yoki matn ichidagi vergul sababli ustunlar siljishiga olib keladi. To'g'ri o'qish: `pd.read_csv('fayl.csv', sep=';')`.

---

### 2-topshiriq: JSON dan jadvalga aylantirish
Quyidagi JSON obyektini oddiy 2D jadval ustunlariga ajrating:
```json
{
  "ism": "Jasur",
  "baho": 85,
  "kontakt": {
    "shahar": "Buxoro",
    "email": "jasur@mail.uz"
  }
}
```

**Yechim:**  
`pd.json_normalize()` qo'llanganda quyidagi ustunli jadval hosil bo'ladi:
- `ism`: "Jasur"
- `baho`: 85
- `kontakt.shahar`: "Buxoro"
- `kontakt.email`: "jasur@mail.uz"

---

### 3-topshiriq: Medallion papka qoidalarini qo'llash
Kompaniya ma'lumotlar quvuri doirasida quyidagi 3 ta fayl qaysi papkaga (`data/raw/`, `data/silver/` yoki `data/gold/`) joylashtirilishi kerak?
1. API dan hozirgina yuklab olingan xom `transactions_2024_09.json` fayli;
2. Barcha duplikatlari o'chirilgan va sanalari yagona formatga keltirilgan `customers_clean.parquet` fayli;
3. Bosh direktor uchun tayyorlangan oylik sotuvlar yakuni va hududlar reytingi `monthly_revenue_kpi.csv` fayli.

**Yechim:**  
1. `data/raw/` (xom, tegilmagan ma'lumotlar zonasi);  
2. `data/silver/` (tozalangan, standartlashtirilgan ma'lumotlar zonasi);  
3. `data/gold/` (yakuniy biznes hisobotlari va KPI ko'rsatkichlari zonasi).

---

## Tezkor savol-javob (Quick Check)

1. **Savol:** Nima uchun CSV fayllarda ma'lumot turlari (Data Types) saqlanmaydi?  
   **Javob:** Chunki CSV oddiy matn fayli (plain text) bo'lib, unda faqat simvollar va ajratgichlar yoziladi, ma'lumotlar turini ifodalovchi meta-axborot (metadata) mavjud emas.

2. **Savol:** API'lar nima sababdan ma'lumot uzatishda CSV dan ko'ra JSON formatini afzal ko'radi?  
   **Javob:** Chunki JSON ichma-ich (nested) ierarxik obyektlarni, ro'yxatlarni va ixtiyoriy maydonlarni moslashuvchan ifodalay oladi.

3. **Savol:** Python'da `UnicodeDecodeError` paydo bo'lganda qanday chora ko'riladi?  
   **Javob:** Faylning kodlash turi tekshiriladi va `pd.read_csv()` funksiyasida `encoding='cp1251'` yoki `encoding='latin1'` parametri belgilanadi.

4. **Savol:** `json_normalize()` funksiyasining asosiy vazifasi nima?  
   **Javob:** Ichma-ich joylashgan daraxtsimon JSON obyektlarini munosabatli jadval (satr va ustunlar) shakliga tekislash.
