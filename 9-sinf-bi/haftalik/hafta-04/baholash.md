# 9-sinf (BI): 4-hafta baholash qaydnomasi

**Mavzular:**
1. Relatsion ma'lumotlar bazalari va model tushunchasi (2-qism): Normalizatsiya asoslari va BI'dagi o'rni
2. Relatsion ma'lumotlar bazalari va model tushunchasi (3-qism): RDBMS muhitlari va ma'lumotlar yaxlitligi
3. SQL asoslari: SELECT, ustunlar va sodda ifodalar

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Normalizatsiya** | Redundansiya va 3 anomaliyani aniqlash, jadvalni 1NF → 2NF → 3NF ga keltirish, Fact va Dimension jadvallarni ajratish | 35 ball |
| **RDBMS va yaxlitlik** | RDBMS larni farqlash, SSMS da baza va jadval yaratish, PK, FK, NOT NULL, UNIQUE, CHECK, DEFAULT cheklovlarini to'g'ri qo'llash, xato xabarini izohlash | 30 ball |
| **SQL SELECT** | Buyruq toifalari, `SELECT *` va ustunli so'rov, `AS`, hisoblangan ustunlar, `DISTINCT`, `TOP`, natijani bashorat qilish | 35 ball |
| **JAMI** | | **100 ball** |

Dasturdagi shkala: **90–100 — 5**, **71–89 — 4**, **60–70 — 3**, **0–59 — 2**.

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Normalizatsiya (35) | RDBMS va yaxlitlik (30) | SQL SELECT (35) | Jami ball (100) | Izoh |
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

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar 2NF va 3NF ni chalkashtiradi: 2NF — kompozit kalitning **bir qismiga** bog'liqlik, 3NF — kalit bo'lmagan **boshqa ustunga** bog'liqlik ekanini «kalitga, butun kalitga, faqat kalitga» qoidasi bilan mustahkamlang. SQL da eng ko'p uchraydigan xatolar: ustunlar orasida vergulni unutish, `FROM` o'rniga `FORM`, o'zbekcha matnda apostrofni ikkilantirmaslik (`N'O''g''il'`), hisoblangan ustunga `AS` bermaslik.
- **Iqtidorli o'quvchilar uchun:** 4–5 jadvalli do'kon modelini to'liq cheklovlar bilan yaratish va undan Star schema (1 Fact + 3 Dimension) loyihalash; `SELECT` da `CONCAT`, `ROUND`, `CAST` funksiyalarini mustaqil o'rganish.
- **Keyingi haftaga ko'prik:** 13-darsda `WHERE`, taqqoslash va mantiqiy operatorlar (`AND`, `OR`, `NOT`) o'rganiladi — 12-darsdagi `Mahsulotlar` jadvali shu darsda filtrlash uchun ishlatiladi.
