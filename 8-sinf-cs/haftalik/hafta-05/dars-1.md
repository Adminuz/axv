# 13-dars. Bulutli xizmatlar va onlayn hamkorlik vositalari (3-qism): sinxronlash, xavfsizlik va mini-loyiha

**Hafta:** 5 · **Davomiyligi:** 80 daqiqa · **Turi:** mustahkamlash + guruhli mini-loyiha · **II-bob**, 7-dars (hafta ichida 1-dars)

> Manba: o'quv dasturi, 11-mavzu (yakuni): «Bulutli xizmatlar tushunchasi va ularning afzalliklari. Google Drive, OneDrive, Dropbox kabi bulutli saqlash xizmatlari. Onlayn hujjatlar bilan ishlash: Google Docs, Sheets, Slides va Microsoft 365. Fayllarni yuklash, ulashish va ruxsatlarni boshqarish. Onlayn hamkorlik va vazifalarni boshqarish vositalari: Microsoft To Do, Google Tasks, Trello.» Metod: hamkorlikda o'rganish (Peer Learning) va amaliy mashqlar. Ushbu dars — mavzuning 3-qismi: 11–12-darslardagi bilimlarni bitta guruhli loyihada birlashtirish. Sinxronlash, bepul xotira hajmlari va oflayn rejim — dasturdagi «bulutli saqlash xizmatlari» bandini kengaytiruvchi qo'shimcha ma'lumot (xizmatlarning rasmiy ma'lumotlari asosida; hajmlar o'zgarishi mumkin).

## 1. Dars rejasi

**Maqsad:** o'quvchilar bulutli xizmatlar bo'yicha bilimlarini mustahkamlaydi: sinxronlash va oflayn ishlash g'oyasini, bepul xotira hajmlarini, bulutdagi akkaunt va fayllar xavfsizligini tushunadi; guruhda «Bulutdagi sinf loyihasi» mini-loyihasini boshidan oxirigacha bajaradi — umumiy papka, to'g'ri ruxsatlar, onlayn hujjat va taqdimot, Trello doskasi va yakuniy taqdimot.

**Kutiladigan natija:**
- Sinxronlash (qurilma ↔ bulut) va oflayn rejim nima ekanini misol bilan tushuntiradi.
- Google Drive, OneDrive va Dropbox ning bepul hajmini taqqoslaydi va to'lgan xotirani qanday bo'shatishni biladi.
- Bulutdagi ma'lumotlar xavfsizligining 5 qoidasini aytadi (kuchli parol, 2 bosqichli tekshiruv, eng kam ruxsat, ochiq havolalarni tekshirish, begona kompyuterda chiqish).
- Guruhda umumiy papka yaratib, a'zolarga to'g'ri ruxsat beradi va «ruxsatlar auditi» o'tkazadi.
- Docs/Slides + Sheets + Trello dan foydalanib loyihani bajaradi va 2 daqiqada taqdim etadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash | 11–12-darslar: «Bulutmi yoki qurilmami?», ruxsat darajalari, vosita tanlash — tezkor viktorina |
| 10–28 daq | Yangi mavzu | Sinxronlash va oflayn rejim, xotira hajmlari, bulutda xavfsizlik, ruxsatlar auditi |
| 28–33 daq | Tanaffus | Harakatli tanaffus |
| 33–68 daq | Guruhli mini-loyiha | «Bulutdagi sinf loyihasi»: papka → ruxsatlar → hujjat va taqdimot → Trello → taqdimot |
| 68–75 daq | Tezkor nazorat | 5 ta savol |
| 75–80 daq | Xulosa va ko'prik | «Versiya tarixi» → Git: keyingi dars mavzusi |

---

## 2. Dars konspekti

### 2.1. Takrorlash (10 daqiqa)
- Bulut nima? (Fayllar internetdagi kuchli serverlarda saqlanadi, istalgan qurilmadan kiriladi.)
- Uchta ruxsat darajasi: **Ko'ruvchi**, **Izohlovchi**, **Muharrir**. Qachon qaysi biri?
- Shaxsiy ro'yxat uchun qaysi vosita, jamoaviy loyiha uchun qaysi biri? (To Do / Google Tasks — shaxsiy, Trello — jamoa.)

### 2.2. Sinxronlash va oflayn rejim
- **Sinxronlash** — qurilmadagi papka va bulutdagi papkaning avtomatik bir xil holatga keltirilishi. Telefonda rasm o'chirilsa, bulutdan ham o'chadi; kompyuterda fayl o'zgartirilsa, telefonda ham yangilanadi.
- Kompyuter ilovalari: **Google Drive for desktop**, **OneDrive** (Windows ichida tayyor), **Dropbox** ilovasi.
- **Oflayn rejim** — internet yo'qligida hujjatni tahrirlash; internet qaytganda o'zgarishlar bulutga yuklanadi (Google Docs'da oflayn rejim brauzer sozlamasidan yoqiladi).
- Diqqat: sinxronlash — **zaxira nusxa emas**: xato o'chirilgan fayl hamma qurilmadan o'chadi. Qutqaruv — **Savat (Korzina)** va **versiya tarixi**.

### 2.3. Bepul xotira hajmlari

| Xizmat | Bepul hajm | Kimniki | Xususiyati |
|---|---|---|---|
| Google Drive | 15 GB (Gmail va Fotosuratlar bilan umumiy) | Google | Docs, Sheets, Slides bilan birga |
| OneDrive | 5 GB | Microsoft | Windows va Microsoft 365 bilan birga |
| Dropbox | 2 GB | Dropbox | sinxronlash tez va sodda |

Xotira to'lsa: katta videolarni toping (fayllarni hajm bo'yicha saralash), keraksizini o'chiring va **Savatni tozalang** — savatdagi fayllar ham joy egallaydi.

### 2.4. Bulutda xavfsizlik — 5 qoida
1. **Kuchli parol** — kamida 12 belgi, harf, raqam, belgi; har bir xizmatga boshqacha.
2. **2 bosqichli tekshiruv (2FA)** — parol + telefondagi kod. Parol o'g'irlansa ham akkaunt himoyada qoladi (batafsil — 19-dars, kiberxavfsizlik).
3. **Eng kam ruxsat** — faqat kerakli odamga va kerakli darajada (Ko'ruvchi yetarli bo'lsa, Muharrir bermang).
4. **«Havolasi bor har kim»** — faqat ommaviy ma'lumot uchun; shaxsiy hujjatlar, pasport, baholar — hech qachon.
5. **Begona kompyuterda** — kirgandan keyin albatta **Chiqish (Sign out)**; brauzerga parolni saqlatmang.

### 2.5. Ruxsatlar auditi
Vaqti-vaqti bilan «kim nimaga kira oladi?»ni tekshirish:
- Google Drive: faylni tanlash → **Ulashish** → ro'yxatdagi odamlar va «Umumiy kirish» sozlamasi.
- Loyiha tugadi — keraksiz a'zolarni olib tashlash yoki ruxsatni **Ko'ruvchi**ga tushirish.
- «Havolasi bor har kim» → **Cheklangan** ga o'zgartirish.

### 2.6. Mini-loyiha: «Bulutdagi sinf loyihasi»
Guruh (3 kishi) mavzu tanlaydi: «Maktabimizdagi eng yaxshi 5 joy», «Sevimli o'yinlar reytingi» yoki «Sinf ekskursiyasi rejasi».

| Bosqich | Vosita | Natija |
|---|---|---|
| 1. Papka | Drive / OneDrive | `5-hafta_Loyiha_GuruhNomi` umumiy papkasi |
| 2. Ruxsat | Ulashish | a'zolar — Muharrir, mentor — Izohlovchi |
| 3. Reja | Trello (yoki qog'oz) | 3 ustun, kamida 6 karta, mas'ul va muddat |
| 4. Ma'lumot | Sheets | jadval: nom, sabab, ball; `=SUM()` yoki o'rtacha |
| 5. Taqdimot | Slides / PowerPoint onlayn | 5 slayd, har kim kamida 1 ta slayd |
| 6. Izoh | izoh va javob | har kim jamoadoshiga 1 ta izoh |
| 7. Audit | Ulashish oynasi | ochiq havola yo'q, ruxsatlar to'g'ri |

### 2.7. Ko'prik: versiya tarixidan Git'ga
Google Docs'dagi **versiya tarixi** — «kim, qachon, nimani o'zgartirdi»ni saqlaydi. Dasturchilar kod uchun xuddi shu vazifani bajaradigan maxsus tizimdan — **Git** dan foydalanadi, kodni esa **GitHub** bulutida saqlab, jamoa bilan ishlaydi. Bu — keyingi darslar mavzusi.

---

## 3. Amaliy mashg'ulotlar

> 3 kishilik guruh. Akkauntlar bo'lmasa, mentor o'z akkauntida umumiy papka yaratib, sinf kompyuterlarida ochib beradi yoki bosqichlar qog'ozda modellashtiriladi (papka daraxti, ruxsatlar jadvali, 3 ustunli doska).

### 1-mashq (oson). Sinxronlashmi yoki zaxira nusxami?
**Vazifa:** Vaziyatlarga javob bering: (a) telefondagi rasm o'chirildi — bulutda qoladimi (sinxronlash yoqilgan)? (b) fayl xato o'chirildi — qanday qaytarasiz? (c) internet yo'q, lekin hujjatni tahrirlash kerak.

**Yechim:** (a) Yo'q — sinxronlash o'chirishni ham ko'chiradi; (b) bulutdagi **Savat**dan tiklash (Google Drive'da 30 kun saqlanadi) yoki versiya tarixidan; (c) oflayn rejim — internet qaytganda o'zgarishlar yuklanadi.

### 2-mashq (oson). Qaysi xizmat?
**Vazifa:** (a) 10 GB video — qaysi xizmatning bepul hajmi yetadi? (b) Windows kompyuterda o'rnatilgan tayyor bulut; (c) Docs va Sheets bilan bitta akkaunt.

**Yechim:** (a) Google Drive (15 GB; agar Gmail/rasmlar joyni band qilmagan bo'lsa); (b) OneDrive; (c) Google Drive.

### 3-mashq (o'rta). Xavfli sozlamani toping
**Vazifa:** Ulashish ro'yxatini tahlil qiling: `Baholar.xlsx` — «Havolasi bor har kim — Muharrir»; `Gazeta.docx` — 3 ta guruhdosh Muharrir; `Pasport_skan.pdf` — «Havolasi bor har kim — Ko'ruvchi»; `Taqdimot` — o'tgan yilgi 5 ta begona odam Muharrir. Nimani o'zgartirasiz?

**Yechim:** `Baholar` — Cheklangan, faqat kerakli odamlar, Ko'ruvchi; `Gazeta` — to'g'ri; `Pasport_skan` — darhol Cheklangan, umuman bulutda ulashmaslik; `Taqdimot` — begonalarni olib tashlash.

### 4-mashq (qiyin). Guruhli mini-loyiha
**Vazifa:** 2.6-bo'limdagi 7 bosqichni bajaring va 2 daqiqada taqdim eting.

**Yechim (tekshiruv ro'yxati):** umumiy papka bor va to'g'ri nomlangan; a'zolar — Muharrir, mentor — Izohlovchi; Trello'da ≥6 karta, ≥3 tasi «Bajarildi»; Sheets'da jadval va formula; Slides'da 5 slayd, har a'zoning hissasi versiya tarixida ko'rinadi; ≥3 izoh va javob; ochiq havola yo'q.

### 5-mashq (bonus). Xotirani tozalash rejasi
**Vazifa:** Drive «to'lib qoldi» (15 GB dan 14,8 GB band). Joyni bo'shatishning 4 qadamli rejasini yozing.

**Yechim:** 1) fayllarni hajm bo'yicha saralash; 2) keraksiz katta videolarni kompyuterga ko'chirish yoki o'chirish; 3) Gmail'dagi katta ilovali xatlarni o'chirish (Google'da joy umumiy); 4) Savatni tozalash.

---

## 4. Tezkor savollar (Checklist)

1. Sinxronlash nima?
   - **Javob:** Qurilmadagi va bulutdagi fayllarning avtomatik bir xil holatda bo'lishi.
2. Nega sinxronlash zaxira nusxa emas?
   - **Javob:** O'chirish ham hamma qurilmaga ko'chadi; qutqaruv — Savat va versiya tarixi.
3. Google Drive, OneDrive va Dropbox ning bepul hajmi?
   - **Javob:** 15 GB, 5 GB, 2 GB.
4. 2 bosqichli tekshiruv nima beradi?
   - **Javob:** Parol o'g'irlansa ham telefondagi kodsiz akkauntga kirib bo'lmaydi.
5. Loyiha tugagach ulashish bilan nima qilish kerak?
   - **Javob:** Ruxsatlar auditi: keraksiz odamlarni olib tashlash, ochiq havolani Cheklangan qilish.

## 5. Kuchli o'quvchi uchun qo'shimcha

- Google Drive'da **Faollik paneli** (Activity) ni ochib, umumiy papkada kim qachon nimani o'zgartirganini kuzating va 3 jumlali hisobot yozing.
- Trello kartalariga **yorliq (label)** va **tekshiruv ro'yxati** qo'shib, loyiha holatini rang bilan ko'rsating.

## 6. Mentor uchun eslatmalar

- Mini-loyiha vaqtini qat'iy ushlang: 5 daqiqa papka va ruxsat, 10 daqiqa reja va jadval, 15 daqiqa taqdimot, 5 daqiqa audit.
- Bepul hajmlar xizmatlar siyosatiga ko'ra o'zgarishi mumkin — darsdan oldin rasmiy sahifalarda tekshirib qo'ying.
- 2FA ni darsda real akkauntda yoqtirmang — faqat tushuncha; amaliy qismi 19-darsda (kiberxavfsizlik).
- Dars oxirida barcha kompyuterlarda akkauntlardan chiqishni nazorat qiling.
- Ko'prik: versiya tarixini ochib ko'rsating va «Ertaga dasturchilarning versiya tarixi — Git bilan tanishamiz» deb yakunlang.
