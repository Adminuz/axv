# 16-dars. Figma platformasi: imkoniyatlari, afzalliklari va ish muhiti

**Fan:** UX/UI dizayn va Advanced Front-end
**Sinf:** 9-sinf
**Hafta:** 6-hafta, 1-dars (umumiy 16-dars)
**Davomiyligi:** 80 daqiqa
**Manba:** Uslubiy ko'rsatma, II bob, 2.1 «Figma'da interfeys dizayni» (ma'ruza): «Figma platformasining imkoniyatlari va afzalliklari»: bulutda ishlash, real vaqtda yangilanish, platformalararo moslashuvchanlik, loyiha turlari (interfeys elementlari, interaktiv prototiplar, illyustratsiya va vektor grafika), SVG eksport. Fayl tuzilmasi va tezkor tugmalar Figma'ning umumiy ish tartibi bo'yicha qo'shildi; interfeys yangilanishi mumkin.

---

## Darsning maqsadi

O'quvchilarga Figma platformasining imkoniyatlari va afzalliklarini (bulut, real vaqt, kross-platforma), fayl tuzilmasini (Project → File → Page → Frame → Layer), qurilmada ko'rish usulini hamda vektor grafika (Pen, shakllar, SVG eksport) bilan ishlashni o'rgatish va «E-kutubxona» loyihasi faylini tartibli tuzish.

## Kutiladigan natija

- Figma'ning 3 ta afzalligini (bulut, real vaqt, kross-platforma) misollar bilan aytadi;
- Fayl tuzilmasini (File → Page → Frame → Layer) tartibli yaratadi va qatlamlarga nom beradi;
- Desktop va Phone frame yaratib, dizaynni smartfonda ko'rish usulini biladi;
- Pen va shakllar bilan oddiy vektor ikonka chizadi;
- Ikonkani SVG qilib eksport qiladi va nega SVG qulayligini tushuntiradi.

## Kerakli jihozlar

- Kompyuter, brauzer va Figma akkaunti
- 15-darsdagi «E-kutubxona» Figma fayli
- Telefon (ixtiyoriy: Figma ilovasi bilan dizaynni ko'rish uchun)

---

## Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 00–08 | Takrorlash | 15-dars: E-kutubxona header va kategoriya paneli |
| 08–22 | Yangi mavzu 1 | Figma platformasi: nima, nega, kimlar uchun |
| 22–32 | Yangi mavzu 2 | Fayl tuzilmasi: sahifalar, frame, qatlam nomlari |
| 32–38 | Tanaffus + mini-quiz | Slayddagi `.quiz` |
| 38–50 | Yangi mavzu 3 | Qurilmada ko'rish va vektor ikonka chizish |
| 50–75 | Amaliyot | SVG eksport, xatolar, xulosa |
| 75–80 | Xulosa | Tezkor nazorat, uyga vazifa |

---

## Konspekt (mentor aytadigan matn)

### 1. Figma platformasi: imkoniyatlari va afzalliklari

**Figma** — dizaynerlar, marketologlar, menejerlar va dasturchilar uchun qulay, ko'p funksiyali **hamkorlikdagi dizayn platformasi**. Uning uchta asosiy afzalligi: 1) **bulut** — fayllar onlayn saqlanadi, o'zgarishlar real vaqtda yangilanadi, zaxira nusxa va versiya tarixi bor; 2) **kross-platforma** — Windows, Mac, Linux va hatto brauzer orqali ishlaydi, alohida dastur o'rnatish shart emas; 3) **hamkorlik** — jamoa a'zolari bir faylda birga ishlaydi, sharh qoldiradi, dasturchi har doim oxirgi versiyani ko'radi. Figma'da uch turdagi ish bajariladi: **interfeys elementlari va komponentlar** (tugma, menyu, forma), **interaktiv prototiplar** (foydalanuvchi harakatini simulyatsiya qiladi) va **illyustratsiya, vektor grafika** (ikonka). Sketch esa faqat Mac'da ishlaydi: shu farq Figma'ni jamoa ishi uchun qulay qiladi.

Figma'ning bepul tarifi o'quv loyihalar uchun yetarli. Akkaunt ochishda yosh va maktab qoidalariga rioya qiling, mentor yordam beradi.

### 2. Fayl tuzilmasi va qurilmada ko'rish

Figma'da ierarxiya: **Project** (jild) → **File** (fayl) → **Page** (sahifa) → **Frame** (ekran) → **Layer** (qatlam: matn, shakl, rasm). «E-kutubxona» fayli uchun sahifalar: `Cover` (muqova), `Ikonkalar`, `Komponentlar`, `Desktop` va `Mobil`. Har qatlamga ma'noli nom bering (`Header`, `Qidiruv`, `Tugma/Asosiy`): «Rectangle 47» kabi nomlar ishni chalkashtiradi. Frame (`F`) — dizayn ekrani; o'ng panelda Desktop (masalan, 1440 × 1024) va Phone (masalan, 390 × 844) tayyor o'lchamlari bor. Dizaynni **Present** (o'ng yuqoridagi play tugmasi) yoki Figma mobil ilovasi bilan haqiqiy smartfonda ko'rish mumkin: mijozga dizayn qurilmada qanday ko'rinishini darhol ko'rsatasiz.

Tezkor tugmalar: `F` — Frame, `R` — to'rtburchak, `T` — matn, `V` — Move, `H` — Hand, `C` — izoh. Tugmalarni o'rganish ishni 2 barobar tezlashtiradi.

### 3. Vektor ikonka va SVG eksport

**Vektor grafika** nuqtalar va chiziqlar formulasidan iborat: har qanday kattalikda aniq ko'rinadi (rastr rasm — **PNG, JPEG** — kattalashganda xiralashadi). Figma'da vektor chizish: **Pen** (`P`) bilan nuqtalar qo'yiladi, shakllar (`R` to'rtburchak, `O` ellips, `L` chiziq) esa **Boolean** amallar (Union, Subtract, Intersect) bilan birlashtiriladi. Misol: «kitob» ikonkasi — ikki to'rtburchakdan va bitta chiziqdan. Tayyor ikonkani tanlab, o'ng paneldagi **Export** bo'limida **SVG** formatini tanlang: bu fayl keyin veb-saytda ishlatiladi va **rangini CSS orqali o'zgartirish** mumkin. Ikonkalarni bir xil o'lchamda (24 × 24) va bir xil qalinlikdagi chiziq bilan chizing.

Ikonka uchun SVG, foto uchun JPEG, shaffof rasm uchun PNG tanlang. Ikonkani eksportdan oldin Frame ichida o'lchamini tekshiring.

---

## Kod namunasi

«E-kutubxona» faylini tayyorlash ro'yxati:

```text
1. Yangi Design fayl: "E-kutubxona"
2. Sahifalar: Cover, Ikonkalar, Komponentlar, Desktop, Mobil
3. Desktop sahifasida Frame (F): 1440 x 1024, nomi "Bosh sahifa"
4. Mobil sahifasida Frame: 390 x 844, nomi "Bosh sahifa"
5. 15-darsdagi Header va Kategoriya panelini Desktop frame ga ko'chirish
6. Ikonkalar sahifasida 24 x 24 frame lar: kitob, qidiruv, profil, savat
7. Har ikonka: nom (ikonka/kitob) va Export -> SVG
8. Present rejimida dizaynni ko'rib chiqish
```

---

## Amaliy topshiriqlar

### 1-topshiriq (oson). Afzalliklarni sanang
Figma'ning 3 afzalligini va har biriga misol yozing.

**Kutiladigan natija:** 3 afzallik.

**Yechim:** Bulut (fayl onlayn), real vaqt (jamoa birga ishlaydi), kross-platforma (brauzerda ishlaydi).

### 2-topshiriq (oson). Qatlam nomlari
`Rectangle 47` va `Frame 12` o'rniga ma'noli nomlar bering.

**Kutiladigan natija:** Ma'noli nomlar.

**Yechim:** Masalan: Qidiruv maydoni, Bosh sahifa Desktop.

### 3-topshiriq (o'rta). Fayl tuzilmasi
E-kutubxona uchun sahifalar ro'yxatini tuzing.

**Kutiladigan natija:** 5 sahifa.

**Yechim:** Cover, Ikonkalar, Komponentlar, Desktop, Mobil.

### 4-topshiriq (o'rta). Frame o'lchamlari
Desktop va Phone frame uchun o'lchamlarni yozing.

**Kutiladigan natija:** To'g'ri o'lchamlar.

**Yechim:** Desktop 1440 × 1024, Phone 390 × 844.

### 5-topshiriq (qiyin). Kitob ikonkasi
24 × 24 «kitob» ikonkasini 2 shakl va 1 chiziqdan chizish ketma-ketligini yozing.

**Kutiladigan natija:** Ketma-ketlik.

**Yechim:** 1) 24×24 frame; 2) ikki to'rtburchak yonma-yon; 3) o'rtaga chiziq; 4) Union; 5) nomi ikonka/kitob; 6) Export SVG.

### 6-topshiriq (qo'shimcha). Format tanlash
Logotip, foto va shaffof banner uchun formatlarni tanlang.

**Kutiladigan natija:** To'g'ri formatlar.

**Yechim:** Logotip — SVG; foto — JPEG; shaffof banner — PNG.

---

## Tezkor nazorat (dars oxirida)

1. Figma'ning 3 afzalligi? — Bulut, real vaqt, kross-platforma.
2. Fayl ierarxiyasi? — Project, File, Page, Frame, Layer.
3. Frame nima? — Dizayn ekrani.
4. Vektor bilan rastr farqi? — Vektor kattalashganda aniq, rastr xiralashadi.
5. Ikonka uchun format? — SVG.

## Keng tarqalgan xatolar

- Qatlamlarga nom bermaslik.
- Hamma narsani bitta sahifaga tashlash.
- Ikonkalarni turli o'lcham va qalinlikda chizish.
- Ikonka uchun JPEG tanlash.
- Faylni mentorga ko'rsatishda ruxsatni (view) o'rnatmaslik.

## Bilasizmi? (qo'shimcha)

- Figma'da mijoz brauzerda havola orqali dizaynni ko'ra oladi va sharh yoza oladi.
- Tesla Model 3 boshqaruv paneli prototipi Figma'da yaratilgan mashhur misol (uslubiy ko'rsatmadan).
- Figma Community'da minglab bepul shablon va UI kitlar bor.
