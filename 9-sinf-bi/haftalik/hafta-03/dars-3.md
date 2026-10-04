# 9-dars. Relatsion ma’lumotlar bazalari va model tushunchasi (1-qism): Jadvallar, Primary Key, Foreign Key va munosabatlar

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga ma'lumotlar bazasi (Database) va DBMS tushunchasi, Edgar F. Codd tomonidan asos solingan relatsion model tamoyillari, jadval (Table), satr (Row/Tuple), ustun (Column/Attribute) elementlari, birlamchi kalit (Primary Key), tashqi kalit (Foreign Key), ma'lumotlar yaxlitligi (Data Integrity) hamda jadvallararo munosabatlar (1:1, 1:N, M:N) mohiyatini nazariy va amaliy jihatdan o'rgatish.
- **Kutiladigan natija:** O'quvchilar nima uchun Excel o'rniga relatsion bazalar kerakligini tushunadi; Primary Key va Foreign Key farqini ajrata oladi; ikkita jadval o'rtasidagi bog'liqlikni aniqlaydi va munosabat turini (One-to-Many, Many-to-Many) to'g'ri modelley oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (PivotTable va Excel xulosasi): 10 daqiqa
  - Yangi mavzu: Ma'lumotlar bazasi, DBMS va Relatsion model: 20 daqiqa
  - Primary Key, Foreign Key va Ma'lumotlar yaxlitligi: 25 daqiqa
  - Jadvallararo munosabatlar (1:1, 1:N, M:N) va model tuzish: 15 daqiqa
  - Mustahkamlash savollari va dars xulosasi: 10 daqiqa

---

## Mentor konspekti

### 1. Ma'lumotlar bazasi (Database) va DBMS tushunchasi
- **Ma'lumotlar bazasi (Database):** Ma'lumotlarni tartibli, tizimli, xavfsiz va bir-biriga bog'langan holda saqlashga mo'ljallangan maxsus elektron axborot omboridir.
- **DBMS (Database Management System / MBBT):** Ma'lumotlar bazasini yaratish, boshqarish, o'zgartirish, qidirish va xavfsizligini ta'minlovchi dasturiy ta'minot majmuasidir (masalan: PostgreSQL, MySQL, Microsoft SQL Server, Oracle).
- **Nega Excel yetarli emas?**
  1. *Hajm chegarasi:* Excel varag'i faqat 1 048 576 qatorni sig'dira oladi, DBMS esa milliardlab yozuvlarni boshqaradi.
  2. *Ko'p foydalanuvchi rejimi:* Bir vaqtning o'zida yuz minglab odamlar bazaga murojaat qilishi va xarid amalga oshirishi mumkin.
  3. *Ma'lumot yaxlitligi va xavfsizlik:* Ruxsatsiz o'zgartirishdan himoya va tranzaksion barqarorlik (ACID).

### 2. Edgar Codd va Relatsion model (Relational Model)
1970-yilda IBM olimi **Edgar F. Codd** tomonidan taklif qilingan. Markazida matematik to'plamlar nazariyasi (set theory) yotadi.
Asosiy tarkibiy elementlari:
1. **Table (Jadval / Relation):** Bir xil tuzilishga ega bo'lgan subyektlar to'plami (masalan, `Oquvchilar`, `Kurslar`, `Buyurtmalar`).
2. **Row (Satr / Tuple / Record):** Jadvaldagi bitta aniq obyektning individual namunasi (masalan, Ali ismli o'quvchi haqidagi ma'lumotlar satri).
3. **Column (Ustun / Attribute / Field):** Obyektning xususiyati yoki ko'rsatkichi (masalan, `StudentID`, `Ism`, `TugilganSana`, `Telefon`).

### 3. Primary Key (Birlamchi kalit)
Jadvaldagi har bir satrni **takrorlanmas va noyob (unique)** tarzda aniqlovchi ustun yoki ustunlar to'plami.
- **Xususiyatlari:**
  - Hech qachon bo'sh (`NULL`) bo'lishi mumkin emas.
  - Qiymati takrorlanmaydi (dublikat bo'lmaydi).
  - Jadvalda faqat 1 ta Primary Key bo'ladi.
- **Misol:** O'zbekiston fuqarosining JShShIR (PINFL) raqami, talabaning `StudentID`, tovarning `Barcode` kodi.

### 4. Foreign Key (Tashqi kalit) va Ma'lumotlar yaxlitligi
Boshqa jadvaldagi Primary Key ustuniga havola qiluvchi ustundir.
- Jadvallar o'rtasida mantiqiy ko'prik yaratadi.
- **Referential Integrity (Referensial yaxlitlik):** Foreign Key ustuniga faqat asosiy jadvalda mavjud bo'lgan ID'larni kiritish mumkin! Mavjud bo'lmagan talabaga baho qo'yib yoki mavjud bo'lmagan mijoz nomiga buyurtma yozib bo'lmaydi.

### 5. Jadvallararo munosabatlar (Relationships)
1. **One-to-One (1:1 / Birga-bir):** Asosiy jadvaldagi bitta yozuv ikkinchi jadvaldagi faqat bitta yozuvga mos keladi.
   - *Misol:* Bitta fuqaro $\leftrightarrow$ Bitta xorijga chiqish pasporti.
2. **One-to-Many (1:N / Birga-ko'p):** Asosiy jadvaldagi bitta yozuv ikkinchi jadvaldagi bir nechta yozuvga bog'lanishi mumkin.
   - *Misol:* Bitta mijoz $\leftrightarrow$ Ko'plab buyurtmalar; Bitta sinf $\leftrightarrow$ Ko'plab o'quvchilar.
3. **Many-to-Many (M:N / Ko'pga-ko'p):** Birinchi jadvaldagi bitta yozuv ikkinchisidagi ko'p yozuvga, va aksincha mos keladi.
   - *Misol:* Bitta o'quvchi bir nechta fanga qatnashadi, bitta fanda bir nechta o'quvchi o'qiydi.
   - *Amaliy yechim:* M:N munosabat relatsion bazalarda to'g'ridan-to'g'ri bog'lanmaydi; u oraliq bog'lovchi jadval (**Junction / Bridge table**) orqali ikkita 1:N munosabatga ajratiladi!

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Primary Key aniqlash (oson)
Maktab kutubxonasi uchun kitoblar jadvali loyihalanmoqda. Quyidagi ustunlardan qaysi biri eng yaxshi Primary Key bo'la oladi va nima uchun?
Ustunlar: `KitobNomi`, `Muallif`, `ISBN_Kodi`, `NashrYili`, `SahifalarSoni`.

**Yechim:**
`ISBN_Kodi` (International Standard Book Number).
Chunki kitob nomi va muallifi bir xil bo'lishi mumkin (turli nashriyotlar chop etgan bo'lishi mumkin), nashr yili va sahifalar soni esa ko'plab kitoblarda aynan bir xil bo'ladi. Dunyoda har bir rasmiy kitob nashriga faqat bitta takrorlanmas unikal ISBN kodi beriladi. Shuningdek, sun'iy avtomatik raqamlanuvchi `BookID` ustunini ham Primary Key qilish mumkin.

### 2-topshiriq. 1:N munosabat va Foreign Key joylashtirish (o'rta)
Kompaniyada `Kafedralar` (Departments) va `Xodimlar` (Employees) jadvallari mavjud. Bitta kafedrada ko'plab xodimlar ishlaydi, har bir xodim faqat bitta kafedraga tegishli.
Ushbu jadvallarning tuzilmasini chizing va Foreign Key qaysi jadvalga qo'yilishini tushuntiring.

**Yechim:**
1. `Kafedralar` jadvali (Parent/Asosiy jadval):
   - `KafedraID` (Primary Key)
   - `KafedraNomi`
2. `Xodimlar` jadvali (Child/Bo'ysunuvchi jadval):
   - `XodimID` (Primary Key)
   - `Ism`
   - `Lavozim`
   - `KafedraID` (Foreign Key $\to$ Kafedralar.KafedraID ga bog'lanadi).
*Qoida:* 1:N munosabatda Foreign Key har doim "Ko'p" (Many) tomonidagi jadvalga joylashtiriladi.

### 3-topshiriq. Ko'pga-ko'p (M:N) munosabatni loyihalash (qiyin)
Onlayn do'konda `Buyurtmalar` (Orders) va `Mahsulotlar` (Products) o'rtasidagi munosabatni tasavvur qiling. Bitta buyurtmada bir nechta mahsulot bo'lishi mumkin, bitta mahsulot bir nechta buyurtmada sotilishi mumkin.
Ushbu Many-to-Many munosabatni relatsion model talablariga mos ravishda oraliq jadval yordamida loyihalang.

**Yechim:**
To'g'ridan-to'g'ri M:N bog'lab bo'lmaydi. Shuning uchun uchinchi oraliq jadval — `BuyurtmaTafsilotlari` (`OrderDetails` yoki `OrderItems`) yaratiladi:
1. `Buyurtmalar`: `OrderID` (PK), `Sana`, `MijozID`
2. `Mahsulotlar`: `ProductID` (PK), `MahsulotNomi`, `Narx`
3. `BuyurtmaTafsilotlari` (Junction Table):
   - `DetailID` (PK)
   - `OrderID` (FK $\to$ Buyurtmalar)
   - `ProductID` (FK $\to$ Mahsulotlar)
   - `Miqdor` (Sotib olingan tovarlar soni)
   - `Narx` (Aynan o'sha vaqtdagi sotuv narxi)
Natijada bitta M:N munosabat ikkita One-to-Many (1:N) munosabatga aylandi!

---

## Tezkor nazorat savollari

1. Jadvalda nechta Primary Key ustuni bo'lishi mumkin?
   - *Javob:* Faqat bitta (ammo u bir nechta ustunning birikmasidan iborat kompozit kalit bo'lishi ham mumkin).
2. Primary Key NULL (bo'sh) qiymat qabul qila oladimi?
   - *Javob:* Yo'q, Primary Key hech qachon NULL bo'lishi mumkin emas.
3. Foreign Key asosiy jadvalda mavjud bo'lmagan ID qiymatini qabul qilsa nima sodir bo'ladi?
   - *Javob:* Referensial yaxlitlik (Data Integrity) qoidasi buziladi va DBMS xatolik berib, yozuvni qo'shishni rad etadi.
4. Many-to-Many (M:N) munosabat amalda qanday amalga oshiriladi?
   - *Javob:* Oraliq ko'prik jadvali (Junction table) yordamida ikkita 1:N munosabatga ajratish orqali.

---

## Uyga vazifa

O'zingiz qiziqqan soha bo'yicha (masalan, Futbol chempionati, Shifoxona yoki Avtomobil ijarasi xizmati) kamida 3 ta bir-biri bilan bog'langan jadval sxemasini daftaringizda chizing.
Har bir jadval uchun:
- Jadval nomi va kamida 4 ta ustunini belgilang;
- Primary Key (PK) ustunini aniqlang;
- Foreign Key (FK) orqali jadvallarni bir-biriga bog'lang va munosabat turini (1:N yoki M:N) yozing.
