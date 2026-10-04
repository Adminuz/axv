# 4-dars. Kompyuterning asosiy va qo'shimcha qurilmalari

> Tizim bloki, monitor va klaviatura kompyuterning faqat «skeleti» xolos. Unga ulangan o'nlab qo'shimcha qurilmalar — printerlar, skanerlar, proyektorlar va drayverlar kompyuterni haqiqiy mo'jizaviy studiyaga aylantiradi. Ushbu darsda kompyuterning barcha a'zolari va ularni xavfsiz ulash sirlarini o'rganamiz.

## Dars xulosasi

- **Asosiy qurilmalar** — kompyuter ishlashi uchun zarur bo'lgan minimal to'plam: Tizim bloki (System Unit), Monitor, Klaviatura va Sichqoncha.
- **Qo'shimcha (periferiya) qurilmalar** — kompyuter imkoniyatini oshiruvchi tashqi qurilmalar: printer, skaner, veb-kamera, proyektor, naushnik va tashqi xotiralar.
- **Kiritish qurilmalari:** klaviatura, sichqoncha, mikrofon, skaner, veb-kamera, grafik planshet.
- **Chiqarish qurilmalari:** monitor, printer, proyektor, dinamiklar (kolonka), naushniklar.
- **Zamonaviy portlar:** USB (Type-A, Type-C), HDMI, DisplayPort, Ethernet (RJ-45), 3.5 mm Audio Jack.
- **Drayver (Driver)** — yangi ulangan qurilmani operatsion tizim to'g'ri boshqarishi uchun xizmat qiluvchi mikrodastur.
- **Xavfsiz foydalanish:** Fleshka va disklarni sug'urishdan oldin doimo «Safely Remove Hardware» (Xavfsiz ajratish) buyrug'ini berish lozim.

---

## Qo'shimcha ma'lumot

### Periferiya qurilmalari: inson va kompyuter suhbati
Kompyuter faqat ichki signallar bilan o'zi uchun yashay olmaydi. U tashqi dunyo bilan aloqa qilishi kerak:
- **Kiritish (Input):** Biz klaviaturada tugma bosganimizda yoki mikrofonga gapirganimizda inson tushunadigan axborot (harf, tovush) elektr signallariga aylanadi va kompyuterga kiradi.
- **Chiqarish (Output):** Kompyuter hisob-kitob qilib bo'lgach, natijani monitor ekranida piksellar bilan yoki printerda qog'ozdagi siyoh orqali insonga tushunarli ko'rinishda qaytaradi.
Shunday qilib, kiritish va chiqarish qurilmalari kompyuter va inson o'rtasidagi ikki tomonlama ko'prikdir.

### Printerlar: Lazerli va Purkagichli (Inkjet) farqi
Bugungi kunda eng ko'p ishlatiladigan printerlar ikkita katta guruhga bo'linadi:
1. **Lazerli printer (Laser printer):** Chop etish uchun suyuq siyoh emas, balki quruq kukun — **toner** ishlatadi. Lazer nuri baraban ustida tasvir chizadi va qog'oz qizdirilib, kukun qog'ozga yopishtiriladi. Juda tez ishlaydi, matnli hujjatlar va kitoblar uchun eng maqbul tanlov.
2. **Purkagichli printer (Inkjet printer):** Mikroskopik teshikchalardan (soplo) suyuq siyoh tomchilarini qog'ozga purkaydi. Rangli fotosuratlar va yorqin grafikalarni juda aniq chop etadi, ammo siyohi tez tugashi va uzoq vaqt ishlatilmasa qurib qolishi mumkin.

### Nega ba'zan qurilma ulanganda ishlamaydi?
Yangi sotib olingan professional veb-kamera yoki geymerlar sichqonchasini USB ga ulaganingizda kompyuter uni tanimasligi yoki tugmalari ishlamasligi mumkin.
Buning sababi — **drayver (driver)** yo'qligidir. Operatsion tizim har bir dunyoda mavjud bo'lgan millionlab qurilmaning qanday ishlashini oldindan bila olmaydi. Ishlab chiqaruvchi qurilma bilan birga maxsus «yo'riqnoma dastur» — drayver yozadi. Siz drayverni o'rnatganingizda operatsion tizim ushbu qurilmaning barcha funksiyalarini boshqara boshlaydi.

### Odatiy xato: Fleshkani to'satdan sug'urib olish
Ko'pchilik o'quvchilar fleshkaga darslik yoki fayl nusxalab bo'lgach, uni to'g'ridan-to'g'ri tortib sug'urib olishadi.
Nima uchun bu xavfli? Windows ma'lumotlarni tezroq yozish uchun ularni bir zumga **kesh xotirada** (RAM) ushlab turadi. Ekranda yuklash tugagandek ko'rinsa-da, qattiq disk yoki fleshka kontrolleri ma'lumotni oxirigacha joylashtirib ulgurmagan bo'lishi mumkin. To'satdan uzilsa, fayl chala yoziladi va fleshkadagi ma'lumotlar shikastlanadi. Shu sababli vazifalar panelidan «Eject» qilish qat'iy odat bo'lishi shart!

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Asosiy qurilmalar** | Kompyuterning ishlashi uchun shart bo'lgan minimal to'plam (tizim bloki, monitor, klaviatura, sichqoncha). |
| **Periferiya qurilmalari** | Kompyuterga qo'shimcha imkoniyat berish uchun tashqi tomondan ulanadigan barcha qurilmalar. |
| **Kiritish qurilmalari (Input)** | Axborotni insoniy shakldan raqamli ko'rinishga o'tkazib kompyuterga uzatuvchi qurilmalar. |
| **Chiqarish qurilmalari (Output)** | Qayta ishlangan raqamli natijani inson qabul qiladigan ko'rinishda (ekran, qog'oz, tovush) taqdim etuvchi qurilmalar. |
| **Drayver (Driver)** | Operatsion tizimga tashqi apparat qurilmasini to'g'ri boshqarishni o'rgatuvchi tizimli dastur. |
| **USB (Universal Serial Bus)** | Zamonaviy periferiya qurilmalarini ulash uchun eng universal yuqori tezlikdagi standart port. |
| **HDMI** | Yuqori aniqlikdagi video tasvir va ko'p kanalli audio tovushni birgalikda uzatuvchi raqamli port. |
| **Device Manager** | Windowsda kompyuterga ulangan barcha qurilmalar va ularning drayverlarini ko'rsatuvchi dispetcher. |

---

## Bilasizmi?

1. Dunyodagi ilk kompyuter sichqonchasi 1964-yilda Duglas Engelbart tomonidan **yog'ochdan** yasalgan bo'lib, uning ichida ikkita metall g'ildirakcha aylangan.
2. Zamonaviy lazerli printerlar daqiqasiga 50 dan 100 betgacha qog'ozni chop eta oladi. Uning ichidagi qizdiruvchi valik (pechka) harorati 200 darajagacha yetadi!
3. USB porti 1996-yilda yettita yirik texnologiya kompaniyasi (Intel, Microsoft, IBM va boshqalar) tomonidan kompyuter orqasidagi o'nlab har xil noqulay simlarni bitta standartga keltirish maqsadida yaratilgan.
4. Bugungi kunda kosmik stansiyalarda va tibbiyotda hatto inson tana a'zolari va murakkab detallarni chop eta oladigan **3D-printerlar** keng qo'llanilmoqda.

---

## Topshiriqlar

### 1. Qurilmalarni 3 guruhga ajratish · oson
Quyidagi 9 ta qurilmani uch ustunga bo'lib yozing: **Kiritish**, **Chiqarish** va **Tashqi saqlash**.
Ro'yxat: Printer, Sichqoncha, Monitor, USB fleshka, Skaner, Dinamiklar, Tashqi qattiq disk, Veb-kamera, Naushnik.
**Kutiladigan natija:** Har bir ustunda 3 tadan qurilma to'g'ri joylashgan jadval.

### 2. Device Manager bilan tanishuv · oson
Klaviaturada `Win + X` tugmalarini bosing va menyudan «Device Manager» darchasini oching. «Display adapters» (Videokarta) va «Keyboards» bo'limlarini ochib, o'z kompyuteringizdagi qurilmalar nomini daftarga yozing.
**Kutiladigan natija:** Videokarta va klaviatura modeli qayd etiladi.

### 3. Monitor portlarini aniqlash · oson
O'z kompyuteringiz yoki noutbukingiz korpusidagi monitor ulash portlarini ko'zdan kechiring. Unda HDMI, DisplayPort yoki VGA portlaridan qaysi biri borligini yozing.
**Kutiladigan natija:** Monitor kabeli qaysi portga ulanganligi aniqlanadi.

### 4. Xavfsiz ajratish mashqi · oson
Fleshkani kompyuterga ulang. So'ngra vazifalar panelining o'ng quyi burchagidagi yashirin belgilar orasidan «Safely Remove Hardware and Eject Media» orqali fleshkani xavfsiz ajrating.
**Kutiladigan natija:** Ekranda «Safe to Remove Hardware» xabari paydo bo'lgach fleshka sug'uriladi.

### 5. Printer turlarini taqqoslash · o'rta
Lazerli printer va Purkagichli (Inkjet) printerning 2 tadan ustunligi va kamchiligini jadval ko'rinishida yozing.
**Kutiladigan natija:** Tezlik, chop etish narxi va ranglar sifati bo'yicha taqqoslovchi jadval.

### 6. USB Type-A va Type-C farqi · o'rta
Zamonaviy noutbuk va smartfonlarda nega eski to'rtburchak USB Type-A o'rniga kichik ovalsimon USB Type-C o'rnatilmoqda? Type-C ning 3 ta asosiy afzalligini yozing.
**Kutiladigan natija:** Har ikki tomondan ulanishi, yuqori tezligi va quvvat uzatish imkoniyati tushuntiriladi.

### 7. Drayverning zarurligini isbotlash · o'rta
Tasavvur qiling: do'stingiz yangi veb-kamera sotib oldi va USB ga uladi, ammo kompyuterda tasvir qotib qolmoqda va mikrofon ishlamayapti. Muammo nimada bo'lishi mumkin va uni qanday hal qilish kerak?
**Kutiladigan natija:** Ishlab chiqaruvchi saytidan rasmiy drayverni yuklab o'rnatish tartibi ko'rsatiladi.

### 8. Kiritish va chiqarishni birlashtirgan qurilmalar · o'rta
Smartfoningiz yoki planshetingizning sensorli ekrani (Touchscreen) bir vaqtning o'zida ham kiritish, ham chiqarish qurilmasi hisoblanadimi? Nima uchun?
**Kutiladigan natija:** Ekranning barmoq teginishini qabul qilishi (kiritish) va tasvirni ko'rsatishi (chiqarish) asosida xulosa.

### 9. Zamonaviy kompyuter ish stolini loyihalash · qiyin
Kelajakda grafik dizayner yoki dasturchi sifatida ishlash uchun o'zingizga ideal kompyuter ish stolini tasavvur qiling. Qanday asosiy va qo'shimcha qurilmalar (monitorlar soni, grafik planshet, akustika) sizga kerak bo'lishini ro'yxat qiling va har birining vazifasini yozing.
**Kutiladigan natija:** 6-8 ta periferiya qurilmasini o'z ichiga olgan reja.

### 10. Statik elektr va kompyuter xavfsizligi · qiyin
Kompyuterning tizim blokini ochib tozalashda nima uchun jun kiyim kiyish yoki to'g'ridan-to'g'ri mikrosxemalarga barmoq tekkizish xavfli hisoblanadi? Statik elektr toki kompyuter chiplariga qanday ta'sir qiladi?
**Kutiladigan natija:** Elektrostatik zaryadlanish va kompyuterni ochishdan oldin yerga ulangan metall korpusga tegib zaryadsizlanish qoidalari tushuntiriladi.

### 11. Kelajak periferiyasi: Neyrointerfeyslar (BCI) · bonus
Inson miyasidagi signallar orqali kompyuterni klaviatura va sichqonchasiz, to'g'ridan-to'g'ri fikr kuchi bilan boshqaruvchi **Brain-Computer Interface (BCI)** texnologiyasi haqida ma'lumot toping. Bu kelajakda kompyuterlar bilan ishlashni qanday o'zgartiradi?
**Kutiladigan natija:** Fikr signallarini qabul qilib buyruqqa aylantiruvchi neyrointerfeyslar haqida qisqacha tavsif.

---

## O'zingizni tekshiring

1. Kompyuterning 4 ta asosiy qurilmasi qaysilar?
2. Periferiya qurilmalari deb qanday qurilmalarga aytiladi?
3. Kiritish qurilmalariga 3 ta, chiqarish qurilmalariga 3 ta misol keltiring.
4. Lazerli va purkagichli printerlarning asosiy farqi nimada?
5. Drayver (Driver) nima va nima uchun operatsion tizimga yangi qurilma uchun drayver kerak?
6. USB Type-C porti Type-A dan qaysi jihatlari bilan ustun?
7. Nima uchun fleshkani kompyuterdan to'satdan sug'urib olish xavfli?

---

## Uyga vazifa

1. Uyingizdagi yoki yaqinlaringizning kompyuteriga ulangan barcha tashqi qurilmalarni ko'zdan kechiring. Ularning nomlarini «Kiritish» va «Chiqarish» ustunlariga ajratib yozing.
2. `Win + X` → «Device Manager» orqali «Sound, video and game controllers» bo'limini ochib, audio qurilmangiz nomini daftaringizga qayd eting.
3. USB orqali ulangan fleshkani xavfsiz ajratish («Eject») amalini mustaqil bajaring.
Vazifani bajarishga 20 daqiqa vaqt ajrating.
