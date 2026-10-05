# 10-dars. Ma’lumotlar tuzilmalari va string (satr) asoslari

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 10-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga ma’lumotlar tuzilmasi (Data Structure) tushunchasini, nega kerakligini, Pythonning asosiy tuzilmalarini (string, list, tuple, set, dict) tanishtirish; `string` (`str`) ni yaratish usullarini, ko‘p qatorli stringni va stringning o‘zgarmasligini (immutable) o‘rgatish.

**Kutiladigan natija:**
- Ma’lumotlar tuzilmasi nima ekanini va noto‘g‘ri tanlansa nima bo‘lishini tushuntira oladi;
- `string` ichida harf, raqam, belgi va bo‘sh joy bo‘lishi mumkinligini biladi;
- Stringni `"..."`, `'...'` va `"""..."""` bilan yarata oladi;
- Stringni o‘zgartirib bo‘lmasligini (`TypeError`) va yangi string yaratish yo‘lini (`"J" + s[1:]`) tushuntira oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 3-hafta takrori: `for`, `while`, `match/case` |
| 5–20 daq | Yangi mavzu 1 | Ma’lumotlar tuzilmasi nima? Nega kerak? 5 ta tuzilma xaritasi |
| 20–35 daq | Yangi mavzu 2 | `string`: belgilar ketma-ketligi, yaratish, ko‘p qatorli string |
| 35–40 daq | Tanaffus | Ko‘z mashqlari |
| 40–55 daq | Yangi mavzu 3 | Immutable string: `TypeError` va yangi string yaratish |
| 55–75 daq | Amaliyot | Topshiriqlar (oson → qiyin) |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

## 2. Konspekt

### 2.1. Ma’lumotlar tuzilmasi (Data Structure) nima?
Rasmiy hujjat bo‘yicha: **ma’lumotlar tuzilmasi** — bu kompyuter xotirasida ma’lumotlarni qanday ko‘rinishda saqlash, qanday tartibda joylashtirish va ular ustida qanday tez va qulay amallar bajarish usulidir.

**Nega kerak?** Tasavvur qiling, bizda 10 000 ta ma’lumot bor va:
- uni qidirish kerak (masalan: «Ali bormi?»);
- qo‘shish/o‘chirish kerak;
- takrorlarni olib tashlash kerak;
- kalit bo‘yicha tez topish kerak («telefon raqam - ism»).

Agar noto‘g‘ri tuzilma tanlansa: kod murakkablashadi, dastur sekinlashadi, xato ko‘payadi.

**Ma’lumotlar xotirada qanday saqlanadi?**
- `"Ali"` (string) — belgilar ketma-ketligi;
- `[1, 2, 3]` (list) — ketma-ket elementlar;
- `{"name": "Ali"}` (dict) — kalit-qiymat.

Bu hafta: `string` va `list`. Keyingi hafta: `tuple`, `set`, `dict`.

*Mentor uchun o‘xshatish (hujjatda yo‘q, o‘zimizdan):* ma’lumotlar tuzilmasi — bu omborxonadagi javon turlari. Poyabzal uchun alohida, kitob uchun alohida javon; to‘g‘ri javon tanlansa kerakli narsa tez topiladi.

### 2.2. String nima?
**String** — belgilar ketma-ketligi (harflar, raqamlar, belgilar, bo‘sh joy va h.k.). Pythonda stringlar `str` turida bo‘ladi (`type("Ali")` → `<class 'str'>`).

String ichida bo‘lishi mumkin:
- Harf: `A`, `b`
- Raqam: `1`, `9`
- Belgi: `!`, `@`, `#`
- Bo‘sh joy: `" "`

### 2.3. String yaratish (1.50-rasm)
Qo‘shtirnoq yoki bir tirnoq yetarli:
```python
s1 = "Hello"
s2 = 'Hello'
```

### 2.4. Ko‘p qatorli string (1.51-rasm)
Matnning boshiga va oxiriga 3 tadan qo‘shtirnoq qo‘yiladi:
```python
s3 = """Bu
ko'p qatorli
matn"""
print(s3)
```
Natija:
```text
Bu
ko'p qatorli
matn
```

### 2.5. String o‘zgarmas (Immutable) (1.52-rasm)
String ichidagi belgini o‘zgartirib bo‘lmaydi:
```python
s = "Python"
s[0] = "J"      # TypeError!
```
Bu yerda `s[0]` — 0-indeksdagi belgi (`P`). Python sanoqni 0 dan boshlaydi. Yechim: o‘zgartirishdan ko‘ra **yangi string yaratiladi** (1.53-rasm):
```python
s = "Python"
s2 = "J" + s[1:]
print(s2)       # Jython
```
`s[1:]` — 1-indeksdan boshlab qolgan qism (`ython`). Unga `"J"` qo‘shilib, yangi `s2` hosil bo‘ldi; `s` esa o‘zgarmay qoldi. (Slicing batafsil — 11-darsda.)

## 3. Kod namunalari

### Namuna 1: Uch xil yaratish
```python
ism = "Ali"
sinf = '9-sinf'
maqsad = """Men back-end
dasturchi bo'laman"""
print(ism)
print(sinf)
print(maqsad)
print(type(ism))
```
Natija: `Ali`, `9-sinf`, ikki qatorli matn, `<class 'str'>`.

### Namuna 2: TypeError ni ko‘rish
```python
s = "Python"
try:
    s[0] = "J"
except TypeError as xato:
    print("Xato:", xato)
```
(`try/except` 6-haftada rasmiy o‘rganiladi; bu yerda faqat xatoni xavfsiz ko‘rsatish uchun. Xohlasangiz, `try` siz yozib, dastur to‘xtashini ko‘rsating.)

### Namuna 3: Yangi string yaratish
```python
s = "Python"
s2 = "J" + s[1:]
print(s)    # Python (o'zgarmadi)
print(s2)   # Jython
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Uch usul (oson)
O‘z ismingizni `"..."` bilan, shahringizni `'...'` bilan yarating va ikkalasini chiqaring.

**Kutiladigan natija:** ikki qatorda ism va shahar.

**Yechim:**
```python
ism = "Dilnoza"
shahar = 'Toshkent'
print(ism)
print(shahar)
```

### 2-topshiriq. Ko‘p qatorli she’r (oson)
`"""..."""` yordamida 3 qatorli maqol yarating va bitta `print()` bilan chiqaring.

**Kutiladigan natija:** 3 qator matn.

**Yechim:**
```python
maqol = """Bilimli kishi
bilmaganini so'raydi,
bilmagan kishi - qo'rqadi."""
print(maqol)
```

### 3-topshiriq. Bashorat (o‘rta)
Quyidagi kod nima chiqaradi?
```python
s = "Python"
t = "J" + s[1:]
print(s, t)
```

**Kutiladigan natija:** `Python Jython`

**Yechim:** `s` o‘zgarmaydi (immutable), `t` yangi string: `"J"` + `"ython"`.

### 4-topshiriq. Birinchi harfni almashtirish (qiyin)
`word = "Salom"` stringining birinchi harfini `"K"` ga almashtirib yangi string yarating (`Kalom`). So‘ng `word` ning oxiriga `"!"` qo‘shib, yana yangi string yarating. Asl `word` o‘zgarmaganini isbotlang.

**Kutiladigan natija:**
```text
Kalom
Salom!
Salom
```

**Yechim:**
```python
word = "Salom"
yangi = "K" + word[1:]
print(yangi)            # Kalom
print(word + "!")       # Salom!
print(word)             # Salom (o'zgarmadi)
```
*Mentor eslatma:* `+` stringlarni ulaydi va doim yangi string yaratadi.

## 5. Tezkor nazorat (savollar va javoblar)

1. **Ma’lumotlar tuzilmasi nima?**
   - *Javob:* Ma’lumotlarni xotirada qanday ko‘rinishda saqlash, joylashtirish va ular ustida tez, qulay amallar bajarish usuli.
2. **Noto‘g‘ri tuzilma tanlansa nima bo‘ladi?**
   - *Javob:* Kod murakkablashadi, dastur sekinlashadi, xato ko‘payadi.
3. **Stringni qanday 3 usulda yaratamiz?**
   - *Javob:* `"..."`, `'...'`, ko‘p qatorli uchun `"""..."""`.
4. **`s = "Python"; s[0] = "J"` nima beradi?**
   - *Javob:* `TypeError`, chunki string o‘zgarmas (immutable).
5. **`"J" + s[1:]` nima qiladi?**
   - *Javob:* Yangi string yaratadi: `Jython`.

## 6. Uyga vazifa

1. `string_1.py` da ism (`"`), familiya (`'`) va 3 qatorli «Men haqimda» matnini (`"""`) yarating, hammasini chiqaring.
2. `s = "Python"` dan `"Jython"` hosil qiling, so‘ng `"Python"` dan yana boshqa (`"Cython"`) yangi string yarating.
3. 5 ta ma’lumotni (ism, yosh, fan ro‘yxati, koordinata, telefon-ism juftligi) qaysi tuzilmaga (string/list/tuple/dict) mos kelishini daftarga yozing (taxmin qiling).
