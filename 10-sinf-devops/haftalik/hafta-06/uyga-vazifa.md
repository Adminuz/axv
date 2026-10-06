# 6-hafta: Uyga vazifa

**Fan:** DevOps  
**Sinf:** 10-sinf  
**Hafta:** 6-hafta  
**Topshirish muddati:** Keyingi darsga qadar (7-hafta, 1-dars)

---

## Topshiriq 1: Git ilg'or texnikalari · qiyin

1. Test repozitoriyda stash → boshqa branch → pop sikl ini bajaring va buyruqlarni yozing.
2. `feature` branch da 3 ta commit qilib, `rebase -i` bilan bittaga birlashtiring; `git log --oneline` natijasini yozing.
3. `git reset --hard HEAD~1` qilib, `reflog` bilan commit ni tiklang.

---

## Topshiriq 2: Taglar va SemVer · o'rta

1. Test repozitoriyda `v0.1.0` annotated tag yarating va GitHub ga yuboring.
2. Quyidagi o'zgarishlar uchun yangi versiyani yozing: 1) xato tuzatish; 2) yangi imkoniyat; 3) API buzildi (boshlang'ich 1.3.4).
3. GitHub da release yarating va 3 jumlali release notes yozing.

---

## Topshiriq 3: GitHub Flow · oson

1. Test repozitoriyda `feature/` branch ochib, PR yarating va skrinshot qo'shing.
2. Hamkasb PR iga kamida 2 ta izoh yozib review qiling.
3. GitHub Flow va Git Flow ni 5 qatorli jadvalda solishtiring.

---

## Baholash mezoni

| Mezon | Ball |
|---|---|
| 16-dars: stash, rebase, cherry-pick va reflog | 3 |
| 17-dars: Tag, SemVer va release | 3 |
| 18-dars: GitHub Flow va PR | 2 |
| Toza, o'z vaqtida va mustaqil bajarilgan | 2 |
| **Jami** | **10** |
| Bonus: bonus darajadagi topshiriq | +2 |

---

## Mentor uchun

**Tekshirish:**
- 16-dars: reflog nima uchun?? Javobi: Yo'qolgan commit ni topib tiklash.
- 17-dars: Release nima?? Javobi: Tag asosidagi GitHub nashr sahifasi.
- 18-dars: CLI va GitKraken farqi?? Javobi: CLI — terminal; GitKraken — grafik, natija bir xil.

**Keng tarqalgan xatolar:**
- 16-dars: Push qilingan umumiy tarixni rebase qilish.
- 17-dars: Tag ni yaratib, GitHub ga push qilishni unutish.
- 18-dars: To'g'ridan-to'g'ri main ga commit qilish.
