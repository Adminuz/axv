# 4-hafta: Uyga vazifa

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 4-hafta  
**Topshirish muddati:** Keyingi darsga qadar (5-hafta, 1-dars)

---

## Topshiriq 1 (10-dars): GROUP BY va HAVING hisoboti · o'rta

`maktab.db` da `uyga_vazifa_4.py` skriptini yozing. Skript quyidagilarni chiqarsin:

1. Yillar bo'yicha jami o'quvchilar, o'qituvchilar va maktablar soni (`GROUP BY yil`).
2. Hududlar bo'yicha o'rtacha o'quvchi/o'qituvchi nisbati; faqat nisbati 13 dan yuqori bo'lganlar (`HAVING`, `NULLIF` va `* 1.0` bilan).
3. Dublikat tekshiruvi: `GROUP BY hudud_id, yil HAVING COUNT(*) > 1` (natija bo'sh bo'lishi kerak).

Natijani `print` bilan tartibli ko'rinishda chiqaring.

---

## Topshiriq 2 (11-dars): JOIN hisoboti · o'rta

1. `qabul_reja` jadvalini (agar yo'q bo'lsa) yarating va 4 ta yozuv kiriting.
2. Har bir hudud uchun nomi, 2024-yil o'quvchilar soni va rejani bitta jadvalda chiqaring (`LEFT JOIN`, reja yo'q bo'lsa `COALESCE(reja, 0)`).
3. `qabul_reja` da rejasi kiritilmagan hududlarni anti-join bilan alohida chiqaring.

---

## Topshiriq 3 (12-dars): CTE va CASE WHEN hisoboti · qiyin

1. CTE da 2024-yil uchun hududlar bo'yicha o'quvchi/o'qituvchi nisbatini hisoblang.
2. `CASE WHEN` bilan toifa bering: 14 dan katta `Yuqori`, 13 dan katta `O'rta`, qolgani `Normal`.
3. Toifalar bo'yicha hududlar sonini chiqaring (`GROUP BY toifa`).
4. Natijani Python orqali chiroyli chop eting.

---

## Topshiriq 4: O'z savolingiz · bonus

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

## Mentor uchun

**Tekshirish bo'yicha eslatmalar:**

- `uyga_vazifa_4.py` xatosiz ishlashi va uchta so'rovning natijasi mantiqan to'g'ri ekanini tekshiring.
- Topshiriq 1.2 da `WHERE` ichida agregat funksiya ishlatilmaganini (`HAVING` bo'lishi kerak) tekshiring.
- Topshiriq 2.2 da o'ng jadval sharti `ON` da turibdimi: `WHERE` ga qo'yilsa, `LEFT JOIN` ma'nosini yo'qotadi.
- Topshiriq 3 da `CASE` shartlari tartibi (kattadan kichikka) to'g'rimi.
- `RIGHT` / `FULL JOIN` ishlamasa, SQLite versiyasi 3.39 dan eski bo'lishi mumkin.

**Keng tarqalgan xatolar:**
1. `WHERE SUM(...) > ...` (agregat `WHERE` da).
2. `GROUP BY` da ustunni unutish.
3. `ON` ni unutish (Cartesian product).
4. `COUNT(*)` ni `LEFT JOIN` da ishlatib, bo'sh hududni 1 deb sanash.
5. `CASE` ni `END` bilan yopmaslik.
6. Integer bo'linma: `* 1.0` esdan chiqarish.
