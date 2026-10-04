# 6-dars: Foydalanuvchi tarixi va senariysini yozish (User Story & User Journey Map)

**Fan:** Advanced UX/UI dizayn va Advanced Front-end  
**Sinf:** 10-sinf  
**Hafta:** 2-hafta, 3-dars (umumiy 6-dars)  
**Dars davomiyligi:** 80 daqiqa  

---

## Darsning maqsadi

O'quvchilarga raqamli mahsulot loyihalashda **User Story (Foydalanuvchi hikoyasi)**, **User Scenario (Foydalanuvchi ssenariysi)** hamda **User Journey Map (Foydalanuvchi sayohati xaritasi)** tushunchalarini o'rgatish; Agile/Scrum tizimidagi standart hikoya shablonini (`"As a..., I want..., so that..."`), yirik Epiklarni mayda hikoyalarga bo'lish qoidalarini hamda qabul qilish mezonlarini (Acceptance Criteria) shakllantirish ko'nikmalarini berish; bosqichlar (Stages), teginish nuqtalari (Touchpoints) va his-tuyg'ular grafigi (Emotional Journey) bo'yicha to'liq sayohat xaritasini chizishni o'rgatish.

---

## Kutilayotgan natijalar (O'quvchi bilishi kerak)

- User Story, User Scenario va Use Case tushunchalarining asosiy farqlari va qo'llanish o'rnini bilish;
- Standart User Story formatini (`"[Foydalanuvchi turi] sifatida, men [biror amalni] bajarmoqchiman, shunda [aniq foyda] olaman"`) mustaqil yoza olish;
- Epik (katta hikoya) tushunchasini bilish va uni sprintlarga mos kichik hikoyalarga bo'lishni o'rganish;
- Har bir hikoyaga aniq Qabul qilish mezonlarini (Acceptance Criteria) yoza olish;
- User Journey Map (UJM) ning asosiy ustunlari va qatorlarini (Bosqichlar, Foydalanuvchi amallari, Fikrlari, Hissiy egri chiziq, Muammolar va Imkoniyatlar) tuza olish.

---

## Kerakli jihozlar va vositalar

- Kompyuter yoki noutbuk;
- Veb-brauzer, Figma yoki FigJam dasturi;
- Qog'oz stikerlar (stroyboard va sayohat xaritasi chizish uchun);
- Proyektor yoki monitor.

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 min** | Tashkiliy qism va takrorlash | Persona va Empatiya xaritasi (Says, Thinks, Does, Feels) bo'yicha savol-javob |
| **10–25 min** | Yangi mavzu: User Story va uning formulasi | Agile/Scrum hikoyalari, Epiklar, qabul shartlari (Acceptance Criteria) |
| **25–45 min** | User Scenario vs Use Case | Hayotiy kontekstli ssenariy (storytelling) va texnik tizim harakatlari (Use Case) |
| **45–60 min** | User Journey Map (UJM) tuzilishi | Bosqichlar (Awareness -> Consideration -> Purchase -> Retention), Touchpoints va his-tuyg'ular grafigi |
| **60–75 min** | Amaliy mashg'ulot | FinTech yoki Onlayn do'kon loyihasi uchun 3 ta User Story va to'liq User Journey Map tuzish |
| **75–80 min** | Xulosa va 2-hafta yakuni | 2-hafta mavzularini jamlash, baholash va uyga vazifa |

---

## Nazariy ma'lumotlar

### 1. User Story (Foydalanuvchi hikoyasi) nima?

**User Story:** Agile dasturiy ta'minot yaratish metodologiyasida foydalanuvchi ehtiyojini uning o'z nuqtayi nazaridan qisqa, sodda va tushunarli ifodalovchi talab formatidir.

**Standart formula:**
$$\text{"[Foydalanuvchi turi] sifatida, men [biror amalni] xohlayman, shunda [aniq foyda/qiymat] olaman."}$$

*Misol:*
*"Onlayn xaridor sifatida, men tovarlarni narxi bo'yicha saralashni xohlayman, shunda byudjetimga mos mahsulotni tezroq topa olaman."*

**Epik (Epic) va bo'linish:**
Haddan tashqari katta, bitta iteratsiyaga sig'maydigan hikoya **Epik** deb ataladi. Masalan:
- *Epik:* "Foydalanuvchi sifatida men tizimda to'liq onlayn to'lov qila olaman."
- *Kichik User Story 1:* "Xaridor sifatida, men plastik karta orqali to'lashni xohlayman, shunda naqd pul qidirmayman."
- *Kichik User Story 2:* "Xaridor sifatida, men to'lov chekini PDF formatda yuklab olishni xohlayman, shunda hisobotimni buxgalteriyaga bera olaman."

**Qabul qilish mezonlari (Acceptance Criteria):**
Hikoya to'liq bajarilgan deb qabul qilinishi uchun qoniqtirilishi shart bo'lgan aniq shartlar ro'yxati (masalan: "Karta raqami kiritilganda bank turi avtomatik aniqlanishi kerak", "SMS tasdiqlash kodi 60 soniya ichida kelishi kerak").

### 2. User Scenario va Use Case farqi

- **User Story:** Yuqori darajadagi ehtiyoj (Nima kerak va nima uchun?).
- **User Scenario:** Kontekst va hayotiy hikoya (Foydalanuvchi kim, qayerda, qanday holatda va qanday ketma-ketlikda ushbu ishni amalga oshirdi?).
- **Use Case:** Tizimli va texnik bosqichlar (Foydalanuvchi tugmani bosdi -> Tizim ma'lumotlar bazasini tekshirdi -> Tizim muvaffaqiyat xabarini chiqardi).

### 3. User Journey Map (Foydalanuvchi sayohati xaritasi)

**User Journey Map (UJM):** Foydalanuvchining muayyan maqsadga erishish yo'lidagi barcha bosqichlarini, raqamli mahsulot bilan to'qnashuv nuqtalarini (Touchpoints) va bu jarayondagi hissiy holatini (Emotional curve) xronologik tartibda aks ettiruvchi vizual xaritadir.

**UJM ning 5 ta asosiy qatori:**
1. **Bosqichlar (Stages):** Ehtiyoj paydo bo'lishi -> Saytga kirish -> Qidiruv -> Xarid -> Yetkazib berish.
2. **Harakatlar (User Actions):** Foydalanuvchi ayni bosqichda aynan nima ish qiladi?
3. **Tegish nuqtalari (Touchpoints):** Qaysi qurilma, reklama, veb-sahifa yoki mobil ilova bilan o'zaro aloqada bo'ladi?
4. **Hissiy egri chiziq (Emotional Journey):** Quvonch, qiziqish, ikkilanish, asabiylik (pasayish) yoki qoniqish (ko'tarilish).
5. **Muammolar va Imkoniyatlar (Pain points & Opportunities):** Har bir tushkunlik nuqtasida UX dizayner qanday yechim bera oladi?

---

## Amaliy mashg'ulot va topshiriqlar

### 1-topshiriq. Xato yozilgan User Storyni standart formulaga keltirish (oson)
Quyidagi 3 ta noto'g'ri (texnik yoki maqsadsiz) yozilgan hikoyani Agile standartidagi formula bo'yicha qayta yozing:
1. `Saytga qidiruv paneli qo'yish kerak, Elasticsearch ishlatilsin.`
2. `Dasturchilar foydalanuvchilar parolini shifrlab saqlashi shart.`
3. `Men talabaman, menga push-bildirishnomalar yoqadi.`

**Yechim:**
1. `Onlayn xaridor sifatida, men qidiruv maydoni orqali tovar nomini yozib topishni xohlayman, shunda katalogda uzoq vaqt sarflamayman.`
2. `Foydalanuvchi sifatida, men shaxsiy hisobim xavfsiz himoyalangan bo'lishini xohlayman, shunda shaxsiy ma'lumotlarim va mablag'im begonalarga o'tib ketmaydi.`
3. `Maktab o'quvchisi sifatida, men yangi dars boshlanishidan 10 daqiqa oldin eslatma olishni xohlayman, shunda muhim onlayn mashg'ulotni o'tkazib yubormayman.`

### 2-topshiriq. User Story uchun Acceptance Criteria (Qabul shartlari) yozish (o'rta)
Quyidagi User Story uchun kamida 4 ta aniq qabul qilish mezonini ishlab chiqing:  
*"Mobil ilova foydalanuvchisi sifatida, men o'z profilim parolini telefon raqamimga keladigan SMS-kod orqali tiklashni xohlayman, shunda eski parolimni unutganimda ham ilovadan foydalanishni davom ettira olaman."*

**Yechim:**
- **Shart 1:** Foydalanuvchi ro'yxatdan o'tgan telefon raqamini kiritganda 6 xonali SMS tasdiq kodi yuborilishi kerak.
- **Shart 2:** SMS kod kiritish uchun 60 soniyalik taymer ko'rinishi va tugagach "Qayta kod yuborish" tugmasi faollashishi lozim.
- **Shart 3:** Yangi parol kamida 8 ta belgidan iborat bo'lishi va murakkablik darajasi indikatori bilan ko'rsatilishi shart.
- **Shart 4:** Parol muvaffaqiyatli yangilangach, barcha boshqa faol sessiyalardan chiqib ketish haqida ogohlantirish berilishi kerak.

### 3-topshiriq. Onlayn dori buyurtma qilish ilovasi uchun User Journey Map (qiyin)
Bemor kechasi favqulodda dori buyurtma qilmoqchi. Ushbu ssenariy bo'yicha 4 ta bosqichdan iborat UJM jadvalini (Bosqich, Harakat, Fikr, Hissiyot, UX Yechim) tuzing.

**Yechim:**
| Bosqich | Foydalanuvchi harakati | Fikrlari (Quotes) | Hissiyot (1-5) | UX Yechim va Imkoniyat |
|---|---|---|---|---|
| **1. Qidiruv** | Ilovani ochib, kerakli antibiotik nomini qidiradi | *"Bu dori yaqin atrofdagi dorixonada bormikan?"* | 3 (Xavotir) | Qidiruvda dorining eng yaqin 24/7 ochiq dorixonadagi mavjudligini ko'rsatish |
| **2. Tanlov** | Retsept talab qilinishini ko'radi va narxni solishtiradi | *"Shifokor retseptini qanday yuklasam bo'ladi?"* | 2 (Qiyinchilik) | Kameradan retsept suratini 1 bosishda yuklash imkoniyati |
| **3. Buyurtma** | To'lov qiladi va manzilni ko'rsatadi | *"Kuryer kechasi adashib ketmay yetib kelarmikin?"* | 3 (Kutish) | Xaritada kuryerning jonli harakatini ko'rsatish |
| **4. Qabul qilish** | Dorini qabul qilib oladi | *"Juda tez yetib keldi, katta rahmat!"* | 5 (Minatdorlik) | Buyurtma tarixida dori qabul qilish vaqti bo'yicha eslatma o'rnatish |

---

## Tezkor nazorat savollari

1. User Story ning 3 ta asosiy komponenti qaysilar?
   - *Javob:* Kim (Role/User), Nima (Action/Desire), Nega (Benefit/Value).
2. Epik nima va u bilan qanday ishlanadi?
   - *Javob:* Katta hajmli umumiy hikoya; u bitta sprintda bajarilishi uchun bir nechta kichik User Storylarga bo'linadi.
3. Acceptance Criteria (Qabul shartlari) nima uchun zarur?
   - *Javob:* Ishlab chiquvchi va dizayner vazifa to'liq va to'g'ri bajarilganini bir xil tushunishi hamda testlash oson bo'lishi uchun.
4. User Journey Map (UJM) dagi "Touchpoint" nima?
   - *Javob:* Foydalanuvchining brend yoki mahsulot bilan bevosita to'qnash keladigan har qanday aloqa nuqtasi (sayt, SMS, kuryer, ilova).

---

## Keng tarqalgan xatolar va ularning oldini olish

- **Foydani (So that...) unutib qoldirish:** Shunchaki "Men tugmani bosmoqchiman" deb yozish xato. Har doim ushbu amal foydalanuvchiga qanday aniq foyda keltirishi ko'rsatilishi shart.
- **UJM ni faqat "baxtli yo'l" (Happy path) qilib chizish:** Foydalanuvchi yo'lida doim muammolar (kartada pul yetmasligi, internet uzilishi) uchraydi. Haqiqiy UJM aynan shu pasayish nuqtalarini ko'rsatib, ularga yechim topishi lozim.
