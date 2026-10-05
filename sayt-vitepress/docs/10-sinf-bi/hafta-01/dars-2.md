---
title: "2-dars. 2-dars: Ma'lumotlar arxitekturasi va hayot sikli (Data Architecture & Data Lifecycle)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 1, "link": "/10-sinf-bi/hafta-01/"}, "g": 2, "title": "2-dars: Ma'lumotlar arxitekturasi va hayot sikli (Data Architecture & Data Lifecycle)", "lead": "Ma'lumotlar arxitekturasi va hayot sikli (6 qatlam, 7 bosqich, Data Quality mezonlari)", "slide": "/slaydlar/10-sinf-bi/hafta-01/dars-2.html", "test": "/slaydlar/10-sinf-bi/hafta-01/dars-2-test.html", "tabs": [{"g": 1, "link": "/10-sinf-bi/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/10-sinf-bi/hafta-01/dars-2", "current": true}, {"g": 3, "link": "/10-sinf-bi/hafta-01/dars-3", "current": false}], "prev": {"g": 1, "title": "1-dars: Ma’lumotlar muhandisligiga kirish (Data Engineering asoslari)", "link": "/10-sinf-bi/hafta-01/dars-1"}, "next": {"g": 3, "title": "3-dars: Ma’lumot formatlari: CSV va JSON bilan ishlash", "link": "/10-sinf-bi/hafta-01/dars-3"}}
---

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Mavzu:** Ma'lumotlar arxitekturasi qatlamlari, Data Lifecycle 7 bosqichi, Data Quality mezonlari va Maktab tahliliy platformasi loyihasi  

---

<div class="blk">

## <Icon name="file-text" /> Nazariy konspekt

### 1. Ma’lumotlar arxitekturasi (Data Architecture) qatlamlari

Ma’lumotlar arxitekturasi — ma’lumotlar qayerdan kelishi, qanday saqlanishi, qanday tozalanishi va kimga qanday ko‘rinishda taqdim etilishini belgilab beruvchi yuqori darajadagi loyihadir.

Asosiy 6 ta qatlam:
1. **Source layer (Manbalar):** Ma'lumot paydo bo'ladigan joylar (maktab LMS tizimlari, Excel jurnallar, API, sensorlar).
2. **Ingestion layer (Yig‘ish):** Ma'lumotlarni qabul qilish (fayl import, avtomatlashtirilgan oqimlar).
3. **Storage layer (Saqlash):** Xom ma'lumotlar saqlanadigan Raw zona (Data Lake) va tahliliy ma'lumotlar ombori (Data Warehouse).
4. **Processing/Transform layer (Qayta ishlash):** Tozalash, duplikatlarni yo'qotish, agregatsiya (ETL/ELT jarayonlari).
5. **Serving layer (Taqdim etish):** BI dashboardlar (Power BI, Tableau), tahliliy hisobotlar va ML modellari uchun yetkazib berish.
6. **Governance & Observability (Boshqaruv va kuzatuv):** Sifat nazorati, xatolar monitoringi, loglar va xavfsizlik.

---

### 2. Ma’lumotlar hayot sikli (Data Lifecycle) - 7 bosqich

Ma’lumot o‘z faoliyati davomida quyidagi 7 bosqichni bosib o‘tadi:
1. **Collect / Ingest (Yig'ish):** Ma'lumotni tashqi manbalardan tizimga kiritish.
2. **Store (Saqlash):** Xom ma'lumotni o'zgartirmasdan saqlash (raw zone).
3. **Validate / Clean (Tekshirish va tozalash):** Xato qiymatlar, duplikatlar va bo'shliqlarni aniqlash hamda tuzatish.
4. **Transform (O'zgartirish):** Biznes talablariga mos hisoblashlar va formatlash.
5. **Serve / Publish (Taqdim etish):** Tahlilchilar va qaror qabul qiluvchilarga yetkazish.
6. **Monitor / Log (Kuzatuv):** Quvurning ishlashi, vaqti va xatolarini qayd etish.
7. **Archive / Retention (Arxivlash):** Eskirgan ma'lumotlarni arxivlash yoki xavfsiz saqlash.

---

### 3. Data Quality (Ma'lumotlar sifati)ning 4 ta asosiy mezoni

Har qanday tahliliy tizim va sun'iy intellekt modeli to'g'ri ishlashi uchun ma'lumotlar 4 ta talabga javob berishi kerak:
- **Completeness (To'liqlik):** Barcha zaruriy ustunlar to'ldirilgan bo'lishi, kritik maydonlarda bo'sh (null) qiymatlar bo'lmasligi.
- **Accuracy (Aniqlik):** Ma'lumotlar haqiqatga mos kelishi (masalan, o'quvchilar soni manfiy bo'lmasligi).
- **Consistency (Izchillik):** Barcha jadvallarda yagona standart format qo'llanishi (masalan, viloyat nomlari bir xil yozilishi).
- **Timeliness (O'z vaqtidalik):** Ma'lumotning o'z vaqtida yangilangan bo'lishi.

---

### 4. Loyiha keysi: "Maktab tahliliy platformasi"

Platformaning asosiy foydalanuvchi rollari:
- **Direktor / MMTB rahbari:** Hududlar kesimida umumiy ko'rsatkichlarni, o'quvchi/maktab va o'quvchi/o'qituvchi resurs yuklamasini kuzatadi.
- **Analitik:** Yillik dinamika (YoY), hududlar reytingi va 3 yillik harakatlanuvchi o'rtacha (moving average) ko'rsatkichlarini hisoblaydi.
- **Administrator (Data Operator):** Xom fayllarni qabul qiladi, Profiling va Validation o'tkazadi, ma'lumotlarni tozalab bazaga yuklaydi va loglarni tekshiradi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1-topshiriq: Arxitektura qatlamlarini moslashtirish <Badge type="tip" text="oson" />
Quyidagi amallarning har biri Data Architecture'ning qaysi qatlamiga tegishli ekanini aniqlang:
a) Maktab o'qituvchilari har kuni baholarni kiritadigan elektron kundalik tizimi;  
b) Har kecha soat 02:00 da barcha hududiy fayllarni bitta omborga nusxalovchi dastur;  
c) Viloyat xalq ta'limi boshqarmasi boshlig'i planshetidagi interaktiv xarita va diagrammalar;  
d) Xom CSV fayllardagi takrorlangan satrlarni o'chiruvchi Python funksiyasi.

### 2-topshiriq: Data Quality mezonini aniqlash <Badge type="tip" text="oson" />
Quyidagi holatda Data Quality'ning qaysi mezoni buzilgan:
*"Kasalxona tizimida bemorning vazni 450 kg, bo'yi esa 12 sm deb yozilgan"*. Bu qaysi mezonga zid?

### 3-topshiriq: Consistency (Izchillik) muammosi <Badge type="tip" text="oson" />
Bitta kompaniyada sana 3 xil usulda saqlangan: `2024-05-12`, `12/05/2024` va `May 12, 2024`. Bu holat qanday tahliliy qiyinchiliklarni keltirib chiqaradi?

### 4-topshiriq: Data Lifecycle ketma-ketligi <Badge type="warning" text="o'rta" />
Ma'lumotlar hayot siklining 5 ta bosqichini to'g'ri mantiqiy ketma-ketlikda joylashtiring:
- Transform (O'zgartirish)
- Ingest (Qabul qilish)
- Archive (Arxivlash)
- Validate (Sifat tekshiruvi)
- Serve (Taqdim etish)

### 5-topshiriq: Ssenariy tahlili (Direktor roli) <Badge type="warning" text="o'rta" />
Maktab direktori platformaga kirganda eng birinchi bo'lib qaysi 4 ta asosiy KPI ko'rsatkichni ko'rishi kerak? Loyihalashtiring.

### 6-topshiriq: Administrator validation qoidalari <Badge type="warning" text="o'rta" />
Yangi o'quv yili uchun maktablar ro'yxati CSV faylda keldi. Administrator ushbu fayl uchun qaysi 3 ta majburiy validation (tekshirish) qoidasini kiritishi shart?

### 7-topshiriq: Python'da manfiy sonlarni topish <Badge type="warning" text="o'rta" />
Quyidagi ro'yxatda o'quvchilar soni saqlangan: `sonlar = [450, 620, -15, 890, 0, 750]`.  
Python'da ro'yxatdagi barcha xato (0 dan kichik) qiymatlarni topib ekranga chiqaruvchi kod yozing.

### 8-topshiriq: Resurs yuklamasi formulasini tuzish <Badge type="danger" text="qiyin" />
Tuman bo'yicha 15 ta maktab, 12 000 nafar o'quvchi va 600 nafar o'qituvchi bor.
a) Bitta maktabga o'rtacha necha nafar o'quvchi to'g'ri keladi?
b) Bitta o'qituvchiga necha nafar o'quvchi to'g'ri keladi?
Ushbu ikki ko'rsatkich ta'lim boshqaruvida nima uchun o'ta muhim?

### 9-topshiriq: "Garbage In, Garbage Out" keysi <Badge type="danger" text="qiyin" />
Tasavvur qiling, maktab kutubxonasi kitoblar soni bo'yicha hisobotda har bir sinf kitoblar sonini 10 barobarga ko'paytirib yozgan. Bu noto'g'ri ma'lumot keyinchalik viloyat budjetiga va yangi darsliklar xaridiga qanday salbiy ta'sir ko'rsatadi?

### 10-topshiriq: To'liq Data Pipeline sxemasini chizish <Badge type="info" text="bonus" />
"Maktab tahliliy platformasi" uchun xom Excel fayllardan to Power BI dashboardigacha bo'lgan to'liq arxitektura sxemasini daftaringizda bloklar ko'rinishida chizing.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'zini tekshirish uchun savollar

1. Ma'lumotlar arxitekturasining 6 ta asosiy qatlami qaysilar?
2. Data Lifecycle ning 7 ta bosqichini sanab bering.
3. Data Quality'ning 4 asosiy ustuni (Completeness, Accuracy, Consistency, Timeliness) o'rtasidagi farq nima?
4. Administrator (Data Operator) qanday tekshiruvlarni amalga oshiradi?
5. Resurs yuklamasi (o'quvchi/o'qituvchi nisbati) nima uchun tahliliy ko'rsatkich hisoblanadi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Uy atrofingizdagi biror tashkilot (masalan, poliklinika, do'kon yoki sport to'garagi) uchun 6 qatlamli ma'lumotlar arxitekturasini loyihalashtiring.
2. Data Quality mezonlarining har biriga hayotiy misol keltirib, konspekt yozing.

</div>

