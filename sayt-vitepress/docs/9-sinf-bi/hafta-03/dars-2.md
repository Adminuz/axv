---
title: "8-dars. Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (BI)", "link": "/9-sinf-bi/"}, "week": {"n": 3, "link": "/9-sinf-bi/hafta-03/"}, "g": 8, "title": "Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi", "lead": "Ma'lumotlar tahlilchisining eng kuchli quroli: birorta formula yozmasdan minglab qatorli ma'lumotlarni soniyalar ichida tahliliy hisobot va interaktiv dashboardga aylantirish!", "slide": "/slaydlar/9-sinf-bi/hafta-03/dars-2.html", "tabs": [{"g": 7, "link": "/9-sinf-bi/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/9-sinf-bi/hafta-03/dars-2", "current": true}, {"g": 9, "link": "/9-sinf-bi/hafta-03/dars-3", "current": false}], "prev": {"g": 7, "title": "Ma’lumotlarni tozalash (Data Cleaning) va transformatsiya", "link": "/9-sinf-bi/hafta-03/dars-1"}, "next": {"g": 9, "title": "Relatsion ma’lumotlar bazalari va model tushunchasi (1-qism): Jadvallar, Primary Key, Foreign Key va munosabatlar", "link": "/9-sinf-bi/hafta-03/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **PivotTable (Yig'ma jadval)** — bu katta hajmdagi xom ma'lumotlar to'plamini hech qanday formulalar yozmasdan, sichqoncha yordamida (drag-and-drop) bir zumda umumlashtirish, guruhlash va ko'p o'lchovli tahliliy hisobotlarga aylantirish imkonini beruvchi vositadir.
- Pivot jadval yaratish uchun ma'lumotlar jadvalidagi istalgan katakka bosilib, `Insert > PivotTable` tanlanadi (yoki klaviaturada `Alt + N + V`).
- **PivotTable Field List 4 ta asosiy maydondan iborat:**
  1. **Rows (Qatorlar):** Qaysi toifalar bo'yicha guruhlash kerakligini belgilaydi (masalan, Viloyat, Mahsulot).
  2. **Columns (Ustunlar):** Ustunlar bo'ylab ikkinchi o'lchovni (kesimni) qo'yish (masalan, Yillar yoki Oylar).
  3. **Values (Qiymatlar):** Hisoblanadigan sonli ko'rsatkichlar (Savdo summasi, Tovar soni).
  4. **Filters (Filtrlar):** Butun hisobotni bitta parametr bo'yicha global saralash.
- **Value Field Settings:** Qiymatlar ustiga o'ng tugma bosilib, hisoblash turini o'zgartirish mumkin (`Sum`, `Average`, `Count`, `Max`, `Min`), shuningdek, `Show Values As > % of Grand Total` orqali foiz ulushini hisoblash mumkin.
- **Sanalarni guruhlash (Date Grouping):** Sana ustuni Rows ga qo'yilganda, Excel ularni avtomatik yoki qo'lda `Oylar`, `Choraklar` va `Yillar` bo'yicha guruhlab beradi.
- **Slicer va Timeline:** Slicer — toifalar bo'yicha chiroyli interaktiv tugmalar bloki, Timeline esa sanalar uchun qulay vaqt slayderi. Ular Pivot jadvallar va grafiklarni bitta bosishda filtrlaydi.
- **PivotChart:** PivotTable bilan chambarchas bog'langan dinamik diagramma bo'lib, filtr o'zgarganda diagramma ham bir zumda avtomatik qayta chiziladi.
- **Refresh (Alt + F5):** Asosiy manba jadvalga yangi ma'lumotlar qo'shilganda yoki o'zgartirilganda, PivotTable avtomatik yangilanmaydi — `Refresh` tugmasini bosish shart!

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega formulalar o'rniga PivotTable?
Tasavvur qiling, sizda 10 000 ta savdo qatori bor. Agar har bir viloyat va mahsulot kesimida sotuvlarni hisoblamoqchi bo'lsangiz, o'nlab `SUMIFS` formulalarini yozib chiqishingiz kerak bo'lardi.
PivotTable yordamida esa:
- `Viloyat`ni Rows ga tashlaysiz;
- `Mahsulot`ni Columns ga tashlaysiz;
- `Summa`ni Values ga tashlaysiz.
Bor-yo'g'i 3 ta sichqoncha harakati va 5 soniya ichida to'liq hisobot tayyor!

### 2. Slicerlarning kuchi: Bir nechta jadvalni bitta tugma bilan boshqarish
Slicer shunchaki oddiy filtr emas. Bitta Slicerni `Report Connections` orqali bir nechta Pivot jadval va PivotChartga ulash mumkin.
Bunda siz bitta tugmani (masalan, "Samarqand") bossangiz, sahifadagi barcha jadvallar va diagrammalar bir vaqtda faqat Samarqand ko'rsatkichlariga moslashadi. Bu haqiqiy professional **BI Dashboard** yaratish imkonini beradi.

### 3. Grand Total va Subtotal boshqaruvi
PivotTable dizayn menyusida (`Design tab`):
- `Subtotals`: Quyi guruhlar bo'yicha oraliq jami yig'indilarni yoqish/o'chirish;
- `Grand Totals`: Jadval oxiridagi umumiy jami satr va ustunlarni boshqarish;
- `Report Layout`: `Compact Form`, `Outline Form` yoki jadvalli `Tabular Form` ko'rinishlariga o'tish imkonini beradi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **PivotTable** | Katta hajmdagi ma'lumotlarni dinamik umumlashtiruvchi va guruhlovchi yig'ma jadval. |
| **Rows (Qatorlar)** | Jadvalning chap tomonidagi satrlar bo'ylab guruhlanuvchi toifalar maydoni. |
| **Columns (Ustunlar)** | Jadval ustunlari bo'ylab ikkinchi o'lchovni hosil qiluvchi maydon. |
| **Values (Qiymatlar)** | Yig'indi, o'rtacha, son kabi matematik hisob-kitoblar bajariladigan sonli maydon. |
| **Filters (Filtrlar)** | Butun hisobot ma'lumotlarini bitta parametr bo'yicha global elakdan o'tkazuvchi maydon. |
| **Value Field Settings** | Qiymatlar maydonidagi hisoblash turini (Sum, Count, Average) va formatini sozlash oynasi. |
| **Grouping** | Sonlar yoki sanalarni oraliqlar (oylar, choraklar, 10-20 oralig'i) bo'yicha birlashtirish. |
| **Slicer** | Jadval va grafiklarni vizual tugmalar yordamida bir bosishda filtrlash vositasi. |
| **Timeline** | Faqat sana maydonlari uchun mo'ljallangan maxsus interaktiv vaqt slayderi. |
| **PivotChart** | PivotTable ma'lumotlariga to'g'ridan-to'g'ri bog'langan dinamik grafik va diagramma. |
| **Refresh (Alt+F5)** | Manba jadvaldagi o'zgarishlarni PivotTablega qayta yuklash va yangilash buyrug'i. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- PivotTable texnologiyasi 1986-yilda **Pito Salas** tomonidan o'ylab topilgan va ilk bor 1991-yilda Steve Jobsning NeXT kompyuterlari uchun yaratilgan *Lotus Improv* dasturida namoyish etilgan.
- Microsoft bu ajoyib g'oyani 1994-yilda **Excel 5.0** versiyasiga `PivotTable` nomi ostida qo'shgan va u bugungi kunda dunyodagi eng mashhur tahliliy vositaga aylangan.
- PivotTable xotirada ma'lumotlarni tezkor saqlash uchun **Pivot Cache** nomli maxsus virtual xotira qatlamidan foydalanadi. Aynan shu sababli millionlab qatorlar ustida ham soniyalar ichida hisob-kitob qiladi!
- Dunyo bo'yicha Exceldan foydalanuvchi 1 milliarddan ortiq insonlarning faqat **5-10 foizi** PivotTable bilan professional darajada ishlay oladi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Birinchi PivotTable yaratish <Badge type="tip" text="oson" />
Savdo jadvali (`Mijoz`, `Shahar`, `Tovar`, `Summa`) asosida yangi ishchi varaqda PivotTable tuzing. Satrlarga `Shahar`, qiymatlarga `Summa` maydonini joylashtiring.
**Kutiladigan natija:** Har bir shahar bo'yicha umumiy savdo summasi hisoblangan ixcham jadval.

### 2. Hisoblash turini o'zgartirish (Average) <Badge type="tip" text="oson" />
Tuzilgan PivotTableda `Sum of Summa` ustuniga o'ng tugmani bosib, `Value Field Settings` orqali hisoblash turini `Average` (o'rtacha savdo cheki) ga o'zgartiring.
**Kutiladigan natija:** Shaharlar bo'yicha o'rtacha xarid summalari ko'rsatilgan ustun.

### 3. Bitimlar sonini sanash (Count) <Badge type="tip" text="oson" />
`Summa` maydonini ikkinchi marta Values maydoniga tashlang va uning hisoblash turini `Count` qilib sozlang.
**Kutiladigan natija:** Bir jadvalda ham umumiy summa, ham har bir shaharda nechta bitim tuzilgani soni chiqishi.

### 4. 2 o'lchovli kross-jadval (Matrix) <Badge type="tip" text="oson" />
Satrlarda `Shahar`, ustunlarda esa `Tovar` toifasi joylashgan 2 o'lchovli kross-jadval tuzing. Qiymatlar maydoniga sotuv summasini qo'ying.
**Kutiladigan natija:** Qatorlarida shaharlar, ustunlarida tovarlar kesishgan ko'p o'lchovli matritsa.

### 5. Valyuta formatini o'rnatish <Badge type="warning" text="o'rta" />
PivotTable'dagi raqamlar ustiga o'ng tugmani bosib, `Number Format > Currency` orqali so'm (yoki dollar) formatini o'rnating, kasr qismini nolga tenglang.
**Kutiladigan natija:** Barcha sonlar `1 250 000 so'm` ko'rinishida formatlangan jadval.

### 6. Sanalarni oylar bo'yicha guruhlash (Grouping) <Badge type="warning" text="o'rta" />
Jadvalning `Sana` ustunini Rows ga joylashtiring. Kunlik sanalarni o'ng tugma orqali `Group` qilib, `Months` va `Quarters` (oylar va choraklar) bo'yicha guruhlang.
**Kutiladigan natija:** Kunlik uzun ro'yxat o'rniga 4 ta chorak va oylar bo'yicha umumlashtirilgan ko'rinish.

### 7. Slicer ulab filtrlash <Badge type="warning" text="o'rta" />
PivotTable menyusidan `Insert Slicer` orqali `Tovar` maydoniga interaktiv tugmalar to'plamini qo'shing. Istalgan tovarni bosib jadval filtrlanishini sinang.
**Kutiladigan natija:** Tugmalar orqali bir bosishda boshqariladigan dinamik jadval.

### 8. Foiz ulushini hisoblash (% of Grand Total) <Badge type="danger" text="qiyin" />
`Summa` ustunining sozlamalaridan `Show Values As` bo'limiga kiring va `% of Grand Total` variantini tanlang.
**Kutiladigan natija:** Har bir shahar yoki tovarning umumiy savdodagi foiz ulushi (% da) aks etgan ustun.

### 9. PivotChart va Timeline bilan dashboard <Badge type="danger" text="qiyin" />
PivotTable asosida `Clustered Column` PivotChart chizing. Unga sana bo'yicha `Timeline` qo'shing. Timeline orqali faqat ma'lum bir oyni tanlaganingizda grafik qanday o'zgarishini tekshiring.
**Kutiladigan natija:** Bir-biri bilan sinxron ishlovchi interaktiv diagramma va vaqt slayderi.

### 10. Pivot Cache va yangilash (Refresh) testi <Badge type="info" text="bonus" />
Manba jadvalga yangi shahar ("Buxoro", 5 000 000 so'm) qatorini qo'shing. PivotTablega o'tib, nima uchun yangi shahar darhol ko'rinmaganini tushuntiring va `Alt + F5` orqali yangilang.
**Kutiladigan natija:** Pivot Cachening ishlash mexanizmini amalda ko'rish va Refresh amali natijasida Buxoro shahrining jadvalga qo'shilishi.

</div>

