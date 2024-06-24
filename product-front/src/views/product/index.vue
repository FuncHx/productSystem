<template>
  <avue-crud ref="crud" 
  :option="option" 
  :data="data"
  :page.sync="page"
  :search.sync="search"
  :table-loading="tableLoading"
  @on-load="getPage"
  @refresh-change="refreshChange"
  @search-change="searchChange"
  @selection-change="selectionChange"
  @row-save="addProduct"
  >
  
  
  </avue-crud>
</template>

<script>
import { tableOption } from '@/const/crud/product';
import { getProduct } from '@/api/product';
export default {
  data() {
    return {
      option: tableOption,
      selectionData: [],
      data: [],
      tableLoading: false,
      page:{ 
          total: 0, 
          currentPage: 1, 
          pageSize: 10
      },
      search: {
        product_name: "",
        category: "",
        suppliers_id: null
      },
    }
  },
  created() {
    this.getPage(this.page, this.search)
  },
  methods: {
    getPage(page, params) {
      this.tableLoading = true
      getProduct(page, params).then(resp => {
        this.data = resp.results
        this.tableLoading = false
        this.page.total = resp.count
      }).catch(error => {
        this.tableLoading = false
        this.$message.error(error)
      })
    },
    searchChange(params, done) {
      this.search = params
      this.page.currentPage = 1
      this.getPage(this.page, this.search)
      done()
    },
    selectionChange(list) {
      this.selectionData = list
    },
    refreshChange(page) {
      this.getPage(this.page, this.search)
    },
    addProduct(row,done,loading) {
      console.log(row);
      loading = false
      done();
    }
  }
}
</script>

<style>

</style>