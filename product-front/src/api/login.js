import request from '@/utils/request'

// 登录
export function login(data) {
  return request({
    url: '/login/',
    method: 'post',
    data
})}

// 获取用户信息
export function getUserInfo() {
    return request({
      url: '/adminUser/userInfo',
      method: 'get',
    })
}

// 退出登录
export function logout() {
    return request({
        url: '/logout/',
        method: 'get',
    })
}