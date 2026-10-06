# 12-dars. Personaj va obyektlar uchun spraytlar chizish

> Mario ham bir paytlar bir necha o'nlab pikseldan iborat edi! Bugun 32×32 piksel ichida o'z qahramoningizni yaratasiz, unga tanga va zelye chizasiz va uni «nafas oldirasiz».

## Dars xulosasi

- **Sprayt yaratishning 6 bosqichi:** uslub va o'lcham → siluyet → asosiy ranglar → soya va yorug'lik → kontur → eksport va test.
- **O'lcham:** retro qahramon — **32×32 px**, mayda obyektlar — **16×16 px**.
- **Siluyet** — avval bitta to'q rangda; qora shaklda ham tanilsa, dizayn yaxshi.
- **Rang:** 10-dars palitrasidan, qahramon uchun **4–6 rang**.
- **Yorug'lik manbai** — doim **yuqori chapda**, soyalar pastki o'ngda (hue shifting bilan).
- **Kontur** — 1 px, qora o'rniga eng to'q rang.
- **Photoshop sozlamalari:** Transparent hujjat, 1 px grid, **Pencil Tool** 1 px, Paint Bucket Anti-alias o'chiq, **Nearest Neighbor** interpolyatsiya.
- **Piksel-art xatolari:** orphan piksellar, doubles (qalin kontur), tartibsiz zinapoyalar (jaggies).
- **Idle animatsiya:** 2 kadr, tana 1 px pastga, har kadr 0.5 s, Timeline orqali.

## Qo'shimcha ma'lumot

### 1. Qatlamlar tartibi

```
05_kontur
04_yoruglik  (Clipping Mask)
03_soya      (Clipping Mask)
02_flat      - asosiy ranglar
01_siluyet   - oxirida yashiriladi
```

### 2. Qahramon nisbatlari (retro uslub, 32×32)

Bosh ~12 px, tana ~10 px, oyoqlar ~8 px, tepada va pastda 1 px bo'sh joy. Ko'zlar — 1×2 px. Katta bosh — qahramon «yoqimli» va tanilishi oson.

### 3. Obyektlar: tez retseptlar

- **Tanga 16×16:** oltin doira, 1 px to'q-jigarrang kontur, yuqori chapda 2–3 px oq yaltiroq.
- **Zelye 16×16:** shisha siluyet, ichida qizil (jon) yoki moviy (mana) suyuqlik, oq aks.
- **Sandiq 32×32:** jigarrang yog'och, oltin qoplamalar va qulf.

### 4. Pencil va Brush

**Brush** chetlarni yumshatadi — piksel-artda xira «loy» piksellar paydo bo'ladi. **Pencil** esa har bir pikselni aniq, qattiq qo'yadi. Shuning uchun piksel-art — faqat Pencil bilan.

### 5. Kattalashtirish sirri

Image Size → Resample: **Nearest Neighbor**. Bicubic tanlansa, sprayt loyqa bo'ladi. 32 px → 256 px (800%) — prezentatsiya uchun ideal.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Piksel-art** | Har bir piksel ataylab qo'yiladigan raqamli rasm uslubi |
| **Siluyet** | Obyektning bitta rangdagi tashqi shakli |
| **Flat rang** | Soyasiz, bir tekis asosiy rang |
| **Kontur (outline)** | Spraytni fondan ajratuvchi chegara chizig'i |
| **Orphan piksel** | Hech narsaga ulanmagan yolg'iz piksel |
| **Doubles** | Kontur 2 px ga qalinlashib qolgan joy |
| **Jaggies** | Tartibsiz, notekis piksel zinapoyalari |
| **Pencil Tool** | Qattiq chetli piksel chizish asbobi |
| **Nearest Neighbor** | Piksellarni keskin saqlaydigan kattalashtirish usuli |
| **Kadr (frame)** | Animatsiyaning bitta rasmi |
| **Idle animatsiya** | Qahramon tik turganda «nafas olish» harakati |
| **Timeline** | Photoshop'da kadrli animatsiya paneli |

## Bilasizmi?

- Asl Super Mario Bros (1985) dagi kichik Mario sprayti atigi 12×16 pikseldan iborat va 3 ta rangda chizilgan.
- Mario ning mo'ylovi va kepkasi bejiz emas: kam pikselda og'iz va sochni chizish qiyin bo'lgani uchun rassomlar shunday yo'l topgan.
- Ko'p zamonaviy piksel o'yinlar qahramonni atigi 2–4 kadr bilan «jonlantiradi» — o'yinchi miyasi qolganini o'zi to'ldiradi.
- Piksel-art rassomlari ko'pincha «1 px siljish ham katta o'zgarish» deyishadi: 32 px qahramonda 1 px — butun tananing 3 foizi.

## Topshiriqlar

### 1. Uchta siluyet · oson
32×32 px da faqat bitta to'q rang bilan 3 ta qahramon siluyetini chizing: ritsar, sehrgar, robot.

**Kutiladigan natija:** 3 ta siluyet; sinfdoshingiz har birini taniydi.

### 2. Piksel-art hujjati · oson
Photoshop'da 32×32 px shaffof hujjat tayyorlang: 1 px grid, Pencil 1 px, Nearest Neighbor.

**Kutiladigan natija:** sozlangan hujjat skrinshoti.

### 3. Yorug'lik yo'nalishi · oson
Oddiy 16×16 px kubikni chizing: yuqori chap yuzasi och, pastki o'ng yuzasi to'q.

**Kutiladigan natija:** 3 rangli kubik PNG.

### 4. Xatolarni toping · oson
Mentor bergan spraytda orphan piksellar, doubles va jaggies joylarini belgilang.

**Kutiladigan natija:** belgilangan skrinshot.

### 5. Qahramon: flat ranglar · o'rta
Siluyetlardan birini tanlab, palitrangizdan 4–6 rang bilan flat ranglarni qo'ying.

**Kutiladigan natija:** `02_flat` qatlami tayyor sprayt.

### 6. Soya va yorug'lik · o'rta
Qahramonga soya va yorug'lik qatlamlarini Clipping Mask bilan qo'shing (hue shifting).

**Kutiladigan natija:** hajmli ko'rinadigan sprayt.

### 7. Kontur va tozalash · o'rta
1 px kontur qo'shing va barcha orphan piksellar hamda doubles ni tozalang.

**Kutiladigan natija:** `sprayt_qahramon_idle_32.png`.

### 8. Tanga va zelye · o'rta
16×16 px da tanga va jon zelyesini qahramon bilan bir uslubda chizing.

**Kutiladigan natija:** 2 ta PNG.

### 9. Kulrang va fon testi · qiyin
Qahramon va obyektlarni 10-dars lokatsiya foniga qo'ying va kulrang testdan o'tkazing. Kerak bo'lsa, ranglarni tuzating.

**Kutiladigan natija:** «oldin/keyin» skrinshotlari va izoh.

### 10. Idle animatsiya · qiyin
Timeline'da 2 kadrli idle animatsiya yarating (tana 1 px pastga, 0.5 s, Forever) va GIF ga eksport qiling.

**Kutiladigan natija:** `qahramon_idle.gif`.

### 11. Dushman spraytini chizing · qiyin
Qahramoningizga qarshi bitta dushman (slime, ko'rshapalak yoki robot) chizing: qahramondan rang va siluyet bilan aniq farq qilsin.

**Kutiladigan natija:** dushman PNG va 2 jumla dizayn asoslash.

### 12. Sandiq ochilishi · bonus
32×32 px sandiqni ikki holatda chizing: yopiq va ochiq (ichida oltin yaltirash).

**Kutiladigan natija:** 2 kadr PNG yoki GIF.

## O'zingizni tekshiring

1. Sprayt yaratishning 6 bosqichini ayting.
2. Nega avval siluyet chiziladi?
3. Piksel-artda nega Pencil Tool ishlatiladi?
4. Nearest Neighbor nima uchun kerak?
5. Yorug'lik manbai qayerda bo'lishi va nega bir xil bo'lishi kerak?
6. Orphan piksel va doubles nima?
7. Idle animatsiya qanday yaratiladi?

## Uyga vazifa

O'z qahramoningizning to'liq 32×32 px spraytini (flat, soya, yorug'lik, kontur), 2 ta 16×16 obyektni va 2 kadrli idle animatsiyani tayyorlang; PNG va GIF ko'rinishida saqlang. Batafsil: `uyga-vazifa.md`.
