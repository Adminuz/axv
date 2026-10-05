# 7-dars: Relyatsion jadvallar, Primary Key, Foreign Key va relyatsion yaxlitlik

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta, 1-dars (umumiy 7-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga relyatsion ma'lumotlar bazasida jadvallar arxitekturasini chuqur o'rgatish; ma'lumotlar yaxlitligi (Data Integrity) tushunchasi va jadval cheklovlari (**Constraints: NOT NULL, UNIQUE, CHECK, DEFAULT**) mohiyatini tushuntirish; **Primary Key** turlari (Natural vs Surrogate Key, Composite Primary Key), **Foreign Key** ishlash mexanizmi hamda bog'langan yozuvlar ustidagi amallar (**ON DELETE CASCADE, RESTRICT, SET NULL**) ni tahlil qilish; relyatsion ma'lumotlar bazasida anomaliyalar (Insert, Update, Delete anomaliyalari) ning oldini olish ko'nikmalarini shakllantirish; Python (`sqlite3`) orqali mukammal jadvallar sxemasini yaratish va yaxlitlik tekshiruvlarini dasturiy amalga oshirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Relyatsion jadval sxemasi (Schema) va uning asosiy cheklovlari (`PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`) vazifalarini bilish;
- Natural Key (tabiiy kalit) va Surrogate Key (sun'iy/avtomatik kalit) o'rtasidagi farqni tushunish;
- Composite Primary Key (bir nechta ustundan iborat murakkab kalit, masalan: `(hudud, yil)`) qachon va nima uchun qo'llanilishini bilish;
- Foreign Key (tashqi kalit) orqali jadvallar bog'langanda relyatsion yaxlitlik (Referential Integrity) qanday saqlanishini tushunish;
- Ota yozuv o'chirilganda yoki yangilanganda `ON DELETE CASCADE`, `RESTRICT` va `SET NULL` qoidalarining farqini amalda ko'rsata olish;
- Normalizatsiyalanmagan ma'lumotlardagi 3 ta asosiy anomaliyani (Qo'shish, Yangilash, O'chirish anomaliyalari) aniqlay olish;
- Python'dagi `sqlite3` moduli orqali barcha qat'iy cheklovlar bilan ta'minlangan relyatsion jadvallarni yarata olish va cheklovlar buzilganda yuzaga keladigan `sqlite3.IntegrityError` xatolarini to'g'ri boshqara olish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun shaxsiy kompyuter;
- Python 3.10+ (o'rnatilgan `sqlite3` moduli bilan);
- DBeaver yoki SQLite Viewer (VS Code kengaytmasi);
- O'quv qo'llanma va rasmiy uslubiy ko'rsatmalar.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | RDBMS konsepti, fayllar va bazalar farqi, ACID tamoyillari bo'yicha blits-so'rov |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | Relyatsion jadvallar, Constraints (NOT NULL, UNIQUE, CHECK, DEFAULT), Natural vs Surrogate Key |
| **30–50 min** | Chuqur tahlil: Composite PK va FK qoidalari | Composite Primary Key `(hudud, yil)`, ON DELETE xatti-harakatlari va relyatsion anomaliyalar |
| **50–70 min** | Amaliy dasturlash (Python sqlite3) | Cheklovlar bilan jadvallar yaratish, IntegrityError xatolarini sinash va bog'langan o'chirish |
| **70–80 min** | Dars xulosasi va baholash | Mavzuni mustahkamlash, tezkor savollar va uyga vazifani tushuntirish |

---

## Nazariy qism (Batafsil konspekt)

### 1. Relyatsion jadval sxemasi va Cheklovlar (Constraints)

Relyatsion ma'lumotlar bazasida har bir jadval qat'iy belgilangan qoidalar asosida quriladi. Ma'lumotlarning tozaligi va xatosizligini ta'minlash uchun **Constraints (Cheklovlar)** qo'llaniladi:

1. **PRIMARY KEY:** Satrni unikal identifikatsiya qiladi (`NOT NULL` + `UNIQUE`).
2. **NOT NULL:** Ustun bo'sh qolishiga (`NULL`) yo'l qo'ymaydi (masalan, o'quvchining ismi bo'sh bo'lishi mumkin emas).
3. **UNIQUE:** Ustundagi barcha qiymatlar takrorlanmas bo'lishi shart (masalan, pasport raqami, telefon, email).
4. **CHECK:** Ustunga kiritilayotgan qiymat ma'lum bir mantiqiy shartga mos kelishini tekshiradi (masalan, `CHECK (yosh >= 6 AND yosh <= 100)` yoki `CHECK (balans >= 0)`).
5. **DEFAULT:** Agar qiymat kiritilmasa, avtomatik tayinlanadigan standart qiymat (masalan, `shahar DEFAULT 'Toshkent'`, `holat DEFAULT 'Faol'`).

---

### 2. Primary Key turlari: Natural, Surrogate va Composite

- **Natural Key (Tabiiy kalit):** Haqiqiy hayotdan olingan unikal xususiyat (masalan, JSHSHIR, avtomobil VIN raqami, kitobning ISBN kodi). Kamchiligi: vaqt o'tishi bilan tashqi standartlar o'zgarishi mumkin.
- **Surrogate Key (Sun'iy kalit):** Baza tomonidan sun'iy ravishda yaratiladigan tartib raqam (`id INTEGER PRIMARY KEY AUTOINCREMENT`). U biznes mantiqqa bog'liq bo'lmaydi va tizim uchun eng qulay hisoblanadi.
- **Composite Primary Key (Murakkab kalit):** Bitta ustun unikal bo'la olmaganda, 2 yoki undan ortiq ustunlar birikmasi Primary Key qilib belgilanadi.
  - *Rasmiy uslubiy ko'rsatmadagi klassik misol:* Ta'lim statistikasida bitta hudud (masalan, "Samarqand") bir necha yil takrorlanadi, bitta yil (2024) ham barcha viloyatlarda takrorlanadi. Lekin **(hudud, yil)** birikmasi har bir ko'rsatkich uchun yagonadir!
  ```sql
  PRIMARY KEY (hudud, yil)
  ```

---

### 3. Foreign Key va Referential Integrity (Relyatsion yaxlitlik)

Foreign Key — bu boshqa jadvaldagi Primary Key ustuniga ishora qiluvchi bog'lovchi zanjirdir. Relyatsion yaxlitlik qoidasiga ko'ra:
- Bolalar jadvalidagi (Child table) FK ustuniga ota jadvalda (Parent table) mavjud bo'lmagan qiymatni kiritish taqiqlanadi.
- **Ota jadvaldan yozuv o'chirilganda nima bo'ladi? (`ON DELETE` qoidalari):**
  1. `ON DELETE RESTRICT` (Standart): Agar bolalar jadvalida bog'langan yozuvlar bo'lsa, ota yozuvni o'chirishga ruxsat berilmaydi (xatolik qaytaradi).
  2. `ON DELETE CASCADE`: Ota yozuv o'chirilganda, unga bog'liq bo'lgan barcha bolalar yozuvlari ham avtomatik o'chirib yuboriladi (masalan, mijoz o'chirilsa, uning barcha buyurtmalari ham o'chadi).
  3. `ON DELETE SET NULL`: Ota yozuv o'chirilganda, bolalar jadvalidagi FK ustunlari qiymati `NULL` qilib qo'yiladi.

---

### 4. Relyatsion anomaliyalar

Agar jadvallar to'g'ri relyatsion modelda loyihalanmasa, 3 xil jiddiy anomaliya vujudga keladi:
1. **Insertion Anomaly (Qo'shish anomaliyasi):** Yangi o'qituvchini tizimga kiritish uchun albatta maktabda sinf ochilgan bo'lishi shart bo'lib qoladi.
2. **Update Anomaly (Yangilash anomaliyasi):** Maktab direktori o'zgarganda, bitta ma'lumotni 10 000 ta qatorda alohida o'zgartirish talab etiladi. Bitta joyda xato ketsa, ma'lumotlar qarama-qarshi bo'lib qoladi.
3. **Deletion Anomaly (O'chirish anomaliyasi):** Bitta o'quvchi maktabdan ketganda, u bilan birga butun bir fan yoki sinf ma'lumotlari ham tasodifan bazadan o'chib ketadi.

Relyatsion jadvallarga ajratish va PK/FK tizimini to'g'ri o'rnatish ushbu barcha anomaliyalarni yo'q qiladi!

---

## Kod namunalari

### 1-namuna: Qat'iy cheklovlar (Constraints) bilan jadval yaratish

```python
import sqlite3

conn = sqlite3.connect('data/talim_tizimi.db')
cursor = conn.cursor()

# SQLite'da xorijiy kalitlarni yoqamiz
cursor.execute("PRAGMA foreign_keys = ON;")

# Maktablar jadvali (Cheklovlar bilan)
cursor.execute('''
CREATE TABLE IF NOT EXISTS maktablar (
    maktab_id INTEGER PRIMARY KEY AUTOINCREMENT,
    raqam INTEGER NOT NULL,
    hudud TEXT NOT NULL,
    sigim INTEGER NOT NULL CHECK (sigim > 0 AND sigim <= 5000),
    turi TEXT DEFAULT 'Umumiy o''rta',
    UNIQUE (raqam, hudud)
);
''')

# O'quvchilar jadvali (Foreign Key va CASCADE bilan)
cursor.execute('''
CREATE TABLE IF NOT EXISTS oquvchilar (
    oquvchi_id INTEGER PRIMARY KEY AUTOINCREMENT,
    maktab_id INTEGER NOT NULL,
    ism TEXT NOT NULL,
    jshshir TEXT UNIQUE NOT NULL,
    sinf INTEGER NOT NULL CHECK (sinf >= 1 AND sinf <= 11),
    holat TEXT DEFAULT 'O''qiydi' CHECK (holat IN ('O''qiydi', 'Ketgan', 'Bitirgan')),
    FOREIGN KEY (maktab_id) REFERENCES maktablar(maktab_id) ON DELETE CASCADE
);
''')

conn.commit()
print("Jadvallar barcha cheklovlar bilan yaratildi!")
```

### 2-namuna: Cheklovlar xatosini (IntegrityError) tutib olish

```python
# 1. To'g'ri maktab qo'shamiz
cursor.execute("INSERT INTO maktablar (raqam, hudud, sigim) VALUES (42, 'Toshkent', 1200);")
conn.commit()

# 2. CHECK xatosini sinaymiz (sig'im manfiy bo'lishi mumkin emas)
try:
    cursor.execute("INSERT INTO maktablar (raqam, hudud, sigim) VALUES (15, 'Samarqand', -50);")
    conn.commit()
except sqlite3.IntegrityError as e:
    print("Kutilgan xatolik (CHECK buzildi):", e)

# 3. UNIQUE xatosini sinaymiz (Toshkentda 42-maktab allaqachon bor)
try:
    cursor.execute("INSERT INTO maktablar (raqam, hudud, sigim) VALUES (42, 'Toshkent', 800);")
    conn.commit()
except sqlite3.IntegrityError as e:
    print("Kutilgan xatolik (UNIQUE buzildi):", e)

conn.close()
```

### 3-namuna: Composite Primary Key (Murakkab kalit) yaratish

```python
conn = sqlite3.connect('data/statistika.db')
c = conn.cursor()

# Hudud va Yil birikmasi Composite Primary Key hisoblanadi
c.execute('''
CREATE TABLE IF NOT EXISTS hududiy_statistika (
    hudud TEXT NOT NULL,
    yil INTEGER NOT NULL,
    maktablar_soni INTEGER NOT NULL CHECK (maktablar_soni >= 0),
    oquvchilar_soni INTEGER NOT NULL CHECK (oquvchilar_soni >= 0),
    oqituvchilar_soni INTEGER NOT NULL CHECK (oqituvchilar_soni >= 0),
    PRIMARY KEY (hudud, yil)
);
''')

# Birinchi yozuv kiritiladi
c.execute("INSERT INTO hududiy_statistika VALUES ('Farg''ona', 2024, 940, 680000, 42000);")
conn.commit()

# Xuddi shu hudud va shu yil qayta kiritilsa - xato beradi!
try:
    c.execute("INSERT INTO hududiy_statistika VALUES ('Farg''ona', 2024, 950, 685000, 42500);")
    conn.commit()
except sqlite3.IntegrityError as e:
    print("Composite PK xatosi: bir xil hudud va yil takrorlanishi taqiqlangan!", e)

conn.close()
```

---

## Amaliy topshiriqlar

### 1-topshiriq: CHECK cheklovini loyihalash (Oson)
Tibbiy tahlil markazi uchun `bemorlar` jadvalini yarating. Unda:
- `bemor_id`: butun son, Primary Key;
- `ism`: matn, `NOT NULL`;
- `yosh`: butun son, `CHECK (yosh >= 0 AND yosh <= 120)`;
- `qon_guruhi`: matn, `CHECK (qon_guruhi IN ('I', 'II', 'III', 'IV'))`;
- `holat`: matn, odatiy qiymati `DEFAULT 'Kuzatuvda'`.  
Noto'g'ri qon guruhi ('V') kiritilganda nima sodir bo'lishini ko'rsating.

**Kutiladigan natija:** Jadval cheklovlar bilan hosil bo'ladi va noto'g'ri qon guruhi kiritilganda `IntegrityError` qaytadi.  
**Yechim:**  
```python
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''
CREATE TABLE bemorlar (
    bemor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism TEXT NOT NULL,
    yosh INTEGER CHECK (yosh >= 0 AND yosh <= 120),
    qon_guruhi TEXT CHECK (qon_guruhi IN ('I', 'II', 'III', 'IV')),
    holat TEXT DEFAULT 'Kuzatuvda'
);
''')
try:
    c.execute("INSERT INTO bemorlar (ism, yosh, qon_guruhi) VALUES ('Aziz', 28, 'V');")
except sqlite3.IntegrityError as err:
    print("Xato tutildi:", err)
conn.close()
```

---

### 2-topshiriq: ON DELETE CASCADE xatti-harakatini tekshirish (O'rta)
O'qituvchi va ularning dars soatlari o'rtasida 1:N munosabat o'rnating:
1. `oqituvchilar (oqituvchi_id PK, ism, fan)`
2. `dars_soatlari (soat_id PK, oqituvchi_id FK, sinf, soat)`
Foreign Key ga `ON DELETE CASCADE` qoidasini bering. O'qituvchi o'chirilganda unga tegishli barcha dars soatlari avtomatik o'chib ketishini kod orqali isbotlang.

**Kutiladigan natija:** Ota jadvaldan yozuv o'chirilgach, bolalar jadvalidagi unga bog'liq barcha yozuvlar soni 0 ga teng bo'ladi.  
**Yechim:**  
```python
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON;")

c.execute("CREATE TABLE oqituvchilar (oqituvchi_id INT PRIMARY KEY, ism TEXT);")
c.execute('''
CREATE TABLE dars_soatlari (
    soat_id INT PRIMARY KEY,
    oqituvchi_id INT,
    sinf TEXT,
    FOREIGN KEY (oqituvchi_id) REFERENCES oqituvchilar(oqituvchi_id) ON DELETE CASCADE
);
''')

c.execute("INSERT INTO oqituvchilar VALUES (1, 'Husanov');")
c.execute("INSERT INTO dars_soatlari VALUES (101, 1, '10-A');")
c.execute("INSERT INTO dars_soatlari VALUES (102, 1, '10-B');")
conn.commit()

# O'qituvchini o'chiramiz
c.execute("DELETE FROM oqituvchilar WHERE oqituvchi_id = 1;")
conn.commit()

c.execute("SELECT COUNT(*) FROM dars_soatlari;")
print("Qolgan dars soatlari soni:", c.fetchone()[0]) # Natija: 0
conn.close()
```

---

### 3-topshiriq: Composite Primary Key va anomaliya tahlili (Qiyin)
Maktab platformasi uchun `fan_baholari` jadvalini loyihalang:
Bitta o'quvchi bitta fandan bitta chorakda faqat bitta yakuniy baho olishi mumkin.
Ustunlar: `(oquvchi_id, fan_id, chorak, baho)`.
Ushbu jadvalda Composite Primary Key qaysi ustunlardan iborat bo'lishini aniqlang va uni SQLite'da amalga oshiring. Nima uchun faqat `oquvchi_id` yoki faqat `fan_id` ni PK qilib bo'lmasligini tushuntiring.

**Kutiladigan natija:** `PRIMARY KEY (oquvchi_id, fan_id, chorak)` orqali uchlik kalit yaratiladi va takroriy baho kiritilishidan himoyalanadi.  
**Yechim:**  
Agar faqat `oquvchi_id` PK bo'lsa, o'quvchi faqat bitta baho ola oladi. Agar faqat `fan_id` PK bo'lsa, fandan butun maktabda bitta o'quvchi baho oladi.
To'g'ri yechim:
```sql
CREATE TABLE fan_baholari (
    oquvchi_id INTEGER NOT NULL,
    fan_id INTEGER NOT NULL,
    chorak INTEGER NOT NULL CHECK (chorak BETWEEN 1 AND 4),
    baho INTEGER NOT NULL CHECK (baho BETWEEN 2 AND 5),
    PRIMARY KEY (oquvchi_id, fan_id, chorak)
);
```

---

## Tezkor nazorat savollari

1. Natural Key va Surrogate Key ning asosiy farqi nimada?  
   *Javob:* Natural key hayotiy mavjud ma'lumot (JSHSHIR, ISBN), Surrogate key esa dastur tomonidan sun'iy ravishda yaratiladigan avtomatik ID raqamdir.
2. Composite Primary Key nima uchun kerak?  
   *Javob:* Jadvalda bitta ustun yozuvni to'liq unikal aniqlay olmaganda (masalan, viloyat va yil), bir nechta ustunlar birikmasidan unikal kalit yasaladi.
3. `ON DELETE RESTRICT` bilan `ON DELETE CASCADE` ning farqi nima?  
   *Javob:* RESTRICT ota yozuvga bog'langan bola yozuvlar bo'lsa o'chirishga ruxsat bermaydi; CASCADE esa ota yozuv bilan birga uning barcha bog'langan bolalarini ham birvarakayiga o'chirib yuboradi.
4. Jadvaldagi `CHECK` cheklovi nima vazifani bajaradi?  
   *Javob:* Ustunga kiritilayotgan ma'lumotning mantiqiy to'g'riligini (masalan, yosh > 0 yoki baho 1 dan 5 gacha) qat'iy nazorat qiladi.

---

## Uyga vazifa

1. Elektron kutubxona uchun 2 ta bog'langan jadval (`kitoblar` va `ijaralar`) sxemasini barcha cheklovlar (`NOT NULL`, `CHECK`, `UNIQUE`, `DEFAULT`) bilan loyihalang.
2. `ijaralar` jadvalida bitta kitobni ayni bir vaqtda faqat bitta kitobxon olib ketishi qoidasini va `ON DELETE RESTRICT` bog'lanishini ta'minlang.
3. Python `sqlite3` da ushbu jadvallarni yarating va cheklovlar to'g'ri ishlayotganini xatolar keltirib chiqarish orqali sinab ko'ring.
