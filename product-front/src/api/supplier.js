import request from '@/utils/request'

export function getSupplier() {
    return request({
        url: "/supplier/",
        method: 'get'
    })
}