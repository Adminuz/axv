# 2-hafta: Uyga vazifalar to'plami (Kiberxavfsizlik)

Ushbu haftada o'tilgan darslar bo'yicha mustaqil amaliy uyga vazifalar ro'yxati:

---

## 4-dars. CIA uchligi: konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari
1. O'zingiz qiziqqan ikkita sohani tanlang (masalan: Elektron tijorat sayti va Tez tibbiy yordam dispetcherlik xizmati).
2. Ushbu ikki soha uchun CIA uchligini (C, I, A) taqqoslang va har biri uchun qaysi mezon birinchi o'rinda turishini, nima sababdan shunday ekanligini 4-5 jumla bilan yozing.
3. Kompyuteringizda ixtiyoriy matnli fayl yarating va uning SHA-256 xeshini oling (`sha256sum` yoki `CertUtil -hashfile`). Matnga bitta probel yoki nuqta qo'shib qayta xesh oling va ikkala natijani daftaringizga ko'chirib solishtiring.

---

## 5-dars. CIA buzilish ssenariylari va MITM hujumlari
1. O'rtadagi odam (MITM) hujumi qanday qilib bir vaqtning o'zida ham Konfidensiallikka, ham Yaxlitlikka putur yetkazishi mumkinligini ssenariy asosida tushuntiring.
2. Nima sababdan kafe yoki aeroportlardagi ochiq jamoat Wi-Fi tarmoqlarida parollarni kiritish xavfli va nima uchun bunday holatlarda VPN ishlatish zarur?
3. Tarmoq kommutatorlarida Dynamic ARP Inspection (DAI) texnologiyasi qanday ishlashini konspektdan foydalanib yozma bayon eting.

---

## 6-dars. Xavfsizlik tafakkuri va kuchli parollar siyosati
1. Xavfsizlik tafakkurining 5 ta tamoyilidan (What could go wrong, Adversarial, Defensive, Assume breach, Know assets) birini tanlang va unga kundalik hayotingizdan bitta misol keltiring.
2. `haveibeenpwned.com/Passwords` xizmatiga kiring (yoki Kaspersky Password Checker) va ilgari ishlatgan oddiy so'zli parollaringiz (masalan: `123456`, `qwerty2020`) necha marta buzilgan bazalarda topilganini tekshiring.
3. O'zingiz uchun kamida 14 belgidan iborat, katta-kichik harflar, sonlar va belgilarni o'z ichiga olgan namunaviy kuchli parol formulasini ishlab chiqing (masalan: sevimli she'r yoki iboraning bosh harflari asosida: `M@kt@b2025#Oqish`).

---

## Mentor uchun

### Baholash mezonlari (100 ballik tizim)

1. **CIA triadasi va sohalar tahlili (30 ball):**
   - Confidentiality, Integrity, Availability mohiyatini to'g'ri tushuntirishi (10 ball);
   - Sohalar bo'yicha ustuvorliklarni (bankda Integrity, 103 da Availability) to'g'ri asoslay olishi (10 ball);
   - Xesh funksiyasi (SHA-256) yaxlitlikni qanday tasdiqlashini amalda ko'rsatishi (10 ball).

2. **MITM va tarmoq xavfsizligi (30 ball):**
   - ARP Spoofing va Man-in-the-Middle ishlash mexanizmini to'g'ri ifodalashi (10 ball);
   - HTTPS va VPN ning MITM ga qarshi qanday himoya qilishini anglashi (10 ball);
   - Statik ARP va DAI usullarini to'g'ri tushuntirishi (10 ball).

3. **Xavfsizlik tafakkuri va parollar siyosati (40 ball):**
   - Security Mindset tamoyillarini (hujumchi va himoyachi kabi fikrlash) to'g'ri qo'llay olishi (15 ball);
   - Nmap va Hydra vositalarining maqsad va vazifalarini bilishi (15 ball);
   - Kuchli parol mezonlari va parol menejerlarining ahamiyatini to'g'ri ochib berishi (10 ball).

### Kutiladigan namunaviy natijalar
- O'quvchi xesh kodining bitta harf o'zgarganda butunlay o'zgarishini o'z ko'zi bilan ko'rgan bo'lishi kerak;
- Parol menejerlaridan foydalanish zarurligini va ochiq Wi-Fi da VPN o'rnini to'liq tushungan bo'lishi lozim.
