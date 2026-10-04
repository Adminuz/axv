# 10-sinf (BI va Machine Learning): 1-hafta baholash qaydnomasi

**Mavzular:**
1. Ma’lumotlar muhandisligiga kirish: DIKW piramidasi, Data Engineer vs Data Scientist, Data Pipeline, Netflix/YouTube tavsiya tizimlari keyslari
2. Ma'lumotlar arxitekturasi va hayot sikli: 6 ta arxitektura qatlami (Source, Ingestion, Storage, Processing, Serving, Governance), 7 ta Lifecycle bosqichi, Data Quality 4 mezoni (Completeness, Accuracy, Consistency, Timeliness), Maktab tahliliy platformasi loyihasi
3. Ma’lumot formatlari: CSV va JSON bilan ishlash: Tabular vs Nested struktura, Medallion arxitekturasi (`data/raw`, `bronze`, `silver`, `gold`), Encoding (`utf-8` vs `cp1251`), Pandas bilan o'qish va `json_normalize()`

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **DIKW & Kasbiy Tushunchalar** | DIKW piramidasi darajalarini to'g'ri ajrata olish, Data Engineering va Pipeline vazifalarini tushunish, real keyslar tahlili | 30 ball |
| **Arxitektura & Data Quality** | Data Architecture 6 qatlami, Lifecycle 7 bosqichi, sifat mezonlari buzilishini aniqlash va resurs yuklamasi tahlili | 35 ball |
| **Fayl Formatlari & Pandas** | CSV va JSON formati xususiyatlari, Medallion loyiha strukturasi, encoding muammolarini yechish va `json_normalize` bilan ishlash | 35 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | DIKW & Roller (30) | Arxitektura & Sifat (35) | CSV/JSON & Pandas (35) | Jami ball (100) | Izoh |
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

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar ko'pincha CSV fayllar ichida vergul qatnashganda ustunlar chalkashib ketishini yoki `UnicodeDecodeError` chiqqanda kod nega to'xtab qolganini tushunishda ikkilanishadi. Ularga `try-except` blokida boshqa encoding (`cp1251`) berish zarurligini amalda ko'rsatish juda foydali bo'ldi.
- **JSON va jadval tushunchasi:** O'quvchilar uchun JSON ning daraxtsimon (nested) shaklidan jadval (satr-ustun) shakliga o'tish dastlab murakkab tuyulishi mumkin. `pd.json_normalize()` funksiyasining qanday qilib ichki kalitlarni nuqta orqali ustun sarlavhasiga aylantirishini doskada yoki slaydda chizib tushuntirish samara beradi.
