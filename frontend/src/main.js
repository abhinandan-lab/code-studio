import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import HomeView from './views/HomeView.vue'
import Codemirror from 'vue-codemirror';
const pinia = createPinia()

const router = createRouter({
  history: createWebHistory(),
  routes: [{ path: '/', component: HomeView }]
})

createApp(App).use(pinia).use(router).use(Codemirror).mount('#app')
