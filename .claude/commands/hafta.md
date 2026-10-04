---
description: Haftalik dars materiallarini tayyorlash. Misol — /hafta 8-sinf 5 yoki /hafta 11-sinf
argument-hint: <8-sinf|11-sinf> [hafta raqami]
---

Mentor haftalik dars materiallarini tayyorlashni so'radi. Argumentlar: `$ARGUMENTS`

1. Argumentlardan sinfni aniqla:
   - `8-sinf` (yoki `8`) → agent `8-sinf-tayyorlov`
   - `11-sinf` (yoki `11`) → agent `11-sinf-tayyorlov`
2. Ikkinchi argument hafta raqami (masalan `5`). Agar berilmasa, agentga «xaritadagi Joriy holat blokidan keyingi darsni ol» de.
3. Sinf aniqlanmasa, mentordan qaysi sinf ekanini so'ra va to'xta.
4. Tanlangan agentni Agent tool orqali ishga tushir. Prompt shunday bo'lsin: «<N>-hafta uchun 3 ta dars materiallarini tayyorla» (hafta berilmagan bo'lsa: «xaritadagi keyingi hafta uchun»). Qolgan qoidalar agentning o'z ko'rsatmasida bor, ularni takrorlama.
5. Agent tugagach, mentorga qisqa ayt: qaysi fayllar yaratildi, qayerda turibdi, nima noaniq qoldi. Fayl mazmunini takrorlama.
