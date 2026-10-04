# 9-dars. Ranglar nazariyasi va dizayn asoslari (2-qism): Color Picker, Swatches va Gradient bilan ishlash

## Darsning asosiy mazmuni

O'yin dizaynida yaxshi g'oyani professional mahsulot darajasiga olib chiqish uchun dizayn tamoyillariga va rang vositalariga qat'iy tayanish zarur. Ushbu darsda biz Photoshop dasturidagi rang asboblari (Color Picker, Eyedropper, Swatches, Gradient Tool) va o'yin UI/grafikasini yaratishning amaliy usullarini o'rganamiz.

---

## 1. O'yin dizaynining 6 ta asosiy tamoyili

1. **Kompozitsiya va Balans:** Sahnadagi har bir element o'zining vizual og'irligiga ega. Elementlar ekran bo'ylab muvozanatli joylashishi kerak.
2. **Vizual Ierarxiya:** O'yinchi ko'zi eng avval qahramonni, keyin xavfli nishonlarni, so'ngra foydali bonuslarni payqashi zarur.
3. **Kontrast:** Asosiy obyektni fondan ajratish uchun shakl, rang yoki o'lcham farqidan foydalanish.
4. **Proportsiya va Ritm:** Obyektlar o'lchamlarining mutanosibligi va bir maromda takrorlanishi (masalan, platformalar yoki tangalar zanjiri).
5. **Tipografiya:** Interfeysdagi yozuvlarning o'yin janriga mosligi va har qanday sharoitda bir zumda o'qilishi.
6. **Soddalik (Minimalizm):** Ortiqcha chalg'ituvchi bezaklardan qochish.

---

## 2. Photoshop Color Picker va Rang Formatlari

Color Picker oynasi orqali rangni 4 xil tizimda aniq belgilash mumkin:

| Tizim | Tavsifi va parametrlari | O'yindagi qo'llanishi |
|---|---|---|
| **HSB** | **H**ue (Tus 0-360°), **S**aturation (To'yinganlik 0-100%), **B**rightness (Yorqinlik 0-100%) | Rassomlar uchun rang tanlashning eng tabiiy va qulay modeli |
| **RGB** | **R**ed (0-255), **G**reen (0-255), **B**lue (0-255) | Raqamli ekranlar va o'yin dvijoklari (Unity, Godot) uchun standart |
| **HEX** | `#RRGGBB` (16-lik tizimdagi 6 ta belgi, masalan `#FF5500`) | Veb va dasturlash kodlariga rang kiritish uchun qulay |
| **Eyedropper (I)** | Sichqoncha bilan ekrandagi istalgan rangga bosib nusxalash | Referens rasmlardan aniq rang palitrasini o'g'irlamasdan ko'chirib olish |

---

## 3. Swatches (Namunalar) Paneli

Professional loyihalarda ranglar tasodifiy tanlanmaydi — butun o'yin uchun 4–6 ta asosiy rangdan iborat rasmiy palitra tuziladi.

- **Swatches panelini ochish:** `Window -> Swatches`.
- **Yangi rang qo'shish:** Xolstda kerakli rang tanlanadi va Swatches panelidagi `+` (New Swatch) tugmasi bosiladi.
- **Guruhlash:** Palitralarni papkalarga ajratish (masalan, `Desert_Level_Colors`, `Hero_Skin`).
- **Eksport qilish:** Tayyor palitrani `.aco` formati ko'rinishida saqlab, butun jamoaga tarqatish mumkin.

---

## 4. Gradient Tool (G) — 5 xil Gradiyent Turi

Gradiyent — ikki yoki undan ortiq ranglarning bir-biriga mayin va silliq o'tishi.

```
1. Linear (Chiziqli)     =========================> To'g'ri chiziq bo'ylab
2. Radial (Aylanma)       (((((( O ))))))          Markazdan tashqariga doira
3. Angle (Burchakli)      |\ /|                    Markaz atrofida 360° aylanma konus
4. Reflected (Akslangan)  <====== | ======>        Markaziy o'qdan ikki tomonga simmetrik
5. Diamond (Olmos)        /\ \/                    Markazdan romb/olmos shaklida
```

### Gradiyent Muharriri (Gradient Editor):
- **Pastki slayderlar (Color Stops):** Ranglarni belgilaydi.
- **Yuqori slayderlar (Opacity Stops):** Kerakli joylarda shaffoflikni (0% dan 100% gacha) boshqaradi.

---

## Amaliy topshiriqlar

### 1-topshiriq. HEX kodlari bilan ranglarni aniqlash · oson
Photoshop Color Picker oynasini oching va quyidagi HEX kodlar qanday ranglarga mos kelishini aniqlang:
a) `#000000` va `#FFFFFF`;
b) `#FF0000`, `#00FF00`, `#0000FF`;
c) `#FFD700` va `#800080`.

### 2-topshiriq. HSB parametrlarini sozlash · oson
Color Picker'da HSB kataklarini quyidagicha to'ldiring:
- `H: 200°`, `S: 80%`, `B: 90%`.
Hosil bo'lgan rang qaysi ranglar oilasiga mansubligini va o'yinda qaysi elementlar uchun ishlatilishi mumkinligini yozing.

### 3-topshiriq. Eyedropper (I) bilan tabiat rasmidan rang olish · oson
Internetdan tog' yoki o'rmon manzarasi rasmini xolstga joylashtiring. Eyedropper (Pipetka) vositasi yordamida rasmdan 3 xil nuqtani (osmon, tog' cho'qqisi, daraxt barglari) tanlab, ularning HEX kodlarini yozib oling.

### 4-topshiriq. Swatches panelida maxsus o'yin palitrasi yaratish · o'rta
`Window -> Swatches` panelini oching. "Mening_O'yinim" nomli yangi guruh papkasi yarating. Unga o'zaro mos keluvchi 5 ta asosiy rang namunasini (Fon, Personaj, Dushman, Oltin tanga, Xavf) qo'shing.

### 5-topshiriq. Quyosh botishi osmonini Linear Gradient bilan chizish · o'rta
Yangi 1920x1080 hujjat oching. `Gradient Tool (G)` ning Linear turini tanlang. Pastdan yuqoriga qarab sariq, to'q sariq, qizil va to'q binafsha ranglar mayin o'tuvchi quyosh botishi osmonini chizing.

### 6-topshiriq. Radial Gradient bilan sehrli qalqon yaratish · o'rta
Bo'sh qatlam oching. Radial Gradient tanlab, markazda oq-moviy (100% Opacity), chetida esa to'q ko'k (0% Opacity) bo'lgan nurni qahramon markazidan tashqariga torting. Qatlam rejimini `Screen` qilib natijani tahlil qiling.

### 7-topshiriq. Reflected Gradient bilan metall qilich tig'i yaltirashi · o'rta
Qilichning tekis metall tig'i chizilgan to'rtburchak sohani belgilang. `Reflected Gradient` vositasi yordamida o'rtasidan ikki chetiga simmetrik yorug'lik aksi bering (oq-kulrang-oq).

### 8-topshiriq. 3 rangli Health Bar (HP) gradiyentini loyihalash · qiyin
Gradient Editor ichida bitta chiziqli gradiyent yarating: 0% joylashuvda qizil (`#FF0000`), 50% joylashuvda sariq (`#FFFF00`), 100% joylashuvda yashil (`#00FF00`). Ushbu gradiyentni UI salomatlik paneliga qo'llang.

### 9-topshiriq. Vizual ierarxiya bo'yicha o'yin bosh menyusini eskizlash · qiyin
Dizaynning "Vizual ierarxiya" va "Kontrast" qoidalariga asoslanib, o'yin bosh menyusini loyihalang: eng katta va yorqin tugma qaysi bo'lishi kerak, ikkilamchi sozlamalar tugmalari qayerda va qanday rangda joylashishi lozim?

### 10-topshiriq. O'yin palitrasini .aco formatida eksport qilish · bonus
Swatches panelida yaratgan 5 rangli palitrangizni `Export Swatches` buyrug'i orqali kompyuteringizga `.aco` fayli ko'rinishida saqlang. Bu fayl boshqa dizaynerlar bilan ishlashda qanday afzallik berishini tushuntiring.
