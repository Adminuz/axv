# 10-sinf (Advanced Python Back-end): 2-hafta baholash qaydnomasi

**Mavzular:**
4. Foydalanuvchilarni boshqarish: Identifikatsiya, autentifikatsiya va avtorizatsiya. Token, session va JWT
5. Ruxsatlar bilan ishlash
6. Filtrlash, qidiruv va tartiblash

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **Autentifikatsiya (JWT)** | Custom User, UserManager, JWT (Access va Refresh) sozlash va tokenni sarlavhada yuborish | 35 ball |
| **Ruxsatlar (Permissions)** | IsStaffOrReadOnly, IsOwnerOrStaff, perform_create va IDOR xavfsizlik tekshiruvlari | 35 ball |
| **Qidiruv & Filtrlar** | django-filter, PostFilter, SearchFilter va OrderingFilter orqali ma'lumotlarni saralash | 30 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | JWT Auth (35) | Ruxsatlar (35) | Filtr & Qidiruv (30) | Jami ball (100) | Izoh |
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

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar ko'pincha `has_permission` va `has_object_permission` ning qaysi paytda chaqirilishini adashtirishadi. Ro'yxat ochilganda obyekt darajasidagi ruxsat ishlamasligini alohida ta'kidlash lozim.
- **Iqtidorli o'quvchilar uchun:** Foydalanuvchi parolini unutganda emailga tasdiqlash kodi yuborish yoki sana oralig'ini bir nechta maydonlar (`created_at`, `published_at`) bo'yicha birlashtirib qidirishni topshirish mumkin.
