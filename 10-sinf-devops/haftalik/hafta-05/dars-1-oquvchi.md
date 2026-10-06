# 13-dars. Matn filtralari va muntazam ifodalar: grep, sed, awk va xargs amaliyoti

> Server logi millionlab qator. Ko'z bilan o'qib bo'lmaydi, lekin `grep`, `sed` va `awk` bilan bir soniyada kerakli narsani topamiz.

---

## Dars xulosasi

- `grep` naqsh bo'yicha qator qidiradi: `-i`, `-n`, `-v`, `-c`, `-r`, `-E`.
- Regex: `^` boshi, `$` oxiri, `.` bitta belgi, `*` takror, `[0-9]` raqam.
- `sed 's/eski/yangi/g'` almashtiradi, `sed -n '3,5p'` qatorlarni tanlaydi.
- `awk '{print $3}'` ustun tanlaydi, `$NF` oxirgi ustun, `-F:` ajratgich.
- `xargs` chiqishni argumentga aylantiradi; qo'llanmadagi zanjir: `ps aux | grep nginx | awk '{print $2}' | xargs kill -9`.
- Zanjir: topish (grep), ajratish (awk), sanash (`sort | uniq -c`).

---

## Qo'shimcha ma'lumot

### 1. Nega `grep` o'zini topadi?
`ps aux | grep nginx` da `grep nginx` jarayonining o'zi ham ro'yxatda chiqadi. `grep [n]ginx` naqshi bu muammoni hal qiladi.

### 2. sed bilan ehtiyotkorlik
`sed -i` faylni to'g'ridan-to'g'ri o'zgartiradi. Avval natijani ekranda tekshiring yoki `-i.bak` bilan nusxa oling.

### 3. Odatiy xatolar
Naqshni tirnoqsiz yozish; `-E` siz `|` ishlatish; `awk` da ustun raqamini adashtirish; `kill -9` ni tekshirmasdan ishlatish.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **grep** | Naqsh bo'yicha qator qidiradi |
| **regex** | Muntazam ifoda: matn naqshi |
| **sed** | Oqim muharriri |
| **awk** | Ustunlar bilan ishlovchi til |
| **xargs** | Chiqishni argumentga aylantiradi |
| **PID** | Jarayon identifikatori |
| **stdin / stdout** | Kirish va chiqish oqimlari |
| **Heredoc** | Matnni skriptda `<<EOF` bilan berish |

---

## Bilasizmi?

- `grep` nomi `g/re/p` (global regular expression print) buyrug'idan kelib chiqqan.
- `awk` nomi uch yaratuvchisi Aho, Weinberger va Kernighan familiyalaridan olingan.
- DevOps muhandislari loglarni aynan shu vositalar bilan tahlil qiladi.

---

## Topshiriqlar

### 1. ERROR toping · oson
`app.log` yarating va `grep` bilan ERROR qatorlarini chiqaring.

**Kutiladigan natija:** 2 ta qator.

### 2. Qator raqami · oson
`grep -n` bilan `login` qatori raqamini toping.

**Kutiladigan natija:** `4:` bilan boshlangan qator.

### 3. Hammasi INFO emas · oson
INFO bo'lmagan qatorlarni chiqaring.

**Kutiladigan natija:** 3 ta qator.

### 4. Sanash · oson
WARN qatorlari sonini `grep -c` bilan toping.

**Kutiladigan natija:** 1

### 5. Registr · o'rta
`grep -i error app.log` va `grep error app.log` farqini tushuntiring.

**Kutiladigan natija:** Birinchisi topadi, ikkinchisi topmaydi.

### 6. Regex · o'rta
`user=` dan keyin 3 harfli nomni (`a.i`) naqsh bilan toping.

**Kutiladigan natija:** `user=ali` qatori.

### 7. sed almashtirish · o'rta
`sed` bilan `user=` ni `foydalanuvchi=` ga almashtiring.

**Kutiladigan natija:** Ekranda yangi matn, fayl o'zgarmagan.

### 8. awk ustun · o'rta
`awk` bilan faqat vaqt (2-ustun) va daraja (3-ustun) ni chiqaring.

**Kutiladigan natija:** `10:00:01 INFO` ko'rinishidagi qatorlar.

### 9. Daraja hisoboti · qiyin
Darajalar bo'yicha sanoqni (`sort | uniq -c`) chiqaring.

**Kutiladigan natija:** 2 ERROR, 2 INFO, 1 WARN.

### 10. Foydalanuvchi ro'yxati · qiyin
`/etc/passwd` dan faqat foydalanuvchi nomlarini `awk -F:` bilan oling va alifbo tartibida chiqaring.

**Kutiladigan natija:** Tartiblangan nomlar.

### 11. xargs bilan fayllar · qiyin
`find` va `xargs grep -l` bilan ichida ERROR bor `.log` fayllarni toping.

**Kutiladigan natija:** Fayl nomlari ro'yxati.

### 12. Xavfsiz kill · bonus
`sleep 300 &` ishga tushirib, `ps aux | grep [s]leep | awk '{print $2}' | xargs kill` bilan to'xtating.

**Kutiladigan natija:** Jarayon yo'qoladi.

---

## O'zingizni tekshiring

1. `grep -c` nima qiladi?
2. `^` va `$` nima?
3. `sed 's/a/b/'` nima qiladi?
4. `awk` da `$NF` nima?
5. `xargs` nima uchun kerak?
6. `grep [n]ginx` nima uchun yoziladi?
7. `sort | uniq -c` nima beradi?

---

## Uyga vazifa

`app.log` ni tahlil qiluvchi `tahlil.sh` yozing (25 daqiqa). To'liq shart: `uyga-vazifa.md`.
