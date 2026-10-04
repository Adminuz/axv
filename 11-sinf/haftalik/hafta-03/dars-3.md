# 9-dars. Loyihalash andozalari: Factory va Singleton arxitekturasi

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + arxitektura amaliyoti · **I-bob**, 9-dars (umumiy 9–51)

## 1. Dars rejasi

**Maqsad:** o'quvchida dasturiy ta'minot muhandisligida sinovdan o'tgan loyihalash andozalari (Design Patterns), ularning tasnifi (Creational, Structural, Behavioral) hamda yaratuvchi (Creational) andozalardan eng mashhurlari bo'lgan Factory Method (Fabrika metodi) va Singleton (Yagona nusxa) andozalarini chuqur tushunish, ularning Python tilida to'g'ri (thread-safe, lazy initialization) implementatsiyasini yaratish hamda testlanishdagi cheklovlarini tahlil qilish ko'nikmalarini shakllantirish.

**Kutiladigan natija:**
- Loyihalash andozalari tayyor kod emas, balki arxitekturaviy fikrlash modeli ekanini tushunadi.
- Andozani qachon qo'llash zarur (kengayuvchanlik, DRY, polimorfizm) va qachon ortiqcha (Over-engineering) ekanini farqlaydi.
- Factory Method andozasi orqali obyektlarni yaratish logikasini mijoz kodidan ajratib, markazlashtiradi.
- Singleton andozasi qachon kerakligini (Database Connection Pool, Logger, Config Manager) va uning global holat (Global State) keltirib chiqarish xatarlarini biladi.
- Python tilida `__new__` metodi va metaprogrammalash orqali Singleton va Factory patternlarini amalda yozadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | O'tgan darsni takrorlash (LSP, ISP, DIP va Refaktoring). Muammoli vaziyat: «Loyiha bo'ylab 50 ta joyda `DatabaseConnection()` chaqirilsa va har safar yangi ulanish ochilsa, server xotirasi nima bo'ladi?» |
| 10–35 daq | Yangi mavzu: Nazariya | Design Patterns tasnifi (GoF), Factory Method mohiyati, Singleton ishlash prinsipi va xatarlari |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliy mashg'ulot | «PaymentProcessorFactory» va «DatabaseConnectionPool (Singleton)» arxitekturasini Python'da noldan yozish va sinash |
| 65–75 daq | Tezkor nazorat | 5 ta savol-javob va andozalarni taqqoslash |
| 75–80 daq | Xulosa va uyga vazifa | Muhim xulosalar va 3-hafta yakuni |

---

## 2. Dars konspekti

### 2.1. Loyihalash andozalari (Design Patterns) nima?

**Design Patterns (Loyihalash andozalari)** — dasturiy ta'minotni ishlab chiqish jarayonida tez-tez uchraydigan arxitektura muammolarining vaqt va amaliyot sinovidan o'tgan, qayta foydalanishga yaroqli konseptual yechimlaridir.

Andozalar 3 ta asosiy toifaga bo'linadi (Gang of Four — GoF):
1. **Yaratuvchi (Creational):** Obyektlarni qanday va qayerda yaratish jarayonini boshqaradi (Factory, Singleton, Builder, Prototype).
2. **Strukturaviy (Structural):** Sinflar va obyektlarni bir-biriga moslashtirish va bog'lash (Adapter, Decorator, Facade).
3. **Xulq-atvor (Behavioral):** Obyektlar o'rtasida ma'lumot va vazifalar taqsimoti (Observer, Strategy, Command).

> **Muhim mezon:** «Andoza bor ekan, ishlatishim kerak» deb har joyga pattern tiqish — **Over-engineering** (ortiqcha murakkablashtirish) hisoblanadi. Har doim Muammo &rarr; Tahlil &rarr; Minimal sodda yechim (KISS) tamoyili ustuvor bo'lishi shart!

### 2.2. Factory Method andozasi

**Maqsad:** Obyektlarni to'g'ridan-to'g'ri `new` yoki `ClassName()` bilan yaratish o'rniga, obyekt yaratishni maxsus «fabrika» orqali markazlashtirish.

Natijada:
- Mijoz kodi aniq sinf nomlarini (masalan, `PostgresDatabase`, `SqliteDatabase`) bilishi shart emas, u faqat umumiy interfeys bilan ishlaydi.
- Yangi turdagi obyekt qo'shilganda mijoz kodi o'zgarmaydi, faqat fabrikani kengaytiramiz (OCP).

```python
from abc import ABC, abstractmethod

# Umumiy mahsulot interfeysi
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float): pass

class UzcardPayment(Payment):
    def pay(self, amount: float):
        return f"Uzcard orqali {amount} so'm to'landi"

class HumoPayment(Payment):
    def pay(self, amount: float):
        return f"Humo orqali {amount} so'm to'landi"

# Fabrika (Factory)
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type: str) -> Payment:
        types = {
            "uzcard": UzcardPayment,
            "humo": HumoPayment
        }
        creator = types.get(payment_type.lower())
        if not creator:
            raise ValueError(f"Noma'lum to'lov turi: {payment_type}")
        return creator()

# Foydalanish: mijoz sinf tafsilotlarini bilmaydi
payment = PaymentFactory.create_payment("uzcard")
print(payment.pay(50000))
```

### 2.3. Singleton andozasi

**Maqsad:** Butun tizim (dastur) bo'yicha ma'lum bir sinfning **faqat bitta nusxasi** mavjud bo'lishini va unga yagona global kirish nuqtasini kafolatlash.

Qayerda kerak?
- **Ma'lumotlar bazasi ulanishlar puli (Connection Pool):** Har bir so'rovda yangi baza ulanishi ochilsa, server xotirasi to'lib ketadi.
- **Konfiguratsiya menejeri (ConfigManager):** Dastur sozlamalari (`settings.env`) xotirada bitta bo'lishi kerak.
- **Logger (Jurnal yozuvchi):** Barcha loglar bitta oqimga yozilishi lozim.

**Python'da Singleton implementatsiyasi (`__new__` metodi orqali):**
```python
class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Faqat birinchi marta xotiradan joy ajratiladi
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, connection_string="db://localhost"):
        if not self._initialized:
            self.connection_string = connection_string
            self._initialized = True
            print("Yangi DB ulanishi muvaffaqiyatli ochildi!")

# Tekshirish:
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # True! Xotiradagi aynan bitta obyekt!
```

### 2.4. Singleton andozasining xatarlari (Anti-pattern deb atalishi sababi)

1. **Yashirin bog'liqliklar va Global holat (Global State):** Dasturning istalgan joyida chaqirib o'zgartirilishi mumkinligi sababli kod o'rtasidagi bog'liqlik ko'rinmas bo'lib qoladi.
2. **Unit-testlashdagi qiyinchilik:** Bitta testda Singleton holati o'zgartirilsa, u keyingi barcha testlarga ta'sir qiladi (flaky tests).
3. **Ko'p oqimli muhit (Multi-threading):** Bir vaqtning o'zida bir nechta oqim murojaat qilsa, poyga holati (Race Condition) tufayli 2 ta obyekt yaratilib ketishi mumkin (Thread-safe Lock talab etiladi).

---

## 3. Amaliy mashg'ulot

### 1-mashq. Logger Singleton yaratish va test qilish
**Vazifa:** Dastur bo'ylab barcha log xabarlarini bitta ro'yxatda to'plovchi `AppLogger` nomli Singleton sinfini tuzing. 2 ta alohida o'zgaruvchi yaratib, xabar qo'shing va ularning bitta xotiraga ulanganini isbotlang.

**Yechim:**
```python
class AppLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message: str):
        self.logs.append(message)

# Sinov:
logger_a = AppLogger()
logger_a.log("Foydalanuvchi tizimga kirdi")

logger_b = AppLogger()
logger_b.log("Buyurtma rasmiylashtirildi")

print(logger_a.logs)
# Natija: ['Foydalanuvchi tizimga kirdi', 'Buyurtma rasmiylashtirildi']
print(logger_a is logger_b)  # True
```

---

## 4. Tezkor savollar (Checklist)

1. Creational (Yaratuvchi) andozalar qanday muammolarni hal qiladi?
   - **Javob:** Obyektlarni yaratish mexanizmini boshqaradi, tizimni obyektlar qanday yaratilishi va qanday tuzilishiga bog'liq bo'lmagan mustaqil holatga keltiradi.
2. Factory Method andozasining asosiy afzalligi nima?
   - **Javob:** Mijoz kodini aniq sinflarga bog'lamaydi, obyekt yaratish logikasini bir joyda markazlashtiradi va OCP tamoyiliga mos kengayish beradi.
3. Singleton andozasida `__new__` metodi nima vazifani bajaradi?
   - **Javob:** Obyekt xotirada yaratilishidan oldin tekshiradi: agar nusxa allaqachon mavjud bo'lsa, o'shani qaytaradi; yo'q bo'lsa, yangi nusxa ochadi.
4. Nega Singleton ba'zida Anti-pattern (zararli andoza) deb hisoblanadi?
   - **Javob:** Chunki u global holat yaratadi, sinflar o'rtasida yashirin bog'liqlik paydo qiladi va unit-testlarni izolyatsiyada o'tkazishni qiyinlashtiradi.
5. Singleton o'rniga qanday zamonaviy arxitektura yechimi tavsiya etiladi?
   - **Javob:** Dependency Injection konteynerlari orqali obyektning bitta nusxasini (Singleton lifecycle) e'lon qilish va kerakli joylarga uzatish.
