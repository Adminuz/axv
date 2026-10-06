# 18-dars: Data Lake konsepsiyasi, Bronze / Silver / Gold zonalari

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 6-hafta, 3-dars (umumiy 18-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

Data Lake nima ekanini va DWH dan farqini, Bronze, Silver, Gold qatlamlarining vazifasini, qatlamdan qatlamga o'tishda nima o'zgarishini tushuntirish va `pandas` bilan kichik raw → bronze → silver → gold oqimini bajarish. Manba: `oquv-dasturi.txt` (Data Lake tushunchasi, xususiyatlari, Bronze/Silver/Gold qatlamlari, DWH vs Data Lake, Lakehouse); `uslubiy-korsatma.txt` (`maktab-pipeline`: `data/raw`, `bronze`, `silver`, `gold`). Kod `pandas` bilan CSV formatda yozilgan va tekshirilgan; uslubiy ko'rsatmadagi Parquet (`pyarrow` kerak) bu yerda tekshirilmagan. Raqamlar xayoliy.

---

## Kutilayotgan natijalar

- Data Lake ni ta'riflaydi va 3 ta xususiyatini aytadi;
- Bronze, Silver, Gold qatlamlari vazifasini farqlaydi;
- DWH va Data Lake farqini jadval bilan tushuntiradi;
- Lakehouse g'oyasini qisqa aytadi;
- `pandas` bilan raw dan gold gacha oqim yozadi.

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`);
- `data/maktab.db` (3–4-haftalardagi jadvallar: `hududlar`, `maktablar`, `yillik_kpi`).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | 17-dars: DWH, qatlamlar, ETL |
| **10–28** | Data Lake | Data Lake: nima va nega |
| **28–40** | Bronze, Silver, Gold | Bronze, Silver, Gold qatlamlari |
| **40–45** | Tanaffus | |
| **45–58** | DWH va Lake, Lakehouse | DWH va Data Lake farqi, Lakehouse |
| **58–75** | Amaliyot | `maktab-pipeline` papkalari va kichik oqim |
| **75–80** | Xulosa | Tezkor nazorat, hafta yakuni, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. Data Lake tushunchasi

**Data Lake** — ma'lumotni asl, xom holatida, har qanday formatda (CSV, JSON, rasm, log) arzon saqlash joyi. Asosiy g'oya: **schema-on-read** — tuzilmani saqlashda emas, o'qishda belgilaymiz, shuning uchun hozir kerak bo'lmagan ma'lumotni ham yo'qotmaymiz. Xususiyatlari: har xil format, katta hajm, past narx, moslashuvchanlik. Xavfi: tartibsiz bo'lsa, «ma'lumot botqog'i» (data swamp) ga aylanadi. Shuning uchun lake qatlamlarga bo'linadi.

```text
maktab-pipeline/
  data/
    raw/      # asl fayllar, o'zgartirilmaydi
    bronze/   # minimal ishlov
    silver/   # tozalangan
    gold/     # biznes uchun tayyor
  src/
  logs/
```

Raw qatlamdagi fayllarni hech qachon tahrirlamang: xato bo'lsa, qayta ishlash uchun asl nusxa kerak.

### 2. Bronze, Silver va Gold qatlamlari

Lake ichidagi tartib: **Bronze** — manbadan kelgan ma'lumot minimal ishlov bilan (formatga keltirilgan, hech narsa tashlanmagan). **Silver** — tozalangan va tekshirilgan: dublikatlar olib tashlangan, bo'sh qiymatlar boshqarilgan, turlar to'g'rilangan. **Gold** — biznes uchun tayyor: jamlangan ko'rsatkichlar, hisobot va ML uchun jadvallar. Qatlamdan qatlamga o'tgan sari ma'lumot sifati oshadi, hajmi odatda kamayadi. Yuqorigi qatlamlarni pastdan qayta tiklash mumkin.

```python
bronze = pd.read_csv("data/raw/maktab.csv", dtype=str)

silver = bronze.drop_duplicates().dropna().copy()
silver["oquvchilar"] = silver["oquvchilar"].astype(int)

gold = silver.groupby("yil", as_index=False)["oquvchilar"].sum()
```

Tozalash qoidasini (`dropna`, `drop_duplicates`) hujjatlang: Silver da nima tashlab yuborilganini keyin tushuntira olishingiz kerak.

### 3. DWH va Data Lake farqi, Lakehouse

DWH — tuzilmali, tozalangan, tez SQL tahlil uchun (schema-on-write). Lake — xom, har xil, moslashuvchan, arzon (schema-on-read). Real tashkilotlarda ikkalasi birga ishlaydi: lake — xom ma'lumot va ML uchun, DWH — hisobot va BI uchun. **Lakehouse** — ikkalasini birlashtirish: lake ning arzon saqlashi va DWH ning tuzilma va SQL imkoniyatlari bitta tizimda. E-commerce misoli: buyurtma loglari va rasmlar lake ga, tozalangan sotuvlar fakti DWH ga tushadi.

```python
gold.to_csv("data/gold/oquvchilar_yillik.csv", index=False)
print(gold.to_string(index=False))
#  yil  oquvchilar
# 2024      932000
```

Real loyihada Gold va Silver ko'pincha Parquet formatda saqlanadi; bu yerda soddalik uchun CSV ishlatildi.

### Odatiy xatolar

1. Raw fayllarni tahrirlash.
2. Tozalash qoidalarini hujjatlamaslik.
3. Barcha ma'lumotni Gold ga bevosita yozish.
4. Lake ni tartibsiz qoldirish (data swamp).
5. DWH o'rniga faqat Lake ni ishlatish va hisobotni xomdan olish.
6. Qatlam nomlarini aralashtirish.

---

## Kod namunalari

### 1-namuna: Raw → Bronze → Silver → Gold (pandas, CSV)

```python
import os
import pandas as pd

for d in ("raw", "bronze", "silver", "gold"):
    os.makedirs(f"data/{d}", exist_ok=True)

pd.DataFrame({
    "hudud": ["Samarqand", "Buxoro", "Buxoro", "Toshkent"],
    "yil": [2024] * 4,
    "oquvchilar": ["620000", "312000", "312000", None],
}).to_csv("data/raw/maktab.csv", index=False)

bronze = pd.read_csv("data/raw/maktab.csv", dtype=str)
bronze.to_csv("data/bronze/maktab.csv", index=False)

silver = bronze.drop_duplicates().dropna().copy()
silver["oquvchilar"] = silver["oquvchilar"].astype(int)
silver["yil"] = silver["yil"].astype(int)
silver.to_csv("data/silver/maktab.csv", index=False)

gold = silver.groupby("yil", as_index=False)["oquvchilar"].sum()
gold.to_csv("data/gold/oquvchilar_yillik.csv", index=False)
print(len(bronze), len(silver))   # 4 2
print(gold.to_string(index=False))
#  yil  oquvchilar
# 2024      932000
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): Qatlamni toping
Quyidagi har amal qaysi qatlamda bajariladi: dublikatlarni olib tashlash; yillik jami hisoblash; asl faylni saqlash?

**Kutiladigan natija:** Silver, Gold, Raw.  
**Yechim:**
```python
Dublikat — Silver; yillik jami — Gold; asl fayl — Raw.
```

### 2-topshiriq (oson): Lake yoki DWH
«Ijtimoiy tarmoqdagi rasmlar va loglar» va «yillik KPI hisoboti» qayerda saqlanadi?

**Kutiladigan natija:** Lake va DWH.  
**Yechim:**
```python
Rasm va loglar — Lake; KPI hisoboti — DWH.
```

### 3-topshiriq (o'rta): Papkalar
`maktab-pipeline` papkalarini yarating va vazifasini yozing.

**Kutiladigan natija:** 4 ta data papka.  
**Yechim:**
```python
raw: asl; bronze: minimal; silver: toza; gold: biznes.
```

### 4-topshiriq (o'rta): Silver yozing
Bronze dagi dublikat va bo'sh qatorlarni olib tashlab, `oquvchilar` ni `int` qiling.

**Kutiladigan natija:** 4 qatordan 2 qator qoladi.  
**Yechim:**
```python
silver = bronze.drop_duplicates().dropna().copy()
silver["oquvchilar"] = silver["oquvchilar"].astype(int)
```

### 5-topshiriq (qiyin): Gold yozing
Silver dan yillik jami o'quvchilarni hisoblang.

**Kutiladigan natija:** 2024 — 932000.  
**Yechim:**
```python
gold = silver.groupby("yil", as_index=False)["oquvchilar"].sum()
```

### 6-topshiriq (bonus): Lakehouse
Lakehouse nima va kim uchun foydali? 2 jumlada yozing.

**Kutiladigan natija:** Lake va DWH birligi.  
**Yechim:**
```python
Lakehouse arzon lake saqlashini DWH ning SQL imkoniyatlari bilan birlashtiradi.
```

---

## Tezkor nazorat savollari

1. Data Lake nima?  
   *Javob:* Ma'lumotni xom, har xil formatda arzon saqlash joyi.
2. Bronze, Silver, Gold vazifasi?  
   *Javob:* Minimal ishlov, tozalash, biznes uchun tayyor.
3. Schema-on-read nima?  
   *Javob:* Tuzilmani saqlashda emas, o'qishda belgilash.
4. DWH va Lake asosiy farqi?  
   *Javob:* DWH tuzilmali, Lake xom va moslashuvchan.
5. Lakehouse nima?  
   *Javob:* Lake va DWH imkoniyatlarining birligi.

---

## Hafta yakuni va keyingi haftaga ko'prik

6-haftada SCD, DWH va Data Lake o'rganildi. 7-haftada keyingi mavzu (kartaga qarang).

---

## Uyga vazifa

`uyga-vazifa.md` ning 3-topshirig'i: raw dan gold gacha oqimni yozish (20–30 daqiqa).
