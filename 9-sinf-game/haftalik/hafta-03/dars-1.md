# 7-dars. Photoshop interfeysi va vositalari (3-qism): Qatlamlar bilan amaliy ishlash va assetlar kollaji

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga Photoshop dasturida qatlamlar (Layers) panelining ilg'or imkoniyatlarini (qurshov maskalari — Clipping Masks, Smart Objects, qatlamlarni guruhlash va qulflash) chuqur o'rgatish hamda turli xil tayyor 2D o'yin elementlaridan (qahramon, dushmanlar, platforma, fon va yorug'lik) uyg'un va yaxlit o'yin sahnasi kollajini (Game Scene Collage) yig'ish ko'nikmasini shakllantirish.
- **Kutiladigan natija:** O'quvchilar ko'p qatlamli fayllarni tartibga solishni (guruhlar, rangli yorliqlar) biladi; Smart Object xususiyatini tushunib, assetlarni sifat yo'qotmasdan masshtablay oladi; Clipping Mask yordamida obyekt chegarasidan chiqmagan holda teksturalar ulaydi; yakuniy o'yin sahnasi kollajini to'liq yig'a oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (Tanlash vositalari, Layer Masks, Blending Modes): 10 daqiqa
  - Yangi mavzu: Qatlamlarni tashkil etish, Smart Objects va Clipping Masks: 25 daqiqa
  - Amaliy mashg'ulot: O'yin darajasi (Level Art) kollajini yaratish: 30 daqiqa
  - Amaliyot tahlili va keng tarqalgan xatolar: 10 daqiqa
  - Dars xulosasi va tezkor savol-javob: 5 daqiqa

---

## Mentor konspekti

### 1. Ko'p qatlamli o'yin loyihalarida tartib va arxitektura
Professional 2D o'yin sahnasi (konsept-art yoki daraja foni) o'nlab, ba'zan yuzlab qatlamlardan iborat bo'ladi. Ularni boshqarish uchun quyidagi qoidalar qo'llaniladi:
1. **Nomlash madaniyati:** Har bir qatlam o'z mazmuniga ko'ra nomlanishi shart (`Hero_Idle`, `Platform_Grass_01`, `VFX_Fire_Glow`). Standart `Layer 1`, `Layer 2 copy 3` kabi nomlar qat'iyan taqiqlanadi.
2. **Guruhlash (Groups - `Ctrl + G`):** Qatlamlar mantiqiy papkalarga yig'iladi:
   - `[04_HUD_UI]` — salomatlik paneli, tangalar hisoblagichi, mini-xarita.
   - `[03_Foreground]` — qahramon, dushmanlar, interaktiv qutilar.
   - `[02_Midground]` — platformalar, zamin tayllari, daraxtlar.
   - `[01_Background]` — osmon, bulutlar, uzoq tog'lar silueti.
3. **Qulflash (Locking):** Tasodifiy surilib ketmasligi uchun orqa fon va tayyor platforma qatlamlari `Lock` (qulf) qilinadi.

### 2. Aqlli obyektlar (Smart Objects)
- **Muammo:** Oddiy rastr qatlamni `Ctrl + T` bilan 10% gacha kichraytirib, `Enter` bosilsa, Photoshop piksellarni tashlab yuboradi. Keyin uni qayta 100% ga kattalashtirsangiz, tasvir butunlay loyqa (xira) bo'lib qoladi.
- **Yechim (Smart Object):**
  - Qatlam ustiga o'ng tugma bosilib, `Convert to Smart Object` qilinadi.
  - Smart Object asl yuqori sifatli faylni o'z konteynerida saqlaydi.
  - Uni necha marta kichraytirib-kattalashtirsangiz ham (original o'lcham doirasida) zarracha sifat yo'qolmaydi!
  - Smart Objectga qo'llanilgan filtrlar (Blur, Sharpen) ham `Smart Filters` ga aylanadi va istalgan paytda qayta sozlanadi.

### 3. Qurshov niqobi (Clipping Mask - `Ctrl + Alt + G`)
- **Tushunchasi:** Yuqori qatlamdagi rasm yoki teksturani faqat pastki qatlam shaklining ichidagina ko'rinadigan qilib bog'lash.
- **O'yindagi amaliy qo'llanilishi:**
  - Metall qalqon chizilgan. Uning ustiga zanglagan temir teksturasi qo'yildi.
  - Agar tekstura qatlamida `Create Clipping Mask` bosilsa, zang teksturasi qalqon chegarasidan bir millimetr ham tashqariga chiqmaydi!
  - Qahramon libosiga soya berish yoki o'yin logotipiga yaltirash (shining) effekti qo'shish uchun eng tezkor usul.

### 4. Assetlar kollaji (Game Scene Collage) tayyorlash algoritmi
1. **Canvas yaratish:** 1920x1080 px, 72 DPI, RGB rejimida o'yin kadrini ochish.
2. **Fonni joylash:** Osmon va uzoq manzarani eng pastki qatlamga joylashtirish.
3. **Platformalarni terish:** Zamin bloklari va toshlarni joylashtirib, perspektiva va masshtabni to'g'rilash.
4. **Qahramon va obyektlarni integratsiya qilish:** Qahramon, qurollar va dushmanlarni kompozitsiya markaziga joylash.
5. **Yorug'lik va soyalar (Light & Shadow):**
   - Har bir obyekt ostiga yangi qatlamda `Multiply` rejimi va 0% Hardness cho'tka bilan soya tushirish.
   - Sahna umumiy atmosferasiga mos nur effektlarini `Screen` qatlamida qo'shish.
6. **Umumiy rang korreksiyasi:** Barcha assetlar turli manbalardan olingani sababli, sahnaning eng ustiga `Adjustment Layer` (Color Balance yoki Curves) qo'yilib, barcha elementlar yagona rang muhitiga keltiriladi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Smart Object bilan personajni himoyalash (oson)
O'yin sahnasiga 500x500 pikselli qahramon sprayti joylashtirildi. Dizayner uni uzoq masofada turgan kichik dushmanga aylantirish uchun o'lchamini 50x50 pikselgacha kichraytirdi, ammo keyingi bosqichda uni yana boshliq (Boss) qahramon sifatida 600x600 pikselgacha kattalashtirishi kerak bo'ldi.
Piksellar loyqalanib ketmasligi uchun ushbu operatsiyani Smart Object yordamida qanday to'g'ri bajarish kerak?

**Yechim:**
1. Qahramon qatlamini masshtablashdan oldin qatlam ustiga sichqonchaning o'ng tugmasi bosiladi va `Convert to Smart Object` buyrug'i tanlanadi (qatlam burchagida Smart Object belgisi paydo bo'ladi).
2. `Ctrl + T` bosilib, o'lcham 50x50 pikselga kichraytiriladi.
3. Keyinchalik yana `Ctrl + T` bosilib, o'lcham bemalol 600x600 pikselgacha kattalashtiriladi. Asl ma'lumotlar konteyner ichida saqlangani sababli, oddiy rastrdan farqli o'laroq tasvir o'zining dastlabki tiniqligini to'liq saqlab qoladi.

### 2-topshiriq. Clipping Mask orqali sehrli qalqon yaratish (o'rta)
O'yin qahramonining dumaloq shakldagi qalqon qatlami (Shield) mavjud. Qalqon ustiga kosmik yulduzlar galaktikasi teksturasini va chetidan yaltirab o'tuvchi yorug'lik nurini qalqon doirasidan tashqariga chiqarmasdan qanday joylashtirish mumkin?

**Yechim:**
1. Qalqon qatlami (Layer: `Shield`) pastda turadi.
2. Uning ustiga yangi qatlamda kosmik galaktika teksturasi rasmi joylashtiriladi (Layer: `Galaxy_Texture`).
3. `Galaxy_Texture` qatlami ustiga sichqonchaning o'ng tugmasi bosilib, `Create Clipping Mask` (yoki klaviaturada `Ctrl + Alt + G`) bosiladi. Natijada tekstura qalqonning dumaloq chegarasi bilan cheklanadi.
4. Uning ustidan yana bitta bo'sh qatlam ochiladi va unga ham Clipping Mask beriladi. Oq yumshoq mo'yqalam bilan nur chizilib, rejimi `Screen` yoki `Overlay` ga o'tkaziladi.

### 3-topshiriq. 4 xil assetdan 2D o'yin sahnasi kollajini yig'ish (qiyin)
Sizda 4 ta alohida asset mavjud:
- 1) Qorong'i g'or foni;
- 2) Toshli zamin platformasi;
- 3) Sehrgar qahramon;
- 4) Sehrli ko'k kristall.
Ushbu elementlardan foydalanib, qahramon kristallga yaqinlashganda uning yuzi va zamin ko'k nur bilan yorishadigan yaxlit kollaj yaratish bosqichlarini tasvirlang.

**Yechim:**
1. **Kompozitsiya:** 1920x1080 xolstda pastki qatlamga `G'or foni`, o'rtaga `Toshli zamin`, zamin ustiga `Sehrgar`, zaminning o'ng tomoniga esa `Sehrli ko'k kristall` joylashtiriladi.
2. **Kontakt soyalari:** Qahramon va kristall ostiga yangi qatlam ochiladi, rejimi `Multiply` qilinadi va to'q binafsha/qora yumshoq cho'tka bilan yerga tegib turgan nuqtalarga qattiqroq, atrofga tarqaluvchi mayin soya chiziladi.
3. **Kristall nuri:** Kristall ustiga yangi qatlam ochilib, rejimi `Screen` yoki `Linear Dodge (Add)` ga o'tkaziladi. Moviy-ko'k yumshoq cho'tka bilan kristall ustiga nur uriladi.
4. **Qahramonga nur tushirish:** Sehrgar qatlamining ustiga yangi qatlam ochilib, qahramonga `Clipping Mask` qilinadi. Uning rejimi `Color Dodge` qilinadi va qahramonning kristallga qaragan o'ng tomoniga ko'k tusli nur akslari beriladi.
5. **Umumiy uyg'unlashtirish:** Barcha qatlamlarning eng yuqorisiga `Adjustment Layer -> Color Lookup` yoki `Curves` qo'shilib, butun sahnaning rangi yagona sovuq-mistik atmosferaga keltiriladi.

---

## Tezkor nazorat savollari

1. Nima uchun qatlamni `Convert to Smart Object` ga aylantirish masshtablashda sifatni saqlaydi?
   - *Javob:* Chunki Smart Object asl fayl ma'lumotlarini o'zgarishsiz alohida ichki konteynerda saqlaydi, masshtablashda esa piksellar tashlab yuborilmaydi.
2. Clipping Mask yaratishning tezkor klaviatura kombinatsiyasi qaysi?
   - *Javob:* `Ctrl + Alt + G` (Mac'da `Cmd + Option + G`) yoki qatlamlar oralig'iga `Alt` tugmasini bosib sichqoncha bilan bosish.
3. Bir nechta tanlangan qatlamlarni bitta guruh papkasiga jamlash qaysi tugma bilan bajariladi?
   - *Javob:* `Ctrl + G` (Mac'da `Cmd + G`).
4. Qatlamlar ustiga umumiy rang berish va barcha assetlarni bitta atmosferaga keltirish uchun qaysi vosita ishlatiladi?
   - *Javob:* Sozlash qatlamlari (Adjustment Layers: Curves, Color Balance, Hue/Saturation).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Tartibsiz qatlamlar:** O'quvchilar qatlamlarni nomlamasdan `Layer 1`, `Layer 2` ko'rinishida 50 ta qatlam yig'ib yuborishadi. Oqibatda qaysi detal qayerdaligini topish imkonsiz bo'ladi. Har doim mantiqiy papkalarga ajratish (`Ctrl + G`) va nom berish shart.
- **Soya berishni unutish:** Assetlar shunchaki fon ustiga tashlanganda havoda muallaq turgandek ko'rinadi (yomon kollaj). Obyekt zaminga "o'tirishi" uchun uning ostiga doimo kontakt soyasi (Contact Shadow) chizilishi shart.
- **Turli rang harorati (Disparate Lighting):** Bir manbadan olingan qahramon issiq quyosh nurida, fon esa sovuq tunda bo'lsa, kollaj sun'iy ko'rinadi. Adjustment Layers va Clipping Mask orqali barcha qatlamlar bitta rang haroratiga keltirilishi kerak.
