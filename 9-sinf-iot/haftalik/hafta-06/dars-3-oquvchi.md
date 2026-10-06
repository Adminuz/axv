# 18-dars. Arduino Uno va Tinkercad asosida svetofor tizimini modellashtirish (1-qism)

> Yo'ldagi svetofor oddiy mantiq bilan ishlaydi: qizil, sariq, yashil — va vaqt. Bugun Tinkercad'da o'zimizning svetoforimizni yig'ib, Arduino bilan boshqaramiz.

## Dars xulosasi

- Svetofor — LEDlar ketma-ket yonadigan tizim.
- Algoritm: qizil 5 s, sariq 2 s, yashil 5 s, takrorlash.
- LED rezistor orqali ulanadi (220–330 Ω), katod — GND.
- `setup()` da pinlar OUTPUT qilinadi.
- `loop()` da yoq → `delay` → o'chir ketma-ketligi takrorlanadi.
- Start Simulation bilan natija tekshiriladi.

## Qo'shimcha ma'lumot

### Om qonuni
U = I · R: kuchlanish, tok va qarshilik bog'liqligi.

### Breadboard
Lehimsiz ulash taxtasi.

### Sekundomer
Simulyatsiyada vaqtlarni o'lchab tekshiring.

### Kodni tartibli yozish
O'zgaruvchi nomlari (red, yellow, green) o'qishni osonlashtiradi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| LED | Yorug'lik chiqaruvchi diod |
| Anod | LEDning (+) oyog'i |
| Katod | LEDning (−) oyog'i |
| Rezistor | Tokni cheklovchi komponent |
| Om qonuni | U = I · R |
| pinMode | Pin rejimini belgilaydi |
| digitalWrite | Pinga HIGH/LOW beradi |
| delay | Kutish funksiyasi (ms) |

## Bilasizmi?

- Haqiqiy svetoforda ko'pincha yashildan keyin sariq yonadi, qizil bilan birga sariq esa ba'zi mamlakatlarda yashil oldidan yonadi.
- Tinkercad — Autodesk'ning bepul onlayn virtual laboratoriyasi.
- LED atamasi Light Emitting Diode — «yorug'lik chiqaruvchi diod» degani.

## Topshiriqlar

### 1. Algoritm · oson

Svetofor ketma-ketligi va vaqtlarini yozing.

**Kutiladigan natija:** Qizil 5, sariq 2, yashil 5

### 2. Komponentlar · oson

Svetofor sxemasi uchun kerakli komponentlarni sanang.

**Kutiladigan natija:** Arduino, 3 LED, 3 rezistor, simlar

### 3. Anod/katod · oson

LEDning qaysi oyog'i GND ga ulanadi?

**Kutiladigan natija:** Katod

### 4. delay · oson

3 soniya kutish uchun `delay` qiymatini yozing.

**Kutiladigan natija:** delay(3000)

### 5. Pinlar · o'rta

Qizil, sariq, yashil LED qaysi pinlarga ulangan?

**Kutiladigan natija:** 9, 8, 7

### 6. setup · o'rta

`setup()` da nima qilinadi?

**Kutiladigan natija:** pinMode OUTPUT

### 7. loop · o'rta

`loop()` nima uchun doimiy takrorlanadi?

**Kutiladigan natija:** Svetofor to'xtamasligi uchun

### 8. Rezistor · o'rta

Rezistorsiz LEDni ulasak nima bo'lishi mumkin?

**Kutiladigan natija:** LED kuyadi

### 9. Vaqt · qiyin

Qizil 4 s, sariq 1 s, yashil 6 s uchun loop() yozing.

**Kutiladigan natija:** Yangi vaqtlar

### 10. Tahlil · qiyin

Simulyatsiyada sariq LED yonmasa, nimalarni tekshirasiz?

**Kutiladigan natija:** Pin, rezistor, kod

### 11. Haqiqiy tartib · qiyin

Qizil → yashil → sariq tartibida kod yozing.

**Kutiladigan natija:** Qayta yozilgan loop()

### 12. O'z g'oyangiz · bonus

Piyodalar uchun ikki LEDli svetofor g'oyasini yozing.

**Kutiladigan natija:** Qizil va yashil

## O'zingizni tekshiring

1. Svetofor algoritmi?
2. LED qanday ulanadi?
3. Rezistor nima uchun?
4. setup va loop farqi?
5. delay nima qiladi?
6. Simulyatsiya qanday boshlanadi?

## Uyga vazifa

Tinkercad'da svetoforni qayta yig'ing va vaqtlarni o'zgartiring (30–40 daqiqa). To'liq shart: `uyga-vazifa.md`.
