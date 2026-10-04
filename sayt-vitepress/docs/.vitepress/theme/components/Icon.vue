<script setup lang="ts">
import { withBase } from 'vitepress'
defineProps<{ name: string }>()
</script>

<template>
  <span class="ic" :style="{ '--m': `url(${withBase('/ikonlar/' + name + '.svg')})` }" aria-hidden="true"></span>
</template>
