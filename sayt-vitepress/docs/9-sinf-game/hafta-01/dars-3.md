---
title: "3-dars. UI va UX ning Game designdagi roli: Interfeys tiplari va HUD arxitekturasi"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Game)", "link": "/9-sinf-game/"}, "week": {"n": 1, "link": "/9-sinf-game/hafta-01/"}, "g": 3, "title": "UI va UX ning Game designdagi roli: Interfeys tiplari va HUD arxitekturasi", "lead": "Eng yaxshi o'yin interfeysi — bu o'yinchi sezmaydigan, ammo har qanday vaziyatda unga ko'maklashadigan ko'rinmas do'stdir!", "slide": "/slaydlar/9-sinf-game/hafta-01/dars-3.html", "test": "/slaydlar/9-sinf-game/hafta-01/dars-3-test.html", "tabs": [{"g": 1, "link": "/9-sinf-game/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/9-sinf-game/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/9-sinf-game/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "O‘yinlarning tarixi va janrlari: O'yin evolyutsiyasi, janrlar tasnifi va madaniy ta'siri", "link": "/9-sinf-game/hafta-01/dars-2"}, "next": null}
---


<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- **UI (User Interface — Foydalanuvchi interfeysi):** O'yinda o'yinchi ko'radigan barcha vizual elementlar to'plami. Tugmalar, menyular, shriftlar, sog'lik panellari, xaritalar va piktogrammalar. (UI = "O'yin qanday ko'rinadi?").
- **UX (User Experience — Foydalanuvchi tajribasi):** O'yinchining o'yin bilan muloqot qilganda his qiladigan qulayligi, intuitiv boshqaruvi, o'yin sur'ati va emotsional qoniqishi. (UX = "O'yin qanday his qilinadi?").
- **O'yin interfeysining 4 ta asosiy tipi:**
  1. **Diyegetik interfeys (Diegetic UI):** O'yin olami va voqeligining ichki qismi. Uni ham o'yinchi, ham o'yin ichidagi bosh qahramon ko'ra oladi (*Dead Space* skafandridagi indikator, *Metro 2033*dagi qo'l soati, *Far Cry 2*dagi qog'oz xarita).
  2. **Nodiyegetik interfeys (Non-Diegetic UI):** O'yin voqeligidan tashqarida bo'lib, bevosita ekran ustiga chiziladi. Qahramon uni ko'rmaydi (*Super Mario*dagi ochkolar va vaqt, *Call of Duty*dagi o'qlar soni).
  3. **Fazoviy interfeys (Spatial UI):** 3D virtual olam fazosida obyektlarga bog'langan holda ko'rsatiladi, ammo qahramonlar undan bexabar bo'ladi (MMORPG'da dushmanlar boshi ustidagi ismlar, nishon belgilari).
  4. **Meta-interfeys (Meta UI):** O'yin olamida mavjud bo'lmagan, lekin qahramonning jismoniy holatini o'yinchiga his qildiruvchi effektlar (ekranning qizarishi, qon sachrashi, muzlashi).
- **HUD (Heads-Up Display):** O'yin jarayonida ekranda doimiy ko'rinib turuvchi barcha axborot panellari majmuasi (Health bar, Mini-map, qurol va o'qlar zaxirasi).
- **Immersiya (Immersion):** O'yinchining virtual o'yin dunyosiga to'liq sho'ng'ishi. Interfeys qanchalik nozik va tabiiy bo'lsa, immersiya darajasi shunchalik yuqori bo'ladi.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. 4 ta interfeys tipi matritsasi
O'yin dizaynerlari interfeysni ikkita savol orqali aniqlaydilar:
1. "Bu element o'yin olamida bormi?" (Hikoyada mavjudmi?)
2. "Bu element 3D o'yin fazosidami yoki tekis ekrandami?"

| | O'yin olamiga tegishli (3D dunyoda bor) | O'yin olamidan tashqarida (Faqat axborot) |
|---|---|---|
| **3D Fazoda joylashgan** | **Diyegetik** (*Skafandr chirog'i, mashina spidometri*) | **Fazoviy (Spatial)** (*Personaj boshi ustidagi ism, nishon*) |
| **2D Ekranga chizilgan** | **Meta-interfeys** (*Ekrandagi qon tomchisi, qahramon ko'zoynagi*) | **Nodiyegetik** (*Klassik sog'lik chizig'i, taymer, ballar*) |

### 2. Yaxshi HUD ning 3 ta oltin qoidasi
1. **Minimalizm va tozalik:** Ekranning 70-80% maydoni o'yin dunyosiga ochiq bo'lishi kerak. Keraksiz bezaklar o'yinchini chalg'itmasin.
2. **Dinamik ko'rinish (Contextual HUD):** O'yinchi tinch joyda yurganda sog'lik yoki qurol panellari avtomatik yo'qolsin; faqat jang boshlanganda yoki o'q otilganda paydo bo'lsin.
3. **Yuqori kontrast:** Qorli oq fonda ham, qorong'u g'orda ham matnlar va raqamlar aniq o'qilishi shart (matnlar atrofida nozik qora hoshiya — stroke qo'llash tavsiya etiladi).

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **UI (User Interface)** | O'yindagi barcha vizual tugmalar, menyular va grafik axborot elementlari. |
| **UX (User Experience)** | O'yinchining o'yin bilan muloqotdagi qulayligi, hissiyoti va umumiy taassuroti. |
| **Diegetic UI** | Ham o'yinchi, ham o'yin qahramoni ko'radigan o'yin olami ichidagi interfeys. |
| **Non-Diegetic UI** | Faqat o'yinchi ekrani ustiga qo'yilgan, qahramonga ko'rinmaydigan interfeys. |
| **Spatial UI** | 3D o'yin fazosidagi obyektlarga bog'langan, ammo virtual dunyoda mavjud bo'lmagan belgilar. |
| **Meta UI** | Qahramon holatini (charchoq, jarohat) ekranda aks ettiruvchi vizual effektlar. |
| **HUD (Heads-Up Display)** | Ekranda doimiy ko'rinib turuvchi tezkor axborot paneli (jon, xarita, o'q). |
| **Immersion (Sho'ng'ish)** | O'yinchining real dunyoni unutib, o'yin olamining bir qismiga aylanib qolish holati. |
| **Feedback (Aks-sado)** | Har bir harakatga o'yinning tovush, vizual yoki tebranish orqali darhol javob qaytarishi. |
| **Wireframe** | Interfeys elementlarining rangsiz, faqat joylashuvini ko'rsatuvchi xom eskizi. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- **HUD (Heads-Up Display)** atamasi dastlab harbiy aviatsiyadan kirib kelgan! Qiruvchi samolyot uchuvchilari boshlarini pastga (asboblarga) egmasdan, to'g'riga qaragan holda ko'rishlari uchun oynaga yashil ma'lumotlar proyeksiyalangan.
- 2008-yilda chiqarilgan mashhur *Dead Space* o'yini barcha klassik nodiyegetik menyulardan voz kechib, 100% diyegetik interfeys yaratgani uchun GameDev sanoatida inqilob yasagan.
- Psixologiyadagi **Fitts qonuni**ga ko'ra, ekranning 4 ta burchagidagi tugmalarni bosish eng oson, chunki kursorni yoki barmoqni chetga surish cheksiz oson. Shuning uchun mini-xarita va asosiy tugmalar har doim burchaklarga joylashtiriladi!
- *Doom* (1993) o'yinida sog'lik ko'rsatkichi uchun raqamlar bilan birga pastda bosh qahramon yuzi ko'rsatilgan: jarohat yetgan sari uning yuzi qonga belanib borgan. Bu video o'yinlar tarixidagi eng dastlabki va mashhur meta-interfeys namunalaridan biri edi.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. UI va UX farqini ifodalash <Badge type="tip" text="oson" />
O'yindagi chiroyli zarhal hoshiyali "Boshlash" tugmasi UI ga kiradimi yoki UX ga? Tugma bosilganda o'yin 3 soniya qotib qolishi nima deb ataladi?
**Kutiladigan natija:** Chiroyli tugma — UI, qotib qolish — yomon UX.

### 2. Diyegetik interfeys misoli <Badge type="tip" text="oson" />
Poyga o'yinida avtomobil tezligini ekranning burchagidagi raqamlar orqali emas, qanday qilib 100% diyegetik usulda ko'rsatish mumkin?
**Kutiladigan natija:** Mashina panelidagi haqiqiy spidometr datchigi orqali.

### 3. Nodiyegetik interfeys afzalligi <Badge type="tip" text="oson" />
Nima sababdan jangovar otishmalarda (CS, Valorant) faqat diyegetik interfeysga tayanmasdan, ekranning burchaklariga nodiyegetik raqamlar (sog'lik, o'qlar) chiqariladi?
**Kutiladigan natija:** Kiberjanglarda sekundning ulushi muhim bo'lib, axborotni darhol va aniq ko'rish talab etiladi.

### 4. Fazoviy (Spatial) interfeysni aniqlash <Badge type="warning" text="o'rta" />
Ko'p kishilik o'yinlarda (masalan, *PUBG* yoki *Fortnite*) sherigingiz yiqilganda uning ustida paydo bo'ladigan qizil xoch va metrlar ko'rsatkichi nima uchun fazoviy interfeys deyiladi?
**Kutiladigan natija:** 3D dunyo ichida joylashgani va obyektga bog'langani sababli.

### 5. Meta-interfeys tahlili <Badge type="warning" text="o'rta" />
O'yin qahramoni suv ostiga sho'ng'iganda o'yinchiga nafas yetishmayotganini ko'rsatuvchi 2 ta meta-interfeys effektini taklif qiling.
**Kutiladigan natija:** Ekranning chetlarida havo pufakchalari paydo bo'lishi, ekran xiralashishi va yurak urishining og'ir audio effekti.

### 6. HUD elementlari muvozanati <Badge type="warning" text="o'rta" />
Tasavvur qiling, o'yin ekrani: mini-xarita, sog'lik, energiya, o'qlar, inventar, vazifalar ro'yxati, kompas va chat bilan to'lib ketdi. Bu o'yinchining immersiyasiga qanday ta'sir qiladi va buni qanday to'g'rilash kerak?
**Kutiladigan natija:** Vizual charchoq va diqqatning bo'linishi; yechim — keraksiz elementlarni yashirish va kontekstli HUD joriy etish.

### 7. Mobil o'yin uchun boshqaruv ergonomikasi <Badge type="warning" text="o'rta" />
Smartfon ekranida o'yinchi ikkala bosh barmog'i bilan o'ynaydi. Ekrandagi eng qulay va eng noqulay zonalar qayerda joylashgan? Eng muhim "Hujum" tugmasi qaysi zonaga qo'yilishi kerak?
**Kutiladigan natija:** Pastki ikki burchak — eng qulay zona (Thumb zone), yuqori o'rta qism — noqulay zona.

### 8. Diyegetik sarguzasht o'yini loyihalash <Badge type="danger" text="qiyin" />
Tarixiy o'g'ri (Ninja) haqidagi o'yinda barcha nodiyegetik elementlarni olib tashlamoqchisiz. Qahramonning:
a) Ko'rinmaslik darajasini (qorong'ulikda ekanini);
b) Qolgan shurikenlar sonini
qanday qilib 100% diyegetik vositalar bilan ko'rsatasiz?
**Kutiladigan natija:** Qorong'ulik — kiyimining rangi yoki oy nuri soyasi orqali; shurikenlar — kamaridagi haqiqiy qurollar soni orqali.

### 9. O'yinda "Feedback" (Qayta aloqa) zanjiri <Badge type="danger" text="qiyin" />
O'yinchi dushmanga zarba berganda, u zarba tekkanini bir zumda bilishi uchun qanday 3 xil (vizual, audio, kinetik) qayta aloqa signallari berilishi lozim?
**Kutiladigan natija:** Vizual: dushman oq rangda miltillashi va qon sachrashi; Audio: zarba ovozi; Kinetik: geympad silkinishi (hit-stop).

### 10. To'liq O'yin HUD Eskizi (Interface Layout) <Badge type="info" text="bonus" />
O'zingiz o'ylab topgan o'yin uchun ekranning to'liq HUD joylashuvini chizing (yoki tasvirlang). Har bir elementning (sog'lik, xarita, qurollar) qaysi burchakka joylashishi va nima uchun aynan o'sha yer tanlanganini mantiqiy asoslab bering.
**Kutiladigan natija:** Ergonomik va muvozanatli HUD arxitekturasi bayoni.

</div>

