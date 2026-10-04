# 6-dars. Photoshop interfeysi va vositalari (2-qism): Tanlash vositalari, qatlamlar va uskunalar

> Professional grafik dizayner hech qachon rasmni buzib o'chirmaydi. U niqoblar (maskalar) va qatlamlar orqali sehrli o'zgarishlar yaratadi!

## Dars xulosasi

- **Tanlash vositalari (Selection Tools):** O'yin obyektlarini fondan ajratish, kesish yoki muayyan sohani bo'yash uchun ishlatiladi:
  - **Marquee Tool (M):** To'rtburchak va doiraviy aniq shakllarni belgilash.
  - **Lasso Tool (L):** Erkin chizish, to'g'ri chiziqli (Polygonal) va rang kontrastiga yopishuvchi magnitli (Magnetic Lasso) uskunalar.
  - **Magic Wand / Quick Selection (W):** Bir xil rangdagi maydonlarni (masalan, bir xil oq yoki yashil fonni) bitta bosishda tanlash.
- **Invert Selection (`Ctrl + Shift + I`):** Tanlangan sohani teskarisiga o'girish (fon tanlangan bo'lsa, qahramonning o'zini tanlab beradi).
- **Chizish va shakl asboblari:**
  - **Brush Tool (B):** Asosiy chizish mo'yqalami (Size, Hardness, Opacity sozlamalari bilan).
  - **Pen Tool (P):** O'yin logotiplari va piktogrammalari uchun silliq vektor konturlarini Bezye egri chiziqlari bilan chizish.
  - **Gradient Tool (G):** Ranglarning biridan ikkinchisiga mayin o'tishi (Linear, Radial).
- **Layer Mask (Qatlam niqobi):** Destruktiv bo'lmagan (faylni buzmaydigan) tahrirlash asosi.
  - *Qora rang:* Qatlamning o'sha qismini ko'rinmas (shaffof) qiladi;
  - *Oq rang:* Yashiringan qismni qayta ko'rsatadi;
  - *Kulrang:* Yarim shaffof qiladi.
- **Blending Modes (Aralashtirish rejimlari):** Qatlamlarning bir-biri bilan optik ta'sirlashuvi:
  - **Multiply:** Qoraytiradi (soyalar uchun).
  - **Screen:** Yoritadi (olov, chaqmoq, neon nurlar uchun).
  - **Overlay:** Kontrast va rang to'yinganligini oshiradi.

---

## Qo'shimcha ma'lumot

### 1. "Marching Ants" (Yuruvchi chumolilar) nima?
Photoshopda biron bir sohani tanlaganingizda (Selection), uning atrofida doimiy qimirlab turuvchi qora-oq chiziq paydo bo'ladi. Dizaynerlar buni erkalab **"Marching Ants"** (Yuruvchi chumolilar) deb atashadi.
Tanlovni bekor qilish uchun klaviaturada shunchaki `Ctrl + D` (Deselect) bosiladi.

### 2. Layer Mask qoidasi: "Black hides, White reveals"
Dunyo dizaynerlarining eng mashhur shiori:
- **"Qora yashiradi, Oq ochadi!"**
Agar siz qahramonning qo'lini o'chirg'ich (Eraser) bilan o'chirib yuborsangiz va ertaga mijoz "yo'q, qo'li tursin" desa, uni qaytarib bo'lmaydi.
Agar Layer Mask bilan qora cho'tkada yashirgan bo'lsangiz, oq cho'tkani olib bitta surtsangiz, qo'l o'z joyida yana paydo bo'ladi!

### 3. Pen Tool va Per Bezye matematikasi
Fransuz muhandisi Per Bezye 1960-yillarda Renault avtomobillari korpusini silliq loyihalash uchun matematik egri chiziqlar formulasini yaratgan.
Bugungi kunda Photoshopdagi `Pen Tool (P)` aynan shu formula asosida ishlaydi: siz 2 ta nuqta qo'yasiz va "mo'ylovchalari"ni tortib, istalgancha silliq va mukammal konturni hosil qilasiz.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Selection (Tanlov)** | Tasvirning faqat ma'lum bir qismini tahrirlash uchun ajratib olingan faol sohasi. |
| **Marquee Tool** | To'g'ri to'rtburchak yoki aylana shaklidagi tanlash uskunasi (`M`). |
| **Lasso Tool** | Erkin qo'l harakati bilan murakkab konturlarni tanlash uskunasi (`L`). |
| **Magic Wand** | Bir xil rangdagi piksellarni bir bosishda avtomatik tanlovchi "sehrli tayoqcha" (`W`). |
| **Invert Selection** | Tanlangan soha bilan tanlanmagan soha o'rnini almashtirish (`Ctrl+Shift+I`). |
| **Layer Mask** | Obyektni o'chirmasdan, qora va oq ranglar orqali ko'rinmas yoki ko'rinuvchi qiluvchi niqob. |
| **Blending Modes** | Ustki qatlam piksellarining ostki qatlam bilan optik qo'shilish algoritmlari. |
| **Multiply** | Oq rangni yo'qotib, qorong'u piksellarni ko'paytiruvchi qoraytirish rejimi. |
| **Screen** | Qora rangni yo'qotib, yorug'likni kuchaytiruvchi yoritish rejimi. |
| **Opacity** | Qatlam yoki cho'tkaning noaniqlik (shaffoflikka qarama-qarshi) darajasi (0–100%). |

---

## Bilasizmi?

- Photoshopda professional rassomlar klaviatura tugmalaridan foydalanish orqali ish unumdorligini **3 barobarga oshiradilar**: bir qo'l doimo klaviaturada (`V`, `B`, `E`, `Space`, `Ctrl`), ikkinchi qo'l esa sichqoncha yoki grafik planshetda bo'ladi!
- `Space` (bo'shliq) tugmasini bosib tursangiz, kursor darhol qo'lchaga (Hand Tool) aylanadi va xolst bo'ylab erkin harakatlanish imkonini beradi.
- Layer Mask texnologiyasi ilk bor qorong'u xonalarda fotoplyonkalarni maxsus qog'oz bilan to'sib (maskalash) nusxalash usulidan raqamli muhitga ko'chirilgan.
- Bezye egri chiziqlari zamonaviy dunyodagi barcha kompyuter shriftlari (TrueType, OpenType) ning asosi hisoblanadi.

---

## Topshiriqlar

### 1. Marquee Tool bilan kvadrat tanlash · oson
Photoshopda mukammal teng tomonli kvadrat tanlash uchun qaysi klaviatura tugmasini bosib turish kerak?
**Kutiladigan natija:** `Shift` tugmasi.

### 2. Selection bekor qilish · oson
Ekranda "yuruvchi chumolilar" (tanlov chizig'i) paydo bo'ldi. Ushbu tanlovni bekor qilish uchun qaysi tezkor tugmalar bosiladi?
**Kutiladigan natija:** `Ctrl + D` (Deselect).

### 3. Magic Wand sezgirligi (Tolerance) · oson
Magic Wand uskunasining `Tolerance` parametri 10 dan 50 ga ko'tarilsa, u tanlaydigan ranglar qamrovi kengayadimi yoki torayadimi?
**Kutiladigan natija:** Sezgirlik oshadi va ko'proq o'xshash rang tuslarini qamrab oladi.

### 4. Invert Selection amaliyoti · o'rta
Siz qahramonning atrofidagi bir xil ko'k osmonni tanladingiz. Qahramonning o'zini yangi qatlamga ko'chirish uchun qaysi 2 ta ketma-ket buyruqni bajarasiz?
**Kutiladigan natija:** `Ctrl + Shift + I` (Invert) va `Ctrl + J` (Layer via Copy).

### 5. Layer Mask va cho'tka ranglari · o'rta
Layer Mask ustida turib:
a) Qora rangli cho'tka bilan surtilsa nima bo'ladi?
b) Oq rangli cho'tka bilan surtilsa nima bo'ladi?
**Kutiladigan natija:** Qora — tasvirni yashiradi, Oq — qayta ko'rsatadi.

### 6. Multiply va soya effekti · o'rta
Nima uchun personajning ostiga tushayotgan soyaning Blending Mode rejimi oddiy Normal emas, balki `Multiply` qilinadi?
**Kutiladigan natija:** Multiply rejimi yerdagi teksturani (o't, qum) yopib qo'ymasdan, uning ustiga tabiiy qorong'ulik beradi.

### 7. Screen va sehrli nur · o'rta
Qora fonda chizilgan olov yoki lazer rasmi bor. Uni o'yin sahnasiga qo'yganda qora fonni kesib o'tirmasdan, qanday qilib 1 soniyada yo'qotish mumkin?
**Kutiladigan natija:** Qatlam rejimini `Screen` qilish kifoya — qora rang to'liq yo'qolib, faqat yorug'lik qoladi.

### 8. Pen Tool bilan o'yin qalqoni chizish · qiyin
O'yin qalqonining silliq qirralarini chizish uchun nima uchun Brush emas, Pen Tool tanlanadi? Uning Anchor Point (tayanch nuqtalari) qanday ishlaydi?
**Kutiladigan natija:** Vektor aniqligi va Bezye tutqichlari yordamida mukammal silliq egri chiziq hosil qilish tahlili.

### 9. Destruktiv va Non-destructive tahrir · qiyin
O'yin qahramoni portretini yaratayotganda nima uchun barcha o'zgarishlar alohida qatlamlarda va maskalarda qilinishi shart? Real o'yin studiyasida bu qanday xatolardan asraydi?
**Kutiladigan natija:** Mijoz yoki art-direktor xohlagan daqiqada o'zgartirish kiritishni so'rashi mumkin; non-destructive usulda hamma narsani noldan chizmasdan tezkor to'g'rilash mumkin.

### 10. Mini O'yin Sahnasi Kollaji · bonus
Photoshopda 4 ta alohida qatlamdan iborat o'yin kollajini loyihalang:
- 1-qatlam: Fon manzarasi;
- 2-qatlam: Qahramon sprayti (fondan ajratilgan);
- 3-qatlam: Qahramon soyasi (`Multiply` rejimida);
- 4-qatlam: Qahramon qurolidan chiqayotgan sehrli nur (`Screen` rejimida).
Loyihaning har bir qatlamidagi sozlamalar va maskalarni yozma tasvirlang.
**Kutiladigan natija:** Mukammal 4 qatlamli kompozitsiya bayoni.
