---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "9-sinf (BI)", "link": "/9-sinf-bi/"}, "n": 3, "bob": "I-bob · Ma’lumotlar tahliliga kirish va Excel bilan ishlash", "lessons": [{"g": 7, "title": "Ma’lumotlarni tozalash (Data Cleaning) va transformatsiya", "lead": "Tahlilchining eng muhim mahorati: ortiqcha bo'shliqlar, xato formatlar va dublikatlardan xoli, 100% toza va sifatli ma'lumotlar to'plamini yaratish san'ati.", "link": "/9-sinf-bi/hafta-03/dars-1", "slide": "/slaydlar/9-sinf-bi/hafta-03/dars-1.html"}, {"g": 8, "title": "Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi", "lead": "Ma'lumotlar tahlilchisining eng kuchli quroli: birorta formula yozmasdan minglab qatorli ma'lumotlarni soniyalar ichida tahliliy hisobot va interaktiv dashboardga aylantirish!", "link": "/9-sinf-bi/hafta-03/dars-2", "slide": "/slaydlar/9-sinf-bi/hafta-03/dars-2.html"}, {"g": 9, "title": "Relatsion ma’lumotlar bazalari va model tushunchasi (1-qism): Jadvallar, Primary Key, Foreign Key va munosabatlar", "lead": "Dunyodagi barcha yirik axborot tizimlarining poydevori: ma'lumotlarni o'zaro bog'langan qat'iy jadvallar tizimida saqlash va boshqarish san'ati!", "link": "/9-sinf-bi/hafta-03/dars-3", "slide": "/slaydlar/9-sinf-bi/hafta-03/dars-3.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan.

---

### 7-dars: Ma’lumotlarni tozalash (Data Cleaning) va transformatsiya

1. Excelda 10 ta "nuqsonli" yozuvdan iborat jadval tayyorlang (ism-familiyasi kichik harflarda, boshida va oxirida ortiqcha bo'shliqlar bor, masalan: `"   anvar   hakimov   "`).
2. `=PROPER(TRIM(...))` formulalaridan foydalanib, butun ro'yxatni toza ko'rinishga keltiring.
3. Yangi ustunda `"Shahar, Tuman, Ko'cha"` ko'rinishidagi manzillarni `Text-to-Columns` (ajratgich: vergul) orqali 3 ta alohida ustunga bo'ling.
4. Jadvaldagi takroriy qatorlarni `Data > Remove Duplicates` orqali o'chiring.

---

### 8-dars: Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi

1. Excelda 15 ta xariddan iborat dataset tuzing (`Sana`, `Mijoz`, `Mahsulot`, `Summa`, `Shahar`).
2. Ushbu jadval asosida yangi varaqda PivotTable yarating: satrlarga `Shahar`, ustunlarga `Mahsulot`, qiymatlarga `Summa`ni qo'ying.
3. `Mahsulot` bo'yicha interaktiv `Slicer` qo'shing va qiymatlar formatini valyuta (`Currency`) ko'rinishiga sozlang.
4. Pivot jadvalga bog'langan `Clustered Column` PivotChart diagrammasini chizing.

---

### 9-dars: Relatsion ma’lumotlar bazalari va model tushunchasi: Jadvallar va kalitlar

1. O'zingiz qiziqqan soha (Kutubxona, Futbol klubi yoki Shifoxona) bo'yicha kamida 3 ta jadvaldan iborat relatsion model loyihalang.
2. Har bir jadvalning nomi, kamida 4 ta ustunini yozing.
3. Har bir jadvalda Primary Key (PK) ustunini belgilang.
4. Jadvallarni bir-biriga Foreign Key (FK) orqali bog'lang va munosabat turini (1:1, 1:N yoki oraliq jadval orqali M:N) aniq ko'rsating.

---

</div>
