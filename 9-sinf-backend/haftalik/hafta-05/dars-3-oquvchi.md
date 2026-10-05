# 15-dars. Dictionary (dict): kalit-qiymat va amaliy loyiha

> Telefon kontaktlari, lug‘at, o‘yindagi profil — hammasi «kalit: qiymat» tamoyilida ishlaydi. Bugun dictionary’ni o‘rganamiz va beshta tuzilmani bitta «Talabalar ma’lumotlari» dasturida birlashtiramiz.

## Dars xulosasi

- **Dictionary (`dict`)** — `key: value` (kalit: qiymat) juftliklarda saqlanadigan tuzilma.
- Kalit orqali tez topiladi, kalit **unikal** bo‘ladi.
- Dict mutable: yangilash, qo‘shish, o‘chirish mumkin; Python 3.7+ da kiritilgan tartib saqlanadi.
- `d["key"]` — qiymatni oladi; kalit bo‘lmasa **xato** chiqadi.
- `d.get("key", "yo'q")` — xatosiz murojaat: kalit bo‘lmasa standart qiymat qaytadi.
- `d["age"] = 23` — mavjud kalitni yangilaydi; `d["phone"] = "+99890"` — yangi juftlik qo‘shadi.
- Har bir vazifaga mos tuzilmani tanlash: string, list, tuple, set, dict.

## Qo'shimcha ma'lumot

### Lug‘at o‘xshatishi
Haqiqiy lug‘atda siz so‘zni (kalit) topib, uning ma’nosini (qiymat) o‘qiysiz. Butun kitobni varaqlamaysiz. Dict ham shunday: kalitni bersangiz, qiymat darhol qaytadi.
```python
lugat = {"apple": "olma", "book": "kitob", "cat": "mushuk"}
print(lugat["book"])   # kitob
```

### `[]` yoki `get()`?
```python
user = {"name": "Ali", "age": 15}
print(user["name"])               # Ali
print(user.get("phone", "yo'q"))  # yo'q — dastur to'xtamaydi
print(user["phone"])              # KeyError — dastur to'xtaydi!
```
Qoida: kalit **aniq bor** bo‘lsa `[]`, **bo‘lmasligi mumkin** bo‘lsa `get()`.

### Bitta yozuv — ikki ish
```python
user["age"] = 16          # "age" bor -> yangilandi
user["city"] = "Xiva"     # "city" yo'q edi -> qo'shildi
print(user)
# {'name': 'Ali', 'age': 16, 'city': 'Xiva'}
```
Kalit unikal bo‘lgani uchun bir xil kalit ikki marta turolmaydi: yangi qiymat eskisining o‘rniga yoziladi.

### if/else zanjiri o‘rniga dict
Rasmiy qo‘llanmadagi misol: til kodiga qarab salomlashish. Uzun `if/elif` o‘rniga:
```python
texts = {"uzl": "Salom!", "rus": "Привет!", "en": "Hello!"}
print(texts["en"])   # Hello!
```
Yangi til qo‘shish uchun bitta qator yetadi. Bu g‘oyani keyingi haftada DRY prinsipida ko‘rasiz.

### Qaysi tuzilmani tanlash kerak?

| Vazifa | Tuzilma |
|---|---|
| Ism, matn | string |
| Fanlar ro‘yxati (o‘zgaradi) | list |
| Tug‘ilgan yil, koordinata (o‘zgarmaydi) | tuple |
| Takrorsiz baholar | set |
| Talaba haqida hamma ma’lumot, kalit bilan | dict |

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Dictionary (dict) | `key: value` juftliklarida saqlanadigan tuzilma |
| Key (kalit) | Qiymatni topish uchun ishlatiladigan unikal nom |
| Value (qiymat) | Kalitga bog‘langan ma’lumot |
| Juftlik (key: value) | Bitta kalit va uning qiymati |
| get() | Kalit bo‘lmasa xato bermasdan standart qiymat qaytaruvchi metod |
| KeyError | Mavjud bo‘lmagan kalitga `[]` bilan murojaatdagi xato |
| Mutable | O‘zgaruvchan: yangilash va qo‘shish mumkin |
| Unikal | Takrorlanmaydigan, yagona |

## Bilasizmi?

- Backend’da serverlar ma’lumotni ko‘pincha JSON ko‘rinishida almashadi — u Python dict’iga juda o‘xshaydi. Kelgusida FastAPI va Telegram botlarda buni ko‘p ishlatasiz.
- Telegram bot olgan har bir xabar ichida `"text"`, `"chat"`, `"from"` kabi kalitlar bor.
- Python 3.7 versiyasidan boshlab dict elementlar kiritilgan tartibni saqlaydi. Undan oldin tartib kafolatlanmas edi.

## Topshiriqlar

### 1. Mening kartam · oson
`ism`, `yosh`, `shahar` kalitlari bilan o‘zingiz haqingizda dict yarating va ismni chiqaring.
**Kutiladigan natija:** Ismingiz.

### 2. Xatosiz murojaat · oson
1-topshiriqdagi dict’dan `telefon` kalitini `get()` bilan oling; topilmasa `"yo'q"` chiqsin.
**Kutiladigan natija:** `yo'q`

### 3. Yoshni yangilash · oson
Dict’dagi `yosh` qiymatini 1 taga oshiring va dict’ni chiqaring.
**Kutiladigan natija:** Yangilangan yosh.

### 4. Yangi kalit · oson
Dict’ga `maktab` kalitini qo‘shing va `len()` bilan juftliklar sonini chiqaring.
**Kutiladigan natija:** `4`

### 5. Bu kod nima chiqaradi? · o'rta
```python
d = {"a": 1, "b": 2}
d["a"] = 10
d["c"] = 3
print(d)
print(len(d))
```
**Kutiladigan natija:** Bashoratingizni yozing va tekshiring.

### 6. Til tanlash · o'rta
`texts = {"uz": "Salom", "ru": "Привет", "en": "Hello"}`. Foydalanuvchi til kodini kiritadi; mos salomlashuv chiqsin, noma'lum bo‘lsa `"Til topilmadi"`.
**Kutiladigan natija:** `en` → `Hello`, `de` → `Til topilmadi`.

### 7. Xatoni toping · o'rta
```python
user = {"name": "Ali", "age": 15}
print(user["Name"])
```
Nega `KeyError` chiqadi? Ikki xil usulda tuzating.
**Kutiladigan natija:** `Ali`

### 8. Mini-lug‘at · o'rta
5 ta inglizcha so‘z va tarjimasidan dict yarating. Foydalanuvchi so‘z kiritsa tarjimasi, topilmasa `"Bunday so'z yo'q"` chiqsin.
**Kutiladigan natija:** `book` → `kitob`.

### 9. Narxlar jadvali · qiyin
`narx = {"non": 4000, "sut": 12000, "tuxum": 1500}`. Foydalanuvchi mahsulot nomi va sonini kiritadi; umumiy narx chiqsin. Mahsulot yo‘q bo‘lsa, xabar bering.
**Kutiladigan natija:** `sut`, `2` → `Jami: 24000 so'm`.

### 10. Talabalar ma’lumotlari · qiyin
Rasmiy loyiha: ism va familiyani **string**, fanlarni **list**, o‘zgarmas shaxsiy ma’lumotni **tuple**, takrorlanuvchi baholarni **set**, hammasini **dict** da jamlang va chiroyli chiqaring.
**Kutiladigan natija:** 5 ta tuzilma ishlatilgan, natija bir necha qatorda.

### 11. Ovoz berish · qiyin
`ovozlar = ["Ali", "Vali", "Ali", "Ali", "Vali"]`. `for` sikli va dict yordamida har bir nomzod nechta ovoz olganini hisoblang (`d[ism] = d.get(ism, 0) + 1`).
**Kutiladigan natija:** `{'Ali': 3, 'Vali': 2}`

### 12. Profil boti · bonus
Telegram bot profiliga o‘xshash dict yarating: `id`, `username`, `til`, `qiziqishlar` (list), `yaratilgan` (tuple: yil, oy, kun). Foydalanuvchiga uning tiliga mos salomlashuvni (2-dict orqali) chiqaring.
**Kutiladigan natija:** Tilga mos salom va profil ma’lumotlari.

## O'zingizni tekshiring

1. Dictionary ma’lumotni qanday ko‘rinishda saqlaydi?
2. Dictionary’ning 4 ta xususiyatini ayting.
3. `d["key"]` va `d.get("key")` ning farqi nima?
4. `d["x"] = 5` qachon yangilaydi, qachon qo‘shadi?
5. Nega dict’da bir xil kalit ikki marta bo‘lmaydi?
6. Takrorsiz baholar, o‘zgarmas tug‘ilgan yil va fanlar ro‘yxati uchun qaysi tuzilmalarni tanlaysiz?

## Uyga vazifa

1. `lugat.py`: 5 ta inglizcha so‘z va tarjimasidan dict yarating; kiritilgan so‘z tarjimasini `get()` bilan chiqaring.
2. «Talabalar ma’lumotlari» loyihasini yakunlang: yana bitta fan (`append`) va `telefon` kalitini qo‘shing.
