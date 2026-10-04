# 5-dars. Photoshop interfeysi va vositalari (1-qism): 2D grafika turlari va interfeys

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga II bob: 2D grafika asoslari bo'yicha kirish bilimlarini berish, 2D grafikaning o'yindagi asosiy elementlari (spraytlar, tayllar, fonlar, UI elementlari), kompyuter grafikasining 3 ta asosiy turi (Rastr, Vektor, Fraktal) hamda Adobe Photoshop dasturining interfeysi, asosiy panellari (Canvas, Tools, Options Bar, Layers) va ishchi muhit sozlamalarini o'rgatish.
- **Kutiladigan natija:** O'quvchilar rastr va vektor grafikasining farqini amalda ko'ra oladi; o'yinda sprayt va tayl xaritalari (Tilemaps) nima uchun kerakligini tushunadi; Adobe Photoshop interfeysida erkin harakatlanadi va o'yin assetlari uchun to'g'ri o'lchamdagi yangi fayl (Canvas) yarata oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (Ssenariy va GDD): 10 daqiqa
  - Yangi mavzu: 2D grafika elementlari (Sprayt, Tayl, Fon): 20 daqiqa
  - Grafika turlari: Rastr, Vektor va Fraktal: 25 daqiqa
  - Adobe Photoshop interfeysi va amaliy tanishuv: 15 daqiqa
  - Nazorat savollari va dars xulosasi: 10 daqiqa

---

## Mentor konspekti

### 1. 2D grafika va uning o'yindagi asosiy elementlari
2D grafika (ikki o'lchamli) — kenglik (X) va balandlik (Y) o'qlari bo'yicha tekislikda mavjud bo'lgan tasvirlardir.
O'yin ishlab chiqishda 2D grafika 4 ta asosiy guruhga bo'linadi:
1. **Spraytlar (Sprites):** O'yindagi har qanday harakatlanuvchi yoki statik obyektlar tasviri (bosh qahramon, dushmanlar, tangalar, sandiqlar). Ular ko'pincha alohida kadrlar ko'rinishida chizilib, keyinchalik kadrma-kadr animatsiyaga birlashtiriladi.
2. **Tayllar (Tiles) va Tayl xaritalari (Tilemaps):** Katta o'yin darajalarini (xaritalarni) bloklardan mozaika kabi terish uchun ishlatiladigan kichik o'lchamdagi takrorlanuvchi rasmlar (masalan, $32\times32$ yoki $64\times64$ pikselli yer, o't, g'isht, suv bloklari). Ular xotirani bir necha o'n barobar tejaydi.
3. **Fonlar (Backgrounds):** O'yin atmosferasini yaratuvchi orqa fon rasmlari. Ko'pincha 3-4 xil qatlamdan iborat bo'lib, **Parallaks effekti** (yaqin qatlam tez, uzoqdagi tog'lar sekin harakatlanishi) orqali chuqurlik hosil qiladi.
4. **UI elementlari:** Tugmalar, menyu ramkalari, yurakchalar va xarita foni.

### 2. Kompyuter grafikasining 3 ta asosiy turi
1. **Rastr grafikasi (Raster):**
   - Rangli nuqtalar — **piksellar to'ri (Matrix of Pixels)** dan iborat.
   - *Afzalligi:* Yuqori darajadagi fotorealistik sifat, ranglarning mayin o'tishi va murakkab gradiyentlar.
   - *Kamchiligi:* Kattalashtirilganda (zoom) sifat yo'qoladi, piksellar ko'rinib qoladi (pikselizatsiya); fayl hajmi kattaroq bo'ladi.
   - *Formatlar:* PNG (shaffof fonli spraytlar uchun), JPEG (fotosuratlar), PSD (Photoshop manba fayli), WebP.
2. **Vektor grafikasi (Vector):**
   - Piksellar emas, balki matematik formulalar va geometrik primitivlar (nuqtalar, to'g'ri va egri chiziqlar, ko'pburchaklar) asosida quriladi.
   - *Afzalligi:* Sifatni mutlaqo yo'qotmasdan istalgancha kattalashtirish (cheksiz masshtablash); fayl hajmi juda kichik.
   - *Kamchiligi:* Fotosurat sifatidagi murakkab rang o'tishlarini yaratish qiyin.
   - *Formatlar:* SVG, AI, EPS. O'yinda logotiplar, piktogrammalar va shriftlar uchun ishlatiladi.
3. **Fraktal grafikasi (Fractal):**
   - Matematik o'z-o'ziga o'xshashlik (self-similarity) formulalari asosida quriladi.
   - Tabiiy obyektlarni (bulutlar, olov, qor parchalari, tog' tizmalari) procedural generatsiya qilishda qo'llaniladi.

### 3. Adobe Photoshop interfeysi arxitekturasi
Photoshop — bu butun dunyo bo'yicha 2D o'yin san'ati va to'qimalarini yaratishda eng keng tarqalgan professional rastr muharriri.
Interfeys 5 ta asosiy zonadan iborat:
1. **Canvas (Ishchi xolst):** Tasvir chiziladigan markaziy maydon. O'yin uchun odatda $1920\times1080$ (Full HD) yoki pikselli o'yinlar uchun kichik o'lchamlarda ochiladi (Resolution: 72 DPI ekranga, 300 DPI esa chop etishga).
2. **Tools Panel (Vositalar paneli — chapda):** Chizish, kesish, bo'yash va tanlash uskunalari (Move V, Brush B, Eraser E va h.k.).
3. **Options Bar (Xususiyatlar paneli — tepada):** Tanlangan uskunaning maxsus parametrlarini (o'lchami, shaffofligi, qattiqligi) sozlaydi.
4. **Layers Panel (Qatlamlar paneli — o'ngda):** Photoshopning eng muhim yuragi. Har bir personaj, fon yoki detal alohida qatlamda (Layer) turadi.
5. **Menu Bar (Asosiy menyu — eng tepada):** File, Edit, Image, Layer, Filter kabi global amallar.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Rastr va vektor farqini amalda aniqlash (oson)
Smartfon o'yinining ekrandagi salomatlik yurakchasi ikonkasi va o'yindagi o'rmon foni rasmi berilgan.
Qaysi biri vektor, qaysi biri rastr formatida bo'lishi maqsadga muvofiq va nima uchun?

**Yechim:**
- **Salomatlik yurakchasi (UI ikonka) $\to$ Vektor (SVG).** Sababi: Turli o'lchamdagi ekranlarda (kichik telefon yoki katta planshet) sifati zarracha buzilmasdan aniq ko'rinishi kerak, fayl hajmi esa bir necha kilobayt bo'ladi.
- **O'rmon foni $\to$ Rastr (PNG/JPEG/PSD).** Sababi: O'rmonda millionlab rang tuslari, soyalar va mayin gradiyentlar mavjud bo'lib, buni faqat piksellar to'ri orqali ifodalash mumkin.

### 2-topshiriq. O'yin xaritasi uchun Tayl (Tile) hisob-kitobi (o'rta)
O'yin ekrani o'lchami $1920\times1080$ piksel. O'yin darajasi esa $32\times32$ pikselli standart kvadrat tayllardan tuzilishi kerak.
Ekranni to'liq qoplash uchun eniga va bo'yiga nechtadan tayl kerak bo'ladi? Tayllardan foydalanish bitta yaxlit ulkan rasmdan ko'ra qanday texnik ustunlik beradi?

**Yechim:**
1. Eniga tayllar soni: $1920 / 32 = 60$ ta tayl;
2. Bo'yiga tayllar soni: $1080 / 32 = 33.75 \approx 34$ ta tayl;
3. Jami ekranda: $60 \times 34 = 2040$ ta tayl katakchasi mavjud.
*Texnik ustunlik:* 2040 ta tayl uchun alohida 2040 ta rasm chizilmaydi! Bor-yo'g'i 5-10 ta unikal blok (o't, tosh, tuproq) chiziladi va o'yin xotirasida (RAM) bir necha megabayt joy tejab qolinadi.

### 3-topshiriq. Photoshopda o'yin loyihasi uchun to'g'ri Canvas ochish (qiyin)
Android smartfonlar uchun 2D o'yin bosh menyusi dizaynini boshlamoqchisiz.
Photoshop dasturida yangi fayl ochish (`Ctrl + N`) oynasida quyidagi parametrlarni qanday sozlashingiz kerakligini asoslang:
1. Width va Height (Kenglik va bo'ylik);
2. Resolution (Ajratish qobiliyati);
3. Color Mode (Rang modeli);
4. Background Contents.

**Yechim:**
1. **Width & Height:** `1920 x 1080 Pixels` (Landscape/Gorizontal) yoki `1080 x 1920 Pixels` (Portrait/Vertikal) — zamonaviy smartfonlarning eng keng tarqalgan Full HD standarti.
2. **Resolution:** `72 Pixels/Inch` (yoki 150 PPI). Sababi: Ekranda ko'rsatiladigan raqamli grafika uchun 72 DPI yetarli, ortiqcha 300 DPI qilish faqat fayl hajmini asossiz oshiradi.
3. **Color Mode:** `RGB Color, 8 bit`. Sababi: Barcha elektron displeylar (ekranlar) qizil, yashil, ko'k nurlar yig'indisi (RGB) asosida ishlaydi (CMYK faqat bosmaxonaga kerak).
4. **Background Contents:** `Transparent` (Shaffof). Sababi: Keyinchalik o'yin dvijogiga o'tkazilganda ortiqcha oq fon xalaqit bermasligi lozim.

---

## Tezkor nazorat savollari

1. 2D o'yinlarda harakatlanuvchi personajlar va buyumlar rasmlari qanday ataladi?
   - *Javob:* Spraytlar (Sprites).
2. Rastr grafikasining asosiy kamchiligi nima?
   - *Javob:* Tasvir kattalashtirilganda uning sifati yo'qolishi va piksellashib qolishi.
3. Shaffof fonni qo'llab-quvvatlaydigan asosiy rastr formati qaysi?
   - *Javob:* PNG (va PSD).
4. Photoshopda har bir ob'ektni alohida tahrirlash imkonini beruvchi eng muhim panel qaysi?
   - *Javob:* Qatlamlar (Layers) paneli.

---

## Uyga vazifa

Daftaringizda:
1. Rastr va vektor grafikasi solishtirilgan taqqoslash jadvalini chizing (Tuzilishi, afzalligi, kamchiligi, o'yindagi o'rni va formatlari);
2. 2D o'yin uchun 3 qatlamli parallaks fon (Background) g'oyasini tasvirlang: 1-oldingi qatlamda nima, 2-o'rta qatlamda nima, 3-uzoq orqa qatlamda nima joylashishini yozing.
