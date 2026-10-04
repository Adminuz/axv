# 1-dars. Internet qanday ishlaydi? DNS, hosting, domain. Front-end va Back-end

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + kichik amaliyot · **I-bob**, 1-dars

## 1. Dars rejasi

**Maqsad:** o'quvchi sayt manzilini yozganda brauzer, DNS va server o'rtasida nima bo'lishini tushuntira oladi; front-end va back-end farqini biladi.

**Kutiladigan natija:**
- Internet, domain, IP manzil, DNS, hosting, server, brauzer, HTTP/HTTPS tushunchalarini o'z so'zi bilan aytadi.
- «So'rov yo'li»ni (brauzer → DNS → server → brauzer) chizib ko'rsata oladi.
- Front-end va back-end vazifalarini farqlaydi.
- Brauzerda DevTools'ni ochib, sahifa yuklanishini ko'radi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 | Tanishuv | Kurs haqida, o'quvchilarning internetdan foydalanish tajribasi |
| 5–20 | Yangi mavzu 1 | Internet nima, IP manzil, DNS |
| 20–30 | Yangi mavzu 2 | Domain va hosting |
| 30–35 | Tanaffus | |
| 35–45 | Yangi mavzu 3 | HTTP/HTTPS, front-end va back-end |
| 45–70 | Amaliyot | Rolli o'yin, DevTools, birinchi HTML fayl |
| 70–75 | Tezkor nazorat | 5 savol |
| 75–80 | Xulosa va uyga vazifa | |

(Birinchi dars bo'lgani uchun «takrorlash» o'rniga tanishuv berilgan.)

## 2. Konspekt

### 2.1. Tanishuv (5 daqiqa)
Savol: «Bugun ertalab nimalar uchun internetdan foydalandingiz?» (YouTube, Telegram, o'yin, dars). Maqsad: internet ularga allaqachon tanish, bugun «ichida nima bor»ligini ochamiz. Kurs oxirida o'zlari sayt va veb-ilova yasashadi.

### 2.2. Internet nima?
**Internet** — dunyodagi millionlab kompyuter, telefon va serverlarni bir-biriga bog'laydigan ulkan tarmoq. Biz u orqali sayt ko'ramiz, xabar yuboramiz, video tomosha qilamiz.

Taqqoslash: internet — butun dunyo bo'ylab yo'llar tarmog'i. Qurilmalar — uylar. Ma'lumot — yo'llarda yuradigan mashinalar.

**Qurilmalar o'zaro aniq manzillar orqali muloqot qiladi.** Bu manzil — **IP manzil**, masalan `142.250.185.78` (raqamlar to'plami). Har bir uyning ko'cha va uy raqami bo'lgani kabi.

**Server** — doimiy yoqilgan, internetga ulangan kompyuter. U saytning fayllarini saqlaydi va so'rov kelganda jo'natadi.
**Klient (mijoz)** — so'rov yuboruvchi: sizning telefoningiz yoki kompyuteringiz, aniqrog'i brauzer (Chrome, Safari, Firefox).

### 2.3. DNS nima qiladi?
Odam `youtube.com` deb yodlaydi, kompyuter esa IP manzil bilan ishlaydi. **DNS (Domain Name System)** — domen nomini IP manzilga aylantiradigan «telefon kitobi».

Agar DNS bo'lmaganida, har bir saytga kirish uchun uzun raqamlarni yodlash kerak bo'lardi. Taqqoslash: telefonda kontaktni «Ona» deb saqlaysiz, raqamni yodlamaysiz.

### 2.4. Domain (domen)
**Domen** — saytning internetdagi nomi: `google.com`, `mysite.uz`. Domen pulga sotib olinadi va yillik to'lanadi; u ro'yxatdan o'tkazilgandan keyingina sizniki bo'ladi.

Domen tuzilishi: `www.mysite.uz` → `uz` (yuqori daraja domeni), `mysite` (asosiy nom), `www` (subdomen).

### 2.5. Hosting
**Hosting** — saytning fayllari (kod, rasm, ma'lumot) saqlanadigan maxsus joy (server). Hosting saytning doimiy ishlashi va hamma uchun ochiq bo'lishini ta'minlaydi.

Taqqoslash: domen — do'konning manzili va nomi; hosting — do'konning o'zi (bino). Ikkalasi ham kerak.

Hosting turlari (hozircha nomini bilish yetarli, keyinroq chuqur o'tiladi): shared hosting, VPS, cloud, static hosting (Netlify, Vercel).

### 2.6. Sahifa brauzerga qanday keladi? (HTTP/HTTPS)
Brauzerga `https://mysite.uz` yozilganda:

1. Brauzer DNS'dan `mysite.uz` ning IP manzilini so'raydi.
2. DNS IP manzilni qaytaradi.
3. Brauzer shu IP dagi serverga **so'rov (request)** yuboradi.
4. Server kerakli fayllarni (HTML, CSS, JS, rasm) **javob (response)** sifatida qaytaradi.
5. Brauzer fayllarni o'qib, sahifani ekranda chizadi.

**HTTP** — brauzer va server o'rtasidagi «muloqot qoidalari». **HTTPS** — shuning himoyalangan varianti (ma'lumot shifrlanadi; manzil yonidagi qulf belgisi). Parol yoki karta kiritiladigan joyda faqat HTTPS bo'lishi kerak.

### 2.7. Front-end va Back-end
| | Front-end | Back-end |
|---|---|---|
| Qayerda ishlaydi | Foydalanuvchining brauzerida | Serverda |
| Nima ko'rinadi | Ko'rinadigan hamma narsa: matn, rang, tugma | Ko'rinmaydi |
| Vazifasi | Interfeys, joylashuv, dizayn, interaktivlik | Ma'lumotlarni saqlash, hisoblash, foydalanuvchini tekshirish |
| Texnologiyalar (dasturda) | HTML, CSS, JavaScript | Python (Django) va ma'lumotlar bazasi |

Restoran misoli: zal, menyu, ofitsiant — front-end; oshxona va ombor — back-end. Mijoz oshxonani ko'rmaydi, lekin ovqat u yerda tayyorlanadi. **Full-stack** dasturchi ikkalasini ham biladi. Kurs davomida ikkalasini ham o'rganamiz: avval front-end (HTML, CSS, JS), keyin back-end.

## 3. Kod namunalari

Bu dars asosan nazariy. Terminal va DevTools bilan ishlash namunalari:

**a) DNS'ni ko'rish (terminal, macOS/Linux/Windows)**
```bash
nslookup google.com
```
Natijada `Address:` qatorida IP manzil chiqadi (har joyda har xil bo'lishi mumkin). Terminal bo'lmasa — mentor ekranda ko'rsatadi.

**b) Birinchi HTML fayl (amaliyot oxirida)**
```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Salom, internet!</h1>
    <p>Bu mening birinchi sahifam.</p>
  </body>
</html>
```
`salom.html` nomi bilan saqlanadi va brauzerda ochiladi. (Struktura 2-darsda batafsil o'tiladi, bugun faqat «ko'rish uchun».)

## 4. Amaliy topshiriqlar

### Oson — «So'rov yo'li» chizmasi
Daftarga yoki doskaga 4 ta qutini chiz va o'qlar bilan ulang: **Brauzer → DNS → Server → Brauzer**. Har bir o'qqa nima yuborilishini yoz («youtube.com ning IP si?», «IP: ...», «sahifani ber», «HTML, CSS, rasmlar»).
**Kutiladigan natija:** 4 bosqich to'g'ri tartibda, nomlari bilan.
**Yechim:** 2.6-bo'limdagi 1–5 qadamlar.

### O'rta — Rolli o'yin va DevTools
1. Uch o'quvchi rol oladi: **Brauzer**, **DNS**, **Server** (mentor yordam beradi). Brauzer «ertalab.uz» sayti uchun DNS'dan manzil so'raydi, DNS qog'ozdagi jadvaldan IP topadi, Brauzer Serverga boradi, Server «fayl» (qog'oz) beradi. Rollarni almashtirib 2 marta o'ynang.
2. Brauzerda ixtiyoriy saytni oching, `F12` (Mac: `Cmd+Option+I`) → **Network** bo'limi → sahifani yangilang. Nechta fayl yuklanganini sanang va 3 ta fayl turini (html, css, js, rasm) toping.

**Kutiladigan natija:** Network ro'yxatida bir nechta so'rov ko'rinadi; o'quvchi har xil fayl turlarini ko'rsata oladi.
**Yechim:** Birinchi qator odatda asosiy HTML hujjat (`Type: document`). Qolganlari uning ichidagi css, js, rasm.

### Qiyin (kuchli o'quvchi uchun) — Mini-tahlil
Sevimli saytingizni tanlang. Aniqlang: (a) domeni qanday tuzilgan (qaysi qismi nom, qaysi qismi domen zonasi); (b) qaysi qismlari front-end (ko'rinadigan), qaysi funksiyalari back-end'da bo'lishi kerak (kamida 3 tadan: masalan, login, qidiruv natijasi, rasm saqlash); (c) `nslookup` bilan uning IP manzilini toping.
**Kutiladigan natija:** yarim sahifalik izoh.
**Yechim namunasi (youtube.com):** (a) `youtube` — nom, `.com` — zona; (b) front-end: video ro'yxati, tugmalar, pleyer; back-end: akkaunt tekshirish, videolarni saqlash, tavsiyalar; (c) IP har xil bo'ladi.

### Yakuniy — Birinchi sahifa
3.b dagi kodni `salom.html` ga yozing, brauzerda oching, `h1` matnini o'z ismingizga o'zgartiring. (Kod muharriri sifatida mentor tanlagan dastur, masalan VS Code.)

## 5. Tezkor nazorat (5 daqiqa, og'zaki)
1. DNS nima qiladi? *(Domen nomini IP manzilga aylantiradi.)*
2. Domen va hosting o'rtasidagi farq nima? *(Domen — nom/manzil, hosting — fayllar saqlanadigan server.)*
3. Brauzer serverdan nimani oladi? *(HTML, CSS, JS, rasm kabi fayllar.)*
4. HTTPS HTTP dan nimasi bilan farq qiladi? *(Ma'lumotni shifrlaydi, himoyalangan.)*
5. Tugma rangini kim belgilaydi — front-end yoki back-end? Parolni tekshirishni-chi? *(Front-end; back-end.)*

## 6. Uyga vazifa (20–30 daqiqa)
Fayl: `uyga-vazifa.md` ga qarang (1-topshiriq).

## 7. Mentor uchun eslatmalar
- Birinchi dars: muhit (kod muharriri, brauzer) o'rnatilganligini oldindan tekshiring. Muhit o'rnatish dasturdagi mavzu emas; shuning uchun tayyor bo'lmasa, 10 daqiqa ajrating va amaliyotni qisqartiring.
- Terminalga o'quvchilarni majburlamang, `nslookup` ixtiyoriy.
