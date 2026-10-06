# 6-hafta: Uyga vazifa

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: SCD va surrogate kalitlar · qiyin

1. `dim_maktab` jadvalini yarating va bitta maktab qo'shing.
2. Direktorni avval Type 1, so'ng (jadvalni qayta yaratib) Type 2 bilan almashtiring; natijani solishtiring.
3. `fakt` jadvaliga ikki yil qo'shing va JOIN bilan har yil direktorini chiqaring.

---

## Topshiriq 2: Data Warehouse (DWH) · o'rta

1. `stg_qabul` va `stg_arxiv` jadvallarini yarating va `dw_oquvchilar` ga birlashtiring.
2. 2024-yil jami o'quvchilar sonini hisoblab, natijani yozing.
3. Maktab ma'lumotlari uchun DWH qatlamlari sxemasini chizing (manba, staging, DWH, mart, BI).

---

## Topshiriq 3: Data Lake va Bronze/Silver/Gold · oson

1. `data/raw/maktab.csv` faylini yarating (kamida 6 qator, 1 dublikat, 1 bo'sh qiymat bilan).
2. Bronze, Silver va Gold qatlamlarini yaratuvchi skript yozing.
3. Har qatlamdagi qatorlar soni va Silver da nima tashlanganini 3 jumlada yozing.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: direktor almashinuvi uchun Type 1 va Type 2 | 3 |
| 17-dars: kichik DWH ni qurish va qatlamlar sxemasi | 3 |
| 18-dars: raw dan gold gacha kichik oqim | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: Joriy qatorni qanday olamiz?? Javobi: WHERE joriy = 1.
- 17-dars: DWH ning bitta afzalligi?? Javobi: Ma'lumot bir joyda va izchil; tarix saqlanadi.
- 18-dars: Lakehouse nima?? Javobi: Lake va DWH imkoniyatlarining birligi.

**Keng tarqalgan xatolar:**
- 16-dars: Tarix kerak joyda Type 1 ishlatish.
- 17-dars: DWH ni operatsion bazaning oddiy nusxasi deb hisoblash.
- 18-dars: Raw fayllarni tahrirlash.
