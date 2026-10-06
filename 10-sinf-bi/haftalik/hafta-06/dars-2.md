# 17-dars: Ma'lumotlar ombori: Data Warehouse (DWH) tushunchasi, arxitekturasi va afzalliklari

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 6-hafta, 2-dars (umumiy 17-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

DWH ning ta'rifini va nima uchun kerakligini (turli manbalardan ma'lumotni birlashtirish, BI uchun moslashtirish), OLTP va OLAP farqini, DWH qatlamlarini (manba, staging, ombor, martlar, BI), afzalliklarini va mashhur DWH texnologiyalarini tushuntirish; kichik DWH ni `sqlite3` da yig'ish. Manba: `oquv-dasturi.txt` (DWH ta'rifi: turli manbalardan kelgan ma'lumotlarni birlashtiruvchi, BI uchun moslashtirilgan maxsus baza; DWH tushunchasi, afzalliklari, mashhur DW texnologiyalari va arxitekturasi). Texnologiyalar ro'yxati va qatlamlar sxemasi standart bilimdan qo'shildi.

---

## Kutilayotgan natijalar

- DWH ni ta'riflaydi va 4 ta xususiyatini aytadi;
- OLTP va OLAP farqini jadval bilan tushuntiradi;
- DWH arxitekturasi qatlamlarini ketma-ket aytadi;
- DWH afzalliklarini misol bilan asoslaydi;
- Ikki manbani staging orqali bitta ombor jadvaliga birlashtiradi.

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`);
- `data/maktab.db` (3–4-haftalardagi jadvallar: `hududlar`, `maktablar`, `yillik_kpi`).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | 16-dars: SCD, surrogate kalit |
| **10–28** | DWH tushunchasi | DWH nima, OLTP va OLAP |
| **28–40** | Arxitektura | Arxitektura: manba, staging, ombor, mart, BI |
| **40–45** | Tanaffus | |
| **45–58** | Afzalliklar va texnologiyalar | Afzalliklar va mashhur texnologiyalar |
| **58–75** | Amaliyot | Ikki manbani birlashtirib kichik DWH yig'ish |
| **75–80** | Xulosa | Tezkor nazorat, hafta yakuni, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. Data Warehouse tushunchasi

**Data Warehouse (DWH)** — turli manbalardan kelgan katta hajmli ma'lumotni birlashtiruvchi, BI jarayonlari uchun moslashtirilgan maxsus ma'lumotlar bazasi. Uning xususiyatlari: **mavzuga yo'naltirilgan** (o'quvchilar, moliya kabi mavzular), **integratsiyalangan** (turli manbalar bir formatga keltiriladi), **tarixiy** (o'zgarishlar tarixi saqlanadi, SCD), **barqaror** (ma'lumot asosan qo'shiladi, o'chirilmaydi). Maqsad — butun tashkilot uchun «yagona haqiqat manbai»: bir savolga hamma bir xil javob oladi.

```text
OLTP (kundalik ish)          OLAP / DWH (tahlil)
- bitta qatorni o'zgartirish  - ko'p qatorni o'qish, jamlash
- tez, qisqa tranzaksiyalar   - murakkab so'rovlar
- joriy holat                 - tarix
- normallashgan jadvallar     - star schema (fakt + dimension)
```

DWH operatsion bazani almashtirmaydi: u undan nusxa oladi va tahlil uchun qayta tashkil qiladi.

### 2. DWH arxitekturasi

Oddiy DWH oqimi: **manbalar** (operatsion baza, CSV, API) → **ETL** (Extract, Transform, Load) → **staging** (xom nusxa, vaqtinchalik) → **DWH** (tozalangan, star schema) → **data martlar** (soha bo'yicha) → **BI** (hisobot, dashboard). Staging manbaga yuklamani kamaytiradi va xatoni tekshirishga imkon beradi. DWH ichida fakt va dimension jadvallar (13–16-darslar) joylashadi. Martlar esa soha foydalanuvchisi uchun qulay ko'rinishdir (15-dars).

```text
Manbalar:  qabul.csv, moliya.xlsx, kadrlar_baza
   |  ETL (Extract -> Transform -> Load)
Staging:   stg_qabul, stg_moliya      (xom nusxa)
   |
DWH:       dim_hudud, dim_maktab, fact_kpi
   |
Martlar:   mart_oquvchilar, mart_moliya
   |
BI:        hisobot, dashboard
```

Staging jadvalini hisobotda ishlatmang: u xom va tozalanmagan. Hisobot faqat DWH yoki martdan o'qiydi.

### 3. Afzalliklar va mashhur DWH texnologiyalari

Afzalliklari: ma'lumot **bir joyda** va izchil; **tarix** saqlanadi; tahlil so'rovlari operatsion bazani sekinlashtirmaydi; ma'lumot sifati nazorat qilinadi; BI vositalari tayyor star schema bilan tez ishlaydi. Mashhur DWH texnologiyalari: bulutda — **Snowflake**, **Google BigQuery**, **Amazon Redshift**, **Azure Synapse**; an'anaviy — **PostgreSQL**, **SQL Server**, **Oracle** asosidagi omborlar. Tanlash ma'lumot hajmi, byudjet va bulut provayderiga bog'liq.

```sql
-- Ikki manbadagi ma'lumotni DWH ga birlashtirish
INSERT INTO dw_oquvchilar (hudud, yil, oquvchilar)
SELECT hudud, yil, oquvchilar FROM stg_qabul
UNION ALL
SELECT hudud, yil, oquvchilar FROM stg_arxiv;
```

Birlashtirishdan oldin ustun nomlari va turlarini bir xil qiling: bu ETL ning Transform bosqichi.

### Odatiy xatolar

1. DWH ni operatsion bazaning oddiy nusxasi deb hisoblash.
2. Hisobotni staging dan olish.
3. Ustun nomlari va turlarini bir xil qilmasdan birlashtirish.
4. Tarixni saqlamaslik (SCD yo'q).
5. Barcha manbani bir kunda ulashga urinish.
6. Ma'lumot sifatini tekshirmaslik.

---

## Kod namunalari

### 1-namuna: Kichik DWH (Python)

```python
import sqlite3
c = sqlite3.connect(":memory:")
c.executescript('''
CREATE TABLE stg_qabul (hudud TEXT, yil INT, oquvchilar INT);
CREATE TABLE stg_arxiv (hudud TEXT, yil INT, oquvchilar INT);
CREATE TABLE dw_oquvchilar (hudud TEXT, yil INT, oquvchilar INT);
INSERT INTO stg_qabul VALUES ('Samarqand', 2024, 620000), ('Buxoro', 2024, 312000);
INSERT INTO stg_arxiv VALUES ('Toshkent', 2024, 312000);
INSERT INTO dw_oquvchilar
SELECT hudud, yil, oquvchilar FROM stg_qabul
UNION ALL
SELECT hudud, yil, oquvchilar FROM stg_arxiv;
''')
print(c.execute("SELECT SUM(oquvchilar) FROM dw_oquvchilar WHERE yil = 2024").fetchone())
# (1244000,)
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): DWH ta'rifi
DWH ni 2 jumlada ta'riflang va 4 xususiyatini sanang.

**Kutiladigan natija:** Ta'rif va 4 xususiyat.  
**Yechim:**
```text
DWH — turli manbalarni birlashtiruvchi tahlil ombori. Xususiyat: mavzuga yo'naltirilgan, integratsiyalangan, tarixiy, barqaror.
```

### 2-topshiriq (oson): OLTP yoki OLAP
«Bitta o'quvchini ro'yxatdan o'tkazish» va «3 yillik hudud kesimidagi hisobot» qaysi turga kiradi?

**Kutiladigan natija:** OLTP va OLAP.  
**Yechim:**
```text
Ro'yxatdan o'tkazish — OLTP; 3 yillik hisobot — OLAP.
```

### 3-topshiriq (o'rta): Qatlamlar
Maktab ma'lumoti uchun DWH oqimini 5 qatlamda yozing.

**Kutiladigan natija:** Manba → staging → DWH → mart → BI.  
**Yechim:**
```text
Manbalar → ETL → stg_* → dim_/fact_* → mart_* → BI.
```

### 4-topshiriq (o'rta): Staging
Nima uchun manbadan to'g'ridan-to'g'ri DWH ga yuklamay, staging ishlatiladi?

**Kutiladigan natija:** Ikkita sabab.  
**Yechim:**
```text
Manbaga yuklama kamayadi; xomni tekshirib, keyin tozalash mumkin.
```

### 5-topshiriq (qiyin): Ikki manba
`stg_qabul` va `stg_arxiv` ni `dw_oquvchilar` ga birlashtiring va 2024-yil jamini chiqaring.

**Kutiladigan natija:** 2024: 1 244 000.  
**Yechim:**
```text
INSERT INTO dw_oquvchilar SELECT hudud, yil, oquvchilar FROM stg_qabul UNION ALL SELECT hudud, yil, oquvchilar FROM stg_arxiv;
SELECT SUM(oquvchilar) FROM dw_oquvchilar WHERE yil = 2024;
```

### 6-topshiriq (bonus): Texnologiya tanlash
Kichik tuman ta'lim bo'limi uchun DWH texnologiyasini tanlang va sababini yozing.

**Kutiladigan natija:** Asosli tanlov.  
**Yechim:**
```text
Kichik hajmda PostgreSQL yetadi; bulut kerak bo'lsa BigQuery.
```

---

## Tezkor nazorat savollari

1. DWH nima?  
   *Javob:* Turli manbalardan ma'lumotni birlashtiruvchi, BI uchun moslangan ombor.
2. OLTP va OLAP farqi?  
   *Javob:* OLTP kundalik tranzaksiyalar uchun, OLAP tahlil uchun.
3. Staging nima?  
   *Javob:* Xom vaqtinchalik nusxa qatlami.
4. ETL bosqichlari?  
   *Javob:* Extract, Transform, Load.
5. DWH ning bitta afzalligi?  
   *Javob:* Ma'lumot bir joyda va izchil; tarix saqlanadi.

---

## Hafta yakuni va keyingi haftaga ko'prik

6-haftada: SCD (16), DWH (17), Data Lake (18). 7-haftada keyingi mavzu (kartaga qarang).

---

## Uyga vazifa

`uyga-vazifa.md` ning 2-topshirig'i: kichik DWH ni qurish va qatlamlar sxemasini chizish (20–30 daqiqa).
