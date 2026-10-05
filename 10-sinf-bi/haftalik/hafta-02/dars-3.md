# 6-dars: Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 2-hafta, 3-dars (umumiy 6-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga zamonaviy axborot tizimlarining markaziy poydevori bo'lgan **Ma'lumotlar bazasi (Database)** va **RDBMS (Relational Database Management System)** konsepsiyasini o'rgatish; faylli tizimlar (CSV, JSON) va ma'lumotlar bazalarining tub farqlarini ko'rsatish; relatsion jadval elementlari (Table, Row, Column), kalitlar tizimi (**Primary Key va Foreign Key**), **ACID tranzaksiya tamoyillari** hamda **ER-diagramma (Entity-Relationship Diagram)** loyihalash asoslarini tushuntirish; Python (`sqlite3` moduli) va SQL tili yordamida dastlabki relyatsion jadvallarni yaratish, ma'lumot kiritish va bog'langan so'rovlarni (`JOIN`) bajarish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Ma'lumotlar bazasi (Database) nima ekanligi va uning fayllardan (CSV/Excel) 5 ta asosiy ustunligini (yaxlitlik, xavfsizlik, tranzaksiyalar, parallel foydalanish, indeksatsiya) bilish;
- RDBMS ning relatsion modeli: Jadval (Relation), Satr (Tuple/Record) va Ustun (Attribute/Field) elementlarini farqlash;
- Primary Key (birlamchi kalit) va Foreign Key (tashqi kalit) vazifalarini hamda relyatsion yaxlitlik (Referential Integrity) qoidalarini tushunish;
- `customers.customer_id → orders.customer_id` va `products.product_id → orders.product_id` kabi real bog'lanishlarni tahlil qila olish;
- ACID tamoyillarini (Atomicity, Consistency, Isolation, Durability) real bank/to'lov operatsiyasi misolida tushuntira olish;
- R-Diagramma (ERD) tushunchasi: Obyektlar, atributlar va munosabat turlarini (1:1, 1:N, M:N) bilish;
- Python'dagi `sqlite3` yordamida o'zaro bog'langan 2 ta jadval yaratish, ma'lumot qo'shish va `SELECT ... INNER JOIN` so'rovini yoza olish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun shaxsiy kompyuter;
- Python 3.10+ (o'rnatilgan `sqlite3` moduli bilan);
- DBeaver yoki SQLite Viewer (VS Code kengaytmasi) ma'lumotlar bazasini vizual ko'rish uchun;
- ERD chizish uchun vositalar (draw.io yoki oq doska).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Parquet va Avro formatlari, Columnar vs Row-based saqlash bo'yicha savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | Ma'lumotlar bazasi nima? Nega CSV yetarli emas? RDBMS tushunchasi, Relatsion model, PK/FK |
| **30–50 min** | ACID tamoyillari va ER-model | ACID tamoyillari, `customers → orders → products` munosabatlari va ERD loyihalash |
| **50–70 min** | Amaliy namoyish va mashg'ulot | Python `sqlite3` da jadvallar yaratish (`CREATE TABLE`), ma'lumot kiritish va `JOIN` so'rovi |
| **70–80 min** | Dars xulosasi va baholash | 2-hafta umumiy xulosalari, tezkor savollar va uyga vazifani tushuntirish |

---

## Nazariy qism (Batafsil konspekt)

### 1. Ma'lumotlar bazasi (Database) nima va nega fayllar yetarli emas?

**Ma'lumotlar bazasi (DB)** — bu o'zaro mantiqiy bog'langan, ma'lum bir tartibda tashkil etilgan va kompyuter xotirasida saqlanadigan ma'lumotlar to'plamidir.

Biz o'tgan darslarda CSV, JSON, Parquet kabi fayllarni ko'rib chiqdik. Ammo nima uchun butun jahon banklari, internet-do'konlar va ijtimoiy tarmoqlar barcha narsani shunchaki fayllarda saqlamaydi?

**Fayllar (CSV/Excel) va Ma'lumotlar bazasi (RDBMS) farqi:**
1. **Parallel foydalanish (Concurrency):** Agar 1000 kishi bir vaqtda bitta CSV faylga yangi qator yozmoqchi bo'lsa, fayl qulflanadi (file lock) yoki ma'lumotlar buziladi. RDBMS bir vaqtda millionlab foydalanuvchilarning xavfsiz ishlashini ta'minlaydi.
2. **Ma'lumotlar yaxlitligi (Data Integrity):** CSV da `yosh` ustuniga xohlagan odam matn yozib qo'yishi mumkin. RDBMS esa cheklovlar (`CHECK`, `NOT NULL`, `UNIQUE`) orqali xato kiritishga yo'l qo'ymaydi.
3. **Tranzaksiyalar (ACID):** Bankda pul o'tkazishda bittadan pul yechilib, ikkinchisiga tushishi shart. Fayllarda bu kafolatlanmaydi.
4. **Xavfsizlik va kirish huquqlari:** RDBMS'da har bir foydalanuvchiga alohida ruxsat berish mumkin (masalan, o'qituvchi baho qo'yishi mumkin, o'quvchi faqat ko'ra oladi).
5. **Katta hajmda tezkor qidiruv:** B-Tree indekslar tufayli milliardlab qatorlar ichidan bitta yozuvni millisekundlarda topadi.

---

### 2. RDBMS — Relatsion ma'lumotlar bazasi modeli

**RDBMS (Relational Database Management System)** — ma'lumotlarni o'zaro bog'langan ikki o'lchovli jadvallar (relations) ko'rinishida saqlovchi va boshqaruvchi tizimdir.

Ushbu model 1970-yilda IBM olimi **Edgar Codd** tomonidan taklif qilingan.

**Jadvalning asosiy elementlari:**
- **Jadval (Table / Relation):** Bitta mavzuga oid ma'lumotlar to'plami (masalan, `customers`, `orders`).
- **Satr (Row / Record / Tuple):** Aniq bitta obyekt haqidagi ma'lumot (masalan, 1-mijoz Alining barcha ma'lumotlari).
- **Ustun (Column / Field / Attribute):** Obyektning aniq bir xususiyati (masalan, `ism`, `telefon`, `balans`).

**Eng mashhur RDBMS tizimlari:**
- **PostgreSQL:** Dunyodagi eng kuchli, kengaytiriladigan ochiq kodli RDBMS.
- **MySQL:** Veb-saytlar va internet-loyihalarda eng keng tarqalgan RDBMS.
- **SQLite:** Server talab qilmaydigan, bitta faylda saqlanuvchi ixcham RDBMS (Python bilan birga keladi).
- **Oracle / MS SQL Server:** Yirik korporativ va bank tizimlari uchun pullik tizimlar.

---

### 3. Kalitlar va Relyatsion bog'lanishlar

Relatsion bazaning eng muhim kuchi — bu **jadvallar o'rtasidagi bog'lanishlar**dir:

1. **Primary Key (PK — Birlamchi kalit):**
   - Jadvaldagi har bir satrni unikal identifikatsiya qiluvchi ustun.
   - **Qoidasi:** Hech qachon takrorlanmasligi (`UNIQUE`) va bo'sh bo'lmasligi (`NOT NULL`) shart! (Masalan, `customer_id`, pasport seriyasi, INN).

2. **Foreign Key (FK — Tashqi kalit):**
   - Boshqa jadvaldagi Primary Key ustuniga havola qiluvchi ustun.
   - Jadvallarni o'zaro bog'laydi va **relyatsion yaxlitlikni (Referential Integrity)** ta'minlaydi (Mavjud bo'lmagan mijoz nomiga buyurtma ochib bo'lmaydi!).

**Rasmiy o'quv dasturidagi klassik bog'lanish zanjiri:**
- `customers.customer_id (PK) ──→ orders.customer_id (FK)`
  *(Bitta mijoz bir nechta buyurtma berishi mumkin: 1-to-Many)*
- `products.product_id (PK) ──→ order_items.product_id (FK)`
  *(Bitta mahsulot bir nechta buyurtmada qatnashishi mumkin)*

---

### 4. ACID tamoyillari

RDBMS ishonchliligining 4 ta ustuni:

- **A — Atomicity (Bo'linmaslik):** Tranzaksiya yo to'liq bajariladi, yo umuman bajarilmaydi.
  *Misol:* Alining kartasidan 100 000 so'm yechildi, lekin Valining kartasiga o'tayotganda svet o'chib qoldi. Tizim avtomatik orqaga qaytadi (ROLLBACK) va Alining puli joyiga qaytadi.
- **C — Consistency (Muvofiqlik / Yaxlitlik):** Baza barcha qoidalarga (`NOT NULL`, balans musbat bo'lishi) mos kelgandagina o'zgarishni qabul qiladi.
- **I — Isolation (Izolyatsiya):** Bir vaqtda bajarilayotgan parallel tranzaksiyalar bir-biriga xalaqit bermaydi.
- **D — Durability (Bardoshlilik):** Agar operatsiya muvaffaqiyatli yakunlansa (COMMIT), server o'chib qolsa ham ma'lumot diskda saqlanib qoladi.

---

### 5. R-Diagram (Entity-Relationship Model — ERD)

Jadval yaratishdan oldin uning modeli chiziladi:
- **Entity (Obyekt):** Ma'lumot to'planadigan narsa (Mijoz, Buyurtma, Mahsulot).
- **Attribute (Xususiyat):** Obyektning ustunlari (Ismi, Narxi).
- **Relationship (Munosabat):**
  - **1:1 (Birga-bir):** Bitta o'quvchiga bitta pasport;
  - **1:N (Birga-ko'p):** Bitta maktabda ko'p o'quvchi;
  - **M:N (Ko'pga-ko'p):** Bitta o'quvchi ko'p to'garakka qatnashadi, bitta to'garakda ko'p o'quvchi bor.

---

## Kod namunalari

### 1-namuna: Python `sqlite3` yordamida relyatsion baza yaratish

```python
import sqlite3

# 1. Baza bilan ulanish hosil qilamiz (fayl ko'rinishida)
conn = sqlite3.connect('data/maktab_tizimi.db')
cursor = conn.cursor()

# Xorijiy kalitlar tekshiruvini faollashtiramiz
cursor.execute("PRAGMA foreign_keys = ON;")

# 2. Customers (Mijozlar) jadvali yaratamiz
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism TEXT NOT NULL,
    telefon TEXT UNIQUE NOT NULL,
    shahar TEXT DEFAULT 'Toshkent'
);
''')

# 3. Orders (Buyurtmalar) jadvali yaratamiz (Foreign Key bog'lanishi bilan)
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    summa REAL NOT NULL,
    buyurtma_sana TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
''')

conn.commit()
print("Jadvallar muvaffaqiyatli yaratildi!")
```

### 2-namuna: Ma'lumot kiritish va `INNER JOIN` so'rovi

```python
# 1. Mijozlarni kiritamiz
cursor.execute("INSERT OR IGNORE INTO customers (customer_id, ism, telefon) VALUES (1, 'Aliyev Ali', '+998901112233');")
cursor.execute("INSERT OR IGNORE INTO customers (customer_id, ism, telefon) VALUES (2, 'Valiyev Vali', '+998904445566');")

# 2. Buyurtmalarni kiritamiz (customer_id bog'lanishi bilan)
cursor.execute("INSERT INTO orders (customer_id, summa, buyurtma_sana) VALUES (1, 150000, '2026-10-04');")
cursor.execute("INSERT INTO orders (customer_id, summa, buyurtma_sana) VALUES (1, 85000, '2026-10-05');")
cursor.execute("INSERT INTO orders (customer_id, summa, buyurtma_sana) VALUES (2, 420000, '2026-10-05');")

conn.commit()

# 3. Relyatsion bog'lanish orqali ma'lumotlarni o'qiymiz (INNER JOIN)
cursor.execute('''
SELECT 
    orders.order_id,
    customers.ism,
    customers.telefon,
    orders.summa,
    orders.buyurtma_sana
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;
''')

natijalar = cursor.fetchall()

print("\n--- Buyurtmalar va Mijozlar (JOIN) ---")
for qator in natijalar:
    print(f"Buyurtma #{qator[0]} | Mijoz: {qator[1]} ({qator[2]}) | Summa: {qator[3]:,} so'm | Sana: {qator[4]}")

conn.close()
```

---

## Amaliy topshiriqlar

### 1-topshiriq: PK va FK mantiqiy bog'lanishini topish (Oson)
Maktab platformasi uchun 2 ta jadval berilgan:
- `maktablar (maktab_id, maktab_nomi, viloyat)`
- `sinflar (sinf_id, maktab_id, sinf_nomi, xona_raqami)`
Ushbu jadvallarda qaysi ustunlar Primary Key, qaysi biri esa Foreign Key ekanligini aniqlang va ular qanday munosabatda (1:1, 1:N yoki M:N) ekanligini tushuntiring.

**Kutiladigan natija:** `maktab_id` maktablarda PK, sinflarda FK ekanligi va munosabat 1:N (Bitta maktabda ko'p sinflar) ekanligi ko'rsatiladi.  
**Yechim:**  
`maktablar` jadvalida `maktab_id` — Primary Key (unikal).  
`sinflar` jadvalida `sinf_id` — Primary Key, `maktab_id` esa — Foreign Key.  
Munosabat: 1:N (Bir-ko'p), chunki bitta maktabda bir nechta sinf bo'ladi, lekin bitta sinf faqat bitta maktabga tegishli bo'lishi mumkin.

---

### 2-topshiriq: Relyatsion yaxlitlik xatosini tahlil qilish (O'rta)
Agar quyidagi so'rov ishga tushirilsa:
```sql
INSERT INTO orders (customer_id, summa, buyurtma_sana) VALUES (999, 50000, '2026-10-04');
```
Agarda `customers` jadvalida `customer_id = 999` bo'lgan mijoz mavjud bo'lmasa, RDBMS qanday munosabat bildiradi? Nega CSV faylda bunday xatolik sezilmay qolishi mumkin?

**Kutiladigan natija:** RDBMS `IntegrityError: FOREIGN KEY constraint failed` xatosini qaytaradi.  
**Yechim:**  
RDBMS relyatsion yaxlitlikni (Referential Integrity) qat'iy nazorat qiladi va mavjud bo'lmagan mijozga buyurtma ochishga ruxsat bermaydi. CSV faylda esa hech qanday aloqa tekshiruvi yo'q — unga xohlagan sonni yozib qo'yish mumkin, natijada ma'lumotlar ifloslanadi va «yetim yozuvlar» (orphan records) paydo bo'ladi.

---

### 3-topshiriq: Mahsulotlar va buyurtmalar ERD loyihasi (Qiyin)
Internet do'kon uchun 3 ta jadvaldan iborat model yarating:
1. `products (product_id, nom, narx, zaxira)`
2. `customers (customer_id, ism, email)`
3. `orders (order_id, customer_id, product_id, miqdor, jami_summa)`
Python `sqlite3` da ushbu jadvallarni barcha PK va FK cheklovlari bilan yarating, ma'lumot kiriting va umumiy hisobotni `JOIN` orqali chiqaring.

**Kutiladigan natija:** 3 ta jadval bog'lanadi va muvaffaqiyatli so'rov olinadi.  
**Yechim:**  
```python
import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON;")

c.execute("CREATE TABLE products (product_id INT PRIMARY KEY, nom TEXT, narx REAL);")
c.execute("CREATE TABLE customers (customer_id INT PRIMARY KEY, ism TEXT);")
c.execute("""
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    miqdor INT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);
""")

c.execute("INSERT INTO products VALUES (1, 'Noutbuk', 8000000);")
c.execute("INSERT INTO customers VALUES (101, 'Sherzod');")
c.execute("INSERT INTO orders VALUES (5001, 101, 1, 2);")

c.execute("""
SELECT o.order_id, c.ism, p.nom, o.miqdor, (o.miqdor * p.narx) as jami
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id;
""")
print(c.fetchall())
conn.close()
```

---

## Tezkor nazorat savollari

1. Primary Key ning 2 ta asosiy sharti qanday?  
   *Javob:* Unikal bo'lishi (`UNIQUE`) va bo'sh qiymat (`NULL`) qabul qilmasligi shart.
2. ACID tamoyillarida "A" (Atomicity) nimani anglatadi?  
   *Javob:* Tranzaksiya yo to'liq 100% bajariladi, yoki zarracha xato bo'lsa umuman bajarilmay, barcha o'zgarishlar bekor qilinadi.
3. Foreign Key nima uchun kerak?  
   *Javob:* Boshqa jadvaldagi Primary Key bilan munosabat o'rnatish va relyatsion yaxlitlikni ta'minlash uchun.
4. Edgar Codd kim va u axborot texnologiyalariga qanday hissa qo'shgan?  
   *Javob:* 1970-yilda relatsion ma'lumotlar bazasi (RDBMS) nazariy asoslarini yaratgan olim.

---

## Uyga vazifa

1. O'zingiz bilgan kutubxona yoki poliklinika tizimi uchun kamida 3 ta jadvaldan iborat relyatsion model (ER-diagramma) chizing.
2. Unda qaysi ustunlar Primary Key, qaysilari Foreign Key ekanligini belgilang.
3. Python `sqlite3` orqali ushbu jadvallarni yaratib, har biriga kamida 2 tadan namunaviy yozuv kiriting.
