# 3-dars. UI va UX ning Game designdagi roli: Interfeys tiplari va HUD arxitekturasi

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga video o'yinlarda foydalanuvchi interfeysi (UI) va foydalanuvchi tajribasi (UX) tushunchalari, ularning o'zaro farqi va uyg'unligi, o'yin interfeysining 4 ta asosiy tipi (Diyegetik, Nodiyegetik, Fazoviy va Meta-interfeys) hamda o'yin ichidagi doimiy axborot displeyi — HUD (Heads-Up Display) elementlarini loyihalashni o'rgatish.
- **Kutiladigan natija:** O'quvchilar UI va UX farqini aniq ajrata oladi; har qanday o'yindagi interfeys elementlarini 4 tip bo'yicha toifalashni o'rganadi; o'yinchini chalg'itmaydigan, qulay va immersiv HUD interfeysini loyihalay oladi.
- **Vaqt taqsimoti:**
  - O'tgan mavzuni takrorlash (O'yinlar tarixi va janrlar): 10 daqiqa
  - Yangi mavzu: UI va UX tushunchalari hamda ularning o'zaro bog'liqligi: 20 daqiqa
  - 4 ta interfeys tipi: Diyegetik, Nodiyegetik, Fazoviy va Meta: 25 daqiqa
  - HUD elementlari va qulaylik (UX) mezonlari: 15 daqiqa
  - Tezkor savollar va dars xulosasi: 10 daqiqa

---

## Mentor konspekti

### 1. UI va UX nima? Ular o'yinda qanday o'zaro ta'sirlashadi?
- **UI (User Interface — Foydalanuvchi interfeysi):** O'yinchi ekranda ko'radigan barcha vizual elementlar to'plami. Tugmalar, menyular, shriftlar, piktogrammalar, ranglar sxemasi va animatsiyalar.
  - *Savol:* "O'yin qanday ko'rinadi?"
- **UX (User Experience — Foydalanuvchi tajribasi):** O'yinchining o'yin bilan muloqot qilganda oladigan umumiy hissiyoti, qulayligi, boshqaruvning silliqligi va tushunarliligi.
  - *Savol:* "O'yin qanday his qilinadi?"
- **UI va UX uyg'unligi:**
  - UX dizayner foydalanuvchi harakat oqimini (qaysi tugmadan keyin qaysi oyna ochilishini) loyihalaydi;
  - UI dizayner bu tuzilmaga go'zal vizual libos kiydiradi (ranglar, ikonalar, shriftlar);
  - Agar UI chiroyli bo'lib, lekin tugmalar noqulay joylashgan bo'lsa $\to$ o'yinchi asabiylashadi va o'yindan chiqib ketadi (yomon UX).

### 2. O'yin interfeysining 4 ta asosiy tipi
Game Design nazariyasida interfeys elementlari o'yin olamiga (Fiction) va fazoga (Space) nisbatan 4 turga bo'linadi:
1. **Diyegetik interfeys (Diegetic UI):**
   - O'yin olamining ichki qismi hisoblanadi. Uni ham o'yinchi, ham o'yin ichidagi bosh qahramon ko'ra oladi!
   - *Misollar:* *Dead Space* o'yinida Ayzek skafandri umurtqasidagi salomatlik indikatori; *Metro 2033*dagi qo'l soati va gazoblok filtr taymeri; *Far Cry 2* yoki *GTA V*da qahramon qo'lidagi haqiqiy xarita va smartfon.
   - *Afzalligi:* O'yin olamiga to'liq sho'ng'ish (Immersion) hissini beradi.
2. **Nodiyegetik interfeys (Non-Diegetic UI):**
   - O'yin olamidan tashqarida bo'lib, to'g'ridan-to'g'ri ekran ustiga qo'yiladi. O'yin ichidagi personajlar bu ma'lumotni ko'rmaydi.
   - *Misollar:* Ekranning burchagidagi qizil sog'lik chizig'i, o'q-dorilar soni hisoblagichi, *Super Mario*dagi tangalar va vaqt taymeri.
   - *Afzalligi:* Bajarish juda oson, barcha kerakli ma'lumotlarni o'yinchiga aniq va tezkor yetkazadi.
3. **Fazoviy interfeys (Spatial UI):**
   - 3D o'yin fazosiga joylashtiriladi, lekin virtual personajlar undan bexabar bo'ladi.
   - *Misollar:* MMORPG (*World of Warcraft*) o'yinlarida personajlar va dushmanlar boshi ustidagi ism taxtachalari; yo'l ko'rsatuvchi 3D strelkalar; nishonga olish doiralari.
   - *Afzalligi:* Ekranni to'ldirmasdan, kerakli obyektning aynan o'ziga ma'lumot bog'lash.
4. **Meta-interfeys (Meta UI):**
   - O'yin voqeligining bir qismi emas, lekin qahramonning jismoniy holatini o'yinchiga his qildiruvchi vizual/audio effektlar.
   - *Misollar:* O'yinchi yaralanganda ekranning qizarishi yoki chetlariga qon sachrashi; suv ostiga tushganda ekranda paydo bo'ladigan pufakchalar; zarba tekkanda geympadning tebranishi (rumble).

### 3. HUD (Heads-Up Display) arxitekturasi
HUD — bu o'yin jarayonida ekranda doimiy yoki vaqtincha ko'rinib turuvchi barcha axborot panellari majmuasidir.
- **Asosiy elementlari:**
  1. *Health / Mana Bar:* Qahramonning hayotiy quvvati.
  2. *Mini-map (Mini xarita):* Hudud va nishonlar yo'nalishi.
  3. *Ammo counter (O'q-dorilar):* Qurol zaxirasi.
  4. *Score / Currency:* Yig'ilgan tangalar yoki ochkolar.
- **HUD dizaynining oltin qoidalari:**
  - *Ekranni to'ldirib yubormaslik:* O'yin jarayoni markazda bo'lishi kerak.
  - *Kontrast va o'qilishi oson shrift:* Har qanday fon (qor, o'rmon, qorong'u xona)da ham ma'lumot aniq ko'rinsin.
  - *Dinamik yashirinish (Contextual HUD):* Jang bo'lmaganda sog'lik panelining avtomatik yo'qolishi.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Interfeys elementlarini toifalash (oson)
Quyidagi 4 ta interfeys elementini 4 ta tipga (Diyegetik, Nodiyegetik, Fazoviy, Meta) ajrating:
1. Qahramon avtomobil minib ketayotganda torpedadagi haqiqiy spidometr ko'rsatkichi;
2. Ekranning yuqori chap burchagidagi qizil yurakchalar (jon soni);
3. Dushmanning boshi ustida aylanib turgan "sariq yulduzchalar" (gangiganlik belgisi);
4. Qahramon qahraton sovuqda qolganda ekranning muzlab borishi.

**Yechim:**
1. Torpedadagi spidometr $\to$ **Diyegetik** (o'yin olami va qahramon ko'radi);
2. Burchakdagi yurakchalar $\to$ **Nodiyegetik** (faqat o'yinchi ko'radi);
3. Bosh ustidagi yulduzchalar $\to$ **Fazoviy (Spatial)** (3D fazoda joylashgan);
4. Ekranning muzlashi $\to$ **Meta-interfeys** (qahramon hissini ekranda aks ettiradi).

### 2-topshiriq. UI/UX muammosini aniqlash va tuzatish (o'rta)
O'yinda o'yinchi dushman bilan jang qilayotganda uning o'q-dorilari tugab qoladi. Ekranning pastki o'ng burchagida juda kichik kulrang shrift bilan "Ammo: 0" yozilgan bo'lsa-da, o'yinchi jang paytida buni sezmaydi va nima uchun qurol otmayotganini tushunmay vafot etadi.
Ushbu vaziyatda UI va UX jihatdan qanday yechimlar qo'llash kerak?

**Yechim:**
- **UI yechimi:** O'q tugaganda nishon yonida yoki ekranning o'rtasida qizil ogohlantiruvchi belgi chiqarish yoki qurol indikatorini miltillovchi qizil rangga aylantirish.
- **UX va Audio yechimi:** Bo'sh zatvorning xos quruq "chertilish" (click) ovozini chiqarish, qahramonning "Reload!" deb qichqirishi yoki geympadning qisqa titrashi. Shunda o'yinchi ekranning burchagiga qaramasdan ham muammoni intuitiv tushunadi.

### 3-topshiriq. Mobil o'yin uchun minimalist HUD loyihalash (qiyin)
Mobil telefonlar ekrani kichik bo'lgani sababli barcha ma'lumotlarni chiqarish ekranni to'ldirib yuboradi.
O'rmonda omon qolish (Survival) janridagi mobil o'yin uchun qanday minimalistik va qulay HUD tizimini taklif qilasiz?

**Yechim:**
1. **Dinamik HUD:** Doimiy barcha ko'rsatkichlarni ko'rsatmaslik. O'yinchi xavfsiz holatda yurganda barcha panellar yashirinadi (to'liq toza ekran).
2. **Diyegetik belgilar:** Qahramonning charchog'i ekranda og'ir nafas olish ovozi bilan beriladi; qorong'ulik esa qo'lidagi mash'alaning tutashi bilan o'lchanadi.
3. **Qalqib chiquvchi piktogrammalar:** Ochlik yoki chanqoqlik kritik darajaga yetgandagina ekranning chetida kichik piktogramma paydo bo'ladi.
4. **Boshqaruv:** Ekranda ortiqcha vizual joystik chizmasdan, ekranning chap yarmini erkin siljitish orqali boshqaruvga moslash.

---

## Tezkor nazorat savollari

1. Qaysi interfeys turini ham o'yinchi, ham o'yin qahramoni birdek ko'ra oladi?
   - *Javob:* Diyegetik interfeys.
2. HUD qisqartmasi nimani anglatadi?
   - *Javob:* Heads-Up Display (Boshni ko'targan holda ko'rinuvchi axborot paneli).
3. Zarba yeganda ekranning qon sachrab qizarishi qaysi interfeys turiga kiradi?
   - *Javob:* Meta-interfeys.
4. UI va UX o'rtasidagi asosiy farq nimada?
   - *Javob:* UI — tashqi ko'rinish va elementlar, UX — boshqaruv qulayligi va umumiy tajriba.

---

## Uyga vazifa

O'zingiz eng ko'p o'ynaydigan bitta o'yinni tanlang:
1. Undagi HUD elementlarining to'liq ro'yxatini yozing (Health bar, xarita, qurol va h.k.);
2. O'yindan 4 ta interfeys turiga (Diyegetik, Nodiyegetik, Fazoviy, Meta) mos keluvchi 1 tadan aniq element topib yozing;
3. Ushbu o'yinda o'zingizga yoqmagan 1 ta noqulay interfeys jihatini tanqid qiling va qanday yaxshilash mumkinligini ayting.
