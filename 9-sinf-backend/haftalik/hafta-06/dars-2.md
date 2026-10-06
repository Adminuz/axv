# 17-dars. Istisnoli holatlar: try, except, else, finally

**Fan:** Advanced Back-end va DevOps
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 2-dars (umumiy 17-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `uslubiy-korsatma.txt`, I bob, 1.5 «Istisnoli holatlarni dasturlash (try/except). Fayllar bilan ishlash» (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`, `IndexError`, `KeyError`; aniq exception ushlash; bir nechta `except`, tuple bilan, `else`, `finally`). `raise` va `while True` bilan kiritishni tekshirish standart Python hujjatiga ko'ra qo'shildi. Barcha kod Python 3 da tekshirilgan.

---

## Darsning maqsadi

O'quvchilarga istisno (exception) tushunchasini, eng ko'p uchraydigan istisnolarni (`ValueError`, `ZeroDivisionError`, `IndexError`, `KeyError`, `FileNotFoundError`), `try/except` tuzilishini, aniq istisnoni ushlashning afzalligini, `else` va `finally` bloklarini va `raise` bilan o'zi istisno chiqarishni o'rgatish.

## Kutiladigan natija

- Traceback xabarini o'qib, xato turi va qatorini topadi;
- `try/except` bilan dastur to'xtamasligini ta'minlaydi;
- Aniq istisnoni (`ValueError`, `ZeroDivisionError`) ushlaydi, «yalang» `except:` dan qochadi;
- `else` va `finally` bloklarining vazifasini tushuntiradi;
- To'g'ri kiritilguncha so'raydigan funksiya yozadi.

## Kerakli jihozlar

- Kompyuter, Python 3
- Kod muharriri (VS Code yoki PyCharm)
- 16-darsdagi funksiyalar

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 16-dars: DRY va funksiyalar |
| 08–22 | Yangi mavzu 1 | Istisno nima va Traceback |
| 22–32 | Yangi mavzu 2 | try/except: aniq istisno, else, finally |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Kiritishni tekshirish: while True va raise |
| 50–75 | Amaliyot | Amaliyot, xatolar, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Istisno va Traceback

**Istisno** (exception) — dastur ishlayotganda yuz beradigan kutilmagan holat, odatdagi oqimni buzadi. Ushlanmasa, dastur **to'xtaydi** va **Traceback** chiqadi: pastdan yuqoriga o'qing, oxirgi qatorda xato **turi** va sababi, undan yuqorida **fayl va qator raqami** bo'ladi. Eng ko'p uchraydiganlari: `ValueError` — qiymat noto'g'ri (`int("abc")`); `ZeroDivisionError` — 0 ga bo'lish; `IndexError` — ro'yxatda yo'q indeks; `KeyError` — lug'atda yo'q kalit; `FileNotFoundError` — fayl topilmadi; `TypeError` — tur mos emas (`"5" + 3`). Istisno — xato emas, signal: biz uni **ushlab**, foydalanuvchiga tushunarli xabar berishimiz mumkin.

Traceback ni o'qishdan qo'rqmang: oxirgi qator — nima bo'ldi, yuqoridagi qatorlar — qayerda bo'ldi. Xato xabarini Google'ga yozish — dasturchining kundalik odati.

### 2. try/except, else va finally

Tuzilishi: `try:` blokida xavfli kod, `except Xato:` blokida xato bo'lsa nima qilish. **Aniq istisnoni** ushlang: `except ValueError:`. «Yalang» `except:` hamma narsani, jumladan, o'zingiz bilmagan xatolarni ham yashiradi. Bir nechta xato uchun bir nechta `except` yoki tuple: `except (ValueError, TypeError):`. **`else`** — xato **bo'lmasa** ishlaydi (muvaffaqiyat natijasini shu yerda yozing). **`finally`** — **doim** ishlaydi (xato bo'lsa ham, bo'lmasa ham): fayl yoki ulanishni yopish kabi tozalash ishlari uchun. Tartib: `try` → `except` → `else` → `finally`. Eslatma: `try/except` xatoni **oldini olmaydi**, uni boshqaradi.

Hamma narsani bitta `except:` bilan ushlamang: dasturdagi haqiqiy xato yashirinib qoladi va uni topish qiyinlashadi.

### 3. Kiritishni tekshirish: while True va raise

Foydalanuvchi har doim ham to'g'ri qiymat kiritmaydi: harf, bo'sh joy, manfiy son. Amaliy andoza: **`while True`** sikli ichida `try` — to'g'ri kiritilguncha so'raydi, to'g'ri bo'lsa `return` bilan chiqadi. Qo'shimcha qoidani (masalan, yosh manfiy bo'lmasin) `int()` o'zi tekshirmaydi: uni `raise ValueError("sabab")` bilan istisnoga aylantirib, bitta `except ValueError` da ushlaymiz. `raise` — o'zimiz istisno chiqarish. Funksiya ichida xato bo'lsa, uni chaqirgan joyga `raise` bilan uzatish yoki o'sha yerda ushlash mumkin; foydalanuvchi bilan muloqot qiladigan joyda xabar beriladi. Backend dasturlashda bu har kuni kerak: tashqi ma'lumotga hech qachon ishonmang, doim tekshiring.

`raise ValueError(...)` va `int("abc")` ikkalasi ham `ValueError`: shuning uchun bitta `except` ikkala holatni ushlaydi.

---

## Kod namunasi

Xavfsiz kalkulyator (xatolarga chidamli):

```python
def hisobla(a, b, amal):
    try:
        a, b = float(a), float(b)
        if amal == "+":
            return a + b
        if amal == "-":
            return a - b
        if amal == "*":
            return a * b
        if amal == "/":
            return a / b
        raise ValueError("noma'lum amal")
    except ZeroDivisionError:
        return "Xato: 0 ga bo'lib bo'lmaydi!"
    except ValueError:
        return "Xato: son yoki amal noto'g'ri."

print(hisobla("10", "2", "/"))     # 5.0
print(hisobla("10", "0", "/"))     # Xato: 0 ga bo'lib bo'lmaydi!
print(hisobla("abc", "2", "+"))    # Xato: son yoki amal noto'g'ri.
print(hisobla("3", "4", "^"))      # Xato: son yoki amal noto'g'ri.
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Xato turini toping
`int("12a")` qaysi istisnoni chiqaradi?

**Kutiladigan natija:** `ValueError`.

**Yechim:** ValueError: matnni butun songa aylantirib bo'lmaydi.

### 2-topshiriq (oson). ValueError ni ushlang
Foydalanuvchi qiymatini songa aylantiring; xato bo'lsa «Butun son kiriting» chiqsin.

**Kutiladigan natija:** ValueError ushlandi.

**Yechim:** 
```python
matn = "abc"
try:
    son = int(matn)
    print("Siz kiritdingiz:", son)
except ValueError:
    print("Xato: Siz butun son emas, boshqa narsa kiritdingiz.")
```

### 3-topshiriq (o'rta). 0 ga bo'lish
Ikki sonni bo'ling; 0 ga bo'lishda «0 ga bo'lib bo'lmaydi!» chiqsin.

**Kutiladigan natija:** ZeroDivisionError ushlandi.

**Yechim:** 
```python
def bol(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Xato: 0 ga bo'lib bo'lmaydi!"

print(bol(10, 2))
print(bol(5, 0))
```

### 4-topshiriq (o'rta). else va finally
Oldingi funksiyaga `else` va `finally` qo'shing («hisob tugadi» doim chiqsin).

**Kutiladigan natija:** else va finally.

**Yechim:** 
```python
def bol(a, b):
    try:
        natija = a / b
    except ZeroDivisionError:
        print("Xato: 0 ga bo'lib bo'lmaydi!")
    else:
        print("Natija:", natija)
    finally:
        print("hisob tugadi")

bol(10, 2)
bol(5, 0)
```

### 5-topshiriq (qiyin). Yosh so'rash
To'g'ri yosh (0 dan katta yoki teng butun son) kiritilguncha so'rang.

**Kutiladigan natija:** Qayta so'rovchi funksiya.

**Yechim:** 
```python
def yosh_ol():
    while True:
        matn = input("Yoshingiz: ")
        try:
            yosh = int(matn)
            if yosh < 0:
                raise ValueError("manfiy")
            return yosh
        except ValueError:
            print("Xato: 0 yoki undan katta butun son kiriting.")
```

### 6-topshiriq (qo'shimcha). Lug'at kaliti
`d["x"]` KeyError bermasligi uchun ikki usulni yozing.

**Kutiladigan natija:** Ikki usul.

**Yechim:** 
```python
d = {"a": 1}
print(d.get("x", 0))
try:
    print(d["x"])
except KeyError:
    print("Kalit yo'q")
```

---

## Tezkor nazorat (dars oxirida)

1. Istisno nima? — Dastur ishlashdagi kutilmagan holat.
2. `int("abc")` qaysi istisnoni beradi? — `ValueError`.
3. `finally` qachon ishlaydi? — Doim.
4. Nega `except:` yalang yozilmaydi? — Haqiqiy xatolarni yashiradi.
5. `raise` nima qiladi? — O'zimiz istisno chiqaradi.

## Keng tarqalgan xatolar

- Yalang `except:` yozib, hamma xatoni yashirish.
- `except` ichiga `pass` yozib, xatoni e'tiborsiz qoldirish.
- `try` ichiga juda ko'p kod yozish.
- `try/except` ni «xatosiz kod» o'rniga ishlatish.
- Traceback ni o'qimasdan «ishlamayapti» deyish.

## Bilasizmi? (qo'shimcha)

- `except Exception as e:` bilan xato obyektini olib, `print(e)` bilan xabarni ko'rsatish mumkin.
- Python'da `try/except` mantiqiy «oldin sinab ko'r» (EAFP) uslubiga mos.
- Backend'da xatolar fayl yoki log tizimiga yoziladi: bu keyingi bosqichlarda.
