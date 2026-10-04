# 6-dars. Balsamiq va Axure RP: asosiy UI komponentlar va dastlabki interfeys sxemalari

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 6-dars

## 1. Dars rejasi

**Maqsad:** o'quvchi Balsamiq va Axure RP dasturlarining imkoniyatlarini taqqoslay oladi, Axure RP ning asosiy ishchi panellari bilan tanishadi, sahifalarni to'g'ri nomlashni, to'rtburchaklar (Rectangle) va matnlar yordamida interfeys bloklarini tuzishni hamda tayyor wireframe'ni PNG/SVG formatida eksport qilib, Figmaga o'tkazishga tayyorlashni o'rganadi.

**Kutiladigan natija:**
- Axure RP va Balsamiq vositalarining vazifalari va farqlarini ajrata oladi.
- Axure RP ish maydonida (Canvas, Pages, Widgets Library, Interactions) yo'nalish oladi.
- Sahifalarni mantiqiy nomlash (`Home_books`, `Book_details`) tamoyillarini biladi.
- Kulrang tuslar palitrasi (Grayscale) yordamida elementlar ierarxiyasini vizual ajratadi.
- 1 ta to'liq veb yoki mobil ilova wireframe sxemasini tuzadi va uni rasm (PNG) ko'rinishida saqlaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 5-dars (Wireframe tushunchasi, Low-fi, Balsamiq asoslari) |
| 10–30 | Yangi mavzu 1 | Axure RP dasturi: professional prototiplash va Balsamiq bilan taqqoslash |
| 30–40 | Yangi mavzu 2 | Axure RP interfeysi: Pages, Default Widgets, Rectangle va Matn |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | Kulranglar ierarxiyasi, eksport (PNG/SVG) va Figmaga tayyorlash |
| 55–75 | Amaliyot | "Home_books" sahifasi to'liq wireframe sxemasini yasash |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, 2-hafta yakuni |

**Vositalar:** Axure RP (bepul trial) yoki Balsamiq / Figma (oq-qora rejimda).

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- Low-fidelity wireframe nima uchun kerak?
- Balsamiq'da "X" bilan chizilgan to'rtburchak nimani bildiradi?

### 2.2. Axure RP nima va u Balsamiqdan nimasi bilan farq qiladi?
**Axure RP** — UI/UX dizayn sohasida murakkab interfeyslar, wireframelar va yuqori darajada interaktiv prototiplar yaratish uchun mo'ljallangan qudratli professional dasturdir.

| Xususiyat | Balsamiq | Axure RP |
|---|---|---|
| **Asosiy uslub** | Qalamaki, daftardagi eskiz (sketch) | Geometrik toza, professional karkas |
| **Maqsad** | Dastlabki tezkor g'oyalar (5-10 daqiqa) | To'liq va batafsil interfeys sxemalari |
| **Mantiq va shartlar** | Faqat oddiy havolalar | Murakkab o'zgaruvchilar, formulalar, shartli o'tishlar |
| **Murakkablik** | Juda sodda, o'rganish 1 kun | Professional, ko'proq vositalarga ega |

### 2.3. Axure RP ning asosiy panellari
1. **Pages (Sahifalar paneli):** Loyihaning barcha sahifalari daraxtsimon (tree structure) ko'rinishida saqlanadi. Sahifalarni tartibli nomlash shart: masalan, `Home_books`, `Search_results`, `Profile`.
2. **Canvas (Ish maydoni):** Markaziy hudud, pikselli setka (grid) bilan jihozlangan.
3. **Libraries / Default Widgets (Komponentlar kutubxonasi):**
   - *Rectangle (To'rtburchak):* Har qanday banner, karta, sarlavha qutisi uchun asosiy g'isht.
   - *Text (Matn):* Sarlavha (Heading) va tavsiflar.
   - *Droplist, Checkbox, Radio:* Formalar uchun vidjetlar.
4. **Interactions paneli:** Tanlangan element bosilganda qayerga o'tish, animatsiya va dinamik holatlarni boshqaradi.

### 2.4. Kulranglar ierarxiyasi (Grayscale Hierarchy)
Wireframe'da rang ishlatilmaydi, ammo bu barcha bloklar bir xil bo'ladi degani emas! Dizaynerlar bir xil rang o'rniga **kulrangning 3–4 xil tusini** ishlatishadi:
- **To'q kulrang (#334155):** Asosiy sarlavhalar va eng muhim tugmalar uchun.
- **O'rta kulrang (#94a3b8):** Ikkilamchi matnlar va chegaralar (border) uchun.
- **Och kulrang (#f1f5f9):** Fon bloklari, bannerlar va kartalar asosi uchun.
- **Oq (#ffffff):** Sahifaning asosiy foni yoki kartalar ichi uchun.

Bu usul ko'zga qaysi element eng muhim ekanini rangsiz ham bir qarashda ko'rsatib beradi.

### 2.5. Eksport va Figmaga ko'chirish
Wireframe tayyor bo'lgach:
1. `File → Export to Image` (PNG yoki SVG formatida).
2. Keyingi bosqichda ushbu PNG rasm **Figma** dasturiga yuklanadi (drag-and-drop orqali).
3. Wireframe rasm sifatida fonga qulflanadi (Lock) va uning ustiga haqiqiy ranglar, shriftlar hamda piktogrammalar chizilib, chiroyli **UI dizayn** shakllantiriladi!

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. "Home_books" veb-sahifasi wireframe'i
Axure RP (yoki Balsamiq/Figma)da quyidagi bloklardan iborat veb-sahifa maketini tuzing:
1. Sahifa nomi: `Home_books`;
2. Yuqori qism (Header): Logo uchun to'rtburchak va 4 ta matnli menyu havolasi;
3. Katta banner (Rectangle): Sarlavha matni va o'ng tomonida kitob rasmi o'rni ([X]);
4. "Tavsiya etilgan kitoblar" bo'limi: 3 ta bir xil to'rtburchak kartalar (Grid).

**Yechim:**
- Header balandligi 70px, och kulrang fon;
- Banner balandligi 250px, ichida qalin sarlavha va "Batafsil" tugmasi;
- 3 ta karta orasidagi masofa (gap) 24px teng taqsimlangan.

### 2-topshiriq. Axure RP da interaktiv bog'lanish (Link)
`Home_books` sahifasidagi kitob kartasini bosganda yangi yaratilgan `Book_details` sahifasiga o'tuvchi oddiy interaktiv hodisa (Click → Open Page) yarating.

**Yechim:**
Kartani tanlash → O'ng tarafdagi `Interactions` panelida `Click or Tap` ni bosish → `Open Link` → `Book_details` sahifasini tanlash.

### 3-topshiriq. Wireframeni PNG ga eksport qilish
Yaratilgan wireframeni kompyuterga `home_books_wireframe.png` nomi bilan saqlang.

**Yechim:**
Menyudan `Publish → Export Pages to Images` orqali saqlangan toza tasvir fayli.

---

## 4. Tezkor nazorat (5 daqiqa)

1. Axure RP dasturi nima uchun kerak va uning Balsamiqdan ustunligi nimada?
   - **Javob:** Axure RP geometrik toza wireframelar va murakkab mantiqiy interaktiv prototiplar yaratish imkonini beradi.
2. Sahifalarni `Home_books` kabi tartibli nomlash nima uchun muhim?
   - **Javob:** Loyihada navigatsiyani osonlashtirish va jamoa a'zolari bir-birini tushunishi uchun.
3. Kulranglar ierarxiyasi (Grayscale) nima maqsadda qo'llaniladi?
   - **Javob:** Ranglarsiz ham qaysi blok va matn muhimroq ekanini vizual ko'rsatish uchun.
4. Wireframe'da Rectangle (To'rtburchak) vositasi qanday vazifalarni bajaradi?
   - **Javob:** Bannerlar, kartalar, tugmalar va fon bloklarining asosiy qurilish g'ishti sifatida.
5. Yaratilgan wireframe keyingi bosqichda Figmaga qanday ko'chiriladi?
   - **Javob:** PNG yoki SVG sifatida eksport qilinib, Figmaga fon rasmi (reference) qilib yuklanadi.

---

## 5. Xulosa va keyingi darsga ko'prik
2-hafta davomida biz foydalanuvchi ssenariylaridan boshlab, User Flow va Balsamiq/Axure RP vositalarida to'liq interfeys wireframe'ini yaratishni o'rgandik!
**Keyingi hafta (3-hafta, 7–9 darslar):** Axure RP va Balsamiqda wireframe yaratish amaliyotini davom ettiramiz, murakkab komponentlar va interaktiv prototiplash sirlarini chuqur o'rganamiz!
