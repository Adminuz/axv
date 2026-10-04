# 9-dars: Ikonka, tugma va navigatsiya elementlarini dizayni (UI Kit)

**Fan:** Advanced UX/UI dizayn va Advanced Front-end  
**Sinf:** 10-sinf  
**Hafta:** 3-hafta, 3-dars (umumiy 9-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga raqamli foydalanuvchi interfeysining (UI) eng muhim interaktiv bloklari — **tugmalar (buttons)**, **ikonkalar (icons)** va **navigatsiya elementlari**ni professional darajada loyihalashni o'rgatish; asosiy va qo'shimcha tugma turlari (Primary, Secondary, Tertiary/Ghost, FAB, Icon button, Link), tugmaning 5 ta holati (Enabled, Hover, Focus, Active, Disabled), mobil teginish o'lchamlari (kamida 44px) hamda kontrast talablarini (kamida 4.5:1) tushuntirish; Figma dasturida Auto Layout (`Shift + A`) va Variantlar yordamida qayta ishlatiluvchi yaxlit **UI Kit** komponentlarini yaratish amaliy ko'nikmalarini shakllantirish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- Foydalanuvchi interfeysida tugmalarning ierarxiyasini (Primary, Secondary, Tertiary/Ghost) ajrata olish;
- Mobil va veb interfeyslardagi maxsus tugmalarning (FAB, Icon button, Link) vazifasini tushunish;
- Tugmaning 5 ta holatini (Enabled, Hover, Focus, Active, Disabled) va nima uchun Focus holati accessibility uchun zarurligini bilish;
- Tugma yorlig'i (label) qoidalarini (fe'l shakli, qisqalik, 14–18px semibold shrift) amalda to'g'ri tanlash;
- Matn va tugma foni o'rtasidagi rang kontrasti kamida 4.5:1 bo'lishi shartligini bilish;
- Mobilda teginish maydoni (touch target) kamida 44px bo'lishi lozimligini o'rganish;
- Ikonkalar bilan ishlash qoidalarini (tanish metaforalardan foydalanish, yangi belgi ixtiro qilmaslik, matnli yorliqlar bilan quvvatlash) bilish;
- Sayt va ilovalardagi asosiy navigatsiya bloklarini (Header/Logo, Gorizontal menyu, Qidiruv, Pastki tab-bar, Non ushoqlari) to'g'ri loyihalay olish;
- Figmada Auto Layout (`Shift + A`) yordamida responsiv tugmalar va UI Kit yaratishni amalda bajara olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk (har bir o'quvchi uchun);
- Internet tarmog'i va veb-brauzer;
- Figma akkaunti (veb yoki desktop ilovasi);
- WCAG kontrast tekshiruvchi plaginlar (masalan, Stark yoki Contrast Checker);
- Proyektor yoki monitor (namoyish uchun).

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Grid tizimlari, 12 ustunli desktop va 8pt masofa qoidalari bo'yicha savol-javob |
| **10–25 min** | Yangi mavzu: Tugmalar va ularning UIdagi roli | Tugmalar ierarxiyasi (Primary, Secondary, Tertiary), FAB, Icon button, Link |
| **25–40 min** | Tugma dizayni omillari va 5 ta holati | Shakl, burchak radiusi, yorliq qoidalari, 5 ta holat (Enabled, Hover, Focus, Active, Disabled), 44px qoidasi |
| **40–55 min** | Ikonkalar va navigatsiya bloklari | Universal ikonalar, gorizontal menyu, qidiruv bloki, mobil bottom bar |
| **55–75 min** | Amaliy mashg'ulot (Figma UI Kit) | Auto Layout bilan Primary va Secondary tugmalarni yaratish, barcha holatlarini (Variants) yig'ish |
| **75–80 min** | Xulosa va darsni yakunlash | Asosiy xulosalar, tezkor nazorat savollari va uyga vazifa topshirig'i |

---

## Nazariy ma'lumotlar

### 1. Tugmalar (Buttons) va ularning UIdagi ahamiyati

Tugmalar — foydalanuvchi interfeysining (UI) eng muhim komponentlaridan biridir. Ular foydalanuvchini harakatga undovchi asosiy vosita (Call to Action — CTA) hisoblanadi. Har qanday interfeysda harakatni amalga oshirish uchun tugmalar ma'lum bir vizual ierarxiya asosida joylashtiriladi.

#### Asosiy tugma turlari:
1. **Birlamchi tugma (Primary button):**
   - Ekrandagi eng muhim amalni bajaradi (masalan: *To'lov qilish*, *Ro'yxatdan o'tish*, *Formani yuborish*).
   - Vizual jihatdan eng yorqin, to'liq fonli va diqqatni birinchi bo'lib tortadigan ko'rinishga ega bo'ladi.
   - Odatda bir ekranda faqat bitta asosiy Primary tugma bo'lishi tavsiya etiladi.
2. **Ikkinchi darajali tugma (Secondary button):**
   - Birlamchi tugmaga nisbatan kamroq muhim, ammo zarur amallarni bajaradi (masalan: *Bekor qilish*, *Qoralama saqlash*).
   - Odatda konturli (outline) yoki och neytral fonli bo'ladi.
3. **Uchinchi darajali (Tertiary) yoki "Ghost" tugma:**
   - Kam ahamiyatli, yordamchi amallar uchun ishlatiladi (masalan: *Parolni unutdingizmi?*, *Tafsilotlar*).
   - Fonsiz yoki faqat matn ko'rinishida bo'lib, sahifani vizual og'irlashtirmaydi.

#### Qo'shimcha tugma turlari:
1. **FAB (Floating Action Button — Suzuvchi amal tugmasi):**
   - Asosan mobil interfeyslarda ekranning pastki o'ng burchagida "suzib turadi".
   - Doira shaklida, soyali (drop shadow) va markazida bitta ikona bo'ladi (masalan, Gmail'dagi *Yangi xat yozish* tugmasi).
2. **Ikona tugma (Icon button):**
   - Matnsiz, faqat piktogramma shaklidagi tugma (qidiruv lupasi, savatcha, bildirishnoma qo'ng'irog'i). Joy tejaydi, biroq faqat 100% tushunarli ramzlar uchun ishlatilishi shart.
3. **Havola tugma (Link button):**
   - Tashqi ko'rinishi giperhavolaga o'xshash, foydalanuvchini boshqa sahifa yoki bo'limga yo'naltiradi.

---

### 2. Tugma dizaynining asosiy omillari

1. **Shakli va burchak radiusi (Corner radius):**
   - To'g'ri to'rtburchak (0–4px radius): jiddiy, moliyaviy va korporativ uslub;
   - Katta radius (8–16px): zamonaviy, qulay va do'stona muhit;
   - To'liq yumaloq (Pill / 999px radius): e'tiborni kuchli tortadi, CTA uchun ayni muddao.
2. **Tugma yorlig'i (Label):**
   - Qisqa va fe'l shaklida bo'lishi shart (*Yuborish*, *Xarid qilish*, *Yuklab olish*);
   - O'qilishi oson shriftlar (Roboto, Inter, Lato) tanlanadi, o'lchami 14–18px, vazni Medium yoki Semibold bo'ladi;
   - Bir butun platforma bo'ylab atamalar bir xil bo'lishi lozim (bir sahifada "Yuborish", boshqa sahifada "Jo'natish" deyilmasligi kerak).
3. **Rang va kontrast talabi (WCAG AA):**
   - Tugma matni va uning foni o'rtasidagi kontrast nisbati kamida **4.5 : 1** bo'lishi shart.
   - Ranglar psixologik ma'noga ega: qizil — xavfli yoki bekor qiluvchi amal (Delete, Logout), yashil/ko'k — muvaffaqiyatli tasdiq (Confirm, Pay).
4. **Ergonomika va o'lcham (44px qoidasi):**
   - Tugmaning balandligi odatda 32–56px bo'ladi.
   - **Mobil interfeyslarda odam barmog'i bilan bexato bosishi uchun minimal teginish maydoni (touch target) kamida 44×44px bo'lishi shart!**

---

### 3. Tugmaning 5 ta holati (Button States)

Har bir professional tugma interfeysda kamida 5 ta holatga ega bo'lishi kerak:
1. **Enabled (Default / Normal):** Tugmaning odatiy, bosishga tayyor turgan holati.
2. **Hover:** Foydalanuvchi sichqoncha kursorini tugma ustiga keltirgandagi holat (fon rangi 10-15% ga to'qroq yoki ochroq bo'ladi).
3. **Focus:** Foydalanuvchi klaviaturadagi `Tab` tugmasi orqali tugmaga kelganda paydo bo'ladigan holat (konturli halqa/ring). Bu imkoniyati cheklangan (accessibility) foydalanuvchilar uchun hayotiy muhim!
4. **Active (Pressed):** Tugma aynan bosilgan lahzadagi reaksiyasi (kichrayish, chuqurlashish yoki rang qorayishi).
5. **Disabled:** Tugma hozircha ishlamaydigan holat (masalan, forma to'liq to'ldirilmaguncha). Odatda 30-40% xira kulrang bo'ladi va kursor "not-allowed" belgisiga aylanadi.

---

### 4. Ikonkalar (Icons) bilan ishlash qoidalari

- **Tanish metaforalar:** Odamlar ko'nikkan belgilardan foydalaning. Qidiruv uchun lupa, savat uchun aravacha, sozlamalar uchun tishli g'ildirak.
- **Yangi ramzlar o'ylab topmang:** Notanish ikonka foydalanuvchini adashtiradi va qo'rquv uyg'otadi.
- **Matn bilan birga qo'llash:** Iloji boricha ikonkani qisqa matnli yorliq bilan birga ishlating. Matnsiz ikona faqat hammaga ma'lum funksiyalarda (qidiruv, profil, uy) o'zini oqlaydi.
- **Birlik va o'lcham:** Barcha ikonalar bitta o'lchamdagi bounding box (masalan, 24×24px) ichida va bir xil chiziq qalinligida (stroke width) chizilishi shart.

---

### 5. Asosiy navigatsiya bloklari va UI Kit tushunchasi

- **Logo / "Asosiy sahifaga" bloki:** Sahifaning yuqori chap burchagida joylashadi, har doim bosh sahifaga qaytaradi.
- **Gorizontal navigatsiya paneli (Navbar):** Asosiy bo'limlarga o'tish giperhavolalari ro'yxati.
- **Qidiruv va tezkor harakatlar (Search & Action):** Odatda o'ng burchakda profil va savatcha bilan birga joylashadi.
- **Mobil pastki menyu (Bottom Navigation Bar):** Mobilda bir qo'l bilan boshqarish uchun pastki qismda 3–5 ta eng muhim tugmani jamlaydi.
- **Non ushoqlari (Breadcrumbs):** Ierarxik chuqur kataloglarda foydalanuvchiga hozir qayerda ekanini ko'rsatadi (`Bosh sahifa > Katalog > Noutbuklar`).
- **UI Kit:** Dizayn loyihasida ishlatiladigan barcha tugmalar, ikonalar, forma maydonlari va navigatsiya elementlarining yagona, standartlashtirilgan komponentlar to'plamidir. Figmada komponentlar (`Ctrl + Alt + K`) va variantlar orqali boshqariladi.

---

## Amaliy topshiriqlar va mashqlar

### 1-topshiriq. Interfeysdagi amallar uchun tugma turini to'g'ri tanlash (oson)
Quyidagi 4 ta amal uchun tugma toifasini (Primary, Secondary, Ghost, FAB, Destructive) to'g'ri biriktiring va tanlovingizni asoslang:
1. Internet-do'konda buyurtmani rasmiylashtirish va to'lash tugmasi;
2. Shaxsiy profilni butunlay o'chirib yuborish (Delete Account) tugmasi;
3. Mobil messenjerda tezda yangi xat yoki suhbat boshlash tugmasi;
4. Mahsulot kartochkasi ostidagi "Mahsulot haqida to'liq sharhlar" havolasi.

**Yechim:**
1. **To'lov qilish:** `Primary button` — ekrandagi eng asosiy maqsad va harakatga chaqiruv (CTA);
2. **Profilni o'chirish:** `Destructive (Qizil) Secondary yoki Alert tugmasi` — xato bosilib ketmasligi uchun uni Primary qilib ajratilmaydi, aksincha ikkilamchi qilib, qizil rangda ogohlantirish beriladi;
3. **Yangi xat yozish:** `FAB (Floating Action Button)` — mobil ekranning pastki o'ng burchagida doimiy suzib turuvchi, bitta harakat bilan yangi xat ochadigan doiraviy tugma;
4. **To'liq sharhlar:** `Ghost / Link tugma` — vizual og'irlik tug'dirmaydigan minimal ko'rinishdagi havola tugma.

---

### 2-topshiriq. Tugma dizaynidagi xatolarni tahlil qilish va to'g'rilash (o'rta)
Yangi boshlovchi dizayner mobil ilova uchun tugma yaratdi va unda quyidagi xususiyatlar mavjud:
- Tugma balandligi: `28px`;
- Fon rangi: och sariq (`#FEF08A`), matn rangi: oq (`#FFFFFF`);
- Tugma matni: *"Iltimos, agar rozi bo'lsangiz, keyingi sahifaga o'tish uchun shu yerni bosing"*;
- Faqat bitta holat chizilgan, Hover yoki Focus ko'rsatilmagan.

Ushbu dizayndagi 4 ta jiddiy xatoni aniqlang va ularni professional qoidalarga moslab to'g'rilang.

**Yechim:**
1. **O'lcham xatosi:** `28px` mobilda barmoq bilan bosish uchun juda kichik. To'g'rilash: Balandlikni kamida `44px` (yoki `48px`) qilish kerak.
2. **Kontrast xatosi:** Och sariq fondagi oq matn o'qilmaydi (kontrast taxminan 1.2:1 bo'lib, 4.5:1 me'yoridan ancha past). To'g'rilash: Fonni to'q rangga o'zgartirish yoki fon sariq qolsa matnni to'q kulrang/qora (`#1F2937`) qilish kerak.
3. **Yorliq (label) xatosi:** Matn juda uzun va noaniq. To'g'rilash: Qisqa fe'lli CTA matn qo'yish kerak: *"Davom etish"* yoki *"Oldinga"*.
4. **Holatlar xatosi:** Tugma bitta holatda qolgan, interaktivlik va accessibility yo'q. To'g'rilash: Kamida 5 ta holatni (Default, Hover, Active, Focus, Disabled) ishlab chiqish kerak.

---

### 3-topshiriq. Figma dasturida to'liq Auto Layout tugma komponentini loyihalash (qiyin)
Figma dasturida zamonaviy veb va mobil ilovalar uchun moslashuvchan **Primary Button** komponentini loyihalashtiring:
1. `T` tugmasi bilan matn yozing va shrift parametrlarini belgilang (Inter, 16px, Semi-bold);
2. Auto Layout (`Shift + A`) qo'llang;
3. Ichki masofalarni (Padding) 8pt tizimi bo'yicha kiriting;
4. Burchak radiusini (Corner radius) o'rnating;
5. Tugmaning barcha 5 ta holati (Enabled, Hover, Focus, Active, Disabled) uchun Variantlar (`Create Component Set`) yarating.

**Yechim:**
1. **Matn yaratish:** *"Saqlash"* deb matn yoziladi. Shrift: Inter, 16px, Semibold, rang oq (`#FFFFFF`).
2. **Auto Layout qo'shish:** Matn tanlanib `Shift + A` bosiladi.
3. **Padding sozlash:** Horizontal padding: `24px`, Vertical padding: `12px` (umumiy balandlik $16 \times 1.2 + 24 \approx 44\text{--}48\text{px}$ ga teng bo'ladi).
4. **Shakl va fon:** Fon rangi: To'q ko'k (`#2563EB`), Corner radius: `8px`.
5. **Variantlar to'plami:**
   - `State=Enabled`: Asosiy ko'k fon (`#2563EB`);
   - `State=Hover`: Bir oz to'qroq ko'k fon (`#1D4ED8`);
   - `State=Focus`: Ko'k fon atrofida 3px qalinlikdagi ochiq havorang halqa (Focus ring: `#93C5FD`);
   - `State=Active`: Chuqurlashgan to'q ko'k fon (`#1E40AF`) va masshtab 98%;
   - `State=Disabled`: Xira kulrang fon (`#E2E8F0`), matn rangi xira kulrang (`#94A3B8`), bosish taqiqlangan.

---

## Tezkor nazorat savollari

1. Birlamchi (Primary) tugma bilan ikkinchi darajali (Secondary) tugma o'rtasidagi asosiy farq nima?
   - *Javob:* Primary tugma ekrandagi eng asosiy harakatni (CTA) ifodalaydi, to'liq yorqin fonga ega va odatda ekranda 1 ta bo'ladi. Secondary esa yordamchi amallar (Bekor qilish) uchun ishlatilib, konturli yoki xiraroq fonga ega bo'ladi.
2. Mobil ekranlarda tugmaning minimal o'lchami nima uchun kamida 44px bo'lishi shart?
   - *Javob:* Inson barmog'ining o'rtacha teginish maydoni (touch target) hisobga olingan holda, adashmasdan va qo'shni elementlarga tegib ketmasdan qulay bosishni ta'minlash uchun.
3. Tugmaning `Focus` holati nima uchun kerak va u kimlar uchun muhim?
   - *Javob:* Klaviaturadagi `Tab` tugmasi orqali interfeysda harakatlanuvchilar, sichqoncha ishlata olmaydigan yoki ko'rishida nuqsoni bor (Accessibility) insonlarga hozir qaysi element tanlanganini aniq ko'rsatish uchun.
4. Nega dizaynerlar ilovada yangi, noodatiy ikonkalarni o'ylab topmasliklari kerak?
   - *Javob:* Foydalanuvchilar o'rganib qolgan universal vizual metaforalarga (lupa, savat, sozlamalar) ega. Yangi noaniq ikonka foydalanuvchini ikkiltiradi, xatoliklarga va tushunmovchilikka olib keladi.

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Bir ekranda bir nechta Primary tugma qo'yish:** Bu foydalanuvchini sarosimaga soladi. Har doim bitta ekranda faqat bitta asosiy maqsad (CTA) bo'lishi kerak.
- **Tugma matnini mavhum qilish ("Bosing", "Bu yerda"):** Tugma aniq nima sodir bo'lishini aytishi lozim: *"Buyurtma berish"*, *"Faylni yuklash"*, *"Hisobni to'ldirish"*.
- **Past kontrastli tugmalar yaratish:** Oq fonda och kulrang matn yoki yashil fonda sariq matn yozish odamlar ko'zini toliqtiradi va foydalanishni qiyinlashtiradi. Har doim 4.5:1 kontrast qoidasiga amal qiling.
