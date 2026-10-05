---
title: "2-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "10-sinf (Cyber)", "link": "/10-sinf-cyber/"}, "n": 2, "bob": "I-bob · Kiberxavfsizlikka kirish", "lessons": [{"g": 4, "title": "CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari", "lead": "CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari", "link": "/10-sinf-cyber/hafta-02/dars-1", "slide": "/slaydlar/10-sinf-cyber/hafta-02/dars-1.html", "test": "/slaydlar/10-sinf-cyber/hafta-02/dars-1-test.html"}, {"g": 5, "title": "CIA uchligi (2-qism): CIA buzilish ssenariylari va MITM hujumlari", "lead": "[!CAUTION]", "link": "/10-sinf-cyber/hafta-02/dars-2", "slide": "/slaydlar/10-sinf-cyber/hafta-02/dars-2.html", "test": "/slaydlar/10-sinf-cyber/hafta-02/dars-2-test.html"}, {"g": 6, "title": "Xavfsizlikni anglash (1-qism): xavfsizlik tafakkuri va kuchli parollar siyosati", "lead": "«Xavfsizlik o'ziga xos fikrlash tarzini talab qiladi. Yaxshi mutaxassislar do'konga kirsa qanday o'g'irlik qilish mumkinligini, kompyuter ko'rsa qanday zaiflik borligini o'ylamasdan turolmaydilar.» — **Bryus Shnayer**", "link": "/10-sinf-cyber/hafta-02/dars-3", "slide": "/slaydlar/10-sinf-cyber/hafta-02/dars-3.html", "test": "/slaydlar/10-sinf-cyber/hafta-02/dars-3-test.html"}], "test": "/slaydlar/10-sinf-cyber/hafta-02/hafta-test.html"}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

### 4-dars. CIA uchligi: konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari
1. O'zingiz qiziqqan ikkita sohani tanlang (masalan: Elektron tijorat sayti va Tez tibbiy yordam dispetcherlik xizmati).
2. Ushbu ikki soha uchun CIA uchligini (C, I, A) taqqoslang va har biri uchun qaysi mezon birinchi o'rinda turishini, nima sababdan shunday ekanligini 4-5 jumla bilan yozing.
3. Kompyuteringizda ixtiyoriy matnli fayl yarating va uning SHA-256 xeshini oling (`sha256sum` yoki `CertUtil -hashfile`). Matnga bitta probel yoki nuqta qo'shib qayta xesh oling va ikkala natijani daftaringizga ko'chirib solishtiring.

---

### 5-dars. CIA buzilish ssenariylari va MITM hujumlari
1. O'rtadagi odam (MITM) hujumi qanday qilib bir vaqtning o'zida ham Konfidensiallikka, ham Yaxlitlikka putur yetkazishi mumkinligini ssenariy asosida tushuntiring.
2. Nima sababdan kafe yoki aeroportlardagi ochiq jamoat Wi-Fi tarmoqlarida parollarni kiritish xavfli va nima uchun bunday holatlarda VPN ishlatish zarur?
3. Tarmoq kommutatorlarida Dynamic ARP Inspection (DAI) texnologiyasi qanday ishlashini konspektdan foydalanib yozma bayon eting.

---

### 6-dars. Xavfsizlik tafakkuri va kuchli parollar siyosati
1. Xavfsizlik tafakkurining 5 ta tamoyilidan (What could go wrong, Adversarial, Defensive, Assume breach, Know assets) birini tanlang va unga kundalik hayotingizdan bitta misol keltiring.
2. `haveibeenpwned.com/Passwords` xizmatiga kiring (yoki Kaspersky Password Checker) va ilgari ishlatgan oddiy so'zli parollaringiz (masalan: `123456`, `qwerty2020`) necha marta buzilgan bazalarda topilganini tekshiring.
3. O'zingiz uchun kamida 14 belgidan iborat, katta-kichik harflar, sonlar va belgilarni o'z ichiga olgan namunaviy kuchli parol formulasini ishlab chiqing (masalan: sevimli she'r yoki iboraning bosh harflari asosida: `M@kt@b2025#Oqish`).

---

</div>
