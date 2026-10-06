# 17-dars. O'yin interfeysini prototiplash (1-qism): Wireframe, Mockup va Prototype bosqichlari

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga prototiplash tushunchasi va uning o'yin yaratishdagi ahamiyatini, qisqacha tarixini, prototip turlarini, Wireframe, Mockup va Prototype bosqichlari va ularning farqini, prototiplash vositalarini tanishtirish hamda qog'ozda bosh menyu wireframe'ini chizdirish.
- **Kutiladigan natija:** O'quvchilar prototiplash nima va nima uchun kerakligini tushuntiradi; wireframe, Mockup va Prototype farqini aytadi; prototip turlaridan 4 tasini va 3 ta vositani sanaydi; prototip va vertikal kesim (vertical slice) farqini biladi; qog'ozda bosh menyu wireframe'ini chizadi.
- **Vaqt taqsimoti:**
  - 16-dars: HUD maketi: 10 daqiqa
  - Prototiplash: nima, nega, tarixi: 10 daqiqa
  - Wireframe, Mockup, Prototype: 20 daqiqa
  - Turlar va vositalar: 15 daqiqa
  - Amaliyot: qog'ozda wireframe: 25 daqiqa

> Manba: o'quv dasturi — «O'yin interfeysini prototiplash» moduli («prototiplash tushunchasi, uning o'yin yaratishda ahamiyati; prototiplash turlari (Wireframe, Mockup, Prototype) va ularning vazifalari; qisqa tarixi; o'yin dvijoklarida prototiplash; texnologiyalar: qog'ozda chizish, grafik dasturlarda yaratish, dvijoklarda sinash»); o'quv qo'llanma — 2.5-bo'lim (prototip vazifalari, turlari, prototip va vertikal kesim farqi, vositalar: Unity, GameMaker, Godot, Construct 3; Figma, Adobe XD, Axure RP; Photoshop'da UI yaratish bosqichlari). Wireframe — Mockup — Prototype ta'riflari umumiy UX amaliyotiga mos soddalashtirilgan.

---

## Mentor konspekti

### 1. Prototiplash tushunchasi va ahamiyati

**Prototiplash** (prototyping) — dizayn g'oyasini vizuallashtirish, uni to'liq ishlab chiqishdan **oldin** tekshirish, o'zaro ta'sirni sinash va foydalanuvchilardan fikr olish jarayoni. Qo'llanmaga ko'ra prototip bir vaqtda bir nechta vazifani bajaradi: dastlabki g'oyani tasdiqlaydi; taxmin qilingan mexanika va geympleyni sinaydi; boshqalarga ko'rsatish uchun birinchi kontent bo'ladi; keyingi vertikal kesim uchun asos yaratadi. Eng muhim foyda — **xatoni erta va arzon topish**: qog'ozdagi chiziqni o'chirish bir daqiqa, tayyor dasturni qayta yozish esa hafta oladi. Qisqa tarix (qo'llanma): prototiplash sanoat dizayni va arxitekturada maketlar bilan boshlangan; dasturiy ta'minotda 1970-yillarda mustaqil usul bo'lib shakllandi; 1990-yillarda GUI tarqalishi bilan jarayonning ajralmas qismiga aylandi; 2002-yilda Axure RP kabi vositalar paydo bo'ldi; hozir Figma, Sketch, Adobe XD kabi vositalar bor.

```text
Prototip nima beradi:
1. G'oyani tasdiqlaydi
2. Mexanika va geympleyni sinaydi
3. Boshqalarga ko'rsatishga tayyor birinchi kontent
4. Vertikal kesim uchun asos

Vaqt:  qog'oz - daqiqalar
       raqamli maket - soatlar
       kod - kunlar, haftalar
```

> Professional maslahat: Vaqt qiyoslari taxminiy, fikrni tushuntirish uchun. Qoida: muammo qanchalik erta topilsa, tuzatish shunchalik arzon.

### 2. Wireframe, Mockup va Prototype

Interfeys uch bosqichda «aniqlashib» boradi. **Wireframe** (simli maket) — eng sodda sxema: qora-oq (yoki kulrang) to'rtburchaklar, chiziqlar va yorliqlar; **tuzilma va joylashuv** (qaysi element qayerda) ko'rsatiladi, rang, rasm va chiroyga e'tibor berilmaydi. **Mockup** (maket) — wireframe ustiga **vizual dizayn**: ranglar, shriftlar, ikonkalar, soyalar; ko'rinishi tayyor mahsulotga o'xshaydi, lekin **statik** (tugma bosilmaydi). **Prototype** — **interaktiv** model: tugma bosilsa keyingi ekran ochiladi, o'tishlar ishlaydi; foydalanish qulayligini sinash mumkin. Tartib: Wireframe → Mockup → Prototype. Har bosqichda savol boshqacha: wireframe'da «hamma narsa o'z o'rnidami?», mockup'da «chiroyli va tushunarlimi?», prototype'da «ishlatish qulaymi?». Prototip **vertikal kesim** (vertical slice) emas: prototip asosiy mexanikaga e'tibor qaratadi, vertikal kesim esa tayyor mahsulotning mini-versiyasi (grafika, ovoz, o'yin jarayoni — hammasi sifatli).

```text
+------------------------------+
|           [LOGO]             |
|                              |
|        [ START ]             |
|        [ SOZLAMALAR ]        |
|        [ CHIQISH ]           |
|                              |
|  [?]                  [v1.0] |
+------------------------------+
```

> Professional maslahat: Wireframe'da faqat qutilar va yozuvlar. Rang, soya, ikonka — keyingi bosqich (Mockup) ishi.

### 3. Prototip turlari va vositalari

Qo'llanma prototip turlarini sanaydi: **qog'oz prototiplari**; raqamli **statik** prototiplar; **bosiladigan** (clickable) prototiplar; **yuqori aniqlikdagi interaktiv** prototiplar; **kodlangan** prototiplar; konseptual va xizmat prototiplari. O'yin interfeysi uchun odatda: qog'ozda chizish → grafik dasturda (Photoshop) maket → o'yin dvigatelida sinash. **Qog'ozda prototiplash** dasturlash ko'nikmasini talab qilmaydi, o'zgartirish oson; kamchiligi — ba'zi interaktiv jihatlarni ko'rsatish qiyin. **Vositalar** (qo'llanma): dvigatellar — Unity, GameMaker, Unreal Engine, Godot, Construct 3, Defold; UI/UX vositalar — Figma, Adobe XD, Axure RP; maxsus — Machinations, Twine; grafik — Photoshop, Illustrator. Tanlov o'yin turi va murakkabligiga bog'liq. Photoshop'da UI yaratishning prototiplash bosqichi — «past darajada detallashtirilgan maketlarni yaratish» (qo'llanma): shundan keyingina vizual dizayn boshlanadi.

```text
Qog'oz va qalam   -> eng birinchi g'oya, 5 daqiqada
Photoshop / Figma -> wireframe va mockup maketi
Unity / Godot     -> interaktiv, o'yin ichida sinash
Machinations      -> o'yin iqtisodi va mexanikasi
Twine             -> hikoya (shoxlanuvchi) prototipi
```

> Professional maslahat: Mukammal vosita yo'q: avval eng oddiyini tanlang. Eng yaxshi prototip — g'oyani eng tez tekshiradigani.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Atamalar (oson)
Wireframe, Mockup va Prototype ni bir gapda ta'riflang.

**Bajarish tartibi:**
Wireframe — tuzilma va joylashuv sxemasi; Mockup — rang va shriftli statik vizual maket; Prototype — bosilib, ekranlar almashadigan interaktiv model.

### 2-topshiriq. Bosqichni toping (oson)
«Menyu tugmalari qora-oq to'rtburchaklar» — bu qaysi bosqich?

**Bajarish tartibi:**
Wireframe — faqat tuzilma va joylashuv, rang va bezak yo'q.

### 3-topshiriq. Vositalar (o'rta)
O'yin interfeysi prototipi uchun 3 ta vosita nomini va ularning vazifasini yozing.

**Bajarish tartibi:**
Photoshop/Figma — wireframe va mockup maketi; Unity yoki Godot — interaktiv sinov o'yin ichida; qog'oz va qalam — eng birinchi g'oya.

### 4-topshiriq. Prototip va vertikal kesim (o'rta)
Prototip va vertikal kesim farqini tushuntiring.

**Bajarish tartibi:**
Prototip asosiy mexanika va g'oyani tez tekshiradi, tayyor bo'lishi shart emas; vertikal kesim — tayyor mahsulotning mini-versiyasi bo'lib, grafika, ovoz va o'yin jarayoni sifatli.

### 5-topshiriq. Qog'ozdagi wireframe (qiyin)
Bosh menyu wireframe'ini qog'ozda chizing: logotip, START, Sozlamalar, Chiqish; hamkasbingiz bilan test qiling.

**Bajarish tartibi:**
16:9 to'rtburchak; yuqori o'rtada logotip qutisi; markazda uchta tugma qutisi (START, SOZLAMALAR, CHIQISH); pastda versiya yorlig'i. Hamkasb 5 soniyada START'ni topsa — joylashuv yaxshi.

### 6-topshiriq. Photoshop'ga ko'chirish (bonus)
Wireframe'ni Photoshop'da 1920×1080 px kulrang qutilar bilan qayta chizing.

**Bajarish tartibi:**
File → New, 1920×1080 px; Rectangle Tool bilan kulrang qutilar; Text Tool bilan yorliqlar; har element alohida qatlam; Ctrl + G bilan «Bosh menyu» guruhi; PNG sifatida eksport.

---

## Tezkor nazorat savollari

1. Prototiplash nima?
   - *Javob:* Dizayn g'oyasini ishlab chiqishdan oldin vizuallashtirib sinash jarayoni.
2. Uch bosqichni ayting.
   - *Javob:* Wireframe, Mockup, Prototype.
3. Wireframe da rang bo'ladimi?
   - *Javob:* Yo'q, faqat tuzilma va joylashuv.
4. Prototip turlaridan 3 tasi?
   - *Javob:* Qog'oz, statik raqamli, bosiladigan, yuqori aniqlikdagi interaktiv.
5. Prototip va vertikal kesim farqi?
   - *Javob:* Prototip mexanikani tekshiradi; vertikal kesim tayyor mahsulotning mini-versiyasi.

---

## Uyga vazifa

1. Bosh menyu wireframe'ini qog'ozda chizing (logotip, START, Sozlamalar, Chiqish) va suratga oling.
2. O'yin ekrani wireframe'ini chizing: HUD elementlarining joylari 16-darsdagi kabi bo'lsin.
3. Wireframe, Mockup va Prototype farqini 3 ta jumlada yozing.
4. Oilangiz a'zosi yoki do'stingizga wireframe'ni ko'rsating: «START tugmasi qayerda?» deb so'rang va natijani yozing.
