import router from '@/router'
import store from '@/store'
import { Message } from 'element-ui'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'
import { getToken } from '@/utils/auth'

NProgress.configure({ showSpinner: false })

const whiteList = ['/login', '/auth-redirect', '/bind', '/register', "/magic", "/qrcode"]

router.beforeEach((to, from, next) => {
    NProgress.start()
    if (getToken()) {
      /* has token*/
      if (to.path === '/login') {
        next({ path: '/' })
        NProgress.done()
      } else {
        if (store.getters.userInfo === null) { // 判断用户是否已经获取user_info信息
          store.dispatch("user/GetInfo").then(res => {
            
          })
          .catch(err => {
            store.dispatch('user/LogOut').then(() => {
              Message.error(err)
              next({ path: '/' })
            })
          })
          next()
        } else {
          next()
        }
        NProgress.done()
      }
    } else {
      // 没有token
      if (whiteList.indexOf(to.path) !== -1) {
        // 在免登录白名单，直接进入
        next()
        NProgress.done()
      } else {
        next(`/login?redirect=${to.fullPath}`) // 否则全部重定向到登录页
        NProgress.done()
      }
    }
  })