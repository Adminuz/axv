# 17-dars. Git va GitHub bilan tanishuv (4-qism): clone, pull va branch

> Loyiha GitHub'da turibdi. Bugun uni boshqa kompyuterga olamiz (clone), yangilaymiz (pull), alohida branchda tajriba qilamiz va chiroyli README yozamiz.

## Dars xulosasi

- `git clone URL` — to'liq nusxa olish.
- `git pull` — yangilanishlarni olish, `git push` — yuborish.
- Branch — parallel yo'l; `main` buzilmaydi.
- `git switch -c nom` — yangi branch, `git merge nom` — qo'shish.
- README.md — Markdown bilan yoziladigan loyiha vizitkasi.
- Ochiq README'ga shaxsiy ma'lumot yozilmaydi.

## Qo'shimcha ma'lumot

### Fork
Boshqaning repo'sini o'z akkauntingizga nusxalash.

### Pull Request
O'zgarishni qo'shishni taklif qilish.

### Conflict
Bir qatorning ikki xil o'zgarishi.

### Issue
GitHub'da vazifa yoki xato haqidagi yozuv.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| clone | Repository'ning to'liq nusxasi |
| pull | Yangilanishlarni yuklab olish |
| Branch | Parallel ish yo'li |
| main | Asosiy branch |
| merge | Branchlarni qo'shish |
| Markdown | Oddiy belgilar bilan matn bezash |
| README.md | Loyiha tavsifi fayli |
| Conflict | Qo'shishda ziddiyat |

## Bilasizmi?

- Katta kompaniyalarda `main` ga to'g'ridan-to'g'ri yozilmaydi: ish branchlarda bajarilib, tekshirilgach qo'shiladi.
- GitHub'da Pull Request orqali o'zgarishni taklif qilish mumkin: buni keyingi bosqichda o'rganasiz.
- Pull paytida ziddiyat (conflict) chiqishi mumkin: ikki kishi bir qatorni o'zgartirsa. Bu odatiy holat.

## Topshiriqlar

### 1. clone · oson

`clone` nima qilishini yozing.

**Kutiladigan natija:** To'liq nusxa olish.

### 2. pull · oson

`pull` nima uchun kerak?

**Kutiladigan natija:** Yangi commitlarni olish.

### 3. Branch · oson

Branch so'zini o'z so'zlaringiz bilan tushuntiring.

**Kutiladigan natija:** Parallel ish yo'li.

### 4. Asosiy branch · oson

Asosiy branch odatda qanday nomlanadi?

**Kutiladigan natija:** `main`.

### 5. Clone buyrug'i · o'rta

Repo'ni clone qilish buyrug'ini yozing.

**Kutiladigan natija:** `git clone URL`.

### 6. Branch ochish · o'rta

`rasm-qoshish` branch'ini yarating.

**Kutiladigan natija:** `git switch -c rasm-qoshish`.

### 7. Qaytish · o'rta

`main` ga qaytish buyrug'ini yozing.

**Kutiladigan natija:** `git switch main`.

### 8. Tartib · o'rta

Ish oldidan va keyin qaysi buyruqlar?

**Kutiladigan natija:** pull oldin, push keyin.

### 9. Merge · qiyin

Branchni `main` ga qo'shish bosqichlarini yozing.

**Kutiladigan natija:** `switch main`, `merge nom`.

### 10. Markdown · qiyin

3 ta Markdown belgisini misol bilan yozing.

**Kutiladigan natija:** `#`, `-`, `**`.

### 11. Xavfsiz README · qiyin

README'ga nimalarni yozish mumkin emas?

**Kutiladigan natija:** Telefon, manzil.

### 12. Portfolio README · bonus

O'zingiz haqingizda xavfsiz README yozing.

**Kutiladigan natija:** Chiroyli, xavfsiz README.

## O'zingizni tekshiring

1. clone nima?
2. pull nima?
3. Branch nima?
4. Branch qanday ochiladi?
5. merge qanday bajariladi?
6. Markdown belgilari?

## Uyga vazifa

README'ni to'ldiring, branch yarating va merge qiling (25–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
