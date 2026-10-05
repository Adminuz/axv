---
title: "8-dars. 8-dars: R-diagrammalar (ERD) loyihalash va SQLite bilan ishlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 3, "link": "/10-sinf-bi/hafta-03/"}, "g": 8, "title": "8-dars: R-diagrammalar (ERD) loyihalash va SQLite bilan ishlash", "lead": "Yaxshi loyihalangan ma'lumotlar bazasi — mustahkam bino poydevoriga o'xshaydi. Agar poydevor egri bo'lsa, ustiga qancha go'zal bino qurmang, u ertami-kechmi qulaydi. Ushbu darsda biz murakkab tizimlarning arxitekturasini qog'ozda va ekranda ERD (Entity-Relationship Diagram) ko'rinishida modellashtirishni hamda O'zbekiston ta'limi bo'yicha «Maktab tahliliy platformasi»ning relyatsion poydevorini qurishni o'rganamiz.", "slide": "/slaydlar/10-sinf-bi/hafta-03/dars-2.html", "test": "/slaydlar/10-sinf-bi/hafta-03/dars-2-test.html", "tabs": [{"g": 7, "link": "/10-sinf-bi/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/10-sinf-bi/hafta-03/dars-2", "current": true}, {"g": 9, "link": "/10-sinf-bi/hafta-03/dars-3", "current": false}], "prev": {"g": 7, "title": "7-dars: Relyatsion jadvallar, Primary Key, Foreign Key va relyatsion yaxlitlik", "link": "/10-sinf-bi/hafta-03/dars-1"}, "next": {"g": 9, "title": "9-dars: SQL analitik operatorlari: SELECT, WHERE, ORDER BY, LIMIT asoslari", "link": "/10-sinf-bi/hafta-03/dars-3"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **ERD (Entity-Relationship Diagram):** Ma'lumotlar bazasida saqlanadigan obyektlar, ularning xususiyatlari va ular o'rtasidagi munosabatlarning vizual loyihasidir.
- **ERD ning 3 ta asosiy komponenti:**
  - **Entity (Obyekt):** Ma'lumot saqlanadigan mavzu yoki tushuncha (O'quvchi, Hudud, Maktab);
  - **Attribute (Atribut):** Obyektning o'ziga xos xususiyatlari va ustunlari (Ism, Shahar, Sig'im);
  - **Relationship (Munosabat):** Obyektlar o'rtasidagi mantiqiy bog'liqlik.
- **Kardinallik (Cardinality) turlari:**
  - **1:1 (Birga-bir):** Bitta ota yozuvga faqat bitta bola yozuv mos keladi (Fuqaro va Pasport);
  - **1:N (Birga-ko'p):** Bitta otaga ko'plab bolalar mos keladi (Bitta viloyatda ko'p maktablar);
  - **M:N (Ko'pga-ko'p):** Har ikkala tomondan ko'plab bog'lanishlar bo'lishi mumkin (O'quvchilar va To'garaklar).
- **Junction / Bridge Table (Oraliq jadval):** Relyatsion bazada M:N munosabatlarni to'g'ridan-to'g'ri yaratib bo'lmaydi. Oraliq jadval orqali M:N munosabat ikkita 1:N munosabatga ajratiladi.
- **Maktab tahliliy platformasi modeli:**
  - `hududlar` (Viloyatlar katalogi);
  - `maktablar` (Har bir hududga tegishli ta'lim muassasalari, 1:N);
  - `yillik_kpi` (Hududlarning yillar kesimidagi umumiy ko'rsatkichlari, `UNIQUE (hudud_id, yil)`).
- **SQLite:** Bitta ixcham `.db` faylida to'liq relyatsion imkoniyatlarni taqdim etuvchi serverless ma'lumotlar bazasi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Chen notatsiyasi va Crow's Foot (Qarg'a oyog'i) farqi
1976-yilda Piter Chen taklif qilgan ilk modelda obyektlar to'rtburchak, atributlar oval, munosabatlar esa romb ichida yozilgan. Zamonaviy sanoatda esa **Crow's Foot** notatsiyasi standartga aylangan: unda jadvallar to'g'ridan-to'g'ri ustunlari va kalitlari (PK, FK) bilan chiziladi, munosabat chizig'ining uchidagi uch ayri chiziq ("qarg'a oyog'i") "ko'p" (Many) tomonni bildiradi.

### 2. Junction jadvalga qo'shimcha atributlar qo'shish
Oraliq jadval (Junction table) faqat ikkita kalitni birlashtirish bilan cheklanmaydi! Masalan, `oquvchi_kurs` jadvaliga `yozilgan_sana`, `to'langan_summa`, `yakuniy_baho` kabi ayni shu bog'lanishning o'ziga xos yangi atributlarini qo'shish mumkin. Bu orqali ma'lumotlar modeli yanada boyiydi.

### 3. DBeaver orqali ERD ni avtomatik chizish
Dasturchilar ko'pincha murakkab bazalarning diagrammasini qo'lda chizib o'tirmaydi. DBeaver yoki DataGrip kabi zamonaviy dasturlarda ma'lumotlar bazasiga ulanib, sichqonchaning o'ng tugmasi orqali **"View Diagram" (ERD)** buyrug'i tanlansa, dastur mavjud Primary va Foreign Key lar asosida to'liq chiroyli grafik diagrammani bir necha soniyada o'zi chizib beradi!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **ERD** | Entity-Relationship Diagram — Obyektlar va ularning munosabatlari modeli |
| **Entity** | Ma'lumot to'planadigan real yoki mavhum obyekt (jadval) |
| **Attribute** | Obyektning xususiyati yoki ko'rsatkichi (ustun) |
| **Relationship** | Ikki yoki undan ortiq obyektlar orasidagi mantiqiy aloqa |
| **Cardinality** | Munosabatda qatnashayotgan obyektlar soniy ko'rsatkichi (1:1, 1:N, M:N) |
| **Crow's Foot** | Munosabatning "ko'p" tomonini ifodalovchi xalqaro grafik belgi |
| **Junction Table** | Ko'pga-ko'p (M:N) munosabatni ikkita 1:N ga ajratuvchi oraliq ko'prik jadval |
| **Maktab KPI** | Ta'lim tizimi samaradorligini o'lchovchi asosiy ko'rsatkichlar to'plami |
| **Redundancy** | Ma'lumotlarning bazada ortiqcha va keraksiz takrorlanishi |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- **Piter Chen ixtirosi:** ERD modelini 1976-yilda AQShlik olim Piter Chen taklif qilgan. Bugungi kunda dunyodagi har qanday yirik IT loyiha (bank tizimi, ijtimoiy tarmoq, sun'iy yo'ldosh boshqaruvi) kod yozishdan oldin aynan ERD chizishdan boshlanadi.
- **Dunyoning eng mashhur ERD lari:** Masalan, WordPress CMS tizimining bazasi bor-yo'g'i 12 ta jadvaldan iborat bo'lsa-da, dunyodagi barcha veb-saytlarning 40% dan ortig'iga xizmat qiladi!
- **SQLite nomi qayerdan kelgan?** SQLite ning asoschisi D. Richard Hipp uni AQSh harbiy-dengiz floti uchun kemalarda server o'rnatmasdan ma'lumotlarni saqlash maqsadida yaratgan. "Lite" so'zi tizimning juda yengil va mustaqilligini bildiradi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Kardinallikni aniqlash <Badge type="tip" text="oson" />
Quyidagi munosabatlar qaysi kardinallik turiga (1:1, 1:N, M:N) mansubligini aniqlang:
1. Shahar va uning Shahar hokimi
2. Bitta kinoteatr va unda namoyish etilayotgan filmlar
3. Aktyorlar va Filmlar (bitta aktyor ko'p filmda o'ynaydi, bitta filmda ko'p aktyor bor)  
**Kutiladigan natija:** Munosabatlar to'g'ri tasniflanadi.

### 2. Obyekt va atributlarni ajratish <Badge type="tip" text="oson" />
Avtomobil ijarasi xizmati uchun quyidagi tushunchalarni Obyekt (Entity) va Atribut (Attribute) guruhlariga ajrating:
- `Mijoz`, `Telefon raqami`, `Avtomobil`, `Davlat raqami`, `Kunlik ijara narxi`, `Ijara shartnomasi`.  
**Kutiladigan natija:** Obyektlar va ularning ustunlari aniq ajratiladi.

### 3. Maktab platformasi bazasini ochish <Badge type="tip" text="oson" />
Python `sqlite3` yordamida `data/maktab.db` bazasini oching, xorijiy kalitlar nazoratini yoqing (`PRAGMA foreign_keys = ON;`) va bazada mavjud jadvallar ro'yxatini (`SELECT name FROM sqlite_master WHERE type='table';`) konsolga chiqaring.  
**Kutiladigan natija:** Baza fayli bilan ulanish o'rnatiladi.

### 4. Hududlar jadvalini yaratish <Badge type="warning" text="o'rta" />
`hududlar` jadvalini quyidagi talablar asosida barpo qiling:
- `hudud_id`: Primary Key, AUTOINCREMENT
- `nomi`: TEXT, takrorlanmas (`UNIQUE`), `NOT NULL`
- `markaz`: TEXT, `NOT NULL`  
Jadvalga O'zbekistonning kamida 3 ta hududini (Toshkent, Samarqand, Farg'ona) kiriting.  
**Kutiladigan natija:** Jadval SQL orqali tuziladi va ma'lumotlar bilan to'ldiriladi.

### 5. 1:N bog'langan Maktablar jadvali <Badge type="warning" text="o'rta" />
`maktablar` jadvalini `hududlar` jadvaliga `FOREIGN KEY (hudud_id) REFERENCES hududlar(hudud_id)` orqali bog'lang. `maktab_raqam` va `hudud_id` birikmasi takrorlanmasligi uchun `UNIQUE (hudud_id, maktab_raqam)` cheklovini qo'ying. Har bir hududga 2 tadan maktab qo'shing.  
**Kutiladigan natija:** To'g'ri 1:N bog'lanish shakllantiriladi.

### 6. Yillik KPI jadvali va ma'lumot kiritish <Badge type="warning" text="o'rta" />
`yillik_kpi` jadvalini yarating: `(kpi_id PK, hudud_id FK, yil, oquvchilar_soni, oqituvchilar_soni, maktablar_soni)`. 2023 va 2024 yillar uchun har bir hududga namunaviy ko'rsatkichlarni kiriting.  
**Kutiladigan natija:** Relyatsion ko'rsatkichlar jadvali ma'lumotlar bilan to'ldiriladi.

### 7. Maktab va Hududlarni JOIN bilan chiqarish <Badge type="warning" text="o'rta" />
`maktablar` va `hududlar` jadvallarini `hudud_id` bo'yicha birlashtiruvchi (`INNER JOIN`) SQL so'rovi yozing. Ekranga: Hudud nomi, Maktab raqami va uning o'quvchi sig'imi chiqsin.  
**Kutiladigan natija:** Ikkita jadval yagona ma'lumotlar oqimiga birlashtiriladi.

### 8. M:N bog'lanish uchun Junction Table yaratish <Badge type="warning" text="o'rta" />
O'quvchilar va Fan to'garaklari o'rtasida Ko'pga-ko'p bog'lanish o'rnating:
1. `oquvchilar (oquvchi_id PK, ism)`
2. `togaraklar (togarak_id PK, togarak_nomi)`
3. `oquvchi_togarak (oquvchi_id FK, togarak_id FK, azo_bolgan_sana, PRIMARY KEY(oquvchi_id, togarak_id))`  
**Kutiladigan natija:** M:N munosabat Junction table orqali ikkita 1:N ga aylantiriladi.

### 9. O'quvchi / maktab yuklamasini hisoblash <Badge type="danger" text="qiyin" />
`yillik_kpi` va `hududlar` jadvallari asosida har bir hudud uchun 2024-yilda bitta maktabga o'rtacha necha nafar o'quvchi to'g'ri kelganini (`oquvchilar_soni / maktablar_soni`) hisoblovchi tahliliy SQL so'rovini yozing va natijani kamayish tartibida (`ORDER BY DESC`) chiqaring.  
**Kutiladigan natija:** Matematik tahlil SQL darajasida amalga oshiriladi.

### 10. O'quvchi / o'qituvchi nisbati tahlili <Badge type="danger" text="qiyin" />
Ta'lim sifati monitoringi uchun muhim KPI — bu 1 nafar o'qituvchiga to'g'ri keladigan o'quvchilar sonidir. SQL orqali har bir hudud bo'yicha ushbu ko'rsatkichni hisoblang va qaysi hududda o'qituvchilarga yuklama eng yuqori ekanligini aniqlang.  
**Kutiladigan natija:** Aniq tahliliy ko'rsatkich ekranga chiqariladi.

### 11. Xatoni toping va tuzating <Badge type="danger" text="qiyin" />
Quyidagi oraliq jadvalda mantiqiy xato bor:
```sql
CREATE TABLE oquvchi_kurs (
    id INTEGER PRIMARY KEY,
    oquvchi_id INTEGER,
    kurs_id INTEGER,
    FOREIGN KEY (oquvchi_id) REFERENCES oquvchilar(id)
    -- Nima yetishmayapti?
);
```
Ushbu jadval nima uchun to'liq Junction table bo'la olmaydi? Undagi barcha kamchiliklarni to'g'rilang.  
**Kutiladigan natija:** `kurs_id` uchun Foreign Key va takroriy yozilishdan saqlovchi cheklov qo'shiladi.

### 12. Kengaytirilgan Ta'lim ERD Platformasi <Badge type="info" text="bonus" />
«Maktab tahliliy platformasi» modelini 4 ta jadvalgacha kengaytiring:
1. `hududlar`
2. `tumanlar` (`hudud_id` ga bog'langan)
3. `maktablar` (`tuman_id` ga bog'langan)
4. `bitiruvchilar_statistika` (har bir maktabning 9- va 11-sinf bitiruvchilari soni)  
Python skripti orqali barcha 4 ta jadvalni yarating, namunaviy ma'lumotlar qo'shing va bir nechta `JOIN` lar orqali viloyat ──→ tuman ──→ maktab ──→ bitiruvchilar zanjiridagi umumiy hisobotni chiqaring!  
**Kutiladigan natija:** Haqiqiy korporativ darajadagi ko'p bosqichli relyatsion arxitektura quriladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. ER-diagramma nima va nima uchun tizimni dasturlashdan oldin uni chizish talab etiladi?
2. Entity (Obyekt) va Attribute (Xususiyat) ning farqini bitta misol bilan tushuntiring.
3. Ko'pga-ko'p (M:N) munosabatni relyatsion bazaga to'g'ridan-to'g'ri kiritib bo'lmasligining sababi nima?
4. Junction (Oraliq) jadval qanday qilib M:N bog'lanishni ikkita 1:N ga aylantiradi?
5. Crow's Foot notatsiyasida "qarg'a oyog'i" belgisi qaysi tomonni (bitta yoki ko'p) ifodalaydi?
6. O'zbekiston ta'limi statistikasida viloyat va maktablar o'rtasida qanday kardinallik mavjud?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. O'zingiz qiziqqan bitta soha (sport klubi, aviasoat, onlayn do'kon) uchun kamida 4 ta jadvaldan iborat ER-diagrammani qog'ozda yoki grafik vositalarda chizing.
2. Unda kamida bitta M:N munosabat bo'lsin va uni Junction table orqali to'g'ri yeching.
3. Python `sqlite3` yordamida ushbu diagramma asosida to'liq `.db` bazasini yarating va namunaviy yozuvlar bilan to'ldirib, bog'langan `JOIN` hisobotini oling.

</div>

