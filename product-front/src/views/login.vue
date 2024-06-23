<template>
  <div class="login">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form">
        <h3 class="title">商品管理系统</h3>
        <el-form-item prop="username">
          <el-input v-model="loginForm.username" type="text" prefix-icon="el-icon-user" auto-complete="off" placeholder="账号">
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input
            v-model="loginForm.password"
            type="password"
            auto-complete="off"
            placeholder="密码"
            prefix-icon="el-icon-lock"
            show-password
            @keyup.enter.native="handleLogin"
          >
          </el-input>
        </el-form-item>
        <el-checkbox v-model="loginForm.rememberMe" style="margin:0px 0px 25px 0px;">记住密码</el-checkbox>
        <el-form-item style="width:100%;">
          <el-button
            :loading="loading"
            size="medium"
            type="primary"
            style="width:100%;"
            @click.native.prevent="handleLogin"
          >
            <span v-if="!loading">登 录</span>
            <span v-else>登 录 中...</span>
          </el-button>
        </el-form-item>
      </el-form>
  </div>
</template>

<script>
import Cookies from 'js-cookie';
import { encrypt, decrypt } from '@/utils/jsencrypt'
export default {
    name: "Login",
    data (){
        return {
            codeUrl: "",
            cookiePassword: "",
            loginForm: {
                username: "",
                password: "",
                rememberMe: false,
            },
            loginRules: {
                username: [{ required: true, trigger: "blur", message: "用户名不能为空" }],
                password: [{ required: true, trigger: "blur", message: "密码不能为空" }],
            },
            loading: false,
            redirect: undefined
        }
    },
    watch: {
        $route: {
            handler: function(route) {
                this.redirect = route.query && route.query.redirect
            },
            immediate: true
        }
    },
    created() {
      this.getCookie();
    },
    methods: {
        getCookie() {   // 自动填充保存的用户名及密码
            const username = Cookies.get("username");
            const password = Cookies.get("password");
            const rememberMe = Cookies.get('rememberMe')
            this.loginForm = {
            username: username === undefined ? this.loginForm.username : username,
            password: password === undefined ? this.loginForm.password : decrypt(password),
            rememberMe: rememberMe === undefined ? false : Boolean(rememberMe)
            };
        },
        handleLogin() {
            this.$refs.loginForm.validate(valid => {
            if (valid) {
                this.loading = true;
                if (this.loginForm.rememberMe) {
                    Cookies.set("username", this.loginForm.username, { expires: 30 });
                    Cookies.set("password", encrypt(this.loginForm.password), { expires: 30 });
                    Cookies.set('rememberMe', this.loginForm.rememberMe, { expires: 30 });
                } else {
                    Cookies.remove("username");
                    Cookies.remove("password");
                    Cookies.remove('rememberMe');
                }
                this.$store.dispatch("user/Login", this.loginForm).then(() => {
                    this.loading = false;
                    this.$router.push({ path: this.redirect || "/" }).catch(()=>{});
                }).catch(() => {
                    this.loading = false;
                });
            }
            });
        }
    }
}
</script>

<style lang="less">
    .login {
        display: flex;
        justify-content: center;
        align-items: center;
        background: url("../assets/images/login-bg.png");
        background-repeat: no-repeat;
        background-size: cover;
        background-color: #bfbfbf;
        height: 100%;
    }
    .title {
        margin: 0px auto 30px auto;
        text-align: center;
        color: #707070;
    }
    
    .login-form {
        border-radius: 6px;
        background: #ffffff;
        width: 400px;
        padding: 25px 25px 5px 25px;
        .el-input {
            height: 38px;
            input {
                height: 38px;
            }
        }
        .input-icon {
            height: 39px;
            width: 14px;
            margin-left: 2px;
        }
    }
    .login-tip {
        font-size: 13px;
        text-align: center;
        color: #bfbfbf;
    }
    .el-login-footer {
        height: 40px;
        line-height: 40px;
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #fff;
        font-family: Arial;
        font-size: 12px;
        letter-spacing: 1px;
    }
</style>