# 6-hafta: Uyga vazifa

**Fan:** Android dasturlash  
**Sinf:** 9-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: Kolleksiyalar: List, Set, Map · qiyin

1. `mutableListOf` bilan 5 ta mahsulot ro'yxatini yarating; 1 ta qo'shing, 1 ta o'chiring va natijani `println` bilan chiqaring.
2. Mahsulot → narx `mutableMapOf` yarating, bir narxni yangilang va `for ((nom, narx) in map)` bilan hisobot chiqaring.
3. `listOf(5, 3, 5, 1, 3)` dan takrorlarni olib tashlang va natijani izohlang.
4. Kod yozish imkoni bo'lmasa: List, Set va Map uchun bittadan kundalik hayotdan misol va ularni yozish usulini daftarga yozing.

---

## Topshiriq 2: Lambda, filter, map, forEach · o'rta

1. 1..20 oralig'idan `filter` bilan 3 ga bo'linadiganlarni tanlang va `map` bilan kvadratini chiqaring.
2. Mahsulot → narx Map yarating (6 ta); narxi o'rtachadan yuqori mahsulotlar nomlarini `filter`, `map` va `forEach` bilan chiqaring.
3. Ism ro'yxatidan faqat 4 ta harfdan uzun ismlarni tanlab, katta harflarda chiqaring.
4. Kod yozish imkoni bo'lmasa: `filter`, `map`, `forEach` farqini misol bilan daftarga yozing.

---

## Topshiriq 3: OOP asoslari va inkapsulyatsiya · oson

1. `BankHisobi` sinfini yozing: `egasi`, `private set` bilan `balans`, `qoshish()` va `yechish()` metodlari (qoidalar bilan). `main()` da sinab ko'ring.
2. `Oquvchi` sinfida `baho` xossasiga maxsus setter yozing (0..100) va 3 xil qiymat bilan tekshiring.
3. `private` xossaga tashqaridan murojaat qilib, kompilyator xatosini daftarga ko'chiring va sababini yozing.
4. Kod yozish imkoni bo'lmasa: 4 ta kirish modifikatorining farqini misollar bilan jadvalda yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: Kolleksiyalar bilan «Omborxona» dasturi | 3 |
| 17-dars: filter, map, forEach bilan mahsulotlarni qayta ishlash | 3 |
| 18-dars: BankHisobi: inkapsulyatsiya va private set | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: Kalit yo'q bo'lsa map[kalit] nima qaytaradi?? Javobi: null.
- 17-dars: forEach nima qaytaradi?? Javobi: Hech narsa (Unit).
- 18-dars: protected qayerda ko'rinadi?? Javobi: Sinf va merosxo'rlarida.

**Keng tarqalgan xatolar:**
- 16-dars: listOf ga add yozish.
- 17-dars: filter natijasini o'zgaruvchiga saqlamaslik.
- 18-dars: Hamma xossani public qoldirish.
