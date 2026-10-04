<script setup lang="ts">
import { withBase } from 'vitepress'
defineProps<{ items: { t: string; l?: string }[] }>()
</script>

<template>
  <nav class="crumbs" aria-label="Yo'l">
    <template v-for="(c, i) in items" :key="i">
      <a v-if="c.l" :href="withBase(c.l)">{{ c.t }}</a>
      <span v-else>{{ c.t }}</span>
      <span v-if="i < items.length - 1" class="sep">›</span>
    </template>
  </nav>
</template>
