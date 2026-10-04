# 9-sinf (BI): 3-hafta baholash qaydnomasi

**Mavzular:**
1. Ma’lumotlarni tozalash (Data Cleaning) va transformatsiya: Power Query, dublikatlar, bo'sh qiymatlar va Text-to-Columns
2. Pivot jadvallar (PivotTable) va ma'lumotlar vizualizatsiyasi: Slicerlar, diagrammalar va tahliliy hisobot yaratish
3. Relatsion ma’lumotlar bazalari va model tushunchasi (1-qism): Jadvallar, Primary Key, Foreign Key va munosabatlar

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Data Cleaning** | TRIM, PROPER, Text-to-Columns, Remove Duplicates, bo'sh qiymatlarni Find & Replace orqali to'ldirish | 30 ball |
| **PivotTable & Vizualizatsiya** | 4 ta maydon (Rows, Columns, Values, Filters), Value Field Settings, Grouping, Slicer va PivotChart | 35 ball |
| **Relatsion Model Asoslari** | Table, Row, Column tushunchalari, Primary Key unikkalligi, Foreign Key va referensial yaxlitlik, munosabatlar (1:1, 1:N, M:N) | 35 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Data Cleaning (30) | PivotTable (35) | Relatsion Model (35) | Jami ball (100) | Izoh |
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

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar ko'pincha PivotTable'da manba jadvalga yangi qator kiritilganda darhol `Refresh` (Alt + F5) bosish kerakligini unutadilar; Pivot Cache mexanizmi haqida qayta eslatma bering. Relatsion bazalarda esa Primary Key hech qachon NULL bo'lmasligi va Foreign Key har doim "ko'p" (Many) tomonidagi jadvalga joylashtirilishi qoidasini mustahkamlang.
- **Iqtidorli o'quvchilar uchun:** Power Query muhitida bir nechta faylni avtomatik birlashtirish (`Append Queries` / `Merge Queries`) yoki 4-5 ta jadvaldan iborat murakkab korporativ ER-model (masalan, Kassa, Chek, Xaridor, Tovar, Kategoriya) loyihasini ishlab chiqish topshirig'i berilishi mumkin.
