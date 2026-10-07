<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'
import Icon from './Icon.vue'
import Crumbs from './Crumbs.vue'
import TypingTrainer from './TypingTrainer.vue'
import FoundationLab from './FoundationLab.vue'

const { frontmatter } = useData()
const kind = computed(() => frontmatter.value.kind)
const home = computed(() => frontmatter.value.home)
const sinf = computed(() => frontmatter.value.sinf)
const hafta = computed(() => frontmatter.value.hafta)
const dars = computed(() => frontmatter.value.dars)
const pct = (c: { done: number; total: number }) => (c.total ? Math.round((100 * c.done) / c.total) : 0)
</script>

<template>
  <!-- KLAVIATURA TRENAJYORI (STAMINA) -->
  <TypingTrainer v-if="kind === 'trenajyor'" />

  <!-- CS LABORATORIYA -->
  <FoundationLab v-else-if="kind === 'foundation'" />

  <!-- BOSH SAHIFA / MENTOR BOSH SAHIFA -->
  <div v-else-if="kind === 'home' || kind === 'mentor_home'" class="axv">
    <Crumbs v-if="kind === 'mentor_home'" :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'Mentor bo\'limi' }]" />
    <section class="hero">
      <img :src="withBase('/logo.png')" alt="AXV" />
      <h1 class="org">{{ home.org }}</h1>
      <p class="tag">{{ home.tag }}</p>
      <p class="tag2">{{ home.tag2 }}</p>
    </section>

    <!-- INTERAKTIV TRENAJYORLAR VA LABORATORIYALAR -->
    <div v-if="kind === 'home'" class="interactive-tools-banner">
      <a :href="withBase('/trenajyor/')" class="tool-banner-card">
        <span class="tbc-icon"><Icon name="keyboard" /></span>
        <div class="tbc-text">
          <h3>Klaviatura trenajyori</h3>
          <p>10 barmoq bilan tez va xatosiz yozishni o'rganing (ovoz profillari, WPM tezlik va yutuqlar)</p>
        </div>
        <span class="tbc-arrow"><Icon name="arrow-right" /></span>
      </a>

      <a :href="withBase('/foundation/')" class="tool-banner-card lab">
        <span class="tbc-icon"><Icon name="binary" /></span>
        <div class="tbc-text">
          <h3>CS Laboratoriya</h3>
          <p>7 ta interaktiv modul: Ikkilik sanoq, mantiqiy darvozalar, xotira, algoritmlar, saralash va kriptografiya</p>
        </div>
        <span class="tbc-arrow"><Icon name="arrow-right" /></span>
      </a>
    </div>

    <h2 class="sec-title">{{ kind === 'mentor_home' ? 'Sinfni tanlang (Mentor rejasi)' : 'Sinfingizni tanlang' }}</h2>
    <div class="tiles">
      <component
        :is="c.link ? 'a' : 'div'"
        v-for="c in home.classes"
        :key="c.name"
        class="tile"
        :class="{ soon: !c.link }"
        :href="c.link ? withBase(c.link) : undefined"
      >
        <span class="t-ic"><Icon :name="c.icon" /></span>
        <h3>{{ c.name }}</h3>
        <p>{{ c.fan }}</p>
        <template v-if="c.link">
          <div class="prog"><i :style="{ width: pct(c) + '%' }"></i></div>
          <div class="prog-l">{{ c.done }} / {{ c.total }} hafta tayyor</div>
        </template>
        <div v-else class="prog-l">Tez orada</div>
      </component>
    </div>
  </div>

  <!-- SINF: HAFTALIK REJA (O'quvchi / Mentor) -->
  <div v-else-if="kind === 'sinf' || kind === 'mentor_sinf'" class="axv">
    <Crumbs v-if="kind === 'mentor_sinf'" :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'Mentor bo\'limi', l: '/mentor/' }, { t: sinf.name }]" />
    <Crumbs v-else :items="[{ t: 'Bosh sahifa', l: '/' }, { t: sinf.name }]" />
    <header class="page-hero">
      <span class="ph-ic"><Icon :name="sinf.icon" /></span>
      <div>
        <h1>{{ sinf.name }} <span v-if="kind === 'mentor_sinf'" class="badge-mentor">(Mentor)</span></h1>
        <p class="sub">{{ sinf.fan }} {{ kind === 'mentor_sinf' ? '— Mentor dars rejalari va yechimlari' : '' }}</p>
      </div>
    </header>
    <div class="facts">
      <span v-for="f in sinf.facts" :key="f.text" class="fact"><Icon :name="f.icon" />{{ f.text }}</span>
      <span class="fact ok"><Icon name="list-checks" />{{ sinf.open }} / {{ sinf.total }} hafta tayyor</span>
    </div>
    <section v-for="q in sinf.quarters" :key="q.name">
      <div class="q-title">
        <h2>{{ q.name }}</h2>
        <span>{{ q.range }}</span>
      </div>
      <component
        :is="w.link ? 'a' : 'div'"
        v-for="w in q.weeks"
        :key="w.n"
        class="wk"
        :class="{ locked: !w.link }"
        :href="w.link ? withBase(w.link) : undefined"
      >
        <div class="n"><b>{{ w.n }}</b><span>hafta</span></div>
        <div class="wb">
          <div class="bob">{{ w.bob }}</div>
          <ul>
            <li v-for="t in w.topics" :key="t.g"><em>{{ t.g }}-dars</em><span>{{ t.t }}</span></li>
          </ul>
        </div>
        <div class="go"><Icon :name="w.link ? 'chevron-right' : 'lock'" /></div>
      </component>
    </section>
  </div>

  <!-- HAFTA (O'quvchi / Mentor) -->
  <div v-else-if="kind === 'hafta' || kind === 'mentor_hafta'" class="axv">
    <Crumbs v-if="kind === 'mentor_hafta'" :items="[{ t: 'Bosh sahifa', l: '/' }, { t: 'Mentor bo\'limi', l: '/mentor/' }, { t: hafta.sinf.name, l: hafta.sinf.link }, { t: hafta.n + '-hafta' }]" />
    <Crumbs v-else :items="[{ t: 'Bosh sahifa', l: '/' }, { t: hafta.sinf.name, l: hafta.sinf.link }, { t: hafta.n + '-hafta' }]" />
    <header class="l-hero">
      <div class="kick">{{ hafta.bob }}</div>
      <h1>{{ hafta.n }}-hafta <span v-if="kind === 'mentor_hafta'" class="badge-mentor">(Mentor)</span></h1>
      <p class="lead">{{ kind === 'mentor_hafta' ? 'Haftada ' + hafta.lessons.length + ' ta dars. Har bir dars uchun to\'liq mentor rejasi, konspekt, doska rejasi, topshiriq yechimlari va baholash mezonlari.' : 'Haftada ' + hafta.lessons.length + ' ta dars. Slaydlarni oching va darsning o\'quvchi sahifasida qo\'shimcha ma\'lumot hamda topshiriqlarni toping.' }}</p>
    </header>
    <div class="lessons">
      <article v-for="l in hafta.lessons" :key="l.g" class="lsn">
        <a class="lsn-main" :href="withBase(l.link)">
          <div class="n">{{ l.g }}</div>
          <div>
            <h3>{{ l.title }}</h3>
            <p>{{ l.lead }}</p>
          </div>
        </a>
        <div class="lsn-act">
          <a v-if="l.slide" class="btn btn-primary btn-sm" :href="withBase(l.slide)" target="_blank" rel="noopener"><Icon name="play" />Slaydlar</a>
          <a v-if="l.test" class="btn btn-ghost btn-sm" :href="withBase(l.test)" target="_blank" rel="noopener"><Icon name="list-checks" />Test</a>
          <a class="btn btn-ghost btn-sm" :href="withBase(l.link)"><Icon :name="kind === 'mentor_hafta' ? 'graduation-cap' : 'book-open'" />{{ kind === 'mentor_hafta' ? 'Mentor rejasi' : 'Dars sahifasi' }}</a>
        </div>
      </article>
    </div>
    <div v-if="hafta.test" class="btns">
      <a class="btn btn-primary btn-lg" :href="withBase(hafta.test)" target="_blank" rel="noopener"><Icon name="list-checks" />Haftalik test<Icon name="arrow-right" /></a>
    </div>
  </div>

  <!-- DARS (O'quvchi) -->
  <div v-else-if="kind === 'dars'" class="axv">
    <Crumbs
      :items="[
        { t: 'Bosh sahifa', l: '/' },
        { t: dars.sinf.name, l: dars.sinf.link },
        { t: dars.week.n + '-hafta', l: dars.week.link },
        { t: dars.g + '-dars' },
      ]"
    />
    <header class="l-hero">
      <div class="kick">{{ dars.week.n }}-hafta · {{ dars.g }}-dars</div>
      <h1>{{ dars.title }}</h1>
      <p v-if="dars.lead" class="lead">{{ dars.lead }}</p>
      <div class="btns">
        <a v-if="dars.slide" class="btn btn-primary btn-lg" :href="withBase(dars.slide)" target="_blank" rel="noopener">
          <Icon name="play" />Slaydlarni ochish<Icon name="arrow-right" />
        </a>
        <a v-if="dars.test" class="btn btn-ghost btn-lg" :href="withBase(dars.test)" target="_blank" rel="noopener"><Icon name="list-checks" />Dars testi</a>
        <a class="btn btn-ghost btn-lg" :href="withBase(dars.week.link)"><Icon name="layers" />{{ dars.week.n }}-hafta</a>
      </div>
      <nav class="tabs" aria-label="Haftadagi darslar">
        <a v-for="t in dars.tabs" :key="t.g" class="tab" :class="{ on: t.current }" :href="withBase(t.link)">{{ t.g }}-dars</a>
      </nav>
    </header>
  </div>

  <!-- DARS (Mentor) -->
  <div v-else-if="kind === 'mentor_dars'" class="axv">
    <Crumbs
      :items="[
        { t: 'Bosh sahifa', l: '/' },
        { t: 'Mentor bo\'limi', l: '/mentor/' },
        { t: dars.sinf.name, l: dars.sinf.link },
        { t: dars.week.n + '-hafta', l: dars.week.link },
        { t: dars.g + '-dars (Mentor)' },
      ]"
    />
    <header class="l-hero">
      <div class="kick"><Icon name="graduation-cap" /> Mentor dars rejasi va yechimlari · {{ dars.week.n }}-hafta · {{ dars.g }}-dars</div>
      <h1>{{ dars.title }}</h1>
      <p v-if="dars.lead" class="lead">{{ dars.lead }}</p>
      <div class="btns">
        <a v-if="dars.slide" class="btn btn-primary btn-lg" :href="withBase(dars.slide)" target="_blank" rel="noopener">
          <Icon name="play" />Slaydlarni ochish<Icon name="arrow-right" />
        </a>
        <a v-if="dars.test" class="btn btn-ghost btn-lg" :href="withBase(dars.test)" target="_blank" rel="noopener"><Icon name="list-checks" />Dars testi</a>
        <a v-if="dars.student_link" class="btn btn-ghost btn-lg" :href="withBase(dars.student_link)"><Icon name="book-open" />O'quvchi sahifasi</a>
        <a class="btn btn-ghost btn-lg" :href="withBase(dars.week.link)"><Icon name="layers" />{{ dars.week.n }}-hafta (Mentor)</a>
      </div>
      <nav class="tabs" aria-label="Haftadagi darslar">
        <a v-for="t in dars.tabs" :key="t.g" class="tab" :class="{ on: t.current }" :href="withBase(t.link)">{{ t.g }}-dars</a>
      </nav>
    </header>
  </div>
</template>
