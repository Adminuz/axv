# 5-hafta: Uyga vazifalar to'plami

Mazkur haftada o'tilgan darslar bo'yicha mustaqil bajarish uchun topshiriqlar. Har bir vazifa 20–30 daqiqaga mo'ljallangan. Barcha fayllarni bitta `5-hafta_Ism` papkasida saqlang — tugma va menyular 6-haftada (HUD va prototip) kerak bo'ladi.

---

## 13-dars: Sprayt sheet (atlas) tayyorlash va optimallashtirish

1. Qahramoningiz uchun idle (2 kadr) va yurish (4 kadr) animatsiyalaridan bitta **128×64 px** sheet tayyorlang: 1-qator — idle, 2-qator — yurish, kataklar 32×32.
2. Oyoq chizig'i (tayanch nuqta) barcha kadrlarda bir xil ekanini gorizontal guide bilan tekshiring.
3. 12-darsdagi obyektlaringizdan (kamida 4 ta) **64×64 px** atlas yig'ing (16×16 kataklar, o'xshashlari bir qatorda).
4. Ikkalasini shaffof PNG, 100% qilib eksport qiling va qoidaga ko'ra nomlang.

**Kutiladigan natija:** `qahramon_sheet_32x32.png`, `obyektlar_atlas_16x16.png` va `.psd` fayllar.

---

## 14-dars: Tugmalar turlari, holatlari (Normal, Hover, Pressed)

1. O'yiningiz uslubida Primary («START») va Secondary («ORTGA») tugmalarni yarating (Rectangle Tool, Corners, Stroke, Text Tool).
2. Har biri uchun Normal, Hover va Pressed holatlarini alohida nomlangan qatlamlarda tayyorlang.
3. Barcha holatlarni bir xil kanvas o'lchamida, shaffof PNG qilib eksport qiling (6 ta fayl).

**Kutiladigan natija:** `btn_start_normal.png` … `btn_ortga_pressed.png` va `.psd` fayl.

---

## 15-dars: Bosh menyu, sozlamalar va pauza menyusi dizayni

1. 1920×1080 hujjatda bosh menyu yarating: «MENU» sarlavhasi, START, Sozlamalar, Chiqish (qizil), Solid Color fon, 2 ta bezak doira.
2. Qatlamlarni `Ctrl + G` bilan guruhlang va nomlang (`Main Menu`).
3. Shu uslubda pauza menyusini chizing: qorong'ilashtirilgan o'yin sahnasi, panel, «PAUZA», Davom etish / Sozlamalar / Bosh menyuga.
4. Ikkala ekranni PNG qilib eksport qiling.

**Kutiladigan natija:** `bosh_menyu.png`, `pauza_menyu.png` va `.psd` fayl.

---

## Mentor uchun

### Baholash mezonlari (Jami 100 ball)
- **13-dars vazifasi (30 ball):** teng kataklar, to'g'ri o'lcham hisobi, bir xil tayanch nuqta, atlasda tartib, shaffof PNG 100%, nomlash qoidasi.
- **14-dars vazifasi (35 ball):** Primary/Secondary ierarxiyasi, 3 holat aniq farqlanadi (kamida 2 belgi bilan), alohida qatlamlar, bir xil kanvas, shaffof PNG.
- **15-dars vazifasi (35 ball):** 3 tugmali vertikal menyu teng oraliqda, sarlavha va fon, guruhlangan va nomlangan qatlamlar, pauza menyusida xira sahna va yagona uslub.

### Eslatma
- `.psd` fayllar ham topshirilsin — qatlam nomlari va guruhlarni tekshirish uchun.
- 6-haftada HUD va prototiplash uchun shu tugma va menyulardan foydalaniladi.
