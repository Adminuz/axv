---
title: "8-dars. Shartli takrorlanish: while sikli va boshqaruv operatorlari"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 3, "link": "/9-sinf-backend/hafta-03/"}, "g": 8, "title": "Shartli takrorlanish: while sikli va boshqaruv operatorlari", "lead": "Dastur siz aytgan shart bajarilmaguncha tinimsiz ishlaydi! Ushbu darsda shartli takrorlanuvchi while sikli, cheksiz sikllardan himoyalanish hamda siklni muddatidan oldin to‘xtatuvchi break va keyingi qadamga o‘tkazuvchi continue operatorlarini o‘rganamiz.", "slide": "/slaydlar/9-sinf-backend/hafta-03/dars-2.html", "test": "/slaydlar/9-sinf-backend/hafta-03/dars-2-test.html", "tabs": [{"g": 7, "link": "/9-sinf-backend/hafta-03/dars-1", "current": false}, {"g": 8, "link": "/9-sinf-backend/hafta-03/dars-2", "current": true}, {"g": 9, "link": "/9-sinf-backend/hafta-03/dars-3", "current": false}], "prev": {"g": 7, "title": "Takrorlanuvchi algoritm va for sikli", "link": "/9-sinf-backend/hafta-03/dars-1"}, "next": {"g": 9, "title": "Tanlash operatori: match / case va amaliy topshiriqlar", "link": "/9-sinf-backend/hafta-03/dars-3"}}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **`while` sikli** — berilgan shart rost (`True`) bo‘lib turgan vaqt davomida amallarni takrorlayveradi va shart yolg‘on (`False`) bo‘lishi bilan to‘xtaydi.
- `for` siklidan farqli o‘laroq, `while` takrorlanishlar soni oldindan aniq bo‘lmaganda (masalan, foydalanuvchi to‘g‘ri parol kiritguncha) ishlatiladi.
- Agar sikl ichidagi hisoblagich qiymati o‘zgartirilmasa (`i += 1`), dastur **cheksiz siklga** tushib qoladi.
- Cheksiz siklni to‘xtatish uchun terminalda `Ctrl + C` tugmalari bosiladi.
- **`break`** operatori siklni zudlik bilan to‘xtatadi va undan butunlay olib chiqadi.
- **`continue`** operatori siklning joriy qadamidagi qolgan amallarni tashlab, navbatdagi aylanishga o‘tadi.
- Rasmiy qo‘llanmadagi parolni 3 ta urinishda tekshirish masalasi `while`, `if` va `break` kombinatsiyasining klassik namunasidir.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega serverlar cheksiz siklda ishlaydi?
Backend va tarmoq texnologiyalarida veb-serverlar (FastAPI, Nginx, Node.js) mohiyatan **boshqariladigan cheksiz sikl** (`while True:`) asosida ishlaydi! Server ertalab yoqiladi va tun-u kun foydalanuvchilardan keladigan HTTP so‘rovlarni kutib turadi:
```python
while True:
    so'rov = yangi_sorovni_kut()
    so'rovga_javob_ber(so'rov)
    if server_toxtatish_buyrugi:
        break
```
Agar sikl bo‘lmaganida, server bitta odam kirishi bilan o‘z ishini tugatib qo‘ygan bo‘lardi.

### while ... else imkoniyati
Pythonda qiziqarli xususiyat mavjud: `while` siklidan keyin `else` yozish mumkin!
- Agar sikl odatiy tarzda, ya'ni shart `False` bo‘lib o‘z vaqtida tugasa &rarr; `else` qismi ishlaydi;
- Agar sikl `break` operatori orqali muddatidan oldin to‘xtatilsa &rarr; `else` qismi **ishlamaydi**.
Bu imkoniyat qidiruv va parollarni tekshirishda juda qulaydir.

### break vs continue: Farqni his qilish
- `break` — bu "Favqulodda tormoz": qolgan barcha takrorlanishlar bekor qilinadi va sikl butunlay yopiladi.
- `continue` — bu "Qadamni o‘tkazib yuborish": masalan, ro‘yxatdagi 100 ta foydalanuvchiga xat jo‘natayotganda, nofaol foydalanuvchini uchratib qolsak, uni `continue` bilan tashlab o‘tamiz va keyingi odamga xat yuboramiz.

### Odatiy xatolar
- Qadamni yozishni unutish:
  ```python
  i = 1
  while i &lt;= 5:
      print(i)
      # i += 1 yozilmadi -> Cheksiz 1 chiqadi!
  ```
- Noto‘g‘ri shart yozish: `while i > 5:` agar boshlang‘ich `i = 1` bo‘lsa, shart boshidanoq `False` bo‘lib, sikl umuman biror marta ham ishlamaydi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| while | Shart rost turguncha ishlovchi takrorlanish operatori |
| Cheksiz sikl (Infinite loop) | Sharti hech qachon False bo‘lmaydigan to‘xtovsiz dastur |
| break | Siklni darhol to‘xtatib, undan chiqish operatori |
| continue | Siklning joriy iteratsiyasini tashlab, keyingisiga o‘tish |
| Ctrl + C | Terminalda qotib qolgan yoki cheksiz dasturni majburiy to‘xtatish |
| Flag (Bayroqcha) | Mantiqiy holatni saqlovchi maxsus o‘zgaruvchi (True/False) |
| Uptime | Serverning to‘xtovsiz ishlab turish vaqti |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Kompyuter o‘yinlarining asosiy yadrosi (Game Loop) aynan `while o'yin_davom_etmoqda:` sikli ustida ishlaydi. Har bir aylanishda o‘yinchi harakati tahlil qilinadi va ekran yangilanadi (FPS — sekundiga aylanishlar soni).
- NASA kosmik apparatlaridagi dasturlarda cheksiz sikllardan saqlanish uchun maxsus apparat taymerlari (Watchdog Timer) qo‘llaniladi. Agar dastur cheksiz aylanib qotsa, taymer tizimni avtomatik qayta yuklaydi (restart).

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. 1 dan 5 gacha chiqarish <Badge type="tip" text="oson" />
`i = 1` boshlang‘ich qiymatidan foydalanib, `while i <= 5:` yordamida sonlarni konsolga chiqaring.
**Kutiladigan natija:** 1, 2, 3, 4, 5 sonlari alohida qatorlarda chiqishi.

### 2. "Parol" so‘zini kutish <Badge type="tip" text="oson" />
Foydalanuvchi `"open"` so‘zini kiritguncha konsoldan takroran so‘rovchi oddiy dastur yozing.
**Kutiladigan natija:** Faqat `"open"` kiritilgandagina sikldan chiqib `"Eshik ochildi"` deb chiqarish.

### 3. Teskari sanoq <Badge type="tip" text="oson" />
`vaqt = 5`. `while` sikli orqali sonni 1 gacha kamaytirib boring va oxirida `"Vaqt tugadi!"` deb chiqaring.
**Kutiladigan natija:** `5 4 3 2 1 Vaqt tugadi!`

### 4. 2 dan 10 gacha juft sonlar <Badge type="tip" text="oson" />
`n = 2` dan boshlab, `while n <= 10:` orqali `n += 2` qadam bilan barcha juft sonlarni chiqaring.
**Kutiladigan natija:** `2 4 6 8 10`

### 5. 0 kiritilguncha sonlar yig‘indisi <Badge type="warning" text="o'rta" />
Foydalanuvchidan son kiritishni so‘rang. U `0` kiritmaguncha barcha kiritilgan sonlarni bir-biriga qo‘shib boring va yakuniy summani ko‘rsating.
**Kutiladigan natija:** `0` kiritilganda umumiy yig‘indi ekranga chiqishi.

### 6. Parol tekshirish (1.43-rasm) <Badge type="warning" text="o'rta" />
Rasmiy qo‘llanmadagi misol bo‘yicha:
`parol = "1234"` bo‘lsin. Foydalanuvchi to‘g‘ri parolni kiritmaguncha `"Xato! Qayta urinib ko'ring"` deb qayta so‘rovchi dastur tuzing.
**Kutiladigan natija:** To‘g‘ri kiritilganda `"Kirish tasdiqlandi"` chiqishi.

### 7. break bilan sonni topish <Badge type="warning" text="o'rta" />
1 dan 100 gacha sonlar ketma-ketligida aylanayotgan sikl birinchi 7 ga va 5 ga bo‘linadigan sonni (`i % 35 == 0`) uchratganda `break` bilan to‘xtasin va o‘sha sonni ko‘rsatsin.
**Kutiladigan natija:** `Topilgan birinchi son: 35`

### 8. continue bilan toqlarni o‘tkazib yuborish <Badge type="warning" text="o'rta" />
1 dan 15 gacha bo‘lgan sonlar orasida toq son uchrasa `continue` bilan tashlab o‘tib, faqat juft sonlarni chiqaruvchi kod yozing.
**Kutiladigan natija:** `2 4 6 8 10 12 14`

### 9. 3 ta urinishli parol tekshiruvi (1.44-rasm) <Badge type="danger" text="qiyin" />
Rasmiy qo‘llanmadagi 1.44-rasm topshirig‘i:
Foydalanuvchiga parolni kiritish uchun bor-yo‘g‘i 3 ta urinish bering.
- Agar 3 tadan kam urinishda to‘g‘ri parol kiritsa &rarr; `"Kirish muvaffaqiyatli!"` xabari chiqsin va `break` bilan sikl to‘xtasin.
- Agar 3 ta urinishda ham xato kiritsa &rarr; `"Urinishlar soni tugadi! Hisob bloklandi"` deb chiqarsin.
**Kutiladigan natija:** To‘liq xavfsiz autentifikatsiya oqimi.

### 10. Sonli taxmin o‘yini <Badge type="danger" text="qiyin" />
Dasturda `yashirin_son = 17` saqlangan. Foydalanuvchi kiritgan son yashirin sondan katta bo‘lsa `"Kichikroq son ayting"`, kichik bo‘lsa `"Kattaroq son ayting"` deb ko‘rsatma beruvchi va topguncha davom etuvchi dastur tuzing.
**Kutiladigan natija:** To‘g‘ri topilganda `"Tabriklaymiz, siz topdingiz!"` chiqishi.

### 11. Savatcha hisoblagich <Badge type="info" text="bonus" />
Foydalanuvchi xarid qilayotgan mahsulot narxlarini kiritadi. Agar u `stop` deb yozsa yoki manfiy son kiritsa, hisob-kitob to‘xtatilib, jami xarid summasi va nechta mahsulot olingani ko‘rsatilsin.
**Kutiladigan natija:** To‘liq chek hisobi va mahsulotlar soni.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Qanday vaziyatlarda `for` emas, aynan `while` siklidan foydalanish to‘g‘ri bo‘ladi?
2. Cheksiz sikl qanday xatolik tufayli yuzaga keladi va uni qanday to‘xtatish mumkin?
3. `break` va `continue` operatorlarining bir-biridan qanday asosiy farqi bor?
4. Rasmiy qo‘llanmadagi 3 ta urinishli parol masalasida `urinishlar` hisoblagichi qanday oshirib borildi?
5. `while False:` deb yozilsa, sikl ichidagi kod necha marta ishlaydi?
6. Qanday qilib `while` siklini serverda doimiy so‘rov kutish uchun ishlatish mumkin?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. `parol_urinish.py` faylida rasmiy 1.44-rasmdagi 3 ta imkoniyatli parol dasturini to‘liq yozing va sinab ko‘ring.
2. 1 dan 50 gacha bo‘lgan sonlar ichidan 5 ga karrali sonlarni `continue` orqali tashlab o‘tib, qolganlarini chiqaruvchi dastur yozing.
3. Foydalanuvchi `exit` so‘zini yozmaguncha unga salom beruvchi mini-chat dasturini tuzing.

</div>

