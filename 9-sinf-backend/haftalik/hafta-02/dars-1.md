# 4-dars. Pythonda operatorlar va ifodalar

**Hafta:** 2 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 4-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga dasturlashda ifoda (expression) va operator tushunchalarini, taqqoslash (`==`, `!=`, `<`, `>`, `<=`, `>=`), mantiqiy (`and`, `or`, `not`), a'zolik (`in`, `not in`) va identifikatsiya (`is`, `is not`) operatorlarini chuqur o‘rgatish.

**Kutiladigan natija:**
- Operator va operand farqini biladi;
- Taqqoslash operatorlari har doim mantiqiy (`bool`) natija (`True` yoki `False`) qaytarishini tushunadi;
- Mantiqiy operatorlar (`and`, `or`, `not`) yordamida bir nechta shartlarni birlashtira oladi;
- A'zolik (`in`, `not in`) operatorlari orqali matn yoki to‘plam ichida element borligini tekshiradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 1-hafta takrori: toifalar, arifmetika va o‘zgaruvchilar |
| 5–25 daq | Yangi mavzu 1 | Operator va operand. Ifoda (expression) tushunchasi |
| 25–40 daq | Yangi mavzu 2 | Taqqoslash operatorlari (==, !=, <, >, <=, >=) |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Yangi mavzu 3 & Amaliyot | Mantiqiy operatorlar (and, or, not), a'zolik (in, not in) |
| 65–75 daq | Amaliy topshiriqlar | Mantiqiy ifodalar tuzish va tekshirish |
| 75–80 daq | Xulosa va tezkor savollar | Dars xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. Operator va Ifoda (Expression)
- **Operator** — bu ma’lumotlar (qiymatlar) ustida biror amal bajarish uchun ishlatiladigan maxsus belgi yoki kalit so‘z (masalan: `+`, `-`, `==`, `and`).
- **Operand** — operator qaysi qiymatlar yoki o‘zgaruvchilar ustida ishlasa, o‘shalar (masalan, `a + b` ifodasida `a` va `b` — operandlar, `+` — operator).
- **Ifoda (Expression)** — operatorlar, operandlar, qavslar va funksiyalar yordamida tuzilgan, hisoblanganda albatta biror natija qaytaruvchi kod yozuvi:
  - `5 + 3` -> `8` (arifmetik ifoda: natija `int`)
  - `10 > 7` -> `True` (taqqoslash ifodasi: natija `bool`)
  - `"salom" + "!"` -> `"salom!"` (matnli ifoda: natija `str`)
  - `len("python")` -> `6` (funksiyali ifoda: natija `int`)

### 2.2. Taqqoslash operatorlari
Taqqoslash operatorlari ikki qiymatni o‘zaro solishtiradi va har doim mantiqiy (`True` yoki `False`) natija beradi:
- `==` (Teng bo‘lsa): `5 == 5` -> `True`, `5 == 6` -> `False`
- `!=` (Teng bo‘lmasa): `10 != 5` -> `True`
- `>` (Katta): `15 > 8` -> `True`
- `<` (Kichik): `4 < 2` -> `False`
- `>=` (Katta yoki teng): `60 >= 60` -> `True`
- `<=` (Kichik yoki teng): `18 <= 20` -> `True`

*Muhim ogohlantirish:* Bitta tenglik (`=`) — qiymat berish amali, ikkita tenglik (`==`) esa taqqoslash amali! Bularni adashtirish qat'iyan taqiqlanadi.

### 2.3. Mantiqiy operatorlar (`and`, `or`, `not`)
Bir nechta shartlarni bir-biriga bog‘lash uchun mantiqiy operatorlardan foydalaniladi:
1. **`and` (va):** Barcha shartlar `True` bo‘lsagina, natija `True` bo‘ladi. Agar kamida bittasi `False` bo‘lsa, natija `False`.
   - `yosh >= 7 and yosh <= 18` (Yosh 7 dan katta yoki teng VA 18 dan kichik yoki teng).
2. **`or` (yoki):** Kamida bitta shart `True` bo‘lsa, natija `True` bo‘ladi. Ikkalasi ham `False` bo‘lsagina, natija `False`.
   - `ball >= 90 or olimpiada_golibi` (Ball 90+ YOKI olimpiada g‘olibi).
3. **`not` (emas):** Shart natijasini teskarisiga o‘zgartiradi: `not True` -> `False`, `not False` -> `True`.

### 2.4. A'zolik (`in`, `not in`) va Identifikatsiya (`is`, `is not`)
- **`in` (ichida bormi?):** Element to‘plam yoki matn ichida mavjud bo‘lsa `True` beradi:
  - `"a" in "salom"` -> `True`
  - `"z" in "salom"` -> `False`
- **`not in` (ichida yo‘qmi?):** Element yo‘qligini tekshiradi:
  - `"x" not in "salom"` -> `True`
- **`is` (aynan bir xil obyektmi?):** Xotiradagi manzili bir xilligini tekshiradi.

## 3. Kod namunalari

### Namuna 1: Taqqoslash va mantiqiy tekshiruvlar
```python
ball = 75
yosh = 16
tatildami = False

# Taqqoslash
otdimi = ball >= 60
print("Imtihondan o'tdimi:", otdimi)  # True

# Mantiqiy ifoda (and, not)
maktabga_boradimi = (yosh >= 7 and yosh <= 18) and not tatildami
print("Maktabga boradimi:", maktabga_boradimi)  # True
```

### Namuna 2: A'zolik operatori bilan matn tekshirish
```python
domen = "admin@maktab.uz"

# Domen .uz bilan tugashini tekshirish
milliy_saytmi = ".uz" in domen
print("O'zbekiston domeni bormi:", milliy_saytmi)  # True

# Ruxsat berilgan rollar
rollar = ["admin", "moderator", "mentor"]
foydalanuvchi_roli = "admin"

ruxsat_bormi = foydalanuvchi_roli in rollar
print("Tizimga kirish huquqi:", ruxsat_bormi)  # True
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Taqqoslash ifodalari (oson)
Berilgan `a = 25` va `b = 30` sonlari uchun `a == b`, `a != b`, `a < b`, `a >= b` ifodalarining qiymatlarini konsolga chiqaring.

**Kutiladigan natija:**
```text
a == b: False
a != b: True
a < b: True
a >= b: False
```

**Yechim:**
```python
a = 25
b = 30
print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a >= b:", a >= b)
```

### 2-topshiriq. Imtihondan o‘tish sharti (oson)
Talabaning bali `68`. Agar ball `60` dan katta yoki teng bo‘lsa `True`, aks holda `False` qaytaruvchi `otdi` nomli mantiqiy o‘zgaruvchi yarating va natijani chiqaring.

**Kutiladigan natija:** `Imtihondan o'tdi: True`

**Yechim:**
```python
ball = 68
otdi = ball >= 60
print("Imtihondan o'tdi:", otdi)
```

### 3-topshiriq. Harorat va ob-havo ifodasi (o'rta)
`harorat = 22` va `yomgir_yogmoqdami = False`. Dastur quyidagi murakkab shartni hisoblasin: "Harorat 18 dan yuqori bo‘lsa VA yomg‘ir yog‘mayotgan bo‘lsa (`not yomgir_yogmoqdami`), sayr qilish tavsiya etiladi".

**Kutiladigan natija:** `Sayr qilish tavsiya etiladimi: True`

**Yechim:**
```python
harorat = 22
yomgir_yogmoqdami = False

sayr_mumkin = harorat > 18 and not yomgir_yogmoqdami
print("Sayr qilish tavsiya etiladimi:", sayr_mumkin)
```

### 4-topshiriq. Xavfsiz parol tekshiruvi (qiyin)
Parol `parol = "super_maxfiy_2026"` deb berilgan. Quyidagi 3 ta shart birdaniga bajarilganligini (`and`) tekshiruvchi ifoda tuzing:
1. Parol uzunligi 8 tadan kam emas (`len(parol) >= 8`);
2. Parol ichida `"_"` belgisi bor (`"_" in parol`);
3. Parol ichida `"admin"` so‘zi yo‘q (`"admin" not in parol`).

**Kutiladigan natija:** `Parol xavfsizmi: True`

**Yechim:**
```python
parol = "super_maxfiy_2026"

xavfsizmi = len(parol) >= 8 and ("_" in parol) and ("admin" not in parol)
print("Parol xavfsizmi:", xavfsizmi)
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **`=` va `==` operatorlarining farqi nimada?**
   - *Javob:* `=` o‘zlashtirish (qiymat berish), `==` esa ikkita qiymatning tengligini tekshirish (taqqoslash).
2. **`True and False` ifodasi qanday natija beradi?**
   - *Javob:* `False` (chunki `and` amali uchun barcha tomonlar `True` bo‘lishi shart).
3. **`not (10 > 5)` ifodasi natijasi nima bo‘ladi?**
   - *Javob:* `False` (chunki `10 > 5` rost (`True`), `not True` esa `False` beradi).
4. **`"uz" in "toshkent.uz"` nima qaytaradi?**
   - *Javob:* `True`, chunki matn ichida `"uz"` qism-matni mavjud.

## 6. Uyga vazifa

1. `foydalanuvchi_yoshi` o‘zgaruvchisini yarating. Agar yosh 14 dan katta yoki teng va 18 dan kichik yoki teng bo‘lsa `True` chiqaruvchi mantiqiy ifoda yozing.
2. Sevimli kitobingiz nomini matn sifatida oling va uning ichida `"va"` yoki `"o'zbek"` so‘zlari bor-yo‘qligini `in` yordamida tekshiring.
3. Uchta son (`x = 12`, `y = 20`, `z = 15`) berilgan. `y` soni `x` dan ham, `z` dan ham katta ekanligini `and` orqali tekshirib konsolga chiqaring.
