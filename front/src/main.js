// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueGeolocation from 'vue-browser-geolocation'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'



import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(VueGeolocation)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)



import * as VueGoogleMaps from 'vue2-google-maps'
Vue.use(VueGoogleMaps, {
  load:{
    key:'AIzaSyAqV_sLHkATBLIyXWP5jpBq5pUyLXYiHEA',
    
  },
  installComponents:true
})


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


