---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "n": 3, "bob": "I-bob · Ma’lumotlar muhandisligiga kirish va ma’lumotlarni boshqarish", "lessons": [{"g": 7, "title": "7-dars: Relyatsion jadvallar, Primary Key, Foreign Key va relyatsion yaxlitlik", "lead": "Ma'lumotlar bazasining go'zalligi uning tartibida va qat'iy intizomidadir. Agar jadvalda to'g'ri kalitlar va cheklovlar o'rnatilmasa, u tez orada tartibsiz raqamlar uyumiga aylanadi. Ushbu darsda biz relyatsion arxitekturaning asosi bo'lgan cheklovlar, Primary Key turlari, Composite kalitlar hamda bog'langan yozuvlar xavfsizligini ta'minlashni o'rganamiz.", "link": "/10-sinf-bi/hafta-03/dars-1", "slide": "/slaydlar/10-sinf-bi/hafta-03/dars-1.html", "test": "/slaydlar/10-sinf-bi/hafta-03/dars-1-test.html"}, {"g": 8, "title": "8-dars: R-diagrammalar (ERD) loyihalash va SQLite bilan ishlash", "lead": "Yaxshi loyihalangan ma'lumotlar bazasi — mustahkam bino poydevoriga o'xshaydi. Agar poydevor egri bo'lsa, ustiga qancha go'zal bino qurmang, u ertami-kechmi qulaydi. Ushbu darsda biz murakkab tizimlarning arxitekturasini qog'ozda va ekranda ERD (Entity-Relationship Diagram) ko'rinishida modellashtirishni hamda O'zbekiston ta'limi bo'yicha «Maktab tahliliy platformasi»ning relyatsion poydevorini qurishni o'rganamiz.", "link": "/10-sinf-bi/hafta-03/dars-2", "slide": "/slaydlar/10-sinf-bi/hafta-03/dars-2.html", "test": "/slaydlar/10-sinf-bi/hafta-03/dars-2-test.html"}, {"g": 9, "title": "9-dars: SQL analitik operatorlari: SELECT, WHERE, ORDER BY, LIMIT asoslari", "lead": "Ma'lumotlar bazasi — bu ulkan kutubxona. SELECT, WHERE, ORDER BY va LIMIT operatorlari esa shu kutubxonaning to'g'ri kitobni topib beradigan aqlli kutubxonachisidir. Ushbu darsda biz O'zbekiston ta'limi statistikasini SQL orqali tahlil qilishni o'rganamiz: eng ko'p o'quvchisi bo'lgan viloyatlarni topish, diapazonli filtrlash va TOP-N reytinglar chiqarish.", "link": "/10-sinf-bi/hafta-03/dars-3", "slide": "/slaydlar/10-sinf-bi/hafta-03/dars-3.html", "test": "/slaydlar/10-sinf-bi/hafta-03/dars-3-test.html"}], "test": "/slaydlar/10-sinf-bi/hafta-03/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta  
**Topshirish muddati:** Keyingi darsga qadar (4-hafta, 1-dars)

---

## Topshiriq 1: Ma'lumotlar bazasini boyitish <Badge type="warning" text="o'rta" />
`maktab.db` bazasiga `hududlar` jadvalida kamida 5 ta viloyat qayd etilgan bo'lishi kerak. `yillik_kpi` jadvaliga shu 5 ta viloyat uchun **2022, 2023 va 2024** yillar bo'yicha quyidagi ustunlar bilan ma'lumotlar kiriting:

- `hudud_id` — viloyat identifikatori
- `yil` — yil
- `oquvchilar_soni` — talabalar soni (maqsadga muvofiq raqamlar, masalan, 300 000 — 900 000 oralig'ida)
- `maktablar_soni` — maktablar soni (masalan, 500 — 2000 oralig'ida)
- `oquvchilar_soni / maktablar_soni` ni hisoblash uchun ikkala ustun ham to'ldirilishi shart

**Eslatma:** `INSERT INTO` SQL buyrug'i yordamida. Qiymatlarni o'ylab topmasdan, o'zingiz yashayotgan yoki o'qiyotgan viloyatlar statistikasini taxminiy kiriting.

---

## Topshiriq 2: Maktab yuklamasi tahlili <Badge type="danger" text="qiyin" />
Python skripti (`uyga_vazifa.py`) yozing. Skript quyidagilarni bajarsin:

1. `maktab.db` ga ulaning, `PRAGMA foreign_keys = ON` qo'ying.
2. **SQL 1 — Barcha hududlar uchun o'rtacha yuklama:** Har bir hudud uchun 2022–2024 yillar bo'yicha o'rtacha bitta maktabga to'g'ri keladigan o'quvchilar sonini hisoblang.
   - `ROUND(... / ..., 1)` va `AS` taxallusidan foydalaning.
   - Natijani hudud nomi bilan chiqaring (JOIN bilan).
3. **SQL 2 — Yuklamasi 700 dan oshgan hududlar:** 2-so'rovda faqat 2024-yilgi yuklamasi 700 nafardan oshgan hududlarni `WHERE` orqali filtrlang.
4. **SQL 3 — TOP-3 hudud:** Yuqori yuklamalidan pastiga `ORDER BY ... DESC` saralang va `LIMIT 3` bilan faqat eng yuqori 3 ta hududni chiqaring.
5. Har uchala so'rov natijasini `print` bilan konsolga tartibli — chiroyli jadval ko'rinishida — chiqaring.

```python
# Kutilayotgan natija ko'rinishi:
# ============================================
# TOP-3: Maktab yuklamasi (2024-yil)
# ============================================
# Hudud                    Yuklama (o'quvchi/maktab)
# ----------------------------------------
# Toshkent viloyati              842.3
# Samarqand viloyati             791.0
# Qashqadaryo viloyati           735.8
```

---

## Topshiriq 3: Mustaqil tadqiqot <Badge type="info" text="bonus" />
Internetdan O'zbekistonning haqiqiy ta'lim statistikasini toping (stat.uz yoki xalqaro ma'lumotlar). Kamida 3 ta viloyat uchun haqiqiy ma'lumotlarni `maktab.db` ga kiriting va SQL tahlil natijalari bilan taqqoslang. Taqqoslash natijasini qisqa (5–7 jumladan iborat) matn ko'rinishida `izoh.txt` faylida yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| Topshiriq 1 (ma'lumotlar kiritilgan, 3 yil × 5 hudud) | 3 |
| Topshiriq 2 (SQL 1: o'rtacha yuklama bilan JOIN) | 2 |
| Topshiriq 2 (SQL 2: WHERE filtri to'g'ri ishlaydi) | 2 |
| Topshiriq 2 (SQL 3: TOP-3 ORDER BY + LIMIT) | 2 |
| Kod izohlangan, `print` natijasi tartibli | 1 |
| **Jami** | **10** |
| Bonus (haqiqiy statistika + izoh.txt) | +2 |

---

</div>
