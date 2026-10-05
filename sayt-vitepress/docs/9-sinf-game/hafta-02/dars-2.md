---
title: "5-dars. Photoshop interfeysi va vositalari (1-qism): 2D grafika turlari va interfeys"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Game)", "link": "/9-sinf-game/"}, "week": {"n": 2, "link": "/9-sinf-game/hafta-02/"}, "g": 5, "title": "Photoshop interfeysi va vositalari (1-qism): 2D grafika turlari va interfeys", "lead": "2D o'yin san'ati — bu har bir piksel va chiziq orqali virtual dunyoni jonlantirish, o'yinchiga estetik zavq va unutilmas vizual muhit ulashish mahoratidir!", "slide": "/slaydlar/9-sinf-game/hafta-02/dars-2.html", "test": "/slaydlar/9-sinf-game/hafta-02/dars-2-test.html", "tabs": [{"g": 4, "link": "/9-sinf-game/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/9-sinf-game/hafta-02/dars-2", "current": true}, {"g": 6, "link": "/9-sinf-game/hafta-02/dars-3", "current": false}], "prev": {"g": 4, "title": "O‘yin loyihalash va ssenariy: G'oyadan voqealar zanjirigacha", "link": "/9-sinf-game/hafta-02/dars-1"}, "next": {"g": 6, "title": "Photoshop interfeysi va vositalari (2-qism): Tanlash vositalari, qatlamlar va uskunalar", "link": "/9-sinf-game/hafta-02/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **2D grafika (ikki o'lchamli)** — kenglik (X) va balandlik (Y) o'qlari bo'yicha tekislikda joylashgan tasvirlar tizimidir.
- **O'yindagi 2D grafika elementlari:**
  1. **Spraytlar (Sprites):** Harakatlanuvchi qahramonlar, dushmanlar, qurollar va yig'iladigan tangalar tasviri.
  2. **Tayllar (Tiles):** Xaritalar va bosqichlarni bloklardan mozaika kabi terish uchun xizmat qiluvchi kichik takrorlanuvchi kvadrat rasmlar ($32\times32$, $64\times64$ px).
  3. **Fonlar (Backgrounds):** O'yin atmosferasini yaratuvchi manzaralar. Bir nechta qatlamdan tuzilib, **Parallaks effekti** orqali chuqurlik hosil qiladi.
  4. **UI elementlari:** Menyu, sog'lik paneli va tugmalar.
- **Kompyuter grafikasining 3 turi:**
  - **Rastr grafikasi:** Piksellar to'ridan iborat. Yuqori fotorealistik sifat va mayin gradiyentlarga ega, ammo kattalashtirilganda sifati yo'qoladi (PNG, JPEG, PSD).
  - **Vektor grafikasi:** Matematik formulalar va geometrik chiziqlardan iborat. Har qanday hajmga cheksiz kattalashtirilsa ham sifatini 100% saqlaydi (SVG, AI).
  - **Fraktal grafikasi:** Matematik o'z-o'ziga o'xshashlik algoritmlari orqali bulutlar, tog'lar, olov kabi tabiiy murakkab shakllarni hosil qiladi.
- **Adobe Photoshop** — 2D o'yin grafikasini yaratish va tahrirlashda dunyodagi eng yetakchi rastr muharriri.
- **Photoshop interfeysi asosiy qismlari:**
  - *Canvas (Xolst):* Markaziy rasm chizish maydoni.
  - *Tools Panel (Chapda):* Barcha asboblar (Move, Brush, Eraser, Pen).
  - *Options Bar (Tepada):* Tanlangan uskunaning joriy sozlamalari.
  - *Layers Panel (O'ngda):* Qatlamlar ierarxiyasi.
  - *Menu Bar (Yuqorida):* Faylni ochish, saqlash va filtrlar.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Parallaks effekti qanday ishlaydi?
Haqiqiy hayotda poezdda ketayotganingizda, deraza yonidagi simyog'ochlar ko'z o'ngingizdan chaqmoqdek o'tib ketadi, uzoqdagi tog'lar esa deyarli joyidan qimirlamay turgandek tuyuladi.
2D o'yinlarda ham xuddi shu qonuniyat ishlatiladi:
- **1-qatlam (Foreground):** O'yinchiga eng yaqin o't-o'lanlar juda tez siljiydi;
- **2-qatlam (Gameplay layer):** Qahramon yuguradigan asosiy platformalar o'rtacha tezlikda harakatlanadi;
- **3-qatlam (Midground):** O'rta masofadagi daraxtlar sekinroq siljiydi;
- **4-qatlam (Far Background):** Uzoqdagi osmon va tog'lar deyarli qimirlamaydi.
Natijada 2D tekis ekranda aql bovar qilmas 3D chuqurlik illyuziyasi paydo bo'ladi!

### 2. Rastr va Vektor mikroskop ostida
- Rastr rasmni kattalashtirsangiz, u kvadrat rangli katakchalarga (piksellarga) ajralib ketadi.
- Vektor rasm esa formuladir ($x^2 + y^2 = r^2$). Kompyuter uni qancha kattalashtirsangiz ham, har safar qaytadan hisoblab chizadi va chiziqlar har doim o'ta silliq va o'tkir bo'lib qoladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **2D Grafika** | Faqat eni va bo'yiga ega bo'lgan ikki o'lchamli tekis raqamli tasvir. |
| **Rastr (Raster)** | Rangli piksellar to'plami (mozaikasi) orqali shakllanuvchi tasvir turi. |
| **Vektor (Vector)** | Matematik formulalar va geometrik nuqtalardan tashkil topgan masshtablanuvchi tasvir. |
| **Fraktal (Fractal)** | Matematik formulalar orqali o'z-o'zini takrorlovchi tabiiy naqshlar grafikasi. |
| **Sprite (Sprayt)** | O'yindagi harakatlanuvchi personaj yoki obyektning ikki o'lchamli 2D tasviri. |
| **Tile (Tayl)** | O'yin xaritasini yig'ish uchun ishlatiladigan kichik kvadrat blok (g'isht, o't, suv). |
| **Tilemap** | Tayllardan tuzilgan butun boshli o'yin bosqichi yoki darajasi xaritasi. |
| **Parallaks** | Turli qatlamlarning turlicha tezlikda harakatlanishi orqali hosil bo'ladigan chuqurlik effekti. |
| **Canvas (Xolst)** | Photoshopda yangi rasm yoki o'yin loyihasi chiziladigan ishchi maydon. |
| **DPI / PPI** | Bir dyuymdagi nuqtalar yoki piksellar soni (tasvir aniqligi). |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- **Piksel (Pixel)** so'zi inglizcha *"Picture Element"* (Tasvir elementi) so'zlarining qisqartmasidan kelib chiqqan bo'lib, ilk bor 1965-yilda kosmik suratlarni tahlil qilishda ishlatilgan.
- Adobe Photoshop dasturining ilk versiyasi 1987-yilda aka-uka **Tomas va Jon Knoll** tomonidan yaratilgan bo'lib, dastlab u Macintosh ekranlarida oq-qora suratlarni ko'rsatish uchun *"Display"* nomi ostida yozilgan edi.
- Parallaks texnologiyasi dastlab 1930-yillarda Uolt Disney tomonidan ixtiro qilingan ulkan **Multiplane Camera** (Ko'p qatlamli kamera) qurilmasi orqali multfilmlarga chuqurlik berish uchun qo'llanilgan.
- Zamonaviy smartfonlar ekranida 1 dyuym joyda 400 dan ortiq piksel joylashgan bo'lib, inson ko'zi ularni alohida ajrata olmaydi — ular yagona silliq rasmga aylanadi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Rastr va Vektor solishtiruvi <Badge type="tip" text="oson" />
Nima uchun o'yin logotipini chizishda Photoshop (rastr) emas, vektorli muharrir (masalan Illustrator) afzal ko'riladi?
**Kutiladigan natija:** Logotip kichik telefonda ham, ulkan ko'cha bannerida ham sifati buzilmasdan ishlatilishi lozimligi haqida javob.

### 2. Sprayt nima? <Badge type="tip" text="oson" />
O'yindagi harakatlanuvchi bosh qahramonning turishi, yugurishi va sakrashi nima uchun alohida spraytlar to'plami deb ataladi?
**Kutiladigan natija:** Har bir harakat alohida kadr ko'rinishida chizilgan 2D tasvirlar ekani bayoni.

### 3. Tayl xaritasining foydasi <Badge type="tip" text="oson" />
Nima uchun o'yin darajasini $10 000 \times 10 000$ pikselli bitta ulkan rasm qilib chizmasdan, $32\times32$ pikselli tayllardan terishadi?
**Kutiladigan natija:** Xotirani (RAM) tejash va darajalarni tez tahrirlash imkoniyati.

### 4. Parallaks qatlamlarini tartiblash <Badge type="warning" text="o'rta" />
O'rmon manzarasi uchun 3 ta qatlam berilgan:
- Qatlam A: Moviy osmon va bulutlar;
- Qatlam B: Yaqindagi daraxtlar va qahramon platformasi;
- Qatlam C: Uzoqdagi ko'kargan tog'lar.
Qahramon yugurganda ushbu qatlamlar harakat tezligini eng tezzdan eng sekingacha tartiblang.
**Kutiladigan natija:** Qatlam B (eng tez) $\to$ Qatlam C (o'rtacha) $\to$ Qatlam A (deyarli qimirlamaydi).

### 5. Fraktal grafikaga hayotiy misol <Badge type="warning" text="o'rta" />
Kompyuter o'yinlarida qaysi tabiiy obyektlarni chizishda fraktal grafikadan keng foydalaniladi? 3 ta misol keltiring.
**Kutiladigan natija:** Bulutlar, tog' tizmalari, daraxt shoxlari yoki qor parchalari.

### 6. Photoshopda yangi fayl ochish sozlamalari <Badge type="warning" text="o'rta" />
Kompyuter o'yini foni uchun yangi fayl ochmoqchisiz. Kenglik, balandlik, Resolution va Color Mode parametrlariga qanday qiymatlar kiritasiz?
**Kutiladigan natija:** $1920\times1080$ px, 72 DPI, RGB Color, 8 bit.

### 7. Formatlar tanlovi (PNG vs JPEG) <Badge type="warning" text="o'rta" />
O'yin qahramonining atrofidagi oq fon ko'rinmasligi (shaffof bo'lishi) uchun qaysi formatda eksport qilish shart va nima uchun JPEG bu vazifaga yaramaydi?
**Kutiladigan natija:** PNG shaffoflik (Alpha channel)ni saqlaydi, JPEG esa shaffoflikni qo'llab-quvvatlamaydi va oq rangga aylantirib qo'yadi.

### 8. Qatlamlar (Layers) ierarxiyasi tahlili <Badge type="danger" text="qiyin" />
Photoshopda 3 ta qatlam bor: 1-qatlamda "Osmon", 2-qatlamda "Qahramon", 3-qatlamda "Daraxt". Agar "Osmon" qatlami eng tepaga ko'tarilsa ekranda nima yuz beradi? Qatlamlar tartibi qoidasini tushuntiring.
**Kutiladigan natija:** Osmon barcha qatlamlarni to'sib qo'yadi; qoida — ustki qatlamlar pastki qatlamlarning ustiga chiziladi.

### 9. Pikselli o'yin (Pixel Art) o'lchamlari <Badge type="danger" text="qiyin" />
Retro uslubdagi pikselli o'yin uchun qahramon sprayti odatda $16\times16$ yoki $32\times32$ pikselda chiziladi. Nima uchun bunday kichik rasm zamonaviy 4K monitorlarda ham chiroyli ko'rinadi?
**Kutiladigan natija:** Piksellar "Nearest Neighbor" usulida kattalashtirilganda ularning qirralari o'tkir kvadrat bo'lib saqlanadi va maxsus retro estetika hosil qiladi.

### 10. O'yin sahna arxitekturasini loyihalash <Badge type="info" text="bonus" />
2D platformer o'yini uchun to'liq sahna qatlamlari ro'yxatini tuzing:
- Qaysi qatlamda nima joylashadi (kamida 5 ta qatlam: Fon, Uzoq obyektlar, Asosiy o'yin maydoni, Oldingi bezaklar, UI HUD);
- Qaysi obyektlar qahramonni to'sadi va qaysilari qahramonning orqasida qoladi.
**Kutiladigan natija:** To'liq 5 qatlamli 2D o'yin sahnasi arxitekturasi bayoni.

</div>

