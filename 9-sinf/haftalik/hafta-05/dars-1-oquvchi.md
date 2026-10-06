# 13-dars. UI kit va dizayn tizimi tushunchasi

> Bitta ilovaning 10 ta ekranida 10 xil ko'k tugma bo'lsa, foydalanuvchi buni darhol «tartibsizlik» deb sezadi. Katta kompaniyalar bu muammoni UI kit va dizayn tizimlari bilan hal qiladi. Bugun ular nima ekanini bilib olasiz va o'zingizning birinchi mini UI kitingizni yaratasiz.

## Dars xulosasi

- **UI Kit** — dizaynerlar va dasturchilar uchun **tayyor, qayta ishlatiladigan** interfeys komponentlari to'plami: tugmalar, ikonalar, formalar, menyular, modal oynalar.
- UI Kit — dizayner uchun vizual **«konstruktor»**: interfeys noldan emas, tayyor bo'laklardan yig'iladi.
- **4 afzallik:** vaqtni tejash, vizual uyg'unlik, moslashuvchanlik, jamoaviy ishlash.
- **Dizayn tizimi (Design System)** — butun mahsulot uchun yagona konseptual tizim.
- Dizayn tizimining **5 qismi:** komponentlar, vizual uslublar (tokenlar), shablonlar, prinsip va qo'llanmalar, hujjatlashtirish.
- **Token** — nomlangan dizayn qiymati: `color-primary = #2563EB`, `space-m = 16px`.

## Qo'shimcha ma'lumot

### LEGO o'xshatishi
**UI Kit** — LEGO bo'laklari qutisi: g'ishtchalar tayyor, ulardan istalgan narsani yig'asiz. **Dizayn tizimi** — shu quti **va** yig'ish yo'riqnomasi, ranglar qoidasi, «qaysi bo'lak qayerga mos» degan hujjat. Yo'riqnomasiz har kim har xil narsa yig'adi, yo'riqnoma bilan esa butun jamoa bir xil uslubda ishlaydi.

### Kichikdan kattaga
| Daraja | Misol |
|---|---|
| Atom | rang, shrift, ikonka, tugma |
| Molekula | qidiruv maydoni = input + tugma + lupa ikonkasi |
| Organizm | header = logotip + qidiruv + profil + savat |
| Sahifa | header + banner + kitob kartalari + pastki menyu |

### Figma'da stillar
- **Color style:** Fill yonidagi to'rtta nuqtali belgi → **+** → nom (`Primary/500`).
- **Text style:** Text bo'limidagi belgi → **+** → nom (`Heading/H1`).
- Stil o'zgarsa — u ishlatilgan **barcha** elementlar avtomatik yangilanadi.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| UI Kit | Tayyor, qayta ishlatiladigan interfeys komponentlari to'plami |
| Design System | Dizayn tizimi — komponentlar, tokenlar, qoidalar va hujjatlar |
| Component | Komponent — qayta ishlatiladigan interfeys bo'lagi |
| Design Token | Dizayn qarorining nomlangan qiymati |
| Template / Layout | Shablon — tayyor sahifa tuzilmasi |
| Guidelines | Qo'llanma — qachon va qanday ishlatish qoidalari |
| Documentation | Hujjatlashtirish — jamoa uchun yozma tavsif |
| Color / Text style | Figma'da saqlangan rang / matn uslubi |

## Bilasizmi?

- Google'ning Material Design tizimi 2014-yilda e'lon qilingan va bugun milliardlab Android qurilmalarida ishlatiladi.
- Ko'plab kompaniyalarning dizayn tizimiga o'z nomi bor: IBM — **Carbon**, Atlassian — **Atlassian Design System**, Shopify — **Polaris**.
- Dizayn tizimi bor jamoada yangi ekran yaratish bir necha baravar tezlashadi — chunki 80–90% bo'laklar allaqachon tayyor.

## Topshiriqlar

### 1. Ta'rif · oson

UI Kit va dizayn tizimiga o'z so'zingiz bilan bir jumladan ta'rif yozing.

**Kutiladigan natija:** 2 ta aniq ta'rif.

### 2. 4 afzallik · oson

UI Kit'ning 4 afzalligini sanang va har biriga bittadan misol keltiring.

**Kutiladigan natija:** 4 ta afzallik va 4 ta misol.

### 3. 5 qism · oson

Dizayn tizimining 5 qismini yozing.

**Kutiladigan natija:** 5 bandli ro'yxat.

### 4. Atom yoki organizm? · oson

Ikonka, qidiruv maydoni, header, rang — har birini atom, molekula yoki organizmga ajrating.

**Kutiladigan natija:** 4 ta javob.

### 5. UI Kit yoki dizayn tizimi? · o'rta

(a) 20 ta tugma fayli; (b) tugmalar + ranglar + qoidalar + hujjat sayti; (c) Figma'dagi «Mobile UI Kit» — qaysi biri nima?

**Kutiladigan natija:** 3 ta asoslangan javob.

### 6. Token jadvali · o'rta

«E-kutubxona» uchun 5 rang, 3 matn uslubi va 4 bo'shliq tokenidan jadval tuzing.

**Kutiladigan natija:** 12 qatorli jadval.

### 7. Color styles · o'rta

Figma'da 5 ta rangni Color style sifatida saqlang.

**Kutiladigan natija:** «Local styles» da 5 ta rang.

### 8. Text styles · o'rta

H1, H2, Body, Caption matn uslublarini yarating.

**Kutiladigan natija:** 4 ta Text style.

### 9. Tugmalar · qiyin

Faqat stillardan foydalanib Primary, Secondary va Disabled tugmalarini chizing (160 × 48, radius 8).

**Kutiladigan natija:** 3 ta bir xil uslubdagi tugma.

### 10. Avtomatik yangilanish · qiyin

Primary Color style rangini o'zgartiring va nima bo'lganini kuzating.

**Kutiladigan natija:** barcha Primary elementlar o'zgargani skrinshoti.

### 11. Ilova tahlili · qiyin

Telefoningizdagi bitta ilovaning 3 ta ekranini solishtiring: tugmalar, ranglar va shriftlar bir xilmi?

**Kutiladigan natija:** 3 ta kuzatuv va xulosa.

### 12. Mini UI kit sahifasi · bonus

Colors, Typography, Buttons va Inputs bo'limli to'liq UI kit sahifasini yarating.

**Kutiladigan natija:** 4 bo'limli Figma sahifasi.

## O'zingizni tekshiring

1. UI Kit nima va nega uni «konstruktor» deyishadi?
2. UI Kit'ning 4 afzalligini sanang.
3. Dizayn tizimi UI Kit'dan nimasi bilan farq qiladi?
4. Dizayn tizimining 5 qismini ayting.
5. Dizayn tokeni nima? Misol keltiring.
6. Atom, molekula va organizmga bittadan misol keltiring.
7. Figma'da Color style nima uchun kerak?

## Uyga vazifa

«E-kutubxona» UI kit sahifasini Inputs bo'limi bilan to'ldiring va token jadvalini yozing (20–30 daqiqa). To'liq shart: `uyga-vazifa.md`.
