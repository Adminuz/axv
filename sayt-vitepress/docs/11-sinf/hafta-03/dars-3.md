---
title: "9-dars. Loyihalash andozalari: Factory va Singleton arxitekturasi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 3, "link": "/11-sinf/hafta-03/"}, "g": 9, "title": "Loyihalash andozalari: Factory va Singleton arxitekturasi", "lead": "Creational patterns: Factory Method yordamida obyekt yaratishni markazlashtirish, Singleton kuchi va global holat xatarlari.", "slide": "/slaydlar/11-sinf/hafta-03/dars-3.html", "tabs": [{"g": 7, "link": "/11-sinf/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/11-sinf/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/11-sinf/hafta-03/dars-3", "current": true}], "prev": {"g": 8, "title": "SOLID chuqurlashtirilgan: LSP, ISP, DIP va Code Smells refaktoringi", "link": "/11-sinf/hafta-03/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Loyihalash andozalari (Design Patterns):** Ko'p uchraydigan arxitektura muammolarining sinovdan o'tgan, qayta foydalanishga yaroqli konseptual fikrlash modellari.
- **Uch toifa (GoF):** Yaratuvchi (Creational), Strukturaviy (Structural) va Xulq-atvor (Behavioral).
- **Factory Method:** Obyektlarni to'g'ridan-to'g'ri sinf nomi orqali yaratish o'rniga, ularni maxsus «fabrika» orqali yaratish. Natijada mijoz kodi aniq sinflarni bilmaydi va tizim OCP bo'yicha oson kengayadi.
- **Singleton:** Dastur bo'ylab ma'lum bir sinfning faqat va faqat bitta nusxasi mavjud bo'lishini ta'minlash (Database Connection Pool, Logger, ConfigManager).
- **Python'da `__new__`:** Obyekt xotiradan joy olish paytini ushlab qolib, Singleton nusxasi mavjudligini nazorat qilish usuli.
- **Singleton xatarlari:** Yashirin global holat yaratishi, ko'p oqimli (multi-threading) muhitda race condition keltirib chiqarishi va unit-testlarni bir-biriga bog'lab qo'yishi mumkinligi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Gang of Four (To'rtlik to'dasi) kimlar?

1994-yilda Erich Gamma, Richard Helm, Ralph Johnson va John Vlissides ismli to'rt nafar me'mor-dasturchi «Design Patterns: Elements of Reusable Object-Oriented Software» nomli kitobni chop etishdi.
Ushbu mualliflar dasturlash olamida hazilomuz tarzda **«Gang of Four» (GoF — To'rtlik to'dasi)** deb ataladi. Ular kitobda 23 ta klassik andozani tavsiflab berishgan bo'lib, bugungi barcha zamonaviy freymvorklar (Django, Spring, FastAPI, React) aynan shu andozalar asosida qurilgan.

### 2. Over-engineering (Ortiqcha murakkablashtirish) qopqoni

Ko'p yosh dasturchilar andozalarni o'rgangach, ularni har bir qatorda qo'llashga intilishadi:
- Oddiygina 5 qatorli skript uchun Factory, Singleton, Abstract Factory qurib tashlashadi.
- Bu holat kodni tushunishni qiyinlashtiradi va rivojlanishni sekinlashtiradi.
- **Oltin qoida:** Har doim eng oddiy va toza yechimdan (KISS) boshlang. Faqat muammo kattalashib, takrorlanish (DRY) va kengayish (OCP) ehtiyoji tug'ilgandagina andozalarni joriy qiling!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Design Pattern** | Dasturiy arxitekturadagi tipik muammolarning sinovdan o'tgan yechim andozasi |
| **Creational Patterns** | Obyektlarni xavfsiz va moslashuvchan yaratish mexanizmini boshqaruvchi andozalar |
| **Factory Method** | Obyekt yaratish interfeysini taqdim etuvchi, lekin aniq sinfni tanlashni fabrikaga topshiruvchi andoza |
| **Singleton** | Tizim bo'yicha sinfning yagona nusxasini kafolatlovchi va unga global kirish beruvchi andoza |
| **Lazy Initialization** | Obyektni dastur boshlanishida emas, faqat unga birinchi marta ehtiyoj tug'ilganda yaratish |
| **Thread-safe** | Bir vaqtning o'zida bir nechta oqimlar murojaat qilganda ham ma'lumotlarning buzilmasligi kafolati |
| **Connection Pool** | Ma'lumotlar bazasi bilan aloqa o'rnatuvchi oldindan tayyorlab qo'yilgan cheklangan ulanishlar to'plami |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- 🐍 **Python'dagi tabiiy Singleton:** Aslida Python tilida har qanday import qilinadigan modul (`import settings`) o'z-o'zidan Singleton hisoblanadi! Chunki Python modulni xotiraga bir marta yuklaydi (`sys.modules`) va keyingi barcha importlarda o'sha nusxani qaytaradi.
- ⚡ **O'yin sanoatida Singleton:** O'yin dasturlashda `AudioEngine` (ovozlar tizimi) yoki `InputManager` ko'pincha Singleton qilib yoziladi, chunki kompyuterda dinamik va klaviatura bitta bo'ladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Savollar va topshiriqlar

### 1-topshiriq <Badge type="tip" text="oson" />
Loyihalash andozalarining 3 ta asosiy toifasini sanab bering va har birining maqsadini bitta jumlada tushuntiring.

### 2-topshiriq <Badge type="tip" text="oson" />
Factory Method andozasi qanday muammoni hal qiladi? Nega har safar to'g'ridan-to'g'ri `ClassName()` deb chaqirmaslik kerak?

### 3-topshiriq <Badge type="tip" text="oson" />
Singleton andozasining asosiy vazifasi nima va nima uchun bitta dasturda 2 ta alohida Logger yaratilmasligi kerak?

### 4-topshiriq <Badge type="warning" text="o'rta" />
Python tilida `__init__` va `__new__` metodlarining farqi nimada? Singleton yaratishda nega aynan `__new__` ishlatiladi?

### 5-topshiriq <Badge type="warning" text="o'rta" />
Quyidagi kod natijasida nima chop etilishini tahlil qiling:
```python
s1 = DatabaseConnection()
s2 = DatabaseConnection()
print(s1 is s2)
```
Nega bu yerda `==` emas, `is` operatoridan foydalanish aniqroq tekshiruv hisoblanadi?

### 6-topshiriq <Badge type="warning" text="o'rta" />
Factory Method andozasi SOLID ning Open/Closed Principle (OCP) tamoyilini qanday qilib qo'llab-quvvatlashini kod misolida tushuntiring.

### 7-topshiriq <Badge type="warning" text="o'rta" />
«Over-engineering» nima? Nega barcha masalalarga ham andozalarni qo'llash tavsiya etilmaydi?

### 8-topshiriq <Badge type="danger" text="qiyin" />
Nega zamonaviy arxitekturada ko'p muhandislar Singleton andozasini «Anti-pattern» deb hisoblashadi? Uning unit-test yozishdagi 2 ta asosiy xatarini yozing.

### 9-topshiriq <Badge type="danger" text="qiyin" />
Python tilida `VehicleFactory` yarating. U kiritilgan turga qarab (`car`, `truck`, `motorcycle`) mos obyektni qaytarsin. Agar noma'lum transport turi kiritilsa, tushunarli xatolik (`ValueError`) tashlasin.

### 10-topshiriq <Badge type="danger" text="qiyin" />
Ko'p oqimli (Multi-threaded) dasturlarda 2 ta oqim bir vaqtda `Singleton()` chaqirganda ikkita alohida nusxa yaratilib ketishi xavfini (Race condition) bartaraf etish uchun qanday texnikadan (`threading.Lock`) foydalaniladi?

### 11-topshiriq <Badge type="info" text="bonus" />
Loyiha konfiguratsiyasini (`settings.json` yoki `.env`) o'quvchi va butun dastur bo'ylab faqat bitta nusxada xotirada saqlovchi `AppConfig` Singleton sinfini yozing. Uni 3 ta alohida faylda chaqirib, ma'lumotlar o'zgarmasligini tekshiring.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'z-o'zini tekshirish savollari

1. GoF kitobida nechta andoza tavsiflab berilgan?
2. Factory Method andozasida mijoz kodi obyekt yaratuvchi qaysi komponent bilan muloqot qiladi?
3. Singleton andozasida `_instance` o'zgaruvchisining vazifasi nima?
4. Nega Python modullari tabiiy ravishda Singleton xususiyatiga ega?
5. Qachon andoza ishlatmasdan oddiy funksiya bilan cheklangan ma'qul?

</div>

