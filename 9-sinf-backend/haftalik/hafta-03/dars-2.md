# 8-dars. Shartli takrorlanish: while sikli va boshqaruv operatorlari

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 8-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga shartli takrorlanuvchi jarayonlar uchun `while` siklidan foydalanishni, cheksiz sikllarning oldini olishni, `break` va `continue` operatorlari yordamida sikl oqimini professional boshqarishni o‘rgatish.

**Kutiladigan natija:**
- `for` va `while` sikllari o‘rtasidagi farqni tushunadi (takrorlanishlar soni noma'lum bo‘lganda `while` ishlatilishini biladi);
- Cheksiz sikl xavfini va hisoblagichni yangilash (`i += 1`) majburiyligini anglaydi;
- `while` yordamida parol so‘rash va 0 kiritilguncha yig‘indini hisoblash algoritmlarini tuzadi;
- `break` (to‘xtatish) va `continue` (o‘tkazib yuborish) operatorlarini to‘g‘ri qo‘llay oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 7-dars: for sikli va range() generatori |
| 5–25 daq | Yangi mavzu 1 | while operatori mohiyati va hayotiy misollar |
| 25–40 daq | Yangi mavzu 2 | Cheksiz sikllar va parol tekshirish (1.43-rasm) |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Yangi mavzu 3 & Amaliyot | break va continue operatorlari, 3 ta urinish (1.44-rasm) |
| 65–75 daq | Amaliy topshiriqlar | O'quvchilar mustaqil while dasturlari yozishi |
| 75–80 daq | Xulosa va tezkor savollar | Dars xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. while operatori mohiyati
Agar `for` siklida takrorlanishlar soni oldindan ma'lum bo‘lsa (masalan: 10 marta, 1 dan N gacha), hayotda takrorlanish necha marta bo‘lishi oldindan noma'lum bo‘lgan holatlar juda ko‘p:
- *"Parol to‘g‘ri kiritilmaguncha qayta so‘ra"* (foydalanuvchi 1 marta yoki 10 marta xato kiritishi mumkin);
- *"Foydalanuvchi 0 kiritmaguncha sonlarni yig‘aver"*;
- *"Hisobda pul tugamaguncha mahsulot xarid qilaver"*.

**`while`** — berilgan shart rost (`True`) bo‘lib turgan vaqt davomida o‘z ichidagi amallarni takrorlayveradi. Qachonki shart natijasi yolg‘on (`False`) bo‘lsa, shundan keyin ishlashdan to‘xtaydi.

### 2.2. while va if/else farqi
`if` berilgan shartni faqat 1 marotaba tekshiradi va 1 marotaba bajaradi.
`while` esa shart natijasi o‘zgarmagunicha (False bo‘lgunicha) qayta va qayta tekshirib, kodni takrorlayveradi.

### 2.3. Oddiy hisoblagich va cheksiz sikl xavfi (Rasmiy 1.42-rasm)
```python
i = 1
while i <= 5:
    print(i)
    i += 1  # Har aylanishda i qiymati 1 taga oshadi
```
*Diqqat:* Agar siz `i += 1` qatorini yozishni unutsangiz, `i` har doim `1` bo‘lib qoladi va `1 <= 5` sharti hech qachon tugamaydi! Natijada dastur **cheksiz siklga (Infinite loop)** tushib qoladi va kompyuter qotadi. Cheksiz sikldan chiqish uchun terminalda `Ctrl + C` bosiladi.

### 2.4. Parol tekshirish masalasi (Rasmiy 1.43-rasm)
```python
parol = "1234"
kirit = input("Parol kiriting: ")

while kirit != parol:
    print("Xato! Qayta urinib ko'ring.")
    kirit = input("Parol: ")

print("Xush kelibsiz! Tizimga muvaffaqiyatli kirdingiz.")
```

### 2.5. break va continue boshqaruv operatorlari (Rasmiy 1.44-rasm)
- **`break`** — siklni muddatidan oldin darhol to‘xtatadi va sikldan butunlay olib chiqadi.
- **`continue`** — siklning joriy aylanishini tashlab yuboradi va to‘g‘ridan-to‘g‘ri keyingi qadamga o‘tadi.

#### 3 ta urinishda parolni tekshirish (1.44-rasm tahlili)
```python
haqiqiy_parol = "1234"
urinishlar = 0

while urinishlar < 3:
    kiritilgan = input("Parolni kiriting: ")
    urinishlar += 1
    
    if kiritilgan == haqiqiy_parol:
        print("Kirish muvaffaqiyatli!")
        break  # Kod shu zahoti to'xtaydi, qaytib while bajarilmaydi
    else:
        print(f"Xato! Qolgan urinishlar: {3 - urinishlar}")
else:
    # Agar break ishlamasdan, urinishlar tugab sikl yakunlansa
    print("Urinishlar soni tugadi! Hisob bloklandi.")
```

## 3. Kod namunalari

### Namuna 1: 0 kiritilguncha yig‘indini hisoblash
```python
jami = 0
son = int(input("Son kiriting (to'xtatish uchun 0): "))

while son != 0:
    jami += son
    son = int(input("Yana son kiriting (to'xtatish uchun 0): "))

print(f"Barcha kiritilgan sonlar yig'indisi: {jami}")
```

### Namuna 2: continue operatori bilan toq sonlarni o‘tkazib yuborish
```python
# Faqat juft sonlarni chiqarish (toq sonlarda continue)
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue  # Toq son bo'lsa, pastdagi print bajarilmaydi
    print("Juft son:", i)
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. 1 dan 5 gacha chiqarish (oson)
`while` sikli yordamida `i = 1` dan boshlab `5` gacha bo‘lgan sonlarni konsolga chiqaring.

**Kutiladigan natija:**
```text
1
2
3
4
5
```

**Yechim:**
```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

### 2-topshiriq. Parol so‘rash (oson)
Foydalanuvchidan `"admin"` so‘zi kiritilguncha qayta-qayta so‘rovchi dastur yozing.

**Kutiladigan natija:** Foydalanuvchi `"admin"` kiritgandagina `"Ruxsat berildi"` xabari chiqishi.

**Yechim:**
```python
kalit = ""
while kalit != "admin":
    kalit = input("Login kiriting: ")
print("Ruxsat berildi")
```

### 3-topshiriq. Teskari sanash (o'rta)
`sekund = 10` deb oling. `while` sikli orqali sekundlarni 1 gacha kamaytirib boring (`sekund -= 1`) va oxirida `"Vaqt tugadi!"` deb chiqaring.

**Kutiladigan natija:** 10 dan 1 gacha sanash va yakuniy xabar.

**Yechim:**
```python
sekund = 10
while sekund > 0:
    print(sekund)
    sekund -= 1
print("Vaqt tugadi!")
```

### 4-topshiriq. 3 ta urinishli PIN-kod (qiyin)
Bankomat PIN-kodi `pin = "7777"`. Foydalanuvchiga 3 ta urinish bering. Agar to‘g‘ri kiritsa `break` qilib `"Mablag'ni yechishingiz mumkin"`, 3 marta xato kiritsa `"Karta bloklandi!"` deb chiqarsin.

**Kutiladigan natija:** 3 ta xatodan so‘ng bloklash, to‘g‘ri kiritsa darhol ruxsat berish.

**Yechim:**
```python
togri_pin = "7777"
urinish = 0
muvaffaqiyat = False

while urinish < 3:
    urinish += 1
    kirit = input("PIN-kodni kiriting: ")
    if kirit == togri_pin:
        print("Mablag'ni yechishingiz mumkin")
        muvaffaqiyat = True
        break
    else:
        print(f"Xato PIN! Qolgan imkoniyat: {3 - urinish}")

if not muvaffaqiyat:
    print("Karta bloklandi!")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **`for` va `while` sikllarining asosiy farqi nimada?**
   - *Javob:* `for` siklida takrorlanishlar soni oldindan ma'lum bo‘ladi, `while` esa berilgan shart rost bo‘lib turguncha noma'lum marta aylanadi.
2. **Cheksiz sikl nima va undan konsolda qanday chiqiladi?**
   - *Javob:* Sharti hech qachon `False` bo‘lmaydigan to‘xtovsiz sikl; konsolda `Ctrl + C` bosib to‘xtatiladi.
3. **`break` operatorining vazifasi nima?**
   - *Javob:* Siklni darhol to‘xtatib, undan butunlay chiqib ketish.
4. **`continue` operatori nima qiladi?**
   - *Javob:* Siklning joriy aylanishini tashlab, navbatdagi iteratsiyaga o‘tadi.

## 6. Uyga vazifa

1. Foydalanuvchi manfiy son kiritguncha sonlarni qabul qiluvchi va musbat sonlar yig‘indisini hisoblovchi dastur yozing.
2. 1 dan 20 gacha bo‘lgan sonlar ichidan 3 ga bo‘linadiganlarini `continue` orqali tashlab o‘tib, qolganlarini chiqaruvchi dastur tuzing.
3. Sirli sonni topish o‘yini: `sirli_son = 42`. Foydalanuvchi ushbu sonni topmaguncha qayta-qayta kiritishni so‘rang.
