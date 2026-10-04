# 9-dars. Tanlash operatori: match / case va amaliy topshiriqlar

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 9-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga Python 3.10+ versiyasida kiritilgan `match / case` (Pattern Matching) tanlash operatorining sintaksisini, menyular va aniq qiymatlarni solishtirishda uning afzalliklarini hamda rasmiy qo‘llanmadagi barcha amaliy topshiriqlarni (3 ga karralilar, oylar nomi) to‘liq o‘rgatish.

**Kutiladigan natija:**
- `match / case` va `if-elif-else` o‘rtasidagi farqni tushunadi va qachon qaysi biri qulayligini biladi;
- `case _` (wildcard) orqali boshqa noma'lum holatlarni (default) to‘g‘ri ushlaydi;
- `[1, n]` intervaldagi 3 ga karrali sonlarni ham `for`, ham `while` sikllari yordamida yecha oladi;
- 1 dan 12 gacha bo‘lgan sonlarga qarab oylar nomini chiqaruvchi dasturni `match/case` orqali tuzadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 8-dars: while sikli, break va continue |
| 5–25 daq | Yangi mavzu 1 | Tanlash operatori nima? match / case sintaksisi (1.46-rasm) |
| 25–40 daq | Yangi mavzu 2 | Menyu va hafta kuni tanlash (1.47, 1.48-rasmlar) |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Amaliy topshiriqlar | 3 ga karrali sonlar (for/while) va 12 oy dasturlari |
| 65–75 daq | Kod tahlili | 1-chorak / 3-hafta bo‘yicha umumiy bilimlarni tekshirish |
| 75–80 daq | Xulosa va tezkor savollar | 3-hafta yakuniy xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. Nega match / case operatori kerak?
Vaziyatga qarab dastur turli amallarni bajarishi uchun avval faqat `if / elif / else` operatoridan foydalanilar edi. Ammo tekshiriladigan variantlar soni ko‘p bo‘lsa (masalan, 7 ta hafta kuni, 12 ta oy yoki 10 ta buyruq menyusi), kod juda uzun, chalkash va o‘qish noqulay bo‘lib ketadi (1.45-rasm).
Python 3.10 versiyasida kiritilgan **`match / case`** operatori esa:
- Kodni ancha qisqartiradi;
- O‘qishni osonlashtiradi;
- Menyu tanlash va aniq qiymatlar bilan ishlashda eng qulay vosita hisoblanadi.

### 2.2. match / case sintaksisi (Rasmiy 1.46-rasm)
```python
match qiymat:
    case 1:
        # 1-holat
    case 2:
        # 2-holat
    case _:
        # boshqa har qanday holat (else ga o'xshaydi)
```
Bu yerda:
- `match qiymat` — tekshiriladigan o‘zgaruvchi;
- `case ...` — kutilayotgan variantlar;
- `case _:` — agar yuqoridagi variantlarning hech biri to‘g‘ri kelmasa, qolgan barcha holatlar uchun ishlaydi (wildcard / default).

### 2.3. Boshqaruv menyusi namunasi (Rasmiy 1.47-rasm)
```python
tanlov = int(input("Tanlovni kiriting (1-3): "))

match tanlov:
    case 1:
        print("Dastur boshlandi")
    case 2:
        print("Sozlamalar ochildi")
    case 3:
        print("Dastur yopildi")
    case _:
        print("Noto'g'ri tanlov")
```

### 2.4. Hafta kunini tanlash (Rasmiy 1.48-rasm)
```python
kun = int(input("Hafta kunini kiriting (1-7): "))

match kun:
    case 1:
        print("Dushanba")
    case 2:
        print("Seshanba")
    case 3:
        print("Chorshanba")
    case 4:
        print("Payshanba")
    case 5:
        print("Juma")
    case 6:
        print("Shanba")
    case 7:
        print("Yakshanba")
    case _:
        print("Xato! 1–7 oralig'ida kiriting")
```

## 3. Kod namunalari

### Namuna 1: Bitta case da bir nechta variantni tekshirish (`|` belgisi)
```python
kun = int(input("Kun raqamini kiriting (1-7): "))

match kun:
    case 1 | 2 | 3 | 4 | 5:
        print("Ish kuni (dars bor)")
    case 6 | 7:
        print("Dam olish kuni!")
    case _:
        print("Noto'g'ri raqam")
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Darsda ko‘rsatilgan ishlarni mustaqil takrorlash (oson)
Rasmiy qo‘llanmadagi 1.47-rasm bo‘yicha dastur menyusini (1 - Boshlash, 2 - Sozlamalar, 3 - Yopish) `match/case` yordamida yozing va sinab ko‘ring.

**Kutiladigan natija:** 1, 2, 3 kiritilganda tegishli xabarlar, boshqa son kiritilganda `"Noto'g'ri tanlov"` chiqishi.

**Yechim:**
```python
tanlov = 2

match tanlov:
    case 1:
        print("Dastur boshlandi")
    case 2:
        print("Sozlamalar ochildi")
    case 3:
        print("Dastur yopildi")
    case _:
        print("Noto'g'ri tanlov")
```

### 2-topshiriq. [1, n] intervaldan faqat 3 ga karrali sonlarni chiqarish (for bilan) (o'rta)
Rasmiy qo‘llanmadagi 2-topshiriq (1-qism):
Foydalanuvchi `n = 20` sonini kiritadi. `for` sikli yordamida 1 dan n gacha bo‘lgan sonlar orasidan faqat 3 ga qoldiqsiz bo‘linadiganlarini ekranga chiqaring.

**Kutiladigan natija:** `3 6 9 12 15 18`

**Yechim:**
```python
n = 20
print("for sikli bilan (3 ga karralilar):", end=" ")
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, end=" ")
print()
```

### 3-topshiriq. [1, n] intervaldan faqat 3 ga karrali sonlarni chiqarish (while bilan) (o'rta)
Rasmiy qo‘llanmadagi 2-topshiriq (2-qism):
Aynan yuqoridagi masalani endi `while` sikli yordamida amalga oshiring.

**Kutiladigan natija:** `3 6 9 12 15 18`

**Yechim:**
```python
n = 20
i = 1
print("while sikli bilan (3 ga karralilar):", end=" ")
while i <= n:
    if i % 3 == 0:
        print(i, end=" ")
    i += 1
print()
```

### 4-topshiriq. [1, 12] intervalda oy nomini chiqarish (match/case bilan) (qiyin)
Rasmiy qo‘llanmadagi 3-topshiriq:
Foydalanuvchi kiritgan 1 dan 12 gacha bo‘lgan songa qarab tegishli oy nomini (Yanvar, Fevral, ..., Dekabr) chiqaruvchi dasturni `match / case` yordamida tuzing. Agar 1–12 oralig‘idan tashqari son kiritilsa `"Xato! 1–12 oralig'ida son kiriting"` deb chiqarsin.

**Kutiladigan natija:**
```text
Oy raqami: 10
Natija: Oktyabr
```

**Yechim:**
```python
oy = 10

match oy:
    case 1:
        print("Yanvar")
    case 2:
        print("Fevral")
    case 3:
        print("Mart")
    case 4:
        print("Aprel")
    case 5:
        print("May")
    case 6:
        print("Iyun")
    case 7:
        print("Iyul")
    case 8:
        print("Avgust")
    case 9:
        print("Sentyabr")
    case 10:
        print("Oktyabr")
    case 11:
        print("Noyabr")
    case 12:
        print("Dekabr")
    case _:
        print("Xato! 1–12 oralig'ida son kiriting")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **`match / case` qaysi Python versiyasidan boshlab joriy qilingan?**
   - *Javob:* Python 3.10 versiyasidan boshlab.
2. **`case _:` yozuvidagi pastki chiziq (`_`) nima vazifani bajaradi?**
   - *Javob:* Yuqoridagi shartlarning hech biri to‘g‘ri kelmagan barcha holatlarni ushlaydi (else vazifasini bajaradi).
3. **Bitta `case` da bir nechta variantni qaysi belgi bilan tekshirish mumkin?**
   - *Javob:* Vertikal chiziq (`|`) belgisi bilan (masalan: `case 6 | 7:`).
4. **Nega ko‘p variantli menyularda `if/elif` dan ko‘ra `match/case` afzal?**
   - *Javob:* Chunki kod ancha ixcham, tezroq va o‘qish uchun juda qulay bo‘ladi.

## 6. Uyga vazifa

1. Foydalanuvchi kiritgan amallarga (`+`, `-`, `*`, `/`) qarab ikkita son ustida arifmetik amal bajaruvchi mini-kalkulyatorni `match / case` bilan yozing.
2. 1 dan 12 gacha bo‘lgan oy raqamiga qarab fasl nomini (Qish, Bahor, Yoz, Kuz) chiqaruvchi dastur tuzing (`case 12 | 1 | 2: print("Qish")` shaklida).
3. `[1, 100]` oralig‘idagi faqat 5 ga karrali sonlarni ham `for`, ham `while` sikli orqali chiqaruvchi dastur yozing.
