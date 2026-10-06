# 6-hafta: Uyga vazifa

**Fan:** Web Full-stack dasturlash  
**Sinf:** 8-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: Responsiv maket amaliyoti · qiyin

1. 14-darsdagi maketdan foydalanib, «Maktab sayti» sahifasini mobile-first usulida yarating: header, hero, kamida 6 ta karta, footer.
2. Kartalar telefonda 1, ≥768px da 2, ≥992px da 3 ustunda bo'lsin; rasmlar toshmasin (`aspect-ratio`, `object-fit`).
3. Sahifani 375px, 768px va 1280px kenglikda skrinshot qiling (DevTools qurilma rejimi) va gorizontal skroll yo'qligini tekshiring.

---

## Topshiriq 2: Figma va front-endga tayyorlash · o'rta

1. Figma'da (mentor yordami bilan) Phone frame yarating va unga sarlavha, rasm o'rni, matn va tugma chizing; elementlarga nom bering.
2. Tugmani komponentga aylantiring va ikkita variant yarating (oddiy va bosilgan).
3. Tugma va karta uchun rang, shrift, padding va radius qiymatlarini CSS ko'rinishida yozing; ranglarni `:root` o'zgaruvchilariga yig'ing.
4. Figma ishlatish imkoni bo'lmasa: qog'ozda telefon maketini chizib, qiymatlarni (rang, o'lcham, masofa) belgilang va CSS yozing.

---

## Topshiriq 3: Git va GitHub: commit va push · oson

1. Git'ni sozlang (`user.name`, `user.email`), «Maktab sayti» papkasini repo qiling va kamida 3 ta mazmunli commit qiling.
2. `.gitignore` yarating (`.env`, `node_modules/`) va `git log --oneline` natijasini daftarga yozing.
3. GitHub'da (ota-ona yoki mentor yordami bilan) `maktab-sayti` nomli bo'sh repo yarating va `push -u origin main` bilan loyihani yuboring.
4. GitHub akkaunti bo'lmasa: barcha buyruqlarni birinchi 3 commit uchun daftarga ketma-ketlikda yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: Responsiv «Maktab sayti» sahifasi | 3 |
| 17-dars: Figma'da tugma va karta, CSS qiymatlari | 3 |
| 18-dars: Loyihani Git bilan boshqarish va GitHub'ga yuborish | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: Breakpoint qanday tanlanadi?? Javobi: Sahifa buzilgan kenglikka qarab.
- 17-dars: 24px necha rem?? Javobi: 1.5rem.
- 18-dars: Push nimani yuboradi?? Javobi: Commit qilinganlarni.

**Keng tarqalgan xatolar:**
- 16-dars: viewport meta tegini unutish.
- 17-dars: Qatlamlarga nom bermaslik («Rectangle 47»).
- 18-dars: add dan keyin commit ni unutish.
