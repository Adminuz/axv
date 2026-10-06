# 6-hafta: Uyga vazifa

**Fan:** Advanced Back-end va DevOps  
**Sinf:** 9-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: DRY va funksiyalar · qiyin

1. Bir xil amal (masalan, chegirma hisoblash) 3 marta takrorlangan dastur yozing, so'ng uni `chegirma(narx, foiz)` funksiyasiga aylantirib, DRY ko'rinishiga keltiring.
2. `format_user(ism, yosh)` funksiyasini yozing va 5 ta odam uchun chaqiring.
3. Til bo'yicha salomlashuvni `if/elif` bilan, so'ng `dict` bilan yozing va ikkala usulni solishtiring.
4. `yigindi`, `ayirma`, `kopaytma`, `bolinma` funksiyalarini yozing va har birini 2 marta chaqiring.

---

## Topshiriq 2: try/except va istisnolar · o'rta

1. Foydalanuvchidan butun son so'rang; harf kiritilsa, `ValueError` ni ushlab, tushunarli xabar bering va dasturni to'xtatmang.
2. Ikki sonni bo'ladigan dastur yozing: `ValueError` va `ZeroDivisionError` ni alohida ushlang; `else` va `finally` dan foydalaning.
3. To'g'ri yosh (0..120) kiritilguncha so'raydigan `yosh_ol()` funksiyasini yozing.
4. 5 ta har xil Traceback chiqarib, har birining turi va qatorini daftarga yozing.

---

## Topshiriq 3: Fayllar bilan ishlash · oson

1. `yozuv_qosh()` va `yozuvlar()` funksiyalarini yozing; `kundalik.txt` ga 3 ta yozuv qo'shib, ularni raqamlab chiqaring.
2. Fayl mavjud bo'lmaganda `FileNotFoundError` ni `try/except` bilan boshqaring va tushunchali xabar bering.
3. `w` va `a` rejimlarini bitta faylda sinab, natija farqini daftarga yozing.
4. Fayldagi qatorlar sonini va eng uzun qatorni topadigan dastur yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: DRY va funksiyalar: chegirma, salomlashuv | 3 |
| 17-dars: Xavfsiz kalkulyator va kiritishni tekshirish | 3 |
| 18-dars: «Kundalik» dasturi: faylga yozish va o'qish | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: if/elif o'rniga nima ishlatamiz?? Javobi: dict.
- 17-dars: raise nima qiladi?? Javobi: O'zimiz istisno chiqaradi.
- 18-dars: Fayl yo'q bo'lsa qaysi istisno?? Javobi: FileNotFoundError.

**Keng tarqalgan xatolar:**
- 16-dars: return o'rniga print yozib, natijani ishlata olmaslik.
- 17-dars: Yalang except: yozib, hamma xatoni yashirish.
- 18-dars: w bilan ochib, eski ma'lumotni yo'qotish.
