# 8-dars: R-diagrammalar (ERD) loyihalash va SQLite bilan ishlash

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta, 2-dars (umumiy 8-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga axborot tizimlari va ma'lumotlar ombori arxitekturasining poydevori hisoblangan **Entity-Relationship Model (ER-model / ERD)** loyihalash metodologiyasini o'rgatish; Obyekt (Entity), Atribut (Attribute) va Munosabat (Relationship) tushunchalarini chuqur tahlil qilish; munosabatlar kardinalligi (**Cardinality: 1:1, 1:N, M:N**) va Ko'pga-ko'p (M:N) munosabatlarni bog'lovchi oraliq jadval (**Junction / Bridge table**) yordamida ikkita 1:N ga ajratish tamoyillarini ko'rsatish; rasmiy o'quv dasturidagi **"Maktab tahliliy platformasi"** loyihasining relyatsion arxitekturasini (`hududlar`, `maktablar`, `yillik_kpi`) noldan loyihalash hamda Python `sqlite3` moduli yordamida to'liq ishchi ma'lumotlar bazasini (`maktab.db`) barpo etish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- ERD (Entity-Relationship Diagram) nima ekanligi va nima uchun kod yozishdan oldin baza arxitekturasini chizish shartligini tushunish;
- Chen notatsiyasi va Crow's Foot (qarg'a oyog'i) notatsiyalari belgilarini farqlay olish;
- Munosabatlar kardinalligi (1:1, 1:N va M:N) ni real ta'lim va biznes ssenariylarida to'g'ri aniqlay olish;
- M:N (ko'pga-ko'p) munosabat relyatsion bazada to'g'ridan-to'g'ri mavjud bo'lolmasligini va unga Junction (oraliq) jadval kerakligini bilish;
- "Maktab tahliliy platformasi" ning ERD modelini mustaqil chiza olish: `hududlar (1) ── (N) maktablar` va `maktablar (1) ── (N) yillik_statistika`;
- Python'dagi `sqlite3` yordamida ushbu arxitekturani amalga oshiruvchi DDL SQL skriptlarini yoza olish;
- DBeaver yoki VS Code SQLite Viewer yordamida bazaning vizual ER-diagrammasini ko'rish va tekshirish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun shaxsiy kompyuter;
- Python 3.10+;
- VS Code va SQLite Viewer kengaytmasi (yoki DBeaver Community);
- ERD chizish uchun qog'oz, doska yoki draw.io / dbdiagram.io vositalari.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Jadval cheklovlari, Primary Key turlari va ON DELETE qoidalari bo'yicha blits-nazorat |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | ER-model konsepsiyasi: Obyektlar, atributlar, munosabatlar va kardinallik (1:1, 1:N, M:N) |
| **30–50 min** | Arxitektura loyihalash: Maktab platformasi | "Maktab tahliliy platformasi" ER-diagrammasini chizish, Junction table mantiqi |
| **50–70 min** | Amaliy dasturlash (Python sqlite3) | `maktab.db` bazasini yaratish, DDL jadvallarni bog'lash va namunaviy ma'lumotlar kiritish |
| **70–80 min** | Dars xulosasi va baholash | ERD tahlili, o'quvchilar ishlarini tekshirish va uyga vazifani tushuntirish |

---

## Nazariy qism (Batafsil konspekt)

### 1. ERD (Entity-Relationship Diagram) nima?

**ERD (Entity-Relationship Diagram)** — bu ma'lumotlar bazasida saqlanadigan obyektlar (Entity), ularning xususiyatlari (Attribute) va ular o'rtasidagi mantiqiy bog'lanishlarni (Relationship) aks ettiruvchi ko'rgazmali grafik chizmadir.

Dasturiy injiniringda eng asosiy qoida: **"Avval loyihala (ERD), keyin kod yoz (CREATE TABLE)!"**  
Agar arxitektura chizmasiz boshlansa, keyinchalik bazani qayta qurish millionlab dollar va oylab mehnat talab qiladi.

**ERD ning 3 ta asosiy ustuni:**
1. **Entity (Obyekt):** Ma'lumot to'planadigan aniq tushuncha yoki narsa (to'rtburchak bilan belgilanadi). Masalan: `O'quvchi`, `Maktab`, `Fan`, `Hudud`.
2. **Attribute (Xususiyat/Atribut):** Obyektni tavsiflovchi xossalar (oval yoki jadval ustunlari). Masalan: `ism`, `sig'im`, `telefon`, `viloyat`.
3. **Relationship (Munosabat):** Obyektlar orasidagi bog'liqlik (romb yoki chiziqlar). Masalan: "O'quvchi maktabda **o'qiydi**", "O'qituvchi fandan **dars beradi**".

---

### 2. Munosabatlar kardinalligi (Cardinality)

Bog'lanayotgan yozuvlar soniga qarab munosabatlar 3 turga bo'linadi:

1. **1:1 (Birga-bir):**
   - Bitta obyekt boshqa jadvaldagi faqat bitta obyektga mos keladi.
   - *Misol:* Bitta fuqaro — bitta biometrik pasport. Bitta talaba — bitta talabalik guvohnomasi.
2. **1:N (Birga-ko'p / One-to-Many):**
   - Ota jadvaldagi bitta satrga bolalar jadvalidagi bir nechta satrlar to'g'ri keladi, lekin har bir bola faqat bitta otaga tegishli bo'ladi.
   - *Misol:* Bitta viloyatda ko'plab maktablar bor, lekin bitta maktab faqat bitta viloyatga qarashli. Eng ko'p ishlatiladigan relyatsion model!
3. **M:N (Ko'pga-ko'p / Many-to-Many):**
   - Bitta obyekt ko'plab boshqa obyektlarga, va aksincha, bog'lanishi mumkin.
   - *Misol:* Bitta o'quvchi bir nechta to'garakka qatnashadi; bitta to'garakda bir nechta o'quvchi bor.

---

### 3. Junction (Bridge) Table — Ko'pga-ko'p munosabatni yechish

Relyatsion ma'lumotlar bazalarida M:N bog'lanishini to'g'ridan-to'g'ri yaratishning iloji yo'q (chunki ustunga bir nechta ID larni massiv qilib yozish relyatsion qonunlarni buzadi).  
Shu sababli, o'rtaga **Junction Table (Oraliq / Ko'prik jadval)** qo'yiladi va bitta M:N bog'lanish ikkita 1:N bog'lanishga aylantiriladi:

```
[oquvchilar] (1) ───< (N) [oquvchi_togarak] (N) >─── (1) [togaraklar]
```
`oquvchi_togarak` oraliq jadvali ikkita Foreign Key ga ega bo'ladi: `oquvchi_id` va `togarak_id`.

---

### 4. Rasmiy keys: "Maktab tahliliy platformasi" ERD modeli

O'zbekiston ta'limi bo'yicha BI tahliliy platformasi quyidagi 3 ta asosiy relyatsion jadvaldan iborat bo'ladi:

1. **hududlar (Viloyatlar va shaharlar):**
   - `hudud_id` (PK, INTEGER)
   - `nomi` (TEXT, UNIQUE, NOT NULL)
   - `markaz` (TEXT)
2. **maktablar (Ta'lim muassasalari):**
   - `maktab_id` (PK, INTEGER)
   - `hudud_id` (FK ──→ `hududlar.hudud_id`)
   - `raqam` (INTEGER)
   - `sigim` (INTEGER CHECK > 0)
   - `turi` (TEXT DEFAULT 'Umumiy o''rta')
3. **yillik_kpi (Ta'lim statistikasi va KPI ko'rsatkichlari):**
   - `kpi_id` (PK, INTEGER)
   - `hudud_id` (FK ──→ `hududlar.hudud_id`)
   - `yil` (INTEGER NOT NULL)
   - `oquvchilar_soni` (INTEGER NOT NULL)
   - `oqituvchilar_soni` (INTEGER NOT NULL)
   - `maktablar_soni` (INTEGER NOT NULL)
   - `UNIQUE (hudud_id, yil)`

---

## Kod namunalari

### 1-namuna: Python `sqlite3` da to'liq Maktab ERD tizimini yaratish

```python
import sqlite3

# 1. Baza faylini ochamiz
conn = sqlite3.connect('data/maktab.db')
cursor = conn.cursor()

# Xorijiy kalitlar tekshiruvini faollashtiramiz
cursor.execute("PRAGMA foreign_keys = ON;")

# 2. Hududlar jadvali
cursor.execute('''
CREATE TABLE IF NOT EXISTS hududlar (
    hudud_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nomi TEXT NOT NULL UNIQUE,
    markaz TEXT NOT NULL
);
''')

# 3. Maktablar jadvali (hududlar ga 1:N bog'langan)
cursor.execute('''
CREATE TABLE IF NOT EXISTS maktablar (
    maktab_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hudud_id INTEGER NOT NULL,
    raqam INTEGER NOT NULL,
    sigim INTEGER NOT NULL CHECK (sigim > 0),
    turi TEXT DEFAULT 'Umumiy o''rta',
    FOREIGN KEY (hudud_id) REFERENCES hududlar(hudud_id) ON DELETE CASCADE,
    UNIQUE (hudud_id, raqam)
);
''')

# 4. Yillik ta'lim KPI jadvali
cursor.execute('''
CREATE TABLE IF NOT EXISTS yillik_kpi (
    kpi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hudud_id INTEGER NOT NULL,
    yil INTEGER NOT NULL CHECK (yil >= 2000 AND yil <= 2100),
    oquvchilar_soni INTEGER NOT NULL CHECK (oquvchilar_soni >= 0),
    oqituvchilar_soni INTEGER NOT NULL CHECK (oqituvchilar_soni >= 0),
    maktablar_soni INTEGER NOT NULL CHECK (maktablar_soni >= 0),
    FOREIGN KEY (hudud_id) REFERENCES hududlar(hudud_id) ON DELETE CASCADE,
    UNIQUE (hudud_id, yil)
);
''')

conn.commit()
print("Maktab platformasi ERD jadvallari muvaffaqiyatli barpo etildi!")
```

### 2-namuna: Ma'lumotlarni to'ldirish va mantiqiy bog'lanishlarni tekshirish

```python
# Hududlarni kiritamiz
cursor.execute("INSERT OR IGNORE INTO hududlar (hudud_id, nomi, markaz) VALUES (1, 'Toshkent shahri', 'Toshkent');")
cursor.execute("INSERT OR IGNORE INTO hududlar (hudud_id, nomi, markaz) VALUES (2, 'Samarqand viloyati', 'Samarqand');")

# Maktablarni kiritamiz
cursor.execute("INSERT OR IGNORE INTO maktablar (hudud_id, raqam, sigim) VALUES (1, 14, 1200);")
cursor.execute("INSERT OR IGNORE INTO maktablar (hudud_id, raqam, sigim) VALUES (1, 28, 850);")
cursor.execute("INSERT OR IGNORE INTO maktablar (hudud_id, raqam, sigim) VALUES (2, 1, 1500);")

# 2024-yilgi KPI ko'rsatkichlarini kiritamiz
cursor.execute("""
INSERT OR IGNORE INTO yillik_kpi (hudud_id, yil, oquvchilar_soni, oqituvchilar_soni, maktablar_soni) 
VALUES (1, 2024, 485000, 32000, 340);
""")
cursor.execute("""
INSERT OR IGNORE INTO yillik_kpi (hudud_id, yil, oquvchilar_soni, oqituvchilar_soni, maktablar_soni) 
VALUES (2, 2024, 620000, 48000, 1260);
""")

conn.commit()

# JOIN so'rovi orqali tahliliy hisobotni ko'ramiz
cursor.execute('''
SELECT 
    h.nomi,
    k.yil,
    k.maktablar_soni,
    k.oquvchilar_soni,
    k.oqituvchilar_soni,
    ROUND(CAST(k.oquvchilar_soni AS REAL) / k.oqituvchilar_soni, 1) AS oquvchi_oqituvchi_nisbati
FROM yillik_kpi k
JOIN hududlar h ON k.hudud_id = h.hudud_id;
''')

print("\n--- O'zbekiston Ta'lim Statistikasi (KPI) ---")
for row in cursor.fetchall():
    print(f"Hudud: {row[0]} | Yil: {row[1]} | Maktablar: {row[2]} | Nisbat: 1 o'qituvchiga {row[5]} o'quvchi")

conn.close()
```

---

## Amaliy topshiriqlar

### 1-topshiriq: M:N bog'lanish va Junction Table (Oson)
Kutubxona tizimida `kitobxonlar` va `kitoblar` o'rtasida Ko'pga-ko'p (M:N) munosabat mavjud (bitta kitobxon ko'p kitob o'qiydi, bitta kitobni ko'p kitobxonlar navbat bilan oladi). Ushbu munosabatni 2 ta 1:N ga aylantiruvchi `ijara_tarixi` nomli oraliq jadval yaratuvchi SQL so'rovini yozing.

**Kutiladigan natija:** Oraliq jadval ikkala jadvalning PK ustunlarini Foreign Key qilib oladi.  
**Yechim:**  
```sql
CREATE TABLE ijara_tarixi (
    ijara_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kitobxon_id INTEGER NOT NULL,
    kitob_id INTEGER NOT NULL,
    olingan_sana TEXT NOT NULL,
    topshirilgan_sana TEXT,
    FOREIGN KEY (kitobxon_id) REFERENCES kitobxonlar(kitobxon_id),
    FOREIGN KEY (kitob_id) REFERENCES kitoblar(kitob_id)
);
```

---

### 2-topshiriq: ERD modeldagi mantiqiy xatoni topish (O'rta)
O'quvchi quyidagi modelni chizgan:
`oquvchilar (oquvchi_id, ism, maktab_raqami, hudud_nomi)`
Ushbu model nima uchun relyatsion talablarga zid va qanday anomaliyalarga olib keladi? Uni qanday qilib to'g'ri ERD ga ajratish lozim?

**Kutiladigan natija:** Maktab va hudud ma'lumotlari dublikat bo'lishi va uni 3 ta alohida jadvalga ajratish kerakligi isbotlanadi.  
**Yechim:**  
Ushbu bitta jadvalda maktab va hudud ma'lumotlari minglab marta takrorlanadi (Redundancy). Agar hudud nomi o'zgarsa, hamma qatorda yangilash kerak bo'ladi (Update anomaly).
To'g'ri model: `hududlar (hudud_id PK) ──→ maktablar (maktab_id PK, hudud_id FK) ──→ oquvchilar (oquvchi_id PK, maktab_id FK)`.

---

### 3-topshiriq: O'quvchi-o'qituvchi resurs yuklamasi hisoboti (Qiyin)
`maktab.db` bazasiga O'zbekistonning yana kamida 3 ta viloyati (Andijon, Namangan, Buxoro) uchun 2023 va 2024-yillardagi ma'lumotlarni kiriting. SQL JOIN orqali har bir hudud bo'yicha:
1. O'quvchi / maktab yuklamasi (`oquvchilar_soni / maktablar_soni`);
2. O'quvchi / o'qituvchi nisbati (`oquvchilar_soni / oqituvchilar_soni`) ni hisoblovchi skript tuzing.

**Kutiladigan natija:** Matematik hisob-kitoblar SQL darajasida bajarilib, chiroyli analitik natija olinadi.  
**Yechim:**  
```python
import sqlite3

conn = sqlite3.connect('data/maktab.db')
c = conn.cursor()

c.execute("""
SELECT 
    h.nomi,
    k.yil,
    ROUND(k.oquvchilar_soni * 1.0 / k.maktablar_soni, 0) AS oquvchi_maktab_yuklama,
    ROUND(k.oquvchilar_soni * 1.0 / k.oqituvchilar_soni, 2) AS oquvchi_oqituvchi_nisbat
FROM yillik_kpi k
JOIN hududlar h ON k.hudud_id = h.hudud_id
ORDER BY k.yil DESC, oquvchi_oqituvchi_nisbat DESC;
""")

for r in c.fetchall():
    print(f"Viloyat: {r[0]:<20} | Yil: {r[1]} | Maktab yukl: {r[2]} o'quvchi | Nisbat: 1/{r[3]}")

conn.close()
```

---

## Tezkor nazorat savollari

1. ER-diagrammadagi "Kardinallik" (Cardinality) nimani anglatadi?  
   *Javob:* Ikkita obyekt o'rtasidagi bog'lanish soniy nisbatini (1:1, 1:N yoki M:N).
2. Relyatsion bazada Ko'pga-ko'p (M:N) munosabatni nega to'g'ridan-to'g'ri saqlab bo'lmaydi?  
   *Javob:* Chunki satr katagiga bir nechta qiymatni (massiv) yozish mumkin emas; bu holda oraliq (Junction) jadval orqali ikkita 1:N ga ajratiladi.
3. Chen notatsiyasi bilan Crow's Foot notatsiyasining qanday farqi bor?  
   *Javob:* Chen modelida obyektlar to'rtburchak, atributlar oval va munosabatlar romb bilan chiziladi; Crow's Foot modelida esa jadvallar to'rtburchak jadval sifatida va uchlaridagi qarg'a oyog'i belgilari bilan ifodalanadi.
4. "Maktab tahliliy platformasi" da `yillik_kpi` jadvalida nima uchun `hudud_id` va `yil` ustunlariga `UNIQUE (hudud_id, yil)` o'rnatildi?  
   *Javob:* Ayni bir viloyatning bir xil yildagi statistikasi bazaga yanglishib 2 marta kiritilishining oldini olish uchun.

---

## Uyga vazifa

1. O'zingiz qiziqqan bitta soha (sport musobaqalari, internet-magazin yoki aviaqatnovlar) uchun kamida 4 ta jadvaldan iborat ER-diagrammani qog'ozda yoki grafik dasturda chizing.
2. Unda kamida bitta M:N munosabat bo'lsin va uni Junction table orqali to'g'ri yeching.
3. Ushbu diagramma asosida Python `sqlite3` yordamida to'liq ishchi `.db` bazasini yarating va kamida 3 tadan namunaviy yozuv kiriting.
