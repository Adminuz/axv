# 3-dars. Axborot o‘lchov birliklari va fayl turlari. Windows operatsion tizimida fayl hamda papkalar yaratish. Tezkor tugmalar (Hot keys)

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliy ko'nikmalar · **I-bob**, 3-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarda axborotning eng kichik birligidan (bit, bayt) tortib yirik o'lchovlarigacha (KB, MB, GB, TB) bo'lgan ierarxiyani hisoblash, fayl tushunchasi, fayl nomlari va kengaytmalari (.txt, .docx, .jpg, .png, .mp4, .exe, .py), Windowsda fayl va papkalarni yaratish, tartiblash, nusxalash, ko'chirish, o'chirish, qayta tiklash hamda eng muhim tezkor tugmalar (Ctrl+C, Ctrl+V, Ctrl+X, Ctrl+Z, Ctrl+A, F2, Delete, Shift+Delete) bilan tez va xatosiz ishlash ko'nikmalarini shakllantirish.

**Kutiladigan natija:**
- Axborot o'lchov birliklarini (bit, bayt, KB, MB, GB, TB) biladi va bir-biriga aylantira oladi (masalan, 1 MB = 1024 KB).
- Fayl nomi va kengaytmasi vazifasini tushuntiradi, asosiy fayl turlarini taniydi.
- Windowsda fayl va papka tuzilmasini daraxtsimon ierarxiya ko'rinishida tushunadi va to'g'ri tashkil qiladi.
- Fayl va papkalarni sichqonchasiz, klaviaturaning tezkor tugmalari (Ctrl+C, Ctrl+V, Ctrl+X, Ctrl+Z, F2) orqali professional boshqaradi.
- Savatcha (Recycle Bin) va to'liq o'chirish (Shift+Delete) xavfsizlik qoidalarini biladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 1–2-darslarni takrorlash (arxitektura, Windows interfeysi). «Bitta fotosurat kompyuter xotirasida qanday saqlanadi?» muammoli savol |
| 10–30 daq | Yangi mavzu: Nazariya | Axborot o'lchov birliklari (ikkilik tizim, 1024 koeffitsienti), fayl turlari va kengaytmalari, papkalar daraxti |
| 30–35 daq | Tanaffus | Ko'rish qobiliyatini yaxshilovchi mashqlar |
| 35–65 daq | Amaliy mashg'ulot | File Explorer'da papkalar tuzilmasini yaratish, fayl kengaytmalarini ko'rsatish, tezkor tugmalar bilan manipulyatsiya |
| 65–75 daq | Tezkor nazorat | 5 ta savol va hisoblash masalasi |
| 75–80 daq | Hafta xulosasi va uyga vazifa | 1-hafta umumiy xulosasi va uy vazifasi |

---

## 2. Dars konspekti

### 2.1. Axborot o'lchov birliklari

Kompyuter faqat elektr signallarini — tok bor (1) yoki tok yo'q (0) holatlarini tushunadi. 
- **Bit (Binary digit):** Axborotning eng kichik o'lchov birligi. U faqat `0` yoki `1` qiymatini qabul qiladi.
- **Bayt (Byte):** 8 ta bitning birlashmasi. 1 bayt xotiraga klaviaturadagi ixtiyoriy 1 ta harf, raqam yoki belgi (masalan, «A» yoki «7») sig'adi.

Kompyuterda ikkilik sanoq tizimi ($2^{10} = 1024$) ishlatilgani sababli keyingi birliklar 1000 emas, **1024** marta kattalashadi:
- **1 KB (Kilobayt)** = 1024 bayt (~1 varaq toza matn).
- **1 MB (Megabayt)** = 1024 KB (~1 ta kitob yoki 1 daqiqalik MP3 musiqa).
- **1 GB (Gigabayt)** = 1024 MB (~1 ta to'liq sifatli film).
- **1 TB (Terabayt)** = 1024 GB (~1000 ta film yoki butun boshli katta kutubxona).

*Hisoblash qoidasi:*
Kichik birlikdan kattasiga o'tishda $1024$ ga bo'linadi, kattasidan kichigiga o'tishda $1024$ ga ko'paytiriladi.

### 2.2. Fayl va uning turlari

**Fayl** — kompyuterning tashqi xotirasida (SSD yoki HDD da) umumiy nom bilan saqlanadigan, ma'lum turdagi axborotlar to'plami.
Har bir fayl ikkita asosiy qismdan iborat bo'lib, ular nuqta `.` bilan ajratiladi:
`fayl_nomi.kengaytma` (masalan: `referat.docx`, `foto.jpg`, `dastur.py`).

- **Fayl nomi:** Foydalanuvchi tomonidan beriladi (istalgan ma'noli nom).
- **Kengaytma (Extension):** Nuqtadan keyingi 3–4 ta harf bo'lib, faylning turini (formati) va uni qaysi dastur ochishini belgilaydi.

Eng ko'p ishlatiladigan kengaytmalar:
- **Matnli fayllar:** `.txt` (oddiy matn), `.docx` (Word hujjati), `.pdf` (elektron kitob/hujjat).
- **Grafik fayllar (Tasvirlar):** `.jpg` / `.jpeg` (fotosuratlar), `.png` (shaffof fonli tasvir), `.svg` (vektorli chizma).
- **Ovozli va video fayllar:** `.mp3`, `.wav` (musiqa); `.mp4`, `.mkv` (video).
- **Dastur va kod fayllari:** `.exe` (ishga tushuvchi dastur), `.py` (Python kodi), `.html` (veb-sahifa), `.zip` / `.rar` (arxiv).

### 2.3. Papka (Folder) va fayl tizimi tuzilmasi

**Papka (Katalog / Directory)** — fayllarni mavzular bo'yicha saralab, tartibli saqlash uchun mo'ljallangan «konvert» yoki «jild».
Papka ichida boshqa papkalar (ichki papkalar — subfolders) bo'lishi mumkin. Bu tuzilma **daraxtsimon ierarxiya** deyiladi.
Faylning to'liq manzili (Path) uning qaysi disk va qaysi papkalar ichidaligini ko'rsatadi:
`C:\Oquvchi\Darslar\8-sinf\1-dars.docx`

### 2.4. Fayl va papkalar ustida amallar

Windowsda fayl va papkalar bilan ishlashning 5 ta oltin amali:
1. **Yaratish:** Sichqonchaning o'ng tugmasi → New (Yaratish) → Folder / Text Document.
2. **Nomlash va qayta nomlash:** Faylni tanlab, `F2` tugmasini bosish.
3. **Nusxalash (Copy):** Asl nusxani o'z joyida qoldirib, uning dublikatini yaratish (`Ctrl + C`).
4. **Ko'chirish (Cut):** Faylni avvalgi joyidan sug'urib olib, yangi joyga ko'chirish (`Ctrl + X`).
5. **O'chirish (Delete):**
   - `Delete`: Faylni Savatchaga (Recycle Bin) yuboradi (qaytarib olish mumkin).
   - `Shift + Delete`: Faylni Savatchani aylanib o'tib, xotiradan butunlay o'chiradi (ehtiyot bo'lish shart!).

### 2.5. Eng muhim tezkor tugmalar (Hot keys)

| Tugmalar | Vazifasi |
|---|---|
| `Ctrl + C` | Tanlangan obyektni nusxalash (Copy) |
| `Ctrl + X` | Tanlangan obyektni qirqib olish (Cut) |
| `Ctrl + V` | Nusxalangan yoki qirqilgan obyektni qo'yish (Paste) |
| `Ctrl + Z` | Oxirgi xato amalni bekor qilish (Undo) |
| `Ctrl + A` | Papkadagi barcha fayllarni bir zumda tanlash (Select All) |
| `F2` | Tanlangan fayl yoki papka nomini o'zgartirish (Rename) |
| `Delete` | Savatchaga o'chirish |
| `Shift + Delete` | Butunlay qayta tiklanmas qilib o'chirish |
| `Win + E` | Fayl boshqaruvchisini (File Explorer) ochish |

---

## 3. Kod / Amaliy buyruqlar

Amaliy mashg'ulotda papkalar tuzilmasini yaratish mashqi:

```
D:\ (yoki C:\Users\Oquvchi\Documents)
└── CS_Foundation\
    ├── 01_Hujjatlar\
    │   └── reja.txt
    ├── 02_Rasmlar\
    │   └── kompyuter.png
    └── 03_Loyiha\
        └── dastur.py
```

File Explorer'da fayl kengaytmalarini ko'rinadigan qilish:
1. File Explorer'ni oching (`Win + E`).
2. Yuqori menyudan «View» (Ko'rinish) → «Show» (Ko'rsatish) bo'limiga o'ting.
3. «File name extensions» (Fayl nomining kengaytmalari) bandiga galochka qo'ying.

---

## 4. Amaliy topshiriqlar

### 1-topshiriq (oson)
`Win + E` orqali «Documents» (Hujjatlar) papkasiga kiring. Klaviaturadagi `Ctrl + Shift + N` tezkor tugmalari yordamida yangi papka oching va `F2` tugmasi bilan unga `Mening_Darslarim` deb nom bering.

**Kutiladigan natija:** «Documents» ichida `Mening_Darslarim` nomli yangi papka paydo bo'ladi.

**Yechim:**
1. `Win + E` bosiladi, chap paneldan «Documents» tanlanadi.
2. `Ctrl + Shift + N` birgalikda bosilganda yangi papka yaratiladi.
3. Klaviaturada darhol `Mening_Darslarim` yoziladi yoki `F2` bosilib qayta nomlanadi va `Enter` bosiladi.

---

### 2-topshiriq (o'rta)
Yaratilgan `Mening_Darslarim` papkasi ichiga kiring. Sichqonchaning o'ng tugmasi orqali yangi Text Document yarating va unga `malumot.txt` nomini bering.
Ushbu fayl ustida quyidagi amallarni bajaring:
1. `Ctrl + C` va `Ctrl + V` bilan uning nusxasini yarating.
2. Hosil bo'lgan ikkinchi faylni `F2` orqali `malumot_nusxa.txt` deb qayta nomlang.
3. `malumot_nusxa.txt` faylini tanlab `Delete` tugmasi bilan o'chiring.
4. Savatchani (Recycle Bin) ochib, o'chirilgan faylni toping va «Restore» (Qayta tiklash) buyrug'i bilan o'z joyiga qaytaring.

**Kutiladigan natija:** Fayl muvaffaqiyatli nusxalanadi, o'chiriladi va Savatchadan qayta tiklanadi.

**Yechim:**
1. Papka ichida bo'sh joyda o'ng tugma bosilib «New» → «Text Document» tanlanadi.
2. Fayl tanlanib `Ctrl + C`, so'ngra `Ctrl + V` bosiladi.
3. `F2` bosilib nomi `malumot_nusxa.txt` qilinadi.
4. Tanlanib `Delete` bosiladi. Ish stolidan «Recycle Bin» ochilib, fayl ustida o'ng tugma va «Restore» bosiladi.

---

### 3-topshiriq (qiyin)
Axborot o'lchov birliklari bo'yicha quyidagi hisoblash masalasini bajaring:
1. Bitta kompyuter diskining bo'sh joyi $4 \text{ GB}$ ni tashkil etadi.
2. Har bir fotosuratning o'rtacha hajmi $4 \text{ MB}$ ga teng.
Ushbu diskka eng ko'pi bilan nechta fotosurat sig'ishini qadamma-qadam hisoblab ko'rsating ($1 \text{ GB} = 1024 \text{ MB}$).

**Kutiladigan natija:** To'g'ri matematik hisob-kitob va fotosuratlar soni aniqlanadi.

**Yechim:**
1. Gigabaytni megabaytga aylantiramiz:
   $$4 \text{ GB} = 4 \times 1024 \text{ MB} = 4096 \text{ MB}$$
2. Sig'adigan rasmlar sonini topish uchun jami bo'sh joyni 1 ta rasm hajmiga bo'lamiz:
   $$\frac{4096 \text{ MB}}{4 \text{ MB}} = 1024 \text{ ta rasm}$$
3. Javob: Diskka aniq 1024 ta fotosurat sig'adi.

---

## 5. Tezkor nazorat

1. Axborotning eng kichik o'lchov birligi nima va 1 baytda nechta bit bor?
   - *Javob:* Eng kichik birlik — bit (0 yoki 1). 1 bayt = 8 bit.
2. 1 Megabaytda (MB) nechta Kilobayt (KB) bor?
   - *Javob:* 1024 KB.
3. Fayl kengaytmasi nima va u qanday vazifani bajaradi?
   - *Javob:* Nuqtadan keyin yoziladigan 3-4 harfli format belgisi. U fayl turini va uni qaysi dastur ochishini belgilaydi.
4. `Ctrl + C` va `Ctrl + X` buyruqlari o'rtasidagi asosiy farq nimada?
   - *Javob:* `Ctrl + C` nusxasini oladi (asli qoladi), `Ctrl + X` esa joyidan qirqib olib ko'chiradi (asli o'chadi).
5. `Shift + Delete` bosilganda fayl bilan nima sodir bo'ladi?
   - *Javob:* Fayl Savatchaga tushmasdan to'g'ridan-to'g'ri diskdan butunlay o'chiriladi.

---

## 6. Uyga vazifa

1. Axborot birliklarini kichigidan kattasiga qarab to'g'ri ketma-ketlikda yozing: `MB`, `Bit`, `TB`, `Bayt`, `GB`, `KB`.
2. $2 \text{ GB}$ hajmdagi fleshkaga $512 \text{ KB}$ hajmdagi matnli kitobchalardan nechta saqlash mumkinligini daftaringizda hisoblab chiqing.
3. Klaviaturadagi `Ctrl+C`, `Ctrl+V`, `Ctrl+X`, `Ctrl+Z`, `F2`, `Win+E` tugmalarining vazifasini yod oling.
Vazifani bajarish vaqti: 20 daqiqa.
