# 7-dars. Axure RP: Dinamik panellar va interaktiv bog'lanishlar (Interactions)

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + dizayn amaliyoti · **I-bob**, 7-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarda Axure RP dasturida statik wireframelarni interaktiv holatga keltirish, dinamik panellar (Dynamic Panels), hodisalar (Events: `OnClick`, `OnMouseEnter`) va sahifalararo o'tishlar (`Open Link`) orqali dastlabki chertiladigan (clickable) prototip yaratish ko'nikmalarini shakllantirish.

**Kutiladigan natija:**
- Statik wireframe va interaktiv prototip o'rtasidagi tafovutni tushunadi.
- Axure RP dagi Dynamic Panel tushunchasini va uning holatlari (States) qanday ishlashini biladi.
- Elementlarga asosiy interaktiv hodisalarni (`OnClick` &rarr; `Open Link` yoki `Set Panel State`) bog'lay oladi.
- Sahifalararo navigatsiyani (masalan, «Kitoblar ro'yxati»dan «Kitob tafsilotlari» sahifasiga o'tish) amalga oshira oladi.
- Foydalanuvchi harakatiga javob qaytaruvchi oddiy tablar (Tabs / Ulashgichlar) yoki ochiluvchi menyu wireframe'ini yasaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 2-hafta xulosasi: Wireframe nima, monoxrom dizayn va Axure RP interfeysi. Muammoli savol: «Mijoz yoki dasturchiga tugma bosilganda sahifada nima o'zgarishini ko'rsatish uchun faqat rasm yetarlimi?» |
| 10–30 daq | Yangi mavzu: Nazariya | Interaktiv prototiplash asoslari, Axure RP Interactions paneli, Dynamic Panel va uning State'lari, hodisa turlari (`OnClick`, `OnHover`) |
| 30–35 daq | Tanaffus | Harakatli tanaffus |
| 35–65 daq | Amaliy mashg'ulot | «E-kutubxona» loyihasida sahifalararo o'tish (`Home_books` &rarr; `Book_details`) va Dynamic Panel orqali 2 ta tab (Tavsif / Fikrlar) yaratish |
| 65–75 daq | Tezkor nazorat | 5 ta savol-javob va o'quvchilar prototiplarini tekshirish |
| 75–80 daq | Xulosa va uyga vazifa | Asosiy xulosalar va uy vazifasini tushuntirish |

---

## 2. Dars konspekti

### 2.1. Wireframeni jonlantirish: Interaktiv prototiplash

Statik wireframe — bu rasm yoki chizma. U sahifada qanday bloklar bo'lishini ko'rsatadi, ammo:
- Tugma bosilganda nima sodir bo'ladi?
- Yangi ma'lumot qanday ochiladi?
- Foydalanuvchi xato qilsa nima ko'rinadi?

Bu savollarga javob berish uchun **Interaktiv Wireframe (Clickable prototype)** yaratiladi. Axure RP aynan mana shu imkoniyati bilan Figma yoki Balsamiq'dan ajralib turadi: unda murakkab mantiqiy shartlar va o'zgaruvchilarni dasturlashsiz (No-code) yaratish mumkin.

### 2.2. Axure RP da Interactions paneli tuzilishi

Interaktivlik 3 ta tarkibiy qismdan iborat bo'ladi:
1. **Trigger (Hodisa / Event):** Foydalanuvchi nima qildi?
   - `OnClick` — sichqoncha bilan bosilganda;
   - `OnMouseEnter` / `OnMouseOut` — kursor element ustiga kelganda yoki ketganda (Hover);
   - `OnKeyUp` — klaviaturada tugma bosilganda.
2. **Action (Harakat):** Tizim nima qilishi kerak?
   - `Open Link` — boshqa sahifani ochish;
   - `Show / Hide` — elementni ko'rsatish yoki yashirish;
   - `Set Panel State` — dinamik panel holatini o'zgartirish;
   - `Scroll to Widget` — sahifani ma'lum qismga siljitish.
3. **Target (Nishon):** Bu harakat qaysi elementga ta'sir qiladi?

```
+-----------------------------------------------------------+
| [Foydalanuvchi amali]  -->  OnClick                       |
| [Bajariladigan amal]   -->  Open Link                     |
| [Natija / Nishon]      -->  Book_details.html             |
+-----------------------------------------------------------+
```

### 2.3. Dinamik panellar (Dynamic Panels)

**Dynamic Panel** — bu Axure RP ning eng qudratli vositasi bo'lib, bitta konteyner ichida bir nechta turli holatlarni (**States**) saqlash imkonini beradi.

Qayerda ishlatiladi?
- **Tablar (Vkladkalar):** Foydalanuvchi «Tavsif» yoki «Sharhlar» tugmasini bosganda, butun sahifani qayta yuklamasdan faqat shu blokning holati (State 1 &rarr; State 2) o'zgaradi.
- **Modal oynalar (Popup):** «Kirish» tugmasi bosilganda ekranda paydo bo'luvchi qorong'ilashgan oyna.
- **Slayderlar (Karusel):** Rasmlar chapga va o'ngga surilishi.

Dinamik panel yaratish bosqichlari:
1. Kerakli elementlarni tanlab, o'ng tugmani bosish &rarr; **Create Dynamic Panel**.
2. Outline / Panel States oynasida `State 1` va `State 2` holatlarini qo'shish.
3. Har bir State ichiga mos wireframe bloklarini chizish.
4. Tugmaga `OnClick` &rarr; `Set Panel State` buyrug'ini biriktirish.

---

## 3. Amaliy mashg'ulot

### 1-mashq. Sahifalararo o'tishni sozlash
**Vazifa:** «Online books» loyihasida `Home_books` sahifasidagi kitob kartasiga bosilganda `Book_details` sahifasini ochadigan interaktiv bog'lanish yarating.

**Yechim:**
1. Axure RP Pages panelida ikkita sahifa ochiladi: `Home_books` va `Book_details`.
2. `Home_books` sahifasida kitob kartasi (Rectangle va Text) tanlanadi.
3. O'ng tarafdagi **Interactions** panelida `New Interaction` tugmasi bosiladi.
4. Ro'yxatdan `Click or Tap` tanlanadi.
5. Harakat sifatida `Open Link` &rarr; `Link to a page in this project` tanlanib, ro'yxatdan `Book_details` belgilanadi.
6. Yuqori paneldagi **Preview** (`Ctrl + F5` yoki brauzer belgisi) bosilib, brauzerda sinab ko'riladi.

---

### 2-mashq. Kitob tafsilotida 2 ta Tab (Dynamic Panel) yasash
**Vazifa:** Kitob sahifasida «Mundarija» va «O'quvchilar fikri» bo'limlarini bitta dinamik panel ichida almashtirishni loyihalang.

**Yechim:**
1. Maydonga to'rtburchak chizilib, o'ng tugma orqali `Create Dynamic Panel` qilinadi. Unga `Book_Tabs_Panel` nomi beriladi.
2. Panel ichiga kirib (ikki marta bosish), ikkita State yaratiladi: `State_Mundarija` va `State_Fikrlar`.
3. `State_Mundarija` ichiga 1–5 boblar ro'yxati matni, `State_Fikrlar` ichiga esa 2 ta sharh bloki qo'yiladi.
4. Panel tepasiga ikkita tugma qo'yiladi: «Mundarija» va «Fikrlar».
5. «Mundarija» tugmasiga: `OnClick` &rarr; `Set Panel State` &rarr; `Book_Tabs_Panel` &rarr; `State_Mundarija`.
6. «Fikrlar» tugmasiga: `OnClick` &rarr; `Set Panel State` &rarr; `Book_Tabs_Panel` &rarr; `State_Fikrlar`.
7. Preview rejimida tekshiriladi: tugmalar bosilganda kontent silliq almashadi.

---

## 4. Tezkor savollar (Checklist)

1. Wireframeni nima uchun interaktiv holatga keltirish kerak?
   - **Javob:** Dizaynning amalda qanday ishlashini, navigatsiya qulayligini va foydalanuvchi harakatlarini dasturlash boshlanishidan oldin real sinab ko'rish uchun.
2. Axure RP da interaktivlikning 3 ta tayanchi qaysilar?
   - **Javob:** Trigger (hodisa), Action (harakat) va Target (nishon obyekti).
3. Dynamic Panel nima va u qanday elementlar uchun zarur?
   - **Javob:** Bitta konteyner ichida bir nechta holatlarni (states) saqlash vositasi. Tablar, ochiluvchi menyular va modal oynalar uchun ishlatiladi.
4. Sahifalararo o'tish qaysi Action yordamida amalga oshiriladi?
   - **Javob:** `Open Link` buyrug'i yordamida loyiha ichidagi boshqa sahifaga yo'naltiriladi.
5. Axure RP prototipini qanday rejimda tekshirish mumkin?
   - **Javob:** **Preview** tugmasi orqali mahalliy brauzerda haqiqiy veb-sayt kabi ochib ko'riladi.
