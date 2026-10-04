# 2-dars. Operatsion tizimlar va Windows muhitida ishlash

**Hafta:** 1 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + amaliyot · **I-bob**, 2-dars

## 1. Dars rejasi

**Maqsad:** o'quvchilarga operatsion tizim (OT) tushunchasi, uning asosiy vazifalari, shaxsiy kompyuter va mobil qurilmalar uchun zamonaviy OT turlari (Windows, Linux, macOS, Android, iOS), Windows 10/11 ish stoli muhiti, Start menyusi, vazifalar paneli, oynalarni boshqarish (Snap layouts), tizim sozlamalari hamda dasturlarni o'rnatish va o'chirish ko'nikmalarini amaliy o'rgatish.

**Kutiladigan natija:**
- Operatsion tizim nima ekanligini va nima uchun kompyuterga OT zarurligini tushuntirib bera oladi.
- Windows, Linux va macOS operatsion tizimlarining o'ziga xos xususiyatlarini farqlaydi.
- Windows ish stoli, Start menyusi va oynalar bilan tezkor ishlay oladi (Snap layouts, `Win + strelkalar`).
- Windows Sozlamalari (Settings) va Boshqaruv paneli (Control Panel) orqali kompyuterni moslay oladi.
- Dasturlarni to'g'ri o'rnatish (.exe / .msi) va xavfsiz to'liq o'chirish (Uninstall) amallarini bajara oladi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 1-darsni takrorlash (CPU, RAM, arxitektura). «Kompyuter qismlari bor, ammo ekranda nima ko'rinadi?» muammoli savoli |
| 10–30 daq | Yangi mavzu: Nazariya | Operatsion tizim tushunchasi, apparat va dasturiy vositachi roli, Windows, Linux, macOS, Android, iOS |
| 30–35 daq | Tanaffus | Jismoniy harakat mashqlari |
| 35–65 daq | Amaliyot | Windows oynalarini boshqarish, Start menyusi, Snap layouts, Settings vs Control Panel, dasturlar ro'yxatini ko'rish |
| 65–75 daq | Tezkor nazorat | 5 ta savol va amaliy vazifa |
| 75–80 daq | Xulosa va uyga vazifa | Asosiy xulosalarni jamlash va uyga topshiriq |

---

## 2. Dars konspekti

### 2.1. Operatsion tizim nima va u nega kerak?

**Operatsion tizim (OT / Operating System — OS)** — bu kompyuterning barcha texnik apparat qismlarini (CPU, RAM, disklar, monitor, klaviatura) boshqaradigan va foydalanuvchi hamda dasturlarning kompyuter bilan qulay muloqotini ta'minlaydigan asosiy tizimli dasturlar majmuasi.

Agar operatsion tizim bo'lmaganida:
- Kompyuter shunchaki temir va mikrosxemalar to'plami bo'lib qolardi.
- Har bir dasturchi o'z dasturini yozayotganda ekranning har bir pikseliga rang berish, klaviaturaning har bir tugmasidan signalni qabul qilish kabi millionlab mayda texnik buyruqlarni noldan yozishi kerak bo'lardi.
- Operatsion tizim barcha texnik murakkabliklarni o'z zimmasiga oladi va foydalanuvchiga qulay **Grafik foydalanuvchi interfeysi (GUI — Graphical User Interface)** taqdim etadi.

### 2.2. Zamonaviy operatsion tizimlar turlari

1. **Shaxsiy kompyuterlar (PC) uchun:**
   - **Microsoft Windows (Windows 10, 11):** Dunyodagi eng mashhur shaxsiy kompyuter OT (bozordagi ulushi ~70%). Foydalanish sodda, o'yinlar va ofis dasturlarining deyarli barchasi unga moslashgan.
   - **macOS:** Apple kompaniyasining Mac kompyuterlari uchun maxsus ishlab chiqilgan OT. Yuqori darajadagi xavfsizlik, chiroyli dizayn va tezkorlikka ega.
   - **Linux (Ubuntu, Debian, Fedora, Arch):** Ochiq kodli (Open-source), bepul va o'ta xavfsiz OT. Dunyodagi aksariyat serverlar, bulut tizimlari, superkompyuterlar va dasturchilar aynan Linux asosida ishlaydi.
2. **Mobil qurilmalar uchun:**
   - **Android:** Google kompaniyasi tomonidan Linux yadrosi asosida yaratilgan, ochiq kodli eng ommabop mobil OT.
   - **iOS:** Apple kompaniyasining iPhone va iPad qurilmalari uchun yaratilgan yopiq va xavfsiz mobil tizim.

### 2.3. Windows ish stoli muhiti elementlari

- **Ish stoli (Desktop):** Tizim yuklangandan so'ng ekranda paydo bo'ladigan asosiy ish maydoni. Unda fayllar, papkalar va yorliqlar (Shortcuts) joylashadi.
- **Vazifalar paneli (Taskbar):** Odatda ekranning pastki qismida joylashgan chiziq. Unda Start tugmasi, qidiruv paneli, mahkamlangan va hozirda ochiq bo'lgan dasturlar belgilari turadi.
- **Start (Boshlash) menyusi:** Kompyuterga o'rnatilgan barcha dasturlar, tizim sozlamalari va kompyuterni o'chirish/qayta yuklash (Power) tugmalarini jamlagan bosh menyu.
- **Bildirishnomalar maydoni (System Tray):** Vazifalar panelining o'ng quyi burchagida joylashgan soat, sana, til indikatori, internet (Wi-Fi), tovush balandligi va batareya holati ko'rinib turadigan maydon.

### 2.4. Oynalar bilan professional ishlash (Snap layouts)

Windows nomi inglizcha «Windows» (oynalar) so'zidan olingan bo'lib, har bir dastur to'rtburchak oynada ochiladi.
- Oynaning yuqori o'ng burchagidagi 3 ta boshqaruv tugmasi:
  - `-` (Minimize) — oynani vazifalar paneliga yashirish;
  - `□` (Maximize / Restore) — oynani butun ekranga yoyish yoki oldingi o'lchamiga qaytarish;
  - `X` (Close) — dasturni butunlay yopish (`Alt + F4`).
- **Snap layouts (Ekran maydonini bo'lish):**
  - `Win + Chapga strelka` — oynani ekranning chap yarmiga joylashtirish.
  - `Win + O'ngga strelka` — oynani o'ng yarmiga joylashtirish.
  - Bu dasturchiga bir vaqtning o'zida bir tomonda kod yozib, ikkinchi tomonda natijani ko'rish imkonini beradi.

### 2.5. Tizim sozlamalari va Boshqaruv paneli

- **Sozlamalar (Settings, `Win + I`):** Zamonaviy va qulay Windows sozlamalar markazi. Unda ekran yorqinligi, internet, shaxsiylashtirish (fon rasmi, mavzu) va o'rnatilgan ilovalar boshqariladi.
- **Boshqaruv paneli (Control Panel):** Chuqurroq tizim sozlamalari, drayverlar va ma'muriy vositalar joylashgan an'anaviy panel.

### 2.6. Dasturlarni o'rnatish va to'g'ri o'chirish

- **Dastur o'rnatish:** Internetdan yuklab olingan o'rnatuvchi fayllar (`.exe` yoki `.msi` kengaytmali) administrator huquqi bilan ishga tushiriladi va o'rnatish ustasi (Setup Wizard) qadamlari bo'yicha o'rnatiladi.
- **Dasturni o'chirish:** Shunchaki ish stolidagi yorliqni (Shortcut) «Delete» bilan o'chirish dasturni kompyuterdan o'chirmaydi! Dasturni to'liq o'chirish uchun:
  - `Win + I` → «Apps» (Ilovalar) → «Installed apps» (O'rnatilgan ilovalar) bo'limiga kiriladi va kerakli dastur ro'yxatdan topilib, «Uninstall» tugmasi bosiladi.

---

## 3. Kod / Amaliy buyruqlar

Windows muhitida tezkor boshqaruv buyruqlari:

```powershell
# 1. Sozlamalar oynasini ochish
Win + I

# 2. Ishlayotgan dasturlar o'rtasida tezkor almashish
Alt + Tab

# 3. Barcha ochiq oynalarni bir zumda minimallashtirib ish stolini ko'rsatish
Win + D

# 4. Fayl boshqaruvchisini (File Explorer) ochish
Win + E

# 5. Oynani yopish
Alt + F4
```

---

## 4. Amaliy topshiriqlar

### 1-topshiriq (oson)
Klaviaturadagi `Win + I` kombinatsiyasi orqali Windows Sozlamalarini (Settings) oching. «System» bo'limidagi «About» (Tizim haqida) bandiga o'tib, Windows operatsion tizimingizning versiyasini (masalan, Windows 10 yoki Windows 11) va nashrini (Pro, Home) aniqlang.

**Kutiladigan natija:** Operatsion tizimning to'liq nomi va versiyasi yoziladi.

**Yechim:**
1. `Win + I` bosiladi.
2. Chap menyudan «System» tanlanadi va eng pastdagi «About» tugmasi bosiladi.
3. «Windows specifications» bo'limida Edition (masalan: *Windows 11 Pro*) va Version (masalan: *23H2*) ko'rinadi.

---

### 2-topshiriq (o'rta)
Brauzer (masalan, Google Chrome) va Bloknot (Notepad) dasturlarini oching. Snap mexanizmidan foydalanib, ekranning chap yarmiga brauzerni, o'ng yarmiga esa bloknotni aniq 50/50 qilib joylashtiring.

**Kutiladigan natija:** Ekran teng ikkiga bo'lingan holda ikkala dastur yonma-yon ishlaydi.

**Yechim:**
1. Brauzer oynasini tanlab, `Win + Chapga strelka` bosiladi.
2. Bloknot oynasini tanlab, `Win + O'ngga strelka` bosiladi.
3. Ikkala oyna ekranni to'ldirib, bir-birini to'smagan holda joylashadi.

---

### 3-topshiriq (qiyin)
Kompyuteringizda o'rnatilgan ilovalar ro'yxatini oching (`Win + I` → Apps → Installed apps). Ro'yxatdan kompyuteringizda o'rnatilgan 5 ta dasturni, ularning egallagan disk hajmini (MB yoki GB) aniqlang va keraksiz bitta yordamchi ilovani to'g'ri «Uninstall» qilish tartibini ko'rsating.

**Kutiladigan natija:** 5 ta dastur nomi, ularning hajmi jadvali tuziladi; dasturni o'chirishning to'liq ketma-ketligi yoziladi.

**Yechim:**
1. `Win + I` orqali «Apps» → «Installed apps» (yoki «Apps & features») bo'limiga kiriladi.
2. Dasturlar ro'yxatidan 5 ta dastur (masalan, Google Chrome, VS Code, VLC Player, Telegram, Flowgorithm) va ularning hajmi yozib olinadi.
3. Keraksiz ilovani o'chirish uchun uning yonidagi 3 nuqta `...` belgisi bosilib, «Uninstall» buyrug'i tanlanadi va tasdiqlanadi.

---

## 5. Tezkor nazorat

1. Operatsion tizimning kompyuterdagi asosiy vazifasi nima?
   - *Javob:* Apparat qismlarini boshqarish, dasturlar ishlashini ta'minlash va foydalanuvchiga qulay grafik interfeys berish.
2. PC uchun eng mashhur 3 ta operatsion tizimni ayting.
   - *Javob:* Windows, Linux, macOS.
3. Ish stolidagi dastur yorlig'ini (Shortcut) Delete bilan o'chirish dasturni kompyuterdan to'liq o'chiradimi?
   - *Javob:* Yo'q! Bu faqat uning belgisini o'chiradi. Dastur fayllari diskda qoladi. To'liq o'chirish uchun «Uninstall» qilish kerak.
4. Ekranni ikkita oyna o'rtasida teng ikkiga bo'lish uchun qaysi klavishlar kombinatsiyasi bosiladi?
   - *Javob:* `Win + Chapga strelka` va `Win + O'ngga strelka`.
5. Barcha ochiq oynalarni bir zumda yashirib, ish stoliga o'tish tugmasi qaysi?
   - *Javob:* `Win + D`.

---

## 6. Uyga vazifa

1. O'z kompyuteringizda quyidagi 4 ta tezkor buyruqni amalda sinab ko'ring va ularning har biri nima qilishini daftaringizga yozing:
   - `Win + E`
   - `Win + D`
   - `Win + I`
   - `Alt + Tab`
2. Kompyuteringizda o'rnatilgan 3 ta eng katta hajmli dasturning nomi va hajmini Settings orqali aniqlab yozing.
Vazifani bajarish vaqti: 20 daqiqa.
