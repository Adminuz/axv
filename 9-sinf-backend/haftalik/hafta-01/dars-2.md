# 2-dars. Sodda ma’lumot toifalari va arifmetik amallar

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 2-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga Pythondagi asosiy ma’lumot toifalari (int, float, str, bool) va arifmetik operatorlarni, xususan butun bo‘lish (`//`) hamda qoldiqni topish (`%`) amallarini to‘liq o‘rgatish.

**Kutiladigan natija:**
- `str`, `int`, `float`, `bool` toifalarining farqini tushunadi va `type()` funksiyasi bilan aniqlay oladi.
- Barcha arifmetik operatorlar (`+`, `-`, `*`, `/`, `//`, `%`, `**`) bilan to‘g‘ri hisob-kitob qila oladi.
- Oddiy bo‘lish (`/`) har doim `float` natija berishini, butun bo‘lish (`//`) esa butun qismni ajratishini amalda qo‘llay oladi.
- Qoldiqli bo‘lish (`%`) orqali juft/toqlikni yoki vaqt birliklarini hisoblashni biladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 1-dars: o‘rnatish, REPL va `print()` xususiyatlari |
| 5–25 daq | Yangi mavzu 1 | Sodda ma'lumot toifalari: int, float, str, bool |
| 25–40 daq | Yangi mavzu 2 | Arifmetik amallar (+, -, *, /) va qavslar tartibi |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Yangi mavzu 3 & Amaliyot | Butun bo‘lish (//), qoldiq (%) va daraja (**) |
| 65–75 daq | Amaliy topshiriqlar | Arifmetik masalalar va qiziqarli hisob-kitoblar |
| 75–80 daq | Xulosa va tezkor savollar | Dars xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. Ma'lumotlarning sodda toifalari
Kompyuter xotirasidagi ma'lumotlar turli toifalarga (Data types) bo‘linadi. Pythonda eng ko‘p uchraydigan sodda toifalar:
1. **`str` (string - matn):** Qo‘shtirnoq yoki birtirnoq ichidagi belgilar ketma-ketligi (`"Salom"`, `'Python'`).
2. **`int` (integer - butun son):** Musbat, manfiy yoki nol bo‘lgan butun sonlar (`10`, `-5`, `0`, `2026`).
3. **`float` (kasr son):** Vergul o‘rniga nuqta bilan yoziladigan o‘nli kasrlar (`2.5`, `3.14`, `-0.75`).
4. **`bool` (boolean - mantiqiy toifa):** Faqat ikkita qiymat qabul qiladi: `True` (rost) yoki `False` (yolg‘on).

O‘zgaruvchi yoki qiymat toifasini bilish uchun `type()` funksiyasidan foydalaniladi:
```python
print(type("Ali"))   # <class 'str'>
print(type(25))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type(True))    # <class 'bool'>
```

### 2.2. Pythonda arifmetik amallar
Pythonda hisoblash amallari to‘g‘ridan-to‘g‘ri yoki o‘zgaruvchilar orqali bajariladi:
- `+` (Qo‘shish): `5 + 3` -> `8`
- `-` (Ayirish): `10 - 4` -> `6`
- `*` (Ko‘paytirish): `6 * 7` -> `42`
- `/` (Oddiy bo‘lish): `8 / 2` -> `4.0` (E'tibor bering: oddiy bo‘lish natijasi har doim `float` toifasida bo‘ladi!).

### 2.3. Butun bo‘lish (`//`) va Qoldiqni topish (`%`)
Bu ikki amal dasturlashda juda ko‘p ishlatiladi:
1. **Butun bo‘lish (`//`):** Kasr qismini tashlab yuboradi va butun son qaytaradi:
   - `91 // 2` -> `45`
   - `7 // 3` -> `2`
   - `15 // 4` -> `3`
2. **Qoldiqni topish (`%`):** Bo‘lishdan hosil bo‘lgan qoldiqni qaytaradi:
   - `8 % 3` -> `2` (chunki `8 = 3 * 2 + 2`)
   - `15 % 4` -> `3` (chunki `15 = 4 * 3 + 3`)
   - `10 % 2` -> `0` (qoldiq nol bo‘lsa, son juft hisoblanadi!)
3. **Darajaga oshirish (`**`):**
   - `2 ** 3` -> `8`
   - `5 ** 2` -> `25`

### 2.4. Amallar ketma-ketligi (Precedence)
Matematikadagi kabi amallar bajarilish ustunligiga ega:
1. Qavslar `( ... )`
2. Darajaga oshirish `**`
3. Ko‘paytirish, bo‘lish, butun bo‘lish va qoldiq `*`, `/`, `//`, `%`
4. Qo‘shish va ayirish `+`, `-`

## 3. Kod namunalari

### Namuna 1: Arifmetik amallar va natijalar
```python
# Standart amallar
a = 17
b = 5

print("Yig'indi:", a + b)       # 22
print("Ayirma:", a - b)         # 12
print("Ko'paytma:", a * b)      # 85
print("Oddiy bo'lish:", a / b)  # 3.4 (float)
print("Butun bo'lish:", a // b) # 3 (int)
print("Qoldiq:", a % b)         # 2 (int)
print("Daraja:", b ** 2)        # 25
```

### Namuna 2: Qoldiq yordamida vaqtni hisoblash
```python
# Berilgan sekundlarni daqiqa va sekundga ajratish
jami_sekund = 195
daqiqa = jami_sekund // 60
qoldiq_sekund = jami_sekund % 60

print(jami_sekund, "sekund =", daqiqa, "daqiqa va", qoldiq_sekund, "sekund")
# Natija: 195 sekund = 3 daqiqa va 15 sekund
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Toifalarni aniqlash (oson)
Quyidagi qiymatlarning toifalarini `type()` funksiyasi yordamida ekranga chiqaring: `500`, `19.99`, `"DevOps"`, `False`.

**Kutiladigan natija:**
```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

**Yechim:**
```python
print(type(500))
print(type(19.99))
print(type("DevOps"))
print(type(False))
```

### 2-topshiriq. Oddiy bo‘lish va butun bo‘lish farqi (oson)
91 sonini 8 ga oddiy bo‘ling (`/`) va 2 ga butun bo‘ling (`//`). Ikkala natijani konsolga chiqaring.

**Kutiladigan natija:**
```text
91 / 8 = 11.375
91 // 2 = 45
```

**Yechim:**
```python
print("91 / 8 =", 91 / 8)
print("91 // 2 =", 91 // 2)
```

### 3-topshiriq. To‘g‘ri to‘rtburchak perimetri va yuzi (o'rta)
To‘g‘ri to‘rtburchakning tomonlari `a = 12` va `b = 7`. Uning yuzi (`S = a * b`) va perimetrini (`P = 2 * (a + b)`) hisoblovchi dastur yozing.

**Kutiladigan natija:**
```text
Yuzi: 84
Perimetri: 38
```

**Yechim:**
```python
a = 12
b = 7
yuzi = a * b
perimetri = 2 * (a + b)
print("Yuzi:", yuzi)
print("Perimetri:", perimetri)
```

### 4-topshiriq. Qoldiq yordamida kassa hisobi (qiyin)
Xaridor do‘kondan 47 000 so‘mlik xarid qildi va kassirga 100 000 so‘m berdi. Qaytimni 10 000 so‘mlik va 1 000 so‘mlik kupyuralarga ajrating.

**Kutiladigan natija:**
```text
Umumiy qaytim: 53000 so'm
10000 so'mliklar: 5 ta
1000 so'mliklar: 3 ta
```

**Yechim:**
```python
berilgan = 100000
xarid = 47000
qaytim = berilgan - xarid

on_minglik = qaytim // 10000
minglik = (qaytim % 10000) // 1000

print("Umumiy qaytim:", qaytim, "so'm")
print("10000 so'mliklar:", on_minglik, "ta")
print("1000 so'mliklar:", minglik, "ta")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **`91 / 2` va `91 // 2` ifodalarining natijalari qanday farq qiladi?**
   - *Javob:* `91 / 2` ifodasi `45.5` (float) qaytaradi, `91 // 2` esa `45` (int) qaytaradi.
2. **`19 % 5` amali qanday natija beradi?**
   - *Javob:* `4` (chunki `19 = 5 * 3 + 4`).
3. **`type(True)` kodi konsolga nima chiqaradi?**
   - *Javob:* `<class 'bool'>`.
4. **Pythonda darajaga oshirish qaysi operator yordamida bajariladi?**
   - *Javob:* Ikkita yulduzcha `**` orqali.

## 6. Uyga vazifa

1. Foydalanuvchining tug‘ilgan yilini ko‘rsatuvchi son berilgan bo‘lsa, 2026-yil bo‘yicha uning yoshini hisoblovchi dastur yozing.
2. 500 daqiqa necha soat va necha daqiqa ekanligini `//` va `%` yordamida hisoblang.
3. Kvadratning tomoni `8` ga teng bo‘lsa, uning yuzini `**` operatori orqali hisoblang.
