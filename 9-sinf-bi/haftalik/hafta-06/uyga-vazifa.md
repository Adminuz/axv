# 6-hafta: Uyga vazifa

**Fan:** Business Intelligence  
**Sinf:** 9-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: Aggregatsiya funksiyalari · qiyin

1. `Mahsulotlar` bo'yicha: mahsulotlar soni, jami dona, eng arzon va eng qimmat narx, o'rtacha narx — bitta so'rovda, har bir ustunga nom bering.
2. `Sotuvlar` bo'yicha Buxorodagi sotuvlar soni va yig'indisini toping.
3. `COUNT(*)` va `COUNT(Chegirma)` ni bitta so'rovda chiqaring; farqini yozma izohlang.
4. `AVG(Miqdor)` va `AVG(CAST(Miqdor AS DECIMAL(10,2)))` natijalarini solishtiring va nima uchun farq qilishini tushuntiring.

---

## Topshiriq 2: GROUP BY va guruhlash · o'rta

1. Har bir shahar bo'yicha sotuvlar soni, jami summa va o'rtacha summani bitta so'rovda chiqaring; jami bo'yicha kamayish tartibida saralang.
2. Har bir toifa bo'yicha eng katta va eng kichik summani toping.
3. `Shahar, Kategoriya` bo'yicha guruhlab, sotuvlar sonini chiqaring.
4. `WHERE Sana >= '2024-03-03'` bilan shaharlar bo'yicha yig'indini hisoblang (Buxoro 3 280 000, Samarqand 2 140 000, Toshkent 3 320 000 chiqishi kerak).
5. `SELECT Shahar, Summa ... GROUP BY Shahar` xatosini yozing, xabarni o'qing va tuzating.

---

## Topshiriq 3: HAVING va WHERE · oson

1. Jami summasi 5 000 000 dan oshgan shaharlarni toping (Samarqand va Toshkent chiqishi kerak).
2. Kamida 3 ta sotuvi bo'lgan toifalarni toping va sotuvlar sonini chiqaring.
3. Aksessuar sotuvlari bo'yicha shaharlar jamini hisoblab, 200 000 dan oshganlarini qoldiring (Toshkent 280 000, Samarqand 240 000).
4. So'rovning mantiqiy bajarilish tartibini o'z so'zlaringiz bilan 6 qadamda yozing.
5. `WHERE SUM(Summa) > 4000000` so'rovidagi xatoni tushuntiring va to'g'rilang.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: Mahsulotlar va Sotuvlar bo'yicha aggregatsiya so'rovlari | 3 |
| 17-dars: GROUP BY: shahar va toifa bo'yicha hisobotlar | 3 |
| 18-dars: HAVING va WHERE bilan hisobotlar | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: INT ustunida AVG nima uchun butun chiqadi?? Javobi: SQL Server butun turdagi natija qaytaradi; CAST AS DECIMAL kerak.
- 17-dars: GROUP BY da alias ishlaydimi?? Javobi: Yo'q; alias faqat ORDER BY da ishlaydi.
- 18-dars: HAVING qayerga yoziladi?? Javobi: GROUP BY dan keyin, ORDER BY dan oldin.

**Keng tarqalgan xatolar:**
- 16-dars: COUNT(*) va COUNT(ustun) ni aralashtirish.
- 17-dars: SELECT da guruhlanmagan va aggregatsiyasiz ustun yozish.
- 18-dars: Aggregatsiyani WHERE ichida yozish.
