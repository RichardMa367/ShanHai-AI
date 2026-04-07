<template>
  <div class="placeholder-page">
    <div class="placeholder-box">
      <h1>{{ title }}</h1>
      <p>{{ description }}</p>
      <a-button type="default" class="back-btn" @click="goHome">返回首页</a-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const goHome = () => router.push('/')
</script>

<style scoped>
.placeholder-page {
  min-height: calc(100vh - 140px);
  display: grid;
  place-items: center;
}

.placeholder-box {
  width: min(560px, 92%);
  background: var(--surface-bg);
  border: 1px solid var(--border-default);
  border-radius: 12px;
  padding: 40px 24px;
  text-align: center;
}

.placeholder-box h1 {
  margin: 0 0 10px;
  color: var(--text-primary);
}

.placeholder-box p {
  margin: 0 0 20px;
  color: var(--text-secondary);
}

.back-btn {
  border-radius: 12px;
  border: 1px solid var(--border-default);
  box-shadow: none;
}
</style>
