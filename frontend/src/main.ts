import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/reset.css'
import './assets/styles/variables.css'
import App from './App.vue'
import LandingView from './views/LandingView.vue'
import PlanView from './views/Home.vue'
import PlaceholderView from './views/PlaceholderView.vue'
import Result from './views/Result.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Landing',
      component: LandingView
    },
    {
      path: '/plan',
      name: 'Plan',
      component: PlanView
    },
    {
      path: '/result',
      name: 'Result',
      component: Result
    }
  ]
})

const app = createApp(App)

app.use(router)
app.use(Antd)

app.mount('#app')

