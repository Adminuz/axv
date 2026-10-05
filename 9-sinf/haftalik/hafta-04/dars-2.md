# 11-dars. UI elementlarida rang nazariyasi

**Hafta:** 4 · **Davomiyligi:** 80 daqiqa · **Turi:** nazariya + dizayn amaliyoti (Figma) · **I-bob**, 1.4-mavzu, 2-dars

**Manba:** o'quv qo'llanma («Ranglar palitrasi va rang nazariyasi», 1.15–1.18-rasmlar), uslubiy ko'rsatma.

## 1. Dars rejasi

**Maqsad:** o'quvchilar rang g'ildiragi (color wheel), 4 xil rang palitrasi (monoxromatik, analog, qo'shimcha/komplementar, triadik), asosiy brend rangi tushunchasi hamda WCAG bo'yicha rang kontrasti (4.5:1 qoidasi) talablarini o'rganadi; Figma dasturida to'g'ri rang palitrasi va kontrastli UI elementlar (tugmalar, kartalar) yaratadi.

**Kutiladigan natija:**
- Rang g'ildiragida asosiy va qo'shimcha ranglarni ko'rsatadi;
- 4 xil palitrani (monoxromatik, analog, komplementar, triadik) farqlaydi;
- Bitta asosiy brend rangi tanlash muhimligini (Facebook, Spotify misolida) tushuntiradi;
- WCAG kontrast talabini (oddiy matn 4.5:1, katta matn 3:1) biladi;
- Figmada HSB/HEX orqali uyg'un ranglar palitrasini yasaydi.

| Vaqt | Bosqich | Mazmun |
|---|---|---|
| 0–10 daq | Takrorlash va kirish | 10-dars: tipografiya takrori. Savol: «Nega Spotify yashil, Facebook ko'k rangda?» |
| 10–35 daq | Yangi mavzu | Rang g'ildiragi, 4 xil palitra, brend rangi, WCAG kontrasti, madaniy farqlar |
| 35–40 daq | Tanaffus | Harakatli tanaffus |
| 40–70 daq | Amaliy mashg'ulot | Figmada 60-30-10 qoidasi bo'yicha rang palitrasi va tugmalar dizayni |
| 70–76 daq | Tezkor nazorat | 4 ta savol |
| 76–80 daq | Xulosa va uyga vazifa | Uyga vazifani tushuntirish |

---

## 2. Dars konspekti

### 2.1. Rang palitrasining 4 asosiy turi
- **1. Monoxromatik (Monochromatic):** Bitta rangning turli to'yinganlik va yorqinlik soyalari (HSB: H bir xil, S va B o'zgaradi). Eng toza va barqaror ko'rinish beradi.
- **2. Analog (Analogous):** Rang g'ildiragida yonma-yon turgan 2–3 ta rang (masalan: ko'k, ko'k-binafsha, feruza). Tabiiy va xotirjam tuyg'u uyg'otadi.
- **3. Qo'shimcha / Komplementar (Complementary):** Rang g'ildiragida bir-biriga qarama-qarshi turgan 2 ta rang (masalan: ko'k va to'q sariq, qizil va yashil). Kuchli kontrast yaratadi.
- **4. Triadik (Triadic):** Rang g'ildiragida teng masofada (uchburchak) joylashgan 3 ta rang. Jonli va boy palitra.

### 2.2. Brend rangi va 60-30-10 qoidasi
Interfeysda yuzlab ranglarni aralashtirish tartibsizlik keltiradi:
- **60% &mdash; Dominant rang:** Odatda neytral fon (oq, och kulrang yoki to'q qora).
- **30% &mdash; Ikkilamchi rang:** Kartalar, sarlavhalar, bo'limlar foni.
- **10% &mdash; Aksent (Brend) rangi:** Asosiy tugmalar (CTA &mdash; Call to Action), faol havolalar, bildirishnomalar.

### 2.3. WCAG Kontrast talabi (Kirish imkoniyati / Accessibility)
Matn fonga nisbatan aniq ko'rinishi shart:
- Oddiy matn (14–16px) uchun kontrast nisbati: kamida **4.5 : 1**;
- Katta sarlavhalar (18px+ Bold) uchun: kamida **3 : 1**.
- Tekshirish vositasi: WebAIM Contrast Checker yoki Figma plaginlari (Stark, Contrast).

---

## 3. Amaliy topshiriqlar va yechimlar

### 1-topshiriq. Monoxromatik palitra yasash (oson)
Figma'da bitta asosiy ko'k rang (`#1877F2`) tanlang va uning 4 ta soyasini (100%, 75%, 50%, 10% to'yinganlikda) 4 ta to'rtburchak shaklida chizing.

### 2-topshiriq. 60-30-10 qoidasi bo'yicha profil kartasi (o'rta)
Figma'da foydalanuvchi profil kartasini chizing:
- Fon: Oq / Och kulrang (60%);
- Matn va ramkalar: To'q kulrang (30%);
- «Kuzatish (Follow)» tugmasi: Yorqin brend rangi (10%).

### 3-topshiriq. Kontrast tekshiruvi (qiyin)
Sariq fonga oq matn yozilgan yomon tugma va qora fonga sariq matn yozilgan to'g'ri tugmani yonma-yon qo'yib, kontrast farqini ko'rsating.

---

## 4. Tezkor nazorat (savollar va javoblar)

1. **Monoxromatik palitra nima?**
   - *Javob:* Bitta rangning turli och-to'q soyalaridan iborat uyg'un palitra.
2. **60-30-10 qoidasi nimani bildiradi?**
   - *Javob:* 60% neytral fon, 30% ikkilamchi strukturaviy rang, 10% aksent (brend) rangi.
3. **WCAG bo'yicha oddiy matn uchun minimal kontrast nisbati qancha?**
   - *Javob:* Kamida 4.5:1.
4. **Komplementar ranglar qanday joylashadi?**
   - *Javob:* Rang g'ildiragida bir-biriga qarama-qarshi (180 gradusda).

---

## 5. Uyga vazifa

1. Figma'da o'zingiz yoqtirgan mavzu (ta'lim, yetkazib berish, musiqa) bo'yicha 3 ta rangdan iborat (Fon, Matn, Aksent) palitra tuzing.
2. Shu palitra asosida bitta «Mahsulot kartasi» (Product Card: rasm, narx, «Sotib olish» tugmasi) dizaynini chizing.
3. Tugma matni va foni orasidagi kontrast 4.5:1 dan yuqori ekanligini tekshiring.
