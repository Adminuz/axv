<script setup lang="ts">
import { computed } from 'vue'
import { useData, withBase } from 'vitepress'
import Icon from './Icon.vue'

const { frontmatter, theme } = useData()
const dars = computed(() => (frontmatter.value.kind === 'dars' ? frontmatter.value.dars : null))
</script>

<template>
  <div class="axv">
    <nav v-if="dars && (dars.prev || dars.next)" class="pn" aria-label="Darslar">
      <a v-if="dars.prev" class="pn-card prev" :href="withBase(dars.prev.link)">
        <span class="dir"><Icon name="arrow-left" />Oldingi dars</span>
        <strong>{{ dars.prev.g }}-dars</strong>
        <span class="t">{{ dars.prev.title }}</span>
      </a>
      <span v-else></span>
      <a v-if="dars.next" class="pn-card next" :href="withBase(dars.next.link)">
        <span class="dir">Keyingi dars<Icon name="arrow-right" /></span>
        <strong>{{ dars.next.g }}-dars</strong>
        <span class="t">{{ dars.next.title }}</span>
      </a>
      <span v-else></span>
    </nav>
    <footer class="axv-foot">
      <img :src="withBase('/logo.png')" alt="" />
      <span>{{ theme.axvFooter }}</span>
    </footer>
  </div>
</template>
