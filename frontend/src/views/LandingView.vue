<template>
  <div class="landing-page">
    <section class="hero-section">
      <div class="hero-inner">
        <div class="icon-wrapper">
        <span class="icon">🚅</span>
        </div>
        <h1 class="hero-title">山海智行</h1>
        <p class="hero-subtitle">AI 规划山海路，轻松奔赴每一处风景</p>
        <div class="hero-actions">
          <a-button type="primary" size="large" class="hero-btn-primary" @click="goPlan">
            开始规划行程
          </a-button>
        </div>
      </div>
    </section>

    <section class="features-section">
      <div class="section-inner features-grid">
        <div class="feature-item">
          <div class="feature-icon">💡</div>
          <h3>AI 智能规划</h3>
          <p>根据偏好自动生成多日行程与预算建议。</p>
        </div>
        <div class="feature-item">
          <div class="feature-icon">🎧</div>
          <h3>AI 导游伴行</h3>
          <p>行中语音讲解与路线提示，旅途更省心。</p>
        </div>
        <div class="feature-item">
          <div class="feature-icon">🌍</div>
          <h3>旅行社区</h3>
          <p>发现目的地灵感，查看真实游玩经验。</p>
        </div>
      </div>
    </section>

    <section class="destinations-section">
      <div class="section-inner">
        <h2 class="section-title">热门目的地</h2>
        <div class="destination-scroll">
          <button
            v-for="city in cities"
            :key="city"
            class="city-chip"
            @click="goPlanWithCity(city)"
            type="button"
          >
            <span>{{ city }}</span>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
const cities = ['北京', '上海', '杭州', '成都', '重庆', '西安']

const goPlan = () => router.push('/plan')
const goExplore = () => router.push('/explore')
const goPlanWithCity = (city: string) => router.push({ path: '/plan', query: { city } })
</script>

<style scoped>
.landing-page {
  min-height: calc(100vh - 140px);
}

.icon-wrapper {
  margin-bottom: 20px;
}

.icon {
  font-size: 80px;
  display: inline-block;
  animation: bounce 2s infinite;
}

.section-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 12px;
}

.hero-section {
  background: var(--bg-gradient-main);
  border: 1px solid var(--border-default);
  border-radius: 12px;
  padding: 92px 20px;
}

.hero-inner {
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

.hero-title {
  margin: 0 0 18px;
  color: var(--text-primary);
  font-size: 54px;
  line-height: 1.15;
}

.hero-subtitle {
  margin: 0 auto 30px;
  color: var(--text-secondary);
  font-size: 20px;
}

.hero-actions {
  display: flex;
  justify-content: center;
  gap: 14px;
  flex-wrap: wrap;
}

.hero-btn-primary {
  height: 46px;
  border-radius: 12px;
  border: 1px solid var(--color-blue-accent);
  background: var(--color-blue-accent);
  box-shadow: none;
}

.hero-btn-secondary {
  height: 46px;
  border-radius: 12px;
  border: 1px solid var(--border-default);
  color: var(--text-primary);
  background: var(--surface-bg);
  box-shadow: none;
}

.features-section {
  background: var(--surface-bg);
  margin-top: 26px;
  padding: 54px 0;
  border: 1px solid var(--border-default);
  border-radius: 12px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 30px;
}

.feature-item {
  text-align: center;
}

.feature-icon {
  font-size: 36px;
  margin-bottom: 10px;
}

.feature-item h3 {
  margin: 0 0 8px;
  color: var(--text-primary);
  font-size: 22px;
}

.feature-item p {
  margin: 0;
  color: var(--text-secondary);
  font-size: 15px;
}

.destinations-section {
  margin-top: 26px;
  background: var(--surface-bg);
  border: 1px solid var(--border-default);
  border-radius: 12px;
  padding: 34px 0 36px;
}

.section-title {
  margin: 0 0 18px;
  color: var(--text-primary);
  font-size: 28px;
}

.destination-scroll {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  padding-bottom: 8px;
}

.city-chip {
  min-width: 140px;
  height: 74px;
  border-radius: 12px;
  border: 1px solid var(--border-default);
  background: linear-gradient(135deg, var(--color-blue-100) 0%, var(--color-green-100) 100%);
  color: var(--text-primary);
  font-size: 20px;
  font-weight: 600;
  cursor: pointer;
}

.city-chip:hover {
  border-color: var(--color-green-200);
}

@media (max-width: 900px) {
  .hero-section {
    padding: 72px 18px;
  }

  .hero-title {
    font-size: 40px;
  }

  .hero-subtitle {
    font-size: 18px;
  }

  .features-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .section-title {
    font-size: 24px;
  }
}
</style>
