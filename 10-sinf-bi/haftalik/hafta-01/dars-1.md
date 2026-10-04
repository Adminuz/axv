# 1-dars: Ma’lumotlar muhandisligiga kirish (Data Engineering asoslari)

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 1-hafta, 1-dars (umumiy 1-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga zamonaviy axborot texnologiyalari va raqamli iqtisodiyotda ma'lumotlar (Data)ning tutgan o'rni, **DIKW piramidasi** (Data, Information, Knowledge, Wisdom) konsepti, **Ma’lumotlar muhandisligi (Data Engineering)** sohasining mohiyati, uning **Data Science** va **Business Intelligence (BI)** bilan bog'liqligi va farqlari, **Data Pipeline (ma'lumotlar quvuri)** tushunchasi hamda «Data to Decision» (ma'lumotdan qaror qabul qilishgacha) jarayonini real kompaniyalar (Netflix, YouTube) amaliy misollari orqali chuqur tushuntirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Ma'lumot (xom data), axborot (information) va bilim (knowledge) o'rtasidagi farqni tushunish va DIKW piramidasini tushuntira olish;
- Data Engineer kasbining vazifalarini va uning Data Analyst hamda Data Scientist mutaxassislaridan farqini bilish;
- "Data Pipeline" nima ekanini va ma'lumotlar manbadan iste'molchiga qanday bosqichlardan o'tib yetib borishini tasavvur qilish;
- "Data to Decision" zanjirini tushunish: qanday qilib xom ko'rsatkichlar asosida biznes va davlat boshqaruvida strategik qarorlar qabul qilinishini bilish;
- Netflix va YouTube tavsiya tizimlari orqasidagi ma'lumotlar oqimini (data flow) tahlil qila olish;
- Data ekotizimining asosiy qurollari (Python, SQL, Apache Airflow, Tableau/PowerBI) haqida birlamchi tasavvurga ega bo'lish.

---

## Kerakli jihozlar va vositalar

- O'qituvchi va o'quvchilar uchun kompyuter yoki noutbuk;
- Internet tarmog'iga ulanish;
- Proyektor yoki monitor;
- Python 3 va Jupyter Notebook (Google Colab yoki lokal muhit).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va yangi kursga kirish | Fanning maqsadi, zamonaviy dunyoda ma'lumotlarning qiymati ("Ma'lumot — yangi neft") haqida interaktiv kirish |
| **10–30 min** | Yangi mavzu bayoni (Nazariya) | DIKW piramidasi, Data Engineering nima, Data Scientist bilan farqi, Data Pipeline va Netflix keysi |
| **30–55 min** | Amaliy mashg'ulot (Tahlil va muhokama) | Python yordamida xom ma'lumotdan axborot hosil qilish (Oddiy Pandas skripti), YouTube data flow chizmasi |
| **55–75 min** | Mustaqil amaliy topshiriqlar | "Data to Decision" ssenariylarini tahlil qilish, rollar xaritasini chizish |
| **75–80 min** | Xulosa va baholash | Tezkor savol-javob, 1-dars xulosalari va uyga vazifa |

---

## Nazariy qism (Batafsil tushuntirish)

### 1. Ma'lumot va Axborot: DIKW Piramidasi

Zamonaviy dunyoda har kuni trillionlab bayt raqamli izlar qoldiriladi: kliklar, to'lovlar, videolarni ko'rish, GPS koordinatalari, maktab jurnallari. Biroq xom raqamlarning o'zi hech qanday foyda keltirmaydi.

Ma'lumotning qiymatga aylanish jarayoni **DIKW piramidasi** orqali ifodalanadi:

1. **Data (Xom ma'lumot):** Belgilar, raqamlar va xom faktlar to'plami. U kontekstga ega emas. Masalan: `38.5, 41.2, 36.6` yoki `101, 102, 103`.
2. **Information (Axborot):** Qayta ishlangan, tartiblangan va kontekstga ega bo'lgan ma'lumot. U "Kim? Nima? Qachon? Qayerda?" savollariga javob beradi. Masalan: *"Toshkent shahar 1-maktab 10-sinf o'quvchilarining o'rtacha tana harorati 36.6°C, lekin 3 nafar o'quvchida 38.5°C dan yuqori"*.
3. **Knowledge (Bilim):** Axborotni tahlil qilish, qonuniyatlarni topish va "Qanday?" degan savolga javob olish. Masalan: *"Oxirgi 3 kunda yuqori haroratli o'quvchilar soni 15% ga oshdi, bu mavsumiy gripp tarqalayotganidan dalolat beradi"*.
4. **Wisdom (Donolik / To'g'ri qaror):** Bilim asosida to'g'ri, maqsadli va strategik qaror qabul qilish. Masalan: *"Maktabda darslarni 3 kunga onlayn formatga o'tkazish va binoni dezinfeksiya qilish to'g'risida buyruq chiqarish"*.

```text
       /\
      /  \     WISDOM (Strategik qarorlar qabul qilish)
     /----\
    /      \    KNOWLEDGE (Qonuniyatlar va tahliliy xulosalar)
   /--------\
  /          \   INFORMATION (Tartiblangan, tushunarli axborot)
 /------------\
/              \  DATA (Xom raqamlar, loglar, kliklar)
----------------
```

---

### 2. Ma’lumotlar muhandisligi (Data Engineering) nima?

Ko'pincha odamlar sun'iy intellekt (AI) va chiroyli grafiklar (BI Dashboard) haqida gapirishadi. Ammo bitta achchiq haqiqat bor: **agar ma'lumotlar iflos, chalkash, kechikkan yoki noto'g'ri bo'lsa, eng zo'r Machine Learning modeli ham safsata bashorat beradi** ("Garbage In, Garbage Out").

**Ma’lumotlar muhandisligi (Data Engineering)** — turli manbalardan (veb-saytlar, mobil ilovalar, sensorlar, bank tranzaksiyalari) kelib tushadigan katta hajmdagi xom ma'lumotlarni ishonchli, xavfsiz va uzluksiz yig'ish, tozalash, saqlash va ularni analitiklar (BI) hamda Machine Learning muhandislari uchun tayyor holatga keltiruvchi infratuzilmani qurish sohasidir.

#### Mutaxassislar farqi:
- **Data Engineer:** "Santexnik va arxitektor". U quvurlarni (data pipeline) yotqizadi, suv (ma'lumot) toza va to'xtovsiz oqishini ta'minlaydi, omborlar (DWH, Data Lake) quradi.
- **Data Analyst / BI Developer:** "Hisobotchi va dizayner". U toza ma'lumotlarni olib, interaktiv dashboardlar, trendlar va grafiklar chizadi.
- **Data Scientist / ML Engineer:** "Olim va bashoratchi". U toza ma'lumotlar asosida matematik va sun'iy intellekt modellarini o'qitadi, kelajakni bashorat qiladi.

---

### 3. Data Pipeline (Ma'lumotlar quvuri) nima?

**Data Pipeline** — ma'lumotlarni manbadan (Source) to yakuniy foydalanuvchi yoki tizimga (Destination) yetkazib beruvchi avtomatlashtirilgan jarayonlar ketma-ketligidir.

Data Pipeline'ning asosiy bosqichlari:
1. **Ingest (Yig'ish):** Ma'lumotlarni turli manbalardan (API, loglar, CSV, ma'lumotlar bazasi) qabul qilish.
2. **Transform (Qayta ishlash va tozalash):** Noto'g'ri qiymatlarni tuzatish, duplikatlarni olib tashlash, ma'lumot turlarini moslashtirish, agregatsiya qilish.
3. **Store (Saqlash):** Ma'lumotlar omboriga (PostgreSQL, Data Warehouse, Parquet) xavfsiz yozish.
4. **Serve (Taqdim etish):** BI dashboardlar va ML modellari uchun tahlilga berish.

---

### 4. Real dunyo keysi: Netflix qanday ishlaydi?

Tasavvur qiling, siz Netflix'da biror kinoni ko'rishni boshladingiz:
1. Siz pleyerni to'xtatdingiz (pause), 10 sekund orqaga qaytardingiz yoki kinoni oxirigacha ko'rmay chiqib ketdingiz.
2. Bu harakatlarning har biri soniyasiga millionlab foydalanuvchilardan **xom ma'lumot (event log)** sifatida serverga keladi.
3. **Data Engineer** yozgan Apache Kafka va Apache Spark quvurlari ushbu ma'lumotlarni real vaqt rejimida yig'adi, tozalaydi va saqlaydi.
4. **Data Scientist** ushbu tozalangan ma'lumotlar asosida: *"Foydalanuvchi filmni 15-daqiqasida tashlab ketdi, demak unga bu janr yoqmadi"* degan xulosaga keladi va sizning bosh sahifangizga boshqa kinoni tavsiya qiladi.

---

## Amaliy topshiriqlar (Sinfda bajarish uchun)

### 1-topshiriq: Xom ma'lumotdan axborotga: Python orqali tahlil

**Vazifa:** Quyidagi xom ma'lumotlar ro'yxati berilgan (o'quvchilar ID raqami va ularning imtihon ballari):
`data = [("Olim", 85), ("Zarina", 92), ("Jasur", 45), ("Madina", 78), ("Aziz", 40), ("Malika", 95)]`
Python skripti yordamida:
1. Sinfdagi o'rtacha ballni hisoblang;
2. Qoniqarsiz baho olgan (balli 60 dan past) o'quvchilarni ajratib oling;
3. Olingan natijani DIKW piramidasi nuqtai nazaridan (Data vs Information) izohlang.

**Yechim:**
```python
# 1. Xom ma'lumotlar (Data)
students = [
    {"name": "Olim", "score": 85},
    {"name": "Zarina", "score": "92"},  # xom ma'lumotda satr (String) bo'lishi mumkin!
    {"name": "Jasur", "score": 45},
    {"name": "Madina", "score": 78},
    {"name": "Aziz", "score": 40},
    {"name": "Malika", "score": 95}
]

# 2. Tozalash va hisoblash (Engineering & Processing)
total_score = 0
failed_students = []

for s in students:
    # Ma'lumot turini to'g'rilash (Data cleaning)
    score = int(s["score"])
    total_score += score
    if score < 60:
        failed_students.append(s["name"])

avg_score = total_score / len(students)

# 3. Axborot (Information)
print(f"Sinfning o'rtacha bali: {avg_score:.1f}")
print(f"Qo'shimcha darsga muhtoj o'quvchilar: {', '.join(failed_students)}")
```
**Izoh:**
- Xom sonlar (85, 92, 45...) — bu **Data**.
- O'rtacha ball 72.5 ekani va 2 nafar o'quvchi yiqilgani — bu **Information**.
- "Jasur va Azizga matematika fanidan qo'shimcha repetitor ajratish" haqidagi qaror — bu **Wisdom**.

---

### 2-topshiriq: YouTube Data Pipeline bosqichlarini modellashtirish

**Vazifa:** Foydalanuvchi YouTube'da yangi video yuklaganda va tomoshabinlar uni ko'rganda sodir bo'ladigan jarayonlarni Data Pipeline ning 4 ta bosqichiga ajrating:
1. Ingestion (Ma'lumot qayerdan yig'iladi?)
2. Transformation (Qanday qayta ishlanadi?)
3. Storage (Qayerda saqlanadi?)
4. Consumption / Serving (Kimga va qanday ko'rinishda beriladi?)

**Yechim:**
1. **Ingestion:** Mobil ilova va veb-saytdan foydalanuvchi harakatlari (ko'rish vaqti, layk, dislike, izoh, videoni o'tkazib yuborish).
2. **Transformation:** Video ko'rish davomiyligi (Watch time %) hisoblanadi, spam izohlar filtrlanadi, botlar tomonidan qilingan sun'iy ko'rishlar tozalanadi.
3. **Storage:** Xom loglar Data Lake (masalan, Google Cloud Storage)da saqlanadi, qayta ishlangan statistik ma'lumotlar esa analitik omborga (BigQuery / DWH) yoziladi.
4. **Consumption / Serving:** 
   - Muallif uchun: YouTube Studio Dashboard'ida tomoshalar grafigi va daromad ko'rsatiladi;
   - ML Tavsiya tizimi uchun: boshqa tomoshabinlarning "Tavsiya etilgan videolar" lentasiga chiqariladi.

---

### 3-topshiriq: "Data to Decision" biznes keysi

**Vazifa:** Elektron tijorat (masalan, Uzum Market) do'koni ma'lumotlar bazasida oxirgi haftada 10 000 ta savatga tovar qo'shilgan, lekin ularning 4 000 tasi to'lov qilinmasdan tashlab ketilgan.
1. Bu vaziyatda xom Data nima?
2. Qanday Information hosil qilish mumkin?
3. Qanday Knowledge paydo bo'ladi?
4. Rahbariyat qanday Wisdom (qaror) qabul qilishi kerak?

**Yechim:**
1. **Data:** `cart_id, user_id, item_id, price, status='abandoned', timestamp`.
2. **Information:** Savatlarning 40% i xarid bilan tugallanmagan, eng ko'p tashlab ketilgan mahsulotlar toifasi — yirik maishiy texnika (muzlatgich, televizor).
3. **Knowledge:** Foydalanuvchilar to'lov sahifasiga yetganda, yetkazib berish narxi to'satdan qimmat chiqqani sababli xaridni to'xtatgani aniqlandi.
4. **Wisdom (Qaror):** Yirik texnika uchun "Bepul yetkazib berish aksiyasi"ni e'lon qilish yoki to'lov bosqichida bo'lib to'lash (muddatli to'lov) tugmasini birinchi o'ringa chiqarish.

---

## Tezkor savol-javob (Quick Check)

1. **Savol:** DIKW piramidasida Data va Information o'rtasidagi asosiy farq nima?  
   **Javob:** Data — bu kontekstsiz xom belgilar va raqamlar to'plami. Information — bu qayta ishlangan, ma'lum kontekst va savollarga javob beradigan tartibli ma'lumotdir.

2. **Savol:** Data Engineer ning asosiy vazifasi nima?  
   **Javob:** Ma'lumotlarni uzluksiz, toza va xavfsiz holatda yig'ish, tozalash, saqlash va ularni analitika hamda Machine Learning uchun yetkazib beruvchi ma'lumotlar quvurlarini (Data Pipeline) qurish.

3. **Savol:** "Garbage In, Garbage Out" qoidasi nimani anglatadi?  
   **Javob:** Agar modelga yoki tahlil tizimiga xato va iflos ma'lumot berilsa, natijada olinadigan tahlil va bashorat ham mutlaqo xato va foydasiz bo'ladi.

4. **Savol:** Data Pipeline ning 4 ta asosiy qadamini sanang.  
   **Javob:** Ingestion (qabul qilish), Transformation (tozalash/o'zgartirish), Storage (saqlash), Serving (taqdim etish).

5. **Savol:** Nima uchun Netflix kabi kompaniyalar Data Engineering ga katta sarmoya kiritadi?  
   **Javob:** Chunki millionlab foydalanuvchilarning real vaqtdagi harakatlarini tahlil qilib, ularga mos tavsiyalar berish orqali mijozlarni platformada ushlab qolish va daromadni oshirish mumkin.

---

## Uyga vazifa

1. DIKW piramidasining 4 ta bosqichini o'zingizning kundalik hayotingizdan bitta misol asosida (masalan, telefon batareyasi yoki sport mashg'ulotlari) tahlil qilib yozing.
2. Data Engineer, Data Analyst va Data Scientist kasblarining asosiy vositalari va farqlarini taqqoslovchi kichik jadval tuzing.
3. Biror mashhur mobil ilovani (masalan, Telegram yoki Spotify) tanlang va undagi bitta harakatingiz qanday ma'lumot quvuridan (Data Pipeline) o'tishini tasavvur qilib yozing.
