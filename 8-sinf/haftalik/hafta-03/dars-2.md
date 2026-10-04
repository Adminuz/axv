# 8-dars. HTML5 multimedia va interaktiv elementlar: `<video>`, `<audio>`, `<figure>`, `<details>`, `<progress>`

**Hafta:** 3 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 8-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarga plaginlarsiz (Flash va boshqalarsiz) veb-sahifaga audio va video integratsiya qilishni (`<video>`, `<audio>`, `<source>`), illyustratsiya va rasmlarga professional izoh beruvchi `<figure>` va `<figcaption>` teglarini hamda zamonaviy interaktiv semantik elementlarni (`<details>`, `<summary>`, `<progress>`, `<meter>`, `<mark>`, `<time>`) to'g'ri qo'llashni o'rgatish.

**Kutiladigan natija:**
- `<video>` va `<audio>` teglari atributlarini (`controls`, `autoplay`, `loop`, `muted`, `poster`) to'g'ri qo'llay oladi.
- Turli brauzerlar uchun bir nechta video formatlarini (`<source src="..." type="video/mp4">`, `webm`) ko'rsata oladi.
- Rasmlarni shunchaki `<img>` emas, balki semantik `<figure>` va `<figcaption>` bilan o'rab izohlaydi.
- JavaScript ishlatmasdan, sof HTML da ochilib-yopiluvchi savol-javob (akkordeon) blokini (`<details>` va `<summary>`) yarata oladi.
- Jarayon foizini ko'rsatish uchun `<progress>`, ma'lum oraliqdagi ko'rsatkichlar uchun `<meter>` teglarini qo'llaydi.
- Matn ichidagi muhim so'zlarni sariq rang bilan ajratish uchun `<mark>`, sanalar va vaqtlarni qidiruv robotlariga tushunarli qilish uchun `<time datetime="...">` dan foydalanadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 7-dars (semantik teglar: header, nav, main, article, footer). «Flash pleyerlar nega yo'qolib ketdi va HTML5 qanday qilib videoni soddalashtirdi?» |
| 10–30 daq | Yangi mavzu: Multimedia | `<video>` va `<audio>` teglari, atributlari, formatlar (mp4, webm, mp3), `<source>` tegi |
| 30–35 daq | Tanaffus | Ko'z va yelka mashqlari |
| 35–50 daq | Yangi mavzu: Interaktiv semantika | `<figure>`, `<figcaption>`, `<details>`, `<summary>`, `<progress>`, `<meter>`, `<mark>`, `<time>` |
| 50–70 daq | Amaliyot | Multimedia va interaktiv savol-javobli (FAQ) sahifa yaratish |
| 70–80 daq | Tezkor nazorat va xulosa | 5 ta savol va uyga vazifani tushuntirish |

---

## 2. Konspekt

### 2.1. Takrorlash (10 daqiqa)
- `<article>` va `<section>` farqi nimada?
- Bitta sahifada nechta `<main>` bo'lishi mumkin?

### 2.2. Vebda multimedia: `<video>` va `<audio>`

HTML5 gacha veb-sahifada video ko'rsatish uchun uchinchi tomon dasturlari (masalan, Adobe Flash Player) o'rnatilishi shart edi. Ular kompyuterni sekinlashtirgan va xavfsizlikka putur yetkazgan.
HTML5 standartida video va audio bevosita brauzerning o'zida plaginlarsiz ishlaydigan bo'ldi:

#### Video o'rnatish:
```html
<video controls width="640" poster="muqova.jpg">
  <source src="dars.mp4" type="video/mp4">
  <source src="dars.webm" type="video/webm">
  Kechirasiz, brauzeringiz ushbu videoni qo'llab-quvvatlamaydi.
</video>
```
Asosiy atributlar:
- `controls`: Videoni boshqarish tugmalarini (play, pause, ovoz balandligi, to'liq ekran) chiqaradi. Busiz video oddiy rasmdek qotib turadi!
- `autoplay`: Sahifa ochilishi bilan videoni avtomatik boshlaydi (aksariyat zamonaviy brauzerlar ovozli videoning avtomatik ijrosini bloklaydi, shuning uchun `muted` bilan birga ishlatiladi).
- `muted`: Videoni ovozsiz qilib qo'yadi.
- `loop`: Video tugagach, uni boshidan qayta aylantiradi.
- `poster`: Video hali qo'yilmasdan oldin ekranda ko'rinib turadigan muqova rasmi.

#### Audio o'rnatish:
```html
<audio controls>
  <source src="musiqa.mp3" type="audio/mpeg">
  <source src="musiqa.ogg" type="audio/ogg">
  Brauzeringiz audioni qo'llab-quvvatlamaydi.
</audio>
```

### 2.3. Rasm va izohlar: `<figure>` va `<figcaption>`

Shunchaki `<img>` qo'yganda, rasm ostidagi matn oddiy `<p>` bo'lib qoladi va ularning bir-biriga bog'liqligi yo'qoladi.
HTML5 da rasm va uning ostidagi ilmiy izohni bitta semantik blokga birlashtirish uchun `<figure>` ishlatiladi:
```html
<figure>
  <img src="monoblok.jpg" alt="Zamonaviy monoblok kompyuteri" width="400">
  <figcaption>1-rasm. Monoblok kompyuterining tashqi ko'rinishi va portlari.</figcaption>
</figure>
```

### 2.4. Interaktiv elementlar: `<details>` va `<summary>`

JavaScript yozmasdan turib, bosganda ochilib-yopiladigan blok yasash mumkin:
```html
<details>
  <summary>HTML5 nima va u qachon qabul qilingan?</summary>
  <p>HTML5 — bu zamonaviy veb-standart bo'lib, 2014-yilda W3C tomonidan rasman qabul qilingan.</p>
</details>
```
Agar sahifa ochilgandayoq uning ochiq turishini xohlasangiz, `<details open>` deb yoziladi.

### 2.5. Indikatorlar va metrikalar: `<progress>` va `<meter>`
- **`<progress>` (Jarayon holati):** Biror amalning qancha qismi bajarilganini (yuklash, vazifa yakuni) foizda ko'rsatadi:
  ```html
  <label for="kurs">Kurs yakunlanishi: 70%</label>
  <progress id="kurs" value="70" max="100"></progress>
  ```
- **`<meter>` (O'lchov shkalasi):** Ma'lum diapazondagi o'lchov ko'rsatkichini (harorat, batareya quvvati, disk to'lishi) ifodalaydi:
  ```html
  <label for="disk">Disk bandligi:</label>
  <meter id="disk" value="85" min="0" max="100" low="30" high="80" optimum="50"></meter>
  ```

### 2.6. `<mark>` va `<time>` teglari
- **`<mark>`:** Matn ichidagi qidirilgan yoki e'tibor qaratilishi kerak bo'lgan so'zni sariq fon bilan ajratib ko'rsatadi.
  ```html
  <p>HTML5 da <mark>semantika</mark> eng muhim mavzudir.</p>
  ```
- **`<time>`:** Sanani inson uchun oddiy matn, qidiruv robotlari va taqvimlar uchun esa xalqaro formatda ko'rsatadi:
  ```html
  <p>Dars vaqti: <time datetime="2026-10-04T14:00">4-oktyabr, soat 14:00</time></p>
  ```

---

## 3. Amaliy topshiriqlar va yechimlari

### 1-topshiriq. Audio va video pleer integratsiyasi
**Vazifa:** Veb-sahifada 1 ta video pleer (boshqaruv tugmalari va muqova rasmi bilan) hamda 1 ta audio pleer yarating.
**Yechim:**
```html
<section>
  <h2>Multimedia darsi</h2>
  <video controls width="480" poster="poster.jpg">
    <source src="intro.mp4" type="video/mp4">
    Videoni ko'rish uchun zamonaviy brauzer ishlating.
  </video>

  <br><br>

  <audio controls>
    <source src="podcast.mp3" type="audio/mpeg">
    Audioni tinglash uchun zamonaviy brauzer ishlating.
  </audio>
</section>
```

### 2-topshiriq. Ko'p beriladigan savollar (FAQ) akkordeoni
**Vazifa:** Veb-sayt uchun `<details>` va `<summary>` yordamida 3 ta savol-javobdan iborat FAQ bo'limini tayyorlang. 1-savol sahifa ochilganda avtomatik ochiq tursin (`open`).
**Yechim:**
```html
<section>
  <h2>Ko'p beriladigan savollar (FAQ)</h2>

  <details open>
    <summary>Kurs qancha davom etadi?</summary>
    <p>Ushbu kurs 12 hafta davomida haftasiga 3 darsdan tashkil etiladi.</p>
  </details>

  <details>
    <summary>Darsda qanday dasturlar kerak bo'ladi?</summary>
    <p>VS Code matn muharriri va zamonaviy Google Chrome brauzeri yetarli.</p>
  </details>

  <details>
    <summary>HTML5 semantik teglari nima uchun kerak?</summary>
    <p>SEO optimallashuvi va screen readerlar orqali to'siqsiz foydalanish uchun kerak.</p>
  </details>
</section>
```

---

## 4. Tezkor nazorat savollari (javoblari bilan)

1. **Savol:** `<video>` tegida `controls` atributi qo'yilmasa nima sodir bo'ladi?
   **Javob:** Video ekranda ko'rinadi, lekin foydalanuvchida play/pause tugmalari va vaqt chizig'i bo'lmaydi, video ishlamay turaveradi.
2. **Savol:** Nima uchun `<video>` ichida bitta emas, bir nechta `<source>` tegi yoziladi?
   **Javob:** Har xil brauzerlar turli video formatlarini (MP4, WebM) qo'llab-quvvatlaydi; birinchi format ochilmasa, brauzer avtomatik ikkinchisini sinab ko'radi.
3. **Savol:** Oddiy `<img>` tegi bilan solishtirganda `<figure>` va `<figcaption>` ning afzalligi nimada?
   **Javob:** Ular rasm va uning ostidagi izoh matnini bitta semantik yaxlit blok sifatida birlashtiradi.
4. **Savol:** JavaScript ishlatmasdan ochilib-yopiluvchi matn yaratish uchun qaysi teglar ishlatiladi?
   **Javob:** `<details>` va uning ichidagi sarlavha uchun `<summary>` teglari.
5. **Savol:** `<progress>` bilan `<meter>` teglari orasidagi farq nima?
   **Javob:** `<progress>` davom etayotgan jarayon foizini (yuklanish), `<meter>` esa qat'iy oraliqdagi statik o'lchov ko'rsatkichini (harorat, batareya quvvati) bildiradi.
