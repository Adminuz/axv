---
title: "3-dars. O‘zgaruvchilar va ma'lumotlar bilan ishlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "week": {"n": 1, "link": "/9-sinf-backend/hafta-01/"}, "g": 3, "title": "O‘zgaruvchilar va ma'lumotlar bilan ishlash", "lead": "Dastur xotirasi bilan ishlash vaqti keldi! Ushbu darsda o‘zgaruvchilar yaratish, to‘g‘ri nomlash qoidalari va rasmiy qo‘llanmadagi \"Tanishuv kartochkasi\" hamda \"Do‘kon kassasi\" loyihalarini qadamma-qadam quramiz.", "slide": "/slaydlar/9-sinf-backend/hafta-01/dars-3.html", "test": "/slaydlar/9-sinf-backend/hafta-01/dars-3-test.html", "tabs": [{"g": 1, "link": "/9-sinf-backend/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/9-sinf-backend/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/9-sinf-backend/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "Sodda ma’lumot toifalari va arifmetik amallar", "link": "/9-sinf-backend/hafta-01/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **O‘zgaruvchi** — kompyuter tezkor xotirasida (RAM) ma'lumotni saqlash va unga murojaat qilish uchun berilgan nom.
- O‘zgaruvchini yorliqli **quti 📦** deb tasavvur qilish mumkin: qutiga qiymat solinadi va nomi orqali chaqiriladi.
- `=` belgisi tenglik emas, balki **o‘zlashtirish (qiymat berish)** operatori hisoblanadi.
- Pythonda o‘zgaruvchi turini oldindan e'lon qilish shart emas (**dinamik tiplashtirish**).
- O‘zgaruvchi nomlari harf yoki `_` bilan boshlanishi shart, raqamdan boshlanishi yoki orasi ochiq bo‘lishi mumkin emas.
- Pythonda qabul qilingan standart nomlash uslubi — **snake_case** (masalan, `foydalanuvchi_nomi`).
- `print(ism, yosh)` orqali bir nechta o‘zgaruvchini bitta qatorda konsolga chiqarish mumkin.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Xotirada o‘zgaruvchilar qanday joylashadi?
Ko‘pchilik o‘zgaruvchini "ma'lumot solingan idish" deb o‘ylaydi. Python ichki tuzilishida esa bu yanada qiziqroq: Python avval xotirada qiymatni yaratadi (masalan, `15` soni yoki `"Ali"` matni), so‘ngra `ism` degan yorliqni shu qiymatga yo‘naltiradi (ip bilan bog‘laydi). Agar keyinchalik `ism = "Vali"` desangiz, yorliq eski qiymatdan uzilib, yangi qiymatga bog‘lanadi. Eski qiymat esa xotiradan "chiqindi yig‘uvchi" (Garbage Collector) tomonidan avtomatik tozalanadi.

### O‘zgaruvchilarni nomlash madaniyati (Clean Code)
Yaxshi dasturchi o‘zgaruvchiga qarab uning nima vazifa bajarishini darhol tushunadi:
- `a = 3000` (Yomon: `a` nima ekanligi noma'lum);
- `non_narxi = 3000` (A'lo: darhol nonga tegishli narx ekanligi ma'lum);
- `x = "Toshkent"` (Tushunarsiz);
- `shahar = "Toshkent"` (Aniq va tushunarli).

### Zamonaviy formatlash: f-string
Python 3.6 versiyasidan boshlab matn ichiga o‘zgaruvchilarni qulay joylashtirish uchun **f-string** formati kiritilgan. Buning uchun qo‘shtirnoq oldiga `f` harfi qo‘yiladi va o‘zgaruvchi jingalak qavs `{ ... }` ichiga yoziladi:
```python
ism = "Ali"
yosh = 15
print(f"Salom, mening ismim {ism} va men {yosh} yoshdaman.")
```
Bu usul kodni juda toza va o‘qishli qiladi.

### Odatiy xatolar
- O‘zgaruvchini raqam bilan boshlash: `1_son = 10` — bu `SyntaxError: invalid decimal literal` xatosiga olib keladi.
- Bo‘sh joy tashlash: `talaba yoshi = 16` — bu `SyntaxError: invalid syntax` beradi. To‘g‘risi: `talaba_yoshi = 16`.
- E'lon qilinmagan o‘zgaruvchini chaqirish: `print(familiya)` — agar `familiya` oldin yaratilmagan bo‘lsa, `NameError: name 'familiya' is not defined` xatosi chiqadi.

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| O‘zgaruvchi (Variable) | Xotiradagi ma'lumotga berilgan nom |
| O‘zlashtirish (=) | O‘zgaruvchiga qiymat yuklash amali |
| Dinamik tiplashtirish | Toifaning dastur ishlashi davomida avtomatik aniqlanishi |
| snake_case | So‘zlarni kichik harf va tagchiziq bilan yozish uslubi |
| f-string | O‘zgaruvchilarni matn ichiga formatlab kiritish usuli |
| NameError | Dasturda mavjud bo‘lmagan o‘zgaruvchiga murojaat xatosi |
| Case-sensitive | Katta va kichik harflarni alohida hisoblash xususiyati |
| Konstant (O‘zgarmas) | Qiymati o‘zgarmaydigan o‘zgaruvchi (odatda KATTA_HARF bilan yoziladi) |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Pythonda bitta qatorda bir nechta o‘zgaruvchiga birdaniga qiymat berish mumkin: `x, y, z = 10, 20, 30`.
- Ikkita o‘zgaruvchining qiymatini almashtirish (Swap) uchun uchinchi yordamchi o‘zgaruvchi shart emas: shunchaki `a, b = b, a` deb yozish yetarli!
- Pythonda o‘zgaruvchi nomlari sifatida o‘zbekcha lotin harflarini (masalan, `yosh = 15`) bemalol ishlatish mumkin bo‘lsa-da, jahon IT standartida o‘zgaruvchilarni inglizcha nomlash (`age = 15`) tavsiya etiladi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Tanishuv kartochkasi <Badge type="tip" text="oson" />
`ism`, `yosh`, `kasb` nomli 3 ta o‘zgaruvchi yarating. Ularga o‘z ma'lumotlaringizni yuklang va bitta `print()` orqali ekranga chiqaring.
**Kutiladigan natija:** `Ism: Jamshid | Yosh: 15 | Kasb: Back-end dasturchi`

### 2. Do‘kon kassasi <Badge type="tip" text="oson" />
Rasmiy qo‘llanmadagi misol bo‘yicha:
`non_narxi = 3000` va `sut_narxi = 12500.5` o‘zgaruvchilarini yarating. Ikkala mahsulotdan bittadan olganda jami qancha bo‘lishini hisoblab, `jami` o‘zgaruvchisiga yuklang va natijani chiqaring.
**Kutiladigan natija:** `Jami summa: 15500.5 so'm`

### 3. Qiymatni yangilash <Badge type="tip" text="oson" />
`ball = 70` o‘zgaruvchisini yarating. Keyingi qatorda unga `15` ball qo‘shib yangilang (`ball += 15`). Yangilangan natijani ekranga chiqaring.
**Kutiladigan natija:** `Yakuniy ball: 85`

### 4. Shaxsiy kompyuter ma'lumotlari <Badge type="tip" text="oson" />
`ram_gb = 16`, `protsessor = "Core i7"`, `ssd_gb = 512` o‘zgaruvchilarini yaratib, ularni bitta satrda chiqaring.
**Kutiladigan natija:** `Tizim: Core i7, RAM: 16 GB, SSD: 512 GB`

### 5. Ko‘paytirilgan xarid <Badge type="warning" text="o'rta" />
Do‘kondan 4 ta non (`non_narxi = 3000`) va 3 ta sut (`sut_narxi = 12500.5`) sotib olindi. `jami_non`, `jami_sut` va `yakuniy_hisob` o‘zgaruvchilarini tuzib, to‘liq chekni chiqaring.
**Kutiladigan natija:**
```text
Nonlar (4 dona): 12000 so'm
Sutlar (3 dona): 37501.5 so'm
Jami to'lov: 49501.5 so'm
```

### 6. f-string yordamida sertifikat <Badge type="warning" text="o'rta" />
`talaba`, `kurs`, `ball` o‘zgaruvchilaridan foydalanib, f-string orqali quyidagi tabriknoma matnini chiqaring:
"Tabriklaymiz, {talaba}! Siz {kurs} kursini {ball} ball bilan muvaffaqiyatli tamomladingiz."
**Kutiladigan natija:** Barcha o‘zgaruvchilar matn ichida chiroyli birlashgan bo‘lishi kerak.

### 7. Xato nomlarni toping <Badge type="warning" text="o'rta" />
Quyidagi o‘zgaruvchi nomlaridan qaysilari xato va nega?
`1_son`, `foydalanuvchi-yoshi`, `user_name`, `narx$`, `class`, `maktab_9`
Xato nomlarni to‘g‘rilab, Python-da xatosiz ishga tushiring.
**Kutiladigan natija:** Xato nomlarning sababi aniqlanishi va to‘g‘ri variantlari yozilishi.

### 8. Tejamkorlik hisoblagichi <Badge type="warning" text="o'rta" />
Oylik byudjet `5 000 000` so‘m. Oziq-ovqatga `2 000 000`, yo‘lkiraga `600 000`, kommunalga `400 000` sarflandi. Qolgan mablag‘ni `jamg‘arma` o‘zgaruvchisiga hisoblab ekranga chiqaring.
**Kutiladigan natija:** `Oy oxirida qolgan jamg'arma: 2000000 so'm`

### 9. O‘rin almashtirish (Swap) <Badge type="danger" text="qiyin" />
Ikkita o‘zgaruvchi berilgan: `x = "Python"`, `y = "DevOps"`. Pythonning qulay imkoniyatidan foydalanib ularning qiymatlarini o‘zaro almashtiring va natijani ko‘rsating.
**Kutiladigan natija:** `x = DevOps, y = Python`

### 10. Server yuklamasi hisobi <Badge type="danger" text="qiyin" />
Serverda jami `1000` ta so‘rov kelib tushdi. Ulardan `950` tasi muvaffaqiyatli (`status 200`), `50` tasi xatolik bilan yakunlandi. Muvaffaqiyatli so‘rovlar foizini hisoblovchi va quyidagicha chiqaruvchi dastur tuzing:
`Muvaffaqiyat darajasi: 95.0%`
**Kutiladigan natija:** Foiz qiymati to‘g‘ri hisoblanib chiqishi.

### 11. Mini-kassa tizimi (Interaktiv) <Badge type="info" text="bonus" />
`input()` funksiyasi orqali foydalanuvchidan o‘z ismini, qancha non va qancha sut olmoqchiligini so‘rab, umumiy summani avtomatik hisoblab chiquvchi to‘liq mini-kassa dasturini yarating.
**Kutiladigan natija:** Foydalanuvchi kiritgan sonlarga qarab to‘lov summasini aniq hisoblash.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. O‘zgaruvchi nima va u kompyuter xotirasida qanday ishlaydi?
2. Nega o‘zgaruvchi nomini raqam bilan boshlab bo‘lmaydi?
3. `a = 5` va `a == 5` yozuvlarining qanday farqi bor?
4. `non_narxi` va `sut_narxi` qo‘shilganda jami natija nega kasr son (`float`) bo‘ldi?
5. `snake_case` va `camelCase` uslublarining farqi nimada?
6. Pythonda f-string nimasi bilan oddiy vergulli `print()` dan afzalroq?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. `server_info.py` faylini oching.
2. Unda server konfiguratsiyasini saqlovchi quyidagi o‘zgaruvchilarni yarating:
   - `server_nomi = "Web-Node-01"`
   - `ip_manzil = "192.168.1.50"`
   - `port = 8000`
   - `ram_mb = 4096`
   - `aktiv = True`
3. f-string yordamida barcha ma'lumotlarni chiroyli ramka ichida konsolga chiqaring.
4. "Do‘kon kassasi" dasturiga yana 2 ta mahsulot qo‘shib, hisob-kitobni yangilang.

</div>

