# 5-hafta: Uyga vazifa

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 5-hafta  
**Topshirish muddati:** Keyingi darsga qadar (6-hafta, 1-dars)

---

## Topshiriq 1 (13-dars): Kimball, Star va Snowflake · o'rta

1. `maktab.db` asosida `dim_hudud`, `dim_sana` va `fact_kpi` jadvallarini yarating va to'ldiring (`fact_kpi` da 15 qator bo'lsin).
2. Star Schema diagrammasini daftarda chizing: PK, FK va 1:N bog'lanishlarni ko'rsating.
3. 3 ta so'rov yozing: yillik jami, hududlar bo'yicha 2024 yil jami, eng ko'p o'quvchili hudud.

---

## Topshiriq 2 (14-dars): Fakt va o'lcham jadvallari · o'rta

1. `maktab.db` da `dim_hudud` (surrogate kalit bilan), `dim_sana` va `fact_kpi` jadvallarini yarating va yuklang.
2. Uch tekshiruvni bajaring: qatorlar soni, yetim kalit, grain dublikati; natijani izohlang.
3. Har bir o'lchovning turini (additive, semi-additive, non-additive) yozing va semi-additive uchun to'g'ri jamlash so'rovini yozing.

---

## Topshiriq 3 (15-dars): Data Mart · qiyin

1. `mart_oquvchilar` va `mart_yuklama` VIEW larini yarating.
2. Yangi, o'zingiz o'ylagan soha marti uchun (masalan, `mart_maktablar`) 1 paragrafli ta'rif yozing va VIEW yarating.
3. Martlardan 5 ta analitik so'rov yozing (kamida 2 tasi `GROUP BY` bilan), natijani izohlang.

---

## Topshiriq 4: O'z savolingiz · bonus

O'zingiz sohani tanlab (masalan, kutubxona yoki do'kon) mini Star Schema loyihalang: 1 fakt, kamida 2 dimension. Grain ni bitta jumlada yozing va 1 ta tahliliy savolga javob bering. Natijani `izoh.txt` ga yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| Topshiriq 1 (Star Schema jadvallari to'g'ri) | 3 |
| Topshiriq 2 (uchta tekshiruv va o'lchov turlari) | 3 |
| Topshiriq 3 (VIEW va analitik so'rovlar) | 3 |
| Kod izohlangan, natija tartibli chiqarilgan | 1 |
| **Jami** | **10** |
| Bonus (o'z savol + izoh.txt) | +2 |

---

## Mentor uchun

- `fact_kpi` da 15 qator (5 hudud x 3 yil) bo'lishi kerak; Xorazm (KPI yo'q) faktga kirmaydi.
- Fakt jadvalida matnli atributlar emas, faqat kalitlar va o'lchovlar bo'lishini tekshiring.
- Semi-additive o'lchov (o'quvchilar soni) yillar bo'yicha qo'shilmasligini tekshiring.
- `VIEW` ma'lumotni nusxalamaydi, so'rovni saqlaydi.

**Keng tarqalgan xatolar:**
1. Grain ni aniqlamasdan fakt yaratish.
2. Faktga matnli atribut qo'yish.
3. Yetim kalit (dimension da yo'q FK).
4. Semi-additive o'lchovni yillar bo'yicha qo'shish.
5. `VIEW` ni jadval deb o'ylab, unga `INSERT` qilish.
