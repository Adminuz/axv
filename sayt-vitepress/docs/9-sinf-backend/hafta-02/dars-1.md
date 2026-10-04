---
title: "4-dars. Pythonda operatorlar va ifodalar"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 2, "link": "/9-sinf-backend/hafta-02/"}, "g": 4, "title": "Pythonda operatorlar va ifodalar", "lead": "Dasturimiz fikrlashni boshlaydi! Ushbu darsda taqqoslash va mantiqiy operatorlar bilan tanishib, kompyuterga qiymatlarni solishtirish, rost va yolg‘onni ajratish hamda murakkab shartli ifodalar tuzishni o‘rgatamiz.", "slide": "/slaydlar/9-sinf-backend/hafta-02/dars-1.html", "tabs": [{"g": 4, "link": "/9-sinf-backend/hafta-02/dars-1", "current": true}, {"g": 5, "link": "/9-sinf-backend/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/9-sinf-backend/hafta-02/dars-3", "current": false}], "prev": null, "next": {"g": 5, "title": "Tarmoqlanuvchi algoritm: if va else operatorlari", "link": "/9-sinf-backend/hafta-02/dars-2"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Operator** — ma'lumotlar ustida amal bajaruvchi belgi (`+`, `==`, `and`). **Operand** — amal bajarilayotgan qiymat.
- **Ifoda (Expression)** — hisoblanganda muayyan natija (qiymat) qaytaruvchi kod bo‘lagi.
- Taqqoslash operatorlari (`==`, `!=`, `<`, `>`, `<=`, `>=`) har doim mantiqiy natija — `True` yoki `False` qaytaradi.
- `=` belgisi o‘zlashtirish, `==` belgisi esa taqqoslash uchun xizmat qiladi; ularni almashtirib bo‘lmaydi.
- `and` operatori barcha shartlar rost bo‘lgandagina `True` beradi; `or` operatori esa kamida bitta shart rost bo‘lsa `True` beradi.
- `not` operatori mantiqiy natijani teskarisiga aylantiradi (`not True` -> `False`).
- `in` va `not in` operatorlari biror element to‘plam yoki matn ichida bor-yo‘qligini tekshiradi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega ifodalar (expressions) muhim?
Backend tizimlarida har bir qaror ifodalar ustiga quriladi. Masalan:
- Foydalanuvchi tizimga kirishga urinmoqda: `parol_togrimi and hisob_faolmi`
- Mahsulot buyurtma qilinmoqda: `omborda_bormi and balans >= narx`
- Ruxsat berish: `rol == "admin" or rol == "moderator"`
Agar dasturchi operatorlar va ifodalarni mukammal bilmasa, tizimda xavfsizlik zaifliklari va hisob-kitob xatolari yuzaga keladi.

### Qisqa tutashuvli baholash (Short-circuit evaluation)
Python `and` va `or` ifodalarini juda tejamkorlik bilan hisoblaydi:
- `and` amali bajarilayotganda, agar birinchi shart `False` bo‘lsa, Python ikkinchi shartni hatto o‘qib ham o‘tirmaydi! Chunki natija baribir `False` bo‘lishi aniq.
- `or` amali bajarilayotganda, agar birinchi shart `True` bo‘lsa, keyingi shartlarni tekshirish to‘xtatiladi, chunki natija baribir `True` bo‘ladi.
Bu xususiyat backendda keraksiz og‘ir operatsiyalarni bajarmaslik uchun juda asqotadi.

### Matnlarni taqqoslash: Alifbo tartibi
Pythonda matnlar ham taqqoslash operatorlari bilan solishtirilishi mumkin (`"olma" < "shaftoli"`). Bu solishtirish harflarning ASCII/Unicode jadvalidagi o‘rniga qarab amalga oshiriladi (alifbo bo‘yicha oldin keladigan so‘z kichik hisoblanadi). E'tibor bering, barcha katta harflar (`"A"`) kichik harflardan (`"a"`) oldin turadi, shuning uchun `"B" < "a"` ifodasi `True` qaytaradi!

### Odatiy xatolar
- Taqqoslash o‘rniga o‘zlashtirish qo‘yish: `if x = 5` — bu jiddiy sintaksis xatosi (`SyntaxError`). To‘g‘risi: `x == 5`.
- String ichida raqamni solishtirish: `"10" > "2"` kodi `False` qaytaradi! Chunki bu yerda sonlar emas, matnlar solishtiriladi va birinchi belgi `"1"` belgisi `"2"` dan kichik. Sonlarni solishtirishdan avval ularni `int()` toifasiga o‘tkazish kerak.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Ifoda (Expression) | Natija qaytaruvchi kod yozuvi (`5 + 3`, `x > 10`) |
| Operator | Amal bajaruvchi belgi (`+`, `-`, `==`, `and`) |
| Operand | Operator qaysi qiymatlar ustida ishlayotgan bo‘lsa, o‘sha qiymatlar |
| Taqqoslash operatori | Qiymatlarni solishtirib bool qaytaruvchi operator (`==`, `!=`, `<`, `>`) |
| Mantiqiy operator | Shartlarni bog‘lovchi operatorlar (`and`, `or`, `not`) |
| A'zolik operatori | Elementning to‘plam ichida mavjudligini tekshiruvchi (`in`, `not in`) |
| Short-circuit | Shartning birinchi qismiga qarab tezkor xulosa chiqarish usuli |
| len() | Matn yoki to‘plam uzunligini qaytaruvchi funksiya |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Pythonda zanjirli taqqoslash mumkin: `10 < x < 20` deb yozish boshqa tillardagi `10 < x and x < 20` bilan bir xil va juda chiroyli o‘qiladi!
- Boolean toifasidagi `True` son sifatida `1` ga, `False` esa `0` ga teng hisoblanadi. Masalan, `True + True` amali `2` qaytaradi!
- `in` operatori backendda qidiruv, filtrlash va foydalanuvchi huquqlarini tekshirishda eng ko‘p qo‘llaniladigan kalit so‘zlardan biridir.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Oddiy taqqoslashlar <Badge type="tip" text="oson" />
`x = 18` va `y = 25` o‘zgaruvchilarini yarating. `x < y`, `x == y`, `x != y` ifodalarining natijalarini konsolga chiqaring.
**Kutiladigan natija:**
```text
x < y: True
x == y: False
x != y: True
```

### 2. Imtihon tekshiruvi <Badge type="tip" text="oson" />
O‘quvchining bali `ball = 82` ga teng. Agar ball 60 dan katta yoki teng bo‘lsa `True` chiqaruvchi `imtihon_otdi` nomli mantiqiy ifoda yozing.
**Kutiladigan natija:** `Imtihondan o'tdi: True`

### 3. Matn ichidan qidiruv (in) <Badge type="tip" text="oson" />
`matn = "Advanced Python Backend va DevOps kursi"` berilgan. Matn ichida `"Backend"` so‘zi bor-yo‘qligini `in` orqali tekshirib konsolga chiqaring.
**Kutiladigan natija:** `Backend so'zi bormi: True`

### 4. not operatori <Badge type="tip" text="oson" />
`yomgir = True` bo‘lsa, `not yomgir` nima natija berishini ekranga chiqaring va ma'nosini tushuntiring.
**Kutiladigan natija:** `Yomg'ir yo'qmi: False`

### 5. Yosh oralig‘i tekshiruvi <Badge type="warning" text="o'rta" />
`yosh = 15`. O‘quvchi maktab yoshidami yoki yo‘qligini aniqlash uchun `yosh >= 7 and yosh <= 18` mantiqiy ifodasini tuzing va natijani ekranga chiqaring.
**Kutiladigan natija:** `Maktab yoshidami: True`

### 6. Do‘kon chegirma sharti <Badge type="warning" text="o'rta" />
Do‘konda xarid summasi `summa = 120000` so‘m yoki mijoz maxsus kartaga ega (`karta_bormi = True`). Chegirma olish uchun `summa >= 100000 or karta_bormi` ifodasini yozing va natijani ko‘ring.
**Kutiladigan natija:** `Chegirma beriladimi: True`

### 7. Taqiqlangan so‘z tekshiruvi <Badge type="warning" text="o'rta" />
Izoh matni berilgan: `izoh = "Ushbu mahsulot juda sifatsiz va yomon ekan"`. Izohda `"spam"` so‘zi yo‘qligini `not in` operatori yordamida tekshiring.
**Kutiladigan natija:** `Izoh toza (spam yo'q): True`

### 8. Juft son ekanligini taqqoslash <Badge type="warning" text="o'rta" />
Sonning juftligini aniqlash uchun qoldiq operatori va taqqoslash birga ishlatiladi: `son % 2 == 0`. `44` va `59` sonlarini juftlikka tekshiruvchi kod yozing.
**Kutiladigan natija:**
```text
44 juftmi: True
59 juftmi: False
```

### 9. Xavfsiz tizimga kirish <Badge type="danger" text="qiyin" />
Tizimga kirish uchun quyidagi shartlar bir vaqtda bajarilishi kerak:
- `login == "admin"`
- `parol == "secret123"`
- `faol == True`
Uchala parametrni e'lon qiling va foydalanuvchiga ruxsat berilganligini bitta mantiqiy ifoda bilan tekshiring.
**Kutiladigan natija:** `Kirishga ruxsat: True`

### 10. Zanjirli taqqoslash <Badge type="danger" text="qiyin" />
Harorat `t = 24` daraja. Harorat xona harorati oralig‘ida (`18 <= t <= 26`) ekanligini Pythondagi zanjirli taqqoslash sintaksisi orqali tekshirib konsolga chiqaring.
**Kutiladigan natija:** `Harorat qulay: True`

### 11. Murakkab kirish tekshiruvi (IP va Rol) <Badge type="info" text="bonus" />
Serverga so‘rov keldi:
`mijoz_ip = "192.168.1.10"`
`admin_ip_list = ["192.168.1.1", "192.168.1.10", "192.168.1.25"]`
`soat = 14`
Foydalanuvchining IP manzili ruxsat etilganlar ro‘yxatida bo‘lsa (`in`) VA ish vaqti (`9 <= soat <= 18`) bo‘lsa, tizimga kirishga ruxsat beruvchi mukammal ifoda tuzing.
**Kutiladigan natija:** `Serverga kirish ruxsati: True`

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Operator va operand tushunchalarini misol bilan tushuntiring.
2. Nega `5 == "5"` ifodasi `False` natija beradi?
3. `and` va `or` mantiqiy operatorlarining asosiy farqi nimada?
4. Qisqa tutashuvli baholash (short-circuit) qanday ishlaydi?
5. `in` operatori qanday vaziyatlarda qo‘llaniladi?
6. Nega `if x = 10` deb yozish xatolik keltirib chiqaradi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. `shartlar.py` faylini oching.
2. Foydalanuvchining balli `78` deb olinsa, uning 4 baho olish shartini (`ball >= 71 and ball < 86`) ifodalang.
3. Berilgan `email = "student@horizon.uz"` matnida `"@"` va `".uz"` belgilari mavjudligini tekshiruvchi dastur tuzing.
4. Foydalanuvchi kiritgan son 3 ga ham, 5 ga ham karrali (qoldiqsiz bo‘linishini) tekshiruvchi ifoda yozing.

</div>

