import { getToken, setToken, removeToken } from '@/utils/auth'
import { login, logout, getUserInfo} from '@/api/login'
import router from '@/router'
import { editAvatar } from '@/api/user'
import { Message } from 'element-ui'

const user = {
    state: {
        userInfo: null,
        status: '',
        token: getToken(),
        name: '',
        avatar: '',
        introduction: '',
        setting: {},
    },
    mutations: {
        SET_USER_INFO(state, userInfo) {
            state.userInfo = userInfo
        },
        SET_AVATAR(state, avatar) {
            state.avatar = avatar
        },
        SET_NAME(state, name) {
            state.name = name
        },
        SET_TOKEN: (state, token) => {
            state.token = token
        },
    },
    actions: {
        // 登录
        Login({commit}, userInfo) {
            const username = userInfo.username.trim()
            const password = userInfo.password
            return new Promise((resolve, reject) => {
                login({username, password}).then(response => {
                    if (response.code != 200) {
                        Message.error(response.message)
                        resolve()
                    }else  {
                        setToken(response.access)
                        commit('SET_TOKEN', response.access)
                        resolve()
                    }
                }).catch(error => {
                    reject(error)
                })
            })
        },
        GetInfo({commit, state}) {
            return new Promise((resolve, reject) => {
                getUserInfo().then(resp => {
                    console.log(resp);
                    commit('SET_NAME', resp.data.nick_name)
                    if (resp.data.avatar) {
                        commit('SET_AVATAR', resp.data.avatar)
                    }else {
                        commit('SET_AVATAR', require('@/assets/images/avatar.jpg'))
                    }
                    commit('SET_USER_INFO', resp.data)
                    resolve(resp)
                })
            })
        },
        // 登出
        LogOut({commit, state}) {
            logout().then(resp =>{
                commit('SET_USER_INFO', null)
                commit('SET_NAME', '')
                commit('SET_AVATAR', '')
                removeToken()
                router.push({path: "/login"})
            })
        },
        editAvatar({commit}, avatar) {
            return new Promise((resolve, reject) => {
                editAvatar(avatar).then(resp => {
                    commit('SET_AVATAR', avatar)
                    resolve(resp)
                }).catch(error => {
                    reject(error)
                })
            })
        }
    },
    namespaced: true,
}

export default user