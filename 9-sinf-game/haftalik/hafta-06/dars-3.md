# 18-dars. O'yin interfeysini prototiplash (2-qism): O'yin stsenariysiga mos interfeys sxemasini chizish

## Dars rejasi

- **Darsning maqsadi:** O'quvchilarga o'yin stsenariysidan kerakli interfeys ekranlarini ajratib olishni, ekranlar o'rtasidagi o'tishlarni sxemada (ekranlar xaritasi) ko'rsatishni, har ekran uchun wireframe tuzishni va uni Photoshop'da guruhlangan qatlamlar bilan chizishni o'rgatish.
- **Kutiladigan natija:** O'quvchilar o'yin stsenariysidan kamida 5 ta kerakli ekranni aniqlaydi; ekranlar xaritasini (qaysi tugma qaysi ekranga olib boradi) chizadi; har bir ekranda ortga qaytish yo'li borligini tekshiradi; har ekran uchun element ro'yxatini (tugma, HUD, matn) tuzadi; photoshop'da ekranlar sxemasini guruhlangan qatlamlar bilan tayyorlaydi.
- **Vaqt taqsimoti:**
  - 17-dars: Wireframe, Mockup, Prototype: 10 daqiqa
  - Stsenariydan ekranlar ro'yxati: 10 daqiqa
  - Ekranlar xaritasi (screen flow): 20 daqiqa
  - Har ekran wireframe'i: 15 daqiqa
  - Amaliyot: Photoshop'da sxema: 25 daqiqa

> Manba: o'quv dasturi — «O'yin interfeysini prototiplash» moduli («o'yin jarayoniga mos interfeys elementlari (tugmalar, menyular, HUD); Photoshopda prototip yaratish jarayoni»; «Tugmalar va menyularni joylashtirib, ekran maketini tayyorlashni o'rganadi»); o'quv qo'llanma — 2.5-bo'lim va Photoshop'da UI yaratish bosqichlari (struktura, foydalanuvchi ssenariylari — User Journey Mapping, past darajali maketlar); uslubiy ko'rsatma — 1.5-mashg'ulot (1920×1080 hujjat, Rectangle Tool, Text Tool, ikonkalar, Ctrl+G). Misol stsenariy («Robo-changyutkich») uslubiy ko'rsatmadagi xona/tanga mashqiga tayanadi.

---

## Mentor konspekti

### 1. O'yin stsenariysidan ekranlar ro'yxati

Interfeys o'yin **stsenariysiga** (o'yinchi nima qiladi, qanday boshlanadi va tugaydi) mos bo'lishi kerak. Birinchi qadam — stsenariyni o'qib, **qaysi ekranlar kerakligini** aniqlash. Qo'llanma Photoshop'da UI yaratish bosqichlarini sanaydi: tuzilmani aniqlash, foydalanuvchi ssenariylarini loyihalash (User Journey Mapping), keyin past darajali maket. **Namunaviy stsenariy:** «Robo-changyutkich xonani aylanib, tanga yig'adi va to'siqlardan qochadi; sog'lig'i tugasa o'yin tugaydi.» Undan ekranlar: 1) **Bosh menyu** (START, Sozlamalar, Chiqish); 2) **O'yin ekrani** (HUD: health bar, tangalar, mini-xarita); 3) **Pauza menyusi** (Davom etish, Sozlamalar, Bosh menyuga); 4) **Sozlamalar** (tovush, grafika, boshqaruv, Ortga); 5) **O'yin tugadi** (natija: yig'ilgan tangalar, Qayta boshlash, Bosh menyuga). Har ekranga nom va qisqa vazifa yoziladi.

```text
1. Bosh menyu     - START, Sozlamalar, Chiqish
2. O'yin ekrani   - HUD: health bar, tangalar, mini-xarita
3. Pauza menyusi  - Davom etish, Sozlamalar, Bosh menyuga
4. Sozlamalar     - Tovush, Grafika, Boshqaruv, Ortga
5. O'yin tugadi   - Natija, Qayta boshlash, Bosh menyuga
```

> Professional maslahat: Savol: «o'yinchi bu lahzada nimani ko'rishi va nimani bosishi kerak?» — har javob bitta ekran elementi bo'ladi.

### 2. Ekranlar xaritasi: qaysi tugma qayerga olib boradi

**Ekranlar xaritasi** (screen flow) — ekranlarni to'rtburchak, o'tishlarni strelka sifatida ko'rsatadigan sxema; har strelkaga o'tishni keltirib chiqaruvchi harakat (tugma) yoziladi. Xaritadan **navigatsiya xatolari** darrov ko'rinadi. Tekshirish qoidalari: 1) har ekrandan **ortga yo'l** bo'lsin (Sozlamalar'da «Ortga» bo'lmasa, o'yinchi chiqa olmaydi); 2) **boshi va oxiri** aniq: o'yin qayerdan boshlanadi (Bosh menyu) va qayerda tugaydi (O'yin tugadi → Bosh menyu yoki Qayta boshlash); 3) **yopiq tuzoq** yo'q (hech qayerga olib bormaydigan ekran); 4) Pauza va Sozlamalar **ikki joydan** ochilishi mumkin — «Ortga» tugmasi qaysi ekranga qaytarishini aniqlang. Xaritani avval qog'ozda chizing, keyin Photoshop'da qutilar va strelkalar bilan qayta yig'ing (Rectangle Tool, Pen Tool/Line).

```text
Bosh menyu --START--> O'yin ekrani --Esc--> Pauza menyusi
    |   ^                  |   ^                |      |
    |   |                  |   +--Davom etish---+      |
    |   +---Bosh menyuga---+--------------------------+
    |                      |
Sozlamalar            sog'liq = 0
    |  ^                   |
  Ortga                    v
                       O'yin tugadi --Qayta boshlash--> O'yin ekrani
```

> Professional maslahat: Bu sxema soddalashtirilgan: asosiy yo'llar ko'rsatilgan. Sozlamalar Pauza menyusidan ham ochilsa, «Ortga» o'sha menyuga qaytaradi.

### 3. Har ekran wireframe'i va Photoshop'da yig'ish

Har ekran uchun **elementlar ro'yxati** va **wireframe** tuziladi. Photoshop'da (uslubiy ko'rsatma 1.5-mashg'ulot asosida): yangi hujjat **1920×1080 px**, RGB; **Rectangle Tool** bilan kulrang qutilar (tugma, panel), **Text Tool** bilan yorliqlar («START», «Sozlamalar»), o'tgan darslardagi ikonkalar (tanga, yurak) o'z joylariga; har ekran elementlari **Ctrl + G** bilan guruhlanadi va ekran nomi beriladi: «1 Bosh menyu», «2 O'yin», «3 Pauza», «4 Sozlamalar», «5 Tugadi». Bir hujjatda ekranlarni yonma-yon qo'yish yoki har ekranni alohida hujjatda saqlash mumkin. Qoidalar: bir xil tugma — bir xil o'lcham va joy; muhim tugma (START, Davom etish) aniq ajralib turadi; HUD 16-darsdagi joylashuvga mos. Bu hali **wireframe** — rang va bezak keyingi dars (19) da, to'liq prototipni yig'ishda qo'shiladi.

```text
+------------------------------+
|        PAUZA                 |
|                              |
|     [ DAVOM ETISH ]          |
|     [ SOZLAMALAR  ]         |
|     [ BOSH MENYUGA ]         |
|                              |
+------------------------------+
Guruh: "3 Pauza"
  Matn: PAUZA
  Tugma x3 (bir xil o'lcham)
```

> Professional maslahat: Eng ko'p kerak bo'ladigan tugma («Davom etish») tepada turadi. Bir ekrandagi tugmalar bir xil o'lcham va oraliqda bo'lsin.

---

## Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Ekranlar ro'yxati (oson)
Namunaviy stsenariydan 5 ta ekranni yozing.

**Bajarish tartibi:**
Bosh menyu; O'yin ekrani (HUD); Pauza menyusi; Sozlamalar; O'yin tugadi.

### 2-topshiriq. O'yin ekrani elementlari (oson)
O'yin ekranida qaysi elementlar bo'lishi kerak?

**Bajarish tartibi:**
Health bar (chap yuqori), tangalar (o'ng yuqori), mini-xarita (o'ng pastki), Pauza tugmasi.

### 3-topshiriq. O'tishlar (o'rta)
«Bosh menyu» dan qaysi ekranlarga o'tish mumkin? Qaysi tugma bilan?

**Bajarish tartibi:**
START → O'yin ekrani; Sozlamalar → Sozlamalar ekrani; Chiqish → o'yindan chiqish.

### 4-topshiriq. Xatoni toping (o'rta)
«Sozlamalar» ekranida faqat Tovush va Grafika bor. Navigatsiya xatosini toping.

**Bajarish tartibi:**
O'yinchi ekrandan chiqa olmaydi. Yechim — «Ortga» tugmasini qo'shish; u kelgan ekranga (Bosh menyu yoki Pauza) qaytaradi.

### 5-topshiriq. Ekranlar xaritasi (qiyin)
5 ekran uchun xaritani chizing; har strelkaga tugma nomini yozing; ortga yo'llarni tekshiring.

**Bajarish tartibi:**
Bosh menyu —START→ O'yin; O'yin —Pauza→ Pauza menyusi —Davom etish→ O'yin; Pauza —Bosh menyuga→ Bosh menyu; O'yin —sog'liq 0→ O'yin tugadi —Qayta boshlash→ O'yin; Bosh menyu va Pauza —Sozlamalar→ Sozlamalar —Ortga→ oldingi ekran.

### 6-topshiriq. Photoshop sxema (bonus)
Pauza menyusi wireframe'ini 1920×1080 px hujjatda chizing va «3 Pauza» guruhiga soling.

**Bajarish tartibi:**
Rectangle Tool bilan 3 ta bir xil kulrang tugma (Davom etish, Sozlamalar, Bosh menyuga), Text Tool bilan sarlavha «PAUZA»; Shift bilan tanlab Ctrl + G; guruhni «3 Pauza» deb nomlang; PNG eksport.

---

## Tezkor nazorat savollari

1. Ekranlar ro'yxati nimaga asoslanadi?
   - *Javob:* O'yin stsenariysiga.
2. Ekranlar xaritasi nima?
   - *Javob:* Ekranlar va ular orasidagi o'tishlar sxemasi.
3. Har ekranda nima bo'lishi shart?
   - *Javob:* Ortga yoki chiqish yo'li.
4. Namunaviy stsenariydan 3 ta ekran ayting.
   - *Javob:* Bosh menyu, O'yin ekrani, Pauza, Sozlamalar, O'yin tugadi.
5. Photoshop'da ekran elementlari qanday tartiblanadi?
   - *Javob:* Ctrl + G bilan guruhlab, nom beriladi.

---

## Uyga vazifa

1. O'z o'yiningiz stsenariysini 3–4 gapda yozing.
2. Stsenariydan kamida 5 ta ekranni ajrating va har biriga 3–4 ta element yozing.
3. Ekranlar xaritasini qog'ozda chizing; har strelkaga tugma nomini yozing; ortga yo'llarni tekshiring.
4. Ikki ekranning wireframe'ini Photoshop'da (1920×1080 px) chizing, har birini guruhlab nom bering.
5. Xaritada chiqishsiz ekran (tuzoq) yo'qligini tekshirib, natijani 2 jumlada yozing.
