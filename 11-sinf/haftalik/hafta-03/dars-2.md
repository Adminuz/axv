# 8-dars. SOLID chuqurlashtirilgan: LSP, ISP, DIP va Code Smells refaktoringi

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + arxitektura amaliyoti · **I-bob**, 8-dars (umumiy 8–51)

## 1. Dars rejasi

**Maqsad:** o'quvchida SOLID tamoyillarining qolgan 3 ta tayanchi bo'lgan Liskov Substitution (LSP), Interface Segregation (ISP) va Dependency Inversion (DIP) tamoyillarini chuqur o'zlashtirish, qatlamli backend arxitekturasida Dependency Injection (DI) mexanizmini qo'llash, hamda loyihada uchraydigan "kod hidlari"ni (Code Smells: Long Method, God Object, Feature Envy) aniqlab, ularni xavfsiz refaktoring qilish ko'nikmalarini shakllantirish.

**Kutiladigan natija:**
- LSP (Liskov almashinish) tamoyili nimani talab qilishini (voris sinf bazaviy sinf o'rnida kutilmagan xatosiz ishlashi) klassik Rectangle/Square va real backend misollarida tushuntira oladi.
- ISP (Interface ajratish) tamoyili asosida "hamma narsani biluvchi semiz interfeyslar"ni mijoz uchun ixcham va maqsadli kichik interfeyslarga ajratadi.
- DIP (Bog'liqlikni teskari qilish) tamoyiliga ko'ra biznes mantiqni (Service) to'g'ridan-to'g'ri bazaga (PostgreSQL/MySQL) emas, abstraksiyaga (Repository) bog'laydi.
- Dependency Injection (DI) orqali sinflarni mustaqil va oson testlanadigan (mocking) holatga keltiradi.
- Kod hidlarini (Code Smells) aniqlaydi va Extract Class, Replace Conditional with Polymorphism kabi refaktoring usullarini amalda qo'llaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | O'tgan darsni takrorlash (Clean Code, DRY/KISS/YAGNI, SRP va OCP). Muammo: «Nega to'g'ridan-to'g'ri `psycopg2` yoki `requests` ga bog'langan servisni test qilib bo'lmaydi va har doim haqiqiy server kerak bo'ladi?» |
| 10–35 daq | Yangi mavzu: Nazariya | LSP (Liskov qoidasi), ISP (ixcham interfeyslar), DIP (Dependency Inversion & Injection), Code Smells turlari |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–65 daq | Amaliy mashg'ulot | `UserService`ni DIP va ISP asosida refaktoring qilish: `UserRepository` interfeysini yaratish va `InMemoryUserRepository` orqali unit-test yozish |
| 65–75 daq | Tezkor nazorat | 5 ta savol-javob va refaktoring tahlili |
| 75–80 daq | Xulosa va uyga vazifa | Muhim xulosalar va uy vazifasi yo'riqnomasi |

---

## 2. Dars konspekti

### 2.1. Liskov Substitution Principle (LSP)

> «Subtypes must be substitutable for their base types.»
> (Voris sinflar o'zlarining bazaviy sinflari o'rnida hech qanday kutilmagan syurprizsiz muammosiz ishlashi kerak).

Agar biror funksiya `BaseClass` qabul qilsa, unga `SubClass` uzatilganda funksiya buzilmasligi yoki dastur noaniq istisno (exception) tashlamasligi lozim.

Klassik xato misoli: `Rectangle` (To'rtburchak) va `Square` (Kvadrat). Matematikada kvadrat to'rtburchakdir, ammo dasturlashda kvadratning enini o'zgartirsangiz, bo'yi ham majburiy o'zgaradi. Natijada `set_width()` funksiyasi kutilmagan natija beradi va LSP buziladi.

LSP ga rioya qilish qoidalari:
- Voris sinf metod parametrlari cheklovlarini kuchaytirmasligi kerak.
- Voris sinf bazaviy sinf va'da qilganidan kamroq xatti-harakat ko'rsatmasligi yoki bo'sh `raise NotImplementedError` tashlamasligi lozim.

### 2.2. Interface Segregation Principle (ISP)

> «Clients should not be forced to depend upon interfaces that they do not use.»
> (Mijozlar o'zlari ishlatmaydigan metodlarga bog'lanishga majbur bo'lmasligi kerak).

Katta va hamma narsani o'z ichiga olgan «semiz» (fat) interfeyslar o'rniga har bir mijoz uchun kerakli bo'lgan kichik, ixcham interfeyslar yaratish lozim.

```python
# YOMON: Ortiqcha metodlarga majburlaydi
class PaymentGateway(ABC):
    @abstractmethod
    def pay_card(self, data): ...
    @abstractmethod
    def pay_cash(self, data): ...
    @abstractmethod
    def refund(self, data): ...

# YAXSHI: Kichik va aniq interfeyslar (ISP)
class CardPayable(ABC):
    @abstractmethod
    def pay_card(self, data): ...

class Refundable(ABC):
    @abstractmethod
    def refund(self, data): ...
```

### 2.3. Dependency Inversion Principle (DIP) va Dependency Injection (DI)

> «High-level modules should not depend on low-level modules. Both should depend on abstractions.»
> (Yuqori darajadagi biznes mantiq past darajadagi detallarga emas, ikkalasi ham abstraksiyalarga tayanishi kerak).

**Yomon arxitektura (Qattiq bog'liqlik - Tight Coupling):**
```python
# YOMON: UserService to'g'ridan-to'g'ri Postgres ga bog'langan
class UserService:
    def __init__(self):
        self.db = PostgresDatabase("localhost:5432") # Qattiq bog'liqlik!
    
    def get_user(self, user_id):
        return self.db.query(f"SELECT * FROM users WHERE id={user_id}")
```
Bu kodni unit-test qilib bo'lmaydi! Chunki kompyuteringizda PostgreSQL o'chirilgan bo'lsa, test ishlamaydi.

**Yaxshi arxitektura (DIP va Dependency Injection):**
```python
from abc import ABC, abstractmethod

# 1. Abstraksiya (Interfeys)
class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int):
        pass

# 2. Past darajadagi aniq amalga oshirish
class PostgresUserRepository(UserRepository):
    def __init__(self, db_connection):
        self.conn = db_connection
    def get_by_id(self, user_id: int):
        # SQL so'rov
        pass

# 3. Yuqori darajadagi biznes mantiq
class UserService:
    def __init__(self, repo: UserRepository):  # Dependency Injection!
        self.repo = repo
    
    def get_user(self, user_id: int):
        return self.repo.get_by_id(user_id)
```
Endi testlarda haqiqiy bazaning o'rniga oddiy Python lug'atidan iborat `InMemoryUserRepository`ni osongina uzatish (Inject qilish) mumkin!

### 2.4. Kod hidlari (Code Smells) va Refaktoring

**Code Smell (Kod hidi)** — bu dasturda xato (bug) emas, balki kelajakda katta muammo tug'dirishi mumkin bo'lgan yomon arxitektura alomatidir:
1. **Long Method (Juda uzun funksiya):** Bitta funksiya 50 qatordan oshib ketgan. Davosi: `Extract Method`.
2. **Large Class / God Object (Xudo-sinf):** Barcha ishlarni bitta ulkan sinf bajaradi. Davosi: `Extract Class` (SRP).
3. **Primitive Obsession:** Har qanday ma'lumotni (telefon raqam, pul, manzil) oddiy `str` yoki `int` deb saqlash. Davosi: Value Object (masalan: `Money`, `PhoneNumber`).
4. **Feature Envy (Boshqa sinfga hasad):** Bir sinfdagi metod o'z sinfidan ko'ra boshqa sinfning ma'lumotlarini ko'proq ishlatadi. Davosi: `Move Method`.

---

## 3. Amaliy mashg'ulot

### 1-mashq. DIP va Testability amaliyoti
**Vazifa:** `UserRepository` interfeysidan foydalanib, unit testlar uchun mo'ljallangan `FakeUserRepository` sinfini yarating va `UserService`ni hech qanday tashqi bazasiz test qiling.

**Yechim:**
```python
# Test uchun soxta (mock/in-memory) ombor
class FakeUserRepository(UserRepository):
    def __init__(self):
        self._users = {
            1: {"id": 1, "name": "Ali", "email": "ali@mail.uz"},
            2: {"id": 2, "name": "Vali", "email": "vali@mail.uz"}
        }
    
    def get_by_id(self, user_id: int):
        return self._users.get(user_id)

# Test jarayoni:
def test_user_service():
    repo = FakeUserRepository()
    service = UserService(repo=repo)
    
    user = service.get_user(1)
    assert user["name"] == "Ali"
    print("Test muvaffaqiyatli o'tdi! Hech qanday Postgres server talab qilinmadi.")

test_user_service()
```

---

## 4. Tezkor savollar (Checklist)

1. Liskov Substitution Principle (LSP) buzilishiga bitta hayotiy misol keltiring.
   - **Javob:** Bazaviy `Bird` (Qush) sinfida `fly()` metodi bo'lsa, undan meros olgan `Penguin` (Pingvin) yoki `Ostrich` (Tuyaqush) ucha olmaydi va xato beradi.
2. Interface Segregation (ISP) nima uchun kerak?
   - **Javob:** Sinflarni o'ziga mutlaqo kerak bo'lmagan ortiqcha metodlarni bo'sh funksiya qilib yozishga majburlamaslik uchun.
3. Dependency Injection (DI) nima?
   - **Javob:** Sinf ichida tashqi obyektni (`new DB()`) o'zi yaratmasdan, uni konstruktor orqali (`__init__(self, db)`) tashqaridan qabul qilib olishi.
4. Nega DIP qoidasi arxitekturani testlanadigan (testable) qiladi?
   - **Javob:** Chunki haqiqiy qimmat yoki sekin ishlaydigan tashqi xizmatlar (DB, to'lov shlyuzi, SMS server) o'rniga testlarda tezkor soxta (mock) obyektlarni kiritish mumkin bo'ladi.
5. "God Object" (Xudo-sinf) qanday kod hidi hisoblanadi?
   - **Javob:** Tizimdagi barcha biznes mantiqni, ma'lumotlarni va boshqaruvni bitta bahaybat sinfga yig'ib qo'yish.
