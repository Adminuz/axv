// VitePress sozlamalari (qo'lda tahrirlanadi). Menyu va sinflar ro'yxati generated.json dan keladi:
// uni `python3 vitepress_yigish.py` yaratadi, qo'lda tahrirlamang.
import { defineConfig } from 'vitepress'
import gen from './generated.json'

export default defineConfig({
  lang: 'uz',
  title: gen.tashkilot,
  titleTemplate: ':title · AXV',
  description: "O'quvchilar uchun darslar: slaydlar, qo'shimcha ma'lumot va topshiriqlar",
  cleanUrls: true,
  appearance: 'dark', // standart qorong'i (VS Code Dark+), tugma bilan yorug' (Light+)
  head: [
    ['meta', { name: 'robots', content: 'noindex' }],
    ['meta', { name: 'mobile-web-app-capable', content: 'yes' }],
    ['link', { rel: 'icon', href: '/logo.png' }],
    ['script', {}, `if ('serviceWorker' in navigator) { navigator.serviceWorker.getRegistrations().then(function(regs) { for (var r of regs) { r.unregister(); } }); }`],
  ],
  markdown: {
    theme: { light: 'light-plus', dark: 'dark-plus' }, // VS Code kod ranglari
    config(md) {
      // satr ichidagi kodda `{{ }}` Vue deb o'qilmasin
      md.renderer.rules.code_inline = (tokens, idx) =>
        '<code v-pre>' + md.utils.escapeHtml(tokens[idx].content) + '</code>'
    },
  },
  themeConfig: {
    logo: '/logo.png',
    siteTitle: 'AXV',
    nav: gen.nav,
    outline: { level: [2, 3], label: 'Sahifada' },
    docFooter: { prev: 'Oldingi', next: 'Keyingi' },
    sidebarMenuLabel: 'Menyu',
    returnToTopLabel: 'Yuqoriga',
    darkModeSwitchLabel: 'Mavzu',
    lightModeSwitchTitle: "Yorug' mavzuga o'tish",
    darkModeSwitchTitle: "Qorong'i mavzuga o'tish",
    axvFooter: gen.podval, // o'z podvalimiz (PageBottom.vue)
    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: { buttonText: 'Qidirish', buttonAriaLabel: 'Qidirish' },
              modal: {
                noResultsText: 'Natija topilmadi',
                resetButtonTitle: 'Tozalash',
                footer: { selectText: 'tanlash', navigateText: "o'tish", closeText: 'yopish' },
              },
            },
          },
        },
      },
    },
  },
})
