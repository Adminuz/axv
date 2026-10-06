# 17-dars. Ma'lumotlar ombori: Data Warehouse (DWH) tushunchasi, arxitekturasi va afzalliklari

> Ma'lumot turli joyda yotsa, bir savolga uch xil javob chiqadi. Bugun bitta ishonchli ombor — DWH ni o'rganamiz.

## Dars xulosasi

- DWH — turli manbalarni birlashtiruvchi, tahlil uchun moslangan ombor.
- Xususiyatlar: mavzuga yo'naltirilgan, integratsiyalangan, tarixiy, barqaror.
- OLTP kundalik ish uchun, OLAP/DWH tahlil uchun.
- Qatlamlar: manba, ETL, staging, DWH, mart, BI.
- Afzalliklar: bir joyda ma'lumot, tarix, tez tahlil, sifat nazorati.
- Texnologiyalar: Snowflake, BigQuery, Redshift, Synapse, PostgreSQL.

## Qo'shimcha ma'lumot

### Yagona haqiqat manbai
Bir ko'rsatkich uchun hamma bir xil raqamni ko'rishi DWH ning asosiy qiymati.

### Kimball va Inmon
Ikki mashhur yondashuv: Kimball — martlardan boshlab yig'ish (13-dars), Inmon — avval markaziy ombor. Dasturda Kimball keltirilgan.

### ETL va ELT
ETL — o'zgartirib yuklash, ELT — avval yuklab, omborda o'zgartirish. 8-mavzuda alohida o'tiladi.

### Staging xavfsizligi
Staging da xom va ba'zan maxfiy ma'lumot bo'ladi: kirishni cheklang.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| DWH | Data Warehouse |
| OLTP | Operatsion tranzaksiyalar |
| OLAP | Tahliliy ishlov |
| ETL | Extract, Transform, Load |
| Staging | Xom qatlam |
| Mart | Soha bo'yicha qism |
| Integratsiya | Manbalarni birlashtirish |
| Tarixiy | O'zgarishlarni saqlovchi |
| BI | Business Intelligence |

## Bilasizmi?

- Snowflake, BigQuery, Redshift kabi bulutli omborlar hisoblash va saqlashni ajratadi.
- Ko'p tashkilotlar DWH ni tunda yangilaydi (batch), ba'zilari real vaqtga yaqin.
- DWH ning kelib chiqishi 1980-yillarga, birinchi tahlil omborlariga borib taqaladi.

## Topshiriqlar

### 1. DWH ta'rifi · oson

DWH ni o'z so'zingiz bilan ta'riflang.

**Kutiladigan natija:** To'g'ri ta'rif.

### 2. 4 xususiyat · oson

DWH ning 4 xususiyatini yozing.

**Kutiladigan natija:** Mavzu, integratsiya, tarix, barqarorlik.

### 3. OLTP/OLAP · oson

OLTP va OLAP farqini 2 jumlada yozing.

**Kutiladigan natija:** Kundalik va tahlil.

### 4. ETL · oson

ETL ning har harfini yozing.

**Kutiladigan natija:** Extract, Transform, Load.

### 5. Qatlamlar · o'rta

5 qatlamli DWH oqimini yozing.

**Kutiladigan natija:** Manba…BI.

### 6. Staging · o'rta

Staging nima uchun kerak?

**Kutiladigan natija:** Xom nusxa va tekshiruv.

### 7. Texnologiya · o'rta

3 ta DWH texnologiyasini yozing.

**Kutiladigan natija:** Snowflake va boshqalar.

### 8. Afzallik · o'rta

DWH ning 3 afzalligini yozing.

**Kutiladigan natija:** Bir joy, tarix, tez tahlil.

### 9. Birlashtirish · qiyin

Ikki jadvalni `UNION ALL` bilan birlashtiring.

**Kutiladigan natija:** Yagona jadval.

### 10. Jami hisoblash · qiyin

2024-yil jamini toping.

**Kutiladigan natija:** 1 244 000 (namunada).

### 11. Xatoni toping · qiyin

Hisobot staging dan olinmoqda. Nima xato?

**Kutiladigan natija:** Xom ma'lumot.

### 12. Sxema · bonus

O'z loyihangiz uchun DWH sxemasini chizing.

**Kutiladigan natija:** Qatlamlar sxemasi.

## O'zingizni tekshiring

1. DWH nima?
2. 4 ta xususiyati?
3. OLTP va OLAP farqi?
4. Qatlamlar?
5. Staging nima?
6. ETL nima?

## Uyga vazifa

Kichik DWH yig'ing va qatlamlar sxemasini chizing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
