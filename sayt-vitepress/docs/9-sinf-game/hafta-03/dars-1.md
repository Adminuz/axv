---
title: "7-dars. Photoshop interfeysi va vositalari (3-qism): Qatlamlar bilan amaliy ishlash va assetlar kollaji"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Game)", "link": "/9-sinf-game/"}, "week": {"n": 3, "link": "/9-sinf-game/hafta-03/"}, "g": 7, "title": "Photoshop interfeysi va vositalari (3-qism): Qatlamlar bilan amaliy ishlash va assetlar kollaji", "lead": "Photoshop interfeysi va vositalari (3-qism): Qatlamlar bilan amaliy ishlash va assetlar kollaji", "slide": "/slaydlar/9-sinf-game/hafta-03/dars-1.html", "test": "/slaydlar/9-sinf-game/hafta-03/dars-1-test.html", "tabs": [{"g": 7, "link": "/9-sinf-game/hafta-03/dars-1", "current": true}, {"g": 8, "link": "/9-sinf-game/hafta-03/dars-2", "current": false}, {"g": 9, "link": "/9-sinf-game/hafta-03/dars-3", "current": false}], "prev": null, "next": {"g": 8, "title": "Ranglar nazariyasi va dizayn asoslari (1-qism): RGB va CMYK, rang g'ildiragi va rang psixologiyasi", "link": "/9-sinf-game/hafta-03/dars-2"}}
---


<div class="blk">

## <Icon name="file-text" /> Darsning asosiy mazmuni

Professional o'yin studiyalarida 2D san'atkorlar (Game Artists) va Level dizaynerlar yuzlab alohida chizilgan elementlarni bitta sahnaga birlashtiradilar. Ushbu jarayon **Assetlar kollaji (Game Scene Collage)** deb ataladi. 

Kollaj shunchaki rasmlarni ustma-ust qo'yish emas, balki ularni yagona yorug'lik, soya, perspektiva va rang gammasi ostida yaxlit o'yin dunyosiga aylantirish mahoratidir.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. Qatlamlarni tashkil etish va boshqarish

Katta o'yin loyihalarida qatlamlar tartibi quyidagi qoidalar asosida quriladi:

| Amaliyot | Tezkor tugma | Vazifasi va foydasi |
|---|---|---|
| **Qatlamlarni guruhlash** | `Ctrl + G` | Bog'liq qatlamlarni bitta papkaga yig'adi (`Foreground`, `Background`, `UI`). |
| **Guruhni tarqatish** | `Ctrl + Shift + G` | Papka ichidagi qatlamlarni yana alohida holatga keltiradi. |
| **Qatlamni nusxalash** | `Ctrl + J` | Tanlangan qatlam yoki sohaning aniq dublikatini yaratadi. |
| **Qatlamlarni birlashtirish** | `Ctrl + E` | Tanlangan qatlamlarni bitta qatlamga yopishtiradi. |
| **Barcha ko'rinuvchini nusxalash** | `Ctrl + Shift + Alt + E` | Mavjud barcha qatlamlarni buzmasdan, ularning yig'indisini yangi qatlam qilib tepaga qo'yadi (Stamp Visible). |
| **Qulflash (Lock)** | Qulf belgisi | Qatlam tasodifiy siljib ketmasligi yoki ustiga xato chizilmasligi uchun bloklaydi. |

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. Smart Objects (Aqlli Obyektlar)

Oddiy rastr qatlamni kichraytirib, keyin yana kattalashtirsangiz, piksellar qaytarib bo'lmas darajada yo'qoladi va tasvir xiralashadi.

```
[Oddiy Rastr]   100% (Tiniq) ---> 10% (Piksel yo'qoldi) ---> 100% (Loyqa va xira!)
[Smart Object]  100% (Tiniq) ---> 10% (Konteynerda saqlandi) ---> 100% (100% Tiniq!)
```

### Smart Object yaratish:
1. Qatlam ustiga sichqonchaning o'ng tugmasini bosing;
2. Menyu ichidan **Convert to Smart Object** bandini tanlang;
3. Qatlam eskizining pastki o'ng burchagida maxsus piktogramma paydo bo'ladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. Clipping Mask (Qurshov Niqobi)

**Clipping Mask (`Ctrl + Alt + G`)** — bu yuqori qatlamdagi rasm yoki teksturani faqat pastdagi asosiy obyekt shaklining ichidagina ko'rsatish usuli.

- **Asos qatlam (Pastda):** Obyekt shakli (masalan, qahramon, dumaloq qalqon, metall zirh).
- **Qurshov qatlami (Tepada):** Tekstura, yorug'lik aksi, qon yoki loy dog'lari.
- **Natija:** Tekstura qanchalik katta bo'lmasin, pastdagi obyektning chetidan tashqariga bir piksel ham chiqmaydi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 4. O'yin sahnasi kollajining 5 ta oltin qoidasi

1. **Masshtab va Perspektiva:** Qahramon, daraxtlar va uylarning nisbati mantiqan to'g'ri bo'lishi kerak. Uzoqdagi narsalar kichik, yaqindagilar katta bo'ladi.
2. **Kontakt soyalari (Contact Shadows):** Har bir obyekt yer bilan to'qnashgan nuqtasida qoramtir zich soya, atrofida esa tarqoq mayin soya qoldirishi shart (`Multiply` rejimi).
3. **Atrof-muhit yorug'ligi (Ambient Lighting):** Agar sahnada quyosh yoki mash'ala bo'lsa, barcha obyektlarning yoritilgan tomoni bir tomonda bo'lishi shart.
4. **Havo perspektivasi (Atmospheric Fog):** Uzoqdagi ob'yektlar (tog'lar, o'rmonlar) xiralashadi va fon rangiga yaqinlashadi (kamroq kontrast).
5. **Yagona rang korreksiyasi:** Eng ustiga `Curves` yoki `Color Balance` kabi sozlash qatlami (Adjustment Layer) qo'yilib, barcha elementlarning rang harorati birlashtiriladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1-topshiriq. Qatlamlarni guruhlash va tartibga keltirish <Badge type="tip" text="oson" />
Photoshopda yangi hujjat oching. 6 ta bo'sh qatlam yarating va ularni quyidagi tartibda nomlab, 2 ta guruh papkasiga (`Background_Group` va `Hero_Group`) birlashtiring:
`Sky`, `Mountains`, `Ground`, `Hero_Body`, `Hero_Sword`, `Hero_Shadow`.

### 2-topshiriq. Smart Object bilan xavfsiz masshtablash <Badge type="tip" text="oson" />
Ixtiyoriy 2D obyekt rasmini xolstga joylashtiring. Uni Smart Objectga aylantiring. `Ctrl + T` yordamida uni 15% gacha kichraytiring va `Enter` bosing. So'ng yana `Ctrl + T` bilan o'zining dastlabki o'lchamiga qaytaring va tasvir tiniqligini tekshiring.

### 3-topshiriq. Clipping Mask orqali metall qalqon teksturasini yaratish <Badge type="tip" text="oson" />
Dumaloq Shape Tool yordamida qora rangli qalqon doirasi chizing. Uning ustiga metall yoki tosh teksturasi rasmini joylashtiring. `Ctrl + Alt + G` buyrug'i bilan unga Clipping Mask qo'llang va tekstura qalqon doirasidan chiqmaganini kuzating.

### 4-topshiriq. Kontakt soyasini chizish <Badge type="warning" text="o'rta" />
Zamin ustida turgan 2D quti yoki qahramon spraytini joylashtiring. Uning ostiga yangi bo'sh qatlam oching va rejimini `Multiply` qiling. Yumshoq (Hardness 0%) qora cho'tka bilan obyektning yerga tegib turgan nuqtasiga realistik kontakt soyasini chizing.

### 5-topshiriq. Qahramonga sehrli aura nurini qorishtirish <Badge type="warning" text="o'rta" />
Qahramon sprayti orqasiga yangi qatlam oching va rejimini `Screen` qiling. Moviy yoki yashil rangli cho'tka bilan qahramon orqasidan taraluvchi sehrli aura chizing. Opacity parametrini 70% ga sozlang.

### 6-topshiriq. Stamp Visible (Yaxlit bosma qatlam) amali <Badge type="warning" text="o'rta" />
Kamida 4 ta turli qatlamdan iborat kichik kompozitsiya tayyorlang. Barcha qatlamlarning eng yuqorisiga chiqing va `Ctrl + Shift + Alt + E` kombinatsiyasini bosing. Hosil bo'lgan yangi qatlamning xususiyatini tushuntiring.

### 7-topshiriq. Havo perspektivasi effekti <Badge type="warning" text="o'rta" />
3 ta ketma-ket joylashgan tog' tizmasi rasmlarini qatlamlarga joylashtiring. Eng uzoqdagi tog' qatlamining Opacity (shaffoflik) darajasini 40% ga, o'rtadagisini 70% ga, oldingisini esa 100% ga o'rnating. Natijada qanday chuqurlik effekti hosil bo'lganini tahlil qiling.

### 8-topshiriq. 2D Platformer darajasi kollaji <Badge type="danger" text="qiyin" />
Olingan 4 ta elementdan (osmon foni, zamin bloklari, 2D qahramon va yig'iladigan tangalar) foydalanib, 1920x1080 o'lchamda to'liq o'yin darajasi kollajini yig'ing. Barcha qatlamlar guruhlarga ajratilgan, soyalar va nurlar to'g'ri ishlangan bo'lishi shart.

### 9-topshiriq. Adjustment Layer bilan umumiy rangni sovuqlashtirish <Badge type="danger" text="qiyin" />
8-topshiriqda tayyorlangan o'yin sahnasining eng yuqorisiga `Adjustment Layer -> Color Balance` yoki `Photo Filter (Cooling Filter)` qo'shing. Barcha issiq rangli detallarni bir tekisda sirli tun va sovuq qish atmosferasiga o'zgartiring.

### 10-topshiriq. Murakkab qahramon kollaji (Zirh va qurol) <Badge type="info" text="bonus" />
Bitta qahramon tanasiga boshqa rasmdan olingan dubulg'a (shlem), qalqon va olovli qilichni ulab, yangi jangchi personajini kollaj qiling. Clipping mask va Blending modes yordamida elementlar orasidagi ulanish chiziqlarini butunlay ko'rinmas darajada tekislang.

</div>

