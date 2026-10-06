# 13-dars. Sprayt sheet (atlas) tayyorlash va optimallashtirish

> Qahramoningiz yurishi uchun 6 ta rasm kerak, tangalar, zelyelar, kalitlar uchun yana o'nlab. Ularni bitta tartibli faylga yig'sak, o'yin tezroq ishlaydi. Bugun shu faylni — sprayt sheet'ni yaratamiz.

## Dars xulosasi

- **Sprayt sheet** — bir nechta sprayt yoki animatsiya kadri bitta PNG faylda to'r ko'rinishida joylashadi.
- **Animatsiya sheet** — bitta harakat kadrlari bir qatorda; **atlas** — turli obyekt va ikonkalar bitta rasmda.
- Atlas yuklanishni tezlashtiradi va **draw call** (videokartaga chizish buyrug'i) sonini kamaytiradi.
- Barcha **kataklar bir xil o'lchamda** (masalan, 32×32) — dvijok to'rni avtomatik kesadi.
- **Padding** (1–2 px oraliq) qo'shni kadr ranglari aralashib ketishidan saqlaydi.
- **Tayanch nuqta** (oyoq chizig'i) barcha kadrlarda bir xil — animatsiya sakramaydi.
- Eksport: shaffof **PNG, 100%**, nomida kadr o'lchami: `qahramon_yurish_sheet_32x32.png`.

## Qo'shimcha ma'lumot

### 1. Albom o'xshatishi
Tasavvur qiling, sizga 30 ta fotosurat kerak. Ularni 30 ta alohida konvertda saqlasangiz, har birini ochish uchun vaqt ketadi. Hammasi bitta albomda bo'lsa — bir marta ochasiz va kerakli sahifani topasiz. O'yin dvijogi uchun sheet aynan shu albom: bitta fayl, ichida tartibli joylashgan kadrlar.

### 2. Sheet o'lchamini hisoblash
Formula oddiy: **kenglik = kadrlar soni × kadr kengligi**, **balandlik = qatorlar soni × kadr balandligi**.

```
Kadr: 32×32 px
1-qator: idle     — 2 kadr
2-qator: yurish   — 6 kadr  (eng uzun qator)
3-qator: sakrash  — 3 kadr

Kenglik  = 6 × 32 = 192 px
Balandlik = 3 × 32 = 96 px
Sheet: 192×96 px (bo'sh kataklar shaffof qoladi)
```

Ko'p dvijoklar 2 ning darajasidagi o'lchamlarni (64, 128, 256, 512) yaxshi ko'radi. Shuning uchun 192×96 o'rniga 256×128 tanlab, zaxira joy qoldirish ham mumkin.

### 3. Nega oyoq chizig'i muhim?
Har kadrda qahramon katak ichida bir xil joyda «turishi» kerak. Agar 2-kadrda u 2 px yuqoriroq chizilsa, o'yinda qahramon har qadamda sakrab ketgandek ko'rinadi. Tekshirish usuli: Photoshop'da gorizontal yo'naltiruvchi chiziqni (guide) oyoq ostiga torting va barcha kadrlarni shu chiziq bo'yicha tekislang.

### 4. Optimallashtirish — 5 ta oddiy qoida
1. Kataklarni keragidan katta qilmang (16×16 obyektni 64×64 katakka qo'ymang).
2. Bir xil kadrlarni takrorlamang — dvijokda kadr vaqtini uzaytirish mumkin.
3. Cheklangan palitra: kam rang — kichik fayl va yaxlit uslub.
4. Dvijokka asl o'lchamni (100%) bering; kattalashtirishni dvijokning o'zi bajaradi.
5. O'xshash narsalarni bir qatorga yig'ing (pullar, zelyelar) — keyin topish oson.

### 5. Odatiy xatolar
- **JPG bilan saqlash** — shaffoflik yo'qoladi, qahramon atrofida oq to'rtburchak qoladi.
- **Har xil katak** — 30 px va 34 px aralash bo'lsa, dvijok kadrni yarmidan kesadi.
- **Padding yo'q** — ekranda qahramon chetida qo'shni kadrning ingichka chizig'i ko'rinadi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Sprayt sheet | Bir nechta kadr yoki sprayt joylashgan bitta rasm fayli |
| Atlas (texture atlas) | Turli spraytlar va ikonkalar yig'ilgan katta rasm |
| Kadr (frame) | Animatsiyaning bitta rasmi |
| Katak (cell) | Sheet to'ridagi bitta kadr o'rni, hammasi bir xil o'lchamda |
| Padding | Kataklar orasidagi kichik bo'sh joy |
| Tayanch nuqta (pivot) | Kadr ichida obyekt «turadigan» nuqta, odatda oyoq osti |
| Draw call | Dvijokning videokartaga «shuni chiz» degan buyrug'i |
| Slice | Dvijokda sheetni alohida kadrlarga kesish |
| Guide Layout | Photoshop'da teng ustun va qatorli yo'naltiruvchi to'r |
| Optimallashtirish | Sifatni saqlagan holda faylni yengil va tartibli qilish |

## Bilasizmi?

- Sprayt sheetlar 1980-yillardagi o'yin konsollarida ham ishlatilgan: xotira juda kam bo'lgani uchun barcha grafika kichik «plitkalar» to'plamida saqlangan.
- Unity'da sheet import qilinganda Sprite Mode: Multiple tanlanadi va Sprite Editor uni bir bosishda to'r bo'yicha kesadi.
- Ba'zi mobil o'yinlarda butun interfeys (tugmalar, ikonkalar, ramkalar) bitta-ikkita atlasga sig'diriladi — bu batareyani tejashga yordam beradi.
- Veb-saytlar ham shu g'oyadan foydalangan: «CSS sprites» — ko'p ikonka bitta rasmda, sahifa tezroq ochilgan.

## Topshiriqlar

### 1. Sheetni tanib oling · oson
Sevimli 2D o'yiningiz qahramonining qanday harakatlari (idle, yurish, sakrash, hujum) bo'lishi mumkinligini yozing va har biriga taxminan nechta kadr kerakligini taxmin qiling.

**Kutiladigan natija:** 4–5 qatorli ro'yxat «harakat — kadr soni».

### 2. O'lchamni hisoblang · oson
Kadr 16×16 px. 8 ta tanga kadri bir qatorda. Sheet o'lchami qancha?

**Kutiladigan natija:** bitta javob (kenglik × balandlik) va hisob.

### 3. Guide Layout · oson
Photoshop'da 128×32 px shaffof hujjat oching va View → New Guide Layout bilan 4 ta teng ustun yarating.

**Kutiladigan natija:** har 32 px da yo'naltiruvchi chiziq bor skrinshot.

### 4. Nomlash qoidasi · oson
Quyidagi fayllarga to'g'ri nom bering: qahramonning sakrash animatsiyasi (32×32), tanganing aylanish animatsiyasi (16×16), barcha obyektlar atlasi (16×16).

**Kutiladigan natija:** 3 ta fayl nomi `obyekt_holat_sheet_WxH.png` qoidasi bo'yicha.

### 5. Idle sheet · o'rta
12-darsdagi 2 kadrli idle animatsiyadan 64×32 px sheet yarating va PNG qilib eksport qiling.

**Kutiladigan natija:** `qahramon_idle_sheet_32x32.png`, oyoq chizig'i ikki kadrda bir xil.

### 6. Xatoni toping · o'rta
Do'stingizning sheetida kadrlar 30, 32, 34 px kenglikda, fon oq, fayl `rasm1.jpg`. Kamida 3 ta xatoni yozing va qanday tuzatishni ayting.

**Kutiladigan natija:** 3 ta xato va 3 ta tuzatish.

### 7. Yurish animatsiyasi · o'rta
4 kadrli yurish animatsiyasini chizing (oyoqlar navbat bilan oldinga) va 128×32 px sheetga yig'ing.

**Kutiladigan natija:** sheet PNG va Timeline'da 0.15 s kadrlar bilan ijro etilgan GIF.

### 8. Obyektlar atlasi · o'rta
64×64 px atlasda (16×16 kataklar) kamida 6 ta obyekt joylashtiring: o'xshashlari bir qatorda.

**Kutiladigan natija:** `obyektlar_atlas_16x16.png`.

### 9. Ko'p qatorli sheet · qiyin
Bitta sheetga 3 ta animatsiya: idle (2), yurish (4), sakrash (3). O'lchamni hisoblang, qatorlarni nomlang va tayanch nuqtani tekshiring.

**Kutiladigan natija:** 128×96 px sheet va qatorlar ro'yxati.

### 10. Optimallashtirish tajribasi · qiyin
6 ta obyektni alohida PNG va bitta atlas qilib saqlang. Fayllar hajmini solishtiring va xulosa yozing.

**Kutiladigan natija:** hajmlar jadvali va 2–3 jumla xulosa.

### 11. Tanga yaltirashi · qiyin
16×16 tanga uchun 4 kadrli aylanish (keng → tor → chiziq → tor) animatsiyasini chizing va sheetga yig'ing.

**Kutiladigan natija:** 64×16 px sheet, GIF namunasi.

### 12. Interfeys atlasi · bonus
11-darsdagi ikonkalaringiz (jon, tanga, kalit, sozlamalar) va bo'sh tugma shaklini bitta 128×128 atlasga joylang — keyingi darsda tugmalar uchun kerak bo'ladi.

**Kutiladigan natija:** `ui_atlas.png` va qaysi katakda nima borligi ro'yxati.

## O'zingizni tekshiring

1. Sprayt sheet va atlasning farqi nimada?
2. Nega o'yin dvijoklari alohida fayllardan ko'ra atlasni afzal ko'radi?
3. Draw call nima?
4. Nega barcha kataklar bir xil o'lchamda bo'lishi shart?
5. Padding qanday muammoni hal qiladi?
6. Tayanch nuqta noto'g'ri bo'lsa, animatsiyada nima bo'ladi?
7. Sheetni nima uchun JPG'da saqlab bo'lmaydi?

## Uyga vazifa

Qahramoningiz uchun idle (2 kadr) va yurish (4 kadr) animatsiyalaridan bitta 128×64 px sheet tayyorlang, obyektlaringizdan 64×64 atlas yig'ing va ikkalasini PNG qilib eksport qiling (20–30 daqiqa). Batafsil — haftalik uyga vazifada.
