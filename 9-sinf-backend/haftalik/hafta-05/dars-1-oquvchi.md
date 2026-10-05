# 13-dars. Tuple (kortej): o‘zgarmas ketma-ketlik

> List’ni hamma o‘zgartira oladi, tuple’ni esa hech kim. Bugun «muhrlangan» ma’lumotlar — koordinatalar, ranglar va sozlamalarni xavfsiz saqlashni o‘rganamiz.

## Dars xulosasi

- **Tuple** — tartibli (ordered) elementlar to‘plami, list’ga o‘xshaydi.
- Eng katta farq: tuple **o‘zgarmas (immutable)** — yaratilgandan keyin elementlarini o‘zgartirib bo‘lmaydi.
- Tuple `( )` qavslar va elementlar orasidagi vergul bilan yaratiladi.
- Bitta elementli tupleda **vergul shart**: `(5,)` — tuple, `(5)` — oddiy `int`.
- Tuple’da indeks va slicing ishlaydi: `t[0]`, `t[-1]`, `t[1:3]`.
- O‘zgartirish kerak bo‘lsa: `list()` → o‘zgartirish → `tuple()`.
- Metodlar: `count()` — sanaydi, `index()` — indeksni topadi.

## Qo'shimcha ma'lumot

### Tuple qachon kerak?
Rasmiy qo‘llanmada uchta holat bor:
1. **O‘zgarmas ma’lumot**: Toshkentning koordinatasi `(41.31, 69.28)` hech qachon o‘zgarmaydi. Rang `(255, 128, 0)` — RGB qiymat.
2. **Funksiya bir nechta qiymat qaytarganda** — buni 6-haftada funksiyalarda ko‘rasiz.
3. **«Record» (kichik yozuv)**: `("Ali", "Valiyev", 2011)` — bitta odam haqidagi bog‘liq ma’lumotlar.

Hayotiy o‘xshatish: list — qalam bilan yozilgan daftar, tuple — notarius muhr bosgan hujjat.

### Vergulning sirli kuchi
Ko‘pchilik tuple’ni qavs yaratadi deb o‘ylaydi. Aslida tuple’ni **vergul** yaratadi:
```python
a = (5)     # bu shunchaki 5 soni
b = (5,)    # bu tuple
print(type(a), type(b))
# <class 'int'> <class 'tuple'>
```
Matematikada `(2 + 3) * 4` dagi qavs — oddiy guruhlash. Python ham `(5)` ni shunday tushunadi.

### Tuple’ni «o‘zgartirish» yo‘li
Tuple’ning o‘zini o‘zgartirib bo‘lmaydi, lekin undan yangi tuple yasash mumkin:
```python
rang = (255, 128, 0)
r = list(rang)     # [255, 128, 0]  — endi o'zgartirsa bo'ladi
r[0] = 100
rang = tuple(r)    # (100, 128, 0)  — yana muhrladik
```

### count() va index()
```python
baholar = (5, 4, 5, 3, 5)
print(baholar.count(5))   # 3 — beshlik 3 marta
print(baholar.index(4))   # 1 — 4 birinchi bo'lib 1-indeksda
```
`index()` faqat **birinchi** uchragan joyni qaytaradi. Element umuman bo‘lmasa, xato (`ValueError`) chiqadi.

### Odatiy xatolar
- `t[0] = 10` → `TypeError: 'tuple' object does not support item assignment`. Tuple o‘zgarmas!
- `t.append(4)` → `AttributeError`: tuple’da `append` yo‘q (u list metodi).
- `(7)` ni tuple deb o‘ylash — vergulni unutmang: `(7,)`.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Tuple (kortej) | Tartibli, o‘zgarmas elementlar to‘plami |
| Immutable | O‘zgarmas: yaratilgach o‘zgartirib bo‘lmaydi |
| Mutable | O‘zgaruvchan: elementlarini o‘zgartirish mumkin (list) |
| Ordered | Tartibli: elementlar joyi saqlanadi |
| Indeks | Elementning tartib raqami (0 dan boshlanadi) |
| Slicing | Ketma-ketlikdan bo‘lak qirqib olish: `t[1:3]` |
| count() | Element necha marta uchrashini sanovchi metod |
| index() | Element indeksini topuvchi metod |
| Record | Bitta obyekt haqidagi bog‘liq ma’lumotlar yozuvi |

## Bilasizmi?

- «Tuple» so‘zi matematikadagi *double, triple, quadruple* (ikkilik, uchlik, to‘rtlik) so‘zlarining umumiy oxiridan olingan.
- Xaritalar va navigatorlar joylashuvni `(kenglik, uzunlik)` juftligi ko‘rinishida saqlaydi — bu tuple uchun eng yaxshi misol.
- Ekrandagi har bir rang uchta son bilan yoziladi: qizil, yashil, ko‘k (RGB). `(255, 0, 0)` — sof qizil.

## Topshiriqlar

### 1. Mening tuple’im · oson
`(ism, familiya, tug‘ilgan_yil)` ko‘rinishida tuple yarating va har bir elementni alohida qatorda chiqaring.
**Kutiladigan natija:** 3 qatorda ism, familiya va yil.

### 2. Vergul sinovi · oson
`x = (7)` va `y = (7,)` ning turini `type()` bilan chiqaring.
**Kutiladigan natija:** `<class 'int'>` va `<class 'tuple'>`.

### 3. Hafta kunlari · oson
Haftaning 7 kunini tuple’ga yozing. Birinchi va oxirgi kunni (manfiy indeks bilan) chiqaring.
**Kutiladigan natija:** `Dushanba` va `Yakshanba`.

### 4. Ish kunlari · oson
3-topshiriqdagi tuple’dan slicing bilan faqat ish kunlarini (birinchi 5 kun) oling.
**Kutiladigan natija:** 5 ta kundan iborat tuple.

### 5. Bu kod nima chiqaradi? · o'rta
```python
t = (10, 20, 30, 40, 50)
print(t[1:4])
print(t[-2])
print(t.index(30))
```
Avval daftarga javob yozing, keyin tekshiring.
**Kutiladigan natija:** 3 qator natija va sizning bashoratingiz bilan solishtirish.

### 6. Rangni yangilash · o'rta
`rang = (0, 0, 255)`. Ikkinchi elementni `200` ga o‘zgartiring (list orqali) va qayta tuple qiling.
**Kutiladigan natija:** `(0, 200, 255)`

### 7. Xatoni toping · o'rta
```python
shahar = ("Toshkent", 41.31, 69.28)
shahar[0] = "Samarqand"
print(shahar)
```
Nega xato chiqadi? Kodni to‘g‘ri ishlaydigan qilib tuzating.
**Kutiladigan natija:** `('Samarqand', 41.31, 69.28)`

### 8. Beshliklar soni · o'rta
`baholar = (5, 4, 5, 3, 5, 4)`. Nechta 5 va nechta 4 borligini `count()` bilan chiqaring.
**Kutiladigan natija:** `5: 3 ta`, `4: 2 ta`.

### 9. Baholar statistikasi · qiyin
`baholar = (5, 3, 4, 5, 5, 2, 4, 5)`. `for` sikli va `count()` yordamida 2 dan 5 gacha har bir baho necha marta uchraganini chiqaring.
**Kutiladigan natija:** 4 qator: `2 bahosi: 1 marta` ... `5 bahosi: 4 marta`.

### 10. Sozlamalar tuple’i · qiyin
Dars sozlamalarini tuple’da saqlang: `(dars_daqiqa, tanaffus_daqiqa, haftada_dars)` = `(80, 10, 3)`. Haftada jami necha daqiqa dars bo‘lishini hisoblang.
**Kutiladigan natija:** `Haftada: 240 daqiqa`

### 11. Eng ko‘p uchragan · qiyin
`(3, 1, 3, 2, 3, 1)` tuple’ida eng ko‘p uchragan sonni `for` va `count()` yordamida toping.
**Kutiladigan natija:** `Eng ko'p: 3 (3 marta)`

### 12. Shaharlar xaritasi · bonus
3 ta shahar uchun `(nom, kenglik, uzunlik)` tuple’larini yarating va ularni bitta list ichiga joylang. `for` bilan har bir shaharni `Toshkent: 41.31, 69.28` formatida chiqaring. Koordinatalarni internetdan toping.
**Kutiladigan natija:** 3 qatorda shaharlar va koordinatalar.

## O'zingizni tekshiring

1. Tuple bilan list’ning eng katta farqi nima?
2. Tuple qachon ishlatiladi? Uchta holatni ayting.
3. Nega `(5)` tuple emas?
4. Tuple elementini o‘zgartirmoqchi bo‘lsak, qanday yo‘l tutamiz?
5. `count()` va `index()` metodlari nima qaytaradi?
6. `t = (1, 2, 3)` bo‘lsa, `t[-1]` nimaga teng?

## Uyga vazifa

1. `tuple_mashq.py`: haftaning 7 kunini tuple’da saqlang; birinchi, oxirgi kunni va ish kunlarini (slicing) chiqaring.
2. `(2, 5, 5, 3, 5, 4, 2)` tuple’ida har bir son necha marta uchrashini `count()` bilan chiqaring.
3. Sevimli shahringiz koordinatasini tuple’da saqlang, list orqali uzunlikni o‘zgartirib, qayta tuple qiling.
