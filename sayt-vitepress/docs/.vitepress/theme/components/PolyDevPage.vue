<script setup lang="ts">
import { ref } from 'vue'
import { withBase } from 'vitepress'
import Icon from './Icon.vue'
import Crumbs from './Crumbs.vue'

const PLAY_STORE_URL = 'https://play.google.com/store/apps/details?id=com.xapi.polydev'

const activeTab = ref<'code' | 'ai' | 'terminal' | 'preview'>('code')

const FEATURES = [
  {
    icon: 'bot',
    title: "O'rnatilgan AI Agent",
    desc: "Oddiy chat emas: agent loyihangiz fayllarini tushunadi, yangi fayllar ochadi, xatolarni tuzatadi va to'liq refaktoring qiladi."
  },
  {
    icon: 'smartphone',
    title: "To'liq Mobil IDE",
    desc: "Fayllar daraxti, bir vaqtda ko'p tablar, tezkor sintaksisni yoritish (Syntax Highlighting) va xatolarni terish vaqtidayoq ko'rsatish."
  },
  {
    icon: 'terminal',
    title: "Haqiqiy Linux Terminal (Alpine)",
    desc: "Telefonda to'laqonli Linux muhiti: Node.js, npm, Python, PHP, Go o'rnatilgan. Hech qanday SSH yoki tashqi serverlarsiz ishlaydi."
  },
  {
    icon: 'play',
    title: "Jonli Veb-Preview & API Tester",
    desc: "Loyihangiz qanday ishlayotganini dasturdan chiqmasdan real vaqtda ko'ring. Backend API'larni sinash uchun HTTP tester ham mavjud."
  },
  {
    icon: 'git-branch',
    title: "Git va GitHub Integratsiyasi",
    desc: "Kommitlar qilish, branchlar yaratish, git tarixini ko'zdan kechirish va loyihani to'g'ridan-to'g'ri GitHub repozitoriyga yuklash."
  },
  {
    icon: 'rocket',
    title: "1-Bosishda Bepul Deploy",
    desc: "Vercel va Cloudflare Pages ga bir bosishda saytingizni internetga chiqaring va do'stlaringizga jonli havola ulashing."
  },
  {
    icon: 'layers',
    title: "20+ Tayyor Texnologiya Steklari",
    desc: "React, Vue, Svelte, Next.js, Django, FastAPI, Express, NestJS, Telegram va Discord botlar, Phaser o'yinlari va boshqalar."
  },
  {
    icon: 'zap',
    title: "AI Modelini Erkin Tanlash",
    desc: "O'rnatilgan bepul AI dan foydalaning yoki o'zingizning API kalitingizni (OpenAI GPT-4o, Anthropic Claude, Google Gemini) ulang."
  }
]

const STACKS = [
  { name: 'React / Next.js', tag: 'Web & Front-end', color: '#61dafb' },
  { name: 'Vue / Nuxt', tag: 'Front-end', color: '#42b883' },
  { name: 'FastAPI / Django', tag: 'Python Back-end', color: '#009688' },
  { name: 'Express / Node.js', tag: 'JavaScript Server', color: '#68a063' },
  { name: 'Telegram Botlar', tag: 'Aiogram / Telegraf', color: '#2aabee' },
  { name: 'Phaser / Three.js', tag: 'Game Dev & 3D', color: '#e02347' },
  { name: 'PHP / Laravel', tag: 'Veb dasturlash', color: '#ff2d20' },
  { name: 'Go (Golang)', tag: 'Mikroservislar', color: '#00add8' },
]
</script>

<template>
  <div class="axv poly-page">
    <Crumbs :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'PolyDev (Android)' }]" />

    <!-- HERO SECTION -->
    <header class="poly-hero">
      <div class="hero-left">
        <div class="app-badge">
          <span class="pulse-dot"></span>
          <span>Mobil Dasturlash Studiyasi</span>
        </div>
        <h1 class="app-title">PolyDev: AI Coding Agent</h1>
        <p class="app-tagline">
          Telefoningizni to'liq dasturlash laboratoriyasiga aylantiring. 
          O'rnatilgan AI agent, Linux terminali, Git va 1-bosishda internetga chiqarish — kompyuter talab qilinmaydi!
        </p>

        <div class="hero-badges">
          <span class="h-badge"><Icon name="smartphone" /> Android 8.0+</span>
          <span class="h-badge"><Icon name="bot" /> O'rnatilgan AI</span>
          <span class="h-badge"><Icon name="terminal" /> Alpine Linux</span>
          <span class="h-badge"><Icon name="rocket" /> 1-Tap Deploy</span>
        </div>

        <div class="hero-actions">
          <a :href="PLAY_STORE_URL" target="_blank" rel="noopener" class="btn-play">
            <svg class="gp-icon" viewBox="0 0 24 24">
              <path fill="#EA4335" d="M3.6 1.7L13.7 12 3.6 22.3c-.4-.4-.6-1.1-.6-1.9V3.6c0-.8.2-1.5.6-1.9z"/>
              <path fill="#FBBC04" d="M17.1 8.6L13.7 12l3.4 3.4 3.9-2.2c1.1-.6 1.1-1.7 0-2.3l-3.9-2.3z"/>
              <path fill="#4285F4" d="M3.6 1.7l10.1 10.3 3.4-3.4L5.6 1c-.8-.5-1.5-.2-2 .7z"/>
              <path fill="#34A853" d="M3.6 22.3l13.5-7.7-3.4-3.4-10.1 10.3c.5.9 1.2 1.2 2 .8z"/>
            </svg>
            <div>
              <span class="gp-sub">Yuklab olish</span>
              <span class="gp-main">Google Play</span>
            </div>
          </a>

          <a href="#simulator" class="btn-sec">
            <Icon name="play" /> Imkoniyatlarni ko'rish
          </a>
        </div>
      </div>

      <div class="hero-right">
        <div class="icon-pod">
          <div class="icon-glow"></div>
          <img :src="withBase('/polydev-icon.png')" alt="PolyDev Icon" class="poly-icon-big" />
          <div class="float-chip fc-1">
            <Icon name="bot" />
            <span>AI Auto-fix</span>
          </div>
          <div class="float-chip fc-2">
            <Icon name="terminal" />
            <span>$ node app.js</span>
          </div>
        </div>
      </div>
    </header>

    <!-- INTERACTIVE PHONE IDE SIMULATOR -->
    <section id="simulator" class="sim-sec">
      <div class="sec-head">
        <h2>Dastur interfeysi qanday ishlaydi?</h2>
        <p>Telefonda kod yozish, konsolda ishga tushirish va AI bilan muloqot qilish jarayoni</p>
      </div>

      <div class="phone-mockup">
        <div class="phone-frame">
          <div class="phone-top-bar">
            <span class="notch"></span>
            <span class="cam"></span>
          </div>

          <div class="ide-screen">
            <!-- IDE HEADER -->
            <div class="ide-header">
              <div class="ide-brand">
                <img :src="withBase('/polydev-icon.png')" alt="" class="ide-logo-mini" />
                <span>PolyDev IDE</span>
              </div>
              <div class="ide-tabs-nav">
                <button :class="{ active: activeTab === 'code' }" @click="activeTab = 'code'">
                  <Icon name="code" /> Kod
                </button>
                <button :class="{ active: activeTab === 'ai' }" @click="activeTab = 'ai'">
                  <Icon name="bot" /> AI Agent
                </button>
                <button :class="{ active: activeTab === 'terminal' }" @click="activeTab = 'terminal'">
                  <Icon name="terminal" /> Terminal
                </button>
                <button :class="{ active: activeTab === 'preview' }" @click="activeTab = 'preview'">
                  <Icon name="globe" /> Preview
                </button>
              </div>
            </div>

            <!-- TAB 1: CODE EDITOR -->
            <div v-if="activeTab === 'code'" class="ide-body tab-code">
              <div class="file-crumb">📁 src / <b>server.js</b></div>
              <pre class="code-view"><code><span class="c-kw">import</span> express <span class="c-kw">from</span> <span class="c-str">'express'</span>;
<span class="c-kw">const</span> app = express();
<span class="c-kw">const</span> PORT = <span class="c-num">3000</span>;

app.get(<span class="c-str">'/api/salom'</span>, (req, res) =&gt; {
  res.json({
    xabar: <span class="c-str">"Muhammad al-Xorazmiy vorislari!"</span>,
    manba: <span class="c-str">"PolyDev Phone IDE"</span>,
    vaqt: <span class="c-kw">new</span> Date().toISOString()
  });
});

app.listen(PORT, () =&gt; {
  console.log(<span class="c-str">`🚀 Server http://localhost:${PORT} da ishga tushdi!`</span>);
});</code></pre>
            </div>

            <!-- TAB 2: AI AGENT -->
            <div v-else-if="activeTab === 'ai'" class="ide-body tab-ai">
              <div class="chat-msg user">
                <div class="c-author">👤 Siz</div>
                <div class="c-bubble">API ga yangi foydalanuvchi qo'shish uchun POST /api/user yo'nalishini qo'shib ber.</div>
              </div>

              <div class="chat-msg bot">
                <div class="c-author">🤖 PolyDev AI Agent</div>
                <div class="c-bubble">
                  Buyurtmangiz tayyor! <code>src/server.js</code> fayliga quyidagi qatorlar qo'shildi va sintaksis tekshirildi:
                  <div class="diff-block">
                    <span class="diff-add">+ app.post('/api/user', (req, res) =&gt; {</span><br/>
                    <span class="diff-add">+   const { name } = req.body;</span><br/>
                    <span class="diff-add">+   res.status(201).json({ status: 'ok', name });</span><br/>
                    <span class="diff-add">+ });</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- TAB 3: TERMINAL -->
            <div v-else-if="activeTab === 'terminal'" class="ide-body tab-term">
              <div class="term-log">
                <span class="t-green">polydev@phone:~/my-project$</span> node --version<br/>
                v20.12.2<br/>
                <span class="t-green">polydev@phone:~/my-project$</span> python3 --version<br/>
                Python 3.11.8 (Alpine Linux)<br/>
                <span class="t-green">polydev@phone:~/my-project$</span> npm run dev<br/>
                <span class="t-blue">&gt; my-project@1.0.0 dev</span><br/>
                <span class="t-blue">&gt; node server.js</span><br/>
                <br/>
                <span class="t-green">🚀 Server http://localhost:3000 da ishga tushdi!</span><br/>
                <span class="t-yellow">⚡ Live Preview faollashtirildi</span><br/>
                <span class="cursor-blink">█</span>
              </div>
            </div>

            <!-- TAB 4: PREVIEW -->
            <div v-else-if="activeTab === 'preview'" class="ide-body tab-prev">
              <div class="prev-bar">
                <span class="dot d-r"></span><span class="dot d-y"></span><span class="dot d-g"></span>
                <span class="url">http://localhost:3000/api/salom</span>
              </div>
              <div class="prev-content">
                <div class="json-card">
                  <div class="jc-title">JSON Response (HTTP 200 OK)</div>
                  <pre class="json-pre">{
  "xabar": "Muhammad al-Xorazmiy vorislari!",
  "manba": "PolyDev Phone IDE",
  "vaqt": "2026-10-19T07:40:00.000Z"
}</pre>
                </div>
                <div class="prev-tip">
                  ✅ Sayt telefondan chiqmasdan ishlamoqda. Birgina tugma bilan Cloudflare Pages yoki Vercel ga yuklashingiz mumkin.
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <!-- FEATURES GRID -->
    <section class="feat-sec">
      <div class="sec-head">
        <h2>Nima uchun PolyDev?</h2>
        <p>Maktab o'quvchilari, mentorlar va mobil dasturchilar uchun qulayliklar</p>
      </div>

      <div class="feat-grid">
        <div v-for="f in FEATURES" :key="f.title" class="f-card">
          <div class="f-ic"><Icon :name="f.icon" /></div>
          <h3>{{ f.title }}</h3>
          <p>{{ f.desc }}</p>
        </div>
      </div>
    </section>

    <!-- STACKS SECTION -->
    <section class="stacks-sec">
      <div class="sec-head">
        <h2>20+ Qo'llab-quvvatlanadigan Steklar</h2>
        <p>Telefonda istalgan mashhur freymvork va dasturlash tillarini ishga tushiring</p>
      </div>

      <div class="stacks-wrap">
        <div v-for="s in STACKS" :key="s.name" class="s-badge">
          <span class="s-dot" :style="{ backgroundColor: s.color }"></span>
          <b>{{ s.name }}</b>
          <span class="s-tag">{{ s.tag }}</span>
        </div>
      </div>
    </section>

    <!-- HOW TO USE IN LESSONS -->
    <section class="usage-sec">
      <div class="sec-head">
        <h2>Darslarda qanday foydalanish mumkin?</h2>
        <p>Kompyuter yo'q paytda ham bilim olishni to'xtatmang</p>
      </div>

      <div class="usage-cards">
        <div class="u-card">
          <div class="u-num">1</div>
          <h3>Uyga vazifalarni bajarish</h3>
          <p>Yo'lda yoki noutbuk bo'lmagan sharoitda o'tilgan dars kodlarini telefonda yozib, natijasini tekshiring.</p>
        </div>
        <div class="u-card">
          <div class="u-num">2</div>
          <h3>AI yordamida xatolarni o'rganish</h3>
          <p>Kodingizda xato chiqsa, PolyDev ichidagi AI agentdan xato sababini va uni to'g'rilash yo'lini so'rang.</p>
        </div>
        <div class="u-card">
          <div class="u-num">3</div>
          <h3>Portfolioni internetga chiqarish</h3>
          <p>1-bosishda Cloudflare Pages yoki Vercel ga bepul deploy qilib, tayyor saytingiz havolasini o'qituvchiga yuboring.</p>
        </div>
      </div>
    </section>

    <!-- DOWNLOAD CTA -->
    <section class="cta-box">
      <div class="cta-inner">
        <img :src="withBase('/polydev-icon.png')" alt="" class="cta-logo" />
        <h2>PolyDev ilovasini hoziroq o'rnating</h2>
        <p>Android smartfoningizda to'liq dasturlash tajribasini sinab ko'ring</p>

        <a :href="PLAY_STORE_URL" target="_blank" rel="noopener" class="btn-play-lg">
          <svg class="gp-icon-lg" viewBox="0 0 24 24">
            <path fill="#EA4335" d="M3.6 1.7L13.7 12 3.6 22.3c-.4-.4-.6-1.1-.6-1.9V3.6c0-.8.2-1.5.6-1.9z"/>
            <path fill="#FBBC04" d="M17.1 8.6L13.7 12l3.4 3.4 3.9-2.2c1.1-.6 1.1-1.7 0-2.3l-3.9-2.3z"/>
            <path fill="#4285F4" d="M3.6 1.7l10.1 10.3 3.4-3.4L5.6 1c-.8-.5-1.5-.2-2 .7z"/>
            <path fill="#34A853" d="M3.6 22.3l13.5-7.7-3.4-3.4-10.1 10.3c.5.9 1.2 1.2 2 .8z"/>
          </svg>
          <div>
            <span class="gp-sub">Google Play'da ochish</span>
            <span class="gp-main">com.xapi.polydev</span>
          </div>
        </a>

        <div class="cta-meta">
          <span>Paket: <code>com.xapi.polydev</code></span>
          <span>•</span>
          <span>Ishlab chiquvchi: XAPI</span>
          <span>•</span>
          <span>Hajmi: Yengil va tezkor</span>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.poly-page {
  padding-bottom: 60px;
}

/* HERO */
.poly-hero {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 40px;
  align-items: center;
  padding: 30px 24px;
  background: linear-gradient(135deg, rgba(88, 166, 255, 0.08), rgba(197, 134, 192, 0.05));
  border: 1px solid var(--vp-c-divider);
  border-radius: 24px;
  margin-bottom: 40px;
}
.app-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 14px;
  background: rgba(88, 166, 255, 0.15);
  border: 1px solid rgba(88, 166, 255, 0.3);
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--vp-c-brand-1);
  margin-bottom: 14px;
}
.pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--vp-c-brand-1);
  box-shadow: 0 0 10px var(--vp-c-brand-1);
  animation: ax-pulse 1.8s infinite;
}
.app-title {
  font-size: 2.3rem;
  font-weight: 800;
  line-height: 1.2;
  margin: 0 0 12px;
  background: linear-gradient(135deg, #fff, #9cdcfe);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
[data-theme="light"] .app-title {
  background: linear-gradient(135deg, #1f1f1f, #0066b8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.app-tagline {
  font-size: 1.05rem;
  line-height: 1.6;
  color: var(--vp-c-text-2);
  margin: 0 0 20px;
}
.hero-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 24px;
}
.h-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 12px;
  border-radius: 8px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  font-size: 0.82rem;
  color: var(--vp-c-text-1);
  font-weight: 500;
}
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
}
.btn-play {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 10px 22px;
  background: #000;
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 14px;
  text-decoration: none;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.3);
}
.btn-play:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(42, 109, 244, 0.4);
}
.gp-icon {
  width: 28px;
  height: 28px;
  flex: none;
}
.gp-sub {
  display: block;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  opacity: 0.8;
}
.gp-main {
  display: block;
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1.1;
}
.btn-sec {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border-radius: 14px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
  font-weight: 600;
  text-decoration: none;
  transition: background 0.2s;
}
.btn-sec:hover {
  background: var(--vp-c-bg-mute);
  color: var(--vp-c-brand-1);
}

.icon-pod {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 240px;
}
.icon-glow {
  position: absolute;
  width: 180px;
  height: 180px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(88, 166, 255, 0.35), transparent 70%);
  filter: blur(20px);
}
.poly-icon-big {
  position: relative;
  width: 140px;
  height: 140px;
  border-radius: 28px;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4);
  z-index: 2;
  border: 2px solid rgba(255, 255, 255, 0.1);
}
.float-chip {
  position: absolute;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 12px;
  font-size: 0.8rem;
  font-weight: 600;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
  z-index: 3;
}
.fc-1 {
  top: 15px;
  right: 10px;
  color: #4cc77f;
}
.fc-2 {
  bottom: 15px;
  left: 10px;
  color: #58a6ff;
  font-family: monospace;
}

/* SIMULATOR */
.sim-sec {
  margin: 50px 0;
}
.sec-head {
  text-align: center;
  margin-bottom: 28px;
}
.sec-head h2 {
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0 0 8px;
  border: none;
  padding: 0;
}
.sec-head p {
  color: var(--vp-c-text-2);
  font-size: 1rem;
  margin: 0;
}
.phone-mockup {
  max-width: 680px;
  margin: 0 auto;
}
.phone-frame {
  background: #141414;
  border: 4px solid #333;
  border-radius: 36px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}
.phone-top-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 8px 0 4px;
  background: #141414;
}
.notch {
  width: 70px;
  height: 5px;
  border-radius: 99px;
  background: #2a2a2a;
}
.ide-screen {
  background: #1e1e1e;
  color: #d4d4d4;
  min-height: 400px;
}
.ide-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
  background: #252526;
  border-bottom: 1px solid #333;
  flex-wrap: wrap;
  gap: 10px;
}
.ide-brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  font-weight: 700;
  color: #fff;
}
.ide-logo-mini {
  width: 22px;
  height: 22px;
  border-radius: 6px;
}
.ide-tabs-nav {
  display: flex;
  gap: 4px;
  background: #1e1e1e;
  padding: 3px;
  border-radius: 8px;
  border: 1px solid #3c3c3c;
}
.ide-tabs-nav button {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border: none;
  background: transparent;
  color: #888;
  font-size: 0.78rem;
  font-weight: 600;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s;
}
.ide-tabs-nav button.active {
  background: var(--vp-c-brand-1);
  color: #fff;
}
.ide-body {
  padding: 16px;
  font-family: ui-monospace, Consolas, monospace;
}
.file-crumb {
  font-size: 0.75rem;
  color: #888;
  margin-bottom: 10px;
  padding-bottom: 6px;
  border-bottom: 1px solid #2a2a2a;
}
.code-view {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.6;
  overflow-x: auto;
}
.c-kw { color: #569cd6; font-weight: bold; }
.c-str { color: #ce9178; }
.c-num { color: #b5cea8; }

.chat-msg {
  margin-bottom: 14px;
}
.c-author {
  font-size: 0.75rem;
  color: #888;
  margin-bottom: 4px;
}
.c-bubble {
  padding: 10px 14px;
  border-radius: 12px;
  font-size: 0.85rem;
  line-height: 1.5;
}
.chat-msg.user .c-bubble {
  background: rgba(88, 166, 255, 0.15);
  border: 1px solid rgba(88, 166, 255, 0.3);
}
.chat-msg.bot .c-bubble {
  background: #252526;
  border: 1px solid #3c3c3c;
}
.diff-block {
  margin-top: 8px;
  padding: 8px 10px;
  background: #181818;
  border-radius: 6px;
  border-left: 3px solid #4cc77f;
}
.diff-add { color: #89d185; }

.term-log {
  font-size: 0.85rem;
  line-height: 1.6;
}
.t-green { color: #4cc77f; }
.t-blue { color: #58a6ff; }
.t-yellow { color: #dcdcaa; }
.cursor-blink { animation: ax-blink 1s infinite; }

.prev-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: #252526;
  border-radius: 8px;
  margin-bottom: 14px;
}
.dot { width: 8px; height: 8px; border-radius: 50%; }
.d-r { background: #ff5f56; }
.d-y { background: #ffbd2e; }
.d-g { background: #27c93f; }
.prev-bar .url {
  font-size: 0.75rem;
  color: #aaa;
  margin-left: 8px;
}
.json-card {
  background: #252526;
  border: 1px solid #3c3c3c;
  border-radius: 10px;
  padding: 12px;
}
.jc-title {
  font-size: 0.75rem;
  font-weight: 700;
  color: #4cc77f;
  margin-bottom: 8px;
}
.json-pre {
  margin: 0;
  font-size: 0.82rem;
  color: #9cdcfe;
}
.prev-tip {
  margin-top: 14px;
  font-size: 0.8rem;
  color: var(--vp-c-text-2);
  line-height: 1.4;
}

/* FEATURES GRID */
.feat-sec {
  margin: 60px 0;
}
.feat-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}
.f-card {
  padding: 22px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 18px;
  transition: transform 0.2s, border-color 0.2s;
}
.f-card:hover {
  transform: translateY(-3px);
  border-color: var(--vp-c-brand-1);
}
.f-ic {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: rgba(88, 166, 255, 0.12);
  color: var(--vp-c-brand-1);
  margin-bottom: 14px;
}
.f-card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  margin: 0 0 8px;
  border: none;
  padding: 0;
}
.f-card p {
  font-size: 0.9rem;
  line-height: 1.5;
  color: var(--vp-c-text-2);
  margin: 0;
}

/* STACKS */
.stacks-sec {
  margin: 60px 0;
}
.stacks-wrap {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
}
.s-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: var(--vp-c-bg);
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  font-size: 0.88rem;
}
.s-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
}
.s-tag {
  font-size: 0.72rem;
  color: var(--vp-c-text-3);
  padding-left: 4px;
  border-left: 1px solid var(--vp-c-divider);
}

/* USAGE */
.usage-sec {
  margin: 60px 0;
}
.usage-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}
.u-card {
  padding: 24px;
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(88, 166, 255, 0.05), rgba(0, 0, 0, 0.02));
  border: 1px solid var(--vp-c-divider);
}
.u-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--vp-c-brand-1);
  color: #fff;
  font-weight: 800;
  margin-bottom: 12px;
}
.u-card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  margin: 0 0 8px;
  border: none;
  padding: 0;
}
.u-card p {
  font-size: 0.9rem;
  color: var(--vp-c-text-2);
  margin: 0;
  line-height: 1.5;
}

/* CTA */
.cta-box {
  margin: 60px 0 20px;
  padding: 40px 24px;
  background: radial-gradient(circle at center, rgba(88, 166, 255, 0.15), transparent 70%), var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 24px;
  text-align: center;
}
.cta-inner {
  max-width: 600px;
  margin: 0 auto;
}
.cta-logo {
  width: 72px;
  height: 72px;
  border-radius: 16px;
  margin: 0 auto 16px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
.cta-box h2 {
  font-size: 1.8rem;
  font-weight: 800;
  margin: 0 0 10px;
  border: none;
  padding: 0;
}
.cta-box p {
  color: var(--vp-c-text-2);
  font-size: 1.05rem;
  margin: 0 0 24px;
}
.btn-play-lg {
  display: inline-flex;
  align-items: center;
  gap: 14px;
  padding: 12px 28px;
  background: #000;
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.25);
  border-radius: 16px;
  text-decoration: none;
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.4);
  transition: transform 0.2s, box-shadow 0.2s;
}
.btn-play-lg:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 32px rgba(42, 109, 244, 0.5);
}
.gp-icon-lg {
  width: 34px;
  height: 34px;
  flex: none;
}
.cta-meta {
  margin-top: 18px;
  display: flex;
  justify-content: center;
  gap: 10px;
  font-size: 0.8rem;
  color: var(--vp-c-text-3);
  flex-wrap: wrap;
}

@keyframes ax-pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.6; }
}
@keyframes ax-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

@media (max-width: 768px) {
  .poly-hero {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .app-badge, .hero-badges, .hero-actions {
    justify-content: center;
  }
  .hero-right {
    order: -1;
  }
}
</style>
