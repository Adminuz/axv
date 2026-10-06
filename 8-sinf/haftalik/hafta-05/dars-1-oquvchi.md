# 13-dars. Flexbox: elementlarni qatorga va ustunga joylash

> O'tgan darsda qutilar ustma-ust tushardi. Bugun bitta qator CSS — `display: flex` — bilan ularni yonma-yon qo'yasiz, markazlaysiz va ekran torayganda keyingi qatorga ko'chirasiz.

## Dars xulosasi

- `display: flex` **konteynerga** yoziladi; uning bevosita bolalari **flex elementlar** bo'ladi.
- `flex-direction`: `row` (qator, standart) yoki `column` (ustun) — **asosiy o'q** yo'nalishi.
- `justify-content` — asosiy o'q bo'yicha: `flex-start`, `center`, `flex-end`, `space-between`, `space-around`.
- `align-items` — ko'ndalang o'q bo'yicha; `align-self` — faqat bitta element uchun.
- `flex-wrap: wrap` — sig'magan element keyingi qatorga o'tadi; `gap` — oralig'i.
- `flex: 1` — element bo'sh joydan ulush oladi (`flex-grow`, `flex-shrink`, `flex-basis`).

## Qo'shimcha ma'lumot

### 1. Konteyner va element: oila o'xshatishi
Konteyner — ota-ona, flex elementlar — bolalar. Ota-ona «hammangiz bir qatorda turinglar» desa, faqat **bolalari** quloq soladi. Nevaralar (bolalarning ichidagi elementlar) bu buyruqni eshitmaydi — ularga o'z ota-onasi alohida `display: flex` deyishi kerak.

### 2. Ikki o'q
```css
.qator  { display: flex; flex-direction: row; }    /* asosiy o'q → */
.ustun  { display: flex; flex-direction: column; } /* asosiy o'q ↓ */
```
Esda tuting: **justify — asosiy o'q, align — ko'ndalang o'q**. `column` da justify vertikal ishlaydi.

### 3. Markazlashning «oltin uchligi»
```css
.markaz {
  display: flex;
  justify-content: center;  /* gorizontal */
  align-items: center;      /* vertikal */
  height: 300px;            /* balandlik bo'lmasa, vertikal markaz ko'rinmaydi */
}
```

### 4. `flex: 1` — joyni bo'lish
```css
.sidebar { flex: 1; }  /* 1 ulush */
.kontent { flex: 3; }  /* 3 ulush */
```
Bo'sh joy 1 + 3 = 4 ulushga bo'linadi: sidebar 25%, kontent 75%. `flex-shrink: 0` yozilsa, element hech qachon siqilmaydi (masalan, logotip).

### 5. Odatiy xatolar
- `display: flex` ni elementlarning o'ziga yozish.
- Konteyner balandligisiz `align-items: center` kutish.
- `flex-wrap` yozmaslik — telefonda kartalar siqilib ketadi.
- Oralarga `margin` berib, chetda ortiqcha joy qoldirish — `gap` qulayroq.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Flexbox | Elementlarni bir o'q bo'yicha joylash tizimi |
| Flex konteyner | `display: flex` yozilgan ota element |
| Flex element | Konteynerning bevosita bolasi |
| Asosiy o'q (main axis) | `flex-direction` bo'yicha yo'nalish |
| Ko'ndalang o'q (cross axis) | Asosiy o'qqa perpendikulyar yo'nalish |
| justify-content | Asosiy o'q bo'yicha taqsimlash |
| align-items | Ko'ndalang o'q bo'yicha tekislash |
| align-self | Bitta elementning o'zini tekislash |
| flex-wrap | Elementlarni keyingi qatorga ko'chirish |
| gap | Elementlar orasidagi masofa |
| flex-grow / shrink / basis | Kengayish, siqilish va boshlang'ich o'lcham |

## Bilasizmi?

- Flexbox paydo bo'lishidan oldin dasturchilar elementlarni yonma-yon qo'yish uchun `float` va jadvallardan foydalanishgan — vertikal markazlash esa «eng qiyin CSS jumbog'i» hisoblanardi.
- «Flexbox Froggy» — qurbaqalarni nilufar bargiga `justify-content` va `align-items` bilan joylashtiradigan bepul o'yin.
- Brauzerning F12 asboblarida flex konteyner yonida `flex` belgisi chiqadi — uni bossangiz, o'qlar va bo'shliqlar chizib ko'rsatiladi.

## Topshiriqlar

### 1. Uch quti qatorda · oson
3 ta rangli `.quti` ni `display: flex` bilan bir qatorga qo'ying.
**Kutiladigan natija:** qutilar yonma-yon.

### 2. Masofa · oson
Qutilar orasiga `gap: 20px` bering.
**Kutiladigan natija:** oralar teng ochilgan.

### 3. Ustun · oson
`flex-direction: column` yozib, qutilarni ustma-ust qo'ying.
**Kutiladigan natija:** qutilar vertikal joylashgan.

### 4. Beshta qiymat · oson
`justify-content` ga 5 xil qiymat berib, har birining skrinshotini oling.
**Kutiladigan natija:** 5 ta turli taqsimot.

### 5. Markazdagi tugma · o'rta
300px balandlikdagi blok markaziga tugma qo'ying (gorizontal va vertikal).
**Kutiladigan natija:** tugma aniq o'rtada.

### 6. Navigatsiya paneli · o'rta
Chapda logotip, o'ngda 4 ta havola; hammasi vertikal o'rtada.
**Kutiladigan natija:** `space-between` li menyu.

### 7. Bitta boshqacha · o'rta
3 qutidan faqat o'rtadagisini `align-self` bilan pastga tushiring.
**Kutiladigan natija:** o'rtadagi quti pastki chetda.

### 8. Ko'chadigan kartalar · o'rta
6 ta karta: `flex-wrap: wrap`, `gap: 16px`, har biri kamida 200px. Oynani toraytiring.
**Kutiladigan natija:** kartalar keyingi qatorga ko'chadi.

### 9. Sidebar va kontent · qiyin
`flex: 1` va `flex: 3` bilan ikki ustunli sahifa yasang.
**Kutiladigan natija:** 1:3 nisbat.

### 10. Xatoni toping · qiyin
```css
.quti { display: flex; justify-content: center; }
```
3 ta `.quti` markazga kelmadi. Nega? Tuzating.
**Kutiladigan natija:** `display: flex` konteynerga ko'chirilgan.

### 11. Profil kartasi · qiyin
Chapda doira rasm, o'ngda ism va kasb (ustun), hammasi vertikal o'rtada.
**Kutiladigan natija:** ichma-ich ikki flex konteyner.

### 12. Flexbox Froggy · bonus
«Flexbox Froggy» o'yinida kamida 12 ta bosqichni o'ting.
**Kutiladigan natija:** oxirgi bosqich skrinshoti.

## O'zingizni tekshiring

1. `display: flex` qaysi elementga yoziladi?
2. Flex elementlar kimlar?
3. Asosiy va ko'ndalang o'q nima?
4. `space-between` va `space-around` qanday farqlanadi?
5. Elementni markazga qo'yish uchun qaysi uch xususiyat kerak?
6. `flex-wrap: wrap` nima beradi?
7. `flex: 1` va `flex: 3` joyni qanday bo'ladi?

## Uyga vazifa

Navigatsiya paneli va 3 kartali qatordan iborat sahifa yasang (Flexbox, `gap`, `flex-wrap`). 20–30 daqiqa. Batafsil — haftalik uyga vazifada.
