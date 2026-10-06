# 13-dars. O'yin uchun ikonka va spraytlar yaratish (3-qism): Sprayt sheet (atlas) tayyorlash va optimallashtirish

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga animatsiya kadrlarini va o'yin obyektlarini bitta PNG faylga — sprayt sheet (atlas) ko'rinishiga yig'ishni o'rgatish; nega o'yin dvijoklari (Unity, Godot, Unreal) atlasni afzal ko'rishini (draw call, xotira, yuklanish) tushuntirish; Photoshop'da teng katakli to'r bo'yicha sheet tayyorlash, nomlash va eksport qilishni amalda bajarish.
- **Kutiladigan natija:** O'quvchilar 12-darsdagi qahramon kadrlaridan va obyekt spraytlaridan 2 ta sheet tayyorlaydi: animatsiya sheet (bir qator, teng kataklar) va obyektlar atlasi (ikonka + sprayt); fayl hajmini va ranglar sonini optimallashtiradi; shaffof PNG qilib eksport qiladi va kadr o'lchamini (masalan, 32×32) hujjatga yozib qo'yadi.
- **Vaqt taqsimoti:**
  - Takrorlash (sprayt bosqichlari, idle animatsiya): 10 daqiqa
  - Yangi mavzu: sprayt sheet va atlas tushunchasi, nega kerak: 15 daqiqa
  - Sheet tuzilishi: katak, qator, padding, tartib: 10 daqiqa
  - Amaliyot: Photoshop'da animatsiya sheet yig'ish: 25 daqiqa
  - Optimallashtirish va eksport, atlas tuzish: 15 daqiqa
  - Xulosa: 5 daqiqa

> Manba: o'quv qo'llanma — 2.3-bo'lim («qahramonning yurishi, sakrashi kabi animatsiyalar sprat-sheet ko'rinishida PNG bilan yaratiladi. O'yin dvijoklari (Unity, Godot, Unreal) PNG-ni juda yaxshi qo'llab-quvvatlaydi»), 2.4-bo'lim, 8-bosqich («Animatsiya yoki turli holatlar bo'lsa, alohida frame yoki sprite sheet tayyorlanadi»), 7-bob («Draw call sonini kamaytirish uchun sprite atlaslaridan foydalaning»). Photoshop'dagi amaliy usullar (Canvas Size, Guides, Trim) — darsni boyituvchi amaliy qism; hujjatda batafsil qadamlar yo'q.

---

## Mentor konspekti

### 1. Sprayt sheet nima?

**Sprayt sheet** — bir nechta sprayt yoki animatsiya kadri bitta rasm faylida (odatda shaffof PNG) to'r ko'rinishida joylashgan fayl. O'yin dvijogi kerakli kadrni shu rasmdan «kesib» oladi.

- **Animatsiya sheet:** bitta harakatning kadrlari ketma-ket (idle 2 kadr, yurish 4–6 kadr, sakrash 3 kadr). Odatda bitta qator = bitta animatsiya.
- **Atlas (texture atlas):** turli spraytlar va ikonkalar bitta katta rasmda (tanga, zelye, kalit, jon belgisi, tugma ikonkalari).

Hayotiy o'xshatish: albom varaqlaridagi fotosuratlar. 20 ta alohida rasmni 20 marta qidirgandan ko'ra, bitta albomni ochib kerakli sahifani olish tezroq.

### 2. Nega kerak?

| Muammo (alohida fayllar) | Sheet/atlas bilan |
|---|---|
| Har rasm uchun alohida yuklash | bitta fayl bir marta yuklanadi |
| Har rasm uchun alohida **draw call** (videokartaga chizish buyrug'i) | bir xil atlasdagi spraytlar birga chiziladi — draw call kamayadi |
| Yuzlab mayda fayllar — tartibsizlik | bitta tartibli fayl, kadrlar ketma-ket |
| Animatsiya kadrlari aralashib ketadi | qator va ustun bo'yicha aniq tartib |

O'quv qo'llanmadagi tavsiya: *«Draw call sonini kamaytirish uchun sprite atlaslaridan foydalaning»* — ayniqsa mobil qurilmalarda.

### 3. Sheet tuzilishi

- **Katak (cell/frame):** har kadr uchun bir xil o'lcham, masalan 32×32 px. Hamma kataklar teng — dvijok to'rni avtomatik kesadi (Unity'da *Grid By Cell Size*).
- **Qator:** bitta animatsiya. 1-qator — idle, 2-qator — yurish, 3-qator — sakrash.
- **Padding (oraliq):** kataklar orasida 1–2 px bo'sh joy — qo'shni kadr rangi «oqib» kirmasligi uchun (bleeding).
- **Tayanch nuqta (pivot):** barcha kadrlarda qahramon oyog'i bir xil balandlikda — aks holda animatsiya «sakraydi».
- **Hajm:** 4 kadr × 32 px = 128 px kenglik. Ko'p dvijoklar uchun 2 ning darajalari (64, 128, 256, 512) qulay.

### 4. Photoshop'da animatsiya sheet yig'ish

1. Yangi hujjat: **128×32 px** (4 kadr × 32), Background — **Transparent**.
2. **View → New Guide Layout:** Columns 4, Gutter 0 — har 32 px da yo'naltiruvchi chiziq.
3. 12-darsdagi `.psd` dan har kadr guruhini nusxalab (`Ctrl + J`, so'ng sudrab), har biri o'z katagiga **Move Tool (V)** bilan joylashtiriladi. Snap yoqilgan bo'lsin (View → Snap).
4. Qatlamlar nomi: `kadr_01`, `kadr_02`... guruh nomi: `idle`.
5. Tekshirish: oyoq chizig'i barcha kadrlarda bir xil y koordinatada.
6. **File → Export → Export As:** PNG, Transparency ✓, 100% — dvijok uchun. Nomi: `qahramon_idle_sheet_32x32.png` (kadr o'lchami nomda).

### 5. Obyektlar atlasi

- Hujjat **64×64 px** (16×16 kataklar, 4×4 = 16 o'rin) yoki 128×128 px.
- Tanga, zelye, kalit, jon belgisi va 11-dars ikonkalari bir uslubda joylashtiriladi.
- Bo'sh kataklar zaxira uchun qoldiriladi — yangi buyum qo'shilganda atlas o'lchami o'zgarmaydi.
- Yonma-yon: o'xshash narsalar bir qatorda (pullar, zelyelar, kalitlar).

### 6. Optimallashtirish

- **Kerakmas bo'sh joyni kesish:** kataklar ichida qahramon atrofidagi juda katta bo'shliq — kadr o'lchamini kichraytiring (lekin hammasi bir xil bo'lsin).
- **Ranglar soni:** cheklangan palitra (16–32 rang) — fayl kichik, uslub yaxlit.
- **Nusxa kadrlarni olib tashlash:** bir xil ikki kadr bo'lsa, birini qoldiring, dvijokda kadr vaqti uzaytiriladi.
- **To'g'ri format:** sheet — PNG (shaffoflik, sifat yo'qotmaydi). JPG — yo'q (shaffoflik yo'q, siqishda artefaktlar). GIF — faqat namoyish uchun.
- **Masshtab:** dvijokka 100% (asl o'lcham) beriladi, kattalashtirishni dvijokning o'zi qiladi (Filter: Point/Nearest).
- **Nomlash:** `obyekt_holat_sheet_WxH.png` — jamoada hamma tushunadi.

### 7. Dvijokda nima bo'ladi (qisqa namoyish, so'z bilan)

Unity'da PNG import qilinadi → Sprite Mode: **Multiple** → Sprite Editor → Slice → *Grid By Cell Size* 32×32 → kadrlar `qahramon_idle_0`, `_1`... bo'lib ajraladi. Bu Unity bo'limida (keyinroq) amalda o'tiladi; bugun faqat «nega to'g'ri katak muhim» ekanini ko'rsating.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Sheet hisobi (oson)
Qahramon kadri 32×32 px. Yurish animatsiyasi 6 kadrdan iborat va bir qatorda joylashadi. Sheet o'lchami qancha bo'ladi? Agar idle (2 kadr) va sakrash (3 kadr) ham alohida qatorlarga qo'shilsa-chi?

**Yechim:**
Bir qator: 6 × 32 = **192×32 px**. Uch qator (eng uzun qator 6 kadr): kenglik 192 px, balandlik 3 × 32 = 96 px → **192×96 px**. Bo'sh kataklar (idle qatorida 4 ta, sakrashda 3 ta) shaffof qoladi.

### 2-topshiriq. Idle sheet (oson)
12-darsdagi 2 kadrli idle animatsiyadan 64×32 px sheet tayyorlang.

**Yechim:**
File → New 64×32, Transparent → View → New Guide Layout (Columns 2) → har kadr guruhini o'z katagiga → oyoq chizig'i bir xil → Export As PNG `qahramon_idle_sheet_32x32.png`. Tekshirish: 800% da ko'rilganda kadrlar chegaradan chiqmaydi.

### 3-topshiriq. Yurish animatsiyasi sheet (o'rta)
Qahramon uchun 4 kadrli yurish animatsiyasini chizing (oyoqlar: o'ng oldinda → birga → chap oldinda → birga) va 128×32 px sheet qilib yig'ing.

**Yechim:**
1. Kadr 1: o'ng oyoq oldinda, tana 1 px pastda; kadr 2: oyoqlar birga, tana asl joyda; kadr 3: chap oyoq oldinda, tana 1 px pastda; kadr 4: kadr 2 ning nusxasi (yoki biroz farqli qo'l holati).
2. 128×32 hujjat, Guide Layout Columns 4, kadrlar joylashtiriladi.
3. Tekshirish: Timeline'da 4 kadr × 0.15 s qilib ijro etilganda qahramon «joyida yuradi», oyoq chizig'i sakramaydi.
4. Export: `qahramon_yurish_sheet_32x32.png`.

### 4-topshiriq. Obyektlar atlasi va optimallashtirish (qiyin)
64×64 px atlasga (16×16 kataklar) kamida 6 ta obyekt va ikonka joylashtiring, o'xshashlarini bir qatorga qo'ying, faylni PNG qilib saqlang va alohida PNG fayllar yig'indisi bilan hajmini solishtiring.

**Yechim:**
- 1-qator: tanga (2 kadr: oddiy + yaltirash), olmos; 2-qator: qizil va moviy zelye; 3-qator: kalit, sandiq ikonkasi; 4-qator: zaxira.
- Ranglar — 12-dars palitrasidan, kontur rangi bir xil.
- Export As PNG `obyektlar_atlas_16x16.png`. Alohida 6 ta PNG odatda jami bir necha KB ko'proq (har faylda sarlavha ma'lumotlari takrorlanadi), atlas esa bitta fayl — hajm va yuklanish kamayadi. Asosiy foyda — dvijokda draw call kamayishi.

---

## Tezkor nazorat savollari

1. Sprayt sheet nima?
   - *Javob:* Bir nechta sprayt yoki animatsiya kadri bitta rasm faylida to'r ko'rinishida.
2. Nega atlas o'yinni tezlashtiradi?
   - *Javob:* Bitta fayl yuklanadi va bir xil atlasdagi spraytlar birga chiziladi — draw call kamayadi.
3. Nega barcha kataklar bir xil o'lchamda bo'lishi kerak?
   - *Javob:* Dvijok to'rni avtomatik kesadi (Grid By Cell Size); har xil katak kadrlarni buzadi.
4. Padding nima uchun kerak?
   - *Javob:* Qo'shni kadr ranglari bir-biriga «oqib» kirmasligi uchun.
5. Sheet qaysi formatda saqlanadi?
   - *Javob:* Shaffof PNG, asl o'lchamda (100%).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Kataklar har xil o'lchamda:** dvijok kadrlarni noto'g'ri kesadi — Guide Layout bilan teng to'r.
- **Tayanch nuqta suriladi:** animatsiyada qahramon «sakraydi» — oyoq chizig'ini barcha kadrlarda tekshiring.
- **Kadrlar orasida padding yo'q:** chetlarda qo'shni kadr rangi ko'rinadi — 1–2 px oraliq yoki toza shaffof chet.
- **JPG eksport:** fon oq bo'lib qoladi — faqat PNG.
- **800% kattalashtirilgan sheetni dvijokka berish:** fayl og'ir — dvijokka 100%.
- **Nomda kadr o'lchami yo'q:** jamoadosh qanday kesishni bilmaydi — `_32x32` qo'shing.
