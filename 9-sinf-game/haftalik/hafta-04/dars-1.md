# 10-dars. Ranglar nazariyasi va dizayn asoslari (3-qism): O'yin atmosferasiga mos rang palitrasi yaratish

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga 8–9-darslarda o'rganilgan rang nazariyasini (rang g'ildiragi, uyg'unlik sxemalari, 60-30-10, Color Picker, Swatches) yagona amaliy jarayonga — o'yin atmosferasiga mos **rang palitrasini** bosqichma-bosqich yaratishga birlashtirishni o'rgatish: kayfiyat taxtasi (mood board), asosiy rang, uyg'unlik, yorug'lik darajasi (value) va kulrang test, soyalarda tus siljitish (hue shifting), to'yinganlik ierarxiyasi, cheklangan palitralar va rang kodlash.
- **Kutiladigan natija:** O'quvchilar tanlangan janr va lokatsiya uchun 5–8 rangdan iborat palitra tuzadi; uni Photoshop Swatches panelida guruh qilib saqlaydi va `.aco` faylga eksport qiladi; palitrani kulrang test orqali tekshiradi; qahramon, dushman va bonus obyektlari fondan ajralib turishini asoslab beradi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (HSB, Swatches, Gradient): 10 daqiqa
  - Yangi mavzu: Palitra nima va uni yaratishning 6 bosqichi: 20 daqiqa
  - Value, hue shifting, to'yinganlik ierarxiyasi: 15 daqiqa
  - Janrlar palitralari, cheklangan palitralar, rang kodlash: 10 daqiqa
  - Amaliy ish: lokatsiya palitrasini yaratish va kulrang test: 20 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv dasturi — «Ranglar nazariyasi va dizayn asoslari» moduli (3 soat), kutilgan natija: «Atmosfera va dizayn — fon rasmlari, rang palitrasi orqali kayfiyat yaratishni biladi»; o'quv qo'llanma — Color Picker, Swatches, «chegaralangan ranglar palitrasi uyg'un tasvir yaratish uchun ishlatiladi», «rassomlar o'yin olamining kayfiyati va muhitini ... ranglar palitrasi va soyalardan foydalanadilar». Hue shifting va kulrang test — sohadagi umumqabul qilingan amaliy usullar.

---

## Mentor konspekti

### 1. Rang palitrasi nima?

**Rang palitrasi** — o'yin (yoki uning bitta lokatsiyasi) uchun oldindan tanlangan, cheklangan va o'zaro uyg'un ranglar to'plami. Rassom sahnadagi barcha obyektlarni faqat shu ranglar (va ularning och/to'q variantlari) bilan bo'yaydi.

Nega kerak:
- **Yaxlit uslub** — barcha spraytlar, fon va UI bitta o'yinga tegishli ko'rinadi.
- **Atmosfera** — ranglar o'yinchida kayfiyat uyg'otadi (qo'rquv, quvonch, sir).
- **O'qiluvchanlik** — o'yinchi muhim obyektlarni (qahramon, dushman, bonus) bir qarashda ajratadi.
- **Tezlik** — jamoa bir xil ranglardan foydalanadi, har safar rang «o'ylab topilmaydi».

### 2. Palitra yaratishning 6 bosqichi

1. **Kayfiyatni aniqlash.** Bitta jumlada yozing: «Sirli, biroz xavfli, kechki sehrli o'rmon».
2. **Mood board (kayfiyat taxtasi).** 5–8 ta namunaviy rasm (tabiat fotosuratlari, kinokadrlar, o'yin skrinshotlari) Photoshop'da bitta xolstga yig'iladi.
3. **Asosiy rang (key color).** Kayfiyatni eng yaxshi ifodalovchi bitta rang; Eyedropper (I) bilan mood board'dan olinadi.
4. **Uyg'unlik sxemasi.** 8-darsdagi sxemalardan biri asosida qo'shimcha ranglar: analog (tinch), komplementar (keskin kontrast), triadik (yorqin, o'yinchoq).
5. **Value pog'onalari.** Har bir rangning 2–3 ta yorug'lik darajasi: soya — asosiy — yorug'lik.
6. **Saqlash va test.** Swatches guruhi, `.aco` eksport, kulrang test va sinov sahnasi.

### 3. Value (yorug'lik darajasi) va kulrang test

**Value** — rangning qanchalik och yoki to'q ekanligi. O'yinchi obyektlarni avval **rang tusi bilan emas, yorug'lik farqi bilan** ajratadi.

**Kulrang test:** sahna tepasiga `Black & White` adjustment layer qo'yiladi (yoki nusxada `Image → Mode → Grayscale`).
- Qahramon fondan kulrangda ham aniq ajralib tursa — palitra yaxshi.
- Hammasi bir xil kulrang dog'ga aylansa — value kontrasti yetarli emas: qahramonni ochroq yoki fonni to'qroq qiling.

Qoida: **fon — o'rta va past kontrastli**, **o'yin obyektlari — yuqori kontrastli**.

### 4. Hue shifting — soyalarda tus siljitish

Boshlovchi xatosi: soya uchun asosiy rangga qora qo'shish → «kir», jonsiz rang.

Professional usul: to'qlashganda tusni (Hue) **sovuq tomonga** (ko'k/binafsha), ochlashganda **issiq tomonga** (sariq/olovrang) bir oz siljitish.

| Pog'ona | Hue | Saturation | Brightness |
|---|---|---|---|
| Yorug'lik | 70° (sariqqa yaqin) | 45% | 90% |
| Asosiy yashil | 100° | 60% | 65% |
| Soya | 140° (ko'k-yashilga) | 65% | 35% |

Natija — tabiiy va boy ko'rinadigan barg. Color Picker'ning HSB maydonlarida sozlanadi.

### 5. To'yinganlik ierarxiyasi

- **Fon** — past to'yinganlik, uzoqlashgan sari ko'k-kulrangga yaqinlashadi (havo perspektivasi).
- **O'yin obyektlari** (platforma, eshik) — o'rtacha to'yinganlik.
- **Eng muhim narsalar** (qahramon, bonus, xavf) — eng yuqori to'yinganlik va kontrast.

Bu 9-darsdagi vizual ierarxiya tamoyilining rangdagi ifodasi.

### 6. Janr va lokatsiya palitralari

| Lokatsiya | Kayfiyat | Palitra yo'nalishi |
|---|---|---|
| Sehrli o'rmon | sir, mo'jiza | to'q yashil, ko'k-binafsha + moviy/oltin «sehr» aksentlari |
| Muz g'ori | sovuqlik, yolg'izlik | oq, och moviy, ko'k; aksent — issiq olovrang (mash'al) |
| Cho'l | issiqlik, charchoq | qum-sariq, olovrang, terrakota; aksent — firuza (voha) |
| Qorong'i yerto'la (horror) | qo'rquv, taranglik | past value, xira yashil-kulrang; aksent — qon-qizil |
| Kiberpank shahar | texnologiya, tun | to'q ko'k-binafsha fon + neon pushti va moviy |
| Bolalar platformeri | quvonch | yuqori to'yingan triadik: osmon moviy, o't yashil, quyosh sariq |

### 7. Cheklangan palitralar

Ko'p mashhur o'yinlar ataylab kam rang ishlatadi:
- **Game Boy** (1989) — atigi 4 ta yashil tusli daraja;
- **PICO-8** fantaziya konsoli — 16 ta qat'iy rang;
- zamonaviy pikselli o'yinlar — ko'pincha 16–32 rang.

Cheklov uslubni yaxlit qiladi. Tayyor palitralar: **Lospec Palette List** (lospec.com/palette-list), **Adobe Color** (color.adobe.com) — HEX kodlarini olish mumkin.

### 8. Rang kodlash va qulaylik

O'yinchi ma'noni rangdan o'qiydi: qizil — xavf, dushman; yashil — sog'liq; oltin — tanga, mukofot; moviy — mana, sehr, suv. Qoidani butun o'yin davomida **o'zgartirmang**.

Rang ko'rishida farqi bor o'yinchilar (erkaklarning taxminan 8 foizi) uchun faqat rangga tayanmang: shakl, belgi yoki ikonka qo'shing (dushman ustida ham qizil, ham «!» belgisi).

### 9. Photoshop'da palitrani saqlash

1. Mood board hujjatida Eyedropper (I) bilan rangni oling.
2. Swatches panelida **Create new group** → nom: `Sehrli_Orman`.
3. Har bir rang uchun **Create new swatch** (`+`) → nom: `Asosiy_Yashil`, `Soya_Yashil`, `Aksent_Oltin`.
4. Guruhni belgilang → panel menyusi → **Export Selected Swatches...** → `Sehrli_Orman.aco`.
5. Palitra kartasi: xolstda har bir rang kvadrati ostiga HEX kodi yoziladi va PNG qilib jamoaga ulashiladi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Kayfiyatdan palitraga (oson)
«Muz g'ori» lokatsiyasi uchun kayfiyat jumlasini yozing va 5 rangli palitra taklif qiling (HEX bilan), bitta aksent rangni ko'rsating.

**Yechim:**
Kayfiyat: «Sovuq, jim, yolg'iz, lekin go'zal g'or». Palitra (namuna): `#0B1E3A` (eng to'q soya), `#1F4E79` (to'q ko'k devor), `#5FA8D3` (muz), `#DFF3FF` (yorug'lik/qor), aksent `#FF8A3D` (mash'al olovi). Aksent — komplementar issiq rang: o'yinchi ko'zi mash'al va yo'lga tortiladi.

### 2-topshiriq. Hue shifting bilan 3 pog'onali rang (o'rta)
Qizil olma uchun yorug'lik — asosiy — soya pog'onalarini HSB qiymatlari bilan tuzing. Soya qora qo'shib emas, tus siljitib olinsin.

**Yechim (namuna):**
- Yorug'lik: H 15°, S 55%, B 95% (olovrang tomonga);
- Asosiy: H 0°, S 80%, B 80%;
- Soya: H 340°, S 75%, B 45% (binafsha-qizil tomonga).
Tekshirish: uchala kvadrat yonma-yon qo'yilganda soya «kir jigarrang» emas, to'q gilos rangida ko'rinadi.

### 3-topshiriq. Kulrang test (o'rta)
Fon (o'rmon) va qahramon spraytiga palitrangizni qo'llang. `Black & White` adjustment layer bilan sahnani tekshiring. Qahramon ajralib turmasa, nima o'zgartiriladi?

**Yechim:**
1. Layers panelida eng yuqoriga `Black & White` adjustment layer qo'shiladi.
2. Qahramon va fon bir xil kulrangda bo'lsa: qahramon ranglarining Brightness qiymati 15–25% ko'tariladi yoki fon Brightness i tushiriladi; fon to'yinganligi kamaytiriladi.
3. Qayta test: qahramon siluyeti aniq ko'rinsa — bajarildi. Adjustment layer ko'z belgisi bilan o'chiriladi.

### 4-topshiriq. Ikki lokatsiya — bitta o'yin (qiyin)
Bir o'yinning ikki darajasi uchun palitra: «Kunduzgi qishloq» va «Tungi qishloq». Ikkalasida ham qahramon ranglari (3 ta) bir xil qolsin. Swatches da 2 guruh qilib saqlang va `.aco` ga eksport qiling.

**Yechim:**
- Qahramon (o'zgarmas): qizil plash `#D7263D`, teri `#F2C29B`, to'q kontur `#2B1B17`.
- Kunduz: osmon `#8FD3FF`, o't `#6BBF59`, tom `#C8553D`, yo'l `#E9D8A6`, soya `#3B6E57`.
- Tun: osmon `#141B41`, o't `#2C4A52`, tom `#5A2E3A`, yo'l `#6C6F7F`, aksent (deraza nuri) `#FFD166`.
- Guruhlar: `Qishloq_Kun`, `Qishloq_Tun`; har biri alohida `.aco`.
Asosiy fikr: tun palitrasida qahramon qizili yanada kuchli ajralib turadi — tun ranglari past to'yinganlik va past value'da.

---

## Tezkor nazorat savollari

1. Rang palitrasi nima va u o'yinga nima beradi?
   - *Javob:* Oldindan tanlangan cheklangan uyg'un ranglar to'plami; yaxlit uslub, atmosfera va o'qiluvchanlik beradi.
2. Kulrang test nima uchun qilinadi?
   - *Javob:* Obyektlar rangsiz, faqat yorug'lik (value) farqi bilan ham ajralib turishini tekshirish uchun.
3. Hue shifting nima?
   - *Javob:* Soya tomonda tusni sovuqroqqa, yorug'lik tomonda issiqroqqa siljitish (qora/oq qo'shish o'rniga).
4. Fon va qahramonning to'yinganligi qanday bo'lishi kerak?
   - *Javob:* Fon — pastroq to'yinganlik va kontrast, qahramon va muhim obyektlar — yuqori.
5. Photoshop'da palitra qaysi formatda eksport qilinadi?
   - *Javob:* `.aco` (Swatches → Export Selected Swatches).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Juda ko'p rang:** 20–30 ta tasodifiy rang uslubni buzadi. Lokatsiya uchun 5–8 ta asosiy rang yetarli.
- **Soyani qora bilan qilish:** rang «kir» bo'ladi — hue shifting ishlating.
- **Hamma narsa bir xil yorqin:** ko'z qayerga qarashni bilmaydi — faqat muhim obyektlar eng yorqin.
- **Faqat rang bilan ma'no berish:** shakl va belgi ham qo'shing.
- **Palitrani saqlamaslik:** keyingi darslarda ikonka va spraytlar shu palitrada chiziladi — `.aco` faylni saqlang.
