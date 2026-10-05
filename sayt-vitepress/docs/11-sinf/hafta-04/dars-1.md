---
title: "10-dars. Loyihalash andozalari: Observer va hodisalar arxitekturasi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 4, "link": "/11-sinf/hafta-04/"}, "g": 10, "title": "Loyihalash andozalari: Observer va hodisalar arxitekturasi", "lead": "Bitta voqea, ko'p javob beruvchi: Observer yordamida «buyurtma yakunlandi» signalini kuzatuvchilarga tarqatamiz va kod bir-biriga bog'lanib qolishining oldini olamiz.", "slide": "/slaydlar/11-sinf/hafta-04/dars-1.html", "test": null, "tabs": [{"g": 10, "link": "/11-sinf/hafta-04/dars-1", "current": true}, {"g": 11, "link": "/11-sinf/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/11-sinf/hafta-04/dars-3", "current": false}], "prev": null, "next": {"g": 11, "title": "REST API va JSON asoslari: REST tamoyillari va HTTP", "link": "/11-sinf/hafta-04/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Muammo:** bitta voqea (masalan, buyurtma yakunlandi) bir nechta mustaqil ishni ishga tushiradi: email, analitika, ball hisoblash. Hammasini `OrderService` ichiga yozsak, qattiq bog'liqlik paydo bo'ladi.
- **Observer** — «publish/subscribe» modelida hodisani kuzatuvchilarga tarqatuvchi xulq-atvor (Behavioral) andozasi.
- **Rollar:** Subject (Publisher) hodisani e'lon qiladi; Observer (Subscriber) javob beradi.
- **Asosiy g'oya:** Subject kuzatuvchilar kimligini bilmaydi, shuning uchun yangi kuzatuvchi qo'shish Subject kodini o'zgartirmaydi (bo'sh bog'liqlik, loose coupling).
- **EventBus:** hodisa nomi bilan ishlaydigan umumiy «shina» (`on`, `off`, `emit`).
- **Event-driven dizayn:** g'oya yirik tizimda navbatlar (message queue) va event bus orqali asinxron hamkorlikka aylanadi.
- **Xavflar:** xotira oqimi (unsubscribe unutilsa), notifikatsiya tartibi, takroriy hodisa (idempotentlik), yutib yuborilgan xato, Observer storm.
- **Sinash:** soxta (mock) kuzatuvchi ulab, metod chaqirilganini tekshiramiz.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Telegram kanali o'xshatishi

Kanal egasi postni bir marta yuboradi. U obunachilarni tanimaydi: kim xohlasa obuna bo'ladi, kim xohlasa chiqib ketadi. Post yuborilganda kanal egasi hech qaysi obunachining telefoniga «ulanib» chiqmaydi. Observer'da ham shunday: Subject faqat «hodisa sodir bo'ldi» deydi.

### 2. Nega `list(self._listeners)` deb nusxa olinadi?

```python
for listener in list(self._listeners):
    listener.on_order_completed(order_id)
```

Agar kuzatuvchi hodisa paytida o'zini ro'yxatdan o'chirsa, asl ro'yxat aylanish vaqtida o'zgaradi va tartib buziladi. Nusxa ustida aylansak, bu muammo yo'q.

### 3. Nega `try/except` kerak, lekin «yutib yuborish» yomon?

Bitta kuzatuvchi (masalan, SMTP ishlamayapti) yiqilsa, qolganlari ham to'xtab qolmasligi kerak. Shuning uchun har chaqiruv `try/except` ichida. Lekin xatoni jimgina tashlab yuborish ham yomon: kamida logga yozing (`print`, keyinroq `logging`). Aks holda muammoni hech kim bilmaydi.

### 4. Xotira oqimi qanday ko'rinadi?

`subscribe` qilingan obyektga Subject havola ushlab turadi. `unsubscribe` qilinmasa, siz obyektdan voz kechgan bo'lsangiz ham, u xotirada qoladi va hodisalarni olishda davom etadi. Yechim: `unsubscribe`/`detach` yoki weak reference (zaif havola).

### 5. Qachon Observer ortiqcha?

Bitta aniq harakat, bitta qabul qiluvchi, 5 qatorli skript bo'lsa, oddiy funksiya chaqirish yetarli. Har yerga andoza qo'yish over-engineering.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Observer** | Hodisani kuzatuvchilarga tarqatish andozasi (publish/subscribe) |
| **Subject / Publisher** | Hodisani e'lon qiluvchi manba; kuzatuvchilar ro'yxatini saqlaydi |
| **Observer / Subscriber** | Hodisaga javob beruvchi kuzatuvchi |
| **subscribe / unsubscribe** | Kuzatuvchini ulash / uzish |
| **Loose coupling** | Bo'sh bog'liqlik: komponentlar bir-birining ichki tuzilishini bilmaydi |
| **Event (hodisa)** | Tizimda yuz bergan voqea haqidagi xabar, masalan `order_completed` |
| **Event bus** | Hodisalarni nomi bo'yicha tarqatuvchi umumiy shina |
| **Message queue** | Xabarlar navbati: hodisalarni saqlab, iste'molchiga yetkazadi |
| **Idempotentlik** | Bir hodisa ikki marta kelsa ham natija bir marta bajarilgandek bo'lishi |
| **Mock / stub** | Testda haqiqiy obyekt o'rniga qo'yiladigan soxta obyekt |
| **Backpressure** | Iste'molchi sekin, ishlab chiqaruvchi tez bo'lganda navbat to'lib borishi |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Observer klassik GoF (Gang of Four) kitobidagi 23 ta andozadan biri bo'lib, Behavioral (xulq-atvor) toifasiga kiradi.
- Telegram, Instagram kabi ilovalardagi bildirishnomalar (push) mohiyatan publish/subscribe g'oyasiga yaqin: manba bir marta e'lon qiladi, obuna bo'lganlar oladi.
- Kafka kabi tizimlarda hodisalar tartibi faqat bitta partition ichida kafolatlanadi (o'quv qo'llanmasida eslatilgan).
- Veb-brauzerdagi tugma bosish hodisalari (`addEventListener`) ham kundalik hayotdagi Observer namunasi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Rollarni toping <Badge type="tip" text="oson" />
Telegram kanalida kim Subject, kim Observer? «Obuna bo'lish» va «obunani bekor qilish» Observer'dagi qaysi metodlarga mos keladi?

**Kutiladigan natija:** rollar va ikki metod nomi (`subscribe`, `unsubscribe`).

### 2. Qattiq bog'liqlikni aniqlash <Badge type="tip" text="oson" />
Mana bu kodda qaysi satrlar `OrderService` ni boshqa ishlarga bog'lab qo'ygan? Yangi talab («ball hisoblash») qo'shilsa nima o'zgaradi?

```python
def complete_order(self, order_id):
    send_email(order_id)
    track_analytics(order_id)
```

**Kutiladigan natija:** ikki chaqiruv ko'rsatiladi; yangi talab uchun `OrderService` ni o'zgartirish kerakligi (OCP buzilishi) tushuntiriladi.

### 3. Bashorat qiling <Badge type="tip" text="oson" />
Observer misolida `email` ni `unsubscribe` qilib, ikkinchi buyurtmani bajarsak, terminalda nechta qator chiqadi va qaysilar?

**Kutiladigan natija:** oldindan yozilgan taxmin, so'ng kod bilan tekshiruv.

### 4. Hodisa nomi ixtiyoriy emas <Badge type="tip" text="oson" />
Kutubxona loyihangiz uchun 3 ta hodisa nomini o'ylab toping (masalan, `book:borrowed`). Har biriga ma'lumot (payload) tarkibini yozing.

**Kutiladigan natija:** 3 ta nom + har birining payload maydonlari.

### 5. Birinchi Observer <Badge type="warning" text="o'rta" />
`OrderService`, `EmailNotifier`, `AnalyticsTracker` ni yozing. `subscribe`, `unsubscribe` va `complete_order` metodlari bo'lsin. Ikkita buyurtmani bajaring, o'rtada bitta kuzatuvchini uzing.

**Kutiladigan natija:** ishlaydigan fayl va chiqish.

### 6. Yiqilgan kuzatuvchi <Badge type="warning" text="o'rta" />
`BrokenListener` yarating (ichida `raise RuntimeError`). Uni ikki sog'lom kuzatuvchi o'rtasiga ulang. `try/except` bilan va usiz natijani solishtiring.

**Kutiladigan natija:** qaysi holatda nechta kuzatuvchi ishlagani haqida yozma xulosa.

### 7. Python EventBus <Badge type="warning" text="o'rta" />
`EventBus` sinfini `on`, `off`, `emit` metodlari bilan yozing. `book:borrowed` hodisasiga ikkita handler ulang.

**Kutiladigan natija:** bitta `emit` ikkala handler'ni ishga tushiradi.

### 8. Mock bilan test <Badge type="warning" text="o'rta" />
Soxta kuzatuvchi sifatida oddiy ro'yxatning `append` metodidan foydalanib, `emit` dan keyin handler chaqirilganini `assert` bilan tasdiqlang.

**Kutiladigan natija:** ishlaydigan `assert` test.

### 9. Idempotent hisoblagich <Badge type="danger" text="qiyin" />
`book:borrowed` hodisalarini kitob bo'yicha sanaydigan `StatsCounter` yozing. Bir xil `event_id` ikki marta kelsa, ikkinchisini e'tiborsiz qoldirsin.

**Kutiladigan natija:** bir `event_id` ikki marta yuborilganda statistika 1 bo'ladi.

### 10. Kutubxona hodisalari <Badge type="danger" text="qiyin" />
`library-api/events.py` da `LibraryService.borrow(book_id, reader)` yozing: kitob band bo'lsa `ValueError`, muvaffaqiyatda `book:borrowed` e'lon qilinsin. Ikki kuzatuvchi ulang: `SmsNotifier` va `StatsCounter`.

**Kutiladigan natija:** o'z GitHub portfolio repoyingizda `library-api/events.py` va qisqa README izohi.

### 11. Qachon ishlatmaslik kerak? <Badge type="danger" text="qiyin" />
Quyidagi 3 vaziyatdan qaysilarida Observer kerak, qaysilarida ortiqcha? Har biriga 1–2 jumlali asos yozing: (a) 5 qatorli skript, hisobotni faylga yozadi; (b) bitta hodisaga email, SMS va analitika javob beradi; (c) tugma bosilganda bitta funksiya chaqirilishi kerak.

**Kutiladigan natija:** uchta qaror va asoslar.

### 12. Weak reference tadqiqoti <Badge type="info" text="bonus" />
`weakref.WeakSet` yordamida kuzatuvchilarni saqlaydigan Subject yozing. Kuzatuvchiga barcha havolalarni o'chirgach (`del`), ro'yxat o'z-o'zidan qisqarishini ko'rsating.

**Kutiladigan natija:** `notify` oldin 1, keyin 0 qaytaradi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Observer andozasida Subject va Observer nima qiladi?
2. Subject nega kuzatuvchilar kimligini bilmasligi kerak?
3. Qaysi holatda xotira oqimi paydo bo'ladi?
4. Bitta kuzatuvchi yiqilsa, qolganlari ishlashi uchun nima qilinadi?
5. Sinxron Observer va asinxron pub/sub (navbat, event bus) farqi nimada?
6. Idempotentlik nega kerak?
7. Observer storm nima?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

`library-api/events.py` ni yakunlang: `EventBus`, `LibraryService.borrow`, ikki kuzatuvchi va kamida 2 ta `assert` test. GitHub portfolio repoyingizga `feat(events)` commit va Pull Request bilan yuboring (20–30 daqiqa). To'liq shartlar `uyga-vazifa.md` da.

</div>

