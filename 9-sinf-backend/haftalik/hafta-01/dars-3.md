# 3-dars. O‘zgaruvchilar va ma'lumotlar bilan ishlash

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** ma'ruza + amaliyot · **I-bob**, 3-dars

## 1. Dars rejasi

**Maqsad:** O‘quvchilarga o‘zgaruvchilar yaratish, qiymat berish (`=`), nomlash qoidalari (snake_case) va rasmiy qo‘llanmadagi "Tanishuv kartochkasi" hamda "Do‘kon kassasi" amaliy loyihalarini mustaqil bajarishni o‘rgatish.

**Kutiladigan natija:**
- O‘zgaruvchini xotiradagi "quti" sifatida tushunadi va to‘g‘ri nomlaydi.
- Pythonda o‘zgaruvchi turini oldindan e'lon qilish shart emasligini (dinamik tiplashuv) biladi.
- Bir nechta o‘zgaruvchini bitta `print()` ichida chiroyli formatlab chiqara oladi.
- "Tanishuv kartochkasi" va "Do‘kon kassasi" loyihalarini to‘liq xatosiz yozadi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–5 daq | Takrorlash | 2-dars: toifalar (int, float, str, bool) va arifmetik amallar |
| 5–25 daq | Yangi mavzu 1 | O‘zgaruvchi nima? "Quti" analogiyasi va `=` operatori |
| 25–40 daq | Yangi mavzu 2 | Nomlash qoidalari, man etilgan nomlar va snake_case |
| 40–45 daq | Tanaffus | Chigil yozdi mashqlari |
| 45–65 daq | Amaliyot 1 & 2 | "Tanishuv kartochkasi" va "Do‘kon kassasi" loyihalari |
| 65–75 daq | Amaliy topshiriqlar | O'quvchilarning mustaqil mini-loyihalari |
| 75–80 daq | Xulosa va tezkor savollar | 1-hafta yakuniy xulosasi va uyga vazifa |

## 2. Konspekt

### 2.1. O‘zgaruvchi nima?
O‘zgaruvchi — bu kompyuter xotirasidagi ma’lumotni saqlash uchun berilgan nomdir.
O‘zgaruvchini oddiy qilib xotiradagi yorliqli **quti 📦** deb tasavvur qilish mumkin:
- Qutining nomi bo‘ladi (masalan, `ism` yoki `yosh`);
- Qutining ichiga biror ma'lumot joylaymiz (masalan, `"Ali"` yoki `15`);
- Dasturning istalgan joyida qutining nomini aytib, uning ichidagi ma'lumotdan foydalanamiz.

```python
ism = "Ali"      # Matnli ma'lumot
yosh = 15        # Butun sonli ma'lumot
```
Bu yerda:
- `ism`, `yosh` — o‘zgaruvchi nomlari;
- `=` — o‘zlashtirish (qiymat berish) operatori;
- `"Ali"`, `15` — o‘zgaruvchiga yuklangan qiymatlar.

### 2.2. Pythonda dinamik tiplashtirish
Muhim qoida: Pythonda o‘zgaruvchi yaratishdan avval uni maxsus e'lon qilish, uning turini avvaldan ko‘rsatish shart emas. Python berilgan qiymatga qarab o‘zgaruvchining turini avtomatik aniqlab oladi.
```python
x = 10        # x avtomatik int bo'ldi
x = "O'n"     # endi x matn (str) bo'lib o'zgardi
```

### 2.3. O‘zgaruvchilarni nomlash qoidalari
Dastur toza va xatosiz ishlashi uchun o‘zgaruvchilarni to‘g‘ri nomlash zarur:
1. **Harf yoki tagchiziq (`_`) bilan boshlanishi kerak:**
   - `ism`, `_maxfiy`, `user_1` — to‘g‘ri.
   - `1_user`, `9-sinf` — XATO! Raqamdan boshlanishi mumkin emas.
2. **Probel (bo‘sh joy) va maxsus belgilar bo‘lishi mumkin emas:**
   - `foydalanuvchi yoshi` — XATO! O‘rniga `foydalanuvchi_yoshi` deb yoziladi.
   - `foydalanuvchi-yoshi`, `narx$` — XATO!
3. **Katta-kichik harflar farqlanadi:**
   - `yosh`, `Yosh`, `YOSH` — bular 3 ta mutlaqo boshqa-boshqa o‘zgaruvchi.
4. **Pythondagi kalit so‘zlardan nom sifatida foydalanib bo‘lmaydi:**
   - `print`, `type`, `if`, `for`, `class` — bularni o‘zgaruvchi nomi qilib bo‘lmaydi.
5. **Uslub qoidasi:** Pythonda so‘zlar kichik harflar bilan va orasi tagchiziq bilan ajratiladi — bu **snake_case** deb ataladi (masalan, `foydalanuvchi_nomi`, `server_porti`).

### 2.4. Rasmiy amaliy loyihalar tahlili

#### Loyiha 1: "Tanishuv kartochkasi"
Talab: `ism`, `yosh`, `kasb` o‘zgaruvchilarini yaratib, ularni bitta `print()` ichida ekranga chiqarish.
```python
ism = "Ali"
yosh = 15
kasb = "Dasturchi"

print("Ism:", ism, "| Yosh:", yosh, "| Kasb:", kasb)
```

#### Loyiha 2: "Do‘kon kassasi"
Talab: `non_narxi = 3000` va `sut_narxi = 12500.5` o‘zgaruvchilarini yaratish. Ikkala mahsulotdan bittadan olganda jami qancha bo‘lishini hisoblab, `jami` o‘zgaruvchisiga yuklash va natijani chiqarish.
```python
non_narxi = 3000
sut_narxi = 12500.5

jami = non_narxi + sut_narxi
print("Jami to'lov:", jami, "so'm")
```

## 3. Kod namunalari

### Namuna 1: Qiymatlarni yangilash (Qayta o‘zlashtirish)
```python
hisob = 50000
print("Boshlang'ich hisob:", hisob)

# Hisobga pul tushdi
hisob = hisob + 20000
print("Yangi hisob:", hisob)

# Qisqartirilgan operator (+=)
hisob += 15000
print("Yakuniy hisob:", hisob)
```

### Namuna 2: f-string orqali o‘zgaruvchilarni matnga joylash
```python
nomi = "FastAPI Server"
port = 8080
faol = True

# Zamonaviy f-string uslubi
log_xabar = f"Tizim: {nomi} | Port: {port} | Holati: {faol}"
print(log_xabar)
```

## 4. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Tanishuv kartochkasi (oson)
`ism`, `yosh`, `kasb` o‘zgaruvchilarini yarating. O‘z ma'lumotlaringizni bering va bitta `print()` yordamida ekranga chiqaring.

**Kutiladigan natija:**
`Ism: Jasur | Yosh: 15 | Kasb: DevOps muhandisi`

**Yechim:**
```python
ism = "Jasur"
yosh = 15
kasb = "DevOps muhandisi"
print("Ism:", ism, "| Yosh:", yosh, "| Kasb:", kasb)
```

### 2-topshiriq. Do‘kon kassasi (oson)
`non_narxi = 3000` va `sut_narxi = 12500.5` o‘zgaruvchilarini yarating. Ularning yig‘indisini `jami` o‘zgaruvchisiga yuklang va natijani konsolga chiqaring.

**Kutiladigan natija:**
`Jami summa: 15500.5 so'm`

**Yechim:**
```python
non_narxi = 3000
sut_narxi = 12500.5
jami = non_narxi + sut_narxi
print("Jami summa:", jami, "so'm")
```

### 3-topshiriq. Kengaytirilgan savat (o'rta)
Savatchada 3 dona non (`non_narxi = 3000`) va 2 dona sut (`sut_narxi = 12500.5`) bor. Har birining umumiy summasi va umumiy xarid qiymatini hisoblang.

**Kutiladigan natija:**
```text
Nonlar summasi: 9000 so'm
Sutlar summasi: 25001.0 so'm
Jami to'lov: 34001.0 so'm
```

**Yechim:**
```python
non_narxi = 3000
sut_narxi = 12500.5

non_soni = 3
sut_soni = 2

jami_non = non_narxi * non_soni
jami_sut = sut_narxi * sut_soni
jami_to'lov = jami_non + jami_sut

print("Nonlar summasi:", jami_non, "so'm")
print("Sutlar summasi:", jami_sut, "so'm")
print("Jami to'lov:", jami_to'lov, "so'm")
```

### 4-topshiriq. Qiymatlarni almashtirish (Swap) (qiyin)
Ikkita o‘zgaruvchi berilgan: `a = 10` va `b = 20`. Qo‘shimcha o‘zgaruvchisiz ularning qiymatlarini o‘zaro almashtiring (`a = 20`, `b = 10`).

**Kutiladigan natija:**
```text
Almashtirishdan oldin: a = 10, b = 20
Almashtirishdan keyin: a = 20, b = 10
```

**Yechim:**
```python
a = 10
b = 20
print(f"Almashtirishdan oldin: a = {a}, b = {b}")

# Pythonning qulay usuli (tuple unpacking)
a, b = b, a

print(f"Almashtirishdan keyin: a = {a}, b = {b}")
```

## 5. Tezkor nazorat (savollar va javoblar)

1. **O‘zgaruvchi nomini `2_sinf` deb nomlash mumkinmi va nega?**
   - *Javob:* Yo‘q, chunki Python o‘zgaruvchilari hech qachon raqam bilan boshlanishi mumkin emas.
2. **`=` belgisi nima vazifani bajaradi?**
   - *Javob:* O‘ng tarafdagi qiymatni chap tarafdagi o‘zgaruvchiga yuklaydi (o‘zlashtirish amali).
3. **`non_narxi` va `sut_narxi` qo‘shilganda natija qaysi toifada bo‘ladi (`int` yoki `float`)?**
   - *Javob:* `float` bo‘ladi, chunki `sut_narxi` (12500.5) kasr son bo‘lgani uchun Python umumiy natijani avtomatik `float` ga o‘tkazadi.
4. **snake_case uslubi qanday yoziladi?**
   - *Javob:* So‘zlar kichik harflar bilan va orasi tagchiziq (`_`) bilan ajratilgan holda (masalan: `talaba_bahosi`).

## 6. Uyga vazifa

1. `profil.py` faylini oching. Unda o‘zingizning virtual serveringiz parametrlarini saqlovchi o‘zgaruvchilar yarating: `server_nomi`, `ip_manzil`, `ram_gb`, `xotira_ssd_gb`, `faolmi`.
2. Ularni konsolga f-string orqali tartibli xabar ko‘rinishida chiqaring.
3. Yangi mahsulotlar (masalan: `olma_narxi = 8000`, `suv_narxi = 2500`) qo‘shib, "Do‘kon kassasi" dasturini 4 ta mahsulot uchun kengaytiring.
