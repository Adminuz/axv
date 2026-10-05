# 4-dars. Ma’lumot formatlari: Parquet va Columnar saqlash formati

> Katta hajmdagi ma'lumotlar olamida saqlash joyi va o'qish tezligi hal qiluvchi ahamiyatga ega. Ushbu darsda biz zamonaviy analitika poydevori bo'lgan Apache Parquet formatining ichki mo'jizalarini, ustunli saqlash tamoyilini va Snappy siqish qudratini o'rganamiz.

---

## Dars xulosasi

- **Row-based vs Columnar:** CSV ma'lumotlarni satrlar bo'yicha saqlasa, Parquet bitta ustunga tegishli barcha ma'lumotlarni yaxlit blok qilib saqlaydi.
- **OLAP uchun optimallashgan:** Analitik hisobotlarda millionlab qatorlarning faqat bir nechta ustuni hisoblanganda, Parquet diskdan ortiqcha ustunlarni o'qimaydi.
- **Projection Pushdown:** So'rovda ko'rsatilgan ustunlarni disk darajasida saralab o'qish imkoniyati — bu orqali disk I/O sarfi keskin kamayadi.
- **Predicate Pushdown:** Fayl metadatasidagi Min/Max statistikalar yordamida shartga to'g'ri kelmaydigan butun satr guruhlari (Row Groups) o'qilmasdan tashlab ketiladi.
- **Snappy siqish:** CPU'ni ortiqcha yuklamasdan ma'lumotlarni 3–5 barobargacha siqib beruvchi yuqori tezlikdagi standart siqish algoritmi.
- **Qat'iy tiplar (Schema):** CSV'dan farqli o'laroq, Parquet ma'lumot turlarini (int, float, datetime) ichida aniq saqlaydi va buzilishlarning oldini oladi.

---

## Qo'shimcha ma'lumot

### 1. Nega bir xil ma'lumotlar yonma-yon tursa yaxshiroq siqiladi?
Tasavvur qiling, sizda quyidagi satrlar bor:
- CSV'da: `Ali, 16, Toshkent`, keyin `Vali, 15, Samarqand`, keyin `G'ani, 16, Toshkent`. Matn, son va yana matn aralashib ketadi.
- Parquet'da: `[16, 15, 16, 15, 16, 16...]`. Faqat butun sonlar ketma-ket turadi!
Kompyuter bir xil turdagi va takrorlanuvchi ma'lumotlarni (Run-Length Encoding, Bit-Packing yoki Dictionary Encoding orqali) aqlbovar qilmas darajada kichik hajmga siqib tashlay oladi.

### 2. Row Group o'lchami qanday tanlanadi?
Parquet faylida Row Group juda kichik bo'lsa (masalan, 1 MB), har bir guruh uchun metadata overhead ko'payib ketadi va fayl kattalashadi. Agar u juda katta bo'lsa (masalan, 2 GB), xotiraga yuklash qiyinlashadi. Sanoatda (Spark, DWH) odatda bitta Row Group hajmi **128 MB dan 512 MB gacha** qilib belgilanadi.

### 3. CSV dan Parquet ga o'tishda keng tarqalgan xatolar
- **Index ustunini unutilishi:** `df.to_parquet('file.parquet', index=False)` qilinmasa, Pandas keraksiz indeks ustunini ham faylga yozib qo'yadi.
- **Kichik datasetlarda kutish:** Agar jadvalingiz bor-yo'g'i 50 qatordan iborat bo'lsa, Parquet fayli CSV dan kattaroq chiqishi mumkin! Chunki Parquet metadatasining o'zi bir necha kilobayt joy oladi. Parquet ning haqiqiy kuchi minglab va millionlab qatorlarda namoyon bo'ladi.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Columnar Storage** | Ma'lumotlarni satrlar bo'yicha emas, ustunlar bo'yicha ketma-ket joylashtiruvchi saqlash arxitekturasi |
| **Row-based Storage** | Ma'lumotlarni to'liq satrlar (records) bo'yicha diskka yozuvchi an'anaviy format (CSV, relational tables) |
| **Row Group** | Parquet fayli ichidagi satrlar to'plami (odatda 128–512 MB hajmda) |
| **Column Chunk** | Bitta Row Group ichidagi ma'lum bir ustunga tegishli ma'lumotlar bloki |
| **Projection Pushdown** | So'rovda talab qilingan ustunlarni diskdan o'qish jarayonining o'zida saralab olish |
| **Predicate Pushdown** | WHERE filtri shartlarini disk darajasiga tushirib, mos kelmaydigan bloklarni o'qimay o'tkazib yuborish |
| **Snappy** | Google tomonidan tezlik uchun ishlab chiqilgan, Parquet'ning standart siqish algoritmi |
| **Schema Enforcement** | Ma'lumot turlari va ustunlar tartibining qat'iy saqlanishi va nazorat qilinishi |
| **Footer Metadata** | Parquet faylining oxirida joylashgan, barcha ustunlar va guruhlar statistikasini saqlovchi qism |

---

## Bilasizmi?

- **Google va Twitter hamkorligi:** Parquet formati 2013-yilda Twitter va Cloudera muhandislari tomonidan Google'ning mashhur Dremel (hozirgi BigQuery) tizimi maqolalari asosida yaratilgan.
- **Bulut xarajatlarini tejash:** AWS Athena yoki Google BigQuery kabi xizmatlar so'rovda o'qilgan ma'lumot hajmi (Gigabaytlar) bo'yicha haq oladi. CSV o'rniga Parquet ishlatilsa, sarflanadigan mablag' 80–90% gacha kamayishi mumkin!
- **PAR1 belgisi:** Har qanday toza Parquet faylini hex-muharririda ochsangiz, uning eng birinchi 4 bayti va eng oxirgi 4 bayti doimo `PAR1` harflaridan iborat bo'ladi.

---

## Topshiriqlar

### 1. Nazariy farqni aniqlash · oson
Nima uchun bank tranzaksiyalarini kiritish (ATM'dan pul yechish) uchun Row-based format qulay, lekin butun yil davomidagi o'rtacha xarajatni hisoblash uchun Columnar format qulay? Fikringizni 2 ta asosiy dalil bilan yozma bayon eting.  
**Kutiladigan natija:** OLTP (yozish) va OLAP (tahlil) farqiga asoslangan qisqa tahliliy javob.

### 2. CSV dan Parquet yaratish · oson
Python Pandas yordamida 5 ta ustundan (id, ism, yosh, shahar, ball) iborat 10 000 qatorli sun'iy DataFrame tuzing va uni `data/talabalar.parquet` nomi bilan saqlang.  
**Kutiladigan natija:** `.parquet` fayli muvaffaqiyatli hosil qilinadi va uning mavjudligi tekshiriladi.

### 3. Indeksni to'g'ri boshqarish · oson
`to_parquet()` metodida `index=False` parametri nima vazifani bajarishini amalda sinab ko'ring: ikkita fayl yarating (biri `index=True`, ikkinchisi `index=False`) va `df.info()` orqali ustunlar farqini ko'rsating.  
**Kutiladigan natija:** Indeks saqlanganda ortiqcha `__index_level_0__` ustuni paydo bo'lishi aniqlanadi.

### 4. Parquet faylini o'qish · oson
Yaratilgan `data/talabalar.parquet` faylini `pd.read_parquet()` orqali xotiraga yuklang va uning dastlabki 5 qatorini konsolga chiqaring.  
**Kutiladigan natija:** Ma'lumotlar jadval ko'rinishida konsolga chiqadi.

### 5. Projection Pushdown amaliyoti · o'rta
Parquet faylidan faqat `ism` va `ball` ustunlarini o'qing (barcha qatorlar bilan). Buni `columns` argumenti yordamida bajaring va xotiradagi DataFrame faqat shu 2 ta ustundan iborat ekanini tasdiqlang.  
**Kutiladigan natija:** Faqat tanlangan 2 ustun yuklanadi.

### 6. Hajm bo'yicha tejamkorlik testi · o'rta
Bir xil 100 000 qatorli ma'lumotni ham `.csv`, ham `.parquet` formatida saqlang. `os.path.getsize()` yordamida ikkala fayl hajmini o'lchab, Parquet necha foiz kam joy olganini hisoblaydigan dastur yozing.  
**Kutiladigan natija:** Foiz ko'rsatkichi (odatda 60–80% tejash) konsolga chiqariladi.

### 7. O'qish tezligini taqqoslash · o'rta
Python'dagi `time` moduli yordamida 100 000 qatorli CSV faylni to'liq o'qish vaqti bilan xuddi shu ma'lumotli Parquet faylni to'liq o'qish vaqtini o'lchang. Qaysi biri necha barobar tez ishlaganini ko'rsating.  
**Kutiladigan natija:** Har ikki formatning sekundlardagi vaqti va nisbati chop etiladi.

### 8. Siqish turlarini solishtirish · o'rta
Bitta DataFrame'ni ikki xil siqish usuli bilan saqlang: `compression='snappy'` va `compression='gzip'`. Ikkala fayl hajmi va ularni qayta o'qish vaqtini solishtiring.  
**Kutiladigan natija:** Gzip kichikroq hajm, lekin Snappy tezroq dekompressiya berishi raqamlarda isbotlanadi.

### 9. PyArrow bilan metadatani tekshirish · qiyin
`pyarrow.parquet` kutubxonasidan foydalanib, Parquet faylining ichki metadatasini o'qing: undagi Row Groups soni, har bir Row Group'dagi qatorlar soni va har bir ustunning ma'lumot turini chop eting.  
**Kutiladigan natija:** Faylning texnik parametrlari to'liq tahlil qilinadi.

### 10. Min/Max statistikalarini tahlil qilish · qiyin
PyArrow orqali Parquet faylidagi ma'lum bir ustunning (masalan, `ball`) Row Group metadatasidagi minimum va maksimum qiymatlarini toping. Predicate pushdown aynan shu statistikalar asosida qanday ishlashini izohlang.  
**Kutiladigan natija:** `col_chunk.statistics.min` va `col_chunk.statistics.max` qiymatlari aniqlanadi.

### 11. Xatoni toping va tuzating · qiyin
Quyidagi kodda xatolik bor:
```python
# Noto'g'ri kod:
df = pd.read_parquet('data/talabalar.parquet', usecols=['ism', 'ball'])
```
Bu kod nima uchun `TypeError` beradi? Uni to'g'rilab yozing.  
**Kutiladigan natija:** Pandas'da `read_parquet` metodi `usecols` emas, `columns` parametrini qabul qilishi tushuntiriladi va to'g'rilanadi.

### 12. Katta dataset simulyatsiyasi va benchmark · bonus
1 000 000 (bir million) qatorlik translyatsiya datasetini hosil qiling. Unda 10 ta ustun bo'lsin. Ushbu datasetda faqat bitta ustun bo'yicha o'rtacha qiymat (`mean()`) hisoblash uchun CSV va Parquet o'rtasida to'liq benchmark o'tkazing va natijalarni chiroyli jadval ko'rinishida chiqaring.  
**Kutiladigan natija:** 1 million qatorda Parquet ustunli o'qish orqali erishilgan ulkan tezlik farqi yaqqol namoyon bo'ladi.

---

## O'zingizni tekshiring

1. Columnar (ustunli) saqlash usuli nima uchun ma'lumotlarni tahlil qilish (OLAP) jarayonida satrli formatdan ustun turadi?
2. Parquet faylidagi Footer qismi nima uchun faylning boshida emas, balki oxirida joylashadi?
3. Projection pushdown va Predicate pushdown o'rtasidagi asosiy farq nimada?
4. Snappy siqish algoritmining asosiy afzalligi nimada va nega u Parquet'da standart qilib olingan?
5. Nima uchun juda kichik (10–20 qatorli) datasetlarda Parquet fayli hajmi CSV faylidan kattaroq bo'lishi mumkin?
6. Parquet formatidagi ma'lumotlarni oddiy matn muharririda ochib o'qish mumkinmi? Nega?

---

## Uyga vazifa

O'zingiz qiziqqan soha (futbol statistikasi, ob-havo, e-tijorat) bo'yicha kamida 50 000 qatorlik CSV dataset toping yoki yarating. Uni Python Pandas yordamida Parquet (Snappy) formatiga o'tkazing. Fayl hajmlari va o'qish tezliklarini o'lchab, 1 betlik tahliliy xulosa tayyorlang.
