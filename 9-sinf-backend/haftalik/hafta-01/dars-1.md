# 1-dars. Python: o‘rnatish, muhit sozlash va ilk dastur

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 1-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga Python interpretatorini kompyuterga to‘g‘ri o‘rnatish, tizim o‘zgaruvchilariga qo‘shish (Add to PATH), buyruqlar satri (CMD/terminal) orqali tekshirish va ilk `print("Hello, World!")` dasturini mustaqil ishga tushirishni o‘rgatish.

**Kutiladigan natija:**
- Python interpretatori nima ekanligini va nima uchun kerakligini tushunadi.
- python.org saytidan kerakli versiyani yuklab olib, "Add python.exe to PATH" parametri bilan o‘rnatadi.
- Terminal/CMD oynasida `python --version` orqali o‘rnatilishni tekshiradi.
- Interaktiv rejimda (`>>>`) va VS Code muharririda birinchi dasturini yozadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Tanishuv va kirish | Backend dasturlash va DevOps kursi maqsadi, Python roli |
| 5–25 daq | Yangi mavzu 1 | Python nima? python.org dan yuklab olish, PATH sozlamasi |
| 25–40 daq | Yangi mavzu 2 | CMD/Terminal bilan ishlash, interaktiv rejim (REPL) |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Yangi mavzu 3 & Amaliyot | VS Code muhiti, `app.py` fayli, `print("Hello, World!")` |
| 65–75 daq | Amaliy topshiriqlar | O'quvchilar mustaqil kod yozishi va xatolarni tekshirish |
| 75–80 daq | Xulosa va tezkor savollar | Dars xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. Python dasturlash tili haqida
Python — ochiq kodli, yuqori darajadagi, o‘rganishga oson va zamonaviy IT sanoatida eng ommabop dasturlash tillaridan biri. U veb backend (FastAPI, Django), avtomatlashtirish, sun'iy intellekt, ma'lumotlar tahlili va DevOps amaliyotlarida asosiy vosita hisoblanadi.

### 2.2. Python interpretatorini o‘rnatish
1. `www.python.org` rasmiy veb-saytiga kiramiz va **Downloads** bo‘limiga o‘tamiz.
2. O‘rnatish faylini (installer) yuklab olib ishga tushiramiz.
3. **Eng muhim nuqta:** O‘rnatish oynasidagi ikkita katakka belgi (галочка) qo‘yish shart:
   - `Use admin privileges when installing py.exe`
   - `Add python.exe to PATH` (Bu parametr kompyuterning istalgan joyidan `python` buyrug‘ini ishga tushirish imkonini beradi).
4. `Customize installation` yoki `Install Now` orqali standart sozlamalar bilan o‘rnatamiz.
5. O‘rnatish yakunlangach, agar `Disable path length limit` ko‘rinsa, uni tasdiqlab, `Close` tugmasini bosamiz.

### 2.3. O‘rnatishni CMD/Terminal orqali tekshirish
- Windows tizimida: `Win + R` bosing, `cmd` deb yozing va `Enter` bosing.
- macOS/Linux tizimida: `Terminal` dasturini oching.
- Buyruqlar satriga quyidagini kiriting:
```bash
python --version
```
Agar `Python 3.12.x` yoki shunga o‘xshash versiya ko‘rinsa, demak interpretator to‘g‘ri o‘rnatilgan.

### 2.4. Interaktiv rejim (REPL) va birinchi dastur
Terminalda shunchaki `python` buyrug‘ini kiritsak, interpretatorning interaktiv rejimi ochiladi va ekranda `>>>` belgisi paydo bo‘ladi.
```python
>>> print("Hello, World!")
Hello, World!
```
Bu rejimdan chiqish uchun `exit()` funksiyasi chaqiriladi yoki `Ctrl + Z` (Windows) / `Ctrl + D` (macOS/Linux) bosiladi.

### 2.5. Faylda dastur yozish (VS Code muhiti)
Interaktiv rejim tezkor sinovlar uchun qulay, lekin katta loyihalar fayllarda (`.py` kengaytmasi bilan) yoziladi.
1. VS Code muharririda yangi `main.py` faylini ochamiz.
2. Kod yozamiz:
```python
print("Salom, Muhammad al-Xorazmiy vorislari!")
print("Men backend dasturchi bo'laman.")
```
3. Terminal orqali ishga tushiramiz:
```bash
python main.py
```

## 3. Kod namunalari

### Namuna 1: print() yordamida matn va xabarlarni chiqarish
```python
# Birinchi Python dasturi
print("Assalomu alaykum!")
print("Backend dasturlash olamiga xush kelibsiz.")

# Bir nechta argumentlarni chiqarish
print("Python", "Back-end", "DevOps", sep=" | ")
```

### Namuna 2: Qatorlarni bo'lish va parametrlar
```python
# end parametri yordamida yangi qatorga o'tishni boshqarish
print("Yuklanmoqda...", end=" ")
print("Bajarildi!")
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Tizimda Python versiyasini tekshirish (oson)
Kompyuteringizda terminalni oching va o‘rnatilgan Python interpretatori versiyasini aniqlang.

**Kutiladigan natija:** Konsolda `Python 3.x.x` ko‘rinishida xabar chiqishi.

**Yechim:**
```bash
python --version
# yoki
python -V
```

### 2-topshiriq. Tanishuv xabari (oson)
`tanishuv.py` faylini yarating va unda o‘zingiz haqingizda 3 qatordan iborat ma'lumot chiqaring: ismingiz, yoshingiz va qiziqqan yo‘nalishingiz.

**Kutiladigan natija:**
```text
Ismim: Sardor
Yoshim: 15
Yo'nalishim: Advanced Back-end va DevOps
```

**Yechim:**
```python
print("Ismim: Sardor")
print("Yoshim: 15")
print("Yo'nalishim: Advanced Back-end va DevOps")
```

### 3-topshiriq. Shior va ramka yasash (o'rta)
`shior.py` faylida konsolda yulduzchalar (`*`) yoki chiziqchalar (`-`) yordamida chiroyli ramka ichida dasturlash shioringizni chiqaring.

**Kutiladigan natija:**
```text
***********************************
*   Backend — tizimning yuragi!   *
***********************************
```

**Yechim:**
```python
print("*" * 35)
print("*   Backend — tizimning yuragi!   *")
print("*" * 35)
```

### 4-topshiriq. sep va end parametrlari bilan ishlash (qiyin)
Bitta `print()` yoki bir nechta `print()` orqali server holatini quyidagicha bitta satrda chiqaring: `Server: OK | Port: 8000 | Status: Active`.

**Kutiladigan natija:**
`Server: OK | Port: 8000 | Status: Active`

**Yechim:**
```python
print("Server: OK", "Port: 8000", "Status: Active", sep=" | ")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **Python o‘rnatishda "Add python.exe to PATH" katagi belgilanmasa nima bo‘ladi?**
   - *Javob:* Terminalda `python` deb yozganda operatsion tizim uni taniydi olmaydi va `'python' is not recognized` xatoligi yuzaga keladi.
2. **Interpretatorning interaktiv rejimi qaysi belgi bilan boshlanadi?**
   - *Javob:* `>>>` belgisi bilan.
3. **Python fayllari qanday kengaytma bilan saqlanadi?**
   - *Javob:* `.py` kengaytmasi bilan.
4. **`print()` funksiyasida matnlar qanday belgilar ichida yoziladi?**
   - *Javob:* Qo‘shtirnoq (`"..."`) yoki birtirnoq (`'...'`) ichida.

## 6. Uyga vazifa

1. Uy kompyuteringizga Python 3.12+ va VS Code dasturini o‘rnating.
2. `salom.py` faylini yaratib, unda 5 ta qatordan iborat dasturlash haqidagi fikrlaringizni konsolga chiqaring.
3. Terminal orqali `python salom.py` buyrug‘i bilan dasturni ishga tushiring va natija skrinshotini tayyorlang.
