---
title: "1-dars. 1-dars: Ma’lumotlar muhandisligiga kirish (Data Engineering asoslari)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 1, "link": "/10-sinf-bi/hafta-01/"}, "g": 1, "title": "1-dars: Ma’lumotlar muhandisligiga kirish (Data Engineering asoslari)", "lead": "**\"Garbage In, Garbage Out\" qoidasi:** Agar tizimga kiruvchi ma'lumot xato yoki iflos bo'lsa, eng mukammal sun'iy intellekt ham xato natija beradi. Shuning uchun Data Engineering — butun AI va analitikaning poydevoridir.", "slide": "/slaydlar/10-sinf-bi/hafta-01/dars-1.html", "tabs": [{"g": 1, "link": "/10-sinf-bi/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/10-sinf-bi/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/10-sinf-bi/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "2-dars: Ma'lumotlar arxitekturasi va hayot sikli (Data Architecture & Data Lifecycle)", "link": "/10-sinf-bi/hafta-01/dars-2"}}
---

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Mavzu:** Ma’lumotlar muhandisligiga kirish (DIKW piramidasi, Data Engineer roli, Data Pipeline, Netflix va YouTube keyslari)

---

<div class="blk">

## <Icon name="file-text" /> Nazariy konspekt

### 1. DIKW Piramidasi: Ma'lumotdan Donolikkacha
Zamonaviy raqamli iqtisodiyotda ma'lumotlar qanday qilib foydali qarorlarga aylanadi?
- **Data (Ma'lumot):** Kontekstsiz xom raqamlar va belgilar (masalan, `39.0`, `105`).
- **Information (Axborot):** Qayta ishlangan va savollarga javob beruvchi ma'lumot (masalan, *"Bemorning tana harorati 39.0°C ga ko'tarildi"*).
- **Knowledge (Bilim):** Sabab va qonuniyatlarni tushunish (masalan, *"Qon tahlillari va harorat virusli infeksiyadan dalolat beradi"*).
- **Wisdom (Donolik / Qaror):** To'g'ri va oqilona chora ko'rish (masalan, *"Maxsus dori-darmon kursini tayinlash va izolyatsiyalash"*).

---

### 2. Ma'lumotlar muhandisligi (Data Engineering) nima?
Data Engineering — turli manbalardan (ilova, veb-sayt, sensorlar) keladigan ulkan hajmdagi xom ma'lumotlarni yig'ish, tozalash, saqlash va ularni analitika hamda Machine Learning uchun yetkazib beruvchi **ma'lumotlar quvurlarini (Data Pipeline)** qurish sohasidir.

**Kasbiy rollar farqi:**
- **Data Engineer:** Quvurlar va omborlar arxitektori. U ma'lumotlarning uzluksiz, toza va xavfsiz kelishini ta'minlaydi.
- **Data Analyst / BI Developer:** Tayyor ma'lumotlar asosida hisobotlar, trendlar va vizual dashboardlar yaratadi.
- **Data Scientist / ML Engineer:** Toza ma'lumotlar asosida bashorat qiluvchi sun'iy intellekt modellarini o'qitadi.


---

### 3. Data Pipeline ning 4 asosiy bosqichi
1. **Ingest (Qabul qilish):** Ma'lumotlarni turli manbalardan (API, fayllar, ma'lumotlar bazasi) yig'ish.
2. **Transform (Tozalash va o'zgartirish):** Xatolarni tuzatish, bo'sh joylarni to'ldirish, formatlarni standartlashtirish.
3. **Store (Saqlash):** Ma'lumotlar ombori (DWH) yoki Data Lake'ga yozish.
4. **Serve (Taqdim etish):** BI dashboardlar va ML modellari uchun taqdim etish.

---

### 4. Real keys: Netflix va YouTube tavsiya tizimlari
Siz YouTube'da videoni qancha vaqt ko'rganingiz, qaysi daqiqada to'xtatganingiz yoki qaysi janrni ko'proq yoqtirganingiz har soniyada Data Pipeline orqali o'tadi. Tozalangan ma'lumotlar ML modeliga yuboriladi va tizim sizga keyingi eng qiziqarli videoni tavsiya qiladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1-topshiriq: DIKW piramidasi bosqichlarini ajratish <Badge type="tip" text="oson" />
Berilgan 4 ta holatni DIKW piramidasi bosqichlariga moslashtiring:
a) *"Do'konda non narxi 4 000 so'm, un narxi 8 000 so'm"*  
b) *"Oxirgi oyda un narxi 20% ga oshgani sababli non tannarxi ham ko'tarildi"*  
c) *"Bug'doy importi bo'yicha yangi ta'minotchi bilan shartnoma imzolash"*  
d) *"4000, 8000, 150, 20"*

### 2-topshiriq: Data mutaxassislari vazifalarini taqsimlash <Badge type="tip" text="oson" />
Quyidagi vazifalarni Data Engineer, Data Analyst va Data Scientist rollariga ajrating:
- Tableau'da kompaniya oylik daromadi bo'yicha dashboard chizish;
- Har kuni kechasi 10 million tranzaksiyani avtomatik tozalab DWH ga yozuvchi pipeline yozish;
- Mijoz keyingi oyda xizmatdan voz kechishini (churn) bashorat qiluvchi model yaratish.

### 3-topshiriq: Maktab ma'lumotlarini tahlil qilish <Badge type="tip" text="oson" />
Maktabingizda har kuni qanday xom ma'lumotlar (Data) hosil bo'lishini sanab chiqing (kamida 5 ta tur).

### 4-topshiriq: Python'da xom ro'yxatni saralash <Badge type="warning" text="o'rta" />
Python'da quyidagi haroratlar ro'yxatidan faqat me'yordan yuqori (37.0°C dan baland) ko'rsatkichlarni ajratib oluvchi sodda kod yozing:
`temps = [36.6, 37.2, 36.5, 38.1, 36.8, 39.0]`

### 5-topshiriq: "Data to Decision" zanjirini tuzish <Badge type="warning" text="o'rta" />
Shahar jamoat transporti (avtobuslar) uchun "Data to Decision" zanjirini yozing: avtobus GPS ma'lumotlaridan qanday qilib yangi yo'nalish ochish qaroriga kelinadi?

### 6-topshiriq: Data Pipeline bosqichlarini tasvirlash <Badge type="warning" text="o'rta" />
Onlayn ta'lim platformasi (masalan, Coursera) uchun 4 bosqichli Data Pipeline sxemasini chizing (Ingestion → Transformation → Storage → Serving).

### 7-topshiriq: Iflos ma'lumot oqibatlarini tahlil qilish <Badge type="warning" text="o'rta" />
Agar bank tizimidagi ma'lumotlar bazasida mijozlar yoshi manfiy son bo'lib qolsa (`age = -25`), bu qaysi jarayonlarga qanday zarar yetkazishi mumkin?

### 8-topshiriq: Netflix tahlili <Badge type="danger" text="qiyin" />
Netflix foydalanuvchisi film ko'rishni 5-daqiqada to'xtatdi. Ushbu hodisa bo'yicha qanday parametrlar (features) ma'lumotlar quvuriga uzatilishini rejalashtiring.

### 9-topshiriq: E-tijorat savatchasi tahlili <Badge type="danger" text="qiyin" />
Onlayn do'konda savatga mahsulot qo'shib, lekin xarid qilmay chiqib ketgan foydalanuvchilar ma'lumotlarini o'rganish bo'yicha 3 ta gipoteza ilgari suring.

### 10-topshiriq: Ekotizim xaritasini tuzish <Badge type="info" text="bonus" />
Ma'lumotlar muhandisligida ishlatiladigan 4 ta asosiy texnologiyani (Python, SQL, Apache Spark/Airflow, Cloud DWH) o'zaro qanday bog'lanishini sxematik ko'rinishda tasvirlang.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'zini tekshirish uchun savollar

1. Nima uchun xom ma'lumotning o'zi qaror qabul qilish uchun yetarli emas?
2. DIKW piramidasida Knowledge va Wisdom o'rtasidagi farq nimada?
3. Data Engineer nima sababdan "zamonaviy infratuzilma santexniki" deb ataladi?
4. "Garbage In, Garbage Out" tamoyilining amaliy ma'nosi nima?
5. Data Pipeline nima va u qanday asosiy bosqichlardan iborat?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. DIKW piramidasini o'zingiz tanlagan bitta soha (tibbiyot, sport, ob-havo yoki o'qish) misolida yoritib bering.
2. Data Engineer va Data Scientist mutaxassisliklarining farqlari bo'yicha taqqoslama jadval tayyorlang.
3. Sevimli ijtimoiy tarmog'ingiz (Instagram, TikTok yoki YouTube) sizga yoqadigan kontentni qanday ma'lumotlar asosida topishini tahlil qilib yozing.

</div>

