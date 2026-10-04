# 8-dars: Grid tizimlari va kompozitsiya

**Fan:** Advanced UX/UI dizayn va Advanced Front-end  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta, 2-dars (umumiy 8-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga raqamli interfeyslar yaratishda **Grid (panjara) tizimlari** va kompozitsiya qoidalarini o'rgatish; 6 ta asosiy grid turini (Baseline, Column, Modular, Manuscript, Pixel, Hierarchical) tushuntirish; zamonaviy veb va mobil dizaynda 12 ustunli responsiv grid (Columns, Gutter, Margin) qanday ishlashini amalda ko'rsatish; sanoat standarti bo'lgan **8pt spacing (panjara) tizimi** orqali mukammal vizual tartib va proporsiyalarni shakllantirish ko'nikmalarini rivojlantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Grid tizimining nima ekanini va nega u ijodkorlikni cheklamay, balki tartib va samaradorlik berishini tushunish;
- 6 ta asosiy grid turini ajrata olish va ularning qo'llanish sohalarini bilish;
- Column grid anatomiyasini (Columns, Gutters, Margins) to'liq tushunish;
- Nega elementlar ustun ichida boshlanib tugashi kerakligi va Gutter (ustunlar oralig'i)ga element qo'yish taqiqlanishini bilish;
- 8pt grid tizimi qoidalarini (4px, 8px, 16px, 24px, 32px, 48px) amaliy loyihalarda qo'llay olish;
- Desktop (12 ustun), planshet (8 ustun) va mobil (4 ustun) responsiv o'tish qoidalarini bilish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Veb-brauzer, Figma yoki FigJam dasturlari;
- Chizg'ich va katak daftar (boshlang'ich tushunchalar uchun);
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Ranglar psixologiyasi, 60-30-10 qoidasi va tipografik iyerarxiya bo'yicha savol-javob |
| **10–25 min** | Yangi mavzu: Grid nima va nega muhim? | Panjara tizimi tarixi, ijodiy cheklovlar kuchi, vizual tartib |
| **25–45 min** | 6 ta asosiy grid turi | Baseline, Column, Modular, Manuscript, Pixel va Hierarchical gridlar |
| **45–60 min** | 12 ustunli responsiv grid va 8pt tizimi | Columns, Gutter, Margin, 8pt spacing qoidasi (4, 8, 16, 24, 32, 48px) |
| **60–75 min** | Amaliy mashg'ulot | Figmada 12 ustunli desktop va 4 ustunli mobil grid sozlab, mahsulot kartochkalarini tekislash |
| **75–80 min** | Xulosa va darsni yakunlash | Asosiy qoidalarni mustahkamlash, tezkor savollar |

---

## Nazariy ma'lumotlar

### 1. Grid (panjara) tizimi nima?

**Grid tizimi:** Dizayndagi barcha elementlarni (matn, rasm, tugma, kartochka) gorizontal va vertikal chiziqlar bo'yicha tartibga soluvchi ko'rinmas skelet yoki strukturadir.

**Nega grid kerak?**
- Bo'sh oq sahifa dizaynerda noaniqlik uyg'otadi. Grid tizimi dizaynerga qat'iy boshlang'ich qoidalar va ramka beradi;
- Dasturlashga (Frontend) o'tkazishni yengillashtiradi (Bootstrap, Tailwind, CSS Grid, Flexbox tizimlari to'liq gridga tayanadi);
- Turli qurilmalarda (Desktop -> Planshet -> Mobil) elementlarning buzilmasdan moslashuvchan (responsiv) joylashishini ta'minlaydi.

### 2. 6 turdagi grid tizimlari (Rasmiy darslik bo'yicha)

1. **Baseline Grid (Asosiy satr panjarasi):** Teng masofadagi gorizontal chiziqlar (maktabdagi katak yoki chiziqli daftar kabi). Matnlarning pastki chizig'ini bir xil tekislikda ushlab turadi.
2. **Column Grid (Kolonka panjarasi):** Sahifa bir nechta vertikal ustunlarga bo'linadi. Raqamli interfeyslarda eng ko'p ishlatiladigan tur.
3. **Modular Grid (Modul panjarasi):** Ustunlar va gorizontal qatorlar kesishuvidan hosil bo'lgan kataklar (modullar). Murakkab jurnallar va analitika panellari (dashboards) uchun ishlatiladi.
4. **Manuscript Grid (Qo'lyozma panjarasi):** Bir ustunli katta blok. An'anaviy kitoblar va o'qish bloglari uchun asosiy maket.
5. **Pixel Grid (Pikselli panjara):** Ekranni maksimal kattalashtirganda ko'rinadigan har bir piksel to'ri. Ikonka va piktogramma chizishda aniqlikni beradi.
6. **Hierarchical Grid (Iyerarxik panjara):** Qat'iy ustunlarga bo'ysunmaydigan, lekin kontentning o'ziga xos ehtiyojidan kelib chiqib joylashadigan zamonaviy moslashuvchan panjara.

### 3. Column Grid anatomiyasi va 8pt tizimi

**Asosiy qismlar:**
- **Columns (Ustunlar):** Kontent joylashtiriladigan vertikal zonalar. Standart bo'yicha:
  - Desktop: **12 ustun**;
  - Planshet: **8 ustun**;
  - Mobil: **4 ustun** (yoki 3 ustun).
- **Gutter (Oraliq bo'shliq):** Ustunlar orasidagi masofa (odatda 16px yoki 24px).
  *Qat'iy qoida:* Elementlar ustun ichida boshlanib, ustun ichida tugashi shart. Gutter ustiga hech qanday element joylashtirilmaydi!
- **Margin (Xavfsiz chetlar):** Ekranning chap va o'ng qirrasidagi bo'shliq (Desktopda 80–120px, Mobilda 16–20px).

**8pt (Pixel) Spacing Tizimi:**
Interfeysdagi barcha o'lchamlar va masofalar 8 ga karrali sonlarda belgilanadi:
$$4\text{px} \rightarrow 8\text{px} \rightarrow 16\text{px} \rightarrow 24\text{px} \rightarrow 32\text{px} \rightarrow 48\text{px} \rightarrow 64\text{px}$$
- Retina ekranlarda to'liq piksel aniqligini (sub-pixel rendering muammosisiz) ta'minlaydi;
- Dizayner har safar "Bu tugmani 13px sursammi yoki 17px?" deb ikkilanib vaqt yo'qotmaydi.

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. 12 ustunli gridda bloklarni taqsimlash (oson)
12 ustunli Desktop gridda quyidagi layout variantlari uchun har bir blok nechtadan ustunni egallashini hisoblang:
1. 3 ta teng o'lchamli xizmatlar kartochkasi;
2. 4 ta teng o'lchamli tovar kartochkasi;
3. Asosiy maqola (katta) va uning yonidagi qo'shimcha yangiliklar paneli (kichik sidebar).

**Yechim:**
1. 3 ta teng blok: $12 / 3 = 4$ ustundan (har bir kartochka 4 ustun kenglikda);
2. 4 ta teng blok: $12 / 4 = 3$ ustundan (har bir tovar 3 ustun kenglikda);
3. Maqola va sidebar: Maqola 8 ustun, Yon panel (sidebar) 4 ustun ($8 + 4 = 12$).

### 2-topshiriq. 8pt tizimi bo'yicha masofalarni to'g'rilash (o'rta)
Yangi boshlagan dizayner kartochka ichidagi elementlar uchun quyidagi noaniq oraliqlarni qo'ygan:
- Kartochkaning ichki chetlari (padding): `13px`;
- Rasm va sarlavha orasidagi masofa: `7px`;
- Sarlavha va matn orasidagi masofa: `11px`;
- Matn va "Batafsil" tugmasi orasidagi masofa: `19px`.  
Ushbu oraliqlarni sanoat standarti bo'lgan **8pt tizimi**ga to'liq moslab qayta yozing.

**Yechim:**
- Ichki padding: `13px` -> `16px` (yoki keng kartochkalar uchun `24px`);
- Rasm va sarlavha orasi: `7px` -> `8px`;
- Sarlavha va matn orasi: `11px` -> `8px` (yoki `16px`);
- Matn va tugma orasi: `19px` -> `24px` (yoki `16px`).

### 3-topshiriq. Responsiv o'tish (Desktop -> Tablet -> Mobile) arxitekturasini loyihalash (qiyin)
Onlayn do'konning "Ommabop tovarlar" bo'limida jami 4 ta tovar mavjud.
Ushbu 4 ta tovarni quyidagi qurilmalar uchun grid bo'yicha qanday joylashtirishni chizma yoki jadval tarzida loyihalashtiring:
1. Desktop (12 ustunli grid): Nechta qatorda, har bir tovar necha ustun egallaydi?
2. Tablet / Planshet (8 ustunli grid): Nechta qatorda, har bir tovar necha ustun egallaydi?
3. Mobile / Smartfon (4 ustunli grid): Tovarlar qanday joylashadi?

**Yechim:**
1. **Desktop (12 ustun):** Barcha 4 ta tovar 1 qatorda yonma-yon joylashadi. Har bir tovar 3 ustun kenglikda bo'ladi ($4 \times 3 = 12$).
2. **Tablet (8 ustun):** Tovarlar 2 qatorga bo'linadi (har qatorda 2 tadan). Har bir tovar 4 ustun kenglikda bo'ladi ($2 \times 4 = 8$).
3. **Mobile (4 ustun):**
   - Variant A (Vertikal ro'yxat): Har bir tovar 4 ustun (to'liq ekran eni) bo'lib, 4 ta qatorda pastma-past joylashadi;
   - Variant B (Gorizontal skroll): Tovarlar yonma-yon gorizontal siljiydigan karusel (slider) holatiga keltiriladi.

---

## Tezkor nazorat savollari

1. Grid tizimi dizaynerning ijodkorligini cheklaydimi?
   - *Javob:* Yo'q, ijodiy cheklovlar boshlang'ich ramka va tartib beradi, tartibsizlikdan asraydi hamda dasturlashni osonlashtiradi.
2. Gutter nima va nima uchun unga element joylashtirilmaydi?
   - *Javob:* Gutter — ustunlar orasidagi ajratuvchi bo'shliq. U elementlarni bir-biriga yopishib ketishdan saqlash uchun xizmat qiladi, shuning uchun uning ustiga kontent qo'yilmaydi.
3. Desktop, planshet va mobil ekranlar uchun standart ustunlar soni nechta?
   - *Javob:* Desktop — 12 ustun, Planshet — 8 ustun, Mobil — 4 ustun.
4. 8pt grid tizimining asosiy afzalligi nima?
   - *Javob:* O'lchamlar va bo'shliqlarning bir xil proporsional bo'lishi, Retina ekranlarda piksellar xiralashmasligi va dizayn tezligini oshirishi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Elementlarni ustun chegarasidan tashqariga chiqarib yuborish:** Element har doim ma'lum bir ustunning chap chizig'ida boshlanib, boshqa ustunning o'ng chizig'ida tugashi shart.
- **Tasodifiy piksellardan foydalanish (13px, 17px, 23px):** Bu interfeysni havaskor ko'rsatadi. Har doim 8pt qoidasiga (4, 8, 16, 24, 32px) amal qilish shart.
