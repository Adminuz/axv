# 4-dars. Android ekotizimi va Google xizmatlari (1-qism)

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 2-hafta  
**Dars tartibi:** 4-dars (umumiy 102 darsdan 4-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Nazariy va amaliy tahlil mashg'uloti  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga Android ochiq manba loyihasi (AOSP) va Google Mobile Services (GMS) o'rtasidagi farq, Google Play Services'ning ekotizimdagi roli, fondagi tizim xizmatlari va API integratsiyasi tamoyillarini o'rgatish.
- **Kutiladigan natijalar:**
  - O'quvchi AOSP (Android Open Source Project) va GMS (Google Mobile Services) o'rtasidagi fundamental farqni tushuntira oladi;
  - Google Play Services nima uchun oddiy ilova emas, balki tizimli xizmatlar ko'prigi ekanini biladi;
  - Google Maps, Firebase Cloud Messaging (FCM), Google Location API xizmatlarining ishlash mexanizmini tushunadi;
  - GMS mavjud bo'lmagan qurilmalar (masalan, Huawei HMS) uchun muqobil texnologiyalarni tahlil qila oladi;
  - Google xizmatlarining quvvat tejamkorligi va xavfsizlikka ta'sirini anglaydi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | O'tgan haftani takrorlash va kirish | Android tarixi va arxitektura qatlamlari bo'yicha blits-so'rov. Muammoli savol: "Nima uchun bitta telefonda Google xizmatlari bor, boshqasida yo'q?" |
| **10–35 daq** | Yangi mavzu: AOSP va GMS farqi | AOSP nima, Google litsenziyalari, Google Mobile Services tarkibi, Huawei sanksiyalari va HMS ekotizimi |
| **35–55 daq** | Yangi mavzu: Google Play Services roli | Fondagi ko'prik, Location API (GPS batareyasini tejash), Firebase Cloud Messaging (FCM), xavfsizlik yangilanishlari |
| **55–65 daq** | Amaliy keys va tahlil | Qurilmada Google Play Services xizmatining mavjudligini dasturiy tekshirish kodi (`GoogleApiAvailability`) tahlili |
| **65–75 daq** | Mustahkamlash va test sinovi | Guruhlarda savol-javob, konspekt tekshirish |
| **75–80 daq** | Xulosa va uyga vazifa | Dars yakunlari, o'quvchilarni baholash, uyga vazifa berish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. AOSP va GMS: Ekotizimning ikki qanoti
Ko'pchilik foydalanuvchilar Android va Googleni aynan bir narsa deb o'ylashadi, ammo texnik jihatdan bu ikki xil qatlamdir:
1. **AOSP (Android Open Source Project):**
   - Bu Androidning asosiy dvigatelidir. U to'liq ochiq kodli (Apache 2.0) bo'lib, har qanday shaxs yoki kompaniya uni bepul yuklab olib, o'z qurilmasiga o'rnatishi mumkin.
   - AOSP tarkibiga Linux yadrosi, tizim kutubxonalari, Android Runtime (ART) va asosiy baza ilovalari (oddiy kalkulyator, xabarlar, brauzer) kiradi.
2. **GMS (Google Mobile Services):**
   - Bu Google tomonidan yaratilgan yopiq kodli, xususiy (proprietary) dasturlar va API'lar to'plamidir.
   - GMS'dan foydalanish uchun telefon ishlab chiqaruvchilari (Samsung, Xiaomi) Google bilan maxsus sertifikatsiya shartnomasini (MADA) imzolashi shart.
   - GMS tarkibiga: Google Play Store, Google Maps, Gmail, YouTube, Google Chrome, Google Drive va **Google Play Services** kiradi.

### 3.2. Google Play Services — ekotizimning aqlli markazi
Google Play Services — bu oddiy foydalanuvchi interfeysiga ega bo'lmagan, orqa fonda (background) uzluksiz ishlovchi tizimli platformadir.
Uning 3 ta asosiy vazifasi:
1. **API Ko'prigi (Abstraction Layer):**
   - Agar dasturchi foydalanuvchining GPS manzilini bilmoqchi bo'lsa, to'g'ridan-to'g'ri sun'iy yo'ldoshga murojaat qilmaydi (bu batareyani bir zumda tugatadi). U `FusedLocationProviderClient` orqali Google Play Services'dan so'raydi. Xizmat esa Wi-Fi tarmoqlari, uyali aloqa minoralari va GPS ma'lumotlarini birlashtirib, eng aniq va batareyani tejovchi koordinatani beradi.
2. **Bildirishnomalar (Push Notifications — FCM):**
   - Har bir ilova (Telegram, Click, Instagram) o'z serveri bilan alohida ulanishni ushlab tursa, telefon batareyasi 2 soatda tugaydi. Google Play Services barcha ilovalar uchun bitta umumiy shifrlangan aloqa kanalini (Firebase Cloud Messaging) ushlab turadi va kelgan xabarlarni tegishli ilovalarga tarqatadi.
3. **OS versiyasiga bog'liq bo'lmagan yangilanishlar:**
   - Eski Android 10 yoki 11 o'rnatilgan telefonlar operatsion tizim yangilanishini olmasa ham, Google Play Services Play Market orqali avtomatik yangilanib, eng so'nggi xavfsizlik va API imkoniyatlarini taqdim etaveradi.

### 3.3. GMS va HMS (Huawei) muammosi
2019-yilda AQSH sanksiyalari tufayli Huawei kompaniyasining yangi qurilmalariga GMS o'rnatish taqiqlandi. Natijada Huawei o'zining **HMS (Huawei Mobile Services)** ekotizimini va AppGallery do'konini yaratdi.
Professional Android dasturchisi o'z ilovasini yozishda ilova halokatga (crash) uchramasligi uchun qurilmada Google xizmatlari mavjudligini tekshirishi kerak:

```kotlin
val availability = GoogleApiAvailability.getInstance()
val resultCode = availability.isGooglePlayServicesAvailable(context)

if (resultCode == ConnectionResult.SUCCESS) {
    // Google Maps yoki Google Play xizmatlarini xavfsiz ishga tushirish
} else {
    // Muqobil xarita (OpenStreetMap) yoki xizmatni taklif qilish
}
```

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. AOSP va GMS taqqoslash jadvali (Oson)
**Topshiriq:** AOSP va GMS xususiyatlarini litsenziya turi, tarkibi va boshqaruvi bo'yicha taqqoslang.

**Yechim:**
| Xususiyat | AOSP (Android Open Source) | GMS (Google Mobile Services) |
|---|---|---|
| Litsenziya | Ochiq manba (Apache 2.0) | Yopiq / Xususiy (Google litsenziyasi) |
| Narxi | Bepul | Sertifikatsiya va shartnoma talab etiladi |
| Tarkibi | Linux yadrosi, ART, asosiy AOSP kodlari | Play Store, Maps, YouTube, Play Services |
| Ishlab chiqaruvchilar | Barcha brendlar va mustaqil dasturchilar | Google tomonidan tasdiqlangan qurilmalar |

### 2-topshiriq. Fused Location mexanizmi tahlili (O'rta)
**Topshiriq:** Nima uchun ilovalar to'g'ridan-to'g'ri telefon GPS moduliga emas, balki Google Play Services Fused Location API'siga murojaat qiladi? Buning 2 ta texnik sababini yozing.

**Yechim:**
1. **Batareya tejamkorligi:** GPS moduli juda ko'p elektr quvvatini sarflaydi. Fused Location Provider esa GPS, Wi-Fi burchaklari, uyali aloqa (Cell Tower) va Bluetooth signallarini aqlli tarzda birlashtirib, minimal quvvat bilan aniq joylashuvni beradi.
2. **Bino ichida ishlash:** GPS sun'iy yo'ldoshlari bino ichida, metroda yoki yerto'lada ko'rinmaydi. Google xizmatlari esa bino ichidagi Wi-Fi tarmoqlari orqali xaritada joylashuvni aniqlashda davom etadi.

### 3-topshiriq. Muqobil ekotizimlar arxitekturasi (Qiyin)
**Topshiriq:** Agar ilovangiz faqat Google Maps va Google Sign-In'ga tayansa, u Huawei telefonlarida qanday ishlaydi? Dasturchi bunday vaziyatda qanday arxitektura yechimini qo'llashi kerak?

**Yechim:**
1. **Muammo:** GMS bo'lmagan qurilmada Google Maps xaritasi ochilmaydi, oq ekran chiqadi yoki ilova to'xtab qoladi (`ClassNotFoundException` / `NullPointerException`).
2. **Yechim arxitekturasi:**
   - Dasturchi arxitekturada Abstraksiya qatlamini (Interface) yaratishi lozim (masalan, `MapProviderInterface`);
   - Qurilmada `GoogleApiAvailability` tekshiriladi;
   - Agar GMS bo'lsa -> Google Maps komponenti ulanadi;
   - Agar GMS bo'lmasa -> Huawei Map Kit yoki ochiq manbali MapLibre / OpenStreetMap komponenti ishga tushiriladi.

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **AOSP qisqartmasi nimani anglatadi?**  
   *Javob:* Android Open Source Project.
2. **GMS tarkibidagi eng asosiy tizimli xizmat nima?**  
   *Javob:* Google Play Services.
3. **FCM xizmati nima uchun javobgar?**  
   *Javob:* Firebase Cloud Messaging — barcha ilovalarga push-bildirishnomalarni yagona kanal orqali tezkor yetkazish uchun.
4. **Nima uchun barcha Android telefonlarda ham GMS mavjud emas?**  
   *Javob:* Ishlab chiqaruvchi Google sertifikatidan o'tmagan bo'lsa yoki xalqaro sanksiyalar mavjud bo'lsa (masalan, yangi Huawei modellari).
5. **Google Play Services qayerdan yangilanadi?**  
   *Javob:* Google Play Store orqali, operatsion tizim yangilanishini kutmasdan avtomatik yangilanadi.

---

## 6. Mentor uchun amaliy tavsiyalar

- O'quvchilarga AOSP'ni mashinaning dvigateli va shassisiga, GMS'ni esa uning ichidagi konditsioner, multimedia va navigatsiya tizimiga o'xshatib tushuntiring.
- Keyingi darsda ushbu Google xizmatlarini real loyihaga qanday ulashni (`google-services.json` va SHA-1 kalitlar) amalda ko'rishimizni bildiring.
