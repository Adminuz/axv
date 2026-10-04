# 2-dars. Business Intelligence (BI) asoslari: Katta to'rtlik va hayotiy sikl

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga Business Intelligence (BI) mohiyati, zamonaviy biznesdagi vazifalari, tahlilning "Katta to'rtligi" (Deskriptiv, Diagnostik, Prediktiv, Preskriptiv), BI ekotizimining 5 ta tayanch komponenti hamda BI ning 6 bosqichli hayotiy siklini tushuntirish.
- **Kutiladigan natija:** O'quvchilar BI nima ekanini va an'anaviy hisobotdan qanday farqlanishini biladi; Katta to'rtlik tahlil turlarini real keyslar orqali ajrata oladi; ETL va Data Warehouse tushunchalarini tizimli tushunadi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (DIKW): 10 daqiqa
  - Yangi mavzu: BI ta'rifi va Katta to'rtlik: 25 daqiqa
  - BI komponentlari va hayotiy sikli: 20 daqiqa
  - Amaliy mashg'ulot (Keys tahlili): 15 daqiqa
  - Tezkor savol-javob va xulosa: 10 daqiqa

---

## Mentor konspekti

### 1. Business Intelligence (BI) nima?
Business Intelligence (BI) — bu tashkilotlarda ma’lumotlarni yig‘ish, tizimlashtirish, qayta ishlash, tahlil qilish va vizuallashtirish orqali to‘g‘ri, tez va strategik qarorlar qabul qilishni qo‘llab-quvvatlovchi texnologiyalar, metodlar va jarayonlar majmuasidir.
BI ning asosiy vazifasi:
$$\text{Xom Ma'lumot} \longrightarrow \text{Axborot} \longrightarrow \text{Tahliliy Tushuncha (Insight)} \longrightarrow \text{Boshqaruv Qarori}$$
zanjirini avtomatlashtirishdan iborat.

### 2. Tahlilning "Katta to'rtligi" (The BI’s Big Four)
Rasmiy darslikka ko'ra, biznes tahlili murakkablik va biznesga keltiradigan qiymat darajasiga qarab 4 toifaga bo'linadi:
1. **Tavsifiy (Deskriptiv) tahlil:** *"O‘tmishda nima sodir bo‘ldi?"*
   - O'tgan davrdagi sotuvlar, mijozlar soni, foyda va xarajatlarni umumlashtiradi.
   - Vositalar: oylik va yillik hisobotlar, KPI panellari.
2. **Diagnostik tahlil:** *"Nima uchun sodir bo‘ldi?"*
   - Anomaliyalar, savdo pasayishi yoki oshishi sabablarini (root causes) aniqlaydi.
   - Vositalar: detallarga chuqur kirish (drill-down), korrelyatsiya tahlili, ma'lumotlarni qidirish (Data Mining).
3. **Bashoratli (Prediktiv) tahlil:** *"Kelajakda nima sodir bo‘lishi mumkin?"*
   - Tarixiy ma'lumotlarga tayanib, kelajakdagi trendlar, ehtimollar va talab darajasini oldindan aytadi.
   - Vositalar: statistik modellar, regressiya tahlili, Machine Learning algoritmlari.
4. **Retseptiv (Preskriptiv) tahlil:** *"Eng yaxshi natijaga erishish uchun nima qilish kerak?"*
   - Tahlil piramidasining eng yuqori pog'onasi. Eng maqbul harakat yo'nalishini tavsiya etadi.
   - Vositalar: optimallashtirish algoritmlari, avtomatlashtirilgan qaror qabul qilish tizimlari (masalan, narxlarni dinamik boshqarish).

### 3. BI ekotizimining 5 ta asosiy komponenti
1. **Ma’lumot manbalari (Data Sources):** Ichki tizimlar (CRM, ERP, POS), tashqi manbalar va sensorlar.
2. **ETL jarayoni (Extract, Transform, Load):** Ma'lumotlarni turli manbalardan yig'ish (Extract), tozalash va standartlashtirish (Transform), omborga yuklash (Load).
3. **Ma’lumotlar ombori (Data Warehouse / Data Mart):** Tahlil uchun maxsus optimallashtirilgan, yagona ishonchli markaziy baza (Single Source of Truth).
4. **Semantik qatlam (Semantic Layer):** Murakkab kodlarni biznesga tushunarli ko'rsatkichlarga (KPI, sof foyda, konversiya) aylantiruvchi ko'prik.
5. **Vizuallashtirish vositalari (Visualization Tools):** Power BI, Tableau, interaktiv dashboardlar orqali natijalarni ko'rsatish.

### 4. BI tizimining hayotiy sikli (6 bosqich)
`Talablarni aniqlash` $\to$ `Ma'lumotlarni yig'ish` $\to$ `Tahlil va modellashtirish` $\to$ `Hisobot (Reporting)` $\to$ `Harakat (Acting)` $\to$ `Takrorlash (Iteration)`.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Tahlil turlarini aniqlash (oson)
Quyidagi vaziyatlar Katta to'rtlikning qaysi turiga kirishini aniqlang:
1. "Kompaniyamiz o'tgan oyda 120 mln so'mlik mahsulot sotdi".
2. "Sotuvlarning 15% ga pasayishiga asosiy raqobatchining 20% lik chegirma e'lon qilgani sabab bo'lgan".
3. "Kelasi oyda maktab formalariga talab 4 barobarga oshishi kutilmoqda".
4. "Ombordagi xarajatlarni 10% kamaytirish uchun har hafta 200 qutidan buyurtma berish optimal hisoblanadi".

**Yechim:**
1. Tavsifiy (Deskriptiv) — o'tmishda nima bo'lganini ko'rsatadi.
2. Diagnostik — hodisaning "nima uchun?" yuz bergan sababini aniqlaydi.
3. Bashoratli (Prediktiv) — kelajakdagi talabni taxmin qiladi.
4. Retseptiv (Preskriptiv) — maqsadga erishish uchun eng yaxshi yechimni tavsiya qiladi.

### 2-topshiriq. ETL jarayoni ketma-ketligi (o'rta)
Onlayn do'konga tegishli quyidagi amallarni ETL ning 3 ta bosqichiga ajrating:
- A: PostgreSQL bazasiga tozalangan buyurtmalar jadvalini joylashtirish.
- B: Telegram bot, veb-sayt va Instagram xabarlaridan mijoz ma'lumotlarini yuklab olish.
- C: Telefon raqamlarni yagona `+998...` formatiga keltirish, dublikat ismlarni o'chirish va bo'sh kataklarni to'ldirish.

**Yechim:**
- Extract (Olish): B (turli manbalardan yig'ish).
- Transform (O'zgartirish): C (formatlash, tozalash, dublikatlarni o'chirish).
- Load (Yuklash): A (markaziy omborga yuklash).

### 3-topshiriq. Supermarket uchun BI arxitekturasini loyihalash (qiyin)
Yirik supermarketlar tarmog'i mahsulotlarning yaroqlilik muddatini nazorat qilish va muddati o'tayotgan tovarlar bo'yicha yo'qotishlarni kamaytirmoqchi.
Ushbu muammoni hal qilish uchun Katta to'rtlikning barcha 4 ta tahlil turini o'z ichiga olgan reja tuzing.

**Yechim:**
1. *Tavsifiy:* O'tgan chorakda muddati o'tib ketgani sababli hisobdan chiqarilgan tovarlar ro'yxati va ularning umumiy zarari hisoblanadi.
2. *Diagnostik:* Nima sababdan ushbu tovarlar sotilmay qolgani o'rganiladi (narx qimmatmidi, peshtaxtaning ko'rinmas burchagidami yoki ortiqcha xarid qilinganmi?).
3. *Bashoratli:* Har bir tovar toifasining kunlik sotilish tezligiga qarab, kelasi 10 kun ichida qaysi mahsulotlarning muddati o'tib ketish xavfi yuqoriligi prognoz qilinadi.
4. *Retseptiv:* Tizim avtomatik ravishda yaroqlilik muddati tugashiga 3 kun qolgan tovarlarga 30% lik chegirma (sariq narx belgisi) belgilashni va ularni markaziy peshtaxtaga ko'chirishni tavsiya qiladi.

---

## Tezkor nazorat savollari

1. Deskriptiv va Diagnostik tahlil o'rtasidagi asosiy farq nima?
   - *Javob:* Deskriptiv tahlil "Nima bo'ldi?" savoliga, Diagnostik esa "Nima uchun bo'ldi?" savoliga javob beradi.
2. ETL qisqartmasi nimani anglatadi va uning eng murakkab bosqichi qaysi?
   - *Javob:* Extract, Transform, Load. Eng ko'p vaqt va mehnat talab qiladigan bosqich — Transform (ma'lumotlarni tozalash va standartlashtirish).
3. Data Warehouse nima uchun kundalik operatsion bazalardan alohida saqlanadi?
   - *Javob:* Chunki kundalik savdo tizimi sekinlashib qolmasligi va tarixiy tahlillar uchun yaxlit yagona manba yaratish uchun.

---

## Uyga vazifa

O'zingiz tanlagan biror biznes (masalan, kofe do'koni, avtomobil yuvish shoxobchasi yoki xususiy klinika) uchun Katta to'rtlikning har bir turiga mos 1 tadan hayotiy misol tuzing (jami 4 ta jumla).
