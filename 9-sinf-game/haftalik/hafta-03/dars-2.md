# 8-dars. Ranglar nazariyasi va dizayn asoslari (1-qism): RGB va CMYK, rang g'ildiragi va rang psixologiyasi

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga ranglar nazariyasining fundamental asoslarini — raqamli (RGB) va poligrafik (CMYK) rang modellarini, Yoxannes Ittenning rang g'ildiragini (birlamchi, ikkilamchi, uchlamchi ranglar), asosiy ranglar uyg'unligi sxemalarini (komplementar, analog, triada) hamda o'yin atmosferasini yaratishda rang psixologiyasining ta'sirini o'rgatish.
- **Kutiladigan natija:** O'quvchilar raqamli o'yin grafikasi uchun RGB modelini nima sababdan ishlatish kerakligini tushunadi; rang g'ildiragidan foydalanib o'zaro uyg'un rang palitrasi tuza oladi; o'yin qahramonlari, interfeysi va muhitiga mos emotsional rang psixologiyasini to'g'ri tanlay oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (Assetlar kollaji va qatlamlar): 10 daqiqa
  - Yangi mavzu: RGB vs CMYK, rang g'ildiragi (Itten) va issiq/sovuq ranglar: 25 daqiqa
  - Rang uyg'unliklari (Harmonies) va o'yinda rang psixologiyasi: 25 daqiqa
  - Amaliy topshiriqlar tahlili: 15 daqiqa
  - Dars xulosasi va nazorat savollari: 5 daqiqa

---

## Mentor konspekti

### 1. Raqamli va chop etish modellari: RGB vs CMYK
- **RGB (Red, Green, Blue) — Additiv model:**
  - Yorug'lik nurlarining qo'shilishiga asoslangan.
  - Kompyuter monitorlari, telefon ekranlari, televizorlar va barcha raqamli o'yinlar uchun yagona standart.
  - Barcha 3 rang 100% qo'shilsa — oq rang (White) hosil bo'ladi. Har bir kanal 0 dan 255 gacha qiymatga ega (jami 16.7 million rang).
- **CMYK (Cyan, Magenta, Yellow, Key/Black) — Subtraktiv model:**
  - Bo'yoqlarning yorug'likni yutishiga asoslangan.
  - Bosmaxona, printer va qog'oz mahsulotlari (posterlar, o'yin qutilari) uchun ishlatiladi.
  - Bo'yoqlar qo'shilgan sari qorayadi.
- **Qat'iy qoida:** O'yin dvijoklari (Unity, Unreal, Godot) faqat RGB modelidagi tekstura va spraytlarni qabul qiladi. Agar Photoshopda adashib CMYK ochilsa, o'yin ranglari so'nib, dvijokda xato ko'rsatadi.

### 2. Yoxannes Itten rang g'ildiragi (Color Wheel)
Ranglar 3 ta avlodga bo'linadi:
1. **Asosiy (Primary) ranglar:** Qizil (Red), Sariq (Yellow), Ko'k (Blue) — ularni boshqa ranglarni aralashtirib hosil qilib bo'lmaydi.
2. **Ikkilamchi (Secondary) ranglar:** Asosiy ranglarni 1:1 aralashtirishdan hosil bo'ladi:
   - Qizil + Sariq = To'q sariq (Orange)
   - Sariq + Ko'k = Yashil (Green)
   - Ko'k + Qizil = Binafsha (Purple)
3. **Uchlamchi (Tertiary) ranglar:** Asosiy va qo'shni ikkilamchi rang aralashmasi (Qizil-to'q sariq, Sariq-yashil, Ko'k-binafsha va h.k.).

### 3. Issiq va sovuq ranglar optikasi
- **Issiq ranglar (Qizil, Sariq, Olovrang):**
  - Olov, quyosh va harakat ramzi.
  - Vizual optik qonun: Issiq ranglar tomoshabinga **yaqinroq** ko'rinadi.
  - O'yinda: Qahramon, jangovar qurollar, "Attack" tugmasi, xavf zonasi.
- **Sovuq ranglar (Ko'k, Yashil, Binafsha):**
  - Suv, muz, osmon va xotirjamlik ramzi.
  - Vizual optik qonun: Sovuq ranglar ko'zga **uzoqlashgandek** tuyuladi.
  - O'yinda: Uzoq fon manzaralari, tuman, sirli g'orlar, sehr energiyasi (Mana).

### 4. Ranglar uyg'unligi sxemalari (Color Harmonies)
Professional geym-artistlar ranglarni ko'r-ko'rona emas, matematik formulalar bo'yicha tanlaydilar:
1. **Monoxrom (Monochromatic):** Bitta rangning turli ochlik va to'qlik darajalari (soya va yorug'lik). Juda sokin va nafis.
2. **Komplementar (Complementary):** Rang g'ildiragida bir-biriga qarama-qarshi turgan ikki rang (Qizil va Yashil, Ko'k va To'q sariq). Maksimal kontrast beradi. O'yin qahramonini fondan keskin ajratish uchun eng yaxshi usul.
3. **Analog (Analogous):** G'ildirakda yonma-yon turgan 3 ta rang (masalan, Sariq, Sariq-olovrang, Olovrang). Tabiiy va ko'zga yoqimli muhit yaratadi.
4. **Triadik (Triadic):** Doirada teng tomonli uchburchak hosil qiluvchi 3 rang (Qizil, Sariq, Ko'k). Rang-barang, jonli retro yoki arkada o'yinlari uchun a'lo tanlov.

### 5. O'yin dizaynida rang psixologiyasi
- **Qizil:** Qon, xavf, ehtiros, jang. Salomatlik paneli (HP) kritik darajaga tushganda miltillaydi. Dushmanlar va "Boss" personajlar ko'pincha qizil rangda bo'ladi.
- **Yashil:** Hayot, tabiat, salomatlik, xavfsizlik. To'la HP bar, o'simliklar, "Save" va "Start" tugmalari.
- **Sariq / Oltin:** Boylik, tangalar, quvonch, chaqmoq, ogohlantirish (Warning).
- **Ko'k:** Ishonch, do'stlik, sovuq aql, suv, sehr kuchi (Mana bar).
- **Binafsha:** Sehr, afsun, hashamat, mistika, nodir va afsonaviy o'lja (Epic/Legendary Loot).
- **Oq va Qora:** Oq — poklik, yorug'lik, ilohiy kuch; Qora — qorong'ulik, yovuzlik, dramatizm, o'lim.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Komplementar rang sxemasi bilan qahramonni fondan ajratish (oson)
O'yin zaminida qalin yashil o'tloq va yashil daraxtlar bor. Agar o'yin qahramoni ham yashil kiyimda bo'lsa, u fonda yo'qolib ketadi.
Komplementar kontrast qonuniga binoan, qahramon kiyimining asosiy rangini qanday tanlash kerak va bu qanday natija beradi?

**Yechim:**
1. Itten rang g'ildiragiga qaraladi: Yashil rangning to'g'ridan-to'g'ri qarama-qarshisida (180 daraja) **Qizil (yoki Qizil-olovrang)** joylashgan.
2. Qahramonning kiyimi yoki qalqoni yorqin qizil rangga bo'yaladi.
3. *Natija:* Ko'z to'r pardasi qarama-qarshi to'lqin uzunliklarini bir vaqtda qabul qilganda maksimal kontrast hosil bo'ladi. Qahramon yashil o'rmon fonida darhol yaqqol ko'zga tashlanadi va o'yinchi uni hech qachon yo'qotib qo'ymaydi.

### 2-topshiriq. RPG o'yini uchun 3 xil status panelining rang palitrasi (o'rta)
Siz 2D RPG o'yinining foydalanuvchi interfeysini (HUD) loyihalayapsiz. Unda 3 ta ko'rsatkich bor:
- 1. Salomatlik (Health Points — HP);
- 2. Sehr energiyasi (Mana Points — MP);
- 3. Qahramon charchog'i / chidamliligi (Stamina).
Rang psixologiyasi va o'yin standartlari asosida har bir panel uchun asosiy rang va uning fon kontrastini belgilab bering.

**Yechim:**
1. **Health (HP):** Asosiy rang — **Qizil** (qon va hayot ramzi). To'q qizil zamin ustida yorqin yoqut qizil to'ldiruvchi chiziq.
2. **Mana (MP):** Asosiy rang — **To'q ko'k / Safir** (sehrli aql va ruhiy quvvat ramzi). Qorong'i g'orlarda ham moviy porlab turadi.
3. **Stamina (Chidamlilik):** Asosiy rang — **Yashil yoki Sariq-yashil** (jismoniy quvvat va harakat dinamikasi). Chopganda tez kamayib, turganda yana to'ladi.
4. *Barcha panellarning ramkasi:* Neytral to'q kulrang yoki oltin naqshli qilib ishlanadi, shunda rangli chiziqlar aniq o'qiladi.

### 3-topshiriq. Fantastik kiberpank o'yini uchun Triadik rang sxemasini tuzish (qiyin)
Kelajak shahri bo'ylab kechuvchi kiberpank (Cyberpunk) janridagi o'yin uchun qorong'i neon atmosferasi talab etiladi.
Triada (Triadic) qoidasiga asoslanib, bir-biriga teng masofadagi 3 ta yorqin neon rangdan iborat rang palitrasini aniqlang va har bir rangning sahnadagi vazifasini taqsimlang.

**Yechim:**
1. **Ranglar tanlovi (Neon Triada):**
   - 1. Neon Pushti/Binafsha (Magenta / Neon Pink — taxminan #FF007F);
   - 2. Neon Moviy (Cyan / Electric Blue — taxminan #00F0FF);
   - 3. Neon Sariq (Acid Yellow / Neon Lime — taxminan #FFE600).
2. **Vazifalar taqsimoti:**
   - *Fon va shahar muhiti (60%):* To'q qora-ko'k fon ustida uzoq binolarning deraza va reklamalarida Magenta/Pushti nurlar.
   - *Interfeys va yordamchi obyektlar (30%):* HUD ramkalari, qurollarning lazer nishonlari va xavfsiz zonalar Cyan/Moviy rangda.
   - *Aktsent va diqqat markazi (10%):* Interaktiv eshiklar, portlovchi bochkalar va bosh dushman nishonlari Acid Yellow rangida porlaydi.

---

## Tezkor nazorat savollari

1. Nima sababdan o'yin grafikasini CMYK emas, balki faqat RGB rejimida yaratish shart?
   - *Javob:* Chunki barcha o'yinlar elektron ekranlarda (monitor, telefon) ko'rsatiladi, ekranlar esa additiv yorug'lik nurlari (RGB) bilan ishlaydi. CMYK esa faqat qog'ozga chop etish uchun mo'ljallangan.
2. Qaysi ranglar Yoxannes Itten g'ildiragida asosiy (birlamchi) hisoblanadi?
   - *Javob:* Qizil, Sariq va Ko'k.
3. Rang g'ildiragida bir-biriga 180 gradus qarama-qarshi turgan ranglar juftligi qanday ataladi?
   - *Javob:* Komplementar (to'ldiruvchi) ranglar.
4. O'yinlarda afsonaviy, juda qimmatbaho sehrli qurollar (Legendary loot) an'anaviy ravishda qaysi rang bilan belgilanadi?
   - *Javob:* Binafsha (Purple) yoki Oltin-sariq rang.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Haddan tashqari ko'p to'yingan ranglar ishlatish ("Kislotali dizayn"):** O'quvchilar barcha obyektlarni eng yorqin, 100% to'yingan ranglarga bo'yab yuborishadi. Natijada o'yinchining ko'zi 2 daqiqada charchaydi. 60-30-10 qoidasiga amal qilish kerak: 60% neytral/baza rang, 30% ikkilamchi rang, faqat 10% yorqin aktsent!
- **Rang kontrasti yetishmasligi:** Matn rangi fon rangi bilan bir xil yorqinlikda bo'lsa, o'yinchi matnni o'qiy olmaydi (masalan, qizil zamin ustiga to'q jigarrang yozuv). Har doim yorqinlik (Value) kontrastini tekshirish lozim.
- **Issiq va sovuq ranglar chuqurligini inobatga olmaslik:** Agar uzoqdagi tog'lar qizil-olovrang, oldingi qahramon esa xira ko'k qilib chizilsa, perspektiva buziladi — tog'lar ko'zga yaqinroq ko'rinib qoladi.
