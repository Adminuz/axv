# 5-hafta. Uyga vazifalar

Har bir vazifa 20–30 daqiqa. Kodlar alohida `hafta-05` papkasida saqlanadi.

## 13-dars uchun (Tuple: o‘zgarmas ketma-ketlik)
**1-topshiriq: «Hafta kunlari va koordinatalar»**
`tuple_mashq.py` faylini oching:
1. Haftaning 7 kunini tuple’da saqlang; birinchi, oxirgi kunni va ish kunlarini (slicing) chiqaring.
2. `(2, 5, 5, 3, 5, 4, 2)` tuple’ida har bir son necha marta uchrashini `count()` bilan chiqaring.
3. Sevimli shahringiz koordinatasini tuple’da saqlang, list orqali uzunlikni o‘zgartirib, qayta tuple qiling.

**Kutiladigan natija:** Tuple to‘g‘ri yaratilgan, indeks, slicing va `count()` ishlatilgan, o‘zgartirish faqat list orqali bajarilgan.

## 14-dars uchun (Set: takrorlanmaydigan elementlar)
**2-topshiriq: «Takrorsiz to‘plamlar»**
`set_mashq.py` faylida:
1. `[3, 7, 3, 9, 7, 1, 9]` listidan takrorlarni olib tashlab, tartiblangan holda chiqaring.
2. Ikki do‘stingizning sevimli o‘yinlarini ikki set qilib birlashtiring: jami nechta turli o‘yin bor?
3. Bloklangan loginlar setini yarating va foydalanuvchi kiritgan login bloklanganini `in` bilan tekshiring.

**Kutiladigan natija:** `set()`, `add()`, birlashtirish, `sorted()` va `in` to‘g‘ri ishlatilgan.

## 15-dars uchun (Dictionary va «Talabalar ma’lumotlari»)
**3-topshiriq: «Lug‘at va talaba kartasi»**
1. `lugat.py`: 5 ta inglizcha so‘z va tarjimasidan dict yarating; foydalanuvchi so‘z kiritsa tarjimasi chiqsin, topilmasa `"Bunday so'z yo'q"` (`get()`).
2. «Talabalar ma’lumotlari» loyihasini yakunlang: yana bitta fan (`append`) va `telefon` kalitini qo‘shing, natijani chiroyli chiqaring.

**Kutiladigan natija:** Dict’da qiymat olish, `get()`, yangilash va qo‘shish ishlatilgan; loyihada 5 ta tuzilma bor.

## Mentor uchun
Keyingi dars (16-dars, DRY va funksiyalar) boshida «Talabalar ma’lumotlari» loyihasidan 2–3 o‘quvchining kodini ekranda ko‘rsating: qayerda bir xil `print` qatorlari takrorlanganini topib, funksiyaga ehtiyojni his qildiring. `{}` ni bo‘sh set deb yozgan va `d["key"]` da `KeyError` olgan o‘quvchilarni alohida tekshiring: bu haftaning eng ko‘p uchraydigan xatolari.
