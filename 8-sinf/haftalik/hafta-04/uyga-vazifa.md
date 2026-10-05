# 4-hafta: Uyga vazifa

**Fan:** Web Full-stack  
**Sinf:** 8-sinf  
**Hafta:** 4-hafta  
**Topshirish muddati:** Keyingi darsga qadar (5-hafta, 1-dars)

---

## Topshiriq 1: Uch xil karta · o'rta

`index.html` va `style.css` fayllar yarating. CSS da `.karta` sinfini aniqlab, **3 ta turli ko'rinishdagi karta** (card) yasang:

- Har bir kartaning `width` i 280px, `padding` i 20px, `border-radius` i kamida 8px bo'lsin.
- Kartalar bir-biridan `margin` orqali ajralib tursin (kamida 16px).
- Har bir karta **boshqa rangdagi border** ga ega bo'lsin (`solid`, `dashed` va `dotted` turlaridan foydalaning).
- Barcha kartada `* { box-sizing: border-box; }` yozilgan bo'lsin.

**Namuna:**
```html
<div class="karta karta-1">
  <h3>Birinchi karta</h3>
  <p>Box model amaliyoti</p>
</div>
```

---

## Topshiriq 2: Hisoblash · o'rta

`hisoblar.txt` (oddiy matn fayli) da quyidagi hisob-kitobni yozing:

`.blok { width: 200px; padding: 15px; border: 4px solid; margin: 10px; }` bo'lsa:

1. **content-box** da blok jami nechi piksel yer egallaydi? (margin bilan va margin siz alohida)
2. **border-box** da blok jami nechi piksel yer egallaydi?
3. Farq qancha piksel?

---

## Topshiriq 3: DevTools skrinshotlari · oson

Brauzerda `index.html` ni oching, F12 bosung. Har bir karta uchun DevTools dan Box model rasmini ko'ring va **3 ta skrinshot** olib, `screenshot-1.png`, `screenshot-2.png`, `screenshot-3.png` nomida saqlang.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 3 ta karta yaratilgan, har biri farqli border | 3 |
| box-sizing: border-box qo'llanilgan | 2 |
| margin bilan kartalar orasida to'g'ri masofa | 2 |
| Hisoblash to'g'ri (hisoblar.txt) | 2 |
| DevTools skrinshot (kamida 1 ta) | 1 |
| **Jami** | **10** |

---

## Mentor uchun

**Tekshirish:**
- `style.css` da `*` universal selektor bilan `box-sizing: border-box` borligini tekshiring.
- F12 → Elements → Computed da Box model rasmini ko'ring.
- `hisoblar.txt` da hisob-kitob:
  - content-box: ko'rinadigan kenglik = 200 + 2×15 + 2×4 = **238px**; jami = 238 + 2×10 = **258px**.
  - border-box: ko'rinadigan kenglik = **200px**; jami = 200 + 20 = **220px**.
  - Farq: 258 − 220 = **38px**.
- Keng tarqalgan xato: `margin: 0 auto;` ni `width` ko'rsatmasdan yozish — markazlanmaydi.
