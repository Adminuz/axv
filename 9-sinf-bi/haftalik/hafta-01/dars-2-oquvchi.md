# 2-dars. Business Intelligence (BI) asoslari: Katta to'rtlik va hayotiy sikl

> Ma'lumotlarni strategik kuchga aylantiring: zamonaviy Business Intelligence arxitekturasi, tahlilning Katta to'rtligi va qaror qabul qilish sikli bilan tanishing.

## Dars xulosasi

- Business Intelligence (BI) — ma’lumotlarni yig‘ish, qayta ishlash, tahlil qilish va vizuallashtirish orqali to‘g‘ri boshqaruv qarorlari qabul qilishni ta'minlovchi tizimdir.
- Tahlilning "Katta to'rtligi" (BI's Big Four): Tavsifiy (Deskriptiv), Diagnostik, Bashoratli (Prediktiv) va Retseptiv (Preskriptiv) tahlillardir.
- Tavsifiy tahlil "O'tmishda nima sodir bo'ldi?", Diagnostik tahlil esa "Nima uchun sodir bo'ldi?" savoliga javob beradi.
- Bashoratli tahlil statistik modellar va Machine Learning yordamida kelajakdagi ehtimollarni prognoz qiladi.
- Retseptiv tahlil piramidaning eng yuqori pog'onasi bo'lib, eng maqbul harakat yo'nalishini tavsiya etadi.
- BI tizimi 5 ta asosiy komponentdan tashkil topgan: Ma'lumot manbalari, ETL jarayoni, Data Warehouse, Semantik qatlam va Vizuallashtirish vositalari.
- BI ning hayotiy sikli 6 bosqichdan iborat bo'lib, biznes ehtiyojlaridan boshlanib, amaliy harakatlar va uzluksiz takomillashuv bilan yakunlanadi.

---

## Qo'shimcha ma'lumot

### 1. An'anaviy hisobot va BI o'rtasidagi farq
Oddiy hisobotlar odatda o'tgan voqealarni statik (qog'ozda yoki oddiy PDF faylda) ko'rsatadi. U yerda ma'lumotlarni filtrlab bo'lmaydi, o'zgarishlar sababini bir bosishda ko'rib bo'lmaydi.
Zamonaviy BI esa dinamik va interaktivdir. Masalan, tumanlar bo'yicha savdo pasayganini ko'rgan rahbar ekrandagi xaritani bosib, darhol qaysi do'konda qaysi tovar sotilmay qolganini (drill-down) ko'ra oladi.

### 2. Katta to'rtlikning bosqichma-bosqich qiymati
Biznes tahlilining to'rt pog'onasi bir-birini to'ldiradi:
1. **Deskriptiv (Descriptive):** "Biz o'tgan yili 1000 ta velosiped sotdik". (Fakt)
2. **Diagnostik (Diagnostic):** "Bahor oylarida ob-havo qulay bo'lgani va sport aksiyasi o'tkazilgani uchun savdo 40% yuqori bo'ldi". (Sabab)
3. **Prediktiv (Predictive):** "Kelgusi bahorda 1400 ta velosipedga talab bo'lishi ehtimoli 85%". (Prognoz)
4. **Preskriptiv (Prescriptive):** "Fevral oyidayoq ehtiyot qismlarni buyurtma qilish va Toshkent parklari yaqinidagi filialga 60% zaxirani yo'naltirish kerak". (Tavsiya va harakat)

### 3. ETL jarayoni — BI yuragi
Ma'lumotlar turli joylarda (biri Excelda, biri CRM tizimida, biri Telegram botda) turlicha saqlanadi. 
ETL jarayoni ularni birlashtiradi:
- **Extract (Olish):** Turli manbalardan ma'lumotlarni ko'chirib olish.
- **Transform (O'zgartirish):** Xatolarni tuzatish, sanalarni bir xil formatga keltirish, takroriy yozuvlarni olib tashlash.
- **Load (Yuklash):** Tayyor toza ma'lumotni markaziy Ma'lumotlar Omboriga (Data Warehouse) yuklash.

### 4. Data Warehouse (Ma'lumotlar ombori) nima uchun kerak?
Kassada yoki veb-saytda ishlaydigan operatsion baza (OLTP) tezkor tranzaksiyalar (masalan, chek urish) uchun mo'ljallangan. Agar analitik 5 yillik barcha millionlab xaridlarni tahlil qilish uchun kassa bazasiga og'ir so'rov yuborsa, kassa to'xtab qolishi mumkin!
Shuning uchun tahlil uchun alohida, maxsus optimallashtirilgan **Data Warehouse** (OLAP) yaratiladi. U yerda faqat tahlil va hisobotlar amalga oshiriladi.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Business Intelligence (BI)** | Ma'lumotlar asosida samarali biznes qarorlari qabul qilishni ta'minlovchi tizim va texnologiyalar. |
| **Descriptive Analytics** | O'tmishda nima sodir bo'lganini umumlashtiruvchi tavsifiy tahlil. |
| **Diagnostic Analytics** | Nima uchun sodir bo'lganini sabab-oqibat orqali ochib beruvchi diagnostik tahlil. |
| **Predictive Analytics** | Kelajakda nima sodir bo'lishini modellar yordamida baholovchi bashoratli tahlil. |
| **Prescriptive Analytics** | Eng maqbul natijaga erishish uchun eng yaxshi qarorni tavsiya qiluvchi retseptiv tahlil. |
| **ETL (Extract, Transform, Load)** | Ma'lumotlarni manbalardan olish, tozalash va omborga yuklash jarayoni. |
| **Data Warehouse (DWH)** | Analitik tahlillar uchun mo'ljallangan yagona, markazlashtirilgan ma'lumotlar ombori. |
| **Data Mart** | Muayyan bo'lim (masalan, moliya yoki marketing) uchun mo'ljallangan kichik ixtisoslashgan ombor. |
| **Semantic Layer** | Murakkab ma'lumotlar bazasini biznes xodimlariga tushunarli ko'rsatkichlarga aylantiruvchi qatlam. |
| **Drill-down** | Umumiy ko'rsatkichdan uning tarkibiy detallariga chuqur kirish funksiyasi. |

---

## Bilasizmi?

- "Business Intelligence" atamasini ilk bor 1865 yilda Richard Millar Devens o'zining "Cyclopaedia of Commercial and Business Anecdotes" kitobida qo'llagan.
- Zamonaviy ma'noda BI atamasini 1989 yilda Gartner tahlilchisi Xovard Dresner ommalashtirgan.
- Bugungi kunda jahon BI dasturiy ta'minot bozori hajmi **30 milliard dollardan** oshadi.
- Katta korxonalarda ma'lumotlar tahlilchisi o'z vaqtining **80% gacha** qismini aynan ETL — ma'lumotlarni tozalash va tayyorlashga sarflaydi.

---

## Topshiriqlar

### 1. Tahlil toifasini aniqlash · oson
Quyidagi fikr qaysi tahlil turiga (Deskriptiv, Diagnostik, Prediktiv, Preskriptiv) tegishli?
*"Kompaniyamizning o'tgan oydagi sof foydasi 45 million so'mni tashkil etdi".*
**Kutiladigan natija:** To'g'ri tahlil turi va uning sababi yozilgan 1 jumla.

### 2. Sababni izlash tahlili · oson
Mobil operator abonentlarining 5% qismi boshqa kompaniyaga o'tib ketganini aniqladi. Boshqaruv jamoasi bu holatning asl sabablarini (narx, aloqa sifati, internet tezligi) tekshirmoqda.
Ushbu tekshirish Katta to'rtlikning qaysi turiga mansub?
**Kutiladigan natija:** Tahlil turi nomi va nima uchun shunday ekanligi haqida tushuntirish.

### 3. Prognoz va tavsiya farqi · oson
Quyidagi ikki jumlani o'qing va qaysi biri "Prediktiv", qaysi biri "Preskriptiv" ekanini aniqlang:
- X: "Kelgusi haftada havo sovuq bo'lishi ehtimoli 90%".
- Y: "Havo sovuq bo'lishi sababli issiq kiyim kiyish va soyabon olish tavsiya etiladi".
**Kutiladigan natija:** Har bir jumlaga mos toifani ko'rsating.

### 4. ETL bosqichlarini saralash · oson
Quyidagi 3 ta amalni ETL ning to'g'ri ketma-ketligida (1, 2, 3) joylashtiring:
- a) Tozalangan ma'lumotlarni PostgreSQL ma'lumotlar bazasiga joylashtirish.
- b) Xaridorlarning tug'ilgan sanasidagi xatolarni to'g'rilash va yoshini hisoblash.
- c) Excel fayllaridan savdo jadvallarini o'qib olish.
**Kutiladigan natija:** Harflarning to'g'ri ketma-ketligi (masalan: c -> b -> a) va ularga mos ETL bosqichlari.

### 5. Kinoteatr tahlili · o'rta
Shahar kinoteatri misolida Katta to'rtlikning 4 ta bosqichiga mos 1 tadan hayotiy misol tuzing:
- Deskriptiv: o'tgan dam olish kunlaridagi chiptalar savdosi.
- Diagnostik: qaysi film eng ko'p tomoshabin yig'gani sababi.
- Prediktiv: yangi premyera kutilmasi.
- Preskriptiv: chipta narxlarini belgilash bo'yicha tavsiya.
**Kutiladigan natija:** Kinoteatr bo'yicha 4 ta aniq tahliliy misol.

### 6. Data Warehouse zarurati · o'rta
Nima sababdan supermarketdagi kassa kompyuteri to'g'ridan-to'g'ri yillik tahliliy hisobotlarni hisoblamasligi kerak? Data Warehouse bu muammoni qanday hal qiladi?
**Kutiladigan natija:** OLTP (kassa) va OLAP (ombor) farqini tushuntiruvchi 2-3 jumlali javob.

### 7. BI hayotiy sikli bo'yicha keys · o'rta
Kiyim do'koni egasi: "Menga oylik sotuvlarimiz qaysi filialda eng yaxshi ketayotganini ko'rsatadigan panel kerak" dedi.
Ushbu loyihani BI hayotiy siklining dastlabki 3 ta bosqichi (Talablar, Yig'ish, Tahlil) bo'yicha qanday boshlash kerakligini yozing.
**Kutiladigan natija:** 3 ta bosqichning qisqacha rejasi.

### 8. Semantik qatlamning vazifasi · qiyin
Tasavvur qiling, ma'lumotlar bazasida `price`, `discount_rate`, `tax_pct` va `qty` degan ustunlar bor. Oddiy menejer esa shunchaki "Sof Daromad" ko'rsatkichini ko'rmoqchi.
Semantik qatlam bu yerda qanday vazifani bajaradi va u nega hisobotlarning aniqligi uchun muhim?
**Kutiladigan natija:** Semantik qatlamning formulasi va biznes xodimlari uchun ahamiyati haqida tahliliy izoh.

### 9. Shahar ekologiyasi bo'yicha BI tizimi · qiyin
Shahar havosi tozaligini nazorat qiluvchi BI tizimi loyihalashtirilmoqda.
- Manbalar: shahar bo'ylab o'rnatilgan 50 ta havo sensori (IoT).
- Katta to'rtlik: ifloslanish darajasini aniqlashdan tortib, transport harakatini cheklashgacha bo'lgan to'liq zanjirni tasvirlang.
**Kutiladigan natija:** Ekologiya monitoringi uchun to'liq BI arxitekturasi va 4 toifali tahlil rejasi.

### 10. Mini-tadqiqot: Power BI va Tableau · bonus
Bugungi kunda dunyoda eng mashhur ikkita BI dasturi mavjud: Microsoft Power BI va Tableau. Ularning o'xshash jihatlari va asosiy farqlarini o'rganib, solishtirma jadval tayyorlang.
**Kutiladigan natija:** Kamida 4 ta mezon (narx, integratsiya, o'rganish osonligi, vizual imkoniyatlar) bo'yicha taqqoslama jadval.

---

## O'zingizni tekshiring

1. Business Intelligence (BI) ning an'anaviy qog'oz hisobotlardan qanday 3 ta asosiy afzalligi bor?
2. Katta to'rtlik piramidasining eng quyi va eng yuqori pog'onasida qaysi tahlillar turadi?
3. Diagnostik tahlilda "drill-down" amali nimani anglatadi?
4. ETL qisqartmasidagi har bir harf qanday amalni ifodalaydi?
5. Data Warehouse nima va u nega "yagona haqiqat manbai" (Single Source of Truth) deb ataladi?
6. BI hayotiy siklining qaysi bosqichida biznesga eng katta real foyda keladi?

---

## Uyga vazifa

O'zingizga ma'lum biror yo'nalish (masalan, sevimli kiber-sport o'yini, maktab o'quvchilari davomati yoki avtobus saroyi) bo'yicha Katta to'rtlikning har bir turiga (Deskriptiv, Diagnostik, Prediktiv, Preskriptiv) mos bittadan aniq gap tuzib daftaringizga yozing.
