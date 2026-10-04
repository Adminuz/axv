# 1-dars. Zamonaviy kompyuterlar va ularning arxitekturasi

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + ko'rgazmali amaliyot · **I-bob**, 1-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarda zamonaviy kompyuterlar turlari, fon Neyman tamoyili asosidagi kompyuter arxitekturasi, asosiy va qo'shimcha qurilmalar, protsessor, xotira turlari (RAM, ROM, SSD/HDD) hamda kompyuterning ishlash tamoyili bo'yicha mustahkam fundamental tushunchalarni shakllantirish.

**Kutiladigan natija:**
- Kompyuter turlarini (statsionar, noutbuk, monoblok, server, superkompyuter) farqlay oladi va vazifasini tushuntiradi.
- Kompyuter arxitekturasining asosiy qismlarini (protsessor, xotira, kiritish-chiqarish qurilmalari, shinalar) sxematik ifodalaydi.
- CPU (takt chastotasi, yadrolar soni), RAM va doimiy xotira (SSD/HDD) farqini va ularning kompyuter tezligiga ta'sirini biladi.
- Windows operatsion tizimida kompyuterning texnik ko'rsatkichlarini (protsessor modeli, RAM hajmi, disk turi) mustaqil aniqlay oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Tanishuv va kirish | O'quvchilar bilan tanishuv, «Computer Science Foundation» kursi maqsadi va qoidalari |
| 5–25 daq | Yangi mavzu: Nazariya | Kompyuter turlari, arxitekturasi (fon Neyman modeli), CPU, RAM, ROM, SSD/HDD, shinalar |
| 25–30 daq | Savol-javob va muhokama | «Nega kompyuter o'chganda ochilgan dasturlar yopiladi?», «RAM va SSD farqi nima?» |
| 30–35 daq | Tanaffus | Ko'z va tana mashqlari |
| 35–65 daq | Amaliy mashg'ulot | Kompyuter texnik ko'rsatkichlarini aniqlash (Task Manager, msinfo32, dxdiag) |
| 65–75 daq | Tezkor nazorat | 5 ta test/savol orqali bilimlarni tekshirish |
| 75–80 daq | Xulosa va uyga vazifa | Asosiy xulosalar va uy vazifasini tushuntirish |

---

## 2. Dars konspekti

### 2.1. Zamonaviy kompyuterlar va ularning turlari

**Kompyuter** — axborotni qabul qilish, saqlash, qayta ishlash va foydalanuvchiga qulay ko'rinishda chiqarib berish uchun mo'ljallangan universal elektron hisoblash mashinasi.

Zamonaviy kompyuterlar vazifasi va o'lchamiga ko'ra quyidagi turlarga bo'linadi:
1. **Statsionar kompyuter (Desktop PC):** Ish stoli uchun mo'ljallangan, tizim bloki, monitor, klaviatura va sichqoncha alohida bloklardan iborat bo'ladi. Quvvati yuqori, qismlarini yangilash (upgrade) oson.
2. **Noutbuk (Laptop):** Barcha qurilmalari (ekran, klaviatura, touchpad, batareya) bitta ixcham korpusda jamlangan, ko'chma kompyuter.
3. **Monoblok (All-in-One):** Tizim bloki va monitor bitta umumiy korpusda birlashtirilgan kompyuter.
4. **Server:** Tarmoqdagi yuzlab yoki millionlab foydalanuvchilarga doimiy xizmat ko'rsatuvchi, 24/7 rejimida to'xtovsiz ishlaydigan kuchli kompyuter.
5. **Superkompyuter:** Sekundiga kvadtrillionlab murakkab matematik hisob-kitoblarni bajaradigan, ob-havo bashorati, kosmik tadqiqotlar va sun'iy intellekt modellarini o'rgatish uchun ishlatiladigan ulkan hisoblash tizimlari.

### 2.2. Kompyuter arxitekturasi va fon Neyman tamoyili

1945-yilda mashhur olim Jon fon Neyman tomonidan taklif etilgan tamoyilga ko'ra, har qanday zamonaviy kompyuter quyidagi 4 ta asosiy qismdan tashkil topadi:
1. **Aрифметик-mantiqiy qurilma va boshqaruv qurilmasi (CPU — Markaziy protsessor):** Barcha hisoblashlar va boshqaruvni amalga oshiradi.
2. **Xotira qurilmasi:** Dastur va ma'lumotlarni saqlash joyi (Ichki: RAM/ROM, Tashqi: SSD/HDD).
3. **Kiritish qurilmalari:** Ma'lumotlarni kompyuterga kiritish (klaviatura, sichqoncha, mikrofon, skaner).
4. **Chiqarish qurilmalari:** Natijalarni foydalanuvchiga taqdim etish (monitor, printer, dinamiklar).

Ushbu qismlar o'zaro **tizimli shina (System Bus)** orqali bog'langan bo'lib, ular orqali ma'lumotlar, manzillar va boshqaruv signallari harakatlanadi.

### 2.3. Tizim blokining asosiy komponentlari

- **Ona plata (Motherboard):** Barcha komponentlarni (CPU, RAM, videokarta, xotira disklari) o'zaro elektr va axborot magistrallari orqali bog'lovchi bosh elektron plata.
- **Markaziy protsessor (CPU — Central Processing Unit):** Kompyuterning «miyasi». U dastur buyruqlarini bajaradi. Asosiy ko'rsatkichlari:
  - *Takt chastotasi (GHz):* Protsessor bir sekundda bajara oladigan operatsiyalar soni (masalan, 3.2 GHz = sekundiga 3.2 milliard takt).
  - *Yadrolar soni (Cores):* Bir vaqtning o'zida parallel bajariladigan ishlar soni (2, 4, 8, 16 yadro).
- **Tezkor xotira (RAM — Random Access Memory):** Kompyuter ishlab turganda joriy dasturlar va ma'lumotlarni vaqtincha saqlovchi juda tezkor xotira. Kompyuter o'chirilganda RAM'dagi barcha ma'lumotlar o'chib ketadi (uchuvchan xotira).
- **Doimiy xotira (ROM — Read Only Memory):** Kompyuterni yoqish uchun zarur bo'lgan dastlabki tizim dasturlarini (BIOS/UEFI) saqlovchi xotira. Faqat o'qish uchun mo'ljallangan, o'chib ketmaydi.
- **Ma'lumotlarni saqlash disklari (HDD va SSD):**
  - *HDD (Hard Disk Drive):* Magnitli aylanuvchi disklarga asoslangan an'anaviy xotira. Sig'imi katta, lekin tezligi sekinroq (100–150 MB/s).
  - *SSD (Solid State Drive):* Mikrochiplar (flesh-xotira) asosidagi zamonaviy xotira. Mexanik harakatlanuvchi qismlari yo'q, ovozsiz va HDD dan 5–30 baravar tezroq (500–5000+ MB/s).
- **Videokarta (GPU — Graphics Processing Unit):** Grafik tasvirlar, animatsiyalar, videolar va 3D grafikalarni qayta ishlovchi va monitorga chiqaruvchi qurilma.
- **Quvvat ta'minoti bloki (Power Supply Unit — PSU):** 220V o'zgaruvchan tokni kompyuter qismlari uchun zarur bo'lgan doimiy 12V, 5V, 3.3V kuchlanishlarga aylantirib beruvchi blok.

---

## 3. Kod / Amaliy namuna

Kompyuterning texnik parametrlarini bilish dasturchi va IT mutaxassisi uchun muhim ko'nikmadir. Windows muhitida buni 3 ta asosiy usulda ko'rish mumkin:

### 1-usul: Vazifalar boshqaruvchisi (Task Manager)
1. Klaviaturada `Ctrl + Shift + Esc` tugmalarini bosing.
2. «Performance» (Samaradorlik) bo'limiga o'ting.
3. CPU, Memory (RAM), Disk (SSD/HDD), Wi-Fi va GPU parametrlarini kuzating.

### 2-usul: Tizim ma'lumotlari oynasi (msinfo32)
1. `Win + R` tugmalarini bosib, «Run» (Bajarish) darchasini oching.
2. `msinfo32` deb yozing va `Enter` bosing.
3. «System Summary» bo'limida protsessor modeli, BIOS versiyasi, operativ xotira hajmi va tizim turi ko'rinadi.

### 3-usul: DirectX diagnostika vositasi (dxdiag)
1. `Win + R` bosing, `dxdiag` deb yozing va `Enter` bosing.
2. Tizim va Displey bo'limlaridan videokarta va protsessor haqida to'liq hisobotni ko'ring.

---

## 4. Amaliy topshiriqlar

### 1-topshiriq (oson)
O'zingiz o'tirgan kompyuterda `Ctrl + Shift + Esc` orqali Task Manager dasturini oching. Protsessorning (CPU) nomini, uning joriy ish chastotasini va kompyuterdagi jami RAM (operativ xotira) hajmini aniqlang.

**Kutiladigan natija:** Protsessor nomi (masalan, Intel Core i5-11400 yoki AMD Ryzen 5 5600G) va RAM hajmi (masalan, 8 GB yoki 16 GB) daftarga yoziladi.

**Yechim:**
1. Klaviaturada `Ctrl + Shift + Esc` birgalikda bosiladi.
2. Chap yoki yuqori menyudan ikkinchi belgi — «Performance» (Samaradorlik) tanlanadi.
3. «CPU» tanlanganda o'ng yuqori burchakda protsessorning aniq modeli va pastda yadrolar soni (Cores/Logical processors) ko'rinadi.
4. «Memory» tanlanganda o'ng yuqori qismda jami RAM hajmi (masalan, `8.0 GB DDR4`) ko'rinadi.

---

### 2-topshiriq (o'rta)
`Win + R` orqali `msinfo32` darchasini oching. Quyidagi 4 ta ma'lumotni toping va yozib oling:
1. Operatsion tizim nomi (OS Name).
2. Tizim turi (System Type: 64-bit yoki 32-bit).
3. Protsessorning yadrolari soni (Cores).
4. O'rnatilgan jismoniy xotira (Installed Physical Memory / RAM).

**Kutiladigan natija:** Jadval shaklida 4 ta parametr aniq yoziladi.

**Yechim:**
1. `Win + R` bosiladi, ochilgan darchaga `msinfo32` yoziladi va `Enter` bosiladi.
2. «System Summary» ro'yxatidan qidiriladi:
   - OS Name: Masalan, *Microsoft Windows 11 Pro* yoki *Windows 10 Enterprise*.
   - System Type: *x64-based PC*.
   - Processor: Masalan, *11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz, 4 Core(s), 8 Logical Processor(s)*.
   - Installed Physical Memory (RAM): Masalan, *8.00 GB*.

---

### 3-topshiriq (qiyin)
Kompyuter xotira diskining turi (SSD yoki HDD) va bo'sh joyini aniqlang. Nima uchun zamonaviy dasturlashda HDD o'rniga SSD tavsiya etilishini texnik jihatdan asoslab bering.

**Kutiladigan natija:** Disk turi va hajmi ko'rsatiladi; SSD ning HDD dan 3 ta asosiy ustunligi (tezlik, shovqinsizlik, ishonchlilik) yoziladi.

**Yechim:**
1. Task Manager dasturida «Performance» → «Disk 0» bo'limiga kiriladi. U yerda disk turi ko'rsatilgan: masalan, `SSD` yoki `HDD`.
2. Model nomi (masalan, NVMe Kingston 512GB) va uning hajmi ko'rinadi.
3. Asoslash:
   - SSD da aylanuvchi magnit plastinka va harakatlanuvchi kallak yo'q, u butunlay mikrochiplarda ishlaydi.
   - O'qish/yozish tezligi: HDD da 100-150 MB/s bo'lsa, NVMe SSD larda 2000-5000+ MB/s ga yetadi (20-30 baravar tez).
   - Dasturlarni kompilyatsiya qilish, fayllarni yuklash va operatsion tizimning yuklanishi bir necha soniyada amalga oshadi.

---

## 5. Tezkor nazorat

1. Jon fon Neyman arxitekturasining 4 ta asosiy qismini sanab bering.
   - *Javob:* Markaziy protsessor (CPU), xotira (RAM/ROM/saqlash), kiritish qurilmalari, chiqarish qurilmalari.
2. RAM va SSD xotiralarining eng asosiy farqi nimada?
   - *Javob:* RAM — vaqtinchalik va juda tezkor (kompyuter o'chsa ma'lumot yo'qoladi); SSD — doimiy va ma'lumotlarni yillar davomida saqlaydi.
3. Protsessorning takt chastotasi (GHz) nimani bildiradi?
   - *Javob:* Protsessor bir sekundda bajara oladigan elektr impulslari (taktlari / amallari) sonini bildiradi. 1 GHz = 1 milliard takt/sekund.
4. Kiritish va chiqarish qurilmalariga 3 tadan misol keltiring.
   - *Javob:* Kiritish: klaviatura, sichqoncha, mikrofon, skaner. Chiqarish: monitor, dinamik (kolonka), printer.
5. Task Manager oynasini ochish uchun qaysi klavishlar kombinatsiyasi ishlatiladi?
   - *Javob:* `Ctrl + Shift + Esc` (yoki `Ctrl + Alt + Delete` orqali).

---

## 6. Uyga vazifa

Uyda yoki maktab kompyuterida o'z kompyuteringiz parametrlarini aniqlang va quyidagi jadvalni daftarga to'ldiring:
1. Kompyuter turi (statsionar, noutbuk yoki monoblok).
2. Protsessor modeli va takt chastotasi.
3. Operativ xotira (RAM) hajmi.
4. Doimiy xotira turi (HDD yoki SSD) va umumiy sig'imi.
5. Kompyuteringizga ulangan 2 ta kiritish va 2 ta chiqarish qurilmasi nomi.
Vazifani bajarish vaqti: 20 daqiqa.
