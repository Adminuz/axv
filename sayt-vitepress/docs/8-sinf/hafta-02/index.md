---
title: "2-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "n": 2, "bob": "I-bob · HTML tili va veb-sahifa tuzishning asoslari", "lessons": [{"g": 4, "title": "Rasm va ro'yxat teglari: <img>, <figure>, <ul>, <ol>, <dl>", "lead": "Surat mingta so'zdan afzal, ro'yxatlar esa har qanday chalkashlikni tartibga soladi. Ushbu darsda veb-sahifaga rasm joylash, to'g'ri manzillarni ko'rsatish va 3 xil ro'yxat turidan foydalanishni o'rganamiz.", "link": "/8-sinf/hafta-02/dars-1", "slide": "/slaydlar/8-sinf/hafta-02/dars-1.html"}, {"g": 5, "title": "Jadval teglari: <table>, <tr>, <td>, <th>, colspan va rowspan", "lead": "Dars jadvali, futbol chempionati turnir jadvali, internet-do'kondagi narxlar va xarid cheki — bularning barchasi jadvallardir. Ushbu darsda HTML yordamida qator va ustunlardan iborat chiroyli jadvallar yaratishni, katakchalarni birlashtirishni o'rganamiz.", "link": "/8-sinf/hafta-02/dars-2", "slide": "/slaydlar/8-sinf/hafta-02/dars-2.html"}, {"g": 6, "title": "Forma elementlari va validatsiyasi: <form>, <input>, <label>, <select>, <textarea>", "lead": "Veb-sayt shunchaki gazeta emas, u foydalanuvchi bilan muloqot qiladigan tirik tizimdir. Ushbu darsda saytlarga login qilish, xabar yuborish, so'rovnomalar to'ldirish va forma ma'lumotlarini to'g'ri tekshirishni (validatsiya) o'rganamiz.", "link": "/8-sinf/hafta-02/dars-3", "slide": "/slaydlar/8-sinf/hafta-02/dars-3.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Har bir vazifa 20–30 daqiqa. Fayllar alohida `hafta-02` papkasida saqlanadi.

### 4-dars uchun (Rasm va ro'yxat teglari)
**1-topshiriq: «Mening sevimli mavzum» sahifasi**
- O'zingiz qiziqqan mavzuda (sport, o'yin, kitob yoki tabiat) `qiziqish.html` sahifasini tayyorlang.
- Sahifada kamida 2 ta rasm (`<img>`, to'g'ri `alt`, `width` va `height` bilan) bo'lsin.
- Bitta rasm `<figure>` va `<figcaption>` bilan o'ralsin.
- Mavzuga oid 1 ta tartiblangan (`<ol>`), 1 ta tartibsiz (`<ul>`) va 1 ta ta'riflar ro'yxati (`<dl>`) yarating.
- **Tekshirish:** barcha rasmlar to'g'ri yuklanadi, `alt` mavjud, ro'yxatlar ichma-ich sintaktik xatosiz yozilgan.

### 5-dars uchun (Jadval teglari, colspan, rowspan)
**2-topshiriq: «Oylik reja va xarajatlar» jadvali**
- `jadval.html` faylini yarating.
- Unda `<caption>`, `<thead>`, `<tbody>` va `<tfoot>` semantik bo'limlari bo'lsin.
- Kamida 4 ta ustun: №, Xarajat moddasi, Miqdori, Narxi.
- Eng pastki `<tfoot>` qatorida `colspan` yordamida "Jami xarajat" hisoblansin.
- Ixtiyoriy: biror qatorda `rowspan` qo'llab ko'ring (masalan, bir xil toifadagi xarajatlar uchun).
- **Tekshirish:** jadval ramkasi buzilmagan, katakchalar matematik muvozanatda, brauzerda to'g'ri tekislangan.

### 6-dars uchun (Forma elementlari va validatsiya)
**3-topshiriq: «Klubga a'zo bo'lish» formasi**
- `forma.html` faylini yarating.
- `<form action="#" method="POST">` oching.
- Unda quyidagi maydonlar bo'lsin va har biri o'z `<label>`iga (`for` va `id`) ega bo'lsin:
  1. Ism va familiya (`type="text"`, `required`);
  2. Email (`type="email"`, `placeholder`);
  3. Parol (`type="password"`, `required`);
  4. Qiziqishlar (`type="checkbox"`, kamida 3 ta variant);
  5. Dars vaqti (`type="radio"`, bir xil `name` bilan 2 ta variant);
  6. Viloyat (`<select>` va `<option>`);
  7. O'zingiz haqingizda qo'shimcha ma'lumot (`<textarea>`);
  8. "A'zo bo'lish" tugmasi (`<button type="submit">`).
- **Tekshirish:** bo'sh holatda yuborishga urinilganda brauzer ogohlantirish beradi, radio tugmalardan faqat bittasi tanlanadi, label bosilganda kursor maydonga tushadi.

</div>
