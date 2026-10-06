# 15-dars. ORALIQ NAZORAT

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 15-dars (umumiy 1–51)

**Manba:** O'quv dasturi, 8-bo'lim (baholash mezonlari, 100 ballik shkala, oraliq nazorat shakli); I bob 1–14-darslar materiallari. Topshiriq mazmuni va ball taqsimoti mentor tomonidan dastur talablari asosida tuzildi.

## 1. Dars rejasi

**Maqsad:** Oraliq nazoratda o'quvchi I bobning (1–14-darslar) bilim va ko'nikmalarini amalda qo'llaydi: Git va PR, Clean Code va SOLID, Observer, REST/JSON kontrakt, muloqot va vaqtni boshqarish. Mentor dastur mezonlari (tasavvur, mohiyatni tushunish, amalda qo'llash, ijodiy fikrlash, mustaqil ish) bo'yicha baholaydi.

**Kutiladigan natija:**
- Nazorat tuzilishi, qoidalari va baholash mezonlarini biladi.
- Kutubxona boshqaruvi topshirig'ini 80 daqiqada mustaqil bajaradi.
- Kod, PR tavsifi va soft skills yozuvini topshiradi.
- O'z xatolarini tahlil qilib, kuchsiz mavzularni belgilaydi.

**Kerakli jihozlar:**
- Kompyuter, Python 3 va kod muharriri
- Git va GitHub hisobi
- Taymer; mentor uchun baholash varaqasi (`baholash.md`)
- Internet faqat rasmiy hujjatlar (Python docs) uchun; tayyor yechimni nusxalash mumkin emas

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | Qoidalar, tuzilma, baholash mezonlari tushuntiriladi |
| 10–35 daq | Yangi mavzu | A va B qismlar: Clean Code, SOLID, Observer; C qism: REST/JSON kontrakt va testlar; D va E qismlar: PR va soft skills |
| 35–40 daq | Tanaffus | Harakatli tanaffus + mini-quiz |
| 40–65 daq | Amaliyot | Topshirish, qisqa og'zaki tahlil va xatolar ustida ishlash |
| 65–75 daq | Tezkor nazorat | 5 ta savol |
| 75–80 daq | Xulosa va uyga vazifa | Xatolar ustida ishlash |

---

## 2. Dars konspekti

### 2.1. Nazorat shakli va qoidalari

Oraliq nazorat — bobning mavzulari tugagach o'tkaziladigan nazorat. Bugun u **amaliy topshiriq** shaklida: bitta «Kutubxona boshqaruvi» vazifasi, beshta qism, 80 daqiqa. Dastur talabiga ko'ra nazoratda topshiriq turlaridan faqat bittasi ishlatiladi. Siz o'z kompyuteringizda ishlaysiz va to'rt fayl topshirasiz: `nazorat.py`, `test_nazorat.py`, `PR.md`, `reflection.md`. Rasmiy hujjatlarga qarash mumkin, tayyor yechimni nusxalash mumkin emas. Baholash 100 ballik shkala bo'yicha.

Vaqtni boshidan taqsimlang (timeboxing): A 15, B 20, C 20, D 10, E 10 daqiqa, 5 daqiqa tekshirishga.

### 2.2. Nazoratda tekshiriladigan mavzular

Nazorat I bobning barcha texnik va soft skills mavzularini qamraydi. **Git va GitHub**: semantik commit, tarmoq, Pull Request, code review (1–6-dars). **Clean Code va SOLID**: ma'noli nomlar, bitta vazifa, ochiq-yopiq tamoyili (7–8-dars). **Loyihalash andozalari**: Factory, Singleton, Observer va EventBus (9–10-dars). **REST va JSON**: URI, status kodlari, error envelope, paginatsiya, xavfsizlik (11–12-dars). **Soft skills**: muloqot, PR tavsifi, Eisenhower, SMART (13–14-dars). Har qismda kod yoki yozma javob bo'ladi.

Kuchsiz mavzuni oldindan aniqlang: 14-dars uyga vazifasida 3 ta kuchsiz mavzuni belgilagan edingiz.

### 2.3. Baholash mezonlari va shkala

Baholash 100 ballik shkalada: **90–100 — 5 (a'lo)**, **71–89 — 4 (yaxshi)**, **60–70 — 3 (qoniqarli)**, **0–59 — 2 (qoniqarsiz)**. Dastur mezonlari: mavzu bo'yicha tasavvur, mohiyatni tushunish va aytib bera olish, bilimni amalda qo'llash, ijodiy fikrlash va xulosa chiqarish, mustaqil ish. Kod toza va o'qilishi oson bo'lishi, funksiyalar to'liq ishlashi, testlar yashil o'tishi alohida baholanadi. Topshirgach, mentor bilan 5 daqiqalik og'zaki tahlil: nimani qanday qildingiz va nimani yaxshilar edingiz.

Topshirishdan oldin testlarni oxirgi marta ishga tushiring: yashil bo'lmagan test baho olib tashlaydi.

### 2.4. Namunalar

Nazorat boshlanishi uchun tavsiya etilgan tartib:

```text
1) Starter kodni o'qing, A qismni boshlang
2) Kichik qadam: yozing -> testlang -> commit
3) B va C qismlar ketma-ket
4) D va E ni oxirgi 20 daqiqada
5) Oxirgi 5 daqiqa: testlar va fayl nomlarini tekshirish
```

## 3. Amaliy mashg'ulot

### 1-mashq (oson). Git tayyorgarligi
**Vazifa:** Yangi tarmoq ochish va semantik commit yozish buyruqlarini yozing.

**Kutiladigan natija:** `git switch -c` va `git commit -m "feat: ..."`.

**Yechim:** `git switch -c feature/nazorat`, `git commit -m "feat: add borrow_book"`.

### 2-mashq (o'rta). Observer tayyorgarligi
**Vazifa:** `EventBus` ning 2 ta metodini yozing va bitta kuzatuvchi ulang.

**Kutiladigan natija:** `subscribe` va `publish` ishlaydi.

**Yechim:** Namunaviy yechimdagi `EventBus` ga qarang.

### 3-mashq (qiyin). Kontrakt tayyorgarligi
**Vazifa:** `paginate` va `make_error` yozing va 2 ta test bilan tekshiring.

**Kutiladigan natija:** Testlar yashil.

**Yechim:** `paginate(list(range(10)),3,6)` natijasi: data [6,7,8], total 10.

### 4-mashq (bonus). O'z-o'zini baholash
**Vazifa:** I bobdagi 3 ta kuchsiz mavzuni yozing va har biriga 1 ta takrorlash qadamini belgilang.

**Kutiladigan natija:** 3 mavzu va 3 qadam.

**Yechim:** Individual.

## 4. Nazorat topshirig'i (faqat mentor uchun)

**Shakl:** amaliy topshiriq (dasturga ko'ra oraliq nazoratda topshiriq turlaridan faqat bittasi ishlatiladi). **Vaqt:** 80 daqiqa. **Mavzu:** «Kutubxona boshqaruvi», I bob bo'yicha. O'quvchi `nazorat.py`, `test_nazorat.py`, `PR.md`, `reflection.md` fayllarini topshiradi.

**Boshlang'ich kod (`starter.py`):**

```python
def process(b, u, t):
    if t == "borrow":
        if b["available"] == True:
            b["available"] = False
            print("EMAIL: " + u["email"] + " kitob oldi: " + b["title"])
            return {"ok": True}
        else:
            return {"ok": False}
    elif t == "return":
        b["available"] = True
        print("EMAIL: " + u["email"] + " kitob qaytardi: " + b["title"])
        return {"ok": True}
```

### A qism. Clean Code va SOLID (20 ball, ~15 daqiqa)
`process` funksiyasini qayta yozing: ma'noli nomlar (`borrow_book`, `return_book`), `== True` yo'q, sehrli satrlar (`"borrow"`) yo'q, bitta funksiya bitta ish (SRP): email chiqarish alohida bo'lsin.

### B qism. Observer (25 ball, ~20 daqiqa)
`EventBus` sinfini yozing (`subscribe`, `publish`). `borrow_book` va `return_book` `book:borrowed` va `book:returned` hodisalarini e'lon qilsin. Bitta kuzatuvchi xato bersa, boshqalar ishlashda davom etsin.

### C qism. REST va JSON kontrakt (25 ball, ~20 daqiqa)
Uchta funksiya: `make_error(code, message, details=None)` — `{"error": {"code", "message", "details"}}`; `paginate(items, limit, offset)` — `{"data": [...], "meta": {"limit", "offset", "total"}}`; `sanitize_user(user)` — `password_hash`, `token`, `secret_key` ni olib tashlaydi (asl obyektni o'zgartirmaydi). `test_nazorat.py` da kamida 4 ta test.

### D qism. Git va PR (20 ball, ~10 daqiqa)
`PR.md`: tarmoq nomi (`feature/...`), 3 ta semantik commit xabari (`feat:`, `refactor:`, `test:`), PR tavsifi (What, Why, How, keyingi qadam).

### E qism. Soft skills (10 ball, ~10 daqiqa)
`reflection.md`: (1) shu nazoratning A–E qismlarini Eisenhower matritsasiga joylang va bajarish tartibini asoslang; (2) hamkasbga PR bo'yicha 3 jumlali «I-xabar» (yoki SBI) fikr yozing.

### Namunaviy yechim (`nazorat.py`)

```python
class EventBus:
    def __init__(self):
        self._handlers = {}

    def subscribe(self, event, handler):
        self._handlers.setdefault(event, []).append(handler)

    def publish(self, event, payload):
        for handler in self._handlers.get(event, []):
            try:
                handler(payload)
            except Exception as exc:  # bitta kuzatuvchi boshqalarni to'xtatmasin
                print(f"handler xatosi: {exc}")


bus = EventBus()


def borrow_book(book, user):
    if not book["available"]:
        return False
    book["available"] = False
    bus.publish("book:borrowed", {"book": book["title"], "email": user["email"]})
    return True


def return_book(book, user):
    book["available"] = True
    bus.publish("book:returned", {"book": book["title"], "email": user["email"]})
    return True


def make_error(code, message, details=None):
    return {"error": {"code": code, "message": message, "details": details or []}}


def paginate(items, limit, offset):
    return {
        "data": items[offset:offset + limit],
        "meta": {"limit": limit, "offset": offset, "total": len(items)},
    }


def sanitize_user(user):
    secret = {"password_hash", "token", "secret_key"}
    return {k: v for k, v in user.items() if k not in secret}
```

### Namunaviy testlar (`test_nazorat.py`)

```python
from nazorat import *

def test_borrow_and_event():
    log = []
    bus.subscribe("book:borrowed", log.append)
    book = {"title": "Sarob", "available": True}
    user = {"email": "ali@mail.uz"}
    assert borrow_book(book, user) is True
    assert book["available"] is False
    assert log == [{"book": "Sarob", "email": "ali@mail.uz"}]
    assert borrow_book(book, user) is False
    assert len(log) == 1

def test_broken_handler():
    bus2 = EventBus()
    seen = []
    bus2.subscribe("x", lambda p: 1 / 0)
    bus2.subscribe("x", seen.append)
    bus2.publish("x", 5)
    assert seen == [5]

def test_error_and_page():
    assert make_error("not_found", "Kitob yo'q")["error"]["details"] == []
    p = paginate(list(range(10)), 3, 6)
    assert p["data"] == [6, 7, 8] and p["meta"] == {"limit": 3, "offset": 6, "total": 10}

def test_sanitize():
    u = {"id": 1, "name": "Ali", "password_hash": "x", "token": "t"}
    assert sanitize_user(u) == {"id": 1, "name": "Ali"}
    assert "password_hash" in u
```

Tekshirilgan: namunaviy yechim va testlar Python 3 da xatosiz o'tadi.

### Baholash (100 ball)

| Qism | Ball | Nimaga qaraladi |
|---|---|---|
| A. Clean Code, SOLID | 20 | Nomlar, SRP, sehrli satrlar yo'q, `== True` yo'q |
| B. Observer | 25 | `EventBus`, ikki hodisa, xato izolyatsiyasi |
| C. REST/JSON | 25 | `make_error`, `paginate`, `sanitize_user`, testlar |
| D. Git/PR | 20 | Tarmoq nomi, semantik commitlar, What/Why/How |
| E. Soft skills | 10 | Matritsa asoslangan, «I-xabar» to'g'ri |
| **Jami** | **100** | 90–100 — 5; 71–89 — 4; 60–70 — 3; 0–59 — 2 |

## 5. Tezkor savollar

1. Nazorat shakli?
   - **Javob:** Amaliy topshiriq, 80 daqiqa.
2. Nechta qism bor?
   - **Javob:** 5 ta: A–E.
3. 100 ball nechta baho?
   - **Javob:** 90–100 — 5; 71–89 — 4; 60–70 — 3; 0–59 — 2.
4. Qaysi fayllar topshiriladi?
   - **Javob:** `nazorat.py`, `test_nazorat.py`, `PR.md`, `reflection.md`.
5. Nazoratdan keyin nima qilinadi?
   - **Javob:** Og'zaki tahlil va xatolar ustida ishlash.

## 6. Mentor uchun eslatmalar

- Nazorat topshirig'i va namunaviy yechim ushbu faylning 4-bo'limida; o'quvchiga nazorat boshlanguncha ko'rsatmang.
- O'quvchi bitta bo'lgani uchun baholash individual; natijani `baholash.md` ga yozing va 5 daqiqa og'zaki tahlil o'tkazing.
- Dastur: oraliq nazoratda topshiriq turlaridan faqat bittasi ishlatiladi; shuning uchun yozma test bu yerda qo'shilmadi (slayd-testlar faqat takrorlash uchun).
- Namunaviy yechim va testlar Python 3 da ishga tushirilib tekshirilgan; pytest o'rnatilmagan bo'lsa, `assert` li funksiyalarni qo'lda chaqiring.
- Nazoratdan keyin xatolar ustida ishlash uyga vazifasi 6-haftadan oldin topshirilsin.
- Keng tarqalgan xatolar: Bitta qismga ko'p vaqt sarflab, boshqasiga ulgurmaslik; Testlarni yozmasdan topshirish; `password_hash` ni javobda qoldirish; Commit xabarini «fix» yoki «update» deb yozish.
