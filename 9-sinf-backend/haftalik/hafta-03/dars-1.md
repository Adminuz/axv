# 7-dars. Takrorlanuvchi algoritm va for sikli

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 7-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga takrorlanuvchi algoritmlar zaruratini, `for` sikli operatori sintaksisini, `range()` funksiyasining barcha parametrlarini (start, stop, step) hamda `[1, N]` oralig‘idagi sonlar yig‘indisini hisoblashni o‘rgatish.

**Kutiladigan natija:**
- Takrorlanuvchi algoritm nima uchun kerakligini hayotiy misollar orqali tushuntira oladi;
- Siklning 3 ta asosiy komponentini (boshlanish, takrorlanish sharti, o‘zgarish) biladi;
- `range(n)`, `range(a, b)` va `range(a, b, step)` parametrlari bilan sonlar ketma-ketligini hosil qiladi;
- `for` sikli yordamida hisoblagich va yig‘indi (`s += i`) hisoblash masalalarini to‘liq yecha oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 2-hafta takrori: if/else va elif shartlari |
| 5–25 daq | Yangi mavzu 1 | Takrorlanuvchi algoritm tushunchasi va sikl qismlari |
| 25–40 daq | Yangi mavzu 2 | for sikli va range() funksiyasining 3 xil ko‘rinishi |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Yangi mavzu 3 & Amaliyot | [1, N] oralig‘idagi yig‘indi dasturi (1.40-rasm) |
| 65–75 daq | Amaliy topshiriqlar | Juft sonlar, karrali sonlar va ko‘paytirish jadvali |
| 75–80 daq | Xulosa va tezkor savollar | Dars xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. Takrorlanuvchi algoritm nima va nega kerak?
Takrorlanuvchi algoritm (sikl / loop) — bir xil amalni bir necha marta bajaradigan algoritm.
Agar sikllar bo‘lmaganida:
- 10 ta raqamni ekranga chiqarish uchun 10 marta `print()` yozish kerak bo‘lardi;
- 100 ta o‘quvchining bahosini hisoblash uchun 100 ta o‘zgaruvchi ochishga to‘g‘ri kelardi;
- 5 sonining ko‘paytirish jadvalini yozish uchun o‘nlab qator kod kerak bo‘lardi.
Sikl yordamida bor-yo‘g‘i 2–3 qator kod bilan har qanday amalni minglab, millionlab marta bir zumda bajarish mumkin.

### 2.2. Siklning 3 ta asosiy qismi
Har qanday sikl 3 ta muhim qismdan iborat bo‘ladi:
1. **Boshlanish (start):** Sikl qaysi qiymatdan boshlanadi?
2. **Takrorlanish soni yoki shart (stop):** Sikl necha marta yoki qachongacha davom etadi?
3. **O‘zgarish (step):** Har bir aylanishda (iteratsiyada) hisoblagich qanday o‘zgaradi?

### 2.3. for sikli va range() funksiyasi
Agar takrorlanishlar soni oldindan ma'lum bo‘lsa, ko‘pincha `for` operatori ishlatiladi.
Umumiy sintaksis:
```python
for i in range(...):
    amal
```
Bu yerda:
- `i` — hisoblagich (har aylanishda navbatdagi qiymatni oladi);
- `range(...)` — qaysi sonlar bo‘yicha aylanishni beruvchi ketma-ketlik generatori.

#### range() funksiyasining 3 xil ko‘rinishi:
1. `range(stop)` — 0 dan boshlab `stop - 1` gacha:
   - `range(5)` &rarr; `0, 1, 2, 3, 4` (dasturlashda indeks 0 dan boshlanadi!).
2. `range(start, stop)` — `start` dan boshlab `stop - 1` gacha (`stop` hisobga kirmaydi!):
   - `range(1, 6)` &rarr; `1, 2, 3, 4, 5`.
3. `range(start, stop, step)` — qadam bilan yurish:
   - `range(0, 11, 2)` &rarr; `0, 2, 4, 6, 8, 10` (juft sonlar).
   - `range(10, 0, -1)` &rarr; `10, 9, 8, ..., 1` (teskari sanash).

### 2.4. [1, N] intervaldagi sonlar yig‘indisini hisoblash (Rasmiy 1.40-rasm)
```python
n = int(input("N sonini kiriting: "))
s = 0

for i in range(1, n + 1):
    s += i

print(f"1 dan {n} gacha sonlar yig'indisi:", s)
```
Dastur qanday ishlaydi:
- `s = 0` — yig‘indini yig‘ib boruvchi o‘zgaruvchi (akkumulyator);
- `for i in range(1, n + 1):` — 1 dan boshlab `n` ham hisobga olinishi uchun `n + 1` gacha aylanadi;
- `s += i` — har aylanishda `i` qiymati `s` ga qo‘shib boriladi;
- `print(s)` — sikl to‘liq tugagach, yig‘indi ekranga chiqariladi.

## 3. Kod namunalari

### Namuna 1: Matnni N marta takrorlash
```python
# Salom so'zini 5 marta chiqarish
for i in range(5):
    print("Salom, Muhammad al-Xorazmiy vorislari!")
```

### Namuna 2: Ko‘paytirish jadvali
```python
son = 7
print(f"--- {son} ning ko'paytirish jadvali ---")
for i in range(1, 11):
    print(f"{son} x {i} = {son * i}")
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. 1 dan 10 gacha sonlarni chiqarish (oson)
`for` sikli yordamida 1 dan 10 gacha bo‘lgan barcha sonlarni konsolga bitta qatorda bo‘sh joy bilan chiqaring (`end=" "`).

**Kutiladigan natija:** `1 2 3 4 5 6 7 8 9 10`

**Yechim:**
```python
for i in range(1, 11):
    print(i, end=" ")
print()
```

### 2-topshiriq. Juft sonlarni chiqarish (oson)
`range(0, 21, 2)` orqali 0 dan 20 gacha bo‘lgan barcha juft sonlarni ekranga chiqaring.

**Kutiladigan natija:**
```text
0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
```

**Yechim:**
```python
for i in range(0, 21, 2):
    print(i, end=", " if i < 20 else "\n")
```

### 3-topshiriq. [1, N] yig‘indisi (o'rta)
Foydalanuvchidan `n = 50` deb oling va 1 dan 50 gacha bo‘lgan barcha butun sonlarning yig‘indisini hisoblang.

**Kutiladigan natija:** `1 dan 50 gacha sonlar yig'indisi: 1275`

**Yechim:**
```python
n = 50
yigindi = 0

for i in range(1, n + 1):
    yigindi += i

print(f"1 dan {n} gacha sonlar yig'indisi: {yigindi}")
```

### 4-topshiriq. Faqat 3 ga karrali sonlar (qiyin)
`[1, 30]` oralig‘idagi sonlar ichidan faqat 3 ga bo‘linadigan sonlarni `for` va `if` yordamida topib, ularning sonini va ro‘yxatini chiqaring.

**Kutiladigan natija:**
```text
3 ga karrali sonlar: 3 6 9 12 15 18 21 24 27 30
Jami: 10 ta
```

**Yechim:**
```python
sanoq = 0
print("3 ga karrali sonlar:", end=" ")
for i in range(1, 31):
    if i % 3 == 0:
        print(i, end=" ")
        sanoq += 1
print()
print(f"Jami: {sanoq} ta")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **`range(1, 5)` qanday sonlarni qaytaradi?**
   - *Javob:* `1, 2, 3, 4` (oxirgi 5 kirmaydi).
2. **`range(5)` deb yozilsa, hisoblash nechinchi sondan boshlanadi?**
   - *Javob:* `0` dan boshlanadi (`0, 1, 2, 3, 4`).
3. **`range(1, 10, 3)` qanday sonlarni hosil qiladi?**
   - *Javob:* `1, 4, 7` (1 dan boshlab 3 qadam bilan).
4. **Nega `for i in range(1, n + 1):` da `n + 1` yoziladi?**
   - *Javob:* Chunki Python `range` da stop qiymatini hisobga olmaydi; `n` sonining o‘zi ham siklga kirishi uchun `n + 1` beriladi.

## 6. Uyga vazifa

1. `ko'paytirish.py` faylida 8 sonining 1 dan 10 gacha bo‘lgan to‘liq ko‘paytirish jadvalini `for` sikli bilan chiqaring.
2. `[1, 100]` oralig‘idagi barcha toq sonlarning yig‘indisini hisoblovchi dastur yozing.
3. 10 dan 1 gacha teskari sanovchi (raketa uchirish tayyorgarligi) va oxirida `"Start!"` deb chiqaruvchi dastur tuzing (`range(10, 0, -1)`).
