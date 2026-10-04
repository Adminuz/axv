# 10-sinf (Advanced Python Back-end): 1-hafta baholash qaydnomasi

**Mavzular:**
1. Django REST Framework. Server side rendering va user side rendering tushunchalari
2. DRF loyiha qurish: MBni loyihalash. Loyihani yaratish, dastlabki sozlamalar
3. Model, View va Serializer. Routerlar

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Nazariy bilim** | SSR/CSR farqi, REST tamoyillari, ERD munosabatlari va N+1 muammosi mohiyati | 30 ball |
| **Muhit va sozlash** | Virtual muhit, requirements.txt, .env xavfsizligi va settings.py modulli arxitekturasi | 30 ball |
| **Amaliyot & Kod** | Modellar, Serializerlar (Read/Write), ModelViewSet va DefaultRouter orqali API ishlashi | 40 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | Nazariya (30) | Muhit sozlash (30) | Amaliyot & Kod (40) | Jami ball (100) | Izoh |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |

---

## Mentor qaydlari va tahlil

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar boshida `select_related` bilan `prefetch_related` farqini yoki nima uchun Read va Write uchun ikkita alohida serializer kerakligini tushunishda biroz ikkilanishi mumkin. Doskada yoki slaydda N+1 so'rovlarini ko'rsatish tavsiya etiladi.
- **Iqtidorli o'quvchilar uchun:** Kategoriya va teglarga qo'shimcha ravishda `Comment` modelini daraxtsimon (replies) shaklda serializer orqali chiqarishni mustaqil topshirish mumkin.
