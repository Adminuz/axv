---
title: "6-dars. 6-dars: Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 2, "link": "/10-sinf-bi/hafta-02/"}, "g": 6, "title": "6-dars: Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari", "lead": "Bugungi raqamli iqtisodiyot — bu milliardlab bog'langan ma'lumotlar oqimidir. Har bir bank o'tkazmasi, har bir xarid va har bir avtorizatsiya ortida ma'lumotlar bazasi va uning qat'iy qoidalari turadi. Ushbu darsda biz nima uchun fayllar davri o'tib, RDBMS (Relatsion ma'lumotlar bazalari) dunyoni boshqarayotganini, Edgar Codd kashfiyotini, ACID tamoyillarini hamda SQL qudratini o'rganamiz.", "slide": "/slaydlar/10-sinf-bi/hafta-02/dars-3.html", "test": "/slaydlar/10-sinf-bi/hafta-02/dars-3-test.html", "tabs": [{"g": 4, "link": "/10-sinf-bi/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/10-sinf-bi/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/10-sinf-bi/hafta-02/dars-3", "current": true}], "prev": {"g": 5, "title": "5-dars: Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash", "link": "/10-sinf-bi/hafta-02/dars-2"}, "next": null}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Ma'lumotlar bazasi (Database):** Shunchaki fayllar yig'indisi emas, balki ma'lumotlarni tartibli saqlash, parallel boshqarish va xavfsizligini kafolatlash tizimidir.
- **Fayllar (CSV/JSON) cheklovlari:** Concurrency (bir vaqtda yozishda file lock va konfliktlar), ma'lumotlar yaxlitligi tekshiruvining yo'qligi, tranzaksiyalar kafolatlanmasligi va xavfsizlik cheklovlari.
- **RDBMS (Relational Database Management System):** Ma'lumotlarni o'zaro mantiqiy bog'langan ikki o'lchovli jadvallar (relations) ko'rinishida tashkil etuvchi tizim (1970-yil, Edgar Codd).
- **Relyatsion model elementlari:** Jadval (Table / Relation), Satr (Row / Record / Tuple), Ustun (Column / Field / Attribute).
- **Primary Key (PK — Birlamchi kalit):** Jadvaldagi har bir satrni unikal identifikatsiya qiluvchi ustun. Asosiy sharti: `UNIQUE` (takrorlanmas) va `NOT NULL` (bo'sh bo'lmasligi).
- **Foreign Key (FK — Tashqi kalit):** Boshqa jadvalning Primary Key ustuniga havola qiluvchi ustun. U relyatsion yaxlitlikni (Referential Integrity) ta'minlaydi.
- **Klassik bog'lanishlar:** `customers.customer_id (PK) ──→ orders.customer_id (FK)` va `products.product_id (PK) ──→ orders.product_id (FK)`.
- **ACID tamoyillari:** Ishonchli tranzaksiyalarning 4 ta oltin ustuni — **A**tomicity (bo'linmaslik), **C**onsistency (muvofiqlik), **I**solation (izolyatsiya), **D**urability (bardoshlilik).
- **ERD (Entity-Relationship Diagram):** Baza jadvallari yaratilishidan oldin uning obyektlari, atributlari va munosabat turlarini (1:1, 1:N, M:N) vizual aks ettiruvchi loyiha.
- **SQLite:** Server talab qilmaydigan, bitta faylda ishlovchi ixcham RDBMS bo'lib, Python standart kutubxonasiga (`sqlite3`) kiritilgan.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega Edgar Codd relyatsion modeli inqilobiy bo'lgan?
1970-yilgacha ma'lumotlar iyerarxik (daraxtsimon) yoki tarmoq (network) ko'rinishidagi fayllarda saqlanardi. Agar siz ma'lumot qidirmoqchi bo'lsangiz, dasturchi diskning qaysi sektoridan qaysi ko'rsatkich (pointer) bo'ylab yurish kerakligini apparat darajasida kodlab chiqishi kerak edi. Edgar Codd ma'lumotlarni jadvallar (matematik to'plamlar nazariyasi) ko'rinishida tasvirlashni va ularga deklarativ so'rovlar (SQL) orqali murojaat qilishni taklif qildi: siz tizimga "qanday qilib diskdan qidirishni" emas, "aynan qanday natija kerakligini" aytasiz!

### 2. Orphan Records (Yetim yozuvlar) muammosi nima?
Faraz qiling, CSV faylda mijoz o'z akkauntini o'chirib yubordi. Ammo buyurtmalar faylida uning ID raqami bilan 10 ta buyurtma saqlanib qolaveradi. Keyinchalik hisobot tuzayotganda tizim bu buyurtmalar kimga tegishli ekanini topolmaydi — bular yetim yozuvlar deyiladi. RDBMS da esa Foreign Key mexanizmi buni bartaraf etadi: u yo ota yozuvni o'chirishga ruxsat bermaydi (`RESTRICT`), yoki o'chirilganda unga bog'liq buyurtmalarni ham avtomatik tozalaydi (`CASCADE`).

### 3. SQLite ning kuchi va chegarasi
SQLite dunyodagi eng ko'p o'rnatilgan ma'lumotlar bazasi hisoblanadi (har bir smartfon, iPhone/Android, brauzerlar va operatsion tizimlarda o'nlab SQLite bazalari yashiringan). U o'qish tezligi bo'yicha hatto gigant serverlardan ham tez ishlaydi, chunki tarmoq protokoli talab etilmaydi. Ammo uning yagona cheklovi: bazaga yozish vaqtida u butun bazani bitta jarayon uchun qulflaydi (database-level locking). Shuning uchun millionlab parallel foydalanuvchilar bir vaqtda yozadigan veb-saytlar uchun PostgreSQL yoki MySQL ishlatiladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Database (DB)** | Ma'lumotlarni saqlash, boshqarish va tezkor olish uchun mo'ljallangan tizimli tuzilma |
| **RDBMS** | Ma'lumotlarni relyatsion jadvallar ko'rinishida boshqaruvchi relyatsion tizim |
| **Table (Jadval / Relation)** | Aniq bir obyekt turiga oid satrlar va ustunlar to'plami |
| **Row (Satr / Record / Tuple)** | Jadvaldagi bitta mustaqil obyektga tegishli yozuv |
| **Column (Ustun / Field / Attribute)** | Obyektning bitta xususiyatini ifodalovchi vertikal kataklar zanjiri |
| **Primary Key (PK)** | Jadvaldagi har bir satrni yagona (unikal) aniqlovchi birlamchi kalit |
| **Foreign Key (FK)** | Boshqa jadvaldagi Primary Key ga ishora qiluvchi va jadvallarni bog'lovchi tashqi kalit |
| **Referential Integrity** | Bog'langan jadvallar o'rtasidagi ma'lumotlar uyg'unligi va qonuniyligi |
| **ACID** | Ishonchli tranzaksiyalarning 4 ta talabi (Atomicity, Consistency, Isolation, Durability) |
| **Transaction (Tranzaksiya)** | Baza bilan amalga oshiriladigan yaxlit va bo'linmas mantiqiy operatsiyalar to'plami |
| **ERD (Entity-Relationship Diagram)** | Ma'lumotlar bazasi arxitekturasi va munosabatlarini tasvirlovchi diagramma |
| **INNER JOIN** | Ikkita jadvalni umumiy kalit (PK = FK) bo'yicha birlashtirib ko'rsatuvchi SQL operatori |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- **Har bir smartfonda 50+ baza:** Siz hozir ishlatayotgan Android yoki iOS smartfoni ichida kontaktlar, SMS xabarlar, WhatsApp chatlari, fotosuratlar metadatasi va ilovalar sozlamalari yuzlab kichik `.sqlite` yoki `.db` ma'lumotlar bazalarida saqlanadi.
- **Edgar Codd mukofoti:** Relyatsion modelni yaratgani uchun Edgar Codd 1981-yilda informatika sohasidagi eng nufuzli hisoblangan Alan Turing mukofotiga sazovor bo'lgan.
- **ACID atamasi:** ACID qisqartmasi kimyodagi "kislota" (acid) so'zi bilan omonim bo'lib, 1983-yilda Andreas Reuter va Jim Gray tomonidan tranzaksiyalarning mustahkamligini eslatuvchi jarangdor so'z sifatida kiritilgan.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. CSV va RDBMS farqini tahlil qilish <Badge type="tip" text="oson" />
Katta supermarket kassa tizimida mijozlar xaridlarini CSV faylga yozish nima uchun xavfli ekanligini 3 ta sabab (parallel kirish, ma'lumotlar yaxlitligi, tranzaksiyalar) bilan tushuntiring.  
**Kutiladigan natija:** Faylli tizimlar va RDBMS tizimlarining tub farqlari bo'yicha tahliliy javob.

### 2. Primary Key shartlarini tekshirish <Badge type="tip" text="oson" />
Quyidagi jadval ustunlaridan qaysi biri Primary Key bo'lishga munosib ekanini aniqlang va sababini tushuntiring:
- O'quvchining ismi (`ism`)
- O'quvchining tug'ilgan yili (`yil`)
- O'quvchining shaxsiy identifikatsiya raqami (`jshshir` / `student_id`)
- O'quvchining telefon raqami (`telefon`)  
**Kutiladigan natija:** PK uchun qat'iy `UNIQUE` va `NOT NULL` talablariga mos ustun tanlanadi.

### 3. Bog'lanish turlarini aniqlash (1:1, 1:N, M:N) <Badge type="tip" text="oson" />
Quyidagi real hayotiy munosabatlar qaysi turga mansubligini aniqlang:
1. Haydovchi va Haydovchilik guvohnomasi
2. Shifokor va Bemorlar
3. Kitoblar va Mualliflar (bitta kitobni bir nechta muallif yozishi mumkin, bitta muallif bir nechta kitob yozishi mumkin)  
**Kutiladigan natija:** Har bir munosabat to'g'ri (1:1, 1:N, M:N) tasniflanadi.

### 4. SQLite ulanishini yaratish <Badge type="tip" text="oson" />
Python'dagi `sqlite3` moduli yordamida `data/maktab.db` nomli yangi fayl bazasini yarating, ulanish (connection) va kursor (cursor) obyektlarini oching hamda baza versiyasini (`SELECT sqlite_version();`) konsolga chiqaring.  
**Kutiladigan natija:** Baza fayli hosil bo'ladi va o'rnatilgan SQLite versiyasi chop etiladi.

### 5. Customers jadvalini yaratish <Badge type="warning" text="o'rta" />
SQLite bazasida `customers` jadvalini quyidagi ustunlar bilan yarating:
- `customer_id`: butun son, Primary Key, avtomatik ortuvchi (AUTOINCREMENT)
- `ism`: matn, bo'sh bo'lmasligi shart (`NOT NULL`)
- `telefon`: matn, takrorlanmas (`UNIQUE`)
- `balans`: haqiqiy son, odatiy qiymati 0.0 (`DEFAULT 0.0`)  
**Kutiladigan natija:** Jadval SQL DDL buyrug'i orqali muvaffaqiyatli barpo etiladi.

### 6. Foreign Key bilan bog'langan Orders jadvali <Badge type="warning" text="o'rta" />
Yuqoridagi `customers` jadvaliga bog'langan `orders` jadvalini yarating:
- `order_id`: butun son, Primary Key
- `customer_id`: butun son, Foreign Key (`customers.customer_id` ga havola)
- `mahsulot_nomi`: matn, `NOT NULL`
- `summa`: haqiqiy son, `NOT NULL`
- `sana`: matn (`TEXT`)  
SQLite'da `PRAGMA foreign_keys = ON;` buyrug'i nima uchun kerakligini amalda tekshiring.  
**Kutiladigan natija:** Tashqi kalitli bog'lanish to'g'ri shakllantiriladi.

### 7. Ma'lumot kiritish va tranzaksiya (COMMIT) <Badge type="warning" text="o'rta" />
`customers` jadvaliga 3 nafar mijoz, `orders` jadvaliga esa ushbu mijozlar ID lariga bog'langan 5 ta buyurtma ma'lumotlarini kiriting (`INSERT INTO`). O'zgarishlarni bazada saqlash uchun `conn.commit()` chaqirilishi shartligini unutmang.  
**Kutiladigan natija:** Har ikkala jadval ma'lumotlar bilan to'ldiriladi.

### 8. Relyatsion yaxlitlik (Integrity) xatosini sinash <Badge type="warning" text="o'rta" />
`orders` jadvaliga mavjud bo'lmagan mijoz ID si bilan (masalan, `customer_id = 9999`) yangi buyurtma kiritishga urinib ko'ring. Dastur qanday xatolik qaytarishini (`sqlite3.IntegrityError`) kuzating va konsolga xatolik xabarini chiqaring.  
**Kutiladigan natija:** RDBMS ning xorijiy kalit cheklovi buzilishiga yo'l qo'ymasligi isbotlanadi.

### 9. INNER JOIN orqali hisobot olish <Badge type="danger" text="qiyin" />
`orders` va `customers` jadvallarini `customer_id` orqali birlashtiruvchi (`INNER JOIN`) SQL so'rovi yozing. Natijada har bir buyurtmaning ID si, xaridorning ismi, uning telefoni, xarid qilingan mahsulot va buyurtma summasi bitta jadval ko'rinishida chiqsin.  
**Kutiladigan natija:** Ikkala jadvaldagi bog'langan yozuvlar yaxlit hisobot sifatida chop etiladi.

### 10. ACID tamoyillari bo'yicha ssenariy tahlili <Badge type="danger" text="qiyin" />
Quyidagi vaziyatda ACID ning aynan qaysi tamoyili buzilish xavfi ostida ekanligini aniqlang:
- Server to'satdan elektr ta'minotidan uzildi, lekin operatsion tizim tranzaksiya muvaffaqiyatli yakunlandi deb hisobot bergan edi. Elektr qaytganida bazada ma'lumotlar o'chib ketgan bo'lsa, qaysi tamoyil buzilgan?
- Bir vaqtda ikkita xaridor omborda oxirgi qolgan bitta telefonni sotib olish tugmasini bosdi va ikkalasiga ham tasdiq xabari ketdi. Qaysi tamoyil buzilgan?  
**Kutiladigan natija:** Durability va Isolation tamoyillarining mohiyati to'g'ri talqin qilinadi.

### 11. Xatoni toping va tuzating <Badge type="danger" text="qiyin" />
Quyidagi SQL jadval yaratish kodida sintaktik va mantiqiy xatolar mavjud:
```sql
CREATE TABLE orders (
    order_id PRIMARY KEY,
    customer_id INTEGER,
    summa REAL
    FOREIGN KEY customer_id REFERENCES customers(id)
)
```
Ushbu kodni to'liq to'g'rilab, ishchi holatga keltiring (vergullar, ma'lumot turlari va qavslar).  
**Kutiladigan natija:** Xatolarsiz ishlaydigan DDL so'rovi taqdim etiladi.

### 12. Kengaytirilgan ERD: Customers, Orders va Products <Badge type="info" text="bonus" />
Haqiqiy e-tijorat tizimi uchun 3 ta jadvaldan iborat model yarating:
1. `customers` (mijozlar)
2. `products` (mahsulotlar: `product_id`, `nom`, `narx`, `ombor_soni`)
3. `orders` (mijoz va mahsulotni bog'lovchi buyurtmalar: `order_id`, `customer_id`, `product_id`, `miqdor`, `jami_summa`, `sana`)
Python dasturi yozing: har bir jadvalni yarating, ma'lumotlar qo'shing va `customers`, `orders` hamda `products` jadvallarini bitta so'rovda 2 ta `JOIN` orqali birlashtirib, chiroyli sotuvlar hisobotini konsolga chiqaring!  
**Kutiladigan natija:** Uch tomonlama relyatsion bog'lanish va ikki bosqichli `JOIN` so'rovi to'liq amalga oshiriladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Nima uchun yirik axborot tizimlarida ma'lumotlarni CSV fayllarda saqlash xavfli va samarasiz hisoblanadi?
2. Primary Key va Foreign Key o'rtasidagi asosiy farq nimada? Ular bir-biri bilan qanday hamkorlik qiladi?
3. Relyatsion yaxlitlik (Referential Integrity) qoidasi nima va u ma'lumotlar bazasini nimalardan himoya qiladi?
4. ACID so'zining har bir harfi qanday ma'noni anglatadi? Har biriga qisqa misol keltiring.
5. 1:1, 1:N va M:N munosabat turlariga maktab hayotidan bittadan aniq misol keltiring.
6. SQL tili bilan fayllarni dasturlash (masalan, Python'da faylni qatorma-qator o'qish) o'rtasidagi deklarativlik farqi nimada?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. O'zingiz tanlagan soha (kutubxona, avtosalon, poliklinika yoki mehmonxona) uchun kamida 3 ta jadvaldan iborat relyatsion model (ER-diagramma) chizing.
2. Unda qaysi ustunlar Primary Key, qaysilari Foreign Key ekanligini aniq belgilang va ular orasidagi munosabatlarni ko'rsating.
3. Python `sqlite3` moduli yordamida ushbu jadvallarni barcha cheklovlar (`PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE`) bilan yarating, ularga kamida 2 tadan namunaviy yozuv kiriting va `INNER JOIN` orqali umumiy hisobot chiqaruvchi skript yozing.

</div>

