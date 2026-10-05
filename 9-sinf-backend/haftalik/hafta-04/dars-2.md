# 11-dars. String: indeks, slicing va metodlar

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 11-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga string indeksi (musbat va manfiy), slicing `[boshlanish : tugash : qadam]` va rasmiy qo‘llanmadagi string metodlarini (`upper()`, `lower()`, `title()`, `capitalize()`) o‘rgatish.

**Kutiladigan natija:**
- Indeks 0 dan boshlanishini va `word[-1]` oxirgi belgini berishini biladi;
- `[1:4]`, `[:3]`, `[3:]`, `[::2]`, `[::-1]` ko‘rinishlarini o‘qiy oladi va yoza oladi;
- Slicing da `tugash` indeksi kirmasligini tushunadi;
- `upper()`, `lower()`, `title()`, `capitalize()` metodlarini qo‘llaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–7 daq | Takrorlash | 10-dars: string yaratish, immutable, `"J" + s[1:]` |
| 7–25 daq | Yangi mavzu 1 | Indeks: musbat (`0` dan) va manfiy (`-1` dan) |
| 25–40 daq | Yangi mavzu 2 | Slicing: `[boshlanish : tugash : qadam]` |
| 40–45 daq | Tanaffus | Ko‘z mashqlari |
| 45–55 daq | Yangi mavzu 3 | String metodlari: `upper`, `lower`, `title`, `capitalize` |
| 55–75 daq | Amaliyot | Topshiriqlar |
| 75–80 daq | Xulosa | Tezkor savollar va uyga vazifa |

## 2. Konspekt

### 2.1. Indeks (1.54-rasm)
Real hayotda sanoq 1 dan boshlanadi, Pythonda esa **0** dan. String ketma-ketlik bo‘lgani uchun unda indeks bor. O‘zgaruvchi yonida `[ ]` ichida indeks yozsak, shu joydagi belgi olinadi.

```python
word = "Python"
print(word[0])    # P
print(word[1])    # y
print(word[-1])   # n (oxirgi)
```
| Belgi | P | y | t | h | o | n |
|---|---|---|---|---|---|---|
| Indeks | 0 | 1 | 2 | 3 | 4 | 5 |
| Manfiy indeks | -6 | -5 | -4 | -3 | -2 | -1 |

Matnni eng oxiridan indekslamoqchi bo‘lsak, sanoq **-1** dan boshlanadi.

### 2.2. Slicing (1.55-rasm)
**Slicing** — kesish, ya’ni string orasidan kerakli qismni kesib olish. Shakli:
```text
[boshlanish : tugash : qadam]
```
Namunalar (`word = "Python"`):
```python
print(word[1:4])    # yth   (1-indeksdan 4-indeksgacha, 4 kirmaydi)
print(word[:3])     # Pyt   (boshlanish yo'q: 0 dan)
print(word[3:])     # hon   (tugash yo'q: oxirigacha)
print(word[::2])    # Pto   (har ikkinchisi: 0, 2, 4)
print(word[::-1])   # nohtyP (teskari tartib)
```
Qoidalar:
- `[1:4]` — 1-indeksdan boshlab, 4-indeksgacha (4 o‘zi kirmaydi, `range` kabi);
- boshlanish berilmasa — 0 dan; tugash berilmasa — oxirigacha;
- `[::2]` — boshidan oxirigacha, har ikkinchisini oladi;
- `[::-1]` — oxiridan boshigacha, teskari.

### 2.3. String metodlari (1.56-rasm)
```python
s = "salom dunyo"
print(s.upper())        # SALOM DUNYO
print(s.lower())        # salom dunyo
print(s.title())        # Salom Dunyo
print(s.capitalize())   # Salom dunyo
```
- `upper()` — hammasi bosh harf;
- `lower()` — hammasi kichik harf;
- `title()` — har so‘zning bosh harfi katta;
- `capitalize()` — faqat birinchi harf katta.

Metodlar string o‘zgarmas bo‘lgani uchun **yangi string qaytaradi**, asl `s` o‘zgarmaydi.

## 3. Kod namunalari

### Namuna 1: Indekslar
```python
word = "Python"
print(word[0], word[1], word[-1])   # P y n
```

### Namuna 2: Slicing majmuasi
```python
word = "Python"
print(word[1:4])
print(word[:3])
print(word[3:])
print(word[::2])
print(word[::-1])
```
Natija: `yth`, `Pyt`, `hon`, `Pto`, `nohtyP`.

### Namuna 3: Metodlar va asl string
```python
s = "salom dunyo"
yangi = s.title()
print(yangi)   # Salom Dunyo
print(s)       # salom dunyo (o'zgarmadi)
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Birinchi va oxirgi harf (oson)
`word = "Backend"` stringining birinchi va oxirgi harfini chiqaring.

**Kutiladigan natija:** `B d`

**Yechim:**
```python
word = "Backend"
print(word[0], word[-1])
```

### 2-topshiriq. Teskari matn (oson)
`"Salom"` so‘zini teskari tartibda chiqaring.

**Kutiladigan natija:** `molaS`

**Yechim:**
```python
print("Salom"[::-1])
```

### 3-topshiriq. Bashorat (o‘rta)
`w = "Programmer"` bo‘lsa, `w[:4]`, `w[3:6]`, `w[::3]` nima beradi?

**Kutiladigan natija:** `Prog`, `gra`, `Pgmr`

**Yechim:** `w[:4]` — 0..3: `Prog`. `w[3:6]` — 3,4,5: `gra`. `w[::3]` — 0,3,6,9: `P`,`g`,`m`,`r` → `Pgmr`.

### 4-topshiriq. Ism formatlash (qiyin)
`ism = "aLiSHer"` ni to‘g‘ri yozing: `Alisher`. So‘ng ismning birinchi 3 harfini bosh harflar bilan chiqaring (`ALI`).

**Kutiladigan natija:**
```text
Alisher
ALI
```

**Yechim:**
```python
ism = "aLiSHer"
toza = ism.lower().capitalize()
print(toza)               # Alisher
print(toza[:3].upper())   # ALI
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **Python indeksi nechadan boshlanadi?**
   - *Javob:* 0 dan.
2. **`word[-1]` nima beradi?**
   - *Javob:* Oxirgi belgini.
3. **`"Python"[1:4]` natijasi?**
   - *Javob:* `yth` (4-indeks kirmaydi).
4. **`[::-1]` nima qiladi?**
   - *Javob:* Stringni teskari tartibda beradi.
5. **`title()` va `capitalize()` farqi?**
   - *Javob:* `title()` har so‘zni, `capitalize()` faqat birinchi harfni bosh qiladi.

## 6. Uyga vazifa

1. `slicing.py` da `word = "Backend"` uchun `[1:4]`, `[:3]`, `[3:]`, `[::2]`, `[::-1]` natijalarini avval taxmin qiling, keyin dasturda tekshiring.
2. `s = "ozbekiston respublikasi"` ni `upper()`, `lower()`, `title()`, `capitalize()` bilan chiqaring.
3. Ismingizni teskari yozing va birinchi harfini bosh harfda chiqaring.
