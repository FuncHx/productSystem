import { baseUrl } from "@/utils/config"
import { getToken } from "@/utils/auth"
export const tableOption = {
    dialogDrag:true,
    border: true,
    index: false,
    indexLabel: '序号',
    stripe: true,
    selection: true,
    menuAlign: 'center',
    align: 'center',
    editBtn: true,
    delBtn: true,
    addBtn: true,
    viewBtn: true,
    searchShow: false,
    menuWidth: 150,
    labelWidth: 120,
    menuType:'text',
    searchMenuSpan: 6,
    column: [
        {
            label: "ID",
            prop: "id", 
            width: 50,
            editDisabled: true,
            addDisplay: false
        },
        {
            label: '商品图片',
            prop: 'product_img',
            type: 'upload',
            propsHttp: {
                url: 'file',
                res: "data"
            },
            headers: {
                Authorization: 'Bearer ' + getToken()
            },
            limit: 5,
            span: 24,
            multiple: true,
            listType: 'picture-card',
            tip: '只能上传jpg/png文件，且不超过500kb',
            action: baseUrl + '/uploadFile/'
        }, 
        {
            label: "名称",
            prop: "product_name", 
            search: true,
            rules: [{
                required: true,
                message: "请输入名称",
                trigger: "blur"
              }]
        },
        {
            label: "类型",
            prop: "category", 
            search: true,
            rules: [{
                required: true,
                message: "请输入类型",
                trigger: "blur"
              }]
        },
        {
            label: "价格",
            prop: "price", 
            formatter: (row) => {
                return "￥" + row.price
            },
            type:'number',
            rules: [{
                required: true,
                message: "请输入价格",
                trigger: "blur"
              }]
        },
        {
            label: "规格",
            prop: "spec", 
        },
        {
            label: "库存",
            prop: "inventory",
            formatter: (row) => {
                return row.inventory.stock_quantity
            },
            type:'number',
            rules: [{
                required: true,
                message: "请输入库存",
                trigger: "blur"
              }]
        },
        {
            label: "备注",
            prop: "comment", 
        },
        {
            label: "供应商",
            prop: "supplier_id", 
            search: true,
            formatter: (row) => {
                return row.supplier_id.supplier_name
            },
            rules: [{
                required: true,
                message: "请选择供应商",
                trigger: "blur"
            }],
            props: {
                label: 'supplier_name',
                value: 'id',
                res:'results'
            },
            type:'select',
            dicHeaders: {
                Authorization: 'Bearer ' + getToken()
            },
            dicMethod:'get',
            dicUrl: baseUrl + "/supplier/"
        },
    ]
}