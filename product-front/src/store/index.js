import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'
import getters from './getters'
import settings  from './modules/settings'


Vue.use(Vuex)

const store = new Vuex.Store({
    modules: {
        user,
        settings
    },
    getters
})


export default store