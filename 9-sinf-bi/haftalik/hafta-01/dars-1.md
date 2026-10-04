# 1-dars. Ma’lumot tushunchasi, uning turlari va DIKW modeli

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga ma’lumot (data) tushunchasi, uning zamonaviy iqtisodiyotdagi strategik o'rni, ma’lumotlarning asosiy turlari (miqdoriy, sifat, strukturaviy, yarim-strukturaviy, nostrukturaviy) hamda DIKW piramidasi (Data → Information → Knowledge → Wisdom) mantiqiy zanjirini tushuntirish.
- **Kutiladigan natija:** O'quvchilar xom ma'lumot va mazmunli axborot farqini biladi; ma'lumotlarni toifalarga ajrata oladi; DIKW piramidasi bosqichlarini real biznes misolida amalda tahlil qila oladi.
- **Vaqt taqsimoti:**
  - Tashkiliy qism va kirish: 10 daqiqa
  - Nazariy konspekt (Ma'lumot tushunchasi va turlari): 20 daqiqa
  - DIKW modeli va real keyslar tahlili: 20 daqiqa
  - Amaliy mashg'ulot va topshiriqlar: 20 daqiqa
  - Tezkor nazorat va xulosa: 10 daqiqa

---

## Mentor konspekti

### 1. Ma’lumot (data) nima?
Ma’lumot (data) — bu real hayotdagi hodisalar, jarayonlar yoki obyektlar haqida o‘lchangan, qayd etilgan yoki yig‘ilgan xom faktlar majmuasidir.
Ma’lumot o‘z holicha faqat "xom material" hisoblanadi. Masalan, shunchaki `25`, `Toshkent`, `olma` so'zlari yoki raqamlari alohida olinganda hech qanday foydali xulosa bermaydi. Ular tahlil qilinib, kontekst berilgandagina qaror qabul qilishga yordam beradigan qimmatli resursga aylanadi.

### 2. Ma’lumotlarning asosiy tasnifi
Rasmiy o'quv qo'llanmaga muvofiq, ma'lumotlar quyidagi turlarga bo'linadi:
1. **Miqdoriy ma’lumotlar (Quantitative Data):** Sonlar va o'lchovlar bilan ifodalanadi.
   - *Diskret (Discrete):* Butun sonlar (masalan, do'konga kirgan 14 nafar xaridor, 5 dona noutbuk).
   - *Uzluksiz (Continuous):* Ma'lum shkala bo'yicha uzluksiz o'lchanadigan qiymatlar (masalan, havo harorati 24.5°C, og'irlik 72.3 kg).
2. **Sifat ma’lumotlar (Qualitative Data):** Sonlarda emas, balki so'zlar, toifalar va tavsiflar orqali ifodalanadi (mijoz sharhlari: "juda yoqdi", mahsulot rangi: "qizil", holati: "yaroqli").
3. **Strukturaviy ma’lumotlar (Structured Data):** Aniq qator va ustunlarga ega jadvallar (Excel, SQL ma'lumotlar bazalari). Oson qidiriladi va tahlil qilinadi.
4. **Nostrukturaviy ma’lumotlar (Unstructured Data):** Oldindan belgilangan jadval shakliga ega bo'lmagan ma'lumotlar (rasmlar, audio yozuvlar, PDF hujjatlar, xabarlar). Bugungi kunda dunyodagi barcha ma'lumotlarning 80% dan ortig'i nostrukturaviydir!
5. **Yarim-strukturaviy ma’lumotlar (Semi-Structured Data):** Qat'iy jadval emas, lekin ma'lumotni belgilab turuvchi teglar mavjud (JSON, XML fayllar).

### 3. DIKW Piramidasi (Ma'lumotlar evolyutsiyasi)
DIKW piramidasi xom faktlarning qanday qilib oqilona qarorga aylanishini ko'rsatuvchi klassik modeldir:
- **Data (Ma’lumot):** Kontekstsiz xom fakt. Misol: `39` raqami.
- **Information (Axborot):** Ma'lumotga "kim, nima, qachon, qayerda?" degan kontekst berilishi. Misol: "Bugun Buxoroda havo harorati 39°C ga yetdi".
- **Knowledge (Bilim):** Tajriba va tahlil asosida hosil qilingan qonuniyat ("Nega?"). Misol: "Buxoroda harorat 38°C dan oshganda, shahar bo'ylab muzdek ichimliklar va muzqaymoqqa bo'lgan talab 60% ga ortadi".
- **Wisdom (Donolik):** Bilimga asoslanib to'g'ri, istiqbolli strategik qaror qabul qilish. Misol: "Ertaga havo harorati 40°C bo'lishi kutilmoqda. Shu sababli markaziy savdo nuqtalariga qo'shimcha 1000 dona muzqaymoq yetkazib berish va sovutkichlarni tekshirish buyrug'i berilsin".

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Ma'lumot turlarini tasniflash (oson)
Berilgan misollarni mos ma'lumot turiga (Miqdoriy diskret, Miqdoriy uzluksiz, Sifat, Nostrukturaviy) ajrating:
1. Maktabdagi kompyuterlar soni (30 dona).
2. Xodimning bir oylik ish safari uchun yoqilg'i sarfi (45.8 litr).
3. "Kuryer xizmati juda tez va xushmuomala" degan mijoz sharhi.
4. Xavfsizlik kamerasidan olingan 15 soniyalik video yozuv.

**Yechim:**
1. Miqdoriy diskret (chunki narsalar butun sonlarda sanaladi).
2. Miqdoriy uzluksiz (chunki suyuqlik hajmi o'lchanadi va o'nlik kasr bo'lishi mumkin).
3. Sifat (chunki tavsifiy matn, hissiyot va fikrni ifodalaydi).
4. Nostrukturaviy (chunki video fayl aniq jadval strukturasiga ega emas).

### 2-topshiriq. Savdo jarayonida DIKW zanjirini tuzish (o'rta)
Kiyim-kechak do'koni uchun quyidagi elementlarni DIKW piramidasining to'g'ri bosqichlariga joylashtiring:
- A: "Qish yaqinlashganda va havo harorati 5°C dan pasayganda qalin kurtkalarga talab 3 barobar ortadi".
- B: "10, 150, kurtka, 05-noyabr".
- C: "Do'konda 5-noyabr kuni 10 dona kurtka 150 dollardan sotildi".
- D: "Noyabr oyi boshida kurtkalar zaxirasini 200 taga yetkazish va aksiyani 1-noyabrdan boshlash kerak".

**Yechim:**
- Data (Ma'lumot): B ("10, 150, kurtka, 05-noyabr" — xom qiymatlar).
- Information (Axborot): C ("Do'konda 5-noyabr kuni 10 dona kurtka..." — kontekst berilgan ma'lumot).
- Knowledge (Bilim): A ("Qish yaqinlashganda... talab 3 barobar ortadi" — tahlil va qonuniyat).
- Wisdom (Donolik): D ("Noyabr oyi boshida zaxirani 200 taga yetkazish..." — aniq boshqaruv qarori).

### 3-topshiriq. Sensor ma'lumotlarini tahlil qilish (qiyin)
Aqlli issiqxona (Smart Greenhouse) tizimi har 10 daqiqada quyidagi qatorni yozib oladi:
`{"sensor_id": "TEMP_01", "val": 34.2, "unit": "C", "status": "WARN", "time": "14:20"}`
1. Bu ma'lumot qaysi strukturaviy turga kiradi?
2. Ushbu ma'lumot qanday qilib Information va Knowledge bosqichlariga aylanadi?
3. Wisdom bosqichida qanday avtomatlashtirilgan harakat amalga oshirilishi lozim?

**Yechim:**
1. Yarim-strukturaviy (Semi-Structured Data), chunki JSON formati orqali kalit-qiymat tuzilmasiga ega.
2. Information: "TEMP_01 sensori soat 14:20 da harorat 34.2°C ga ko'tarilganini va bu me'yordan yuqoriligi (WARN)ni qayd etdi". Knowledge: "Agar issiqxonada harorat soat 14:00 dan 16:00 gacha 32°C dan oshsa, pomidor gullari to'kilishi va hosildorlik 20% ga pasayishi kuzatiladi".
3. Wisdom: Tizim zudlik bilan avtomatik sovutish va soyabon ventilyatorlarini ishga tushiradi hamda agronom telefoniga ogohlantirish xabarini yuboradi.

---

## Tezkor nazorat savollari

1. Xom ma’lumot (data) va axborot (information) o‘rtasidagi tub farq nimada?
   - *Javob:* Ma’lumot kontekstsiz xom fakt bo‘lsa, axborot unga kontekst, ma’no va aniq maqsad yuklangan ko‘rinishidir.
2. Nima sababdan fototasvirlar nostrukturaviy ma’lumot hisoblanadi?
   - *Javob:* Chunki ularda relyatsion jadvallarga xos ustun va satrlar bo‘lmaydi, piksellar majmuasidan iborat.
3. DIKW modelidagi Knowledge (Bilim) bosqichi qanday savolga javob beradi?
   - *Javob:* "Nima uchun?" (sabab-oqibat bog'liqligi va qonuniyatlar).

---

## Uyga vazifa

O'zingiz qiziqqan biror soha (masalan, futbol jamoasi, mobil o'yin yoki maktab oshxonasi) misolida DIKW piramidasining to'rttala bosqichini (Data, Information, Knowledge, Wisdom) aniq yozib keling.
