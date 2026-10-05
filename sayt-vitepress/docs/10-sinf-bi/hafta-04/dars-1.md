---
title: "10-dars. 10-dars: SQL analitik operatorlari: GROUP BY va HAVING bilan ma'lumotlarni guruhlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 4, "link": "/10-sinf-bi/hafta-04/"}, "g": 10, "title": "10-dars: SQL analitik operatorlari: GROUP BY va HAVING bilan ma'lumotlarni guruhlash", "lead": "Bitta so'rov bilan millionlab satrni bir qatorli hisobotga aylantirishni xohlaysizmi? GROUP BY va HAVING aynan shuni qiladi: guruhlaydi, hisoblaydi va keraksiz guruhlarni saralab tashlaydi.", "slide": "/slaydlar/10-sinf-bi/hafta-04/dars-1.html", "test": "/slaydlar/10-sinf-bi/hafta-04/dars-1-test.html", "tabs": [{"g": 10, "link": "/10-sinf-bi/hafta-04/dars-1", "current": true}, {"g": 11, "link": "/10-sinf-bi/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/10-sinf-bi/hafta-04/dars-3", "current": false}], "prev": null, "next": {"g": 11, "title": "11-dars: SQL JOIN turlari (INNER, LEFT, RIGHT, FULL) va amaliy tahlil", "link": "/10-sinf-bi/hafta-04/dars-2"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Agregat funksiyalar** ko'p satrni bitta qiymatga aylantiradi: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
- `COUNT(*)` barcha satrlarni, `COUNT(ustun)` esa `NULL` bo'lmaganlarni sanaydi.
- **`GROUP BY`** satrlarni guruhlarga bo'ladi; agregat funksiya har guruh uchun alohida hisoblanadi.
- `SELECT` dagi har bir ustun yoki `GROUP BY` da bo'lishi, yoki agregat ichida turishi kerak.
- **`WHERE`** satrlarni guruhlashdan **oldin**, **`HAVING`** guruhlarni guruhlashdan **keyin** filtrlaydi.
- Mantiqiy ijro tartibi: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`.
- `NULLIF(a, 0)` nolga bo'lish xatosidan saqlaydi (KPI nisbatida).
- Dublikatni topish: `GROUP BY kalit HAVING COUNT(*) > 1`.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Guruhlash: savat o'xshatishi
Tasavvur qiling: stol ustida 15 ta kartochka (har biri hudud va yil). `GROUP BY yil` — kartochkalarni yil bo'yicha 3 ta savatga ajratish. Keyin `SUM` har savatdagi sonlarni qo'shadi. Natijada 15 emas, 3 qator chiqadi.

### 2. Nega WHERE ichida SUM yozib bo'lmaydi?
`WHERE` satrlarni birinchi bo'lib ko'zdan kechiradi, guruhlar esa hali yo'q. Yig'indi hali hisoblanmagan! Shuning uchun agregat shart faqat guruhlardan keyin ishlaydigan `HAVING` da yoziladi:

```sql
-- XATO
SELECT yil, SUM(oquvchilar_soni) FROM yillik_kpi
WHERE SUM(oquvchilar_soni) > 2500000 GROUP BY yil;

-- TO'G'RI
SELECT yil, SUM(oquvchilar_soni) FROM yillik_kpi
GROUP BY yil HAVING SUM(oquvchilar_soni) > 2500000;
```

### 3. Ikkala filtr birga
`WHERE` ni kuchli tarzda ishlating: u satrlarni oldindan kamaytiradi, guruhlash tezroq ishlaydi. `HAVING` ni faqat agregatga bog'liq shart uchun saqlang.

```sql
SELECT hudud_id, COUNT(*) AS maktab_soni, SUM(sigim) AS umumiy_sigim
FROM maktablar
WHERE sigim >= 600          -- satr filtri
GROUP BY hudud_id
HAVING COUNT(*) >= 2        -- guruh filtri
ORDER BY umumiy_sigim DESC;
```

### 4. Nolga bo'lish
Ba'zi bazalar nolga bo'lishda xato beradi. `NULLIF(SUM(oqituvchilar_soni), 0)` maxraj nol bo'lsa `NULL` qaytaradi, natija ham `NULL` bo'ladi, dastur esa to'xtamaydi. SQLite da butun sonlar bo'linmasi kasrni kesib tashlaydi (`5 / 2 = 2`), shuning uchun `* 1.0` qo'shing.

### 5. Odatiy xatolar
- `GROUP BY` da ko'rsatilmagan oddiy ustunni `SELECT` ga yozish.
- `HAVING` o'rniga `WHERE` yozish.
- `COUNT(*)` va `COUNT(ustun)` ni almashtirib yuborish.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Aggregate function** | Ko'p satrdan bitta qiymat hosil qiluvchi funksiya (`SUM`, `AVG`...) |
| **GROUP BY** | Satrlarni ustun qiymati bo'yicha guruhlarga ajratadi |
| **HAVING** | Guruhlarni agregat natijasi bo'yicha filtrlaydi |
| **COUNT** | Satrlar yoki qiymatlar sonini sanaydi |
| **NULLIF** | Ikki qiymat teng bo'lsa `NULL` qaytaradi |
| **Alias** | Ustun yoki hisobga berilgan vaqtinchalik nom (`AS`) |
| **KPI** | Muhim ko'rsatkich (masalan, o'quvchi/o'qituvchi nisbati) |
| **Dublikat** | Kalit bo'yicha takrorlangan yozuv |
| **Mantiqiy ijro tartibi** | So'rov bandlarining bajarilish ketma-ketligi |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Dashboard dagi "oylik daromad" grafigi ko'pincha oddiy `GROUP BY oy` + `SUM` so'rovi bilan hisoblanadi.
- SQL da NULL "nol" emas, "noma'lum" degani: shuning uchun `AVG` ular ustidan sakrab o'tadi.
- Telegram yoki Instagram "bugun nechta xabar" statistikasi ham guruhlab sanash orqali chiqadi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

> Hamma topshiriq `maktab.db` ning `hududlar`, `maktablar`, `yillik_kpi` jadvallari uchun. Dars boshida mentor bergan to'ldirish skriptini ishga tushiring.

### 1. Funksiyani moslashtiring <Badge type="tip" text="oson" />
Har bir vazifa uchun to'g'ri agregat funksiyani yozing: (a) hududlar sonini sanash; (b) eng katta maktab sig'imi; (c) o'quvchilar umumiy yig'indisi; (d) o'rtacha o'qituvchi soni.  
**Kutiladigan natija:** to'rtta funksiya nomi va ular ishlatiladigan ustun.

### 2. Birinchi hisobot <Badge type="tip" text="oson" />
`yillik_kpi` dan `COUNT(*)`, `SUM(oquvchilar_soni)`, `MAX(oquvchilar_soni)` ni bitta `SELECT` da chiqaring.  
**Kutiladigan natija:** bitta qator, uchta son.

### 3. Yillar bo'yicha jami <Badge type="tip" text="oson" />
Har bir yil uchun jami o'quvchilar sonini chiqaring, yil bo'yicha saralang.  
**Kutiladigan natija:** har yil uchun bitta qator (uchta yil).

### 4. Bu kod nima chiqaradi? <Badge type="tip" text="oson" />
```sql
SELECT turi, COUNT(*) FROM maktablar GROUP BY turi;
```
Qancha qator chiqadi? Qatorlar nimani bildiradi? Avval fikringizni yozing, keyin ishga tushirib tekshiring.  
**Kutiladigan natija:** bashorat va haqiqiy natija taqqoslanadi.

### 5. WHERE yoki HAVING? <Badge type="warning" text="o'rta" />
Quyidagi shartlar uchun qaysi biri (`WHERE` yoki `HAVING`) kerakligini yozing va sababini tushuntiring: (a) `yil = 2024`; (b) `SUM(oquvchilar_soni) > 1000000`; (c) `sigim >= 600`; (d) `COUNT(*) >= 2`.  
**Kutiladigan natija:** to'rtta javob va ularning izohi.

### 6. KPI nisbati <Badge type="warning" text="o'rta" />
Har bir yil uchun o'quvchi/o'qituvchi nisbatini 2 xona aniqlikda hisoblang (`NULLIF` va `* 1.0` bilan).  
**Kutiladigan natija:** uch qator, qiymatlar 13 atrofida.

### 7. Hudud bo'yicha o'rtacha <Badge type="warning" text="o'rta" />
Har bir hudud uchun o'quvchilarning 3 yillik o'rtachasini toping va faqat 500 000 dan ko'p bo'lganlarni qoldiring.  
**Kutiladigan natija:** `HAVING AVG(...) > 500000` ishlatilgan, o'rtachasi kattasi birinchi.

### 8. Xatoni toping <Badge type="warning" text="o'rta" />
```sql
SELECT hudud_id, yil, SUM(oquvchilar_soni)
FROM yillik_kpi
GROUP BY hudud_id;
```
So'rov nima uchun noto'g'ri yoki noaniq? Qanday tuzatasiz?  
**Kutiladigan natija:** `yil` ustuni `GROUP BY` da yo'qligi aniqlanib, tuzatilgan so'rov yoziladi.

### 9. Dublikat ovchisi <Badge type="danger" text="qiyin" />
`yillik_kpi` da bir hudud va bir yil uchun ikki marta yozilgan qator bormi? Tekshiruvchi so'rov yozing. Keyin `UNIQUE (hudud_id, yil)` cheklovi nima uchun dublikatga yo'l qo'ymasligini tushuntiring.  
**Kutiladigan natija:** `GROUP BY ... HAVING COUNT(*) > 1` so'rovi, natija bo'sh.

### 10. Maktab hisoboti <Badge type="danger" text="qiyin" />
`maktablar` dan har bir hudud uchun maktab soni va umumiy sig'imni chiqaring; faqat sig'imi 600 va undan katta maktablarni hisobga oling; kamida 2 maktabi bo'lgan hududlar qolsin; umumiy sig'im kamayish tartibida bo'lsin.  
**Kutiladigan natija:** `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY` to'rttasi ham ishlatilgan so'rov.

### 11. Ijro tartibini chizing <Badge type="danger" text="qiyin" />
10-topshiriqdagi so'rovning mantiqiy ijro bosqichlarini ketma-ket yozing va har bosqichda satrlar soni qanday o'zgarishini taxmin qiling.  
**Kutiladigan natija:** `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY` zanjiri va izohlar.

### 12. Mini-loyiha: o'z maktabingiz <Badge type="info" text="bonus" />
`maktablar` jadvaliga o'zingizning hududingizdan 5 ta maktab qo'shing (`INSERT`), keyin hudud bo'yicha o'rtacha sig'imni hisoblab, natijani `print` bilan jadval ko'rinishida chiqaruvchi Python skript yozing.  
**Kutiladigan natija:** ishlaydigan skript va chiroyli formatlangan natija.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Agregat funksiya oddiy funksiyadan nimasi bilan farq qiladi?
2. `COUNT(*)` bilan `COUNT(oquvchilar_soni)` qachon farq qiladi?
3. `GROUP BY yil` bo'lsa, `SELECT` ga yana qanday ustunlarni yozish mumkin?
4. `WHERE` va `HAVING` ning asosiy farqi nima?
5. Nega `WHERE SUM(x) > 5` ishlamaydi?
6. `NULLIF(a, 0)` nima qaytaradi, `a` nolga teng bo'lsa?
7. Dublikatni topish uchun qanday so'rov yoziladi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

`maktab.db` da yillar va hududlar kesimida hisobot tuzing: (1) yillar bo'yicha jami o'quvchi, o'qituvchi va maktablar soni; (2) hududlar bo'yicha o'rtacha o'quvchi/o'qituvchi nisbati, faqat 13 dan yuqori bo'lganlar (`HAVING`); (3) dublikat tekshirish so'rovi. Natijani Python skript orqali chiroyli chiqaring. (20–30 daqiqa)

</div>

