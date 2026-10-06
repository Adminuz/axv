# 15-dars. UI kit amaliyoti: «E-kutubxona» header va kategoriya paneli

> Nazariya tugadi — endi qo'l ishi! Bugun Figma'da haqiqiy elektron kutubxona sahifasining eng muhim ikki qismini yasaysiz: qidiruvli header va kategoriyalar paneli. Har bir piksel, rang va burchak aniq qiymat bilan beriladi.

## Dars xulosasi

- **Qidiruv maydoni:** Rectangle, Fill **oq**, **Corner radius 25** — yumaloq «pill» shakl.
- **Qidiruv tugmasi:** **50 × 50**, sariq, **opacity ≈ 47%**, radius 25; ichida lupa ikonka (**Fill → Image + Crop**).
- **«Kirish»:** shrift **Inter, 25 px**; profil ikonka **38 × 38**, savat ikonka; ko'rinish **Exposure** bilan sozlanadi.
- **Line:** stroke qora, **2 px**, **Center** — bo'limlarni ajratadi.
- **Kategoriya paneli:** Fill oq, Stroke qora **1 px Inside**, **Drop shadow**; ichida ajratuvchi chiziqlar, nomlar va **«more categories»**.
- **Red guides** (Alt/Option) — masofalarni tekshirish.
- Hamma element **yagona uslubda**: bir xil ranglar, shrift, radius va oraliqlar.

## Qo'shimcha ma'lumot

### Design paneli xaritasi
| Bo'lim | Nima sozlanadi |
|---|---|
| W / H | eni va bo'yi |
| X / Y | sahifadagi joylashuv |
| Corner radius | burchaklarni silliqlash |
| Fill | rang yoki rasm (Image) |
| Stroke | chegara: rang, qalinlik, Inside/Center/Outside |
| Effects | Drop shadow, Inner shadow, Blur |

### Radius siri
Balandlik **50 px** bo'lsa, radius **25** (yarmi) — burchaklar yarim doira bo'lib, element to'liq yumaloq ko'rinadi. 40 px balandlik uchun — 20.

### Foydali tugmalar
- **R** — Rectangle, **L** — Line, **T** — Text.
- **Alt (Option)** bosib turish — red guides (masofa).
- **Ctrl/Cmd + Alt/Option + K** — komponent yaratish.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Header | Sahifaning yuqori paneli |
| Search field | Qidiruv maydoni |
| Corner radius | Burchak silliqlik radiusi |
| Fill → Image | Shakl ichiga rasm joylash |
| Crop | Rasmni kesib moslash |
| Exposure | Rasm yorug'ligini sozlash |
| Stroke | Shakl chegarasi (chiziq) |
| Inside / Center / Outside | Stroke joylashuvi |
| Drop shadow | Tashqi soya effekti |
| Red guides | Figma'dagi qizil o'lchov chiziqlari |

## Bilasizmi?

- Foydalanuvchilar sayt header'ida qidiruvni odatda yuqori markazda yoki o'ng tomonda kutishadi — shuning uchun uni u yerga qo'yamiz.
- Dumaloq «pill» shakldagi qidiruv maydoni Google, Amazon kabi ko'plab yirik saytlarda uchraydi.
- Figma'da «Stroke Inside» panel o'lchamini o'zgartirmaydi — shuning uchun panellarda ko'pincha aynan shu tanlanadi.

## Topshiriqlar

### 1. Frame · oson

1440 × 1024 Desktop frame yarating va unga `E-kutubxona` nomini bering.

**Kutiladigan natija:** nomlangan frame.

### 2. Qidiruv maydoni · oson

600 × 50 oq Rectangle, Corner radius 25.

**Kutiladigan natija:** yumaloq qidiruv maydoni.

### 3. Qidiruv tugmasi · oson

50 × 50 sariq (opacity 47%) dumaloq tugmani maydonning o'ng tomoniga qo'ying.

**Kutiladigan natija:** maydonga tekislangan tugma.

### 4. Lupa · oson

Fill → Image orqali lupa ikonkasini yuklang va Crop bilan moslang.

**Kutiladigan natija:** tugma ichida lupa.

### 5. «Kirish» · o'rta

Header o'ng tomoniga «Kirish» (Inter 25 px) va 38 × 38 profil ikonkasini qo'shing.

**Kutiladigan natija:** bir chiziqda turgan matn va ikonka.

### 6. Savat va Exposure · o'rta

Savat ikonkasini qo'shing va Exposure bilan fonga moslang.

**Kutiladigan natija:** uyg'un ikonkalar.

### 7. Ajratuvchi chiziq · o'rta

Header ostiga qora, 2 px, Center Line chizing.

**Kutiladigan natija:** to'g'ri stroke sozlamalari.

### 8. Yon panel · o'rta

Oq panel: Stroke qora 1 px Inside, Drop shadow.

**Kutiladigan natija:** fondan ajralib turgan panel.

### 9. Kategoriyalar · qiyin

5 ta kategoriya nomi, orasida ajratuvchi chiziqlar va pastda «more categories».

**Kutiladigan natija:** to'liq kategoriya paneli.

### 10. Red guides · qiyin

Alt bilan barcha qatorlar orasidagi masofani tekshiring va teng qiling (16 yoki 24 px).

**Kutiladigan natija:** teng oraliqlar.

### 11. Komponent · qiyin

Qidiruv blokini `Search/Default` komponentiga aylantiring.

**Kutiladigan natija:** Assets'da komponent.

### 12. Yagona uslub · bonus

Sahifaga menyu va «Barcha kitoblar» tugmasini header uslubida qo'shing.

**Kutiladigan natija:** uyg'un, tugallangan sahifa qismi.

## O'zingizni tekshiring

1. Design panelida W, H, X, Y nimani bildiradi?
2. Nega 50 px balandlikdagi maydonga radius 25 beriladi?
3. Rectangle ichiga ikonka qanday joylanadi?
4. Exposure nima uchun kerak?
5. Stroke'ning Inside, Center, Outside joylashuvlari farqi nima?
6. Drop shadow panelga nima beradi?
7. Red guides qanday ochiladi va nima uchun kerak?

## Uyga vazifa

Sahifaga menyu, «Barcha kitoblar» tugmasi va banner joyini qo'shing, yagona uslubni ta'minlang va qidiruv blokini komponentga aylantiring (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
