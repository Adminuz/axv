# 16-dars: Sekin o'zgaruvchi o'lchamlar (SCD Type 1, Type 2) va surrogat kalitlar

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 6-hafta, 1-dars (umumiy 16-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

Dimension jadvallardagi atribut vaqt o'tishi bilan o'zgarishini (Slowly Changing Dimensions), Type 1 (ustiga yozish) va Type 2 (yangi qator, tarix saqlanadi) usullarining farqini, surrogate kalit nima uchun kerakligini tushuntirish va `sqlite3` da ikkala usulni amalda bajarish. Manba: `oquv-dasturi.txt` (Slowly Changing Dimensions va turlari, Surrogate Keys). Dasturda faqat mavzu nomlari bor: misollar (`dim_maktab`, direktor o'zgarishi) o'quv maqsadida yozilgan va `sqlite3` da tekshirilgan, raqamlar xayoliy.

---

## Kutilayotgan natijalar

- SCD nima ekanini va nima uchun kerakligini aytadi;
- Type 1 va Type 2 ni farqlaydi va biznes savoliga qarab tanlaydi;
- Type 2 jadvalini `boshlandi`, `tugadi`, `joriy` ustunlari bilan loyihalaydi;
- Surrogate va natural kalit farqini tushuntiradi;
- Type 2 yangilanishini `UPDATE` + `INSERT` bilan bajaradi va JOIN orqali tarixni tekshiradi.

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`);
- `data/maktab.db` (3–4-haftalardagi jadvallar: `hududlar`, `maktablar`, `yillik_kpi`).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | 15-dars: Data Mart, VIEW |
| **10–28** | SCD turlari | SCD nima, Type 1 va Type 2 |
| **28–40** | Type 2 amalda | Type 2 jadvali va yangilash |
| **40–45** | Tanaffus | |
| **45–58** | Surrogate kalit | Surrogate va natural kalit, qaysi tur qachon |
| **58–75** | Amaliyot | `dim_maktab` da ikkala usulni sinash |
| **75–80** | Xulosa | Tezkor nazorat, hafta yakuni, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. Slowly Changing Dimensions: Type 1 va Type 2

Dimension atributlari vaqt o'tishi bilan sekin o'zgaradi: maktabning direktori almashadi, hududning markazi ko'chadi. **SCD** (Slowly Changing Dimensions) — shu o'zgarishlarni dimension da qanday saqlash usullari. **Type 1** — eski qiymat ustiga yangisi yoziladi, tarix yo'qoladi; oddiy, xato tuzatish uchun mos. **Type 2** — eski qator «yopiladi» (`tugadi`, `joriy = 0`), yangi qiymat bilan yangi qator qo'shiladi; tarix saqlanadi. Tanlov biznes savoliga bog'liq: «2023-yilda direktor kim edi?» degan savol bo'lsa, Type 2 kerak.

```sql
UPDATE dim_maktab
SET direktor = 'B. Aliyev'
WHERE maktab_id = 101;
-- Natija: faqat 'B. Aliyev'. 'A. Karimov' yo'q bo'ldi.
```

Type 1 ni yozuv xatosini tuzatishda ishlating. Tarix kerak bo'lsa, Type 1 xavfli: eski hisobotlar jimgina o'zgaradi.

### 2. Type 2 jadvali va yangilash

Type 2 jadvalida har versiya alohida qator: `boshlandi` va `tugadi` sanalari, `joriy` bayrog'i (1 — hozirgi qator). Joriy qator uchun `tugadi = '9999-12-31'`. O'zgarish bo'lganda ikki qadam: 1) joriy qatorni yoping (`tugadi = yangi sana`, `joriy = 0`); 2) yangi qiymat bilan yangi qator qo'shing. Yangi qator yangi **surrogate kalit** oladi, natural kalit (`maktab_id`) esa bir xil qoladi. Fakt jadval o'sha paytda amal qilgan qatorning surrogate kaliti bilan bog'lanadi, shuning uchun eski yil hisobotida eski direktor ko'rinadi.

```sql
UPDATE dim_maktab
SET tugadi = '2024-09-01', joriy = 0
WHERE maktab_id = 101 AND joriy = 1;

INSERT INTO dim_maktab (maktab_id, nomi, direktor, boshlandi, tugadi, joriy)
VALUES (101, '5-maktab', 'B. Aliyev', '2024-09-01', '9999-12-31', 1);
```

Ikki amalni bitta tranzaksiyada bajaring: yarim bajarilsa, jadvalda ikkita joriy qator yoki bitta ham joriy qator qolmaydi.

### 3. Surrogate va natural kalit

**Natural kalit** — manba tizimdagi identifikator (`maktab_id`). **Surrogate kalit** — omborning o'zi beradigan sun'iy butun son (`maktab_key`), ma'nosi yo'q. Type 2 da bir maktab bir nechta qatorda turadi, natural kalit takrorlanadi va birlamchi kalit bo'la olmaydi; surrogate kalit har versiyani aniq ajratadi. Boshqa afzalliklari: manba kalitlari o'zgarsa yoki turli manbalarda to'qnashsa ombor buzilmaydi; butun son bo'lgani uchun JOIN tez. Fakt jadval faqat surrogate kalitga tayanadi.

```sql
SELECT m.direktor, f.yil, f.oquvchilar
FROM fakt f
JOIN dim_maktab m ON m.maktab_key = f.maktab_key
ORDER BY f.yil;
-- A. Karimov | 2023 | 640
-- B. Aliyev  | 2024 | 655
```

Joriy holatni olish uchun `WHERE joriy = 1` yozing, aks holda bir maktab bir necha marta chiqadi.

### Odatiy xatolar

1. Tarix kerak joyda Type 1 ishlatish.
2. Type 2 da joriy qatorni yopishni unutish (ikkita joriy qator).
3. Natural kalitni birlamchi kalit qilish.
4. `WHERE joriy = 1` ni yozmaslik (qatorlar takrorlanadi).
5. Faktni natural kalitga bog'lash.
6. UPDATE va INSERT ni alohida tranzaksiyalarda bajarish.

---

## Kod namunalari

### 1-namuna: Type 2 ni Python da bajarish

```python
import sqlite3
c = sqlite3.connect(":memory:")
c.executescript('''
CREATE TABLE dim_maktab (
    maktab_key INTEGER PRIMARY KEY AUTOINCREMENT,
    maktab_id INTEGER, nomi TEXT, direktor TEXT,
    boshlandi TEXT, tugadi TEXT, joriy INTEGER);
INSERT INTO dim_maktab (maktab_id, nomi, direktor, boshlandi, tugadi, joriy)
VALUES (101, '5-maktab', 'A. Karimov', '2022-09-01', '9999-12-31', 1);
''')

def scd2(maktab_id, yangi, sana):
    c.execute("UPDATE dim_maktab SET tugadi=?, joriy=0 WHERE maktab_id=? AND joriy=1",
              (sana, maktab_id))
    c.execute("INSERT INTO dim_maktab (maktab_id, nomi, direktor, boshlandi, tugadi, joriy) "
              "SELECT maktab_id, nomi, ?, ?, '9999-12-31', 1 FROM dim_maktab "
              "WHERE maktab_id=? AND tugadi=?", (yangi, sana, maktab_id, sana))

scd2(101, 'B. Aliyev', '2024-09-01')
for r in c.execute("SELECT * FROM dim_maktab ORDER BY maktab_key"):
    print(r)
# (1, 101, '5-maktab', 'A. Karimov', '2022-09-01', '2024-09-01', 0)
# (2, 101, '5-maktab', 'B. Aliyev', '2024-09-01', '9999-12-31', 1)
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): SCD turini tanlang
Qaysi holatda Type 1, qaysida Type 2: familiyadagi imlo xatosi; direktor almashishi?

**Kutiladigan natija:** Imlo xatosi: Type 1; direktor: Type 2.  
**Yechim:**
```sql
Imlo xatosi — Type 1 (tarix kerak emas); direktor — Type 2 (tarix kerak).
```

### 2-topshiriq (oson): Jadvalni yarating
Type 2 uchun `dim_maktab` ni yarating.

**Kutiladigan natija:** Jadval 7 ustunli.  
**Yechim:**
```sql
CREATE TABLE dim_maktab (
    maktab_key INTEGER PRIMARY KEY AUTOINCREMENT,
    maktab_id INTEGER, nomi TEXT, direktor TEXT,
    boshlandi TEXT, tugadi TEXT, joriy INTEGER
);
```

### 3-topshiriq (o'rta): Type 1
101-maktab direktorini Type 1 bilan `B. Aliyev` ga o'zgartiring.

**Kutiladigan natija:** 1 qator yangilandi, tarix yo'q.  
**Yechim:**
```sql
UPDATE dim_maktab SET direktor = 'B. Aliyev' WHERE maktab_id = 101;
```

### 4-topshiriq (o'rta): Type 2
Direktorni Type 2 bilan `2024-09-01` sanasida almashtiring.

**Kutiladigan natija:** 2 qator: eskisi yopilgan, yangisi joriy.  
**Yechim:**
```sql
UPDATE dim_maktab SET tugadi = '2024-09-01', joriy = 0
WHERE maktab_id = 101 AND joriy = 1;
INSERT INTO dim_maktab (maktab_id, nomi, direktor, boshlandi, tugadi, joriy)
VALUES (101, '5-maktab', 'B. Aliyev', '2024-09-01', '9999-12-31', 1);
```

### 5-topshiriq (qiyin): Tarixni JOIN qiling
`fakt` bilan JOIN qilib har yil direktorini chiqaring.

**Kutiladigan natija:** 2023 — A. Karimov, 2024 — B. Aliyev.  
**Yechim:**
```sql
SELECT m.direktor, f.yil, f.oquvchilar
FROM fakt f JOIN dim_maktab m ON m.maktab_key = f.maktab_key
ORDER BY f.yil;
```

### 6-topshiriq (bonus): Joriy qatorlar
Faqat joriy direktorlar ro'yxatini chiqaring.

**Kutiladigan natija:** Faqat `joriy = 1` qatorlar.  
**Yechim:**
```sql
SELECT maktab_id, nomi, direktor FROM dim_maktab WHERE joriy = 1;
```

---

## Tezkor nazorat savollari

1. SCD nima?  
   *Javob:* Dimension atributlarining sekin o'zgarishini boshqarish usullari.
2. Type 1 va Type 2 farqi?  
   *Javob:* Type 1 ustiga yozadi, Type 2 yangi qator qo'shib tarixni saqlaydi.
3. Type 2 ustunlari?  
   *Javob:* `boshlandi`, `tugadi`, `joriy`.
4. Surrogate kalit nima?  
   *Javob:* Omborning o'zi beradigan sun'iy butun kalit.
5. Joriy qatorni qanday olamiz?  
   *Javob:* `WHERE joriy = 1`.

---

## Hafta yakuni va keyingi haftaga ko'prik

6-haftada: SCD va surrogate kalitlar (16), Data Warehouse (17), Data Lake va Bronze/Silver/Gold (18). 7-haftada keyingi mavzu (kartaga qarang).

---

## Uyga vazifa

`uyga-vazifa.md` ning 1-topshirig'i: Type 1 va Type 2 ni `dim_maktab` da sinash (20–30 daqiqa).
