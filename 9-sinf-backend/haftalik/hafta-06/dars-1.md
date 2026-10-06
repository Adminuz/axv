# 16-dars. DRY prinsipi va Pythonda funksiyalar (def)

**Fan:** Advanced Back-end va DevOps
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 1-dars (umumiy 16-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** `uslubiy-korsatma.txt`, I bob, 1.4 «DRY prinsipi. Pythonda funksiyalar» (chegirma hisoblash, `format_user`, til bo'yicha salomlashuv — `dict` bilan, `salom_ber`, `yigindi`). Standart qiymat, `None` va docstring Python hujjatiga ko'ra qo'shildi. Barcha kod namunalari Python 3 da ishga tushirib tekshirilgan.

---

## Darsning maqsadi

O'quvchilarga DRY (Don't Repeat Yourself) prinsipining mazmunini, takrorlangan kodning xavfini, `def` bilan funksiya e'lon qilishni (nom, parametrlar, `return`), standart qiymatli parametrlarni, `print` va `return` farqini hamda `dict` yordamida `if/elif` zanjirini soddalashtirishni o'rgatish.

## Kutiladigan natija

- DRY prinsipini va takrorlangan kodning 3 ta xavfini aytadi;
- `def` bilan parametrli funksiya yozadi va chaqiradi;
- `return` va `print` farqini tushuntiradi;
- Standart qiymatli parametrdan foydalanadi (`def f(a, b=10)`);
- Uzun `if/elif` zanjirini `dict` bilan almashtiradi.

## Kerakli jihozlar

- Kompyuter, Python 3
- Kod muharriri (VS Code yoki PyCharm)
- 15-darsdagi dict namunalari

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 13–15-dars: tuple, set, dict |
| 08–22 | Yangi mavzu 1 | DRY: takrorlangan kodning muammosi |
| 22–32 | Yangi mavzu 2 | def: parametr, return, standart qiymat |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | dict bilan DRY: if/elif o'rniga |
| 50–75 | Amaliyot | Amaliyot, xatolar, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. DRY: Don't Repeat Yourself

**DRY** (Don't Repeat Yourself — «o'zingni takrorlama») — bir xil mantiqni bir necha joyda yozma, uni bitta joyga (funksiya, klass, modul) jamla va hamma joyda shu «bitta manba»dan foydalan. Agar bir xil kod 5 joyda tursa: xato chiqsa — 5 joyni tuzatish kerak; bittasi unutilsa — **bug**; kod uzayadi va o'qish qiyinlashadi; testlash qimmatlashadi. DRY qilinsa: o'zgartirish bitta joyda, kod ixcham, qayta ishlatish oson. Misol: do'konda chegirma uch joyda hisoblanadi. Formula (masalan, foiz) o'zgarsa, uchala joyni topib o'zgartirish kerak. Funksiya bilan esa formula bir marta yoziladi.

Qoida: bir xil kodni ikkinchi marta yozayotgan bo'lsangiz — to'xtang va funksiya qiling. Uch marta takrorlangan kod — funksiya uchun qat'iy signal.

### 2. def: parametr, return va standart qiymat

**Funksiya** — ma'lum vazifani bajaradigan, qayta ishlatiladigan kod bloki. Tuzilishi: `def` kalit so'zi, **nom** (`snake_case`: kichik harf va pastki chiziq), qavs ichida **parametrlar**, ikki nuqta `:` va **tana** (4 bo'shliq surilgan). `return` natijani qaytaradi va funksiyani tugatadi; `return` bo'lmasa, funksiya `None` qaytaradi. **Parametr** — funksiya e'lonidagi nom, **argument** — chaqirishda berilgan qiymat. Parametrga **standart qiymat** berish mumkin: `def salom(ism="Mehmon")`. Muhim farq: `print()` qiymatni ekranga **chiqaradi**, `return` esa qiymatni dasturning o'ziga **qaytaradi** (uni boshqa hisobda ishlatish mumkin). Funksiya ichida e'lon qilingan o'zgaruvchi faqat shu funksiya ichida ishlaydi (lokal).

Funksiya ichida natijani faqat `print` qilsangiz, uni keyin hisobda ishlata olmaysiz: `yigindi(3, 4) * 2` ishlashi uchun `return` kerak.

### 3. dict bilan DRY: ko'p if/elif o'rniga

Takrorlanish faqat bir xil qatorlar emas, uzun `if/elif` zanjiri ham bo'lishi mumkin. Misol: til bo'yicha salomlashuv. Variant ko'paysa, kod chalkashadi. DRY yechimi — **lug'at**: kalit — til kodi, qiymat — matn. Yangi tilni qo'shish uchun faqat bitta juftlik yoziladi, funksiya o'zgarmaydi. Kalit bo'lmasa xato chiqmasligi uchun `get(kalit, standart)` ishlatiladi. Funksiya **bir nechta qiymat** qaytarishi ham mumkin (aslida `tuple`): `return min(s), max(s)` — chaqiruvda `kichik, katta = chegara(sonlar)`. Eslatma: funksiya bitta ish qilsin va nomi shu ishni aytsin (`narx_hisobla`, `salom_ber`).

Kalit bo'lmasa `texts["de"]` `KeyError` beradi, `texts.get("de", ...)` esa standart qiymat qaytaradi.

---

## Kod namunasi

Do'kon: chegirma, soliq va jami (DRY):

```python
def foiz_qosh(narx, foiz):
    return narx + narx * foiz / 100

def chegirma(narx, foiz):
    return narx - narx * foiz / 100

def jami(narxlar, chegirma_foizi=0, soliq_foizi=12):
    summa = sum(narxlar)
    summa = chegirma(summa, chegirma_foizi)
    return round(foiz_qosh(summa, soliq_foizi), 2)

savat = [120, 80, 50]
print(jami(savat))                       # 280.0
print(jami(savat, chegirma_foizi=10))    # 252.0
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Funksiya yozing
Ikki sonni qo'shib qaytaradigan `yigindi(a, b)` yozing.

**Kutiladigan natija:** Yig'indi funksiyasi.

**Yechim:** 
```python
def yigindi(a, b):
    return a + b

print(yigindi(3, 4))   # 7
```

### 2-topshiriq (oson). Salom funksiyasi
Standart ismi «Mehmon» bo'lgan `salom(ism)` yozing.

**Kutiladigan natija:** Standart qiymat.

**Yechim:** 
```python
def salom(ism="Mehmon"):
    return f"Salom, {ism}!"

print(salom())
print(salom("Ali"))
```

### 3-topshiriq (o'rta). Chegirma
`chegirma(narx, foiz)` funksiyasini yozing va 3 marta chaqiring.

**Kutiladigan natija:** Chegirma funksiyasi.

**Yechim:** 
```python
def chegirma(narx, foiz):
    return narx - narx * foiz / 100

print(chegirma(200, 10))   # 180.0
print(chegirma(500, 20))   # 400.0
print(chegirma(90, 5))     # 85.5
```

### 4-topshiriq (o'rta). format_user
Ism va yoshni «Ali — 20 yosh» ko'rinishida qaytaradigan funksiya yozing.

**Kutiladigan natija:** Formatlovchi funksiya.

**Yechim:** 
```python
def format_user(ism, yosh):
    return f"{ism} — {yosh} yosh"

for ism, yosh in [("Ali", 20), ("Vali", 22)]:
    print(format_user(ism, yosh))
```

### 5-topshiriq (qiyin). dict bilan salom
Til bo'yicha salom beradigan funksiya yozing (uz, ru, en); noma'lum til — inglizcha.

**Kutiladigan natija:** dict bilan DRY.

**Yechim:** 
```python
texts = {"uz": "Assalomu alaykum!", "ru": "Zdravstvuyte!", "en": "Hello!"}

def salomlash(til):
    return texts.get(til, texts["en"])

print(salomlash("uz"))
print(salomlash("de"))
```

### 6-topshiriq (qo'shimcha). Eng kichik va eng katta
Sonlar ro'yxatidan eng kichik va eng katta sonni qaytaring.

**Kutiladigan natija:** Ikki qiymat qaytdi.

**Yechim:** 
```python
def chegara(sonlar):
    return min(sonlar), max(sonlar)

kichik, katta = chegara([4, 9, 1, 7])
print(kichik, katta)   # 1 9
```

---

## Tezkor nazorat (dars oxirida)

1. DRY nima? — Kodni takrorlamaslik prinsipi.
2. Funksiya qaysi so'z bilan e'lon qilinadi? — `def`.
3. Parametr va argument farqi? — Parametr — e'londa, argument — chaqirishda.
4. `return` bo'lmasa funksiya nima qaytaradi? — `None`.
5. if/elif o'rniga nima ishlatamiz? — `dict`.

## Keng tarqalgan xatolar

- `return` o'rniga `print` yozib, natijani ishlata olmaslik.
- Tanani surmaslik: `IndentationError`.
- Ikki nuqtani (`:`) unutish.
- Funksiyani e'lon qilib, chaqirmaslik.
- Funksiyaga juda ko'p vazifa yuklash.

## Bilasizmi? (qo'shimcha)

- Python'da funksiya ham qiymat: uni o'zgaruvchiga yoki boshqa funksiyaga berish mumkin.
- Funksiya birinchi qatoridagi uch qo'shtirnoqli matn — docstring: funksiyani tushuntiradi (`help(f)`).
- `*args` va `**kwargs` funksiyaga ixtiyoriy sondagi argument berishga imkon beradi.
