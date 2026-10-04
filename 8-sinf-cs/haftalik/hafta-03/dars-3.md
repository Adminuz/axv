# 9-dars. Raqamli transformatsiya tushunchasi

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliy keys-tahlil · **II-bob**, 3-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarda raqamli transformatsiya (Digital Transformation) tushunchasi, an'anaviy jarayonlarni raqamlashtirishning mohiyati, zamonaviy texnologiyalarning ta'lim (e-maktab, onlayn platformalar), biznes (raqamli banklar, fintech, elektron tijorat) va davlat xizmatlaridagi (my.gov.uz, elektron litsenziyalar) o'rni, qog'ozsiz elektron hujjat aylanishi (EDO), elektron raqamli imzo (ERI) hamda transformatsiya jarayonida xavfsizlik va moslashuvchanlik bo'yicha tizimli bilim va amaliy tushunchalarni shakllantirish.

**Kutiladigan natija:**
- Raqamlashtirish bosqichlarini (Digitization → Digitalization → Digital Transformation) aniq farqlay oladi.
- Davlat xizmatlari (my.gov.uz), ta'lim (e-maktab) va biznes sohalaridagi raqamli o'zgarishlarni real hayotiy misollarda tushuntira oladi.
- Elektron hujjat aylanishi (EDO) va elektron raqamli imzo (ERI) qanday ishlashini biladi.
- Raqamli transformatsiyaning afzalliklari (tezkorlik, qulaylik, shaffoflik, xarajatlarni tejash) va yuzaga keladigan xatarlar (kiberxavflar, tizim uzilishlari) tahlilini amalga oshira oladi.
- Zamonaviy raqamli servislar orqali oddiy so'rov yuborish yoki amaliy keysni bosqichma-bosqich yechish ko'nikmasiga ega bo'ladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | O'tgan darsni takrorlash (raqamli madaniyat, feyk xabarlar). Muammoli vaziyat: «O'n yil oldin pasport olish yoki bankdan pul o'tkazish uchun nimalar qilish kerak edi va hozir bu jarayon qanday amalga oshiriladi?» |
| 10–35 daq | Yangi mavzu: Nazariya | Raqamli transformatsiya mohiyati, 3 ta bosqich, davlat xizmatlari (my.gov.uz), ta'lim, fintech, qog'ozsiz hujjat aylanishi va axborot xavfsizligi |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliy mashg'ulot | Keys-tahlil: «An'anaviy maktab kutubxonasini to'liq raqamli tizimga aylantirish loyihasi» va my.gov.uz portali arxitekturasi bilan tanishish |
| 65–75 daq | Tezkor nazorat | 5 ta test/savol va mini-debat («Raqamli tizimlar inson mehnatini to'liq almashtira oladimi?») |
| 75–80 daq | Xulosa va uyga vazifa | Asosiy tushunchalarni umumlashtirish, hafta xulosasi va uyga vazifa yo'riqnomasi |

---

## 2. Dars konspekti

### 2.1. Raqamli transformatsiya (Digital Transformation) nima?

**Raqamli transformatsiya (Digital Transformation - DX)** — bu raqamli texnologiyalarni inson hayoti, biznes faoliyati va davlat boshqaruvining barcha jabhalariga chuqur integratsiya qilish orqali mavjud jarayonlarni tubdan o'zgartirish, tezlashtirish va sifat jihatidan yangi bosqichga olib chiqish jarayonidir.

Raqamlashtirishning uchta asosiy pog'onasi:
1. **Digitization (Raqamli ko'rinishga keltirish):** Jismoniy yoki qog'ozdagi axborotni raqamli formatga (faylga) o'tkazish. Masalan: qog'oz hujjatni skanerlab PDF qilish yoki qo'lda yozilgan daftarni kompyuterda Word fayliga ko'chirish.
2. **Digitalization (Raqamlashtirish):** Raqamli ma'lumotlar yordamida mavjud ish jarayonlarini optimallashtirish. Masalan: hisobotlarni qog'ozda emas, balki Excel yoki elektron pochta orqali almashish.
3. **Digital Transformation (Raqamli transformatsiya):** Butun tizim, madaniyat va xizmat ko'rsatish modelini zamonaviy texnologiyalar (AI, bulut, API, mobil ilovalar) asosida tubdan qayta qurish. Masalan: jismoniy bankka bormasdan, mobil ilova orqali bir necha soniyada hisob ochish, kredit olish va to'lovlarni amalga oshirish.

```
+---------------------------------------------------------------+
| 1. Digitization        -->  Qog'ozni PDF / faylga aylantirish |
| 2. Digitalization      -->  Jarayonni kompyuterda bajarish    |
| 3. Digital Transf.     -->  Yangi biznes-model va avtomatika  |
+---------------------------------------------------------------+
```

### 2.2. Davlat xizmatlarida raqamli transformatsiya

Ilgari biror ma'lumotnoma (yashash joyidan, o'qish joyidan yoki sudlanmaganlik haqida) olish uchun turli idoralarga borish, navbatda turish va bir necha kun kutish talab etilardi.

Hozirgi davlat xizmatlari ekotizimi:
- **my.gov.uz (Yagona interaktiv davlat xizmatlari portali):** 500 dan ortiq davlat xizmatlari yagona darcha orqali elektron taqdim etiladi.
- **Elektron raqamli imzo (ERI):** Jismoniy va yuridik shaxslarning elektron hujjatdagi shaxsiy imzosining qonuniy ekvivalenti bo'lib, hujjatning haqiqiyligini kafolatlaydi.
- **OneID (Yagona identifikatsiya tizimi):** Barcha davlat va rasmiy axborot tizimlariga bitta login va parol orqali xavfsiz kirish imkonini beruvchi tizim.
- **Qog'ozsiz hujjat aylanishi (EDO):** Tashkilotlar o'rtasida shartnomalar, schyot-fakturalar va buyruqlarni qog'ozsiz, ERI orqali tasdiqlangan elektron shaklda uzatish.

### 2.3. Ta'lim va biznes sohalaridagi transformatsiya

1. **Ta'limda:**
   - **e-maktab (Kundalik.com):** Elektron jurnallar, o'quvchilar baholari, dars jadvallari va ota-onalar uchun real vaqt monitoringi.
   - **Onlayn ta'lim platformalari (Coursera, edX, Khan Academy):** Dunyoning istalgan nuqtasidan sifatli bilim olish imkoniyati.
   - **Elektron darsliklar va virtual laboratoriyalar:** Og'ir qog'oz darsliklar o'rniga interaktiv multimedia vositalari.

2. **Biznes va moliya sohasida (Fintech):**
   - **Raqamli banklar va to'lov tizimlari (Click, Payme, Uzum, Anorbank):** 24/7 rejimida kartadan kartaga pul o'tkazish, kommunal to'lovlar, omonat ochish.
   - **Elektron tijorat (E-commerce):** Uzum Market, Amazon kabi platformalarda mahsulotlarni uydan chiqmasdan xarid qilish va yetkazib berish.
   - **Avtomatlashtirilgan kuryerlik va logistika:** Buyurtmaning qayerda kelayotganini xaritada real vaqtda kuzatish (GPS tracking).

### 2.4. Raqamli transformatsiyaning afzalliklari va qiyinchiliklari

**Afzalliklari:**
- **Tezkorlik:** Bir necha kunlik jarayonlar soniyalar ichida hal bo'ladi.
- **Shaffoflik va korrupsiyaning oldini olish:** Inson omili aralashmaydigan avtomatlashtirilgan tizimlarda adolatli xizmat ko'rsatiladi.
- **Iqtisodiy tejamkorlik:** Tonnalab qog'oz, printer bo'yog'i, arxiv xonalari va transport xarajatlari tejaladi.
- **24/7 qulaylik:** Xizmatlardan haftaning istalgan kuni va soatida foydalanish mumkin.

**Xavflar va qiyinchiliklar:**
- **Kiberxavfsizlik xavfi:** Barcha ma'lumotlar serverlarda saqlangani sababli hakerlik hujumlari va ma'lumotlar sizib chiqish xavfi ortadi.
- **Tizim nosozliklari:** Elektr energiyasi yoki internet uzilib qolsa, butun ish to'xtab qolishi mumkin.
- **Raqamli tengsizlik (Digital Divide):** Barcha insonlarda ham zamonaviy qurilmalar yoki yuqori tezlikdagi internet bo'lmasligi mumkin.
- **Xodimlarning tayyor emasligi:** Yangi dasturlar bilan ishlash uchun odamlarni qayta o'qitish zarurati.

---

## 3. Amaliy mashg'ulotlar va keyslar

### 1-mashq. Bosqichlarni ajratish (Digitization vs Digitalization vs DX)
**Vazifa:** Quyidagi holatlarning qaysi biri Digitization, qaysi biri Digitalization va qaysi biri Raqamli Transformatsiya ekanligini aniqlang:
1. Maktab kutubxonachisi barcha kitoblar ro'yxatini daftardan Excel jadvaliga ko'chirib yozib chiqdi.
2. Har bir kitobga QR-kod yopishtirildi va o'quvchi kitobni qaytarganda skaner orqali tizimga avtomatik belgilandi.
3. Maxsus mobil ilova yaratildi: o'quvchi istalgan kitobni ilovadan qidiradi, uning bandligini ko'radi, elektron nusxasini o'qiydi yoki audio formatini tinglaydi, sun'iy intellekt esa unga qiziqishiga qarab yangi kitoblar tavsiya qiladi.

**Yechim:**
1. **Digitization** — ma'lumot qog'ozdan raqamli faylga ko'chirildi.
2. **Digitalization** — mavjud kutubxona jarayoni kompyuter va skaner yordamida tezlashtirildi.
3. **Raqamli transformatsiya (DX)** — kitob o'qish va kutubxona xizmati tubdan yangi, to'liq avtomatlashgan, sun'iy intellektga asoslangan raqamli formatga o'tdi.

---

### 2-mashq. my.gov.uz va an'anaviy xizmat tahlili
**Vazifa:** Yashash joyidan ma'lumotnoma olishning «Eski usuli» va «my.gov.uz orqali yangi usuli»ni quyidagi parametrlar bo'yicha jadvalda taqqoslang: vaqt, xarajat, kerakli qog'ozlar soni, inson omili.

**Yechim:**
| Parametr | Eski usul (an'anaviy) | my.gov.uz orqali (raqamli) |
|---|---|---|
| Sarflanadigan vaqt | 1–3 kun (mahalla va hokimiyatga borish) | 1–2 daqiqa |
| Transport va boshqa xarajatlar | Yo'l haqi, qog'oz nusxalari (kopiya) | 0 so'm (uydan turib) |
| Kerakli hujjatlar | Pasport nusxasi, ariza qog'ozi, ma'lumotnoma blankasi | Shaxsiy JShShIR orqali avtomatik ma'lumot |
| Inson omili | Mansabdor shaxsning kayfiyati, navbatlar, xatoliklar | 100% avtomatlashgan, QR-kodli rasmiy hujjat |

---

## 4. Tezkor savollar (Checklist)

1. Digitization va Raqamli transformatsiyaning farqi nimada?
   - **Javob:** Digitization shunchaki qog'ozdagi axborotni raqamli faylga ko'chirishdir. Raqamli transformatsiya esa butun xizmat va jarayonni yangi texnologiyalar yordamida tubdan avtomatlashtirish va yangilashdir.
2. Elektron raqamli imzo (ERI) nima uchun kerak?
   - **Javob:** Elektron hujjatlarning haqiqiyligini tasdiqlash va qonuniy kuch berish uchun jismoniy imzo o'rnida ishlatiladi.
3. OneID tizimining vazifasi nima?
   - **Javob:** Davlat axborot portallariga yagona identifikatsiya orqali xavfsiz kirishni ta'minlash.
4. Raqamli transformatsiya korrupsiyani qanday kamaytiradi?
   - **Javob:** Inson omilini kamaytiradi; xizmatlar avtomatik tarzda shaffof algoritmlar asosida ko'rsatiladi va har bir harakat tizimda qayd etiladi.
5. Raqamli transformatsiyaning eng katta xavfi nima?
   - **Javob:** Kiberxavfsizlik tahdidlari (hakerlik hujumlari, shaxsiy ma'lumotlarning tarqalishi) va tizimning texnik nosozliklarga bog'liqligi.
