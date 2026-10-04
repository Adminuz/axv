---
title: "9-dars. 6-dars: Foydalanuvchi tarixi va senariysini yozish (User Story & User Journey Map)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (UX/UI)", "link": "/10-sinf-uxui/"}, "week": {"n": 2, "link": "/10-sinf-uxui/hafta-02/"}, "g": 9, "title": "6-dars: Foydalanuvchi tarixi va senariysini yozish (User Story & User Journey Map)", "lead": "Ikonka, tugma va navigatsiya elementlarini dizayni (UI Kit)", "slide": "/slaydlar/10-sinf-uxui/hafta-02/dars-6.html", "tabs": [{"g": 7, "link": "/10-sinf-uxui/hafta-02/dars-4", "current": false}, {"g": 8, "link": "/10-sinf-uxui/hafta-02/dars-5", "current": false}, {"g": 9, "link": "/10-sinf-uxui/hafta-02/dars-6", "current": true}], "prev": {"g": 8, "title": "5-dars: Persona va empatiya xaritasini yaratish", "link": "/10-sinf-uxui/hafta-02/dars-5"}, "next": null}
---

**Sinf:** 10-sinf  
**Yo'nalish:** Advanced UX/UI dizayn va Advanced Front-end  
**Hafta:** 2-hafta, 3-dars  

---

<div class="blk">

## <Icon name="file-text" /> Darsning qisqacha mazmuni

Ushbu darsda biz raqamli mahsulot talablarini ifodalashning xalqaro Agile standarti — **User Story (Foydalanuvchi hikoyasi)**, batafsil hayotiy vaziyatlarni tasvirlovchi **User Scenario (Foydalanuvchi ssenariysi)** hamda butun tajriba xaritasini chizuvchi **User Journey Map (Foydalanuvchi sayohati xaritasi)** bilan tanishamiz. Siz standart hikoya shablonini, katta Epiklarni bo'lish qoidalarini, Qabul mezonlarini (Acceptance Criteria) va foydalanuvchining his-tuyg'ulari grafigini tuzishni o'rganasiz.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar va atamalar

| Atama | Inglizcha | Tavsif |
|---|---|---|
| **User Story** | User Story | Foydalanuvchi nuqtayi nazaridan yozilgan qisqa va aniq talab ("As a..., I want..., so that...") |
| **Epik** | Epic | Bitta sprintga sig'maydigan, bir nechta kichik hikoyalarga bo'linuvchi yirik funksionallik |
| **Acceptance Criteria**| Acceptance Criteria | Hikoya to'liq va to'g'ri bajarilgan deb hisoblanishi uchun zarur bo'lgan shartlar ro'yxati |
| **User Scenario** | User Scenario | Foydalanuvchining mahsulot bilan muloqotini hikoya (kontekst) tarzida yorituvchi tavsif |
| **Use Case** | Use Case | Tizim muayyan natijaga erishish uchun bajaradigan texnik amallari ketma-ketligi |
| **User Journey Map** | User Journey Map (UJM)| Foydalanuvchining maqsad sari bosib o'tgan barcha bosqichlari va his-tuyg'ulari xaritasi |
| **Touchpoint** | Touchpoint | Foydalanuvchi mahsulot yoki xizmat bilan to'qnashadigan har qanday aloqa nuqtasi |

---

</div>

<div class="blk">

## <Icon name="file-text" /> Nazariy xulosa

### 1. User Story standart formulasi
$$\text{"[Foydalanuvchi roli] sifatida, men [biror amalni] xohlayman, shunda [aniq foyda] olaman."}$$
- **Rol:** Kim? (O'quvchi, xaridor, haydovchi).
- **Harakat:** Nima qilmoqchi? (Filtrlamoqchi, yuklab olmoqchi).
- **Qiymat/Foyda:** Nima uchun kerak? (Vaqtni tejash, adashmaslik).

### 2. Uch vosita farqi
- **User Story:** "Nima kerak va nima uchun?" (Agile talab).
- **User Scenario:** "Qanday vaziyatda va qanday kontekstda ishlatiladi?" (Hayotiy hikoya).
- **Use Case:** "Tizim qanday javob qaytaradi?" (Texnik qadamlar).

### 3. User Journey Map (UJM) ning 5 qatori
1. **Bosqichlar (Stages):** Qidiruv -> Ko'rish -> Xarid -> Qabul qilish.
2. **Harakatlar (Actions):** Bosqichda bajariladigan amallar.
3. **Tegish nuqtalari (Touchpoints):** Sayt, mobil ilova, SMS, kuryer.
4. **Hissiy egri chiziq (Emotional curve):** Tushkunlik va quvonch lahzalari.
5. **UX Imkoniyatlari (Opportunities):** Muammoni bartaraf etuvchi dizayn yechimlari.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Mustaqil bajarish uchun topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Agile tizimidagi standart User Story formulasining 3 ta asosiy bo'lagini yozing va formulaga bitta hayotiy misol keltiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Epik (Epic) nima va nima sababdan dasturiy loyihalarda Epiklar mayda User Storylarga bo'linadi?

### 3-topshiriq <Badge type="tip" text="oson" />
User Journey Map dagi "Touchpoint" (aloqa nuqtasi) tushunchasiga 3 ta misol keltiring (masalan, yetkazib berish xizmati uchun).

### 4-topshiriq <Badge type="warning" text="o'rta" />
Quyidagi noto'g'ri (texnik) yozilgan talabni standart User Story formulasiga keltiring:  
`"Ma'lumotlar bazasiga foydalanuvchilar manzilini saqlash jadvali qo'shilsin."`

### 5-topshiriq <Badge type="warning" text="o'rta" />
User Story va Use Case o'rtasidagi asosiy farqni 2 jumlada tushuntiring. Nima uchun Use Case ko'proq dasturchilar uchun kerak bo'ladi?

### 6-topshiriq <Badge type="warning" text="o'rta" />
Quyidagi User Story uchun 3 ta aniq Qabul qilish mezonini (Acceptance Criteria) yozing:  
*"Onlayn o'quvchi sifatida, men dars videosining tezligini (0.5x, 1x, 1.5x, 2x) o'zgartirishni xohlayman, shunda mavzuni o'zlashtirish tezligimga moslasha olaman."*

### 7-topshiriq <Badge type="warning" text="o'rta" />
Nima uchun User Journey Map faqat "baxtli yo'l"ni (muammosiz ideal holatni) emas, balki foydalanuvchining hafsalasi pir bo'lgan salbiy nuqtalarini ham ko'rsatishi shart?

### 8-topshiriq <Badge type="danger" text="qiyin" />
Onlayn taksi buyurtma qilish ilovasi uchun quyidagi Epikni 3 ta kichik User Storyga bo'ling:  
**Epik:** *"Yo'lovchi sifatida men taksi safari uchun to'liq to'lovni amalga oshira olaman."*

### 9-topshiriq <Badge type="danger" text="qiyin" />
Maktab kutubxonasidan kitob olish jarayoni uchun 4 bosqichli User Journey Map jadvalini tuzing:
- 1-bosqich: Kitob qidirish;
- 2-bosqich: Mavjudligini tekshirish;
- 3-bosqich: Band qilish (Reserve);
- 4-bosqich: Kitobni qabul qilish.  
Har bir bosqich uchun foydalanuvchi harakati, his-tuyg'usi va UX yechimini ko'rsating.

### 10-topshiriq <Badge type="info" text="bonus" />
Figma yoki FigJamda elektron ta'lim platformasi uchun foydalanuvchining "Birinchi marta ro'yxatdan o'tish va test topshirish" jarayoni aks etgan to'liq vizual User Journey Map chizmasini tayyorlang (hissiyotlar grafigi bilan).

</div>

