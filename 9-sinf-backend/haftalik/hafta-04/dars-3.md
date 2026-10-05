# 12-dars. List (ro‘yxat): yaratish, indeks va metodlar

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 12-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga `list` (ro‘yxat) ning xususiyatlarini (tartibli, o‘zgaruvchan), yaratish, indeks va slicing, hamda `append()`, `insert()`, `remove()`, `pop()`, `clear()` metodlarini o‘rgatish.

**Kutiladigan natija:**
- List tartibli (ordered) va o‘zgaruvchan (mutable) ekanini, turli tipdagi qiymatlarni saqlashini biladi;
- `[ ]` bilan list yaratadi, indeks va slicing ishlatadi;
- Elementni indeks orqali o‘zgartiradi;
- `append`, `insert`, `remove`, `pop`, `clear` ni farqlab qo‘llaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–7 daq | Takrorlash | 11-dars: indeks, slicing, `upper()/lower()` |
| 7–22 daq | Yangi mavzu 1 | List nima? Yaratish, indeks, slicing, string bilan o‘xshashlik |
| 22–35 daq | Yangi mavzu 2 | Mutable list: `a[1] = 99`, `append()`, `insert()` |
| 35–40 daq | Tanaffus | Ko‘z mashqlari |
| 40–52 daq | Yangi mavzu 3 | `remove()`, `pop()`, `clear()` va farqlari |
| 52–75 daq | Amaliyot | Mini-loyiha: «fanlar ro‘yxati» |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

## 2. Konspekt

### 2.1. List nima?
**List** — bu tartibli (ordered) elementlar to‘plami. Unda:
- elementlar ketma-ket saqlanadi (indeks bor);
- bir xil yoki turli tipdagi qiymatlar bo‘lishi mumkin;
- **o‘zgaruvchan (mutable)**: ichidagi elementlarni o‘zgartirish, qo‘shish, o‘chirish mumkin.

### 2.2. List yaratish (1.57, 1.58-rasm)
```python
a = [10, 20, 30]
b = ["olma", "banan", "gilos"]
c = [1, "Ali", 3.14, True]   # turli tiplar
nums = [1, 2, 3]
```
Bo‘sh `[ ]` ham list yaratadi; keyin elementlar qo‘shiladi.

### 2.3. Indeks va slicing (1.59, 1.60-rasm)
List ham string kabi ketma-ketlik: indeks 0 dan boshlanadi, `-1` oxirgi element.
```python
a = ["a", "b", "c", "d", "e"]
print(a[0])      # a
print(a[-1])     # e (oxirgi)
print(a[1:4])    # ['b', 'c', 'd']
print(a[:3])     # ['a', 'b', 'c']
print(a[3:])     # ['d', 'e']
print(a[::2])    # ['a', 'c', 'e']
print(a[::-1])   # ['e', 'd', 'c', 'b', 'a']
```
Slicing qoidalari stringniki bilan bir xil: `[boshlanish : tugash : qadam]`.

### 2.4. List o‘zgaruvchan — string esa yo‘q (1.61-rasm)
```python
a = [10, 20, 30]
a[1] = 99
print(a)   # [10, 99, 30]
```
String `s[0] = "J"` da `TypeError` berardi; listda indeks orqali yangi qiymat berish mumkin.

### 2.5. append() va insert() (1.62, 1.63-rasm)
```python
a = [1, 2]
a.append(3)
print(a)        # [1, 2, 3]  (oxiriga qo'shadi)

a = [1, 2, 3]
a.insert(1, 99)
print(a)        # [1, 99, 2, 3]  (list.insert(index, value))
```

### 2.6. remove(), pop(), clear() (1.64–1.66-rasm)
```python
a = [1, 2, 2, 3]
a.remove(2)
print(a)        # [1, 2, 3]  (birinchi uchragan 2 o'chdi)

a = [10, 20, 30]
x = a.pop()     # oxirgisi
y = a.pop(0)    # 0-indeksdagi
print(x, y)     # 30 10
print(a)        # [20]

a = [1, 2, 3]
a.clear()
print(a)        # []
```
| Metod | Nima qiladi |
|---|---|
| `append(v)` | oxiriga qo‘shadi |
| `insert(i, v)` | `i`-indeksga qo‘shadi |
| `remove(v)` | qiymat bo‘yicha (birinchisini) o‘chiradi |
| `pop()` / `pop(i)` | oxirgisini / `i`-indeksdagini olib tashlaydi |
| `clear()` | hammasini o‘chiradi |

## 3. Kod namunalari

### Namuna 1: Fanlar ro‘yxati
```python
fanlar = ["Matematika", "Fizika", "Informatika"]
print(fanlar[0])
print(fanlar[-1])
fanlar.append("Kimyo")
fanlar.insert(1, "Ona tili")
print(fanlar)
```
Natija: `Matematika`, `Informatika`, `['Matematika', 'Ona tili', 'Fizika', 'Informatika', 'Kimyo']`.

### Namuna 2: Olib tashlash usullari
```python
fanlar = ["Matematika", "Ona tili", "Fizika", "Kimyo"]
fanlar.remove("Fizika")
oxirgi = fanlar.pop()
print(oxirgi)    # Kimyo
print(fanlar)    # ['Matematika', 'Ona tili']
```

### Namuna 3: Listni string kabi kesish
```python
a = [10, 20, 30, 40, 50]
print(a[1:4])    # [20, 30, 40]
print(a[::-1])   # [50, 40, 30, 20, 10]
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Meva ro‘yxati (oson)
`mevalar = ["olma", "banan", "gilos"]` yarating, birinchi va oxirgi elementni chiqaring.

**Kutiladigan natija:** `olma gilos`

**Yechim:**
```python
mevalar = ["olma", "banan", "gilos"]
print(mevalar[0], mevalar[-1])
```

### 2-topshiriq. Qo‘shish (oson)
`a = [1, 2]` ga `append(3)`, so‘ng `insert(0, 0)` qo‘llang.

**Kutiladigan natija:** `[0, 1, 2, 3]`

**Yechim:**
```python
a = [1, 2]
a.append(3)
a.insert(0, 0)
print(a)
```

### 3-topshiriq. Bashorat (o‘rta)
Kod nima chiqaradi?
```python
a = [1, 2, 2, 3]
a.remove(2)
x = a.pop(0)
print(x, a)
```

**Kutiladigan natija:** `1 [2, 3]`

**Yechim:** `remove(2)` birinchi 2 ni o‘chiradi → `[1, 2, 3]`; `pop(0)` birinchi elementni (1) qaytaradi → `a = [2, 3]`.

### 4-topshiriq. Mini-loyiha: talabaning fanlari (qiyin)
Talaba ismini string, fanlarini list sifatida saqlang: 3 fan bilan boshlang, 1 fan qo‘shing (`append`), 1 fanni 1-o‘ringa qo‘ying (`insert`), bitta fanni `remove` qiling, oxirgisini `pop` qiling va natijalarni chiqaring.

**Kutiladigan natija:** har bosqichda o‘zgargan ro‘yxat.

**Yechim:**
```python
ism = "Dilnoza Karimova"
fanlar = ["Matematika", "Fizika", "Informatika"]
print(ism, fanlar)

fanlar.append("Kimyo")
fanlar.insert(1, "Ona tili")
print(fanlar)

fanlar.remove("Fizika")
oxirgi = fanlar.pop()
print("Olib tashlandi:", oxirgi)
print(fanlar)
```
Natija: oxirida `['Matematika', 'Ona tili', 'Informatika']`.

## 5. Tezkor nazorat (savollar va javoblar)

1. **List qanday xususiyatlarga ega?**
   - *Javob:* Tartibli (indeks bor), turli tipdagi qiymatlar saqlay oladi, o‘zgaruvchan (mutable).
2. **`a = [10, 20, 30]; a[1] = 99` natijasi?**
   - *Javob:* `[10, 99, 30]`.
3. **`append()` va `insert()` farqi?**
   - *Javob:* `append` oxiriga qo‘shadi, `insert(index, value)` belgilangan joyga.
4. **`remove(2)` dublikat bo‘lsa nima qiladi?**
   - *Javob:* Birinchi uchraganini o‘chiradi.
5. **`pop()` va `pop(0)` farqi?**
   - *Javob:* `pop()` oxirgisini, `pop(0)` 0-indeksdagini olib tashlaydi (qaytaradi).

## 6. Uyga vazifa

1. `royxat.py` da 5 ta sevimli filmingiz ro‘yxatini yarating; birinchi, oxirgi elementni, `[1:4]` va `[::-1]` ni chiqaring.
2. `a = [1, 2]` ni `append`, `insert`, `remove`, `pop`, `clear` ketma-ketligi bilan o‘zgartirib, har qadamdan keyin chiqaring.
3. «Talabalar ma’lumotlari» loyihasining boshlanishi: ism va familiyani string, fanlarni list qiling (qolgan qismi 5-haftada).
