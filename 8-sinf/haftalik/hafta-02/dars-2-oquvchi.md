# 5-dars. Jadval teglari: `<table>`, `<tr>`, `<td>`, `<th>`, `colspan` va `rowspan`

> Dars jadvali, futbol chempionati turnir jadvali, internet-do'kondagi narxlar va xarid cheki — bularning barchasi jadvallardir. Ushbu darsda HTML yordamida qator va ustunlardan iborat chiroyli jadvallar yaratishni, katakchalarni birlashtirishni o'rganamiz.

## Dars xulosasi

- `<table>` — HTMLda jadval yaratish uchun asosiy ota konteyner tegi.
- HTMLda jadval **qatorlar bo'yicha** yoziladi: har bir yangi qator `<tr>` (table row) orqali ochiladi.
- Oddiy katakchalar `<td>` (table data), sarlavha katakchalari esa `<th>` (table header) orqali yoziladi.
- `<th>` ichidagi matn odatda qalin (bold) bo'ladi va katakchaning markazida joylashadi.
- `<caption>` tegi jadvalga rasmiy sarlavha/nom berish uchun xizmat qiladi.
- Katta jadvallar semantik jihatdan 3 qismga ajratiladi: `<thead>` (boshi), `<tbody>` (asosiy tanasi) va `<tfoot>` (yakuniy jami qismi).
- Katakchalarni gorizontaliga bir nechta ustunga cho'zish uchun `colspan="N"` ishlatiladi.
- Katakchalarni vertikaliga bir nechta qatorga cho'zish uchun `rowspan="N"` ishlatiladi.

## Qo'shimcha ma'lumot

### Nega HTMLda ustunlar bo'yicha emas, qatorlar bo'yicha yoziladi?
Boshlovchilar ko'pincha "Jadvalni ustunma-ustun yozib bo'lmaydimi?" deb so'rashadi. HTML tili yuqoridan pastga qarab o'qilganligi sababli, har bir qator alohida gorizontal chiziq sifatida hosil qilinadi (`<tr>`), so'ng uning ichiga katakchalar (`<td>`) chapdan o'ngga ketma-ket joylashtiriladi. Shuning uchun barcha qatorlardagi katakchalar soni bir xil bo'lishi shart!

### Katakchalarni birlashtirish siri: Matematik muvozanat
Katakchalarni birlashtirganda jadval buzilib ketmasligi uchun bitta oddiy qoidaga amal qiling:
- Agar jadvalingiz 3 ta ustundan iborat bo'lsa, har bir qatorda jami `<td>` lar qiymati 3 ga teng bo'lishi kerak.
- Agar birinchi katakchaga `colspan="2"` bersangiz, u 2 ta katakcha o'rnini egallaydi. Demak, shu qatorda yana faqat bitta oddiy `<td>` yozilishi kerak (2 + 1 = 3).
- Agar `rowspan="2"` bersangiz, u pastki qatorning ham bitta katakchasini "yeb qo'yadi". Shuning uchun pastki qatorda bitta `<td>` kam yoziladi!

### `border="1"` nima uchun kerak?
Odatiy holatda brauzer jadval chizig'ini (ramkasini) ko'rsatmaydi. Katakchalarni ko'z bilan ko'rib, tekshirib olish uchun `table` tegiga vaqtincha `border="1"` atributi beriladi. Keyinchalik CSS o'rgangach, ramkalarni juda chiroyli va nafis qilib bezatamiz.

### `thead`, `tbody`, `tfoot` ning amaliy foydasi
Agar saytingizdagi katta jadval (masalan, 100 qatordan iborat ro'yxat) printerdan chiqarilayotgan bo'lsa, brauzer avtomatik ravishda har bir qog'oz varag'ining yuqori qismida `<thead>` ni takrorlaydi, pastida esa `<tfoot>` ni qo'yadi. Bu juda qulay va professional yondashuvdir.

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| `<table>` (Table) | Jadval yaratuvchi asosiy konteyner tegi |
| `<tr>` (Table Row) | Jadvalning bitta gorizontal satri/qatori |
| `<td>` (Table Data) | Jadvaldagi oddiy ma'lumot katakchasi |
| `<th>` (Table Header) | Jadval sarlavhasi katakchasi (qalin va o'rtada) |
| `<caption>` | Jadvalning ustki sarlavhasi yoki nomi |
| `<thead>` (Table Head) | Jadvalning bosh qismi bo'limi |
| `<tbody>` (Table Body) | Jadvalning asosiy ma'lumotlar qismi bo'limi |
| `<tfoot>` (Table Foot) | Jadvalning yakuniy xulosa yoki jami bo'limi |
| `colspan` (Column Span) | Bir nechta ustunni bitta katakchaga birlashtirish |
| `rowspan` (Row Span) | Bir nechta qatorni bitta katakchaga birlashtirish |

## Bilasizmi?

- 1990-yillarda (CSS hali rivojlanmagan davrda) butun saytlarning dizayni va maketi `<table>` teglari yordamida tuzilgan! Saytning menyusi, logotipi va yangiliklari bitta ulkan jadval ichiga joylashtirilgan.
- Bugungi kunda jadvallar faqat o'zining asl maqsadi — ma'lumotlarni tartibli jadval shaklida taqdim etish uchun ishlatiladi. Sayt dizaynini jadval bilan qilish hozir qattiq xato hisoblanadi!
- Excel yoki Google Sheets dasturidagi istalgan jadvalni bir necha tugma orqali to'g'ridan-to'g'ri HTML jadvalga o'girish mumkin.
- `cellpadding` va `cellspacing` kabi eski HTML atributlari mavjud bo'lgan, ammo hozirda ularning o'rniga faqat zamonaviy CSS ishlatiladi.

## Topshiriqlar

### 1. Haftalik ob-havo jadvali · oson
Haftaning 3 kuni (Dushanba, Seshanba, Chorshanba) uchun kun nomi va kutilayotgan haroratdan iborat oddiy jadval tuzing.

**Kutiladigan natija:** 2 ta ustun va 4 ta qatordan iborat ob-havo ma'lumoti.

### 2. Baholar daftarcham · oson
3 ta fan (Matematika, Ona tili, Informatika) va ulardan olgan baholaringizdan iborat jadval tuzing. Birinchi qatorda `<th>` ishlatilsin.

**Kutiladigan natija:** `<th>` sarlavhalari bilan ajratilgan chiroyli baholar jadvali.

### 3. Do'stlar telefon kitobchasi · oson
Ism, Familiya va Telefon raqami ustunlaridan iborat 3 nafar do'stingizning ma'lumotlari yozilgan jadval yarating.

**Kutiladigan natija:** 3 ta ustunli tartibli telefon ma'lumotnomasi.

### 4. Jadval sarlavhasi (`<caption>`) · oson
Oldingi topshiriqlardan biriga `<caption>` tegi yordamida rasmiy nom bering (masalan: "8-sinf o'quvchilari ro'yxati").

**Kutiladigan natija:** jadval ustida markazlashgan holda chiquvchi sarlavha.

### 5. Xarid cheki va jami hisob (`colspan`) · o'rta
Do'kondan olingan 3 ta tovar (nomi, soni, narxi) va eng pastki qatorda 2 ta ustunni birlashtiruvchi `colspan="2"` bilan "Jami:" so'zi yozilgan chek jadvalini tuzing.

**Kutiladigan natija:** oxirgi qatorda ustunlari birlashgan to'lov cheki.

### 6. Xatoni toping · o'rta
Quyidagi kodda jadval strukturasiga oid qanday xato bor? Uni toping va to'g'rilang:
```html
<table border="1">
  <tr>
    <td>Dushanba</td>
    <td>Matematika</td>
    <td>Fizika</td>
  </tr>
  <tr>
    <td>Seshanba</td>
    <td>Ingliz tili</td>
  </tr>
</table>
```

**Kutiladigan natija:** xatoning sababi tushuntirilgan va katakchalar soni tenglashtirilgan kod.

### 7. Semantik tuzilma (`thead`, `tbody`, `tfoot`) · o'rta
Futbol bo'yicha musobaqa jadvalini `<thead>`, `<tbody>` va `<tfoot>` ga ajratgan holda yozing. Jamoalar soni kamida 3 ta bo'lsin.

**Kutiladigan natija:** barcha semantik bloklar to'g'ri joylashtirilgan turnir jadvali.

### 8. Umumiy dars soati (`rowspan`) · o'rta
Dushanba va Seshanba kunlari soat 09:00 da bir xil dars — "Dasturlash asoslari" bo'ladi. `rowspan="2"` yordamida ikkala kunning 09:00 katakchasini bitta qilib birlashtiring.

**Kutiladigan natija:** vertikal 2 qatorni egallagan birlashgan katakcha.

### 9. To'liq maktab dars jadvali · qiyin
Dushanbadan jumagacha bo'lgan 5 kunlik, kuniga 4 tadan dars va 2-darsdan keyin butun jadval bo'ylab o'tuvchi "Katta tanaffus" (`colspan`) katakchasi mavjud bo'lgan professional dars jadvalini tayyorlang.

**Kutiladigan natija:** to'liq va mukammal formatlangan haftalik maktab dars jadvali.

### 10. Murakkab tariflar jadvali · qiyin
Mobil operatorning 3 xil tarifi (Oddiy, Standart, VIP) uchun taqqoslash jadvalini tuzing. Jadvalda narxi, daqiqalar, internet megabaytlari bo'lsin. Ba'zi qatorlarda `colspan` va `rowspan` qo'llanilsin (masalan, barcha tariflar uchun bepul Telegram).

**Kutiladigan natija:** katakchalari chiroyli birlashtirilgan zamonaviy xizmatlar taqqoslashi.

### 11. Shaxmat doskasi simulyatsiyasi · bonus
HTML jadvali yordamida 8x8 o'lchamdagi shaxmat doskasini yarating. Har bir katakchaga oq yoki qora kvadrat ramzi yoki shaxmat donalarining nomini yozing.

**Kutiladigan natija:** teng 8 qator va 8 ustundan iborat simmetrik doska.

## O'zingizni tekshiring

1. `<th>` va `<td>` katakchalari tashqi ko'rinish va ma'no jihatidan qanday farqlanadi?
2. `colspan` nima qiladi va u qaysi yo'nalish bo'yicha ishlaydi?
3. `rowspan` ishlatilganda keyingi qatorlardagi katakchalar soni nima uchun kamayishi kerak?
4. Jadval nomi qaysi teg orqali beriladi va u qayerda joylashishi shart?
5. `<thead>`, `<tbody>` va `<tfoot>` teglarining dasturlashdagi asosiy afzalligi nima?

## Uyga vazifa

O'zingiz yoki oila a'zolaringiz uchun oylik xarajatlar rejasini HTML jadvali ko'rinishida tuzing. Unda kamida 5 ta xarajat moddasi (Kommunal, Oziq-ovqat, Internet, Transport va boshqalar), `<thead>`, `<tbody>`, `<tfoot>` hamda `colspan` orqali hisoblangan "Jami oylik xarajat" bo'lsin.
