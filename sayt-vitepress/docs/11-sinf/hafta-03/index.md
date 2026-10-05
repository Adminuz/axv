---
title: "3-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "n": 3, "bob": "I-bob · Dasturiy ta'minot ishlab chiqish asoslari", "lessons": [{"g": 7, "title": "Clean Code asoslari va SOLID: SRP hamda OCP tamoyillari", "lead": "Professional kod madaniyati, to'g'ri nomlash, DRY/KISS/YAGNI tamoyillari hamda barqaror arxitektura poydevori: SRP va OCP.", "link": "/11-sinf/hafta-03/dars-1", "slide": "/slaydlar/11-sinf/hafta-03/dars-1.html", "test": "/slaydlar/11-sinf/hafta-03/dars-1-test.html"}, {"g": 8, "title": "SOLID chuqurlashtirilgan: LSP, ISP, DIP va Code Smells refaktoringi", "lead": "Liskov almashinish qoidasi, ixcham interfeyslar, Dependency Injection kuchi va yomon arxitektura alomatlarini (Code Smells) davolash.", "link": "/11-sinf/hafta-03/dars-2", "slide": "/slaydlar/11-sinf/hafta-03/dars-2.html", "test": "/slaydlar/11-sinf/hafta-03/dars-2-test.html"}, {"g": 9, "title": "Loyihalash andozalari: Factory va Singleton arxitekturasi", "lead": "Creational patterns: Factory Method yordamida obyekt yaratishni markazlashtirish, Singleton kuchi va global holat xatarlari.", "link": "/11-sinf/hafta-03/dars-3", "slide": "/slaydlar/11-sinf/hafta-03/dars-3.html", "test": "/slaydlar/11-sinf/hafta-03/dars-3-test.html"}], "test": "/slaydlar/11-sinf/hafta-03/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Har bir vazifa 20–30 daqiqa. Parol, shaxsiy token, maxfiy kalit va shaxsiy ma'lumotlarni repozitoriyga yozmang: topshirishda faqat ochiq GitHub repo yoki Pull Request havolasi kerak.

### 7-dars uchun (Clean Code, SRP va OCP)
**1-topshiriq: «Kodni tozalash va OCP kengaytirish»**
1. O'z GitHub portfolio repozitoriyangizda yangi `refactor/clean-code` tarmog'ini oching.
2. `order_processor.py` nomli fayl yarating. Unga kamida 30 qatordan iborat «Spaghetti» kod (hisoblash, chegirma, soliq, xabar jo'natish bitta funksiyada) yozing.
3. Ushbu kodni Clean Code qoidalari asosida tozalang:
   - Funksiyalarni bo'ling (`Extract Method`);
   - Mas'uliyatlarni alohida sinflarga ajrating (`SRP`);
   - `PaymentProcessor` abstrakt sinfi (`abc.ABC`) orqali to'lov turlarini OCP talablariga moslang.
4. O'zgarishlarni semantik commitlar (`refactor(core): apply SRP and OCP to order processor`) bilan saqlab, GitHub'ga push qiling.

**Kutiladigan natija:** tushunarli nomlangan, SRP va OCP tamoyillariga javob beradigan toza Python moduli.  
**Topshirish:** GitHub commit yoki fayl havolasi.

---

### 8-dars uchun (LSP, ISP, DIP va Unit Test)
**2-topshiriq: «Dependency Injection va Bazasiz Unit Test»**
1. `service_architecture.py` faylida `UserRepository` abstrakt interfeysini e'lon qiling (`get_user(id)`, `save_user(user)`).
2. Ushbu interfeysga tayanuvchi `UserService` biznes mantiq sinfini yozing (Dependency Injection orqali repositoriyani qabul qilsin).
3. Testlar uchun xotirada ishlovchi `FakeUserRepository` (oddiy Python `dict` orqali) sinfini yozing.
4. `test_user_service.py` faylida hech qanday PostgreSQL yoki tashqi serverga ulanmasdan `pytest` yoki oddiy `assert` orqali 3 ta test yozing (foydalanuvchi topilishi, yangi foydalanuvchi qo'shilishi, topilmaganda xatolik).

**Kutiladigan natija:** DIP va DI tufayli 100% mustaqil, 0.01 soniyada yashil o'tuvchi unit-testlar to'plami.  
**Topshirish:** GitHub tarmog'i va testlarning terminaldagi muvaffaqiyatli skrinshoti.

---

### 9-dars uchun (Factory va Singleton andozalari)
**3-topshiriq: «Loyiha ConfigManager Singleton va Logger»**
1. `patterns.py` faylida `__new__` metodi yordamida `AppConfig` nomli Singleton sinfini tuzing. U dastur sozlamalarini (masalan: `APP_NAME`, `DEBUG`, `PORT`) faqat bir marta xotiraga yuklasin.
2. Ikkita alohida joyda `cfg1 = AppConfig()` va `cfg2 = AppConfig()` deb chaqirib, `cfg1 is cfg2` natijasi `True` ekanini `assert` bilan tasdiqlang.
3. Xabarnomalar tizimi uchun `NotificationFactory` yarating (`email`, `sms`, `telegram` turlari bo'yicha mos obyektlarni qaytarsin). Noma'lum tur kiritilganda `ValueError` tashlashini ta'minlang.
4. Hammasini `main` tarmog'iga Pull Request qilib yuboring.

**Kutiladigan natija:** Singleton va Factory andozalari to'g'ri tatbiq etilgan, to'liq testlangan Python kodi.  
**Topshirish:** GitHub Pull Request havolasi.

---

</div>
