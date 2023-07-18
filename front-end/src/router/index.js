import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import EditTransaction from '../components/EditTransaction.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomePage },
    { path: '/edit/:id', component: EditTransaction }
  ]
})

export default router
