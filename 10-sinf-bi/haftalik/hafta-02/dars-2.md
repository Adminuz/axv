# 5-dars: Ma’lumot formatlari: Avro va formatlarni chuqur taqqoslash

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 2-hafta, 2-dars (umumiy 5-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga voqealarga asoslangan (Event-driven) va oqimli (Streaming) ma'lumotlar uzatishda jahon standarti bo'lgan **Apache Avro** formatining ichki arxitekturasi va tamoyillarini o'rgatish; **Schema Evolution** (sxema evolyutsiyasi: yangi maydonlar qo'shilishi va o'chirilishida tizim mosligi) mohiyatini tushuntirish; ma'lumotlar muhandisligidagi 4 ta asosiy format — **CSV, JSON, Parquet va Avro** o'rtasidagi chuqur texnik va amaliy farqlarni tahlil qilish hamda Python yordamida Avro sxemasini loyihalash, ma'lumotlarni yozish va o'qish ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Apache Avro formatining nima uchun qatorga asoslangan (Row-based) va zich ikkilik (dense binary) format ekanligini tushunish;
- Avro faylining tuzilishi: JSON formatidagi sxema va binar ma'lumotlar bloklarini bilish;
- Schema Evolution tushunchasi va uning turlari (Backward, Forward, Full compatibility) mohiyatini anglash;
- Real-time oqimlar (Apache Kafka, Event Hubs) da nima uchun Avro formati JSON o'rniga tanlanishini asoslab bera olish;
- CSV, JSON, Parquet va Avro formatlarini 6 ta mezon (saqlash usuli, sxema, o'qish/yozish tezligi, siqilish, qo'llanish sohasi) bo'yicha mustaqil qiyoslash;
- Python'da (`fastavro` yoki `pyarrow`) Avro sxemasi (JSON schema) yaratish, ma'lumot yozish va o'qish amaliyotini bajarish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun shaxsiy kompyuter (kamida 8 GB RAM);
- Python 3.10+, VS Code muhiti;
- O'rnatilgan kutubxonalar: `fastavro`, `pyarrow`, `pandas`;
- Namuna JSON va Avro sxema fayllari.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Parquet formati, columnar saqlash, Projection/Predicate pushdown bo'yicha savol-javob |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | Apache Avro formati, JSON schema, Schema Evolution, Kafka va oqimli tizimlarda Avro |
| **30–50 min** | Formatlarni chuqur taqqoslash | CSV vs JSON vs Parquet vs Avro — 4 ta formatning kuchli va zaif tomonlari tahlili |
| **50–70 min** | Mustaqil amaliy mashg'ulot | Python'da Avro sxemasi yaratish, binar formatda saqlash va ma'lumotlarni o'qish |
| **70–80 min** | Dars xulosasi va baholash | Tezkor savol-javob, amaliy ishlarni tekshirish va uyga vazifa topshirish |

---

## Nazariy qism (Batafsil konspekt)

### 1. Apache Avro formati nima?

**Apache Avro** — bu ma'lumotlarni ketma-ketlashtirish (serialization) va qatorga asoslangan (Row-based) saqlash uchun mo'ljallangan, yuqori tezlikdagi zich ikkilik (compact binary) formatdir.

Avro formati Hadoop asoschisi Doug Cutting tomonidan ishlab chiqilgan bo'lib, uning asosiy maqsadi — tarmoq orqali minimal bayt uzatish va turli dasturlash tillari (Java, Python, C++, Go) o'rtasida ma'lumotlarni bir xil qat'iyat bilan almashishdir.

**Avro formatining asosiy xususiyatlari:**
1. **Sxema JSON da yoziladi:** Ma'lumotlarning strukturasi, turlari va default qiymatlari inson o'qiy oladigan JSON formatida tavsiflanadi.
2. **Ikkilik ma'lumot (Binary payload):** Ma'lumotlarning o'zi esa o'ta ixcham ikkilik shaklda saqlanadi. Har bir qatorda ustun nomlari qayta-qayta yozilmaydi (JSON'dan farqi!).
3. **Self-describing (O'zini o'zi tavsiflovchi):** Fayl ko'rinishida saqlanganda, sxema faylning boshida (header) joylashadi. Faylni o'qiyotgan har qanday tizim avval sxemani o'qiydi va shunga qarab binar baytlarni ochadi.

---

### 2. Schema Evolution (Sxema evolyutsiyasi)

Haqiqiy biznes tizimlarida ilovalar doimiy yangilanadi: yangi ustunlar qo'shiladi, eskilar o'chiriladi yoki o'zgartiriladi. Agar saqlash formati buni qo'llab-quvvatlamasa, butun pipeline buziladi.

Avro formatida **Schema Evolution** juda mukammal yo'lga qo'yilgan:
- **Backward Compatibility (Orqaga moslik):** Yangi sxema bilan eski kod yozgan ma'lumotlarni xatosiz o'qish mumkin.
- **Forward Compatibility (Oldinga moslik):** Eski sxema bilan yangi kod yozgan ma'lumotlarni o'qish mumkin (yangi maydonlar e'tiborga olinmaydi).
- **Full Compatibility (To'liq moslik):** Ham orqaga, ham oldinga moslik ta'minlanadi.

> **Qoida:** Avro sxemasiga yangi maydon qo'shayotganda doimo unga standart qiymat (`"default": null` yoki `"default": 0`) berish shart! Aks holda tizim orqaga moslikni yo'qotadi.

---

### 3. Nega Apache Kafka va Streaming tizimlarda Avro ishlatiladi?

Taksi buyurtma ilovalari (Yandex, Uber), to'lov tizimlari (Click, Payme) soniyasiga yuz minglab tranzaksiya voqealarini (events) hosil qiladi.
- Agar bu ma'lumotlar **JSON** formatida yuborilsa: har bir xabarda `"user_id": 12345, "amount": 50000, "timestamp": "..."` kabi matnlar qayta-qayta ketadi. Bu tarmoqni to'ldirib tashlaydi.
- **Avro + Schema Registry** yondashuvida: Kafka orqali faqat 4 baytlik sxema ID raqami va siqilgan binar qiymatlar ketadi. Natijada tarmoq trafigi **70–80% ga kamayadi**, xabarlarni yozish tezligi esa bir necha barobar oshadi.

---

### 4. Katta to'rtlik: CSV vs JSON vs Parquet vs Avro

| Mezon | CSV | JSON | Apache Parquet | Apache Avro |
|---|---|---|---|---|
| **Struktura turi** | Satrli (Row-based, text) | Yarim-tuzilmali (Nested row) | Ustunli (Columnar, binary) | Satrli (Row-based, binary) |
| **Sxema mavjudligi** | Yo'q (hammasi matn) | Ixtiyoriy / noaniq | Ichki qat'iy sxema | Qat'iy JSON sxema |
| **Yozish tezligi** | O'rta | Sekin | Sekinroq (buferlanadi) | **O'ta tez (Append-only)** |
| **Tahlil tezligi (OLAP)**| Sekin | Juda sekin | **O'ta tez (Pushdown)** | O'rta |
| **Siqilish darajasi**| Past (siqilmagan) | Past | **Juda yuqori (Snappy/Gzip)**| Yuqori |
| **Schema Evolution**| Yo'q | Cheklangan | Bor | **Juda mukammal** |
| **Eng maqbul o'rni** | Eksport, oddiy hisobot | Web API, Config, Loglar | **Data Lake (Silver/Gold), DWH**| **Streaming (Kafka), Raw Ingestion** |

---

## Kod namunalari

### 1-namuna: Python'da Avro sxemasi yaratish va ma'lumot yozish (`fastavro`)

```python
import fastavro
import os

# 1. JSON formatida Avro sxemasini belgilaymiz
schema = {
    'doc': 'Maktab oquvchilari baholari',
    'name': 'OquvchiBaho',
    'namespace': 'uz.maktab.bi',
    'type': 'record',
    'fields': [
        {'name': 'id', 'type': 'int'},
        {'name': 'ism', 'type': 'string'},
        {'name': 'fan', 'type': 'string'},
        {'name': 'baho', 'type': 'int'},
        {'name': 'izoh', 'type': ['null', 'string'], 'default': None}  # ixtiyoriy maydon
    ]
}

# 2. Saqlash uchun namunaviy yozuvlar
records = [
    {'id': 1, 'ism': 'Aliyev Ali', 'fan': 'Informatika', 'baho': 95, 'izoh': "A'lo"},
    {'id': 2, 'ism': 'Valiyeva Vali', 'fan': 'Matematika', 'baho': 88, 'izoh': None},
    {'id': 3, 'ism': 'Ganiyev Gani', 'fan': 'Fizika', 'baho': 76, 'izoh': 'Yaxshi'}
]

os.makedirs('data/avro', exist_ok=True)
avro_file = 'data/avro/oquvchilar.avro'

# 3. Ma'lumotlarni Avro fayliga yozamiz (Snappy siqish bilan)
parsed_schema = fastavro.parse_schema(schema)

with open(avro_file, 'wb') as out:
    fastavro.writer(out, parsed_schema, records, codec='snappy')

print("Avro fayli muvaffaqiyatli yaratildi:", avro_file)
```

### 2-namuna: Avro faylini o'qish va sxemasini tekshirish

```python
# 1. Avro faylini o'qiymiz
with open(avro_file, 'rb') as f:
    avro_reader = fastavro.reader(f)
    
    # Fayl boshidagi sxemani chiqaramiz
    print("Fayl sxemasi:")
    print(avro_reader.writer_schema)
    
    # Ma'lumotlarni satrma-satr o'qiymiz
    print("\nO'qilgan yozuvlar:")
    for record in avro_reader:
        print(f"ID: {record['id']} | Ism: {record['ism']} | Baho: {record['baho']}")
```

---

## Amaliy topshiriqlar

### 1-topshiriq: Row vs Columnar qo'llanish o'rnini tanlash (Oson)
Quyidagi ikki vaziyat uchun eng mos formatni tanlang va sababini tushuntiring:
1. Bankomatdan har soniyada yechilayotgan pullar haqidagi xabarlarni Kafka orqali uzatish.
2. 5 yillik 500 million tranzaksiya ichidan har bir viloyat bo'yicha yillik o'rtacha xarajatni hisoblash.

**Kutiladigan natija:** 1-vaziyat uchun Avro, 2-vaziyat uchun Parquet tanlanadi.  
**Yechim:**  
1-vaziyatda doimiy yangi qatorlar qo'shiladi (streaming/write-heavy), shuning uchun satrli ixcham Avro formati mos keladi. 2-vaziyatda esa faqat 2-3 ta ustun bo'yicha ulkan agregatsiya bajariladi (OLAP/analytical), shuning uchun ustunli va tezkor Parquet formati tanlanadi.

---

### 2-topshiriq: Avro sxemasiga yangi maydon qo'shish (O'rta)
Mavjud `OquvchiBaho` sxemasiga `telefon` maydonini qo'shing. Schema Evolution qoidalariga ko'ra, eski ma'lumotlar bilan xatolik kelib chiqmasligi uchun bu maydon qanday e'lon qilinishi kerak?

**Kutiladigan natija:** Maydon ixtiyoriy va standart qiymatga ega bo'lishi kerak.  
**Yechim:**  
```json
{
  "name": "telefon",
  "type": ["null", "string"],
  "default": null
}
```
`"default": null` berilishi shart, aks holda eski yozuvlarda telefon maydoni bo'lmagani uchun `SchemaIncompatibleException` xatosi yuzaga keladi.

---

### 3-topshiriq: 4 ta formatning hajmini taqqoslash (Qiyin)
Bir xil 50 000 qatordan iborat datasetni 4 ta formatda saqlang:
1. `data.csv`
2. `data.json`
3. `data.parquet` (snappy)
4. `data.avro` (snappy)
Ularning hajmlarini baytlarda o'lchab, eng kattasidan eng kichigiga qarab tartiblab chiqaring.

**Kutiladigan natija:** 4 ta format hajmi tahlil qilinadi (odatda JSON > CSV > Avro > Parquet).  
**Yechim:**  
```python
import os
files = ['data.json', 'data.csv', 'data.avro', 'data.parquet']
sizes = {f: os.path.getsize(f) for f in files}
sorted_sizes = sorted(sizes.items(), key=lambda x: x[1], reverse=True)

for name, size in sorted_sizes:
    print(f"{name}: {size / 1024:.2f} KB")
```

---

## Tezkor nazorat savollari

1. Avro formati Parquet'dan asosiy qaysi jihati bilan tubdan farq qiladi?  
   *Javob:* Avro — qatorga asoslangan (Row-based) ikkilik format, Parquet esa ustunli (Columnar) formatdir.
2. Avro faylida ma'lumotlar sxemasi qayerda saqlanadi?  
   *Javob:* Faylning eng boshida (File Header) JSON formatida saqlanadi.
3. Nima uchun Kafka oqimlarida JSON o'rniga Avro ishlatiladi?  
   *Javob:* Avro har bir xabarda ustun nomlarini takrorlamaydi, hajmi 70–80% kichik bo'ladi va tarmoq yuklamasini keskin kamaytiradi.
4. Schema Evolution'da "Backward Compatibility" nimani anglatadi?  
   *Javob:* Yangi sxema yordamida eski kod tomonidan yozilgan ma'lumotlarni muammosiz o'qiy olish imkoniyatini anglatadi.

---

## Uyga vazifa

1. Do'kon mahsulotlari (id, nom, toifa, narx, qoldiq) uchun Avro sxemasini JSON formatida yozing.
2. Python'da 10 000 ta mahsulot ma'lumotini hosil qilib, uni ham JSON, ham Avro formatida saqlang.
3. Fayl hajmlarini solishtirib, Avro qancha joy tejaganini ko'rsating.
