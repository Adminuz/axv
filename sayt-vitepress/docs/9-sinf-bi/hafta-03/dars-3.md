---
title: "9-dars. Relatsion ma’lumotlar bazalari va model tushunchasi (1-qism): Jadvallar, Primary Key, Foreign Key va munosabatlar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (BI)", "link": "/9-sinf-bi/"}, "week": {"n": 3, "link": "/9-sinf-bi/hafta-03/"}, "g": 9, "title": "Relatsion ma’lumotlar bazalari va model tushunchasi (1-qism): Jadvallar, Primary Key, Foreign Key va munosabatlar", "lead": "Dunyodagi barcha yirik axborot tizimlarining poydevori: ma'lumotlarni o'zaro bog'langan qat'iy jadvallar tizimida saqlash va boshqarish san'ati!", "slide": "/slaydlar/9-sinf-bi/hafta-03/dars-3.html", "tabs": [{"g": 7, "link": "/9-sinf-bi/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/9-sinf-bi/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf-bi/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi", "link": "/9-sinf-bi/hafta-03/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Ma'lumotlar bazasi (Database)** — bu ma'lumotlarni tartibli, tizimli, xavfsiz va boshqaruv imkoniyatiga ega bo'lgan holda saqlashga mo'ljallangan axborot omboridir.
- **DBMS / MBBT (Database Management System)** — ma'lumotlar bazasini yaratish, boshqarish, o'zgartirish va xavfsizligini ta'minlovchi dasturiy vositadir (PostgreSQL, MySQL, Microsoft SQL Server, Oracle).
- **Relatsion model (Relational Model)** — 1970-yilda Edgar F. Codd tomonidan ishlab chiqilgan bo'lib, ma'lumotlarni jadvallar (relations) ko'rinishida ifodalaydi.
- **Relatsion modelning 3 asosiy elementi:**
  1. **Table (Jadval / Relation):** Bitta ob'ektga (masalan, Talabalar, Tovar) tegishli ma'lumotlar jamlanmasi.
  2. **Row (Satr / Tuple / Record):** Ob'ektning bitta aniq namunasi (bitta talaba).
  3. **Column (Ustun / Attribute / Field):** Ob'ektning xususiyati yoki ko'rsatkichi (`Ism`, `Yoshi`, `Telefon`).
- **Primary Key (Birlamchi kalit / PK):** Jadvaldagi har bir satrni takrorlanmas tarzda noyob aniqlovchi ustun. Hech qachon bo'sh (`NULL`) bo'lishi va takrorlanishi mumkin emas.
- **Foreign Key (Tashqi kalit / FK):** Boshqa jadvaldagi Primary Key ustuniga murojaat qiluvchi va jadvallar o'rtasida mantiqiy bog'lanish yaratuvchi ustundir.
- **Referensial yaxlitlik (Referential Integrity):** Tashqi kalit qiymati faqat asosiy jadvaldagi mavjud bo'lgan Primary Key qiymatlariga teng bo'lishi mumkin. Bu mavjud bo'lmagan xaridorga buyurtma rasmiylashtirish kabi xatolarning oldini oladi.
- **Jadvallararo munosabat turlari:**
  - **1:1 (Birga-bir):** Bitta fuqaroga faqat bitta xorijiy pasport.
  - **1:N (Birga-ko'p):** Bitta sinfda ko'plab o'quvchilar, bitta o'quvchi faqat bitta sinfga tegishli.
  - **M:N (Ko'pga-ko'p):** Bitta o'quvchi bir nechta to'garakka qatnashadi, bitta to'garakda ko'plab o'quvchilar o'qiydi (oraliq ko'prik jadvali orqali tuziladi).

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega Excel o'rniga Ma'lumotlar Bazasi kerak?
Excel ajoyib jadval dasturi bo'lsa-da, katta biznes tizimlari uchun uning imkoniyatlari cheklangan:
- **Hajm chegarasi:** Excel bitta varaqda maksimal 1 048 576 qatorni qabul qiladi. Millionlab tranzaksiyalarga ega bank yoki onlayn-do'kon uchun bu juda oz. RDBMS esa milliardlab qatorlar ustida sekundlarda ishlaydi.
- **Ko'p foydalanuvchili ishlash:** Excel faylida bir vaqtning o'zida yuzlab odam bir xil katakni o'zgartirsa chalkashlik yuzaga keladi. DBMS esa bir vaqtning o'zida millionlab so'rovlarni xavfsiz navbatga qo'yadi.
- **Qat'iy yaxlitlik qoidalari:** Excelda ixtiyoriy foydalanuvchi tasodifan formulani o'chirib yuborishi yoki matn o'rniga son yozib qo'yishi mumkin. DBMS esa qat'iy qoidalar (Constraints) bilan ma'lumot buzilishini taqiqlaydi.

### 2. Primary Key turlari: Tabiiy va Sun'iy kalitlar
- **Natural Key (Tabiiy kalit):** Haqiqiy hayotdan olingan noyob ma'lumot (masalan, pasport seriyasi, avtomobil VIN raqami, ISBN kodi).
- **Surrogate Key (Sun'iy kalit):** Baza tomonidan avtomatik ravishda ketma-ket generatsiya qilinadigan tartib raqam (`ID`, `1, 2, 3...`). Amaliyotda ko'pincha sun'iy kalitlar afzal ko'riladi, chunki inson ma'lumotlari (familiya, pasport) vaqt o'tib o'zgarishi mumkin, ammo ichki tizim ID'si hech qachon o'zgarmasligi lozim.

### 3. Ko'pga-ko'p (M:N) munosabat siri: Junction Table
Ko'pga-ko'p munosabatni ikkita jadval o'rtasida to'g'ridan-to'g'ri bog'lash ma'lumotlar takrorlanishiga olib keladi.
Shu sababli relatsion bazalarda uchinchi **Junction Table** (ko'prik jadval) ochiladi:
Masalan: `Talabalar` $\leftrightarrow$ `TalabaKurslari` $\leftrightarrow$ `Kurslar`.
Ko'prik jadval har ikkala jadvalning Primary Key ustunlarini Foreign Key sifatida o'zida saqlaydi va bitta murakkab M:N aloqani ikkita sodda 1:N aloqaga ajratib beradi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Database (Ma'lumotlar bazasi)** | Ma'lumotlarni tartibli, tuzilgan va xavfsiz saqlovchi elektron tizim. |
| **DBMS / MBBT** | Ma'lumotlar bazasini boshqarish tizimi (dasturiy ta'minot). |
| **RDBMS** | Relatsion ma'lumotlar bazasini boshqarish tizimi (PostgreSQL, MySQL, SQL Server). |
| **Relational Model** | Edgar Codd tomonidan yaratilgan, ma'lumotlarni jadvallar orqali ifodalovchi model. |
| **Table (Jadval / Relation)** | Ma'lum bir subyektga oid satrlar va ustunlardan iborat tuzilma. |
| **Row (Satr / Tuple)** | Jadvaldagi bitta alohida yozuv (obyekt namunasi). |
| **Column (Ustun / Attribute)** | Yozuvning ma'lum bir xossasi yoki maydoni. |
| **Primary Key (PK)** | Jadvaldagi har bir satrni noyob aniqlovchi takrorlanmas kalit ustun. |
| **Foreign Key (FK)** | Boshqa jadvaldagi Primary Keyga havola qiluvchi bog'lovchi kalit ustun. |
| **Referential Integrity** | Tashqi kalit orqali bog'langan jadvallardagi ma'lumotlar uyg'unligi va to'g'riligi. |
| **Junction Table** | Many-to-Many munosabatini ikkita One-to-Many ga ajratuvchi oraliq ko'prik jadvali. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Relatsion model nazariyasini ishlab chiqqani uchun **Edgar F. Codd** 1981-yilda informatika sohasidagi eng nufuzli hisoblangan **Turing mukofoti** (Nobel mukofotining IT'dagi ekvivalenti) bilan taqdirlangan.
- Edgar Codd ushbu modelni taklif qilgan paytda IBM rahbariyati dastlab uni rad etgan, chunki ularning o'sha vaqtdagi ierarxik tizimlari yaxshi sotilayotgan edi.
- Dunyodagi barcha yirik banklar, aeroportlar, sog'liqni saqlash muassasalari va davlat ro'yxatlari aynan relatsion ma'lumotlar bazalariga tayanadi.
- Relatsion modelning asosi — Georg Cantor tomonidan 19-asrda kashf etilgan sof matematik **To'plamlar nazariyasi** (Set Theory) hisoblanadi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Primary Key tanlash <Badge type="tip" text="oson" />
Sinfdagi o'quvchilar ro'yxatida quyidagi ustunlar bor: `Ism`, `Familiya`, `TugilganYil`, `ID_Raqam`, `Shahar`. Ushbu ustunlardan qaysi biri eng maqbul Primary Key bo'ladi va nima uchun?
**Kutiladigan natija:** To'g'ri ustun tanlovi va unikal sababi yozilgan qisqa javob.

### 2. Table, Row, Column ajratish <Badge type="tip" text="oson" />
Maktab dars jadvali misolida:
a) Jadval (Entity) nima?
b) Satr (Tuple) nima?
c) Ustun (Attribute) nima?
Har biriga 1 tadan aniq misol keltiring.
**Kutiladigan natija:** 3 ta elementga mos tushuntirish va misollar.

### 3. Nima uchun Primary Key NULL bo'lolmaydi? <Badge type="tip" text="oson" />
Agar Primary Key katagiga bo'sh (NULL) qiymat kiritishga ruxsat berilsa, qanday mantiqiy muammo kelib chiqishini tushuntiring.
**Kutiladigan natija:** Identifikatsiya va noyoblikning buzilishi haqida mantiqiy xulosa.

### 4. 1:1 munosabatga misol topish <Badge type="tip" text="oson" />
Kundalik hayotimizdan (fuqarolik, ta'lim yoki texnologiya) 1:1 (Birga-bir) munosabatiga mos keladigan 2 ta real misol keltiring.
**Kutiladigan natija:** Har bir obyekt faqat bitta ikkinchi obyektga mos keluvchi 2 ta real juftlik.

### 5. Foreign Key vazifasini aniqlash <Badge type="warning" text="o'rta" />
`Talabalar` jadvali va `Guruhlar` jadvali berilgan.
a) Qaysi jadval asosiy (parent), qaysi biri bo'ysunuvchi (child)?
b) Foreign Key ustuni qaysi jadvalga qo'shiladi va u nimani ko'rsatadi?
**Kutiladigan natija:** Jadvallar bo'ysunishi va FK joylashuvi ko'rsatilgan sxema.

### 6. 1:N munosabat loyihalash <Badge type="warning" text="o'rta" />
Kutubxona tizimi uchun `Mualliflar` va `Kitoblar` jadvallarini tuzing. Bitta muallif bir nechta kitob yozishi mumkin, har bir kitob bitta muallifga tegishli deb hisoblang.
Har ikkala jadval ustunlarini va kalitlarini yozing.
**Kutiladigan natija:** MuallifID orqali bog'langan ikkita jadval loyihasi.

### 7. Referensial yaxlitlik xatosini aniqlash <Badge type="warning" text="o'rta" />
Kafedralar jadvalida faqat 3 ta kafedra bor: `101`, `102`, `103`.
Yangi xodim qo'shilayotganda uning `KafedraID` ustuniga adashib `999` kiritildi. RDBMS bu holatda nima qiladi va nega?
**Kutiladigan natija:** Referential Integrity xatoligi sababi va tizim reaksiyasi bayoni.

### 8. Many-to-Many (M:N) muammosini hal qilish <Badge type="danger" text="qiyin" />
Shifoxonada `Shifokorlar` va `Bemorlar` mavjud. Bitta shifokor ko'p bemorlarni ko'radi, bitta bemor bir nechta mutaxassis shifokor qabulida bo'ladi.
Ushbu munosabat uchun oraliq ko'prik jadvalini (`Qabullar` / `Appointments`) loyihalang va undagi ustunlarni belgilang.
**Kutiladigan natija:** 3 ta jadvaldan iborat relyatsion model sxemasi.

### 9. Composite Primary Key (Kompozit kalit) tushunchasi <Badge type="danger" text="qiyin" />
Ba'zan bitta ustun noyob bo'lmasligi mumkin. Masalan, musobaqa jadvalida `Yil` va `MusobaqaNomi` birgalikda noyoblikni ta'minlaydi. Ikkita ustun birlashib bitta Primary Key vazifasini bajarishi mumkinligini misol bilan tushuntiring.
**Kutiladigan natija:** Kompozit kalitning qanday ishlashi va qachon qo'llanilishi haqida tahlil.

### 10. Mini Relatsion Sxema (ER diagramma) loyihalash <Badge type="info" text="bonus" />
Onlayn ta'lim platformasi (masalan, Coursera yoki Udemy) uchun kamida 4 ta jadvaldan iborat relatsion sxema tuzing (`Foydalanuvchilar`, `Kurslar`, `Modullar`, `Xaridlar`). Har bir jadvalning Primary Key, Foreign Key ustunlarini va munosabat turlarini to'liq ifodalang.
**Kutiladigan natija:** O'zaro bog'langan 4 ta jadval arxitekturasi va munosabatlar xaritasi.

</div>

