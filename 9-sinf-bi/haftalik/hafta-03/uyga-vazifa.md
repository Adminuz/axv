# 3-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

## 7-dars: Ma’lumotlarni tozalash (Data Cleaning) va transformatsiya

1. Excelda 10 ta "nuqsonli" yozuvdan iborat jadval tayyorlang (ism-familiyasi kichik harflarda, boshida va oxirida ortiqcha bo'shliqlar bor, masalan: `"   anvar   hakimov   "`).
2. `=PROPER(TRIM(...))` formulalaridan foydalanib, butun ro'yxatni toza ko'rinishga keltiring.
3. Yangi ustunda `"Shahar, Tuman, Ko'cha"` ko'rinishidagi manzillarni `Text-to-Columns` (ajratgich: vergul) orqali 3 ta alohida ustunga bo'ling.
4. Jadvaldagi takroriy qatorlarni `Data > Remove Duplicates` orqali o'chiring.

---

## 8-dars: Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi

1. Excelda 15 ta xariddan iborat dataset tuzing (`Sana`, `Mijoz`, `Mahsulot`, `Summa`, `Shahar`).
2. Ushbu jadval asosida yangi varaqda PivotTable yarating: satrlarga `Shahar`, ustunlarga `Mahsulot`, qiymatlarga `Summa`ni qo'ying.
3. `Mahsulot` bo'yicha interaktiv `Slicer` qo'shing va qiymatlar formatini valyuta (`Currency`) ko'rinishiga sozlang.
4. Pivot jadvalga bog'langan `Clustered Column` PivotChart diagrammasini chizing.

---

## 9-dars: Relatsion ma’lumotlar bazalari va model tushunchasi: Jadvallar va kalitlar

1. O'zingiz qiziqqan soha (Kutubxona, Futbol klubi yoki Shifoxona) bo'yicha kamida 3 ta jadvaldan iborat relatsion model loyihalang.
2. Har bir jadvalning nomi, kamida 4 ta ustunini yozing.
3. Har bir jadvalda Primary Key (PK) ustunini belgilang.
4. Jadvallarni bir-biriga Foreign Key (FK) orqali bog'lang va munosabat turini (1:1, 1:N yoki oraliq jadval orqali M:N) aniq ko'rsating.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **7-dars vazifasi (30 ball):** TRIM va PROPER formulalari to'g'ri biriktirilgani, Text-to-Columns vositasi to'g'ri qo'llangani va dublikatlar tozalangani.
- **8-dars vazifasi (35 ball):** PivotTable maydonlari (Rows, Columns, Values) to'g'ri joylashtirilgani, Slicer ulanishi va PivotChart mavjudligi.
- **9-dars vazifasi (35 ball):** 3 ta jadvalning mantiqiy to'g'riligi, Primary Key (unikal, bo'sh bo'lmagan) va Foreign Key bog'lanishlarining referensial yaxlitlik qoidalariga mosligi.

### Eslatma
- O'quvchi M:N munosabatni to'g'ridan-to'g'ri bog'lamasdan, oraliq ko'prik jadvali (Junction table) orqali yechgan bo'lsa, qo'shimcha rag'batlantiruvchi ball beriladi.
