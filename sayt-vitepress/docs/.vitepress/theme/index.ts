import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import PageTop from './components/PageTop.vue'
import PageBottom from './components/PageBottom.vue'
import Icon from './components/Icon.vue'
import './custom.css'

// Standart VitePress mavzusi (qidiruv, menyu, qorong'i/yorug' tugma) saqlanadi.
// Sahifa ichi (bosh sahifa, reja, kartalar, tugmalar) bizning komponentlar bilan chiziladi.
export default {
  extends: DefaultTheme,
  Layout: () =>
    h(DefaultTheme.Layout, null, {
      'doc-before': () => h(PageTop),
      'doc-after': () => h(PageBottom),
    }),
  enhanceApp({ app }) {
    app.component('Icon', Icon)
  },
}
