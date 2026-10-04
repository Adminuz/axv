# 1-dars. Ma’lumot tushunchasi, uning turlari va DIKW modeli

> Raqamlar olamiga kirish: xom ma'lumotlar qanday qilib foydali axborot, chuqur bilim va oqilona qarorlarga aylanishini DIKW piramidasi orqali kashf eting.

## Dars xulosasi

- Ma’lumot (data) — bu voqelik, jarayonlar yoki hodisalar haqidagi xom, qayta ishlanmagan faktlar to‘plamidir.
- Ma’lumot o‘z-o‘zidan xulosa bermaydi; unga ma’no va kontekst berilgandagina u axborotga aylanadi.
- Miqdoriy ma’lumotlar sonlar bilan ifodalanadi va ikki turga bo‘linadi: diskret (butun sonlar) va uzluksiz (o‘lchanadigan kasr qiymatlar).
- Sifat ma’lumotlari toifalar, belgilar va matnli tavsiflar orqali ifodalanadi (masalan, rang, mamnunlik darajasi).
- Strukturaviy ma’lumotlar qat’iy ustun va satrlarga ega bo‘lib (Excel, SQL), tahlil uchun eng qulay hisoblanadi.
- Nostrukturaviy ma’lumotlar (tasvirlar, audio, video) dunyodagi ma’lumotlarning 80% dan ortig‘ini tashkil etadi.
- DIKW piramidasi to‘rtta pog‘onadan iborat: Data (Ma’lumot) → Information (Axborot) → Knowledge (Bilim) → Wisdom (Donolik).

---

## Qo'shimcha ma'lumot

### 1. Nega xom ma'lumotning o'zi yetarli emas?
Tasavvur qiling, sizga shunchaki "42, 100, Toshkent" degan yozuv berildi. Bu sonlar nimani anglatadi? Avtobus raqamimi, haroratmi yoki mahsulot narximi? Ma’lumot kontekstsiz bo‘lsa, u inson uchun ham, kompyuter uchun ham tushunarsiz shovqin (noise) hisoblanadi. 
Ammo agar biz "Toshkent shahridagi 42-maktabda 100 nafar o'quvchi xalqaro olimpiadada qatnashdi" desak, bu darhol qimmatli **axborotga** aylanadi.

### 2. Diskret va Uzluksiz miqdorlar farqi
- **Diskret (Discrete):** Faqat butun sonlar bilan sanaladi. Siz 2.5 nafar o'quvchi yoki 3.7 ta avtomobil deya olmaysiz. Ular doimo butun: 1, 2, 3, 4...
- **Uzluksiz (Continuous):** O'lchov asbobi (termometr, tarozi, sekundomer) yordamida olinadi va istalgan aniqlikdagi o'nlik kasr bo'lishi mumkin: 36.6°C, 75.45 kg, 12.38 soniya.

### 3. Yarim-strukturaviy ma'lumotlar: JSON formati
Zamonaviy veb-saytlar va mobil ilovalar bir-biri bilan aloqa qilganda ko'pincha JSON (JavaScript Object Notation) formatidan foydalanadi. Unda qat'iy jadval bo'lmasada, kalit va qiymatlar juftligi mavjud:
```json
{
  "ism": "Jasur",
  "yosh": 15,
  "fanlar": ["Matematika", "Informatika"],
  "ball": 94.5
}
```
Bu tuzilma relyatsion jadvaldan ko'ra moslashuvchan bo'lib, ijtimoiy tarmoqlar va mobil ilovalarda keng qo'llaniladi.

### 4. DIKW zanjiri — amaliy biznes keysi
Navbatdagi jadval DIKW bosqichlarining savdo markazidagi hayotiy tatbiqini ko'rsatadi:

| Bosqich | Savol | Misol |
|---|---|---|
| **Data** | Nima bor? | `1200`, `soyabon`, `15-aprel` |
| **Information** | Qayerda va qachon? | 15-aprel kuni yomg'ir yoqqanda 1200 dona soyabon sotildi |
| **Knowledge** | Nega shunday bo'ldi? | Yomg'irli kunlarda shahar markazidagi do'konlarda soyabon savdosi 400% ga oshadi |
| **Wisdom** | Nima qilish kerak? | Ertangi ob-havo ma'lumotiga ko'ra yomg'ir kutilmoqda. Barcha filiallar oldiga soyabon stendlarini o'rnatish lozim |

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Data (Ma'lumot)** | Real olam hodisalari haqidagi xom, qayta ishlanmagan faktlar va o'lchovlar. |
| **Information (Axborot)** | Ma'no, kontekst va maqsad yuklangan qayta ishlangan ma'lumot. |
| **Knowledge (Bilim)** | Tahlil, tajriba va sabab-oqibat bog'liqliklari asosida shakllangan tushuncha. |
| **Wisdom (Donolik)** | Bilimga tayanib to'g'ri, foydali va uzoq muddatli strategik qarorlar qabul qilish. |
| **Quantitative Data** | Sonlar va miqdorlar orqali ifodalanadigan o'lchanuvchi ma'lumotlar. |
| **Qualitative Data** | Belgilar, toifalar va so'zlar orqali ifodalanadigan sifat ma'lumotlari. |
| **Structured Data** | Qat'iy qator va ustunlarga ega jadvalli ma'lumotlar (Excel, SQL). |
| **Unstructured Data** | Aniq formati bo'lmagan erkin axborotlar (audio, video, fotosurat, matn). |
| **Semi-Structured Data** | Teglar va kalitlar orqali tartiblangan ma'lumotlar (JSON, XML). |
| **Context (Kontekst)** | Ma'lumotning ma'nosini ochib beruvchi atrof-muhit, vaqt va shart-sharoit. |

---

## Bilasizmi?

- Dunyoda har kuni taxminan **328 million terabayt** yangi ma'lumot yaratiladi.
- Insoniyat yaratgan ma'lumotlarning **90% dan ortig'i** so'nggi ikki yil ichida hosil bo'lgan.
- "Data" so'zi lotincha "datum" so'zining ko'pligi bo'lib, "berilgan narsa" yoki "fakt" ma'nosini anglatadi.
- Nostrukturaviy ma'lumotlarni tahlil qilish uchun bugungi kunda Sun'iy intellekt (AI) va Kompyuter ko'rishi (Computer Vision) keng qo'llaniladi.

---

## Topshiriqlar

### 1. Ma'lumot va axborotni ajratish · oson
Quyidagi ikki jumlani o'qing va qaysi biri "xom ma'lumot", qaysi biri "axborot" ekanini aniqlang:
- A: "Javohir, 9-sinf, 85, 92, 78".
- B: "9-sinf o'quvchisi Javohir matematika fanidan 85, fizikadan 92 va ingliz tilidan 78 ball to'pladi".
**Kutiladigan natija:** Har bir jumlaning nima sababdan ma'lumot yoki axborot ekanligi haqida 1 jumlali tushuntirish.

### 2. Miqdoriy turlarni farqlash · oson
Quyidagi qiymatlarni diskret yoki uzluksiz turlarga ajrating:
a) Sinfdagi partalar soni (15 dona);
b) Avtomobil tezligi (65.4 km/soat);
c) Supermarketdagi xarid chekidagi mahsulotlar soni (7 ta);
d) Telefon akkumulyatori quvvati (84.5%).
**Kutiladigan natija:** 4 ta parametrning diskret yoki uzluksizligi aniq ko'rsatilgan ro'yxat.

### 3. Sifat ko'rsatkichlarini aniqlash · oson
Quyidagi ro'yxatdan faqat sifat (qualitative) ma'lumotlarni ajratib yozing:
- Mahsulot narxi (25 000 so'm)
- Mijozning xizmatdan mamnunligi ("Yuqori")
- Xodimning qon guruhi ("AB+")
- Ombor maydoni (120 kv.m)
- Mahsulot ta'mi ("Shirin")
**Kutiladigan natija:** Sifat ma'lumotlari ro'yxati va ularning umumiy xususiyati.

### 4. Jadval strukturasi tahlili · oson
Oddiy qog'ozga yoki matn muharririga o'zingizning oxirgi 3 kundagi xarajatlaringiz haqida strukturaviy jadval tuzing. Jadvalda kamida 3 ta ustun bo'lsin: "Sana", "Xarajat nomi", "Miqdori (so'm)".
**Kutiladigan natija:** 3 ta qator va 3 ta ustundan iborat tartibli jadval.

### 5. Ob-havo stansiyasida DIKW modeli · o'rta
Tog'dagi gidrometeorologiya stansiyasi uchun DIKW piramidasining 4 ta bosqichini tuzing.
- Data: qor qalinligi va harorat bo'yicha xom sonlar.
- Information: oxirgi 24 soatdagi o'zgarishlar.
- Knowledge: qor ko'chishi xavfi qonuniyati.
- Wisdom: FVV (Favqulodda vaziyatlar vazirligi) qabul qiladigan qaror.
**Kutiladigan natija:** Har bir bosqich uchun 1 tadan batafsil jumla.

### 6. JSON ma'lumotidan axborot chiqarish · o'rta
Quyidagi yarim-strukturaviy ma'lumot berilgan:
```json
{
  "shahar": "Samarqand",
  "mehmonlar_soni": 14500,
  "eng_mashhur_manzil": "Registon",
  "qoniqish_foizi": 98.2
}
```
Ushbu JSON ma'lumotini o'qib, turizm bo'limi boshlig'i uchun 2 ta tushunarli axborot xulosasi yozing.
**Kutiladigan natija:** JSON ma'lumotiga asoslangan 2 ta tahliliy jumla.

### 7. Maktab oshxonasi tahlili · o'rta
Maktab oshxonasida haftaning dushanba kunidan juma kunigacha eng ko'p sotilgan 3 ta taom bo'yicha ma'lumot yig'ildi. 
Ushbu ma'lumotlar oshxona mudiriga haftalik xaridlar bo'yicha qanday "Knowledge" (Bilim) va "Wisdom" (Donolik) berishi mumkinligini tushuntiring.
**Kutiladigan natija:** Oshxona misolida bilim va donolik bosqichlarining yozma tavsifi.

### 8. Nostrukturaviy ma'lumotni strukturaviy shaklga keltirish · qiyin
Kompaniya elektron pochtasiga quyidagi xat keldi:
*"Salom, mening ismim Anvar Qodirov. 3-oktyabr kuni buyurtma bergan 1 dona noutbuk sumkam (kod: BG-104) yetib kelmadi. Telefonim: +998901234567."*
Ushbu erkin matndan qanday qilib CRM tizimi uchun mos strukturaviy jadval yozuvini (ustunlar va qiymatlar) hosil qilish mumkin?
**Kutiladigan natija:** Aniq ustun nomlari va ularga moslashtirilgan ma'lumotlar jadvali.

### 9. Shahar transport tizimi uchun DIKW modeli · qiyin
Shahar jamoat transportida o'rnatilgan validatorlar har kuni avtobusga mingan yo'lovchilar kartalarini skanerlaydi.
Ushbu tizim misolida Data bosqichidan (har bir yo'lovchi urgan karta vaqti) to Wisdom bosqichigacha (shahar hokimiyati yangi avtobus yo'nalishlarini ochishi) bo'lgan to'liq jarayonni yoritib bering.
**Kutiladigan natija:** Transport boshqaruvi uchun 4 bosqichli kengaytirilgan DIKW tahlili.

### 10. Mini-tadqiqot: Dunyodagi ma'lumotlar oqimi · bonus
Zamonaviy dunyoda "Big Data" (katta hajmdagi ma'lumotlar) ning qaysi sohalarda eng ko'p hosil bo'layotgani (ijtimoiy tarmoqlar, tibbiyot, bank tizimlari, internet-savdo) bo'yicha kichik taqqoslama hisobot tayyorlang. Qaysi sohada nostrukturaviy ma'lumotlar eng ko'p uchraydi?
**Kutiladigan natija:** Kamida 1 sahifalik tahliliy xulosa va solishtirma tushuntirish.

---

## O'zingizni tekshiring

1. Nima uchun "25" soni o'z holicha ma'lumot hisoblanadi, lekin axborot emas?
2. Diskret va uzluksiz miqdoriy ma'lumotlar o'rtasida qanday asosiy farq bor?
3. Nostrukturaviy ma'lumotlarga 3 ta real misol keltiring.
4. Nima sababdan Excel jadvallari strukturaviy ma'lumotlar toifasiga kiradi?
5. DIKW piramidasida Information va Knowledge bosqichlari bir-biridan nima bilan farqlanadi?
6. Wisdom bosqichining pirovard maqsadi nima?

---

## Uyga vazifa

O'zingiz yoqtirgan biror soha (masalan, sevimli futbol klubingiz, kiber-sport o'yini yoki maktab kutubxonasi) faoliyatini tanlang. Tanlagan sohangiz bo'yicha DIKW piramidasining har bir pog'onasiga mos 1 tadan aniq, hayotiy misol yozing (jami 4 ta pog'ona).
