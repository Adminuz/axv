---
title: "12-dars. Sikllar va takrorlanishlar (for, while, until) hamda matnli oqimlarni qayta ishlash"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "10-sinf (DevOps)", "link": "/10-sinf-devops/"}, "week": {"n": 4, "link": "/10-sinf-devops/hafta-04/"}, "g": 12, "title": "Sikllar va takrorlanishlar (for, while, until) hamda matnli oqimlarni qayta ishlash", "lead": "Kompyuter charchamaydi: 1000 marta takrorlash unga bir qator. Bugun sikllar va quvurlar bilan matnli ma'lumotni «tegirmon» kabi ishlaymiz.", "slide": "/slaydlar/10-sinf-devops/hafta-04/dars-3.html", "test": "/slaydlar/10-sinf-devops/hafta-04/dars-3-test.html", "tabs": [{"g": 10, "link": "/10-sinf-devops/hafta-04/dars-1", "current": false}, {"g": 11, "link": "/10-sinf-devops/hafta-04/dars-2", "current": false}, {"g": 12, "link": "/10-sinf-devops/hafta-04/dars-3", "current": true}], "prev": {"g": 11, "title": "Shart operatorlari va mantiqiy ifodalar (if/elif/else, test, [[ ]], arifmetik amallar)", "link": "/10-sinf-devops/hafta-04/dars-2"}, "next": null}
---

---

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- `for` ro'yxat, diapazon (`{1..5}`), fayl naqshi (`*.txt`) yoki C uslubi (`((i=0;i<5;i++))`) bo'yicha takrorlaydi.
- `while` shart rost ekan davomida, `until` shart rost bo'lmaguncha (yolg'on ekan davomida) takrorlaydi.
- `while true; do ...; done` cheksiz sikl, `Ctrl+C` bilan to'xtatiladi.
- `break` siklni to'xtatadi, `continue` aylanishni o'tkazib yuboradi.
- `while read -r QATOR; do ...; done < fayl` faylni qatorma-qator o'qiydi.
- Quvur (`|`) bilan `sort`, `uniq`, `wc`, `grep`, `cut`, `head` ni zanjirlab, matnni qayta ishlaymiz.

---

</div>

<div class="blk">

## <Icon name="book-open" /> Qo'shimcha ma'lumot

### 1. Sikl = takrorlash mashinasi
Tasavvur qiling, 30 ta o'quvchiga bir xil xat yozish kerak. Qo'lda 30 marta yozasiz, sikl esa bitta shablonni 30 marta o'zi to'ldiradi. O'quv qo'llanmada ham shunday misol bor: `for pkg in docker.io docker-doc ...; do sudo apt-get remove $pkg; done`: ro'yxatdagi har bir paket uchun bir xil amal.

### 2. while va until: ko'zgu juftlik
```bash
n=3
while [ $n -gt 0 ]; do echo $n; n=$((n-1)); done   # 3 2 1
k=0
until [ $k -ge 3 ]; do echo $k; k=$((k+1)); done   # 0 1 2
```
`while` «shart rost ekan, davom et», `until` «shart rost bo'lmaguncha davom et» deydi. Hujjatdagi `while true; do wget ...; done` serverga yuklama berish uchun ishlatilgan, to'xtatish `Ctrl+C`.

### 3. Matn oqimlari
Qo'llanmaga ko'ra, jarayon stdin dan o'qiydi va stdout ga yozadi; quvur bir buyruq chiqishini keyingisiga kirishga ulaydi. `uniq` faqat ketma-ket takrorlarni olib tashlaydi, shuning uchun avval `sort`:
```bash
sort royxat.txt | uniq -c      # har qator necha marta
ls ~ | wc -l                   # uy papkadagi elementlar soni
ps aux | grep ssh              # ssh jarayonlari
```

### 4. Odatiy xatolar
- Siklda hisoblagichni o'zgartirishni unutish: cheksiz sikl.
- `for F in $(ls)` fayl nomida bo'sh joy bo'lsa buziladi; `for F in *` xavfsizroq.
- `done < fayl` ni unutish: `read` klaviaturadan kutadi.
- `sort` siz `uniq` ishlatish.

---

</div>

<div class="blk">

## <Icon name="languages" /> Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Loop (sikl)** | Buyruqlar blokini takror bajarish. |
| **for** | Ro'yxat yoki diapazon bo'yicha sikl. |
| **while** | Shart rost bo'lguncha ishlaydigan sikl. |
| **until** | Shart rost bo'lmaguncha (yolg'on ekan) ishlaydigan sikl. |
| **break / continue** | Siklni to'xtatish / aylanishni o'tkazish. |
| **Pipe (quvur)** | Bir buyruq chiqishini keyingisiga kirish qilib ulaydi. |
| **stdin / stdout / stderr** | Kirish, chiqish va xato oqimlari. |
| **wc -l** | Qatorlar sonini hisoblaydi. |
| **uniq** | Ketma-ket takrorlanuvchi qatorlarni birlashtiradi. |

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- `while true` shaklidagi cheksiz sikllar serverlarda monitoring skriptlarining asosi: ular har soniyada holatni tekshirib turadi.
- Unix falsafasi: har dastur bitta ishni yaxshi qilsin, murakkab ishni esa quvur bilan yig'ing.
- `seq 1 5` ham `{1..5}` kabi sonlarni chiqaradi.
- `RANDOM % 20 + 1` 1 dan 20 gacha tasodifiy son berish uchun mashhur formula.

---

</div>

<div class="blk">

## <Icon name="clipboard-list" /> Topshiriqlar

### 1. Birdan o'ngacha <Badge type="tip" text="oson" />
`for` bilan 1 dan 10 gacha sonlarni chiqaring.

**Kutiladigan natija:** 10 qator.

### 2. Ro'yxat bo'yicha salom <Badge type="tip" text="oson" />
`for` bilan 3 ta do'stingiz ismiga salom yozing.

**Kutiladigan natija:** 3 ta salom.

### 3. Bashorat qiling <Badge type="tip" text="oson" />
Bu kod nima chiqaradi?
```bash
for i in 1 2 3 4 5; do
  [ $i -eq 2 ] && continue
  [ $i -eq 4 ] && break
  echo $i
done
```
**Kutiladigan natija:** oldindan javob yozing, so'ng tekshiring.

### 4. Xatoni toping <Badge type="tip" text="oson" />
`n=3; while [ $n -gt 0 ]; do echo $n; done` nega to'xtamaydi? Tuzating.

**Kutiladigan natija:** `n=$((n-1))` kerakligi tushuntirilgan.

### 5. Teskari sanoq <Badge type="warning" text="o'rta" />
`while` bilan 10 dan 1 gacha sanang va oxirida «Start!» deb yozing.

**Kutiladigan natija:** 10, 9, ... 1, Start!

### 6. Fayllar ro'yxati <Badge type="warning" text="o'rta" />
`for F in *` bilan joriy papkadagi har bir element fayl yoki papkaligini aytib bering.

**Kutiladigan natija:** har element yonida `fayl` yoki `papka`.

### 7. Qatorlarni sanash <Badge type="warning" text="o'rta" />
`while read` yordamida o'zingiz yaratgan `royxat.txt` ni raqamlab chiqaring.

**Kutiladigan natija:** `1. ...`, `2. ...` ko'rinishida.

### 8. Takrorlarni sanash <Badge type="warning" text="o'rta" />
Quvur bilan `royxat.txt` da har qator necha marta uchrashini ko'rsating (`sort | uniq -c`).

**Kutiladigan natija:** sanoq va qator ro'yxati.

### 9. Ko'paytirish jadvali <Badge type="danger" text="qiyin" />
Argument sifatida son oling va uning 1-10 ko'paytirish jadvalini `printf` bilan tekis chiqaring.

**Kutiladigan natija:** `7 x 3 = 21` kabi 10 qator.

### 10. Mini-loyiha: taxmin o'yini <Badge type="danger" text="qiyin" />
1..20 orasida son o'ylansin (`RANDOM`), siz topguncha `until` bilan so'rasin va «katta/kichik» desin; urinishlarni sanang.

**Kutiladigan natija:** topilganda «urinishlar soni» chiqadi.

### 11. Tizim hisoboti <Badge type="danger" text="qiyin" />
`/etc/passwd` dan `cut -d: -f1` bilan foydalanuvchi nomlarini oling va nechtaligini `wc -l` bilan ko'rsating; ro'yxatni alifbo tartibida (`sort`) chiqaring.

**Kutiladigan natija:** tartiblangan ro'yxat va umumiy son.

### 12. Bonus: ping monitori <Badge type="info" text="bonus" />
`for` bilan 3 ta manzilni (masalan, `8.8.8.8`, `1.1.1.1`, `127.0.0.1`) `ping -c 1` bilan tekshirib, har biri uchun «ishlayapti/ishlamayapti» deb yozing (chiqish kodi + `if`).

**Kutiladigan natija:** har manzil uchun holat xabari.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. `for i in {1..5}` nechta aylanish beradi?
2. `while` bilan `until` ning farqi nima?
3. `break` va `continue` farqi nima?
4. `read` ni fayl bilan qanday bog'laymiz?
5. `uniq` dan oldin nega `sort` kerak?
6. Cheksiz siklni qanday to'xtatamiz?
7. `ls ~ | wc -l` nimani hisoblaydi?

---

</div>

<div class="blk">

## <Icon name="house" /> Uyga vazifa

`hisobot.sh` yozing: berilgan matn fayldagi qatorlarni raqamlab chiqarsin, so'ng noyob qatorlar sonini (`sort | uniq | wc -l`) ko'rsatsin. Kutiladigan vaqt: 25 daqiqa.

</div>

