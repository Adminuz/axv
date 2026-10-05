# 9-dars: Ikonka, tugma va navigatsiya elementlarini dizayni (UI Kit)

**Fan:** Advanced UX/UI dizayn va Advanced Front-end  
**Sinf:** 10-sinf  
**Mavzu:** Ikonka, tugma va navigatsiya elementlarini dizayni (UI Kit)  

---

## Darsning qisqacha mazmuni

Foydalanuvchi interfeysidagi har qanday maqsadli harakat (Call to Action — CTA) tugmalar orqali amalga oshadi. Ushbu darsda biz interfeysdagi vizual ierarxiyaning asosiy vositalari bo'lgan tugma turlari, ularning holatlari, universal ikonalar va navigatsiya bloklarini loyihalash sirlarini o'rganamiz:

1. **Tugmalar ierarxiyasi:**
   - **Primary (Birlamchi):** Ekranning asosiy maqsadi (bitta ekranda bitta asosiy CTA);
   - **Secondary (Ikkinchi darajali):** Yordamchi, ammo muhim harakatlar (Bekor qilish, Saqlash);
   - **Tertiary / Ghost (Uchinchi darajali):** Kam ahamiyatli amallar, fonsiz yoki matnli havolalar;
   - **Maxsus tugmalar:** FAB (Floating Action Button — suzuvchi amal tugmasi), Icon button (ikona tugma) va Link button.
2. **Tugmaning 5 ta holati (States):**
   - **Enabled (Default):** Odatdagi bosishga tayyor holat;
   - **Hover:** Kursorni ustiga olib kelgandagi reaksiya;
   - **Focus:** Klaviaturadagi `Tab` orqali tanlangandagi halqa (Accessibility uchun shart);
   - **Active (Pressed):** Tugma bosilgan paytdagi chuqurlashish;
   - **Disabled:** Amal bajarish vaqtincha taqiqlangan nofaol holat.
3. **Ergonomika va standartlar:**
   - Mobil ekranda minimal teginish maydoni (touch target) kamida **44×44px** bo'lishi shart;
   - Matn va fon o'rtasidagi rang kontrasti kamida **4.5 : 1** (WCAG standarti);
   - Qisqa, aniq fe'l shaklidagi yorliqlar (*Yuborish*, *Xarid qilish*).
4. **Ikonkalar va navigatsiya bloklari:**
   - Odamlar biladigan universal ramzlardan foydalanish (lupa, savatcha, uy, sozlamalar);
   - Header, Navbar, Qidiruv, Pastki tab-bar va Breadcrumbs (non ushoqlari).

---

## Mustaqil bajarish uchun amaliy topshiriqlar

Quyidagi 10 ta amaliy vazifani diqqat bilan o'rganing va ularni daftaringizda yoki Figma dasturida bajaring:

### 1-topshiriq · oson
Elektron tijorat (e-commerce) veb-saytidagi "Savat" (Cart) sahifasini tasavvur qiling. Unda 3 ta harakat mavjud:
1. *Buyurtmani rasmiylashtirish va to'lash*;
2. *Savatni tozalash*;
3. *Xarid qilishda davom etish*.  
Ushbu harakatlarning har biriga qaysi tugma turini (Primary, Secondary, Ghost/Link) biriktirish kerakligini aniqlang va sababini tushuntiring.

### 2-topshiriq · oson
Tugmalarda ishlatiladigan yorliqlar (labels) bo'yicha quyidagi xato matnlarni professional qoidaga moslab, qisqa va aniq fe'l shakliga o'zgartiring:
- *"Bu yerga bosilsa yangi akkaunt ochiladi"*;
- *"Ha, men rostdan ham buyumni o'chirmoqchiman"*;
- *"Hujjatni yuklab olish jarayonini boshlash"*;
- *"Oldingi ko'rinishga qaytish"*.

### 3-topshiriq · oson
Nima uchun mobil ilovalarda asosiy tugmalar o'lchami kamida 44px balandlikda qilinadi? Agar tugma 24px bo'lsa, foydalanuvchida qanday noqulayliklar yuzaga keladi? Fikringizni 3–4 ta gap bilan ifodalang.

### 4-topshiriq · o'rta
Tugmaning 5 ta asosiy holatini (Enabled, Hover, Focus, Active, Disabled) o'z ichiga olgan vizual xarita tuzing. Har bir holatda tugmaning foni, matn rangi, ramkasi yoki kursor qanday o'zgarishini jadval ko'rinishida yozib chiqing.

### 5-topshiriq · o'rta
Dizayner mobil ilovadagi xabarlar ro'yxati uchun pastki o'ng burchakka FAB (Floating Action Button) tugmasini qo'ymoqchi. 
- FAB tugmasi nima va uning asosiy afzalligi nimada?
- Ekranda birdaniga 3 ta turli rangdagi FAB tugmasini qo'yish to'g'rimi yoki xatomi? Nega?

### 6-topshiriq · o'rta
Sizga yangi yetkazib berish (delivery) ilovasi uchun quyidagi vazifalarga mos ikonka tanlash topshirildi:
1. Manzilni xaritada ko'rsatish;
2. Kuryer bilan telefon orqali bog'lanish;
3. Taomlar kategoriyalarini filtrlash;
4. Buyurtmalar tarixini ko'rish.  
Ushbu 4 ta amal uchun qaysi universal metafora va ikonkalardan foydalanish maqsadga muvofiqligini yozing. Nega ushbu amallar uchun mutlaqo yangi ramz ixtiro qilmaslik kerak?

### 7-topshiriq · qiyin
Figma dasturida **Auto Layout** (`Shift + A`) yordamida to'liq moslashuvchan (responsive) tugma yarating:
- Shrift: Inter yoki Roboto, 16px, Semibold;
- Ichki masofalar: Horizontal padding — 24px, Vertical padding — 12px;
- Fon rangi va burchak radiusi: 8px;
- Tugmaga chap tomondan 20×20px o'lchamdagi ikona joylashtiring (masalan, yuklab olish ikonasi) va ikona bilan matn orasidagi masofani 8px qilib belgilang.
- Matn uzunligini o'zgartirib ko'ring — tugma qanday kengayishini kuzating.

### 8-topshiriq · qiyin
Katta korporativ bank ilovasi uchun foydalanuvchi hisobidan pul o'tkazish oynasi (Modal dialog) loyihalanmoqda. Oynada quyidagi 3 ta tugma bo'lishi kerak:
- *O'tkazmani tasdiqlash*;
- *Bekor qilish*;
- *To'lov shartlari bilan tanishish*.  
Ushbu 3 ta tugmaning vizual ierarxiyasini, joylashuv tartibini (chapda yoki o'ngda) hamda rang va holatlarini to'liq tavsiflab bering.

### 9-topshiriq · qiyin
WCAG (Web Content Accessibility Guidelines) talabiga ko'ra matn va uning foni o'rtasidagi kontrast nisbati kamida **4.5 : 1** bo'lishi shart.
- Och ko'k fonda (`#60A5FA`) oq rangli matn (`#FFFFFF`) ushbu talabga javob beradimi?
- Agar talabga javob bermasa, qanday o'zgartirish kiritish kerak (fonni to'qroq qilishmi yoki matnni qoraytirish)?
- Klaviatura orqali boshqaruvda tugmaning Focus holati nima uchun muhim?

### 10-topshiriq · bonus
Figma dasturida o'zingizning shaxsiy mini **UI Kit**ingizni yarating:
1. 3 turdagi tugma: Primary, Secondary, Ghost;
2. Har bir tugma uchun 3 ta holat (Default, Hover, Disabled) bilan Variants to'plamini shakllantiring;
3. 4 ta asosiy navigatsiya ikonkasini (Home, Search, Cart, Profile) bitta o'lchamdagi (24×24px) freym ichiga joylashtiring;
4. Mini UI Kit elementlaridan foydalanib, mobil ekran uchun sodda Header va Bottom Navigation bar yasang.
