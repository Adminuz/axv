---
title: "5-dars. 5-dars: Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 2, "link": "/10-sinf-bi/hafta-02/"}, "g": 5, "title": "5-dars: Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash", "lead": "Real-time rejimida millionlab voqealarni uzatishda har bir bayt hisobda turadi. Ushbu darsda biz Apache Kafka va oqimli tizimlarning sevimlisi bo'lgan Apache Avro formatini hamda Data Engineeringdagi \"Katta to'rtlik\" (CSV, JSON, Parquet, Avro) formatlarining o'zaro raqobatini o'rganamiz.", "slide": "/slaydlar/10-sinf-bi/hafta-02/dars-2.html", "test": "/slaydlar/10-sinf-bi/hafta-02/dars-2-test.html", "tabs": [{"g": 4, "link": "/10-sinf-bi/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/10-sinf-bi/hafta-02/dars-2", "current": true}, {"g": 6, "link": "/10-sinf-bi/hafta-02/dars-3", "current": false}], "prev": {"g": 4, "title": "4-dars: Ma’lumot formatlari: Parquet va Columnar saqlash formati (Snappy siqish, CSV vs Parquet)", "link": "/10-sinf-bi/hafta-02/dars-1"}, "next": {"g": 6, "title": "6-dars: Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) asoslari", "link": "/10-sinf-bi/hafta-02/dars-3"}}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Apache Avro:** Qatorlarga asoslangan (Row-based), zich ikkilik (dense binary) ma'lumot formati.
- **JSON Sxema:** Avro ma'lumotlar strukturasini inson o'qiy oladigan JSON formatida ifodalaydi, ma'lumotlarning o'zi esa o'ta ixcham ikkilik baytlarda saqlanadi.
- **Ustun nomlari takrorlanmaydi:** JSON har bir qatorda kalit nomlarini qayta-qayta yozsa, Avro ularni faqat fayl boshida bir marta saqlaydi — bu tarmoq trafigini 70–80% ga kamaytiradi.
- **Schema Evolution:** Dastur yangilanganda yangi ustunlar qo'shilishi yoki eskilari o'chirilishiga qaramay, tizimning uzluksiz ishlashini ta'minlovchi mexanizm.
- **Streaming va Kafka:** Tezkor yozish (Append-only) va minimal hajm talab etiladigan joylarda Avro tengsizdir.
- **Formatlar taqsimoti:** Web API uchun — JSON, tezkor eksport uchun — CSV, Big Data tahlil uchun — Parquet, oqimli tranzaksiyalar uchun — Avro.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Avro qanday qilib JSON'dan 5 barobar kichik bo'ladi?
JSON faylida:
```json
{"foydalanuvchi_id": 1001, "harakat": "bosing", "vaqt": "2026-10-04 10:00:00"}
```
Har bir qatorda `"foydalanuvchi_id"`, `"harakat"`, `"vaqt"` so'zlari takrorlanadi. Agar 10 million qator bo'lsa, siz Gigabaytlarcha faqat ustun nomlarini uzatasiz!  
Avro esa ustun nomlarini Header'da bir marta saqlaydi, qatorlarda esa faqat binary qiymatlarni ketma-ket yozadi.

### 2. Schema Evolution ning 3 oltin qoidasi
1. Yangi qo'shilayotgan maydonga doimo `"default"` qiymat bering.
2. Hech qachon mavjud maydon nomini o'zgartirmang (agar kerak bo'lsa, `aliases` xususiyatidan foydalaning).
3. Majburiy (required) maydonni birdaniga o'chirib yubormang.

### 3. Confluent Schema Registry nima?
Kafka ekotizimida xabarlar ichida hatto Avro sxemasining o'zi ham yuborilmaydi! Sxemalar markaziy **Schema Registry** serverida saqlanadi. Xabar ichida esa bor-yo'g'i 4 baytlik ID ketadi. Iste'molchi (Consumer) shu ID orqali sxemani serverdan bir marta keshlab oladi va barcha millionlab xabarlarni o'qiydi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Apache Avro** | Qatorli (Row-based) saqlash va ixcham ikkilik serializatsiyaga asoslangan ochiq ma'lumot formati |
| **Serialization** | Xotiradagi obyektlarni diskka saqlash yoki tarmoq orqali uzatish uchun baytlar ketma-ketligiga aylantirish |
| **Schema Evolution** | Ma'lumotlar sxemasi o'zgarganda (yangi ustunlar qo'shilganda) eski va yangi dasturlar o'rtasidagi moslikni saqlash |
| **Backward Compatibility** | Yangi sxema yordamida eski tizim yozgan ma'lumotlarni xatosiz o'qiy olish |
| **Forward Compatibility** | Eski sxema yordamida yangi tizim yozgan ma'lumotlarni xatosiz o'qiy olish |
| **Full Compatibility** | Ham orqaga (backward), ham oldinga (forward) to'liq moslik holati |
| **Dense Binary** | Ortiqcha probel va belgilarsiz, maksimal ixchamlashtirilgan ikkilik ma'lumot |
| **Event Streaming** | Real vaqt rejimida doimiy ravishda hosil bo'luvchi voqealar oqimini uzatish va qayta ishlash |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- **Hadoop asoschisi yaratgan:** Avro formati 2009-yilda mashhur Apache Hadoop loyihasi asoschisi Doug Cutting tomonidan RPC (Remote Procedure Call) va ma'lumotlarni saqlashni soddalashtirish uchun yaratilgan.
- **Koinot kemalarida Avro:** NASA va kosmik stansiyalar sensorlaridan Yerga ma'lumot uzatishda tarmoq kanali juda qimmat bo'lgani sababli Avro kabi binar ixcham formatlar ishlatiladi.
- **JSON vs Avro tarmoqda:** Yirik to'lov tizimlarida JSON dan Avro'ga o'tish orqali serverlarning tarmoq kartalariga (NIC) tushadigan yuklama 65–75% ga kamaygan.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Formatlar vazifasini ajratish <Badge type="tip" text="oson" />
Quyidagi 4 ta vazifa uchun CSV, JSON, Parquet va Avro formatlaridan eng mosini tanlang:
a) Telegram boti uchun konfiguratsiya va sozlamalar fayli;  
b) Onlayn taksi haydovchilarining GPS koordinatalarini har soniyada serverga uzatish;  
c) Excel'da tezda ochib ko'rish uchun oylik hisobot;  
d) 50 million qatorlik sotuvlar jadvalida har bir mahsulot bo'yicha daromadni tahlil qilish.  
**Kutiladigan natija:** Har bir band uchun to'g'ri format va 1 jumlalik asos.

### 2. Oddiy Avro sxemasi yozish <Badge type="tip" text="oson" />
Maktab o'quvchisi uchun quyidagi maydonlardan iborat Avro JSON sxemasini yozing: `id` (int), `ism` (string), `sinf` (int), `faol` (boolean).  
**Kutiladigan natija:** To'g'ri sintaksisli JSON schema kodi.

### 3. Nullable maydon yaratish <Badge type="tip" text="oson" />
Yuqoridagi sxemaga `email` maydonini shunday qo'shingki, agar o'quvchida email bo'lmasa, u `null` bo'lishi mumkin bo'lsin (`type: ["null", "string"]`, `default: null`).  
**Kutiladigan natija:** Schema Evolution talablariga javob beruvchi maydon ta'rifi.

### 4. Fastavro bilan fayl yaratish <Badge type="tip" text="oson" />
Python'da `fastavro` kutubxonasidan foydalanib, 3 ta namunaviy o'quvchi ma'lumotini `data/oquvchilar.avro` fayliga yozing.  
**Kutiladigan natija:** Fayl diskda paydo bo'ladi.

### 5. Avro faylini o'qish <Badge type="warning" text="o'rta" />
Yaratilgan `data/oquvchilar.avro` faylini `fastavro.reader` yordamida oching va uning ichidagi barcha yozuvlarni konsolga chop eting.  
**Kutiladigan natija:** Yozuvlar ro'yxat ko'rinishida chiqariladi.

### 6. Sxemani tekshirish <Badge type="warning" text="o'rta" />
Avro faylini ochmasdan, uning Header qismidagi `writer_schema` obyektini konsolga chiqaruvchi dastur yozing.  
**Kutiladigan natija:** Fayl yaratilgan sxemaning strukturasi ko'rinadi.

### 7. JSON va Avro hajmini taqqoslash <Badge type="warning" text="o'rta" />
Bir xil 10 000 qatorli tranzaksiyalar ro'yxatini ham `.json`, ham `.avro` formatida saqlang. Ikkala fayl hajmini o'lchab, tejalgan foizni hisoblang.  
**Kutiladigan natija:** Avro fayli JSON'dan kamida 2–3 barobar kichik ekanligi isbotlanadi.

### 8. Schema Evolution: yangi maydon qo'shish <Badge type="warning" text="o'rta" />
Eski Avro faylini yangilangan sxema (yangi ixtiyoriy maydon qo'shilgan) bilan o'qishga harakat qiling. Dastur xato bermasdan eski ma'lumotlarda yangi maydon o'rniga default qiymat qo'yganini tekshiring.  
**Kutiladigan natija:** Backward compatibility amalda tekshiriladi.

### 9. Katta to'rtlik benchmarki <Badge type="danger" text="qiyin" />
Python yordamida 50 000 qatorli bir xil datasetni CSV, JSON, Parquet va Avro formatlarida diskka saqlang. Har birining yozish vaqtini `time.time()` bilan o'lchab, qaysi biri eng tez yozilganini aniqlang.  
**Kutiladigan natija:** Yozish tezligi bo'yicha reyting hosil qilinadi.

### 10. Sxema mos kelmaslik xatosini tahlil qilish <Badge type="danger" text="qiyin" />
Agar Avro sxemasiga `"default"` qiymatsiz majburiy (required) yangi maydon qo'shilsa va eski fayl o'qilsa nima sodir bo'ladi? Xatolikni maxsus kod orqali keltirib chiqaring va xulosa yozing.  
**Kutiladigan natija:** `SchemaIncompatibleException` xatosi olinadi va sababi tushuntiriladi.

### 11. Xatoni toping va tuzating <Badge type="danger" text="qiyin" />
Quyidagi Avro sxemasida sintaktik xatolik bor:
```json
{
  "name": "yosh",
  "type": "integer"
}
```
Avro standartida qaysi ma'lumot turlari mavjud? Nega `integer` xato hisoblanadi? Uni to'g'rilang.  
**Kutiladigan natija:** Avro'da `integer` emas, `int` yoki `long` ishlatilishi ko'rsatiladi.

### 12. Streaming ingestion simulyatsiyasi <Badge type="info" text="bonus" />
Python'da real-time oqimni simulyatsiya qiling: har 0.1 soniyada hosil bo'ladigan 100 ta tranzaksiyani ketma-ket Avro fayliga qo'shib (append) boring. Qatorli ikkilik formatning oqimli yozishdagi samaradorligini tahlil qiling.  
**Kutiladigan natija:** Streaming yozuv mexanizmi ishlaydi va o'lchov natijalari taqdim etiladi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Nima uchun Avro formati qatorga asoslangan (Row-based) bo'lsa ham, CSV va JSON'dan ancha ixcham hisoblanadi?
2. Schema Evolution qanday muammoni hal qiladi va nima uchun biznes tizimlarida juda muhim?
3. Nega Kafka va boshqa event-driven tizimlarda Parquet emas, balki Avro formati tanlanadi?
4. Backward va Forward compatibility o'rtasidagi asosiy farq nima?
5. Qachon Parquet, qachon esa Avro ishlatish kerak? Aniq 2 ta misol bilan tushuntiring.

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Kutubxona kitoblari (kitob_id, sarlavha, muallif, nashr_yili, mavjudlik_holati) uchun Avro sxemasini tuzing. 20 000 ta kitob ma'lumotini hosil qilib, uni JSON va Avro formatlarida saqlang. Hajm va yozish tezligini solishtirib, qisqa hisobot tayyorlang.

</div>

