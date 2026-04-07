<template>
  <div id="app">
    <a-layout class="app-shell">
      <a-layout-header class="app-header">
        <div class="header-inner">
          <div class="app-title">
            山海智行
          </div>
          <nav class="top-nav" aria-label="Main Navigation">
            <router-link to="/" class="nav-link">首页</router-link>
            <router-link to="/plan" class="nav-link">规划行程</router-link>
          </nav>
        </div>
      </a-layout-header>
      <a-layout-content class="app-content">
        <router-view />
      </a-layout-content>
      <a-layout-footer class="app-footer">
        山海智行 基于HelloAgents框架
      </a-layout-footer>
    </a-layout>
  </div>
</template>

<script setup lang="ts">
</script>

<style>
html,
body {
  margin: 0;
  padding: 0;
}

#app {
  min-height: 100vh;
  background: var(--bg-gradient-main);
  color: var(--text-primary);
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial,
    'Noto Sans', sans-serif;
}

.app-shell {
  min-height: 100vh;
  background: transparent;
}

.app-header {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(6px);
  border-bottom: 1px solid var(--border-default);
  padding: 0 20px;
  height: auto;
  line-height: normal;
}

.header-inner {
  max-width: 1200px;
  min-height: 68px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.app-title {
  color: var(--text-primary);
  font-size: 22px;
  font-weight: 700;
}

.top-nav {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.nav-link {
  text-decoration: none;
  color: var(--text-secondary);
  border: 1px solid transparent;
  border-radius: 12px;
  padding: 8px 12px;
}

.nav-link:hover {
  color: var(--text-primary);
  background: var(--surface-bg);
  border-color: var(--border-default);
}

.nav-link.router-link-active {
  color: var(--text-primary);
  background: linear-gradient(135deg, var(--color-blue-100) 0%, var(--color-green-100) 100%);
  border-color: var(--border-default);
}

.app-content {
  padding: 32px;
}

.app-footer {
  text-align: center;
  color: var(--text-secondary);
  background: transparent;
  border-top: 1px solid var(--border-default);
}

@media (max-width: 780px) {
  .header-inner {
    padding: 10px 0;
    flex-direction: column;
    align-items: flex-start;
  }

  .app-content {
    padding: 18px;
  }
}
</style>

