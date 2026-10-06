# 9-sinf (IoT — Buyumlar Interneti): 4-hafta baholash qaydnomasi

**Mavzular:**
1. Arduino UNO va tugma orqali LED holatini boshqarish dasturi: holat va hodisa, `#define`, `checkSwitch()`, `millis()`, heartbeat LED, 4 rejimli boshqaruv
2. Breadboardda DIP switch (DPST) va LED yordamida oddiy elektron sikl yaratish (1-qism): zanjir qismlari, ochiq/yopiq zanjir, breadboard, kalit turlari, Om qonuni
3. Breadboardda DIP switch (DPST) va LED yordamida oddiy elektron sikl yaratish (2-qism): AND/OR zanjirlari, multimetr, nosozlikni izlash, DIP switch → Arduino (2 bit)

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **LED holatini boshqarish dasturi** | Nomli konstantalar, `checkSwitch()` va `&`, `delay()` siz `millis()` andozasi, heartbeat, `mode = (mode + 1) % 4` va `switch/case`, Serial'ga faqat o'zgarishda yozish | 35 ball |
| **DIP switch zanjiri (1-qism)** | Zanjir qismlari, breadboard qatorlari, DIP ariqcha ustida, LED qutbi, Om qonuni bo'yicha rezistor (5 V va 9 V), ikki mustaqil LED | 30 ball |
| **Mantiq, o'lchov va Arduino (2-qism)** | AND va OR sxemalari va haqiqat jadvallari, multimetr bilan kuchlanish/tok, rezistor tajribasi, nosozlikni izlash, `INPUT_PULLUP` bilan 2 bitli rejim tanlagichi | 35 ball |
| **JAMI** | | **100 ball** |

Dasturdagi shkala: **90–100 — 5**, **71–89 — 4**, **60–70 — 3**, **0–59 — 2**.

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | LED dasturi (35) | DIP zanjiri (30) | Mantiq va Arduino (35) | Jami ball (100) | Izoh |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

---

## Mentor qaydlari va tahlil

- **Darsdagi asosiy qiyinchiliklar:** `millis()` andozasini (`millis() - oxirgi >= interval`) birinchi marta ko'rganda o'quvchilar ko'pincha `oxirgi = millis()` qatorini unutadi — natijada blok har aylanishda bajariladi. Breadboardda eng ko'p xato — komponent oyoqlarining bitta qatorga tushishi va DIP switch'ning ariqcha ustiga qo'yilmasligi.
- **Tekshirish usuli:** har bir o'quvchidan tok yo'lini barmoq bilan «yurib» ko'rsatishni so'rang (manba → kalit → rezistor → LED → GND). 9 V batareya ishlatilsa, rezistor kamida 470 Om ekanini nazorat qiling.
- **Iqtidorli o'quvchilar uchun:** uzoq bosish (long press) bilan rejimni nolga qaytarish, PWM bilan 4 darajali tungi chiroq, 4 pozitsiyali DIP switch'dan 0–15 sonni o'qish.
