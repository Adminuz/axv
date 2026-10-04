---
description: O'quvchilar saytini yig'ish (VitePress). Misol — /sayt yoki /sayt 5 (faqat 1–5-haftalar)
argument-hint: [oxirgi hafta raqami]
---

Mentor o'quvchilar saytini yig'ishni so'radi. Argument: `$ARGUMENTS`

1. Loyiha papkasida (`/Users/dev/AXV Mentor`) kontentni tayyorla:
   - argument bo'sh: `python3 vitepress_yigish.py`
   - argument raqam (masalan `5`): `python3 vitepress_yigish.py --gacha 5` (keyingi haftalar «tez orada» bo'lib qoladi)
2. Saytni yig': `cd sayt-vitepress && npx vitepress build docs` (natija: `sayt-vitepress/docs/.vitepress/dist`). Agar `node_modules` yo'q bo'lsa, avval `npm install` kerak: bu paketlarni internetdan yuklaydi, shuning uchun mentordan so'ra.
3. Yechim yoki mentor izohi sizib chiqmaganini tekshir: `grep -rl 'class="notes"' sayt-vitepress/docs/.vitepress/dist` bo'sh bo'lsin; `grep -rli "yechim" sayt-vitepress/docs/.vitepress/dist` natijalarini ko'r: faqat oddiy so'z bo'lishi mumkin, topshiriq yechimi bo'lmasin.
4. Mentorga qisqa ayt: nechta sahifa yig'ildi va tayyor papka qayerda. Saytni internetga yuklash mentorning o'zi qiladi: hech qayerga yuklama va nashr qilma.
