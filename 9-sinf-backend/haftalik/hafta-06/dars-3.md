# 18-dars. Fayllar bilan ishlash: open, with, o'qish va yozish

**Fan:** Advanced Back-end va DevOps
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 3-dars (umumiy 18-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `uslubiy-korsatma.txt`, I bob, 1.5 «Istisnoli holatlarni dasturlash (try/except). Fayllar bilan ishlash»: fayl nima, `open()`, `with open(...) as f`, 1.4-jadval (fayl rejimlari r, w, a, x, b, t, +), `write`, `writelines`, `read`, `readline`, `readlines`, fayl yo'q bo'lsa `try/except`. `splitlines()` va `encoding="utf-8"` standart Python hujjatiga ko'ra qo'shildi. Kod Python 3 da tekshirilgan.

---

## Darsning maqsadi

O'quvchilarga fayl tushunchasini, `open()` va `with open(...) as f` (fayl avtomatik yopiladi) konstruksiyasini, fayl rejimlarini (`r`, `w`, `a`, `x`), faylga yozishni (`write`, `writelines`), fayldan o'qishni (`read`, `readline`, `readlines`, sikl bilan), `encoding="utf-8"` ni va fayl topilmaganda `FileNotFoundError` ni `try/except` bilan boshqarishni o'rgatish.

## Kutiladigan natija

- `with open(...) as f` bilan faylni ochadi va nega `with` afzalligini tushuntiradi;
- `r`, `w`, `a`, `x` rejimlarining farqini aytadi (`w` eskisini o'chiradi!);
- Faylga `write` bilan yozadi va `a` bilan qo'shib yozadi;
- Faylni `read`, `readlines` yoki `for` sikli bilan o'qiydi;
- Fayl topilmaganda `FileNotFoundError` ni ushlaydi.

## Kerakli jihozlar

- Kompyuter, Python 3
- Kod muharriri (VS Code yoki PyCharm)
- Alohida ishchi papka (masalan, `hafta6`)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 17-dars: try/except |
| 08–22 | Yangi mavzu 1 | Fayl nima: open, with va rejimlar |
| 22–32 | Yangi mavzu 2 | Yozish: w va a; o'qish: read, readlines, for |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | FileNotFoundError va yozuvlar funksiyalari |
| 50–75 | Amaliyot | Amaliyot: «Kundalik» dasturi, xatolar, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Fayl, open, with va rejimlar

**Fayl** — kompyuter xotirasida saqlanadigan ma'lumot (matn, rasm, jadval). Dastur fayl orqali ma'lumotni **saqlaydi**, keyin qayta **o'qiydi**, hisobot va **log** yozadi. Ochish: `open(nom, rejim)`. Eng to'g'ri usul — **`with open(...) as f:`**: blok tugagach fayl **avtomatik yopiladi** (xato bo'lsa ham). Rejimlar: **`r`** — o'qish (fayl bo'lmasa xato, standart), **`w`** — yozish (**eski mazmunni o'chirib** qayta yozadi!), **`a`** — oxiriga qo'shib yozadi (o'chirmaydi), **`x`** — yangi yaratadi (bor bo'lsa xato). Matn fayllarda `encoding="utf-8"` yozing: o', g', sh kabi harflar buzilmaydi. Yo'l faqat nom bo'lsa, fayl **joriy papkada** qidiriladi/yaratiladi.

`w` rejimi mavjud faylni darhol **tozalaydi**. Eski ma'lumot kerak bo'lsa, `a` (qo'shib yozish) ishlating. `\n` — yangi qator belgisi.

### 2. Fayldan o'qish: read, readline, readlines

O'qish usullari: **`read()`** — butun faylni bitta matn qilib; **`readline()`** — bitta qatorni; **`readlines()`** — barcha qatorlarni ro'yxat qilib (har qator oxirida `\n` bor). Eng qulay va xotirani tejaydigan usul — faylni **`for`** sikli bilan qator-qator o'qish. Qator oxiridagi `\n` ni `strip()` olib tashlaydi, butun matnni qatorlarga bo'lish uchun esa `read().splitlines()`. Muhim: faylni o'qiyotganda `w` rejimida ochmang, aks holda mazmun o'chadi. Bitta ochilgan fayldan `read()` ikkinchi marta chaqirilsa, bo'sh matn qaytadi (kursor oxirda); kerak bo'lsa faylni qayta oching.

`for qator in f` katta fayllar uchun ham xavfsiz: butun fayl xotiraga birdaniga yuklanmaydi.

### 3. FileNotFoundError va yozuvlar funksiyalari

Fayl yo'q bo'lsa (`r` rejimi) Python `FileNotFoundError` chiqaradi. Uni 17-darsdagi `try/except` bilan ushlaymiz: foydalanuvchiga tushunarli xabar beramiz yoki bo'sh natija qaytaramiz. Real dasturda fayl bilan ishlash **funksiyalarga** (DRY!) ajratiladi: `yozuv_qosh(matn)` faylga qo'shadi, `yozuvlar()` hamma yozuvlarni ro'yxat qilib qaytaradi; fayl yo'q bo'lsa — bo'sh ro'yxat. Shunday qilib, fayl bilan ishlash tafsiloti bitta joyda, qolgan kod esa oddiy chaqiruvlardan iborat. Bu andoza Backend'da ma'lumotlarni saqlash va log yozishning asosi: keyinroq fayl o'rnini ma'lumotlar bazasi egallaydi.

Faylga yozishda ham xato bo'lishi mumkin (papka yo'q, ruxsat yo'q): `PermissionError`, `OSError`. Kerak bo'lsa ularni ham ushlang.

---

## Kod namunasi

«Kundalik» dasturi: yozuvlarni faylda saqlash:

```python
FAYL = "kundalik.txt"

def yozuv_qosh(matn):
    with open(FAYL, "a", encoding="utf-8") as f:
        f.write(matn + "\n")

def yozuvlar():
    try:
        with open(FAYL, encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def korsat():
    royxat = yozuvlar()
    if not royxat:
        print("Hozircha yozuv yo'q.")
    for i, matn in enumerate(royxat, 1):
        print(f"{i}. {matn}")

korsat()
yozuv_qosh("Funksiyalarni o'rgandim")
yozuv_qosh("Fayllar bilan ishladim")
korsat()
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Faylga yozing
`salom.txt` fayliga ikki qator yozing.

**Kutiladigan natija:** Fayl yaratildi.

**Yechim:** 
```python
with open("salom.txt", "w", encoding="utf-8") as f:
    f.write("Salom!\n")
    f.write("Python o'rganyapman\n")
```

### 2-topshiriq (oson). Hammasini o'qing
`salom.txt` ni o'qib, ekranga chiqaring.

**Kutiladigan natija:** Mazmun chiqdi.

**Yechim:** 
```python
with open("salom.txt", encoding="utf-8") as f:
    print(f.read())
```

### 3-topshiriq (o'rta). Qo'shib yozish
`salom.txt` oxiriga yangi qator qo'shing (eskisi o'chmasin).

**Kutiladigan natija:** Qator qo'shildi.

**Yechim:** 
```python
with open("salom.txt", "a", encoding="utf-8") as f:
    f.write("Uchinchi qator\n")
```

### 4-topshiriq (o'rta). Qatorlarni raqamlang
Fayl qatorlarini «1. ...», «2. ...» ko'rinishida chiqaring.

**Kutiladigan natija:** Raqamlangan chiqish.

**Yechim:** 
```python
with open("salom.txt", encoding="utf-8") as f:
    for i, qator in enumerate(f, 1):
        print(f"{i}. {qator.strip()}")
```

### 5-topshiriq (qiyin). Fayl yo'q bo'lsa
`yoq.txt` ni o'qing; fayl yo'q bo'lsa «Fayl topilmadi» chiqsin.

**Kutiladigan natija:** Xato ushlandi.

**Yechim:** 
```python
try:
    with open("yoq.txt", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi")
```

### 6-topshiriq (qo'shimcha). Qatorlar soni
Fayldagi bo'sh bo'lmagan qatorlar sonini hisoblang.

**Kutiladigan natija:** Soni topildi.

**Yechim:** 
```python
with open("salom.txt", encoding="utf-8") as f:
    soni = sum(1 for qator in f if qator.strip())
print(soni)
```

---

## Tezkor nazorat (dars oxirida)

1. Faylni xavfsiz ochish usuli? — `with open(...) as f`.
2. `w` rejimi nima qiladi? — Eskisini o'chirib, qayta yozadi.
3. Oxiriga qo'shish rejimi? — `a`.
4. Qator-qator o'qish usuli? — `for qator in f`.
5. Fayl yo'q bo'lsa qaysi istisno? — `FileNotFoundError`.

## Keng tarqalgan xatolar

- `w` bilan ochib, eski ma'lumotni yo'qotish.
- `with` o'rniga `open()` ochib, yopishni unutish.
- `encoding="utf-8"` yozmaslik: harflar buziladi.
- Fayl yo'lini noto'g'ri berish: dastur boshqa papkada ishga tushgan.
- `\n` ni unutib, qatorlarni birlashtirib yuborish.

## Bilasizmi? (qo'shimcha)

- `pathlib.Path` yordamida fayl yo'llari bilan qulay ishlash mumkin (keyingi bosqichlarda).
- `json` moduli lug'at va ro'yxatlarni faylga yozish uchun qulay.
- Backend'da yozuvlar fayl o'rniga ma'lumotlar bazasiga (PostgreSQL) yoziladi.
