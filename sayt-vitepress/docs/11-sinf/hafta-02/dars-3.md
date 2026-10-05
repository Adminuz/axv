---
title: "6-dars. Code Review metodologiyasi, etikasi va Branch Protection"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "11-sinf", "link": "/11-sinf/"}, "week": {"n": 2, "link": "/11-sinf/hafta-02/"}, "g": 6, "title": "Code Review metodologiyasi, etikasi va Branch Protection", "lead": "Eng zo'r kod — bu bir kishi yozgan, lekin butun jamoaning aqli bilan sayqallangan koddir. Code Review nafaqat xatolarni ushlaydi, balki dasturchini tezroq o'stiradi. Ushbu darsda professional muloqot etikasi, \"Nitpick vs Blocker\", GitHub taklif kodi va asosiy tarmoqni qulflash (Branch Protection)ni o'rganamiz.", "slide": "/slaydlar/11-sinf/hafta-02/dars-3.html", "test": "/slaydlar/11-sinf/hafta-02/dars-3-test.html", "tabs": [{"g": 4, "link": "/11-sinf/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/11-sinf/hafta-02/dars-2", "current": false}, {"g": 6, "link": "/11-sinf/hafta-02/dars-3", "current": true}], "prev": {"g": 5, "title": "Pull Request (PR) madaniyati, PR shabloni va Merge konfliktlar", "link": "/11-sinf/hafta-02/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Code Review** — yozilgan kodni asosiy tarmoqqa birlashtirishdan oldin jamoa a'zolari tomonidan tahlil qilinishi va baholanishi.
- Code Review'ning 3 maqsadi: xatolarni erta aniqlash, xavfsizlik zaifliklarini to'sish va jamoada bilim almashish.
- **Review etikasi:** "Odamni emas, kodni tahlil qiling". Buyruq bermasdan, asoslangan savollar bering va yaxshi yechimlarni ham e'tirof eting.
- **Blocker (Kritik to'siq)** — xavfsizlik, buzilgan mantiq yoki qulash xavfi; tuzatmaguncha merge taqiqlanadi (`Request changes`).
- **Nitpick (Mayda maslahat)** — uslub, nomlash yoki bo'sh qatorlar; ixtiyoriy hisoblanadi va PR birlashishini to'xtatmaydi.
- GitHub'dagi ````suggestion```` bloki muallifga to'g'rilangan kodni taklif qiladi va uni bitta tugma bilan commit qilish imkonini beradi.
- **Branch Protection Rules** — `main` tarmog'ini to'g'ridan-to'g'ri pushlardan himoyalash va kamida 1 ta tasdiq (Approve) talab qilish qoidasi.

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Psixologik xavfsizlik va toksik muloqotdan saqlanish
Dasturchilar ko'pincha o'zlari yozgan kodga o'z farzandlaridek bog'lanib qolishadi. Har qanday keskin tanqidiy sharh insonning g'ururiga tegishi yoki uni tushkunlikka tushirishi mumkin.
Shu sababli so'zlarni to'g'ri tanlash — texnik bilimdan kam emas:
- ❌ *"Nega bunday bema'ni sikl yozding?"* (Hujumkor)
- ✅ *"Bu yerdagi ikkinchi sikl katta ma'lumotlarda sekinlashishi mumkin. Keling, buni qanday tezlashtirishni o'ylab ko'ramiz."* (Hamkorlik)

### Reviewer uchun 5 ta nazorat savoli
Hamkasbingizning PR'ini ko'rib chiqayotganda o'zingizga quyidagi savollarni bering:
1. **Mantiq:** Bu kod belgilangan vazifani to'g'ri bajaryaptimi?
2. **Chekka holatlar (Edge Cases):** Bo'sh ro'yxat, nol raqami yoki xato parol kiritilsa nima bo'ladi?
3. **Xavfsizlik:** Kodda ochiq qolgan parollar, shifrlanmagan ma'lumotlar yo'qmi?
4. **O'qilishi:** Bu kodni 6 oydan keyin boshqa odam tushunishi osonmi?
5. **Testlar:** Yangi yozilgan qism uchun unit testlar qo'shilganmi?

### Branch Protection: Hatto xo'jayin ham buza olmaydi!
Professional kompaniyalarda Branch Protection sozlamasida *"Do not allow bypassing the above settings"* (Yuqoridagi cheklovlarni chetlab o'tishga yo'l qo'yilmasin) bandi yoqiladi. Bu hatto repozitoriya egasi yoki bosh direktor bo'lsa ham, o'z kodini kamida bitta muhandis ko'rib tasdiqlamaguncha `main` ga tiqa olmasligini kafolatlaydi!

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Code Review | Kodni birlashtirishdan oldin jamoaviy ko'rib chiqish jarayoni |
| Reviewer | Kodni o'qib, tahlil qilib, fikr bildiruvchi tekshiruvchi |
| Author | Kodni yozgan va Pull Request ochgan muallif |
| Inline Comment | Kodning aynan bitta qatoriga qoldirilgan aniq sharh |
| Code Suggestion | Bir bosishda qabul qilib commit qilinadigan taklif kodi |
| Blocker | Tuzatish majburiy bo'lgan jiddiy xato yoki xavfsizlik teshigi |
| Nitpick (`nit:`) | PR'ni to'xtatmaydigan ixtiyoriy mayda maslahat |
| Approve | Kod ma'qullanganligi va birlashtirishga tayyorligi belgisi |
| Request Changes | Kodda kamchiliklar borligi va tuzatish talabi belgisi |
| Branch Protection | Asosiy tarmoqni to'g'ridan-to'g'ri push va ruxsatsiz o'zgarishlardan qulflash |

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- SmartBear kompaniyasi o'tkazgan tadqiqotga ko'ra, dasturchi bir vaqtning o'zida 200 dan 400 qatorgacha kodni eng yuqori samaradorlik bilan tekshira oladi. 600 qatordan oshgach, xatolarni ilg'ash qobiliyati 70% ga tushib ketadi!
- Bir vaqtlar kodni ko'rib chiqish qog'ozda o'tkazilgan: muhandislar kodni printerdan chiqarib, xonada yig'ilib qizil ruchka bilan tekshirib chiqishgan.
- Hozirgi kunda katta kompaniyalarda PR ochilishi bilanoq sun'iy intellekt linterlari va xavfsizlik botlari odamdan oldin dastlabki tahlilni yakunlab qo'yadi.

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Xushmuomala sharhga aylantiring <Badge type="tip" text="oson" />
Quyidagi qo'pol sharhni professional, konstruktiv va ijobiy sharhga aylantirib yozing:
*"Bu funksiyang juda sekin ishlaydi, umuman o'ylamasdan yozgansan."*

**Kutiladigan natija:** xolis, dalilli va hurmat bilan yozilgan yangi sharh matni.

### 2. Blocker yoki Nitpick? <Badge type="tip" text="oson" />
Quyidagi 4 ta holatni ajrating:
1. Ma'lumotlar bazasi paroli ochiq matnda qolib ketgan;
2. Fayl oxirida bitta bo'sh qator yetishmayapti;
3. Foydalanuvchi hisobida pul yetmaganda ham tovar berib yuborilmoqda;
4. O'zgaruvchi nomi `res` emas, `response` bo'lsa yaxshiroq bo'lardi.

**Kutiladigan natija:** 4 ta to'g'ri tasniflangan band (Blocker / Nitpick) va qisqa sabab.

### 3. GitHub suggestion sintaksisini yozing <Badge type="tip" text="oson" />
GitHub sharh oynasida bir bosishda qabul qilinadigan taklif kodi yaratish uchun Markdown formatida sintaksis yozing (masalan, `x = x + 1` o'rniga `x += 1` taklifi).

**Kutiladigan natija:** to'g'ri formatlangan suggestion kodi bloki.

### 4. Branch Protection qoidasi nimani to'sadi? <Badge type="tip" text="oson" />
Agar `main` tarmog'ida Branch Protection yoqilgan bo'lsa va dasturchi terminaldan `git push origin main` buyrug'ini bersa nima sodir bo'ladi?

**Kutiladigan natija:** Git chiqaradigan xatolik sababining 2 jumlalik tushuntirishi.

### 5. Xavfli kodni tahlil qiling (Security Review) <Badge type="warning" text="o'rta" />
Quyidagi Python kodini ko'rib chiqing va undagi jiddiy xavfsizlik xatosini toping:
```python
def check_admin(password):
    if password == "admin123":
        return True
    return False
```
Ushbu kod muallifiga GitHub inline sharhi shaklida xavfni tushuntiring va xavfsizroq yechim taklif qiling.

**Kutiladigan natija:** xavf tahlili (Hardcoded password) va professional sharh matni.

### 6. GitHub'da `Files changed` yordamida sharh qoldirish <Badge type="warning" text="o'rta" />
O'zingiz yoki do'stingiz ochgan PR'dagi biror qator ustiga bosib, rasmiy inline sharh qoldiring va unga code suggestion biriktiring.

**Kutiladigan natija:** GitHub PR oynasida qoldirilgan taklif kodi skrinshoti.

### 7. Branch Protection qoidasini o'rnatish <Badge type="warning" text="o'rta" />
O'z repozitoriyangizda `Settings → Branches` bo'limiga kiring va `main` uchun kamida 1 ta approve talab qiluvchi qoida yarating.

**Kutiladigan natija:** sozlangan Branch Protection sahifasi skrinshoti.

### 8. Himoyalangan tarmoqni sinash <Badge type="warning" text="o'rta" />
Branch Protection o'rnatilgach, terminaldan `main` tarmog'ida turib to'g'ridan-to'g'ri push qilishga urinib ko'ring. Terminal chiqarib bergan xatolik matnini tahlil qiling.

**Kutiladigan natija:** push rad etilganligi haqidagi terminal chiqishi.

### 9. Katta loyiha uchun "Reviewer Checklist" tuzish <Badge type="danger" text="qiyin" />
Jamoangiz uchun har qanday PR'ni ko'rib chiqishda tekshirilishi shart bo'lgan 5 ta asosiy bo'limdan (Xavfsizlik, Unumdorlik, Kod uslubi, Testlar, Biznes mantiq) iborat mukammal nazorat hujjati (Audit Guide) yozing.

**Kutiladigan natija:** har bir bo'limida kamida 2 tadan aniq mezon bo'lgan professional checklist.

### 10. To'liq Code Review simulyatsiyasi <Badge type="danger" text="qiyin" />
Do'stingiz (yoki o'zingizning ikkinchi akkauntingiz) bilan hamkorlikda PR oching. Unga `Request changes` bering, kamchiliklarni ko'rsating. Muallif ularni to'g'rilagach, tekshirib `Approve` bosing va squash merge qiling.

**Kutiladigan natija:** to'liq sikldan o'tgan PR sahifasining skrinshoti (sharhlar, tuzatishlar va yashil Approve belgisi).

### 11. Botlar yordamida avtomatlashtirilgan review (Linter CI) <Badge type="info" text="bonus" />
GitHub repozitoriyangizga oddiy GitHub Action (masalan, flake8 yoki ESLint linter) ulang. Yangi PR ochilganda kod uslubi avtomatik tekshirilib, xatolik bo'lsa qizil xoch bilan mergeni to'xtatib qo'yishini amalda ko'ring.

**Kutiladigan natija:** PR ostida avtomatik tekshiruv o'tgani yoki xatolik topgani haqidagi CI status skrinshoti.

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Code Review'ning dasturchi shaxsiy o'sishidagi eng katta ahamiyati nimada?
2. "Nitpick" belgisini sharhga qo'yishning qanday madaniy foydasi bor?
3. Code suggestion blokining odatiy matnli izohdan qanday afzalligi mavjud?
4. Qachon `Approve`, qachon esa `Request changes` bosilishi shart?
5. Branch Protection sozlamalarida "Require approvals" nimani kafolatlaydi?
6. Nega buyruq ohangidagi tanqid jamoada samarasiz hisoblanadi?

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

Portfolio loyihangizda `main` tarmog'i uchun Branch Protection qoidasini yoqing (kamida 1 ta approve va to'g'ridan-to'g'ri pushni taqiqlash). Do'stingiz yoki o'zingiz yangi branchdan PR ochib, unga kamida 2 ta inline sharh (biri suggestion bilan) qoldiring va muvaffaqiyatli merge qiling.

</div>

