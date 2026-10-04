---
title: "8-dars. SOLID chuqurlashtirilgan: LSP, ISP, DIP va Code Smells refaktoringi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 3, "link": "/11-sinf/hafta-03/"}, "g": 8, "title": "SOLID chuqurlashtirilgan: LSP, ISP, DIP va Code Smells refaktoringi", "lead": "Liskov almashinish qoidasi, ixcham interfeyslar, Dependency Injection kuchi va yomon arxitektura alomatlarini (Code Smells) davolash.", "slide": "/slaydlar/11-sinf/hafta-03/dars-2.html", "tabs": [{"g": 7, "link": "/11-sinf/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/11-sinf/hafta-03/dars-2", "current": true}, {"g": 9, "link": "/11-sinf/hafta-03/dars-3", "current": false}], "prev": {"g": 7, "title": "Clean Code asoslari va SOLID: SRP hamda OCP tamoyillari", "link": "/11-sinf/hafta-03/dars-1"}, "next": {"g": 9, "title": "Loyihalash andozalari: Factory va Singleton arxitekturasi", "link": "/11-sinf/hafta-03/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **LSP (Liskov Substitution):** Voris sinf har doim o'zining ota sinfi o'rnida hech qanday kutilmagan xatosiz va qo'shimcha cheklovlarsiz ishlay olishi shart.
- **ISP (Interface Segregation):** Katta, «semiz» interfeyslar o'rniga har bir mijoz uchun alohida, tor maqsadli ixcham interfeyslar yaratish.
- **DIP (Dependency Inversion):** Biznes mantiq qatlamini aniq ma'lumotlar bazasi yoki tashqi API'ga bog'lamasdan, abstrakt interfeysga tayanish.
- **Dependency Injection (DI):** Kerakli bog'liqliklarni (Repository, Logger, Client) sinf ichida yaratmasdan, konstruktor orqali tashqaridan uzatish.
- **Code Smells (Kod hidlari):** Xato emas, lekin loyihaning tez orada parokanda bo'lishidan darak beruvchi yomon me'moriy belgilar (Long Method, God Object, Feature Envy).
- **Refaktoring madaniyati:** Mavjud kodning tashqi xatti-harakatini o'zgartirmagan holda uning ichki tuzilmasini tozalash va yaxshilash.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Barbara Liskov kim?

Liskov Substitution tamoyilining muallifi — amerikalik olima **Barbara Liskov**. U 1987-yilda ushbu tamoyilni kashf qilgan va 2008-yilda kompyuter fanlarining «Nobel mukofoti» hisoblangan nufuzli **Turing mukofoti** (Turing Award) bilan taqdirlangan.
Liskov tamoyili polimorfizmni faqat «nomi bir xil metodlar» deb emas, balki «xatti-harakat va natija kafolati» deb tushunishni talab qiladi.

### 2. Dependency Injection — dasturchining eng yaxshi do'sti

Faraz qiling, siz avtomobil ishlab chiqaryapsiz:
- Agar dvigatelni mashina ramasiga payvandlab tashlasangiz (Tight coupling — qattiq bog'liqlik), dvigatel buzilganda yoki uni elektr motorga almashtirmoqchi bo'lsangiz, butun mashinani kesib tashlashga to'g'ri keladi.
- Ammo dvigatel maxsus standart ulanishlar (Interface) orqali kiritilsa (Dependency Injection), siz uni xohlagan paytda benzin, dizel yoki elektr dvigateliga bir necha daqiqada almashtira olasiz.
Dasturlashda ham ma'lumotlar bazasi, to'lov tizimi yoki xat jo'natuvchi xizmat xuddi shu dvigatel kabi almashtiriladigan bo'lishi kerak!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **LSP** | Liskov Substitution Principle — voris sinf bazaviy sinf o'rnini to'liq bosa olishi |
| **ISP** | Interface Segregation Principle — interfeyslarni kichik va aniq qismlarga ajratish |
| **DIP** | Dependency Inversion Principle — yuqori va quyi modullarning abstraksiyaga tayanishi |
| **Dependency Injection** | Bog'liqliklarni sinf ichida emas, tashqaridan uzatish usuli |
| **Code Smell** | Dasturning ichki arxitekturasi sifatsizligidan darak beruvchi yomon belgilar |
| **God Object** | Tizimdagi hamma narsani boshqaruvchi haddan tashqari ulkan, xunuk sinf |
| **Tight Coupling** | Sinflarning bir-biriga qattiq bog'lanib, alohida ajratib bo'lmaydigan holati |
| **Loose Coupling** | Sinflarning mustaqil va faqat umumiy interfeyslar orqali aloqa qilishi |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- 🏛️ **Turing mukofoti:** Barbara Liskov kompyuter fanlari sohasida Turing mukofotini qo'lga kiritgan tarixdagi ikkinchi ayol olima hisoblanadi.
- ⚡ **Mikroxizmatlar asosi:** Bugungi kunda jahon miqyosidagi kompaniyalar (Netflix, Uber, Amazon) mikroxizmatlar arxitekturasini qura olishlarining asosiy sababi — DIP va Loose Coupling tamoyillariga qat'iy amal qilishidir.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Savollar va topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
LSP (Liskov Substitution) tamoyilini «Qush va Pingvin» misolida bitta sodda jumlada tushuntiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Interface Segregation (ISP) nima uchun katta va universal interfeyslardan ko'ra bir nechta kichik interfeyslarni afzal ko'radi?

### 3-topshiriq <Badge type="tip" text="oson" />
Dependency Injection (DI) tushunchasini avtomobil va uning dvigateli analogiyasi yordamida izohlab bering.

### 4-topshiriq <Badge type="warning" text="o'rta" />
Quyidagi kodda LSP qanday buzilganini ko'rsating va uni qanday to'g'rilash kerakligini tushuntiring:
```python
class Bird:
    def fly(self):
        return "Uchyapman!"

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Tuyaqush ucha olmaydi!")
```

### 5-topshiriq <Badge type="warning" text="o'rta" />
Quyidagi «semiz» interfeysni ISP tamoyili asosida 2 ta mustaqil va mantiqiy interfeysga ajrating:
```python
class Worker(ABC):
    @abstractmethod
    def write_code(self): ...
    @abstractmethod
    def design_ui(self): ...
    @abstractmethod
    def manage_budget(self): ...
```

### 6-topshiriq <Badge type="warning" text="o'rta" />
DIP tamoyiliga ko'ra: nima uchun `OrderService` sinfi to'g'ridan-to'g'ri `MySQLDatabase()` sinfiga bog'lanmasligi kerak? Bu qanday qiyinchilik tug'diradi?

### 7-topshiriq <Badge type="warning" text="o'rta" />
«Code Smell» nima? U kompilyatsiya xatosi (syntax error) yoki dasturning to'xtab qolishi (crash) bilan bir xil narsami? Farqini tushuntiring.

### 8-topshiriq <Badge type="danger" text="qiyin" />
«God Object» kod hidining 3 ta asosiy alomatini sanang. Nega yosh dasturchilar ko'pincha barcha funksiyalarni bitta sinfga to'plab qo'yishga moyil bo'lishadi?

### 9-topshiriq <Badge type="danger" text="qiyin" />
Python tilida `EmailService` va `SMSService` uchun umumiy `MessageSender` interfeysini yozing. Keyin `NotificationManager` sinfini shunday tuzingki, u konstruktori orqali har qanday xabar xizmatini (DI) qabul qila olsin.

### 10-topshiriq <Badge type="danger" text="qiyin" />
Kodni refaktoring qilishda Unit Testlarning o'rni qanday? Nega testsiz qilingan katta refaktoring «minada yurish» bilan tenglashtiriladi?

### 11-topshiriq <Badge type="info" text="bonus" />
SOLID ning 5 ta tamoyili (SRP, OCP, LSP, ISP, DIP) qatnashgan kichik «E-kutubxona kitob ijarasi» arxitekturasining UML sxemasi yoki toza Python kod skeletini yozib chiqing.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. Voris sinf metodida `raise NotImplementedError` yozilishi qaysi tamoyilning buzilishidan darak beradi?
2. Tight Coupling (qattiq bog'liqlik) loyihaning o'sishiga qanday to'sqinlik qiladi?
3. Sinflararo munosabatda Dependency Injection qanday qilib unit-test yozishni osonlashtiradi?
4. «Feature Envy» kod hidi nimani anglatadi?
5. SOLID qoidalariga rioya qilingan loyiha bilan rioya qilinmagan loyihaning 1 yildan keyingi taqdiri qanday bo'ladi?

</div>

