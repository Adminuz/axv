# 14-dars. Set (to‘plam): takrorlanmaydigan elementlar

> Bir xil ism ro‘yxatda besh marta yozilib qolganmi? Set ularni bir zumda bittaga aylantiradi. Bugun takrorsiz to‘plamlar va tezkor tekshiruvni o‘rganamiz.

## Dars xulosasi

- **Set** — takrorlanmaydigan (unique) elementlar to‘plami.
- Set’da takror element bo‘lmaydi, `in` bilan tekshirish juda tez.
- Set’da indeks yo‘q (`s[0]` ishlamaydi), tartib kafolatlanmaydi.
- Set mutable: `add()` bilan qo‘shish, `remove()` bilan o‘chirish mumkin.
- Set `{ }` bilan yaratiladi, lekin **bo‘sh set faqat `set()`** — `{}` bo‘sh dictionary.
- Ikki setni birlashtirganda dublikatlar o‘zi yo‘qoladi: `a | b`.
- `set(nums)` — listdagi takrorlarni olib tashlaydi; `sorted(s)` — tartiblangan list qaytaradi.

## Qo'shimcha ma'lumot

### Set — to‘garak ro‘yxati
Tasavvur qiling, Python to‘garagiga yozilish varag‘i bor. Ali shoshilib ikki marta yozildi. Lekin to‘garakda Ali baribir bitta! Set aynan shunday ishlaydi:
```python
yozilganlar = ["Ali", "Laylo", "Ali", "Sardor"]
azolar = set(yozilganlar)
print(azolar)        # {'Ali', 'Laylo', 'Sardor'}
print(len(azolar))   # 3
```

### Nega `{}` bo‘sh set emas?
Pythonda jingalak qavslarni ikki tuzilma ishlatadi: set va dictionary. Bo‘sh `{}` tarixan dictionary’ga tegishli. Shuning uchun bo‘sh set uchun maxsus yozuv bor:
```python
a = {}        # bo'sh dict
b = set()     # bo'sh set
print(type(a), type(b))
```

### Indeks yo‘q — demak «bormi?» deb so‘raymiz
Set’dan «birinchi elementni ber» deb bo‘lmaydi. Uning o‘rniga «bu element bormi?» deb so‘raymiz:
```python
bloklangan = {"spam_bot", "fake_user"}
print("spam_bot" in bloklangan)   # True
print("ali_2011" in bloklangan)   # False
```
Bunday tekshiruv set’da juda tez ishlaydi — hatto millionlab elementda ham.

### Birlashtirish
```python
a = {"Ali", "Vali"}
b = {"Vali", "Laylo"}
print(a | b)          # {'Ali', 'Vali', 'Laylo'}
print(a.union(b))     # xuddi shu natija
```
Vali ikkala setda bor edi, lekin natijada bir marta turibdi.

### Odatiy xatolar
- `s = {}` keyin `s.add(1)` → `AttributeError: 'dict' object has no attribute 'add'`.
- `s[0]` → `TypeError: 'set' object is not subscriptable`.
- Set’dagi tartibga ishonish: `print({3, 1, 2})` har doim siz yozgan tartibda chiqmasligi mumkin. Tartib kerak bo‘lsa — `sorted()`.
- `remove()` bilan yo‘q elementni o‘chirish → `KeyError`. Avval `in` bilan tekshiring.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Set (to‘plam) | Takrorlanmaydigan elementlar to‘plami |
| Unique | Unikal, yagona: takrorlanmaydigan |
| Dublikat | Takroriy, ikkinchi nusxa element |
| add() | Set’ga element qo‘shuvchi metod |
| remove() | Set’dan elementni o‘chiruvchi metod |
| Birlashtirish (union) | Ikki setning barcha elementlarini bitta setga yig‘ish: `a \| b` |
| in | Element bor-yo‘qligini tekshiruvchi operator |
| sorted() | Tartiblangan list qaytaruvchi funksiya |
| Mutable | O‘zgaruvchan: element qo‘shish/o‘chirish mumkin |

## Bilasizmi?

- Set g‘oyasi matematikadagi to‘plamlar nazariyasidan olingan. Uni XIX asrda nemis matematigi Georg Kantor asoslagan.
- Ijtimoiy tarmoqlar «umumiy do‘stlar» sonini ko‘rsatganda, aslida ikkita to‘plam ustida amal bajariladi.
- Spam-filtrlar ko‘pincha bloklangan manzillarni set kabi tuzilmada saqlaydi: tekshiruv bir zumda bo‘ladi.

## Topshiriqlar

### 1. Takrorlarsiz sonlar · oson
`nums = [4, 1, 4, 2, 1, 5]` dan takrorlarni olib tashlang va tartiblangan holda chiqaring.
**Kutiladigan natija:** `[1, 2, 4, 5]`

### 2. Bo‘sh set · oson
Bo‘sh set yarating, unga `"Python"`, `"Linux"`, `"Python"` ni qo‘shing va uzunligini chiqaring.
**Kutiladigan natija:** `2`

### 3. Bormi? · oson
`mevalar = {"olma", "nok", "uzum"}`. Foydalanuvchi meva nomini kiritadi; setda bor bo‘lsa `"Bor"`, bo‘lmasa `"Yo'q"` chiqsin.
**Kutiladigan natija:** `nok` → `Bor`, `anor` → `Yo'q`.

### 4. Turini aniqlang · oson
`a = {}`, `b = set()`, `c = {1, 2}` ning turlarini chiqaring.
**Kutiladigan natija:** `dict`, `set`, `set`.

### 5. Xatoni toping · o'rta
```python
mevalar = {}
mevalar.add("olma")
print(mevalar[0])
```
Bu kodda 2 ta xato bor. Ularni toping va tuzating.
**Kutiladigan natija:** Kod ishlaydi va `{'olma'}` chiqadi.

### 6. Ikki sinf · o'rta
`sinf_a = {"Ali", "Vali", "Laylo"}`, `sinf_b = {"Laylo", "Sardor", "Ali"}`. Birlashtiring va jami nechta turli o‘quvchi borligini chiqaring.
**Kutiladigan natija:** `Jami: 4 ta o'quvchi`

### 7. Bu kod nima chiqaradi? · o'rta
```python
s = {1, 2, 3}
s.add(2)
s.add(4)
s.remove(1)
print(sorted(s), len(s))
```
**Kutiladigan natija:** Bashoratingizni yozing va tekshiring.

### 8. Mehmonlar ro‘yxati · o'rta
`["Ali", "Vali", "Ali", "Laylo", "Vali", "Madina"]` listida nechta turli mehmon borligini va ularni alifbo tartibida chiqaring.
**Kutiladigan natija:** `4` va tartiblangan ismlar.

### 9. Takrorlanmas so‘zlar · qiyin
Foydalanuvchi matn kiritadi. Matndagi takrorlanmas so‘zlarni (kichik harflarda) alifbo tartibida va ularning sonini chiqaring.
**Kutiladigan natija:** `Salom dunyo salom Python` → `['dunyo', 'python', 'salom']`, `3 ta`.

### 10. Bloklangan loginlar · qiyin
Bloklangan loginlar setini yarating. Foydalanuvchidan login so‘rang: bloklangan bo‘lsa `"Kirish taqiqlangan"`, aks holda `"Xush kelibsiz"`, so‘ng yangi loginni ham `add()` bilan «faol foydalanuvchilar» setiga qo‘shing.
**Kutiladigan natija:** To‘g‘ri xabar va yangilangan set.

### 11. Takrorlar sonini toping · qiyin
`nums = [1, 2, 2, 3, 3, 3]`. Listda nechta element **takror** bo‘lganini `len(nums)` va `len(set(nums))` farqi orqali toping.
**Kutiladigan natija:** `Takrorlar: 3 ta`

### 12. Umumiy o‘yinlar · bonus
Ikki do‘stning sevimli o‘yinlarini ikkita set qilib yozing. Ikkalasi ham yoqtiradigan o‘yinlarni toping (`for` va `in` bilan yoki internetdan set uchun mos operatorni izlab).
**Kutiladigan natija:** Ikkalasiga ham yoqqan o‘yinlar ro‘yxati.

## O'zingizni tekshiring

1. Set qanday elementlar to‘plami?
2. Set’ning 5 ta xususiyatini sanab bering.
3. Bo‘sh set qanday yaratiladi va nega `{}` bo‘lmaydi?
4. Nega `s[0]` set’da ishlamaydi?
5. Ikki setni birlashtirganda bir xil elementlar bilan nima bo‘ladi?
6. Listdagi dublikatlarni qanday olib tashlash mumkin?
7. Set’ni tartiblangan holda qanday chiqaramiz?

## Uyga vazifa

1. `set_mashq.py`: `[3, 7, 3, 9, 7, 1, 9]` dan takrorlarni olib tashlab, tartiblangan holda chiqaring.
2. Ikki do‘stingizning sevimli o‘yinlarini ikki set qilib birlashtiring: jami nechta turli o‘yin?
3. Bloklangan loginlar setini yarating va kiritilgan loginni `in` bilan tekshiring.
