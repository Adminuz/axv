# 17-dars. Interfeys elementlari va UI komponentlar: tugma, maydon, karta, Auto layout va variantlar

> Sahifadagi tugma, karta va menyu ko'p marta takrorlanadi. Bugun ularni bir marta chizib, komponentga aylantiramiz va turli holatlari uchun variantlar yaratamiz.

## Dars xulosasi

- Elementlar: tugma, maydon, ikonka, karta.
- Har interaktiv elementning holatlari bor.
- Auto layout: yo'nalish, gap, padding; Flexbox ga mos.
- Hug — mazmunga, Fill — bo'sh joyga, Fixed — qotirilgan.
- Komponent: main va instance; main o'zgarsa, hammasi yangilanadi.
- Variantlar bir komponentning turli holatlarini saqlaydi.

## Qo'shimcha ma'lumot

### Override
Instance da matn yoki ikonkani o'zgartirish.

### Constraints
Frame o'lchami o'zgarganda element joyi.

### Variables
Rang va masofalarning nomlangan qiymatlari.

### Component set
Variantlar to'plami.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Holat | Elementning ko'rinish varianti |
| Hover | Kursor ustida holati |
| Auto layout | Avtomatik tizish |
| Gap | Elementlar orasidagi masofa |
| Padding | Ichki masofa |
| Komponent | Qayta ishlatiladigan element |
| Instance | Komponent nusxasi |
| Variant | Komponent varianti |

## Bilasizmi?

- Material Design va iOS Human Interface Guidelines tugmalar va ularning holatlari uchun tayyor qoidalar beradi.
- Figma'dagi `Variables` rang va masofalarni nomlangan qiymat (token) sifatida saqlaydi.
- Auto layout ichida Auto layout joylashtirish mumkin: murakkab maketlar shunday yig'iladi.

## Topshiriqlar

### 1. Elementlar · oson

4 ta interfeys elementini sanang.

**Kutiladigan natija:** Tugma, maydon, ikonka, karta.

### 2. Holatlar · oson

Tugmaning 3 holatini yozing.

**Kutiladigan natija:** Oddiy, hover, bosilgan.

### 3. Auto layout · oson

Auto layout tugmasi?

**Kutiladigan natija:** `Shift+A`.

### 4. Komponent tugmasi · oson

Komponent yaratish tugmalari?

**Kutiladigan natija:** `Ctrl+Alt+K`.

### 5. Gap va padding · o'rta

Gap va padding farqini yozing.

**Kutiladigan natija:** Gap — elementlar orasi, padding — ichki.

### 6. Hug va Fill · o'rta

Hug va Fill farqini yozing.

**Kutiladigan natija:** Mazmunga / bo'sh joyga.

### 7. Instance · o'rta

Instance va main component farqi?

**Kutiladigan natija:** Nusxa va asl nusxa.

### 8. Variant xossasi · o'rta

Tugma uchun variant xossalarini yozing.

**Kutiladigan natija:** Holat va O'lcham.

### 9. CSS ga o'tkazish · qiyin

Auto layout qiymatlarini CSS ga o'tkazing.

**Kutiladigan natija:** `display:flex; gap; padding`.

### 10. Karta komponenti · qiyin

Kitob kartasi qatlamlarini yozing.

**Kutiladigan natija:** Rasm, nom, muallif, tugma.

### 11. Holat ko'p · qiyin

Nima uchun holatlarni chizish kerak?

**Kutiladigan natija:** Dasturchiga aniq ko'rsatma.

### 12. Komponentlar kutubxonasi · bonus

E-kutubxona uchun 5 ta komponent rejalashtiring.

**Kutiladigan natija:** Tugma, maydon, karta, header, menyu.

## O'zingizni tekshiring

1. Tugma holatlari?
2. Auto layout nima?
3. Hug va Fill?
4. Komponent va instance?
5. Variantlar nima?
6. Nima uchun komponent kerak?

## Uyga vazifa

E-kutubxona uchun tugma va kitob kartasi komponentlarini yarating (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
