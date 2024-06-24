import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css';
import "@/router/permiss_router.js"; // permission control
import "@/assets/icon/iconfont"
import Avue from '@smallwei/avue';
import '@smallwei/avue/lib/index.css';
import axios from 'axios'

Vue.use(Element, {
  size:  'medium' // set element-ui default size
})

Vue.config.productionTip = false
Vue.use(Avue,{axios})

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
