# 6-dars. Ko‘p tarmoqli shartlar: elif operatori va amaliy topshiriqlar

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 6-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga ko‘p tarmoqli shartli konstruksiyalar (`if`, `elif`, `else`), mantiqiy operatorlar bilan birgalikda ishlash va rasmiy qo‘llanmadagi 4 ta amaliy topshiriqni (musbat/manfiy/nol, kattasini topish, yosh toifasi, harorat tavsiyasi) to‘liq yechishni o‘rgatish.

**Kutiladigan natija:**
- `elif` ("aks holda agar") operatorining vazifasini va bir nechta shartlar ketma-ketligini tushunadi;
- Baholash tizimi (5, 4, 3, 2) va oraliq shartlarni xatosiz kodlay oladi;
- Rasmiy qo‘llanmadagi barcha 4 ta amaliy topshiriqni mustaqil bajara oladi;
- Odatiy xatolarni (`=` vs `==`, ikki nuqta, noto‘g‘ri chekinish) mustaqil bartaraf etadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 5-dars: if/else, ikki nuqta va 4 bo‘sh joy qoidasi |
| 5–25 daq | Yangi mavzu 1 | elif operatori va ko‘p variantli shartlar tuzilishi |
| 25–40 daq | Yangi mavzu 2 | Mantiqiy operatorlar (and, or) bilan murakkab shartlar |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Amaliy topshiriqlar | Rasmiy 4 ta topshiriqni bosqichma-bosqich yechish |
| 65–75 daq | Kod tahlili | Odatiy xatolarni bartaraf qilish va testlash |
| 75–80 daq | Xulosa va tezkor savollar | 2-hafta xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. Nega elif kerak?
Hayotda ko‘pincha ikkita emas, uchta yoki undan ortiq tanlovlar uchraydi:
- Son 0 dan katta (musbat), 0 dan kichik (manfiy) yoki 0 ga teng bo‘lishi mumkin (3 ta holat);
- Baho 5, 4, 3 yoki 2 bo‘lishi mumkin (4 ta holat);
- Harorat sovuq, salqin yoki issiq bo‘lishi mumkin (3 ta holat).

Bunday paytda faqat `if/else` ishlatilsa, kod ichma-ich chuqurlashib, o‘qish noqulay bo‘lib ketadi. Pythonda bu muammoni hal qilish uchun **`elif`** (inglizcha *else if* — "aks holda agar") operatori kiritilgan.

### 2.2. if - elif - else sintaksisi
```python
if 1_shart:
    amal_1
elif 2_shart:
    amal_2
elif 3_shart:
    amal_3
else:
    boshqa_amallar
```
Dastur yuqoridan pastga qarab tekshiradi: qaysi shart birinchi bo‘lib `True` bo‘lsa, faqat o‘sha blok ishlaydi va qolgan `elif`/`else` lar tashlab o‘tib ketiladi.

### 2.3. Baholash tizimi namunasi (Rasmiy 1.29-rasm)
```python
ball = 78

if ball >= 86:
    print("Baho: 5 (A'lo)")
elif ball >= 71:
    print("Baho: 4 (Yaxshi)")
elif ball >= 56:
    print("Baho: 3 (Qoniqarli)")
else:
    print("Baho: 2 (Qoniqarsiz)")
```

### 2.4. Mantiqiy operatorlar bilan if/elif (Rasmiy 1.28-rasm)
```python
yosh = 14
tatil = False

if yosh >= 7 and yosh <= 18 and not tatil:
    print("Maktabga boradi")
else:
    print("Uyda qoladi")
```

### 2.5. Keng tarqalgan xatolar (Rasmiy 1.30–1.33 rasmlar)
1. **`=` va `==` ni adashtirish:**
   - ❌ `if ball = 60:` (o‘zlashtirish qo‘yib yuborilgan)
   - ✅ `if ball == 60:` (to‘g‘ri taqqoslash)
2. **`:` ni unutish:**
   - ❌ `if a > 0`
   - ✅ `if a > 0:`
3. **Tabulyatsiyani (chekinishni) xato qo‘yish:**
   - Pythonda operatorga tegishli kod undan chapga 4 ta bo‘sh joy ichkarida yozilishi shart.

## 3. Kod namunalari

### Namuna: Foydalanuvchidan son kiritish (`int(input())`)
```python
# Foydalanuvchi kiritgan sonni butun songa aylantiramiz
son = int(input("Butun son kiriting: "))

if son > 0:
    print("Musbat son")
elif son < 0:
    print("Manfiy son")
else:
    print("Nolga teng")
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Son musbat, manfiy yoki nol ekanligini aniqlash (oson)
Rasmiy qo‘llanmadagi 1-topshiriq:
Foydalanuvchidan bitta butun son oling. Agar son 0 dan katta bo‘lsa `"Musbat son"`, 0 dan kichik bo‘lsa `"Manfiy son"`, 0 ga teng bo‘lsa `"Nolga teng"` deb chiqaring.

**Kutiladigan natija:**
```text
Son: -8
Natija: Manfiy son
```

**Yechim:**
```python
son = -8

if son > 0:
    print("Musbat son")
elif son < 0:
    print("Manfiy son")
else:
    print("Nolga teng")
```

### 2-topshiriq. Ikki sondan kattasini aniqlash (o'rta)
Rasmiy qo‘llanmadagi 2-topshiriq:
Ikkita son berilgan. Qaysi son katta ekanligini chiqaring. Agar ikkala son o‘zaro teng bo‘lsa `"Sonlar teng"` deb chiqaring.

**Kutiladigan natija:**
```text
a = 15, b = 20
Kattasi: 20
```

**Yechim:**
```python
a = 15
b = 20

if a > b:
    print(f"Kattasi: {a}")
elif b > a:
    print(f"Kattasi: {b}")
else:
    print("Sonlar teng")
```

### 3-topshiriq. Yoshga qarab toifa aniqlash (o'rta)
Rasmiy qo‘llanmadagi 3-topshiriq:
Foydalanuvchidan yoshini kiriting:
- Agar yosh 0–6 oralig‘ida bo‘lsa &rarr; `"Bog‘cha yoshi"`
- 7–17 oralig‘ida bo‘lsa &rarr; `"Maktab o‘quvchisi"`
- 18 va undan katta bo‘lsa &rarr; `"Voyaga yetgan"`

**Kutiladigan natija:**
```text
Yosh: 15
Toifa: Maktab o‘quvchisi
```

**Yechim:**
```python
yosh = 15

if yosh >= 0 and yosh <= 6:
    print("Bog‘cha yoshi")
elif yosh >= 7 and yosh <= 17:
    print("Maktab o‘quvchisi")
else:
    print("Voyaga yetgan")
```

### 4-topshiriq. Haroratga qarab tavsiya berish (qiyin)
Rasmiy qo‘llanmadagi 4-topshiriq:
Havo harorati (butun son) berilgan:
- Agar harorat 0 dan past bo‘lsa &rarr; `"Sovuq, qalin kiyining"`
- 0 dan 20 gacha bo‘lsa &rarr; `"Salqin"`
- 20 dan yuqori bo‘lsa &rarr; `"Issiq"`

**Kutiladigan natija:**
```text
Harorat: 25
Tavsiya: Issiq
```

**Yechim:**
```python
harorat = 25

if harorat < 0:
    print("Sovuq, qalin kiyining")
elif harorat <= 20:
    print("Salqin")
else:
    print("Issiq")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **`elif` so‘zi qaysi so‘zlarning qisqartmasi?**
   - *Javob:* `else if` (aks holda agar).
2. **Bitta `if` konstruksiyasida nechta `elif` ishlatish mumkin?**
   - *Javob:* Xohlagancha ko‘p (cheklanmagan).
3. **Nega `if son = 0:` deb yozib bo‘lmaydi?**
   - *Javob:* Chunki `=` qiymat berish amali, taqqoslash uchun `==` ishlatilishi kerak.
4. **Agar `if` va birinchi `elif` shartlari `False` bo‘lib, ikkinchi `elif` `True` bo‘lsa, qaysi blok bajariladi?**
   - *Javob:* Ikkinchi `elif` bloki bajariladi va qolgan qismi tashlab ketiladi.

## 6. Uyga vazifa

1. Rasmiy 4 ta topshiriqni (`musbat_manfiy.py`, `kattasi.py`, `yosh_toifa.py`, `harorat.py`) alohida fayllarda yozib, to‘liq testdan o‘tkazing.
2. Baholash tizimini yaratib, 100 ballik tizim bo‘yicha o‘z bahoingizni aniqlovchi dastur yozing.
3. Haftaning tartib raqamiga (1–7) qarab tegishli kun nomini (Dushanba, ..., Yakshanba) chiqaruvchi dastur tuzing.
