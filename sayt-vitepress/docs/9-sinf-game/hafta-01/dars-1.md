---
title: "1-dars. Game Design faniga kirish: Tushunchasi, ahamiyati va dasturiy vositalar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Game)", "link": "/9-sinf-game/"}, "week": {"n": 1, "link": "/9-sinf-game/hafta-01/"}, "g": 1, "title": "Game Design faniga kirish: Tushunchasi, ahamiyati va dasturiy vositalar", "lead": "O'yin yaratish — bu shunchaki kod yozish yoki rasm chizish emas. Bu insonlar his qiladigan butun boshli yangi olam va unutilmas sarguzashtni barpo etish san'atidir!", "slide": "/slaydlar/9-sinf-game/hafta-01/dars-1.html", "tabs": [{"g": 1, "link": "/9-sinf-game/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/9-sinf-game/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/9-sinf-game/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "O‘yinlarning tarixi va janrlari: O'yin evolyutsiyasi, janrlar tasnifi va madaniy ta'siri", "link": "/9-sinf-game/hafta-01/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Game Design (o'yin dizayni)** — o'yinlarni g'oyadan boshlab to yakuniy relizgacha rejalashtirish, loyihalash va shakllantirish jarayonidir. U o'yindagi qoidalar, maqsadlar, o'yinchi harakatlari, atrof-muhit, grafika, ovozlar, hikoya va umumiy foydalanuvchi tajribasini ishlab chiqishni o'z ichiga oladi.
- **Game Designer (O'yin dizayneri)** — o'yinning umumiy arxitekturasi va hissiy tajribasini yaratuvchi mutaxassis. Uni o'yinning "rejissyori" deb atashadi. U dasturchilar, rassomlar, ssenaristlar va kompozitorlar ishini bitta g'oya atrofida birlashtiradi.
- **O'yin dizaynining 5 ta asosiy komponenti:**
  1. **Gameplay (O'yin jarayoni):** O'yinchining faol harakatlari — yugurish, sakrash, resurs to'plash, jang qilish, jumboq yechish.
  2. **Level Design (Bosqich dizayni):** Xaritalar, labirintlar, platformalar, to'siqlar va dushmanlarning fazoviy joylashuvi.
  3. **Narratsiya (Hikoya va syujet):** Voqealar rivoji, qahramonlar fe'l-atvori, dialoglar va o'yin olami tarixi (Lore).
  4. **UI (User Interface):** O'yinchi ekranda ko'radigan barcha tugmalar, menyular, mini-xarita va ko'rsatkichlar.
  5. **UX (User Experience):** O'yinchi o'yin davomida his qiladigan qulaylik, hayajon, qoniqish va intuitiv boshqaruv.
- **O'yin balansi (Balancing):** O'yin o'ta oson (zerikarli) yoki o'ta qiyin (tushkunlikka tushiruvchi) bo'lmasligi, o'yinchini doimo qiziqish holatida ("Flow") ushlab turishi shart.
- **Zamonaviy o'yin dvijoklari:**
  - **Unity:** Universal dvijok, 2D va 3D mobil, kompyuter va konsol o'yinlari uchun keng qo'llaniladi (C#).
  - **Unreal Engine:** Eng yuqori sifatli fotorealistik grafika (AAA o'yinlar) yaratish platformasi (C++ va Blueprints).
  - **Godot Engine:** Bepul, ochiq kodli va tezkor dvijok (GDScript).
  - **Construct 3 & GameMaker:** Kod yozmasdan yoki vizual bloklar orqali 2D o'yinlar yaratish uchun eng yaxshi vositalar.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Nega o'yin dizayneri dasturchidan farq qiladi?
Dasturchi kompyuterga nima qilishni aytadi (kod yozadi).
O'yin dizayneri esa **odamlar nima his qilishini** o'ylab topadi.
O'yin dizayneri:
- "Qahramon sakraganda oyoqlari qanchalik balandga ko'tariladi?"
- "Dushman zarba berishidan oldin qanday belgi berishi kerak?"
- "Qaysi qurol qancha zarar yetkazadi?"
kabi yuzlab savollarga javob beruvchi qoidalarni yozadi.

### 2. O'yin balansining "Oqim" (Flow) nazariyasi
Psixolog Mixay Chiksantmixayi tomonidan kashf etilgan "Flow" (Oqim) holati o'yin dizaynining eng muhim qonunidir:
- Agar o'yin vazifasi juda oson bo'lsa $\to$ o'yinchi **zerikadi** (Boredom);
- Agar vazifa o'yinchi mahoratidan ancha qiyin bo'lsa $\to$ o'yinchi **asabiylashadi va o'yinni o'chiradi** (Anxiety);
- Agar vazifa qiyinligi o'yinchining o'sib borayotgan mahoratiga aynan mos kelsa $\to$ o'yinchi **oqim holatiga tushadi** va vaqt qanday o'tganini sezmay qoladi!

### 3. GDD (Game Design Document) nima?
O'yin dizaynerining eng asosiy ish hujjati bu **GDD** hisoblanadi. Bu o'yinning to'liq "pasporti" bo'lib, unda:
- O'yinning bosh g'oyasi va janri;
- Asosiy qahramonlar va ularning qobiliyatlari;
- Barcha bosqichlar va dushmanlar turlari;
- Boshqaruv sxemasi va interfeys eskizlari batafsil qayd etiladi.
GDD bo'lmasa, dasturchilar va rassomlar bir-birini tushunmay qoladi.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Game Design** | O'yin qoidalari, mexanikasi, muhiti va hissiy tajribasini loyihalash jarayoni. |
| **Game Designer** | Video o'yinning kontseptsiyasi va qoidalarini yaratuvchi bosh mutaxassis ("rejissyor"). |
| **Gameplay** | O'yin jarayoni: o'yinchining o'yin ichida nima qilishi va bajaradigan harakatlari. |
| **Level Design** | O'yin xaritalari, bosqichlari, to'siqlari va labirintlarini rejalashtirish. |
| **Narratsiya** | O'yin ichidagi hikoya, syujet rivoji, qahramonlar dialoglari va dunyo tarixi. |
| **UI (User Interface)** | O'yinchi ekranda ko'radigan barcha tugmalar, panellar va ko'rsatkichlar. |
| **UX (User Experience)** | O'yinchining o'yin davomida oladigan umumiy hissiyoti va qulaylik darajasi. |
| **Game Engine (Dvijok)** | O'yinlar yaratish uchun tayyor fizika, grafika va ovoz modullariga ega dasturiy muhit. |
| **Game Balance** | O'yin qiyinligi, resurslar va qahramon kuchlarining adolatli va qiziqarli muvozanati. |
| **Indie Developer** | Katta korporatsiyalarga bog'liq bo'lmagan, o'z kuchi bilan o'yin yaratuvchi mustaqil ijodkor. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- 2024-yil holatiga ko'ra, dunyo o'yin industriyasining yillik aylanmasi **187 milliard dollardan oshdi** — bu butun dunyo Gollivud kinolari va global musiqa industriyasi yig'indisidan ancha ko'p!
- *Grand Theft Auto V* (GTA V) o'yini chiqarilgan ilk 3 kun ichida **1 milliard dollar** daromad keltirib, insoniyat tarixidagi barcha ko'ngilochar mahsulotlar orasida eng tez daromad keltirgan loyiha bo'lib tarixga kirdi.
- Dunyodagi eng ko'p sotilgan o'yin — *Minecraft* (300 milliondan ortiq nusxa) dastlab shved dasturchisi **Markus Persson (Notch)** tomonidan mustaqil ravishda bir o'zi boshlangan edi!
- Bepul ochiq kodli **Godot** o'yin dvijogining nomi mashhur Samuel Bekketning *"Godoni kutish"* ("Waiting for Godot") pyesasidan olingan bo'lib, o'yin dvijogining mukammallikka erishish yo'lidagi cheksiz rivojlanishini ramziy ifodalaydi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Game Designer vazifasini aniqlash <Badge type="tip" text="oson" />
Game Designer va 3D Modeller kasblari o'rtasidagi asosiy farqni 2 ta jumla bilan tushuntiring.
**Kutiladigan natija:** Dizayner o'yin qoidasini, modeler esa obyektning 3D shaklini yaratishi haqida to'g'ri javob.

### 2. O'yinning Gameplay qismini ajratish <Badge type="tip" text="oson" />
O'zingiz o'ynagan biror poyga o'yini (masalan, *Asphalt* yoki *Need for Speed*) misolida: undagi Gameplay elementlariga 3 ta aniq misol keltiring.
**Kutiladigan natija:** Gaz bosish, drift qilish, nitro faollashtirish kabi amallar.

### 3. Narratsiya nima? <Badge type="tip" text="oson" />
Nima uchun o'yinda shunchaki yugurishdan ko'ra, qahramonning maqsadi va hikoyasi (narratsiya) bo'lishi o'yinni qiziqroq qiladi?
**Kutiladigan natija:** Hissiy bog'lanish va maqsadlilik haqida fikr.

### 4. Dvijok tanlash: Unity vs Unreal <Badge type="warning" text="o'rta" />
Do'stingiz oddiy smartfonlar uchun 2D platformer o'yin yaratmoqchi. Unga Unreal Engine emas, balki Unity yoki Godot tanlashni maslahat berdingiz. 2 ta asosiy sababni keltiring.
**Kutiladigan natija:** Tizim resurslari yengilligi va 2D grafikaga moslashganligi sabablari.

### 5. Level Design tahlili <Badge type="warning" text="o'rta" />
*Super Mario* o'yinining 1-bosqichini eslang: nima uchun birinchi dushman (qo'ziqorin) o'yinchi ko'z o'ngida paydo bo'ladi va ustiga sakrashga undaydi? Game Designer bu bilan o'yinchiga qanday ko'nikmani o'rgatadi?
**Kutiladigan natija:** O'qituvchisiz (tutorialsiz) intuitiv boshqaruvni o'rgatish tahlili.

### 6. O'yinda "Flow" (Oqim) holatini saqlash <Badge type="warning" text="o'rta" />
O'yin boshlanishida o'yinchiga eng kuchli qurol va cheksiz jon berilsa nima yuz beradi? Flow nazariyasi bo'yicha bu o'yin taqdiriga qanday ta'sir qilishini tushuntiring.
**Kutiladigan natija:** Qiyinchilik yo'qligi sababli zerikish (boredom) yuzaga kelishi.

### 7. O'yin komponentlarini ajratish <Badge type="warning" text="o'rta" />
Stol ustidagi *Shaxmat* o'yinini Game Designning 5 komponenti (Gameplay, Level Design, Narratsiya, UI, UX) bo'yicha tahlil qilib yozing.
**Kutiladigan natija:** 64 katak (Level), donalar yurishi (Gameplay), ikki armiya jangi (Narratsiya), taxta va donalar ko'rinishi (UI), intellektual hayajon (UX).

### 8. Konstruktor vositalari tahlili <Badge type="danger" text="qiyin" />
*Construct 3* dasturida hodisalar qanday usulda (kod yozilmasdan) tuziladi? Event va Action mantiqiy juftligini o'yindagi oddiy misol bilan tushuntiring (masalan: tugma bosilganda o'q otish).
**Kutiladigan natija:** "Trigger (shart) $\to$ Action (harakat)" formulasi asosidagi tushuntirish.

### 9. O'yin balansi xatosini tuzatish <Badge type="danger" text="qiyin" />
O'yinda bitta qahramon boshqalarga qaraganda 5 barobar tez yuguradi va raqiblar unga yetolmaydi. Barcha o'yinchilar faqat shu qahramonni tanlay boshladi (Meta dominant). Ushbu muammoni qanday qilib adolatli muvozanatga (nerf/balance) keltirish mumkin? Kamida 2 ta yechim taklif qiling.
**Kutiladigan natija:** Tezlikni pasaytirish, uning himoyasini (jonini) kamaytirish yoki raqiblarga sekinlashtiruvchi to'r qobiliyatini berish.

### 10. Mini-o'yin g'oyasi konsepsiyasi (One-Page Pitch) <Badge type="info" text="bonus" />
Yangi mobil o'yin uchun 1 sahifalik qisqa konsept yozing:
1. O'yin nomi;
2. Janri;
3. Bosh qahramon va uning maqsadi;
4. Asosiy o'yin mexanikasi (o'yinchi nima qiladi);
5. Qaysi o'yin dvijogida yaratilishi.
**Kutiladigan natija:** To'liq shakllantirilgan yangi o'yin loyihasi loyihasi.

</div>

