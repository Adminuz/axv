# 8-dars. HTML5 multimedia va interaktiv elementlar: video, audio, figure, details, progress

> Veb-sahifani video va audio bilan jonlantirish, rasmlarni ilmiy izohlash hamda JavaScriptsiz sof HTML da interaktiv bloklar yaratish sirlari.

## Dars xulosasi

- **Plaginlarsiz multimedia:** HTML5 gacha videolarni ko'rish uchun Flash pleerlar kerak bo'lgan, HTML5 esa `<video>` va `<audio>` orqali buni brauzerning o'ziga o'rnatdi.
- **`<video>` va `<audio>` atributlari:** `controls` (boshqaruv tugmalari), `autoplay` (avtomatik ijro), `muted` (ovozsiz qilish), `loop` (takrorlash) va `poster` (video muqovasi).
- **Formatlar xilma-xilligi:** Brauzerlar mosligi uchun bitta videoni `<source>` tegi yordamida MP4 va WebM formatlarida taqdim etish eng to'g'ri amaliyotdir.
- **`<figure>` va `<figcaption>`:** Rasmlar, grafiklar va chizmalarni ularning ostidagi matnli izohi bilan bitta semantik bog'lamda birlashtiradi.
- **Interaktiv `<details>` va `<summary>`:** Hech qanday murakkab kod yozmasdan, bosganda ochilib-yopiluvchi zamonaviy akkordeon (FAQ) blokini yasash imkoni.
- **Indikatorlar:** Jarayon bajarilish foizini ko'rsatish uchun `<progress>`, aniq oraliqdagi o'lchovlar uchun `<meter>`, matnni sariq ajratish uchun `<mark>`, vaqtni standartlashtirish uchun `<time>`.

---

## Qo'shimcha ma'lumot

### 1. Nega Flash texnologiyasi tarixga aylandi?

2000-yillarning boshlarida internetdagi barcha o'yinlar, animatsiyalar va videolar Adobe Flash orqali ishlagan. Ammo 2010-yilda Stiv Jobs (Apple asoschisi) mashhur «Thoughts on Flash» maqolasini e'lon qilib, iPhone va iPad qurilmalarida Flash'ni butunlay taqiqladi.
Sabablari:
1. Flash telefonlar batareyasini bir zumda tugatib, qurilmani qizdirib yuborardi.
2. Xavfsizlik teshiklari juda ko'p bo'lib, xakerlar Flash orqali kompyuterga virus yuqtirar edi.
3. Flash sensorli ekranlarga (barmoq bilan boshqarishga) moslashmagan edi.

HTML5 ning `<video>` va `<audio>` teglari chiqishi bilan barcha brauzerlar va smartfonlar Flash'dan voz kechdi va veb butunlay ochiq, xavfsiz va yengil multimedia davriga qadam qo'ydi.

### 2. Autoplay (Avto-ijro) muammosi: Nega video o'z-o'zidan o'ynamaydi?

Ko'pincha yangi boshlagan dasturchilar `<video autoplay controls>` deb yozishadi, lekin sayt ochilganda video baribir boshlanmaydi.
Nega shunday?
Foydalanuvchilar to'satdan baland ovozda baqirib chiquvchi reklamalardan bezor bo'lgani sababli, Google Chrome va boshqa barcha zamonaviy brauzerlar **ovozli videolarning avtomatik ijrosini taqiqlab qo'ygan**.
Agar videongiz sayt ochilishi bilanoq fonda o'ynashini xohlasangiz, albatta `muted` (ovozsiz) atributini qo'shishingiz shart:
```html
<video autoplay muted loop width="100%">
  <source src="fon-video.mp4" type="video/mp4">
</video>
```

### 3. `<details>` va `<summary>` yordamida zamonaviy menyular

Ko'pchilik dasturchilar akkordeon yoki «Ko'proq o'qish» bloklarini yasash uchun yuzlab qator JavaScript kod yozishadi.
Lekin HTML5 buni 3 qatorda hal qiladi:
```html
<details>
  <summary>To'liq ma'lumotni o'qish...</summary>
  <p>Bu yerda maqolaning yashirilgan ikkinchi qismi joylashgan bo'lib, u faqat foydalanuvchi qiziqqanda ko'rinadi.</p>
</details>
```
Agar unga `open` atributini qo'shsangiz (`<details open>`), u boshidan ochiq turadi va bosilganda yopiladi.

### 4. `<progress>` va `<meter>` ning nozik farqi

- **`<progress>`:** O'zgaruvchan jarayon. Masalan, kompyuterga o'yin yuklanyapti yoki anketaning 3 ta qadamidan 2 tasi to'ldirildi. U harakat va rivojlanishni ifodalaydi.
- **`<meter>`:** Muayyan diapazondagi holat. Masalan, xonadagi havo harorati (18 gradus), avtomobil bakidagi benzin miqdori (40 litr) yoki telefondagi batareya quvvati (15%). Unda `low`, `high`, `optimum` kabi qulay chegara atributlari mavjud.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **`<video>`** | Veb-sahifada video fayllarni plaginlarsiz ijro etuvchi HTML5 tegi |
| **`<audio>`** | Ovozli fayllarni (musiqa, podkast, audioyozuv) ijro etish tegi |
| **`controls`** | Pleerda play, pause, ovoz balandligi kabi boshqaruv tugmalarini ko'rsatish atributi |
| **`poster`** | Video qo'yilmasdan oldin pleerda ko'rinib turadigan muqova rasmi manzili |
| **`<source>`** | Brauzer tanlashi uchun pleer ichida turli formatdagi fayllarni ko'rsatish tegi |
| **`<figure>`** | Rasm, illyustratsiya yoki kod blokini o'z ichiga oluvchi semantik qobiq |
| **`<figcaption>`** | `<figure>` ichidagi rasm yoki chizmaning ostiga yoziladigan izoh matni |
| **`<details>`** | Bosilganda ochilib-yopiladigan interaktiv blok tegi |
| **`<summary>`** | `<details>` blokining ko'rinib turadigan sarlavhasi / tugmasi |
| **`<progress>`** | Biror jarayonning bajarilish foizini vizual chiziq tarzida ko'rsatuvchi indikator |
| **`<meter>`** | Muayyan shkala oralig'idagi o'lchov ko'rsatkichini ifodalovchi element |
| **`<mark>`** | Matn ichidagi so'zlarni sariq fonga olib e'tiborni tortuvchi belgilash tegi |
| **`<time>`** | Inson va kompyuter tushunadigan formatda sana hamda vaqtni ko'rsatish tegi |

---

## Bilasizmi?

1. **YouTube va HTML5:** YouTube 2015-yil yanvar oyida o'zining barcha videopleerlarini butunlay Adobe Flash'dan HTML5 `<video>` ga o'tkazganini rasman e'lon qilgan.
2. **Kichik hajm — WebM formati:** Google tomonidan ishlab chiqilgan `WebM` video formati MP4 bilan bir xil sifat beradi, lekin hajmi 30 foizga kichikroq bo'lib, internet trafigini juda tejaydi.
3. **Smartfonlarda video:** Ko'pgina mobil telefonlarda `<video>` tegidagi video to'liq ekran bo'lib ochilmasligi uchun unga `playsinline` atributi qo'shiladi.
4. **Vaqtni qidiruv tizimlariga bildirish:** Agar siz maqola sanasini `<time datetime="2026-10-04">` deb yozsangiz, Google qidiruv natijalarida aynan shu sana chiroyli chiqib turadi.

---

## Topshiriqlar

### 1. Boshqaruv tugmali audio pleer yaratish · oson
O'zingiz yoqtirgan musiqa yoki tabiat tovushini veb-sahifaga joylang. Unda `controls` atributi bo'lsin va agar brauzer audioni qo'llab-quvvatlamasa, ogohlantirish matni chiqsin.
**Kutiladigan natija:** Veb-sahifada ishlovchi standart HTML5 audio pleer.

### 2. Video pleerga muqova (poster) o'rnatish · oson
Kengligi 500 piksel bo'lgan video pleer joylashtiring. Video boshlanishidan oldin uning o'rnida chiroyli rasm (`poster="poster.jpg"`) ko'rinib tursin.
**Kutiladigan natija:** Muqova rasmi va boshqaruv paneliga ega video pleer kodi.

### 3. Rasmni `<figure>` va `<figcaption>` bilan bezash · oson
Kompyuter protsessori (CPU) rasmini veb-sahifaga qo'ying. Rasm ostida «1-rasm. Ko'p yadroli zamonaviy protsessor» degan semantik izoh chiqsin.
**Kutiladigan natija:** `<figure>` va `<figcaption>` teglari to'g'ri birlashtirilgan blok.

### 4. Savol-javobli akkordeon (`<details>`) yaratish · oson
«Bizning to'garaklarimiz» mavzusida 2 ta savol-javobdan iborat akkordeon qiling:
- 1-savol: «Mashg'ulotlar qaysi kunlari o'tkaziladi?» (javob matni ichida).
- 2-savol: «To'garakda nimalar o'rgatiladi?» (javob matni ichida).
**Kutiladigan natija:** Bosganda ochilib-yopiluvchi 2 ta `<details>` bloki.

### 5. Ko'p formatli video (`<source>`) ulash · o'rta
Bitta video pleer yarating va uning ichiga 2 xil formatdagi manbani joylang:
1. `video.mp4` (`type="video/mp4"`).
2. `video.webm` (`type="video/webm"`).
Shuningdek, video tugagach avtomatik boshidan qayta aylansin (`loop`).
**Kutiladigan natija:** Zamonaviy ko'p formatli va tsiklli video pleer kodi.

### 6. Jarayon va o'lchov indikatorlari (`<progress>` va `<meter>`) · o'rta
Shaxsiy profil sahifasi uchun ikkita indikator yarating:
1. «Profilingiz to'ldirildi: 80%» — `<progress>` tegi orqali.
2. «Haftalik mashg'ulot balansi: 10 tadan 7 ta dars» — `<meter>` tegi orqali (`min="0" max="10" value="7"`).
**Kutiladigan natija:** Sahifada chiroyli vizual shkalalarga ega ikkita indikator.

### 7. Matnda `<mark>` va `<time>` teglarini qo'llash · o'rta
Quyidagi gapni HTML da yozing:
«Muhammad al-Xorazmiy vorislari to'garagi 2026-yil 15-oktyabr kuni soat 15:30 da o'z ishini boshlaydi».
- `Muhammad al-Xorazmiy vorislari` iborasi `<mark>` bilan sariq ajratilsin.
- Sana va vaqt esa `<time datetime="2026-10-15T15:30">` tegi bilan qamrab olinsin.
**Kutiladigan natija:** Semantik va vizual jihatdan to'g'ri ajratilgan matnli paragraf.

### 8. Fon videosi (Background Video) maketi · o'rta
Veb-sayt bosh sahifasi (hero section) uchun ovozsiz, o'z-o'zidan cheksiz aylanuvchi fon videosi kodini yozing (`autoplay`, `muted`, `loop`, `width="100%"`). Nima sababdan `muted` siz `autoplay` ishlamasligini izohlang.
**Kutiladigan natija:** Fon videosi uchun to'liq moslashtirilgan video tegi.

### 9. Katta ilmiy maqola uchun multimedia bo'limi · qiyin
Bitta ilmiy maqola bo'limi yarating:
- Maqola ichida bitta mavzuga oid video;
- Ikkita taqqoslovchi rasm (har biri o'zining `<figure>` va `<figcaption>`i bilan);
- Maqola so'ngida ushbu mavzu bo'yicha 3 ta eng ko'p beriladigan savollar akkordeoni (`<details>`);
- Maqola e'lon qilingan vaqt `<time>` tegi bilan.
**Kutiladigan natija:** Boyitilgan multimedia va interaktiv elementlarga ega yaxlit veb-sahifa bo'limi.

### 10. Interaktiv dasturlash qo'llanmasi sahifasi · qiyin
HTML5 teglari haqida o'quv qo'llanmasi sahifasini loyihalashtiring:
- Yuqorida kurs o'zlashtirish darajasini ko'rsatuvchi `<progress>` indikatori (masalan: 65%);
- Har bir mavzu (semantika, formalar, multimedia) `<details>` ichida yashirilgan bo'lsin, bosilganda uning qisqacha konspekti va kodi chiqsin;
- Har bir blokda teg nomi `<mark>` bilan ajratilsin.
**Kutiladigan natija:** Toza semantika va qulay interfeysga ega interaktiv o'quv sahifasi.

### 11. Multimedia yuklanish tezligini optimallashtirish tadqiqoti · bonus
Internetdan 100 MB hajmli video va 5 MB hajmli videoni veb-saytga joylashtirishdagi farqni tahlil qiling:
- Qaysi video formatlari internetda eng tez yuklanadi?
- `preload="none"`, `preload="metadata"` va `preload="auto"` atributlari videoning yuklanish tezligi va internet trafigiga qanday ta'sir qiladi?
Daftaringizda qisqa tadqiqot hisoboti yozing.
**Kutiladigan natija:** Video optimallashtirish va `preload` atributi bo'yicha mustahkam texnik bilim.

---

## O'zingizni tekshiring

1. HTML5 chiqishidan oldin vebda videoni ko'rish uchun qanday texnologiyalardan foydalanilgan va ularning qanday kamchiliklari bo'lgan?
2. `<video>` tegida `controls` bo'lmasa video qanday ko'rinishda bo'ladi?
3. Zamonaviy brauzerlarda `autoplay` ishlashi uchun videoga qaysi atribut majburiy qo'shilishi kerak?
4. Oddiy `<img>` tegidan ko'ra `<figure>` va `<figcaption>` qanday ustunlikka ega?
5. JavaScript ishlatmasdan ochiluvchi blok yasashda `<details>` va `<summary>` qanday vazifalarni taqsimlaydi?
6. `<progress>` va `<meter>` teglari orasidagi farqni misollar bilan tushuntiring.
7. `<time>` tegining `datetime` atributi nima maqsadda ishlatiladi?

---

## Uyga vazifa

1. **Nazariy takrorlash:** Multimedia va interaktiv elementlar konspektini o'qib chiqing.
2. **Video amaliyoti:** Kompyuteringizdagi kichik bir video faylni (yoki internetdan yuklangan namuna videoni) veb-sahifaga `controls` va `poster` bilan joylashtiring.
3. **FAQ akkordeoni:** O'zingiz yoqtirgan biror dasturlash tili (masalan, Python yoki HTML) bo'yicha 3 ta savol va javobdan iborat `<details>` akkordeonini yarating.
4. **Indikator qo'shish:** Sahifa tepasiga «Mening HTML5 ni o'rganish darajam» nomli `<progress value="75" max="100">` progress chizig'ini joylashtiring.
