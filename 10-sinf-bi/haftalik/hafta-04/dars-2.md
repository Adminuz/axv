# 11-dars: SQL JOIN turlari (INNER, LEFT, RIGHT, FULL) va amaliy tahlil

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 4-hafta, 2-dars (umumiy 11-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga bir nechta jadvalni **kalit (PK/FK) orqali bog'lash**ni o'rgatish: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`, har birining natijasini oldindan ayta olish, `JOIN` ni `GROUP BY` bilan birga ishlatish va `LEFT JOIN ... IS NULL` bilan "yo'qlarni" topish. Rasmiy uslubiy ko'rsatmadagi tamoyil: jadvallar kalit orqali `JOIN` qilinib yagona analitik ko'rinishga (view) keltiriladi; fakt jadval o'lcham jadvallari bilan `JOIN` qilinadi.

---

## Kutilayotgan natijalar

- `JOIN` ning vazifasini va `ON` sharti (PK = FK) rolini tushuntiradi;
- 4 turdagi `JOIN` natijasini Venn diagrammasi va jadval ko'rinishida ayta oladi;
- Jadval taxalluslari (`h`, `k`, `m`) bilan o'qiladigan so'rov yozadi;
- 3 ta jadvalni ketma-ket bog'laydi;
- `JOIN + GROUP BY + HAVING` bilan hisobot tuzadi;
- `LEFT JOIN` + `WHERE ... IS NULL` bilan bog'lanmagan yozuvlarni topadi;
- `LEFT JOIN` da `ON` va `WHERE` farqini biladi.

---

## Kerakli jihozlar

- Python 3.10+ (`sqlite3`; `RIGHT` va `FULL JOIN` uchun SQLite 3.39+, tekshirish: `print(sqlite3.sqlite_version)`);
- `data/maktab.db` (10-darsdagi to'ldirish skriptidan keyin), qo'shimcha `qabul_reja` jadvali (pastda).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10** | Takrorlash | `GROUP BY` / `HAVING`; PK va FK (7-dars); tezkor savollar |
| **10–25** | `INNER JOIN` | Sintaksis, `ON`, taxalluslar, 3 jadval |
| **25–40** | `LEFT`, `RIGHT`, `FULL JOIN` | Natijalar farqi, `NULL` lar, anti-join |
| **40–45** | Tanaffus | |
| **45–55** | `JOIN` + agregatsiya | `GROUP BY`, `COALESCE`, `ON` va `WHERE` farqi |
| **55–75** | Amaliyot | 3 darajali topshiriqlar |
| **75–80** | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Nazariy qism (konspekt)

### 1. Nega JOIN kerak?

Relatsion bazada ma'lumot **bo'laklarga ajratilgan**: hudud nomi `hududlar` da, o'quvchilar soni `yillik_kpi` da. Hisobotda esa "Samarqand viloyati — 620 000" kerak. `JOIN` jadvallarni **kalit orqali** vaqtincha birlashtiradi (jadval ichidagi ma'lumot ko'chirilmaydi, takrorlanmaydi). Bog'lanish: `yillik_kpi.hudud_id` (FK) → `hududlar.hudud_id` (PK).

### 2. INNER JOIN: faqat mos kelganlar

```sql
SELECT h.nomi, k.yil, k.oquvchilar_soni
FROM hududlar h
INNER JOIN yillik_kpi k ON k.hudud_id = h.hudud_id
WHERE k.yil = 2024
ORDER BY k.oquvchilar_soni DESC;
```

Ikkala jadvalda ham mos satri bor yozuvlar qoladi. `JOIN` yolg'iz yozilsa, `INNER JOIN` ma'nosida. Natija: 5 qator (Xorazm viloyatida KPI yo'q, shuning uchun u chiqmaydi).

### 3. LEFT, RIGHT, FULL JOIN

| Tur | Natija |
|---|---|
| `INNER JOIN` | Faqat ikkala tomonda mos kelganlar |
| `LEFT JOIN` | Chap jadvalning **barcha** satrlari + o'ngdagi mosi (yo'q bo'lsa `NULL`) |
| `RIGHT JOIN` | O'ng jadvalning **barcha** satrlari + chapdagi mosi |
| `FULL JOIN` | Ikkala jadvalning **hamma** satrlari; mos kelmaganlar `NULL` bilan |

```sql
-- LEFT: Xorazm KPI siz ham ko'rinadi
SELECT h.nomi, k.oquvchilar_soni
FROM hududlar h
LEFT JOIN yillik_kpi k ON k.hudud_id = h.hudud_id AND k.yil = 2024
ORDER BY h.hudud_id;
-- ... ('Buxoro viloyati', 312000), ('Xorazm viloyati', None)
```

`RIGHT JOIN` — `LEFT JOIN` ning jadval o'rinlari almashtirilgani. Amalda ko'pchilik `LEFT JOIN` yozadi, shuning uchun o'qish osonroq. Eski SQLite (3.39 dan oldin) `RIGHT`/`FULL` ni qo'llamaydi: `LEFT JOIN` ga almashtirish yoki `UNION` bilan yig'ish mumkin.

**Anti-join** (bog'lanmaganlarni topish): `LEFT JOIN` + `WHERE o'ng_PK IS NULL`.

```sql
SELECT h.nomi
FROM hududlar h
LEFT JOIN yillik_kpi k ON k.hudud_id = h.hudud_id
WHERE k.kpi_id IS NULL;
-- Xorazm viloyati
```

**FULL JOIN uchun misol jadval** (hudud nomi bo'yicha bog'lanadi, FK yo'q; nomlar o'quv uchun o'ylab topilgan reja):

```sql
CREATE TABLE IF NOT EXISTS qabul_reja (hudud_nomi TEXT PRIMARY KEY, reja INTEGER NOT NULL);
INSERT OR IGNORE INTO qabul_reja VALUES
 ('Toshkent shahri', 9000), ('Samarqand viloyati', 12000),
 ('Buxoro viloyati', 6000), ('Qoraqalpog''iston Respublikasi', 5000);

SELECT h.nomi, q.hudud_nomi, q.reja
FROM hududlar h
FULL JOIN qabul_reja q ON q.hudud_nomi = h.nomi;
```

Natijada: faqat `hududlar` da bor (Farg'ona, Andijon, Xorazm: o'ng tomoni `NULL`), faqat `qabul_reja` da bor (Qoraqalpog'iston: chap tomoni `NULL`) va ikkalasida bor qatorlar ko'rinadi.

### 4. Ko'p jadvalli JOIN va agregatsiya

Rasmiy ko'rsatmadagi usul: fakt jadval o'lcham jadvallari bilan ketma-ket bog'lanadi. Bizning model:

```sql
SELECT h.nomi, m.raqam, k.oquvchilar_soni
FROM maktablar m
JOIN hududlar h    ON h.hudud_id = m.hudud_id
JOIN yillik_kpi k  ON k.hudud_id = h.hudud_id AND k.yil = 2024
ORDER BY h.nomi, m.raqam;
```

`JOIN` + `GROUP BY`: har hududda nechta maktab va jami sig'im (maktabi yo'q hudud ham chiqsin):

```sql
SELECT h.nomi,
       COUNT(m.maktab_id)        AS maktablar,
       COALESCE(SUM(m.sigim), 0) AS sigim
FROM hududlar h
LEFT JOIN maktablar m ON m.hudud_id = h.hudud_id
GROUP BY h.hudud_id, h.nomi
ORDER BY sigim DESC;
```

`COUNT(m.maktab_id)` ishlatildi (`COUNT(*)` emas), chunki `NULL` bo'lmaganlarni sanaydi: maktabi yo'q hudud uchun 0 chiqadi. `COALESCE(x, 0)` — `x` `NULL` bo'lsa `0` beradi.

### 5. ON va WHERE farqi (LEFT JOIN da)

`LEFT JOIN yillik_kpi k ON ... AND k.yil = 2024` — chap jadval satrlari saqlanadi. Shu shartni `WHERE k.yil = 2024` ga ko'chirsangiz, `NULL` li satrlar filtrlanib, natija `INNER JOIN` ga aylanadi. Qoida: o'ng jadval sharti `ON` da.

### Odatiy xatolar
1. `ON` shartini unutish: har satr har satrga ko'paytiriladi (Cartesian product).
2. `SELECT hudud_id` deb yozish: ikkala jadvalda ham bor, noaniq ustun (`h.hudud_id` yozish kerak).
3. `LEFT JOIN` da o'ng jadval shartini `WHERE` ga qo'yish.
4. Taxallus berib, keyin to'liq jadval nomini ishlatish.

---

## Kod namunalari

### 1-namuna: Python da `INNER JOIN`

```python
import sqlite3
conn = sqlite3.connect("data/maktab.db")
c = conn.cursor()
c.execute("""
SELECT h.nomi, k.oquvchilar_soni
FROM hududlar h
INNER JOIN yillik_kpi k ON k.hudud_id = h.hudud_id
WHERE k.yil = 2024
ORDER BY k.oquvchilar_soni DESC;
""")
for nomi, son in c.fetchall():
    print(f"{nomi:<22} {son:>9,}")
# Samarqand viloyati       620,000
# Farg'ona viloyati        585,000 ...
```

### 2-namuna: `LEFT JOIN` va `None` bilan ishlash

```python
c.execute("""
SELECT h.nomi, k.oquvchilar_soni
FROM hududlar h
LEFT JOIN yillik_kpi k ON k.hudud_id = h.hudud_id AND k.yil = 2024
ORDER BY h.hudud_id;
""")
for nomi, son in c.fetchall():
    print(nomi, "-", f"{son:,}" if son is not None else "ma'lumot yo'q")
```

### 3-namuna: JOIN + GROUP BY + HAVING

```python
c.execute("""
SELECT h.nomi, SUM(k.oquvchilar_soni) AS jami
FROM yillik_kpi k
JOIN hududlar h ON h.hudud_id = k.hudud_id
GROUP BY h.nomi
HAVING SUM(k.oquvchilar_soni) > 1500000
ORDER BY jami DESC;
""")
print(c.fetchall())  # Samarqand 1830000, Farg'ona 1717000, Andijon 1536000
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson): INNER JOIN
2023-yil uchun hudud nomi va o'qituvchilar sonini chiqaring (hudud nomi bo'yicha alifbo tartibida).

**Kutiladigan natija:** 5 qator (Xorazm yo'q).  
**Yechim:**
```sql
SELECT h.nomi, k.oqituvchilar_soni
FROM hududlar h
JOIN yillik_kpi k ON k.hudud_id = h.hudud_id
WHERE k.yil = 2023
ORDER BY h.nomi;
```

### 2-topshiriq (o'rta): Yo'qlarni topish
(a) KPI si umuman kiritilmagan hududlarni; (b) hech qanday maktabi kiritilmagan hududlarni toping.

**Kutiladigan natija:** (a) Xorazm viloyati; (b) Xorazm viloyati.  
**Yechim:**
```sql
-- (a)
SELECT h.nomi FROM hududlar h
LEFT JOIN yillik_kpi k ON k.hudud_id = h.hudud_id
WHERE k.kpi_id IS NULL;

-- (b)
SELECT h.nomi FROM hududlar h
LEFT JOIN maktablar m ON m.hudud_id = h.hudud_id
WHERE m.maktab_id IS NULL;
```

### 3-topshiriq (qiyin): Hudud hisoboti (3 jadval)
Har bir hudud uchun: nomi, maktablar soni (`maktablar` jadvalidan), 2024-yil o'quvchilar soni (`yillik_kpi` dan). Xorazm ham ko'rinsin (o'quvchilar soni o'rniga `0`). Natija o'quvchilar soni kamayish tartibida.

**Kutiladigan natija:** 6 qator, birinchisi Samarqand (3 maktab, 620000), oxirgisi Xorazm (0, 0).  
**Yechim:**
```sql
SELECT h.nomi,
       COUNT(m.maktab_id) AS maktablar,
       COALESCE(k.oquvchilar_soni, 0) AS oquvchilar_2024
FROM hududlar h
LEFT JOIN maktablar m   ON m.hudud_id = h.hudud_id
LEFT JOIN yillik_kpi k  ON k.hudud_id = h.hudud_id AND k.yil = 2024
GROUP BY h.hudud_id, h.nomi, k.oquvchilar_soni
ORDER BY oquvchilar_2024 DESC;
```
Eslatma: bu yerda maktablar soni to'g'ri chiqadi, chunki `yillik_kpi` bir hududga 2024-yil uchun bitta satr beradi (`UNIQUE (hudud_id, yil)`). `k.yil` shartisiz bo'lsa, satrlar ko'payib ketardi.

---

## Tezkor nazorat savollari

1. `INNER JOIN` va `LEFT JOIN` farqi nima?  
   *Javob:* `INNER` faqat mos kelganlarni, `LEFT` chapdagi barcha satrlarni (mosi yo'qlariga `NULL`) qaytaradi.
2. `ON` da nima yoziladi?  
   *Javob:* Bog'lash sharti, odatda `PK = FK`.
3. Bog'lanmagan yozuvlarni qanday topamiz?  
   *Javob:* `LEFT JOIN` + `WHERE o'ng_jadval_PK IS NULL`.
4. `FULL JOIN` natijasida nima bo'ladi?  
   *Javob:* Ikkala jadvalning barcha satrlari, mos kelmaganlar `NULL` bilan.
5. `ON` bo'lmasa nima bo'ladi?  
   *Javob:* Har satr har satr bilan juftlanadi (Cartesian product), natija juda katta.

---

## Uyga vazifa

`uyga-vazifa.md` ning 2-topshirig'i: JOIN hisoboti (20–30 daqiqa).
