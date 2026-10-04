# 7-dars. Clean Code asoslari va SOLID: SRP hamda OCP tamoyillari

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + arxitektura amaliyoti · **I-bob**, 7-dars (umumiy 7–51)

## 1. Dars rejasi

**Maqsad:** o'quvchida professional dasturiy ta'minot muhandisligining tayanch ustunlari bo'lgan Clean Code madaniyati, to'g'ri nomlash (Naming conventions), kichik va bitta maqsadli funksiyalar yozish, DRY, KISS, YAGNI tamoyillari hamda obyektga yo'naltirilgan dizaynning ilk 2 ta qoidasi: Single Responsibility (SRP) va Open/Closed (OCP) tamoyillarini chuqur o'rganish va kodni refaktoring qilish ko'nikmalarini shakllantirish.

**Kutiladigan natija:**
- Clean Code'ning iqtisodiy va texnik ahamiyatini («Kodni yozishdan ko'ra uni o'qishga 10 barobar ko'p vaqt sarflanadi») asoslab bera oladi.
- DRY (Don't Repeat Yourself), KISS (Keep It Simple, Stupid) va YAGNI (You Aren't Gonna Need It) tamoyillarini kodda farqlaydi va qo'llaydi.
- «Spaghetti code» (aralash-quralash kod)dan metodlarni ajratish (Extract Method) orqali toza arxitektura qura oladi.
- SRP (Single Responsibility) tamoyili buzilgan sinf/funksiyani aniqlab, mas'uliyatlarni alohida sinflarga ajratadi.
- OCP (Open/Closed) tamoyili yordamida `if/elif/switch` tarmoqlarini polimorfizm va abstrakt interfeyslar (`abc.ABC`) asosida kengaytirishga moslashtiradi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 2-hafta xulosasi (PR, Code Review, Branch Protection). Muammo: «Review'da yomon kodni qanday ajratamiz? Kod 'ishlayotgan' bo'lsa ham nega uni qabul qilib bo'lmaydi?» |
| 10–35 daq | Yangi mavzu: Nazariya | Clean Code qoidalari, nomlash, kichik funksiyalar, DRY/KISS/YAGNI, SOLID ga kirish: SRP va OCP |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliy mashg'ulot | «Buyurtma va to'lov tizimi» kodini refaktoring qilish: bitta bahaybat funksiyani SRP va OCP ga mos sinflarga ajratish |
| 65–75 daq | Tezkor nazorat | 5 ta savol-javob va kod tahlili |
| 75–80 daq | Xulosa va uyga vazifa | Muhim xulosalar va uy vazifasi yo'riqnomasi |

---

## 2. Dars konspekti

### 2.1. Clean Code nima va nega u texnik estetika emas?

**Clean Code (Toza kod)** — bu shunchaki chiroyli formatlangan matn emas. Bu boshqa bir muhandis (yoki 6 oydan keyin o'zingiz) o'qiganda maqsadi, niyati va mantiqini hech qanday qiyinchiliksiz bir qarashda tushuna oladigan, testlanadigan va o'zgartirishga oson bo'lgan koddir.

Robert Martin («Uncle Bob») ta'kidlaganidek: dasturchilar vaqtining 90% qismini yangi kod yozishga emas, balki **mavjud kodni o'qish va tushunishga** sarflashadi. Tushunarsiz yozilgan kod korxona uchun katta moliyaviy zarar va rivojlanish tezligining pasayishiga olib keladi.

### 2.2. Clean Code'ning 3 ta oltin qoidasi

1. **Tushunarli va ma'noli nomlash (Meaningful Names):**
   - Yomon: `d`, `temp`, `data`, `doProcess()`, `x1`.
   - Yaxshi: `days_since_last_login`, `calculate_invoice_total()`, `discount_rate`.
   - Qoida: O'zgaruvchi va funksiya nomlari «Nima qiladi?» degan savolga izohsiz javob berishi kerak.
2. **Kichik va bitta vazifali funksiyalar (Do One Thing):**
   - Funksiya faqat bitta ishni qilsin va uni a'lo darajada bajarsin.
   - Agar funksiya 20-30 qatordan oshib ketsa, unda bir nechta mantiq aralashib ketgan bo'ladi (`Extract Method` usuli bilan bo'lish shart).
3. **DRY, KISS va YAGNI:**
   - **DRY (Don't Repeat Yourself):** Kodni takrorlama. Bir xil mantiq faqat bitta joyda yozilsin. O'zgarish bo'lsa, faqat bitta joy tuzatiladi.
   - **KISS (Keep It Simple, Stupid):** Oddiy saqla, murakkablashtirma. Ehtiyoj bo'lmagan joyda murakkab tuzilmalar qurma.
   - **YAGNI (You Aren't Gonna Need It):** «Kelajakda kerak bo'lib qolar» deb hozir kerak bo'lmagan funksiyalarni yozma. Ular ortiqcha texnik qarzga aylanadi.

### 2.3. SOLID: S — Single Responsibility Principle (SRP)

> «A class should have one, and only one, reason to change.»
> (Har bir sinf faqat bitta sababga ko'ra o'zgarishi kerak).

Agar bitta `InvoiceService` sinfi hisob-kitob qilsa, PDF fayl yasasa va mijozga email yuborsa — unda kamida 3 ta mas'uliyat bor:
- Soliq qonuni o'zgarsa &rarr; sinf o'zgaradi;
- PDF dizayni o'zgarsa &rarr; yana shu sinf o'zgaradi;
- Email serveri o'zgarsa &rarr; yana shu sinf o'zgaradi.

**Yechim:** Mas'uliyatlarni 3 ta alohida sinfga ajratish:
```python
# YAXSHI: SRP ga mos
class InvoiceCalculator:
    def calculate_total(self, items):
        return sum(item.price * item.qty for item in items)

class InvoicePdfGenerator:
    def generate(self, invoice):
        # Faqat PDF tuzish
        pass

class InvoiceEmailSender:
    def send(self, invoice, email):
        # Faqat pochta jo'natish
        pass
```

### 2.4. SOLID: O — Open/Closed Principle (OCP)

> «Software entities should be open for extension, but closed for modification.»
> (Dasturiy modullar kengaytirishga ochiq, lekin mavjud kodni o'zgartirishga yopiq bo'lishi kerak).

Yomon yondashuv — yangi to'lov turi qo'shilganda har safar asosiy funksiyaga kirib `if/elif` zanjirini cho'zish:
```python
# YOMON: OCP buzilishi
def process_payment(payment_type, amount):
    if payment_type == "card":
        ...
    elif payment_type == "cash":
        ...
    elif payment_type == "crypto":  # har yangi turda funksiya buziladi
        ...
```

**Yechim:** Polimorfizm va abstrakt sinflar (`ABC`):
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> bool:
        pass

class CardPayment(PaymentProcessor):
    def process(self, amount: float) -> bool:
        # Karta to'lovi
        return True

class CryptoPayment(PaymentProcessor):
    def process(self, amount: float) -> bool:
        # Kripto to'lov
        return True

# Mijoz funksiyasi o'zgarmaydi!
def process_order_payment(processor: PaymentProcessor, amount: float):
    return processor.process(amount)
```
Yangi to'lov turi kerakmi? Faqat yangi sinf qo'shamiz (`ApplePayPayment`). Mavjud `process_order_payment` kodiga bitta ham tegmaymiz!

---

## 3. Amaliy mashg'ulot

### 1-mashq. Spaghetti kodni refaktoring qilish (Extract Method)
**Vazifa:** Quyidagi barcha ishlarni bitta joyda qilayotgan funksiyani Clean Code talablari asosida kichik, sof funksiyalarga ajrating:

```python
# Boshlang'ich kod
def process_order(order):
    total = 0
    for it in order.items:
        total += it.price * it.qty
    tax = total * 0.12
    if order.customer.is_vip:
        total *= 0.9
    # email yuborish
    print(f"Receipt sent to {order.customer.email}")
    return total + tax
```

**Yechim:**
```python
def calculate_subtotal(order):
    return sum(it.price * it.qty for it in order.items)

def apply_discount(amount: float, is_vip: bool) -> float:
    return amount * 0.9 if is_vip else amount

def calculate_tax(amount: float, rate: float = 0.12) -> float:
    return amount * rate

def notify_customer(email: str):
    print(f"Receipt sent to {email}")

def process_order(order):
    subtotal = calculate_subtotal(order)
    discounted = apply_discount(subtotal, order.customer.is_vip)
    total = discounted + calculate_tax(discounted)
    notify_customer(order.customer.email)
    return total
```

---

## 4. Tezkor savollar (Checklist)

1. Nega Clean Code texnik xarajatlarni kamaytiradi?
   - **Javob:** Kodni o'qish, tushunish va xatolarni tuzatish vaqtini keskin qisqartiradi, yangi dasturchilar loyihaga tez kirishib ketadi.
2. DRY va YAGNI qoidalarining farqi nimada?
   - **Javob:** DRY kodning takrorlanishini yo'qotadi; YAGNI esa hozircha talab etilmagan keraksiz funksiyalarni kelajak uchun deb yozishdan to'xtatadi.
3. Single Responsibility Principle (SRP) buzilganini qanday sezish mumkin?
   - **Javob:** Agar sinf nomi «Manager», «Processor», «Handler» bo'lib, ichida bir-biriga bog'liq bo'lmagan vazifalar (hisoblash, saqlash, xat yuborish) bo'lsa va uning o'zgarishiga bir nechta sabab bo'lsa.
4. OCP tamoyilida «o'zgartirishga yopiq» degani nimani anglatadi?
   - **Javob:** Tizimga yangi funksionallik qo'shish uchun avval yozilgan va ishlab turgan sinflarning ichki kodini o'zgartirish shart emasligini bildiradi.
5. OCP tamoyilini amalga oshirishda qaysi OOP xususiyati asosiy rol o'ynaydi?
   - **Javob:** Polimorfizm va Abstraksiya (Interfeyslar yoki Abstrakt bazaviy sinflar).
