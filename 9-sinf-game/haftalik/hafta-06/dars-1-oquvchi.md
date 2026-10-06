# 16-dars. UI dizayn: tugmalar, menyular, HUD (3-qism): Jonli o'yin HUD'i (Health bar, tangalar, mini-xarita)

> O'yin davomida sog'liq, tangalar va xarita doim ko'z oldimizda. Bugun shu jonli HUD'ni Photoshop'da o'zimiz chizamiz.

## Dars xulosasi

- HUD — o'yin davomida doim ko'rinadigan interfeys.
- Asosiy elementlar: sog'liq, tangalar/ball, mini-xarita, vaqt, inventar.
- Talablar: aniqlik, burchaklar, minimalizm, janrga moslik, uslub.
- Health bar — fon, to'ldirish, ramka qatlamlari.
- To'ldirish uzunligi = kenglik × HP / maks HP.
- Guruhlab, shaffof PNG qilib eksport qiling.

## Qo'shimcha ma'lumot

### Safe area
Ba'zi ekranlarda chekkalar kesilishi mumkin — HUD ni chekkadan biroz ichkariga qo'ying.

### Animatsiya
Health bar kamayganda silliq o'zgarishi yaxshi taassurot beradi.

### Rang ko'rligi
Faqat rangga tayanmay, raqam yoki shakl ham qo'shing.

### Janrlar
Racing'da tezlik va vaqt, RPG'da tajriba paneli.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| HUD | Ekran usti interfeysi |
| Health bar | Sog'liq shkalasi |
| Mini-xarita | Kichik xarita |
| HP | Sog'liq ballari |
| Layer | Qatlam |
| Stroke | Kontur |
| Transparent | Shaffof fon |
| Sprite | Dvigatelga import qilinadigan rasm |

## Bilasizmi?

- «HUD» nomi aviatsiyadan: uchuvchining old oynasiga tushirilgan ma'lumotdan kelib chiqqan.
- Shooter o'yinlarida HUD minimal, RPG'da esa batafsil bo'ladi.
- Ba'zi o'yinlar HUD ni deyarli butunlay yashiradi — bu «minimalistik HUD» deyiladi.

## Topshiriqlar

### 1. HUD ta'rifi · oson

HUD nima? O'z so'zlaringiz bilan yozing.

**Kutiladigan natija:** Doimiy ko'rinadigan interfeys

### 2. Elementlar · oson

HUD ning 4 ta elementini sanang.

**Kutiladigan natija:** HP, tanga, mini-xarita, vaqt

### 3. Joylashuv · oson

HUD odatda ekranning qayerida bo'ladi?

**Kutiladigan natija:** Burchaklarda

### 4. Fon · oson

HUD uchun hujjat foni qanday bo'lishi kerak?

**Kutiladigan natija:** Transparent

### 5. Bar uzunligi · o'rta

Bar 400 px, HP 75/100. To'ldirish uzunligi?

**Kutiladigan natija:** 300 px

### 6. Qatlamlar · o'rta

Health bar qatlamlarini nomlang.

**Kutiladigan natija:** Fon, to'ldirish, ramka

### 7. Rang · o'rta

HP 20% bo'lsa bar rangi qanday bo'lishi kerak va nega?

**Kutiladigan natija:** Qizil — xavf

### 8. Tangalar · o'rta

Tanga hisoblagichi uchun qanday elementlar kerak?

**Kutiladigan natija:** Ikonka + matn

### 9. Mini-xarita · qiyin

Doira shaklini mukammal chizish usulini yozing.

**Kutiladigan natija:** Ellipse Tool + Shift

### 10. Guruhlash · qiyin

HUD qatlamlarini qanday guruhlaysiz? Tuzilmani yozing.

**Kutiladigan natija:** Ctrl+G, HUD > HP, Tangalar, Mini-xarita

### 11. Janr · qiyin

Shooter va RPG uchun HUD farqini tushuntiring.

**Kutiladigan natija:** Minimal va batafsil

### 12. To'liq HUD · bonus

O'z o'yiningiz uchun HUD maketini chizing va PNG qiling.

**Kutiladigan natija:** hud.png

## O'zingizni tekshiring

1. HUD nima?
2. HUD talablari qaysilar?
3. Health bar necha qatlam?
4. Bar uzunligi qanday hisoblanadi?
5. Doira qanday chiziladi?
6. Qaysi formatda eksport qilamiz?

## Uyga vazifa

O'z o'yiningiz uchun HUD maketini chizing (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
