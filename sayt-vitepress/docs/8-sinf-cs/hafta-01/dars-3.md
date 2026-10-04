---
title: "3-dars. Axborot o‘lchov birliklari va fayl turlari. Windows operatsion tizimida fayl hamda papkalar yaratish. Tezkor tugmalar (Hot keys)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "8-sinf (Foundation)", "link": "/8-sinf-cs/"}, "week": {"n": 1, "link": "/8-sinf-cs/hafta-01/"}, "g": 3, "title": "Axborot o‘lchov birliklari va fayl turlari. Windows operatsion tizimida fayl hamda papkalar yaratish. Tezkor tugmalar (Hot keys)", "lead": "Nega kompyuterda 1 kilobayt 1000 emas, balki 1024 baytga teng? Har bir fayl ortida qanday kengaytma yashiringan va nima uchun professional dasturchilar sichqonchadan ko'ra tezkor tugmalarni (Hot keys) afzal ko'rishadi? Ushbu darsda axborot hisob-kitoblari va fayllarni boshqarish sirlarini o'rganamiz.", "slide": "/slaydlar/8-sinf-cs/hafta-01/dars-3.html", "tabs": [{"g": 1, "link": "/8-sinf-cs/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/8-sinf-cs/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/8-sinf-cs/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "Operatsion tizimlar va Windows muhitida ishlash", "link": "/8-sinf-cs/hafta-01/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **Bit** — axborotning eng kichik o'lchov birligi (faqat `0` yoki `1`).
- **Bayt** — 8 ta bitdan iborat guruh. 1 bayt xotiraga 1 ta belgi yoki harf sig'adi.
- **Ikkilik karralilik:** $2^{10} = 1024$. Shuning uchun $1 \text{ KB} = 1024 \text{ bayt}$, $1 \text{ MB} = 1024 \text{ KB}$, $1 \text{ GB} = 1024 \text{ MB}$, $1 \text{ TB} = 1024 \text{ GB}$.
- **Fayl** — umumiy nomga ega bo'lgan ma'lumotlar to'plami. U nom va kengaytmadan iborat: `nomi.kengaytma`.
- **Kengaytma (Extension)** — fayl qaysi turga mansubligini va uni qaysi dastur ochishini belgilaydi (`.docx`, `.jpg`, `.mp4`, `.py`, `.exe`).
- **Papka (Katalog)** — fayllarni mavzular bo'yicha tartibga soluvchi daraxtsimon tuzilma.
- **Tezkor tugmalar:** `Ctrl+C` (nusxalash), `Ctrl+X` (qirqish), `Ctrl+V` (qo'yish), `Ctrl+Z` (bekor qilish), `F2` (nomini o'zgartirish), `Delete` (savatchaga tashlash), `Shift+Delete` (butunlay o'chirish).

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### Nega 1000 emas, aynan 1024?
Biz hayotda o'nlik sanoq sistemasidan (0 dan 9 gacha bo'lgan 10 ta raqam) foydalanamiz, shuning uchun bizda 1 kilometr = 1000 metr, 1 kilogramm = 1000 grammdir.
Kompyuter esa faqat ikkilik sanoq sistemasini (faqat 0 va 1) biladi. 2 sonining darajalarini hisoblasak:
$2^1=2$, $2^2=4$, $2^3=8$, $2^4=16$, $2^5=32$, $2^6=64$, $2^7=128$, $2^8=256$, $2^9=512$, $2^{10}=1024$!
Ko'rib turganingizdek, 2 ning darajalari ichida 1000 ga eng yaqin bo'lgan son aynan **1024** dir. Shu sababli kompyuter texnikasida har bir keyingi o'lchov birligi o'zidan oldingisidan 1024 baravar katta bo'ladi.

### Fayl kengaytmalari nega ko'rinmaydi?
Windows operatsion tizimida dastlab yangi o'rnatilganda xavfsizlik va soddalik uchun fayl kengaytmalari yashiringan bo'ladi. Foydalanuvchi faqat `hujjat` nomini ko'radi, ammo uning oxiridagi `.docx` ko'rinmaydi.
Lekin dasturchi va IT mutaxassisi har doim faylning aniq kengaytmasini ko'rib turishi shart! Buni yoqish juda oson:
1. `Win + E` tugmalari bilan File Explorer'ni oching.
2. Yuqoridagi «View» (Ko'rinish) → «Show» menyusiga o'ting.
3. «File name extensions» (Fayl nomining kengaytmalari) bandini yoqing.
Endi har bir faylning haqiqiy yuzi ochiladi!

### Savatcha (Recycle Bin) qanday ishlaydi?
Faylni shunchaki `Delete` tugmasi bilan o'chirganingizda, u diskdan butunlay yo'qolib ketmaydi. U qattiq diskning maxsus himoyalangan qismi — **Savatchaga** ko'chiriladi. Agar siz tasodifan kerakli faylni o'chirib yuborsangiz, istalgan payt Savatchaga kirib, faylni o'ng tugma bilan bosib, «Restore» (Qayta tiklash) qilsangiz, u avvalgi o'z papkasiga qaytadi.
Agar `Shift + Delete` tugmalarini bossangiz, fayl Savatchaga tushmasdan butunlay xotiradan o'chiriladi. Shuning uchun `Shift + Delete` buyrug'ini ishlatishda juda ehtiyot bo'lish zarur!

### Odatiy xato: Fayl kengaytmasini o'zgartirib yuborish
Fayl nomini o'zgartirayotganda (`F2`), agar siz nuqtadan keyingi harflarni ham o'chirib tashlasangiz (masalan, `dars.docx` o'rniga shunchaki `dars` deb yozsangiz), Windows bu faylni qaysi dastur ochishi kerakligini bilmay qoladi va uning belgisi oq qog'ozga aylanadi.
Fayl nomini o'zgartirganda har doim nuqta va uning kengaytmasini (`.docx`, `.png`) tegilmasdan saqlab qolish kerak!

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Bit (Binary digit)** | Axborotning eng kichik o'lchov birligi, faqat 0 yoki 1 qiymatiga ega. |
| **Bayt (Byte)** | 8 ta bitdan iborat axborot birligi, 1 ta belgini saqlashga teng. |
| **Kilobayt (KB)** | 1024 baytga teng axborot o'lchovi. |
| **Megabayt (MB)** | 1024 Kilobaytga teng axborot o'lchovi. |
| **Gigabayt (GB)** | 1024 Megabaytga teng axborot o'lchovi. |
| **Terabayt (TB)** | 1024 Gigabaytga teng yirik axborot o'lchovi. |
| **Fayl** | Kompyuter xotirasida umumiy nom ostida saqlanadigan ma'lumotlar majmuasi. |
| **Kengaytma (Extension)** | Fayl turini belgilovchi va nuqtadan keyin yoziladigan format nomi (masalan, `.jpg`, `.py`). |
| **File Explorer** | Windowsda fayl va papkalarni boshqaruvchi standart dastur (`Win + E`). |
| **Recycle Bin (Savatcha)** | O'chirilgan fayllarni vaqtincha saqlash va qayta tiklash joyi. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

1. Dunyodagi ilk kompyuter qattiq diski (IBM 305 RAMAC, 1956-yil) bor-yo'g'i **5 Megabayt** ma'lumot sig'dirgan va uning og'irligi 1 tonnadan ortiq bo'lgan! Bugungi kunda 5 MB — bu smartfoningizda olingan atigi bitta sifatli rasm hajmiga teng.
2. 1 Terabayt (TB) hajmdagi xotiraga taxminan 250 000 ta fotosurat yoki 500 soatlik HD formatdagi video sig'adi.
3. Klaviaturadagi `Ctrl + C` (nusxalash) va `Ctrl + V` (qo'yish) buyruqlarini 1970-yillarda amerikalik mashhur kompyuter olimi Larri Tesler o'ylab topgan.
4. Bugungi kunda insoniyat har kuni 300 million terabaytdan (300 million GB) ortiq yangi raqamli ma'lumot ishlab chiqaradi!

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Axborot birliklarini saralash <Badge type="tip" text="oson" />
Quyidagi axborot o'lchov birliklarini eng kichigidan boshlab eng kattasiga qarab to'g'ri o'sish tartibida yozing:
`GB`, `Bit`, `TB`, `Bayt`, `KB`, `MB`.
**Kutiladigan natija:** 6 ta birlik to'g'ri ketma-ketlikda yoziladi (Bit → Bayt → KB → MB → GB → TB).

### 2. Fayl turlarini aniqlash <Badge type="tip" text="oson" />
Quyida berilgan 6 ta fayl kengaytmasi qaysi turdagi ma'lumotga (matn, rasm, musiqa, video, dastur) tegishli ekanligini toping:
`.txt`, `.jpg`, `.mp3`, `.mp4`, `.py`, `.exe`.
**Kutiladigan natija:** Har bir kengaytmaning to'g'ri tavsifi jadvalda keltiriladi.

### 3. File Explorer tezkor tugmasi <Badge type="tip" text="oson" />
Klaviaturadagi `Win + E` tugmalarini bosing. Qaysi oyna ochildi? Ochilgan oynaning asosiy bo'limlarini ayting.
**Kutiladigan natija:** Fayl boshqaruvchisi (File Explorer) ochilgani va chap panelda disklar hamda tezkor papkalar ko'ringani yoziladi.

### 4. Yangi papka ochish va nomlash <Badge type="tip" text="oson" />
`Documents` papkasida `Ctrl + Shift + N` tugmalari orqali yangi papka oching va `F2` tugmasi yordamida unga `Kompyuter_Sabog'i` nomini bering.
**Kutiladigan natija:** Yangi papka yaratilib, unga to'g'ri nom beriladi.

### 5. Baytlarni hisoblash <Badge type="warning" text="o'rta" />
«Men Muhammad al-Xorazmiy vorisiman!» jumlasida bo'shliqlar va tinish belgilari bilan birga jami nechta belgi borligini sanang. Ushbu matn kompyuter xotirasida necha bayt va necha bit joy egallashini hisoblang (1 belgi = 1 bayt).
**Kutiladigan natija:** Belgilar soni sanaladi, bayt va bit qiymatlari aniq hisoblab yoziladi.

### 6. MB dan KB ga o'tish hisob-kitobi <Badge type="warning" text="o'rta" />
Sizning sevimli taronangiz hajmi $8 \text{ MB}$ ga teng. Ushbu qo'shiq necha Kilobayt (KB) joy egallaydi? Qadamma-qadam hisoblang ($1 \text{ MB} = 1024 \text{ KB}$).
**Kutiladigan natija:** $8 \times 1024 = 8192 \text{ KB}$ hisobi to'liq ko'rsatiladi.

### 7. Nusxalash va ko'chirish tajribasi <Badge type="warning" text="o'rta" />
Ixtiyoriy matnli fayl yarating.
1. `Ctrl + C` va `Ctrl + V` yordamida uning nusxasini hosil qiling.
2. Boshqa bir yangi papka ochib, `Ctrl + X` va `Ctrl + V` yordamida ikkinchi faylni o'sha yangi papkaga ko'chiring.
3. Nusxalash (Copy) va Ko'chirish (Cut) amallarining amaliy farqini yozing.
**Kutiladigan natija:** Nusxalashda asl fayl o'z joyida qolishi, ko'chirishda esa butunlay yangi manzilga o'tishi qayd etiladi.

### 8. Savatchadan qayta tiklash mashqi <Badge type="warning" text="o'rta" />
Yaratgan faylingizni `Delete` tugmasi orqali o'chiring. Ish stolidan «Recycle Bin» (Savatcha) darchasini oching. O'chirilgan faylni topib, ustida sichqonchaning o'ng tugmasini bosing va «Restore» buyrug'ini bering. Fayl qayerga qaytganini tekshiring.
**Kutiladigan natija:** Fayl o'chirilgan avvalgi asl papkasiga muvaffaqiyatli tiklanadi.

### 9. Katta fleshka sig'imini hisoblash <Badge type="danger" text="qiyin" />
$16 \text{ GB}$ hajmdagi yangi fleshka xarid qilindi.
- Har bir kitob PDF formati o'rtacha $2 \text{ MB}$ hajmda.
- Har bir film Full HD formati o'rtacha $4 \text{ GB}$ hajmda.
Ushbu fleshkaga nechta kitob yoki nechta film sig'ishini alohida-alohida hisoblab chiqing.
**Kutiladigan natija:** Kitoblar soni ($16 \times 1024 / 2 = 8192 \text{ ta}$) va filmlar soni ($16 / 4 = 4 \text{ ta}$) aniq hisoblanadi.

### 10. Fayl manzili (Path) ierarxiyasi <Badge type="danger" text="qiyin" />
Quyidagi daraxtsimon strukturani daftaringizga chizing va `dastur.py` faylining to'liq manzilini (Path) yozing:
`C:` disk ichida `Loyiha` papkasi, uning ichida `Backend` papkasi, uning ichida `dastur.py` fayli joylashgan.
**Kutiladigan natija:** `C:\Loyiha\Backend\dastur.py` to'liq manzili va chizmasi keltiriladi.

### 11. Yashirin kengaytmalarni ochish siri <Badge type="info" text="bonus" />
File Explorer sozlamalariga kirib, «File name extensions» opsiyasini yoqing. Do'stingiz yuborgan `rasm.jpg.exe` nomli faylning nima uchun xavfli bo'lishi mumkinligini va kiberjinoyatchilar nega kengaytmalarni yashirishga urinishini tushuntiring.
**Kutiladigan natija:** Kengaytmasi `.exe` bo'lgan fayl aslida rasm emas, balki virus yoki zararli dastur bo'lishi mumkinligi haqida xavfsizlik xulosasi.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. Bit va bayt nima? 1 baytda nechta bit bor?
2. Nima uchun kompyuterda keyingi axborot birliklari 1000 emas, 1024 marta kattalashadi?
3. Fayl kengaytmasi qanday vazifani bajaradi va u qayerda yoziladi?
4. `Ctrl + C`, `Ctrl + V`, `Ctrl + X` va `Ctrl + Z` tezkor tugmalari nima vazifani bajaradi?
5. `Delete` bilan `Shift + Delete` o'rtasidagi farq nimada?
6. O'chirilgan faylni Savatchadan qanday qayta tiklash mumkin?
7. Fayl nomini o'zgartirish uchun qaysi klaviatura tugmasi ishlatiladi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. Axborot birliklarini kichigidan kattasiga tartiblang: `1 TB`, `500 MB`, `1024 KB`, `8 Bit`, `1 GB`, `2 Bayt`.
2. $4 \text{ GB}$ hajmdagi xotiraga $512 \text{ KB}$ hajmdagi rasm fayllaridan eng ko'pi bilan nechta saqlash mumkinligini hisoblang ($4 \text{ GB} = 4096 \text{ MB} = 4096 \times 1024 \text{ KB}$).
3. Quyidagi tezkor tugmalarni amalda sinab, vazifasini yod oling: `Ctrl+C`, `Ctrl+V`, `Ctrl+X`, `Ctrl+A`, `Ctrl+Z`, `F2`, `Win+E`.
Vazifani bajarishga 20 daqiqa vaqt ajrating.

</div>

