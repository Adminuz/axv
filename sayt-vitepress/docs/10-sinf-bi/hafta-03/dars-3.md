---
title: "9-dars. 9-dars: SQL analitik operatorlari: SELECT, WHERE, ORDER BY, LIMIT asoslari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 3, "link": "/10-sinf-bi/hafta-03/"}, "g": 9, "title": "9-dars: SQL analitik operatorlari: SELECT, WHERE, ORDER BY, LIMIT asoslari", "lead": "Ma'lumotlar bazasi — bu ulkan kutubxona. SELECT, WHERE, ORDER BY va LIMIT operatorlari esa shu kutubxonaning to'g'ri kitobni topib beradigan aqlli kutubxonachisidir. Ushbu darsda biz O'zbekiston ta'limi statistikasini SQL orqali tahlil qilishni o'rganamiz: eng ko'p o'quvchisi bo'lgan viloyatlarni topish, diapazonli filtrlash va TOP-N reytinglar chiqarish.", "slide": "/slaydlar/10-sinf-bi/hafta-03/dars-3.html", "test": "/slaydlar/10-sinf-bi/hafta-03/dars-3-test.html", "tabs": [{"g": 7, "link": "/10-sinf-bi/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/10-sinf-bi/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/10-sinf-bi/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "8-dars: R-diagrammalar (ERD) loyihalash va SQLite bilan ishlash", "link": "/10-sinf-bi/hafta-03/dars-2"}, "next": null}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **SQL guruhlar:** DDL (jadval yaratish: CREATE), DML (ma'lumot qo'shish: INSERT, UPDATE, DELETE) va DQL (ma'lumot olish: SELECT) — biz DQL ga e'tibor qaratamiz.
- **SELECT:** Relyatsion jadvaldan kerakli ustunlarni tanlash operatori. `*` belgisi barcha ustunlarni, aniq nom esa faqat o'sha ustunni qaytaradi.
- **AS alias (taxallus):** Ustun yoki hisoblangan qiymatga yangi ixcham nom berish: `ROUND(a/b, 2) AS nisbat`.
- **SQL so'rovining mantiqiy ijro tartibi:** `FROM` → `WHERE` → `SELECT` → `ORDER BY` → `LIMIT`.
- **WHERE filtri:**
  - Solishtirish: `=`, `!=`, `>`, `<`, `>=`, `<=`
  - Mantiqiy: `AND`, `OR`, `NOT`
  - Diapazon: `BETWEEN 2020 AND 2024` (chegaralar kiritilgan)
  - Ro'yxat: `IN (1, 2, 3)`
  - Matn shablon: `LIKE 'Toshkent%'` (`%` — ixtiyoriy belgilar, `_` — aynan 1 belgi)
  - Bo'sh qiymat: `IS NULL` va `IS NOT NULL` (`= NULL` ishlamaydi!)
- **ORDER BY:** Natijalarni bir yoki bir nechta ustun bo'yicha `ASC` (o'sish) yoki `DESC` (kamayish) tartibida saralash.
- **LIMIT va OFFSET (Sahifalash / TOP-N):**
  - `LIMIT N`: Faqat N ta yozuvni chiqaradi;
  - `LIMIT N OFFSET K`: K ta yozuvni tashlab, N tadan chiqaradi.
  - N-sahifa formulasi: `LIMIT sahifa_hajmi OFFSET (sahifa_raqami - 1) * sahifa_hajmi`.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega `= NULL` ishlamaydi?
SQL mantiqida `NULL` — bu "noma'lum" qiymat hisoblanadi. Matematik qonun bo'yicha `noma'lum = noma'lum` hamisha `FALSE` bo'lib qaytadi, chunki ikki noma'lumni taqqoslab bo'lmaydi. Shuning uchun `NULL` larni aniqlash uchun faqat `IS NULL` yoki `IS NOT NULL` konstruksiyasi ishlatiladi.

### 2. LIKE va katta-kichik harflar
SQLite da `LIKE` operatori ingliz harflari uchun katta-kichik harfga sezgir emas (`LIKE 'Toshkent%'` ham `'toshkent%'` ham ishlaydi). Ammo PostgreSQL da standart `LIKE` katta-kichik harfga sezgir, buning uchun `ILIKE` operatori ishlatiladi. Haqiqiy loyihalarda buni doimo hisobga olish kerak!

### 3. TOP-N tahlili nima uchun kerak?
Biznes amaliyotida doim bir nechta savollar paydo bo'ladi:
- Qaysi 5 ta hudud eng ko'p o'quvchiga ega?
- Qaysi 10 ta maktabda o'qituvchi yetishmovchiligi eng yuqori?
- Oxirgi 3 ta yillik ko'rsatkich eng yuqori qaysi viloyatlar?

`ORDER BY ... LIMIT` kombinatsiyasi ana shunday tahlillarni bir necha satr SQL kodida hal qiladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **DQL (Data Query Language)** | Ma'lumotlarni o'qish va olish uchun mo'ljallangan SQL buyruqlar guruhi |
| **SELECT** | Jadvaldan kerakli ustunlarni tanlash operatori |
| **AS** | Ustun yoki hisoblangan qiymatga taxallus (alias) berish kalit so'zi |
| **WHERE** | Qatorlarni mantiqiy shartlar asosida filtrovchi operatorn |
| **BETWEEN** | Ko'rsatilgan diapazondagi qiymatlarni qidiruv operatori (chegaralar kiradi) |
| **IN** | Ro'yxatdagi qiymatlardan biriga tengligi uchun qidiruv operatori |
| **LIKE** | Matnli shablon (`%`, `_`) orqali qidiruvchi operator |
| **IS NULL** | Ustundagi bo'sh qiymatlarni aniqlash operatori |
| **ORDER BY** | Natijani ko'rsatilgan ustun bo'yicha saralash buyrug'i |
| **LIMIT** | Natija qatorlarini son bilan chegaralovchi buyruq |
| **OFFSET** | Ko'rsatilgan sondagi dastlabki qatorlarni tashlab yuborib, qolganlarini chiqarish |
| **Pagination** | Katta natijani sahifalarga bo'lib chiqarish mexanizmi |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- **SQL 1974-yilda:** SQL tilini IBM kompaniyasining muhandislari Donald Chamberlin va Raymond Boyce 1974-yilda ishlab chiqqan. Dastlab u SEQUEL deb atagan (Structured English Query Language).
- **"O'quvchilar soni" yoki "count":** O'zbekistonda 2024-yilgi davlat statistikasiga ko'ra umumta'lim maktablarida 6,5 milliondan ortiq o'quvchi ta'lim olmoqda — SQL ORDER BY va LIMIT orqali shu sonni mintaqalar kesimida tahlil qilish mumkin.
- **Google, Meta, Amazon:** Dunyodagi eng yirik IT kompaniyalarida kundalik ishda yozilayotgan SQL so'rovlarining aksariyati aynan `SELECT ... WHERE ... ORDER BY ... LIMIT` tuzilmasiga tayanadi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. SELECT va barcha ustunlar <Badge type="tip" text="oson" />
`yillik_kpi` jadvalidagi barcha ustunlarni (jami, yillik KPI yozuvlarini) konsolga chiqaring. Avval `SELECT *` orqali, so'ngra faqat `hudud_id`, `yil`, `oquvchilar_soni` ustunlarini tanlang va ikki so'rovni taqqoslang.  
**Kutiladigan natija:** `SELECT *` barcha ustunlarni, nomlovchi `SELECT` esa faqat tanlangan ustunlarni qaytaradi.

### 2. Arifmetik amallar va AS taxallus <Badge type="tip" text="oson" />
`yillik_kpi` dan hudud identifikatori, yili va maktabga to'g'ri keladigan o'rtacha o'quvchilar sonini (`oquvchilar_soni / maktablar_soni`) `maktab_yuklamasi` taxallusi bilan hisoblang. Natijani 1 ta kasr belgigacha yaxlitlang (`ROUND`).  
**Kutiladigan natija:** Hisoblangan ustun chiroyli nom bilan chiqariladi.

### 3. WHERE: solishtirish va AND <Badge type="tip" text="oson" />
Faqat 2024-yil uchun va o'quvchilar soni 300 000 dan ortiq bo'lgan hududlarni tanlang.  
**Kutiladigan natija:** Ikkita shart AND bilan birlashtiriladi.

### 4. BETWEEN bilan diapazonli filtr <Badge type="tip" text="oson" />
`yillik_kpi` dan 2022 dan 2024 yillar oralig'idagi (ikki chek kiradi) barcha yozuvlarni chiqaring.  
**Kutiladigan natija:** `WHERE yil BETWEEN 2022 AND 2024` qo'llaniladi.

### 5. IN operatori — ko'p hudud qidirish <Badge type="warning" text="o'rta" />
`yillik_kpi` dan `hudud_id` si 1, 3 yoki 5 ga teng bo'lgan 2024-yilgi yozuvlarni `IN` operatori yordamida chiqaring. Hudud nomlari ham chiqishi uchun `hududlar` jadvalini `INNER JOIN` bilan birlashtiring.  
**Kutiladigan natija:** `WHERE k.yil = 2024 AND k.hudud_id IN (1, 3, 5)` va JOIN birga qo'llaniladi.

### 6. LIKE bilan matn qidirish <Badge type="warning" text="o'rta" />
`hududlar` jadvalidan nomida "viloyati" so'zi qatnashgan barcha hududlarni toping. So'ng nomining oxirgi 2 harfi "ti" bilan tugagan hududlarni `LIKE '%ti'` orqali qidiring.  
**Kutiladigan natija:** Matn shablon qidiruvi natijasi ko'rsatiladi.

### 7. IS NULL tekshiruvi <Badge type="warning" text="o'rta" />
`maktablar` jadvaliga yangi maktab qo'shing, lekin `turi` ustunini ko'rsatmang (u `NULL` bo'lib qolsin). So'ngra `WHERE turi IS NULL` orqali shu yozuvni topib, konsolga chiqaring.  
**Kutiladigan natija:** `IS NULL` va `IS NOT NULL` operatorlarining farqi amalda ko'rsatiladi.

### 8. Ko'p ustunli ORDER BY <Badge type="warning" text="o'rta" />
`yillik_kpi` ni avval `yil DESC` (yangi yillar birinchi), so'ng `oquvchilar_soni DESC` (ko'proq o'quvchi birinchi) bo'yicha saralang. Ikki mezonli saralash qanday ishlashini tushuntiring.  
**Kutiladigan natija:** Ko'p ustunli saralash to'g'ri amalga oshiriladi.

### 9. TOP-5 ta resurs yuklamasi tahlili <Badge type="danger" text="qiyin" />
2024-yil uchun bitta maktabga o'rtacha to'g'ri keladigan o'quvchilar soni (`oquvchilar_soni / maktablar_soni`) bo'yicha TOP-5 ta yuklamali hududni aniqlang. Natijada hudud nomi, o'quvchilar soni va hisoblangan yuklama ko'rsatilsin.  
**Kutiladigan natija:** `ORDER BY ... DESC LIMIT 5` va JOIN birga ishlatiladi.

### 10. Sahifalash (Pagination) mexanizmi <Badge type="danger" text="qiyin" />
Barcha hududlarning 2024-yilgi statistikasini o'quvchilar soni bo'yicha kamayish tartibida saralab, sahifalash mexanizmini yarating: har sahifada 3 ta hudud ko'rsatilsin. 1-sahifa, 2-sahifa va 3-sahifani chiqaruvchi 3 ta alohida so'rov yozing.  
**Kutiladigan natija:** `LIMIT 3 OFFSET 0`, `LIMIT 3 OFFSET 3`, `LIMIT 3 OFFSET 6` qo'llaniladi.

### 11. Xatoni toping va tuzating <Badge type="danger" text="qiyin" />
Quyidagi SQL so'rovida xatolar mavjud:
```sql
SELECT nomi, oquvchilar_soni
FROM yillik_kpi, hududlar
WHERE hudud_id = NULL
AND yil = 2024
ORDERBY oquvchilar_soni DESC
LIMIT 10;
```
Qanday xatolar bor? Ularni to'liq to'g'rilab, ishchi so'rovga aylantiring.  
**Kutiladigan natija:** `IS NULL` o'rniga `= NULL`, `ORDERBY` yozuvi va JOIN yo'qligi xatosi topiladi va tuzatiladi.

### 12. Kompleks ta'lim monitoringi hisoboti <Badge type="info" text="bonus" />
`maktab.db` bazasiga 5 ta viloyat uchun 2022, 2023, 2024 yillar bo'yicha ma'lumotlar kiriting. So'ngra bitta SQL so'rovi yozing:
- Faqat o'quvchilar soni 400 000 dan ortiq bo'lgan va yili 2022 dan katta hududlarni oling;
- O'quvchi/o'qituvchi nisbatini `AS` taxallusi bilan hisoblang;
- Yil bo'yicha kamayish tartibida, nisbat bo'yicha kamayish tartibida saralaing;
- Natijaning faqat dastlabki 6 qatorini chiqaring.  
**Kutiladigan natija:** Bir necha WHERE sharti, arifmetika, JOIN, ORDER BY va LIMIT birgalikda ishlaydi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. SQL buyruqlarida `SELECT` va `WHERE` qaysi tartibda mantiqiy bajariladi?
2. `BETWEEN 10 AND 20` va `>= 10 AND <= 20` bir xil natija beradimi?
3. `LIKE 'A_or'` qanday so'zlarga mos keladi?
4. `IS NULL` o'rniga `= NULL` yozsak nima bo'ladi va nima uchun?
5. `ORDER BY yil DESC, oquvchilar_soni ASC` qanday ishlaydi?
6. 4-sahifada `LIMIT 10 OFFSET` qiymat qancha bo'lishi kerak?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. `maktab.db` bazasidagi barcha hududlar bo'yicha o'rtacha bitta maktabga to'g'ri kelgan o'quvchilar sonini hisoblang.
2. Yuklama 700 nafardan oshgan hududlarni `WHERE` orqali filtrlang va `ORDER BY` bilan kamayish tartibida saraling.
3. Natijaning TOP-3 ta hududini `LIMIT` orqali chiqaruvchi va `AS` bilan chiroyli taxalluslar berilgan Python skriptini yozing.

</div>

