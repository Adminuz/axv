# 5-hafta: Uyga vazifa

**Fan:** Web Full-stack  
**Sinf:** 8-sinf  
**Hafta:** 5-hafta  
**Topshirish muddati:** Keyingi darsga qadar (6-hafta, 1-dars)

---

## Topshiriq 1: Flexbox navigatsiya va kartalar · o'rta

`index.html` va `style.css` yarating:

- `header` ichida chapda logotip, o'ngda 4 ta havola: `display: flex`, `justify-content: space-between`, `align-items: center`.
- Ostida 6 ta karta: `flex-wrap: wrap`, `gap: 16px`, har bir karta `flex: 1 1 220px`.
- Kartalardan birini `align-self` yoki `order` bilan ajratib ko'rsating (ixtiyoriy).

---

## Topshiriq 2: Grid sahifa maketi · o'rta

`maket.html` sahifasida Grid bilan quyidagi maketni quring:

- `header` va `footer` — butun kenglik (`grid-column: 1 / -1`).
- Chapda `aside` (220px), o'ngda `main` (`1fr`).
- `main` ichida 6 ta rasmli galereya: `repeat(3, 1fr)`, birinchi rasm `span 2`, rasmlarda `object-fit: cover`.

---

## Topshiriq 3: Responsiv qilish · qiyin

2-topshiriqdagi sahifani **mobile-first** usulida moslashtiring:

- `<head>` da `viewport` meta tegi bo'lsin.
- Telefonda (asosiy CSS): maket 1 ustun, galereya 1 ustun, menyu ustun ko'rinishida.
- `@media (min-width: 768px)`: maket 2 ustun, galereya 2 ustun, menyu qatorda.
- `@media (min-width: 992px)`: galereya 3 ustun.
- DevTools (Ctrl+Shift+M) da 375px, 768px va 1200px kenglikdagi **3 ta skrinshot** oling.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| Flexbox header va ko'chadigan kartalar to'g'ri ishlaydi | 3 |
| Grid maketi: header/footer butun kenglikda, sidebar + main | 2 |
| Galereya: `repeat`, `span 2`, `object-fit` | 1 |
| Mobile-first media so'rovlar (`min-width`), viewport tegi | 3 |
| 3 ta breakpoint skrinshoti | 1 |
| **Jami** | **10** |

---

## Mentor uchun

**Tekshirish:**
- `display: flex` / `display: grid` konteynerga yozilganini tekshiring (eng ko'p xato — elementlarga yozish).
- `header` ichidagi havolalar uchun ichki konteyner (`nav`) ham flex bo'lishi kerak — ular `header` ning nevaralari.
- Media so'rovlar asosiy qoidalardan **pastda** joylashganini va `min-width` ishlatilganini ko'ring; `max-width` ishlatilgan bo'lsa — desktop-first, mezon bo'yicha qisman ball.
- Telefon skrinshotida gorizontal aylantirish (scroll) bo'lmasligi kerak — bo'lsa, odatda rasmga qat'iy `width` berilgan yoki `max-width: 100%` yo'q.
- Galereyadagi `span 2` li rasm 1 ustunli telefon ko'rinishida to'rni «buzmasligi» uchun media so'rov ichida berilgani afzal (ixtiyoriy kuzatuv).
