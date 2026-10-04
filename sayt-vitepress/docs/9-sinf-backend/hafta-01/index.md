---
title: "1-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "9-sinf (Back-end)", "link": "/9-sinf-backend/"}, "n": 1, "bob": "I-bob · Python dasturlash tili asoslari", "lessons": [{"g": 1, "title": "Python: o‘rnatish, muhit sozlash va ilk dastur", "lead": "Serverlar olamiga xush kelibsiz! Ushbu darsda zamonaviy IT sanoatining eng qudratli tili bo‘lgan Python interpretatorini o‘rnatamiz, terminal bilan do‘stlashamiz va ilk dasturimizni ishga tushiramiz.", "link": "/9-sinf-backend/hafta-01/dars-1", "slide": "/slaydlar/9-sinf-backend/hafta-01/dars-1.html"}, {"g": 2, "title": "Sodda ma’lumot toifalari va arifmetik amallar", "lead": "Kompyuter shunchaki ulkan hisoblagich! Ushbu darsda Pythondagi sodda ma'lumot turlari bilan tanishamiz va butun bo‘lish, qoldiq olish hamda darajaga oshirish kabi amallarni professional darajada o‘rganamiz.", "link": "/9-sinf-backend/hafta-01/dars-2", "slide": "/slaydlar/9-sinf-backend/hafta-01/dars-2.html"}, {"g": 3, "title": "O‘zgaruvchilar va ma'lumotlar bilan ishlash", "lead": "Dastur xotirasi bilan ishlash vaqti keldi! Ushbu darsda o‘zgaruvchilar yaratish, to‘g‘ri nomlash qoidalari va rasmiy qo‘llanmadagi \"Tanishuv kartochkasi\" hamda \"Do‘kon kassasi\" loyihalarini qadamma-qadam quramiz.", "link": "/9-sinf-backend/hafta-01/dars-3", "slide": "/slaydlar/9-sinf-backend/hafta-01/dars-3.html"}]}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Har bir vazifa 20–30 daqiqa. Kodlar alohida `hafta-01` papkasida saqlanadi.

### 1-dars uchun (Python o‘rnatish va ilk dastur)
**1-topshiriq: «Mening ilk dasturim»**
1. Shaxsiy kompyuteringizga Python 3.12+ va VS Code dasturini o‘rnating (Add to PATH belgisi bilan).
2. `salom.py` faylini yarating va unda o‘zingiz, qiziqishlaringiz va backend yo‘nalishini tanlaganingiz sababi haqida kamida 4 qatordan iborat ma'lumotni ekranga chiqaring.
3. Terminalda `python salom.py` buyrug‘i orqali dasturni ishga tushiring.

**Kutiladigan natija:** Dastur konsolda xatosiz bajarilib, matnlarni chiroyli chiqarishi.

### 2-dars uchun (Sodda ma’lumot toifalari va arifmetika)
**2-topshiriq: «Hisob-kitoblar va vaqt konverteri»**
`hisob.py` faylini oching:
1. Tomonlari 18 va 9 bo‘lgan to‘g‘ri to‘rtburchakning yuzi (`*`) va perimetrini hisoblang.
2. 5000 sekund vaqt berilgan. Undan to‘liq soat, daqiqa va qoldiq sekundlarni `//` va `%` yordamida ajratib oling.
3. `2 ** 10` (1 Kilobayt baytlarda) ifodasini hisoblab chiqaring.

**Kutiladigan natija:** Konsolda barcha hisob-kitoblar tushunarli sarlavhalar bilan chiqishi.

### 3-dars uchun (O‘zgaruvchilar va amaliy loyihalar)
**3-topshiriq: «Virtual server profil paneli»**
`server_profil.py` faylini yarating:
1. Quyidagi o‘zgaruvchilarni e'lon qiling:
   - `server_nomi = "FastAPI-Production"`
   - `ip_manzil = "192.168.1.100"`
   - `port = 8000`
   - `ram_gb = 8`
   - `disk_gb = 120`
   - `status_faol = True`
2. f-string yordamida konsolda chiroyli server monitoring kartochkasini chiqaring.
3. "Do‘kon kassasi" dasturini 4 ta mahsulot (non, sut, yog‘, shakar) uchun qayta hisoblab, to‘liq chekni chiqaring.

**Kutiladigan natija:** O‘zgaruvchilar to‘g‘ri nomlangan (snake_case) va hisob-kitoblar to‘g‘ri bajarilgan.

</div>
