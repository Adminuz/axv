# 10-dars. Loyihalash andozalari: Observer va hodisalar arxitekturasi

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + kod amaliyoti · **I-bob**, 10-dars (umumiy 1–51)

**Manba:** o'quv qo'llanma, «Loyihalash andozalari: Factory, Singleton, Observer» ma'ruzasi, «Observer va hodisa-yo'naltirilgan dizayn» bo'limi; o'quv dasturi, shu mavzu bayoni va natijalari.

## 1. Dars rejasi

**Maqsad:** o'quvchi Observer (publish/subscribe) andozasini, Subject va Observer rollarini, bo'sh bog'liqlik (loose coupling) g'oyasini tushunadi; hodisa-yo'naltirilgan dizayn (event-driven) ga o'tishni, hodisa tarqatishdagi xavflarni (xotira oqimi, tartib, idempotentlik, xatoni yutmaslik) biladi; Python'da Observer va oddiy `EventBus` yozadi hamda uni soxta kuzatuvchi (mock) bilan testlaydi.

**Kutiladigan natija:**
- «Buyurtma yakunlandi» kabi bitta hodisaga bir nechta mustaqil kuzatuvchi ulay oladi.
- Subject kuzatuvchilar kimligini bilmasligining foydasini tushuntiradi.
- `subscribe` / `unsubscribe` to'g'ri ishlatilmasa nima bo'lishini (xotira oqimi) biladi.
- Bitta kuzatuvchi yiqilsa, qolganlariga xalaqit bermaslikni (try/except) qo'llaydi.
- Observer'ni birlik (unit) darajasida soxta kuzatuvchi bilan sinaydi.
- Mini-loyiha («Kutubxona boshqaruvi» REST API) uchun `book:borrowed` hodisasini loyihalaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | Factory, Singleton va Singleton xatarlari. Muammoli vaziyat: «Buyurtma yakunlanganda email, analitika, ball hisoblash kerak. Hammasini `OrderService` ichiga yozsak nima bo'ladi?» |
| 10–35 daq | Yangi mavzu | Observer: Subject/Observer, subscribe, notify; loose coupling; event-driven arxitektura (queue, event bus); xavflar |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliyot | `OrderService` + 2 ta kuzatuvchi; `unsubscribe`; `EventBus`; mock bilan test; `book:borrowed` |
| 65–75 daq | Tezkor nazorat | 5 ta savol |
| 75–80 daq | Xulosa va uyga vazifa | Observer va 11-darsga ko'prik (REST) |

---

## 2. Dars konspekti

### 2.1. Muammo: qattiq bog'liqlik

Bitta voqea («buyurtma yakunlandi») yuz berganda bir nechta mustaqil ish bajariladi: mijozga email, analitika jurnaliga yozish, sodiqlik (loyalty) ballarini hisoblash. Hammasini `OrderService` ichiga yozsak (qattiq bog'liqlik), kod murakkablashadi va sinovlar qimmatlashadi: har yangi ish uchun `OrderService` ni o'zgartirish kerak (OCP buziladi).

```python
class OrderService:
    def complete_order(self, order_id):
        # ... asosiy mantiq ...
        send_email(order_id)        # qattiq bog'langan
        track_analytics(order_id)   # qattiq bog'langan
        add_loyalty_points(order_id)  # yangi talab: yana shu yerga tegamiz
```

### 2.2. Observer andozasi

**Observer** — «publish/subscribe» modelida hodisalarni kuzatuvchilarga tarqatuvchi xulq-atvor (Behavioral) andozasi. Bitta «manba» (**Subject / Publisher**) voqea yuz berganini e'lon qiladi; **Observer / Subscriber** lar bu e'londan mustaqil xabardor bo'lib o'z ishini bajaradi.

Asosiy g'oya: **Subject kuzatuvchilar kimligini bilmaydi**, u faqat «hodisa sodir bo'ldi» deydi. Shuning uchun yangi kuzatuvchi qo'shish yoki eskisini olib tashlash Subject kodini o'zgartirmaydi: **bo'sh bog'liqlik (loose coupling)**.

Hayotiy o'xshatish: Telegram kanali. Kanal egasi postni bir marta yuboradi, obunachilarni tanimaydi; kim xohlasa obuna bo'ladi, kim xohlasa chiqib ketadi.

Rollar:
- **Subject (Publisher)** — kuzatuvchilar ro'yxatini saqlaydi, `subscribe`/`unsubscribe` beradi, hodisani e'lon qiladi (notify).
- **Observer (Subscriber)** — bir xil imzoli (kontrakt) metodni amalga oshiradi (masalan, `on_order_completed(order_id)`).

### 2.3. Python'da minimal Observer (o'quv qo'llanma namunasi asosida)

```python
from typing import Protocol, List


class OrderEventListener(Protocol):
    def on_order_completed(self, order_id: str) -> None: ...


class OrderService:
    def __init__(self) -> None:
        self._listeners: List[OrderEventListener] = []

    def subscribe(self, listener: OrderEventListener) -> None:
        self._listeners.append(listener)

    def unsubscribe(self, listener: OrderEventListener) -> None:
        if listener in self._listeners:
            self._listeners.remove(listener)

    def complete_order(self, order_id: str) -> None:
        # ... asosiy biznes mantiq, validatsiya ...
        for listener in list(self._listeners):
            try:
                listener.on_order_completed(order_id)
            except Exception as e:
                print(f"[WARN] listener failed: {e}")


class EmailNotifier:
    def on_order_completed(self, order_id: str) -> None:
        print(f"Email -> {order_id}")


class AnalyticsTracker:
    def on_order_completed(self, order_id: str) -> None:
        print(f"Analytics -> {order_id}")


svc = OrderService()
email = EmailNotifier()
svc.subscribe(email)
svc.subscribe(AnalyticsTracker())
svc.complete_order("ORD-001")
svc.unsubscribe(email)
svc.complete_order("ORD-002")
```

Natija (tekshirilgan):

```text
Email -> ORD-001
Analytics -> ORD-001
Analytics -> ORD-002
```

Izohlar:
- `list(self._listeners)` — ro'yxat nusxasi: aylanish paytida kuzatuvchi o'zini o'chirsa ham xatoga tushmaymiz.
- `try/except` — bitta kuzatuvchi yiqilsa, boshqalarga xalaqit bermaslik uchun (qo'llanmadagi «Muhim» izohi). Xatoni **yutib yubormaymiz**: kamida logga yozamiz.
- Testlash oson: soxta kuzatuvchi ulab, metod chaqirilganini tekshiramiz.

### 2.4. EventBus: hodisa nomi bilan (Python varianti)

O'quv qo'llanmada JavaScript `EventBus` (`on`, `off`, `emit`) berilgan; shu g'oyaning Python varianti:

```python
from collections import defaultdict


class EventBus:
    def __init__(self):
        self._handlers = defaultdict(list)

    def on(self, event, handler):
        self._handlers[event].append(handler)

    def off(self, event, handler):
        if handler in self._handlers[event]:
            self._handlers[event].remove(handler)

    def emit(self, event, payload):
        for handler in list(self._handlers[event]):
            try:
                handler(payload)
            except Exception as e:
                print(f"[WARN] {event}: {e}")


bus = EventBus()
bus.on("book:borrowed", lambda p: print("SMS ->", p["reader"]))
bus.emit("book:borrowed", {"book_id": 7, "reader": "Ali"})
```

JavaScript variantini (qo'llanmadan) ham ko'rsating: `bus.on('order:completed', fn)`, `bus.emit('order:completed', 'ORD-002')`. UI komponentlarida manba faqat `emit` qiladi, kim tinglayotganini bilmaydi.

### 2.5. Hodisa-yo'naltirilgan dizayn (Event-driven)

G'oya yirik tizim darajasiga ko'tarilganda xizmatlar o'rtasida **publish/subscribe**, **navbatlar (message queue: RabbitMQ, Kafka, SQS)** va **voqealar shinasi (event bus)** orqali asinxron hamkorlik quriladi. Foydasi: xizmatlararo bog'liqlik yanada bo'shaydi, cho'qqi yuk (burst) paytida navbat buferi yordam beradi, kechikishni (latency) boshqarish va mustaqil masshtablash osonlashadi.

| | Sinxron Observer (sinf ichida) | Asinxron pub/sub (navbat / event bus) |
|---|---|---|
| Qayerda | bitta jarayon ichida | xizmatlar o'rtasida |
| Kechikish | kuzatuvchi tugamaguncha kutiladi | e'lon qilish tez, kuzatuvchi mustaqil |
| Ishonchlilik | jarayon yiqilsa hodisa yo'qoladi | navbat hodisani saqlaydi |
| Murakkablik | juda sodda | ko'proq (infratuzilma kerak) |

### 2.6. Xavflar va ehtiyot choralari

1. **Xotira oqimi (memory leak):** kuzatuvchi `subscribe` qilinib, keyin `unsubscribe` qilinmasa, Subject uni ushlab turadi va xotira tozalanmaydi. Yechim: `unsubscribe`/`detach`, kerak bo'lsa weak reference (o'quv dasturi: «unsubscribe/weak reference»).
2. **Notifikatsiya tartibi:** kuzatuvchilar chaqirilish tartibiga ishonmaslik; Kafka'da tartib faqat bitta partition ichida kafolatlanadi.
3. **Idempotentlik:** bir hodisa qayta yetib kelsa kuzatuvchi ikki marta bajarmasligi kerak: deduplikatsiya kaliti (event-id), outbox naqshi.
4. **Xatoni yutmaslik:** yiqilgan kuzatuvchi xatosini logga yoki dead-letter queue (DLQ) ga yuborish.
5. **Observer storm:** nazoratsiz ko'payib ketgan kuzatuvchilar debug'ni qiyinlashtiradi. Hodisa kontrakti (event-schema) va versiyalash barqaror bo'lsin.
6. **Yashirin yon ta'sirlar:** Subject «faqat e'lon qildim» deydi, observer kutilmagan ish qilishi mumkin; oq ro'yxat (whitelist) bilan cheklash.
7. **Backpressure:** kuzatuvchi hodisalarni tezroq oladigan tezlikdan sekin ishlasa, navbat to'lib boradi; o'quv dasturi buni «boshqarish kerak» muammolar qatoriga kiritadi (qo'llanmada batafsil yo'q: mentor qisqa tushuntiradi).
8. **Kuzatuvchanlik:** har bir hodisaga `trace-id` biriktirish, producer va consumer logida bir xil id.

### 2.7. Sinash

Unit: Subject'ga soxta (mock/stub) kuzatuvchi ulab, kerakli metod chaqirilganini tekshiramiz. Integratsion: real navbat va real consumer bilan, natijani idempotent assert bilan tekshiramiz.

```python
calls = []
bus = EventBus()
bus.on("book:borrowed", calls.append)
bus.emit("book:borrowed", {"book_id": 1})
assert calls == [{"book_id": 1}]
```

### 2.8. Qachon Observer kerak, qachon ortiqcha?

Kerak: bitta hodisaga bir nechta mustaqil javob, javob beruvchilar soni o'zgarib turadi, UI komponentlari. Ortiqcha: bitta aniq harakat, faqat bitta qabul qiluvchi, 5 qatorli skript: oddiy funksiya chaqirish yetarli (over-engineering).

---

## 3. Amaliy mashg'ulot (mini-loyiha: «Kutubxona boshqaruvi»)

Dasturdagi loyiha mavzularidan biri: «Kutubxona boshqaruvi» REST API (kitob/avtor CRUD, JWT autentifikatsiya). Bu hafta o'quvchi uni bosqichma-bosqich quradi: 10-dars: hodisalar, 11-dars: REST endpointlar, 12-dars: JSON kontrakt va xavfsizlik. Papka: portfolio repozitoriysidagi `library-api/`.

### 1-mashq (oson). OrderService va ikki kuzatuvchi
**Vazifa:** 2.3-bo'limdagi kodni yozing, ishga tushiring. `EmailNotifier` ni `unsubscribe` qilib, ikkinchi buyurtmada email chiqmasligini ko'rsating.

**Kutiladigan natija:** yuqoridagi 3 qatorli chiqish.

**Yechim:** 2.3-bo'limdagi kod to'liq javob. Asosiy nuqta: `email` o'zgaruvchisi saqlanadi, chunki `unsubscribe` aynan o'sha obyektni talab qiladi (yangi `EmailNotifier()` o'chirmaydi).

### 2-mashq (o'rta). Yiqilgan kuzatuvchi
**Vazifa:** `BrokenListener` yarating (`on_order_completed` ichida `raise RuntimeError("SMTP ishlamayapti")`). `EmailNotifier`, `BrokenListener`, `AnalyticsTracker` tartibida ulang. Qolgan ikki kuzatuvchi ishlaganini ko'rsating. Keyin `try/except` ni olib tashlab nima o'zgarishini ayting.

**Kutiladigan natija:** `try/except` bilan ham Email, ham Analytics chiqadi, `[WARN]` qatori bor. Usiz esa istisno `complete_order` dan chiqib ketadi va `AnalyticsTracker` umuman chaqirilmaydi.

**Yechim:**
```python
class BrokenListener:
    def on_order_completed(self, order_id: str) -> None:
        raise RuntimeError("SMTP ishlamayapti")

svc = OrderService()
svc.subscribe(EmailNotifier())
svc.subscribe(BrokenListener())
svc.subscribe(AnalyticsTracker())
svc.complete_order("ORD-001")
# Email -> ORD-001
# [WARN] listener failed: SMTP ishlamayapti
# Analytics -> ORD-001
```

### 3-mashq (o'rta). EventBus va test
**Vazifa:** 2.4-bo'limdagi `EventBus` ni yozing. `book:borrowed` hodisasiga ikkita handler ulang: biri `print`, biri ro'yxatga `book_id` qo'shadi. So'ng soxta kuzatuvchi bilan `assert` test yozing.

**Kutiladigan natija:** `SMS -> Ali`, `[7]`, test o'tadi.

**Yechim:**
```python
bus = EventBus()
log = []
bus.on("book:borrowed", lambda p: print("SMS ->", p["reader"]))
bus.on("book:borrowed", lambda p: log.append(p["book_id"]))
bus.emit("book:borrowed", {"book_id": 7, "reader": "Ali"})
print(log)  # [7]

calls = []
test_bus = EventBus()
test_bus.on("book:borrowed", calls.append)
test_bus.emit("book:borrowed", {"book_id": 1})
assert calls == [{"book_id": 1}]
```

### 4-mashq (qiyin). Kutubxona hodisalari
**Vazifa:** `library-api/events.py` da `EventBus` va `LibraryService.borrow(book_id, reader)` yozing. Kitob band bo'lsa `ValueError`. Muvaffaqiyatda `book:borrowed` e'lon qilinsin. Ikki kuzatuvchi: `SmsNotifier` (o'quvchiga xabar), `StatsCounter` (kitob bo'yicha qarz soni). Dublikat hodisani (bir `event_id` ikki marta) `StatsCounter` ikki marta sanamasin (idempotentlik).

**Kutiladigan natija:** bir `event_id` bilan ikki marta emit qilinsa, statistika 1 bo'ladi.

**Yechim:**
```python
import uuid

class LibraryService:
    def __init__(self, bus):
        self.bus = bus
        self.available = {1: True, 2: True}

    def borrow(self, book_id, reader):
        if not self.available.get(book_id):
            raise ValueError("Kitob band yoki mavjud emas")
        self.available[book_id] = False
        self.bus.emit("book:borrowed", {
            "event_id": str(uuid.uuid4()),
            "book_id": book_id,
            "reader": reader,
        })

class StatsCounter:
    def __init__(self):
        self.seen = set()
        self.count = {}

    def __call__(self, payload):
        if payload["event_id"] in self.seen:   # idempotentlik
            return
        self.seen.add(payload["event_id"])
        self.count[payload["book_id"]] = self.count.get(payload["book_id"], 0) + 1

bus = EventBus()
stats = StatsCounter()
bus.on("book:borrowed", stats)
bus.on("book:borrowed", lambda p: print("SMS ->", p["reader"]))
LibraryService(bus).borrow(1, "Ali")
event = {"event_id": "e-1", "book_id": 2, "reader": "Vali"}
bus.emit("book:borrowed", event)
bus.emit("book:borrowed", event)   # takror
print(stats.count)   # {1: 1, 2: 1}
```

### 5-mashq (bonus). Xotira oqimini ko'rish
**Vazifa:** `weakref.WeakSet` bilan kuzatuvchilarni saqlaydigan Subject yozing; kuzatuvchiga havola o'chirilganda u ro'yxatdan o'z-o'zidan tushishini isbotlang.

**Yechim:** (ixtiyoriy, o'quv dasturi «weak reference» ni eslatadi)
```python
import weakref, gc

class Subject:
    def __init__(self):
        self._obs = weakref.WeakSet()
    def subscribe(self, o):
        self._obs.add(o)
    def notify(self):
        return len(self._obs)

class Obs: pass

s = Subject()
o = Obs()
s.subscribe(o)
print(s.notify())   # 1
del o
gc.collect()
print(s.notify())   # 0
```

---

## 4. Tezkor savollar

1. Observer andozasida Subject va Observer rollari nima?
   - **Javob:** Subject (publisher) hodisani e'lon qiladi va kuzatuvchilar ro'yxatini saqlaydi; Observer (subscriber) hodisaga javob beradi. Subject kuzatuvchilar kimligini bilmaydi.
2. Observer qanday bo'sh bog'liqlik (loose coupling) beradi?
   - **Javob:** Subject faqat kuzatuvchi kontraktini (interfeysini) biladi; yangi kuzatuvchi qo'shish yoki o'chirish Subject kodini o'zgartirmaydi.
3. `unsubscribe` unutilsa nima bo'ladi?
   - **Javob:** Subject kuzatuvchiga havolani ushlab turadi, xotira tozalanmaydi (xotira oqimi); eskirgan kuzatuvchi hodisalarni olishda davom etadi.
4. Nega bitta kuzatuvchi yiqilsa, qolganlari ishlashi kerak? Qanday ta'minlanadi?
   - **Javob:** Kuzatuvchilar mustaqil. Har bir chaqiruv `try/except` ichida; xato logga/DLQ ga yoziladi, yutib yuborilmaydi.
5. Sinxron Observer va asinxron pub/sub farqi?
   - **Javob:** Birinchisi bitta jarayon ichida, kuzatuvchi tugamaguncha kutiladi; ikkinchisi navbat/event bus orqali xizmatlar o'rtasida, mustaqil va masshtablanuvchi, lekin murakkabroq.

## 5. Mentor uchun eslatmalar

- 9-dars uyga vazifasi (Factory/Singleton PR) ni dars boshida 3–4 daqiqada ko'zdan kechiring.
- Qo'llanmada backpressure batafsil yoritilmagan; dastur natijalarida nomi bor. Qisqa (1 daqiqa) tushuntiring: ishlab chiqaruvchi tezroq, iste'molchi sekinroq bo'lsa, navbat to'ladi.
- `EventBus` Python varianti qo'llanmadagi JavaScript namunasining o'zgartirilgan ko'rinishi: o'quvchiga shuni ayting.
- Telegram kanali o'xshatishi yordamchi analogiya, rasmiy hujjatdan emas.
