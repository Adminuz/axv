# 7-dars. Clean Code asoslari va SOLID: SRP hamda OCP tamoyillari

> Professional kod madaniyati, to'g'ri nomlash, DRY/KISS/YAGNI tamoyillari hamda barqaror arxitektura poydevori: SRP va OCP.

## Dars xulosasi

- **Clean Code (Toza kod):** Maqsadi bir o'qishda tushunarli bo'lgan, oson testlanadigan va o'zgartirishga chidamli dasturiy kod.
- **Kodni o'qish nisbati:** Dasturchi kod yozishdan ko'ra mavjud kodni o'qishga 10 barobar ko'p vaqt sarflaydi. Shuning uchun aniq nomlash — birinchi raqamli vazifadir.
- **DRY (Don't Repeat Yourself):** Takrorlanuvchi mantiqni bitta joyga jamlash.
- **KISS (Keep It Simple, Stupid):** Tizimni asossiz murakkablashtirmaslik.
- **YAGNI (You Aren't Gonna Need It):** Faqat bugun kerak bo'lgan kodni yozish, kelajak taxminlari bilan ortiqcha yuk yaratmaslik.
- **SRP (Single Responsibility):** Har bir sinf yoki modul faqat bitta mas'uliyatga ega bo'lishi va faqat bitta sabab bilan o'zgarishi kerak.
- **OCP (Open/Closed):** Kod yangi imkoniyatlar uchun ochiq (kengaytiriladigan), lekin mavjud kodni o'zgartirish uchun yopiq bo'lishi lozim (Polimorfizm va Abstraksiya orqali).

---

## Qo'shimcha ma'lumot

### 1. «Buzilgan derazalar» nazariyasi (Broken Windows Theory) dasturlashda

Kriminologiyada mashhur tushuncha bor: agar binodagi bitta singan deraza tuzatilmay qolsa, tez orada qolgan barcha derazalar ham toshbo'ron qilinadi va bino xarobaga aylanadi.
Dasturlashda ham xuddi shunday:
- Agar siz loyihada shoshilinch yozilgan, yomon nomlangan bitta funksiyani ko'rsangiz va «mayli, keyinroq to'g'rilayman» deb qoldirsangiz, jamoaning boshqa a'zolari ham shunga o'xshash tartibsiz kod yozishga o'rganadi.
- Bir necha oydan so'ng loyiha «spaghetti kod» botqog'iga botadi.
- **Boy Scout Rule (Skautlar qoidasi):** «Lagerdan ketayotganingda, u yerni kelganingdagidan ko'ra tozaroq qilib qoldir». Har safar faylni tahrir qilganingizda, undagi hech bo'lmaganda bitta kichik nom yoki formatni yaxshilang!

### 2. Side Effects (Yon ta'sirlar) balosi

Funksiya o'z nomida va'da qilgan ishidan boshqa yashirin amallarni bajarsa, bu **Side Effect** deyiladi.
Masalan: `check_password(user, password)` funksiyasi parolni tekshirayotib, bir vaqtning o'zida sessiyani ham tozalab tashlasa, boshqa dasturchi buni bilmaydi va kutilmagan yashirin xatolar (bugs) yuzaga keladi.
Funksiya kutilmagan yon ta'sirlarga ega bo'lmasligi, global o'zgaruvchilarga tegmasligi va faqat o'z natijasini qaytarishi lozim.

---

## Atamalar lug'ati

| Atama | Ma'nosi |
|---|---|
| **Clean Code** | O'qilishi va tushunilishi oson, o'zgarishlarga moslashuvchan yuqori sifatli kod |
| **DRY** | «Don't Repeat Yourself» — kodni takrorlamaslik tamoyili |
| **KISS** | «Keep It Simple, Stupid» — yechimni imkon qadar sodda saqlash tamoyili |
| **YAGNI** | «You Aren't Gonna Need It» — ortiqcha va erta kod yozmaslik tamoyili |
| **SOLID** | Obyektga yo'naltirilgan dizaynning 5 ta tayanch arxitektura tamoyili |
| **SRP** | Single Responsibility Principle — yagona mas'uliyat tamoyili |
| **OCP** | Open/Closed Principle — kengaytirishga ochiq, o'zgartirishga yopiq tamoyili |
| **Extract Method** | Katta funksiyadan alohida mantiqiy qismni ajratib mustaqil funksiya qilish |
| **Polimorfizm** | Bir xil interfeys orqali turli obyektlarning har xil ishlash qobiliyati |

---

## Bilasizmi?

- 📖 **Clean Code kitobi:** Robert C. Martin tomonidan 2008-yilda yozilgan ushbu kitob butun dunyoda millionlab dasturchilarning dasturiy ta'minotga bo'lgan qarashini tubdan o'zgartirgan.
- 💰 **Texnik qarz (Technical Debt):** Ward Cunningham tomonidan kiritilgan atama. Sifatsiz yozilgan kod xuddi foizli qarz kabidir: hozir vaqt tejalgandek tuyuladi, lekin har bir yangi funksiyada foiz to'lashga (xatolarni tuzatish va sekin ishlashga) to'g'ri keladi.

---

## Savollar va topshiriqlar

### 1-topshiriq · oson
DRY, KISS va YAGNI qisqartmalarining kengaytmasi va asosiy g'oyasini o'z so'zlaringiz bilan tushuntiring.

### 2-topshiriq · oson
Quyidagi o'zgaruvchi nomlarini Clean Code talablari asosida tushunarli qilib qayta nomlang:
1. `d = 14` (foydalanuvchining sinov muddati kunlari);
2. `fn(u)` (foydalanuvchiga faollashtirish xatini yuborish funksiyasi);
3. `lst` (saralangan kitoblar ro'yxati).

### 3-topshiriq · oson
Single Responsibility Principle (SRP) mohiyati nimada? Nega bitta sinfda faqat bitta sabab bilan o'zgarish bo'lishi kerak?

### 4-topshiriq · o'rta
Quyidagi kodda SRP qanday buzilganligini aniqlang va uni qanday qilib to'g'ri sinflarga ajratish mumkinligini tushuntiring:
```python
class UserManager:
    def create_user(self, email, password):
        ...
    def hash_password(self, password):
        ...
    def save_to_database(self, user):
        ...
    def send_welcome_email(self, email):
        ...
```

### 5-topshiriq · o'rta
Open/Closed Principle (OCP) tamoyiliga ko'ra «kengaytirishga ochiq, o'zgartirishga yopiq» iborasini real hayotiy misol (masalan, elektr rozetkasi va turli qurilmalar vilkalari) orqali tushuntiring.

### 6-topshiriq · o'rta
Quyidagi hisob-kitob kodini `if/elif` shartlaridan xalos qilib, OCP talablariga mos (abstrakt sinf va strategiyalar yordamida) qanday qayta qurish mumkinligini rejalang:
```python
def calculate_shipping(order):
    if order.delivery_type == "standard":
        return 15000
    elif order.delivery_type == "express":
        return 35000
    elif order.delivery_type == "drone":
        return 60000
```

### 7-topshiriq · o'rta
Funksiyalardagi Side Effect (yon ta'sir) nima va u nega yashirin xatoliklarga sabab bo'ladi? Bitta sodda misol keltiring.

### 8-topshiriq · qiyin
Kodni tahlil qiling: Agar bir funksiya 8 ta parametr qabul qilsa (`name, age, email, phone, city, zip, street, country`), bu qanday kod hidini (code smell) bildiradi va uni Clean Code asosida qanday yechish kerak?

### 9-topshiriq · qiyin
Python tilida `abc` moduli yordamida `NotificationSender` abstrakt bazaviy sinfini va undan meros oluvchi `EmailSender` hamda `SmsSender` sinflarini yozing. Yangi `TelegramSender` qo'shilganda asosiy kod o'zgarmasligini isbotlang.

### 10-topshiriq · qiyin
«Texnik qarz» (Technical debt) nima? Nega kompaniyalar tez-tez reliz chiqarish bahonasida Clean Code'ni chetga surib qo'ysa, 1 yildan keyin tizimni butunlay qayta yozishga majbur bo'ladi?

### 11-topshiriq · bonus
O'zingiz avval yozgan (yoki ochiq manbali) biror Python funksiyasini toping va uni bugun o'rganilgan barcha qoidalar: nomlash, bitta maqsad, DRY, KISS va SRP bo'yicha to'liq refaktoring qilib, «Oldin» va «Keyin» holatlarini taqqoslang.

---

## O'z-o'zini tekshirish savollari

1. «Boy Scout Rule» dasturchiga qanday vazifa yuklaydi?
2. Nega izohlar (comments) ko'pincha yomon kodning belgisi hisoblanadi?
3. SRP buzilgan sinfni testlash nega qiyin bo'ladi?
4. OCP tamoyilini buzgan dasturga yangi funksiya qo'shish qanday xatarlarni keltirib chiqaradi?
5. Immutability (o'zgarmaslik) kod sifatiga qanday ta'sir qiladi?
