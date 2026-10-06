# 9-sinf (BI): 5-hafta baholash qaydnomasi

**Mavzular:**
1. SQL asoslari: WHERE shartli filtrlash, taqqoslash va mantiqiy operatorlar (AND, OR, NOT)
2. SQL asoslari: ORDER BY saralash (ASC, DESC), LIMIT va OFFSET
3. SQL asoslari: NULL qiymatlar bilan ishlash va ma'lumot turlari

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **WHERE va mantiqiy operatorlar** | Taqqoslash operatorlari, `AND`, `OR`, `NOT`, qavs bilan tartib, `IN`, `BETWEEN`, `LIKE`, natija qatorlarini oldindan aytish | 35 ball |
| **ORDER BY va sahifalash** | `ASC` / `DESC`, ko'p ustunli saralash, `TOP` + `ORDER BY`, `OFFSET ... FETCH` va `LIMIT`, sahifa formulasi | 30 ball |
| **NULL va ma'lumot turlari** | `IS NULL` / `IS NOT NULL`, `ISNULL`, `COALESCE`, `<>` tuzog'i, turni tanlash va `CAST` | 35 ball |
| **JAMI** | | **100 ball** |

Dasturdagi shkala: **90–100 — 5**, **71–89 — 4**, **60–70 — 3**, **0–59 — 2**.

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | WHERE va mantiqiy operatorlar (35) | ORDER BY va sahifalash (30) | NULL va ma'lumot turlari (35) | Jami ball (100) | Izoh |
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

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar `AND` va `OR` tartibini (avval `AND`) hamda `= NULL` va `IS NULL` farqini chalkashtiradi. Har ikkisini ham natijadagi qatorlar sonini oldindan aytish orqali mustahkamlang.
- **Iqtidorli o'quvchilar uchun:** `LIKE` namunalari (`_`, `[a-c]`), `TOP ... WITH TIES`, `CASE` bilan shartli ustun va `ISNULL` ni `COALESCE` bilan almashtirish haqida qisqa taqdimot.
- **Keyingi haftaga ko'prik:** 16-darsda `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` o'rganiladi — 15-darsdagi `NULL` qoidalari (agregatlar NULL ni hisobga olmaydi) shu darsda kerak bo'ladi.
