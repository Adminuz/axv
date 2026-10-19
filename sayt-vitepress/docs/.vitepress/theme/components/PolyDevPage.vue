<script setup lang="ts">
import { withBase } from 'vitepress'
import Icon from './Icon.vue'
import Crumbs from './Crumbs.vue'

const PLAY_STORE_URL = 'https://play.google.com/store/apps/details?id=com.xapi.polydev'

const HIGHLIGHTS = [
  {
    icon: 'bot',
    title: "AI Coding Agent",
    desc: "Loyihangiz fayllari bilan ishlaydi: kod yozadi, xatolarni tuzatadi va refaktoring qiladi."
  },
  {
    icon: 'smartphone',
    title: "To'laqonli Mobil IDE",
    desc: "Fayllar daraxti, tablar, sintaksisni yoritish va o'rnatilgan Git (commit, branch, GitHub)."
  },
  {
    icon: 'terminal',
    title: "Alpine Linux Terminal",
    desc: "Node.js, npm, Python, PHP, Go to'g'ridan-to'g'ri telefonda — hech qanday SSH yoki server talab qilinmaydi."
  },
  {
    icon: 'rocket',
    title: "Live Preview & Deploy",
    desc: "Telefondan chiqmasdan natijani ko'rish va 1-bosishda Vercel / Cloudflare Pages'ga yuklash."
  }
]
</script>

<template>
  <div class="axv poly-compact">
    <Crumbs :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'PolyDev (Android)' }]" />

    <!-- MAIN COMPACT CARD -->
    <div class="poly-card">
      <div class="poly-header">
        <img :src="withBase('/polydev-icon.png')" alt="PolyDev" class="poly-app-icon" />
        <div class="poly-meta">
          <div class="poly-tag-row">
            <span class="poly-chip">Android 8.0+</span>
            <span class="poly-chip free">Bepul versiya</span>
          </div>
          <h1 class="poly-title">PolyDev: AI Coding Agent</h1>
          <p class="poly-sub">
            Telefoningizda to'liq dasturlash muhiti. O'rnatilgan AI agent, Linux terminali, Git va 1-bosishda internetga chiqarish.
          </p>
        </div>
        <div class="poly-cta">
          <a :href="PLAY_STORE_URL" target="_blank" rel="noopener" class="btn-gp">
            <svg class="gp-svg" viewBox="0 0 24 24">
              <path fill="#EA4335" d="M3.6 1.7L13.7 12 3.6 22.3c-.4-.4-.6-1.1-.6-1.9V3.6c0-.8.2-1.5.6-1.9z"/>
              <path fill="#FBBC04" d="M17.1 8.6L13.7 12l3.4 3.4 3.9-2.2c1.1-.6 1.1-1.7 0-2.3l-3.9-2.3z"/>
              <path fill="#4285F4" d="M3.6 1.7l10.1 10.3 3.4-3.4L5.6 1c-.8-.5-1.5-.2-2 .7z"/>
              <path fill="#34A853" d="M3.6 22.3l13.5-7.7-3.4-3.4-10.1 10.3c.5.9 1.2 1.2 2 .8z"/>
            </svg>
            <div>
              <span class="gp-lbl">Yuklab olish</span>
              <span class="gp-name">Google Play</span>
            </div>
          </a>
          <span class="pkg-info">Paket: <code>com.xapi.polydev</code></span>
        </div>
      </div>

      <!-- FEATURES ROW -->
      <div class="poly-grid">
        <div v-for="h in HIGHLIGHTS" :key="h.title" class="poly-item">
          <div class="pi-ic"><Icon :name="h.icon" /></div>
          <div>
            <h4>{{ h.title }}</h4>
            <p>{{ h.desc }}</p>
          </div>
        </div>
      </div>

      <!-- COMPACT TERMINAL SNAPSHOT -->
      <div class="poly-terminal-box">
        <div class="pt-bar">
          <span class="pt-dot red"></span><span class="pt-dot yellow"></span><span class="pt-dot green"></span>
          <span class="pt-title">Alpine Linux Terminal · Node.js 20 & Python 3.11</span>
        </div>
        <pre class="pt-code"><code><span class="c-prompt">polydev@phone:~/project$</span> npm run dev
<span class="c-info">&gt; app@1.0.0 dev: node server.js</span>
<span class="c-ok">🚀 Server http://localhost:3000 da ishga tushdi!</span>
<span class="c-tip">⚡ Live Preview faol · Vercel / Cloudflare 1-tap deploy tayyor</span></code></pre>
      </div>

      <!-- USE IN CLASS NOTE -->
      <div class="poly-foot-note">
        <Icon name="lightbulb" />
        <span><b>O'quvchilar va mentorlar uchun:</b> Noutbuk yo'q paytda ham dars amaliyotlarini to'g'ridan-to'g'ri telefonda yozib sinab ko'rish imkoniyati.</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.poly-compact {
  padding-bottom: 30px;
}
.poly-card {
  background: linear-gradient(180deg, var(--ax-card-hi), var(--ax-card));
  border: 1px solid var(--ax-line);
  border-radius: 20px;
  padding: 24px;
  box-shadow: var(--ax-shadow);
}
.poly-header {
  display: flex;
  align-items: center;
  gap: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--ax-line);
  flex-wrap: wrap;
}
.poly-app-icon {
  width: 72px;
  height: 72px;
  border-radius: 16px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.1);
  flex: none;
}
.poly-meta {
  flex: 1;
  min-width: 260px;
}
.poly-tag-row {
  display: flex;
  gap: 8px;
  margin-bottom: 6px;
}
.poly-chip {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 999px;
  background: rgba(88, 166, 255, 0.15);
  color: var(--vp-c-brand-1);
}
.poly-chip.free {
  background: rgba(76, 199, 127, 0.15);
  color: #4cc77f;
}
.poly-title {
  font-size: 1.5rem;
  font-weight: 800;
  margin: 0 0 6px;
  line-height: 1.2;
  border: 0;
  padding: 0;
  color: var(--vp-c-text-1);
}
.poly-sub {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.45;
  color: var(--vp-c-text-2);
}
.poly-cta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
  flex: none;
}
.btn-gp {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 8px 18px;
  background: #000;
  color: #fff !important;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  text-decoration: none !important;
  transition: transform 0.15s, box-shadow 0.15s;
}
.btn-gp:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(42, 109, 244, 0.35);
}
.gp-svg {
  width: 22px;
  height: 22px;
  flex: none;
}
.gp-lbl {
  display: block;
  font-size: 0.62rem;
  text-transform: uppercase;
  opacity: 0.8;
  line-height: 1;
}
.gp-name {
  display: block;
  font-size: 0.95rem;
  font-weight: 700;
  line-height: 1.1;
}
.pkg-info {
  font-size: 0.72rem;
  color: var(--vp-c-text-3);
}

.poly-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  padding: 20px 0;
}
.poly-item {
  display: flex;
  gap: 12px;
  align-items: flex-start;
}
.pi-ic {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: rgba(88, 166, 255, 0.12);
  color: var(--vp-c-brand-1);
  flex: none;
}
.poly-item h4 {
  margin: 0 0 3px;
  font-size: 0.92rem;
  font-weight: 700;
  border: 0;
  padding: 0;
  color: var(--vp-c-text-1);
}
.poly-item p {
  margin: 0;
  font-size: 0.82rem;
  line-height: 1.4;
  color: var(--vp-c-text-2);
}

.poly-terminal-box {
  background: #141414;
  border: 1px solid #2a2a2a;
  border-radius: 12px;
  overflow: hidden;
  margin-top: 4px;
}
.pt-bar {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  background: #1f1f1f;
  border-bottom: 1px solid #2a2a2a;
}
.pt-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
.pt-dot.red { background: #ff5f56; }
.pt-dot.yellow { background: #ffbd2e; }
.pt-dot.green { background: #27c93f; }
.pt-title {
  margin-left: 8px;
  font-size: 0.72rem;
  color: #888;
  font-family: monospace;
}
.pt-code {
  margin: 0;
  padding: 10px 14px;
  font-size: 0.8rem;
  line-height: 1.5;
  font-family: ui-monospace, Consolas, monospace;
  color: #ddd;
  background: transparent;
}
.c-prompt { color: #4cc77f; }
.c-info { color: #58a6ff; }
.c-ok { color: #89d185; }
.c-tip { color: #e5c07b; }

.poly-foot-note {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 16px;
  padding: 10px 14px;
  border-radius: 10px;
  background: rgba(88, 166, 255, 0.08);
  border: 1px solid rgba(88, 166, 255, 0.2);
  font-size: 0.82rem;
  color: var(--vp-c-text-2);
}
.poly-foot-note .ic {
  color: var(--vp-c-brand-1);
}

@media (max-width: 768px) {
  .poly-header {
    flex-direction: column;
    align-items: flex-start;
  }
  .poly-cta {
    align-items: flex-start;
    width: 100%;
  }
  .btn-gp {
    width: 100%;
    justify-content: center;
  }
}
</style>
