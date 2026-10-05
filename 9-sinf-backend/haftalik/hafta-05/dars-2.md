# 14-dars. Set (to‘plam): takrorlanmaydigan elementlar

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 14-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga `set` (to‘plam) tuzilmasini, uning xususiyatlarini (unikal elementlar, tez `in` tekshiruvi, indeks yo‘qligi, tartib kafolatlanmasligi, mutable), set yaratish (bo‘sh set — `set()`), element qo‘shish/o‘chirish, ikkita setni birlashtirish, listdagi dublikatlarni olib tashlash va setni tartiblashni o‘rgatish.

**Kutiladigan natija:**
- Set nima ekanini va uning 5 ta xususiyatini aytib bera oladi;
- `{ }` bilan set, `set()` bilan bo‘sh set yaratadi va `{}` nega bo‘sh set emasligini tushuntiradi;
- `add()` va `remove()` bilan element qo‘shadi/o‘chiradi;
- Ikkita setni birlashtiradi va dublikat qanday yo‘qolishini tushuntiradi;
- `set(nums)` bilan listdagi takrorlarni olib tashlaydi va `sorted()` bilan tartiblaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 13-dars: tuple, `count()`, `index()` |
| 5–20 daq | Yangi mavzu 1 | Set nima? 5 ta xususiyat (1.74-rasm) |
| 20–35 daq | Yangi mavzu 2 | Set yaratish, bo‘sh set, `add()` / `remove()` (1.75–1.76-rasm) |
| 35–40 daq | Tanaffus | Chigil yozdi |
| 40–55 daq | Yangi mavzu 3 | Setlarni birlashtirish, dublikatni olib tashlash, tartiblash (1.77–1.79-rasm) |
| 55–75 daq | Amaliyot | Topshiriqlar (oson → qiyin) |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

## 2. Konspekt

### 2.1. Set nima? (1.74-rasm)
Rasmiy hujjat bo‘yicha: **Set** — bu takrorlanmaydigan (unique) elementlar to‘plami.

Set xususiyatlari:
- takror element bo‘lmaydi;
- `in` bilan tekshirish juda tez;
- indeks yo‘q (`s[0]` bo‘lmaydi);
- tartib kafolatlanmaydi (ko‘p hollarda tartib baribir kerak bo‘lmaydi);
- mutable: qo‘shish/o‘chirish mumkin.

O‘xshatish: set — to‘garakka yozilganlar ro‘yxati. Bir o‘quvchi ikki marta yozilsa ham, ro‘yxatda u bir marta turadi.

```python
mevalar = {"olma", "nok", "olma", "uzum"}
print(mevalar)          # {'nok', 'olma', 'uzum'} (tartib boshqacha bo'lishi mumkin)
print("nok" in mevalar) # True
```

### 2.2. Set yaratish va bo‘sh set (1.75-rasm)
Set `{ }` qavslar bilan yaratiladi — **bo‘sh set bundan mustasno**. Bo‘sh `{}` Pythonda bo‘sh **dictionary** bo‘ladi (uni 15-darsda o‘rganamiz). Bo‘sh set yaratish uchun `set()` yoziladi.

```python
a = {}
b = set()
print(type(a))  # <class 'dict'>
print(type(b))  # <class 'set'>
```

### 2.3. Element qo‘shish va o‘chirish (1.76-rasm)
Set mutable, shuning uchun:
- **`add(x)`** — elementni qo‘shadi (agar u bor bo‘lsa, hech narsa o‘zgarmaydi);
- **`remove(x)`** — elementni o‘chiradi.

```python
tillar = {"Python", "SQL"}
tillar.add("Bash")
tillar.add("Python")    # takror: qo'shilmaydi
tillar.remove("SQL")
print(tillar)           # {'Python', 'Bash'}
```

### 2.4. Indeks yo‘q
```python
s = {10, 20, 30}
print(s[0])  # TypeError: 'set' object is not subscriptable
```
Setda «birinchi», «ikkinchi» element tushunchasi yo‘q. Elementni olish o‘rniga, uning **bor-yo‘qligini** `in` bilan tekshiramiz.

### 2.5. Ikkita setni birlashtirish (1.77, 1.78-rasm)
Faraz qilaylik, bizda ikkita set bor va ularni birlashtirish kerak. Setning muhim xususiyati — dublikat qabul qilmaydi. Shuning uchun ikkala setda bir xil element bo‘lsa, set ulardan bittasini saqlab qoladi.

```python
a_guruh = {"Ali", "Vali", "Laylo"}
b_guruh = {"Laylo", "Sardor"}
hammasi = a_guruh | b_guruh          # yoki a_guruh.union(b_guruh)
print(hammasi)  # {'Ali', 'Vali', 'Laylo', 'Sardor'} — Laylo bir marta
```

### 2.6. Dublikatlarni olib tashlash (1.79-rasm)
`nums` — bu list. `unique = set(nums)` deb yozsak, listdagi takror elementlar olib tashlanadi.

```python
nums = [1, 2, 2, 3, 3, 3, 4]
unique = set(nums)
print(unique)   # {1, 2, 3, 4}
```

### 2.7. Setni tartiblash
Set — tartiblanmagan tur. Agar tartiblangan ko‘rinish kerak bo‘lsa, `sorted()` ishlatiladi; u tartiblangan **list** qaytaradi.

```python
baholar = {5, 3, 4, 2}
print(sorted(baholar))  # [2, 3, 4, 5]
```

## 3. Kod namunalari

### Namuna 1: Takrorlanmas mehmonlar
```python
royxat = ["Ali", "Vali", "Ali", "Laylo", "Vali"]
mehmonlar = set(royxat)
print("Mehmonlar soni:", len(mehmonlar))  # 3
print(sorted(mehmonlar))                  # ['Ali', 'Laylo', 'Vali']
```

### Namuna 2: Tez tekshiruv
```python
bloklangan = {"spam_bot", "fake_user"}
login = "spam_bot"
if login in bloklangan:
    print("Kirish taqiqlangan!")
else:
    print("Xush kelibsiz!")
```

### Namuna 3: Ikki to‘garak a'zolari
```python
python_togarak = {"Ali", "Laylo", "Sardor"}
robot_togarak = {"Sardor", "Madina"}
barcha = python_togarak | robot_togarak
print("Jami a'zolar:", len(barcha))  # 4
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Takrorlarsiz sonlar (oson)
`nums = [4, 1, 4, 2, 1, 5]` listidagi takrorlarni olib tashlang va natijani tartiblangan holda chiqaring.

**Kutiladigan natija:** `[1, 2, 4, 5]`

**Yechim:**
```python
nums = [4, 1, 4, 2, 1, 5]
print(sorted(set(nums)))
```

### 2-topshiriq. Bo‘sh set (oson)
Bo‘sh set yarating, unga `"Python"`, `"Linux"`, `"Python"` ni qo‘shing va natijani hamda uzunligini chiqaring.

**Kutiladigan natija:** 2 ta element: `Python` va `Linux` (tartib har xil bo‘lishi mumkin), `len` = `2`.

**Yechim:**
```python
s = set()
s.add("Python")
s.add("Linux")
s.add("Python")
print(s, len(s))
```

### 3-topshiriq. Xatoni toping (o‘rta)
Quyidagi kodda 2 ta xato bor. Toping va tuzating.
```python
mevalar = {}
mevalar.add("olma")
print(mevalar[0])
```

**Kutiladigan natija:** Ishlaydigan kod, `{'olma'}` chiqadi.

**Yechim:** 1) `{}` — bo‘sh dict, bo‘sh set uchun `set()` kerak; 2) setda indeks yo‘q, `mevalar[0]` o‘rniga butun setni chiqaramiz.
```python
mevalar = set()
mevalar.add("olma")
print(mevalar)
```

### 4-topshiriq. Ikki sinf birlashmasi (o‘rta)
`sinf_a = {"Ali", "Vali", "Laylo"}`, `sinf_b = {"Laylo", "Sardor", "Ali"}`. Ikkala sinfni birlashtirib, jami nechta turli o‘quvchi borligini chiqaring.

**Kutiladigan natija:** `Jami: 4 ta o'quvchi`

**Yechim:**
```python
sinf_a = {"Ali", "Vali", "Laylo"}
sinf_b = {"Laylo", "Sardor", "Ali"}
hammasi = sinf_a | sinf_b
print(f"Jami: {len(hammasi)} ta o'quvchi")
```

### 5-topshiriq. Takrorlanmas so‘zlar (qiyin)
Foydalanuvchi matn kiritadi. Matndagi takrorlanmas so‘zlarni alifbo tartibida va ularning sonini chiqaring (`lower()` va `split()` 4-haftadan).

**Kutiladigan natija** (kiritish: `Salom dunyo salom Python`):
```text
['dunyo', 'python', 'salom']
Takrorlanmas so'zlar: 3 ta
```

**Yechim:**
```python
matn = input("Matn kiriting: ")
sozlar = set(matn.lower().split())
print(sorted(sozlar))
print(f"Takrorlanmas so'zlar: {len(sozlar)} ta")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **Set qanday elementlar to‘plami?**
   - *Javob:* Takrorlanmaydigan (unique) elementlar to‘plami.
2. **Bo‘sh set qanday yaratiladi? `{}` nima bo‘ladi?**
   - *Javob:* `set()`; `{}` esa bo‘sh dictionary.
3. **Nega `s[0]` setda ishlamaydi?**
   - *Javob:* Setda indeks yo‘q, tartib kafolatlanmaydi.
4. **Listdagi dublikatlarni qanday olib tashlash mumkin?**
   - *Javob:* `set(nums)` orqali.
5. **Setni tartiblangan ko‘rinishda qanday chiqaramiz?**
   - *Javob:* `sorted(s)` — tartiblangan list qaytaradi.

## 6. Uyga vazifa

1. `set_mashq.py` faylida `[3, 7, 3, 9, 7, 1, 9]` listidan takrorlarni olib tashlab, tartiblangan holda chiqaring.
2. Ikki do‘stingiz sevgan o‘yinlarni ikkita set qilib yozing va birlashtiring: jami nechta turli o‘yin bor?
3. Bloklangan loginlar setini yarating va foydalanuvchi kiritgan login bloklanganini `in` bilan tekshiring.
