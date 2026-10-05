# 15-dars. Dictionary (dict): kalit-qiymat va amaliy loyiha

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + loyiha amaliyoti · **I-bob**, 15-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga `dictionary` (`dict`, lug‘at) tuzilmasini — `key: value` juftliklarini, uning xususiyatlarini, kalit orqali qiymat olishni (`dict["key"]` va `dict.get()`), qiymatni yangilash va yangi juftlik qo‘shishni o‘rgatish; 4–5-hafta yakunida beshta tuzilmani (string, list, tuple, set, dict) bitta «Talabalar ma’lumotlari» loyihasida birlashtirish.

**Kutiladigan natija:**
- Dictionary `key: value` juftliklarda saqlanishini va uning 4 ta xususiyatini aytadi;
- `user["name"]` bilan qiymat oladi va kalit bo‘lmasa xato chiqishini biladi;
- `user.get("phone", "yo'q")` bilan xatosiz murojaat qiladi;
- `user["age"] = 23` bilan qiymatni yangilaydi, `user["phone"] = "+99890"` bilan yangi juftlik qo‘shadi;
- String, list, tuple, set va dict ni bitta dasturda to‘g‘ri tanlab ishlatadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 14-dars: set, `add()`, `set(nums)`, `sorted()` |
| 5–20 daq | Yangi mavzu 1 | Dictionary nima? Xususiyatlari, sintaksis (1.80-rasm) |
| 20–35 daq | Yangi mavzu 2 | Kalit orqali olish: `dict["key"]`, `get()` (1.81-rasm) |
| 35–40 daq | Tanaffus | Ko‘z mashqlari |
| 40–50 daq | Yangi mavzu 3 | Yangilash va qo‘shish (1.82-rasm); 5 ta tuzilma taqqoslash |
| 50–75 daq | Loyiha | «Talabalar ma’lumotlari» mini-loyihasi |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

## 2. Konspekt

### 2.1. Dictionary nima? (1.80-rasm)
Rasmiy hujjat bo‘yicha: **Dictionary** — bu `key: value` juftliklarda saqlanadigan tuzilma.

Xususiyatlari:
- kalit orqali tez topiladi;
- mutable (yangilash, qo‘shish, o‘chirish mumkin);
- kalit (key) unikal bo‘ladi;
- Python 3.7+ da kiritilgan tartib saqlanadi (amaliyotda foydali).

O‘xshatish: haqiqiy lug‘at. So‘z (kalit) bo‘yicha uning ma’nosini (qiymat) topamiz. Yoki telefon kontaktlari: ism → raqam.

```python
user = {
    "name": "Ali",
    "age": 15,
    "city": "Toshkent"
}
print(user)
```

### 2.2. Kalit orqali qiymat olish (1.81-rasm)
Qiymat kerak bo‘lsa, `dict["key"]` — kalitga murojaat qilamiz. Agar kalit bo‘lmasa, **xato** chiqadi.

```python
print(user["name"])   # Ali
print(user["phone"])  # KeyError: 'phone'
```

Xato olishni xohlamasak, `get()` ishlatamiz — u xato bermaydi, kod to‘xtamaydi:

```python
print(user.get("phone", "yo'q"))  # yo'q
print(user.get("city", "yo'q"))   # Toshkent
```

### 2.3. Yangilash va qo‘shish (1.82-rasm)
- `user["age"] = 23` — mavjud kalit qiymati **yangilanadi**: kalitga murojaat qilinadi va `=` orqali yangi qiymat beriladi.
- `user["phone"] = "+99890"` — yangi kalit va qiymat beriladi, ya’ni **yangi element (key: value) qo‘shiladi**.

```python
user["age"] = 23
user["phone"] = "+99890"
print(user)
# {'name': 'Ali', 'age': 23, 'city': 'Toshkent', 'phone': '+99890'}
```

Diqqat: bitta yozuv `d[key] = value` ikki ishni qiladi — kalit bor bo‘lsa yangilaydi, bo‘lmasa qo‘shadi. Kalit unikal bo‘lgani uchun bir xil kalit ikki marta turmaydi.

### 2.4. Dict — if/else o‘rniga (DRY’ga tayyorgarlik)
Hujjatda (1.88-rasm) til bo‘yicha salomlashuvni ko‘p `if/else` o‘rniga dict bilan yozish ko‘rsatilgan. Kalitga murojaat qilsak, kerakli matn darhol olinadi:

```python
texts = {"uzl": "Salom!", "rus": "Привет!", "en": "Hello!"}
til = "en"
print(texts[til])  # Hello!
```

Bu g‘oyani 6-haftada DRY prinsipida chuqurroq ko‘ramiz.

### 2.5. Beshta tuzilma: qaysi birini tanlash kerak?

| Tuzilma | Ko‘rinishi | O‘zgaradimi? | Qachon |
|---|---|---|---|
| string | `"Ali"` | Yo‘q | Matn, ism |
| list | `[1, 2, 3]` | Ha | Tartibli ro‘yxat, fanlar |
| tuple | `(41.3, 69.2)` | Yo‘q | O‘zgarmas ma’lumot, record |
| set | `{5, 4}` | Ha | Takrorsiz to‘plam |
| dict | `{"ism": "Ali"}` | Ha | Kalit bo‘yicha topish |

## 3. Amaliy loyiha: «Talabalar ma’lumotlari»

Rasmiy hujjatdagi topshiriq. Dasturda:
- talabaning ismi va familiyasini **string** yordamida saqlang;
- fanlar ro‘yxatini **list** ko‘rinishida yarating;
- o‘zgarmas shaxsiy ma’lumotlarni **tuple** da saqlang;
- takrorlanuvchi baholarni **set** orqali tartibga soling;
- talaba haqidagi umumiy ma’lumotlarni **dictionary** da jamlang.

**Yechim (namuna):**
```python
# 1. string
ism = "Ali"
familiya = "Valiyev"

# 2. list
fanlar = ["Matematika", "Informatika", "Fizika"]
fanlar.append("Ingliz tili")

# 3. tuple: o'zgarmas shaxsiy ma'lumot (tug'ilgan yil, guvohnoma)
shaxsiy = (2011, "AB1234567")

# 4. set: takrorlanuvchi baholar
baholar_royxati = [5, 4, 5, 5, 3, 4, 5]
turli_baholar = sorted(set(baholar_royxati))

# 5. dict: hammasini jamlash
talaba = {
    "toliq_ism": ism + " " + familiya,
    "fanlar": fanlar,
    "shaxsiy": shaxsiy,
    "baholar": turli_baholar,
}
talaba["sinf"] = "9-sinf"

print("Talaba:", talaba["toliq_ism"])
print("Fanlar soni:", len(talaba["fanlar"]))
print("Tug'ilgan yil:", talaba["shaxsiy"][0])
print("Turli baholar:", talaba["baholar"])
print("Telefon:", talaba.get("telefon", "kiritilmagan"))
print("Sinf:", talaba["sinf"])
```

**Kutiladigan natija:**
```text
Talaba: Ali Valiyev
Fanlar soni: 4
Tug'ilgan yil: 2011
Turli baholar: [3, 4, 5]
Telefon: kiritilmagan
Sinf: 9-sinf
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Mening kartam (oson)
`ism`, `yosh`, `shahar` kalitlari bilan o‘zingiz haqingizda dict yarating va `ism` ni chiqaring.

**Kutiladigan natija:** `Ali`

**Yechim:**
```python
men = {"ism": "Ali", "yosh": 15, "shahar": "Toshkent"}
print(men["ism"])
```

### 2-topshiriq. Xatosiz murojaat (oson)
Yuqoridagi dict’dan `telefon` kalitini xato chiqarmasdan oling; topilmasa `"yo'q"` chiqsin.

**Kutiladigan natija:** `yo'q`

**Yechim:**
```python
print(men.get("telefon", "yo'q"))
```

### 3-topshiriq. Bashorat (o‘rta)
Kod nima chiqaradi?
```python
d = {"a": 1, "b": 2}
d["a"] = 10
d["c"] = 3
print(d)
print(len(d))
```

**Kutiladigan natija:** `{'a': 10, 'b': 2, 'c': 3}` va `3`.

**Yechim:** `d["a"] = 10` mavjud kalitni yangiladi, `d["c"] = 3` yangi juftlik qo‘shdi; jami 3 ta kalit.

### 4-topshiriq. Til tanlash (o‘rta)
`texts = {"uz": "Salom", "ru": "Привет", "en": "Hello"}`. Foydalanuvchi til kodini kiritadi; mos salomlashuv chiqsin, noma'lum kod bo‘lsa `"Til topilmadi"`.

**Kutiladigan natija:** `en` → `Hello`; `de` → `Til topilmadi`.

**Yechim:**
```python
texts = {"uz": "Salom", "ru": "Привет", "en": "Hello"}
kod = input("Til kodi: ")
print(texts.get(kod, "Til topilmadi"))
```

### 5-topshiriq. «Talabalar ma’lumotlari» (qiyin)
Yuqoridagi 3-bo‘limdagi loyihani o‘z ma’lumotlaringiz bilan yozing va kamida 1 ta yangi kalit qo‘shing.

**Kutiladigan natija:** 5 ta tuzilma ishlatilgan, natija 6 qatorda chiqadi.

**Yechim:** 3-bo‘limdagi namuna kod.

## 5. Tezkor nazorat (savollar va javoblar)

1. **Dictionary qanday juftliklarda saqlanadi?**
   - *Javob:* `key: value` (kalit: qiymat).
2. **`user["phone"]` kalit bo‘lmasa nima bo‘ladi?**
   - *Javob:* Xato (`KeyError`) chiqadi, dastur to‘xtaydi.
3. **Xatosiz qanday murojaat qilinadi?**
   - *Javob:* `user.get("phone", "yo'q")`.
4. **`user["age"] = 23` qachon yangilaydi, qachon qo‘shadi?**
   - *Javob:* `age` kaliti bor bo‘lsa yangilaydi, bo‘lmasa yangi juftlik qo‘shadi.
5. **Takrorsiz baholar uchun qaysi tuzilma mos?**
   - *Javob:* `set`.

## 6. Uyga vazifa

1. `lugat.py` faylida 5 ta inglizcha so‘z va ularning o‘zbekcha tarjimasidan iborat dict yarating; foydalanuvchi so‘z kiritsa tarjimasi chiqsin, topilmasa `"Bunday so'z yo'q"` (`get()`).
2. «Talabalar ma’lumotlari» loyihasini yakunlang: yana bitta fan (`append`) va `telefon` kalitini qo‘shing.
