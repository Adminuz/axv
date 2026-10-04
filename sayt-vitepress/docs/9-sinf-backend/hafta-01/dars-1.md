---
title: "1-dars. Python: o‘rnatish, muhit sozlash va ilk dastur"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 1, "link": "/9-sinf-backend/hafta-01/"}, "g": 1, "title": "Python: o‘rnatish, muhit sozlash va ilk dastur", "lead": "Serverlar olamiga xush kelibsiz! Ushbu darsda zamonaviy IT sanoatining eng qudratli tili bo‘lgan Python interpretatorini o‘rnatamiz, terminal bilan do‘stlashamiz va ilk dasturimizni ishga tushiramiz.", "slide": "/slaydlar/9-sinf-backend/hafta-01/dars-1.html", "tabs": [{"g": 1, "link": "/9-sinf-backend/hafta-01/dars-1", "current": true}, {"g": 2, "link": "/9-sinf-backend/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/9-sinf-backend/hafta-01/dars-3", "current": false}], "prev": null, "next": {"g": 2, "title": "Sodda ma’lumot toifalari va arifmetik amallar", "link": "/9-sinf-backend/hafta-01/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Python** — sodda sintaksisga ega, o‘qilishi oson va backend, DevOps, sun'iy intellektda yetakchi dasturlash tili.
- **Interpretator** — biz yozgan Python kodini kompyuter tushunadigan mashina tiliga o‘girib, qatorma-qator bajaruvchi maxsus dastur.
- O‘rnatish paytida **"Add python.exe to PATH"** katagini belgilash shart, aks holda tizim terminalda `python` buyrug‘ini topa olmaydi.
- O‘rnatilgan versiyani tekshirish uchun terminalda `python --version` buyrug‘i beriladi.
- Terminalda `python` deb yozilganda interaktiv rejim (**REPL**) ochiladi va `>>>` belgisi chiqadi.
- Ilk dasturimiz `print("Hello, World!")` funksiyasi orqali matnni ekranga chiqaradi.
- Katta dasturlar faylda saqlanadi va ularning kengaytmasi `.py` bo‘ladi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega aynan Python va backend?
Backend — bu foydalanuvchi ko‘rmaydigan, ammo sayt yoki ilovaning barcha mantiqiy jarayonlari, xavfsizligi va ma'lumotlar bazasi boshqariladigan server qismidir. Masalan, Telegramda xabar yozganingizda uni qabul qilish, do‘stingizga yetkazish, bazada saqlash va botlarni ishlatish backend hisoblanadi. Python tili o‘zining tezkorligi, qulayligi va ulkan ekotizimi tufayli backend va DevOps sohasida dunyodagi birinchi raqamli tanlovlardan biridir.

### PATH o‘zi nima va u nega muhim?
Tasavvur qiling, siz katta kutubxonadasiz. Agar kitoblar ro‘yxati (katalog) bo‘lmasa, kerakli kitobni topish uchun har bir xonani birma-bir ko‘rib chiqishingiz kerak bo‘ladi. Operatsion tizimdagi **PATH** tizim o‘zgaruvchisi ham xuddi shunday katalogdir. Siz terminalda biror buyruq yozganingizda (masalan, `python`), operatsion tizim uni aynan PATH ro‘yxatida ko‘rsatilgan papkalardan qidiradi. Agar o‘rnatishda "Add to PATH" belgilanmasa, kompyuter Python qayerda joylashganini bilmay qoladi.

### Interaktiv rejim (REPL) vs Kod muharriri
Python ikki xil usulda ishlaydi:
1. **Interaktiv rejim (REPL - Read-Eval-Print Loop):** Terminalda `python` deb kiritsangiz ochiladi. Har bir qator yozilishi bilan darhol natija beradi. Tezkor hisob-kitoblar va yangi buyruqlarni sinab ko‘rish uchun juda qulay.
2. **Skript (fayl) rejimi:** Kod `main.py` kabi faylga yoziladi va `python main.py` orqali ishga tushiriladi. Barcha professional loyihalar aynan shu usulda yoziladi.

### Odatiy xatolar
- `Print("Salom")` — Python katta va kichik harflarni farqlaydi (case-sensitive). Funksiya nomi kichik harflar bilan `print()` bo‘lishi kerak.
- `print(Salom)` — Matnlar albatta qo‘shtirnoq yoki birtirnoq ichida bo‘lishi lozim: `print("Salom")`. Aks holda `NameError` yuzaga keladi.
- Qo‘shtirnoqni yopishni unutish: `print("Salom)` — bu `SyntaxError` (EOL while scanning string literal) xatosiga olib keladi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Python | Yuqori darajadagi, interpretatsiya qilinadigan dasturlash tili |
| Interpretator | Kodni qatorma-qator o‘qib, bajaruvchi dastur |
| Terminal / CMD | Matnli buyruqlar kiritiladigan operatsion tizim oynasi |
| PATH | Operatsion tizim bajariluvchi dasturlarni qidiradigan manzillar ro‘yxati |
| REPL | Interaktiv muhit (Read-Eval-Print Loop — O‘qish, Bajarish, Chiqarish) |
| print() | Ekranga yoki konsolga ma'lumot chiqaruvchi standart Python funksiyasi |
| .py | Python dasturiy kodi saqlanadigan fayl kengaytmasi |
| Case-sensitive | Katta va kichik harflarni qat'iy farqlovchi xususiyat |
| Backend | Veb-ilova va serverlarning foydalanuvchiga ko‘rinmaydigan mantiqiy qismi |
| DevOps | Dastur yaratish va uni serverlarga joylashtirishni avtomatlashtirish sohasi |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Python dasturlash tili 1991-yilda gollandiyalik dasturchi Gvido van Rossum (Guido van Rossum) tomonidan yaratilgan.
- Tilning nomi ilon (piton) sharafiga emas, balki britaniyalik mashhur komik guruh "Monty Python" sharafiga qo‘yilgan!
- NASA, Google, Netflix, Spotify va Instagram kabi gigant kompaniyalarning server infratuzilmasi asosan Python tilida ishlaydi.
- Python shiori — "Soddalik murakkablikdan afzaldir" (The Zen of Python). Buni terminalda `import this` deb yozib o‘qishingiz mumkin.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Python versiyasi <Badge type="tip" text="oson" />
Kompyuteringizda terminalni oching va Python interpretatori o‘rnatilganligini tekshiring. Qaysi versiya o‘rnatilganini aniqlang.
**Kutiladigan natija:** Ekranda `Python 3.x.x` ko‘rinishida xabar chiqishi.

### 2. Interaktiv salom <Badge type="tip" text="oson" />
Terminalda `python` buyrug‘i orqali REPL muhitiga kiring va o‘zingizning birinchi salomlashuv xabaringizni konsolga chiqaring.
**Kutiladigan natija:** `>>>` belgisidan so‘ng yozilgan `print(...)` ekranga siz yozgan matnni chiqarishi kerak.

### 3. Ikki qatorli xabar <Badge type="tip" text="oson" />
`xabar.py` faylini yarating. Dastur ishga tushganda birinchi qatorda sevimli kitobingiz nomini, ikkinchi qatorda esa uning muallifini chiqarsin.
**Kutiladigan natija:**
```text
Kitob: O'tkan kunlar
Muallif: Abdulla Qodiriy
```

### 4. Ism va familiya <Badge type="tip" text="oson" />
Bitta `print()` funksiyasi ichida vergul bilan ajratgan holda ismingiz va familiyangizni chiqaring.
**Kutiladigan natija:** Ism va familiyangiz o‘rtasida bo‘sh joy bilan bitta qatorda chiqishi.

### 5. Ko'p qatorli matn <Badge type="warning" text="o'rta" />
Python'da uchta qo‘shtirnoq (`""" ... """`) yordamida bir nechta satrdan iborat she'r yoki dasturchi qoidasini bitta `print()` orqali ekranga chiqaring.
**Kutiladigan natija:** Matn aynan kodda yozilganidek bir necha qatorda konsolga chiqishi.

### 6. Xatoni toping <Badge type="warning" text="o'rta" />
Quyidagi kod berilgan:
```python
Print("Salom, dasturchi!)
```
Bu kodda qanday 2 ta xato borligini toping va uni to‘g‘rilab ishga tushiring.
**Kutiladigan natija:** Kod xatosiz bajarilib, `Salom, dasturchi!` yozuvini chiqarishi kerak.

### 7. Ajratuvchi belgi (sep) <Badge type="warning" text="o'rta" />
`sep=" - "` parametridan foydalanib, hafta kunlaridan uchtasini (Dushanba, Seshanba, Chorshanba) chiziqcha bilan ajratilgan holda chiqaring.
**Kutiladigan natija:** `Dushanba - Seshanba - Chorshanba`

### 8. Qator oxiri (end) <Badge type="warning" text="o'rta" />
Ikkita alohida `print()` funksiyasidan foydalaning, ammo `end=" "` parametri yordamida ikkala xabarni ham bitta qatorda birlashtiring.
**Kutiladigan natija:** Ikkala xabar bitta qatorda konsolda ko‘rinishi kerak.

### 9. Server status paneli <Badge type="danger" text="qiyin" />
`status.py` nomli fayl yarating. U konsolda quyidagi ko‘rinishdagi chiroyli server holati panelini chiqarsin:
```text
========================================
[SERVER LOG] Ishga tushirildi: Port 8000
[STATUS] Aloqa: A'lo darajada
========================================
```
**Kutiladigan natija:** Ko‘rsatilgan formatdagi toza log ekranda hosil bo‘lishi.

### 10. Zen of Python tadqiqoti <Badge type="danger" text="qiyin" />
Terminalda interaktiv rejimni oching va `import this` buyrug‘ini kiriting. Chiqqan falsafiy qoidalardan kamida bittasini daftaringizga ko‘chirib oling va ma'nosini tushuntiring.
**Kutiladigan natija:** Terminalda Tim Peters tomonidan yozilgan 19 ta qoida ekranga chiqishi.

### 11. Badiiy konsol rasmi (ASCII Art) <Badge type="info" text="bonus" />
Yulduzchalar (`*`), chiziqchalar (`|`, `-`) va bo‘sh joylar yordamida konsolda server yoki kompyuter monitorining rasmini (ASCII art) chizuvchi dastur tuzing.
**Kutiladigan natija:** Konsolda chiroyli monitor yoki server ramkasi rasmi chiqishi.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Python interpretatori nima va u kompilyatordan nimasi bilan farq qiladi?
2. Nega Windows operatsion tizimida Python o‘rnatayotganda "Add to PATH" katagi muhim hisoblanadi?
3. O‘rnatilgan Python versiyasini terminalda qanday buyruq bilan tekshiramiz?
4. Interaktiv rejimdan (REPL) qanday qilib chiqish mumkin?
5. `print()` funksiyasida `sep` va `end` parametrlari nima vazifani bajaradi?
6. Nega `print(Hello)` deb yozsak xatolik yuz beradi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Shaxsiy kompyuteringizga Python 3.12+ va VS Code muharririni o‘rnating.
2. `salom.py` faylini yarating va unda o‘zingiz, qiziqishlaringiz va ushbu kursdan kutilmalaringiz haqida 5 qatorli ma'lumot yozing.
3. Terminal orqali dasturni ishga tushirib, natijani tekshiring.

</div>

