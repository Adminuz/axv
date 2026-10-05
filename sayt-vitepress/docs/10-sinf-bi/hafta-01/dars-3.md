---
title: "3-dars. 3-dars: Ma’lumot formatlari: CSV va JSON bilan ishlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (BI & ML)", "link": "/10-sinf-bi/"}, "week": {"n": 1, "link": "/10-sinf-bi/hafta-01/"}, "g": 3, "title": "3-dars: Ma’lumot formatlari: CSV va JSON bilan ishlash", "lead": "Ma’lumot formatlari: CSV va JSON bilan ishlash (Tabular vs Nested, Medallion arxitekturasi)", "slide": "/slaydlar/10-sinf-bi/hafta-01/dars-3.html", "test": "/slaydlar/10-sinf-bi/hafta-01/dars-3-test.html", "tabs": [{"g": 1, "link": "/10-sinf-bi/hafta-01/dars-1", "current": false}, {"g": 2, "link": "/10-sinf-bi/hafta-01/dars-2", "current": false}, {"g": 3, "link": "/10-sinf-bi/hafta-01/dars-3", "current": true}], "prev": {"g": 2, "title": "2-dars: Ma'lumotlar arxitekturasi va hayot sikli (Data Architecture & Data Lifecycle)", "link": "/10-sinf-bi/hafta-01/dars-2"}, "next": null}
---

**Fan:** BI (Ma'lumotlar muhandisligi va Machine Learning)  
**Sinf:** 10-sinf  
**Mavzu:** CSV va JSON formatlari, tabular vs nested struktura, Medallion arxitekturasi va Pandas amaliyoti  

---

<div class="blk">

## <Icon name="file-text" /> Nazariy konspekt

### 1. CSV (Comma-Separated Values)
- **Tuzilishi:** Jadval ko'rinishidagi satrli (tabular) oddiy matn formati;
- **Ajratgichlar:** Vergul (`,`), nuqta-vergul (`;`), tabulyatsiya (`\t`);
- **Afzalliklari:** Sodda, universal, Excel va Python tomonidan oson o'qiladi;
- **Kamchiliklari:** Ma'lumot turlari (schema) saqlanmaydi, siqilmagan, encoding (`utf-8` vs `cp1251`) va ajratgich to'qnashuvlari yuz berishi mumkin.

---

### 2. JSON (JavaScript Object Notation)
- **Tuzilishi:** Kalit-qiymat (`"kalit": qiymat`) va massivlar (`[...]`) asosidagi ierarxik format;
- **Afzalliklari:** Moslashuvchan (yarim-strukturali), ichma-ich (nested) ma'lumotlarni ifodalay oladi, zamonaviy API va web servislarning asosiy standarti;
- **Kamchiliklari:** Kalit nomlari takrorlanishi sababli ortiqcha hajm (overhead) egallaydi, BI va SQL tahlilidan oldin `json_normalize()` bilan tekislash talab etiladi.

---

### 3. Data Engineering Loyiha Papkalari (Medallion arxitekturasi)
- `data/raw/` — birlamchi o'zgartirilmagan xom fayllar;
- `data/bronze/` — qabul qilingan va minimal tekshirilgan nusxalar;
- `data/silver/` — tozalangan va normalizatsiya qilingan oraliq ma'lumotlar;
- `data/gold/` — yakuniy agregatsiya qilingan tahliliy jadvallar (Data Marts);
- `src/` — Python pipeline skriptlari;
- `logs/` — jarayonlar va xatoliklar jurnali.

---

### 4. Pandas bilan asosiy amallar
```python
import pandas as pd

# CSV o'qish (ajratgich va kodlash bilan)
df_csv = pd.read_csv('fayl.csv', sep=';', encoding='utf-8')

# JSON o'qish va tekislash
df_json = pd.json_normalize(json_malumot)

# Birlamchi tahlil
print(df_csv.shape)     # (qatorlar, ustunlar)
print(df_csv.head(3))   # Dastlabki 3 qator
print(df_csv.info())    # Ustunlar va turlar
```

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

### 1-topshiriq: Delimiter turlarini aniqlash <Badge type="tip" text="oson" />
Quyidagi 3 ta satrning har birida qaysi belgi ajratgich (delimiter) vazifasini bajarayotganini aniqlang:
a) `1;Toshkent;3500000;2024`  
b) `101,Matematika,Aliyev,95`  
c) `ID\tIsm\tYosh\tSinf`

### 2-topshiriq: CSV va JSON taqqoslash <Badge type="tip" text="oson" />
Nima uchun bank mobil ilovasi serverga tranzaksiyani yuborayotganda CSV emas, JSON formatini tanlaydi? 2 ta asosiy sabab keltiring.

### 3-topshiriq: Oddiy CSV fayl tuzish <Badge type="tip" text="oson" />
Maktabingizdagi 3 nafar o'quvchi (ID, Ism, Familiya, Sinf, O'rtacha ball) uchun CSV formatidagi matn tuzing.

### 4-topshiriq: Medallion papkalariga ajratish <Badge type="warning" text="o'rta" />
Quyidagi fayllar qaysi papkaga (`raw`, `bronze`, `silver`, `gold`) tegishli ekanini aniqlang:
- `maktab_statistikasi_tozalangan.csv`
- `e_maktab_export_xom_2024.json`
- `hududlar_yillik_reytingi_kpi.csv`

### 5-topshiriq: Encoding xatosini aniqlash <Badge type="warning" text="o'rta" />
Dasturchi faylni `pd.read_csv('malumot.csv')` orqali o'qiganda `UnicodeDecodeError: 'utf-8' codec can't decode byte...` xatosi chiqdi. Bu xato nima sababdan sodir bo'ldi va uni bartaraf etish uchun kodga qanday parametr qo'shish kerak?

### 6-topshiriq: JSON formatini tahlil qilish <Badge type="warning" text="o'rta" />
Quyidagi JSON obyektida necha xil ma'lumot turi (string, number, boolean, array, object) qatnashganini sanang:
```json
{
  "maktab_id": 15,
  "faol": true,
  "nomi": "15-maktab",
  "direktor": {"ism": "Karim", "tajriba_yil": 12},
  "fanlar": ["Fizika", "Kimyo", "Informatika"]
}
```

### 7-topshiriq: Python'da ustunlarni o'rganish <Badge type="warning" text="o'rta" />
Pandas DataFrame'da barcha ustunlar ro'yxatini va ulardagi bo'sh (null) qiymatlar sonini aniqlash uchun qaysi ikkita buyruq bajariladi?

### 8-topshiriq: json_normalize amaliyoti <Badge type="danger" text="qiyin" />
Quyidagi ichma-ich JSON strukturasini `json_normalize` yordamida qanday qilib 4 ta ustunli (`shahar`, `hudud.tuman`, `ob-havo.harorat`, `ob-havo.namlik`) tekis jadvalga aylantirish mumkinligini yozing:
```json
{
  "shahar": "Toshkent",
  "hudud": {"tuman": "Yunusobod"},
  "ob-havo": {"harorat": 24, "namlik": 45}
}
```

### 9-topshiriq: Format tanlash keysi <Badge type="danger" text="qiyin" />
Katta korporatsiyada har daqiqada 50 000 ta sensor ma'lumoti yig'iladi. Agar ushbu ma'lumotlar CSV formatida saqlansa qanday muammo, JSON formatida saqlansa qanday muammo yuzaga keladi? Tahlil qiling.

### 10-topshiriq: To'liq konvertatsiya skripti <Badge type="info" text="bonus" />
Python'da `data/raw/data.csv` faylini o'qib, uni JSON formatiga (`data/silver/data.json`) o'giruvchi va konsolga qatorlar sonini chiqaruvchi to'liq Python skriptini yozing.

---

</div>

<div class="blk">

## <Icon name="file-text" /> O'zini tekshirish uchun savollar

1. CSV formatining eng katta 2 ta afzalligi va 2 ta kamchiligi nima?
2. JSON qachon va qaysi sohalarda ajralmas format hisoblanadi?
3. Medallion arxitekturasida `raw` va `silver` qatlamlarining farqi nimada?
4. `pd.json_normalize()` qanday vaziyatlarda qo'llaniladi?
5. Encoding nima va nima uchun `cp1251` xatoligi yuzaga keladi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

1. O'zingiz yoqtirgan 5 ta kitob haqidagi ma'lumotlarni (Nomi, Muallifi, Chiqqan yili, Janrlar ro'yxati) bitta JSON fayl ko'rinishida yozib keling.
2. `maktab-pipeline` loyihasi papka strukturasini o'z kompyuteringizda yarating (`mkdir -p data/{raw,bronze,silver,gold} src logs`).

</div>

