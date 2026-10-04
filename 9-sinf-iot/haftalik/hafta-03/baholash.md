# 9-sinf (IoT — Buyumlar Interneti): 3-hafta baholash qaydnomasi

**Mavzular:**
1. Elektron sxema asosida ikki LED lampaning ishlash prinsipi va ulanishi: ketma-ket vs parallel, Pin 9 va Pin 11, mustaqil vaqt tsikllari
2. Arduino UNO yordamida LED indikatorlari va push-button bilan ishlash (1-qism): 4 kontaktli tugma, suzuvchi pin, INPUT_PULLUP, Serial Monitor
3. Arduino UNO yordamida LED indikatorlari va push-button bilan interaktiv interfeys (2-qism): Toggle mantig'i, Bounce va Debounce, ko'p tugmali tizim

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Ikki LED va Parallel Boshqaruv** | Ketma-ket vs parallel ulanish qoidalari, alohida 220 Om rezistorlar, navbatma-navbat yoqish (Qizil 5s, Sariq 2s), stroboskop kodi | 30 ball |
| **Push-Button va INPUT_PULLUP** | Tugma mexanikasi, suzuvchi pinni bartaraf etish, ichki rezistor bilan ulash, `digitalRead()`, `Serial.begin(9600)` bilan monitoring | 35 ball |
| **Interaktiv Interfeys va Debounce** | Tugma bosilish lahzasini tutish (`lastButtonState`), dirillashni 50 ms filtr bilan tozalash, Toggle mantig'i (`!ledState`), ko'p tugmali boshqaruv | 35 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Ikki LED & Parallel (30) | Push-Button & Serial (35) | Toggle & Debounce (35) | Jami ball (100) | Izoh |
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

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar ko'pincha Toggle mantig'ini tushunishda qiynalishadi. Agar `buttonState == LOW` deb yozilsa, barmog'ini tugmadan olguncha tsikl soniyasiga yuzlab marta aylanib, holat tasodifiy bo'lib qoladi. Aynan holat o'zgarishi (`reading != lastBtn`) va `delay(50)` zarurligini real osiloskop to'lqinlari misolida ko'rsatish juda foydali.
- **Iqtidorli o'quvchilar uchun:** 3 ta tugma va 3 ta LED yordamida "Simon Says" xotira o'yini prototipini yaratish yoki tugma bosilganda har xil ohang chiqaruvchi passiv buzzer qo'shish topshirig'i berilishi mumkin.
