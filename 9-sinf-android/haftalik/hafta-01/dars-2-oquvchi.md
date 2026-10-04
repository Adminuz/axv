# 2-dars. Android tizimi va uning arxitekturasi

Bugungi darsda biz Android operatsion tizimining ichki "anatomiyasi" — ya'ni uning ko'p qatlamli arxitekturasi bilan tanishamiz. Siz yozgan kod qanday qilib telefon kamerasini ishlatishi, ilovalar qanday qilib bir zumda ochilishi va ma'lumotlar qayerda saqlanishini bilib olasiz.

---

## Asosiy tushunchalar

- **Linux Kernel** — Androidning eng quyi poydevori; protsessor, xotira, quvvat va drayverlarni boshqaradi.
- **Hardware Abstraction Layer (HAL)** — apparat ta'minoti (kamera, bluetooth, datchiklar) uchun umumiy standart interfeys.
- **ART (Android Runtime)** — Android ilovalarini ishga tushiruvchi zamonaviy virtual mashina (AOT va JIT kompilyatsiyasi bilan).
- **.dex fayl (Dalvik Executable)** — Java/Kotlin kodi kompilyatsiya qilingandan so'ng hosil bo'ladigan optimallashgan baytkod.
- **Java API Framework** — dasturchilar ilova yozishda foydalanadigan barcha tizim xizmatlari (Activity Manager, View System, Content Providers).
- **Application Sandbox** — har bir ilovani alohida foydalanuvchi va alohida jarayonda izolyatsiyalab himoyalovchi xavfsizlik mexanizmi.

---

## 1. Androidning 5 ta arxitektura qatlami

Android arxitekturasi 5 ta vertikal qatlamdan tashkil topgan ko'p qavatli binoga o'xshaydi:

```
[ 5. Applications (Ilovalar) ]
        ▲
[ 4. Java API Framework (Xizmatlar karkasi) ]
        ▲
[ 3. Android Runtime (ART) + Native C/C++ Kutubxonalari ]
        ▲
[ 2. Hardware Abstraction Layer (HAL) ]
        ▲
[ 1. Linux Kernel (Operatsion tizim yadrosi) ]
```

### 1-qatlam: Linux Kernel (Linux yadrosi)
Android to'liq Linux operatsion tizimi bo'lmasa-da, uning yadrosiga (Kernel) tayanadi. U quyidagilar uchun javobgar:
- **Drayverlar:** Kamera, Wi-Fi, Bluetooth, displey, ovoz chiplarini boshqaradi;
- **Xotira va protsessor:** RAM xotirani ilovalar o'rtasida taqsimlaydi va quvvat sarfini nazorat qiladi;
- **Xavfsizlik:** Linux foydalanuvchilari tizimi orqali ilovalarni bir-biridan ajratadi.

### 2-qatlam: Hardware Abstraction Layer (HAL)
Har bir telefon ishlab chiqaruvchisi har xil kameralar yoki audio chiplardan foydalanadi. HAL apparat qismining farqlarini yashirib, yuqoridagi ilovalarga yagona standart interfeys beradi. Dasturchi har bir telefon modeli uchun alohida kod yozishi shart emas!

### 3-qatlam: Android Runtime (ART) va Native kutubxonalar
- **Native C/C++ kutubxonalari:** Grafika chizuvchi `Surface Manager`, ma'lumotlar bazasi `SQLite`, audio-video kodeklari `Media Framework` va `libc`.
- **ART (Android Runtime):** Biz yozgan kod `.dex` fayliga aylanadi va ART uni qurilma tushunadigan mashina kodiga o'giradi. Android 5.0 dan boshlab ART kiritilgan bo'lib, u dasturlarni oldindan kompilyatsiya qiladi (**AOT — Ahead-of-Time**) va ilovalarning juda tez ochilishini ta'minlaydi.

### 4-qatlam: Java API Framework
Dasturchilar Android Studio'da ilova yozayotganda aynan shu qatlam xizmatlaridan foydalanishadi:
- **Activity Manager:** Ilova ekranlarining ochilishi va hayot siklini boshqaradi;
- **View System:** Tugmalar, matnlar, rasmlar, ro'yxatlar va oynalarni ekranga chizadi;
- **Notification Manager:** Yuqori bildirishnomalar panelida xabar ko'rsatadi;
- **Content Providers:** Ilovalar o'rtasida ma'lumot almashish (masalan, kontaktlar ro'yxatini olish).

### 5-qatlam: Applications (Ilovalar)
Foydalanuvchi ko'radigan barcha dasturlar:
- **Tizimli ilovalar:** Sozlamalar, Telefon, Kamera, Soat;
- **O'rnatilgan ilovalar:** Telegram, Click, YouTube, sevimli o'yinlarimiz va biz yaratadigan dasturlar.

---

## 2. Nima uchun Android xavfsiz? (Application Sandbox)

Har safar telefoningizga yangi ilova o'rnatganingizda, Android unga alohida virtual foydalanuvchi identifikatori (**UID**) beradi (masalan, `app_124`). 

Har bir ilova o'zining shaxsiy "qumqutisi" (Sandbox) ichida ishlaydi. Bir ilova hech qachon boshqa ilovaning fayllarini yoki xotirasini ruxsatsiz o'qiy olmaydi. Agar ilova kamerani yoki kontaktlarni ishlatmoqchi bo'lsa, u foydalanuvchidan rasman ruxsat so'rashi shart!

---

## 3. Ma'lumotlarni saqlash texnologiyalari

Androidda ma'lumotlar 3 xil usulda saqlanadi:
1. **SharedPreferences / DataStore:** Kichik sozlamalar (til, qorong'u rejim, kirish holati) kalit-qiymat (Key-Value) tarzida saqlanadi.
2. **SQLite va Room kutubxonasi:** Ko'p sonli ma'lumotlar va jadvallar (masalan, tovarlar ro'yxati, xabarlar tarixi) telefon xotirasidagi reliesion bazada saqlanadi.
3. **Bulutli bazalar (Firebase):** Internet orqali real vaqtda yangilanadigan bulutli ma'lumotlar bazalari.

---

## Amaliy topshiriqlar

1. **Arxitektura qatlamlarini tartiblang** `· oson`  
   Quyidagi qatlamlarni eng pastki (poydevor) qatlamdan eng yuqori qatlamgacha to'g'ri ketma-ketlikda daftaringizga yozing:  
   *Applications, Linux Kernel, Java API Framework, HAL, Android Runtime.*

2. **Drayverlar qaysi qatlamda joylashgan?** `· oson`  
   Wi-Fi va kamera drayverlari Android arxitekturasining qaysi qatlamiga tegishli ekanini va nima uchunligini tushuntiring.

3. **.dex formati nima?** `· oson`  
   Nima uchun Androidda kompyuterlardagi oddiy `.class` yoki `.jar` fayllari to'g'ridan-to'g'ri ishlatilmaydi va nima uchun `.dex` faylga o'tkaziladi?

4. **Kamera ochilish jarayoni** `· o'rta`  
   Siz ekrandagi "Rasmga olish" tugmasini bosganingizda, bu buyruq qaysi qatlamlar orqali fizik kamera moduliga yetib borishini zanjir ko'rinishida yozing.

5. **Dalvik va ART taqqoslashi** `· o'rta`  
   Dalvik (JIT) va ART (AOT) kompilyatsiyalari o'rtasidagi asosiy farqni va nima sababdan ART batareyani tejashini tushuntiruvchi qisqa jadval tuzing.

6. **Activity Manager vazifasi** `· o'rta`  
   Siz biror ilovadan chiqib, "Home" tugmasini bosganingizda va boshqa ilovaga o'tganingizda, bu jarayonni qaysi menejer boshqaradi?

7. **Sandbox nima va u telefonni qanday himoya qiladi?** `· o'rta`  
   Bitta soxta o'yin o'rnatilsa, u telefoningizdagi bank ilovasi parollarini nega birdaniga o'g'irlab ketolmasligini Sandbox tamoyili asosida tushuntiring.

8. **SQLite va SharedPreferences tanlovi** `· qiyin`  
   Quyidagi holatlarning qaysi birida `SharedPreferences`, qaysi birida `SQLite (Room)` ishlatilishi to'g'ri ekanini aniqlang va sababini ayting:
   - A) Foydalanuvchining tungi rejim sozlamasini saqlash;
   - B) 500 ta kitobdan iborat elektron kutubxona ma'lumotlarini saqlash;
   - C) Ilovadagi audio ovoz balandligi foizini saqlash;
   - D) Barcha kiruvchi va chiquvchi xatlar ro'yxatini saqlash.

9. **Low Memory Killer ssenariysi** `· qiyin`  
   Telefonda operativ xotira (RAM) to'lib qolganda, Linux yadrosidagi Low Memory Killer mexanizmi qaysi ilovalarni birinchi navbatda yopadi: oldinda turgan ilovanimi yoki orqa fondagi ilovalarnimi? Nima uchun?

10. **Tadqiqotchi tahlilchi** `· bonus`  
    Android arxitekturasida Java API Framework va Native C/C++ kutubxonalari ajratilgan. Nima uchun Androidning barcha qismlari boshidan oxirigacha faqat Java/Kotlin tilida yozilmagan? C/C++ tillarining afzalligi nima?

---

## Bilasizmi?

- Androidda ishlaydigan **SQLite** ma'lumotlar bazasi shunchalik ishonchli va yengilki, u hatto AQSH harbiy samolyotlarida, kosmik kemalarda va barcha iPhone telefonlarida ham qo'llaniladi!
- Dastlabki Android tizimlarida ilovalar Dalvik virtual mashinasida ishlagan. "Dalvik" nomi Android jamoasi muhandislaridan birining ajdodlari yashagan Islandiyadagi kichik qishloq nomi sharafiga qo'yilgan.

---

## Dars xulosasi

- Android — 5 ta asosiy qatlamdan (Linux Kernel, HAL, ART/Libraries, Java API Framework, Applications) tashkil topgan.
- Tizimning barqarorligi va tezkorligi AOT texnologiyasiga ega zamonaviy ART virtual mashinasiga tayanadi.
- Linux yadrosidagi ko'p foydalanuvchili tizim har bir ilovaga alohida UID berib, xavfsiz Sandbox muhitini yaratadi.
- Ma'lumotlarni saqlash uchun SharedPreferences (kichik sozlamalar) va SQLite/Room (katta jadvallar) ishlatiladi.

---

## O'zingizni tekshiring

1. Android arxitekturasining eng poydevor qatlami nima?
2. Hardware Abstraction Layer (HAL) ning asosiy vazifasi nima?
3. ART va Dalvik o'rtasidagi asosiy farq nima?
4. Ilovalararo ma'lumot almashishni qaysi Framework komponenti ta'minlaydi?
5. Nima sababdan har bir ilova alohida jarayonda ishlaydi?
