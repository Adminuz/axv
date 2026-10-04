# 5-dars. Tarmoqlanuvchi algoritm: if va else operatorlari

> Dasturingiz yo‘l ayrilishiga kelib qoldi! Ushbu darsda tarmoqlanuvchi algoritmlar, shart tekshirish, `if` va `else` operatorlari hamda Pythonning eng mashhur xususiyati — tabulyatsiya (chekinish) qoidasini o‘rganamiz.

## Dars xulosasi

- **Tarmoqlanuvchi algoritm** — shartning rost (`True`) yoki yolg‘on (`False`) bo‘lishiga qarab dastur oqimini ikki yo‘ldan biriga yo‘naltiruvchi algoritm.
- `if` — "agar" degani bo‘lib, shart rost bo‘lsa o‘ziga tegishli kod blokini ishga tushiradi.
- `else` — "aks holda" degani bo‘lib, `if` sharti bajarilmagan barcha holatlarda ishga tushadi.
- Har bir `if` va `else` qatori oxirida albatta ikki nuqta (`:`) qo‘yiladi.
- Pythonda bloklar boshqa tillardagi kabi `{}` emas, balki **chekinish (indentation - 4 ta probel)** orqali belgilanadi.
- `son % 2 == 0` sharti orqali sonning juft yoki toqligi bir zumda aniqlanadi.
- Shart operatori yordamida imtihon natijalari (o‘tdi/o‘tmadi), parollar va foydalanuvchi huquqlari tekshiriladi.

## Qo'shimcha ma'lumot

### Nega Pythonda qavslar emas, chekinish (indentation) ishlatiladi?
C++, Java, PHP va JavaScript kabi ko‘pgina tillarda kod bloklari jingalak qavslar `{ ... }` ichiga olinadi. Gvido van Rossum Pythonni yaratayotganida dasturchilarning kodlari toza, tartibli va bir xil o‘qilishini ta'minlashni maqsad qilgan. Agar chekinish majburiy bo‘lmasa, ba'zi dasturchilar kodni chalkashtirib, bir qatorda yoki pala-partish yozib tashlashadi. Pythonda esa chekinish — tilning qat'iy qonunidir. Shuning uchun har qanday Python kodi kitob kabi chiroyli o‘qiladi.

### Bitta if operatori (else bo‘lmasligi mumkinmi?)
Ha! Dasturlashda `else` bo‘lishi har doim ham shart emas. Ba'zan faqat biror holat sodir bo‘lgandagina amal bajarish kerak bo‘ladi:
```python
hisob = 100000
bonus = True

if bonus:
    hisob += 20000

print(f"Jami mablag': {hisob}")
```
Bu yerda agar `bonus` bo‘lmasa, hech narsa qilinmaydi va dastur to‘g‘ridan-to‘g‘ri keyingi qatorga o‘tib ketaveradi.

### Ichma-ich shartlar (Nested if)
Bitta `if` blokining ichida yana boshqa bir `if` operatorini joylashtirish mumkin. Masalan, foydalanuvchi tizimga kirdi, endi uning parolini tekshiramiz:
```python
login = "admin"
parol = "12345"

if login == "admin":
    if parol == "12345":
        print("Tizimga to'liq kirdingiz!")
    else:
        print("Parol noto'g'ri!")
else:
    print("Bunday foydalanuvchi topilmadi.")
```
Ammo ichma-ich `if`larni haddan tashqari ko‘paytirib yubormaslik tavsiya etiladi (kodni o‘qish qiyinlashadi).

### Odatiy xatolar
- Ikki nuqtani unutish: `if x > 0` &rarr; `SyntaxError: expected ':'`
- Chekinish xatosi (IndentationError): `if` dan keyingi qatorni surmasdan yozish &rarr; `IndentationError: expected an indented block after 'if' statement on line ...`
- Probel va Tablarni aralashtirish: Bir joyda Tab, boshqa joyda probel ishlatsangiz, `TabError` paydo bo‘lishi mumkin. VS Code muharriri odatda Tab bosilganda avtomatik 4 ta probel qo‘yadi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Tarmoqlanish | Dasturning shartga qarab turli yo‘llar bo‘yicha ketishi |
| if | Shart rost bo‘lsa ishlovchi operator ("agar") |
| else | Shart yolg‘on bo‘lsa ishlovchi operator ("aks holda") |
| Indentation (Chekinish) | Kod blokini ko‘rsatish uchun satr boshidan 4 ta bo‘sh joy tashlash |
| IndentationError | Chekinish noto‘g‘ri qo‘yilganda chiqadigan sintaktik xatolik |
| Blok (Code block) | Bitta shart yoki funksiyaga tegishli bo‘lgan kodlar guruhi |
| Nested if | Bitta if ichida boshqa if joylashishi (ichma-ich shart) |
| Juft son | 2 ga bo‘lganda qoldiq 0 bo‘ladigan son |

## Bilasizmi?

- Pythondagi 4 ta bo‘sh joy (space) qoidasi PEP 8 (Python rasmiy uslub qo‘llanmasi) da qat'iy standart sifatida belgilab qo‘yilgan.
- Ko‘pgina server xavfsizlik devorlari (Firewall) tarmoqlanuvchi algoritmlar asosida ishlaydi: "Agar kelgan so‘rov shubhali bo‘lsa &rarr; uni blokla; Aks holda &rarr; o‘tkazib yubor".
- Har bir kompyuter prosessori (CPU) ichida millionlab mantiqiy "darvozalar" (Logic Gates: AND, OR, NOT) mavjud bo‘lib, ular aynan `if/else` mantiqi bo‘yicha elektr signallarini boshqaradi.

## Topshiriqlar

### 1. Ball bo‘yicha tekshiruv · oson
O‘quvchining to‘plagan bali `ball = 72` ga teng. Agar ball 60 yoki undan katta bo‘lsa `"O'tdi"`, aks holda `"O'tmadi"` deb chiqaruvchi dastur tuzing.
**Kutiladigan natija:** `O'tdi`

### 2. Juft yoki toqlik · oson
`son = 18`. `% 2 == 0` shartidan foydalanib, sonning juft yoki toqligini aniqlang va konsolga chiqaring.
**Kutiladigan natija:** `18 - juft son`

### 3. Havo harorati · oson
`harorat = -3`. Agar harorat 0 dan kichik bo‘lsa `"Havo sovuq, muzlama bo'lishi mumkin"`, aks holda `"Harorat noldan yuqori"` xabarini chiqaring.
**Kutiladigan natija:** `Havo sovuq, muzlama bo'lishi mumkin`

### 4. Parol tekshiruvi · oson
`parol = "kod_123"`. Agar foydalanuvchi kiritgan parol `"kod_123"` ga teng bo‘lsa `"Xush kelibsiz"`, aks holda `"Parol xato"` xabarini chiqaring.
**Kutiladigan natija:** `Xush kelibsiz`

### 5. Ikki sondan kattasi · o'rta
Ikkita son berilgan: `a = 45` va `b = 62`. `if/else` yordamida qaysi son katta ekanligini toping va `f"Katta son: {katta}"` shaklida chiqaring.
**Kutiladigan natija:** `Katta son: 62`

### 6. Do‘kondagi aksiya · o'rta
Xarid narxi `xarid = 85000` so‘m. Agar xarid 70 000 so‘mdan oshsa, mijozga bepul yetkazib berish xizmati taqdim etiladi (`"Yetkazib berish bepul!"`), aks holda 15 000 so‘m yetkazib berish haqi qo‘shiladi.
**Kutiladigan natija:** `Yetkazib berish bepul!`

### 7. Xatolikni to‘g‘rilang · o'rta
Quyidagi kod berilgan:
```python
yosh = 14
if yosh >= 16
print("Pasport olishingiz mumkin")
else
print("Hali erta")
```
Ushbu kodda mavjud 2 ta asosiy xatoni toping va uni to‘g‘rilab ishga tushiring.
**Kutiladigan natija:** Kod xatosiz bajarilib, `Hali erta` yozuvini chiqarishi kerak.

### 8. Batareya quvvati ogohlantirishi · o'rta
Noutbuk batareyasi `quvvat = 15` foiz. Agar quvvat 20 foizdan kam bo‘lsa `"DIQQAT: Zaryadlovchi moslamani ulang!"`, aks holda `"Batareya yetarli"` xabarini chiqaring.
**Kutiladigan natija:** `DIQQAT: Zaryadlovchi moslamani ulang!`

### 9. Server yuklamasi balansi · qiyin
Serverga sekundiga tushayotgan so‘rovlar soni: `rps = 1200` (requests per second). Agar so‘rovlar 1000 dan oshsa, tizim ikkinchi zaxira serverni yoqishi haqida xabar chiqarsin (`"Zaxira serveri ishga tushirildi"`), aks holda `"Bitta server yuklamani ko'tarmoqda"` deb chiqarsin.
**Kutiladigan natija:** `Zaxira serveri ishga tushirildi`

### 10. Qoldiqsiz bo‘linish (3 ga karrali) · qiyin
Berilgan son `n = 21`. U 3 ga qoldiqsiz bo‘linishini (`n % 3 == 0`) tekshiruvchi va mos xabar chiqaruvchi dastur tuzing.
**Kutiladigan natija:** `21 soni 3 ga qoldiqsiz bo'linadi`

### 11. Mini bankomat dasturi · bonus
Bankomatda hisobingizda `balans = 250000` so‘m pul bor. Foydalanuvchi yechib olmoqchi bo‘lgan summa `yechish = 300000` so‘m.
- Agar mablag‘ yetarli bo‘lsa, pul berilsin va qolgan qoldiq konsolda ko‘rsatilsin;
- Agar mablag‘ yetarli bo‘lmasa, `"Hisobingizda mablag' yetarli emas! Sizda bor: 250000 so'm"` xabari chiqsin.
**Kutiladigan natija:** Mablag‘ yetarli emasligi haqida ogohlantirish chiqishi.

## O'zingizni tekshiring

1. Tarmoqlanuvchi algoritm chiziqli algoritmdan nimasi bilan tubdan farq qiladi?
2. `if` operatoridan so‘ng ikki nuqta (`:`) qo‘yilmasa qanday xatolik yuz beradi?
3. Indentatsiya nima va Pythonda nima uchun unga qat'iy talab qo‘yilgan?
4. Dasturda `else` qismi majburiymi yoki uni yozmaslik ham mumkinmi?
5. `son % 2 == 0` ifodasi qanday ishlaydi?
6. Bitta `if` blokining ichiga yana boshqa `if` yozish mumkinmi va u nima deb ataladi?

## Uyga vazifa

1. `juft_toq.py` faylini oching. O‘zingiz xohlagan butun sonni o‘zgaruvchiga yuklang va uning juft yoki toqligini aniqlovchi dastur yozing.
2. `kirish.py` faylida foydalanuvchi parolini tekshiruvchi dastur tuzing: agar parol `"devops2026"` bo‘lsa `"Tizimga xush kelibsiz"`, aks holda `"Parol xato, qayta urinib ko'ring"` xabari chiqsin.
3. Kassa dasturida xarid 100 000 so‘mdan oshsa 5% chegirma hisoblovchi, aks holda chegirmasiz to‘lovni chiqaruvchi dastur yozing.
