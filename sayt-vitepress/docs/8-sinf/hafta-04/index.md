---
title: "4-hafta"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "hafta"
hafta: {"sinf": {"name": "8-sinf", "link": "/8-sinf/"}, "n": 4, "bob": "II-bob · CSS texnologiyasi va sahifa dizayni", "lessons": [{"g": 10, "title": "CSS asoslari: ulash va selektorlar", "lead": "HTML sahifangiz hozircha oq-qora ko'ylakda. Bugun unga CSS bilan rang, uslub va xarakter beramiz va kerakli elementni aniq tanlashni o'rganamiz.", "link": "/8-sinf/hafta-04/dars-1", "slide": "/slaydlar/8-sinf/hafta-04/dars-1.html", "test": null}, {"g": 11, "title": "CSS: rang va shrift bilan ishlash, meros olish", "lead": "Bugun sahifangizga rang beramiz: matn, fon, gradient. Shrift va matn uslubi bilan o'qishni qulay qilamiz va «meros» sirini ochamiz.", "link": "/8-sinf/hafta-04/dars-2", "slide": "/slaydlar/8-sinf/hafta-04/dars-2.html", "test": null}, {"g": 12, "title": "CSS Box model: content, padding, border, margin", "lead": "Veb-sahifadagi har bir narsa bu quti. Bugun qutining ichini, devorini va atrofidagi bo'sh joyni boshqarishni o'rganasiz, shundan so'ng maketlar yasash osonlashadi.", "link": "/8-sinf/hafta-04/dars-3", "slide": "/slaydlar/8-sinf/hafta-04/dars-3.html", "test": null}], "test": null}
---

<div class="blk">

## <Icon name="house" /> Uyga vazifa

**Fan:** Web Full-stack  
**Sinf:** 8-sinf  
**Hafta:** 4-hafta  
**Topshirish muddati:** Keyingi darsga qadar (5-hafta, 1-dars)

---

## Topshiriq 1: Uch xil karta <Badge type="warning" text="o'rta" />
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

## Topshiriq 2: Hisoblash <Badge type="warning" text="o'rta" />
`hisoblar.txt` (oddiy matn fayli) da quyidagi hisob-kitobni yozing:

`.blok { width: 200px; padding: 15px; border: 4px solid; margin: 10px; }` bo'lsa:

1. **content-box** da blok jami nechi piksel yer egallaydi? (margin bilan va margin siz alohida)
2. **border-box** da blok jami nechi piksel yer egallaydi?
3. Farq qancha piksel?

---

## Topshiriq 3: DevTools skrinshotlari <Badge type="tip" text="oson" />
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

</div>
