---
title: "4-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "n": 4, "bob": "I-bob · Ma’lumotlar muhandisligiga kirish va ma’lumotlarni boshqarish", "lessons": [{"g": 10, "title": "10-dars: SQL analitik operatorlari: GROUP BY va HAVING bilan ma'lumotlarni guruhlash", "lead": "Bitta so'rov bilan millionlab satrni bir qatorli hisobotga aylantirishni xohlaysizmi? GROUP BY va HAVING aynan shuni qiladi: guruhlaydi, hisoblaydi va keraksiz guruhlarni saralab tashlaydi.", "link": "/10-sinf-bi/hafta-04/dars-1", "slide": "/slaydlar/10-sinf-bi/hafta-04/dars-1.html", "test": "/slaydlar/10-sinf-bi/hafta-04/dars-1-test.html"}, {"g": 11, "title": "11-dars: SQL JOIN turlari (INNER, LEFT, RIGHT, FULL) va amaliy tahlil", "lead": "Ma'lumot bitta jadvalda emas, bo'laklarga bo'lib saqlanadi. JOIN esa ularni kalit orqali bir joyga yig'adigan \"yelim\". Bugun to'rt xil yelimni va ularning qachon qo'llanishini o'rganasiz.", "link": "/10-sinf-bi/hafta-04/dars-2", "slide": "/slaydlar/10-sinf-bi/hafta-04/dars-2.html", "test": "/slaydlar/10-sinf-bi/hafta-04/dars-2-test.html"}, {"g": 12, "title": "12-dars: Subquery, CTE (WITH) va CASE WHEN operatorlari", "lead": "Murakkab savolni bitta ulkan so'rovga tiqish shart emas: uni bosqichlarga bo'ling. Subquery savol ichidagi savol, CTE nomlangan oraliq natija, CASE WHEN esa SQL ning \"agar... bo'lsa\" iborasi.", "link": "/10-sinf-bi/hafta-04/dars-3", "slide": "/slaydlar/10-sinf-bi/hafta-04/dars-3.html", "test": "/slaydlar/10-sinf-bi/hafta-04/dars-3-test.html"}], "test": "/slaydlar/10-sinf-bi/hafta-04/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 4-hafta  
**Topshirish muddati:** Keyingi darsga qadar (5-hafta, 1-dars)

---

## Topshiriq 1 (10-dars): GROUP BY va HAVING hisoboti <Badge type="warning" text="o'rta" />
`maktab.db` da `uyga_vazifa_4.py` skriptini yozing. Skript quyidagilarni chiqarsin:

1. Yillar bo'yicha jami o'quvchilar, o'qituvchilar va maktablar soni (`GROUP BY yil`).
2. Hududlar bo'yicha o'rtacha o'quvchi/o'qituvchi nisbati; faqat nisbati 13 dan yuqori bo'lganlar (`HAVING`, `NULLIF` va `* 1.0` bilan).
3. Dublikat tekshiruvi: `GROUP BY hudud_id, yil HAVING COUNT(*) > 1` (natija bo'sh bo'lishi kerak).

Natijani `print` bilan tartibli ko'rinishda chiqaring.

---

## Topshiriq 2 (11-dars): JOIN hisoboti <Badge type="warning" text="o'rta" />
1. `qabul_reja` jadvalini (agar yo'q bo'lsa) yarating va 4 ta yozuv kiriting.
2. Har bir hudud uchun nomi, 2024-yil o'quvchilar soni va rejani bitta jadvalda chiqaring (`LEFT JOIN`, reja yo'q bo'lsa `COALESCE(reja, 0)`).
3. `qabul_reja` da rejasi kiritilmagan hududlarni anti-join bilan alohida chiqaring.

---

## Topshiriq 3 (12-dars): CTE va CASE WHEN hisoboti <Badge type="danger" text="qiyin" />
1. CTE da 2024-yil uchun hududlar bo'yicha o'quvchi/o'qituvchi nisbatini hisoblang.
2. `CASE WHEN` bilan toifa bering: 14 dan katta `Yuqori`, 13 dan katta `O'rta`, qolgani `Normal`.
3. Toifalar bo'yicha hududlar sonini chiqaring (`GROUP BY toifa`).
4. Natijani Python orqali chiroyli chop eting.

---

## Topshiriq 4: O'z savolingiz <Badge type="info" text="bonus" />
Bazaga qarab o'zingiz bitta tahliliy savol o'ylab toping (masalan, "qaysi hududda yuklama eng tez o'sdi?") va unga `JOIN`, CTE yoki `CASE WHEN` yordamida javob bering. Savolni va 3 jumlali xulosani `izoh.txt` ga yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| Topshiriq 1 (3 ta so'rov to'g'ri ishlaydi) | 3 |
| Topshiriq 2 (`LEFT JOIN`, `COALESCE`, anti-join) | 3 |
| Topshiriq 3 (CTE, `CASE WHEN`, guruhlash) | 3 |
| Kod izohlangan, natija tartibli chiqarilgan | 1 |
| **Jami** | **10** |
| Bonus (o'z savol + izoh.txt) | +2 |

---

</div>
