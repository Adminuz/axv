---
title: "4-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "n": 4, "bob": "I-bob · Python dasturlash tili asoslari", "lessons": [{"g": 10, "title": "Ma’lumotlar tuzilmalari va string (satr) asoslari", "lead": "Bir nechta son yoki matnlarni qanday tartibda saqlashni bilmayapsizmi? Ushbu darsda Python'dagi ma'lumotlar tuzilmalari xaritasi va eng ko'p ishlatiladigan string (satr) turining xususiyatlarini o'rganamiz.", "link": "/9-sinf-backend/hafta-04/dars-1", "slide": "/slaydlar/9-sinf-backend/hafta-04/dars-1.html", "test": null}, {"g": 11, "title": "String: indeks, slicing va metodlar", "lead": "Matndan ma'lum bir harfni ajratib olish yoki so'zlarni bosh harfga aylantirish kerakmi? Ushbu darsda indekslash, qirqib olish (slicing) va eng muhim satr metodlari bilan tanishamiz.", "link": "/9-sinf-backend/hafta-04/dars-2", "slide": "/slaydlar/9-sinf-backend/hafta-04/dars-2.html", "test": null}, {"g": 12, "title": "List (ro‘yxat): yaratish, indeks va metodlar", "lead": "O'nlab o'zgaruvchilarni alohida e'lon qilishdan charchadingizmi? Ushbu darsda Python'ning eng ko'p qo'llaniladigan va moslashuvchan tuzilmasi &mdash; list (ro'yxat) hamda uning amallari bilan tanishamiz.", "link": "/9-sinf-backend/hafta-04/dars-3", "slide": "/slaydlar/9-sinf-backend/hafta-04/dars-3.html", "test": null}], "test": null}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Har bir vazifa 20–30 daqiqa. Kodlar alohida `hafta-04` papkasida saqlanadi.

### 10-dars uchun (Ma’lumotlar tuzilmalari va string asoslari)
**1-topshiriq: «Tirnoqlar va Immutability»**
`string_asos.py` faylini oching:
1. Ism (`"`), familiya (`'`) va 3 qatorli «Men haqimda» matnini (`"""`) e'lon qilib, hammasini chiroyli formatda ekranga chiqaring.
2. `s = "Python"` satridan `"Jython"` hosil qiling, so‘ng `"Python"` dan yana boshqa (`"Cython"`) yangi string yarating. Asl `s` o'zgaruvchisi o'zgarmasdan qolganini isbotlang.
3. 5 ta ma’lumotni (ism, yosh, fan ro‘yxati, koordinata, telefon-ism juftligi) qaysi tuzilmaga (`str`, `list`, `tuple`, `dict`) mos kelishini izoh shaklida yozing.

**Kutiladigan natija:** String yaratish usullari va immutability qoidalari to'g'ri qo'llanilishi.

---

### 11-dars uchun (String: indeks, slicing va metodlar)
**2-topshiriq: «Slicing laboratoriyasi va matnlarni tozalash»**
`slicing_mashq.py` faylida:
1. `word = "Backend"` uchun `[1:4]`, `[:3]`, `[3:]`, `[::2]`, `[::-1]` natijalarini ekranga chiqaring.
2. `s = "ozbekiston respublikasi"` satrini `.upper()`, `.lower()`, `.title()`, `.capitalize()` metodlari bilan alohida qatorlarda chiqaring.
3. Foydalanuvchi kiritgan so'zning palindrom (masalan `"radar"`, `"non"`) ekanligini slicing `[::-1]` yordamida tekshiruvchi dastur yozing.

**Kutiladigan natija:** Indekslash, qirqib olish va satr metodlarining to'g'ri ishlashi.

---

### 12-dars uchun (List: yaratish, indeks va metodlar)
**3-topshiriq: «Talabaning fanlari va ro'yxat amallari»**
`list_mashq.py` faylini oching:
1. 5 ta sevimli filmingiz ro‘yxatini yarating; birinchi, oxirgi elementni, `[1:4]` va `[::-1]` kesmalarini chiqaring.
2. `a = [1, 2]` ni `append`, `insert`, `remove`, `pop`, `clear` ketma-ketligi bilan o‘zgartirib, har qadamdan keyin natijani chop eting.
3. «Talabalar ma’lumotlari» mini-loyihasining boshlang'ich qismini tuzing: ism va familiyani `string`, fanlarni `list` qiling (yangi fan qo'shish, o'chirish amallarini bajaring).

**Kutiladigan natija:** Listning barcha asosiy metodlari to'liq va xatosiz ishlashi.

---

</div>
