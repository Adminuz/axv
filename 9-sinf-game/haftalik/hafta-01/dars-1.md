# 1-dars. Game Design faniga kirish: Tushunchasi, ahamiyati va dasturiy vositalar

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga Game Design (o'yin dizayni) sohasi, uning zamonaviy raqamli madaniyat va iqtisodiyotdagi o'rni, Game Designer kasbiy roli va vazifalari, o'yin dizaynining 5 ta asosiy komponenti (Gameplay, Level Design, Narratsiya, UI va UX) hamda zamonaviy o'yin dvijoklari (Unity, Unreal Engine, Godot) va konstruktorlari haqida chuqur nazariy va amaliy tushuncha berish.
- **Kutiladigan natija:** O'quvchilar o'yin dizayneri faqat dasturchi yoki rassom emas, balki butun o'yin tajribasini yaratuvchi "rejissyor" ekanini anglaydi; o'yinning 5 komponentini mustaqil tahlil qila oladi; o'z g'oyasiga mos o'yin dvijogini tanlay oladi.
- **Vaqt taqsimoti:**
  - Kirish va yo'nalish bilan tanishuv: 10 daqiqa
  - Yangi mavzu: Game Design nima va uning ahamiyati: 20 daqiqa
  - Game Designer roli va 5 ta asosiy komponent: 25 daqiqa
  - Dasturiy vositalar (Dvijoklar va konstruktorlar) tahlili: 15 daqiqa
  - Tezkor savol-javob va xulosa: 10 daqiqa

---

## Mentor konspekti

### 1. Game Design tushunchasi va uning ahamiyati
- **Game Design (o'yin dizayni)** — bu o'yinlarni g'oyadan boshlab to yakuniy ko'rinishigacha rejalashtirish, loyihalash va shakllantirish jarayonidir. U o'yindagi qoidalar, maqsadlar, o'yinchi harakatlari, atrof-muhit, grafika, ovozlar, hikoya va umumiy foydalanuvchi tajribasini ishlab chiqishni qamrab oladi.
- **Ahamiyati:**
  - *Ta'limiy ahamiyati:* Simulyatsiya va ta'limiy o'yinlar orqali fizika, tarix, biologiya kabi murakkab fanlarni interaktiv o'zlashtirish.
  - *Ijodiy fikrlash:* Yangi virtual olamlar, noan'anaviy personajlar va qiziqarli mexanikalarni yaratish.
  - *Iqtisodiy ahamiyati:* Dunyoda o'yin industriyasi (GameDev) kino va musiqa sohalarining umumiy daromadidan ham oshib ketgan (yillik 200+ milliard dollar).
  - *Psixologik va ijtimoiy:* Motivatsiya, jamoaviy hamkorlik va strategik qaror qabul qilish ko'nikmalarini shakllantirish.

### 2. Game Designer (O'yin dizayneri) kim?
Game Designer — bu video o'yinning kontseptsiyasi, mexanikasi va qoidalarini ishlab chiqish uchun mas'ul bo'lgan asosiy mutaxassis.
- Uni o'yinning **"bosh rejissyori"** deb atash mumkin.
- **Asosiy vazifalari:**
  1. *Kontseptsiya va qoidalar:* O'yin nima haqida, unda qanday qoidalar mavjudligini belgilash.
  2. *Gameplay loyihalash:* O'yinchi har soniyada nima qiladi va qanday his qiladi?
  3. *O'yin balansi (Balancing):* O'yin haddan tashqari oson bo'lib zeriktirmasligi yoki o'ta qiyin bo'lib tushkunlikka tushirmasligi kerak.
  4. *Jamoani muvofiqlashtirish:* Dasturchilar, 2D/3D rassomlar, kompozitorlar va ssenaristlar ishini yagona maqsad sari birlashtirish.

### 3. O'yin dizaynining 5 ta asosiy komponenti
Robert Zubek va Kris Krouford tasnifiga ko'ra:
1. **Gameplay (O'yin jarayoni):** O'yinchining faol harakatlari — yugurish, sakrash, jang qilish, resurs yig'ish, jumboq yechish.
2. **Level Design (Bosqich dizayni):** O'yin xaritalari, labirintlar, to'siqlar va dushmanlarning joylashuv arxitekturasi.
3. **Narratsiya (Hikoya va syujet):** Voqealar rivoji, qahramonlar xarakteri, dialoglar va o'yin olami tarixi (Lore).
4. **UI (User Interface):** O'yinchi ekranda ko'radigan barcha boshqaruv tugmalari, menyular va ko'rsatkichlar.
5. **UX (User Experience):** O'yinchi o'yin davomida oladigan umumiy hissiyot, qoniqish va boshqaruv qulayligi.

### 4. Dasturiy vositalar: O'yin dvijoklari va konstruktorlar
- **Game Engine (O'yin dvijogi):** Noldan hamma narsani dasturlamasdan, tayyor fizika, render, animatsiya va audio tizimlaridan foydalanib o'yin yaratish muhiti.
  - **Unity:** Dunyodagi eng ommabop universal dvijok. 2D va 3D mobil, kompyuter va konsol o'yinlari uchun ideal (C# tili).
  - **Unreal Engine:** Eng yuqori sifatli fotorealistik grafika (AAA loyihalar) dvijogi (C++ va Blueprints vizual skripti).
  - **Godot Engine:** Bepul, ochiq kodli (open-source), juda yengil va tezkor dvijok (GDScript, C#).
- **Konstruktorlar (Boshlovchilar uchun):**
  - **Construct 3:** Kod yozmasdan, brauzerda bloklar va hodisalar (Event Sheet) orqali 2D o'yinlar yaratish.
  - **GameMaker Studio:** 2D platformerlar va pikselli o'yinlar yaratishda yetakchi (GML tili).
  - **RPG Maker:** Maxsus 2D rolli (RPG) o'yinlar yaratish vositasi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Mashhur o'yinning 5 komponentini tahlil qilish (oson)
O'zingizga ma'lum bo'lgan bitta mashhur o'yinni (masalan, *Subway Surfers* yoki *Minecraft*) o'yin dizaynining 5 ta asosiy komponenti bo'yicha tahlil qiling.

**Yechim:**
*Subway Surfers* misolida:
1. **Gameplay:** Poezdlar ustida chopish, to'siqlardan chapga-o'ngga qochish, sakrash, tangalar va kuchaytirgichlar (jetpack, magnet) yig'ish.
2. **Level Design:** Cheksiz davom etuvchi 3 ta temir yo'l izi, dinamik harakatlanuvchi vagonlar, tunnellar va to'siqlar joylashuvi.
3. **Narratsiya:** Grafiti chizayotgan yosh qahramonning qattiqqo'l nazoratchi va uning itidan qochishi haqidagi sodda, ammo jozibali motivatsiya.
4. **UI:** Ekranning tepasidagi tangalar soni, masofa hisoblagichi, multiplikator ko'rsatkichi va pauza tugmasi.
5. **UX:** Bir barmog'ingiz bilan boshqariladigan silliq siljitish (swipe) mexanikasi, yorqin ranglar va dinamik musiqa orqali hayajon uyg'otishi.

### 2-topshiriq. Loyiha talabiga qarab o'yin dvijogini tanlash (o'rta)
Mustaqil ishlab chiquvchi (Indie developer) jamoasi quyidagi o'yinni yaratmoqchi:
"2D uslubidagi mobil boshqotirma o'yini, jamoada dasturchi yo'q, hamma narsani 2 oy ichida vizual tarzda yaratib, Android'ga yuklash kerak."
Qaysi dasturiy vosita eng maqbul hisoblanadi va nima uchun?

**Yechim:**
**Construct 3** (yoki GameMaker).
*Sababi:*
1. Dasturlash tillarini (C#, C++) bilish talab etilmaydi — voqealar mantiqiy bloklar (Event System) orqali yig'iladi.
2. 2D grafikaga to'liq ixtisoslashgan va mobil ekranlarga juda tez moslashadi.
3. Ishlab chiqish muddati juda qisqa (rapid prototyping).

### 3-topshiriq. O'yin mexanikasi va balansi loyihasi (qiyin)
Tasavvur qiling, siz yangi jangovar o'yinda o'yinchiga "Sehrli qalqon" (Magic Shield) qobiliyatini berdingiz. Ushbu qalqon barcha zarbalarni 100% qaytaradi.
Ushbu qobiliyat o'yin balansini buzmasligi uchun qanday cheklovlar va muvozanat mexanizmlari kiritishingiz kerak?

**Yechim:**
Agar qalqon cheksiz ishlasa, o'yinchi yengilmas bo'lib qoladi va o'yin zerikarli bo'lib qoladi (Balans buziladi). Muvozanat uchun:
1. **Cooldown (Qayta yuklanish vaqti):** Qalqon faqat 3 soniya ishlaydi, qayta ishlatish uchun 15 soniya kutish kerak.
2. **Energiya/Mana sarfi:** Qalqon har soniyada katta miqdorda energiya (mana) sarflaydi.
3. **Qisman o'tkazuvchanlik:** 100% o'rniga faqat 70% zarbani yutadi, qolgan 30% esa o'yinchiga tegadi.
4. **Qarshi qurol (Counter-play):** Raqiblarda qalqonni bir zarbada sindiruvchi maxsus og'ir qurol bo'lishi lozim.

---

## Tezkor nazorat savollari

1. Game Designer va Game Programmer o'rtasidagi asosiy farq nimada?
   - *Javob:* Designer o'yinning qoidalari, his-tuyg'usi va umumiy tizimini o'ylab topadi; Programmer esa ushbu g'oyalarni dasturiy kodga aylantiradi.
2. O'yin dizaynining qaysi komponenti o'yinchi ekranda ko'radigan menyu va sog'lik panelini o'z ichiga oladi?
   - *Javob:* UI (User Interface).
3. Ochiq kodli va bepul zamonaviy o'yin dvijogi qaysi?
   - *Javob:* Godot Engine.
4. Nima uchun o'yin juda oson bo'lishi xavfli?
   - *Javob:* Oson o'yin o'yinchiga hech qanday qiyinchilik (challenge) taqdim etmaydi va tezda zerikarli bo'lib qoladi.

---

## Uyga vazifa

O'zingiz yoqtirgan bitta mobil yoki kompyuter o'yinini tanlang.
Daftaringizda:
1. O'yin nomi va yaratuvchi studiyasini yozing;
2. Ushbu o'yinda Game Designer qanday asosiy maqsad qo'yganini (o'yinchi nima qilishi kerakligini) 3 ta jumlada tasvirlang;
3. O'yindagi 3 ta ijobiy va 1 ta salbiy dizayn jihatini (kamchiligini) ko'rsating.
