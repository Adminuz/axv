# 5-hafta. Uyga vazifalar

Har bir vazifa 20–30 daqiqa vaqt oladi. Vazifalar daftarda yoki kompyuterda alohida papkada saqlanadi. Akkaunt kerak bo'lgan qadamlarni ota-onangiz ruxsati va yordami bilan bajaring; akkaunt yoki Git bo'lmasa, shu qadamni daftarda chizma, jadval yoki «commit kartochkalari» ko'rinishida bajaring.

## 13-dars uchun (Bulutli xizmatlar, 3-qism)
**1-topshiriq: «Mening bulutim xavfsizmi?»**
1. O'zingizning (yoki ota-onangiz bilan tanlangan namunaviy) 3 ta bulutdagi faylingiz uchun ruxsatlar auditi jadvalini tuzing: fayl, kim kira oladi, qanday ruxsat, o'zgartirish kerakmi.
2. Kamida bitta keraksiz ruxsatni olib tashlang yoki «Havolasi bor har kim» ni **Cheklangan** ga o'zgartiring (yoki daftarda qanday qilishni yozing).
3. Bulutdagi xotirangiz qancha band ekanini toping va joyni bo'shatishning 3 qadamli rejasini yozing.
4. Bulutda xavfsizlikning 5 qoidasidan oilangiz uchun «eslatma varaqasi» tayyorlang.

**Kutiladigan natija:** 3 qatorli audit jadvali, kamida 1 ta tuzatilgan ruxsat, xotira rejasi va 5 bandli eslatma.

## 14-dars uchun (Git va GitHub, 1-qism)
**2-topshiriq: «Men haqimda» repository'si**
1. GitHub'da `men-haqimda` nomli repository'ni **Add a README file** bilan yarating.
2. README'ni Markdown'da to'ldiring: `#` sarlavha, `##` «Qiziqishlarim» bo'limi, **qalin** matn va kamida 3 bandli ro'yxat. Telefon raqami va manzil yozmang!
3. Kamida **3 ta commit** qiling, har biriga tushunarli xabar yozing.
4. Commits sahifasidan har commitning xabari, vaqti va qisqa ID'sini daftarga yozing.

**Kutiladigan natija:** repository havolasi, formatlangan README va 3 ta commit jadvali.

## 15-dars uchun (Git va GitHub, 2-qism)
**3-topshiriq: «Kundalik» davomi**
1. Darsdagi `kundalik` repository'sida har kun uchun bitta fayl yarating (`seshanba.txt`, `chorshanba.txt`, ...) — kamida 3 ta yangi fayl.
2. Har bir faylni alohida commit qiling (`git add` → `git commit -m "..."`), har safar oldin va keyin `git status` ni tekshiring.
3. `README.md` ga «Bu hafta nimani o'rgandim» bo'limini qo'shib, commit qiling.
4. `git log --oneline` natijasining skrinshotini oling yoki daftarga ko'chiring (kamida 6 ta commit).

**Kutiladigan natija:** kamida 6 ta commitli tarix va har bir commit uchun aniq xabar.

## Mentor uchun
16-dars boshida 3-topshiriqdagi `kundalik` repository'lari GitHub'ga **push** qilinadi — o'quvchilar papkani o'chirmasligi va kompyuterni almashtirmasligi kerak (yoki papkani fleshkaga nusxalab olsin). 2-topshiriqda README'dagi shaxsiy ma'lumotlarni tekshiring. Commit xabarlarini baholashda «nima o'zgardi?» savoliga javob berishiga qarang; `asdf`, `123` kabi xabarlar uchun ball kamaytiriladi. Git o'rnatilmagan uyda topshiriq «commit kartochkalari» (har kartada: xabar, sana, o'zgargan fayl) bilan bajarilishi mumkin.
