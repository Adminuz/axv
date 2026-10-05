# 12-dars. Subquery, CTE (WITH) va CASE WHEN operatorlari

> Murakkab savolni bitta ulkan so'rovga tiqish shart emas: uni bosqichlarga bo'ling. Subquery savol ichidagi savol, CTE nomlangan oraliq natija, CASE WHEN esa SQL ning "agar... bo'lsa" iborasi.

---

## Dars xulosasi

- **Subquery** — boshqa so'rov ichidagi `SELECT` (qavs ichida); avval ichki, keyin tashqi so'rov bajariladi.
- Subquery turlari: **skalyar** (bitta qiymat), **`IN` / `NOT IN`** (ro'yxat), **`FROM`** dagi (vaqtinchalik jadval, taxallus bilan).
- **CTE** — `WITH nom AS (...)` bilan so'rov oldidan nomlangan vaqtinchalik natija; so'rov tepadan pastga o'qiladi.
- Bir nechta CTE vergul bilan ketma-ket yoziladi.
- **`CASE WHEN ... THEN ... ELSE ... END`** — shartli ustun (toifalash), yuqoridan pastga tekshiriladi.
- `SUM(CASE WHEN ...)` yordamida **pivot** (yillar ustunlarga) va shartli sanash bajariladi.
- Rasmiy uslubiy ko'rsatmadagi yillik o'sish (YoY) misoli: CTE + `LAG`.
- Bu hafta: `GROUP BY` / `HAVING`, `JOIN`, Subquery / CTE / `CASE WHEN`.

---

## Qo'shimcha ma'lumot

### 1. Subquery: savol ichida savol
"Qaysi hudud o'rtachadan katta?" Avval o'rtachani topish kerak (ichki savol), keyin har hududni u bilan solishtirish (tashqi savol). Subquery shuni bir so'rovda qiladi.

```sql
SELECT hudud_id, oquvchilar_soni
FROM yillik_kpi
WHERE yil = 2024
  AND oquvchilar_soni > (SELECT AVG(oquvchilar_soni) FROM yillik_kpi WHERE yil = 2024);
```

### 2. IN va NOT IN
`IN (subquery)` ro'yxatdagi qiymatlardan biriga tenglikni tekshiradi. `NOT IN` ro'yxatda **yo'qlarni** topadi, lekin ichki ro'yxatda `NULL` bo'lsa, natija kutilmagan bo'lishi mumkin. Shu sababli `LEFT JOIN ... IS NULL` xavfsizroq.

### 3. CTE: o'qiladigan so'rov
```sql
WITH t AS (
    SELECT yil, SUM(oquvchilar_soni) AS jami
    FROM yillik_kpi GROUP BY yil
)
SELECT yil, jami,
       jami - LAG(jami) OVER (ORDER BY yil) AS yoy_change
FROM t ORDER BY yil;
```
`t` — vaqtinchalik "jadval", faqat shu so'rov ichida mavjud. `LAG` oldingi satr qiymatini oladi: shunday qilib har yilning o'sishi (YoY) chiqadi (birinchi yilda oldingi yo'q, shuning uchun `NULL`).

### 4. Subquery yoki CTE?
| Holat | Tanlov |
|---|---|
| Bir joyda bitta oddiy qiymat | Subquery |
| Bir necha bosqich yoki bir hisob qayta ishlatiladi | CTE |
| O'qish osonligi muhim | CTE |

### 5. CASE WHEN: SQL dagi if/elif/else
```sql
CASE WHEN oquvchilar_soni >= 600000 THEN 'Katta'
     WHEN oquvchilar_soni >= 400000 THEN 'O''rta'
     ELSE 'Kichik' END AS toifa
```
Tartib muhim: agar `>= 400000` ni birinchi qo'ysangiz, 620 000 ham "O'rta" bo'lib qoladi! Matn ichidagi apostrof SQL da ikkilanadi (`'O''rta'`).

### 6. Pivot
Odatda yillar satrlarda turadi. `SUM(CASE WHEN yil = 2022 THEN ... END)` bilan har yil o'z ustuniga o'tadi: hisobotlarda keng qo'llaniladi. Rasmiy uslubiy ko'rsatmada dbt modelida ham `CASE WHEN` orqali pivot qilinib, o'quvchi/o'qituvchi nisbati kabi ko'rsatkichlar hisoblanadi.

### 7. Odatiy xatolar
- `CASE` ni `END` bilan yopmaslik.
- Skalyar subquery bittadan ko'p qiymat qaytarishi.
- `FROM` dagi subquery ga taxallus bermaslik.
- CTE lar orasida vergulni unutish yoki oxirgisidan keyin ortiqcha vergul qo'yish.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Subquery** | Boshqa so'rov ichidagi `SELECT` |
| **Skalyar subquery** | Aynan bitta qiymat qaytaradigan ichki so'rov |
| **IN / NOT IN** | Qiymat ro'yxatda bor / yo'qligini tekshirish |
| **CTE** | Common Table Expression, `WITH` bilan nomlangan vaqtinchalik natija |
| **WITH** | CTE ni e'lon qiluvchi kalit so'z |
| **CASE WHEN** | Shartli ustun yaratuvchi ifoda |
| **Pivot** | Satrlardagi qiymatlarni ustunlarga aylantirish |
| **YoY** | Year-over-Year: yilma-yil o'zgarish |
| **LAG** | Oldingi satr qiymatini beruvchi oyna funksiyasi |
| **Toifa (kategoriya)** | Qiymatlarni guruhlarga ajratuvchi yorliq (Katta/O'rta/Kichik) |

---

## Bilasizmi?

- CTE nomi "Common Table Expression" so'zlarining qisqartmasi; uni ko'pincha dasturlashdagi "vaqtinchalik o'zgaruvchi"ga o'xshatishadi.
- `CASE WHEN` BI vositalarida (Tableau, Power BI) ham aynan shu nom bilan yoki shunga o'xshash `IF` ifodasi sifatida uchraydi.
- YoY (yilma-yil) o'zgarish iqtisodchilar, startaplar va hukumat hisobotlarida eng ko'p ishlatiladigan ko'rsatkichlardan biri.

---

## Topshiriqlar

> Jadvallar o'tgan darsdagidek. Ma'lumotlar o'quv uchun o'ylab topilgan, haqiqiy statistika emas.

### 1. Subquery turini aniqlang · oson
Har bir so'rov uchun subquery turini ayting (skalyar, `IN`, `FROM` dagi): (a) `WHERE x > (SELECT AVG(x) FROM t)`; (b) `WHERE id IN (SELECT id FROM t2)`; (c) `FROM (SELECT ... GROUP BY ...) AS q`.  
**Kutiladigan natija:** uchta tur nomi.

### 2. Eng kattani toping · oson
2024-yilda eng ko'p o'quvchisi bo'lgan hududni `MAX` va subquery yordamida toping.  
**Kutiladigan natija:** bitta qator (`hudud_id` va o'quvchilar soni).

### 3. Birinchi CTE · oson
Yillar bo'yicha jami o'quvchilar sonini hisoblaydigan CTE yozing va uni `SELECT` bilan chaqiring.  
**Kutiladigan natija:** har yil uchun bitta qator.

### 4. Bu kod nima chiqaradi? · oson
```sql
SELECT CASE WHEN 7 > 10 THEN 'A' WHEN 7 > 5 THEN 'B' ELSE 'C' END;
```
Natijani bashorat qiling, keyin tekshiring.  
**Kutiladigan natija:** bashorat va sabab (birinchi to'g'ri shart ishlaydi).

### 5. O'rtachadan yuqori · o'rta
2024-yil o'quvchilar soni o'rtachadan katta hududlarning nomlarini chiqaring (hudud nomi uchun `JOIN` yoki `IN` subquery).  
**Kutiladigan natija:** o'rtachadan katta uchta hudud nomi.

### 6. Hududi yo'qlarni topish · o'rta
`NOT IN (subquery)` yordamida KPI si umuman yo'q hududlarni toping. Keyin shuni `LEFT JOIN ... IS NULL` bilan ham yozing va taqqoslang.  
**Kutiladigan natija:** ikkala usulda bir xil natija (ma'lumotsiz hudud).

### 7. Toifalash · o'rta
2024-yil uchun har bir hududga o'quvchilar soni bo'yicha toifa bering: 600 000 va undan yuqori `Katta`, 400 000 va undan yuqori `O'rta`, qolgani `Kichik`.  
**Kutiladigan natija:** hudud nomi, o'quvchilar soni va toifa ustuni.

### 8. Tartib xatosi · o'rta
Quyidagi so'rovda barcha hududlar nega "Kichik" chiqadi? Tuzating.
```sql
CASE WHEN oquvchilar_soni > 0 THEN 'Kichik'
     WHEN oquvchilar_soni >= 400000 THEN 'O''rta'
     ELSE 'Katta' END
```
**Kutiladigan natija:** shartlar tartibi tuzatiladi (kattadan kichikka).

### 9. YoY o'sish · qiyin
CTE va `LAG` yordamida yillik jami o'quvchilar sonining o'sishini hisoblang. Birinchi yil uchun nega `NULL` chiqishini tushuntiring.  
**Kutiladigan natija:** 2022 uchun `NULL`, keyingi yillar uchun musbat o'sish.

### 10. Pivot · qiyin
`SUM(CASE WHEN ...)` bilan har hudud uchun 2022, 2023, 2024 o'quvchilar sonini uchta ustunga ajrating.  
**Kutiladigan natija:** hudud boshiga bitta qator, uchta yil ustuni.

### 11. Ikki CTE · qiyin
Birinchi CTE: har hudud uchun 3 yillik jami. Ikkinchi CTE: shu jamilarning o'rtachasi. Asosiy so'rov: jami o'rtachadan yuqori hududlarni chiqarsin.  
**Kutiladigan natija:** uchta hudud, vergul bilan ajratilgan ikki `WITH` blok.

### 12. Mini-loyiha: BI hisoboti · bonus
O'zingiz mavzu tanlang (masalan, hududlar yuklamasi) va quyidagilardan foydalanib bitta tahliliy so'rov yozing: `JOIN`, CTE, `CASE WHEN`, `GROUP BY`. Natijani Python orqali jadval ko'rinishida chiqaring va 3 jumlali xulosa yozing.  
**Kutiladigan natija:** ishlaydigan so'rov va qisqa tahliliy xulosa.

---

## O'zingizni tekshiring

1. Subquery nima, qaysi tartibda bajariladi?
2. Skalyar subquery va `IN` subquery farqi nimada?
3. CTE ni qanday e'lon qilamiz va u qaysi vaqtgacha "yashaydi"?
4. Bir nechta CTE orasida nima turadi?
5. `CASE WHEN` da shartlar qaysi tartibda tekshiriladi?
6. `ELSE` yozilmasa nima bo'lishi mumkin?
7. Pivot nima va qanday qilinadi?
8. YoY nima va `LAG` nima uchun kerak?

---

## Uyga vazifa

Bitta mustaqil hisobot yozing: CTE da 2024-yil uchun hududlar bo'yicha o'quvchi/o'qituvchi nisbatini hisoblang, so'ng `CASE WHEN` bilan `Yuqori` (14 dan katta) / `O'rta` (13 dan katta) / `Normal` toifasini bering, toifalar bo'yicha hududlar sonini chiqaring. Natijani Python orqali chop eting. (20–30 daqiqa)
