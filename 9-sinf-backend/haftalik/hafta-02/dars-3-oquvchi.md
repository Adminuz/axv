# 6-dars. Ko‘p tarmoqli shartlar: elif operatori va amaliy topshiriqlar

> Dasturimiz ko‘p variantli murakkab qarorlarni qabul qilishni o‘rganadi! Ushbu darsda `elif` operatori, baholash tizimlari va rasmiy qo‘llanmadagi 4 ta amaliy topshiriqni (musbat/manfiy/nol, kattasini topish, yosh toifalari, harorat) to‘liq kodlaymiz.

## Dars xulosasi

- **`elif`** — inglizcha *else if* ("aks holda agar") so‘zlarining qisqartmasi bo‘lib, 3 va undan ortiq tanlovlar mavjud bo‘lganda ishlatiladi.
- Dastur shartlarni yuqoridan pastga qarab tekshiradi: birinchi to‘g‘ri kelgan (`True`) shart bajariladi va qolgan barcha `elif` hamda `else` bloklari tashlab ketiladi.
- `if - elif - else` zanjirida `else` har doim eng oxirida turadi va oldingi hech qaysi shart bajarilmaganda ishga tushadi.
- Rasmiy dasturimizdagi muhim topshiriqlar: sonning ishorasini aniqlash, ikki sondan kattasini topish, yosh toifasi va ob-havo harorati tavsiyalari.
- Boshlang‘ich dasturchilar eng ko‘p yo‘l qo‘yadigan 3 ta xato: `=` va `==` ni adashtirish, `:` ni unutish hamda noto‘g‘ri chekinish (indentation).

## Qo'shimcha ma'lumot

### Nega ko‘p if emas, aynan if-elif-else?
Faraz qiling, bizda 4 ta alohida `if` yozilgan:
```python
# Yomon usul (4 ta if)
if ball >= 86:
    baho = 5
if ball >= 71:
    baho = 4
if ball >= 56:
    baho = 3
```
Agar `ball = 90` bo‘lsa, dastur birinchi shartni tekshiradi (`baho = 5`), keyin ikkinchi shartni tekshiradi (90 >= 71 ham True, shuning uchun `baho = 4` bo‘lib qoladi!), keyin uchinchi shartni tekshiradi va oxirida `baho = 3` bo‘lib chiqadi! Bu jiddiy mantiqiy xatodir.
`elif` ishlatilganda esa, birinchi to‘g‘ri shart bajarilishi bilan qolganlari tekshirilmaydi:
```python
# To'g'ri usul (if-elif-else)
if ball >= 86:
    baho = 5
elif ball >= 71:
    baho = 4
elif ball >= 56:
    baho = 3
else:
    baho = 2
```

### input() funksiyasi bilan konsoldan ma'lumot olish
Haqiqiy backend dasturlarida ma'lumotlar foydalanuvchidan qabul qilinadi. Pythonda buning uchun `input()` funksiyasi ishlatiladi.
Diqqat! `input()` har doim ma'lumotni matn (`str`) ko‘rinishida qabul qiladi. Shu sababli sonli shartlarda uni albatta `int()` ga o‘tkazish kerak:
```python
son = int(input("Butun son kiriting: "))
```

### Odatiy xatolar
- Taqqoslashda bitta tenglik qo‘yish: `if ball = 60:` &rarr; `SyntaxError: cannot assign to comparison`
- Shartlar tartibini adashtirish: Agar eng kichik shartni tepaga qo‘ysangiz (masalan, `if ball >= 56:` ni eng birinchi yozsangiz), 90 olgan talabaga ham 3 baho qo‘yilib ketadi. Shartlar har doim qat'iy mantiqiy tartibda yozilishi lozim!

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| elif | else if ("aks holda agar") qisqartmasi |
| if-elif-else | Ko‘p tarmoqli shartli tekshiruv konstruksiyasi |
| input() | Foydalanuvchidan konsol orqali ma'lumot qabul qiluvchi funksiya |
| int(input()) | Kiritilgan matnni butun songa aylantirish |
| Mantiqiy xato | Dastur xatosiz ishlaydi, ammo natija noto‘g‘ri chiqadi |
| Chekinish (Indent) | Kod blokini ajratib ko‘rsatuvchi 4 ta bo‘sh joy |
| Oraliq shart | Qiymatning ma'lum intervalda (`a <= x <= b`) yotishini tekshirish |

## Bilasizmi?

- Veb-serverlar foydalanuvchi so‘rovlariga javob qaytarishda aynan `elif` zanjiridan foydalanadi: "Agar sahifa topilsa &rarr; 200 OK; Agar ruxsat bo‘lmasa &rarr; 403 Forbidden; Agar sahifa mavjud bo‘lmasa &rarr; 404 Not Found; Aks holda &rarr; 500 Server Error".
- Python 3.10 versiyasigacha Pythonda C/Java tillaridagi `switch/case` operatori yo‘q edi, uning o‘rnini faqat `if-elif-else` bosgan. (Keyingi haftada biz yangi `match/case` operatorini ham o‘rganamiz!)

## Topshiriqlar

### 1. Musbat, manfiy yoki nol · oson
Rasmiy qo‘llanmadagi 1-topshiriq:
Bitta butun son berilgan. Agar son 0 dan katta bo‘lsa `"Musbat son"`, 0 dan kichik bo‘lsa `"Manfiy son"`, 0 ga teng bo‘lsa `"Nolga teng"` deb chiqaring.
**Kutiladigan natija:** `-15` kiritilganda `Manfiy son` chiqishi.

### 2. Baholash tizimi · oson
O‘quvchining bali `ball = 88` deb oling. Rasmiy mezon bo‘yicha:
- `ball >= 86` &rarr; 5
- `ball >= 71` &rarr; 4
- `ball >= 56` &rarr; 3
- Aks holda &rarr; 2
natijasini konsolga chiqaring.
**Kutiladigan natija:** `Baho: 5`

### 3. Harorat tavsiyasi · oson
Rasmiy qo‘llanmadagi 4-topshiriq:
Havo harorati `harorat = 16` daraja.
- 0 dan past bo‘lsa &rarr; `"Sovuq, qalin kiyining"`
- 0 dan 20 gacha bo‘lsa &rarr; `"Salqin"`
- 20 dan yuqori bo‘lsa &rarr; `"Issiq"`
**Kutiladigan natija:** `Salqin`

### 4. Svetafor signallari · oson
Rang `rang = "yashil"` deb berilgan.
- `"qizil"` &rarr; `"To'xtang!"`
- `"sariq"` &rarr; `"Tayyorlaning!"`
- `"yashil"` &rarr; `"Harakatlaning!"`
- Boshqa rang &rarr; `"Noto'g'ri rang"`
**Kutiladigan natija:** `Harakatlaning!`

### 5. Ikki sondan kattasi yoki tengligi · o'rta
Rasmiy qo‘llanmadagi 2-topshiriq:
`a = 25` va `b = 25`. Agar `a > b` bo‘lsa a ni, `b > a` bo‘lsa b ni chiqaring. Agar teng bo‘lsa `"Sonlar teng"` deb chiqaring.
**Kutiladigan natija:** `Sonlar teng`

### 6. Yoshga qarab toifa · o'rta
Rasmiy qo‘llanmadagi 3-topshiriq:
`yosh = 14`.
- 0–6 &rarr; `"Bog‘cha yoshi"`
- 7–17 &rarr; `"Maktab o‘quvchisi"`
- 18 va undan katta &rarr; `"Voyaga yetgan"`
**Kutiladigan natija:** `Maktab o‘quvchisi`

### 7. Hafta kuni nomi · o'rta
Raqam `kun = 3` berilgan bo‘lsa, `elif` yordamida hafta kunining nomini (1 - Dushanba, ..., 7 - Yakshanba) chiqaring. 1–7 oralig‘ida bo‘lmasa `"Xato kun"` xabarini bering.
**Kutiladigan natija:** `Chorshanba`

### 8. Fikr va takliflar bahosi · o'rta
Mijoz xizmat sifatiga 1 dan 5 gacha yulduzcha berdi (`yulduz = 4`):
- 5 &rarr; `"A'lo xizmat"`
- 4 &rarr; `"Yaxshi, minnatdormiz"`
- 3 &rarr; `"O'rtacha, xatolarni to'g'rilaymiz"`
- 1 yoki 2 &rarr; `"Kechirasiz, shikoyatingiz qabul qilindi"`
**Kutiladigan natija:** `Yaxshi, minnatdormiz`

### 9. Uchta sondan eng kattasini topish · qiyin
Uchta son berilgan: `x = 45`, `y = 89`, `z = 62`. Faqat `if-elif-else` va `and` operatorlaridan foydalanib, uchta sondan eng kattasini topuvchi mukammal dastur tuzing.
**Kutiladigan natija:** `Eng katta son: 89`

### 10. Valyuta konverteri · qiyin
Foydalanuvchida `mablag = 1000000` so‘m bor va u valyutani tanlaydi (`valyuta = "USD"` yoki `"EUR"` yoki `"RUB"`).
- USD: 12 800 so‘m
- EUR: 13 900 so‘m
- RUB: 140 so‘m
Tanlangan valyutaga qarab mablag‘ni hisoblab chiqaruvchi dastur yozing.
**Kutiladigan natija:** `Sizning mablag'ingiz: 78.12 USD`

### 11. To‘liq interaktiv diagnostika bot · bonus
`input()` orqali foydalanuvchining server monitoring holatini so‘rovchi mini diagnostika dasturi tuzing:
- CPU yuklamasi (0–100%)
- RAM yuklamasi (0–100%)
Agar ikkalasi ham 85% dan oshsa &rarr; `"KRITIK HOLAT: Server qizib ketmoqda!"`
Agar faqat bittasi 85% dan oshsa &rarr; `"OGOHLANTIRISH: Resurslar chegarada"`
Aks holda &rarr; `"Tizim normal holatda ishlamoqda"`.
**Kutiladigan natija:** To‘liq ishlovchi server monitoring tahlili.

## O'zingizni tekshiring

1. `elif` operatorining `else if` dan qanday farqi bor?
2. Nega `if-elif-else` zanjirida shartlarning yozilish tartibi muhim?
3. Agar hech qaysi `if` va `elif` sharti bajarilmasa nima sodir bo‘ladi?
4. `input()` orqali olingan ma'lumotni nima uchun `int()` ga o‘tkazish kerak?
5. Pythonda `=` va `==` operatorlarining vazifalarini yana bir bor tushuntiring.
6. Rasmiy qo‘llanmadagi "Harorat tavsiyasi" topshirig‘ida shartlar qanday tartibda tuzildi?

## Uyga vazifa

1. Rasmiy 4 ta topshiriqni alohida fayllarga yozing:
   - `musbat_manfiy.py` (0 dan katta, kichik yoki nol);
   - `kattasi.py` (ikki sondan kattasini yoki tengligini topish);
   - `yosh_toifa.py` (bog‘cha, maktab, voyaga yetgan);
   - `harorat.py` (sovuq, salqin, issiq).
2. Dasturlarni turli xil qiymatlar bilan sinab ko‘ring va konsol natijalarini tekshiring.
