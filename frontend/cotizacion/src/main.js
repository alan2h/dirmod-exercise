import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import {routes} from './routes'
axios.defaults.baseURL = 'http://127.0.0.1:8000/'

//Bootstrap
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
//router
Vue.use(VueRouter)
//axios
Vue.use(VueAxios, axios)

const router = new VueRouter({
  routes // short for `routes: routes`
})

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
