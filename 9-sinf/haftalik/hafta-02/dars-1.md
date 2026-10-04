# 4-dars. Foydalanuvchi ssenariysi, User Flow va Customer Journey Map (CJM)

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + dizayn amaliyoti · **I-bob**, 4-dars

## 1. Dars rejasi

**Maqsad:** o'quvchi foydalanuvchi personasi asosida ilovadan foydalanish ssenariysini (User Scenario) yoza oladi, maqsadga erishish qadamlarini blok-sxema ko'rinishidagi User Flow'ga aylantiradi va foydalanuvchining his-tuyg'ularini ifodalovchi sodda Customer Journey Map (CJM) tuza oladi.

**Kutiladigan natija:**
- Foydalanuvchi ssenariysi (User Scenario) nima ekanini va uning tuzilishini (Kim? Qayerda? Nima maqsad? Qanday harakatlar?) tushuntiradi.
- User Flow (foydalanuvchi oqimi) tushunchasini biladi, shartli tarmoqlanishlarni (ha/yo'q) ifodalay oladi.
- Customer Journey Map (CJM) bosqichlarini (xabardor bo'lish, qidirish, qaror qabul qilish, amal bajarish, taassurot) ajratadi.
- Tanlangan mobil ilova yoki sayt (masalan, kitob buyurtma qilish yoki taksi chaqirish) uchun to'liq ssenariy va User Flow chizadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 | Takrorlash | 1-hafta (UX va UI farqi, tadqiqot usullari, Persona kartasi) |
| 10–30 | Yangi mavzu 1 | Foydalanuvchi ssenariysi: hikoya yaratish, kontekst va maqsad |
| 30–40 | Yangi mavzu 2 | User Flow: qadamlar, harakatlar va qarorlar sxemasi |
| 40–45 | Tanaffus | |
| 45–55 | Yangi mavzu 3 | Customer Journey Map (CJM) va og'riq nuqtalari |
| 55–75 | Amaliyot | "Mobile_Book" yoki "Taksi buyurtma" ilovasi uchun User Flow chizish |
| 75–80 | Tezkor nazorat va xulosa | 5 ta savol, xulosa |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- Persona nima? (Bizning mahsulotimizdan foydalanuvchi xayoliy, ammo real ma'lumotlarga asoslangan qahramon).
- Nega dizayner loyihani chizishdan oldin tadqiqot o'tkazishi kerak?

### 2.2. Foydalanuvchi ssenariysi (User Scenario) nima?
**Foydalanuvchi ssenariysi** — bu muayyan personaning o'z maqsadiga erishish uchun raqamli mahsulotdan qanday foydalanishini tavsiflovchi qisqa hikoyadir.
Dizayner interfeys chizishdan oldin: "Foydalanuvchi ilovaga qanday holatda kiradi va nima qilmoqchi?" degan savolga javob yozib olishi kerak.

Ssenariy 4 ta asosiy savolga javob beradi:
1. **Kim?** (Persona: yoshi, kasbi, odatlari).
2. **Qayerda va qachon?** (Kontekst: avtobusda, tunda, shoshilinchda, kompyuter qarshisida).
3. **Nima maqsadda?** (Ehtiyoj: kitob topish, chipta sotib olish, ovqat buyurtma qilish).
4. **Qanday qadamlar bilan?** (Ilovadagi harakatlar zanjiri).

*Misol:*
> "10-sinf o'quvchisi Shaxnoza darsdan keyin fizika fanidan ilmiy maqola tayyorlashi kerak. U uyga ketayotib avtobusda 'Mobile_Book' ilovasini ochadi. Qidiruv paneliga 'Kvant fizikasi' deb yozadi, natijalar orasidan eng yuqori baholangan kitobni tanlaydi, uning mundarijasi va qisqa mazmuni bilan tanishib, PDF formatini telefoniga yuklab oladi."

Ushbu ssenariydan bizga qanday interfeys elementlari kerakligi darhol oydinlashadi:
- Qidiruv qatori;
- Natijalar ro'yxati (muqova, nom, reyting bilan);
- Kitob tafsilotlari sahifasi (mundarija, izoh);
- "Yuklab olish" tugmasi.

### 2.3. User Flow (Foydalanuvchi oqimi)
Ssenariy matn ko'rinishida bo'lsa, **User Flow** — foydalanuvchi ekranda bosadigan qadamlarning vizual xaritasi yoki blok-sxemasidir.

User Flow elementlari:
- **To'rtburchak:** Sahifa yoki ekran (masalan: "Bosh sahifa", "Savat", "To'lov ekrani").
- **Doira / Oval:** Boshlanish yoki tugash nuqtasi.
- **Romb (Qaror qabul qilish):** Shartli savollar (masalan: "Tizimga kirganmi? Ha bo'lsa → Buyurtmaga o'tish; Yo'q bo'lsa → Login oynasiga o'tish").
- **Strelkalar (O'qlar):** Foydalanuvchi bosgan tugma yoki o'tish yo'nalishi.

User Flow orqali dizayner foydalanuvchining "tupik"ka (chiqish yo'li yo'q holatga) tushib qolmasligini kafolatlaydi.

### 2.4. Customer Journey Map (CJM — Mijoz tajribasi xaritasi)
CJM — foydalanuvchining mahsulot bilan birinchi tanishuvidan to maqsadiga yetguniga qadar bo'lgan hissiy yo'li.
CJM 5 bosqichdan iborat:
1. **Xabardorlik (Awareness):** Muammoni his qilish yoki reklama ko'rish.
2. **Ko'rib chiqish (Consideration):** Ilovani yuklab olish va variantlarni solishtirish.
3. **Qaror / Harakat (Action):** Mahsulotni xarid qilish yoki xizmatdan foydalanish.
4. **Foydalanish (Usage):** Ilova bilan bevosita ishlash.
5. **Sodiqlik (Loyalty):** Qoniqish hosil qilish, tavsiya qilish yoki qayta kirish.

CJM da har bir bosqichda foydalanuvchining **og'riq nuqtalari (pain points)** va uning hissiy holati (quvonch, ikkilanish, asabiylashish) qayd etiladi. Masalan, "ro'yxatdan o'tish juda uzun bo'lib, odamni asabiylashtirdi" degan og'riq nuqtasi dizaynerga loginni bitta tugmali (Google orqali) qilish kerakligini ko'rsatadi.

---

## 3. Amaliy topshiriqlar

### 1-topshiriq. "Kitob buyurtma qilish" ssenariysi
Keltirilgan Shaxnoza personasiga asoslanib, kitob buyurtma qilish jarayonining to'liq ssenariysini yozing.

**Yechim:**
```markdown
**Ssenariy nomi:** "Mobile_Book"da elektron kitob yuklab olish
**Qahramon:** Shaxnoza, 16 yosh, abituriyent.
**Kontekst:** Uyda kechqurun, dars tayyorlamoqda.
**Qadamlar:**
1. Shaxnoza ilovani ochadi.
2. Qidiruv qatoriga "O'tkan kunlar" deb yozadi.
3. Qidiruv natijalaridan kitob kartasini bosadi.
4. Kitob sahifasida kitob tili, hajmi va o'quvchilar fikrini o'qiydi.
5. "Yuklab olish" tugmasini bosadi.
6. Tizim muvaffaqiyatli yuklanganligi haqida bildirishnoma beradi.
7. Shaxnoza kitobni "Mening kutubxonam" bo'limida ko'radi.
```

### 2-topshiriq. User Flow blok-sxemasi
Yuqoridagi ssenariy asosida kamida bitta shartli romb ("Tizimda bormi?") qatnashgan User Flow chizing (qog'ozda yoki FigJam'da).

**Yechim:**
```
[Bosh sahifa] 
      │
      ▼ (Qidiruv maydoniga yozadi)
[Qidiruv natijalari]
      │
      ▼ (Kitobni tanlaydi)
[Kitob tafsilotlari]
      │
      ▼ ("Yuklab olish" tugmasini bosadi)
   < Tizimga kirganmi? >
      ├── (Yo'q) ──► [Login / Ro'yxatdan o'tish] ──► [Muvaffaqiyatli]
      └── (Ha) ───────────────────────────────────► [Yuklab olish yakunlandi]
```

### 3-topshiriq. Og'riq nuqtasini yechish (CJM tahlili)
Foydalanuvchi taksi chaqirish ilovasida mashina qidirish 10 daqiqadan oshganda asabiylashmoqda. Bu og'riq nuqtasini UI/UX dizayn orqali qanday hal qilasiz?

**Yechim:**
1. Ekran markazida mashinalar qidirilayotganligini ko'rsatuvchi interaktiv radar animatsiyasini qo'yish (noaniqlikni kamaytiradi).
2. "Haydovchiga qo'shimcha haq taklif qilish" yoki "Boshqa tarifni (masalan, Komfort) tanlash" tezkor tugmalarini chiqarish.
3. Taxminiy kutish vaqtini daqiqalarda ko'rsatib turish.

---

## 4. Tezkor nazorat (5 daqiqa)

1. Foydalanuvchi ssenariysi qaysi 4 ta asosiy savolga javob beradi?
   - **Javob:** Kim? Qayerda va qachon? Nima maqsadda? Qanday qadamlar bilan?
2. User Flow sxemasida to'rtburchak va romb shakllari nimani anglatadi?
   - **Javob:** To'rtburchak — ekran yoki sahifani; romb — shartli tanlov/qaror qabul qilish nuqtasini.
3. User Flow dizaynerga qanday asosiy xatodan qochishga yordam beradi?
   - **Javob:** Foydalanuvchi chiqib ketolmaydigan "tupik" holatlarga tushib qolishining va ortiqcha bosqichlarning oldini oladi.
4. Customer Journey Map (CJM) da "og'riq nuqtasi" (pain point) nima?
   - **Javob:** Foydalanuvchi ilovadan foydalanish jarayonida duch keladigan qiyinchilik, tushunmovchilik yoki salbiy his-tuyg'ular.
5. Ssenariy va User Flow o'rtasidagi asosiy farq nima?
   - **Javob:** Ssenariy — matnli hikoya, User Flow — uning vizual blok-sxemasi.

---

## 5. Xulosa va keyingi darsga ko'prik
Bugun biz foydalanuvchining ilova ichidagi harakatlarini ssenariy va User Flow yordamida loyihalashni o'rgandik.
**Keyingi dars (5-dars):** Chizilgan sxemalar asosida interfeysning birinchi skeletini — **Wireframe** yaratishni va bu boradagi eng qulay dastur **Balsamiq** bilan ishlashni boshlaymiz!
