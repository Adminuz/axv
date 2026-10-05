# 13-dars. Tuple (kortej): o‘zgarmas ketma-ketlik

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 13-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga `tuple` (kortej) tuzilmasini, uning `list` dan asosiy farqi — o‘zgarmasligini (immutable), qachon ishlatilishini, yaratish usullarini (shu jumladan bitta elementli tuple), indeks va slicing orqali murojaatni hamda `count()` va `index()` metodlarini o‘rgatish.

**Kutiladigan natija:**
- Tuple nima ekanini va u `list` dan nimasi bilan farq qilishini tushuntira oladi;
- Tuple qachon ishlatilishini (koordinata, ranglar, config, bir nechta qiymat qaytarish, «record») misol bilan aytadi;
- `( )` va vergul yordamida tuple yaratadi, bitta elementli tupleda vergul shartligini biladi;
- Indeks va slicing bilan tuple elementlarini oladi;
- Tuple’ni o‘zgartirish kerak bo‘lsa `list()` → o‘zgartirish → `tuple()` yo‘lini qo‘llaydi;
- `count()` va `index()` metodlaridan foydalanadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 4-hafta: string va list, `append()`, `pop()`, slicing |
| 5–20 daq | Yangi mavzu 1 | Tuple nima? List bilan farqi, qachon ishlatiladi (1.67-rasm) |
| 20–35 daq | Yangi mavzu 2 | Tuple yaratish, bitta elementli tuple, indeks va slicing (1.68–1.70-rasm) |
| 35–40 daq | Tanaffus | Ko‘z va qo‘l mashqlari |
| 40–55 daq | Yangi mavzu 3 | Immutable tuple: `TypeError`, list orqali o‘zgartirish; `count()`, `index()` (1.71–1.73-rasm) |
| 55–75 daq | Amaliyot | Topshiriqlar (oson → qiyin) |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

## 2. Konspekt

### 2.1. Tuple nima? (1.67-rasm)
Rasmiy hujjat bo‘yicha: **Tuple** — bu tartibli (ordered) elementlar to‘plami. U `list` ga o‘xshaydi, lekin eng katta farqi bor:
- **Tuple o‘zgarmas (immutable)** — ichidagi elementlarni keyin o‘zgartirib bo‘lmaydi.

O‘xshatish: `list` — qalam bilan yozilgan daftar (o‘chirib, qayta yozish mumkin). `tuple` — muhr bosilgan hujjat (bir marta yozildi, endi o‘zgarmaydi).

### 2.2. Qachon tuple ishlatiladi?
Hujjatda 3 ta holat ko‘rsatilgan:
1. **Ma’lumot o‘zgarmas bo‘lishi kerak bo‘lganda** — koordinata, ranglar, config (sozlamalar).
2. **Funksiya bir nechta qiymat qaytarganda** (funksiyalarni 6-haftada o‘rganamiz).
3. **«Record» (kichik struktura) ko‘rinishida saqlashda** — masalan, o‘quvchining tug‘ilgan yili va guvohnoma raqami.

```python
koordinata = (41.31, 69.28)       # Toshkent: kenglik, uzunlik
rang = (255, 128, 0)              # RGB rang
talaba = ("Ali", "Valiyev", 2011) # kichik "record"
```

### 2.3. Tuple yaratish (1.68-rasm)
Tuple yaratilishi listga o‘xshaydi, faqat qavslar `( )` ko‘rinishida bo‘ladi va har bir element orasida vergul qo‘yiladi.

```python
fanlar = ("Matematika", "Fizika", "Informatika")
print(fanlar)        # ('Matematika', 'Fizika', 'Informatika')
print(type(fanlar))  # <class 'tuple'>
```

### 2.4. Bitta elementli tuple (1.69-rasm)
Agar tuple ichida bitta element bo‘lsa, **oxirida vergul bo‘lishi shart**, aks holda u tuple emas, oddiy `int` bo‘lib qoladi.

```python
a = (5)
b = (5,)
print(type(a))  # <class 'int'>
print(type(b))  # <class 'tuple'>
```

Sabab: Python uchun `(5)` — bu matematikadagi qavs ichidagi oddiy son. Tuple’ni aynan **vergul** yaratadi.

### 2.5. Indeks va slicing (1.70-rasm)
Tuple ham ketma-ketlik, shuning uchun unda ham indeks bor: kerakli elementga indeks orqali murojaat qilish va slicing (qirqib olish) mumkin. Bu string va listdagi bilan bir xil ishlaydi.

```python
kunlar = ("Dush", "Sesh", "Chor", "Pay", "Juma")
print(kunlar[0])     # Dush
print(kunlar[-1])    # Juma
print(kunlar[1:3])   # ('Sesh', 'Chor')
```

### 2.6. Tuple o‘zgarmas (1.71-rasm)
Tuple elementini o‘zgartirmoqchi bo‘lsak, xato chiqadi:

```python
rang = (255, 128, 0)
rang[0] = 100   # TypeError: 'tuple' object does not support item assignment
```

Agar o‘zgartirish baribir kerak bo‘lsa, hujjatdagi yo‘l: **avval listga aylantiramiz → o‘zgartiramiz → yana tuple’ga o‘tkazamiz.**

```python
rang = (255, 128, 0)
vaqtincha = list(rang)   # [255, 128, 0]
vaqtincha[0] = 100       # [100, 128, 0]
rang = tuple(vaqtincha)  # (100, 128, 0)
print(rang)
```

### 2.7. Tuple metodlari: count() va index() (1.72, 1.73-rasm)
Tupleda metodlar kam, ammo foydali:
- **`count(x)`** — qavs ichiga berilgan element tuple ichida nechta borligini sanaydi.
- **`index(x)`** — berilgan qiymatning tuple ichidagi indeks raqamini aniqlaydi (birinchi uchragan joyi).

```python
baholar = (5, 4, 5, 3, 5, 4)
print(baholar.count(5))  # 3
print(baholar.index(3))  # 3
```

## 3. Kod namunalari

### Namuna 1: Maktab sozlamalari (config)
```python
# O'zgarmas sozlamalar: dars davomiyligi, tanaffus, darslar soni
sozlama = (80, 10, 3)
print("Dars:", sozlama[0], "daqiqa")
print("Tanaffus:", sozlama[1], "daqiqa")
print("Haftada:", sozlama[2], "ta dars")
```

### Namuna 2: Tuple’ni list orqali yangilash
```python
haftalik = ("Python", "Python", "Linux")
royxat = list(haftalik)
royxat[2] = "Python"
haftalik = tuple(royxat)
print(haftalik)                 # ('Python', 'Python', 'Python')
print(haftalik.count("Python")) # 3
```

### Namuna 3: Tuple bo‘ylab for sikli
```python
ranglar = ("qizil", "sariq", "yashil")
for r in ranglar:
    print("Svetofor rangi:", r)
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Mening tuple’im (oson)
O‘zingiz haqingizda `(ism, familiya, tug‘ilgan_yil)` tuple yarating va uchala elementni alohida qatorda chiqaring.

**Kutiladigan natija:**
```text
Ism: Ali
Familiya: Valiyev
Yil: 2011
```

**Yechim:**
```python
men = ("Ali", "Valiyev", 2011)
print("Ism:", men[0])
print("Familiya:", men[1])
print("Yil:", men[2])
```

### 2-topshiriq. Bitta elementli tuple (oson)
`x = (7)` va `y = (7,)` ning turini chiqaring va farqini izohlang.

**Kutiladigan natija:** `<class 'int'>` va `<class 'tuple'>`.

**Yechim:**
```python
x = (7)
y = (7,)
print(type(x))  # <class 'int'>
print(type(y))  # <class 'tuple'>
# Tuple'ni vergul yaratadi, qavs emas
```

### 3-topshiriq. Bashorat (o‘rta)
Kod nima chiqaradi? Avval daftarga yozing, keyin tekshiring.
```python
t = (10, 20, 30, 40, 50)
print(t[1:4])
print(t[-2])
print(t.index(30))
```

**Kutiladigan natija:** `(20, 30, 40)`, `40`, `2`.

**Yechim:** `t[1:4]` 1-, 2-, 3-indekslarni oladi → `(20, 30, 40)`; `t[-2]` oxiridan ikkinchi → `40`; `30` ning indeksi → `2`.

### 4-topshiriq. Ranglarni yangilash (o‘rta)
`rang = (0, 0, 255)` berilgan. Ikkinchi elementni `200` ga o‘zgartiring (list orqali) va natijani tuple ko‘rinishida chiqaring.

**Kutiladigan natija:** `(0, 200, 255)`

**Yechim:**
```python
rang = (0, 0, 255)
r = list(rang)
r[1] = 200
rang = tuple(r)
print(rang)
```

### 5-topshiriq. Baholar statistikasi (qiyin)
`baholar = (5, 3, 4, 5, 5, 2, 4, 5)` berilgan. Har bir baho (2, 3, 4, 5) necha marta uchraganini `for` sikli va `count()` yordamida chiqaring. Birinchi `2` qaysi indeksda turganini ham chiqaring.

**Kutiladigan natija:**
```text
2 bahosi: 1 marta
3 bahosi: 1 marta
4 bahosi: 2 marta
5 bahosi: 4 marta
Birinchi 2 indeksi: 5
```

**Yechim:**
```python
baholar = (5, 3, 4, 5, 5, 2, 4, 5)
for b in range(2, 6):
    print(f"{b} bahosi: {baholar.count(b)} marta")
print("Birinchi 2 indeksi:", baholar.index(2))
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **Tuple bilan list ning eng katta farqi nima?**
   - *Javob:* Tuple o‘zgarmas (immutable), list esa o‘zgaruvchan.
2. **`(5)` va `(5,)` ning farqi nima?**
   - *Javob:* `(5)` — `int`, `(5,)` — tuple. Bitta elementli tupleda vergul shart.
3. **Tuple elementini qanday «o‘zgartirish» mumkin?**
   - *Javob:* `list()` ga aylantirib, o‘zgartirib, yana `tuple()` ga o‘tkazish orqali.
4. **`count()` va `index()` nima qiladi?**
   - *Javob:* `count()` elementni sanaydi, `index()` uning indeksini qaytaradi.
5. **Tuple qachon ishlatiladi? Bitta misol ayting.**
   - *Javob:* Ma’lumot o‘zgarmas bo‘lishi kerak bo‘lganda: koordinata, rang, config.

## 6. Uyga vazifa

1. `tuple_mashq.py` faylida haftaning 7 kunini tuple’da saqlang, birinchi va oxirgi kunni, so‘ng ish kunlarini (slicing) chiqaring.
2. `(2, 5, 5, 3, 5, 4, 2)` tuple’ida har bir son necha marta uchrashini `count()` bilan chiqaring.
3. Sevimli shahringiz koordinatasini tuple’da saqlang va list orqali uzunlik qiymatini o‘zgartirib qayta tuple qiling.
