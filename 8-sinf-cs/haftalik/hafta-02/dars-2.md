# 5-dars. Internet, brauzerlar va elektron pochta bilan ishlash

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliy mashg'ulot · **I-bob**, 5-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarga Internet va World Wide Web (WWW) tushunchalari, zamonaviy brauzerlarning ishlash mexanizmlari, qidiruv tizimlarida samarali qidiruv operatorlaridan foydalanish ko'nikmalari hamda elektron pochta (Email) tizimida xat yozish, formatlash, fayllarni to'g'ri biriktirish va kibergigiyena qoidalarini amaliy o'rgatish.

**Kutiladigan natija:**
- Internet va veb-sayt (WWW) tushunchalari o'rtasidagi farqni tushuntira oladi.
- Mashhur brauzerlar (Chrome, Edge, Firefox, Safari) interfeysini, xatcho'plar (bookmarks), tarix (history), kesh (cache) va inkognito rejimidan foydalanishni biladi.
- Qidiruv operatorlari (`""`, `-`, `site:`, `filetype:`) yordamida aniq axborotni bir necha soniyada topadi.
- Elektron pochta manzili strukturasi, xat yozishdagi maydonlar (`To`, `Cc`, `Bcc`, `Subject`, `Body`, `Attachment`) vazifasini farqlaydi va professional xat yoza oladi.
- Fishing (phishing), spam va shubhali fayllardan himoyalanishning asosiy xavfsizlik qoidalariga rioya qiladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va muammo qo'yish | O'tgan darsni takrorlash (kompyuter qurilmalari va portlar). Muammoli savol: «Internet va brauzer bitta narsami? Google qidiruvida kerakli natijani qanday qilib 1-sahifadayoq topish mumkin?» |
| 10–30 daq | Yangi mavzu: Nazariya | Internet tushunchasi, brauzerlar ishlashi, qidiruv operatorlari, elektron pochta anatomiyasi va xavfsizlik |
| 30–35 daq | Tanaffus | Ko'z va tana mashqlari |
| 35–65 daq | Amaliy mashg'ulot | Brauzer sozlamalarini o'rganish, Google qidiruv operatorlarini sinash, elektron pochta xatini tayyorlash (Cc/Bcc va birikma bilan) |
| 65–75 daq | Tezkor nazorat | 5 ta tezkor savol-javob va interaktiv tahlil |
| 75–80 daq | Xulosa va uyga vazifa | Muhim fikrlarni jamlash va topshiriqlarni belgilash |

---

## 2. Dars konspekti

### 2.1. Internet va World Wide Web (WWW) tushunchasi

- **Internet (International Network):** Butun dunyo bo'ylab millionlab kompyuterlar, serverlar va mobil qurilmalarni o'zaro bog'lagan global axborot tarmog'idir. U jismoniy infratuzilma (kabellar, optik tolalar, sun'iy yo'ldoshlar, marshrutizatorlar) hisoblanadi.
- **World Wide Web (WWW / Butunjahon o'rgimchak to'ri):** Internet tarmog'ida joylashgan, gipermatnlar (HTML) va multimedia fayllaridan iborat veb-sahifalar va saytlar tizimidir. Internet — bu yo'llar tarmog'i bo'lsa, WWW — bu yo'lda harakatlanayotgan mashinalar va yetkazilayotgan yuklardir.
- **Mijoz-Server modeli (Client-Server):**
  - **Mijoz (Client):** Ma'lumot so'rovchi qurilma (masalan, sizning kompyuteringiz yoki brauzeringiz).
  - **Server:** Ma'lumotlarni saqlovchi va so'rovga binoan ularni qaytaruvchi kuchli kompyuter.

### 2.2. Veb-brauzerlar va ularning imkoniyatlari

Brauzer (Web Browser) — internetdagi veb-sayt kodlarini (HTML, CSS, JavaScript) o'qib, ularni insonga tushunarli grafik ko'rinishga keltirib beruvchi dasturdir.

Eng mashhur brauzerlar:
1. **Google Chrome:** Dunyoda eng keng tarqalgan va tezkor brauzer (Blink dvigateli).
2. **Microsoft Edge:** Windows tizimiga o'rnatilgan, Chromium asosidagi brauzer.
3. **Mozilla Firefox:** Ochiq manbali, shaxsiy maxfiylikka katta e'tibor beruvchi brauzer.
4. **Apple Safari:** Apple qurilmalari (macOS, iOS) uchun optimallashtirilgan brauzer.

Brauzerning asosiy elementlari va vositalari:
- **Tablar (Yorliqlar):** Bir oynada bir vaqtning o'zida bir nechta sahifani ochish (`Ctrl+T` — yangi tab, `Ctrl+W` — tabni yopish, `Ctrl+Shift+T` — yopilgan tabni qayta ochish).
- **Xatcho'plar (Bookmarks):** Muhim va tez-tez kiriladigan saytlarni bir tugma bilan saqlab qo'yish (`Ctrl+D`).
- **Ko'rish tarixi (History):** Avval kirilgan sahifalar ro'yxati (`Ctrl+H`).
- **Inkognito / Maxfiy rejim (`Ctrl+Shift+N`):** Bu rejimda brauzer kirilgan saytlar tarixini, qidiruv so'rovlarini va cookie fayllarini xotirada saqlab qolmaydi.
- **Kesh (Cache) va Kukilar (Cookies):**
  - *Kesh:* Sayt tez yuklanishi uchun kompyuterga saqlab olinadigan rasmlar va fayllar.
  - *Kukilar:* Foydalanuvchi identifikatori, sayt sozlamalari yoki savatcha ma'lumotlarini eslab qoluvchi kichik matnli fayllar.

### 2.3. Qidiruv tizimlari va professional qidiruv operatorlari

Qidiruv tizimi (Search Engine) — internetdagi milliardlab sahifalar orasidan kerakli ma'lumotni kalit so'zlar bo'yicha topib beruvchi maxsus xizmat (Google, Yandex, Bing).

Google qidiruvini professional darajaga ko'taruvchi operatorlar:
1. `""` (Iqtibos): Aniq so'z birikmasini aynan qidirish.
   - Misol: `"Muhammad al-Xorazmiy vorislari"`
2. `-` (Minus / Istisno): Natijalar ichidan muayyan so'zni olib tashlash.
   - Misol: `jaguar mashina -hayvon`
3. `site:` Faqat ma'lum bir sayt yoki domendan qidirish.
   - Misol: `python darslari site:edu.uz`
4. `filetype:` Faqat belgilangan formatdagi fayllarni topish (pdf, docx, pptx).
   - Misol: `computer science foundation filetype:pdf`
5. `OR` (Yoki): Bir vaqtda bir nechta variantdan birini qidirish.
   - Misol: `noutbuk Acer OR Asus`
6. `*` (Yulduzcha / Wildcard): Eslab qolinmagan so'z o'rnida joy to'ldiruvchi.
   - Misol: `bir * ikki bo'lmaydi`

### 2.4. Elektron pochta (Email) bilan ishlash

Elektron pochta (Electronic Mail) — internet orqali xat, hujjat va fayllarni tezkor almashish tizimi.

Pochta manzili tuzilishi: `foydalanuvchi_nomi@pochta_serveri.domen`
- Masalan: `sherzod.alimov@gmail.com` (`@` belgisi — «kuchukcha» yoki «at» deb ataladi).

Xat yuborish oynasining asosiy maydonlari:
- **To (Kimga):** Xatning asosiy qabul qiluvchi shaxsining manzili.
- **Cc (Carbon Copy / Nusxa):** Xatdan xabardor bo'lishi kerak bo'lgan ikkinchi darajali qabul qiluvchilar (barcha oluvchilar bu manzilni ko'ra oladi).
- **Bcc (Blind Carbon Copy / Yashirin nusxa):** Xat nusxasi yuboriladi, lekin asosiy qabul qiluvchilar bu manzilga xat ketganini ko'ra olmaydi (maxfiylik uchun juda muhim).
- **Subject (Mavzu):** Xatning qisqa mazmuni (1 qator). Bo'sh qoldirish odobsizlik hisoblanadi!
- **Body (Xat matni):** Xatning asosiy matni: salomlashish, murojaat maqsadi, xulosa va imzo.
- **Attachment (Biriktirilgan fayl):** Qisqich (paperclip) belgisi orqali xatga rasm, PDF, Word yoki arxiv fayl biriktirish. Ko'p pochta xizmatlarida (Gmail) maksimal hajm 25 MB.

### 2.5. Internet va elektron pochtada xavfsizlik qoidalari

1. **Fishing (Phishing) xatlar:** Bank yoki taniqli kompaniya nomidan soxta xat yuborib, login va parolni o'g'irlashga urinish. Hech qachon shubhali xatdagi havolaga kirmang!
2. **Spam (Keraksiz reklama xatlari):** Ommaviy jo'natiladigan keraksiz xabarlar. Ularni ochmasdan o'chirish yoki «Spam»ga belgilash lozim.
3. **Shubhali birikmalar (Attachments):** `.exe`, `.bat`, `.vbs`, `.scr` yoki shubhali arxivli fayllarni HECH QACHON ochmang — ular kompyuterga virus yuqtiradi.
4. **Jamoat Wi-Fi tarmoqlarida ehtiyotkorlik:** Parolsiz ochiq Wi-Fi nuqtalarida shaxsiy pochtaga yoki bank kartasi ma'lumotlariga kirmaslik tavsiya etiladi.

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq. Brauzer tezkor tugmalari va inkognito rejim
**Vazifa:** Brauzerni oching, 3 ta yangi tab hosil qiling, ulardan birini yoping va qayta tiklang. So'ngra inkognito rejimiga o'ting.
**Yechim:**
- Brauzerda yangi tab ochish uchun `Ctrl + T` tugmasi 3 marta bosiladi.
- Tabni yopish uchun `Ctrl + W` bosiladi.
- Tasodifan yopilgan tabni qayta ochish uchun `Ctrl + Shift + T` bosiladi.
- Maxfiy/inkognito oynasini ochish uchun `Ctrl + Shift + N` (yoki Firefox'da `Ctrl + Shift + P`) bosiladi.

### 2-topshiriq. Google qidiruv operatorlaridan foydalanish
**Vazifa:** Quyidagi shartlar bo'yicha Google qidiruviga to'g'ri so'rov tuzing:
1. O'zbekistondagi ta'lim saytlaridan (`.edu.uz`) faqat `dasturlash` mavzusini toping.
2. «Sun'iy intellekt asoslari» nomli faqat PDF kitoblarni toping.
3. «Python» so'zini qidirganda ilon haqidagi ma'lumotlar chiqmasin.
**Yechim:**
1. `dasturlash site:edu.uz`
2. `"Sun'iy intellekt asoslari" filetype:pdf`
3. `Python -ilon -snake`

### 3-topshiriq. To'g'ri elektron xat loyihasini tayyorlash
**Vazifa:** Mentorga uy vazifasini yuborish bo'yicha xat tayyorlang. Qoidalar:
- Asosiy qabul qiluvchi: `mentor@maktab.uz`
- Yashirin nusxa (Bcc): o'zingizning zaxira pochtangiz
- Mavzu (Subject): «8-sinf CS 2-hafta uy vazifasi - [Ismingiz]»
- Xat matnida salomlashish, vazifa nima haqida ekanligi va fayl biriktirilganligi yozilsin.
**Yechim:**
- **To:** `mentor@maktab.uz`
- **Bcc:** `shaxsiy_zaxira@gmail.com`
- **Subject:** `8-sinf CS 2-hafta uy vazifasi - Sherzod Alimov`
- **Body:**
  ```text
  Assalomu alaykum, hurmatli ustoz!

  Men 8-sinf o'quvchisi Sherzod Alimovman. Ushbu xatga 2-hafta bo'yicha tayyorlangan amaliy uy vazifasi hujjatini biriktirdim.
  Iltimos, tekshirib o'z xulosangizni bersangiz.

  Hurmat bilan,
  Sherzod Alimov.
  ```
- **Biriktirish:** Pastdagi qisqich (paperclip) belgisini bosib, fayl tanlanadi va `Send` (Yuborish) bosiladi.

---

## 4. Tezkor nazorat savollari (javoblari bilan)

1. **Savol:** Internet bilan World Wide Web (WWW) ning farqi nimada?
   **Javob:** Internet — bu butun dunyodagi kompyuterlarni bog'lovchi global apparat/tarmoq infratuzilmasi. WWW esa internet ustida ishlovchi, veb-saytlar va gipermatnli sahifalar tizimidir.
2. **Savol:** Brauzerdagi Kesh (Cache) va Kuki (Cookies) nima vazifani bajaradi?
   **Javob:** Kesh sayt tezroq ochilishi uchun sahifa qismlarini (rasmlar, stillar) xotirada saqlaydi. Kuki esa sayt sozlamalari, foydalanuvchi ma'lumotlari va tizimga kirish holatini eslab qoladi.
3. **Savol:** Google'da faqat PDF formatidagi ma'lumotlarni qidirish uchun qaysi operator ishlatiladi?
   **Javob:** `filetype:pdf` operatori ishlatiladi.
4. **Savol:** Elektron pochtada `Cc` va `Bcc` maydonlarining farqi nimada?
   **Javob:** `Cc` (nusxa) barcha qabul qiluvchilarga ko'rinadi. `Bcc` (yashirin nusxa) dagi manzillarni asosiy qabul qiluvchilar ko'ra olmaydi.
5. **Savol:** Fishing (phishing) xati qanday xavf tug'diradi?
   **Javob:** Fishing xatlari foydalanuvchini aldab soxta saytga kiritadi va uning login, parol yoki bank karta ma'lumotlarini o'g'irlashga harakat qiladi.
