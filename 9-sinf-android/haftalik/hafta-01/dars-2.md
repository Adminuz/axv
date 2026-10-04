# 2-dars. Android tizimi va uning arxitekturasi

**Sinf:** 9-sinf (Android dasturlash)  
**Hafta:** 1-hafta  
**Dars tartibi:** 2-dars (umumiy 102 darsdan 2-darsi)  
**Davomiyligi:** 80 daqiqa  
**Format:** Nazariy va tizimli tahlil mashg'uloti  

---

## 1. Dars maqsadi va kutiladigan natijalar

- **Maqsad:** O'quvchilarga Android operatsion tizimining ko'p qatlamli vertikal arxitekturasi (Linux Kernel, HAL, Native Libraries, Android Runtime, Java API Framework, Applications) hamda tizimda ma'lumotlarni saqlash mexanizmlari (SQLite, Room, SharedPreferences, Firebase) haqida chuqur bilim berish.
- **Kutiladigan natijalar:**
  - O'quvchi Android arxitekturasining 5 ta asosiy qatlamini tartib bilan biladi va har bir qatlamning vazifasini tushuntira oladi;
  - Linux Kernel va Hardware Abstraction Layer (HAL) ning apparat ta'minoti bilan aloqasini tushunadi;
  - Dalvik Virtual Machine (DVM) va Android Runtime (ART) o'rtasidagi farqni (JIT vs AOT kompilyatsiya) anglaydi;
  - Java API Framework tarkibidagi asosiy menejerlarni (Activity Manager, Notification Manager, Content Provider, View System) ajrata oladi;
  - Nima uchun har bir Android ilovasi alohida jarayonda (Process) va alohida foydalanuvchi (UID) sifatida ishga tushishini xavfsizlik nuqtai nazaridan asoslay oladi;
  - Androidda ma'lumot saqlash texnologiyalari (SharedPreferences, SQLite, Room, Firebase) farqini biladi.

---

## 2. Dars rejasi (80 daqiqa)

| Vaqt | Bosqich | Tavsif |
|---|---|---|
| **00–10 daq** | O'tgan mavzuni takrorlash va kirish | Andy Rubin, Google xaridi, HTC Dream, Android versiyalari bo'yicha blits-savol. Muammoli savol: "Ilova kodimiz qanday qilib telefon kamerasini ishlatadi?" |
| **10–35 daq** | Yangi mavzu: Qatlamli arxitektura | Linux Kernel, HAL, Native C/C++ kutubxonalari, Android Runtime (Dalvik vs ART), Java baytkodi va `.dex` fayllar |
| **35–55 daq** | Yangi mavzu: Framework va ilovalar | Java API Framework (Activity Manager, View System va boshqalar), Ilovalar qatlami, jarayonlar izolyatsiyasi (Sandbox) |
| **55–65 daq** | Ma'lumotlarni saqlash texnologiyalari | SharedPreferences, Room / SQLite, Firebase Realtime Database va Cloud Firestore |
| **65–75 daq** | Amaliy mashq va sxematik tahlil | Android arxitektura sxemasini daftarga chizish va tarkibiy elementlarni to'g'ri joylashtirish |
| **75–80 daq** | Xulosa va baholash | Dars yakunlari, o'quvchilarni baholash, uyga vazifa topshirish |

---

## 3. Nazariy tushunchalar (Mentor uchun to'liq konspekt)

### 3.1. Android arxitekturasining vertikal qatlamlari
Android operatsion tizimi modulli, ko'p qatlamli (stack) arxitekturaga ega. Har bir qatlam faqat o'zidan pastdagi qatlam xizmatlaridan foydalanadi va yuqoridagi qatlamga tayyor interfeys taqdim etadi:

```
+-------------------------------------------------------+
| 5. Applications (Ilovalar qatlami)                   |
|    System Apps (Phone, Contacts) + User Apps (Click)   |
+-------------------------------------------------------+
| 4. Java API Framework (Tizim karkasi)                |
|    Activity Manager, View System, Content Providers... |
+-------------------------------------------------------+
| 3. Android Runtime (ART)   | Native C/C++ Libraries   |
|    DEX bytecode, AOT / JIT | SQLite, WebKit, Media    |
+-------------------------------------------------------+
| 2. Hardware Abstraction Layer (HAL)                   |
|    Kamera, Audio, Bluetooth, Datchiklar interfeysi   |
+-------------------------------------------------------+
| 1. Linux Kernel (Linux yadrosi)                       |
|    Drayverlar, Xotira, Jarayonlar, Quvvat boshqaruvi  |
+-------------------------------------------------------+
```

### 3.2. 1-qatlam: Linux Kernel (Linux yadrosi)
Android to'liq Linux operatsion tizimi emas, lekin uning yadrosi (Linux Kernel 5.x / 6.x) ustiga qurilgan.
Linux yadrosining asosiy vazifalari:
- **Drayverlar boshqaruvi:** Kamera (Camera Driver), displey, klaviatura, Bluetooth, Wi-Fi, audio drayverlari;
- **Xotira va resurslar:** Virtual xotira (RAM) boshqaruvi, Low Memory Killer (RAM tugaganda keraksiz ilovalarni yopish);
- **Jarayonlar nazorati (Process Management):** CPU vaqtini ilovalar o'rtasida rejalashtirish;
- **Xavfsizlik modeli:** Linux foydalanuvchilari tizimi (har bir o'rnatilgan ilovaga alohida `app_xxxx` UID beriladi).

### 3.3. 2-qatlam: Hardware Abstraction Layer (HAL)
Har xil smartfonlarda har xil ishlab chiqaruvchilarning kameralari, Bluetooth chiplari yoki audio mikrosxemalari o'rnatilgan bo'ladi.
- **HAL vazifasi:** Apparat qismining o'ziga xos xususiyatlarini yuqori qatlamdagi Java kodidan yashirish va standart C/C++ interfeysini taqdim etish.
- Natijada, dasturchi kamera uchun bitta umumiy Camera API kodini yozadi, HAL esa uni Samsung, Sony yoki Xiaomi sensoriga to'g'ri o'tkazib beradi.

### 3.4. 3-qatlam: Android Runtime (ART) va Native kutubxonalar
- **Native C/C++ kutubxonalari:**
  - `libc` (standart C tizimli kutubxonasi);
  - `Media Framework` (audio va video formatlarni dekodlash va ijro etish);
  - `Surface Manager` (turli ilovalardan keluvchi 2D va 3D grafika qatlamlarini ekranda birlashtiruvchi);
  - `SQLite` (engil relyatsion ma'lumotlar bazasi dvigateli);
  - `WebKit / Chromium` (veb sahifalarni ko'rsatish dvigateli).
- **Dalvik vs Android Runtime (ART):**
  - **Dalvik Virtual Machine (DVM):** Android 4.4 gacha ishlatilgan. Dastur kodi `.dex` (Dalvik Executable) baytkodiga aylanadi va ilova ochilganda **JIT (Just-in-Time)** usulida mashina kodiga o'giriladi (sekinroq ochilar edi).
  - **ART (Android Runtime):** Android 5.0 dan boshlab kiritilgan. **AOT (Ahead-of-Time)** kompilyatsiyasi orqali ilova o'rnatilayotgan paytda mashina kodiga kompilyatsiya qilinadi. Natijada ilovalar darhol, silliq va batareyani tejagan holda ishga tushadi.

### 3.5. 4-qatlam: Java API Framework
Dasturchilar Android ilovalari yozishda to'g'ridan-to'g'ri foydalanadigan barcha asosiy tayyor xizmatlar:
- **Activity Manager:** Ilovalarning hayotiy sikli (Lifecycle) va orqaga qaytish steki (Backstack) ni boshqaradi;
- **View System:** Tugmalar, matnlar, rasmlar, ro'yxatlar, gridlar va oynalarni chizuvchi komponentlar;
- **Notification Manager:** Foydalanuvchiga yuqori paneldan bildirishnoma ko'rsatish;
- **Content Providers:** Ilovalar o'rtasida ma'lumot almashish (masalan, kontaktlar bazasidan raqam olish);
- **Resource Manager:** XML maketlar, matnlar, rasmlar va ranglarni boshqaruvchi xizmat.

### 3.6. 5-qatlam: Applications (Ilovalar qatlami)
Foydalanuvchi ko'radigan barcha dasturlar:
- **Tizimli ilovalar (System Apps):** Telefon (Dialer), Kontaktlar, Soat, Kamera, Sozlamalar;
- **Foydalanuvchi ilovalari (User Apps):** Telegram, Click, Payme, o'yinlar va biz yaratadigan dasturlar.

### 3.7. Ma'lumotlarni saqlash texnologiyalari
Ilovalar ma'lumotlarini qayerda saqlaydi?
1. **SharedPreferences / DataStore:** Kichik sozlamalar (foydalanuvchi tili, tungi rejim, login holati) kalit-qiymat (Key-Value) juftligida saqlanadi.
2. **SQLite va Room:** Murakkab relyatsion ma'lumotlar, jadvallar (masalan, mahsulotlar katalogi, xabarlar tarixi). Room — SQLite ustiga qurilgan qulay va xavfsiz Google kutubxonasidir.
3. **Bulutli bazalar (Firebase Realtime DB / Cloud Firestore):** Internet orqali real vaqtda sinxronlashuvchi online bazalar.

---

## 4. Darsda bajariladigan amaliy topshiriqlar va yechimlari

### 1-topshiriq. Android arxitekturasi qatlamlari matritsasi (Oson)
**Topshiriq:** 5 ta arxitektura qatlamini pastdan yuqoriga qarab jadvalga joylashtiring va har bir qatlamga bittadan aniq misol yozing.

**Yechim:**
| Qatlam tartibi | Qatlam nomi | Misol / Komponent |
|---|---|---|
| 5 (Yuqori) | Applications | Telegram, Sozlamalar ilovasi |
| 4 | Java API Framework | Activity Manager, Notification Manager |
| 3 | Runtime & Libraries | ART (Android Runtime), SQLite, Media Framework |
| 2 | HAL | Camera HAL, Audio HAL |
| 1 (Quyi) | Linux Kernel | Bluetooth drayveri, Process Scheduler |

### 2-topshiriq. DVM va ART taqqoslash tahlili (O'rta)
**Topshiriq:** Dalvik Virtual Machine (DVM) va Android Runtime (ART) o'rtasidagi farqni JIT va AOT tushunchalari asosida taqqoslang. Nega zamonaviy smartfonlar faqat ART'dan foydalanadi?

**Yechim:**
- **Dalvik (JIT — Just-in-Time):** Ilova kodini har safar ishga tushganda yoki funksiya chaqirilganda bosqichma-bosqich mashina tiliga o'giradi. Bu protsessorga har safar ortiqcha yuk beradi va ilova sekinroq ochiladi.
- **ART (AOT — Ahead-of-Time):** Ilova o'rnatilayotganda kodi oldindan to'liq mashina tiliga kompilyatsiya qilinadi. Natijada ilova bir zumda ochiladi, CPU kuchi tejaladi, batareya quvvati 15-20% uzoqroq yetadi. Shuning uchun barcha zamonaviy Android tizimlari ART'dan foydalanadi.

### 3-topshiriq. Tizim xavfsizligi va Sandbox tahlili (Qiyin)
**Topshiriq:** Nega bitta ilova (masalan, zararli dastur) boshqa ilovaning (masalan, Click yoki Payme ilovasining) shaxsiy ma'lumotlarini to'g'ridan-to'g'ri o'qiy olmaydi? Linux arxitekturasi bunga qanday to'sqinlik qiladi?

**Yechim:**
Android Linuxning ko'p foydalanuvchili (multi-user) xavfsizlik modelidan foydalanadi:
1. Har bir o'rnatilgan ilovaga operatsion tizim tomonidan alohida virtual foydalanuvchi ID (UID) belgilanadi (masalan, `u0_a125`).
2. Har bir ilova alohida izolyatsiyalangan Linux jarayonida (Process) ishlaydi.
3. Linux fayl tizimida ilovaning shaxsiy papkasi (`/data/data/com.example.app/`) faqat o'sha ilovaning UID'si uchungina ruxsat etiladi (chmod 700 / 750).
4. Boshqa ilovaning UID'si boshqa bo'lgani sababli, operatsion tizim darajasida «Permission Denied» (Ruxsat yo'q) xatosi yuzaga keladi. Bu model «Application Sandbox» (ilova qumqutisi) deb ataladi.

---

## 5. Tezkor savol-javob (Blits-savollar)

1. **Android arxitekturasining eng poydevor qatlami nima?**  
   *Javob:* Linux Kernel (Linux yadrosi).
2. **HAL nimani anglatadi va uning vazifasi nima?**  
   *Javob:* Hardware Abstraction Layer — apparat ta'minotining abstraksiya qatlami bo'lib, Java kodini turli kameralar va chiplar bilan standart interfeys orqali bog'laydi.
3. **Androidda kompilyatsiya qilingan Java/Kotlin kodi qanday fayl formatiga aylanadi?**  
   *Javob:* `.dex` (Dalvik Executable) formatiga.
4. **Ilovalarning hayotiy siklini qaysi Framework komponenti boshqaradi?**  
   *Javob:* Activity Manager.
5. **Kichik foydalanuvchi sozlamalarini saqlash uchun qaysi texnologiya ishlatiladi?**  
   *Javob:* SharedPreferences yoki zamonaviy DataStore.

---

## 6. Mentor uchun amaliy tavsiyalar

- O'quvchilarga arxitekturani «ko'p qavatli bino» o'xshatishi orqali tushuntiring: 1-qavat — mustahkam poydevor (Linux), 2-qavat — santexnika va simlar (HAL), 3-qavat — elektr motorlar (ART va kutubxonalar), 4-qavat — xonalar karkasi (Framework), 5-qavat — mebel va yashovchilar (Ilovalar).
- Doskada yoki ekranda Linux UID izolyatsiyasini misol qilib ko'rsating, bu ularda kiberxavfsizlikka oid dastlabki to'g'ri tasavvurni shakllantiradi.
