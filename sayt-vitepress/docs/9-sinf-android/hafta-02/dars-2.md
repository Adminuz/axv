---
title: "5-dars. Android ekotizimi va Google xizmatlari (2-qism)"
layout: "doc"
sidebar: false
aside: false
outline: false
kind: "dars"
dars: {"sinf": {"name": "9-sinf (Android)", "link": "/9-sinf-android/"}, "week": {"n": 2, "link": "/9-sinf-android/hafta-02/"}, "g": 5, "title": "Android ekotizimi va Google xizmatlari (2-qism)", "lead": "Android ekotizimi va Google xizmatlari (2-qism): Google Play Console, SHA-1 barmoq izi, xavfsizlik va AAB formati", "slide": "/slaydlar/9-sinf-android/hafta-02/dars-2.html", "tabs": [{"g": 4, "link": "/9-sinf-android/hafta-02/dars-1", "current": false}, {"g": 5, "link": "/9-sinf-android/hafta-02/dars-2", "current": true}, {"g": 6, "link": "/9-sinf-android/hafta-02/dars-3", "current": false}], "prev": {"g": 4, "title": "Android ekotizimi va Google xizmatlari (1-qism)", "link": "/9-sinf-android/hafta-02/dars-1"}, "next": {"g": 6, "title": "Android Studio va Android SDK bilan tanishuv (1-qism)", "link": "/9-sinf-android/hafta-02/dars-3"}}
---

Bugungi darsda biz mobil ilovamizni Google xizmatlari (Firebase va Google Cloud) bilan rasman bog'lashni o'rganamiz. Ilovaning "raqamli barmoq izi" (SHA-1) nima ekanini, maxfiy kalitlarni qanday himoyalashni hamda Play Market'dagi zamonaviy AAB formatining afzalliklarini tushunib olamiz.

---

<div class="blk">

## <Icon name="file-text" /> Asosiy tushunchalar

- **applicationId (Package Name)** — ilovaning butun dunyoda (Google Play'da) yagona bo'lgan unikal nomi (masalan, `uz.edu.myapp`).
- **SHA-1 barmoq izi** — ilovangiz aynan sizning kompyuteringizda yaratilganini tasdiqlovchi 40 belgili xavfsizlik sertifikati xeshi.
- **google-services.json** — Firebase va Google xizmatlarini loyihaga bog'lovchi maxsus konfiguratsiya fayli.
- **local.properties** — maxfiy API kalitlari saqlanadigan va internetga (GitHub) yuklanmaydigan xavfsiz fayl.
- **APK (Android Package Kit)** — ilovaning barcha resurslarini o'zida jamlagan an'anaviy to'liq o'rnatish paketi.
- **AAB (Android App Bundle)** — Google Play'ga yuklanadigan, faqat foydalanuvchi telefoniga kerakli qismlarni uzatuvchi zamonaviy yengil format.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 1. Ilova nomi: `applicationId`

Har bir mobil ilova dunyo bo'yicha yagona identifikatorga ega bo'lishi kerak. Bu identifikator teskari domen shaklida yoziladi:
- `uz.click.clickuz`
- `com.payme.uz`
- `uz.maktab.kutubxona`

Bu nom orqali operatsion tizim ilovaga alohida shaxsiy papka ajratadi va uning xavfsizligini ta'minlaydi. Ilova bir marta Google Play'da nashr qilinsa, uning `applicationId`sini keyinchalik o'zgartirib bo'lmaydi!

---

</div>

<div class="blk">

## <Icon name="file-text" /> 2. Raqamli barmoq izi: SHA-1 nima va u qanday olinadi?

Ilovangiz Firebase yoki Google Maps xizmatlaridan foydalanishi uchun Google sizning shaxsingizni tasdiqlashi kerak. Buning uchun kompyuterdagi Keystore kalitining **SHA-1** barmoq izi olinadi.

Android Studio ichidagi terminal oynasida quyidagi buyruq kiritiladi:
```bash
./gradlew signingReport
```
Terminalda bir necha soniya ichida quyidagicha natija chiqadi:
```text
Variant: debug
Config: debug
Store: ~/.android/debug.keystore
SHA1: 4B:12:8A:99:32:DE:01:54:...
SHA-256: 7F:89:AB:41:...
```
Ushbu SHA-1 kodini nusxalab, Firebase Console'ga kiritamiz. Shundan so'ng Google xizmatlari sizning ilovangizni rasman tan oladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 3. `google-services.json` fayli bilan ishlash

Firebase Console loyihangizni ro'yxatdan o'tkazgach, sizga **`google-services.json`** nomli faylni yuklab olishni taklif qiladi.

- Bu faylda loyihaning identifikatori, API kalitlari va server manzillari saqlanadi.
- **Qat'iy qoida:** Ushbu fayl loyihaning **`app/`** papkasi ichiga joylashtirilishi shart! (Loyiha ildiz papkasiga emas, balki aynan `app/` papkasiga).

---

</div>

<div class="blk">

## <Icon name="file-text" /> 4. Xavfsizlik: API kalitlarni qayerda saqlaymiz?

Dasturchilar ko'pincha qimmatbaho API kalitlarini (masalan, Google Maps kalitini) to'g'ridan-to'g'ri kod ichida yozib qoldiradilar. Agar ushbu loyiha GitHub'ga yuklansa, avtomatlashtirilgan xaker botlari kalitni o'g'irlab oladi.

### Professional yechim: `local.properties`
Barcha maxfiy kalitlar `local.properties` faylida saqlanadi:
```properties
MAPS_API_KEY=AIzaSyB-namuna-kalit-12345
```
Ushbu fayl `.gitignore` ro'yxatida bo'lgani sababli hech qachon GitHubga chiqmaydi va sizning hisobingiz xavfsiz qoladi.

---

</div>

<div class="blk">

## <Icon name="file-text" /> 5. APK va AAB formatlari

| Xususiyat | APK (Eski format) | AAB (Zamonaviy format) |
|---|---|---|
| Hajmi | Katta (50–80 MB) | 30–50% kichikroq (20–40 MB) |
| Tarkibi | Barcha protsessorlar kodi va barcha rasmlar | Faqat kerakli resurslar |
| Google Play talabi | Yangi ilovalar uchun cheklangan | Barcha yangi ilovalar uchun **majburiy** |
| Ishlash mexanizmi | Telefon keraksiz qismlarni ham yuklaydi | **Dynamic Delivery:** Telefonga moslab beriladi |

---

</div>

<div class="blk">

## <Icon name="file-text" /> Amaliy topshiriqlar

1. **Shaxsiy applicationId yarating** `· oson`  
   O'zingiz orzu qilgan mobil ilova uchun to'g'ri `applicationId` yozing (masalan: `uz.family.photogallery`). Nega unda bo'sh joy bo'lishi mumkin emasligini tushuntiring.

2. **SHA-1 olish buyrug'ini yozing** `· oson`  
   Android Studio terminalida SHA-1 va SHA-256 barmoq izlarini chiqaruvchi Gradle buyrug'ini daftaringizga yozing.

3. **google-services.json qayerda turadi?** `· oson`  
   Ushbu fayl Android Studio loyihasining qaysi papkasi ichiga qo'yilishi shart?

4. **Nega AAB formati APK'dan afzal?** `· o'rta`  
   AAB formatining foydalanuvchilar va mobil internet trafigi uchun 2 ta asosiy afzalligini yozing.

5. **Dynamic Delivery qanday ishlaydi?** `· o'rta`  
   Google Play Store AAB faylidan foydalanib, har bir smartfonga qanday qilib moslashtirilgan yengil paket yuborishini tushuntiring.

6. **API kalit o'g'irlanishi oqibatlari** `· o'rta`  
   Agar dasturchi o'zining pullik Google Maps API kalitini ochiq kodda GitHubga yuklab yuborsa, qanday salbiy oqibatlar kelib chiqishi mumkin?

7. **local.properties faylining afzalligi** `· o'rta`  
   Nima sababdan `local.properties` fayli GitHub kabi versiya nazorati tizimlariga yuklanmaydi? Bu faylni qaysi mexanizm himoyalaydi?

8. **SHA-1 xavfsizlik tahlili** `· qiyin`  
   Nima uchun begona odam sizning `applicationId` nomingizni bilib olgan taqdirda ham, sizning nomingizdan Firebase'ga ulanolmaydi? SHA-1 bu yerda qanday to'siq bo'ladi?

9. **APK hajmini kamaytirish keysi** `· qiyin`  
   Bir dasturchining APK fayli 70 MB chiqdi. U ilovani AAB formatiga o'tkazganda hajmi 32 MB ga tushdi. Qolgan 38 MB qayerga ketdi? Qaysi resurslar tejaldi?

10. **Tadqiqotchi dasturchi** `· bonus`  
    Debug Keystore va Release Keystore o'rtasidagi farqni tadqiq qiling. Nima uchun Play Market'ga ilova yuklashda debug kalitidan foydalanish taqiqlanadi?

---

</div>

<div class="blk">

## <Icon name="sparkles" /> Bilasizmi?

- Google Play Store'da har kuni **100 milliondan ortiq** ilova yuklab olinadi. AAB formatiga o'tilishi natijasida butun dunyo bo'yicha millionlab gigabayt internet trafigi va gigavattlab elektr energiyasi tejalmoqda!
- `google-services.json` fayli ichida maxfiy parollar saqlanmaydi, lekin u ilovangizni aynan sizning Firebase ma'lumotlar bazangizga ulab beruvchi unikal ko'prikdir.

---

</div>

<div class="blk">

## <Icon name="list-checks" /> Dars xulosasi

- Har bir ilova `applicationId` nomli yagona identifikatorga va SHA-1 raqamli barmoq iziga ega.
- `google-services.json` fayli loyihaning `app/` jildida saqlanadi va Google xizmatlarini faollashtiradi.
- Maxfiy API kalitlarni `local.properties`da saqlash — xavfsizlikning oltin qoidasidir.
- AAB formati ilovalarni 30-50% ga ixchamlashtirib, zamonaviy standartga aylangan.

---

</div>

<div class="blk">

## <Icon name="circle-question-mark" /> O'zingizni tekshiring

1. `applicationId` qanday formatda yoziladi?
2. Terminalda SHA-1 olish uchun qanday buyruq kiritiladi?
3. `google-services.json` fayli loyihaning qaysi papkasiga joylashtiriladi?
4. Maxfiy API kalitlarni qayerda saqlash xavfsiz?
5. AAB formati nima sababdan APK'dan yengilroq?

</div>

