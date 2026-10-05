# 12-dars. Kotlin sintaksisi: if va when shart operatorlari

> Dasturda qarorlar qabul qilish va shartlar bo'yicha turli amallarni bajarish vaqti keldi! Ushbu darsda Kotlindagi `if-else` ifodalari hamda eng qudratli `when` operatorini o'rganamiz.

## Dars xulosasi

- **`if-else` ifoda sifatida (Expression):** Kotlinda `if` nafaqat shart tekshiradi, balki natija ham qaytara oladi (`val max = if (a > b) a else b`).
- **Ternar operatori yo'qligi:** Java'dagi `a ? b : c` o'rniga to'g'ridan-to'g'ri `if (a) b else c` yoziladi.
- **`when` operatori:** Java'dagi `switch` operatorining zamonaviy va kuchaytirilgan ko'rinishi.
- **`when` afzalliklari:**
  - `break` so'zini yozish umuman shart emas;
  - Bir nechta qiymatni vergul bilan tekshirish mumkin (`1, 2 -> ...`);
  - Oraliqlarni (`in 1..10 -> ...`) tekshirish mumkin;
  - Ifoda sifatida o'zgaruvchiga qiymat yuklay oladi (`val baho = when (ball) { ... }`).

## Qo'shimcha ma'lumot

### Nega `when` ifoda sifatida ishlatilganda `else` shart?
Agar `val natija = when (kun) { 1 -> "Du", 2 -> "Se" }` deb yozsak va `kun = 5` bo'lib qolsa, o'zgaruvchiga qanday qiymat yuklash noma'lum bo'ladi. Shu sababli Kotlin kompilyatori xatolik bermasligi uchun majburiy `else` talab qiladi.

### Range (Oraliq) &mdash; `..` operatori
Kotlinda `1..5` yozuvi 1, 2, 3, 4, 5 sonlarini o'z ichiga olgan oraliqni bildiradi. Shart tekshirishda `in 1..5` yoki `!in 1..5` (oraliqqa kirmaslik) ko'rinishida qo'llaniladi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| Condition (Shart) | Mantiqiy ifoda (`true` yoki `false`) |
| if-else | Shartli tarmoqlanish operatori |
| when | Ko'p variantli tanlash operatori |
| Expression (Ifoda) | Bajarilgach, aniq bir natija (qiymat) qaytaruvchi kod bo'lagi |
| Range | Sonlar oralig'i (`1..100`) |
| else | Yuqoridagi barcha shartlar bajarilmaganda ishga tushuvchi zaxira blok |

## Bilasizmi?

- Kotlindagi `when` operatori nafaqat son va matnlarni, balki har qanday murakkab obyektlarni va ularning turlarini (`is String`, `is Int`) ham tekshira oladi.
- Android ilovalarida tugma bosilganda qaysi element tanlanganini aniqlashda `when (view.id) { ... }` eng ko'p ishlatiladigan andoza hisoblanadi.

## Topshiriqlar

### 1. Juft yoki toq · oson

Sonning juft yoki toqligini `val tur = if (son % 2 == 0) "Juft" else "Toq"` shaklida aniqlang. 3 xil son bilan sinang.

**Kutiladigan natija:** har son uchun to'g'ri javob.

### 2. Katta son · oson

`a` va `b` sonlardan kattasini `if` ifodasi bilan bitta qatorda toping.

**Kutiladigan natija:** `val kattasi = if (a > b) a else b` va to'g'ri natija.

### 3. Fasllar · oson

1–4 raqamga qarab fasl nomini `when` bilan chiqaring. Boshqa son kelsa, «Noto'g'ri fasl raqami» chiqsin.

**Kutiladigan natija:** 5 ta sinovda to'g'ri javob, jumladan `else` holati.

### 4. Kirish ruxsati · oson

Yosh 18 dan katta yoki teng bo'lsa «Xush kelibsiz!», aks holda «Kirish taqiqlanadi.» chiqaring.

**Kutiladigan natija:** 17 va 18 yosh uchun ikki xil natija.

### 5. Hafta kunlari · o'rta

1 dan 7 gacha son bo'yicha hafta kuni nomini `when` ifodasi bilan `val kunNomi` ga saqlang.

**Kutiladigan natija:** 7 ta to'g'ri javob va `else` uchun «Bunday kun yo'q».

### 6. Ball → baho · o'rta

Ballni `when` va `in` oraliqlari bilan bahoga aylantiring: 90–100 → 5, 70–89 → 4, 60–69 → 3, 0–59 → 2.

**Kutiladigan natija:** 88 → 4, 95 → 5, 59 → 2, 120 → «Noto'g'ri ball».

### 7. Natijani bashorat qiling · o'rta

Ishga tushirmasdan javob bering, keyin tekshiring:

```kotlin
val x = 10
val s = when {
    x > 5 -> "katta"
    x > 0 -> "musbat"
    else -> "boshqa"
}
println(s)
```

**Kutiladigan natija:** `katta`: birinchi to'g'ri shart bajarilgach `when` to'xtaydi.

### 8. Bir nechta qiymat · o'rta

Oy raqami bo'yicha faslni toping: `12, 1, 2 -> "Qish"` kabi vergul bilan bir nechta qiymat yozing.

**Kutiladigan natija:** 12 ta oy uchun to'g'ri fasl.

### 9. Xatoni toping · qiyin

Bu kod kompilyatsiya bo'lmaydi. Nega? Tuzating:

```kotlin
val ball = 75
val baho = when (ball) {
    in 90..100 -> "A'lo"
    in 70..89 -> "Yaxshi"
}
```

**Kutiladigan natija:** sabab: ifoda sifatidagi `when` da `else` yo'q; `else -> ...` qo'shilgan.

### 10. Svetofor moduli · qiyin

Chiroq rangi (`"Qizil"`, `"Sariq"`, `"Yashil"`) va tezlik berilgan. Yashilda tezlik 60 dan oshsa ogohlantirish chiqaring. `when` ichida `if` ishlating.

**Kutiladigan natija:** 4 ta holat uchun to'g'ri ko'rsatma, jumladan noma'lum signal.

### 11. Mini-kalkulyator · qiyin

`a = 20.0`, `b = 5.0` va `amal` (`"+"`, `"-"`, `"*"`, `"/"`) berilgan. `when (amal)` bilan natijani hisoblang. `b = 0.0` bo'lsa bo'lishda ogohlantirish chiqsin.

**Kutiladigan natija:** to'rt amal uchun to'g'ri natija va nolga bo'lish holati.

### 12. Chegirma tizimi · bonus

Xarid summasiga qarab chegirmani toping: 100 minggacha 0%, 500 minggacha 5%, 1 milliongacha 10%, undan ko'p 15%. Yakuniy to'lovni chiqaring.

**Kutiladigan natija:** bir nechta summa uchun to'g'ri chegirma va to'lov.

## O'zingizni tekshiring

1. Kotlin'da ternar operator bormi? Uning o'rniga nima ishlatiladi?
2. `if` ifoda sifatida ishlatilganda `else` shartmi?
3. `when` Java'dagi qaysi operator o'rnini bosadi?
4. `when` da `break` yozish kerakmi?
5. Oraliq qanday tekshiriladi?
6. `when` ifoda sifatida ishlatilganda nima majburiy?
7. Argumentsiz `when { ... }` qachon qulay?

## Uyga vazifa

Yosh toifasini aniqlash (`when` + `in`), mini-kalkulyator va chegirma tizimi dasturlarini yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
