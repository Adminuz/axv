# 10-sinf: o'quv xaritasi (BI va Machine Learning)

Manba: `4.4. Standart`, `4.4. Uslubiy ko`rsatma`, `4.4. O`quv qo`llanma`. Agentlar avval shu faylni o'qiydi, katta .docx'ni qayta o'qimaydi. Matnlari `_matn/` papkasida (chiqarilgan .txt).

**Tuzilma:** 102 dars, haftasiga 3 dars (har biri 80 daqiqa). Hafta = ceil(dars № / 3), jami 34 hafta.

**Holat belgilari:** ⬜ rejada · 📝 materiallar tayyorlangan · ✅ o'tilgan

## Joriy holat

- Oxirgi o'tilgan dars: **0**
- Keyingi dars: **1** (1-hafta)
- Oxirgi yangilanish: —

## Eslatmalar

- Dastur: «Muhammad al-Xorazmiy vorislari» tizimi bo'yicha maxsus guruhlar (BI (Ma'lumotlar muhandisligi va Machine Learning)).
- O'quv yili 34 hafta, haftasiga 3 darsdan jami 102 dars rejalashtirilgan.


## 1-bob haqida umumiy ma’lumot

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|
| 1 | 1 | Kompyuter yoki noutbuk (kamida 8 GB RAM tavsiya etiladi) | ⬜ |
| 2 | 1 | Barqaror internet aloqasi (resurslar va datasetlar uchun) | ⬜ |
| 3 | 1 | Ma’lumotlar muhandisligi (Data Engineering) nima? | ⬜ |
| 4 | 2 | Ma’lumotlar arxitekturasi (Data Architecture) tushunchasi | ⬜ |
| 5 | 2 | Source layer (Manbalar): LMS/SIS eksportlari, Excel/CSV jurnallar, API, sensorlar | ⬜ |
| 6 | 2 | Ingestion layer (Yig‘ish): fayl import, API orqali olish, stream | ⬜ |
| 7 | 3 | Storage layer (Saqlash): Raw zona (Data Lake) va/yo DWH ombor | ⬜ |
| 8 | 3 | Processing/Transform layer (Qayta ishlash): tozalash, birlashtirish, agregatsiya (ETL/ELT) | ⬜ |
| 9 | 3 | Serving/Consumption layer (Taqdim etish): Data Mart, BI dashboard, ML feature store/ dataset | ⬜ |
| 10 | 4 | Governance & Observability: monitoring, logging, validation, access control | ⬜ |
| 11 | 4 | Ma’lumotlar hayot sikli (Data Lifecycle) | ⬜ |
| 12 | 4 | Collect/Ingest: ma’lumotni olish (CSV/JSON eksport, API) | ⬜ |
| 13 | 5 | Store: xom holatda saqlash (raw zone) va versiyalash | ⬜ |
| 14 | 5 | Validate/Clean: sifat tekshiruvi, bo‘sh qiymatlar, duplicate, format xatolarini tuzatish | ⬜ |
| 15 | 5 | Transform: biznes qoidalari asosida qayta tuzish (staging → mart) | ⬜ |
| 16 | 6 | Serve/Publish: analitika va hisobotlar uchun taqdim etish | ⬜ |
| 17 | 6 | Monitor/Log: pipeline ishlashi, xatolar, kechikishlarni kuzatish | ⬜ |
| 18 | 6 | Archive/Retention: saqlash muddatlari va arxiv siyosati | ⬜ |
| 19 | 7 | Nega bu mavzu BI va ML uchun “poydevor”? | ⬜ |
| 20 | 7 | to‘liq (completeness), | ⬜ |
| 21 | 7 | aniq (accuracy), | ⬜ |
| 22 | 8 | yagona standartda (consistency), | ⬜ |
| 23 | 8 | Analitik (o‘quv bo‘limi / reja bo‘limi) – yillar bo‘yicha trendlarni, hududlar reytingini, YoY o‘sish/pasayishni tahlil qiladi, hisobot tayyorlaydi | ⬜ |
| 24 | 8 | “Qaysi hududlarda o‘quvchi/maktab ko‘rsatkichi juda yuqori?” (yuklama) | ⬜ |
| 25 | 9 | “Qaysi hududlarda o‘quvchi/o‘qituvchi ko‘rsatkichi yuqori?” (kadr yetishmovchiligi proksisi) | ⬜ |
| 26 | 9 | “Bitiruvchilar soni trendi qanday o‘zgaryapti?” | ⬜ |
| 27 | 9 | YoY (yildan-yilga) o‘sish va pasayishlarni topish (LAG) | ⬜ |
| 28 | 10 | Hududlar reytingi (RANK) | ⬜ |
| 29 | 10 | 3 yillik moving average (AVG OVER) bilan barqaror trend chiqarish | ⬜ |
| 30 | 10 | Hisobot (CSV/PDF/Excel) tayyorlash | ⬜ |
| 31 | 11 | Hudud resurs ko‘rsatkichlariga qarab ta’lim jarayoni bosimini baholash | ⬜ |
| 32 | 11 | Resurs taqsimoti bo‘yicha tavsiyalar berish (masalan, o‘qituvchi shtati ehtiyoji) | ⬜ |
| 33 | 11 | CSV/JSON fayllarni yuklash va yangilash | ⬜ |
| 34 | 12 | Validation: null/duplicate, yil diapazoni, manfiy qiymatlar, hudud nomlari standartligi | ⬜ |
| 35 | 12 | Raw → processed/csv → parquet pipeline’ni ishlatish va monitoring qilish | ⬜ |
| 36 | 12 | Direktor platformaga kiradi | ⬜ |
| 37 | 13 | “Dashboard” bo‘limini tanlaydi | ⬜ |
| 38 | 13 | “Maktablar soni”, “O‘quvchilar soni”, “O‘qituvchilar soni”, “9/11 bitiruvchilar” KPI kartalarini ko‘radi | ⬜ |
| 39 | 13 | Filtr orqali hudud va yil ni tanlaydi | ⬜ |
| 40 | 14 | “Yuklama” bo‘limida quyilarni ko‘radi: | ⬜ |
| 41 | 14 | o‘quvchi/maktab (resurs bosimi) | ⬜ |
| 42 | 14 | o‘quvchi/o‘qituvchi (kadr yetishmovchiligi proksisi) | ⬜ |
| 43 | 15 | “Eng yuqori yuklama hududlar” reyting jadvalini ko‘radi | ⬜ |
| 44 | 15 | “Hisobotni yuklab olish” tugmasi orqali natijani (CSV/Excel/PDF) yuklab oladi | ⬜ |
| 45 | 15 | “YoY o‘zgarish” hisobotini ko‘radi: hududlar bo‘yicha o‘quvchilar sonining yillik farqi va foizi (LAG) | ⬜ |
| 46 | 16 | “Hududlar reytingi” hisobotini ochadi (RANK): | ⬜ |
| 47 | 16 | o‘quvchi/o‘qituvchi bo‘yicha TOP/BOTTOM hududlar | ⬜ |
| 48 | 16 | “3 yillik moving average” trendini ko‘radi (AVG OVER) | ⬜ |
| 49 | 17 | “Ulush (%)” hisobotini ko‘radi: hududning respublika bo‘yicha ulushi (SUM OVER) | ⬜ |
| 50 | 17 | Natijalarni docs/ bo‘limiga xulosa sifatida yozadi | ⬜ |
| 51 | 17 | Administrator data/raw/csv/ va data/raw/json/ papkalariga yangi fayllarni joylaydi: | ⬜ |
| 52 | 18 | maktablar_soni.csv | ⬜ |
| 53 | 18 | maktab_oquvchilar_soni.csv | ⬜ |
| 54 | 18 | oqituvchilar_soni.csv (+ oqituvchilar_soni.json bo‘lsa) | ⬜ |
| 55 | 19 | bitiruvchilar_9_sinf.csv, bitiruvchilar_11_sinf.csv | ⬜ |
| 56 | 19 | Notebook’da “Raw profiling”ni ishga tushiradi: shape, dtypes, null, duplicate tekshiradi | ⬜ |
| 57 | 19 | hudud va yil bo‘yicha duplicate yo‘qmi | ⬜ |
| 58 | 20 | soni manfiy emasmi | ⬜ |
| 59 | 20 | yil mantiqan to‘g‘rimi (masalan 2000–2025 oralig‘i) | ⬜ |
| 60 | 20 | “Cleaning” bosqichi: ustun nomlari standard, hudud matni strip, yil va soni numeric | ⬜ |
| 61 | 21 | Tozalangan ma’lumot data/processed/csv/*_tozalangan.csv ga saqlanadi | ⬜ |
| 62 | 21 | Keyin Parquet konvertatsiya bajariladi: data/processed/parquet/*.parquet (snappy) | ⬜ |
| 63 | 21 | SQL bazaga (SQLite) import qilinadi va v_talim view yangilanadi | ⬜ |
| 64 | 22 | Dashboard yangilanadi, administrator monitoring bo‘limida pipeline natijasini tekshiradi (row count, null check, log) | ⬜ |
| 65 | 22 | Filtrlar (hudud/yil) tushunarli va to‘g‘ri ishlayaptimi? | ⬜ |
| 66 | 22 | KPI ko‘rsatkichlar mantiqan to‘g‘rimi (masalan, o‘quvchi/o‘qituvchi juda katta chiqib ketmayaptimi)? | ⬜ |
| 67 | 23 | SQL natijalarda YoY va reytinglar to‘g‘ri hisoblanganmi? | ⬜ |
| 68 | 23 | Pipeline validation xatolari aniq chiqayaptimi (null/duplicate/manfiy qiymat)? | ⬜ |
| 69 | 23 | Export (CSV/Excel) ishlayaptimi? | ⬜ |
| 70 | 24 | Tanlangan mavzu bo‘yicha quyidagi savollarga javob yozing: | ⬜ |
| 71 | 24 | Shu ma’lumotlar asosida ssenariy yozing | ⬜ |
| 72 | 24 | BI Ma‘lumotlar muhandisligi va ML uchun berilgan loyiha mavzularidan birini tanlang.(Loyiha mavzulari rejada ko‘rsatilgan) | ⬜ |
| 73 | 25 | Ma’lumot formatlari: CSV, JSON, Parquet | ⬜ |
| 74 | 25 | Sintaksisni ajratib ko'rsatish va avtomatik to'ldirish: Kodni o'qishni yaxshilaydi va kodlashni tezlashtiradi | ⬜ |
| 75 | 25 | Integratsiyalashgan nosozliklarni tuzatish: Kodni to'g'ridan-to'g'ri muharrirda sinab ko'rish va tuzatishga yordam beradi | ⬜ |
| 76 | 26 | O'rnatilgan Git integratsiyasi: Oson versiyani boshqarish va hamkorlikni ta'minlaydi | ⬜ |
| 77 | 26 | Kengaytirilishi: Tillar, mavzular va vositalar uchun kengaytmalar qo'shish imkonini beradi | ⬜ |
| 78 | 26 | Yuqoridagi amallarni ketma-ketlik bo‘yicha bajaring | ⬜ |
| 79 | 27 | Quyidagilarni tekshiring: | ⬜ |
| 80 | 27 | Xulosalaringizni yozing | ⬜ |
| 81 | 27 | O‘zingiz tanlagan loyihaga doir kerakli fayllarni shakllantiring | ⬜ |
| 82 | 28 | Ma’lumotlar bazalari: konsept va tuzilma. Relatsion ma’lumotlar bazasi (RDBMS) | ⬜ |
| 83 | 28 | ma’lumotlarni markazlashtirib saqlaydi; | ⬜ |
| 84 | 28 | ko‘p foydalanuvchi ishlaganda bir xil ma’lumot bilan ishlashni ta’minlaydi; | ⬜ |
| 85 | 29 | ma’lumotlar yaxlitligi (integrity) va xavfsizligini boshqaradi; | ⬜ |
| 86 | 29 | ma’lumot jadval ko‘rinishida saqlanadi; | ⬜ |
| 87 | 29 | jadvallar o‘rtasida bog‘lanish (FK/PK) o‘rnatiladi; | ⬜ |
| 88 | 30 | SQL orqali so‘rov va boshqaruv ishlari bajariladi; | ⬜ |
| 89 | 30 | tranzaksiyalar va ACID tamoyillari qo‘llab-quvvatlanadi; | ⬜ |
| 90 | 30 | yaxlitlik va cheklovlar (constraints) bilan data quality nazorati kuchli | ⬜ |
| 91 | 31 | ma’lumotlar jadvallarga yuklanadi (import); | ⬜ |
| 92 | 31 | schema/kalitlar/bog‘lanishlar aniqlanadi; | ⬜ |
| 93 | 31 | SQL so‘rovlari orqali ma’lumot olinadi; | ⬜ |
| 94 | 32 | natija view/hisobot/dashboards qatlamida ishlatiladi | ⬜ |
| 95 | 32 | SELECT — ma’lumot olish | ⬜ |
| 96 | 32 | WHERE — shartli qidirish | ⬜ |
| 97 | 33 | JOIN — jadvallarni bog‘lash | ⬜ |
| 98 | 33 | GROUP BY — agregatsiya (yig‘indi, o‘rtacha, h.k.) | ⬜ |
| 99 | 33 | bosqich. PostgreSQL ni o‘rnatish | ⬜ |
| 100 | 34 | Windows uchun PostgreSQL o'rnatuvchisini yuklab oling | ⬜ |
| 101 | 34 | PostgreSQL-ni o'rnating | ⬜ |
| 102 | 34 | O'rnatishni tasdiqlang | ⬜ |

## 2-bob haqida umumiy ma’lumot

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|

## 3-bob haqida umumiy ma’lumot

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|

## 4-bob haqida umumiy ma’lumot

| Dars | Hafta | Mavzu | Holat |
|---|---|---|---|
