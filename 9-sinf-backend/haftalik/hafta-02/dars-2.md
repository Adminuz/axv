# 5-dars. Tarmoqlanuvchi algoritm: if va else operatorlari

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 5-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga tarmoqlanuvchi algoritmlar mohiyatini, `if` va `else` operatorlari sintaksisini, ikki nuqta (`:`) va tabulyatsiya (chekinish / indentation) qoidalarini hamda shartli masalalarni dasturlashni o‘rgatish.

**Kutiladigan natija:**
- Tarmoqlanuvchi algoritm nima ekanligini va qachon ishlatilishini tushuntirib bera oladi;
- `if` va `else` sintaksisini to‘g‘ri yozadi va 4 ta bo‘sh joy (indentation) qoidasiga qat'iy amal qiladi;
- Taqqoslash operatorlari va qoldiq (`%`) yordamida shartlarni tekshira oladi (masalan, juft/toq sonlar, o‘tdi/o‘tmadi);
- Sintaktik xatolarni (ikki nuqtani unutish, noto‘g‘ri surilish) mustaqil tuzata oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 4-dars: taqqoslash va mantiqiy operatorlar |
| 5–25 daq | Yangi mavzu 1 | Tarmoqlanuvchi algoritm mohiyati va hayotiy misollar |
| 25–40 daq | Yangi mavzu 2 | if/else sintaksisi, ikki nuqta (:) va indentatsiya |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Yangi mavzu 3 & Amaliyot | Juft/toqlik tekshiruvi va ball bo‘yicha qaror qabul qilish |
| 65–75 daq | Amaliy topshiriqlar | O'quvchilar mustaqil shartli dasturlar tuzishi |
| 75–80 daq | Xulosa va tezkor savollar | Dars xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. Tarmoqlanuvchi algoritm nima?
Chiziqli dasturlarda kodlar yuqoridan pastga qarab ketma-ket bajariladi. Ammo hayotda ham, dasturlashda ham doim tanlov oldida turamiz:
- *Agar bugun yomg‘ir yog‘sa &rarr; soyabon olamiz.*
- *Aks holda (yomg‘ir yog‘masa) &rarr; soyabonsiz chiqamiz.*

**Tarmoqlanuvchi algoritm** — dastur bajarilishi jarayonida muayyan shart tekshirilib, natijaga qarab:
- Shart rost (`True`) bo‘lsa — birinchi tarmoq (amal_1) bajariladi;
- Shart yolg‘on (`False`) bo‘lsa — ikkinchi tarmoq (amal_2) bajariladi.

### 2.2. if va else operatorining sintaksisi
Pythonda shart operatori quyidagi tartibda yoziladi:
```python
if shart:
    amal_1  # Shart rost (True) bo'lsa bajariladi
else:
    amal_2  # Shart yolg'on (False) bo'lsa bajariladi
```

### 2.3. Ikki nuqta (:) va Tabulyatsiya (Indentation) qoidasi
Pythonda boshqa dasturlash tillari (C++, Java, JavaScript) kabi jingalak qavslar `{ ... }` ishlatilmaydi. Buning o‘rniga ikkita qat'iy qoida amal qiladi:
1. `if` va `else` qatorlarining oxiriga albatta **ikki nuqta (`:`)** qo‘yilishi shart;
2. `if` yoki `else` ning ichidagi kodlar chap tomondan **4 ta bo‘sh joy (space)** yoki bitta **Tab** surilib (chekinish bilan) yozilishi shart.

Agar chekinish qilinmasa, Python `IndentationError: expected an indented block` xatosini beradi.

### 2.4. Rasmiy qo‘llanmadagi asosiy holatlar

#### 1-holat: Ball tekshiruvi (O‘tdi / O‘tmadi)
Agar foydalanuvchi to‘plagan ball `60` dan katta yoki teng bo‘lsa "O‘tdi", aks holda "O‘tmadi" xabari chiqadi:
```python
ball = 65

if ball >= 60:
    print("O'tdi")
else:
    print("O'tmadi")
```

#### 2-holat: Qoldiq (%) bilan sonni juft/toqlikka tekshirish
Har qanday sonni 2 ga bo‘lganda qoldiq 0 bo‘lsa — son juft, aks holda toq:
```python
son = 14

if son % 2 == 0:
    print("Juft son")
else:
    print("Toq son")
```

## 3. Kod namunalari

### Namuna 1: Foydalanuvchi yoshi bo‘yicha ruxsat
```python
yosh = 17

if yosh >= 18:
    print("Xush kelibsiz! Siz voyaga yetgansiz.")
    print("Barcha bo'limlar siz uchun ochiq.")
else:
    print("Kirish cheklangan!")
    print("Ushbu xizmatdan faqat 18 yoshdan kattalar foydalanishi mumkin.")
```

### Namuna 2: Parol mosligini tekshirish
```python
haqiqiy_parol = "admin2026"
kiritilgan_parol = "admin2026"

if kiritilgan_parol == haqiqiy_parol:
    print("Muvaffaqiyatli kirdingiz!")
else:
    print("Xato parol! Qaytadan urinib ko'ring.")
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Imtihon natijasi (oson)
`ball = 54` o‘zgaruvchisi berilgan. Agar ball 60 dan katta yoki teng bo‘lsa `"Tabriklaymiz, siz o'tdingiz!"`, aks holda `"Afsuski, qayta topshirishingiz kerak"` deb chiqaruvchi dastur yozing.

**Kutiladigan natija:** `Afsuski, qayta topshirishingiz kerak`

**Yechim:**
```python
ball = 54

if ball >= 60:
    print("Tabriklaymiz, siz o'tdingiz!")
else:
    print("Afsuski, qayta topshirishingiz kerak")
```

### 2-topshiriq. Juft yoki toq son (oson)
`son = 27` deb oling. `% 2 == 0` sharti yordamida son juft yoki toqligini aniqlab, mos xabarni chiqaring.

**Kutiladigan natija:** `27 - toq son`

**Yechim:**
```python
son = 27

if son % 2 == 0:
    print(f"{son} - juft son")
else:
    print(f"{son} - toq son")
```

### 3-topshiriq. Do‘kondagi chegirma (o'rta)
Xarid summasi `summa = 150000` so‘m. Agar summa `100000` so‘mdan oshsa, mijozga 10% chegirma beriladi (`summa * 0.9`) va chegirmali summa chiqariladi. Aks holda chegirmaning mavjud emasligi va to‘liq summa aytiladi.

**Kutiladigan natija:**
```text
10% chegirma berildi!
To'lov: 135000.0 so'm
```

**Yechim:**
```python
summa = 150000

if summa > 100000:
    yakuniy = summa * 0.9
    print("10% chegirma berildi!")
    print(f"To'lov: {yakuniy} so'm")
else:
    print("Chegirma mavjud emas.")
    print(f"To'lov: {summa} so'm")
```

### 4-topshiriq. Server holatini tekshirish (qiyin)
Serverning xotira (RAM) sarfi `ram_sarf_foiz = 85` deb berilgan. Agar sarf 80 foizdan yuqori bo‘lsa `"OGOHLANTIRISH: Xotira to'lib bormoqda!"`, aks holda `"Server barqaror ishlamoqda"` xabarini chiqaring.

**Kutiladigan natija:** `OGOHLANTIRISH: Xotira to'lib bormoqda!`

**Yechim:**
```python
ram_sarf_foiz = 85

if ram_sarf_foiz > 80:
    print("OGOHLANTIRISH: Xotira to'lib bormoqda!")
else:
    print("Server barqaror ishlamoqda")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **`if` va `else` qatorlarining oxiriga qaysi belgi qo‘yilishi shart?**
   - *Javob:* Ikki nuqta (`:`).
2. **Pythonda chekinish (indentation) qanday maqsad uchun ishlatiladi?**
   - *Javob:* Qaysi kodlar `if` yoki `else` blokiga tegishli ekanligini belgilash uchun (boshqa tillardagi `{}` vazifasini bajaradi).
3. **Agar shart `False` bo‘lsa, qaysi blokdagi kod bajariladi?**
   - *Javob:* `else` blokidagi kod.
4. **`son % 2 == 0` sharti nimani aniqlaydi?**
   - *Javob:* Sonning 2 ga qoldiqsiz bo‘linishini, ya'ni juft son ekanligini.

## 6. Uyga vazifa

1. Foydalanuvchi kiritgan butun son berilgan. Agar son 0 dan katta bo‘lsa `"Musbat son"`, aks holda `"Musbat emas"` deb chiqaruvchi dastur tuzing.
2. Harorat `gradus = -5` deb berilgan. Agar u 0 dan past bo‘lsa `"Havo sovuq, qalin kiyining"`, aks holda `"Havo yaxshi"` xabarini chiqaring.
3. Kassa dasturida foydalanuvchining hisobidagi puli va mahsulot narxi solishtirilib, yetarli bo‘lsa `"Xarid muvaffaqiyatli"`, yetarli bo‘lmasa `"Mablag' yetarli emas"` xabari chiqarilsin.
