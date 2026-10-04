# 8-dars. Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga Excelda PivotTable (yig'ma jadval) yaratish texnologiyasi, uning 4 ta asosiy maydoni (Rows, Columns, Values, Filters), Value Field Settings hisob-kitoblari, sana va sonlarni guruhlash (Grouping), interaktiv Slicerlar va Timeline bilan ishlash hamda PivotChart vositasi orqali tahliliy dashboardlar qurishni o'rgatish.
- **Kutiladigan natija:** O'quvchilar yuzlab qatorli savdo datasetini formulalarsiz 1 daqiqada umumlashtira oladi; Rows, Columns va Values maydonlarini to'g'ri joylashtiradi; Slicerlar orqali interaktiv filtr ulay oladi va PivotChart diagrammalari bilan vizual xulosalar chiqara oladi.
- **Vaqt taqsimoti:**
  - O'tgan darsni takrorlash (Data Cleaning): 10 daqiqa
  - Yangi mavzu: PivotTable tushunchasi va 4 ta maydon: 20 daqiqa
  - Value Field Settings, Guruhlash va Slicerlar: 25 daqiqa
  - PivotChart va vizual tahlil amaliyoti: 15 daqiqa
  - Nazorat savollari va xulosa: 10 daqiqa

---

## Mentor konspekti

### 1. PivotTable (Yig'ma jadval) nima?
PivotTable — bu katta hajmdagi xom ma'lumotlar to'plamini hech qanday formulalar yozmasdan, sichqoncha yordamida (drag-and-drop) bir zumda guruhlash, umumlashtirish va ko'p o'lchovli tahliliy hisobotlarga aylantirish imkonini beruvchi Excelning eng kuchli analitik vositasidir.
- **PivotTable yaratish:**
  1. Jadval ichidagi istalgan katakka bosiladi.
  2. `Insert > PivotTable` tanlanadi.
  3. `New Worksheet` (Yangi varaq) belgilanadi va `OK` bosiladi.
  4. Tezkor tugmalar: `Alt + N + V` (Windows).

### 2. PivotTable Field List — 4 ta maydon arxitekturasi
Pivot jadval ochilganda o'ng tomonda 4 ta hudud paydo bo'ladi:
1. **Rows (Qatorlar):** Qaysi toifalar bo'yicha guruhlash kerakligini belgilaydi (masalan, Mahsulot nomi, Filial, Menejer).
2. **Columns (Ustunlar):** Ustunlar bo'ylab ikkinchi o'lchovni qo'yish (masalan, Yillar yoki Oylar kesimi).
3. **Values (Qiymatlar):** Hisoblanadigan raqamli ko'rsatkichlar (Savdo summasi, Tovar soni).
4. **Filters (Filtrlar):** Butun hisobotni tepadagi bitta parametr (masalan, Mamlakat) bo'yicha saralash.

### 3. Value Field Settings va Sanalarni guruhlash (Grouping)
- **Value Field Settings:**
  - Qiymat ustiga o'ng tugma bosilib, hisoblash turini o'zgartirish mumkin: `Sum`, `Average`, `Count`, `Max`, `Min`.
  - `Show Values As > % of Grand Total`: umumiy tushumga nisbatan har bir toifaning foiz ulushini hisoblaydi.
- **Sanalarni guruhlash (Date Grouping):**
  - Sana katagiga o'ng tugma bosib `Group...` tanlansa, kunlik sanalarni avtomatik ravishda `Oylar`, `Choraklar` va `Yillar` bo'yicha guruhlab beradi.

### 4. Interaktiv filtrlar: Slicer va Timeline
- **Slicer (Kesuvchi):** `Insert > Slicer` orqali toifalar (masalan, Viloyatlar) bo'yicha interaktiv tugmalar bloki yaratiladi. Bitta tugmani bossangiz, Pivot jadval darhol o'sha viloyat bo'yicha qayta hisoblanadi.
- **Timeline (Vaqt chizig'i):** Sanalar uchun interaktiv vaqt slayderi.

### 5. PivotChart bilan vizualizatsiya
Pivot jadval asosida `Insert > PivotChart` orqali dinamik diagramma ulanadi:
- **Column Chart (Ustunli):** Kategoriyalar bo'yicha solishtirish uchun.
- **Line Chart (Chiziqli):** Vaqt bo'yicha o'zgarishlar (trendlar) uchun.
- **Pie / Donut Chart:** Bozor ulushlari va foizlarni ko'rsatish uchun.
- **Refresh muhimligi:** Agar asosiy jadvalga yangi qatorlar qo'shilsa, PivotTable Analyze menyusidan `Refresh` (Alt + F5) bosilishi shart!

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Oddiy PivotTable tuzish (oson)
100 ta savdo yozuvidan iborat jadval berilgan: `Sana`, `Viloyat`, `Kategoriya`, `Summa`.
Viloyatlar kesimida umumiy savdo summasini hisoblovchi PivotTable yarating.

**Yechim:**
1. Jadval tanlanadi va `Insert > PivotTable > New Worksheet` bosiladi.
2. `Viloyat` maydoni sudrab `Rows` hududiga tashlanadi.
3. `Summa` maydoni sudrab `Values` hududiga tashlanadi (avtomatik `Sum of Summa` chiqadi).

### 2-topshiriq. 2 o'lchovli kross-jadval va oylar bo'yicha guruhlash (o'rta)
O'tgan topshiriqdagi jadvalga:
1. `Kategoriya` maydonini `Columns` hududiga joylashtiring.
2. `Summa` qiymat sozlamalaridan `Value Field Settings > Number Format > Currency` qilib sozlang.
3. `Kategoriya` bo'yicha `Slicer` qo'shing va interaktiv filtrlashni sinang.

**Yechim:**
1. Kategoriya `Columns` ga o'tkazilganda satrlarda Viloyat, ustunlarda esa Kategoriya bo'lgan kross-jadval (Matrix) hosil bo'ladi.
2. Qiymatlar formatiga so'm/valyuta belgisi ulanadi.
3. `PivotTable Analyze > Insert Slicer` orqali Kategoriya belgilanadi va tugmali filtr ulanadi.

### 3-topshiriq. PivotChart va Dashboard yaratish (qiyin)
PivotTable asosida:
1. Viloyatlar bo'yicha sotuvlarni aks ettiruvchi `Clustered Column` PivotChart yarating.
2. `Values` dagi ikkinchi ustunni `% of Grand Total` qilib qo'shing.
3. `Timeline` qo'shib, faqat 2-chorak savdolarini ajrating va grafika qanday avtomatik o'zgarishini kuzating.

**Yechim:**
1. PivotTable tanlanib, `Insert > PivotChart > Clustered Column` chiziladi.
2. `Summa` maydoni yana bir bor `Values` ga tashlanadi, o'ng tugma bosilib `Show Values As > % of Grand Total` tanlanadi.
3. `Insert > Timeline` bosilib, Sana ustuni tanlanadi, davr filtri `Quarters > Q2` qilib belgilanadi.

---

## Tezkor nazorat savollari

1. PivotTable Field List ning qaysi maydoni hisoblanadigan sonli ko'rsatkichlarni qabul qiladi?
   - *Javob:* Values (Qiymatlar) maydoni.
2. Manba jadvalga yangi qatorlar qo'shilganda PivotTable avtomatik yangilanadimi?
   - *Javob:* Yo'q, `Refresh` (Alt + F5) tugmasini bosish kerak bo'ladi.
3. Slicer vositasi oddiy filtrdan nimasi bilan ustun turadi?
   - *Javob:* Interaktiv tugmalar shaklida bo'lib, bir vaqtning o'zida bir nechta Pivot jadval va grafiklarni bitta bosishda boshqara oladi.

---

## Uyga vazifa

Excelda 15 ta xariddan iborat dataset tuzing (`Sana`, `Mijoz`, `Mahsulot`, `Summa`, `Shahar`).
Ushbu jadval asosida yangi varaqda PivotTable yarating: satrlarga `Shahar`, ustunlarga `Mahsulot`, qiymatlarga `Summa`ni qo'ying. Slicer ulab, qulay ko'rinishga keltiring.
