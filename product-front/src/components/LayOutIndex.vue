<template>
  <el-container class="operation-wrapper">
  <el-aside width="auto"><Aside :routes="routers"/></el-aside>
  <el-container>
    <el-header><NavBar/></el-header>
    <el-main><router-view></router-view></el-main>
  </el-container>
</el-container>
</template>


<script>
import { indexChildren } from '@/router';

import NavBar from "./Navbar"
import Aside from './SideBar';

export default {
    name: "LayoutIndex",
    components: {
      NavBar,
      Aside
    },
    data() {
        return {
            routers: indexChildren
        }
    },

    computed: {
    },
}
</script>


<style lang="less">
  .el-header {
    text-align: center;
    padding: 0 !important;
    height: 50px !important;
    line-height: 50px;
  }

  .operation-wrapper {
    width: 100% !important;
    .el-header {
      box-shadow: 2px 2px 5px 1px rgba(0, 0, 0, 0.3);
      padding: 0;
    }
    .el-aside {
      height: 100vh;
      overflow-y: auto;
      box-shadow: 2px 2px 10px 2px rgba(0, 0, 0, 0.3);
    }
    .el-main {
      padding: 0px 16px !important;
      height: calc(100vh - 200px); 
      overflow-y: auto;
      >div {
        padding: 20px;
      }
    }
  }
  
  .el-aside {
    position: relative;
    height: 100vh;
    .el-menu {
    // 解决侧边栏凸出来的一小块儿白边
        border-right: none;
    }
  }
  .el-aside::-webkit-scrollbar {
    display: none;
    overflow-y: hidden;
  }
  
</style>