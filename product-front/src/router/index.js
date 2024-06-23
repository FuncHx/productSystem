import Vue from 'vue'
import Router from 'vue-router';
import LayoutIndex from "@/components/LayOutIndex.vue"

Vue.use(Router)


export const indexChildren = [
  {
    path: 'index',
    name: 'index',
    meta: {title: '首页', icon: 'shouye1', noCache: true,},
    component: (resolve) => require(['@/views/index'], resolve),
  },
  {
    path: "product",
    name: "product",
    meta: {title: '商品', icon: 'shangpin', noCache: true,},
    component: (resolve) => require(['@/views/product'], resolve),
  },
  {
    path: "order",
    name: "order",
    meta: {title: '订单', icon: 'dingdan', noCache: true,},
    component: (resolve) => require(['@/views/order'], resolve),
  },
  {
    path: "user",
    name: "user",
    meta: {title: '用户', icon: 'haoyourenzheng', noCache: true,},
    component: (resolve) => require(['@/views/user'], resolve),
  }
]

export const constantRoutes = [
  {
    path: '',
    component: LayoutIndex,
    redirect: 'index',
    name: "首页",
    meta: {title: '首页', icon: 'shouye', noCache: true,},
    children: indexChildren
  },
  {
    path: '',
    component: LayoutIndex,
    redirect: 'userInfo',
    name: "用户信息",
    meta: {title: '用户信息', icon: 'shouye', noCache: true,},
    children: [
      {
        path: "userInfo",
        name: "userInfo",
        component: (resolve) => require(["@/views/userInfo"], resolve)
      }
    ]
  },
  {
    name: "login",
    path: "/login",
    meta: {
      title: '登录',
      message: null,
      status: true
    },
    component: (resolve) => require(['@/views/login.vue'], resolve),
  },
]


export default new Router({
  routes: constantRoutes
})