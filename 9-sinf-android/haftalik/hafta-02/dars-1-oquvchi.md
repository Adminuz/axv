# 4-dars. Android ekotizimi va Google xizmatlari (1-qism)

Bugungi darsda biz Android tizimining ochiq manba kodi (AOSP) va Google Mobile Services (GMS) o'rtasidagi farqni o'rganamiz. Qanday qilib Google Play Services orqa fonda ishlab, telefoningiz batareyasini tejashi va xaritalar, bildirishnomalarni boshqarishini tahlil qilamiz.

---

## Asosiy tushunchalar

- **AOSP (Android Open Source Project)** — Androidning hamma uchun bepul va ochiq bo'lgan bazaviy operatsion tizim kodi.
- **GMS (Google Mobile Services)** — Google tomonidan yaratilgan rasmiy dasturlar (Play Store, Maps, YouTube) va maxsus API xizmatlari to'plami.
- **Google Play Services** — ilovalar bilan Google serverlari o'rtasida ko'prik bo'lib xizmat qiluvchi fondagi tizim xizmati.
- **FCM (Firebase Cloud Messaging)** — barcha mobil ilovalarga push-bildirishnomalarni bitta umumiy xavfsiz kanal orqali yetkazuvchi xizmat.
- **Fused Location Provider** — GPS, Wi-Fi va uyali aloqa signallarini birlashtirib, kam quvvat bilan aniq joylashuvni aniqlovchi aqlli texnologiya.
- **HMS (Huawei Mobile Services)** — Google xizmatlari bo'lmagan qurilmalardagi muqobil ekotizim.

---

## 1. AOSP va GMS: Ekotizimning ikki qanoti

Android tizimiga ega smartfon sotib olganingizda, unda ikki xil qism birlashgan bo'ladi:

```
+-----------------------------------------------------------+
|          GMS (Google Mobile Services)                     |
|  Play Store, Google Maps, YouTube, Google Play Services   |
+-----------------------------------------------------------+
|          AOSP (Android Open Source Project)               |
|  Linux Kernel, ART, Tizim kutubxonalari, Baza tizimi       |
+-----------------------------------------------------------+
```

### AOSP — Ochiq manba dvigateli
AOSP — bu avtomobilning dvigateli, g'ildiraklari va kuzoviga o'xshaydi. Google ushbu kodni butun dunyoga bepul beradi. Har qanday texnologik kompaniya AOSP kodini olib, o'zining smartfoni, televizori yoki soatiga o'rnatishi mumkin.

### GMS — Google qulayliklari
GMS — bu avtomobildagi qulay charm o'rindiqlar, zamonaviy multimedia ekrani va aqlli avtopilotdir. Unga Google Play Store do'koni, Google Maps, Gmail, YouTube va eng muhimi — **Google Play Services** kiradi. GMS faqat Google bilan rasmiy shartnoma imzolagan brendlarga beriladi.

---

## 2. Google Play Services nima va u nega muhim?

Google Play Services — bu menyuda ikonka bo'lib ko'rinmaydigan, lekin telefoningizning eng faol xizmatidir:
1. **Batareyani tejovchi xaritalar va GPS:** Agar 10 ta turli ilova (Yandex Go, Telegram, Instagram) to'g'ridan-to'g'ri telefon GPS moduliga murojaat qilsa, telefon batareyasi 2 soatda tugaydi. Google Play Services barcha ilovalar nomidan bitta markaziy Fused Location orqali koordinatani oladi va batareyani tejaydi.
2. **Yagona bildirishnomalar kanali (FCM):** Barcha ilovalarning xabarlari bitta umumiy aloqa kanali orqali keladi.
3. **Eski telefonlarni yangilash:** Operatsion tizim yangilanmasa ham, Google Play Services Play Market orqali avtomatik yangilanib, eng so'nggi xavfsizlik va API imkoniyatlarini taqdim etadi.

---

## 3. GMS bo'lmagan qurilmalarda nima bo'ladi?

Yangi Huawei smartfonlarida xalqaro cheklovlar sababli GMS yo'q. Ular o'zlarining **HMS (Huawei Mobile Services)** tizimidan foydalanadi. 
Professional Android dasturchisi o'z ilovasida quyidagi tekshiruvni amalga oshirishi shart:

```kotlin
val isAvailable = GoogleApiAvailability.getInstance()
    .isGooglePlayServicesAvailable(context)

if (isAvailable == ConnectionResult.SUCCESS) {
    // Google Maps xaritasini xavfsiz ochish
} else {
    // Muqobil ochiq xaritani (OpenStreetMap) ochish
}
```

---

## Amaliy topshiriqlar

1. **Smartfoningizda Google Play Services'ni toping** `· oson`  
   Telefoningizning «Sozlamalar» -> «Ilovalar» (Apps) bo'limiga kiring. Ro'yxatdan «Google Play xizmatlari» (Google Play Services) ilovasini toping. Uning xotirada egallagan hajmini va oxirgi versiyasini yozib oling.

2. **AOSP nima degani?** `· oson`  
   AOSP qisqartmasining to'liq inglizcha va o'zbekcha ma'nosini yozing.

3. **GMS tarkibidagi 5 ta ilovani sanang** `· oson`  
   Google Mobile Services paketiga kiruvchi 5 ta mashhur Google ilovasini ayting.

4. **Nima uchun GPS batareyani ko'p yeydi?** `· o'rta`  
   Smartfondagi jismoniy GPS moduli nima sababdan ko'p energiya sarflashini va Fused Location qanday qilib bu muammoni hal qilishini tushuntiring.

5. **AOSP va GMS taqqoslash jadvali** `· o'rta`  
   AOSP va GMS'ni litsenziya, narx va imkoniyatlar bo'yicha taqqoslovchi jadval tuzing.

6. **FCM (Firebase Cloud Messaging) vazifasi** `· o'rta`  
   Agar FCM xizmati bo'lmaganida, har bir ilova (Telegram, WhatsApp) yangi xabarlarni tekshirish uchun nima qilishiga to'g'ri kelardi? Bu telefon unumdorligiga qanday ta'sir qilgan bo'lardi?

7. **Huawei muammosi tahlili** `· o'rta`  
   Nima uchun Huawei kompaniyasi yangi telefonlariga Google Play Store o'rnatolmaydi va ular qanday muqobil tizim yaratishdi?

8. **GoogleApiAvailability tekshiruvi** `· qiyin`  
   Dasturchi nima sababdan ilova ichida Google xizmatlarining mavjudligini kod orqali tekshirishi kerak? Agar bu tekshiruv bajarilmasa, GMS bo'lmagan telefonda nima sodir bo'ladi?

9. **Bino ichidagi navigatsiya ssenariysi** `· qiyin`  
   Yer osti savdo markazida yoki metroda turganingizda, GPS sun'iy yo'ldoshlari ko'rinmaydi. Google Play Services sizning taxminiy joylashuvingizni qaysi signallar orqali aniqlay oladi?

10. **Tadqiqotchi dasturchi** `· bonus`  
    Kelajakda bitta ilovani ham Google Play do'koniga, ham Huawei AppGallery do'koniga bir vaqtda moslab chiqarish uchun qanday arxitektura tamoyillariga rioya qilish kerak?

---

## Bilasizmi?

- Google Play Services shunchalik muhimki, u bir kunda dunyo bo'yicha **100 milliarddan ortiq** API so'rovlarini xavfsiz qayta ishlaydi!
- Android operatsion tizimi ochiq kodli bo'lgani sababli, Amazon kompaniyasi o'zining "Fire OS" tizimini aynan AOSP asosida yaratgan va undan barcha Google xizmatlarini olib tashlagan.

---

## Dars xulosasi

- AOSP — bu Androidning ochiq va erkin yadrosi, GMS esa Google xususiy xizmatlari majmuasidir.
- Google Play Services ilovalar va Google serverlari o'rtasida xavfsiz ko'prik vazifasini o'taydi va quvvatni tejaydi.
- Dasturchi o'z ilovalarini turli xil ekotizimlarda (GMS va HMS) barqaror ishlashini ta'minlash uchun xavfsizlik tekshiruvlarini qo'llashi zarur.

---

## O'zingizni tekshiring

1. AOSP va GMS o'rtasidagi asosiy farq nima?
2. Google Play Services foydalanuvchiga nima beradi?
3. Fused Location Provider qaysi manbalardan ma'lumot oladi?
4. Push-bildirishnomalarni tarqatuvchi xizmat qanday ataladi?
5. Huawei smartfonlaridagi muqobil xizmatlar to'plami qanday nomlanadi?
