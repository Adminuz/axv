# 9-dars. Wireframe loyihasini yakunlash, annotatsiyalar va Figmaga eksport

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + dizayn amaliyoti · **I-bob**, 9-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarda «Online books / E-kutubxona» veb-ilovasining to'liq wireframe loyihasini (bosh sahifa, katalog/qidiruv, kitob tafsilotlari, ro'yxatdan o'tish) mantiqiy yakunlash, dasturchilar va jamoa uchun izohli simli ramkalar (Annotated wireframes) yozish, loyihani PNG, SVG va PDF formatlarida eksport qilish hamda uni Figma dasturiga UI dizayn uchun asosiy referens (reference layer) sifatida import qilish ko'nikmalarini shakllantirish.

**Kutiladigan natija:**
- Izohli wireframe (Annotated wireframe) nima ekanini va undagi eslatmalar (Notes/Specifications) qanday tuzilishini biladi.
- «E-kutubxona» veb-saytining barcha 4 ta asosiy ekranini yagona tizimga birlashtira oladi.
- Wireframe loyihasini Axure RP yoki Balsamiq dasturidan PNG, SVG va PDF formatlarida to'g'ri eksport qiladi.
- Eksport qilingan wireframeni Figma dasturiga import qilib, yangi Frame va Layerlar ustida UI dizaynga tayyorlaydi.
- I-bobning «Wireframe loyihalash» bo'limi bo'yicha to'liq amaliy portfolio ishiga ega bo'ladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | O'tgan darslarni takrorlash (Interactions, Formalar). Muammo: «Wireframe chizildi, lekin dasturchi yoki UI dizayner unga qarab qanday ishlashini qayerdan biladi?» |
| 10–30 daq | Yangi mavzu: Nazariya | Izohli wireframe (Annotations), eksport formatlari (PNG, SVG, PDF) va Figmaga ko'chirish arxitekturasi |
| 30–35 daq | Tanaffus | Harakatli tanaffus |
| 35–65 daq | Amaliy mashg'ulot | «E-kutubxona» loyihasining to'liq ekranlariga annotatsiyalar qo'yish, PNG/SVG eksport qilish va Figma ish maydoniga referens sifatida yuklash |
| 65–75 daq | Tezkor nazorat | 5 ta savol-javob va loyihalar himoyasi |
| 75–80 daq | Xulosa va uyga vazifa | I-bob 1.3-mavzusi xulosasi va haftalik vazifalar |

---

## 2. Dars konspekti

### 2.1. Izohli simli ramkalar (Annotated Wireframes)

Faqatgina vizual bloklarning o'zi dasturchi yoki jamoaga har doim ham hamma narsani tushuntira olmaydi. Shu sababli professional dizaynda **Annotated Wireframe (Izohli simli ramka)** qo'llaniladi.

Annotatsiya — bu wireframe yonida joylashgan raqamlangan eslatmalar bo'lib, quyidagilarni aniqlashtiradi:
1. **Funksional qoidalar:** «Ushbu tugma bosilganda foydalanuvchi tizimga kirgan bo'lsa, yuklab olish boshlansin, kirmagan bo'lsa login oynasi ochilsin».
2. **Cheklovlar va validatsiya:** «Qidiruv maydoniga kamida 3 ta harf kiritilgandan so'ng avtomatik takliflar (autocomplete) chiqsin».
3. **Resurslar va ma'lumotlar:** «Bu blokdagi kitoblar bazaning `top_rated` jadvalidan tortib olinadi».

```
+-----------------------------------------------------------+
| [ Wireframe Ekrani ]          | [ Annotatsiyalar ]        |
|  (1) [ Qidiruv maydoni ]      | (1) Min 3 ta belgi        |
|  (2) [ Banner slayder  ]      | (2) Har 5 sek.da aylanadi |
|  (3) [ Kitob kartasi   ]      | (3) Bosilganda details    |
+-----------------------------------------------------------+
```

### 2.2. Eksport formatlari va ularning qo'llanilishi

Tayyor wireframeni boshqalar bilan bo'lishish uchun to'g'ri format tanlash zarur:
- **PNG (Raster rasm):** Taqdimotlar, messenjerlarda mijozga tezkor ko'rsatish va Figmaga fon rasmi sifatida kiritish uchun qulay.
- **SVG (Vektor grafikasi):** Vektorli format bo'lib, o'lchami o'zgarganda sifati buzilmaydi, Figmada har bir chiziqni alohida tahrirlash imkonini beradi.
- **PDF (Hujjat):** Butun loyihani ko'p sahifali rasmiy texnik hujjat (Specification) sifatida chop etish va mijozga tasdiqlatish uchun eng yaxshi format.

### 2.3. Wireframeni Figmaga o'tkazish (UI Dizaynga ko'prik)

Wireframing — bu loyihaning skeleti. Keyingi bosqich — **UI Dizayn (User Interface)** bo'lib, unda ranglar, shriftlar, rasmlar va komponentlar qo'shiladi.

Ko'chirish bosqichlari:
1. Axure RP yoki Balsamiq'dan wireframe PNG yoki SVG formatida eksport qilinadi.
2. Figma ochiladi va yangi loyiha (Design File) yaratiladi.
3. Eksport qilingan wireframe Figmaga `Drag & Drop` (sudrab tashlash) yoki `File &rarr; Place Image` orqali yuklanadi.
4. Wireframe qatlami (Layer) shaffofligi 30-40% ga tushiriladi va qulflanadi (`Lock`).
5. Uning ustidan yangi Frame chizilib, haqiqiy UI elementlari (Auto Layout, Komponentlar, Ranglar) bilan boyitiladi.

---

## 3. Amaliy mashg'ulot

### 1-mashq. «Online books» bosh sahifasiga annotatsiya tuzish
**Vazifa:** Bosh sahifadagi Header, Banner, Kitoblar ro'yxati va Footer bloklariga 4 ta raqamli marker qo'yib, har biri uchun texnik izoh yozing.

**Yechim:**
- **Marker 1 (Header/Search):** «Foydalanuvchi qidiruvga kitob nomi yoki muallifni yozganda real vaqtda mos natijalar ro'yxati chiqadi».
- **Marker 2 (Aksiya banneri):** «Banner har 5 soniyada avtomatik keyingi aksiyaga o'tadi, sichqoncha ustiga borganda to'xtaydi».
- **Marker 3 (Ommabop kitoblar):** «Bir qatorda 4 ta kitob kartasi joylashadi, 'Barchasi' bosilganda to'liq katalogga yo'naltiriladi».
- **Marker 4 (Footer):** «Sayt navigatsiyasi, ijtimoiy tarmoqlar va mualliflik huquqi ma'lumotlari keltiriladi».

---

### 2-mashq. Figmaga eksport va referens qatlamini yaratish
**Vazifa:** Tayyorlangan wireframeni PNG formatida eksport qilib, Figma ish maydoniga joylashtiring va ustiga yangi UI Frame chizing.

**Yechim:**
1. Axure RP da `File &rarr; Export &rarr; Export Pages to Image...` (Balsamiq'da `Project &rarr; Export &rarr; Current Wireframe to PNG`).
2. Figma veb-versiyasi yoki dasturida `Desktop 1440` o'lchamli Frame ochiladi.
3. PNG rasm Frame ichiga joylashtiriladi.
4. Layer qismida uning Opacity qiymati `40%` qilinadi va `Lock` belgisi bosiladi.
5. Dizayner endi ushbu karkas ustidan aniq piksellar va ranglar bilan yakuniy UI dizaynni chizishga tayyor.

---

## 4. Tezkor savollar (Checklist)

1. Annotated wireframe (Izohli simli ramka) nima uchun kerak?
   - **Javob:** Dasturchilar va buyurtmachiga interfeys qanday ishlashi, cheklovlar va funksional qoidalarni aniq tushuntirish uchun.
2. Wireframeni eksport qilishda qaysi 3 ta format eng ko'p qo'llaniladi?
   - **Javob:** PNG (rasm), SVG (vektor) va PDF (hujjat).
3. Figmaga wireframeni import qilgandan so'ng nega uning shaffofligi (Opacity) kamaytiriladi va qulflanadi?
   - **Javob:** U shunchaki asos (reference) vazifasini bajaradi; ustidan yangi toza UI elementlarini chizishda xalaqit bermasligi va siljib ketmasligi uchun.
4. Wireframe bosqichidan UI dizayn bosqichiga o'tganda nimalar qo'shiladi?
   - **Javob:** Haqiqiy ranglar, professional tipografiya, fotosuratlar, piktogrammalar (ikonlar) va dizayn tizimi (UI Kit).
5. 1.3-mavzu davomida biz qanday asosiy dasturlarni o'rgandik?
   - **Javob:** Balsamiq (tezkor Low-fi eskizlar) va Axure RP (chuqur interaktiv va mantiqiy prototiplar).
