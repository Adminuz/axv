# 10-sinf (Kiberxavfsizlik): 2-hafta baholash qaydnomasi

**Mavzular:**
1. CIA uchligi (1-qism): konfidensiallik, yaxlitlik va foydalanuvchanlik tamoyillari
2. CIA uchligi (2-qism): CIA buzilish ssenariylari va MITM hujumlari
3. Xavfsizlikni anglash (1-qism): xavfsizlik tafakkuri va kuchli parollar siyosati

---

## Baholash mezonlari

| Mezon | Tavsif | Maks. ball |
|---|---|---|
| **CIA Triadasi** | Confidentiality, Integrity, Availability mohiyati, SHA-256 xesh tahlili | 30 ball |
| **MITM va Tarmoq** | ARP Spoofing mexanizmi, arpspoof, Wiresharkda HTTP tahlili, DAI va VPN | 30 ball |
| **Tafakkur & Parollar** | Security Mindset tamoyillari, Nmap va Hydra tahlili, Bitwarden va kuchli parollar | 40 ball |
| **JAMI** | | **100 ball** |

---

## O'quvchilar natijalari jadvali

| № | O'quvchi F.I.Sh. | CIA triadasi (30) | MITM & Tarmoq (30) | Tafakkur & Parol (40) | Jami ball (100) | Izoh |
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

- **Darsdagi asosiy qiyinchiliklar:** O'quvchilar ko'pincha ARP protokoli nega himoyalanmaganligini va MITM paytida IP Forwarding yoqilmasa nima sababdan internet uzilib qolishini tushunishda qiyinchilikka duch kelishlari mumkin. Ushbu jarayonni doskada paketlar yo'nalishi bilan chizib ko'rsating.
- **Iqtidorli o'quvchilar uchun:** Wireshark filtrlari (masalan, `arp.duplicate-address-frame` yoki `tcp.flags.syn == 1 and tcp.flags.ack == 0`) orqali tarmoqda anomal harakatlarni avtomatik aniqlash amaliyotini berish tavsiya etiladi.
